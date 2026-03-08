# Collect Azure Storage Audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-storage-audit/  
**Scraped:** 2026-03-05T09:20:12.611518Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure Storage Audit logs
Supported in:
Google secops
SIEM
This document explains how to export Azure Storage Audit logs to Google Security Operations using an Azure Storage Account. The parser processes logs in JSON format, transforming them into the Unified Data Model (UDM). It extracts fields from the raw log, performs data type conversions, enriches the data with additional context (like user agent parsing and IP address breakdown), and maps the extracted fields to the corresponding UDM fields.
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
How to configure Log Export for Azure Storage Audit Logs
Sign in to the
Azure Portal
using your privileged account.
Go to
Storage Accounts
>
Diagnostic Settings
.
Click
+ Add diagnostic setting
.
Select the diagnostic settings for
blob
,
queue
,
table
and
file
.
Select the
allLogs
option in
Category groups
for each diagnostic setting.
Enter a descriptive name for each diagnostic setting.
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
How to set up the Azure storage audit feed
Click the
Azure Platform
pack.
Locate the
Azure Storage Audit
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
callerIpAddress
principal.asset.ip
The IP address is extracted from the
callerIpAddress
field using a grok pattern and assigned to
principal.asset.ip
.
callerIpAddress
principal.ip
The IP address is extracted from the
callerIpAddress
field using a grok pattern and assigned to
principal.ip
.
callerIpAddress
principal.port
The port number is extracted from the
callerIpAddress
field using a grok pattern and assigned to
principal.port
.
category
security_result.category_details
The value of the
category
field is assigned to
security_result.category_details
.
correlationId
security_result.detection_fields[0].key
The literal string
correlationId
is assigned to the key field.
correlationId
security_result.detection_fields[0].value
The value of the
correlationId
field is assigned to
security_result.detection_fields[0].value
. The value of the
time
field is parsed as a timestamp and assigned to
event.idm.read_only_udm.metadata.event_timestamp
.  If
category
is
StorageWrite
and
principal.user.userid
exists (derived from
properties.accountName
), the value is set to
USER_RESOURCE_UPDATE_CONTENT
. If
category
is
StorageDelete
and
principal.user.userid
exists, the value is set to
USER_RESOURCE_DELETION
. Otherwise, the value is set to
USER_RESOURCE_ACCESS
. The literal string
AZURE_STORAGE_AUDIT
is assigned to
event.idm.read_only_udm.metadata.log_type
. The literal string
AZURE_STORAGE_AUDIT
is assigned to
event.idm.read_only_udm.metadata.product_name
. The value of the
schemaVersion
field is assigned to
event.idm.read_only_udm.metadata.product_version
. The literal string
AZURE_STORAGE_AUDIT
is assigned to
event.idm.read_only_udm.metadata.vendor_name
.
location
target.location.name
The value of the
location
field is assigned to
target.location.name
.
operationName
additional.fields[x].key
The literal string
operationName
is assigned to the key field.
operationName
additional.fields[x].value.string_value
The value of the
operationName
field is assigned to
additional.fields[x].value.string_value
.
operationVersion
additional.fields[x].key
The literal string
operationVersion
is assigned to the key field.
operationVersion
additional.fields[x].value.string_value
The value of the
operationVersion
field is assigned to
additional.fields[x].value.string_value
.
properties.accountName
principal.user.userid
The value of the
properties.accountName
field is assigned to
principal.user.userid
.
properties.clientRequestId
additional.fields[x].key
The literal string
clientRequestId
is assigned to the key field.
properties.clientRequestId
additional.fields[x].value.string_value
The value of the
properties.clientRequestId
field is assigned to
additional.fields[x].value.string_value
.
properties.etag
additional.fields[x].key
The literal string
etag
is assigned to the key field.
properties.etag
additional.fields[x].value.string_value
The value of the
properties.etag
field is assigned to
additional.fields[x].value.string_value
.
properties.objectKey
additional.fields[x].key
The literal string
objectKey
is assigned to the key field.
properties.objectKey
additional.fields[x].value.string_value
The value of the
properties.objectKey
field is assigned to
additional.fields[x].value.string_value
.
properties.requestMd5
additional.fields[x].key
The literal string
requestMd5
is assigned to the key field.
properties.requestMd5
additional.fields[x].value.string_value
The value of the
properties.requestMd5
field is assigned to
additional.fields[x].value.string_value
.
properties.responseMd5
additional.fields[x].key
The literal string
responseMd5
is assigned to the key field.
properties.responseMd5
additional.fields[x].value.string_value
The value of the
properties.responseMd5
field is assigned to
additional.fields[x].value.string_value
.
properties.serviceType
additional.fields[x].key
The literal string
serviceType
is assigned to the key field.
properties.serviceType
additional.fields[x].value.string_value
The value of the
properties.serviceType
field is assigned to
additional.fields[x].value.string_value
.
properties.tlsVersion
network.tls.version
The value of the
properties.tlsVersion
field is assigned to
network.tls.version
.
properties.userAgentHeader
network.http.parsed_user_agent
The value of the
properties.userAgentHeader
field is parsed as a user agent string and assigned to
network.http.parsed_user_agent
.
properties.userAgentHeader
network.http.user_agent
The value of the
properties.userAgentHeader
field is assigned to
network.http.user_agent
.
protocol
network.application_protocol
The value of the
protocol
field is assigned to
network.application_protocol
.
resourceId
target.resource.id
The value of the
resourceId
field is assigned to
target.resource.id
.
resourceId
target.resource.product_object_id
The value of the
resourceId
field is assigned to
target.resource.product_object_id
. The literal string
DATABASE
is assigned to
target.resource.resource_type
.
resourceType
additional.fields[x].key
The literal string
resourceType
is assigned to the key field.
resourceType
additional.fields[x].value.string_value
The value of the
resourceType
field is assigned to
additional.fields[x].value.string_value
. If
statusText
is
Success
, the value is set to
ALLOW
.
statusCode
network.http.response_code
The value of the
statusCode
field is converted to an integer and assigned to
network.http.response_code
. The literal string
MICROSOFT_AZURE
is assigned to
target.cloud.environment
.
time
timestamp
The value of the
time
field is parsed as a timestamp and assigned to
timestamp
.
uri
network.http.referral_url
The value of the
uri
field is assigned to
network.http.referral_url
.
Need more help?
Get answers from Community members and Google SecOps professionals.
