# CreditDebitIndicator

Indicates whether the transfer is a credit or debit transaction from the perspective of the account holder.

## Example Usage

```python
from mollie.models import CreditDebitIndicator

value = CreditDebitIndicator.CREDIT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name     | Value    |
| -------- | -------- |
| `CREDIT` | credit   |
| `DEBIT`  | debit    |