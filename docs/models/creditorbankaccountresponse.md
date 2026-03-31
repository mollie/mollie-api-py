# CreditorBankAccountResponse

The bank account details of the creditor (recipient) for Verification of Payee.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `account_holder_name`                                                          | *str*                                                                          | :heavy_check_mark:                                                             | The full name of the creditor account holder to verify against bank records.   | Jan Jansen                                                                     |
| `format_`                                                                      | [models.AccountNumberFormatResponse](../models/accountnumberformatresponse.md) | :heavy_check_mark:                                                             | The format of the account number.                                              | iban                                                                           |
| `account_number`                                                               | *str*                                                                          | :heavy_check_mark:                                                             | The bank account details of the creditor.                                      | NL02ABNA0123456789                                                             |