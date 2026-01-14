import uuid
import sys
import json

from httpx import Request
from typing import Union
from urllib.parse import parse_qs, urlencode, urlparse, urlunparse

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

        # Then populate profile ID and testmode if OAuth (this may update headers again)
        if self._is_oauth_request(headers, hook_ctx):
            request = self._populate_profile_id_and_testmode(request, hook_ctx)

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
    
    def _populate_profile_id_and_testmode(self, request: Request, hook_ctx: BeforeRequestContext) -> Request:        
        client_profile_id = hook_ctx.config.globals.profile_id
        client_testmode = hook_ctx.config.globals.testmode

        # Get the HTTP method
        method = request.method
        
        if method == "GET":
            # Update the query parameters. If testmode or profileId are not present, add them.
            parsed_url = urlparse(str(request.url))
            query_params = parse_qs(parsed_url.query, keep_blank_values=True)
            
            # Add profileId if not already present
            if client_profile_id is not None and 'profileId' not in query_params:
                query_params['profileId'] = [client_profile_id]
            
            # Add testmode if not already present
            if client_testmode is not None and 'testmode' not in query_params:
                query_params['testmode'] = [str(client_testmode).lower()]
            
            # Rebuild the URL with updated query parameters
            new_query = urlencode(query_params, doseq=True)
            new_url = urlunparse((
                parsed_url.scheme,
                parsed_url.netloc,
                parsed_url.path,
                parsed_url.params,
                new_query,
                parsed_url.fragment
            ))
            
            return Request(
                method=request.method,
                url=new_url,
                headers=request.headers,
                content=request.content,
                extensions=request.extensions
            )

        # It's POST, DELETE, PATCH
        # Update the JSON body. If testmode or profileId are not present, add them.
        if request.content:
            try:
                body = json.loads(request.content)
            except (json.JSONDecodeError, TypeError):
                # If it's not JSON, return the request unchanged
                return request
        else:
            body = {}
        
        # Add profileId if not already present
        if client_profile_id is not None and 'profileId' not in body:
            body['profileId'] = client_profile_id
        
        # Add testmode if not already present
        if client_testmode is not None and 'testmode' not in body:
            body['testmode'] = client_testmode
        
        # Create a new request with updated body
        new_content = json.dumps(body).encode('utf-8')
        
        # Update headers with correct Content-Length
        new_headers = dict(request.headers)
        new_headers['content-length'] = str(len(new_content))
        
        return Request(
            method=request.method,
            url=request.url,
            headers=new_headers,
            content=new_content,
            extensions=request.extensions
        )
