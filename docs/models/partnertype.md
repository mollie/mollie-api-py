# PartnerType

Indicates the type of partner. Will be `null` if the currently authenticated organization is not
enrolled as a partner.

## Example Usage

```python
from mollie.models import PartnerType

value = PartnerType.OAUTH
```


## Values

| Name         | Value        |
| ------------ | ------------ |
| `OAUTH`      | oauth        |
| `SIGNUPLINK` | signuplink   |
| `USERAGENT`  | useragent    |