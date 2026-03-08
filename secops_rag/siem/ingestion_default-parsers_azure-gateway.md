# Collect Azure Application Gateway logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/azure-gateway/  
**Scraped:** 2026-03-05T09:20:06.839692Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Azure Application Gateway logs
Supported in:
Google secops
SIEM
This document explains how to collect Azure Application Gateway logs by setting up a Google Security Operations feed. This parser handles both single and multi-record JSON structures, extracts fields from the "records" array, performs data type conversions, maps fields to the UDM, and enriches the data with metadata and derived fields like network connection type. It also handles specific logic for different
operationName
values, extracting relevant IP addresses, subnets, and other configuration details.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to an Azure subscription
An Azure application gateway environment (tenant) in Azure
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
page, select submenu
Access keys
in
Security + networking
.
Click
Show
next to
key1
or
key2
Click
Copy to clipboard
to copy the key.
Save the key in a secure location for later use.
From the
Storage Account Overview
page, select submenu
Endpoints
in
Settings
.
Click
Copy to clipboard
to copy the
Blob service
endpoint URL. (for example,
https://<storageaccountname>.blob.core.windows.net
)
Save the endpoint URL in a secure location for later use.
How to configure Azure Application Gateway
Sign in to the Azure portal.
Go to the resource group you want.
Select
Application gateway
(the
Application gateway
window appears).
In the
Monitoring
section, select
Diagnostic settings
>
Turn on diagnostics
.
Select
Add diagnostics setting
(the
Diagnostic settings
window displays the settings for the diagnostic logs).
In the
log
section, do the following:
Select the
ApplicationGatewayAccessLog
checkbox.
Select the
ApplicationGatewayFirewallLog
checkbox.
To store logs in the storage account, do the following:
Select
Archive to a storage account
checkbox.
In the
Subscription
list, select an existing subscription.
In the
Storage account
list, select an existing storage account.
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
How to set up the Azure application gateway feed
Click the
Azure Platform
pack.
Locate the
Azure Application Gateway
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
: The blob endpoint URL. (
https://<storageaccountname>.blob.core.windows.net
)
BLOB_NAME
: The name of the blob. (such as,
insights-logs-<logname>
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
Category
metadata.product_event_type
Directly mapped from the
Category
field.
ClientOperationId
additional.fields[].key:"ClientOperationId", value.string_value
Directly mapped from the
ClientOperationId
field.
CorrelationRequestId
additional.fields[].key:"CorrelationRequestId", value.string_value
Directly mapped from the
CorrelationRequestId
field.
GatewayManagerVersion
additional.fields[].key:"GatewayManagerVersion", value.string_value
Directly mapped from the
GatewayManagerVersion
field.
category
metadata.product_event_type
Directly mapped from the
category
field.
level
security_result.severity
Directly mapped from the
level
field, converted to uppercase. If the value is "WARNING", the severity is set to "HIGH" and
security_result.severity_details
is set to the original value.
properties.clientIP
principal.ip
,
principal.asset.ip
Directly mapped from the
properties.clientIP
field.
properties.clientPort
principal.port
Directly mapped from the
properties.clientPort
field, converted to an integer.
properties.clientResponseTime
additional.fields[].key:"clientResponseTime", value.string_value
Directly mapped from the
properties.clientResponseTime
field.
properties.configuration.BgpConfiguration.GatewayConfig.Asn
security_result.detection_fields[].key:"ASN", value
Directly mapped from the
properties.configuration.BgpConfiguration.GatewayConfig.Asn
field when
operationName
is "SetGatewayConfiguration".
properties.configuration.BgpConfiguration.GatewayConfig.PeerAddress
target.ip
,
target.asset.ip
Directly mapped from the
properties.configuration.BgpConfiguration.GatewayConfig.PeerAddress
field when
operationName
is "SetGatewayConfiguration".
properties.configuration.BgpConfiguration.GatewayConfig.PeerType
security_result.detection_fields[].key:"PeerType", value
Directly mapped from the
properties.configuration.BgpConfiguration.GatewayConfig.PeerType
field when
operationName
is "SetGatewayConfiguration".
properties.configuration.IkeVersion
principal.resource.attribute.labels[].key:"ike_version", value
Directly mapped from the
properties.configuration.IkeVersion
field when
operationName
is "SetConnectionConfiguration".
properties.configuration.LocalSubnets
principal.resource.attribute.labels[].key:"local subnets", value
Concatenated string of IP addresses from the
properties.configuration.LocalSubnets
array when
operationName
is "SetConnectionConfiguration".
properties.configuration.LocalTunnelEndpoint
principal.ip
,
principal.asset.ip
Directly mapped from the
properties.configuration.LocalTunnelEndpoint
field when
operationName
is "SetConnectionConfiguration".
properties.configuration.Name
principal.hostname
,
principal.asset.hostname
Directly mapped from the
properties.configuration.Name
field. If empty, the value is taken from
properties.instance
.
properties.configuration.RemoteSite
target.hostname
,
target.asset.hostname
Directly mapped from the
properties.configuration.RemoteSite
field.
properties.configuration.RemoteSubnets
principal.resource.attribute.labels[].key:"remote subnets", value
Concatenated string of IP addresses from the
properties.configuration.RemoteSubnets
array when
operationName
is "SetConnectionConfiguration".
properties.configuration.RemoteTunnelEndpoint
target.ip
,
target.asset.ip
Directly mapped from the
properties.configuration.RemoteTunnelEndpoint
field when
operationName
is "SetConnectionConfiguration".
properties.configuration.VIPAddress
principal.ip
,
principal.asset.ip
Directly mapped from the
properties.configuration.VIPAddress
field when
operationName
is "SetGatewayConfiguration".
properties.configuration.VirtualNetworkRanges
principal.resource.attribute.labels[].key:"virutal network ranges", value
Concatenated string of IP addresses from the
properties.configuration.VirtualNetworkRanges
array when
operationName
is "SetGatewayConfiguration".
properties.configuration.VirtualNetworkSubnets
principal.resource.attribute.labels[].key:"virtual network subnets", value
Concatenated string of IP addresses from the
properties.configuration.VirtualNetworkSubnets
array when
operationName
is "SetGatewayConfiguration".
properties.error_info
additional.fields[].key:"error_info", value.string_value
Directly mapped from the
properties.error_info
field.
properties.host
principal.hostname
,
principal.asset.hostname
Directly mapped from the
properties.host
field if
properties.originalHost
is empty.
properties.httpMethod
network.http.method
Directly mapped from the
properties.httpMethod
field.
properties.httpStatus
network.http.response_code
Directly mapped from the
properties.httpStatus
field, converted to an integer.
properties.httpVersion
network.application_protocol
Set to "HTTP" if the
properties.httpVersion
field contains "HTTP".
properties.instance
principal.hostname
,
principal.asset.hostname
Used as the value for
principal.hostname
if
properties.configuration.Name
is empty.
properties.message
metadata.description
Directly mapped from the
properties.message
field.
properties.operationName
additional.fields[].key:"operationName", value.string_value
Directly mapped from the
properties.operationName
field.
properties.operationStatus
security_result.category_details
Directly mapped from the
properties.operationStatus
field. If the value is "Success" or "InProgress",
security_result.action
is set to "ALLOW".
properties.originalHost
principal.hostname
,
principal.asset.hostname
Directly mapped from the
properties.originalHost
field.
properties.originalRequestUriWithArgs
additional.fields[].key:"originalRequestUriWithArgs", value.string_value
Directly mapped from the
properties.originalRequestUriWithArgs
field.
properties.receivedBytes
network.received_bytes
Directly mapped from the
properties.receivedBytes
field, converted to an unsigned integer.
properties.requestQuery
additional.fields[].key:"requestQuery", value.string_value
Directly mapped from the
properties.requestQuery
field.
properties.requestUri
target.url
Directly mapped from the
properties.requestUri
field.
properties.sentBytes
network.sent_bytes
Directly mapped from the
properties.sentBytes
field, converted to an unsigned integer.
properties.serverResponseLatency
additional.fields[].key:"Server Response Latency", value.string_value
Directly mapped from the
properties.serverResponseLatency
field.
properties.serverRouted
target.ip
,
target.asset.ip
,
target.port
The IP and port are extracted from the
properties.serverRouted
field using a regular expression.
properties.sslCipher
network.tls.cipher
Directly mapped from the
properties.sslCipher
field.
properties.sslClientCertificateIssuerName
network.tls.server.certificate.issuer
Directly mapped from the
properties.sslClientCertificateIssuerName
field.
properties.sslProtocol
network.tls.version
Directly mapped from the
properties.sslProtocol
field.
properties.timeTaken
additional.fields[].key:"timeTaken", value.string_value
Directly mapped from the
properties.timeTaken
field.
properties.transactionId
network.session_id
Directly mapped from the
properties.transactionId
field.
properties.userAgent
network.http.user_agent
,
network.http.parsed_user_agent
Directly mapped from the
properties.userAgent
field. Also, the field is converted to a parsed user agent and mapped to
network.http.parsed_user_agent
.
properties.WAFEvaluationTime
additional.fields[].key:"WAFEvaluationTime", value.string_value
Directly mapped from the
properties.WAFEvaluationTime
field.
properties.WAFMode
additional.fields[].key:"WAFMode", value.string_value
Directly mapped from the
properties.WAFMode
field.
resourceId
target.resource.id
Directly mapped from the
resourceId
field.
resourceid
target.resource.product_object_id
Directly mapped from the
resourceid
field.
ruleName
security_result.rule_name
Directly mapped from the
ruleName
field.
time
/
timeStamp
metadata.event_timestamp
,
timestamp
Parsed as a timestamp using RFC 3339 or ISO8601 format.
timeStamp
is preferred, but
time
is used if
timeStamp
is not present.
(Parser Logic)
metadata.event_type
Set to "NETWORK_CONNECTION" if both principal and target are present, "STATUS_UPDATE" if only principal is present, and "GENERIC_EVENT" otherwise.
(Parser Logic)
metadata.product_name
Set to "Azure Gateway".
(Parser Logic)
metadata.vendor_name
Set to "Microsoft".
(Parser Logic)
has_principal
A boolean flag, set to "true" if any principal information (hostname, IP, or port) is extracted, and "false" otherwise.
(Parser Logic)
has_target
A boolean flag, set to "true" if any target information (hostname, IP, port, resource ID, or URL) is extracted, and "false" otherwise.
(Parser Logic)
disambiguation_key
Added when multiple events are extracted from a single log entry.
