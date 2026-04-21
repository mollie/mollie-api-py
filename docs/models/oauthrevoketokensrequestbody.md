# OauthRevokeTokensRequestBody


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `token_type_hint`                                                                      | *str*                                                                                  | :heavy_check_mark:                                                                     | The type of token you want to revoke.<br/><br/>Possible values: `access_token` `refresh_token` |
| `token`                                                                                | *str*                                                                                  | :heavy_check_mark:                                                                     | The token you want to revoke.                                                          |