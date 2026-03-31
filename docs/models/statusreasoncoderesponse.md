# StatusReasonCodeResponse

A machine-readable code indicating the reason for the transfer's terminal status.

## Example Usage

```python
from mollie.models import StatusReasonCodeResponse

value = StatusReasonCodeResponse.INSUFFICIENT_FUNDS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `INSUFFICIENT_FUNDS` | insufficient-funds   |
| `REJECTED`           | rejected             |
| `ERROR`              | error                |