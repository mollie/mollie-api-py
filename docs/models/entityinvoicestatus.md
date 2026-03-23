# EntityInvoiceStatus

Status of the invoice.

## Example Usage

```python
from mollie.models import EntityInvoiceStatus

value = EntityInvoiceStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `OPEN`    | open      |
| `PAID`    | paid      |
| `OVERDUE` | overdue   |