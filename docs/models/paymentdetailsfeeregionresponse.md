# PaymentDetailsFeeRegionResponse

The applicable card fee region.

## Example Usage

```python
from mollie.models import PaymentDetailsFeeRegionResponse

value = PaymentDetailsFeeRegionResponse.AMERICAN_EXPRESS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                 | Value                |
| -------------------- | -------------------- |
| `AMERICAN_EXPRESS`   | american-express     |
| `AMEX_INTRA_EEA`     | amex-intra-eea       |
| `CARTE_BANCAIRE`     | carte-bancaire       |
| `INTRA_EU`           | intra-eu             |
| `INTRA_EU_CORPORATE` | intra-eu-corporate   |
| `DOMESTIC`           | domestic             |
| `MAESTRO`            | maestro              |
| `OTHER`              | other                |
| `INTER`              | inter                |
| `INTRA_EEA`          | intra_eea            |