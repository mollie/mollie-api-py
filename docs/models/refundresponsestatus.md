# RefundResponseStatus

## Example Usage

```python
from mollie.models import RefundResponseStatus

value = RefundResponseStatus.QUEUED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `QUEUED`     | queued       |
| `PENDING`    | pending      |
| `PROCESSING` | processing   |
| `REFUNDED`   | refunded     |
| `FAILED`     | failed       |
| `CANCELED`   | canceled     |