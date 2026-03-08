# Collect Zscaler VPN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-vpn/  
**Scraped:** 2026-03-05T09:49:09.143505Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler VPN logs
Supported in:
Google secops
SIEM
This document explains how to export Zscaler VPN logs by setting up Bindplane agent and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler VPN and the Bindplane agent configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler VPN
: The platform from which you collect logs.
Bindplane agent
: The Bindplane agent fetches logs from Zscaler VPN and sends logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_VPN
label.
Before you begin
Ensure that you have access to the Zscaler Private Access console. For more information, see
Secure Private Access (ZPA) Help
.
Ensure that you are using Zscaler VPN 2024 or later.
Ensure that all systems in the deployment architecture are configured with the UTC time zone.
Configure Log Receiver in Zscaler Private Access
Use the following steps to configure and manage Log Receiver in Zscaler Private Access:
Add a log receiver
Go to
Configuration & Control
>
Private Infrastructure
>
Log Streaming Service
>
Log Receivers
.
Click
Add Log Receiver
.
In the
Log Receiver
tab, do the following:
In the
Name
field, enter the name for the log receiver.
In the
Description
field, enter a description.
In the
Domain or IP Address
field, enter the fully qualified domain name (FQDN) or IP address for the log receiver.
In the
TCP Port
field, enter the TCP port number used by the log receiver .
Select the encryption type in
TLS Encryption
to enable or disable the encryption of the traffic between the App Connector and the log receiver. By default, this setting is disabled.
Select App Connector groups that can forward logs to the receiver from the
App Connector groups
list and click
Done
.
Click
Next
.
In the
Log Stream
tab, do the following:
Select a
Log Type
from the menu.
Select a
Log Template
from the menu.
Copy-paste the
Log Stream Content
and add new fields. Ensure the key names match the actual field names.
The following are the default
Log Stream Content
settings for each log type:
User Activity:
{"LogTimestamp": %j{LogTimestamp:time},"Customer": %j{Customer},"SessionID": %j{SessionID},"ConnectionID": %j{ConnectionID},"InternalReason": %j{InternalReason},"ConnectionStatus": %j{ConnectionStatus},"IPProtocol": %d{IPProtocol},"DoubleEncryption": %d{DoubleEncryption},"Username": %j{Username},"ServicePort": %d{ServicePort},"ClientPublicIP": %j{ClientPublicIP},"ClientPrivateIP": %j{ClientPrivateIP},"ClientLatitude": %f{ClientLatitude},"ClientLongitude": %f{ClientLongitude},"ClientCountryCode": %j{ClientCountryCode},"ClientZEN": %j{ClientZEN},"Policy": %j{Policy},"Connector": %j{Connector},"ConnectorZEN": %j{ConnectorZEN},"ConnectorIP": %j{ConnectorIP},"ConnectorPort": %d{ConnectorPort},"Host": %j{Host},"Application": %j{Application},"AppGroup": %j{AppGroup},"Server": %j{Server},"ServerIP": %j{ServerIP},"ServerPort": %d{ServerPort},"PolicyProcessingTime": %d{PolicyProcessingTime},"ServerSetupTime": %d{ServerSetupTime},"TimestampConnectionStart": %j{TimestampConnectionStart:iso8601},"TimestampConnectionEnd": %j{TimestampConnectionEnd:iso8601},"TimestampCATx": %j{TimestampCATx:iso8601},"TimestampCARx": %j{TimestampCARx:iso8601},"TimestampAppLearnStart": %j{TimestampAppLearnStart:iso8601},"TimestampZENFirstRxClient": %j{TimestampZENFirstRxClient:iso8601},"TimestampZENFirstTxClient": %j{TimestampZENFirstTxClient:iso8601},"TimestampZENLastRxClient": %j{TimestampZENLastRxClient:iso8601},"TimestampZENLastTxClient": %j{TimestampZENLastTxClient:iso8601},"TimestampConnectorZENSetupComplete": %j{TimestampConnectorZENSetupComplete:iso8601},"TimestampZENFirstRxConnector": %j{TimestampZENFirstRxConnector:iso8601},"TimestampZENFirstTxConnector": %j{TimestampZENFirstTxConnector:iso8601},"TimestampZENLastRxConnector": %j{TimestampZENLastRxConnector:iso8601},"TimestampZENLastTxConnector": %j{TimestampZENLastTxConnector:iso8601},"ZENTotalBytesRxClient": %d{ZENTotalBytesRxClient},"ZENBytesRxClient": %d{ZENBytesRxClient},"ZENTotalBytesTxClient": %d{ZENTotalBytesTxClient},"ZENBytesTxClient": %d{ZENBytesTxClient},"ZENTotalBytesRxConnector": %d{ZENTotalBytesRxConnector},"ZENBytesRxConnector": %d{ZENBytesRxConnector},"ZENTotalBytesTxConnector": %d{ZENTotalBytesTxConnector},"ZENBytesTxConnector": %d{ZENBytesTxConnector},"Idp": %j{Idp},"ClientToClient": %j{c2c},"ClientCity": %j{ClientCity},"MicroTenantID": %j{MicroTenantID},"AppMicroTenantID": %j{AppMicroTenantID}}\n
User Status:
{
"LogTimestamp"
:
%
j
{
LogTimestamp:
time
},
"Customer"
:
%
j
{
Customer
},
"Username"
:
%
j
{
Username
},
"SessionID"
:
%
j
{
SessionID
},
"SessionStatus"
:
%
j
{
SessionStatus
},
"Version"
:
%
j
{
Version
},
"ZEN"
:
%
j
{
ZEN
},
"CertificateCN"
:
%
j
{
CertificateCN
},
"PrivateIP"
:
%
j
{
PrivateIP
},
"PublicIP"
:
%
j
{
PublicIP
},
"Latitude"
:
%
f
{
Latitude
},
"Longitude"
:
%
f
{
Longitude
},
"CountryCode"
:
%
j
{
CountryCode
},
"TimestampAuthentication"
:
%
j
{
TimestampAuthentication:
iso8601
},
"TimestampUnAuthentication"
:
%
j
{
TimestampUnAuthentication:
iso8601
},
"TotalBytesRx"
:
%
d
{
TotalBytesRx
},
"TotalBytesTx"
:
%
d
{
TotalBytesTx
},
"Idp"
:
%
j
{
Idp
},
"Hostname"
:
%
j
{
Hostname
},
"Platform"
:
%
j
{
Platform
},
"ClientType"
:
%
j
{
ClientType
},
"TrustedNetworks"
:
[
%
j
(,){
TrustedNetworks
}],
"TrustedNetworksNames"
:
[
%
j
(,){
TrustedNetworksNames
}],
"SAMLAttributes"
:
%
j
{
SAMLAttributes
},
"PosturesHit"
:
[
%
j
(,){
PosturesHit
}],
"PosturesMiss"
:
[
%
j
(,){
PosturesMiss
}],
"ZENLatitude"
:
%
f
{
ZENLatitude
},
"ZENLongitude"
:
%
f
{
ZENLongitude
},
"ZENCountryCode"
:
%
j
{
ZENCountryCode
},
"FQDNRegistered"
:
%
j
{
fqdn_registered
},
"FQDNRegisteredError"
:
%
j
{
fqdn_register_error
},
"City"
:
%
j
{
City
},
"MicroTenantID"
:
%
j
{
MicroTenantID
}}
\n
Browser Access:
{"LogTimestamp":%j{LogTimestamp:time},"ConnectionID":%j{ConnectionID},"Exporter":%j{Exporter},"TimestampRequestReceiveStart":%j{TimestampRequestReceiveStart:iso8601},"TimestampRequestReceiveHeaderFinish":%j{TimestampRequestReceiveHeaderFinish:iso8601},"TimestampRequestReceiveFinish":%j{TimestampRequestReceiveFinish:iso8601},"TimestampRequestTransmitStart":%j{TimestampRequestTransmitStart:iso8601},"TimestampRequestTransmitFinish":%j{TimestampRequestTransmitFinish:iso8601},"TimestampResponseReceiveStart":%j{TimestampResponseReceiveStart:iso8601},"TimestampResponseReceiveFinish":%j{TimestampResponseReceiveFinish:iso8601},"TimestampResponseTransmitStart":%j{TimestampResponseTransmitStart:iso8601},"TimestampResponseTransmitFinish":%j{TimestampResponseTransmitFinish:iso8601},"TotalTimeRequestReceive":%d{TotalTimeRequestReceive},"TotalTimeRequestTransmit":%d{TotalTimeRequestTransmit},"TotalTimeResponseReceive":%d{TotalTimeResponseReceive},"TotalTimeResponseTransmit":%d{TotalTimeResponseTransmit},"TotalTimeConnectionSetup":%d{TotalTimeConnectionSetup},"TotalTimeServerResponse":%d{TotalTimeServerResponse},"Method":%j{Method},"Protocol":%j{Protocol},"Host":%j{Host},"URL":%j{URL},"UserAgent":%j{UserAgent},"XFF":%j{XFF},"NameID":%j{NameID},"StatusCode":%d{StatusCode},"RequestSize":%d{RequestSize},"ResponseSize":%d{ResponseSize},"ApplicationPort":%d{ApplicationPort},"ClientPublicIp":%j{ClientPublicIp},"ClientPublicPort":%d{ClientPublicPort},"ClientPrivateIp":%j{ClientPrivateIp},"Customer":%j{Customer},"ConnectionStatus":%j{ConnectionStatus},"ConnectionReason":%j{ConnectionReason},"Origin":%j{Origin},"CorsToken":%j{CorsToken}}\n
Private Service Edge Status:
{"LogTimestamp": %j{LogTimestamp:time},"Customer": %j{Customer},"SessionID": %j{SessionID},"SessionType": %j{SessionType},"SessionStatus": %j{SessionStatus},"Version": %j{Version},"PackageVersion": %j{PackageVersion},"Platform": %j{Platform},"ZEN": %j{ZEN},"ServiceEdge": %j{ServiceEdge},"ServiceEdgeGroup": %j{ServiceEdgeGroup},"PrivateIP": %j{PrivateIP},"PublicIP": %j{PublicIP},"Latitude": %f{Latitude},"Longitude": %f{Longitude},"CountryCode": %j{CountryCode},"TimestampAuthentication": %j{TimestampAuthentication:iso8601},"TimestampUnAuthentication": %j{TimestampUnAuthentication:iso8601},"CPUUtilization": %d{CPUUtilization},"MemUtilization": %d{MemUtilization},"InterfaceDefRoute": %j{InterfaceDefRoute},"DefRouteGW": %j{DefRouteGW},"PrimaryDNSResolver": %j{PrimaryDNSResolver},"HostUpTime": %j{HostUpTime},"ServiceEdgeStartTime": %j{ServiceEdgeStartTime},"NumOfInterfaces": %d{NumOfInterfaces},"BytesRxInterface": %d{BytesRxInterface},"PacketsRxInterface": %d{PacketsRxInterface},"ErrorsRxInterface": %d{ErrorsRxInterface},"DiscardsRxInterface": %d{DiscardsRxInterface},"BytesTxInterface": %d{BytesTxInterface},"PacketsTxInterface": %d{PacketsTxInterface},"ErrorsTxInterface": %d{ErrorsTxInterface},"DiscardsTxInterface": %d{DiscardsTxInterface},"TotalBytesRx": %d{TotalBytesRx},"TotalBytesTx": %d{TotalBytesTx},"MicroTenantID": %j{MicroTenantID}}\n
App Connector Status:
{"LogTimestamp": %j{LogTimestamp:time},"Customer": %j{Customer},"SessionID": %j{SessionID},"SessionType": %j{SessionType},"SessionStatus": %j{SessionStatus},"Version": %j{Version},"Platform": %j{Platform},"ZEN": %j{ZEN},"Connector": %j{Connector},"ConnectorGroup": %j{ConnectorGroup},"PrivateIP": %j{PrivateIP},"PublicIP": %j{PublicIP},"Latitude": %f{Latitude},"Longitude": %f{Longitude},"CountryCode": %j{CountryCode},"TimestampAuthentication": %j{TimestampAuthentication:iso8601},"TimestampUnAuthentication": %j{TimestampUnAuthentication:iso8601},"CPUUtilization": %d{CPUUtilization},"MemUtilization": %d{MemUtilization},"ServiceCount": %d{ServiceCount},"InterfaceDefRoute": %j{InterfaceDefRoute},"DefRouteGW": %j{DefRouteGW},"PrimaryDNSResolver": %j{PrimaryDNSResolver},"HostStartTime": %j{HostStartTime},"ConnectorStartTime": %j{ConnectorStartTime},"NumOfInterfaces": %d{NumOfInterfaces},"BytesRxInterface": %d{BytesRxInterface},"PacketsRxInterface": %d{PacketsRxInterface},"ErrorsRxInterface": %d{ErrorsRxInterface},"DiscardsRxInterface": %d{DiscardsRxInterface},"BytesTxInterface": %d{BytesTxInterface},"PacketsTxInterface": %d{PacketsTxInterface},"ErrorsTxInterface": %d{ErrorsTxInterface},"DiscardsTxInterface": %d{DiscardsTxInterface},"TotalBytesRx": %d{TotalBytesRx},"TotalBytesTx": %d{TotalBytesTx},"MicroTenantID": %j{MicroTenantID}}\n
In the
SAML Attributes
, click
Select IdP
and select the IdP configuration you want to include in the policy.
In the
Application Segments
menu, select the application segments you want to include and click
Done
.
In the
Segment Groups
menu, select the segment groups you want to include and click
Done
.
In the
Client Types
menu, select the client types you want to include and click
Done
.
In the
Session Statuses
menu, select the session status codes you want to exclude and click
Done
.
Click
Next
.
In the
Review
tab, review your log receiver configuration and click
Save
.
Note:
The
ZSCALER_VPN
Gold parser only supports JSON log format, therefore make sure to select
JSON
as
Log Template
from the menu while configuring log stream.
Copy a log Receiver
Go to
Control
>
Private Infrastructure
>
Log Streaming Service
>
Log Receivers
.
In the table, locate the log receiver you want to modify and click
Copy
.
In the
Add Log Receiver
window, modify fields as necessary. To learn more about each field, see the procedure in the
Add Log Receiver
section.
Click
Save
.
Edit a log Receiver
Go to
Control
>
Private Infrastructure
>
Log Streaming Service
>
Log Receivers
.
In the table, locate the log receiver you want to modify and click
Edit
.
In the
Edit Log Receiver
window, modify fields as necessary. To learn more about each field, see the procedure in the
Add Log Receiver
section.
Click
Save
.
Delete a log Receiver
Go to
Control
>
Private Infrastructure
>
Log Streaming Service
>
Log Receivers
.
In the table, locate the log receiver you want to modify and click
Delete
.
In the
Confirmation
window, click
Delete
.
Forward Logs to Google SecOps using Bindplane agent
Install and set up a
Linux Virtual Machine
.
Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see
the Bindplane agent installation and configuration instructions
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Supported Zscaler VPN log formats
The Zscaler VPN parser supports logs in JSON format.
Supported Zscaler VPN Sample Logs
JSON:
{
  "LogTimestamp": "Thu Jan 18 10:31:01 2024",
  "Customer": "ABC Group",
  "SessionID": "session-id",
  "ConnectionID": "session-id,connection-id",
  "InternalReason": "OPEN_OR_ACTIVE_CONNECTION",
  "ConnectionStatus": "open",
  "IPProtocol": 6,
  "DoubleEncryption": 0,
  "Username": "bc@myownpersonaldomain.com",
  "ServicePort": 443,
  "ClientPublicIP": "198.51.100.0",
  "ClientPrivateIP": "198.51.100.0",
  "ClientLatitude": 51.000000,
  "ClientLongitude": 0.000000,
  "ClientCountryCode": "GB",
  "ClientZEN": "EU-GB-9900",
  "Policy": "RG-NAC-IT",
  "Connector": "abc.mc.local",
  "ConnectorZEN": "EU-GB-9900",
  "ConnectorIP": "198.51.100.0",
  "ConnectorPort": 51146,
  "Host": "xyz.io",
  "Application": "blabla",
  "AppGroup": "HB App Segments",
  "Server": "0",
  "ServerIP": "198.51.100.0",
  "ServerPort": 443,
  "PolicyProcessingTime": 63,
  "ServerSetupTime": 13069,
  "TimestampConnectionStart": "2024-01-18T10:31:01.152Z",
  "TimestampConnectionEnd": "",
  "TimestampCATx": "",
  "TimestampCARx": "2024-01-18T10:31:01.152Z",
  "TimestampAppLearnStart": "",
  "TimestampZENFirstRxClient": "",
  "TimestampZENFirstTxClient": "",
  "TimestampZENLastRxClient": "",
  "TimestampZENLastTxClient": "",
  "TimestampConnectorZENSetupComplete": "2024-01-18T10:31:01.172Z",
  "TimestampZENFirstRxConnector": "",
  "TimestampZENFirstTxConnector": "2024-01-18T10:31:01.172Z",
  "TimestampZENLastRxConnector": "",
  "TimestampZENLastTxConnector": "2024-01-18T10:31:01.172Z",
  "ZENTotalBytesRxClient": 710,
  "ZENBytesRxClient": 710,
  "ZENTotalBytesTxClient": 0,
  "ZENBytesTxClient": 0,
  "ZENTotalBytesRxConnector": 0,
  "ZENBytesRxConnector": 0,
  "ZENTotalBytesTxConnector": 0,
  "ZENBytesTxConnector": 0,
  "Idp": "Azure IdP Config",
  "ClientToClient": "0",
  "ClientCity": "Thamesmead",
  "MicroTenantID": "0",
  "AppMicroTenantID": "0"
}
Field mapping reference
Field mapping reference: ZSCALER_VPN
The following table lists the log fields of the
ZSCALER_VPN
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
AppLearnTime
additional.fields[app_learn_time]
AppMicroTenantID
additional.fields[app_micro_tenant_id]
BytesRxInterface
additional.fields[bytes_rx_interface]
BytesTxInterface
additional.fields[bytes_tx_interface]
CAProcessingTime
additional.fields[ca_processing_time]
ClientToClient
additional.fields[client_to_client]
ClientZEN
additional.fields[client_zen]
ConnectionID
additional.fields[connection_id]
ConnectionReason
additional.fields[connection_reason]
ConnectionSetupTime
additional.fields[connection_setup_time]
ConnectorZEN
additional.fields[connector_zen]
ConnectorGroup
additional.fields[connector_group]
ConnectorStartTime
additional.fields[connector_start_time]
ConnectorZENSetupTime
additional.fields[connector_zen_setup_time]
Connector
additional.fields[connector]
CPUUtilization
additional.fields[cpu_utilization]
Customer
additional.fields[customer]
DefRouteGW
additional.fields[def_route_gw]
DiscardsRxInterface
additional.fields[discards_rx_interface]
DiscardsTxInterface
additional.fields[discards_tx_interface]
DoubleEncryption
additional.fields[double_encryption]
If the
DoubleEncryption
log field value is equal to
0
or the
DoubleEncryption
log field value is equal to
"0"
, then the
additional.fields.double_encryption
UDM field is set to
Off
Else if the
DoubleEncryption
log field value is equal to
1
or the
DoubleEncryption
log field value is equal to
"1"
, then the
additional.fields.double_encryption
UDM field is set to
On
Else the
DoubleEncryption
log field is mapped to the
additional.fields.double_encryption
UDM field.
ErrorsRxInterface
additional.fields[errors_rx_interface]
ErrorsTxInterface
additional.fields[errors_tx_interface]
Exporter
additional.fields[exporter]
HostStartTime
additional.fields[host_start_time]
Idp
additional.fields[idp]
InterfaceDefRoute
additional.fields[interface_def_route]
MemUtilization
additional.fields[mem_utilization]
MicroTenantID
additional.fields[micro_tenant_id]
NumOfInterfaces
additional.fields[num_of_interfaces]
PackageVersion
additional.fields[package_version]
PacketsRxInterface
additional.fields[packets_rx_interface]
PacketsTxInterface
additional.fields[packets_tx_interface]
PolicyProcessingTime
additional.fields[policy_processing_time]
PRAApprovalID
additional.fields[pra_approval_id]
PRACapabilityPolicyID
additional.fields[pra_capability_policy_id]
PRAConnectionID
additional.fields[pra_connection_id]
PRAConsoleType
additional.fields[pra_console_type]
PRACredentialLoginType
additional.fields[pra_credential_login_type]
PRACredentialPolicyID
additional.fields[pra_credential_policy_id]
PRACredentialUserName
additional.fields[pra_credential_user_name]
PRAErrorStatus
additional.fields[pra_error_status]
PRAFileTransferList
additional.fields[pra_file_transfer_list]
PRARecordingStatus
additional.fields[pra_recording_status]
PRASessionType
additional.fields[pra_session_type]
PRASharedMode
additional.fields[pra_shared_mode]
PRASharedUserList
additional.fields[pra_shared_user_list]
PrimaryDNSResolver
additional.fields[primary_dns_resolver]
RequestSize
additional.fields[request_size]
ResponseSize
additional.fields[response_size]
SAMLAttributes
additional.fields[saml_attributes]
ServerSetupTime
additional.fields[server_setup_time]
ServiceCount
additional.fields[service_count]
ServiceEdgeGroup
additional.fields[service_edge_group]
ServiceEdgeStartTime
additional.fields[service_edge_start_time]
ServiceEdge
additional.fields[service_edge]
SessionType
additional.fields[session_type]
TimestampAppLearnStart
additional.fields[timestamp_app_learn_start]
TimestampCARx
additional.fields[timestamp_ca_rx]
TimestampCATx
additional.fields[timestamp_ca_tx]
TimestampConnectionEnd
additional.fields[timestamp_connection_end]
TimestampConnectorZENSetupComplete
additional.fields[timestamp_connector_zen_setup_complete]
TimestampRequestReceiveFinish
additional.fields[timestamp_request_receive_finish]
TimestampRequestReceiveHeaderFinish
additional.fields[timestamp_request_receive_header_finish]
TimestampRequestReceiveStart
additional.fields[timestamp_request_receive_start]
TimestampRequestTransmitFinish
additional.fields[timestamp_request_transmit_finish]
TimestampRequestTransmitStart
additional.fields[timestamp_request_transmit_start]
TimestampResponseReceiveFinish
additional.fields[timestamp_response_receive_finish]
TimestampResponseReceiveStart
additional.fields[timestamp_response_receive_start]
TimestampResponseTransmitFinish
additional.fields[timestamp_response_transmit_finish]
TimestampResponseTransmitStart
additional.fields[timestamp_response_transmit_start]
TimestampZENFirstRxClient
additional.fields[timestamp_zen_first_rx_client]
TimestampZENFirstRxConnector
additional.fields[timestamp_zen_first_rx_connector]
TimestampZENFirstTxClient
additional.fields[timestamp_zen_first_tx_client]
TimestampZENFirstTxConnector
additional.fields[timestamp_zen_first_tx_connector]
TimestampZENLastRxClient
additional.fields[timestamp_zen_last_rx_client]
TimestampZENLastRxConnector
additional.fields[timestamp_zen_last_rx_connector]
TimestampZENLastTxClient
additional.fields[timestamp_zen_last_tx_client]
TimestampZENLastTxConnector
additional.fields[timestamp_zen_last_tx_connector]
TotalTimeConnectionSetup
additional.fields[total_time_connection_setup]
TotalTimeRequestReceive
additional.fields[total_time_request_receive]
TotalTimeRequestTransmit
additional.fields[total_time_request_transmit]
TotalTimeResponseReceive
additional.fields[total_time_response_receive]
TotalTimeResponseTransmit
additional.fields[total_time_response_transmit]
TotalTimeServerResponse
additional.fields[total_time_server_response]
Version
additional.fields[version]
XFF
additional.fields[xff]
ZEN
additional.fields[zen]
Connector
intermediary.application
ConnectorIP
intermediary.ip
If the
ConnectorIP
log field value is
not
empty, then the
ConnectorIP
log field is mapped to the
intermediary.ip
UDM field.
ZENCountryCode
intermediary.location.country_or_region
ZENLatitude
intermediary.location.region_coordinates.latitude
ZENLongitude
intermediary.location.region_coordinates.longitude
ZENTotalBytesRxClient
intermediary.network.received_bytes
ZENTotalBytesTxClient
intermediary.network.sent_bytes
ConnectorPort
intermediary.port
If the
ConnectorPort
log field value is
not
empty, then the
ConnectorPort
log field is mapped to the
intermediary.port
UDM field.
ZENBytesTxClient
intermediary.resource.attribute.labels[zen_bytes_tx_client]
ZENTotalBytesTxConnector
intermediary.resource.attribute.labels[zen_total_bytes_tx_connector]
ZENBytesRxConnector
intermediary.resource.attribute.labels[zen_bytes_rx_connector]
ZENTotalBytesRxConnector
intermediary.resource.attribute.labels[zen_total_bytes_rx_connector]
ZENBytesRxClient
intermediary.resource.attribute.labels[zen_bytes_rx_client]
Policy
metadata.description
LogTimestamp
metadata.event_timestamp
If the
LogTimestamp
log field value is
not
empty, then the
LogTimestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
TimestampConnectionStart
metadata.event_timestamp
If the
LogTimestamp
log field value is
not
empty, then the
LogTimestamp
log field value is mapped to the
metadata.event_timestamp
UDM field.
Else if the
TimestampAuthentication
log field value is
not
empty, then the
TimestampAuthentication
log field value is mapped to the
metadata.event_timestamp
UDM field.
Else if the
TimestampUnAuthentication
log field value is
not
empty, then the
TimestampUnAuthentication
log field value is mapped to the
metadata.event_timestamp
UDM field.
Else if the
TimestampConnectionStart
log field value is
not
empty, then the
TimestampConnectionStart
log field is mapped to the
metadata.event_timestamp
UDM field.
InternalReason
metadata.product_event_type
SessionStatus
metadata.product_event_type
network.ip_protocol
If the
IPProtocol
log field value contain one of the following values, then if the
IPProtocol
log field value is equal to
88
, then the
network.ip_protocol
UDM field is set to
EIGRP
.
Else, if the
IPProtocol
log field value is equal to
50
, then the
network.ip_protocol
UDM field is set to
ESP
.
Else, if the
IPProtocol
log field value is equal to
97
, then the
network.ip_protocol
UDM field is set to
ETHERIP
.
Else, if the
IPProtocol
log field value is equal to
47
, then the
network.ip_protocol
UDM field is set to
GRE
.
Else, if the
IPProtocol
log field value is equal to
1
, then the
network.ip_protocol
UDM field is set to
ICMP
.
Else, if the
IPProtocol
log field value is equal to
58
, then the
network.ip_protocol
UDM field is set to
ICMP6
.
Else, if the
IPProtocol
log field value is equal to
2
, then the
network.ip_protocol
UDM field is set to
IGMP
.
Else, if the
IPProtocol
log field value is equal to
41
, then the
network.ip_protocol
UDM field is set to
IP6IN4
.
Else, if the
IPProtocol
log field value is equal to
103
, then the
network.ip_protocol
UDM field is set to
PIM
.
Else, if the
IPProtocol
log field value is equal to
132
, then the
network.ip_protocol
UDM field is set to
SCTP
.
Else, if the
IPProtocol
log field value is equal to
6
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
IPProtocol
log field value is equal to
17
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
IPProtocol
log field value is equal to
0
, then the
network.ip_protocol
UDM field is set to
UNKNOWN_IP_PROTOCOL
.
Else, if the
IPProtocol
log field value is equal to
112
, then the
network.ip_protocol
UDM field is set to
VRRP
.
88
50
97
47
1
58
2
41
103
132
6
17
0
112
additional.fields[protocol]
If the
IPProtocol
log field value does not contain one of the following values, then the
IPProtocol
log field is mapped to the
additional.fields.protocol
UDM field.
88
50
97
47
1
58
2
41
103
132
6
17
0
112
SessionID
network.session_id
ClientType
principal.application
Hostname
principal.hostname
ClientPrivateIp
principal.ip
If the
ClientPrivateIp
log field value is
not
empty, then the
ClientPrivateIp
log field is mapped to the
principal.ip
UDM field.
PrivateIP
principal.ip
Else, if the
PrivateIP
log field value is
not
empty, then the
PrivateIP
log field is mapped to the
principal.ip
UDM field.
ClientPrivateIP
principal.ip
Else, if the
ClientPrivateIP
log field value is
not
empty, then the
ClientPrivateIP
log field is mapped to the
principal.ip
UDM field.
ClientCity
principal.location.city
City
principal.location.city
ClientCountryCode
principal.location.country_or_region
CountryCode
principal.location.country_or_region
ClientLatitude
principal.location.region_coordinates.latitude
Latitude
principal.location.region_coordinates.latitude
ClientLongitude
principal.location.region_coordinates.longitude
Longitude
principal.location.region_coordinates.longitude
Protocol
principal.network.application_protocol.ApplicationProtocol
If the
Protocol
log field value contain one of the following values, then the
Protocol
log field is mapped to the
principal.network.application_protocol
UDM field.
AFP
AMQP
APPC
ATOM
BEEP
BIT_TORRENT
BITCOIN
CFDP
CIP
COAP
COTP
DCERPC
DDS
DEVICE_NET
DHCP
DICOM
DNP3
DNS
E_DONKEY
ENRP
FAST_TRACK
FINGER
FREENET
FTAM
GOOSE
GOPHER
GRPC
H323
HL7
HTTP
HTTPS
IEC104
IRCP
KADEMLIA
KRB5
LDAP
LPD
MIME
MMS
MODBUS
MQTT
NETCONF
NFS
NIS
NNTP
NTCIP
NTP
OSCAR
PNRP
PTP
QUIC
RDP
RELP
RIP
RLOGIN
RPC
RTMP
RTP
RTPS
RTSP
SAP
SDP
SIP
SLP
SMB
SMTP
SNMP
SNTP
SSH
SSMS
STYX
SV
TCAP
TDS
TOR
TSP
UNKNOWN_APPLICATION_PROTOCOL
VTP
WEB_DAV
WHOIS
X400
X500
XMPP
ClientPublicIp
principal.nat_ip
If the
ClientPrivateIp
log field value is
not
empty or the
PrivateIP
log field value is
not
empty or the
ClientPrivateIP
log field value is
not
empty, then if the
ClientPublicIp
log field value is
not
empty, then the
ClientPublicIp
log field is mapped to the
principal.nat_ip
UDM field.
PublicIP
principal.nat_ip
If the
ClientPrivateIp
log field value is
not
empty or the
PrivateIP
log field value is
not
empty or the
ClientPrivateIP
log field value is
not
empty, then if the
PublicIP
log field value is
not
empty, then the
PublicIP
log field is mapped to the
principal.nat_ip
UDM field.
ClientPublicIP
principal.nat_ip
If the
ClientPrivateIp
log field value is
not
empty or the
PrivateIP
log field value is
not
empty or the
ClientPrivateIP
log field value is
not
empty, then if
ClientPublicIP
log field value is
not
empty, then the
ClientPublicIP
log field is mapped to the
principal.nat_ip
UDM field.
ClientPublicPort
principal.nat_port
Method
principal.network.http.method
URL
principal.network.http.referral_url
StatusCode
principal.network.http.response_code
UserAgent
principal.network.http.user_agent
TotalBytesRx
principal.network.received_bytes
TotalBytesTx
principal.network.sent_bytes
principal.platform
If the
Platform
log field value matches the regular expression pattern
.*(Windows|windows|WINDOWS|Win|win)
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
Platform
log field value matches the regular expression pattern
.*(MAC|mac|Mac)
, then the
principal.platform
UDM field is set to
MAC
.
Else, if the
Platform
log field value matches the regular expression pattern
.*(Linux|linux)
, then the
principal.platform
UDM field is set to
LINUX
.
ServicePort
principal.port
ApplicationPort
principal.port
FQDNRegisteredError
principal.security_result.about.labels[fqdn_registered_error]
FQDNRegistered
principal.security_result.about.labels[fqdn_registered]
PosturesHit
principal.security_result.detection_fields[postures_hit]
The
PosturesHit
log field is mapped to the
principal.security_result.detection_fields.postures_hit
UDM field.
PosturesMiss
principal.security_result.detection_fields[postures_miss]
The
PosturesMiss
log field is mapped to the
principal.security_result.detection_fields.postures_miss
UDM field.
TrustedNetworksNames
principal.security_result.detection_fields[trusted_networks_names]
TrustedNetworks
principal.security_result.detection_fields[trusted_networks]
Username
principal.user.email_addresses
If the
SessionStatus
log field value does not contain one of the following values, then if the
Username
log field value matches the regular expression pattern
(^.*@.*$)
, then the
Username
log field is mapped to the
principal.user.email_addresses
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Else, if the
InternalReason
log field value does not contain one of the following values, then if the
Username
log field value matches the regular expression pattern
(^.*@.*$)
, then the
Username
log field is mapped to the
principal.user.email_addresses
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Username
principal.user.user_display_name
If the
SessionStatus
log field value does not contain one of the following values, then if the
Username
log field value does not match the regular expression pattern
(^.*@.*$)
, then the
Username
log field is mapped to the
principal.user.user_display_name
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
NameID
principal.user.email_addresses
If the
SessionStatus
log field value does not contain one of the following values, then if the
NameID
log field value matches the regular expression pattern
(^.*@.*$)
, then the
NameID
log field is mapped to the
principal.user.email_addresses
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Else if the
InternalReason
log field value does not contain one of the following values, then if the
NameID
log field value matches the regular expression pattern
(^.*@.*$)
, then the
NameID
log field is mapped to the
principal.user.email_addresses
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
ConnectionStatus
security_result.about.labels[connection_status]
CorsToken
security_result.detection_fields [cors_token]
CertificateCN
security_result.detection_fields[certificate_cn]
Server
security_result.detection_fields[server]
Policy
security_result.rule_name
Application
target.application
Host
target.hostname
ServerIP
target.ip
ZENBytesTxConnector
target.network.sent_bytes
ServerPort
target.port
AppGroup
target.user.group_identifiers
UserID
target.user.email_addresses
If the
SessionStatus
log field value contain one of the following values, then if the
UserID
log field value matches the regular expression pattern
(^.*@.*$)
, then the
UserID
log field is mapped to the
target.user.email_addresses
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
UserID
target.user.userid
If the
SessionStatus
log field value contain one of the following values, then if the
UserID
log field value matches the regular expression pattern
(^.*@.*$)
, then the
UserID
log field is mapped to the
target.user.userid
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
UserID
target.user.user_display_name
If the
SessionStatus
log field value contain one of the following values, then if the
UserID
log field value is
not
empty and the
UserID
log field value does not match the regular expression pattern
(^.*@.*$)
, then the
UserID
log field is mapped to the
target.user.user_display_name
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Username
target.user.user_display_name
If the
SessionStatus
log field value contain one of the following values, then if the
UserID
log field value is
not
empty and the
UserID
log field value does not match the regular expression pattern
(^.*@.*$)
, then else, if the
Username
log field value is
not
empty and the
Username
log field value does not match the regular expression pattern
(^.*@.*$)
, then the
Username
log field is mapped to the
target.user.user_display_name
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
security_result.category
If the
InternalReason
log field value is equal to
BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY
, then the
security_result.category
UDM field is set to
ACL_VIOLATION
.
security_result.summary
If the
InternalReason
log field value is equal to
ZPN_STATUS_AUTHENTICATED
, then the
security_result.summary
UDM field is set to
User connected to a ZPA Service Edge
.
Else, if the
SessionStatus
log field value is equal to
ZPN_STATUS_AUTHENTICATED
, then the
security_result.summary
UDM field is set to
User connected to a ZPA Service Edge
.
Else, if the
InternalReason
log field value is equal to
ZPN_STATUS_DISCONNECTED
, then the
security_result.summary
UDM field is set to
User disconnected from a ZPA Service Edge
.
Else, if the
SessionStatus
log field value is equal to
ZPN_STATUS_DISCONNECTED
, then the
security_result.summary
UDM field is set to
User disconnected from a ZPA Service Edge
.
Else, if the
InternalReason
log field value is equal to
BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY
, then the
The user isn't allowed to access the requested application.
log field is mapped to the
security_result.summary
UDM field.
Else, if the
SessionStatus
log field value is equal to
BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY
, then the
The user isn't allowed to access the requested application.
log field is mapped to the
security_result.summary
UDM field.
Else, if the
InternalReason
log field value is equal to
BRK_MT_TERMINATED
, then the
security_result.summary
UDM field is set to
Client closed app TLS connection
.
Else, if the
SessionStatus
log field value is equal to
BRK_MT_TERMINATED
, then the
security_result.summary
UDM field is set to
Client closed app TLS connection
.
Else, if the
InternalReason
log field value is equal to
INVALID_DOMAIN
, then the
DNS resolution or healthcheck failed.
log field is mapped to the
security_result.summary
UDM field.
Else, if the
SessionStatus
log field value is equal to
INVALID_DOMAIN
, then the
DNS resolution or healthcheck failed.
log field is mapped to the
security_result.summary
UDM field.
Else, if the
InternalReason
log field value is equal to
MT_CLOSED_TLS_CONN_GONE_CLIENT_CLOSED
, then the
security_result.summary
UDM field is set to
Client closed app TLS connection
.
Else, if the
SessionStatus
log field value is equal to
MT_CLOSED_TLS_CONN_GONE_CLIENT_CLOSED
, then the
security_result.summary
UDM field is set to
Client closed app TLS connection
.
security_result.description
If the
InternalReason
log field value is equal to
ZPN_STATUS_AUTH_FAILED
, then the
security_result.description
UDM field is set to
User failed to authenticate in ZPA
.
Else, if the
InternalReason
log field value is equal to
BRK_MT_SETUP_FAIL_SAML_EXPIRED
, then the
security_result.description
UDM field is set to
The ZPA service blocked the application request because the timeout policy requires the user to authenticate.
Else, if the
InternalReason
log field value is equal to
BRK_MT_SETUP_FAIL_SCIM_INACTIVE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge has failed to set up the data connection due to the user being deactivated or not synced in SCIM.
Else, if the
InternalReason
log field value is equal to
BRK_MT_SETUP_FAIL_TOO_MANY_FAILED_ATTEMPTS
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge has received the exceeded limit of errors to accept any additional connection requests for this domain. New requests are not received until the preset waiting period has elapsed.
Else, if the
InternalReason
log field value is equal to
BRK_MT_SETUP_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge was waiting for a data connection request from an App Connector that could provide access to the application, but the request timed out while waiting. The request from an App Connector is triggered in response to the initial application request from the Zscaler Client Connector.
Else, if the
InternalReason
log field value is equal to
BRK_MT_TERMINATED_APPROVAL_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge terminated the session and caused a timeout due to approval time window expiration.
Else, if the
InternalReason
log field value is equal to
BRK_MT_TERMINATED_BRK_SWITCHED
, then the
security_result.description
UDM field is set to
The Zscaler Client Connector connection to a ZPA Public Service Edge was terminated due to a ZPA Public Service Edge initiated switch.
Else, if the
InternalReason
log field value is equal to
BRK_MT_TERMINATED_IDLE_TIMEOUT
, then the
security_result.description
UDM field is set to
If an idle timeout is configured, ZPA will keep the user's application session alive for the interval specified by the Idle Connection Timeout prior to terminating the session. This is not an error scenario, only a function of the service.
Else, if the
InternalReason
log field value is equal to
BRK_MT_TERMINATED
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge closed the application tunnel connection. This is part of the Service Edge's regular process at the end of an application request.
Else, if the
InternalReason
log field value is equal to
BROKER_NOT_ENABLED
, then the
security_result.description
UDM field is set to
Remote assistance communication is disabled for the ZPA Public Service Edge.
Else, if the
InternalReason
log field value is equal to
C2C_CLIENT_CONN_EXPIRED
, then the
security_result.description
UDM field is set to
The client connection expired during the initiation of a remote assistance session.
Else, if the
InternalReason
log field value is equal to
C2C_CLIENT_NOT_FOUND
, then the
security_result.description
UDM field is set to
The client connection is closed during the initiation of a remote assistance session.
Else, if the
InternalReason
log field value is equal to
C2C_MTUNNEL_BAD_STATE
, then the
security_result.description
UDM field is set to
The remote assistance connection expired due to inconsistencies in the connection.
Else, if the
InternalReason
log field value is equal to
C2C_MTUNNEL_FAILED_FORWARD
, then the
security_result.description
UDM field is set to
The remote assistance connection failed to initiate the connection to the destination client and expired.
Else, if the
InternalReason
log field value is equal to
C2C_MTUNNEL_NOT_FOUND
, then the
security_result.description
UDM field is set to
The remote assistance connection is not found.
Else, if the
InternalReason
log field value is equal to
C2C_NOT_AVAILABLE
, then the
security_result.description
UDM field is set to
The remote assistance connection is not available.
Else, if the
InternalReason
log field value is equal to
CLT_CONN_FAILED
, then the
security_result.description
UDM field is set to
The incoming TCP connection failed.
Else, if the
InternalReason
log field value is equal to
CLT_DOUBLEENCRYPT_NOT_SUPPORTED
, then the
security_result.description
UDM field is set to
The double encryption of the incoming Microtunnel request is not supported by the Zscaler Client Connector.
Else, if the
InternalReason
log field value is equal to
CLT_DUPLICATE_TAG
, then the
security_result.description
UDM field is set to
The tag ID is used in the Zscaler Client Connector.
Else, if the
InternalReason
log field value is equal to
CLT_INVALID_CLIENT
, then the
security_result.description
UDM field is set to
The receiving Zscaler Client Connector device doesn't match with the request.
Else, if the
InternalReason
log field value is equal to
CLT_INVALID_DOMAIN
, then the
security_result.description
UDM field is set to
The FQDN destination host doesn't match the receiving Zscaler Client Connector detected.
Else, if the
InternalReason
log field value is equal to
CLT_INVALID_TAG
, then the
security_result.description
UDM field is set to
The tag ID is not designed for the incoming Microtunnel flow.
Else, if the
InternalReason
log field value is equal to
CLT_PORT_UNREACHABLE
, then the
security_result.description
UDM field is set to
The port is not listening.
Else, if the
InternalReason
log field value is equal to
CLT_PROBE_FAILED
, then the
security_result.description
UDM field is set to
The port probe failed.
Else, if the
InternalReason
log field value is equal to
CLT_PROTOCOL_NOT_SUPPORTED
, then the
security_result.description
UDM field is set to
The IP protocol of the incoming Microtunnel request is not supported by the Zscaler Client Connector.
Else, if the
InternalReason
log field value is equal to
CLT_READ_FAILED
, then the
security_result.description
UDM field is set to
The Zscaler Client Connector local socket read failed.
Else, if the
InternalReason
log field value is equal to
CLT_WRONG_PORT
, then the
security_result.description
UDM field is set to
The incoming Microtunnel request asks for the listening ports of the Zscaler Client Connector itself.
Else, if the
InternalReason
log field value is equal to
CUSTOMER_NOT_ENABLED
, then the
security_result.description
UDM field is set to
Remote assistance communication is disabled for the current customer.
Else, if the
InternalReason
log field value is equal to
DSP_MT_SETUP_FAIL_CANNOT_SEND_TO_BROKER
, then the
security_result.description
UDM field is set to
The path selection service is unable to communicate with the ZPA Public Service Edge or ZPA Private Service Edge.
Else, if the
InternalReason
log field value is equal to
DSP_MT_SETUP_FAIL_DISCOVERY_TIMEOUT
, then the
security_result.description
UDM field is set to
The health information request timed out when attempting to reach the App Connector.
Else, if the
InternalReason
log field value is equal to
DSP_MT_SETUP_FAIL_MISSING_HEALTH
, then the
security_result.description
UDM field is set to
The App Connector was unable to process the continuous health report due to missing health information.
Else, if the
InternalReason
log field value is equal to
EXPTR_FCONN_GONE
, then the
security_result.description
UDM field is set to
User access fails due to a network error that caused the Browser Access service to remove the user's application sessions.
Else, if the
InternalReason
log field value is equal to
EXPTR_MT_TLS_SETUP_FAIL_CERT_CHAIN_ISSUE
, then the
security_result.description
UDM field is set to
ZPA is not able to validate the chain of trust for the server certificate configured for this application.
Else, if the
InternalReason
log field value is equal to
EXPTR_MT_TLS_SETUP_FAIL_NOT_TRUSTED_CA
, then the
security_result.description
UDM field is set to
The application server certificate is not signed by a trusted CA and ZPA is configured to verify that the web server certificate is signed by a trusted CA.
Else, if the
InternalReason
log field value is equal to
EXPTR_MT_TLS_SETUP_FAIL_PEER
, then the
security_result.description
UDM field is set to
Browser Access service cannot set up a HTTPS connection towards the web server due to an issue occurring during TLS setup.
Else, if the
InternalReason
log field value is equal to
EXPTR_MT_TLS_SETUP_FAIL_VERSION_MISMATCH
, then the
security_result.description
UDM field is set to
A TLS version mismatch between ZPA and the Browser Access-enabled application occurred. This happens when the web server is running TLS 1.0/1.1 or earlier versions.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_AST_DATA_CONN_FLOW_CONTROL
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge data connection was closed by App Connector because the connection was idle or blocked for more than 5 minutes.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_AST_PBRK_CTRL_CONN_CFG_CHG
, then the
security_result.description
UDM field is set to
The ZPA Private Service Edge connection was closed due to a change in the ZPA Private Service Edge configuration.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_AST_PBRK_DATA_DOWN
, then the
security_result.description
UDM field is set to
The ZPA Private Service Edge connection to the App Connector was disconnected.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_AST_PBRK_VERIFY_FAILED
, then the
security_result.description
UDM field is set to
The ZPA Private Service Edge connection was closed because the connection was made with a ZPA Private Service Edge different than the expected ZPA Private Service Edge.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_BRK_DATA_CONN_FLOW_CONTROL
, then the
security_result.description
UDM field is set to
The data connection was closed by the ZPA Public Service Edge or ZPA Private Service Edge because the connection was idle or blocked for more than 5 minutes.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_CALLBACK_ERR
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection callback returned an error.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_CERT_VERIFY
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was unable to verify the server certificate.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_CONNECT_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge timed out while setting up a connection. This is not an error scenario, only a function of the service.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_DATA_CONN_FLOW_CONTROL
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed because flow control was blocked for more than 5 minutes.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_HTTP_RESPONSE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed because the returned code was not 200. The returned code 200 means that a connection is OK.
If the code does not come back with 200, the connection is closed.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_LOG_RECONN
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge reconnection to the log channels timed out because the reconnection timer expired.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_MEMORY
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection closed because of one of the following reasons: a memory error due to the read buffer on the connection not being allocated, or the SSL state from the SSL context is unavailable.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_OPS
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed at the user's request.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_PROXY_DNS
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection closed because the address resolution for this destination is no longer available.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_PROXY_FAIL
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed due to one of the following proxy connection issues received: a failed connection, unable to send a connection request, or an error from the proxy.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_PROXY_IDLE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection closed because the connection through the proxy timed out.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_PROXY_NOT_200
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection through the proxy was closed because the returned code was not 200. The returned code 200 means that a connection is OK.
If the code does not come back with 200, the connection is closed.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_PROXY_PARSE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection through the proxy was closed because the proxy modified the HTTP fields which caused parsing issues.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_PROXY_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed because the connection through the proxy exceeded the proxy timeout value.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_REDIRECT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was redirected to another ZPA Public Service Edge or ZPA Private Service Edge.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_REGISTRATION
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge was unable to register status callbacks.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_RX_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection timed out while waiting for a connection response from the server.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SERIALIZE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed because the serializer was unable to serialize an internal control message.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SETSOCKOPT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed because the status of the proxy connection was unavailable.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SNI_MISSING
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection is closed because the Server Name Indication (SNI) is missing.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SNI_SLOW
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection closed because the maximum number of Server Name Indication (SNI) callbacks was reached.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SNI_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection is closed because the wait time for Server Name Indication (SNI) callbacks has expired.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SOCKET_CLOSE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed because the end of file was received. This is not an error scenario, only a function of the service.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SOCKET_ERR
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was closed due to a socket error.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_SSL_CTX_NONE
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection closed because it was unable to identify the SSL context.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_TIMEOUT
, then the
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge keeps the user's application session alive for the time interval specified by the Idle Connection Timeout prior to terminating the session. This is not an error scenario, only a function of the service.
Else, if the
InternalReason
log field value is equal to
FOHH_CLOSE_REASON_TLV_CALLBACK
, then the
security_result.description
UDM field is set to
security_result.description
UDM field is set to
The ZPA Public Service Edge or ZPA Private Service Edge connection was
. closed due to a deserialization error.the
security_result.description
UDM field is set to
User failed to authenticate in ZPA
.
Else, if the
InternalReason
log field value is equal to
APP_NOT_AVAILABLE
, then the
security_result.description
UDM field is set to
The Application Segment is not configured for access.
Else, if the
InternalReason
log field value is equal to
APP_NOT_REACHABLE
, then the
security_result.description
UDM field is set to
None of the App Connectors configured for the application can reach the server.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_APP_NOT_FOUND
, then the
security_result.description
UDM field is set to
The App Connector cannot set up a connection to the server because it cannot find the application in the configuration database.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_AST_CFG_DISABLE
, then the
security_result.description
UDM field is set to
The Microtunnel setup has failed because the App Connector has been disabled in the ZPA Admin Portal.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_AST_IN_PAUSE_STATE_FOR_UPGRADE
, then the
security_result.description
UDM field is set to
The App Connector is in a paused state for upgrade. The App Connector will return to a normal state after the upgrade completes.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_BIND_ACK
, then the
security_result.description
UDM field is set to
The connection confirmation from the ZPA Public Service Edge or ZPA Private Service Edge has an error.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_BIND_GLOBAL_OWNER
, then the
security_result.description
UDM field is set to
The App Connector processing the data connection request encountered an error.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_BIND_TO_AST_LOCAL_OWNER
, then the
security_result.description
UDM field is set to
The App Connector processing the data connection request has encountered an error.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_BRK_HASH_TBL_FULL
, then the
security_result.description
UDM field is set to
The App Connector cannot set up a connection to the ZPA Public Service Edge or ZPA Private Service Edge because the connection database is full.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_BROKER_BIND_FAIL
, then the
security_result.description
UDM field is set to
The App Connector encountered an error when setting up a data connection to the ZPA Public Service Edge or ZPA Private Service Edge.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_CONN_PEER
, then the
security_result.description
UDM field is set to
The App Connector encountered an error when connecting the ZPA Public Service Edge or ZPA Private Service Edge and server connections.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_CPU_LIMIT_REACHED
, then the
security_result.description
UDM field is set to
The App Connector CPU limit is exceeded for a Privileged Remote Access (PRA) connection. No more PRA connections are allowed.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_DUP_MT_ID
, then the
security_result.description
UDM field is set to
The App Connector cannot set up a data connection because another data connection with the same tag ID already exists.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_HASH_TBL_FULL
, then the
security_result.description
UDM field is set to
The App Connector cannot set up a connection to the server because the connection database is full.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_INIT_FOHH_MCONN
, then the
security_result.description
UDM field is set to
The App Connector encountered an error when setting up a connection to the ZPA Public Service Edge or ZPA Private Service Edge.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_MAX_SESSIONS_REACHED
, then the
security_result.description
UDM field is set to
The maximum session limit is reached for Privileged Remote Access (PRA) connections on the App Connector.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_MEM_LIMIT_REACHED
, then the
security_result.description
UDM field is set to
The App Connector memory limit is exceeded for a Privileged Remote Access (PRA) connection. No more PRA connections are allowed.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_NO_DNS_TO_SERVER
, then the
security_result.description
UDM field is set to
The end host (not a proxy or a configured server group) is not resolvable. The code only comes up in a specific use case when there is all of the following:
.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_NO_EPHEMERAL_PORT
, then the
security_result.description
UDM field is set to
The transaction failed as the operating system has run out of source ports
.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_NO_PROCESS_FD
, then the
security_result.description
UDM field is set to
The transaction failed as the App Connector processing could not secure additional file descriptors from the operating system
.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_NO_SYSTEM_FD
, then the
security_result.description
UDM field is set to
The transaction failed as the operating system has run out of file descriptors.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_OPEN_BROKER_CONN
, then the
security_result.description
UDM field is set to
The App Connector encountered an error when opening a connection to the ZPA Public Service Edge or ZPA Private Service Edge.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_OPEN_SERVER_CLOSE
, then the
security_result.description
UDM field is set to
During data connection setup, the connection from the server to the App Connector was closed.
Else, if the
InternalReason
log field value is equal to
AST_MT_SETUP_ERR_OPEN_SERVER_CONN</code
security_result.action
If the
InternalReason
log field value contain one of the following values, then the
security_result.action
UDM field is set to
BLOCK
.
BRK_MT_SETUP_FAIL_NO_POLICY_FOUND
BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY
BRK_MT_SETUP_FAIL_SAML_EXPIRED
metadata.event_type
If the
InternalReason
log field value contain one of the following values, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
ZPN_STATUS_AUTH_FAILED
APP_NOT_AVAILABLE
APP_NOT_REACHABLE
AST_MT_SETUP_ERR_APP_NOT_FOUND
AST_MT_SETUP_ERR_AST_CFG_DISABLE
AST_MT_SETUP_ERR_AST_IN_PAUSE_STATE_FOR_UPGRADE
AST_MT_SETUP_ERR_BIND_ACK
AST_MT_SETUP_ERR_BIND_GLOBAL_OWNER
AST_MT_SETUP_ERR_BIND_TO_AST_LOCAL_OWNER
AST_MT_SETUP_ERR_BRK_HASH_TBL_FULL
AST_MT_SETUP_ERR_BROKER_BIND_FAIL
AST_MT_SETUP_ERR_CONN_PEER
AST_MT_SETUP_ERR_CPU_LIMIT_REACHED
AST_MT_SETUP_ERR_DUP_MT_ID
AST_MT_SETUP_ERR_HASH_TBL_FULL
AST_MT_SETUP_ERR_INIT_FOHH_MCONN
AST_MT_SETUP_ERR_MAX_SESSIONS_REACHED
AST_MT_SETUP_ERR_MEM_LIMIT_REACHED
AST_MT_SETUP_ERR_NO_DNS_TO_SERVER
AST_MT_SETUP_ERR_NO_EPHEMERAL_PORT
AST_MT_SETUP_ERR_NO_PROCESS_FD
AST_MT_SETUP_ERR_NO_SYSTEM_FD
AST_MT_SETUP_ERR_OPEN_BROKER_CONN
AST_MT_SETUP_ERR_OPEN_SERVER_CLOSE
AST_MT_SETUP_ERR_OPEN_SERVER_CONN
AST_MT_SETUP_ERR_OPEN_SERVER_ERROR
AST_MT_SETUP_ERR_OPEN_SERVER_TIMEOUT
AST_MT_SETUP_ERR_PRA_UNAVAILABLE
AST_MT_SETUP_TIMEOUT_CANNOT_CONN_TO_BROKER
AST_MT_SETUP_TIMEOUT_CANNOT_CONN_TO_SERVER
AST_MT_SETUP_TIMEOUT_NO_ACK_TO_BIND
AST_MT_SETUP_TIMEOUT
AST_MT_TERMINATED
BRK_CONN_UPGRADE_REQUEST_FAILED
BRK_CONN_UPGRADE_REQUEST_FORBIDDEN
BRK_MT_AUTH_ALREADY_FAILED
BRK_MT_AUTH_NO_SAML_ASSERTION_IN_MSG
BRK_MT_AUTH_SAML_CANNOT_ADD_ATTR_TO_HASH
BRK_MT_AUTH_SAML_CANNOT_ADD_ATTR_TO_HEAP
BRK_MT_AUTH_SAML_DECODE_FAIL
BRK_MT_AUTH_SAML_FAILURE
BRK_MT_AUTH_SAML_FINGER_PRINT_FAIL
BRK_MT_AUTH_SAML_NO_USER_ID
BRK_MT_AUTH_TWO_SAML_ASSERTION_IN_MSG
BRK_MT_CLOSED_FROM_ASSISTANT
BRK_MT_CLOSED_FROM_CLIENT
BRK_MT_CLOSED_ZIA_CONN_GONE_CLOSED
BRK_MT_RESET_FROM_SERVER
BRK_MT_SETUP_FAIL_APP_NOT_FOUND
BRK_MT_SETUP_FAIL_BIND_RECV_IN_BAD_STATE
BRK_MT_SETUP_FAIL_BIND_TO_AST_LOCAL_OWNER
BRK_MT_SETUP_FAIL_BIND_TO_CLIENT_LOCAL_OWNER
BRK_MT_SETUP_FAIL_CANNOT_PROMOTE
BRK_MT_SETUP_FAIL_CANNOT_SEND_MT_COMPLETE
BRK_MT_SETUP_FAIL_CANNOT_SEND_TO_DISPATCHER
BRK_MT_SETUP_FAIL_CONNECTOR_GROUPS_MISSING
BRK_MT_SETUP_FAIL_CTRL_BRK_CANNOT_FIND_CONNECTOR
BRK_MT_SETUP_FAIL_DUPLICATE_TAG_ID
BRK_MT_SETUP_FAIL_ICMP_RATE_LIMIT_EXCEEDED
BRK_MT_SETUP_FAIL_ICMP_RATE_LIMIT_NUM_APP_EXCEEDED
BRK_MT_SETUP_FAIL_NO_POLICY_FOUND
BRK_MT_SETUP_FAIL_RATE_LIMIT_EXCEEDED
BRK_MT_SETUP_FAIL_RATE_LIMIT_LOOP_DETECTED
BRK_MT_SETUP_FAIL_RATE_LIMIT_NUM_APP_EXCEEDED
BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY_APPROVAL
BRK_MT_SETUP_FAIL_REJECTED_BY_POLICY
BRK_MT_SETUP_FAIL_REPEATED_DISPATCH
BRK_MT_SETUP_FAIL_SAML_EXPIRED
BRK_MT_SETUP_FAIL_SCIM_INACTIVE
BRK_MT_SETUP_FAIL_TOO_MANY_FAILED_ATTEMPTS
BRK_MT_SETUP_TIMEOUT
BRK_MT_TERMINATED_APPROVAL_TIMEOUT
BRK_MT_TERMINATED_BRK_SWITCHED
BRK_MT_TERMINATED_IDLE_TIMEOUT
BRK_MT_TERMINATED
BROKER_NOT_ENABLED
C2C_CLIENT_CONN_EXPIRED
C2C_CLIENT_NOT_FOUND
C2C_MTUNNEL_BAD_STATE
C2C_MTUNNEL_FAILED_FORWARD
C2C_MTUNNEL_NOT_FOUND
C2C_NOT_AVAILABLE
CLT_CONN_FAILED
CLT_DOUBLEENCRYPT_NOT_SUPPORTED
CLT_DUPLICATE_TAG
CLT_INVALID_CLIENT
CLT_INVALID_DOMAIN
CLT_INVALID_TAG
CLT_PORT_UNREACHABLE
CLT_PROBE_FAILED
CLT_PROTOCOL_NOT_SUPPORTED
CLT_READ_FAILED
CLT_WRONG_PORT
CUSTOMER_NOT_ENABLED
DSP_MT_SETUP_FAIL_CANNOT_SEND_TO_BROKER
DSP_MT_SETUP_FAIL_DISCOVERY_TIMEOUT
DSP_MT_SETUP_FAIL_MISSING_HEALTH
EXPTR_FCONN_GONE
EXPTR_MT_TLS_SETUP_FAIL_CERT_CHAIN_ISSUE
EXPTR_MT_TLS_SETUP_FAIL_NOT_TRUSTED_CA
EXPTR_MT_TLS_SETUP_FAIL_PEER
EXPTR_MT_TLS_SETUP_FAIL_VERSION_MISMATCH
FOHH_CLOSE_REASON_AST_DATA_CONN_FLOW_CONTROL
FOHH_CLOSE_REASON_AST_PBRK_CTRL_CONN_CFG_CHG
FOHH_CLOSE_REASON_AST_PBRK_DATA_DOWN
FOHH_CLOSE_REASON_AST_PBRK_VERIFY_FAILED
FOHH_CLOSE_REASON_BRK_DATA_CONN_FLOW_CONTROL
FOHH_CLOSE_REASON_CALLBACK_ERR
FOHH_CLOSE_REASON_CERT_VERIFY
FOHH_CLOSE_REASON_CONNECT_TIMEOUT
FOHH_CLOSE_REASON_DATA_CONN_FLOW_CONTROL
FOHH_CLOSE_REASON_HTTP_RESPONSE
FOHH_CLOSE_REASON_LOG_RECONN
FOHH_CLOSE_REASON_MEMORY
FOHH_CLOSE_REASON_OPS
FOHH_CLOSE_REASON_PROXY_DNS
FOHH_CLOSE_REASON_PROXY_FAIL
FOHH_CLOSE_REASON_PROXY_IDLE
FOHH_CLOSE_REASON_PROXY_NOT_200
FOHH_CLOSE_REASON_PROXY_PARSE
FOHH_CLOSE_REASON_PROXY_TIMEOUT
FOHH_CLOSE_REASON_REDIRECT
FOHH_CLOSE_REASON_REGISTRATION
FOHH_CLOSE_REASON_RX_TIMEOUT
FOHH_CLOSE_REASON_SERIALIZE
FOHH_CLOSE_REASON_SETSOCKOPT
FOHH_CLOSE_REASON_SNI_MISSING
FOHH_CLOSE_REASON_SNI_SLOW
FOHH_CLOSE_REASON_SNI_TIMEOUT
FOHH_CLOSE_REASON_SOCKET_CLOSE
FOHH_CLOSE_REASON_SOCKET_ERR
FOHH_CLOSE_REASON_SSL_CTX_NONE
FOHH_CLOSE_REASON_TIMEOUT
FOHH_CLOSE_REASON_TLV_CALLBACK
FOHH_CLOSE_REASON_TLV_DESERIALIZE
FOHH_CLOSE_REASON_TLV_LEN
FOHH_CLOSE_REASON_TLV_NO_CALLBACK
FQDN_BAD_REGEX
FQDN_BAD_SCHEMA
FQDN_EMPTY
FQDN_NO_ENTRIES
FQDN_NO_MATCH
FQDN_TOO_MANY_REGEX
INVALID_DOMAIN
MT_CLOSED_INTERNAL_ERROR
MT_CLOSED_TERMINATED
MT_CLOSED_TLS_CONN_GONE_AST_CLOSED
MT_CLOSED_TLS_CONN_GONE_CLIENT_CLOSED
MT_CLOSED_TLS_CONN_GONE_MANUAL_DRAIN
MT_CLOSED_TLS_CONN_GONE_SCIM_USER_DISABLE
MT_CLOSED_TLS_CONN_GONE
NO_CONNECTOR_AVAILABLE
OPEN_OR_ACTIVE_CONNECTION
ZIA_MT_BLOCKED_BY_INSPECTION
ZIA_MT_BLOCKED_BY_SYSTEM_ERROR
ZPN_ERR_AUTH_APP_FAIL
ZPN_ERR_AUTH_CUSTOMER_FAIL
ZPN_ERR_AUTH_CUSTOMER_MISSING
ZPN_ERR_AUTH_EXPIRED
ZPN_ERR_AUTH_NOT_COMPLETE
ZPN_ERR_AUTH_SAML_EXPIRED
ZPN_ERR_AUTH_SERVICE_DISABLED
ZPN_ERR_AUTH_TIMEOUT
ZPN_ERR_CERT_EXPIRED
ZPN_ERR_CUSTOMER_DISABLED
ZPN_ERR_SCIM_INACTIVE
Else, if the
SessionStatus
log field value is equal to
ZPN_STATUS_AUTHENTICATED
and (the
Application
log field value is
not
empty or the
Host
log field value is
not
empty or the
ServerIP
log field value is
not
empty or the
ZENBytesTxConnector
log field value is
not
empty or the
ServerPort
log field value is
not
empty or the
AppGroup
log field value is
not
empty or the
UserID
log field value is
not
empty or the
Username
log field value is
not
empty or the
NameID
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
SessionStatus
log field value is equal to
ZPN_STATUS_DISCONNECTED
and (the
Application
log field value is
not
empty or the
Host
log field value is
not
empty or the
ServerIP
log field value is
not
empty or the
ZENBytesTxConnector
log field value is
not
empty or the
ServerPort
log field value is
not
empty or the
AppGroup
log field value is
not
empty or the
UserID
log field value is
not
empty or the
Username
log field value is
not
empty or the
NameID
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
USER_LOGOUT
.
Else, if the
principal.ip
log field value is
not
empty or the
principal.mac
log field value is
not
empty or the
principal.hostname
log field value is
not
empty or the
principal.asset_id
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
If the
InternalReason
log field value contain one of the following values, then if the
Username
log field value is
not
empty, then the
extensions.auth.type
UDM field is set to
VPN
.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Else, if the
SessionStatus
log field value contain one of the following values, then if the
Username
log field value is
not
empty, then the
extensions.auth.type
UDM field is set to
VPN
.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
NameID
metadata.vendor_name
If the
SessionStatus
log field value does not contain one of the following values, then if the
NameID
log field value does not match the regular expression pattern
(^.*@.*$)
, then the
NameID
log field is mapped to the
principal.user.userid
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Else, if the
InternalReason
log field value does not contain one of the following values, then if the
NameID
log field value does not match the regular expression pattern
(^.*@.*$)
, then the
NameID
log field is mapped to the
principal.user.userid
UDM field.
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
ZPN_STATUS_AUTHENTICATED
ZPN_STATUS_DISCONNECTED
Need more help?
Get answers from Community members and Google SecOps professionals.
