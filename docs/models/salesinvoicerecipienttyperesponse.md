# SalesInvoiceRecipientTypeResponse

The type of recipient, either `consumer` or `business`. This will determine what further fields are
required on the `recipient` object.

## Example Usage

```python
from mollie.models import SalesInvoiceRecipientTypeResponse

value = SalesInvoiceRecipientTypeResponse.CONSUMER

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `CONSUMER` | consumer   |
| `BUSINESS` | business   |