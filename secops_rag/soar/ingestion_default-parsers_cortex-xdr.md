# Collect Palo Alto Cortex XDR alerts logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cortex-xdr/  
**Scraped:** 2026-03-05T09:59:01.772930Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Cortex XDR alerts logs
Supported in:
Google secops
SIEM
This document describes how you can collect Palo Alto Cortex XDR alerts logs by
setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
CORTEX_XDR
ingestion label.
Configure Palo Alto Cortex XDR alerts
To configure Palo Alto Cortex XDR alerts, complete the following tasks:
Get the Palo Alto Cortex XDR alerts API key
.
Get the Palo Alto Cortex XDR alerts API key ID
.
Get the fully qualified domain name (FQDN)
.
Get the Palo Alto Cortex XDR alerts API key
Sign in to the Cortex XDR portal.
In the
Settings
menu, click
Settings
.
Select
+New key
.
In the
Security level
section, select
Advanced
.
In the
Roles
section, select
Viewer
.
Click
Generate
.
Copy the API key, and then click
Done
. The API key represents your unique
authorization key and is displayed only at the time of creation. It is required
when you configure the Google Security Operations feed.
Get the Palo Alto Cortex XDR alerts API key ID
In the
Configurations
section, navigate to
API keys
>
ID
. Note your
corresponding ID number, which represents the
x-xdr-auth-id:{key_id}
token.
Get FQDN
Navigate to
API keys
.
Click
Copy URL
. Save the URL, which is required when you configure the
Google Security Operations feed.
Set up feeds
To configure this log type, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Select the
Cortex XDR
feed pack.
Configure the following mandatory input parameters:
Source Type
: Third party API (recommended)
Authentication HTTP headers
: Provide the authorization key and authorization
key ID that you obtained previously.
API hostname
: Provide the URL that you obtained previously.
Endpoint
: Specify the endpoint.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create Feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. 
For information about requirements for each feed type, see
Feed configuration by type
.
Field mapping reference
This parser extracts security logs from Palo Alto Networks Cortex XDR in either JSON or SYSLOG (key-value) format, normalizes fields, and maps them to the UDM. It handles both JSON and key-value formats, performs date extraction, enriches the data with metadata, and structures the output for ingestion into Google SecOps.
Enable REST API requests on Cortex XDR and configure a Google SecOps feed
This guide provides step-by-step instructions for enabling REST API requests on Cortex XDR and configuring a corresponding feed in Google SecOps.
Part 1: Enable REST API requests on Cortex XDR
Cortex XDR uses API keys for authentication. Follow these steps to generate an API key:
Log in to the Cortex XDR management console.
Go to
Settings
.
Access
API Keys
.
Generate a new key.
Provide a key name (for example, "SecOps Integration").
Assign the API key the necessary permissions to access the required data. This is crucial for security and ensures the key only has access to what it needs. Consult the Cortex XDR documentation for the specific permissions required for your use case.
Securely store the API key. You will need it for the Google SecOps feed configuration.
This is the only time you will see the full key, so make sure to copy it now.
(Optional) Configure an expiration date for the API key for enhanced security.
Part 2: Configure the feed in Google SecOps
After you generate the API key, configure the feed in Google SecOps to receive data from Cortex XDR:
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
Select
Third Party API
as the
Source type
.
Select the required log type that corresponds to the data you want to ingest from Cortex XDR.
Click
Next
.
Configure the following input parameters:
API Endpoint
: Enter the base URL for the Cortex XDR API. This can be found in the Cortex XDR API documentation.
API Key
: Paste the API key that you generated earlier.
Other Parameters
: Depending on the specific Cortex XDR API that you are using, you might need to provide additional parameters, such as specific data filters or time ranges. Refer to the Cortex XDR API documentation for details.
Click
Next
and then click
Submit
.
Important considerations:
Rate limiting
: Be aware of any rate limits imposed by the Cortex XDR API. Configure the feed accordingly to avoid exceeding these limits.
Error handling
: Implement proper error handling in your Google SecOps configuration to manage situations where the Cortex XDR API is unavailable or returns errors.
Security
: Securely store the API key and follow security best practices. Regularly rotate API keys to minimize the impact of potential compromises.
Documentation
: Refer to the official Cortex XDR API documentation for detailed information on available endpoints, parameters, and data formats.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.action
If
action
contains "BLOCKED", set to "BLOCK".
action
security_result.action_details
If
act
is not empty, null or "none", use the value of
act
. Otherwise, if
action
is not "BLOCKED", use the value of
action
.
action_country
security_result.about.location.country_or_region
Direct mapping. Also used in nested
events
field.
action_file_path
target.resource.attribute.labels
Creates a label with key "action_file_path" and value from the log field.
action_file_sha256
target.file.sha256
Converts to lowercase.
action_local_port
principal.port
Converts to integer.
action_remote_ip
target.ip
Merged into the
target.ip
array.
action_remote_ip
target.asset.ip
Merged into the
target.asset.ip
array.
action_remote_port
target.port
Converts to integer.
act
security_result.action_details
Used if not empty, null, or "none".
agent_data_collection_status
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
agent_device_domain
target.administrative_domain
Direct mapping.
agent_fqdn
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
agent_install_type
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
agent_is_vdi
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
agent_os_sub_type
target.platform_version
Direct mapping.
agent_os_type
target.platform
If "Windows", set to "WINDOWS".
agent_version
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
alert_id
security_result.rule_id
Direct mapping.
app
target.application
Direct mapping.
cat
security_result.category_details
Merged into the
security_result.category_details
field.
category
security_result.category
If "Malware", set to "SOFTWARE_MALICIOUS".
category
security_result.category_details
Merged into the
security_result.category_details
field.
cn1
network.session_id
Direct mapping.
cn1Label
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
contains_featured_host
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
contains_featured_ip
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
contains_featured_user
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
creation_time
metadata.event_timestamp
Converted to timestamp.
cs1
security_result.rule_name
Concatenated with
cs1Label
to form the
security_result.rule_name
.
cs1Label
security_result.rule_name
Concatenated with
cs1
to form the
security_result.rule_name
.
cs2
additional.fields
Creates a key-value pair in
additional.fields
with key from
cs2Label
and string value from
cs2
.
cs2Label
additional.fields
Used as the key for the
cs2
value in
additional.fields
.
cs3
additional.fields
Creates a key-value pair in
additional.fields
with key from
cs3Label
and string value from
cs3
.
cs3Label
additional.fields
Used as the key for the
cs3
value in
additional.fields
.
cs4
additional.fields
Creates a key-value pair in
additional.fields
with key from
cs4Label
and string value from
cs4
.
cs4Label
additional.fields
Used as the key for the
cs4
value in
additional.fields
.
cs5
additional.fields
Creates a key-value pair in
additional.fields
with key from
cs5Label
and string value from
cs5
.
cs5Label
additional.fields
Used as the key for the
cs5
value in
additional.fields
.
cs6
additional.fields
Creates a key-value pair in
additional.fields
with key from
cs6Label
and string value from
cs6
.
cs6Label
additional.fields
Used as the key for the
cs6
value in
additional.fields
.
CSPaccountname
additional.fields
Creates a key-value pair in
additional.fields
with key "CSPaccountname" and string value from the log field.
description
metadata.description
Direct mapping. Also used for
security_result.description
if
event_type
is not GENERIC_EVENT.
destinationTranslatedAddress
target.ip
Merged into the
target.ip
array.
destinationTranslatedAddress
target.asset.ip
Merged into the
target.asset.ip
array.
destinationTranslatedPort
target.port
Converted to integer if not empty or -1.
deviceExternalId
security_result.about.asset_id
Prefixed with "Device External Id: ".
dpt
target.port
Converted to integer if
destinationTranslatedPort
is empty or -1.
dst
target.ip
Merged into the
target.ip
array.
dst
target.asset.ip
Merged into the
target.asset.ip
array.
dst_agent_id
target.ip
Converted to IP address and merged into the
target.ip
array if valid IP.
dst_agent_id
target.asset.ip
Converted to IP address and merged into the
target.asset.ip
array if valid IP.
dvchost
principal.hostname
Direct mapping.
dvchost
principal.asset.hostname
Direct mapping.
endpoint_id
target.process.product_specific_process_id
Prefixed with "cor:".
event_id
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
event_sub_type
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
event_timestamp
metadata.event_timestamp
Converted to timestamp. Also used in nested
events
field.
event_type
metadata.event_type
Mapped to a UDM event type based on logic. Also used in nested
events
field.
event_type
metadata.product_event_type
Direct mapping.
event_type
security_result.threat_name
Direct mapping.
events
Nested Events
Fields within the
events
array are mapped to corresponding UDM fields within nested
events
objects.  See individual field mappings for details.
external_id
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fileId
target.resource.attribute.labels
Creates a label with key "fileId" and value from the log field.
fileHash
target.file.sha256
Converted to lowercase. Sets
metadata.event_type
to FILE_UNCATEGORIZED.
filePath
target.file.full_path
Direct mapping. Sets
metadata.event_type
to FILE_UNCATEGORIZED.
fw_app_category
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_app_id
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_app_subcategory
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_app_technology
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_device_name
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_email_recipient
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_email_sender
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_email_subject
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_interface_from
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_interface_to
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_is_phishing
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_misc
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_rule
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_rule_id
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_serial_number
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_url_domain
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_vsys
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
fw_xff
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
host_ip
principal.ip
Split by comma and merged into the
principal.ip
array.
host_ip
principal.asset.ip
Split by comma and merged into the
principal.asset.ip
array.
host_name
principal.hostname
Direct mapping.
host_name
principal.asset.hostname
Direct mapping.
hosts
target.hostname
Extracts hostname from the first element of the
hosts
array.
hosts
target.asset.hostname
Extracts hostname from the first element of the
hosts
array.
hosts
target.user.employee_id
Extracts user ID from the first element of the
hosts
array.
incident_id
metadata.product_log_id
Direct mapping.
is_whitelisted
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
local_insert_ts
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
mac
principal.mac
Split by comma and merged into the
principal.mac
array.
matching_status
Not Mapped
Although present in the raw log, this field is not mapped to the IDM object in the final UDM.
metadata.description
security_result.description
Used if
event_type
is GENERIC_EVENT.
metadata.event_type
metadata.event_type
Set based on logic using
event_type
,
host_ip
, and other fields.
metadata.log_type
metadata.log_type
Set to "CORTEX_XDR".
metadata.product_name
metadata.product_name
Set to "Cortex".
metadata.vendor_name
metadata.vendor_name
Set to "Palo Alto Networks".
msg
security_result.description
Direct mapping.
name
security_result.summary
Direct mapping.
PanOSDGHierarchyLevel1
security_result.detection_fields
Creates a key-value pair in
security_result.detection_fields
with key "PanOSDGHierarchyLevel1" and value from the log field.
PanOSDestinationLocation
target.location.country_or_region
Direct mapping.
PanOSDynamicUserGroupName
principal.group.group_display_name
Direct mapping if not empty or "-".
PanOSSourceLocation
principal.location.country_or_region
Direct mapping.
PanOSThreatCategory
security_result.category_details
Merged into the
security_result.category_details
field.
PanOSThreatID
security_result.threat_id
Direct mapping.
principal.asset.attribute.labels
principal.asset.attribute.labels
Creates a label with key "Source" and value from the
source
field.
proto
network.ip_protocol
Converted to uppercase. Sets
metadata.event_type
to NETWORK_CONNECTION.
request
network.http.referral_url
Direct mapping.
rt
metadata.event_timestamp
Converted to timestamp.
security_result.severity
security_result.severity
Set to uppercase value of
severity
.
severity
security_result.severity
Converted to uppercase.
shost
principal.hostname
Direct mapping. Sets
metadata.event_type
to STATUS_UPDATE.
shost
principal.asset.hostname
Direct mapping. Sets
metadata.event_type
to STATUS_UPDATE.
source
principal.asset.attribute.labels
Used as the value for the "Source" label.
source
security_result.summary
Used if
not_json
and
grok
filter matches.
sourceTranslatedAddress
principal.ip
Merged into the
principal.ip
array.
sourceTranslatedAddress
principal.asset.ip
Merged into the
principal.asset.ip
array.
sourceTranslatedPort
principal.port
Converted to integer if not empty or -1.
spt
principal.port
Converted to integer.
sr_summary
security_result.summary
Used if
not_json
and
grok
filter matches.
src
principal.ip
Merged into the
principal.ip
array.
src
principal.asset.ip
Merged into the
principal.asset.ip
array.
suser
principal.user.user_display_name
Direct mapping.
tenantCDLid
additional.fields
Creates a key-value pair in
additional.fields
with key "tenantCDLid" and string value from the log field.
tenantname
additional.fields
Creates a key-value pair in
additional.fields
with key "tenantname" and string value from the log field.
users
target.user.userid
Uses the first element of the
users
array.
xdr_url
metadata.url_back_to_product
Direct mapping.
Need more help?
Get answers from Community members and Google SecOps professionals.
