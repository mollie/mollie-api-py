# SalesInvoiceEInvoiceStatus

The e-invoice submission status for the invoice, if it was configured to be an e-invoice.

## Example Usage

```python
from mollie.models import SalesInvoiceEInvoiceStatus

value = SalesInvoiceEInvoiceStatus.ISSUING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ISSUING` | issuing   |
| `ISSUED`  | issued    |
| `FAILED`  | failed    |