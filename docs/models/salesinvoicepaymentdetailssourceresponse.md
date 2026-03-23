# SalesInvoicePaymentDetailsSourceResponse

The way through which the invoice is to be set to paid.

## Example Usage

```python
from mollie.models import SalesInvoicePaymentDetailsSourceResponse

value = SalesInvoicePaymentDetailsSourceResponse.MANUAL

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `MANUAL`       | manual         |
| `PAYMENT_LINK` | payment-link   |
| `PAYMENT`      | payment        |