# EntityReportStatus

The report's current status.

## Example Usage

```python
from mollie.models import EntityReportStatus

value = EntityReportStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `COMPLETED` | completed   |
| `FAILED`    | failed      |