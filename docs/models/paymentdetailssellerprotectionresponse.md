# PaymentDetailsSellerProtectionResponse

Indicates to what extent the payment is eligible for PayPal's Seller Protection. Only available for PayPal
payments, and if the information is made available by PayPal.

## Example Usage

```python
from mollie.models import PaymentDetailsSellerProtectionResponse

value = PaymentDetailsSellerProtectionResponse.ELIGIBLE_UPPER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                                    | Value                                   |
| --------------------------------------- | --------------------------------------- |
| `ELIGIBLE_UPPER`                        | ELIGIBLE                                |
| `PARTIALLY_ELIGIBLE_UPPER`              | PARTIALLY_ELIGIBLE                      |
| `NOT_ELIGIBLE`                          | NOT_ELIGIBLE                            |
| `ELIGIBLE_MIXED`                        | Eligible                                |
| `INELIGIBLE`                            | Ineligible                              |
| `PARTIALLY_ELIGIBLE_INR_ONLY`           | Partially Eligible - INR Only           |
| `PARTIALLY_ELIGIBLE_UNAUTH_ONLY`        | Partially Eligible - Unauth Only        |
| `PARTIALLY_ELIGIBLE_MIXED`              | Partially Eligible                      |
| `NONE`                                  | None                                    |
| `ACTIVE`                                | Active                                  |
| `FRAUD_CONTROL_UNAUTH_PREMIUM_ELIGIBLE` | Fraud Control - Unauth Premium Eligible |