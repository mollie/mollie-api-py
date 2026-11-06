# GetNextSettlementRate

The service rates, further divided into `fixed` and `percentage` costs.

For pass-through fees, which are charged by an external party rather than at an agreed Mollie
rate, both `fixed` and `percentage` are `null`.


## Fields

| Field                                                                                             | Type                                                                                              | Required                                                                                          | Description                                                                                       | Example                                                                                           |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `fixed`                                                                                           | [Nullable[models.AmountNullable]](../models/amountnullable.md)                                    | :heavy_check_mark:                                                                                | In v2 endpoints, monetary amounts are represented as objects with a `currency` and `value` field. |                                                                                                   |
| `percentage`                                                                                      | *Nullable[str]*                                                                                   | :heavy_check_mark:                                                                                | N/A                                                                                               | 2.5                                                                                               |