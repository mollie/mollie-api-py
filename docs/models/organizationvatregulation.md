# OrganizationVatRegulation

Mollie applies Dutch VAT for merchants based in The Netherlands, British VAT for merchants based in The United
Kingdom, and shifted VAT for merchants in the European Union.

The field is not present for merchants residing in other countries.

## Example Usage

```python
from mollie.models import OrganizationVatRegulation

value = OrganizationVatRegulation.DUTCH

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name      | Value     |
| --------- | --------- |
| `DUTCH`   | dutch     |
| `BRITISH` | british   |
| `SHIFTED` | shifted   |