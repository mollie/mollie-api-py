# BalanceTransferDestinationType

The default destination of automatic scheduled transfers. Currently only `bank-account` is supported.

* `bank-account` — Transfer the balance amount to an external bank account

## Example Usage

```python
from mollie.models import BalanceTransferDestinationType

value = BalanceTransferDestinationType.BANK_ACCOUNT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name           | Value          |
| -------------- | -------------- |
| `BANK_ACCOUNT` | bank-account   |