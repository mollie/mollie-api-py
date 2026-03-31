# VerificationResultEnum

The result of the Verification of Payee check.

## Example Usage

```python
from mollie.models import VerificationResultEnum

value = VerificationResultEnum.MATCH

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `MATCH`         | match           |
| `NO_MATCH`      | no-match        |
| `CLOSE_MATCH`   | close-match     |
| `NOT_AVAILABLE` | not-available   |