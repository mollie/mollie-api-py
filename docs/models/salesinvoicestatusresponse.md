# SalesInvoiceStatusResponse

The current status of the invoice.

## Example Usage

```python
from mollie.models import SalesInvoiceStatusResponse

value = SalesInvoiceStatusResponse.DRAFT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `DRAFT`            | draft              |
| `ISSUING`          | issuing            |
| `ISSUED`           | issued             |
| `PENDING_PAYMENT`  | pending-payment    |
| `PAID`             | paid               |
| `OVERDUE`          | overdue            |
| `PAYMENT_REVERSED` | payment_reversed   |
| `CANCELLED`        | cancelled          |
| `EXPIRED`          | expired            |
| `FAILED`           | failed             |