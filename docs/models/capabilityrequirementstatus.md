# CapabilityRequirementStatus

The status of the requirement depends on its due date.
If no due date is given, the status will be `requested`.

## Example Usage

```python
from mollie.models import CapabilityRequirementStatus

value = CapabilityRequirementStatus.CURRENTLY_DUE

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name            | Value           |
| --------------- | --------------- |
| `CURRENTLY_DUE` | currently-due   |
| `PAST_DUE`      | past-due        |
| `REQUESTED`     | requested       |