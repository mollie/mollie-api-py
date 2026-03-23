# SalesInvoiceVatSchemeResponse

The VAT scheme to create the invoice for. You must be enrolled with One Stop Shop enabled to use it.

## Example Usage

```python
from mollie.models import SalesInvoiceVatSchemeResponse

value = SalesInvoiceVatSchemeResponse.STANDARD

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `STANDARD`      | standard        |
| `ONE_STOP_SHOP` | one-stop-shop   |