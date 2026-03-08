# Collect Datadog logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/datadog/  
**Scraped:** 2026-03-05T09:23:02.186498Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Datadog logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Datadog logs, performs several mutations and Grok matching to structure the data, and maps the extracted fields to the UDM. It handles different log formats within the
message
field, including key-value pairs and JSON objects, and converts specific fields into UDM-compliant labels and additional fields.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Google Cloud IAM.
Privileged access to Cloud Storage.
logs_write_archive
user access to Datadog.
Option 1: Datadog log sharing through Cloud Storage configuration
Configure Datadog integration with Google Cloud Platform
Set up an integration for
Google Cloud Platform in Datadog
. For more information, see the
Datadog Google Cloud integration setup
.
Create a Google Cloud Storage Bucket
Sign in to the Google Cloud console.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
On the
Create a bucket
page, enter your bucket information. After each of the following steps, click
Continue
to proceed to the next step:
In the
Get started
section, do the following:
Enter a unique name that meets the bucket name requirements (for example,
datadog-data
).
To enable hierarchical namespace, click the expander arrow to expand the
Optimize for file oriented and data-intensive workloads
section, and then select
Enable Hierarchical namespace on this bucket
.
To add a bucket label, click the expander arrow to expand the
Labels
section.
Click
Add label
, and specify a key and a value for your label.
In the
Choose where to store your data
section, do the following:
Select a
Location type
.
Use the location type drop-down to select a
Location
where object data within your bucket will be permanently stored.
If you select the
dual-region
location type, you can also choose to enable
turbo replication
by using the relevant checkbox.
To set up cross-bucket replication, expand the
Set up cross-bucket replication
section.
In the
Choose a storage class for your data
section, either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management of your bucket's data.
In the
Choose how to control access to objects
section, select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the expander arrow labeled
Data encryption
, and select a
Data encryption method
.
Click
Create
.
Create a Google Cloud Service Account
Go to
IAM & Admin
>
Service Accounts
.
Create a new service account.
Give it a descriptive name (For example,
datadog-user
).
Grant the service account with
Storage Object Admin
role on the Cloud Storage bucket you created in the previous step.
Create an
SSH key
for the service account.
Download a JSON key file for the service account. Keep this file secure.
Configure Datadog to send logs to Cloud Storage
Sign in to Datadog using a privileged account.
Go to
Logs
>
Log Forwarding
.
Click
+ Create New Archive
.
Select
Google Cloud Storage
.
Input the required parameters and click
Save
.
Option 2: Datadog log sharing through Webhook configuration
Set up feeds
To configure a feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Datadog Logs
).
Select
Webhook
as the
Source type
.
Select
Datadog
as the
Log type
.
Click
Next
.
Optional: Specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
From the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. You need to specify this endpoint URL in your client application.
Click
Done
.
Create an API key for the webhook feed
Go to
Google Cloud console
>
Credentials
.
Go to Credentials
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Chronicle API
.
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL.
If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google SecOps.
SECRET
: the secret key that you generated to authenticate the feed.
Configure Datadog to send logs to webhook
Sign in to Datadog using a privileged account.
Go to
Logs
>
Log Forwarding
.
Select
Custom Destinations
.
Click
+ Create a New Destination
.
Specify values for the following input parameters:
Choose a destination type
: Select
HTTP
.
Name the destination
: Provide a descriptive name for the webhook (for example,
Google SecOps Webhook
).
Configure the destination
: Enter the
ENDPOINT_URL
, followed by the
API_KEY
and
SECRET
.
Configure authentication settings
: Add a general header like the following, this won't malform the HTTP request and allow Datadog to complete webhook creation.
Header name:
Accept
.
Header value:
application/json
.
Click
Save
.
Reference Links
Sharing Logs to Cloud Storage
Forwarding Logs to Webhook
Supported Datadog sample logs
This log sample contains the raw application log data embedded as a JSON string in the
data
field:
{
"batch"
:
{
"id"
:
"DUMMY_BATCH_ID"
,
"source"
:
{
"customer_id"
:
"DUMMY_CUSTOMER_ID"
,
"collector_id"
:
"DUMMY_COLLECTOR_ID"
},
"log_type"
:
"DDOG"
,
"entries"
:
{
"data"
:
"{\"date\":\"2023-06-20T13:41:42.359Z\",\"service\":\"ftcp-converter\",\"host\":\"DUMMY_HOST-001\",\"attributes\":{\"_trace\":{\"baggage\":{\"device_id\":\"DUMMY-DEVICE-ID\",\"vehicle_id\":\"DUMMY-VEHICLE-ID\",\"_sli_service\":\"ftcp-converter/DUMMY_ENCODED_SLI\"},\"origin\":{\"service\":\"ftcp-converter\",\"operation\":\"ProcessingService.processAndPublish\"},\"id\":\"DUMMY_TRACE_ID\"},\"@timestamp\":\"2023-06-20T13:41:42.359Z\",\"level\":\"WARN\",\"thread_name\":\"Processing-327\",\"level_value\":30000,\"@version\":\"1\",\"logger_name\":\"com.autonomic.ftcp.conversion.FTCPConverter\"},\"_id\":\"DUMMY_EVENT_ID\",\"source\":\"ftcp-converter\",\"message\":\"Timestamp Exception thrown: TOO_FAR_IN_PAST errorMessage: No timestamp available, error status:TOO_FAR_IN_PAST { \\\"context\\\":{\\\"BusArch\\\":\\\"3\\\",\\\"esn\\\":\\\"FP001CE3\\\",\\\"CANDBVersion\\\":\\\"B_v19.04A\\\",\\\"ftcpVersion\\\":\\\"5.0.9\\\",\\\"AlertName\\\":\\\"MotiveModeEndAlert\\\",\\\"ingestMessageId\\\":\\\"DUMMY-INGEST-ID\\\",\\\"vehicleId\\\":\\\"DUMMY-VEHICLE-ID\\\",\\\"redactedVin\\\":\\\"len=17\\\",\\\"deviceId\\\":\\\"DUMMY-DEVICE-ID\\\",\\\"timestamp\\\":null} }\",\"status\":\"warn\",\"tags\":[\"kube_namespace:alfa\",\"pod_label_autonomic.ai/tracing:true\",\"kube_app_name:ftcp-converter\", /* ... other tags ... */, \"docker_image:DUMMY_ECR_HOST/au/ftcp-converter:DUMMY_TAG\",\"aws-instance-type:m5.8xlarge\",\"cluster_name:staging\",\"env:staging\",\"kube_cluster_name:staging\",\"kube_role:node\",\"autonomic_ai_team:telemetry-data\"]}"
,
"collection_time"
:
{
"seconds"
:
1689231423
,
"nanos"
:
972102587
}
}
}
}
This sample details an API request and includes network and threat intelligence metadata:
[
{
"date"
:
"2025-02-13T08:35:41.000Z"
,
"attributes"
:
{
"auth_method"
:
"SESSION"
,
"evt"
:
{
"actor"
:
{
"type"
:
"USER"
},
"name"
:
"Request"
},
"org"
:
{
"uuid"
:
"DUMMY-ORG-UUID"
},
"usr"
:
{
"id"
:
"dummy.user@example.com"
,
"uuid"
:
"DUMMY-USER-UUID"
,
"email"
:
"dummy.user@example.com"
},
"action"
:
"accessed"
,
"http"
:
{
"status_code"
:
202
,
"url_details"
:
{
"path"
:
"/api/ui/frontend_telemetry/metrics"
,
"host"
:
"us1.DUMMY-HOST.dog"
},
"method"
:
"POST"
,
"useragent"
:
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
},
"threat_intel"
:
{
"indicators_matched"
:
[
"IP"
],
"results"
:
[
{
"indicator"
:
"0.0.0.0"
,
"additional_data"
:
{
"tunnels"
:
[
{
"anonymous"
:
true
,
"type"
:
"VPN"
}
],
"as"
:
{
"number"
:
16509
,
"organization"
:
"DUMMY-AS-ORGANIZATION"
},
"risks"
:
[
"TUNNEL"
],
"infrastructure"
:
"DATACENTER"
,
"organization"
:
"DUMMY-ORG-GMBH"
,
"client"
:
{},
"location"
:
{
"country"
:
"DE"
,
"city"
:
"Frankfurt am Main"
,
"state"
:
"Hesse"
},
"services"
:
[
"IPSEC"
]
},
"source"
:
{
"name"
:
"spur"
,
"type"
:
"managed"
,
"url"
:
"https://DUMMY-URL.us"
},
"type"
:
"IP"
,
"category"
:
"hosting_proxy"
,
"intention"
:
"suspicious"
}
]
},
"network"
:
{
"client"
:
{
"geoip"
:
{
"continent"
:
{
"code"
:
"EU"
,
"name"
:
"Europe"
},
"country"
:
{
"name"
:
"Germany"
,
"iso_code"
:
"DE"
},
"subdivision"
:
{
"name"
:
"Hesse"
,
"iso_code"
:
"DE-HE"
},
"as"
:
{
"number"
:
"AS16509"
,
"route"
:
"DUMMY_CIDR"
,
"domain"
:
"DUMMY-DOMAIN.com"
,
"name"
:
"DUMMY-AS-NAME, Inc."
,
"type"
:
"hosting"
},
"city"
:
{
"name"
:
"Frankfurt am Main"
},
"timezone"
:
"Europe/Berlin"
,
"ipAddress"
:
" "
,
"location"
:
{
"latitude"
:
50.11552
,
"longitude"
:
8.68417
}
},
"ip"
:
" "
}
},
"status"
:
"info"
,
"timestamp"
:
"2025-02-13T08:35:41Z"
,
"emitted_source"
:
"edge"
},
"_id"
:
"AZT-cxO1AAA63poCZjbsDgAA"
,
"source"
:
"audit"
,
"message"
:
"POST request made to /api/ui/frontend_telemetry/metrics by dummy.user@example.com with response 202"
,
"status"
:
"info"
,
"tags"
:
[
"source:audit"
]
}
]
This sample details a user modification to a resource (log forwarding query):
{
"date"
:
"2025-08-12T10:33:55.000Z"
,
"attributes"
:
{
"evt"
:
{
"actor"
:
{
"type"
:
"USER"
},
"name"
:
"Log Management"
},
"metadata"
:
{
"dd"
:
{
"request_id"
:
"DUMMY-REQUEST-ID"
}
},
"auth_method"
:
"SESSION"
,
"org"
:
{
"name"
:
"DUMMY_ORG_NAME"
,
"uuid"
:
"DUMMY-ORG-UUID"
},
"usr"
:
{
"created"
:
"2025-05-13T13:33:27Z"
,
"name"
:
"John Doe"
,
"id"
:
"user.name@example.com"
,
"uuid"
:
"DUMMY-USER-UUID"
,
"email"
:
"user.name@example.com"
},
"action"
:
"modified"
,
"http"
:
{
"status_code"
:
200
,
"url_details"
:
{
"path"
:
"/api/ui/event-platform/logs/custom-destinations/DUMMY-DESTINATION-ID"
},
"method"
:
"PUT"
,
"level"
:
"info"
,
"useragent"
:
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36 Edg/139.0.0.0"
},
"asset"
:
{
"modified_field"
:
"query"
,
"name"
:
"Google Secops Logs"
,
"id"
:
"DUMMY-DESTINATION-ID"
,
"type"
:
"log_forwarding"
,
"prev_value"
:
{
"data"
:
{
"attributes"
:
{
"query"
:
"host:(DUMMY-HOST-PRD-01 OR DUMMY-HOST-PRD-02 OR DUMMY-HOST-PRD-03 OR DUMMY-HOST-STG-01 OR DUMMY-HOST-STG-02 OR DUMMY-HOST-STG-03 OR DUMMY-HOST-EMEA-01 OR DUMMY-HOST-STG-04 OR DUMMY-HOST-PRD-04) status:(notice OR warn OR error)"
}
}
},
"new_value"
:
{
"data"
:
{
"attributes"
:
{
"query"
:
"service:(sqb-connector-services OR nginx-ingress-controller) status:(notice OR warn OR error)"
}
}
}
},
"network"
:
{
"client"
:
{
"geoip"
:
{
"continent"
:
{
"code"
:
"EU"
,
"name"
:
"Europe"
},
"country"
:
{
"name"
:
"United Kingdom"
,
"iso_code"
:
"GB"
},
"subdivision"
:
{
"name"
:
"DUMMY_CITY"
,
"iso_code"
:
"DUMMY_CODE"
},
"as"
:
{
"number"
:
"AS25180"
,
"route"
:
"DUMMY-CIDR-RANGE"
,
"domain"
:
"DUMMY-DOMAIN.com"
,
"name"
:
"DUMMY-ISP-NAME"
,
"type"
:
"hosting"
},
"city"
:
{
"name"
:
"London"
},
"timezone"
:
"Europe/London"
,
"ipAddress"
:
" "
,
"location"
:
{
"latitude"
:
51.50853
,
"longitude"
:
-0.12574
}
},
"ip"
:
" "
}
},
"status"
:
"info"
,
"timestamp"
:
"2025-08-12T10:33:55Z"
},
"_id"
:
"AZid2AB0AAAxoDbhbVS-EAAA"
,
"source"
:
"audit"
,
"message"
:
"user.name@example.com successfully changed query from \"host:(DUMMY-HOST-PRD-01 OR DUMMY-HOST-PRD-02 OR DUMMY-HOST-PRD-03 OR DUMMY-HOST-STG-01 OR DUMMY-HOST-STG-02 OR DUMMY-HOST-STG-03 OR DUMMY-HOST-EMEA-01 OR DUMMY-HOST-STG-04 OR DUMMY-HOST-PRD-04) status:(notice OR warn OR error)\" to \"service:(sqb-connector-services OR nginx-ingress-controller) status:(notice OR warn OR error)\" for custom destination \"Google Secops Logs\" (DUMMY-DESTINATION-ID)"
,
"status"
:
"info"
}
UDM Mapping Table
Log Field
UDM Mapping
Logic
_id
read_only_udm.metadata.product_log_id
Directly mapped from the
_id
field.
alert
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
alert
field and added as a label within the
security_result
object.
attributes.@timestamp
read_only_udm.metadata.event_timestamp
The event timestamp is extracted from the
attributes.@timestamp
field and converted to seconds and nanoseconds.
attributes.@version
read_only_udm.metadata.product_version
Directly mapped from the
attributes.@version
field.
attributes.level_value
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
attributes.level_value
field and added as a label within the
security_result
object.
attributes.logger_name
read_only_udm.principal.application
Directly mapped from the
attributes.logger_name
field.
attributes._trace.baggage._sli_service
read_only_udm.additional.fields
Directly mapped from the
attributes._trace.baggage._sli_service
field and added as an additional field.
attributes._trace.baggage.device_id
read_only_udm.principal.asset.asset_id
Directly mapped from the
attributes._trace.baggage.device_id
field, prefixed with "Device Id:".
attributes._trace.origin.operation
read_only_udm.metadata.product_event_type
Directly mapped from the
attributes._trace.origin.operation
field.
caller
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
caller
field and added as a label within the
security_result
object.
component
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
component
field and added as a label within the
security_result
object.
context.AlertName
read_only_udm.security_result.threat_name
Directly mapped from the
context.AlertName
field.
context.BusArch
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.BusArch
field and added as a label within the
security_result
object.
context.CANDBVersion
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.CANDBVersion
field and added as a label within the
security_result
object.
context.esn
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.esn
field and added as a label within the
security_result
object.
context.ftcpVersion
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.ftcpVersion
field and added as a label within the
security_result
object.
context.ingestMessageId
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.ingestMessageId
field and added as a label within the
security_result
object.
context.redactedVin
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.redactedVin
field and added as a label within the
security_result
object.
context.vehicleId
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
context.vehicleId
field and added as a label within the
security_result
object.
date
read_only_udm.metadata.collected_timestamp
The collected timestamp is extracted from the
date
field (renamed to
date1
in the parser) and converted to seconds and nanoseconds.
host
read_only_udm.principal.hostname
Directly mapped from the
host
field.
message
read_only_udm.security_result.about.resource.attribute.labels
The
message
field is parsed, and parts of it are used to populate the
summary
and
json_data
fields. The remaining part is treated as key-value pairs and added as labels within the
security_result
object.
msg
read_only_udm.security_result.about.resource.attribute.labels
Extracted from the
msg
field and added as a label within the
security_result
object.
service
read_only_udm.metadata.product_name
Directly mapped from the
service
field.
status
read_only_udm.security_result.severity
The severity is determined based on the
status
field. "INFO", "DEBUG", "debug", and "info" map to "LOW", "WARN" maps to "MEDIUM", and other values are not explicitly mapped in the provided code snippet.
tags
read_only_udm.additional.fields
Each tag in the
tags
array is parsed into key-value pairs and added as additional fields.
N/A
read_only_udm.metadata.event_type
Set to "STATUS_UPDATE" if the
host
field is present, and "GENERIC_EVENT" otherwise.
Need more help?
Get answers from Community members and Google SecOps professionals.
