# SettlementMode

Whether this entity was created in live mode or in test mode. Settlements are always in live mode.

## Example Usage

```python
from mollie.models import SettlementMode

value = SettlementMode.LIVE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name   | Value  |
| ------ | ------ |
| `LIVE` | live   |