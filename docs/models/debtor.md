# Debtor

The debtor (sender) of the transfer, including their name and account details.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `full_name`                                                            | *str*                                                                  | :heavy_check_mark:                                                     | The full name of the account holder.                                   | Jan Jansen                                                             |
| `account`                                                              | [models.TransferResponseAccount](../models/transferresponseaccount.md) | :heavy_check_mark:                                                     | The bank account details of the party.                                 |                                                                        |