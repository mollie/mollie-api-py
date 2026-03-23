import uuid
import sys
import os
import json

from httpx import Request
from typing import Union

from .types import (
    BeforeRequestHook,
    BeforeRequestContext,
)

def generate_idempotency_key() -> str:
    """
    Generates a UUID4 to be used as an idempotency key.
    @see https://docs.mollie.com/reference/api-idempotency#using-an-idempotency-key

    :return: A string representation of a UUID4.
    """
    return str(uuid.uuid4())


class MollieHooks(BeforeRequestHook):
    def __init__(self):
        super().__init__()
        self.global_usage = self.set_global_usage()

    def set_global_usage(self) -> dict:
        routes_path = os.path.join(os.path.dirname(__file__), "global_usage.json")
        with open(routes_path, "r", encoding="utf-8") as f:
            return json.load(f)        

    def before_request(self, hook_ctx: BeforeRequestContext, request: Request) -> Union[Request, Exception]:
        """
        Modify the request before sending.

        :param hook_ctx: Context for the hook, containing request metadata.
        :param request: The HTTP request to modify.
        :return: The modified request or an exception.
        """
        # Validate path parameters
        self._validate_path_parameters(request)
        
        # Create a copy of the headers
        headers = dict(request.headers or {})

        # Add the idempotency key if it doesn't already exist
        headers = self._handle_idempotency_key(headers)

        # Customize the User Agent header
        headers = self._customize_user_agent(headers, hook_ctx)

        # Update request with new headers first
        request = Request(
            method=request.method,
            url=request.url,
            headers=headers,
            content=request.content,
            extensions=request.extensions
        )

        if self._can_inject_global_fields(hook_ctx):
            request = self._inject_global_fields(request, hook_ctx)

        return request

    def _validate_path_parameters(self, request: Request) -> None:
        path = request.url.path
        path_segments = path.split('/')
        
        for i, segment in enumerate(path_segments):
            if i == 0 and segment == '':
                continue
            
            if segment == '' or segment.strip() == '':
                raise ValueError(
                    f"Invalid request: empty path parameter detected in [{request.method}] '{path}'"
                )
            
    def _get_security_from_context(self, hook_ctx: BeforeRequestContext) -> Union[None, object]:
        security = hook_ctx.config.security

        if callable(security):
            return security()

        return security

    def _can_inject_global_fields(self, hook_ctx: BeforeRequestContext) -> bool:
        if not self.global_usage:
            return False
        
        security = self._get_security_from_context(hook_ctx)

        if security is None:
            return False
        
        return hook_ctx.config.can_have_global_fields()  # type: ignore[attr-defined]

    def _inject_global_fields(self, request: Request, hook_ctx: BeforeRequestContext) -> Request:
        """
        Check if the current request's operation ID is listed under any of the global fields in the global_usage mapping.
        If it is, inject the corresponding global field in the body (if not already present) and return the modified request.
        """
        operation_id = hook_ctx.operation_id
        globals_dict = hook_ctx.config.globals.model_dump(by_alias=True, exclude_none=True)

        fields_to_inject = {
            field: globals_dict[field]
            for field, operations in self.global_usage.items()
            if operation_id in operations and field in globals_dict
        }

        if not fields_to_inject:
            return request

        if request.content:
            try:
                body = json.loads(request.content)
            except (json.JSONDecodeError, TypeError):
                return request
        else:
            body = {}

        for field, value in fields_to_inject.items():
            if field not in body:
                body[field] = value

        new_content = json.dumps(body).encode("utf-8")
        new_headers = dict(request.headers)
        new_headers["content-length"] = str(len(new_content))

        return Request(
            method=request.method,
            url=request.url,
            headers=new_headers,
            content=new_content,
            extensions=request.extensions,
        )

    def _is_oauth_request(self, headers: dict, hook_ctx: BeforeRequestContext) -> bool:
        security = hook_ctx.config.security

        if callable(security):
            security = security()

        if security is None:
            return False

        o_auth = getattr(security, 'o_auth', None)
        if o_auth is None:
            return False

        return headers.get("authorization", None) == f"Bearer {o_auth}"

    def _handle_idempotency_key(self, headers: dict) -> dict:
        idempotency_key = "idempotency-key"
        if idempotency_key not in headers or not headers[idempotency_key]:
            headers[idempotency_key] = generate_idempotency_key()
        return headers
    
    def _customize_user_agent(self, headers: dict, hook_ctx: BeforeRequestContext) -> dict:
        user_agent_key = "user-agent"

        gen_version = hook_ctx.config.gen_version
        sdk_version = hook_ctx.config.sdk_version
        python_version = sys.version.split(" ", maxsplit=1)[0]
        package_name = "mollie-api-py"

        new_user_agent = f"Speakeasy/{gen_version} Python/{python_version} {package_name}/{sdk_version}"
        if hook_ctx.config.globals.custom_user_agent:
            new_user_agent = f"{new_user_agent} {hook_ctx.config.globals.custom_user_agent}"

        headers[user_agent_key] = new_user_agent

        return headers
