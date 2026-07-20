# ListDraftTransferResponseStatus

The status of the draft transfer.

## Example Usage

```python
from mollie.models import ListDraftTransferResponseStatus

value = ListDraftTransferResponseStatus.AWAITING_INITIATION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                  | Value                 |
| --------------------- | --------------------- |
| `AWAITING_INITIATION` | awaiting-initiation   |
| `INITIATED`           | initiated             |
| `DECLINED`            | declined              |