# MandateDetailsCardLabelResponse

The card's label. Available for card mandates, if the card label could be detected.

## Example Usage

```python
from mollie.models import MandateDetailsCardLabelResponse

value = MandateDetailsCardLabelResponse.AMERICAN_EXPRESS

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name               | Value              |
| ------------------ | ------------------ |
| `AMERICAN_EXPRESS` | American Express   |
| `CARTA_SI`         | Carta Si           |
| `CARTE_BLEUE`      | Carte Bleue        |
| `DANKORT`          | Dankort            |
| `DINERS_CLUB`      | Diners Club        |
| `DISCOVER`         | Discover           |
| `JCB`              | JCB                |
| `LASER`            | Laser              |
| `MAESTRO`          | Maestro            |
| `MASTERCARD`       | Mastercard         |
| `UNIONPAY`         | Unionpay           |
| `VISA`             | Visa               |