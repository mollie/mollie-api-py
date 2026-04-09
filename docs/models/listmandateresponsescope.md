# ListMandateResponseScope

An array defining the eligible use cases for the mandate. For creditcard mandates, this field will always be 
present and can contain one or both of the following values:

## Example Usage

```python
from mollie.models import ListMandateResponseScope

value = ListMandateResponseScope.CUSTOMER_PRESENT

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                   | Value                  |
| ---------------------- | ---------------------- |
| `CUSTOMER_PRESENT`     | customer-present       |
| `CUSTOMER_NOT_PRESENT` | customer-not-present   |