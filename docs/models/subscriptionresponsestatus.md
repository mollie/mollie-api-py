# SubscriptionResponseStatus

The subscription's current status is directly related to the status of the underlying customer or mandate that is
enabling the subscription.

## Example Usage

```python
from mollie.models import SubscriptionResponseStatus

value = SubscriptionResponseStatus.PENDING

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `PENDING`   | pending     |
| `ACTIVE`    | active      |
| `CANCELED`  | canceled    |
| `SUSPENDED` | suspended   |
| `COMPLETED` | completed   |