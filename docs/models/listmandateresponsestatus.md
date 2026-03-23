# ListMandateResponseStatus

The status of the mandate. A status can be `pending` for mandates when the first payment is not yet finalized, or
when we did not received the IBAN yet from the first payment.

## Example Usage

```python
from mollie.models import ListMandateResponseStatus

value = ListMandateResponseStatus.VALID

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `VALID`   | valid     |
| `PENDING` | pending   |
| `INVALID` | invalid   |