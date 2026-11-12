# Reports

## Overview

### Available Operations

* [create](#create) - Create report
* [get](#get) - Get report

## create

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change. To
> join the beta program, reach out to [partners@mollie.com](mailto:partners@mollie.com).

Create a report. Mollie generates it in the background, so you get a `pending` status back right away.

Poll [Get report](get-report) to check on progress, and grab a download link once it's ready.

Creating a report with the exact same parameters while one is already pending or completed doesn't create
a new one. You get the existing report back instead, whatever status it currently has.

### Example Usage

<!-- UsageSnippet language="python" operationID="create-report" method="post" path="/v2/reports" -->
```python
from datetime import date
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN"),
    ),
) as client_sdk:

    client_sdk.reports.create(create_report_request={
        "report_type": mollie.ReportType.TRANSACTION_MARGIN,
        "from_date": date.fromisoformat("2026-08-01"),
        "until_date": date.fromisoformat("2026-08-31"),
    }, idempotency_key="123e4567-e89b-12d3-a456-426")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `create_report_request`                                                          | [models.CreateReportRequest](../../models/createreportrequest.md)                | :heavy_check_mark:                                                               | N/A                                                                              |                                                                                  |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 403, 422, 429   | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |

## get

> 🚧 Beta feature
>
> This feature is currently in private beta, and the final specification may still change. To
> join the beta program, reach out to [partners@mollie.com](mailto:partners@mollie.com).

Retrieve a single report by its ID. Poll this to check on a report you created, and to grab a download
link once it's ready.

The download link is pre-signed and freshly generated on every call, and expires 15 minutes after you get
it. If it expires before you download the file, just call this endpoint again for a new one. Expiry of
the link doesn't affect the report itself.

### Example Usage: get-report-200-completed

<!-- UsageSnippet language="python" operationID="get-report" method="get" path="/v2/reports/{reportId}" example="get-report-200-completed" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN"),
    ),
) as client_sdk:

    res = client_sdk.reports.get(report_id="rpt_XRAG3v9EUyCDcX99pJ2Vc", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
### Example Usage: get-report-200-failed

<!-- UsageSnippet language="python" operationID="get-report" method="get" path="/v2/reports/{reportId}" example="get-report-200-failed" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN"),
    ),
) as client_sdk:

    res = client_sdk.reports.get(report_id="rpt_XRAG3v9EUyCDcX99pJ2Vc", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```
### Example Usage: get-report-200-pending

<!-- UsageSnippet language="python" operationID="get-report" method="get" path="/v2/reports/{reportId}" example="get-report-200-pending" -->
```python
import mollie
from mollie import ClientSDK
import os


with ClientSDK(
    security=mollie.Security(
        advanced_access_token=os.getenv("CLIENT_ADVANCED_ACCESS_TOKEN"),
    ),
) as client_sdk:

    res = client_sdk.reports.get(report_id="rpt_XRAG3v9EUyCDcX99pJ2Vc", idempotency_key="123e4567-e89b-12d3-a456-426")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `report_id`                                                                      | *str*                                                                            | :heavy_check_mark:                                                               | Provide the ID of the related report.                                            | rpt_XRAG3v9EUyCDcX99pJ2Vc                                                        |
| `idempotency_key`                                                                | *Optional[str]*                                                                  | :heavy_minus_sign:                                                               | A unique key to ensure idempotent requests. This key should be a UUID v4 string. | 123e4567-e89b-12d3-a456-426                                                      |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.EntityReport](../../models/entityreport.md)**

### Errors

| Error Type           | Status Code          | Content Type         |
| -------------------- | -------------------- | -------------------- |
| models.ErrorResponse | 400, 403, 404, 429   | application/hal+json |
| models.APIError      | 4XX, 5XX             | \*/\*                |