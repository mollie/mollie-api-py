# DraftTransferStatusReasonCodeResponse

A machine-readable code that indicates the reason for the draft transfer's current status.

## Example Usage

```python
from mollie.models import DraftTransferStatusReasonCodeResponse

value = DraftTransferStatusReasonCodeResponse.DELETED_BY_CREATOR

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `DELETED_BY_CREATOR`    | deleted-by-creator      |
| `DECLINED_BY_INITIATOR` | declined-by-initiator   |
| `ACCOUNT_CLOSED`        | account-closed          |