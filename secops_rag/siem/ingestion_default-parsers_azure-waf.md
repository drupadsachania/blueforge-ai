# Collect Azure WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-waf/  
**Scraped:** 2026-03-05T09:20:15.732501Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure WAF logs
Supported in:
Google secops
SIEM
This document explains how to export Azure Web Application Firewall (WAF) logs to Google Security Operations using an Azure Storage Account. The parser handles logs in JSON format, transforming them into UDM. It processes logs containing a
records
array by iterating through each record and mapping specific fields to UDM properties. If the
records
array is absent, the parser handles the log as a single event, extracting and mapping fields accordingly.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
An active Azure tenant
Privileged access to Azure
Configure Azure Storage Account
In the Azure console, search for
Storage accounts
.
Click
Create
.
Specify values for the following input parameters:
Subscription
: Select the subscription.
Resource Group
: Select the resource group.
Region
: Select the region.
Performance
: Select the performance (Standard recommended).
Redundancy
: Select the redundancy (GRS or LRS recommended).
Storage account name
: Enter a name for the new storage account.
Click
Review + create
.
Review the overview of the account and click
Create
.
From the
Storage Account Overview
page, select the
Access keys
submenu in
Security + networking
.
Click
Show
next to
key1
or
key2
.
Click
Copy to clipboard
to copy the key.
Save the key in a secure location for later use.
From the
Storage Account Overview
page, select the
Endpoints
submenu in
Settings
.
Click
Copy to clipboard
to copy the
Blob service
endpoint URL; for example,
https://<storageaccountname>.blob.core.windows.net
.
Save the endpoint URL in a secure location for later use.
How to configure Log Export for Azure WAF Logs
Sign in to the
Azure Portal
using your privileged account.
Go to
Web Application Firewall (WAF) rules
and select a WAF to monitor.
Select
Monitoring
>
Diagnostic Settings
.
Click
+ Add diagnostic setting
.
Enter a descriptive name for the diagnostic setting.
Select
allLogs
.
Select the
Archive to a storage account
checkbox as the destination.
Specify the
Subscription
and
Storage Account
.
Click
Save
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the Azure WAF feed
Click the
Azure Platform
pack.
Locate the
Azure WAF
log type and click
Add new feed
.
Specify values for the following fields:
Source Type
: Microsoft Azure Blob Storage V2.
Azure URI
: The blob endpoint URL.
ENDPOINT_URL/BLOB_NAME
Replace the following:
ENDPOINT_URL
: The blob endpoint URL (
https://<storageaccountname>.blob.core.windows.net
)
BLOB_NAME
: The name of the blob (such as,
<logname>-logs
)
Source deletion options
: Select the deletion option according to your ingestion preferences.
Note: If you select the
Delete transferred files
or
Delete transferred files and empty directories
option, make sure that you granted appropriate permissions to the service account.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Shared key
: The access key to the Azure Blob Storage.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
:
Namespace associated with the feed
.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
backendPoolName
additional.fields[?key=='backendPoolName'].value.string_value
The value is taken from the
backendPoolName
field in the raw log.
backendSettingName
additional.fields[?key=='backendSettingName'].value.string_value
The value is taken from the
backendSettingName
field in the raw log.
category
metadata.product_event_type
The value is taken from the
category
field in the raw log.
EventEnqueuedUtcTime
additional.fields[?key=='EventEnqueuedUtcTime'].value.string_value
The value is taken from the
EventEnqueuedUtcTime
field in the raw log when
records
field exists.
EventProcessedUtcTime
additional.fields[?key=='EventProcessedUtcTime'].value.string_value
The value is taken from the
EventProcessedUtcTime
field in the raw log when
records
field exists.
operationName
additional.fields[?key=='operationName'].value.string_value
The value is taken from the
operationName
field in the raw log.
properties.action
additional.fields[?key=='action'].value.string_value
The value is taken from the
properties.action
field in the raw log when
records
field exists.
properties.action
security_result.action_details
The value is taken from the
properties.action
field in the raw log when
records
field does not exist.
properties.clientIP
,
properties.clientIp
principal.asset.ip
,
principal.ip
The value is taken from either the
properties.clientIP
or
properties.clientIp
field in the raw log, prioritizing
clientIP
.
properties.clientPort
principal.port
The value is taken from the
properties.clientPort
field in the raw log.
properties.clientResponseTime
principal.resource.attribute.labels[?key=='Client Response Time'].value
The value is taken from the
properties.clientResponseTime
field in the raw log when
records
field does not exist.
properties.details.data
additional.fields[?key=='Properties data'].value.string_value
The value is taken from the
properties.details.data
field in the raw log when
records
field exists.
properties.details.file
principal.process.file.full_path
The value is taken from the
properties.details.file
field in the raw log when
records
field does not exist.
properties.details.matches[].matchVariableName
,
properties.details.matches[].matchVariableValue
additional.fields[?key.startsWith('%{idx} ')].value.string_value
The value is taken from the
properties.details.matches
array in the raw log. The
key
in the UDM is constructed using the index (
idx
) and
matchVariableName
. The
value
is taken from
matchVariableValue
.
properties.details.message
metadata.description
The value is taken from the
properties.details.message
field in the raw log after removing backslashes and quotes.
properties.details.msg
metadata.description
The value is taken from the
properties.details.msg
field in the raw log when
records
field exists.
properties.httpMethod
network.http.method
The value is taken from the
properties.httpMethod
field in the raw log.
properties.httpStatus
network.http.response_code
The value is taken from the
properties.httpStatus
field in the raw log.
properties.httpVersion
network.application_protocol
If the
properties.httpVersion
field contains
HTTP
, the value
HTTP
is assigned.
properties.host
,
properties.hostname
,
properties.originalHost
principal.asset.hostname
,
principal.hostname
The value is taken from one of
properties.originalHost
,
properties.host
, or
properties.hostname
, prioritizing them in that order.
properties.policyId
security_result.detection_fields[?key=='policyId'].value
The value is taken from the
properties.policyId
field in the raw log.
properties.policyMode
security_result.detection_fields[?key=='policyMode'].value
The value is taken from the
properties.policyMode
field in the raw log when
records
field exists.
properties.policy
additional.fields[?key=='Properties policy'].value.string_value
The value is taken from the
properties.policy
field in the raw log when
records
field exists.
properties.receivedBytes
network.received_bytes
The value is taken from the
properties.receivedBytes
field in the raw log.
properties.requestUri
target.url
The value is taken from the
properties.requestUri
field in the raw log.
properties.ruleId
security_result.rule_id
The value is taken from the
properties.ruleId
field in the raw log.
properties.ruleName
security_result.rule_name
The value is taken from the
properties.ruleName
field in the raw log when
records
field exists.
properties.ruleName
,
ruleSetType
security_result.rule_name
The value is taken from the
properties.ruleName
field, or if empty, from the
ruleSetType
field in the raw log when
records
field does not exist.
properties.ruleSetVersion
security_result.detection_fields[?key=='ruleSetVersion'].value
The value is taken from the
properties.ruleSetVersion
field in the raw log.
properties.sentBytes
network.sent_bytes
The value is taken from the
properties.sentBytes
field in the raw log.
properties.serverResponseLatency
additional.fields[?key=='Server Response Latency'].value.string_value
The value is taken from the
properties.serverResponseLatency
field in the raw log when
records
field does not exist.
properties.serverRouted
target.asset.ip
,
target.ip
,
target.port
The IP and port are extracted from the
properties.serverRouted
field.
properties.sslCipher
network.tls.cipher
The value is taken from the
properties.sslCipher
field in the raw log.
properties.sslClientCertificateIssuerName
network.tls.server.certificate.issuer
The value is taken from the
properties.sslClientCertificateIssuerName
field in the raw log.
properties.sslProtocol
network.tls.version
The value is taken from the
properties.sslProtocol
field in the raw log.
properties.timeTaken
additional.fields[?key=='Properties Timetaken'].value.string_value
The value is taken from the
properties.timeTaken
field in the raw log when
records
field does not exist.
properties.trackingReference
additional.fields[?key=='trackingReference'].value.string_value
The value is taken from the
properties.trackingReference
field in the raw log when
records
field exists.
properties.transactionId
network.session_id
The value is taken from the
properties.transactionId
field in the raw log.
properties.userAgent
network.http.user_agent
The value is taken from the
properties.userAgent
field in the raw log.
properties.WAFEvaluationTime
additional.fields[?key=='Properties WAFEvaluationTime'].value.string_value
The value is taken from the
properties.WAFEvaluationTime
field in the raw log when
records
field does not exist.
properties.WAFMode
additional.fields[?key=='Properties WAFMode'].value.string_value
The value is taken from the
properties.WAFMode
field in the raw log when
records
field does not exist.
rec.category
metadata.product_event_type
The value is taken from the
rec.category
field in the raw log when
records
field exists.
rec.operationName
additional.fields[?key=='operationName'].value.string_value
The value is taken from the
rec.operationName
field in the raw log when
records
field exists.
rec.properties.clientIP
,
rec.properties.clientIp
principal.asset.ip
,
principal.ip
The value is taken from either the
rec.properties.clientIP
or
rec.properties.clientIp
field in the raw log, prioritizing
clientIP
when
records
field exists.
rec.properties.clientPort
principal.port
The value is taken from the
rec.properties.clientPort
field in the raw log when
records
field exists.
rec.properties.host
principal.asset.hostname
,
principal.hostname
The value is taken from the
rec.properties.host
field in the raw log when
records
field exists.
rec.properties.policy
additional.fields[?key=='Properties policy'].value.string_value
The value is taken from the
rec.properties.policy
field in the raw log when
records
field exists.
rec.properties.requestUri
target.url
The value is taken from the
rec.properties.requestUri
field in the raw log when
records
field exists.
rec.properties.ruleName
security_result.rule_name
The value is taken from the
rec.properties.ruleName
field in the raw log when
records
field exists.
rec.properties.trackingReference
additional.fields[?key=='trackingReference'].value.string_value
The value is taken from the
rec.properties.trackingReference
field in the raw log when
records
field exists.
rec.resourceId
target.resource.id
The value is taken from the
rec.resourceId
field in the raw log when
records
field exists.
rec.time
metadata.event_timestamp
The value is taken from the
rec.time
field in the raw log when
records
field exists.
resourceId
target.resource.id
The value is taken from the
resourceId
field in the raw log when
records
field does not exist.
timeStamp
metadata.event_timestamp
The value is taken from the
timeStamp
field in the raw log when
records
field does not exist.
N/A
metadata.event_type
The value is set to
NETWORK_CONNECTION
if both principal (hostname or client IP) and destination IP are present. It's set to
STATUS_UPDATE
if a principal is present but destination IP is missing. Otherwise, it defaults to
GENERIC_EVENT
or the value of the
event_type
field.
N/A
metadata.log_type
The value is hardcoded to
AZURE_WAF
.
N/A
metadata.product_name
The value is hardcoded to
Azure WAF Logs
.
N/A
metadata.vendor_name
The value is hardcoded to
Microsoft
.
N/A
security_result.action
The value is set to
ALLOW
if
properties.action
is
Matched
,
BLOCK
if
properties.action
is
Block
.
Need more help?
Get answers from Community members and Google SecOps professionals.
