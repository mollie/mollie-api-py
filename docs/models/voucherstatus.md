# VoucherStatus

The status of the issuer.
If the status is `pending-issuer`, an additional action from your side may be required with the issuer.

## Example Usage

```python
from mollie.models import VoucherStatus

value = VoucherStatus.ACTIVATED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name             | Value            |
| ---------------- | ---------------- |
| `ACTIVATED`      | activated        |
| `PENDING_ISSUER` | pending-issuer   |