# ListEntitySettlementStatus

The status of the settlement.

## Example Usage

```python
from mollie.models import ListEntitySettlementStatus

value = ListEntitySettlementStatus.OPEN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `OPEN`    | open      |
| `PENDING` | pending   |
| `PAIDOUT` | paidout   |
| `FAILED`  | failed    |