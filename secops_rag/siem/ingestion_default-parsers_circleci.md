# Collect CircleCI audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/circleci/  
**Scraped:** 2026-03-05T09:21:09.087859Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CircleCI audit logs
Supported in:
Google secops
SIEM
This parser extracts fields from CircleCI audit logs in CSV and JSON formats, transforming them into the Unified Data Model (UDM). It handles both formats, performs data transformations and enrichments, and maps the extracted fields to their corresponding UDM fields within the
event
object. It focuses on user actions, resource access, and update events, categorizing them and populating relevant UDM fields like
principal
,
target
,
network
, and
metadata
.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to CircleCI.
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
CircleCI Logs
).
Select
Webhook
as the
Source type
.
Select
CircleCI
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
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label applied to the events from this feed.
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
Google Security Operations API
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
Configuring a webhook in CircleCI
Sign in to the CircleCI web interface.
Select the project you want to ingest the logs from.
Click
Project Settings
.
Select
Webhooks
.
Click
Add Webhook
.
Specify values for the following input parameters:
Webhook Name
: provide a descriptive name (for example,
Google SecOps
).
Endpoint URL
: enter the
<ENDPOINT_URL>
of the Google SecOps API endpoint.
Events:
Select the CircleCI events that should trigger the webhook (for example, select
workflow-completed
to send data after a workflow finishes).
Click
Save
to create the webhook.
UDM Mapping Table
Log Field
UDM Mapping
Logic
account.id
read_only_udm.about.resource.attribute.labels.value
The value of
account.id
from the raw log is assigned to the UDM field
read_only_udm.about.resource.attribute.labels.value
where the corresponding
key
is
account_id
.
action
read_only_udm.metadata.product_event_type
The value of
action
from the raw log is assigned to the UDM field
read_only_udm.metadata.product_event_type
.
actor.id
read_only_udm.principal.user.product_object_id
The value of
actor.id
from the raw log is assigned to the UDM field
read_only_udm.principal.user.product_object_id
.
actor.name
read_only_udm.principal.user.userid
The "github: " prefix is removed from the
actor.name
field in the raw log. The remaining value is assigned to the UDM field
read_only_udm.principal.user.userid
. If
actor.name
exists in the raw log, the value
USER_RESOURCE_UPDATE_CONTENT
is assigned to
read_only_udm.metadata.event_type
. Otherwise,
USER_RESOURCE_ACCESS
is assigned.
id
read_only_udm.metadata.product_log_id
The value of
id
from the raw log is assigned to the UDM field
read_only_udm.metadata.product_log_id
. The parser sets the
read_only_udm.metadata.log_type
to
CIRCLECI
. The parser sets the
read_only_udm.metadata.product_name
to
CIRCLECI
. The parser sets the
read_only_udm.metadata.vendor_name
to
CIRCLECI
.
occurred_at
read_only_udm.metadata.event_timestamp
The value of
occurred_at
from the raw log is parsed as a timestamp and assigned to the UDM field
read_only_udm.metadata.event_timestamp
.
organization.name
read_only_udm.target.administrative_domain
The "github: " prefix is removed from the
organization.name
field in the raw log. The remaining value is assigned to the UDM field
read_only_udm.target.administrative_domain
.
payload.job.id
read_only_udm.about.resource.attribute.labels.value
The value of
payload.job.id
from the raw log is assigned to the UDM field
read_only_udm.about.resource.attribute.labels.value
where the corresponding
key
is
job_id
.
payload.job.job_name
read_only_udm.about.resource.attribute.labels.value
The value of
payload.job.job_name
from the raw log is assigned to the UDM field
read_only_udm.about.resource.attribute.labels.value
where the corresponding
key
is
job_name
.
payload.job.job_status
read_only_udm.about.resource.attribute.labels.value
The value of
payload.job.job_status
from the raw log is assigned to the UDM field
read_only_udm.about.resource.attribute.labels.value
where the corresponding
key
is
job_status
.
payload.workflow.id
read_only_udm.about.resource.attribute.labels.value
The value of
payload.workflow.id
from the raw log is assigned to the UDM field
read_only_udm.about.resource.attribute.labels.value
where the corresponding
key
is
workflow_id
.
request.id
read_only_udm.network.session_id
The value of
request.id
from the raw log is assigned to the UDM field
read_only_udm.network.session_id
.
scope.id
read_only_udm.about.resource.attribute.labels.value
The value of
scope.id
from the raw log is assigned to the UDM field
read_only_udm.about.resource.attribute.labels.value
where the corresponding
key
is
scope_id
. The parser initially sets
sec_action
to
BLOCK
. If the
success
field in the raw log is true,
sec_action
is changed to
ALLOW
. The value of
sec_action
is then assigned to the UDM field
read_only_udm.security_result.action
.
target.id
read_only_udm.target.resource.product_object_id
The value of
target.id
from the raw log is assigned to the UDM field
read_only_udm.target.resource.product_object_id
.
target.name
read_only_udm.target.resource.name
The "github: " prefix is removed from the
target.name
field in the raw log. The remaining value is assigned to the UDM field
read_only_udm.target.resource.name
. The parser sets the
read_only_udm.target.resource.resource_type
to
STORAGE_OBJECT
.
version
read_only_udm.target.resource.attribute.labels.value
The value of
version
from the raw log is converted to a string and assigned to the UDM field
read_only_udm.target.resource.attribute.labels.value
where the corresponding
key
is
version
.
Need more help?
Get answers from Community members and Google SecOps professionals.
