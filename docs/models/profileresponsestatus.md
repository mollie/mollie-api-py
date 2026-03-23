# ProfileResponseStatus

The profile status determines whether the profile is able to receive live payments.

* `unverified`: The profile has not been verified yet and can only be used to create test payments.
* `verified`: The profile has been verified and can be used to create live payments and test payments.
* `blocked`: The profile is blocked and can no longer be used or changed.

## Example Usage

```python
from mollie.models import ProfileResponseStatus

value = ProfileResponseStatus.UNVERIFIED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `UNVERIFIED` | unverified   |
| `VERIFIED`   | verified     |
| `BLOCKED`    | blocked      |