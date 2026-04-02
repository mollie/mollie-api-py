# CreditDebitIndicator

Indicates whether the entry is a credit or debit from the perspective of the account holder.

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