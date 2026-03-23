# MethodStatus

The payment method's activation status for this profile.

## Example Usage

```python
from mollie.models import MethodStatus

value = MethodStatus.ACTIVATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `ACTIVATED`        | activated          |
| `PENDING_BOARDING` | pending-boarding   |
| `PENDING_REVIEW`   | pending-review     |
| `PENDING_EXTERNAL` | pending-external   |
| `REJECTED`         | rejected           |