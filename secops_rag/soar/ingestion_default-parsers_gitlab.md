# Collect GitLab logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gitlab/  
**Scraped:** 2026-03-05T09:56:33.464823Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect GitLab logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from GitLab JSON logs, normalizes them into the Unified Data Model (UDM), and enriches the data with additional context. It handles various GitLab event types, focusing on user actions, resource access, and security results, while also processing network and application-related information. The parser also performs logic based on roles and actions within GitLab, categorizing events and assigning appropriate severities.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to GitLab.
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
GitLab Logs
).
Select
Webhook
as the
Source type
.
Select
Gitlab
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
Configure a webhook in GitLab for Google SecOps
Open your web browser and go to the GitLab project for which you want to configure the webhook.
In your project, go to
Settings
>
Webhooks
.
Click
Add new webhook
.
In the
URL
field, paste the Google SecOps Endpoint URL.
Click
Add custom header
.
Type
X-Webhook-Access-Key
in the
Header Name
field.
For the
Header Value
field, copy the Secret Key generated during Google SecOps Feed configuration.
Click
Add custom header
.
Type
X-goog-api-key
in the
Header Name
field.
For the
Header Value
field, copy the API Key generated during Google SecOps Feed configuration.
Note: For enhanced security, generate a secret token and add it to both the GitLab webhook configuration and the corresponding Google SecOps Feed configuration. This helps verify the authenticity of incoming webhooks.
Choose the GitLab events that should trigger the webhook. For example, you might select
Push events
to send data to Google SecOps every time code is pushed to the repository. Carefully consider which events are relevant to your security monitoring needs. Too many events can lead to unnecessary load.
To better understand the webhooks purpose, give it a meaningful name, such as
Google SecOps Webhook
.
Ensure the
Enable SSL verification
checkbox is selected. This is crucial for secure communication.
Click
Add webhook
to save your configuration.
UDM Mapping Table
Log Field
UDM Mapping
Logic
author_id
principal.user.userid
Converted to string.
author_name
principal.user.email_addresses
If the value matches an email address regex.
author_name
principal.user.user_display_name
If the value does not match an email address regex.
details.as
principal.resource.attribute.labels
Added as a label with key "as".
details.add
principal.resource.attribute.labels
Added as a label with key "add".
details.as
principal.user.role_name
The raw log field value.
details.as
principal.user.attribute.roles.type
Set to "ADMINISTRATOR" if
details.as
is "Owner", "SERVICE_ACCOUNT" if
details.as
is "Developer", "Maintainer", or "Reporter", and "TYPE_UNSPECIFIED" if
details.as
is "Guest".
details.custom_message
security_result.description
The raw log field value.
details.custom_message.action
security_result.summary
The raw log field value.
details.entity_path
target.file.full_path
The raw log field value.
details.target_id
target.resource.id
Converted to string.
entity_path
target.file.full_path
The raw log field value.
entity_type
target.resource.attribute.labels
Added as a label with key "Entity Type".
event_type
metadata.product_event_type
The raw log field value.
insertId
metadata.product_log_id
The raw log field value.
ip_address
principal.ip
,
principal.asset.ip
The raw log field value.
jsonPayload.action
additional.fields
Added as a field with key "action" and string value.
jsonPayload.controller
additional.fields
Added as a field with key "controller" and string value.
jsonPayload.correlation_id
principal.asset_id
Prefixed with "id: ".
jsonPayload.cpu_s
additional.fields
Added as a field with key "cpu_s" and string value.
jsonPayload.details.custom_message.protocol
network.application_protocol
Set to "UNKNOWN_APPLICATION_PROTOCOL" if the value is "web", otherwise converted to uppercase.  Also added as an additional field with key "Application Protocol" if the value is "web".
jsonPayload.mem_total_bytes
additional.fields
Added as a field with key "mem_total_bytes" and string value.
jsonPayload.meta_caller_id
additional.fields
Added as a field with key "Caller Id" and string value.
jsonPayload.meta_client_id
target.user.userid
The raw log field value.
jsonPayload.meta_feature_category
additional.fields
Added as a field with key "Feature Category" and string value.
jsonPayload.meta_remote_ip
principal.ip
,
principal.asset.ip
The raw log field value, parsed as a JSON array and merged into the IP fields.
jsonPayload.meta_user
principal.user.userid
Used as a fallback if
jsonPayload.username
is empty.
jsonPayload.method
network.http.method
The raw log field value.
jsonPayload.path
target.process.file.full_path
The raw log field value.
jsonPayload.pid
target.process.pid
Converted to string.
jsonPayload.remote_ip
principal.ip
,
principal.asset.ip
The raw log field value.
jsonPayload.request_urgency
additional.fields
Added as a field with key "Request Urgency" and string value.
jsonPayload.severity
security_result.severity
Set to "INFORMATIONAL" if the value is "INFO", "ERROR" if the value is "ERROR", and "MEDIUM" if the value is "NOTICE".
jsonPayload.status
network.http.response_code
Converted to integer if not "ACTIVE".
jsonPayload.ua
network.http.user_agent
The raw log field value.
jsonPayload.username
principal.user.userid
The raw log field value.
jsonPayload.worker_id
principal.application
The raw log field value.
labels.instance_name
principal.hostname
,
principal.asset.hostname
The raw log field value, used if the message contains "Removing user".
logName
security_result.category_details
The raw log field value.
message
security_result.summary
The raw log field value, used if
jsonPayload.severity
is "ERROR".
protoPayload.@type
additional.fields
Added as a field with key "protoPayload type" and string value.
protoPayload.authenticationInfo.principalEmail
principal.user.email_addresses
,
principal.user.userid
The raw log field value.
protoPayload.authenticationInfo.principalSubject
additional.fields
Added as a field with key "authenticationInfo principalSubject" and string value.
protoPayload.authenticationInfo.serviceAccountKeyName
additional.fields
Added as a field with key "authenticationInfo serviceAccountKeyName" and string value.
protoPayload.authorizationInfo
target.resource.attribute.labels
,
security_result.action
Values within this field are added as labels with keys prefixed with "authenticationInfo". The
security_result.action
is set to "ALLOW" if a value within
granted
is true, and "BLOCK" if false. Nested fields like
resourceAttributes
are also added as labels with keys prefixed with "authenticationInfo_resourceAttributes".
protoPayload.methodName
additional.fields
Added as a field with key "protoPayload methodName" and string value.
protoPayload.request.@type
additional.fields
Added as a field with key "Request Type" and string value.
protoPayload.request.resource
target.resource.attribute.labels
Added as a label with key "Request resource".
protoPayload.requestMetadata.callerIp
additional.fields
Added as a field with key "requestMetadata callerIp" and string value.
protoPayload.requestMetadata.callerSuppliedUserAgent
additional.fields
Added as a field with key "requestMetadata callerSuppliedUserAgent" and string value.
protoPayload.serviceName
additional.fields
Added as a field with key "serviceName" and string value.
protoPayload.status.code
additional.fields
Added as a field with key "protoPayload status code" and string value.
protoPayload.status.message
additional.fields
,
target.user.email_addresses
,
target.user.userid
Added as a field with key "protoPayload status message" and string value.  If an email address can be extracted from the message, it's added to
target.user.email_addresses
and
target.user.userid
.
receiveTimestamp
metadata.event_timestamp
,
timestamp
Parsed as the event timestamp.
resource.labels.project_id
target.resource.attribute.labels
Added as a label with key "Project id".
resource.labels.zone
target.cloud.availability_zone
The raw log field value.
resource.type
target.cloud.environment
Set to "GOOGLE_CLOUD_PLATFORM" if the value matches "gce".
security_result.action
security_result.action
Derived from
protoPayload.authorizationInfo.granted
.
security_result.category_details
security_result.category_details
Merged with
logName
.
security_result.description
security_result.description
Derived from
jsonPayload.details.custom_message
.
security_result.severity
security_result.severity
Derived from
severity
or
jsonPayload.severity
.
security_result.summary
security_result.summary
Derived from
jsonPayload.details.custom_message.action
or
jsonPayload.message
.
severity
security_result.severity
Set to "INFORMATIONAL" if the value is "INFO", "ERROR" if the value is "ERROR", and "MEDIUM" if the value is "NOTICE".
sourceLocation
principal.resource.attribute.labels
Values within this field are added as labels.
target_details
target.resource.attribute.labels
Added as a label with key "Target Details".
target_type
target.resource.attribute.labels
Added as a label with key "target type".
timestamp
timestamp
The raw log field value. Set based on the presence of principal and target fields.  Defaults to "GENERIC_EVENT" if no specific condition is met. Possible values are "USER_RESOURCE_UPDATE_CONTENT", "USER_RESOURCE_ACCESS", "USER_UNCATEGORIZED".  Set to "GITLAB". Set to "GITLAB".
Need more help?
Get answers from Community members and Google SecOps professionals.
