# ReportTypeResponse

The type of report to generate. Determines which other fields the request needs, and which fields show up
on the resulting report.

## Example Usage

```python
from mollie.models import ReportTypeResponse

value = ReportTypeResponse.TRANSACTION_MARGIN

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `TRANSACTION_MARGIN` | transaction_margin   |