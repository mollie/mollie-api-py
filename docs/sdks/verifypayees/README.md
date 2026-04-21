# VerifyPayees

## Overview

### Available Operations

* [create](#create) - Verify Payee

## create

> 🚧 Beta feature
>
> This feature is currently in beta testing, and the final specification may still change.

Perform a Verification of Payee (VoP) check. This allows you to verify the account holder name against the
records held by the receiving bank before initiating a transfer.

The verification result indicates whether the provided name matches, closely matches, or does not match the
name on file at the receiving bank. This helps prevent misdirected payments.

### Simulating verification scenarios in test mode

In test mode, you can simulate various verification outcomes by adjusting the creditor name in the
`creditorBankAccount.accountHolderName` property. This allows you to test all possible Verification of Payee
results without needing special properties. The names are case insensitive.

| Account holder name                    | Scenario                                      | Verification result | Suggested name |
|----------------------------------------|-----------------------------------------------|---------------------|----------------|
| `John Close Match`                     | Name closely matches the bank records          | `close-match`       | `John Match`   |
| `John No Match`                        | Name does not match the bank records           | `no-match`          | —              |
| `John Unavailable`                     | Verification is not available                  | `not-available`     | —              |
| Any other name                         | Default: name matches the bank records         | `match`             | —              |

### Example Usage: verify-payee-200-close-match

<!-- UsageSnippet language="python" operationID="verify-payee" method="post" path="/v2/business-accounts/payee-verifications" example="verify-payee-200-close-match" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.verify_payees.create(idempotency_key="123e4567-e89b-12d3-a456-426", verification_of_payee_request={
        "creditor_bank_account": {
            "account_holder_name": "Jan Jansen",
            "format_": mollie.AccountNumberFormat.IBAN,
            "account_number": "NL02ABNA0123456789",
        },
        "testmode": False,
    })

    # Handle response
    print(res)

```
### Example Usage: verify-payee-200-match

<!-- UsageSnippet language="python" operationID="verify-payee" method="post" path="/v2/business-accounts/payee-verifications" example="verify-payee-200-match" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.verify_payees.create(idempotency_key="123e4567-e89b-12d3-a456-426", verification_of_payee_request={
        "creditor_bank_account": {
            "account_holder_name": "Jan Jansen",
            "format_": mollie.AccountNumberFormat.IBAN,
            "account_number": "NL02ABNA0123456789",
        },
        "testmode": False,
    })

    # Handle response
    print(res)

```
### Example Usage: verify-payee-200-no-match

<!-- UsageSnippet language="python" operationID="verify-payee" method="post" path="/v2/business-accounts/payee-verifications" example="verify-payee-200-no-match" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.verify_payees.create(idempotency_key="123e4567-e89b-12d3-a456-426", verification_of_payee_request={
        "creditor_bank_account": {
            "account_holder_name": "Jan Jansen",
            "format_": mollie.AccountNumberFormat.IBAN,
            "account_number": "NL02ABNA0123456789",
        },
        "testmode": False,
    })

    # Handle response
    print(res)

```
### Example Usage: verify-payee-200-not-available

<!-- UsageSnippet language="python" operationID="verify-payee" method="post" path="/v2/business-accounts/payee-verifications" example="verify-payee-200-not-available" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        organization_access_token=os.getenv("CLIENT_ORGANIZATION_ACCESS_TOKEN", ""),
    ),
) as client_sdk:

    res = client_sdk.verify_payees.create(idempotency_key="123e4567-e89b-12d3-a456-426", verification_of_payee_request={
        "creditor_bank_account": {
            "account_holder_name": "Jan Jansen",
            "format_": mollie.AccountNumberFormat.IBAN,
            "account_number": "NL02ABNA0123456789",
        },
        "testmode": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                 | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `idempotency_key`                                                                         | *Optional[str]*                                                                           | :heavy_minus_sign:                                                                        | A unique key to ensure idempotent requests. This key should be a UUID v4 string.          | 123e4567-e89b-12d3-a456-426                                                               |
| `verification_of_payee_request`                                                           | [Optional[models.VerificationOfPayeeRequest]](../../models/verificationofpayeerequest.md) | :heavy_minus_sign:                                                                        | N/A                                                                                       |                                                                                           |
| `retries`                                                                                 | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                          | :heavy_minus_sign:                                                                        | Configuration to override the default retry behavior of the client.                       |                                                                                           |

### Response

**[models.VerificationOfPayeeResponse](../../models/verificationofpayeeresponse.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 422, 429             | application/hal+json |
| models.ErrorResponse | 503                  | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |