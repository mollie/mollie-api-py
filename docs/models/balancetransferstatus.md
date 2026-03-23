# BalanceTransferStatus

The status of the transfer.

## Example Usage

```python
from mollie.models import BalanceTransferStatus

value = BalanceTransferStatus.CREATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `CREATED`   | created     |
| `FAILED`    | failed      |
| `SUCCEEDED` | succeeded   |