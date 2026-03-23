# PaymentDetailsCardFundingResponse

The card type.

## Example Usage

```python
from mollie.models import PaymentDetailsCardFundingResponse

value = PaymentDetailsCardFundingResponse.DEBIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `DEBIT`          | debit            |
| `CREDIT`         | credit           |
| `PREPAID`        | prepaid          |
| `DEFERRED_DEBIT` | deferred-debit   |