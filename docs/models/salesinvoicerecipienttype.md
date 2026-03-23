# SalesInvoiceRecipientType

The type of recipient, either `consumer` or `business`. This will determine what further fields are
required on the `recipient` object.

## Example Usage

```python
from mollie.models import SalesInvoiceRecipientType

value = SalesInvoiceRecipientType.CONSUMER
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `CONSUMER` | consumer   |
| `BUSINESS` | business   |