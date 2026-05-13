# PayoutStatusReasonCode

A machine-readable code describing the reason for the payout's current status.

## Example Usage

```python
from mollie.models import PayoutStatusReasonCode

value = PayoutStatusReasonCode.REQUESTED

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                     | Value                    |
| ------------------------ | ------------------------ |
| `REQUESTED`              | requested                |
| `INITIATED`              | initiated                |
| `PROCESSING_AT_BANK`     | processing_at_bank       |
| `COMPLETED`              | completed                |
| `CANCELED`               | canceled                 |
| `FAILED`                 | failed                   |
| `INSUFFICIENT_FUNDS`     | insufficient_funds       |
| `RETURNED`               | returned                 |
| `INVALID_REQUEST`        | invalid_request          |
| `ORGANIZATION_INACTIVE`  | organization_inactive    |
| `PAYOUTS_BLOCKED`        | payouts_blocked          |
| `BANK_PROCESSING_FAILED` | bank_processing_failed   |
| `BALANCE_NOT_FOUND`      | balance_not_found        |
| `EXPIRED`                | expired                  |