# TransactionType

Indicates what kind of transaction this is.

We may introduce new transaction types as we expand the product. We recommend building your integration
to handle unexpected values gracefully, so nothing breaks when that happens. 

## Example Usage

```python
from mollie.models import TransactionType

value = TransactionType.CARD_PAYMENT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `CARD_PAYMENT`        | card-payment          |
| `BANK_TRANSFER`       | bank-transfer         |
| `PSP_TRANSFER`        | psp-transfer          |
| `INTERNAL_TRANSFER`   | internal-transfer     |
| `IDEAL_PAYMENT`       | ideal-payment         |
| `FEE`                 | fee                   |
| `CORRECTION`          | correction            |
| `DIRECT_DEBIT`        | direct-debit          |
| `DIRECT_DEBIT_REFUND` | direct-debit-refund   |