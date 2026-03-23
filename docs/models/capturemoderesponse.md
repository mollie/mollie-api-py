# CaptureModeResponse

Indicate if the funds should be captured immediately or if you want to [place a hold](https://docs.mollie.com/docs/place-a-hold-for-a-payment#/) 
and capture at a later time.

This field needs to be set to `manual` for method `riverty`.

## Example Usage

```python
from mollie.models import CaptureModeResponse

value = CaptureModeResponse.AUTOMATIC

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name        | Value       |
| ----------- | ----------- |
| `AUTOMATIC` | automatic   |
| `MANUAL`    | manual      |