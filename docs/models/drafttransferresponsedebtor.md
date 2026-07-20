# DraftTransferResponseDebtor

The debtor (sender) of the draft transfer, resolved from `debtorIban` at creation time.


## Fields

| Field                                                                            | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `full_name`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | The full name of the account holder.                                             | Jan Jansen                                                                       |
| `account`                                                                        | [models.DraftTransferResponseAccount](../models/drafttransferresponseaccount.md) | :heavy_check_mark:                                                               | The bank account details of the party.                                           |                                                                                  |