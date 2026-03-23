# SalesInvoicePaymentDetailsSource

The way through which the invoice is to be set to paid.

## Example Usage

```python
from mollie.models import SalesInvoicePaymentDetailsSource

value = SalesInvoicePaymentDetailsSource.MANUAL
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `MANUAL`       | manual         |
| `PAYMENT_LINK` | payment-link   |
| `PAYMENT`      | payment        |