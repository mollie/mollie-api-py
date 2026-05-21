# EntityPairingCodeDetails

Additional pairing code data, present only when requested via the `include` parameter.


## Fields

| Field                                                                                    | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `qr_code`                                                                                | [OptionalNullable[models.EntityPairingCodeQrCode]](../models/entitypairingcodeqrcode.md) | :heavy_minus_sign:                                                                       | The QR code representation of the pairing code.                                          |