<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import mollie
from mollie import ClientSDK


with ClientSDK() as client_sdk:

    res = client_sdk.oauth.generate(security=mollie.OauthGenerateTokensSecurity(
        username="",
        password="",
    ), idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
        "grant_type": mollie.OauthGrantType.AUTHORIZATION_CODE,
        "code": "auth_...",
        "refresh_token": "refresh_...",
        "redirect_uri": "https://example.com/redirect",
    })

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import mollie
from mollie import ClientSDK

async def main():

    async with ClientSDK() as client_sdk:

        res = await client_sdk.oauth.generate_async(security=mollie.OauthGenerateTokensSecurity(
            username="",
            password="",
        ), idempotency_key="123e4567-e89b-12d3-a456-426", request_body={
            "grant_type": mollie.OauthGrantType.AUTHORIZATION_CODE,
            "code": "auth_...",
            "refresh_token": "refresh_...",
            "redirect_uri": "https://example.com/redirect",
        })

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->