# EntityPairingCodeStatus

The status of the pairing code.

## Example Usage

```python
from mollie.models import EntityPairingCodeStatus

value = EntityPairingCodeStatus.ACTIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `ACTIVE`  | active    |
| `EXPIRED` | expired   |
| `REVOKED` | revoked   |