# Collect Azure Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-firewall/  
**Scraped:** 2026-03-05T09:20:10.327914Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure Firewall logs
Supported in:
Google secops
SIEM
This document explains how to export Azure Firewall logs to Google Security Operations using Azure Storage Account. The parser first attempts to process the input as JSON, extracting data from the
Records
field. If the
Record
field is empty, the parser then uses a series of Grok patterns and conditional statements to extract relevant fields from the message, handling different formats and variations in the Azure Firewall logs.
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
+ Create
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
How to configure Log Export for Azure Firewalls Logs
Sign in to the
Azure Portal
using your privileged account.
Go to
Firewalls
and select the required firewall.
Select
Monitoring
>
Diagnostic Services
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
How to set up the Azure firewall feed
Click the
Azure Platform
pack.
Locate the
Azure firewall
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
Maximum File Age
: Includes files modified in the last number of days. 
Default is 180 days.
Shared key
: The shared key (a 512-bit random string in base-64 encoding) used to access Azure resources.
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
UDM Mapping
Log field
UDM mapping
Logic
@timestamp
metadata.event_timestamp
Converts the raw log field
@timestamp
to UDM Format.
category
security_result.rule_type
Maps the raw log field
category
to UDM.
operationName
metadata.product_event_type
Maps the raw log field
operationName
to UDM.
properties.Action
security_result.action
Maps the raw log field
properties.Action
to UDM, converting
ALLOW
to
ALLOW
,
DENY
to
BLOCK
, and any other value to
UNKNOWN_ACTION
.
properties.DestinationIp
target.ip
Maps the raw log field
properties.DestinationIp
to UDM.
properties.DestinationPort
target.port
Maps the raw log field
properties.DestinationPort
to UDM.
properties.DnssecOkBit
additional.fields.value.bool_value
Maps the raw log field
properties.DnssecOkBit
to UDM.
properties.EDNS0BufferSize
additional.fields.value.number_value
Maps the raw log field
properties.EDNS0BufferSize
to UDM.
properties.ErrorMessage
additional.fields.value.string_value
Maps the raw log field
properties.ErrorMessage
to UDM.
properties.ErrorNumber
additional.fields.value.number_value
Maps the raw log field
properties.ErrorNumber
to UDM.
properties.Policy
security_result.detection_fields.value
Maps the raw log field
properties.Policy
to UDM.
properties.Protocol
network.ip_protocol
Maps the raw log field
properties.Protocol
to UDM if it's not
HTTPS
or
HTTP
.
properties.Protocol
network.application_protocol
Maps the raw log field
properties.Protocol
to UDM if it's
HTTPS
or
HTTP
.
properties.QueryClass
network.dns.questions.class
Maps the raw log field
properties.QueryClass
to UDM using a lookup table for mapping DNS query classes.
properties.QueryId
network.dns.id
Maps the raw log field
properties.QueryId
to UDM.
properties.QueryName
network.dns.questions.name
Maps the raw log field
properties.QueryName
to UDM.
properties.QueryType
network.dns.questions.type
Maps the raw log field
properties.QueryType
to UDM using a lookup table for mapping DNS record types.
properties.RequestSize
network.sent_bytes
Maps the raw log field
properties.RequestSize
to UDM.
properties.ResponseCode
network.dns.response_code
Maps the raw log field
properties.ResponseCode
to UDM using a lookup table for mapping DNS response codes.
properties.ResponseFlags
additional.fields.value.string_value
Maps the raw log field
properties.ResponseFlags
to UDM.
properties.ResponseSize
network.received_bytes
Maps the raw log field
properties.ResponseSize
to UDM.
properties.Rule
security_result.rule_name
Maps the raw log field
properties.Rule
to UDM.
properties.RuleCollection
security_result.detection_fields.value
Maps the raw log field
properties.RuleCollection
to UDM.
properties.RuleCollectionGroup
security_result.detection_fields.value
Maps the raw log field
properties.RuleCollectionGroup
to UDM.
properties.SourceIp
principal.ip
Maps the raw log field
properties.SourceIp
to UDM.
properties.SourcePort
principal.port
Maps the raw log field
properties.SourcePort
to UDM.
properties.msg
security_result.description
Maps the raw log field
properties.msg
to UDM after extracting other fields from it.
records.category
security_result.rule_type
Maps the raw log field
records.category
to UDM.
records.operationName
metadata.product_event_type
Maps the raw log field
records.operationName
to UDM.
records.properties.msg
This field is used for extracting multiple fields using Grok patterns and doesn't have a direct mapping to UDM.
records.resourceId
metadata.product_log_id
Maps the raw log field
records.resourceId
to UDM.
resourceId
metadata.product_log_id
Maps the raw log field
resourceId
to UDM.
time
metadata.event_timestamp
Converts the raw log field
time
to UDM Format.
metadata.vendor_name
This field is populated by the parser with the value
Microsoft Inc.
.
metadata.product_name
This field is populated by the parser with the value
Azure Firewall Application Rule
.
metadata.log_type
This field is populated by the parser with the value
AZURE_FIREWALL
.
additional.fields.key
This field is populated by the parser with the key for the additional field.
security_result.detection_fields.key
This field is populated by the parser with the key for the detection field.
network.application_protocol
This field is populated by the parser with the value
DNS
for DNS logs.
metadata.event_type
This field is populated by the parser based on the log message. It can be
NETWORK_CONNECTION
,
GENERIC_EVENT
,
STATUS_UPDATE
, or
NETWORK_DNS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
