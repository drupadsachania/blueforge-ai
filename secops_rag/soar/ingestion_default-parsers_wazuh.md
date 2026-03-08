# Collect Wazuh logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wazuh/  
**Scraped:** 2026-03-05T10:02:32.918870Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Wazuh logs
Supported in:
Google secops
SIEM
Overview
This Wazuh parser ingests SYSLOG and JSON formatted logs, normalizes fields into a common format, and enriches them with Wazuh-specific metadata. It then uses a series of conditional statements based on the
event_type
and
rule_id
fields to map the raw log data to the appropriate UDM event type and fields, handling various log formats and edge cases within the Wazuh ecosystem.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Active Wazuh instance.
Privileged access to Wazuh configuration files.
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
Wazuh Logs
.
Select
Webhook
as the
Source type
.
Select
Wazuh
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
Go to **Google Cloud console
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
Configure Wazuh Cloud Webhook
Complete the following steps to configure Wazuh Cloud Webhook:
Sign in to your Wazuh Cloud.
Go to
Settings
, located in the left pane menu under
Server management
.
Click the
Edit configuration
.
Add the following integration block within the
<integration>
section of the 
configuration.
If the section doesn't exist, copy the entire block with
<integration>
to create one.
Replace the placeholder values with your actual Google SecOps details:
<integration>
<name>google-chronicle</name>
<hook_url>https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs?key=<API_KEY>&secret=<SECRET></hook_url>
<alert_format>json</alert_format>
<level>0</level>
<!--
Adjust
the
level
as
needed
-->
</integration>
CHRONICLE_REGION
: Your Google SecOps region (for example,
us
,
europe-west1
).
GOOGLE_PROJECT_NUMBER
: Your Google Cloud project number.
LOCATION
: Your Google SecOps region (for example,
us
,
europe-west1
).
CUSTOMER_ID
: Your Google SecOps customer ID.
FEED_ID
: The ID of your Google SecOps feed.
API_KEY
: The API Key of your Google Cloud that hosts Google SecOps.
SECRET
: The Secret of your Google SecOps feed.
alert_format
: Set to
json
for Google SecOps compatibility.
level
: Specifies the minimum alert level to be forwarded.
0
sends all alerts.
Click
Save
button.
Click
Restart wazuh-manager
.
Configure Wazuh On-Premise Webhook
Complete the following steps to configure Wazuh On-Premise Webhook:
Access your on-premise Wazuh manager.
Go to
/var/ossec/etc/
directory.
Open the
ossec.conf
file using a text editor (for example,
nano
,
vim
).
Add the following integration block within the
<integration>
section of the configuration.
If the section doesn't exist, copy the entire block with
<integration>
to create one.
Replace the placeholder values with your actual Google SecOps details:
<integration>
<name>google-chronicle</name>
<hook_url>https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs?key=<API_KEY>&secret=<SECRET></hook_url>
<alert_format>json</alert_format>
<level>0</level>
<!--
Adjust
the
level
as
needed
-->
</integration>
CHRONICLE_REGION
: Your Google SecOps region (for example,
us
,
europe-west1
).
GOOGLE_PROJECT_NUMBER
: Your Google Cloud project number.
LOCATION
: Your Google SecOps region (for example,
us
,
europe-west1
).
CUSTOMER_ID
: Your Google SecOps customer ID.
FEED_ID
: The ID of your Google SecOps feed.
API_KEY
: The API Key of your Google Cloud that hosts Google SecOps.
SECRET
: The Secret of your Google SecOps feed.
alert_format
: Set to
json
for Google SecOps compatibility.
level
: Specifies the minimum alert level to be forwarded.
0
sends all alerts.
Restart Wazuh manager to apply the changes:
sudo
systemctl
restart
wazuh-manager
UDM Mapping Table
Log Field
UDM Mapping
Logic
Acct-Authentic
event.idm.read_only_udm.security_result.authentication_mechanism
Directly mapped from the
Acct-Authentic
field.
Acct-Status-Type
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
Acct-Status-Type
field.  The key is set to "Acct-Status-Type".
agent.id
event.idm.read_only_udm.intermediary.resource.id
Directly mapped from the
agent.id
field.
agent.ip
event.idm.read_only_udm.intermediary.ip
,
event.idm.read_only_udm.intermediary.asset.ip
,
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
,
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
agent.ip
field. Also used for principal/target IP in some cases based on event type.
agent.name
event.idm.read_only_udm.security_result.about.hostname
Directly mapped from the
agent.name
field.
application
event.idm.read_only_udm.target.application
Directly mapped from the Wazuh
application
field.
audit-session-id
event.idm.read_only_udm.network.session_id
Directly mapped from the
audit-session-id
field.
ClientIP
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
ClientIP
field.
ClientPort
event.idm.read_only_udm.principal.port
Directly mapped from the
ClientPort
field and converted to integer.
cmd
event.idm.read_only_udm.target.process.command_line
Directly mapped from the
cmd
field.
CommandLine
event.idm.read_only_udm.target.process.command_line
Directly mapped from the
CommandLine
field.
ConfigVersionId
event.idm.read_only_udm.additional.fields[].value.number_value
Directly mapped from the
ConfigVersionId
field. The key is set to "Config Version Id".
data.Account Number
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
data.Account Number
field for specific rule IDs.
data.Control
event.idm.read_only_udm.security_result.action_details
Directly mapped from the
data.Control
field for specific rule IDs.
data.Message
event.idm.read_only_udm.security_result.description
Directly mapped from the
data.Message
field for specific rule IDs.
data.Profile
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
data.Profile
field for specific rule IDs.
data.Region
event.idm.read_only_udm.principal.location.name
Directly mapped from the
data.Region
field for specific rule IDs.
data.Status
event.idm.read_only_udm.security_result.action
Mapped from the
data.Status
field. If the value is "Pass" or "AUDIT_SUCCESS", the action is set to "ALLOW". If the value is "ERROR", "AUDIT_FAILURE", or "FAIL", the action is set to "BLOCK".
data.aws.awsRegion
event.idm.read_only_udm.principal.location.name
Directly mapped from the
data.aws.awsRegion
field for specific rule IDs.
data.aws.eventID
event.idm.read_only_udm.target.resource.attribute.labels[].value
Directly mapped from the
data.aws.eventID
field. The key is set to "Event ID".
data.aws.eventName
event.idm.read_only_udm.metadata.description
Directly mapped from the
data.aws.eventName
field for specific rule IDs.
data.aws.eventSource
event.idm.read_only_udm.metadata.url_back_to_product
Directly mapped from the
data.aws.eventSource
field for specific rule IDs.
data.aws.eventType
event.idm.read_only_udm.metadata.product_event_type
Directly mapped from the
data.aws.eventType
field for specific rule IDs.
data.aws.requestID
event.idm.read_only_udm.target.resource.attribute.labels[].value
Directly mapped from the
data.aws.requestID
field. The key is set to "Request ID".
data.aws.requestParameters.loadBalancerName
event.idm.read_only_udm.target.resource.attribute.labels[].value
Directly mapped from the
data.aws.requestParameters.loadBalancerName
field. The key is set to "LoadBalancer Name".
data.aws.sourceIPAddress
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
data.aws.sourceIPAddress
field for specific rule IDs.
data.aws.source_ip_address
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
data.aws.source_ip_address
field.
data.aws.userIdentity.accountId
event.idm.read_only_udm.principal.user.product_object_id
Directly mapped from the
data.aws.userIdentity.accountId
field for specific rule IDs.
data.aws.userIdentity.principalId
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
data.aws.userIdentity.principalId
field for specific rule IDs.
data.aws.userIdentity.sessionContext.sessionIssuer.arn
event.idm.read_only_udm.target.resource.attribute.labels[].value
Directly mapped from the
data.aws.userIdentity.sessionContext.sessionIssuer.arn
field. The key is set to "ARN".
data.aws.userIdentity.sessionContext.sessionIssuer.userName
event.idm.read_only_udm.principal.user.user_display_name
Directly mapped from the
data.aws.userIdentity.sessionContext.sessionIssuer.userName
field for specific rule IDs.
data.command
event.idm.read_only_udm.target.file.full_path
Directly mapped from the
data.command
field.
data.docker.message
event.idm.read_only_udm.security_result.description
Directly mapped from the
data.docker.message
field for specific event types.
data.dstuser
event.idm.read_only_udm.target.user.userid
Directly mapped from the
data.dstuser
field.
data.file
event.idm.read_only_udm.target.file.full_path
Directly mapped from the
data.file
field.
data.package
event.idm.read_only_udm.target.asset.software[].name
Directly mapped from the
data.package
field.
data.srcip
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
data.srcip
field.
data.srcuser
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
data.srcuser
field.
data.subject.account_domain
event.idm.read_only_udm.target.administrative_domain
Directly mapped from the
data.subject.account_domain
field for specific rule IDs.
data.subject.account_name
event.idm.read_only_udm.target.user.user_display_name
Directly mapped from the
data.subject.account_name
field for specific rule IDs.
data.subject.security_id
event.idm.read_only_udm.target.user.windows_sid
Directly mapped from the
data.subject.security_id
field for specific rule IDs.
data.title
event.idm.read_only_udm.target.resource.name
Directly mapped from the
data.title
field.
data.version
event.idm.read_only_udm.target.asset.software[].version
Directly mapped from the
data.version
field.
decoder.name
event.idm.read_only_udm.about.resource.name
,
event.idm.read_only_udm.target.application
Directly mapped from the
decoder.name
field. Also used for target application in some cases.
decoder.parent
event.idm.read_only_udm.about.resource.parent
Directly mapped from the
decoder.parent
field.
Description
event.idm.read_only_udm.metadata.description
Directly mapped from the
Description
field.
Destination
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
,
event.idm.read_only_udm.target.port
Parsed to extract target IP and port.
DestinationIPAddress
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
DestinationIPAddress
field.
DestinationPort
event.idm.read_only_udm.target.port
Directly mapped from the
DestinationPort
field and converted to integer.
device_ip_address
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
device_ip_address
field.
feature
event.idm.read_only_udm.metadata.product_event_type
Directly mapped from the
feature
field, sometimes combined with
message_type
.
file_path
event.idm.read_only_udm.target.file.full_path
Directly mapped from the
file_path
field.
Framed-IP-Address
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
Framed-IP-Address
field.
full_log
event.idm.read_only_udm.principal.port
,
event.idm.read_only_udm.security_result.description
,
event.idm.read_only_udm.about.labels[].value
Parsed to extract port number, security result description, and subject logon ID.
Hashes
event.idm.read_only_udm.target.process.file.sha256
,
event.idm.read_only_udm.target.process.file.md5
Parsed to extract SHA256 and MD5 hashes.
hostname
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
hostname
field.
Image
event.idm.read_only_udm.target.process.file.full_path
Directly mapped from the
Image
field.
IntegrityLevel
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
IntegrityLevel
field. The key is set to "Integrity Level".
kv_data
event.idm.read_only_udm.target.process.file.full_path
,
event.idm.read_only_udm.target.process.pid
,
event.idm.read_only_udm.target.process.parent_process.file.full_path
,
event.idm.read_only_udm.target.process.parent_process.command_line
,
event.idm.read_only_udm.target.process.parent_process.product_specific_process_id
,
event.idm.read_only_udm.target.process.product_specific_process_id
,
event.idm.read_only_udm.metadata.description
,
event.idm.read_only_udm.additional.fields[].value.string_value
Parsed to extract various fields related to process creation, file hashes, and description.
kv_log_data
event.idm.read_only_udm.security_result.severity_details
Parsed to extract Alert Level.
location
event.idm.read_only_udm.target.file.full_path
Directly mapped from the
location
field.
LogonGuid
event.idm.read_only_udm.additional.fields[].value.string_value
Directly mapped from the
LogonGuid
field after removing curly braces. The key is set to "Logon Guid".
LogonId
event.idm.read_only_udm.about.labels[].value
,
event.idm.read_only_udm.additional.fields[].value.string_value
Used for subject logon ID in logoff events and directly mapped for other events. The key is set to "Logon id".
log_description
event.idm.read_only_udm.metadata.description
Directly mapped from the
log_description
field.
log_message
event.idm.read_only_udm.target.file.full_path
,
event.idm.read_only_udm.metadata.description
Parsed to extract path and log description.
manager.name
event.idm.read_only_udm.about.user.userid
,
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
manager.name
field. Also used for principal user ID in some cases.
md5
event.idm.read_only_udm.target.process.file.md5
Directly mapped from the
md5
field.
message
event.idm.read_only_udm.metadata.product_event_type
,
event.idm.read_only_udm.metadata.description
,
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
,
event.idm.read_only_udm.target.process.command_line
,
event.idm.read_only_udm.network.http.method
,
event.idm.read_only_udm.network.http.response_code
,
event.idm.read_only_udm.principal.user.userid
,
event.idm.read_only_udm.principal.mac
,
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
,
event.idm.read_only_udm.target.port
,
event.idm.read_only_udm.principal.nat_ip
,
event.idm.read_only_udm.principal.nat_port
,
event.idm.read_only_udm.security_result.severity
,
event.idm.read_only_udm.network.session_id
,
event.idm.read_only_udm.security_result.detection_fields[].value
,
event.idm.read_only_udm.additional.fields[].value.number_value
,
event.idm.read_only_udm.target.url
,
event.idm.read_only_udm.target.application
,
event.idm.read_only_udm.principal.resource.attribute.labels[].value
,
event.idm.read_only_udm.security_result.rule_type
,
event.idm.read_only_udm.security_result.description
,
event.idm.read_only_udm.network.http.user_agent
,
event.idm.read_only_udm.principal.process.pid
,
event.idm.read_only_udm.principal.resource.attribute.labels[].value
,
event.idm.read_only_udm.security_result.severity_details
Parsed using grok to extract various fields depending on the log format.
message_data
event.idm.read_only_udm.metadata.description
,
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
,
event.idm.read_only_udm.principal.port
,
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
,
event.idm.read_only_udm.target.port
,
event.idm.read_only_udm.network.sent_bytes
,
event.idm.read_only_udm.network.received_bytes
,
event.idm.read_only_udm.network.ip_protocol
,
event.idm.read_only_udm.metadata.event_type
Parsed to extract message data, IP addresses, ports, bytes sent/received, and event type.
message_type
event.idm.read_only_udm.metadata.product_event_type
,
event.idm.read_only_udm.metadata.description
Directly mapped from the
message_type
field, sometimes combined with
feature
. Also used for description in some cases.
method
event.idm.read_only_udm.network.http.method
Directly mapped from the
method
field.
NAS-IP-Address
event.idm.read_only_udm.principal.nat_ip
Directly mapped from the
NAS-IP-Address
field.
NAS-Port
event.idm.read_only_udm.principal.nat_port
Directly mapped from the
NAS-Port
field and converted to integer.
NAS-Port-Type
event.idm.read_only_udm.principal.resource.attribute.labels[].value
Directly mapped from the
NAS-Port-Type
field. The key is set to "nas_port_type".
NetworkDeviceName
event.idm.read_only_udm.intermediary.hostname
Directly mapped from the
NetworkDeviceName
field after removing backslashes.
ParentCommandLine
event.idm.read_only_udm.target.process.parent_process.command_line
Directly mapped from the
ParentCommandLine
field.
ParentImage
event.idm.read_only_udm.target.process.parent_process.file.full_path
Directly mapped from the
ParentImage
field.
ParentProcessGuid
event.idm.read_only_udm.target.process.parent_process.product_specific_process_id
Directly mapped from the
ParentProcessGuid
field after removing curly braces and prepending "ID:".
ParentProcessId
event.idm.read_only_udm.target.process.parent_process.pid
Directly mapped from the
ParentProcessId
field.
predecoder.hostname
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
Directly mapped from the
predecoder.hostname
field.
ProcessGuid
event.idm.read_only_udm.target.process.product_specific_process_id
Directly mapped from the
ProcessGuid
field after removing curly braces and prepending "ID:".
ProcessId
event.idm.read_only_udm.target.process.pid
Directly mapped from the
ProcessId
field.
product_event_type
event.idm.read_only_udm.metadata.product_event_type
Directly mapped from the
product_event_type
field.
response_code
event.idm.read_only_udm.network.http.response_code
Directly mapped from the
response_code
field and converted to integer.
rule.description
event.idm.read_only_udm.metadata.event_type
,
event.idm.read_only_udm.security_result.summary
Used to determine event type and directly mapped to security result summary.
rule.id
event.idm.read_only_udm.metadata.product_log_id
,
event.idm.read_only_udm.security_result.rule_id
Directly mapped from the
rule.id
field.
rule.info
event.idm.read_only_udm.target.url
Directly mapped from the
rule.info
field.
rule.level
event.idm.read_only_udm.security_result.severity_details
Used to set severity details.
r_cat_name
event.idm.read_only_udm.metadata.event_type
Used to determine event type.
r_msg_id
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
r_msg_id
field.
security_result.severity
event.idm.read_only_udm.security_result.severity
Directly mapped from the
security_result.severity
field.
ServerIP
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
ServerIP
field.
ServerPort
event.idm.read_only_udm.target.port
Directly mapped from the
ServerPort
field and converted to integer.
sha256
event.idm.read_only_udm.target.process.file.sha256
Directly mapped from the
sha256
field.
Source
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
,
event.idm.read_only_udm.principal.port
Parsed to extract principal IP and port.
src_ip
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.asset.ip
Directly mapped from the
src_ip
field.
sr_description
event.idm.read_only_udm.metadata.event_type
,
event.idm.read_only_udm.security_result.description
Used to determine event type and directly mapped to security result description.
syscheck.md5_after
event.idm.read_only_udm.target.process.file.md5
Directly mapped from the
syscheck.md5_after
field.
syscheck.md5_before
event.idm.read_only_udm.src.process.file.md5
Directly mapped from the
syscheck.md5_before
field.
syscheck.path
event.idm.read_only_udm.target.file.full_path
Directly mapped from the
syscheck.path
field.
syscheck.sha1_after
event.idm.read_only_udm.target.process.file.sha1
Directly mapped from the
syscheck.sha1_after
field.
syscheck.sha1_before
event.idm.read_only_udm.src.process.file.sha1
Directly mapped from the
syscheck.sha1_before
field.
syscheck.sha256_after
event.idm.read_only_udm.target.process.file.sha256
Directly mapped from the
syscheck.sha256_after
field.
syscheck.sha256_before
event.idm.read_only_udm.src.process.file.sha256
Directly mapped from the
syscheck.sha256_before
field.
syscheck.size_after
event.idm.read_only_udm.target.process.file.size
Directly mapped from the
syscheck.size_after
field and converted to unsigned integer.
syscheck.size_before
event.idm.read_only_udm.src.process.file.size
Directly mapped from the
syscheck.size_before
field and converted to unsigned integer.
syscheck.uname_after
event.idm.read_only_udm.principal.user.user_display_name
Directly mapped from the
syscheck.uname_after
field.
target_url
event.idm.read_only_udm.target.url
Directly mapped from the
target_url
field.
timestamp
event.idm.read_only_udm.metadata.event_timestamp
Directly mapped from the
timestamp
field.
Total_bytes_recv
event.idm.read_only_udm.network.received_bytes
Directly mapped from the
Total_bytes_recv
field and converted to unsigned integer.
Total_bytes_send
event.idm.read_only_udm.network.sent_bytes
Directly mapped from the
Total_bytes_send
field and converted to unsigned integer.
User-Name
event.idm.read_only_udm.principal.user.userid
,
event.idm.read_only_udm.principal.mac
Directly mapped from the
User-Name
field if it's not a MAC address. Otherwise, parsed as a MAC address.
user_agent
event.idm.read_only_udm.network.http.user_agent
Directly mapped from the
user_agent
field.
user_id
event.idm.read_only_udm.principal.user.userid
Directly mapped from the
user_id
field.
UserName
event.idm.read_only_udm.principal.user.userid
,
event.idm.read_only_udm.principal.mac
Directly mapped from the
UserName
field if it's not a MAC address. Otherwise, parsed as a MAC address.
VserverServiceIP
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.asset.ip
Directly mapped from the
VserverServiceIP
field.
VserverServicePort
event.idm.read_only_udm.target.port
Directly mapped from the
VserverServicePort
field and converted to integer.
win.system.channel
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
win.system.channel
field. The key is set to "channel".
win.system.computer
event.idm.read_only_udm.principal.resource.attribute.labels[].value
Directly mapped from the
win.system.computer
field. The key is set to "computer".
win.system.eventID
event.idm.read_only_udm.metadata.product_log_id
Directly mapped from the
win.system.eventID
field.
win.system.message_description
event.idm.read_only_udm.metadata.description
Directly mapped from the
win.system.message_description
field.
win.system.processID
event.idm.read_only_udm.principal.process.pid
Directly mapped from the
win.system.processID
field.
win.system.providerGuid
event.idm.read_only_udm.principal.resource.attribute.labels[].value
Directly mapped from the
win.system.providerGuid
field. The key is set to "providerGuid".
win.system.providerName
event.idm.read_only_udm.principal.resource.attribute.labels[].value
Directly mapped from the
win.system.providerName
field. The key is set to "providerName".
win.system.severityValue
event.idm.read_only_udm.security_result.severity
,
event.idm.read_only_udm.security_result.severity_details
Directly mapped from the
win.system.severityValue
field if it's a valid severity value.
win.system.systemTime
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
win.system.systemTime
field. The key is set to "systemTime".
win.system.threadID
event.idm.read_only_udm.security_result.detection_fields[].value
Directly mapped from the
win.system.threadID
field. The key is set to "threadID".
N/A
event.idm.read_only_udm.metadata.event_type
Set to "GENERIC_EVENT" as a default value, overridden by specific logic for different event types.
N/A
event.idm.read_only_udm.extensions.auth.mechanism
Set to "REMOTE" for login events.
N/A
event.idm.read_only_udm.extensions.auth.type
Set to "PASSWORD" for login/logout events, overridden to "MACHINE" for some events.
N/A
event.idm.read_only_udm.network.ip_protocol
Set to "TCP" for TCP network connections.
N/A
event.idm.read_only_udm.security_result.action
Set to "ALLOW" for login and successful events, "BLOCK" for failed events.
N/A
event.idm.read_only_udm.metadata.log_type
Set to "WAZUH".
N/A
event.idm.read_only_udm.metadata.product_name
Set to "Wazuh".
Need more help?
Get answers from Community members and Google SecOps professionals.
