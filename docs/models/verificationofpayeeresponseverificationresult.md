# VerificationOfPayeeResponseVerificationResult


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `outcome`                                                            | [models.VerificationResultEnum](../models/verificationresultenum.md) | :heavy_check_mark:                                                   | The result of the Verification of Payee check.                       | matched                                                              |
| `account_holder_name`                                                | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | The corrected name if the verification result is `close_match`.      | Jan Jansen                                                           |