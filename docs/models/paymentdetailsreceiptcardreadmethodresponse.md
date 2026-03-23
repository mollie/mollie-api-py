# PaymentDetailsReceiptCardReadMethodResponse

The method by which the card was read by the terminal.

## Example Usage

```python
from mollie.models import PaymentDetailsReceiptCardReadMethodResponse

value = PaymentDetailsReceiptCardReadMethodResponse.CHIP

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `CHIP`                     | chip                       |
| `MAGNETIC_STRIPE`          | magnetic-stripe            |
| `NEAR_FIELD_COMMUNICATION` | near-field-communication   |
| `CONTACTLESS`              | contactless                |
| `MOTO`                     | moto                       |