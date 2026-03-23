<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    testmode=True,
    security=mollie.Security(
        o_auth=os.getenv("CLIENT_O_AUTH", ""),
    ),
) as client_sdk:

    res = client_sdk.balances.list(currency="EUR", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

    while res is not None:
        # Handle items

        res = res.next()
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
import asyncio
import mollie
from mollie import ClientSDK
import os

async def main():

    async with ClientSDK(
        testmode=True,
        security=mollie.Security(
            o_auth=os.getenv("CLIENT_O_AUTH", ""),
        ),
    ) as client_sdk:

        res = await client_sdk.balances.list_async(currency="EUR", limit=50, idempotency_key="123e4567-e89b-12d3-a456-426")

        while res is not None:
            # Handle items

            res = res.next()

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->