import hmac
import hashlib
from typing import List, Optional, Union


class InvalidSignatureException(Exception):
    pass


class SignatureValidator:
    """Validates Mollie webhook signatures using HMAC-SHA256."""

    SIGNATURE_HEADER = "X-Mollie-Signature"
    _SIGNATURE_PREFIX = "sha256="

    def __init__(self, signing_secrets: Union[str, List[str]]):
        """
        Create a new SignatureValidator instance.

        :param signing_secrets: One or more signing secrets (supports multiple for migration periods).
        """
        if isinstance(signing_secrets, str):
            self._signing_secrets = [signing_secrets]
        else:
            self._signing_secrets = list(signing_secrets)

    @classmethod
    def validate(
        cls,
        payload: str,
        signing_secrets: Union[str, List[str]],
        signatures: Optional[Union[str, List[str]]] = None,
    ) -> bool:
        """
        Static method for simpler usage.

        :param payload: Raw request body as a string.
        :param signing_secrets: One or more signing secrets.
        :param signatures: One or more signatures to validate against.
        :return: True if a valid signature is found, False if legacy webhook (no signature).
        :raises InvalidSignatureException: If all signatures are invalid.
        """
        return cls(signing_secrets).validate_payload(payload, signatures)

    def validate_payload(
        self, payload: str, signatures: Union[str, List[str], None]
    ) -> bool:
        """
        Verify a raw webhook payload with provided signature(s).

        :param payload: Raw request body as a string.
        :param signatures: One or more signatures to validate against.
        :return: True if any signature is valid, False if no signatures provided (legacy webhook).
        :raises InvalidSignatureException: If all signatures are invalid.
        """
        if isinstance(signatures, str):
            signatures = [signatures] if signatures else []
        elif signatures is None:
            signatures = []

        signatures = [s for s in signatures if s]

        if not signatures:
            return False

        return self._validate_signatures(payload, signatures)

    def _validate_signatures(self, payload: str, signatures: List[str]) -> bool:
        valid_signature_found = any(
            self._is_valid_signature(self._extract_signature(sig), payload)
            for sig in signatures
        )

        if not valid_signature_found:
            raise InvalidSignatureException("Invalid webhook signature")

        return valid_signature_found

    def _extract_signature(self, signature_header: str) -> str:
        if signature_header.startswith(self._SIGNATURE_PREFIX):
            return signature_header[len(self._SIGNATURE_PREFIX):]
        return signature_header

    def _is_valid_signature(self, provided_signature: str, payload: str) -> bool:
        return any(
            hmac.compare_digest(
                self.create_signature(payload, secret),
                provided_signature,
            )
            for secret in self._signing_secrets
        )

    @staticmethod
    def create_signature(payload: str, secret: str) -> str:
        """Create an HMAC-SHA256 signature for a given payload and secret."""
        return hmac.new(
            secret.encode("utf-8"),
            payload.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
