# ReportStatusReasonCode

A machine-readable code for the failure reason.

## Example Usage

```python
from mollie.models import ReportStatusReasonCode

value = ReportStatusReasonCode.GENERATION_FAILED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `GENERATION_FAILED`        | generation-failed          |
| `EMPTY_REPORT`             | empty-report               |
| `REPORT_VALIDATION_FAILED` | report-validation-failed   |