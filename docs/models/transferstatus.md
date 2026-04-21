# TransferStatus

The status of the transfer.

## Example Usage

```python
from mollie.models import TransferStatus

value = TransferStatus.REQUESTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `REQUESTED`      | requested        |
| `INITIATED`      | initiated        |
| `PENDING_REVIEW` | pending-review   |
| `PROCESSED`      | processed        |
| `FAILED`         | failed           |
| `BLOCKED`        | blocked          |
| `RETURNED`       | returned         |