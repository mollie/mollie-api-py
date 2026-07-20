# DraftTransferResponseSource

Whether the draft transfer was created via this API, or created in Mollie Apps.

## Example Usage

```python
from mollie.models import DraftTransferResponseSource

value = DraftTransferResponseSource.API

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `API`        | api          |
| `MOLLIE_APP` | mollie-app   |