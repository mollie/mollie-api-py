# AccountStatus

The status of the business account.

## Example Usage

```python
from mollie.models import AccountStatus

value = AccountStatus.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ACTIVE`  | active    |
| `BLOCKED` | blocked   |
| `CLOSED`  | closed    |