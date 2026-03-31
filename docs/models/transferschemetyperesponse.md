# TransferSchemeTypeResponse

The transfer scheme to be used for the transfer. The transfer scheme determines the processing time and method of the transfer.

## Example Usage

```python
from mollie.models import TransferSchemeTypeResponse

value = TransferSchemeTypeResponse.SEPA_CREDIT_INST

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `SEPA_CREDIT_INST` | sepa-credit-inst   |
| `SEPA_CREDIT`      | sepa-credit        |