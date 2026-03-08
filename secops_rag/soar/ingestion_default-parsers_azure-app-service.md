# Collect Azure APP Service logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-app-service/  
**Scraped:** 2026-03-05T09:50:59.815203Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure APP Service logs
Supported in:
Google secops
SIEM
This document explains how to export Azure APP Service logs to Google Security Operations using an Azure Storage Account. The parser transforms raw JSON formatted Azure App Service logs into a structured Unified Data Model (UDM). It extracts relevant fields from the raw logs, performs data cleaning and normalization, and maps the extracted information to corresponding UDM fields, ultimately outputting a UDM-compliant JSON object for each log entry.
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
How to configure Log Export for Azure APP Service Logs
Sign in to the
Azure Portal
using your privileged account.
Go to
App Services
and select the required app service in use.
Select
Monitoring
>
App Service Logs
.
Turn
ON
for
Application Logging (blob)
.
Select
Storage
under
Web Service Logging
.
Select the
Subscription
and
Storage Account
.
Define the
Retention Period
and
Quota
according to your requirements.
Turn
ON
for
Detailed error messages
.
Turn
ON
for
Failed request tracing
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
How to set up the Azure App Service feed
Click the
Azure Platform
pack.
Locate the
Azure App Service
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
AppRoleInstance
read_only_udm.principal.resource.product_object_id
Direct mapping
AppRoleName
read_only_udm.principal.resource.name
Direct mapping
AppVersion
read_only_udm.principal.resource.attribute.labels.value
Direct mapping
Category
read_only_udm.metadata.product_event_type
Direct mapping
CIp
read_only_udm.target.asset.ip
Direct mapping
CIp
read_only_udm.target.ip
Direct mapping
ClientCity
read_only_udm.principal.location.city
Direct mapping
ClientCountryOrRegion
read_only_udm.principal.location.country_or_region
Direct mapping
ClientIP
read_only_udm.principal.asset.ip
Direct mapping
ClientIP
read_only_udm.principal.ip
Direct mapping
ClientStateOrProvince
read_only_udm.principal.location.state
Direct mapping
ClientType
read_only_udm.additional.fields.value.string_value
Direct mapping
ComputerName
read_only_udm.principal.asset.hostname
Direct mapping
ComputerName
read_only_udm.principal.hostname
Direct mapping
Cookie
read_only_udm.principal.resource.attribute.labels.value
Direct mapping
CsBytes
read_only_udm.network.sent_bytes
Renamed from CsBytes
CsHost
read_only_udm.additional.fields.value.string_value
Direct mapping
CsMethod
read_only_udm.network.http.method
Direct mapping
CsUriQuery
read_only_udm.principal.resource.attribute.labels.value
Direct mapping
CsUriStem
read_only_udm.additional.fields.value.string_value
Direct mapping
CsUriStem
read_only_udm.target.url
Direct mapping
CsUsername
read_only_udm.principal.user.user_display_name
Direct mapping
EventIpAddress
read_only_udm.principal.asset.ip
Direct mapping
EventIpAddress
read_only_udm.principal.ip
Direct mapping
EventPrimaryStampName
read_only_udm.additional.fields.value.string_value
Direct mapping
EventStampName
read_only_udm.additional.fields.value.string_value
Direct mapping
EventStampType
read_only_udm.additional.fields.value.string_value
Direct mapping
Host
read_only_udm.principal.asset.hostname
Direct mapping
Host
read_only_udm.principal.hostname
Direct mapping
IKey
read_only_udm.target.resource.attribute.labels.value
Direct mapping
Instance
read_only_udm.additional.fields.value.string_value
Direct mapping
Name
read_only_udm.additional.fields.value.string_value
Direct mapping
Protocol
read_only_udm.additional.fields.value.string_value
Direct mapping
Protocol
read_only_udm.network.application_protocol
Mapped to
HTTP
if Protocol is
HTTP/1.1
Referer
read_only_udm.network.http.referral_url
Direct mapping
ResourceGUID
read_only_udm.target.resource.product_object_id
Renamed from ResourceGUID
SDKVersion
read_only_udm.additional.fields.value.string_value
Direct mapping
SDKVersion
read_only_udm.principal.resource.attribute.labels.value
Direct mapping
SPort
read_only_udm.principal.port
Renamed from SPort
ScBytes
read_only_udm.network.received_bytes
Renamed from ScBytes
ScStatus
read_only_udm.network.http.response_code
Renamed from ScStatus
TimeTaken
read_only_udm.additional.fields.value.string_value
Direct mapping
Type
read_only_udm.additional.fields.value.string_value
Direct mapping
User
read_only_udm.principal.user.userid
Direct mapping
UserAddress
read_only_udm.principal.asset.ip
Extracted from UserAddress if it's a valid IP address
UserAddress
read_only_udm.principal.ip
Extracted from UserAddress if it's a valid IP address
UserAgent
read_only_udm.network.http.user_agent
Direct mapping
UserDisplayName
read_only_udm.principal.user.user_display_name
Direct mapping
category
read_only_udm.metadata.product_event_type
Direct mapping
level
read_only_udm.security_result.severity
Uppercased and renamed from level
location
read_only_udm.principal.location.name
Direct mapping
operationName
read_only_udm.additional.fields.value.string_value
Direct mapping
record.properties.Protocol
read_only_udm.additional.fields.value.string_value
Direct mapping
record.properties.Result
read_only_udm.security_result.summary
Direct mapping
record.time
read_only_udm.metadata.event_timestamp
Parsed as RFC 3339 timestamp
resourceId
read_only_udm.target.resource.attribute.labels.value
Direct mapping
resourceId
read_only_udm.target.resource.product_object_id
Renamed from resourceId
read_only_udm.metadata.event_type
Determined based on the presence of principal, target, and Protocol. Set to
NETWORK_HTTP
if principal, target, and Protocol=
HTTP
are present. Set to
NETWORK_CONNECTION
if principal and target are present. Set to
STATUS_UPDATE
if only principal is present. Otherwise, set to
GENERIC_EVENT
.
Need more help?
Get answers from Community members and Google SecOps professionals.
