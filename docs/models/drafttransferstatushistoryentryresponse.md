# DraftTransferStatusHistoryEntryResponse

A single entry in the draft transfer's status history.


## Fields

| Field                                                                          | Type                                                                           | Required                                                                       | Description                                                                    | Example                                                                        |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `status`                                                                       | [models.DraftTransferStatusResponse](../models/drafttransferstatusresponse.md) | :heavy_check_mark:                                                             | The status of the draft transfer.                                              | awaiting-initiation                                                            |
| `created_at`                                                                   | [date](https://docs.python.org/3/library/datetime.html#date-objects)           | :heavy_check_mark:                                                             | The date and time the draft transfer entered this status, in ISO 8601 format.  | 2025-01-01T12:00:00+00:00                                                      |