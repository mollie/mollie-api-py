# Owner

Personal data of your customer.


## Fields

| Field                                                                  | Type                                                                   | Required                                                               | Description                                                            | Example                                                                |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `email`                                                                | *str*                                                                  | :heavy_check_mark:                                                     | The email address of your customer.                                    | john@example.org                                                       |
| `given_name`                                                           | *str*                                                                  | :heavy_check_mark:                                                     | The given name (first name) of your customer.                          | John                                                                   |
| `family_name`                                                          | *str*                                                                  | :heavy_check_mark:                                                     | The family name (surname) of your customer.                            | Doe                                                                    |
| `locale`                                                               | [OptionalNullable[models.LocaleResponse]](../models/localeresponse.md) | :heavy_minus_sign:                                                     | Allows you to preset the language to be used.                          | en_US                                                                  |