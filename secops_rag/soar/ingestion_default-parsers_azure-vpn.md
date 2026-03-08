# Collect Azure VPN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-vpn/  
**Scraped:** 2026-03-05T09:51:06.198003Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure VPN logs
Supported in:
Google secops
SIEM
This guide explains how to export Azure VPN logs to Google Security Operations using an Azure Storage Account. The parser extracts fields from JSON-formatted Azure VPN logs and then uses Grok patterns to extract further details from the
properties.message
field. Finally, it maps the extracted information to the standardized fields of the Unified Data Model (UDM).
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
How to configure Log Export for Azure VPN Gateway Logs
Sign in to the
Azure Portal
using your privileged account.
Select the
Subscription
being monitored.
In the resource list of that subscription, locate the VPN gateway (this should typically be of the Resource Type, Virtual Network Gateway).
Click the Gateway.
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
How to set up the Azure VPN feed
Click the
Azure Platform
pack.
Locate the
Azure VPN
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
category
security_result.category_details
Directly mapped from the
category
field in the raw log.
IV_PLAT
security_result.detection_fields.value
Directly mapped from the
IV_PLAT
field in the raw log. Part of a key-value pair within the detection_fields array, where the key is
IV_PLAT
.
IV_PLAT_VER
security_result.detection_fields.value
Directly mapped from the
IV_PLAT_VER
field in the raw log. Part of a key-value pair within the detection_fields array, where the key is
IV_PLAT_VER
.
IV_PROTO
security_result.detection_fields.value
Directly mapped from the
IV_PROTO
field in the raw log. Part of a key-value pair within the detection_fields array, where the key is
IV_PROTO
.
IV_VER
security_result.detection_fields.value
Directly mapped from the
IV_VER
field in the raw log. Part of a key-value pair within the detection_fields array, where the key is
IV_VER
.
level
security_result.severity
Mapped from the
level
field in the raw log. If
level
is
Informational
, the
severity
is set to
INFORMATIONAL
.
local_ip
target.ip
Extracted from the
properties.message
field using grok patterns and mapped to the target IP address.
local_port
target.port
Extracted from the
properties.message
field using grok patterns and mapped to the target port number. Converted to integer type.
operationName
metadata.product_event_type
Directly mapped from the
operationName
field in the raw log.
properties.message
metadata.description
Extracted from the
properties.message
field using grok patterns. Depending on the message format, the description might include additional details extracted from
desc2
field.
remote_ip
principal.ip
Extracted from the
properties.message
field using grok patterns and mapped to the principal IP address.
remote_port
principal.port
Extracted from the
properties.message
field using grok patterns and mapped to the principal port number. Converted to integer type.
resourceid
target.resource.product_object_id
Directly mapped from the
resourceid
field in the raw log.
time
timestamp, metadata.event_timestamp
Parsed from the
time
field in the raw log using the RFC 3339 format and mapped to both the event timestamp and the UDM timestamp.
metadata.log_type
Hardcoded to
AZURE_VPN
.
metadata.vendor_name
Hardcoded to
AZURE
.
metadata.product_name
Hardcoded to
VPN
.
metadata.event_type
Dynamically set based on the presence of IP addresses. If both
remote_ip
and
local_ip
are present, it's set to
NETWORK_CONNECTION
, otherwise
USER_RESOURCE_ACCESS
.
extensions.auth.type
Hardcoded to
VPN
.
Need more help?
Get answers from Community members and Google SecOps professionals.
