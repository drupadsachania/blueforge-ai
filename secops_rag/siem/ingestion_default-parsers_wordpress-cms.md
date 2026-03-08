# Collect Wordpress CMS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wordpress-cms/  
**Scraped:** 2026-03-05T09:30:20.281005Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Wordpress CMS logs
Supported in:
Google secops
SIEM
Overview
This parser extracts WordPress CMS logs from JSON or plain text formatted messages. It handles both JSON and non-JSON formatted logs, parsing relevant fields and mapping them to the UDM, including user details, network information, resource attributes, and security result details. The parser also performs several data transformations, such as converting data types, merging fields, and handling specific log patterns for Kubernetes and other resources.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to a WordPress website.
Plugin that enables webhook functionality (for example,
WP Webhooks
).
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
field, enter a name for the feed; for example,
Wordpress CMS Logs
.
Select
Webhook
as the
Source type
.
Select
Wordpress
as the
Log type
.
Click
Next
.
Optional: specify values for the following input parameters:
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
On the
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
: Specify the API key as a header instead of specifying it in the URL. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Configure Wordpress Webhook
Install
and
activate
the
WP Webhooks plugin
(or your chosen webhook plugin) through the WordPress plugin directory.
Go to the
WP Webhooks
submenu in the WordPress administrator menu, typically located under settings.
Click
Send Data
in the top bar menu.
Select the WordPress action that will trigger the webhook. Common examples include
publish_post
(when a new post is published),
user_register
(when a new user registers), or
comment_post
(when a new comment is posted). This depends on the data you select and send to Google SecOps.
Click
Add Webhook URL
.
Configure the Webhook:
Name
: Give your webhook a descriptive name (for example,
Google SecOps Feed
).
Webhook URL
: Paste your Google SecOps endpoint URL.
Click
Save Webhook
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
ClientIP
principal.ip
The client's IP address is extracted from the
ClientIP
field in the raw log.
Code
target.resource.attribute.labels.key
The value "Code" is assigned as a key in the
target.resource.attribute.labels
object.
Code
target.resource.attribute.labels.value
The value of the
Code
field from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
CurrentUserID
target.user.userid
The
CurrentUserID
from the raw log is converted to a string and mapped to the
target.user.userid
field.
EditUserLink
target.url
The
EditUserLink
from the raw log is mapped to the
target.url
field.
EventType
metadata.product_event_type
The
EventType
from the raw log is mapped to the
metadata.product_event_type
field.
FirstName
target.user.first_name
The
FirstName
from the raw log is mapped to the
target.user.first_name
field.
insertId
metadata.product_log_id
The
insertId
from the raw log is mapped to the
metadata.product_log_id
field.
labels.compute.googleapis.com/resource_name
additional.fields.key
The value "Resource Name" is assigned as a key in the
additional.fields
object.
labels.compute.googleapis.com/resource_name
additional.fields.value.string_value
The value of
labels.compute.googleapis.com/resource_name
from the raw log is assigned as a string value in the
additional.fields
object.
labels.k8s-pod/app_kubernetes_io/instance
target.resource.attribute.labels.key
The value "Kubernetes IO Instance" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/app_kubernetes_io/instance
target.resource.attribute.labels.value
The value of
labels.k8s-pod/app_kubernetes_io/instance
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/app_kubernetes_io/managed-by
target.resource.attribute.labels.key
The value "Kubernetes IO Instance Manager" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/app_kubernetes_io/managed-by
target.resource.attribute.labels.value
The value of
labels.k8s-pod/app_kubernetes_io/managed-by
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/app_kubernetes_io/name
target.resource.attribute.labels.key
The value "Kubernetes IO Instance Name" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/app_kubernetes_io/name
target.resource.attribute.labels.value
The value of
labels.k8s-pod/app_kubernetes_io/name
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/controller-revision-hash
target.resource.attribute.labels.key
The value "Controller Revision Hash" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/controller-revision-hash
target.resource.attribute.labels.value
The value of
labels.k8s-pod/controller-revision-hash
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/helm_sh/chart
target.resource.attribute.labels.key
The value "Kubernetes IO Instance Manager SH" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/helm_sh/chart
target.resource.attribute.labels.value
The value of
labels.k8s-pod/helm_sh/chart
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/k8s-app
target.resource.attribute.labels.key
The value "Application" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/k8s-app
target.resource.attribute.labels.value
The value of
labels.k8s-pod/k8s-app
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/pod-template-generation
target.resource.attribute.labels.key
The value "Pod Template Generation" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/pod-template-generation
target.resource.attribute.labels.value
The value of
labels.k8s-pod/pod-template-generation
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
labels.k8s-pod/pod-template-hash
target.resource.attribute.labels.key
The value "Pod Template Hash" is assigned as a key in the
target.resource.attribute.labels
object.
labels.k8s-pod/pod-template-hash
target.resource.attribute.labels.value
The value of
labels.k8s-pod/pod-template-hash
from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
LastName
target.user.last_name
The
LastName
from the raw log is mapped to the
target.user.last_name
field.
logName
target.resource.attribute.labels.key
The value "Log Name" is assigned as a key in the
target.resource.attribute.labels
object.
logName
target.resource.attribute.labels.value
The value of the
logName
field from the raw log is assigned as a value in the
target.resource.attribute.labels
object.
receiveTimestamp
metadata.event_timestamp
The
receiveTimestamp
from the raw log is parsed and mapped to the
metadata.event_timestamp
field.
resource.labels.cluster_name
additional.fields.key
The value "Cluster Name" is assigned as a key in the
additional.fields
object.
resource.labels.cluster_name
additional.fields.value.string_value
The value of
resource.labels.cluster_name
from the raw log is assigned as a string value in the
additional.fields
object.
resource.labels.cluster_name
target.resource.resource_type
If
resource.labels.cluster_name
is present, the value "CLUSTER" is assigned to
target.resource.resource_type
.
resource.labels.container_name
metadata.product_event_type
If
resource.type
is "k8s_container", the value of
resource.labels.container_name
along with
resource.labels.namespace_name
is used to construct the
metadata.product_event_type
.
resource.labels.container_name
target.resource.name
The value of
resource.labels.container_name
from the raw log is assigned to the
target.resource.name
field.
resource.labels.location
target.location.country_or_region
The value of
resource.labels.location
from the raw log is assigned to the
target.location.country_or_region
field.
resource.labels.namespace_name
additional.fields.key
The value "Namespace Name" is assigned as a key in the
additional.fields
object.
resource.labels.namespace_name
additional.fields.value.string_value
The value of
resource.labels.namespace_name
from the raw log is assigned as a string value in the
additional.fields
object.
resource.labels.namespace_name
metadata.product_event_type
If
resource.type
is "k8s_container", the value of
resource.labels.namespace_name
along with
resource.labels.container_name
is used to construct the
metadata.product_event_type
.
resource.labels.node_name
metadata.product_event_type
If
resource.type
is "k8s_node", the value of
resource.labels.node_name
is used to construct the
metadata.product_event_type
.
resource.labels.pod_name
additional.fields.key
The value "Pod Name" is assigned as a key in the
additional.fields
object.
resource.labels.pod_name
additional.fields.value.string_value
The value of
resource.labels.pod_name
from the raw log is assigned as a string value in the
additional.fields
object.
resource.labels.project_id
additional.fields.key
The value "Project Id" is assigned as a key in the
additional.fields
object.
resource.labels.project_id
additional.fields.value.string_value
The value of
resource.labels.project_id
from the raw log is assigned as a string value in the
additional.fields
object.
resource.type
target.resource.resource_subtype
The value of
resource.type
from the raw log is assigned to the
target.resource.resource_subtype
field.
Roles
target.user.user_role
The
Roles
field from the raw log is converted to uppercase and mapped to the
target.user.user_role
field.
SessionID
network.session_id
The
SessionID
from the raw log is mapped to the
network.session_id
field.
sev
security_result.severity
The value of the
sev
field determines the value of
security_result.severity
. "INFO" or "NOTICE" maps to "INFORMATIONAL", "WARN" maps to "MEDIUM", and "ERR" maps to "ERROR".
TargetUsername
target.user.user_display_name
The
TargetUsername
from the raw log is mapped to the
target.user.user_display_name
field.
textPayload
metadata.description
If
resource.type
is "k8s_node", the value of
textPayload
is mapped to the
metadata.description
field.
textPayload
network.application_protocol
The protocol (for example, HTTP) is extracted from the
textPayload
field using grok patterns.
textPayload
network.http.method
The HTTP method (for example, GET, POST) is extracted from the
textPayload
field using grok patterns.
textPayload
network.http.referral_url
The URL is extracted from the
textPayload
field using grok patterns.
textPayload
network.http.response_code
The HTTP response code is extracted from the
textPayload
field using grok patterns and converted to an integer.
textPayload
network.received_bytes
The received bytes are extracted from the
textPayload
field using grok patterns and converted to an unsigned integer.
textPayload
principal.ip
The source IP address is extracted from the
textPayload
field using grok patterns.
textPayload
security_result.description
The description is extracted from the
textPayload
field using grok patterns.
textPayload
target.file.full_path
The path is extracted from the
textPayload
field using grok patterns.
UserAgent
network.http.user_agent
The
UserAgent
from the raw log is mapped to the
network.http.user_agent
field. The value "USER_RESOURCE_ACCESS" is assigned to
metadata.event_type
.
Need more help?
Get answers from Community members and Google SecOps professionals.
