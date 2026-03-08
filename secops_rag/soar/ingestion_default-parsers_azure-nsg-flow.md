# Collect Azure NSG Flow logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-nsg-flow/  
**Scraped:** 2026-03-05T09:51:03.859830Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure NSG Flow logs
Supported in:
Google secops
SIEM
This document describes how to collect Microsoft Azure NSG Flow logs by setting up a Google Security Operations feed using Microsoft Azure Blob Storage V2.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to
Microsoft Azure
portal with permissions to:
Create Storage Accounts
Configure Network Security Groups (NSGs)
Configure Network Watcher
Manage access keys
Azure subscription with Network Watcher enabled in the regions where your NSGs are located
Configure Azure Storage Account
To store and organize the log data collected from Azure, you must set up a 
storage account and retrieve the necessary connection credentials for 
Google SecOps.
Create Storage Account
In the
Azure portal
, search for
Storage accounts
.
Click
+ Create
.
Provide the following configuration details:
Setting
Value
Subscription
Select your Azure subscription
Resource group
Select existing or create new
Storage account name
Enter a unique name (for example,
nsgflowlogs
)
Region
Select the region (for example,
East US
)
Performance
Standard (recommended)
Redundancy
GRS (Geo-redundant storage) or LRS (Locally redundant storage)
Click
Review + create
.
Review the overview of the account and click
Create
.
Wait for the deployment to complete.
Get Storage Account credentials
Go to the
Storage Account
you just created.
Select
Security + networking
>
Access keys
.
Click
Show keys
.
Copy and save the following for later use:
Storage account name
:
nsgflowlogs
Key 1
or
Key 2
: The shared access key (a 512-bit random string in base64 encoding)
Get Blob Service endpoint
In the same Storage Account, select
Endpoints
.
Copy and save the
Blob service
endpoint URL.
Example:
https://nsgflowlogs.blob.core.windows.net/
Configure Network Security Group Flow Logs
In the
Azure portal
, search for
Network Watcher
.
Select
Logs
>
NSG flow logs
.
Click
+ Create
to create a new flow log.
Provide the following configuration details:
Subscription
: Select your subscription.
Network Security Group
: Select the NSG for which you want to enable flow logs.
Storage Account
: Select the storage account you created earlier.
Retention (days)
: Select the number of days to retain logs (for example, 90 days).
Flow Logs Version
: Select
Version 2
(recommended).
Enable Traffic Analytics
: Optional, enable if you want additional analytics in Azure.
Click
Create
to enable NSG flow logs.
In the
Azure portal
, search for
Network security groups
.
Select the
NSG
you want to configure.
Select
Monitoring
>
Flow logs
.
Click
Create
and follow the same steps as above.
Configure a feed in Google SecOps to ingest Microsoft Azure NSG Flow logs
After configuring your Azure environment, you must create a feed in the 
Google SecOps console to automate the ingestion process.
Set up the feed
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
Azure NSG Flow Logs
).
Select
Microsoft Azure Blob Storage V2
as the
Source type
.
Select
Microsoft Azure NSG Flow
as the
Log type
.
Click
Next
.
Configure feed parameters
Specify values for the following input parameters:
Azure URI
: Enter the
Blob Service endpoint URL
with the container path:
https://<storage-account-name>.blob.core.windows.net/insights-logs-networksecuritygroupflowevent/
Replace the following:
<storage-account-name>
: Your Azure storage account name.
Example:
https://nsgflowlogs.blob.core.windows.net/insights-logs-networksecuritygroupflowevent/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers.
On success
: Deletes all files and empty directories after successful transfer.
Maximum File Age
: Enter the number of days to include files modified within. Default is 180 days.
Shared key
: Enter the shared key value (access key) you captured from the Storage Account.
Asset namespace
: The
asset namespace
.
Ingestion labels
: Labels applied to all events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Configure Azure Storage firewall (if enabled)
If your Azure Storage Account uses a firewall, you must add Google SecOps IP ranges.
In the
Azure portal
, go to your
Storage Account
.
Select
Security + networking
>
Networking
.
Under
Firewalls and virtual networks
, select
Enabled from selected virtual networks and IP addresses
.
In the
Firewall
section, under
Address range
, click
+ Add IP range
.
Add each Google SecOps IP range in CIDR notation.
To get the current IP ranges:
See
IP Allowlisting documentation
Or retrieve them programmatically using the
Feed Management API
Click
Save
.
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. For information about requirements for each feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds,
contact Google Security Operations support
.
UDM mapping table
Log Field
UDM Mapping
Logic
ClientOperationId
udm.additional.fields
Key "ClientOperationId" is set to the value of
ClientOperationId
.
CorrelationRequestId
udm.additional.fields
Key "CorrelationRequestId" is set to the value of
CorrelationRequestId
.
GatewayManagerVersion
udm.additional.fields
Key "GatewayManagerVersion" is set to the value of
GatewayManagerVersion
.
flow_tuple.column9
(
flowstate
)
udm.additional.fields
For version 2 logs, key "flow_state" is set to "BEGIN" if
flowstate
is 'B'/'b', "CONTINUE" if 'C'/'c', or "END" if 'E'/'e'.
properties.addressfamily
udm.additional.fields
Key "Address Family" is set to the value of
properties.addressfamily
.
properties.locprf
udm.additional.fields
Key "Local Pref" is set to the value of
properties.locprf
.
properties.path
udm.additional.fields
Key "Path" is set to the value of
properties.path
.
properties.peeringType
udm.additional.fields
Key "Peering Type" is set to the value of
properties.peeringType
.
properties.weight
udm.additional.fields
Key "Weight" is set to the value of
properties.weight
.
flow_tuple.column1
udm.metadata.collected_timestamp
Value taken from the first column of the CSV
flowtupleValue
and converted from UNIX epoch.
record.time
/
time
udm.metadata.event_timestamp
Value taken from
record.time
(for
records
array events) or
time
(for other events) and parsed.
udm.metadata.event_type
Set to
NETWORK_FLOW
if both principal and target entities are identified, or for all inner flow tuple events. Set to
STATUS_UPDATE
if only a principal is identified. Otherwise, set to
GENERIC_EVENT
.
record.operationName
/
operationName
udm.metadata.product_event_type
Value taken from
record.operationName
or
operationName
.
record.flowLogGUID
udm.metadata.product_log_id
Value taken from
record.flowLogGUID
.
record.flowLogVersion
/
record.properties.Version
/
version
udm.metadata.product_version
Value taken from
record.flowLogVersion
,
record.properties.Version
(via the
version
variable), or the top-level
version
field.
flow_tuple.column7
(
trafficFlow
)
udm.network.direction
Value is
INBOUND
if
trafficFlow
is "I", or
OUTBOUND
if
trafficFlow
is "O".
flow_tuple.column6
(
protocol
)
udm.network.ip_protocol
Value is
TCP
if
protocol
is "T", or
UDP
if
protocol
is "U".
flow_tuple.column11
/
flow_tuple.column13
udm.network.received_bytes
For version 2 logs, if
trafficFlow
is "I", value is taken from
bytesSentSourceToDestinationV2
(column 11). If
trafficFlow
is "O", value is taken from
bytesSentFromDestinationToSourceV2
(column 13).
flow_tuple.column11
/
flow_tuple.column13
udm.network.sent_bytes
For version 2 logs, if
trafficFlow
is "I", value is taken from
bytesSentFromDestinationToSourceV2
(column 13). If
trafficFlow
is "O", value is taken from
bytesSentSourceToDestinationV2
(column 11).
properties.deviceName
udm.principal.asset.hostname
Value taken from
properties.deviceName
.
record.properties.primaryIPv4Address
/
properties.primaryIPv4Address
/
SrcIP_s_s
/
properties.network
udm.principal.asset.ip
Value taken from
record.properties.primaryIPv4Address
,
properties.primaryIPv4Address
,
SrcIP_s_s
, or grok-extracted from
properties.network
.
properties.vnetResourceGuid
udm.principal.asset_id
Value is constructed as "vnetResourceGuid: %{properties_vnetResourceGuid}". The GUID is extracted from
properties.vnetResourceGuid
.
properties.deviceName
udm.principal.hostname
Value taken from
properties.deviceName
.
record.properties.primaryIPv4Address
/
flow_tuple.column2
/
properties.primaryIPv4Address
/
SrcIP_s_s
/
properties.network
udm.principal.ip
Value taken from
record.properties.primaryIPv4Address
,
sourceIP
(column 2 of CSV),
properties.primaryIPv4Address
,
SrcIP_s_s
, or grok-extracted from
properties.network
.
record.macAddress
/
record.properties.macAddress
/
properties.macAddress
/
MACAddress_s_s
udm.principal.mac
Value taken from
record.macAddress
,
record.properties.macAddress
,
properties.macAddress
, or
MACAddress_s_s
. Dashes are replaced with colons.
flow_tuple.column4
/
properties.network
udm.principal.port
Value taken from
sourcePort
(column 4 of CSV) or grok-extracted from
properties.network
.
properties.serviceKey
udm.principal.resource.attribute.labels
Key "Service Key" is set to the value of
properties.serviceKey
.
properties.conditions.destinationPortRange
udm.security_result.about.labels
Key "Conditions_destinationPortRange" is set to the value of
properties.conditions.destinationPortRange
.
properties.conditions.sourcePortRange
udm.security_result.about.labels
Key "Conditions_sourcePortRange" is set to the value of
properties.conditions.sourcePortRange
.
record.properties.direction
/
properties.direction
udm.security_result.about.labels
Key "Direction" is set to the value of
record.properties.direction
or
properties.direction
.
properties.priority
udm.security_result.about.labels
Key "Priority" is set to the value of
properties.priority
.
record.properties.type
/
properties.type
udm.security_result.about.labels
Key "ruleType" is set to the value of
record.properties.type
or
properties.type
.
record.flowLogResourceID
udm.security_result.about.resource.name
Value taken from
record.flowLogResourceID
.
flow_tuple.column8
(
trafficDecision
)
udm.security_result.action
Value is
ALLOW
if
trafficDecision
is "A", or
BLOCK
if
trafficDecision
is "D".
flow.aclID
udm.security_result.detection_fields
Key
aclID[%{Index}]
is set to the value of
flow.aclID
.
flowGroup.flowTuples
udm.security_result.detection_fields
Key
flowTuple[%{Index}][%{Index1}][%{Index2}]
is set to the value of the flow tuple string.
flowGroup.rule
udm.security_result.detection_fields
Key
rule[%{Index}][%{Index1}]
is set to the value of
flowGroup.rule
.
record.properties.ruleName
/
flow.rule
/
properties.ruleName
udm.security_result.rule_name
Value taken from
record.properties.ruleName
,
flow.rule
, or
properties.ruleName
.
record.category
/
category
udm.security_result.rule_type
Value taken from
record.category
or
category
.
level
udm.security_result.severity
Set to
INFORMATIONAL
if
level
contains "Info".
record.resourceId
/
resourceId
udm.target.application
Value taken from the
appname
field, which is grok-extracted from
record.resourceId
or
resourceId
.
properties.nexthop
/
DestIP_s_s
udm.target.asset.ip
Value taken from
DestIP_s_s
or grok-extracted from
properties.nexthop
.
record.systemId
/
systemId
udm.target.asset_id
Value is constructed as "System Id: %{systemId}".
udm.target.cloud.environment
Set to
MICROSOFT_AZURE
.
flow_tuple.column3
/
properties.nexthop
/
DestIP_s_s
udm.target.ip
Value taken from
destinationIP
(column 3 of CSV),
DestIP_s_s
, or grok-extracted from
properties.nexthop
.
flowTuple.mac
udm.target.mac
Value taken from
flowTuple.mac
and formatted with colons.
flow_tuple.column5
/
DestPort_d_d
udm.target.port
Value taken from
destinationPort
(column 5 of CSV) or
DestPort_d_d
.
record.resourceId
/
resourceId
udm.target.resource.attribute.labels
Key "NSG Name" is set to the value of
rscname
, grok-extracted from the resource ID.
record.resourceId
/
resourceId
udm.target.resource.attribute.labels
Key "Resource Group" is set to the value of
rscgrp
, grok-extracted from the resource ID.
record.resourceId
/
resourceId
udm.target.resource.attribute.labels
Key "Subcription Id" is set to the value of
subcriptionid
, grok-extracted from the resource ID.
record.resourceId
/
resourceid
udm.target.resource.product_object_id
Value taken from
record.resourceId
or
resourceid
.
udm.target.resource.resource_type
Set to
STORAGE_BUCKET
.
udm.metadata.product_name
Set to
Azure NSG Flow
.
udm.metadata.vendor_name
Set to
Microsoft
.
Need more help?
Get answers from Community members and Google SecOps professionals.
