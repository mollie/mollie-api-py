# CaptureResponseStatus

The capture's status.

## Example Usage

```python
from mollie.models import CaptureResponseStatus

value = CaptureResponseStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `SUCCEEDED` | succeeded   |
| `FAILED`    | failed      |