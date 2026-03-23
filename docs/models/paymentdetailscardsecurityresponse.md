# PaymentDetailsCardSecurityResponse

The level of security applied during card processing.

## Example Usage

```python
from mollie.models import PaymentDetailsCardSecurityResponse

value = PaymentDetailsCardSecurityResponse.NORMAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `NORMAL`       | normal         |
| `THREEDSECURE` | 3dsecure       |