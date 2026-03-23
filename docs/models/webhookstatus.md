# WebhookStatus

The subscription's current status.

## Example Usage

```python
from mollie.models import WebhookStatus

value = WebhookStatus.ENABLED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name       | Value      |
| ---------- | ---------- |
| `ENABLED`  | enabled    |
| `BLOCKED`  | blocked    |
| `DISABLED` | disabled   |
| `DELETED`  | deleted    |