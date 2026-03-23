# RouteGetResponseDestination

The destination of the route.


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               | Example                                                                                   |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `type`                                                                                    | [models.RouteDestinationTypeResponse](../models/routedestinationtyperesponse.md)          | :heavy_check_mark:                                                                        | The type of destination. Currently only the destination type `organization` is supported. | organization                                                                              |
| `organization_id`                                                                         | *str*                                                                                     | :heavy_check_mark:                                                                        | N/A                                                                                       | org_1234567                                                                               |