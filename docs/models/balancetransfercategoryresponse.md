# BalanceTransferCategoryResponse

The type of the transfer. Different fees may apply to different types of transfers.

## Example Usage

```python
from mollie.models import BalanceTransferCategoryResponse

value = BalanceTransferCategoryResponse.INVOICE_COLLECTION

# Open enum: unrecognized values are captured as UnrecognizedStr
```


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `INVOICE_COLLECTION`    | invoice_collection      |
| `PURCHASE`              | purchase                |
| `CHARGEBACK`            | chargeback              |
| `REFUND`                | refund                  |
| `SERVICE_PENALTY`       | service_penalty         |
| `DISCOUNT_COMPENSATION` | discount_compensation   |
| `MANUAL_CORRECTION`     | manual_correction       |
| `OTHER_FEE`             | other_fee               |