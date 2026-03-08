# Collect Cisco ASA firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-asa-firewall/  
**Scraped:** 2026-03-05T09:47:42.576561Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cisco ASA firewall logs
Supported in:
Google secops
SIEM
This document describes how you can collect Cisco ASA firewall logs by configuring Cisco Adaptive Security Appliance
(ASA) firewall and a Google Security Operations forwarder. This
document also lists the supported log types and supported Cisco ASA versions.
For more information, see
Data ingestion to Google Security Operations
.
Overview
The following deployment architecture diagram shows how Cisco ASA firewall
devices are configured to send logs to Google Security Operations. Each customer
deployment might differ from this representation and might be more complex.
The architecture diagram shows the following components:
Cisco ASA devices
. To configure remote logging,
Cisco ASDM
is installed on each of the
Cisco ASA device
. The Cisco
ASA devices are connected over VPN to a central Cisco ASA device.
Central Cisco ASA device
. To collect logs from each Cisco ASA device, Syslog is
configured in the central Cisco ASA device. The central Cisco ASA device forwards
the collected logs to a Google Security Operations forwarder.
Google Security Operations forwarder
. The Google Security Operations forwarder is a lightweight
software component, deployed in the customer's network, that supports syslog.
The Google Security Operations forwarder forwards the logs to Google Security Operations.
Google Security Operations
. Google Security Operations retains and analyzes the logs that
the Cisco ASA devices generate.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
CISCO_ASA_FIREWALL
ingestion label.
Before you begin
Ensure that you use a Cisco ASA software version that the Google Security Operations
parser supports. The Google Security Operations parser supports Cisco ASA software version 9.16(1).
Verify the Cisco ASA message IDs that the Google Security Operations parser supports.
For information about the list of message IDs that Google Security Operations parser supports, see
Cisco ASA message IDs
.
Ensure that all systems in the deployment architecture are configured
in the UTC time zone.
Before you use the Cisco ASA firewall parser, review the
changes in field mappings between the previous parser and the current Cisco ASA firewall parser
. As part of the migration,
ensure that the rules, searches, dashboards, or other processes that depend on
the original fields use the updated fields.
For example, in the previous parser, for the message ID
605005
, the
target_service
field is mapped to the
network.application_protocol
UDM field. In the current Cisco ASA firewall parser,
the
target_service
field is mapped to the
target.application
UDM field. If
you migrate to the current Cisco ASA firewall parser and use the
target_service
field in your rules,
you need to modify the rules to use the
target.application
UDM field of the current parser.
Configure Cisco ASA and the Google Security Operations forwarder
To configure Cisco ASA and the Google Security Operations forwarder, do the following:
Configure remote logging by using Cisco Adaptive Security Device Manager (ASDM).
For more information, see
Configure by using ASDM
.
When you configure remote logging, to filter logs based on their severity level,
ensure that you specify the following severity levels:
Severity 1 - Alert messages
Severity 2 - Critical messages
Severity 3 - Error messages
Severity 4 - Warning messages
Severity 5 - Notification messages
Severity 6 - Informational messages
Severity 7 - Debugging messages
Deploy syslog server. For more information, see
How to install and set up Rsyslog server
.
Configure Nxlogs Service in Ubuntu Syslog server to collect syslogs from a Cisco ASA Firewall and Log parsers to Google SecOps. For more information, see
Configure Nxlog
.
The following is an example of a Nxlog configuration file:
LogFile /var/log/nxlog/nxlog.log
  LogLevel INFO

  define CISCO_ASA_ADDRESS <Enter syslog server ip address>
  define CISCO_ASA_PORT <Enter syslog server port>

  <Input syslog>
    Module      im_file
    File        '/var/log/syslog'

  </Input>

  <Output out_chronicle>
    Module  om_tcp
    Host    %CISCO_ASA_ADDRESS%
    Port    %CISCO_ASA_PORT%
  </Output>

  <Route ciscoasa_to_chronicle>
    Path syslog => out_chronicle
  </Route>
Configure the Google Security Operations forwarder to send logs to
Google Security Operations.
For more information, see
Installing and configuring the forwarder on Linux
.
The following is an example of a Google Security Operations forwarder configuration:
- syslog:
      common:
        enabled: true
        data_type: CISCO_ASA_FIREWALL
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 192.0.2.1:10514
      connection_timeout_sec: 60
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
Supported Cisco ASA firewall log formats
The Cisco ASA firewall parser supports logs in SYSLOG format.
Supported Cisco ASA firewall sample logs
SYSLOG:
<163>Nov 03 2021 10:10:13 hostname : %ASA-3-212011: SNMP engineBoots is set to maximum value. Reason: error accessing persistent data. User intervention necessary
Field mapping reference
This section explains how the parser applies grok patterns to
map Cisco ASA firewall message IDs to Google Security Operations UDM fields. You can use
grok patterns to create predefined patterns in addition to regular expressions
to match log messages and extract values into tokens from the log message.
Mapping conditions
The following table lists the mapping conditions used to determine the UDM field
for some of the commonly used fields, and example logs:
Common log fields
Mapping conditions
Examples
src_ip
if src_ip holds hostname then it is mapped to 'principal.hostname',
else
"principal.ip" is set to "src_ip"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302013: Built inbound TCP
     connection 3124260595 for trans-vrf:xyzhost/40297 (192.0.2.1/xxxxx) to qat-vrf:198.51.100.1/xxxxx
     (198.51.100.1/xxxxx)','tagCountry':'US'}
dst_ip
if dst_ip holds hostname then it is mapped to 'target.hostname',
else
"target.ip" is set to "dst_ip"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302014: Teardown TCP
     connection 3124210259 for trans-vrf:203.0.113.1/xxxx to qat-vrf:192.0.2.1/xxxxx
     duration 0:00:29 bytes 9190 TCP FINs','tagCountry':'US'}"
direction
if 'src_interface_name' != 'dst_interface_name' and
if [src_interface_name] == "OUTSIDE" or [dst_interface_name] in ["INSIDE", "DMZ"]
     then, "event.idm.read_only_udm.network.direction" is set to "INBOUND"
else if [src_interface_name] in ["INSIDE", "DMZ"] or [dst_interface_name] == "OUTSIDE"
     then, "event.idm.read_only_udm.network.direction" is set to "OUTBOUND"
else if [src_interface_name] =~ "INT" or [dst_interface_name] =~ "EXT" then, "event.idm.
     read_only_udm.network.direction" is set to "OUTBOUND"
else if [src_interface_name] =~ "EXT" or [dst_interface_name] =~ "INT" then, "event.idm.
     read_only_udm.network.direction" is set to "INBOUND"
if [cisco_message_number] == "302021" then, "event.idm.read_only_udm.network.direction"
     is set to "OUTBOUND"
if [cisco_message_number] in ["106016", "106017", "106021", "402116"] then, "event.idm.read_only_udm.network.direction" is set to "INBOUND"
{'Message':'2021-12-21T23:50:49-08:00 ecnp01094fe03 : %ASA-4-106023: Deny tcp src Outside:
     192.0.2.1/xxxxx dst Inside:198.51.100.1/xxxxx by access-group "OutsideToInside" [0x0, 0x0]','tagCountry':'US'}"
Here, direction is INBOUND.
src_mapped_ip
if [src_mapped_ip] != [src_ip] then, merge "principal.ip" is set to "src_mapped_ip"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302013: Built inbound TCP
     connection 3124260595 for trans-vrf:xyzhost/40297 (192.0.2.1/xxxxx)
     to qat-vrf:198.51.100.1/xxxxx (198.51.100.1/xxxxx)','tagCountry':'US'}
dst_mapped_ip
if [dst_mapped_ip] != [dst_ip] then, merge "target.ip" is set to "dst_mapped_ip"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302013: Built inbound TCP connection
     3124260595 for trans-vrf:xyzhost/40297 (203.0.113.1/xxxxx) to qat-vrf:198.51.100.1/xxxxx
     (198.51.100.1/xxxxx)','tagCountry':'US'}198.51.100.1
category
if [category] == "Clustering" then "target.resource.resource_type" is set to "CLUSTER"
None
security_description
if [cisco_message_number] in ["212001","212002"] and
if error_code is 1, then "security_description" is set to "1 - ASA cannot open the SNMP transport for the interface."
if [cisco_message_number] == "212003" and
if error_code is 1, then "security_description" is set to "1 - ASA cannot find a supported transport type for the interface.",
if error_code is 5, then "security_description" is set to "5 - ASA received no data from the UDP channel for the interface.",
if error_code is 7, then "security_description" is set to "7 - ASA received an incoming request that exceeded the supported buffer size.",
if error_code is 14, then "security_description" is set to "14 - ASA cannot determine the source IP address from the UDP channel.",
if error_code is 22, then "security_description" is set to "22 - ASA received an invalid parameter."
if [cisco_message_number] == "212004" and
if error_code is 1, then "security_description" is set to "1 - ASA cannot find a supported transport type for the interface.",
if error_code is 2, then "security_description" is set to "2 - ASA sent an invalid parameter.",
if error_code is 3, then "security_description" is set to "3 - ASA was unable to set the destination IP address in the UDP channel.",
if error_code is 4, then "security_description" is set to "4 - ASA sent a PDU length that exceeded the supported UDP segment size.",
if error_code is 5, then "security_description" is set to "5 - ASA was unable to allocate a system block to construct the PDU."
None
src_fwuser
if [src_username] == "" and [src_fwuser] != "", then mapped "src_fwuser" with "principal.user.userid"
<174>Dec 21 2021 23:52:18: %ASA-6-602303: IPSEC: An outbound LAN-to-LAN SA
     (SPI= 0x20211643) between 198.51.100.1 and 192.0.2.1(user= 192.0.2.1) has been created.
dst_fwuser
if [user_name] == "" and [dst_fwuser] != "", then mapped "dst_fwuser" with "target.user.userid"
<166>Dec 22 01:56:14 enal-fw1 : %ASA-6-315011: SSH session from 192.0.2.1 on
     interface inside for user "*****" disconnected by SSH server, reason: "Internal error"(0x00)
src_port
"src_port" is set to "principal.port"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302013: Built inbound TCP
     connection 3124260595 for trans-vrf:xyzhost/40297 (192.0.2.1/xxxxx) to
     qat-vrf:198.51.100.1/xxxxx (198.51.100.1/xxxxx)','tagCountry':'US'}
action
if [action] =~ "(built|permitted|succeeded|accept|successful|created|received|passed|
     est-allowed|up|granted)" then "security_result.action" is set to "ALLOW"
else if [action] =~ "(deny|denied|denied by acl|shunned|dropped|rejected|no matching connection
     |invalid|terminated|terminating|deleted|discarded|rejecting|deleting|rejected|reset|dropping|
     teardown|down|restricted)" then "security_result.action" is set to "BLOCK"
else if [action] =~ "(failure|failed)" then "security_result.action" is set to "FAIL"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302013: Built inbound TCP connection
     3124260595 for trans-vrf:xyzhost/40297 (192.0.2.1/xxxxx) to qat-vrf:198.51.100.1/xxxxx
     (198.51.100.1/xxxxx)','tagCountry':'US'}
target_platform
if [target_platform] =~ /(?i)win/, then "target.platform" is set to "WINDOWS"
else if [target_platform] =~ /(?i)linux/, then "target.platform" is set to "LINUX"
else if [target_platform] =~ /(?i)mac/ or [target_platform] =~ /(?i)osx/, then "target.platform" is set to "MAC"
None
protocol
For protocol enum value mapping we have used @include["parse_ip_protocol.include"]
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302014: Teardown TCP connection
     3124210259 for trans-vrf:192.0.2.1/xxxx to qat-vrf:198.51.100.1/xxxxx
     duration 0:00:29 bytes 9190 TCP FINs','tagCountry':'US'}"
application_protocol
For application_protocol enum value mapping we have used @include["parse_app_protocol.include"]
<162>%ASA-2-106007: Deny inbound UDP from 198.51.100.1/xxxxx to 192.0.2.1/xx due to DNS Query
dst_port
"dst_port" is set to "target.port"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302014: Teardown TCP
     connection 3124210259 for trans-vrf:192.0.2.1/xxxx to qat-vrf:198.51.100.1/xxxxx
     duration 0:00:29 bytes 9190 TCP FINs','tagCountry':'US'}"
cisco_severity
if [cisco_severity] == "1"
"security_result.severity" is set to "HIGH"
"security_result.severity_details" is set to "Immediate action needed"
else if [cisco_severity] == "2"
"security_result.severity" is set to "HIGH"
"security_result.severity_details" is set to "Critical condition"
else if [cisco_severity] == "3" {
"security_result.severity" is set to "ERROR"
"security_result.severity_details" is set to "Error condition"
else if [cisco_severity] == "4" {
"security_result.severity" is set to "LOW"
"security_result.severity_details" is set to "Warning condition"
else if [cisco_severity] == "5" {
"security_result.severity" is set to "LOW"
"security_result.severity_details" is set to "Normal but significant condition"
else if [cisco_severity] == "6" {
"security_result.severity" is set to "INFORMATIONAL"
"security_result.severity_details" is set to "Informational message only"
{'Message':'2021-12-21T23:50:49-08:00 QAT : %ASA-6-302014: Teardown TCP
     connection 3124210259 for trans-vrf:198.51.100.1/xxxx to qat-vrf:192.0.2.1/xxxxx duration 0:00:29 bytes 9190 TCP FINs','tagCountry':'US'}"
asa_device_ip
"asa_device_ip" is set to "observer.ip"
<163>198.50.100.0 %ASA-3-202010: PAT pool exhausted. Unable to create UDP connection from 198.50.100.2/63201 to 198.50.100.1/443
Field mapping reference: Cisco ASA firewall event IDs to UDM fields
The following table lists the message IDs, grok patterns, and corresponding UDM fields:
Message IDs
Grok pattern
UDM field
103001
((Primary|Secondary|ASA)) No response from other firewall (reason code = {reason_code})
reason_code is set to about.labels.key/value
103002, 103003
((Primary|Secondary|ASA)) Other firewall network interface {interface_number} <message_text>
interface_number is set to about.labels.key/value
103004
((Primary|Secondary|ASA)) Other firewall reports this firewall failed. Reason: {summary}
summary is set to security_result.summary
103005
((Primary|Secondary|ASA)) Other firewall reporting failure. Reason: {summary}
summary is set to security_result.summary
103006, 103007
((Primary|Secondary|ASA)) Mate version {target_version_num} is not <message_text> with ours {principal_version_num}
target_version_num is set to target.labels.key/value, principal_version_num is set to principal.labels.key/value
104001, 104002, 104500, 104501
((Primary|Secondary|ASA)) Switching to {role} (cause: {summary})
((Primary|Secondary|ASA)) Switching to {role} - {cause}
role is set to about.labels.key/value, summary is set to security_result.summary
105003, 105004
(<message_text>) Monitoring on interface {interface_name} <message_text>
interface_name is set to about.labels.key/value
105005
(<message_text>) Lost Failover communications with mate on interface {interface_name}
interface_name is set to about.labels.key/value
105006, 105007
((Primary|Secondary|ASA)) Link status <message_text> on interface {interface_name}
interface_name is set to about.labels.key/value
105008
(<message_text>) Testing interface {interface_name}
interface_name is set to about.labels.key/value
105009
(<message_text>) Testing on interface {interface_name} <message_text>
interface_name is set to about.labels.key/value
105021
({failover_unit}) Standby unit failed to sync due to a locked {context_name} config. Lock held by {lock_owner_name}
failover_unit is set to about.labels.key/value, context_name is set to about.labels.key/value, lock_owner_name is set to about.labels.key/value
105044
((Primary|Secondary|ASA)) Mate operational mode {target_mode} is not compatible with my mode {principal_mode}
target_mode is set to target.labels.key/value, principal_mode is set to principal.labels.key/value
105045
((Primary|Secondary|ASA)) Mate license ({target_license}) is not compatible with my license ({principal_license})
target_license is set to target.labels.key/value, principal_license is set to principal.labels.key/value
105047
Mate has a {target_io_card_name} card in slot {slot_number} which is different from my {principal_io_card_name}
target_io_card_name is set to target.labels.key/value, slot_number is set to about.labels.key/value, principal_io_card_name is set to principal.labels.key/value
105048
({unit_name}) Mate's service module ({target_service}) is different from mine ({src_service})
unit_name is set to about.labels.key/value, target_service is set to target.application, src_service is set to principal.application
105502
((Primary|Secondary|ASA)) Restarting Cloud HA on this unit, reason: {summary}
summary is set to security_result.summary
105503
((Primary|Secondary|ASA)) Internal state change from {previous_state} to {new_state}
previous_state is set to about.labels.key/value, new_state is set to about.labels.key/value
105504
((Primary|Secondary|ASA)) Connected to peer {dst_ip}:{dst_port}
dst_ip is set to target.ip, dst_port is set to target.port
105505
((Primary|Secondary|ASA)) Failed to connect to peer unit {dst_ip}:{dst_port}
dst_ip is set to target.ip, dst_port is set to target.port
105506, 105507
((Primary|Secondary|ASA)) Unable to <message_text> socket on port {dst_port} for <message_text>, error: {error}
dst_port is set to target.port, error is set to about.labels.key/value
105508
((Primary|Secondary|ASA)) Error creating failover connection socket on port {dst_port}
dst_port is set to target.port
105509
((Primary|Secondary|ASA)) Error sending {message_name} message to peer unit {dst_ip}, error: {error}
message_name is set to about.labels.key/value, dst_ip is set to target.ip, error is set to about.labels.key/value
105510
((Primary|Secondary|ASA)) Error receiving message from peer unit {dst_ip}, error: {error}
dst_ip is set to target.ip, error is set to about.labels.key/value
105511
((Primary|Secondary|ASA)) Incomplete read of message header of message from peer unit {dst_ip}: bytes {received_bytes} read of expected {header_length} <message_text>
dst_ip is set to target.ip, received_bytes is set to network.received_bytes, header_length is set to about.labels.key/value
105512
((Primary|Secondary|ASA)) Error receiving message body of message from peer unit {dst_ip}, error: {error}
dst_ip is set to target.ip, error is set to about.labels.key/value
105513
((Primary|Secondary|ASA)) Incomplete read of message body of message from peer unit {dst_ip}: bytes {received_bytes} read of expected {message_length} <message_text>
dst_ip is set to target.ip, received_bytes is set to network.received_bytes, message_length is set to about.labels.key/value
105514
((Primary|Secondary|ASA)) Error occurred when responding to {message_name} message received from peer unit {dst_ip}, error: {error}
message_name is set to about.labels.key/value, dst_ip is set to target.ip, error is set to about.labels.key/value
105515
((Primary|Secondary|ASA)) Error receiving {message_name} message from peer unit {dst_ip}, error: {error}
message_name is set to about.labels.key/value, dst_ip is set to target.ip, error is set to about.labels.key/value
105516
((Primary|Secondary|ASA)) Incomplete read of message header of {message_name} message from peer unit {dst_ip}: bytes {received_bytes} read of expected {header_length} <message_text>
message_name is set to about.labels.key/value, dst_ip is set to target.ip, received_bytes is set to network.received_bytes, header_length is set to about.labels.key/value
105517
((Primary|Secondary|ASA)) Error receiving message body of {message_name} message from peer unit {dst_ip}, error: {error}
message_name is set to about.labels.key/value, dst_ip is set to target.ip, error is set to about.labels.key/value
105518
((Primary|Secondary|ASA)) Incomplete read of message body of {message_name} message from peer unit {dst_ip}: bytes {received_bytes} read of expected {message_length} <message_text>
message_name is set to about.labels.key/value, dst_ip is set to target.ip, received_bytes is set to network.received_bytes, message_length is set to about.labels.key/value
105519
((Primary|Secondary|ASA)) Invalid response to {message_name} message received from peer unit {dst_ip}: type {message_type}, version {message_version}, length {message_length}
message_name is set to about.labels.key/value, dst_ip is set to target.ip, message_type is set to about.labels.key/value, message_version is set to about.labels.key/value, message_length is set to about.labels.key/value
105522
((Primary|Secondary|ASA)) Updating route {route_table_name}
route_table_name is set to about.labels.key/value
105523
((Primary|Secondary|ASA)) Updated route {route_table_name}
route_table_name is set to about.labels.key/value
105526
((Primary|Secondary|ASA)) Unexpected status in response to access token request: {status}
status is set to about.labels.key/value
105531
((Primary|Secondary|ASA)) Failed to obtain route-table information needed for change request for route-table {route_table_name}
route_table_name is set to about.labels.key/value
105532
((Primary|Secondary|ASA)) Unexpected status in response to route-table change request for route-table {route_table_name}: {status}
route_table_name is set to about.labels.key/value, status is set to about.labels.key/value
105533
((Primary|Secondary|ASA)) Failure reading response to route-table change request for route-table {route_table_name}
route_table_name is set to about.labels.key/value
105534
((Primary|Secondary|ASA)) No provisioning state in response to route-table change request route-table {route_table_name}
route_table_name is set to about.labels.key/value
105535
((Primary|Secondary|ASA)) No response to route-table change request for route-table {route_table_name} from
route_table_name is set to about.labels.key/value
105536
((Primary|Secondary|ASA)) Failed to obtain Azure authentication header for route status request for route {route_name}
route_name is set to about.labels.key/value
105537
((Primary|Secondary|ASA)) Unexpected status in response to route state request for route {route_name}: {status}
route_name is set to about.labels.key/value, status is set to about.labels.key/value
105538
((Primary|Secondary|ASA)) Failure reading response to route state request for route {route_name}
route_name is set to about.labels.key/value
105539
((Primary|Secondary|ASA)) No response to route state request for route {route_name} from <message_text>
route_name is set to about.labels.key/value
105541
((Primary|Secondary|ASA)) Failed to update route-table {route_table_name}, provisioning state: {state_string}
route_table_name is set to about.labels.key/value, state_string is set to about.labels.key/value
105545
((Primary|Secondary|ASA)) Error starting load balancer probe socket on port {src_port}, error code: {internal_error_code}
src_port is set to principal.port, internal_error_code is set to about.labels.key/value
106001
(?P<direction>Inbound) (?P<protocol>TCP) connection {action} from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} flags {flag} on interface {interface_name}
direction is set to network.direction, protocol is set to network.ip_protocol, action is set to security_result.action, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, flag is set to about.labels.key/value, interface_name is set to about.labels.key/value
106002
{protocol} Connection {action} by {direction} list {acl_id} src {src_ip} dest {dst_ip}
protocol is set to network.ip_protocol, action is set to security_result.action, direction is set to network.direction, acl_id is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
106006
(?P<action>Deny) (?P<direction>inbound) (?P<protocol>UDP) from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
106007
(?P<action>Deny) (?P<direction>inbound) (?P<protocol>UDP) from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} due to {application_protocol} (?P<tag>Query|Response)
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, , src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, application_protocol is set to network.application_protocol
106010
(?P<action>Deny) (?P<direction>inbound) {protocol}<message_text>src {src_interface_name}:{src_ip}(/{src_port})? dst {dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
106011
(?P<action>Deny) (?P<direction>inbound) <message_text> protocol src {src_interface_name}:{src_ip}(/{src_port})? dst {dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, direction is set to network.direction, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
106012
(?P<action>Deny) IP from {src_ip} to {dst_ip}, IP options{ip_options}
action is set to security_result.action, src_ip is set to principal.ip, dst_ip is set to target.ip, ip_options is set to about.labels.key/value
106013
(?P<action>Dropping) echo request from {src_ip} to PAT address {dst_ip}
action is set to security_result.action, src_ip is set to principal.ip, dst_ip is set to target.ip
106014
(?P<action>Deny) (?P<direction>inbound) (?P<protocol>ICMP|icmp) src {src_interface_name}:{src_ip}<message_text>dst {dst_interface_name}:{dst_ip}<message_text>(type {icmp_type}, code {icmp_code})
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value
106015
(?P<action>Deny) (?P<protocol>TCP) <message_text> from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} flags {tcp_flags} on interface {interface_name}
action is set to security_result.action, protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, tcp_flags is set to about.labels.key/value, interface_name is set to about.labels.key/value
106016
(?P<action>Deny) IP spoof from ({src_ip}) to {dst_ip} on interface {interface_name}
action is set to security_result.action, src_ip is set to principal.ip, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
"security_result.category" is set to "NETWORK_SUSPICIOUS"
"network.direction" is set to "INBOUND"
106017
(?P<action>Deny) IP due to Land Attack from {src_ip} to {dst_ip}
action is set to security_result.action, src_ip is set to principal.ip, dst_ip is set to target.ip
"security_result.category" is set to "NETWORK_SUSPICIOUS"
"network.direction" is set to "INBOUND"
106018
(?P<protocol>ICMP|icmp) packet type {icmp_type} denied by outbound list {acl_id} src {src_ip} dest {dst_ip}
protocol is set to network.ip_protocol, icmp_type is set to about.labels.key/value, acl_id is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
106020
(?P<action>Deny) IP teardrop fragment (size={received_bytes}, offset={offset}) from {src_ip} to {dst_ip}
action is set to security_result.action, received_bytes is set to network.received_bytes, offset is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
106021
(?P<action>Deny) {protocol} reverse path check from {src_ip} to {dst_ip} on interface {interface_name}
action is set to security_result.action, protocol is set to network.ip_protocol, src_ip is set to principal.ip, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
"security_result.category" is set to "NETWORK_SUSPICIOUS"
"network.direction" is set to "INBOUND"
106022
(?P<action>Deny) {protocol} connection spoof from {src_ip} to {dst_ip} on interface {interface_name}
action is set to security_result.action, protocol is set to network.ip_protocol, src_ip is set to principal.ip, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
106023
(?P<action>Deny) (protocol )?{protocol} src {src_interface_name}:{src_ip}(/{src_port})?<message_text>dst {dst_interface_name}:{dst_ip}((/|.){dst_port})?( (type {icmp_type}, code {icmp_code}))?<message_text>by access-group \?{policy_id}\"? {hashcode1}, {hashcode2}]"
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value, policy_id is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
106025, 106026
Failed to determine the security context for the packet:<message_text>:{src_ip} {dst_ip} {src_port} {dst_port} protocol
src_ip is set to principal.ip, dst_ip is set to target.ip, src_port is set to principal.port, dst_port is set to target.port
106027
{acl_id}: (?P<action>Deny) src {src_ip} dst {dst_ip} by access-group \{access_list_entry}\""
action is set to security_result.action, acl_id is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, access_list_entry is set to about.labels.key/value
106027
(?P<action>Deny)<message_text>src<message_text>:{src_ip} dst<message_text>:{dst_ip} by access-group \{access_list_entry}\""
action is set to security_result.action, src_ip is set to principal.ip, dst_ip is set to target.ip, access_list_entry is set to about.labels.key/value
106102
access-list {acl_id} (?P<action>permitted|denied) {protocol} for user {user_name} {src_interface_name}/{src_ip}({src_port})<message_text> -> {dst_interface_name}/{dst_ip}({dst_port})<message_text>hit-cnt {hit_count} (?P<tag>first hit|<message_text>-second interval) {hashcode1}, {hashcode2}]
action is set to security_result.action, , acl_id is set to about.labels.key/value, protocol is set to network.ip_protocol, user_name is set to target.user.userid, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
106102
access-list {acl_id} (?P<action>permitted|denied) {protocol} for user {user_name} {src_interface_name}/{src_ip}({src_port})<message_text>{dst_interface_name}/{dst_ip}({dst_port})<message_text>hit-cnt {hit_count} (?P<tag>first hit|<message_text>-second interval) {hashcode1}, {hashcode2}]
action is set to security_result.action, , acl_id is set to about.labels.key/value, protocol is set to network.ip_protocol, user_name is set to target.user.userid, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
106100
access-list {acl_id} (?P<action>permitted|denied|est-allowed) {protocol} {src_interface_name}/{src_ip}({src_port})<message_text> -> {dst_interface_name}/{dst_ip}({dst_port})<message_text>hit-cnt {hit_count} (?P<tag>first hit|<message_text>-second interval) {hashcode1}, {hashcode2}]
action is set to security_result.action, , acl_id is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
106100
access-list {acl_id} (?P<action>permitted|denied|est-allowed) {protocol} {src_interface_name}/{src_ip}({src_port})<message_text>{dst_interface_name}/{dst_ip}({dst_port})<message_text>hit-cnt {hit_count} (?P<tag>first hit|<message_text>-second interval) {hashcode1}, {hashcode2}]
action is set to security_result.action, , acl_id is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
106101
Number of cached deny-flows for ACL log has reached limit ({limit})
limit is set to about.labels.key/value
106103
access-list {acl_id} (?P<action>denied) {protocol} for user {user_name} {src_interface_name}/{src_ip}({src_port})<message_text> -> {dst_interface_name}/{dst_ip}({dst_port})<message_text>hit-cnt {hit_count} {hashcode1}, {hashcode2}]
action is set to security_result.action, acl_id is set to about.labels.key/value, protocol is set to network.ip_protocol, user_name is set to target.user.userid, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
106103
access-list {acl_id} (?P<action>denied) {protocol} for user {user_name} {src_interface_name}/{src_ip}({src_port})<message_text>{dst_interface_name}/{dst_ip}({dst_port})<message_text>hit-cnt {hit_count} {hashcode1}, {hashcode2}]
action is set to security_result.action, acl_id is set to about.labels.key/value, protocol is set to network.ip_protocol, user_name is set to target.user.userid, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value, hashcode1 is set to about.labels.key/value, hashcode2 is set to about.labels.key/value
107001
(?P<application_protocol>RIP) auth failed from {dst_ip}: version={version_number}, type={type}, mode={mode}, sequence={sequence_number} on interface {interface_name}
application_protocol is set to network.application_protocol, dst_ip is set to target.ip, version_number is set to about.labels.key/value, type is set to about.labels.key/value, mode is set to about.labels.key/value, sequence_number is set to about.labels.key/value, interface_name is set to about.labels.key/value
107002
(?P<application_protocol>RIP) pkt failed from {dst_ip}: version={version_number} on interface {interface_name}
application_protocol is set to network.application_protocol, dst_ip is set to target.ip, version_number is set to about.labels.key/value, interface_name is set to about.labels.key/value
108002
(?P<application_protocol>SMTP) replaced string: out {src_ip} in {dst_ip} data: {summary}
application_protocol is set to network.application_protocol, src_ip is set to principal.ip, dst_ip is set to target.ip, summary is set to security_result.summary
108003
Terminating ESMTP/SMTP connection; malicious pattern detected in the mail address from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}. Data:{summary}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
108004
{action_class}: {action} ESMTP <message_text> from {src_interface_name}:{src_ip} to {dst_interface_name}:{dst_ip};{summary}
action_class is set to about.labels.key/value, action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, summary is set to security_result.summary
108005
{action_class}: Received ESMTP <message_text> from {src_interface_name}:{src_ip} to {dst_interface_name}:{dst_ip};{summary}
action_class is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, summary is set to security_result.summary
108007
TLS started on ESMTP session between client {src_interface_name}:{src_ip}(/{src_port})? and server {dst_interface_name}:{dst_ip}(/{dst_port})?
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
109001
Auth start for user {user_name} from {src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
user_name is set to target.user.userid, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
109002
Auth from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} failed (server {src_ip} failed) on interface {interface_name}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, interface_name is set to about.labels.key/value
109003
Auth from {src_ip} to {dst_ip}/{dst_port} failed (all servers failed) on interface {interface_name}, so marking all servers ACTIVE again
src_ip is set to principal.ip, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
109005, 109006, 109007
Authentication (?P<action>succeeded|failed|permitted|denied) for user {user_name} from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
action is set to security_result.action, user_name is set to target.user.userid, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
109007
Authorization (?P<action>permitted) for user {user_name} from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
action is set to security_result.action, user_name is set to target.user.userid, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
109008
Authorization (?P<action>denied) for user {user_name} from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
action is set to security_result.action, user_name is set to target.user.userid, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
109010
Auth from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} failed (too many pending auths) on interface {interface_name}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
109011
Authen Session Start: user {user_name}, sid {sid}
user_name is set to target.user.userid, sid is set to about.labels.key/value
109012
Authen Session End: user {user_name}, sid {sid}, elapsed {elapsed_number_seconds} seconds
user_name is set to target.user.userid, sid is set to about.labels.key/value, elapsed_number_seconds is set to about.labels.key/value
109016
Can't find authorization ACL {acl_id} for user {user_name}
acl_id is set to about.labels.key/value, user_name is set to target.user.userid
109017
User at {dst_ip} exceeded auth proxy connection limit
dst_ip is set to target.ip
109018
Downloaded ACL {acl_id} is empty
acl_id is set to about.labels.key/value
109019
Downloaded ACL {acl_id} has parsing error; ACE
acl_id is set to about.labels.key/value
109023
User from {src_ip}/{src_port} to {dst_ip}/{dst_port} on interface {interface_name} must authenticate before using this service
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
109024
Authorization (?P<action>denied) from {src_ip}/{src_port} to {dst_ip}/{dst_port} (not authenticated) on interface {interface_name} using {protocol}
action is set to security_result.action, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value, protocol is set to network.ip_protocol
109025
Authorization (?P<action>denied) (acl={acl_id}) for user {user_name} from {src_ip}/{src_port} to {dst_ip}/{dst_port} on interface {interface_name} using {protocol}
action is set to security_result.action, acl_id is set to about.labels.key/value, user_name is set to target.user.userid, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value, protocol is set to network.ip_protocol
109027
Unable to decipher response message Server = {dst_ip}, User = {user_name}
dst_ip is set to target.ip, user_name is set to target.user.userid
109028
aaa bypassed for same-security traffic from {ingress_interface}:{src_ip}/{src_port} to {egress_interface}:{dst_ip}/{dst_port}
ingress_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, egress_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
109029
Parsing downloaded ACL: {error}
error is set to about.labels.key/value
109030
Autodetect ACL convert wildcard did not convert ACL {access_list} {src_ip}|{dst_ip} netmask {subnet_mask}
access_list is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, subnet_mask is set to about.labels.key/value
109031
NT Domain Authentication Failed: rejecting guest login for {user_name}
user_name is set to target.user.userid
109032
Unable to install ACL {access_list}, downloaded for user {user_name}; Error in ACE: {access_list_entry}
access_list is set to about.labels.key/value, user_name is set to target.user.userid, access_list_entry is set to about.labels.key/value
109033
Authentication {action} for admin user {user_name} from {dst_ip}. Interactive challenge processing is not supported for {protocol} connections
action is set to security_result.action, user_name is set to target.user.userid, dst_ip is set to target.ip, protocol is set to network.ip_protocol
109034
Authentication {action} for network user {user_name} from {src_ip}/{src_port} to {dst_ip}/{dst_port}. Interactive challenge processing is not supported for {protocol} connections
action is set to security_result.action, user_name is set to target.user.userid, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, protocol is set to network.ip_protocol
109035
Exceeded maximum number ({max_num}) of DAP attribute instances for user {user_name}
max_num is set to about.labels.key/value, user_name is set to target.user.userid
109036, 109037
Exceeded <message_text> attribute values for the {attribute_name} attribute for user {user_name}
attribute_name is set to about.labels.key/value, user_name is set to target.user.userid
109038
Attribute {attribute_name} value {string_from_server} from AAA server could not be parsed as a {type}
attribute_name is set to about.labels.key/value, string_from_server is set to about.labels.key/value, type is set to about.labels.key/value
109039
AAA Authentication:Dropping an unsupported <message_text> packet from {ingress_interface}:{src_ip} to {egress_interface}:{dst_ip}
ingress_interface is set to about.labels.key/value, src_ip is set to principal.ip, egress_interface is set to about.labels.key/value, dst_ip is set to target.ip
109040
User at {src_ip} exceeded auth proxy rate limit of 10 connections/sec
src_ip is set to principal.ip
109100
Received CoA update from {dst_ip} for user {user_name}, with session ID(:)? {session_id}, changing authorization attributes
dst_ip is set to target.ip, user_name is set to target.user.userid, session_id is set to network.session_id
109101
Received CoA disconnect request from {dst_ip} for user {user_name}, with audit-session-id: {session_id}
dst_ip is set to target.ip, user_name is set to target.user.userid, session_id is set to network.session_id
109102
Received CoA {action_details} from {dst_ip}, but cannot find named session {session_id}
action_details is set to security_result.action_details, dst_ip is set to target.ip, session_id is set to network.session_id
109103
CoA {action_details} from {dst_ip} failed for user {user_name}, with session ID: {session_id}
action_details is set to security_result.action_details, dst_ip is set to target.ip, user_name is set to target.user.userid, session_id is set to network.session_id
109104
CoA {action_details} from {dst_ip} failed for user {user_name}, session ID: {session_id}. Action not supported
action_details is set to security_result.action_details, dst_ip is set to target.ip, user_name is set to target.user.userid, session_id is set to network.session_id
109105
Failed to determine the egress interface for locally generated traffic destined to <{protocol}><{dst_ip}>:<{dst_port}>
protocol is set to network.ip_protocol, dst_ip is set to target.ip, dst_port is set to target.port
110002
Failed to locate egress interface for( <message_text>-)?{protocol} from {src_interface_name}:{src_ip}/{src_port} to {dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
110003
Routing failed to locate next hop for {protocol} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
110004
Egress interface changed from {old_interface_name} to {new_interface_name} on {protocol} connection {session_id} for <message_text> :{dst_ip}/{dst_port} (<message_text>) to <message_text> :{src_ip}/{src_port} (<message_text>)
old_interface_name is set to about.labels.key/value, new_interface_name is set to about.labels.key/value, protocol is set to network.ip_protocol, session_id is set to network.session_id, dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
111001
Begin configuration: {dst_ip} writing to <message_text>
dst_ip is set to target.ip
111002, 111007
Begin configuration: {dst_ip} reading from <message_text>
dst_ip is set to target.ip
111003
{dst_ip} Erase configuration
dst_ip is set to target.ip
111004, 111005
{dst_ip} end configuration:
dst_ip is set to target.ip
111008
User {user_name} executed the {command} command
user_name is set to target.user.userid, command is set to target.process.command_line
111010
User {user_name}, running {target_service} from IP {src_ip}, executed {command}
user_name is set to target.user.userid, target_service is set to target.application, src_ip is set to principal.ip, command is set to target.process.command_line
"target.resource.resource_type" is set to "SETTING"
113003
AAA group policy for user {user_name} is being set to {policy_name}
user_name is set to target.user.userid, policy_name is set to target.resource.name
113004
AAA user <message_text> {action} : server ={dst_ip}<message_text>user = {user_name}
action is set to security_result.action, dst_ip is set to target.ip, user_name is set to target.user.userid
113005
AAA user (authorization|authentication) {action} : reason = {summary} : server = {src_ip}: user = {user_name}(: user IP = {dst_ip})?
action is set to security_result.action, summary is set to security_result.summary, src_ip is set to principal.ip, user_name is set to target.user.userid, dst_ip is set to target.ip
113006
User {user_name} locked out on exceeding {failed_attempts} successive failed authentication attempts
user_name is set to target.user.userid, failed_attempts is set to about.labels.key/value
113007
User {user_name} unlocked by {administrator}
user_name is set to target.user.userid, administrator is set to about.labels.key/value
113008
AAA transaction status ACCEPT: user = {user_name}
user_name is set to target.user.userid
"auth_type" is set to "VPN"
113009
AAA retrieved default group policy {group_policy} for user {user_name}
group_policy is set to about.labels.key/value, user_name is set to target.user.userid
113010
AAA challenge received for user {user_name} from server {src_ip}
user_name is set to target.user.userid, src_ip is set to principal.ip
113011
AAA retrieved user specific group policy {group_policy} for user {user_name}
group_policy is set to about.labels.key/value, user_name is set to target.user.userid
113012
AAA user authentication Successful: local database: user = {user_name}
user_name is set to target.user.userid
113013
AAA unable to complete the request Error: reason = {summary}: user = {user_name}
summary is set to security_result.summary, user_name is set to target.user.userid
113014
AAA (authorization|authentication) server not accessible: server ={src_ip}: user = {user_name}
src_ip is set to principal.ip, user_name is set to target.user.userid
113015
AAA user authentication Rejected: reason = {summary}: local database: user = {user_name}(: user IP = {src_ip})?
summary is set to security_result.summary, user_name is set to target.user.userid, src_ip is set to target.ip, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
113016
AAA credentials rejected: reason = {summary}: server = {src_ip}: user = {user_name}(: user IP = {dst_ip})?
summary is set to security_result.summary, src_ip is set to principal.ip, user_name is set to target.user.userid, dst_ip is set to target.ip
113017
AAA credentials rejected: reason = {summary}: local database: user = {user_name}(: user IP = {dst_ip})?
summary is set to security_result.summary, user_name is set to target.user.userid, dst_ip is set to target.ip
113018
User: {user_name}, Unsupported downloaded ACL Entry: {acl_entry} , Action: {action}
user_name is set to target.user.userid, acl_entry is set to about.labels.key/value, action is set to security_result.action
113019
Group = {group_name}, Username = {user_name}, IP = {dst_ip}, Session disconnected. Session Type: {session_type}, Duration: {duration}, Bytes xmt: {sent_bytes}, Bytes rcv: {received_bytes}, Reason: {summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, session_type is set to about.labels.key/value, duration is set to network.session_duration, sent_bytes is set to network.sent_bytes, received_bytes is set to network.received_bytes, summary is set to security_result.summary
113020
Kerberos error: Clock skew with server {src_ip} greater than 300 seconds
src_ip is set to principal.ip
113021
Attempted console login failed(.)? (user|User) {user_name} did NOT have appropriate Admin Rights
user_name is set to target.user.userid
113022
AAA Marking {protocol}(.)? server {dst_ip} in aaa-server group {group_name} as FAILED
protocol is set to network.ip_protocol, dst_ip is set to target.ip, group_name is set to target.user.group_identifiers
113023
AAA Marking {protocol}(.)? server {dst_ip} in (aaa-&vert;)server group {group_name} as ACTIVE
protocol is set to network.ip_protocol, dst_ip is set to target.ip, group_name is set to target.user.group_identifiers
113024
Group {group_name}: Authenticating {connection} connection from {dst_ip} with username, {user_name}, from client certificate
group_name is set to target.user.group_identifiers, connection is set to about.labels.key/value, dst_ip is set to target.ip, user_name is set to target.user.userid
113025
Group {group_name}: {dn_fields} Could not authenticate {connection} connection from {dst_ip}
group_name is set to target.user.group_identifiers, dn_fields is set to about.labels.key/value, connection is set to about.labels.key/value, dst_ip is set to target.ip
113026
Error {summary} while executing Lua script for group {group_name}
summary is set to security_result.summary, group_name is set to target.user.group_identifiers
113029
Group {group_name} User {user_name} IP {dst_ip} Session could not be established: session limit of {limit} reached
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, limit is set to about.labels.key/value
113030
Group {group_name} User {user_name} IP {dst_ip} User ACL {acl_id} from AAA doesn't exist on the device, (?P<action>terminating) connection
action is set to security_result.action, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, acl_id is set to about.labels.key/value
113031
Group {group_name} User {user_name} IP {dst_ip} AnyConnect vpn-filter {vpn_filter} is an IPv6 ACL; ACL not applied
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, vpn_filter is set to about.labels.key/value
113032
Group {group_name} User {user_name} IP {dst_ip} AnyConnect ipv6-vpn-filter {vpn_filter} is an IPv4 ACL; ACL not applied
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, vpn_filter is set to about.labels.key/value
113033
Group {group_name} User {user_name} IP {dst_ip} AnyConnect session not allowed. ACL parse error
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
113034
Group {group_name} User {user_name} IP {dst_ip} User ACL {acl_id} from AAA ignored, AV-PAIR ACL used instead
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, acl_id is set to about.labels.key/value
113035
Group {group_name} User {user_name} IP {dst_ip} Session terminated: AnyConnect not enabled or invalid AnyConnect image on the ASA
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
113036
Group {group_name} User {user_name} IP {dst_ip} AAA parameter {parameter_name} value invalid
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, parameter_name is set to about.labels.key/value
113038
Group {group_name} User {user_name} IP {dst_ip} Unable to create AnyConnect parent session
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
113039
Group {group_name} User {user_name} IP {src_ip} AnyConnect parent session started
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, src_ip is set to principal.ip, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
113040
Terminating the VPN connection attempt from {attempted_group}. Reason: This connection is group locked to {locked_group}
attempted_group is set to about.labels.key/value, locked_group is set to about.labels.key/value
113041
Redirect ACL configured for {dst_ip} does not exist on the device
dst_ip is set to target.ip
113042
Non-HTTP connection from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}( for user username at {dst_ip1})? (?P<summary>(?P<action>denied) by redirect filter; only HTTP connections are supported for redirection)
summary is set to security_result.summary, action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_ip1 is set to target.ip
113045
AAA SDI server {src_ip} in aaa-server group {group_name}: status changed from {previous_state} to {current_state}
src_ip is set to principal.ip, group_name is set to target.user.group_identifiers, previous_state is set to about.labels.key/value, current_state is set to about.labels.key/value
114001
Failed to initialize 4GE SSM I/O card (error {summary})
summary is set to security_result.summary
114002
Failed to initialize SFP in 4GE SSM I/O card (error {summary})
summary is set to security_result.summary
114003
Failed to run cached commands in 4GE SSM I/O card (error {summary})
summary is set to security_result.summary
114006, 114007, 114009, 114010, 114011, 114012, 114013, 114014, 114015, 114016, 114017, 114018, 114019
Failed to (?P<tag>set mac address table|get port statistics|get current msr|set multicast address|set multicast hardware address|delete multicast address|delete multicast hardware address|set mac address|set mode|set multicast mode|get link status|set port speed|set media type) in 4GE SSM I/O card (error {error})
, error is set to about.labels.key/value
114021, 114022, 114023
Failed to (?P<tag>set multicast address table|pass broadcast traffic|cache/flush mac table) in 4GE SSM I/O card due to {error}
, error is set to about.labels.key/value
115000
Critical assertion in process: {target_process_name} fiber: {fiber_name} , component: {component_name} , subcomponent: {subcomponent_name} , file: {target_file_full_path} , line: {line_number} , cond: {condition}
target_process_name is set to target.process.pid, fiber_name is set to about.labels.key/value, component_name is set to about.labels.key/value, subcomponent_name is set to about.labels.key/value, target_file_full_path is set to target.file.full_path, line_number is set to about.labels.key/value, condition is set to about.labels.key/value
115001
Error in process: {target_process_name} fiber: {fiber_name} , component: {component_name} , subcomponent: {subcomponent_name} , file: {target_file_full_path} , line: {line_number} , cond: {condition}
target_process_name is set to target.process.pid, fiber_name is set to about.labels.key/value, component_name is set to about.labels.key/value, subcomponent_name is set to about.labels.key/value, target_file_full_path is set to target.file.full_path, line_number is set to about.labels.key/value, condition is set to about.labels.key/value
115002
Warning in process: {target_process_name} fiber: {fiber_name} , component: {component_name} , subcomponent: {subcomponent_name} , file: {target_file_full_path} , line: {line_number} , cond: {condition}
target_process_name is set to target.process.pid, fiber_name is set to about.labels.key/value, component_name is set to about.labels.key/value, subcomponent_name is set to about.labels.key/value, target_file_full_path is set to target.file.full_path, line_number is set to about.labels.key/value, condition is set to about.labels.key/value
120003
Process event {event_group} {event_title}
event_group is set to about.labels.key/value, event_title is set to about.labels.key/value
120003
{event_group} is processing <message_text> event {event_title}
event_group is set to about.labels.key/value, event_title is set to about.labels.key/value
120004
Event {event_group} {event_title} is dropped. Reason {summary}
event_group is set to about.labels.key/value, event_title is set to about.labels.key/value, summary is set to security_result.summary
120005
Message {event_group} to (?P<destination_email>) is dropped. Reason {summary}
destination_email is set to security_result.about.email, event_group is set to about.labels.key/value, summary is set to security_result.summary
120005
Message {event_group} to {redirect_url} is dropped. Reason {summary}
event_group is set to about.labels.key/value, redirect_url is set to target.url, summary is set to security_result.summary
120006
Delivering message {event_group} to (?P<destination_email>) failed. Reason {summary}
destination_email is set to security_result.about.email, event_group is set to about.labels.key/value, summary is set to security_result.summary
120006
Delivering message {event_group} to {redirect_url} failed. Reason {summary}
event_group is set to about.labels.key/value, redirect_url is set to target.url, summary is set to security_result.summary
120007
Message {event_group} to (?P<destination_email>) delivered
destination_email is set to security_result.about.email, event_group is set to about.labels.key/value
120007
Message {event_group} to {redirect_url} delivered
event_group is set to about.labels.key/value, redirect_url is set to target.url
120008
SCH client {client_name} is activated
client_name is set to about.labels.key/value
120009
SCH client {client_name} is deactivated
client_name is set to about.labels.key/value
120010
Notify command {action_details} to SCH client {client_name} failed. Reason {summary}
action_details is set to security_result.action_details, client_name is set to about.labels.key/value, summary is set to security_result.summary
120012
User {user_name} chose to {choice} call-home anonymous reporting at the prompt
user_name is set to target.user.userid, choice is set to about.labels.key/value
121001
msgId {message_id}. Telemetry support on the chassis: {status}
message_id is set to about.labels.key/value, status is set to about.labels.key/value
121002
Telemetry support on the blade: {status}
status is set to about.labels.key/value
121003
msgId {message_id}. Telemetry request from the chassis received. SSE connector status: {connector_status}. Telemetry config on the blade: {blade_status}. Telemetry data {data_status}
message_id is set to about.labels.key/value, connector_status is set to about.labels.key/value, blade_status is set to about.labels.key/value, data_status is set to about.labels.key/value
199001
Reload command executed from Telnet (remote {dst_ip})
dst_ip is set to target.ip
199011
Close on bad channel in <message_text> {process_or_fiber}, channel ID {channel_id} , channel state {channel_state} <message_text> name of the process/fiber that caused the bad channel close operation
process_or_fiber is set to about.labels.key/value, channel_id is set to about.labels.key/value, channel_state is set to about.labels.key/value
199012
Stack smash during {new_stack_call} in <message_text> {process_or_fiber}, call target {call_target}, stack size {stack_size},
new_stack_call is set to about.labels.key/value, process_or_fiber is set to about.labels.key/value, call_target is set to target.labels.key/value, stack_size is set to about.labels.key/value
199020
System memory utilization has reached {memory_utilization}%. System will reload if memory usage reaches the configured trigger level of {trigger_level}%
memory_utilization is set to about.labels.key/value, trigger_level is set to about.labels.key/value
199021
System memory utilization has reached the configured watchdog trigger level of {trigger_level}%. System will now reload
trigger_level is set to about.labels.key/value
199027
Restore operation was aborted at {time}
time is set to about.labels.key/value
201002
Too many {protocol} connections on <message_text> {dst_ip} ! {max_embryonic_conn} {max_conn}
protocol is set to network.ip_protocol, dst_ip is set to target.ip, max_embryonic_conn is set to about.labels.key/value, max_conn is set to about.labels.key/value
201003
Embryonic limit exceeded {max_embryonic_conn}/{max_conn} for {dst_ip}/{dst_port} ({dst_ip1}) {dst_ip2}/{dst_port} on {interface_number} {interface_name}
max_embryonic_conn is set to about.labels.key/value, max_conn is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_ip1 is set to target.ip, dst_ip2 is set to target.ip, dst_port is set to target.port, interface_number is set to about.labels.key/value, interface_name is set to about.labels.key/value
201004
Too many {protocol} connections on <message_text> {dst_ip}!{max_udp_conn}
protocol is set to network.ip_protocol, dst_ip is set to target.ip, max_udp_conn is set to about.labels.key/value
201005
{protocol} data connection failed for {dst_ip} {dst_ip1}
protocol is set to network.ip_protocol, dst_ip is set to target.ip, dst_ip1 is set to target.ip
201006
{protocol} backconnection failed for {dst_ip}/{dst_port}
protocol is set to network.ip_protocol, dst_ip is set to target.ip, dst_port is set to target.port
201009
{protocol} connection limit of {max_conn} for host {dst_ip} on {interface_name} exceeded
protocol is set to network.ip_protocol, max_conn is set to about.labels.key/value, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
201010
Embryonic connection limit exceeded {embryonic_conn}/{max_conn} for {direction} packet from {src_ip}/{src_port} to {dst_ip}/{dst_port} on interface {interface_name}
embryonic_conn is set to about.labels.key/value, max_conn is set to about.labels.key/value, direction is set to network.direction, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
201011
Connection limit exceeded {cur_conn_count}/{conf_conn_count} for {direction} packet from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
cur_conn_count is set to about.labels.key/value, conf_conn_count is set to about.labels.key/value, direction is set to network.direction, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
201012
Per-client embryonic connection limit exceeded {cur_num}/{conf_limit} for (input|output) packet from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
cur_num is set to about.labels.key/value, conf_limit is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
201013
Per-client connection limit exceeded {cur_num}/{conf_limit} for (input|output) packet from {src_ip}(/{src_port})? to {dst_ip}/{dst_port} on interface {interface_name}
cur_num is set to about.labels.key/value, conf_limit is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value
202005
Non-embryonic in embryonic list {dst_ip}/{dst_port} {src_ip}/{src_port}
dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
202010
<message_text> pool exhausted( for {pool_name})?.*:{src_ip}/{src_port}.*:{dst_ip}(/{dst_port})?
pool_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
208005
({function}:{line_number}) {summary}
function is set to about.labels.key/value, line_number is set to about.labels.key/value, summary is set to security_result.summary
209003
Fragment database limit of number exceeded: src = {src_ip} , dest = {dst_ip} , proto = {protocol} , id = <message_text>
src_ip is set to principal.ip, dst_ip is set to target.ip, protocol is set to network.ip_protocol
209004
Invalid IP fragment, size = {bytes_exceed} maximum size = {max_bytes} : src = {src_ip} , dest = {dst_ip} , proto = {protocol} , id = <message_text>
bytes_exceed is set to about.labels.key/value, max_bytes is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, protocol is set to network.ip_protocol
209006
Fragment queue threshold exceeded, dropped {protocol}.*{src_ip}/{src_port} to (IP )?{dst_ip}/{dst_port}( on {dst_interface_name})?
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, dst_interface_name is set to target.labels.key/value
210001
LU <message_text> error = {error_number}
error_number is set to about.labels.key/value
210005
LU allocate .* protocol {protocol} connection from ingress interface {src_interface_name}:{src_ip}(/{src_port})? to egress interface {dst_interface_name}:{dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
210005
LU allocate connection failed for {protocol} connection from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
210006
LU look NAT for {dst_ip} failed
dst_ip is set to target.ip
210007
LU allocate xlate failed for <message_text> {protocol} translation from {src_interface_name}:{src_ip}(/{src_port}) ({src_ip1}/{src_port}) to {dst_interface_name}:{dst_ip}/{dst_port} ({dst_ip1}/{dst_port})
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_ip1 is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_ip1 is set to target.ip, dst_port is set to target.port
210008
LU no xlate for {src_ip}(/{src_port})? {dst_ip}(/{dst_port})?
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
210010
LU make {protocol} connection for {dst_ip}:{dst_port} {src_ip}:{src_port}
protocol is set to network.ip_protocol, dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
210020
LU PAT port {dst_port} reserve failed
dst_port is set to target.port
210021
LU create static xlate {dst_ip}
dst_ip is set to target.ip
211004
WARNING: Minimum Memory Requirement for ASA version {image_version} not met for ASA image. <message_text> MB required, <message_text> MB found
image_version is set to about.labels.key/value
212001, 212002
Unable to open {protocol} (trap )?channel ({protocol} port {dst_port}) on interface {interface_number} , error code = {error_code}
protocol is set to network.ip_protocol, protocol is set to network.ip_protocol, dst_port is set to target.port, interface_number is set to about.labels.key/value, error_code is set to security_result.description
212003
Unable to receive an {protocol} request on interface {interface_number} , error code = {error_code}
protocol is set to network.ip_protocol, interface_number is set to about.labels.key/value, error_code is set to security_result.description
212004
Unable to send an {protocol} response to IP (a|A)ddress {dst_ip}Port {dst_port}(I|i)nterface {interface_name}, error code = (-)?{error_code}
protocol is set to network.ip_protocol, dst_ip is set to target.ip, dst_port is set to target.port, interface_name is set to about.labels.key/value, error_code is set to security_result.description
212005
incoming {protocol} request ({received_bytes} bytes) (from IP address {src_ip} Port {src_port})?(on)? (i|I)nterface (")?%{interface_name}(")? exceeds
protocol is set to network.ip_protocol, interface_name is set to about.labels.key/value, received_bytes is mapped to network.received_bytes, src_ip is mapped to principal.ip, src_port is mapped to principal.port
212006
Dropping {protocol} request from {src_ip}(/{src_port})? to ifc :{dst_ip1}/{dst_port} because: {summary} {user_name}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip1 is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary, user_name is set to target.user.userid
212009
Configuration request for {protocol} group {group_name} failed. User {user_name} ,{summary}
protocol is set to network.ip_protocol, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, summary is set to security_result.summary
212010
Configuration request for {protocol} user {user_name} failed. Host {target_hostname} {summary}
protocol is set to network.ip_protocol, user_name is set to target.user.userid, target_hostname is set to target.hostname, summary is set to security_result.summary
212011
{protocol} engineBoots is set to maximum value. Reason: {summary} User intervention necessary
protocol is set to network.ip_protocol, summary is set to security_result.summary
213001
PPTP control daemon socket io {io_string}, errno = {error_string}
io_string is set to about.labels.key/value, error_string is set to about.labels.key/value
213002
PPTP tunnel hashtable insert failed, peer = {dst_ip}
dst_ip is set to target.ip
213003
PPP virtual interface {interface_number} isn't opened
interface_number is set to about.labels.key/value
213004
PPP virtual interface {interface_number} client ip allocation failed
interface_number is set to about.labels.key/value
213007
L2TP: Failed to install Redirect URL:{redirect_url} Redirect ACL: non_exist for {dst_ip}
redirect_url is set to target.url, dst_ip is set to target.ip
214001
Terminating manager session from {dst_ip} on interface {interface_name}. Reason: {summary}
dst_ip is set to target.ip, interface_name is set to about.labels.key/value, summary is set to security_result.summary
215001
Bad route_compress() call, sdb = {sdb}
sdb is set to about.labels.key/value
216001
internal error in: {function}: {summary}
function is set to about.labels.key/value, summary is set to security_result.summary
216002
Unexpected event (major: {major_id}, minor: {minor_id}) received by {task_string} in {function} at line: {line_number}
major_id is set to about.labels.key/value, minor_id is set to about.labels.key/value, task_string is set to about.labels.key/value, function is set to about.labels.key/value, line_number is set to about.labels.key/value
216003
Unrecognized timer {timer_pointer}, {timer_id} received by {task_string} in {function} at line: {line_number}
timer_pointer is set to about.labels.key/value, timer_id is set to about.labels.key/value, task_string is set to about.labels.key/value, function is set to about.labels.key/value, line_number is set to about.labels.key/value
216004
prevented: {error} in {function} at <message_text> - {stack_trace}
error is set to about.labels.key/value, function is set to about.labels.key/value, stack_trace is set to about.labels.key/value
216005
ERROR: Duplex-mismatch on {interface_name} resulted in transmitter lockup. A soft reset of the switch was performed
interface_name is set to about.labels.key/value
218002
Module ({slot}) is a registered proto-type for Cisco Lab use only, and not certified for live network operation
slot is set to about.labels.key/value
218003
Module Version in {slot} is obsolete. The module in slot = <message_text> is obsolete and must be returned via RMA to Cisco Manufacturing. If it is a lab unit, it must be returned to Proto Services for upgrade
slot is set to about.labels.key/value
219002
{api_name} error, slot = {slot_number}, device = {device_number}, address = {address}, byte count = {count}. Reason: {summary}
api_name is set to about.labels.key/value, slot_number is set to about.labels.key/value, device_number is set to about.labels.key/value, address is set to about.labels.key/value, count is set to about.labels.key/value, summary is set to security_result.summary
302003
Built H245 connection for (foreign_address|faddr) {src_ip}(/{src_port})? (local_address|laddr) {dst_ip}(/{dst_port})?
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
302004
Pre-allocate H323 (?P<protocol>UDP) backconnection for (foreign_address|faddr) {src_ip}(/{src_port} )?to (local_address|laddr) {dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
302010
{connections_in_use} in use, {connections_most_used} most used
connections_in_use is set to about.labels.key/value, connections_most_used is set to about.labels.key/value
302012
Pre-allocate H225 Call Signalling Connection for faddr {src_ip}(/{src_port})? to laddr {dst_ip}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip
302013
(?P<action>Built)(?: (?P<direction>Inbound|inbound|Outbound|outbound))? (?P<protocol>TCP)( connection)? {session_id} for {src_interface_name}:{src_ip}/{src_port}( ({src_mapped_ip}/{src_mapped_port}))?(?:({src_fwuser}))? to {dst_interface_name}:{dst_ip}/{dst_port}( ({dst_mapped_ip}/{dst_mapped_port}))?(({dst_fwuser}))?<message_text>
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, dst_fwuser is set to target.user.userid/target.labels.key/value
302014, 302015, 302016
(?P<action>Built|Teardown)(?: (?P<direction>Inbound|inbound|Outbound|outbound))? {protocol} connection {session_id} for {src_interface_name}(:| ){src_ip}/{src_port}( ({src_mapped_interface}?{src_mapped_ip}/{src_mapped_port}))?(?:({src_fwuser}))? to {dst_interface_name}(:| ){dst_ip}/{dst_port}( ({dst_mapped_ip}/{dst_mapped_port}))?(({dst_fwuser}))?(?: duration {duration} bytes {sent_bytes})?<message_text>
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_interface is set to principal.labels.key/value, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, dst_fwuser is set to target.user.userid/target.labels.key/value, duration is set to network.session_duration, sent_bytes is set to network.sent_bytes
302017
Built (?P<direction>inbound|outbound) (?P<protocol>GRE) connection {session_id} from {src_interface_name}:{src_ip} ({src_translated_address}) (?:({src_fwuser}))?to {dst_interface_name}:{dst_ip}/{real_cid} ({dst_translated_address}/{translated_cid})(?:({dst_fwuser}))?<message_text>
direction is set to network.direction, protocol is set to network.ip_protocol, session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_translated_address is set to principal.nat_ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, real_cid is set to about.labels.key/value, dst_translated_address is set to target.nat_ip, translated_cid is set to about.labels.key/value, dst_fwuser is set to target.user.userid/target.labels.key/value
302018
Teardown (?P<protocol>GRE) connection {session_id} from {src_interface_name}:{src_ip} ({src_translated_address}) (?:({src_fwuser}) )?to {dst_interface_name}:{dst_ip}/{real_cid} ({dst_translated_address}/{translated_cid})(?:({dst_fwuser}))? duration {duration} bytes {bytes_transferred}<message_text>
protocol is set to network.ip_protocol, session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_translated_address is set to principal.nat_ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, real_cid is set to about.labels.key/value, dst_translated_address is set to target.nat_ip, translated_cid is set to about.labels.key/value, dst_fwuser is set to target.user.userid/target.labels.key/value, duration is set to network.session_duration, bytes_transferred is set to about.labels.key/value
302019
H.323 {library_name} ASN Library failed to initialize, error {error_code}
library_name is set to about.labels.key/value, error_code is set to security_result.description
302020, 302021
(?P<action>Built|Teardown)((?P<direction>Inbound|inbound|Outbound|outbound))?{protocol} connection for faddr {dst_ip}/{icmp_seq_num}(?:({fwuser}))? gaddr {src_xlated_ip}/{icmp_code_xlated} laddr {src_ip}/{icmp_code_laddr}(?: type {icmp_type} code {icmp_code})?
action is set to security_result.action, direction is set to network.direction, protocol is set to network.ip_protocol, dst_ip is set to target.ip, icmp_seq_num is set to about.labels.key/value, fwuser is set to about.labels.key/value, src_xlated_ip is set to principal.labels.key/value, icmp_code_xlated is set to about.labels.key/value, src_ip is set to principal.ip, icmp_code_laddr is set to about.labels.key/value, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value
302022, 302023, 302024, 302025, 302027
(?P<action>Built|Teardown)(?: <message_text>)?( stub)? {protocol} connection for {src_interface_name}:{src_ip}/{src_port}(?: ({src_mapped_ip}(?:/{src_mapped_port})?))? to {dst_interface_name}:{dst_ip}/{dst_port}(?: ({dst_mapped_ip}(?:/{dst_mapped_port})?))?(?: duration {duration} forwarded bytes {sent_bytes} )?{summary}
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, duration is set to network.session_duration, sent_bytes is set to network.sent_bytes, summary is set to security_result.summary
302022, 302023, 302024, 302025, 302027
(?P<action>Built|Teardown)(?: <message_text>)?( stub)? {protocol} connection for {src_interface_name}:{src_ip}/{src_port}(?: ({src_mapped_ip}(?:({src_mapped_port})?))? to {dst_interface_name}:{dst_ip}/{dst_port}(?: ({dst_mapped_ip}(?:/{dst_mapped_port})?))?(?: duration {duration} forwarded bytes {sent_bytes} )?{summary}
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, duration is set to network.session_duration, sent_bytes is set to network.sent_bytes, summary is set to security_result.summary
302026
(?P<action>Built|Teardown)(?: <message_text>)? stub (?P<protocol>ICMP) connection for {src_interface_name}:{src_ip}/{src_port}(?: ({src_mapped_ip} ))? to {dst_interface_name}:{dst_ip}/{dst_port}(?: ({dst_mapped_ip} ))?
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip
302033
Pre-allocated H323 GUP Connection for faddr {src_interface_name}:{src_ip}(/{src_port})? to laddr {dst_interface_name}:{dst_ip}(/{dst_port})?
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
302034
Unable to pre-allocate H323 GUP Connection for faddr {src_interface_name}:{src_ip}(/{src_port})? to laddr {dst_interface_name}:{dst_ip}(/{dst_port})?
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
302035
Built (?P<direction>inbound|outbound) SCTP connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? ({mapped_outside_ip}/{mapped_outside_port})(((?:{outside_idfw_user})?(,)?(?:{outside_sg_info})?))? to {dst_interface_name}:{dst_ip}/{dst_port} ({mapped_inside_ip}/{mapped_inside_port})(((?:{inside_idfw_user})?(,)?(?:{inside_sg_info})?))?
direction is set to network.direction, session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, mapped_outside_ip is set to about.labels.key/value, mapped_outside_port is set to about.labels.key/value, outside_idfw_user is set to about.labels.key/value, outside_sg_info is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, mapped_inside_ip is set to about.labels.key/value, mapped_inside_port is set to about.labels.key/value, inside_idfw_user is set to about.labels.key/value, inside_sg_info is set to about.labels.key/value
302035
Built (?P<direction>inbound|outbound) SCTP connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? ({mapped_outside_ip}/{mapped_outside_port})<message_text> to {dst_interface_name}:{dst_ip}/{dst_port} ({mapped_inside_ip}/{mapped_inside_port})
direction is set to network.direction, session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, mapped_outside_ip is set to about.labels.key/value, mapped_outside_port is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, mapped_inside_ip is set to about.labels.key/value, mapped_inside_port is set to about.labels.key/value
302036
Teardown SCTP connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? (((?:{outside_idfw_user})?(,)?(?:{outside_sg_info})?))? to {dst_interface_name}:{dst_ip}/{dst_port} (((?:{inside_idfw_user})?(,)?(?:{inside_sg_info})?))? duration {duration} bytes {received_bytes} {summary}
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, outside_idfw_user is set to about.labels.key/value, outside_sg_info is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, inside_idfw_user is set to about.labels.key/value, inside_sg_info is set to about.labels.key/value, duration is set to network.session_duration, received_bytes is set to network.received_bytes, summary is set to security_result.summary
302036
Teardown SCTP connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? <message_text> to {dst_interface_name}:{dst_ip}/{dst_port} <message_text> duration {duration} bytes {received_bytes} {summary}
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, duration is set to network.session_duration, received_bytes is set to network.received_bytes, summary is set to security_result.summary
302302
ACL = (?P<action>deny); no <message_text> created
action is set to security_result.action
302303
Built TCP state-bypass connection {session_id} from {src_interface_name}:{src_ip}(/{src_port})? <message_text> to {dst_interface_name}:{dst_ip}/{dst_port} <message_text>
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
302304
Teardown TCP state-bypass connection {session_id} from {src_interface_name}:{src_ip}(/{src_port})?((<message_text>))? to {dst_interface_name}:{dst_ip}/{dst_port} duration {duration} bytes {received_bytes} {summary}
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, duration is set to network.session_duration, received_bytes is set to network.received_bytes, summary is set to security_result.summary
302305
Built SCTP state-bypass connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? ({mapped_outside_ip}/{mapped_outside_port})(((?:{outside_idfw_user})?(,)?(?:{outside_sg_info})?))? to {dst_interface_name}:{dst_ip}/{dst_port} ({mapped_inside_ip}/{mapped_inside_port})(((?:{inside_idfw_user})?(,)?(?:{inside_sg_info})?))?
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, mapped_outside_ip is set to about.labels.key/value, mapped_outside_port is set to about.labels.key/value, outside_idfw_user is set to about.labels.key/value, outside_sg_info is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, mapped_inside_ip is set to about.labels.key/value, mapped_inside_port is set to about.labels.key/value, inside_idfw_user is set to about.labels.key/value, inside_sg_info is set to about.labels.key/value
302305
Built SCTP state-bypass connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? ({mapped_outside_ip}/{mapped_outside_port})<message_text> to {dst_interface_name}:{dst_ip}/{dst_port} ({mapped_inside_ip}/{mapped_inside_port})
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, mapped_outside_ip is set to about.labels.key/value, mapped_outside_port is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, mapped_inside_ip is set to about.labels.key/value, mapped_inside_port is set to about.labels.key/value
302306
Teardown SCTP state-bypass connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? (((?:{outside_idfw_user})?(,)?(?:{outside_sg_info})?))? to {dst_interface_name}:{dst_ip}/{dst_port} (((?:{inside_idfw_user})?(,)?(?:{inside_sg_info})?))? duration {duration} bytes {received_bytes} {summary}
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, outside_idfw_user is set to about.labels.key/value, outside_sg_info is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, inside_idfw_user is set to about.labels.key/value, inside_sg_info is set to about.labels.key/value, duration is set to network.session_duration, received_bytes is set to network.received_bytes, summary is set to security_result.summary
302306
Teardown SCTP state-bypass connection {session_id} for {src_interface_name}:{src_ip}(/{src_port})? <message_text>to {dst_interface_name}:{dst_ip}/{dst_port} <message_text> duration {duration} bytes {received_bytes} {summary}
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, duration is set to network.session_duration, received_bytes is set to network.received_bytes, summary is set to security_result.summary
302311
Failed to create a new {protocol} connection from {ingress_interface}:{src_ip}(/{src_port})? to {egress_interface}:{dst_ip}/{dst_port} due to application cache memory allocation failure. The app-cache memory threshold level is {threshold}% and threshold check is
protocol is set to network.ip_protocol, ingress_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, egress_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, threshold is set to about.labels.key/value
303002
(?P<application_protocol>FTP) connection from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, user ({user_name} )?(Stored|Retrieved) file {filename}
application_protocol is set to network.application_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, filename is set to about.labels.key/value
303004
(?P<application_protocol>FTP) {cmd} command unsupported - failed strict inspection, (?P<action>terminating) connection from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
application_protocol is set to network.application_protocol, action is set to security_result.action, cmd is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
303005
Strict (?P<application_protocol>FTP) inspection matched {match_string} in policy-map {policy_name}, {action_details} from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
application_protocol is set to network.application_protocol, match_string is set to about.labels.key/value, policy_name is set to target.resource.name, action_details is set to security_result.action_details, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
304001
{src_ip}(({idfw_user}))? Accessed( JAVA)? URL {dst_ip}:{redirect_url}
src_ip is set to principal.ip, idfw_user is set to about.labels.key/value, dst_ip is set to target.ip, redirect_url is set to target.url
304002
Access (?P<action>denied) URL {redirect_url} SRC {src_ip}(({idfw_user}))? DEST {dst_ip}
action is set to security_result.action, redirect_url is set to target.url, src_ip is set to principal.ip, idfw_user is set to about.labels.key/value, dst_ip is set to target.ip
304003, 304004
URL Server {dst_ip} <message_text> <message_text> URL {redirect_url}
dst_ip is set to target.ip, redirect_url is set to target.url
304006, 304007
URL Server {dst_ip} not responding
dst_ip is set to target.ip
305005
No translation group found for {protocol} src {src_interface_name}:{src_ip}(/{src_port})?(({idfw_user}))? dst {dst_interface_name}:{dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, idfw_user is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
305006
(?P<tag>outbound static|identity|portmap|regular) translation creation failed for {protocol} src {src_interface_name}:{src_ip}(/{src_port})?(({idfw_user}) )?dst {dst_interface_name}:{dst_ip}(/{dst_port})?((type {icmp_type}, code {icmp_code}))?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, idfw_user is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value
305007
addrpool_free(): Orphan IP {dst_ip} on interface {interface_number}
dst_ip is set to target.ip, interface_number is set to about.labels.key/value
305009
^(?P<action>Built) (dynamic|static) translation from (?P<src_interface_name>^:]*)(({acl_name}))?:{src_ip}(({src_fwuser}))? to (?P<dst_interface_name>[^:]*):{dst_ip}
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, acl_name is set to about.labels.key/value, src_ip is set to principal.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_ip is set to target.ip
305010
^(?P<action>Teardown) (dynamic|static) translation from {src_interface_name}:{src_ip}(({src_fwuser}))?to {dst_interface_name}:{dst_ip} duration {duration}
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, duration is set to network.session_duration
305011
^(?P<action>|Built) (dynamic|static) {protocol} translation from {src_interface_name}:{src_ip}/{src_port}(({src_fwuser}))? to {dst_interface_name}:{dst_ip}/{dst_port}
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
305012
(?P<action>Teardown) (dynamic|static) (?P<protocol>TCP|UDP|ICMP|SCTP) translation from {src_interface_name}:{src_ip}/{src_port}({src_fwuser})? to {dst_interface_name}:{dst_ip}/{dst_port} duration {duration}
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, duration is set to network.session_duration
305013
Asymmetric NAT rules matched for forward and reverse flows; Connection (for )?{protocol} src {src_interface_name}:{src_ip}(/{src_port})?({src_fwuser})? dst {dst_interface_name}:{dst_ip}(/{dst_port})?<message_text>(?P<summary>(?P<action>denied) due to NAT reverse path failure)
summary is set to security_result.summary, action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
305014
Allocated block of ports for translation from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
305016
Unable to create protocol connection from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} due to {summary}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
305017
Pba-interim-logging: Active (?P<protocol>ICMP) block of ports for translation from {src_ip} to {dst_ip}/<message_text>
protocol is set to network.ip_protocol, src_ip is set to principal.ip, dst_ip is set to target.ip
305018
MAP translation from {src_interface_name}:{src_ip}/{src_port}-{dst_interface_name}:{dst_ip}/{dst_port} to {src_translated_interface}:{src_translated_address}/{src_translated_port}-{dst_translated_interface}:{dst_translated_address}/{dst_translated_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, src_translated_interface is set to principal.labels.key/value, src_translated_address is set to principal.nat_ip, src_translated_port is set to principal.nat_port, dst_translated_interface is set to target.labels.key/value, dst_translated_address is set to target.nat_ip, dst_translated_port is set to target.nat_port
305019
MAP node address {dst_ip}/{dst_port} has inconsistent Port Set ID encoding
dst_ip is set to target.ip, dst_port is set to target.port
305020
MAP node with address {dst_ip} is not allowed to use port {dst_port}
dst_ip is set to target.ip, dst_port is set to target.port
308001
(Console|console) enable password incorrect for {incorrect_password_attempts} tries (from {dst_ip})
incorrect_password_attempts is set to about.labels.key/value, dst_ip is set to target.ip
308001
(Console|console) enable password incorrect for {incorrect_password_attempts} tries (from ssh (remote {dst_ip}))
incorrect_password_attempts is set to about.labels.key/value, dst_ip is set to target.ip
308002
static {static_global_address} {static_inside_address} netmask <message_text> overlapped with {global_address} {inside_address}
static_global_address is set to about.labels.key/value, static_inside_address is set to about.labels.key/value, global_address is set to about.labels.key/value, inside_address is set to about.labels.key/value
312001
RIP hdr failed from {dst_ip}: cmd={cmd}, version={version} domain={target_hostname} on interface {interface_name}
dst_ip is set to target.ip, cmd is set to about.labels.key/value, version is set to about.labels.key/value, target_hostname is set to target.hostname, interface_name is set to about.labels.key/value
313001, 313004
(?P<action>Denied) (?P<protocol>ICMP|icmp) type={icmp_type}, code={icmp_code} from {src_ip} on interface {dst_interface_name}( to {dst_ip})?
action is set to security_result.action, protocol is set to network.ip_protocol, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
313004
(?P<action>Denied) {protocol} type={icmp_type}, from laddr {src_ip} on interface {dst_interface_name} to {dst_ip}: no matching session
action is set to security_result.action, protocol is set to network.ip_protocol, icmp_type is set to about.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
313005
No matching connection for (?P<protocol>ICMP|icmp) error message: icmp src {src_interface_name}:{src_ip}(({src_fwuser}))? dst {dst_interface_name}:{dst_ip} (type {icmp_type}, code {icmp_code}) on {src_interface_name} interface.s+ Original IP payload: <message_text> src {ori_src_ip}(/{src_port})? dst {ori_dst_ip}(/{dst_port})?<message_text>,
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, ori_src_ip is set to principal.labels.key/value, src_port is set to principal.port, ori_dst_ip is set to target.labels.key/value, dst_port is set to target.port, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value
313008
(?P<action>Denied) IPv6-ICMP type={icmp_type}, code={icmp_code} from {src_ip} on interface {dst_interface_name}( to {dst_ip})?
action is set to security_result.action, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
313009
(?P<action>Denied) invalid {protocol} code {icmp_code}, for {src_interface_name}:{src_ip}/{src_port} ({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port} ({dst_mapped_ip}/{dst_mapped_port})({user}])?(({user}))?, ICMP id {icmp_id}, ICMP type {icmp_type}
action is set to security_result.action, protocol is set to network.ip_protocol, icmp_code is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, user is set to about.labels.key/value, user is set to about.labels.key/value, icmp_id is set to network.session_id, icmp_type is set to about.labels.key/value
314001
Pre-(allocated|allocate) RTSP (?P<protocol>UDP) backconnection for {src_interface_name}:{src_ip} to {dst_interface_name}:{dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
314002
RTSP failed to allocate (?P<protocol>UDP) media connection from {src_interface_name}:{src_ip} to {dst_interface_name}:{dst_ip}/{dst_port}: {summary}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
314003
Dropped RTSP traffic from {src_interface_name}:{src_ip} due to: {summary}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, summary is set to security_result.summary
314004
RTSP client {src_interface_name}:{src_ip} accessed RTSP URL {rtsp_url}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, rtsp_url is set to about.labels.key/value
314005
RTSP client {src_interface_name}:{src_ip} denied access to URL {rtsp_url}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, rtsp_url is set to about.labels.key/value
314006
RTSP client {src_interface_name}:{src_ip} exceeds configured rate limit of {rate} for {request_method} messages
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, rate is set to about.labels.key/value, request_method is set to about.labels.key/value
315011
(?P<application_protocol>SSH) session from {src_ip} on interface {src_interface_name} for user {dst_fwuser}( disconnected by SSH server, reason:)? {summary}
application_protocol is set to network.application_protocol, src_ip is set to principal.ip, src_interface_name is set to principal.labels.key/value, dst_fwuser is set to target.user.userid/target.labels.key/value, summary is set to security_result.summary
315012
Weak SSH cipher ({cipher_name}) provided from client {dst_ip} on interface {dst_interface_name}. Connection failed. Not FIPS 140-2 compliant
cipher_name is set to network.tls.cipher, dst_ip is set to target.ip, dst_interface_name is set to target.labels.key/value
315012
Weak SSH MAC ({mac_address}) provided from client {dst_ip} on interface {dst_interface_name}. Connection failed. Not FIPS 140-2 compliant
mac_address is set to about.labels.key/value, dst_ip is set to target.ip, dst_interface_name is set to target.labels.key/value
315013
SSH session from {dst_ip} on interface {dst_interface_name} for user {user_name} rekeyed successfully
dst_ip is set to target.ip, dst_interface_name is set to target.labels.key/value, user_name is set to target.user.userid
316001
Denied new tunnel to {dst_ip}. VPN peer limit ({platform_vpn_peer_limit}) exceeded
dst_ip is set to target.ip, platform_vpn_peer_limit is set to about.labels.key/value
316002
VPN Handle error: protocol={protocol}, src {src_interface_name}:{src_ip}, dst {dst_interface_name}:{dst_ip}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
317002
Bad path index of number for {src_ip}, {max_num} max
src_ip is set to principal.ip, max_num is set to about.labels.key/value
317003
IP routing table creation failure -{summary}
summary is set to security_result.summary
317005
IP routing table limit exceeded -{summary}
summary is set to security_result.summary
317006
Pdb index error {pdb}, {pdb_index}, {pdb_type}
pdb is set to about.labels.key/value, pdb_index is set to about.labels.key/value, pdb_type is set to about.labels.key/value
317007
Added {route_type} route {dst_ip} {netmask} via {gateway_address} <message_text> on {interface_name} {route_type}
route_type is set to about.labels.key/value, dst_ip is set to target.ip, netmask is set to about.labels.key/value, gateway_address is set to about.labels.key/value, interface_name is set to about.labels.key/value, route_type is set to about.labels.key/value
317008
Community list check with bad list {list_number}
list_number is set to about.labels.key/value
317012
Interface IP route counter negative - {interface_name}
interface_name is set to about.labels.key/value
318004
area <message_text> lsid {src_ip} mask {netmask} adv {dst_ip} type <message_text>
src_ip is set to principal.ip, netmask is set to about.labels.key/value, dst_ip is set to target.ip
318005, 318105
lsid {src_ip} adv {dst_ip}<message_text>gateway {gateway_address}<message_text> network {network_address} mask {netmask}<message_text>
src_ip is set to principal.ip, dst_ip is set to target.ip, gateway_address is set to about.labels.key/value, network_address is set to about.labels.key/value, netmask is set to about.labels.key/value
318007
OSPF is enabled on {interface_name} during idb initialization
interface_name is set to about.labels.key/value
318008, 613011
OSPF process {process_number} is changing router-id. Reconfigure virtual link neighbors with our new router-id
process_number is set to about.labels.key/value
318009
OSPF: Attempted reference of stale data encountered in {function}, line: {line_number}
function is set to about.labels.key/value, line_number is set to about.labels.key/value
318012
Process {target_process_name} (re-originates|flushes) LSA ID {src_ip} type-<message_text>adv-rtr {dst_ip}<message_text>
target_process_name is set to target.process.pid, src_ip is set to principal.ip, dst_ip is set to target.ip
318107
OSPF is enabled on {interface_name} during idb initialization
interface_name is set to about.labels.key/value
318108
OSPF process {process_number} is changing router-id. Reconfigure virtual link neighbors with our new router-id
process_number is set to about.labels.key/value
318110
Invalid encrypted key {encrypted_key}
encrypted_key is set to about.labels.key/value
318111
SPI {spi} is already in use with ospf process {process_number}
spi is set to about.labels.key/value, process_number is set to about.labels.key/value
318112
SPI {spi} is already in use by a process other than ospf process {process_number}
spi is set to about.labels.key/value, process_number is set to about.labels.key/value
318113
s {interface_name} is already configured with SPI {spi}
interface_name is set to about.labels.key/value, spi is set to about.labels.key/value
318114
The key length used with SPI {spi} is not valid
spi is set to about.labels.key/value
318115, 318118
{error} (error )?occurred when attempting to <message_text> <message_text> (IPsec|IPSec) policy <message_text> SPI {spi}
error is set to about.labels.key/value, spi is set to about.labels.key/value
318116
SPI {spi} is not being used by ospf process {process_number}
spi is set to about.labels.key/value, process_number is set to about.labels.key/value
318117
The policy for SPI {spi} could not be removed because it is in use
spi is set to about.labels.key/value
318119
Unable to close secure socket with SPI {spi} on interface {interface_name}
spi is set to about.labels.key/value, interface_name is set to about.labels.key/value
318121
IPsec reported a GENERAL ERROR: message {summary}, count {total_msgs}
summary is set to security_result.summary, total_msgs is set to about.labels.key/value
318122
IPsec sent a {specified_message_} message {specified_message} to OSPFv3 for interface {specified_interface}. Recovery attempt {recovery_attempts}
specified_message_ is set to about.labels.key/value, specified_message is set to about.labels.key/value, specified_interface is set to about.labels.key/value, recovery_attempts is set to about.labels.key/value
318123
IPsec sent a {specified_message_} message {specified_message} to OSPFv3 for interface {interface_name}. Recovery aborted
specified_message_ is set to about.labels.key/value, specified_message is set to about.labels.key/value, interface_name is set to about.labels.key/value
318125
Init failed for interface {interface_name}
interface_name is set to about.labels.key/value
318126
Interface {interface_name} is attached to more than one area
interface_name is set to about.labels.key/value
319001, 319002
Acknowledge for <message_text> update for IP address {dst_ip} not received<message_text>
dst_ip is set to target.ip
319003
Arp update for IP address {dst_ip} to NP<message_text>
dst_ip is set to target.ip
319004
Route update for IP address {dst_ip} failed<message_text>
dst_ip is set to target.ip
321001, 321002
Resource {resource} (rate )?limit of {resource_limit} reached
resource is set to target.resource.name, resource_limit is set to about.labels.key/value
321003, 321004
Resource {resource} (rate )?log level of {log_level} reached
resource is set to target.resource.name, log_level is set to about.labels.key/value
321005
System CPU utilization reached {utilization}%
utilization is set to about.labels.key/value
321006
System (M|m)emory usage reached {utilization}\s*%
utilization is set to about.labels.key/value
321007
System is low on free memory blocks of size {block_size} ({free_blocks} CNT out of {max_blocks} MAX)
block_size is set to about.labels.key/value, free_blocks is set to about.labels.key/value, max_blocks is set to about.labels.key/value
322001
(?P<action>Deny) MAC address {src_mac}, possible spoof attempt on interface {interface_name}
action is set to security_result.action, src_mac is set to principal.mac, interface_name is set to about.labels.key/value
322002
ARP inspection check failed for arp {action_details} received from host {src_mac} on interface {interface_name}. This host is advertising MAC Address {mac_address_1} for IP Address {dst_ip} , which is <message_text> bound to MAC Address {mac_address_2}
action_details is set to security_result.action_details, src_mac is set to principal.mac, interface_name is set to about.labels.key/value, mac_address_1 is set to about.labels.key/value, dst_ip is set to target.ip, mac_address_2 is set to about.labels.key/value
322003
ARP inspection check failed for arp {action_details} received from host {src_mac} on interface {interface_name}\s*. This host is advertising MAC Address {mac_address_1} for IP Address {dst_ip} , which is not bound to any MAC Address
action_details is set to security_result.action_details, src_mac is set to principal.mac, interface_name is set to about.labels.key/value, mac_address_1 is set to about.labels.key/value, dst_ip is set to target.ip
322004
No management IP address configured for transparent firewall. Dropping protocol {protocol} packet from {input_interface}:{src_ip}(/{src_port})? to {output_interface}:{dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, input_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, output_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
323001
Module {module_id} experienced a control channel communication(s)? failure
module_id is set to about.labels.key/value
323001
Module in slot {slot_number} experienced a control channel communication(s)? failure
slot_number is set to about.labels.key/value
323002
Module {module_id} is not able to shut down, shut down request not answered
module_id is set to about.labels.key/value
323002
Module in slot {slot_number} is not able to shut down, shut down request not answered
slot_number is set to about.labels.key/value
323003
Module {module_id} is not able to reload, reload request not answered
module_id is set to about.labels.key/value
323003
Module in slot {slot_number} is not able to reload, reload request not answered
slot_number is set to about.labels.key/value
323004
Module {info} failed to write software {new_version_number} (currently {current_version_number}), {summary}. Hw-module reset is required before further use
info is set to about.labels.key/value, new_version_number is set to about.labels.key/value, current_version_number is set to about.labels.key/value, summary is set to security_result.summary
323005
Module {module_id} (?P<tag>cannot|can not) be started completely
module_id is set to about.labels.key/value
323005
Module in slot {slot_number} cannot be started completely
slot_number is set to about.labels.key/value
324000
Drop GTPv {version} message {msg_type} from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port} Reason: {summary}
version is set to about.labels.key/value, msg_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
324001
GTPv0 packet parsing error from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, TID: {tid_value}, Reason: {summary}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, tid_value is set to about.labels.key/value, summary is set to security_result.summary
324002
No PDPMCB] exists to process GTPv0 {msg_type} from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, TID: {tid_value}
msg_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, tid_value is set to about.labels.key/value
324003
No matching request to process GTPv {version} {msg_type} from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
version is set to about.labels.key/value, msg_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
324004
GTP packet with version{version} from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})? is not supported
version is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
324005
Unable to create tunnel from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
324006
GSN {dst_ip} tunnel limit {tunnel_limit} exceeded, PDP Context TID {tid_value} failed
dst_ip is set to target.ip, tunnel_limit is set to about.labels.key/value, tid_value is set to about.labels.key/value
324007
Unable to create GTP connection for response from {src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
324010
Subscriber {imsi} PDP Context activated on network MCC/MNC {mccmnc} (<message_text>)( CellID {cell_id})?
imsi is set to about.labels.key/value, mccmnc is set to about.labels.key/value, cell_id is set to about.labels.key/value
324300
Radius Accounting Request from {dst_ip} has an incorrect request authenticator
dst_ip is set to target.ip
324301
Radius Accounting Request has a bad header length {header_length}, packet length {packet_length}
header_length is set to about.labels.key/value, packet_length is set to about.labels.key/value
324303
Server=(<)?%{IPORHOST:src_ip}:%{INT:src_port}(>)?\s*,\s*ID=(<)?%{DATA:radius_id}(>)?\s*:\s*%{GREEDYDATA:summary}
src_ip is set to principal.ip, src_port is set to principal.port, radius_id is set to additional.fields[id], summary is set to security_result.summary
325001
Router {ipv6_address} on {interface_name} has conflicting ND (Neighbor Discovery) settings
ipv6_address is set to about.labels.key/value, interface_name is set to about.labels.key/value
325002
Duplicate address {ipv6_address}/{src_mac} on {interface_name}
ipv6_address is set to about.labels.key/value, src_mac is set to principal.mac, interface_name is set to about.labels.key/value
325003
<message_text>source address check failed.{action} packet from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})? with source MAC address {src_mac}
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, src_mac is set to principal.mac
325004
IPv6 Extension Header {header_type} action configuration. {protocol} from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
header_type is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
325006
IPv6 Extension Header not in order: Type {header_type} occurs after Type <message_text>\s*. (?P<protocol>TCP) <message_text> from inside {src_interface_name}\s*:{src_ip}\s*/{src_port} to {dst_interface_name}\s*:{dst_ip}\s*/{dst_port}
protocol is set to network.ip_protocol, header_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
326001
Unexpected error in the timer library: {error}
error is set to about.labels.key/value
326005
Mrib notification failed for ({dst_ip}, {dst_ip1})
dst_ip is set to target.ip, dst_ip1 is set to target.ip
326006, 326007
Entry-(?P<tag>creation|update) failed for ({dst_ip}, {dst_ip1})
dst_ip is set to target.ip, dst_ip1 is set to target.ip
326012
Initialization of {functionality} functionality failed
functionality is set to about.labels.key/value
326014
Initialization failed: error_message {error_message}
error_message is set to security_result.description
326015
Communication error: error_message {error_message}
error_message is set to security_result.description
326016
Failed to set un-numbered interface for {interface_name} ({info})
interface_name is set to about.labels.key/value, info is set to about.labels.key/value
326026
Server unexpected error: {error_message}
error_message is set to security_result.description
326027
Corrupted update: {error_message}
error_message is set to security_result.description
326028
Asynchronous error: {error_message}
error_message is set to security_result.description
328001
Attempt made to overwrite a set stub function in {function}
function is set to about.labels.key/value
328002
Attempt made in {register_key} to register with out of bounds key
register_key is set to about.labels.key/value
329001
The <message_text> subblock named {sub_block_name} was not removed
sub_block_name is set to about.labels.key/value
331001
Dynamic DNS Update for '{target_hostname}'= {dst_ip} failed
target_hostname is set to target.hostname, dst_ip is set to target.ip
331002
Dynamic DNS {type} RR for ('{target_hostname}' - {dst_ip}|{dst_ip}- '{target_hostname}') successfully updated in DNS server {dst_ip}
type is set to about.labels.key/value, target_hostname is set to target.hostname, dst_ip is set to target.ip, dst_ip is set to target.ip, target_hostname is set to target.hostname, dst_ip is set to target.ip
332003, 332004
Web Cache {dst_ip}/{service_id} <message_text>
dst_ip is set to target.ip, service_id is set to about.labels.key/value
333001, 333003
{protocol} association <message_text>- context:{session_id}
protocol is set to network.ip_protocol, session_id is set to network.session_id
333002
Timeout waiting for EAP response- context:{session_id}
session_id is set to network.session_id
333009, 333010
{protocol}-SQ response .* - context:{session_id}
protocol is set to network.ip_protocol, session_id is set to network.session_id
334001, 334002, 334003
EAPoUDP association .* - {dst_ip}
dst_ip is set to target.ip
334004
Authentication request for NAC Clientless host - {dst_ip}
dst_ip is set to target.ip
334005
Host put into NAC Hold state - {dst_ip}
dst_ip is set to target.ip
334006
{response} failed to get a response from host - {dst_ip}
response is set to about.labels.key/value, dst_ip is set to target.ip
334007
{response} association terminated - {dst_ip}
response is set to about.labels.key/value, dst_ip is set to target.ip
334008
<message_text> EAP association initiated - {dst_ip} , EAP context: {session_id}
dst_ip is set to target.ip, session_id is set to network.session_id
334009
Audit request for <message_text> Clientless host - {dst_ip}
dst_ip is set to target.ip
335001
NAC session initialized - {dst_ip}
dst_ip is set to target.ip
335002
Host is on the NAC Exception List - {dst_ip} , OS: {target_platform}
dst_ip is set to target.ip, target_platform is set to target.platform
335003
NAC Default ACL applied, ACL:{acl_name} - {dst_ip}
acl_name is set to about.labels.key/value, dst_ip is set to target.ip
335004
NAC is disabled for host - {dst_ip}
dst_ip is set to target.ip
335005
NAC Downloaded ACL parse failure - {dst_ip}
dst_ip is set to target.ip
335006
NAC Applying ACL: {acl_name} - {dst_ip}
acl_name is set to about.labels.key/value, dst_ip is set to target.ip
335008
NAC (IPsec|IPSec) terminate from dynamic ACL:{acl_name} - {dst_ip}
acl_name is set to about.labels.key/value, dst_ip is set to target.ip
335009
NAC Revalidate request by administrative action - {dst_ip}
dst_ip is set to target.ip
335010
NAC Revalidate All request by administrative action - {num_of_sessions} sessions
num_of_sessions is set to about.labels.key/value
335011
NAC Revalidate Group request by administrative action for {group_name} group - {num_of_sessions} sessions
group_name is set to target.user.group_identifiers, num_of_sessions is set to about.labels.key/value
335012
NAC Initialize request by administrative action - {dst_ip}
dst_ip is set to target.ip
335013
NAC Initialize All request by administrative action - {num_of_sessions} sessions
num_of_sessions is set to about.labels.key/value
335014
NAC Initialize Group request by administrative action for {group_name} group - {num_of_sessions} sessions
group_name is set to target.user.group_identifiers, num_of_sessions is set to about.labels.key/value
336001
Route {route_name} stuck-in-active state in EIGRP-{dst_ip} {eigrp_router}. Cleaning up
route_name is set to about.labels.key/value, dst_ip is set to target.ip, eigrp_router is set to about.labels.key/value
336002
Handle {handle_id} is not allocated in pool
handle_id is set to about.labels.key/value
336003
No buffers available for {no_of_bytes} byte packet
no_of_bytes is set to about.labels.key/value
336004
Negative refcount in pakdesc {packet_identifier}
packet_identifier is set to about.labels.key/value
336005
Flow control error, {error_message} , on {interface_name}
error_message is set to security_result.description, interface_name is set to about.labels.key/value
336006
{no_of_peers} peers exist on IIDB {interface_name}
no_of_peers is set to about.labels.key/value, interface_name is set to about.labels.key/value
336008
Lingering DRDB deleting IIDB, dest {dst_ip}, {next_hop_address} ({interface_name}), origin {origin_str}
dst_ip is set to target.ip, next_hop_address is set to about.labels.key/value, interface_name is set to about.labels.key/value, origin_str is set to about.labels.key/value
336009
{pdm_name} {autonomous_system_id}: Internal Error
pdm_name is set to about.labels.key/value, autonomous_system_id is set to about.labels.key/value
336010
{protocol}-<message_text> {table_id} {autonomous_system_id}: Neighbor {neighbor_address} (<message_text>) is {event_msg}: {security_description}
protocol is set to network.ip_protocol, table_id is set to about.labels.key/value, autonomous_system_id is set to about.labels.key/value, neighbor_address is set to about.labels.key/value, interface_name is set to about.labels.key/value, event_msg is set to about.labels.key/value, security_description is set to security_result.description
336012
Interface {interface_name} going down and {neighbor_links} links exist
interface_name is set to about.labels.key/value, neighbor_links is set to about.labels.key/value
336013
Route iproute, {iproute_successors} successors, {db_successors} rdbs
iproute_successors is set to about.labels.key/value, db_successors is set to about.labels.key/value
336015
Unable to open socket for AS {as_number}
as_number is set to about.labels.key/value
336016
Unknown timer type {timer_type} expiration
timer_type is set to about.labels.key/value
336019
{target_file_full_path} {as_number}: {prefix_source} threshold prefix level ({prefix_threshold}) reached
target_file_full_path is set to target.file.full_path, as_number is set to about.labels.key/value, prefix_source is set to about.labels.key/value, prefix_threshold is set to about.labels.key/value
337000
Created BFD session with local discriminator <{id}> on <{real_interface}> with neighbor <{dst_ip}
id is set to about.labels.key/value, real_interface is set to about.labels.key/value, dst_ip is set to target.ip
337001
Terminated BFD session with local discriminator <{id}> on <{real_interface}> with neighbor <{dst_ip}> due to <{summary}>
id is set to about.labels.key/value, real_interface is set to about.labels.key/value, dst_ip is set to target.ip, summary is set to security_result.summary
337005
Phone Proxy SRTP: Media session not found for media_term_ip/media_term_port for packet from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
338001
Dynamic filter monitored blacklisted protocol traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port} , (<message_text>), source malicious address resolved from local or dynamic list: domain name, threat-level: {threat_level}, category: {category}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338003
Dynamic filter monitored blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port} , (<message_text>), source {malicious_address} resolved from (local|dynamic) list: {ip_address}/{subnet_mask}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, malicious_address is set to about.labels.key/value, ip_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338004
Dynamic (Filter|filter) (permitted|monitored) blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {ip_address}/{subnet_mask}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, ip_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338005
Dynamic filter dropped blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), source {malicious_address} resolved from (local|dynamic) list: {domain_name}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338006
Dynamic filter dropped blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {domain_name}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338007
Dynamic filter dropped blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), source {malicious_address} resolved from (local|dynamic) list: {ip_address}/{subnet_mask}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, ip_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338008
Dynamic (Filter|filter) dropped blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {ip_address}/{subnet_mask}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, ip_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338103
Dynamic filter {filter_action} whitelisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}, (<message_text>), source {malicious_address} resolved from (local|dynamic) list: {ip_address}/{subnet_mask}
filter_action is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, malicious_address is set to about.labels.key/value, ip_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value
338101
Dynamic filter {filter_action} whitelisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}, (<message_text>), source {malicious_address} resolved from (local|dynamic) list: {domain_name}
filter_action is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value
338102
Dynamic filter {filter_action} whitelisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {domain_name}
filter_action is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value
338104
Dynamic filter {filter_action} whitelisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {ip_address}/{subnet_mask}
filter_action is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, ip_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value
338201
Dynamic filter monitored greylisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}, (<message_text>), source {malicious_address} resolved from (local|dynamic) list: {domain_name}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338202
Dynamic filter monitored greylisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {domain_name}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338203
Dynamic filter dropped greylisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), source {malicious_address} resolved from (local|dynamic) list: {domain_name}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338204
Dynamic (Filter|filter) dropped greylisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination ({malicious_address}|malicious address) resolved from (local|dynamic) list: {domain_name}, threat-level: {threat_level}, category: {category}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338002
Dynamic (Filter|filter) (permitted|monitored) blacklisted {protocol} traffic from {src_interface_name}:{src_ip}/{src_port}({src_mapped_ip}/{src_mapped_port}) to {dst_interface_name}:{dst_ip}/{dst_port}({dst_mapped_ip}/{dst_mapped_port}), destination {malicious_address} resolved from (local|dynamic) list: {domain_name}( threat-level: {threat_level}, category: {category})?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_mapped_ip is set to principal.ip, src_mapped_port is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_mapped_ip is set to target.ip, dst_mapped_port is set to target.labels.key/value, malicious_address is set to about.labels.key/value, domain_name is set to about.labels.key/value, threat_level is set to about.labels.key/value, category is set to security_result.category_details
338301
Intercepted DNS reply for domain {domain_name} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} , matched {administrator_list}
domain_name is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, administrator_list is set to about.labels.key/value
338302
Address {dst_ip} discovered for domain {domain_name} from {administrator_list} , Adding rule
dst_ip is set to target.ip, domain_name is set to about.labels.key/value, administrator_list is set to about.labels.key/value
338303
Address {dst_ip} ({domain_name}) timed out(.|,) Removing rule
dst_ip is set to target.ip, domain_name is set to about.labels.key/value
338304
Successfully downloaded dynamic filter data file from updater server {redirect_url}
redirect_url is set to target.url
338305
Failed to download dynamic filter data file from updater server {redirect_url}
redirect_url is set to target.url
338306
Failed to authenticate with dynamic filter updater server {redirect_url}
redirect_url is set to target.url
338308
Dynamic filter updater server dynamically changed from {src_hostname} : {src_port} to {target_hostname} : {dst_port}
src_hostname is set to principal.hostname, src_port is set to principal.port, target_hostname is set to target.hostname, dst_port is set to target.port
338310
Failed to update from dynamic filter updater server {redirect_url}, reason: {summary}
redirect_url is set to target.url, summary is set to security_result.summary
339001
<message_text> certificate update failed for <{num_tries}>
num_tries is set to about.labels.key/value
339002
Umbrella device registration failed with error code <{error_code}>
error_code is set to security_result.description
339005
Umbrella device registration failed after <{num_tries}> retries
num_tries is set to about.labels.key/value
339006
Umbrella resolver {current_resolver} {dst_ip} is reachable, resuming Umbrella redirect
current_resolver is set to about.labels.key/value, dst_ip is set to target.ip
339007
Umbrella resolver {current_resolver} {dst_ip} is unreachable, moving to fail-open. Starting probe to resolver
current_resolver is set to about.labels.key/value, dst_ip is set to target.ip
339008
Umbrella resolver {current_resolver} {dst_ip} is unreachable, moving to fail-close
current_resolver is set to about.labels.key/value, dst_ip is set to target.ip
340001
Loopback-proxy error: {summary} context id {context_id} , context type = {version_protocol}/{request_type}/{address_type} client socket (internal)= {src_ip}/{src_port} server socket (internal)= {server_address_internal} /{server_port_internal} server socket (external)= {server_address_external} /{server_port_external} remote socket (external)= {dst_ip}/{dst_port}
summary is set to security_result.summary, context_id is set to about.labels.key/value, version_protocol is set to network.tls.version_protocol, request_type is set to about.labels.key/value, address_type is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, server_address_internal is set to about.labels.key/value, server_port_internal is set to about.labels.key/value, server_address_external is set to about.labels.key/value, server_port_external is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
340002
Loopback-proxy info: {summary} context id {context_id} , context type = {version_protocol}/{request_type}/{address_type} client socket (internal)= {src_ip}/{src_port} server socket (internal)= {server_address_internal}/{server_port_internal} server socket (external)= {server_address_external}/{server_port_external} remote socket (external)= {dst_ip}/{dst_port}
summary is set to security_result.summary, context_id is set to about.labels.key/value, version_protocol is set to network.tls.version_protocol, request_type is set to about.labels.key/value, address_type is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, server_address_internal is set to about.labels.key/value, server_port_internal is set to about.labels.key/value, server_address_external is set to about.labels.key/value, server_port_external is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
341001, 341002
Policy Agent (started|stopped) successfully for {dst_service} {dst_ip}
dst_ip is set to target.ip
341003
Policy Agent failed to start for {dst_service} {dst_ip}
dst_ip is set to target.ip
341004
Storage device not available: Attempt to shutdown module {software_module_name} failed
software_module_name is set to about.labels.key/value
341005
Storage device not available. Shutdown issued for module {software_module_name}
software_module_name is set to about.labels.key/value
341006
Storage device not available. Failed to stop recovery of module {software_module_name}
software_module_name is set to about.labels.key/value
341007
Storage device not available. Further recovery of module {software_module_name} was stopped.*
software_module_name is set to about.labels.key/value
341008
Storage device not found. Auto-boot of module {software_module_name} cancelled.*
software_module_name is set to about.labels.key/value
341010
Storage device with serial number {serial_number} (inserted into|removed from) bay {bay_no}
serial_number is set to about.labels.key/value, bay_no is set to about.labels.key/value
341011
Storage device with serial number {serial_number} in bay {bay_no} faulty
serial_number is set to about.labels.key/value, bay_no is set to about.labels.key/value
342002
REST API Agent failed, reason: {summary}
summary is set to security_result.summary
342006, 342008
Failed to (install|uninstall) REST API image, reason: <{summary}>
summary is set to security_result.summary
400000 to 400050
{label} {protocol} (?P<summary><message_text>) from {src_ip} to {dst_ip} on interface {dst_interface_name}
summary is set to security_result.summary, label is set to about.labels.key/value, protocol is set to network.ip_protocol, src_ip is set to principal.ip, dst_ip is set to target.ip, dst_interface_name is set to target.labels.key/value
400000 to 400050
{label} (?P<summary><message_text>) from {src_ip} to {dst_ip} on interface {dst_interface_name}
summary is set to security_result.summary, label is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, dst_interface_name is set to target.labels.key/value
401002
Shun added: IP_address {src_ip} port {src_port}
src_ip is set to principal.ip, src_port is set to principal.port
401003
Shun deleted: {src_ip}
src_ip is set to principal.ip
401004
Shunned packet:<message_text>= {src_ip} on interface {src_interface_name}
src_ip is set to principal.ip, src_interface_name is set to principal.labels.key/value
401004
Shunned packet:{src_ip} {pkg_direction} {dst_ip} on interface {dst_interface}
src_ip is set to principal.ip, pkg_direction is set to about.labels.key/value, dst_ip is set to target.ip, dst_interface is set to about.labels.key/value
401005
Shun add failed: unable to allocate resources for<message_text> {src_ip} port {src_port}
src_ip is set to principal.ip, src_port is set to principal.port
402114
IPSEC: Received an {protocol} packet (SPI={spi} , sequence number={seq_number}) from {src_ip} to {dst_ip} with an invalid SPI
protocol is set to network.ip_protocol, spi is set to about.labels.key/value, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
402115
IPSEC: Received a packet from {src_ip} to {dst_ip} containing {received_protocol} data instead of {expected_protocol} data
src_ip is set to principal.ip, dst_ip is set to target.ip, received_protocol is set to about.labels.key/value, expected_protocol is set to about.labels.key/value
402116
IPSEC: Received an {protocol} packet (SPI={spi}, sequence number={seq_number}) from {src_ip} ({src_username}) to {dst_ip}. The decapsulated inner packet doesn't match the negotiated policy in the SA. The packet specifies its destination as {dst_ip1}, its source as {src_ip1}, and its protocol as tcp. The SA specifies its local proxy as {src_ip2}/{local_proxy_port} and its remote_proxy as {dst_ip2}/{remote_proxy_subnetmask}/{remote_transport_protocol}/{remote_proxy_port}
protocol is set to network.ip_protocol, spi is set to about.labels.key/value, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, src_username is set to principal.user.userid, dst_ip is set to target.ip, dst_ip1 is set to target.ip, src_ip1 is set to principal.ip, src_ip2 is set to principal.ip, local_proxy_subnetmask is set to about.labels.key/value, local_transport_protocol is set to about.labels.key/value, local_proxy_port is set to about.labels.key/value, dst_ip2 is set to target.ip, remote_proxy_subnetmask is set to about.labels.key/value, remote_transport_protocol is set to about.labels.key/value, remote_proxy_port is set to about.labels.key/value
"security_result.category" is set to "NETWORK_SUSPICIOUS"
"network.direction" is set to "INBOUND"
402117
IPSEC: Received a non-IPsec ({protocol}) packet from {src_ip} to {dst_ip}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, dst_ip is set to target.ip
402118
IPSEC: Received an {protocol} packet (SPI={spi}, sequence number={seq_number}) from {src_ip} ({src_username}) to {dst_ip} containing an illegal IP fragment of length {frag_len} with offset {frag_offset}
protocol is set to network.ip_protocol, spi is set to about.labels.key/value, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, src_username is set to principal.user.userid, dst_ip is set to target.ip, frag_len is set to about.labels.key/value, frag_offset is set to about.labels.key/value
402119
IPSEC: Received an {protocol} packet (SPI={spi}, sequence number={seq_number}) from {src_ip} ({src_username}) to {dst_ip} that failed anti-replay checking
protocol is set to network.ip_protocol, spi is set to about.labels.key/value, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, src_username is set to principal.user.userid, dst_ip is set to target.ip
402120
IPSEC: Received an {protocol} packet (SPI={spi} , sequence number={seq_number}) from {src_ip} ({src_username}) to {dst_ip} that failed authentication
protocol is set to network.ip_protocol, spi is set to about.labels.key/value, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, src_username is set to principal.user.userid, dst_ip is set to target.ip
402121
IPSEC: Received an {protocol} packet (SPI={spi} , sequence number={seq_number}) from {src_ip} ({src_username}) to {dst_ip} that was dropped by (IPsec|IPSec) ({summary})
protocol is set to network.ip_protocol, spi is set to about.labels.key/value, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, src_username is set to principal.user.userid, dst_ip is set to target.ip, summary is set to security_result.summary
402122
Received a cleartext packet from {src_ip} to {dst_ip} that was to be encapsulated in (IPsec|IPSec) that was dropped by (IPsec|IPSec) ({summary})
src_ip is set to principal.ip, dst_ip is set to target.ip, summary is set to security_result.summary
402123
{category}: The {accel_type} hardware accelerator encountered an error (code={error_message}) while executing crypto command {command}
category is set to security_result.category_details, accel_type is set to about.labels.key/value, error_message is set to security_result.description, command is set to target.process.command_line
402124
{category}: The ASA hardware accelerator encountered an error (HWErrAddr= {hardware_error_address}, Core= {crypto_core}, HwErrCode= {hardware_error_code}, IstatReg= 0x8, PciErrReg= 0x0, CoreErrStat= 0x41, CoreErrAddr={core_error_address},<message_text>)
category is set to security_result.category_details, hardware_error_address is set to about.labels.key/value, crypto_core is set to about.labels.key/value, hardware_error_code is set to about.labels.key/value, core_error_address is set to about.labels.key/value
402125
The ASA hardware accelerator {ring} timed out ({parameters})
ring is set to about.labels.key/value, parameters is set to about.labels.key/value
402126
{category}: The ASA created Crypto Archive File {target_file_full_path} as a Soft Reset was necessary
category is set to security_result.category_details, target_file_full_path is set to target.file.full_path
402127
{category}: The ASA is skipping the writing of latest Crypto Archive File as the maximum # of files, {max_num}, allowed have been written to {target_file_full_path}. Please {summary} if you want more Crypto Archive Files saved
category is set to security_result.category_details, max_num is set to about.labels.key/value, target_file_full_path is set to target.file.full_path, summary is set to security_result.summary
402128
{category}: An attempt to allocate a large memory block failed, size: {block_size}, limit: {limit}
category is set to security_result.category_details, block_size is set to about.labels.key/value, limit is set to about.labels.key/value
402129
{category}: An attempt to release a DMA memory block failed, location: {address}
category is set to security_result.category_details, address is set to about.labels.key/value
402130
{category}: Received an ESP packet (SPI = {spi}, sequence number={sequence_number}) from {src_ip} (user={user_name}) to {dst_ip} with incorrect (IPsec|IPSec) padding
category is set to security_result.category_details, spi is set to about.labels.key/value, sequence_number is set to about.labels.key/value, src_ip is set to principal.ip, user_name is set to target.user.userid, dst_ip is set to target.ip
402131
{category}: {summary} changing the {accel_instance} hardware accelerator's configuration bias from {old_config_bias} to {new_config_bias}
category is set to security_result.category_details, summary is set to security_result.summary, accel_instance is set to about.labels.key/value, old_config_bias is set to about.labels.key/value, new_config_bias is set to about.labels.key/value
402140
{category}: {summary}: modulus len {length}
category is set to security_result.category_details, summary is set to security_result.summary, length is set to about.labels.key/value
402141
{category}: {summary}: key set {crypto_type}, reason {error_message}
category is set to security_result.category_details, summary is set to security_result.summary, crypto_type is set to about.labels.key/value, error_message is set to security_result.description
402142
{category}: {summary}: algorithm {algorithm}, mode {mode}
category is set to security_result.category_details, summary is set to security_result.summary, algorithm is set to about.labels.key/value, mode is set to about.labels.key/value
402144
{category}: Digital signature error: signature algorithm {signature} , hash algorithm {algo_hash}
category is set to security_result.category_details, signature is set to about.labels.key/value, algo_hash is set to about.labels.key/value
402146
{category}: Keyed hash generation error: algorithm {algo_hash}, key len {length}
category is set to security_result.category_details, algo_hash is set to about.labels.key/value, length is set to about.labels.key/value
402145
{category}: Hash generation error: algorithm {algo_hash}
category is set to security_result.category_details, algo_hash is set to about.labels.key/value
402147
{category}: HMAC generation error: algorithm {algorithm}
category is set to security_result.category_details, algorithm is set to about.labels.key/value
402149
{category}: weak {encryption_type} ({length}). Operation disallowed. Not FIPS 140-2 compliant
category is set to security_result.category_details, encryption_type is set to about.labels.key/value, length is set to about.labels.key/value
402150
{category}: Deprecated hash algorithm used for RSA {operation} ({algo_hash}). Operation disallowed. Not FIPS 140-2 compliant
category is set to security_result.category_details, operation is set to about.labels.key/value, algo_hash is set to about.labels.key/value
403101
PPTP session state not established, but received an X{protocol} packet, tunnel_id={tunnel_id}, session_id={session_id}
protocol is set to network.ip_protocol, tunnel_id is set to about.labels.key/value, session_id is set to network.session_id
403102
PPP virtual interface {interface_name} rcvd pkt with invalid protocol: {protocol}, reason: {summary}
interface_name is set to about.labels.key/value, protocol is set to network.ip_protocol, summary is set to security_result.summary
403104
PPP virtual interface {interface_name} requires mschap for MPPE
interface_name is set to about.labels.key/value
403106
PPP virtual interface {interface_name} requires RADIUS for MPPE
interface_name is set to about.labels.key/value
403107
PPP virtual interface {interface_name} missing aaa server group info
interface_name is set to about.labels.key/value
403108
PPP virtual interface {interface_name} missing client ip address option
interface_name is set to about.labels.key/value
403109
Rec'd packet not an PPTP packet. ({dst_ip}) dest_address={dst_ip}, src_addr={src_ip}, data:.*
dst_ip is set to target.ip, dst_ip is set to target.ip, src_ip is set to principal.ip
403110
PPP virtual interface {interface_name} , user: {src_username} missing MPPE key from {resource}
interface_name is set to about.labels.key/value, src_username is set to principal.user.userid, resource is set to target.resource.name
403500
PPPoE - Service name 'any' not received in PADO. {interface_name} AC:{ac_name}
interface_name is set to about.labels.key/value, ac_name is set to about.labels.key/value
403501
PPPoE - Bad host-unique in PADO - packet dropped. {interface_name} AC:{ac_name}
interface_name is set to about.labels.key/value, ac_name is set to about.labels.key/value
403502
PPPoE - Bad host-unique in PADS - dropping packet. {interface_name} AC:{ac_name}
interface_name is set to about.labels.key/value, ac_name is set to about.labels.key/value
403503
PPPoE:PPP link down:{summary}
summary is set to security_result.summary
403504
PPPoE:No 'vpdn group {group_name}' for PPPoE is created
group_name is set to target.user.group_identifiers
403505
PPPoE:PPP - Unable to set default route to {dst_ip} at {interface_name}
dst_ip is set to target.ip, interface_name is set to about.labels.key/value
403506
PPPoE:failed to assign PPP {dst_ip} netmask {subnet_mask} at {interface_name}
dst_ip is set to target.ip, subnet_mask is set to about.labels.key/value, interface_name is set to about.labels.key/value
403507
PPPoE:PPPoE client on interface {interface_name} failed to locate PPPoE vpdn group {group_name}
interface_name is set to about.labels.key/value, group_name is set to target.user.group_identifiers
405001
Received ARP {action_details} collision from {dst_ip}/{dst_mac} on interface {interface_name} with existing ARP entry {src_ip}/{src_mac}
action_details is set to security_result.action_details, dst_ip is set to target.ip, dst_mac is set to target.mac, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_mac is set to principal.mac
405002
Received mac mismatch collision from {dst_ip}/{dst_mac} for authenticated host
dst_ip is set to target.ip, dst_mac is set to target.mac
405003
IP address collision detected between host {src_ip} at {src_mac} and interface {interface_name}, {dst_mac}
src_ip is set to principal.ip, src_mac is set to principal.mac, interface_name is set to about.labels.key/value, dst_mac is set to target.mac
405101
Unable to Pre-allocate H225 Call Signalling Connection for (foreign_address|faddr) {dst_ip} /{dst_port}] to (local_address|laddr) {src_ip} [/{src_port}]
dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
405102
Unable to Pre-allocate H245 Connection for (foreign_address|faddr) {dst_ip} /{dst_port}] to (local_address|laddr) {src_ip} [/{src_port}]
dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
405103
H225 message from {src_ip}/{src_port} to {dst_ip}/{dst_port} contains bad protocol discriminator {hex}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, hex is set to about.labels.key/value
405104
H225 message<message_text>received from {dst_ip}/{dst_port} to {src_ip}/{src_port} before SETUP
dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
405105
H323 RAS message AdmissionConfirm received from {dst_ip}/{dst_port} to {src_ip}/{src_port} without an AdmissionRequest
dst_ip is set to target.ip, dst_port is set to target.port, src_ip is set to principal.ip, src_port is set to principal.port
405106
H323 {channel_number} channel is not created from <message_text>
channel_number is set to about.labels.key/value
405201
ILS {ILS_message_type} from {src_interface_name}:{src_ip} to {dst_interface_name}:/{dst_ip} has wrong embedded address {embedded_ip_address}
ILS_message_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, embedded_ip_address is set to about.labels.key/value
405300
Radius Accounting Request received from {dst_ip} is not allowed
dst_ip is set to target.ip
405301
Attribute {attribute_number} does not match for user {dst_ip}
attribute_number is set to about.labels.key/value, dst_ip is set to target.ip
406001
FTP port command low port: {src_ip}/{src_port} to {dst_ip} on interface {interface_name}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
406002
FTP port command different address: IP_address({src_ip}) to {dst_ip} on interface {interface_name}
src_ip is set to principal.ip, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
407001
Deny traffic for local-host {interface_name}:{dst_ip} , license limit of {license_limit_number} exceeded
interface_name is set to about.labels.key/value, dst_ip is set to target.ip, license_limit_number is set to about.labels.key/value
407002
Embryonic limit {nconns}/{elimit} for through connections exceeded.{dst_ip}/{dst_port} to {global_address} ({src_ip})/{src_port} on interface {interface_name}
nconns is set to about.labels.key/value, elimit is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, global_address is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, interface_name is set to about.labels.key/value
408001
IP route counter negative - {summary}, {dst_ip} Attempt: {attempt_number}
summary is set to security_result.summary, dst_ip is set to target.ip, attempt_number is set to about.labels.key/value
408002
ospf process {route_id} {route_name} {route_type} update {address1} {netmask1} {distance1}/{metric1}] via source {src_ip} :{interface1} {address2} {netmask2} [{distance2}/{metric2}] {interface2}
route_id is set to about.labels.key/value, route_name is set to about.labels.key/value, route_type is set to about.labels.key/value, address1 is set to about.labels.key/value, netmask1 is set to about.labels.key/value, distance1 is set to about.labels.key/value, metric1 is set to about.labels.key/value, src_ip is set to principal.ip, interface1 is set to about.labels.key/value, address2 is set to about.labels.key/value, netmask2 is set to about.labels.key/value, distance2 is set to about.labels.key/value, metric2 is set to about.labels.key/value, interface2 is set to about.labels.key/value
408003
can't track this type of object {hex}
hex is set to about.labels.key/value
408101
KEYMAN : Type {encrption_type} encryption unknown. Interpreting keystring as literal
encrption_type is set to about.labels.key/value
408102
KEYMAN : Bad encrypted keystring for {encrypted_key} id {encrypted_key_id}
encrypted_key is set to about.labels.key/value, encrypted_key_id is set to about.labels.key/value
409002
db_free: external LSA {dst_ip} {subnet_mask}
dst_ip is set to target.ip, subnet_mask is set to about.labels.key/value
409003
Received invalid packet: {summary} from {dst_ip} , {interface_name}
summary is set to security_result.summary, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
409004
Received reason from unknown neighbor {dst_ip}
dst_ip is set to target.ip
409005
Invalid length number in OSPF packet from {dst_ip} (ID {src_ip}), {interface_name}
dst_ip is set to target.ip, src_ip is set to principal.ip, interface_name is set to about.labels.key/value
409006
Invalid lsa: {summary} Type {lsa_number} , LSID <message_text> from {dst_ip} , <message_text> , {interface_name}
summary is set to security_result.summary, lsa_number is set to about.labels.key/value, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
409007
Found LSA with the same host bit set but using different mask LSA ID {src_ip} {src_netmask} New: Destination {dst_ip} {dst_netmask}
src_ip is set to principal.ip, src_netmask is set to principal.labels.key/value, dst_ip is set to target.ip, dst_netmask is set to target.labels.key/value
409008, 409106
Found generating default LSA with non-zero mask LSA type: {lsa_number} Mask: {netmask} metric: {metric_number} area: {area}
lsa_number is set to about.labels.key/value, netmask is set to about.labels.key/value, metric_number is set to about.labels.key/value, area is set to about.labels.key/value
409010, 409108
Virtual link information found in non-backbone area: {area}
area is set to about.labels.key/value
409011
OSPF detected duplicate router-id {duplicate_ip} from {dst_ip} on interface {interface_name}
duplicate_ip is set to about.labels.key/value, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
409012
Detected router with duplicate router ID {dst_ip} in area {area}
dst_ip is set to target.ip, area is set to about.labels.key/value
409013
Detected router with duplicate router ID {duplicate_ip} in Type-4 LSA advertised by {dst_ip}
duplicate_ip is set to about.labels.key/value, dst_ip is set to target.ip
409014
No valid authentication send {authentication_key} is available on interface {interface_name}
authentication_key is set to about.labels.key/value, interface_name is set to about.labels.key/value
409015
Key ID {key_id} received on interface {interface_name}
key_id is set to about.labels.key/value, interface_name is set to about.labels.key/value
409016
Key chain name {key_chain_name} on {interface_name} is invalid
key_chain_name is set to about.labels.key/value, interface_name is set to about.labels.key/value
409017
Key ID {key_id} in key chain {key_chain_name} is invalid
key_id is set to about.labels.key/value, key_chain_name is set to about.labels.key/value
409023
Attempting AAA Fallback method {method_name} for {request_type} request for user {user_name} :{auth_server} group {server_tag} unreachable
method_name is set to about.labels.key/value, request_type is set to about.labels.key/value, user_name is set to target.user.userid, auth_server is set to about.labels.key/value, server_
409101
Received invalid packet: {packet} from {sender} , <message_text>
packet is set to about.labels.key/value, sender is set to about.labels.key/value
409102
Received packet with incorrect area from {sender} , {packet} , area {interface_area_id_str} , packet area {packet_area_id_str}
sender is set to about.labels.key/value, packet is set to about.labels.key/value, interface_area_id_str is set to about.labels.key/value, packet_area_id_str is set to about.labels.key/value
409103
Received {packet} from unknown neighbor {neighbor}
packet is set to about.labels.key/value, neighbor is set to about.labels.key/value
409104
Invalid length {packet_length} in OSPF packet type {packet_type} from {sender} (ID {packet_id}), {packet}
packet_length is set to about.labels.key/value, packet_type is set to about.labels.key/value, sender is set to about.labels.key/value, packet_id is set to about.labels.key/value, packet is set to about.labels.key/value
409105
Invalid lsa: {lsa_name} : Type 0x {lsa_type} , Length 0x {lsa_length} , LSID {lsid} from {sender}
lsa_name is set to about.labels.key/value, lsa_type is set to about.labels.key/value, lsa_length is set to about.labels.key/value, lsid is set to about.labels.key/value, sender is set to about.labels.key/value
409107
OSPFv3 process {target_process_name} could not pick a router-id, please configure manually
target_process_name is set to target.process.pid
409109
OSPF detected duplicate router-id {router_id} from <message_text> on interface {interface_name}
router_id is set to about.labels.key/value, interface_name is set to about.labels.key/value
409110
Detected router with duplicate router ID {router_id} in area {area_id_str}
router_id is set to about.labels.key/value, area_id_str is set to about.labels.key/value
409111
Multiple interfaces ({interface_name}) on a single link detected
interface_name is set to about.labels.key/value
409114
Doubly linked list prev linkage is NULL {summary}
summary is set to security_result.summary
409115
Unrecognized timer {timer} in OSPF {ofps}
timer is set to about.labels.key/value, ofps is set to about.labels.key/value
409116
Error for timer {timer} in OSPF process {target_process_name}
timer is set to about.labels.key/value, target_process_name is set to target.process.pid
409117
Can't find LSA database type {database_type}, area {area_id_str}, interface {interface_name}
database_type is set to about.labels.key/value, area_id_str is set to about.labels.key/value, interface_name is set to about.labels.key/value
409120, 613029
Router-ID {router_id} is in use by ospf process {ospf_process}
router_id is set to about.labels.key/value, ospf_process is set to about.labels.key/value
409128
OSPFv3<message_text>Area {area_id_str}: Router {router} originating invalid<message_text>, ID {id}, Metric {metric_number} on Link ID {link_id} Link Type {link_type}
area_id_str is set to about.labels.key/value, router is set to about.labels.key/value, id is set to about.labels.key/value, metric_number is set to about.labels.key/value, link_id is set to about.labels.key/value, link_type is set to about.labels.key/value
410001
({action} )?(?P<protocol>UDP) DNS <message_text> from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port};<message_text>length <message_text> bytes exceeds (remaining packet length|protocol|configured)( limit of)? <message_text> bytes
protocol is set to network.ip_protocol, action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
410002
(?P<action>Dropped) {dropped_requests} (?P<protocol>DNS) responses with mis-matched id in the past {seconds}<message_text> from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
action is set to security_result.action, protocol is set to network.ip_protocol, dropped_requests is set to about.labels.key/value, seconds is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
410003, 410004
{action_class}:{action} DNS (query|response) from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
action_class is set to about.labels.key/value, action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
411001, 411002
Line protocol on (interface|Interface) {interface_name} changed state to <message_text>
interface_name is set to about.labels.key/value
411005
Interface {interface_name} experienced a hardware transmit hang. The interface has been reset
interface_name is set to about.labels.key/value
412001
MAC {src_mac} moved from {src_interface_name} to {dst_interface_name}
src_mac is set to principal.mac, src_interface_name is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value
412002
Detected bridge table full while inserting MAC {src_mac} on interface {src_interface_name}. Number of entries = {no_of_fields}
src_mac is set to principal.mac, src_interface_name is set to principal.labels.key/value, no_of_fields is set to about.labels.key/value
413001, 413002
Module {module_id} is not able to (shut down|reload). Module Error: {summary}
module_id is set to about.labels.key/value, summary is set to security_result.summary
413003
Module {module_name} one is not a recognized type
module_name is set to about.labels.key/value
413004
Module {module_name} one failed to write software {new_version_number} (currently {current_version_number}), {summary}. Trying again
module_name is set to about.labels.key/value, new_version_number is set to about.labels.key/value, current_version_number is set to about.labels.key/value, summary is set to security_result.summary
413005
Module {product_id} in slot {slot_number}, application is not supported {target_service} version {app_version} type {app_type}
product_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, target_service is set to target.application, app_version is set to about.labels.key/value, app_type is set to about.labels.key/value
413005
Module {module_id}, application is not supported {target_service} version {app_version} type {app_type}
module_id is set to about.labels.key/value, target_service is set to target.application, app_version is set to about.labels.key/value, app_type is set to about.labels.key/value
413006
{product_id} Module software version mismatch; slot {slot_number} is<message_text>version {running_version}. Slot <message_text>requires {required_version}
product_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, running_version is set to about.labels.key/value, required_version is set to about.labels.key/value
413007
An unsupported ASA and IPS configuration is installed. {mpc_description} with {ips_description} is not supported
mpc_description is set to about.labels.key/value, ips_description is set to about.labels.key/value
414001
Failed to save logging buffer using file name {src_file_full_path} to FTP server {src_ip} on interface {interface_name}: {summary}
src_file_full_path is set to src.file.full_path, src_ip is set to principal.ip, interface_name is set to about.labels.key/value, summary is set to security_result.summary
414002
Failed to save logging buffer to flash:/syslog directory using file name: {src_file_full_path}: {summary}
src_file_full_path is set to src.file.full_path, summary is set to security_result.summary
414003
(?P<protocol>TCP) Syslog Server {src_interface_name}:{src_ip}/{src_port} not responding, New connections are (?P<action>permitted|denied) based on logging permit-hostdown policy
protocol is set to network.ip_protocol, action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port
414004
(?P<protocol>TCP) Syslog Server {src_interface_name}:{src_ip}/{src_port}- Connection restored
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port
414005
(?P<protocol>TCP) Syslog Server {src_interface_name}:{src_ip}/{src_port} connected, New connections are permitted based on logging permit-hostdown policy
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port
415001, 415002
HTTP - matched {matched_string} in policy-map {map_name}, header field <message_text> exceeded {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415003, 415005, 415018
HTTP - matched {matched_string} in policy-map {map_name}, <message_text> length exceeded {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415004
HTTP - matched {matched_string} in policy-map {map_name}, content-type verification failed {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415006, 415007, 415008, 415009
HTTP - matched {matched_string} in policy-map {map_name}, <message_text> matched {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415010
matched {matched_string} in policy-map {map_name}, transfer encoding matched {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415011
HTTP - policy-map {map_name} :Protocol violation {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415012
HTTP - matched {matched_string} in policy-map {map_name}, (Unknown|unknown) mime-type {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415013
HTTP - policy-map {map_name}:(Malformed|malformed) chunked encoding {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415014
HTTP - matched {matched_string} in policy-map {map_name}, Mime-type in response wasn't found in the accept-types of the request {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415015
HTTP - matched {matched_string} in policy-map {map_name}, transfer-encoding unknown {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415017
HTTP - {matched_string} in policy-map {map_name}, <message_text> matched {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415016
policy-map {policy_name}:Maximum number of unanswered HTTP requests exceeded {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
policy_name is set to target.resource.name, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415019
HTTP - matched {matched_string} in policy-map {map_name}, status line matched {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
415020
HTTP - matched {matched_string} in policy-map {map_name}, a non-ASCII character was matched {connection_action} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
matched_string is set to about.labels.key/value, map_name is set to about.labels.key/value, connection_action is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
416001
(?P<action>Dropped) (?P<protocol>UDP) SNMP packet from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}; version ({version_protocol}) is not allowed (through|thru) the firewall
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, version_protocol is set to network.tls.version_protocol
417004
Filter violation error: conn {modified_attribute_number} <message_text>
modified_attribute_number is set to about.labels.key/value
417006
No memory for {operation} ) in {dst_operation}. Handling: {another_mechanism}
operation is set to about.labels.key/value, dst_operation is set to about.labels.key/value, another_mechanism is set to about.labels.key/value
418001
Through-the-device packet to/from management-only network is denied: {protocol} src {src_interface_name}:{src_ip}/{src_port} dst {dst_interface_name}:{dst_ip}/{dst_port}
Through-the-device packet to/from management-only network is denied: {protocol} from {src_interface_name} {src_ip} ({src_port}) ([<message_text>], {src_sg_info} )] to {dst_interface_name} {dst_ip} ({dst_port}) [(<message_text> ), {dst_sg_info} ]
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_sg_info is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_sg_info is set to target.labels.key/value
418018
neighbor {dst_ip} IPv4 Unicast topology base removed from session {summary}
dst_ip is set to target.ip, summary is set to security_result.summary
418018
neighbor {dst_ip} (Down|Up){summary}
dst_ip is set to target.ip, summary is set to security_result.summary
418019
(sent to|received from) neighbor {dst_ip}, Reason: {summary}, Bytes: {bytes_transferred}
dst_ip is set to target.ip, summary is set to security_result.summary, bytes_transferred is set to about.labels.key/value
418019
(sent to|received from) neighbor {dst_ip}<message_text>bytes {bytes_transferred}
dst_ip is set to target.ip, bytes_transferred is set to about.labels.key/value
418019
(received from|sent to) neighbor {dst_ip}<message_text>{bytes_transferred} bytes
dst_ip is set to target.ip, bytes_transferred is set to about.labels.key/value
419001
Dropping {protocol} packet from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} , {summary} : MSS exceeded, MSS {mss_size} , data {data_size}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary, mss_size is set to about.labels.key/value, data_size is set to about.labels.key/value
419002
(Received )?(duplicate|Duplicate) TCP SYN from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} with different initial sequence number
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
419003
Cleared {protocol} urgent flag from {dst_interface_name}:{src_ip}/{src_port} to {src_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, dst_interface_name is set to target.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_interface_name is set to principal.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
419004
TCP connection {connection_id} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} is probed by DCD
connection_id is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
419005
TCP connection {connection_id} from {src_interface_name}:{src_ip}/{src_port} duration {duration} data {bytes_transferred}, is kept open by DCD as valid connection
connection_id is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, duration is set to network.session_duration, bytes_transferred is set to about.labels.key/value
419006
TCP connection {connection_id} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} duration{duration} data {bytes_transferred}, DCD probe was not responded from (client|server) interface {interface_name}
connection_id is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, duration is set to network.session_duration, bytes_transferred is set to about.labels.key/value, interface_name is set to about.labels.key/value
420001
IPS card not up and fail-close mode used, dropping ICMP packet {src_interface_name}:{src_ip} to {dst_interface_name}:{dst_ip} (type {icmp_type}, code {icmp_code} )
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value
420002
IPS requested to drop {protocol} packet(s)?( from)? {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?( (type {icmp_type}, code {icmp_code} ))?
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, icmp_type is set to about.labels.key/value, icmp_code is set to about.labels.key/value
420003
IPS requested to reset TCP connection from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
420004
Virtual Sensor {sensor_name} was added on the AIP SSM
sensor_name is set to about.labels.key/value
420005
Virtual Sensor {sensor_name} was deleted on the AIP SSM
sensor_name is set to about.labels.key/value
420006
Virtual Sensor not present and fail-close mode used, dropping {protocol} packet from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
420007
{target_service} cannot be enabled for the module in slot {slot_id}. The module's current software version does not support this feature. Upgrade the software on the module in slot slot_id to support this feature. Received backplane header version {version_number}, required backplane header version version_number or higher.
target_service is set to target.application, slot_id is set to about.labels.key/value, version_number is set to about.labels.key/value
421001
(TCP|UDP) flow from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} is dropped because {target_service} has failed
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, target_service is set to target.application
421002
(TCP|UDP) flow from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} bypassed {target_service} checking because the protocol is not supported
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, target_service is set to target.application
421005
{interface_name} :{dst_ip} is counted as a user of {target_service}
interface_name is set to about.labels.key/value, dst_ip is set to target.ip, target_service is set to target.application
421006
There are {no_of_users} users of {target_service} accounted during the past 24 hours
no_of_users is set to about.labels.key/value, target_service is set to target.application
421007
{protocol} flow from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} is skipped because {target_service} has failed
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, target_service is set to target.application
422004
IP SLA Monitor {sla_operation_number}: Duplicate event received. Event number {sla_operation_event_id}
sla_operation_number is set to about.labels.key/value, sla_operation_event_id is set to about.labels.key/value
422006
IP SLA Monitor Probe {sla_id}:{summary}
sla_id is set to about.labels.key/value, summary is set to security_result.summary
423001, 423002
(?P<action>Allowed|Dropped) (invalid|mismatched) NBNS {pkt_type_name} with {summary} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
action is set to security_result.action, pkt_type_name is set to about.labels.key/value, summary is set to security_result.summary, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
423003, 423004
(?P<action>Allowed|Dropped) (invalid|mismatched) NBDGM {pkt_type_name} with {summary} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
action is set to security_result.action, pkt_type_name is set to about.labels.key/value, summary is set to security_result.summary, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
423005
(?P<action>Allowed|Dropped) NBDGM {pkt_type_name} fragment with {summary} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
action is set to security_result.action, pkt_type_name is set to about.labels.key/value, summary is set to security_result.summary, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
424001
Packet (?P<action>denied) {protocol} {src_interface_name}:{src_ip}/{src_port}( ({src_fwuser}))? {dst_interface_name}:{dst_ip}/{dst_port}( ({dst_fwuser}))?. (Ingress|Egress) interface is in a backup state
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_fwuser is set to principal.user.userid/principal.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, dst_fwuser is set to target.user.userid/target.labels.key/value
424002
Connection to the backup interface is (?P<action>denied): {protocol} {src_interface_name}:{src_ip}(/{src_port})? {dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
425003, 425004
Interface {src_interface_name} (added|removed) (into|from) redundant interface {dst_interface_name}
src_interface_name is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value
425001, 425002
Redundant interface {src_interface_name} (removed|created)
src_interface_name is set to principal.labels.key/value
425005
Interface {src_interface_name} become active in redundant interface {dst_interface_name}
src_interface_name is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value
425006
Redundant interface {dst_interface_name} switch active member to {src_interface_name} failed
dst_interface_name is set to target.labels.key/value, src_interface_name is set to principal.labels.key/value
426001, 426002
PORT-CHANNEL:Interface {src_interface_name} <message_text> <message_text> EtherChannel interface Port-channel {port_channel}
src_interface_name is set to principal.labels.key/value, port_channel is set to about.labels.key/value
426003
PORT-CHANNEL:Interface {src_interface_name} has become standby in EtherChannel interface Port-channel {port_channel}
src_interface_name is set to principal.labels.key/value, port_channel is set to about.labels.key/value
426004
PORT-CHANNEL: Interface {src_interface_name} is not compatible with {dst_interface_name} and will be suspended <message_text>
src_interface_name is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value
426101, 426102
PORT-CHANNEL:Interface {src_interface_name} is <message_text> to <message_text> <message_text> EtherChannel interface {port_channel} by CLACP
src_interface_name is set to principal.labels.key/value, port_channel is set to about.labels.key/value
426103
PORT-CHANNEL:Interface {src_interface_name} is selected to move from standby to bundle in EtherChannel interface {port_channel} by CLACP
src_interface_name is set to principal.labels.key/value, port_channel is set to about.labels.key/value
426104
PORT-CHANNEL:Interface {src_interface_name} is unselected in EtherChannel interface {port_channel} by CLACP
src_interface_name is set to principal.labels.key/value, port_channel is set to about.labels.key/value
428002
WAAS confirmed from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, inspection services bypassed on this connection
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
429001
CXSC card not up and fail-close mode used. (?P<action>Dropping) {protocol} packet from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
429002, 429003
CXSC service card requested to (?P<action>drop|reset) {protocol} (packet|connection) from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
429004
Unable to set up authentication-proxy rule for the cx action on interface {src_interface_name} for {policy_type} service-policy
src_interface_name is set to principal.labels.key/value, policy_type is set to about.labels.key/value
429005
Set up authentication-proxy {protocol} rule for the CXSC action on interface {dst_interface_name} for traffic destined to {dst_ip}/{dst_port} for {policy_type} service-policy
protocol is set to network.ip_protocol, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, policy_type is set to about.labels.key/value
429006
Cleaned up authentication-proxy rule for the CXSC action on interface {dst_interface_name} for traffic destined to {dst_ip} for {policy_type} service-policy
dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, policy_type is set to about.labels.key/value
429007
CXSC redirect will override Scansafe redirect for flow from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port} with {user_name}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
429008
Unable to respond to VPN query from CX for session {session_id}. Reason {summary}
session_id is set to network.session_id, summary is set to security_result.summary
4302310
SCTP packet received from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port} contains unsupported<message_text>
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
431001, 431002
<message_text> conformance: (?P<action>Dropping) <message_text> packet from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, Drop reason: {summary}
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
434001
SFR card not up and fail-close mode used, (?P<action>dropping) {protocol} packet from ingress {src_interface_name}:{src_ip}(/{src_port})? to egress {dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
434002, 434003
SFR requested to (?P<action>drop|reset) {protocol} (packet|connection) from (ingress )?{src_interface_name}:{src_ip}(/{src_port})? to (egress )?{dst_interface_name}:{dst_ip}(/{dst_port})?
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
434004
SFR requested <message_text> to bypass further packet redirection and process<message_text>flow from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port} locally
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
434007
SFR redirect will override Scansafe redirect for flow from ingress {src_interface_name}:{src_ip}(/{src_port})? to egress {dst_interface_name}:{dst_ip}/{dst_port} ({user_name})
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
444004
Temporary license key {temporary_key} has expired. Applying permanent license key {permanent_key}
temporary_key is set to about.labels.key/value, permanent_key is set to about.labels.key/value
444005
Timebased activation key {activation_key} will expire in {days_left} days
activation_key is set to about.labels.key/value, days_left is set to about.labels.key/value
444007
Timebased activation key {activation_key} has expired. Reverting to (permanent|timebased) license key. The following features will be affected: {feature_affected}
activation_key is set to about.labels.key/value, feature_affected is set to about.labels.key/value
444008
{target_license} license has expired, and the system is scheduled to reload in {days_left} days. Apply a new activation key to enable <message_text> license and prevent the automatic reload
target_license is set to target.labels.key/value, days_left is set to about.labels.key/value
444009
{target_license} license has expired 30 days ago. The system will now reload
target_license is set to target.labels.key/value
444100
Shared {request} request failed. Reason: {summary}
request is set to about.labels.key/value, summary is set to security_result.summary
444101
Shared license service is active. License server address:{dst_ip}
dst_ip is set to target.ip
444103
Shared {license_type} license usage is over 90% capacity
license_type is set to about.labels.key/value
444104
Shared {license_type} license availability: {license_availability}
license_type is set to about.labels.key/value, license_availability is set to about.labels.key/value
444105
Released {license_availability} shared {license_type} license<message_text>License server has been unreachable for 24 hours
license_availability is set to about.labels.key/value, license_type is set to about.labels.key/value
444106
Shared license backup server {dst_ip} is not available
dst_ip is set to target.ip
444107
Shared license service {status} on interface {dst_interface_name}
status is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value
444108
Shared license {status} client id {user_name}
status is set to about.labels.key/value, user_name is set to target.user.userid
444109
Shared license backup server role changed to {status}
status is set to about.labels.key/value
444110
Shared license server backup has {days_left} remaining as active license server
days_left is set to about.labels.key/value
444111
Shared license backup service has been terminated due to the primary license server {dst_ip} being unavailable for more than {days_left} days. The license server needs to be brought back online to continue using shared licensing
dst_ip is set to target.ip, days_left is set to about.labels.key/value
446001
Maximum TLS Proxy session limit of {max_session} reached
max_session is set to about.labels.key/value
446003
(?P<action>Denied) TLS Proxy session from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, UC-IME license is disabled
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
447001
ASP DP to CP {queue_name} was full. Queue length {queue_length}, limit {queue_limit}
queue_name is set to about.labels.key/value, queue_length is set to about.labels.key/value, queue_limit is set to about.labels.key/value
448001
(?P<action>Denied) SRTP crypto session setup on flow from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port}, licensed K8 SRTP crypto session of {k8_limit} exceeded
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, k8_limit is set to about.labels.key/value
450001
Deny traffic for protocol {protocol_id} src {src_interface_name}:{src_ip}(/{src_port})? dst {dst_interface_name}:{dst_ip}/{dst_port}, licensed host limit of {maximum_host} exceeded
protocol_id is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, maximum_host is set to about.labels.key/value
500001
ActiveX content in java script is modified: src {src_ip} dest {dst_ip} on interface {interface_name}
src_ip is set to principal.ip, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
500002
Java content in java script is modified: src {src_ip} dest {dst_ip} on interface {interface_name}
src_ip is set to principal.ip, dst_ip is set to target.ip, interface_name is set to about.labels.key/value
500003
Bad {protocol} hdr length (hdrlen={hdr_len}, pktlen={pkt_len}) from {src_ip}(/{src_port})? to {dst_ip}/{dst_port}, flags: {tcp_flags}, on interface {interface_name}
protocol is set to network.ip_protocol, hdr_len is set to about.labels.key/value, pkt_len is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, tcp_flags is set to about.labels.key/value, interface_name is set to about.labels.key/value
500004
Invalid transport field for protocol={protocol}, from {src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
500005
connection terminated for {protocol} from {input_interface} :{src_ip}(/{src_port})? to {output_interface} :{dst_ip}/{dst_port} due to invalid combination of inspections on same flow. Inspect {inspect_name} is not compatible with filter {filter_name}
protocol is set to network.ip_protocol, input_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, output_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, inspect_name is set to about.labels.key/value, filter_name is set to about.labels.key/value
502101
New user added to local dbase: Uname: {user_name} Priv: {privilege_level} Encpass: {encrypted_pass}
user_name is set to target.user.userid, privilege_level is set to about.labels.key/value, encrypted_pass is set to about.labels.key/value
502102
User deleted from local dbase: Uname: {user_name} Priv: {privilege_level} Encpass: {encrypted_pass}
user_name is set to target.user.userid, privilege_level is set to about.labels.key/value, encrypted_pass is set to about.labels.key/value
502103
User priv level changed: Uname: {user_name} From: {old_privilege_level} To: {new_privilege_level}
user_name is set to target.user.userid, old_privilege_level is set to about.labels.key/value, new_privilege_level is set to about.labels.key/value
502111
New group policy added: name: {group_policy} Type: {policy_type}
group_policy is set to about.labels.key/value, policy_type is set to about.labels.key/value
502112
Group policy deleted: name: {group_policy} Type: {policy_type}
group_policy is set to about.labels.key/value, policy_type is set to about.labels.key/value
503001, 503101
Process {process_number}, Nbr {src_ip} on {interface_name} from .*, {summary}
process_number is set to about.labels.key/value, src_ip is set to principal.ip, interface_name is set to about.labels.key/value, summary is set to security_result.summary
503002
The last key has expired for interface {interface_name}, packets sent using last valid key
interface_name is set to about.labels.key/value
503003
Packet <message_text> on interface {interface_name} with expired Key ID {key_id}
interface_name is set to about.labels.key/value, key_id is set to about.labels.key/value
503004
Key ID {key_id} in key chain {key_chain_name} does not have a key
key_id is set to about.labels.key/value, key_chain_name is set to about.labels.key/value
503005
Key ID {key_id} in key chain {key_chain_name} does not have a cryptographic algorithm
key_id is set to about.labels.key/value, key_chain_name is set to about.labels.key/value
504001
Security context {context_name} was added to the system
context_name is set to about.labels.key/value
504002
Security context {context_name} was removed from the system
context_name is set to about.labels.key/value
505002
Module {ips_description} is reloading. Please wait
ips_description is set to about.labels.key/value
505005
Module {module_name} is initializing control communication.*
module_name is set to about.labels.key/value
505007
Module {prod_id} in slot {slot_number} is recovering. Please wait.*
prod_id is set to about.labels.key/value, slot_number is set to about.labels.key/value
505007
Module {module_id} is recovering.*
module_id is set to about.labels.key/value
505008
Module {module_id} in slot {slot_number} software is being updated to {newver} (currently {version})
module_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, newver is set to about.labels.key/value, version is set to about.labels.key/value
505008
Module {module_id} software is being updated to {newver} (currently {version})
module_id is set to about.labels.key/value, newver is set to about.labels.key/value, version is set to about.labels.key/value
505009
Module {modual} one software was updated to {new_version_number}
modual is set to about.labels.key/value, new_version_number is set to about.labels.key/value
505010
Module in slot {slot_number} removed
slot_number is set to about.labels.key/value
505011
Module {module_name}(,)? data channel communication is UP
module_name is set to about.labels.key/value
505016
Module {prod_id} in slot {slot_number} application changed from: {src_service} version {src_application_version} state {src_application_state} to: {target_service} {dst_application_version} state {dst_application_state}
prod_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, src_service is set to principal.application, src_application_version is set to principal.labels.key/value, src_application_state is set to principal.labels.key/value, target_service is set to target.application, dst_application_version is set to target.labels.key/value, dst_application_state is set to target.labels.key/value
505016
Module {module_id} application changed from: {src_service} version {src_application_version} state {src_application_state} to: {target_service} {dst_application_version} state {dst_application_state}
module_id is set to about.labels.key/value, src_service is set to principal.application, src_application_version is set to principal.labels.key/value, src_application_state is set to principal.labels.key/value, target_service is set to target.application, dst_application_version is set to target.labels.key/value, dst_application_state is set to target.labels.key/value
505012
Module {prod_id} in slot {slot_number}, application stopped {target_service}, version {version}
prod_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, target_service is set to target.application, version is set to about.labels.key/value
505012
Module {module_id}, application stopped {target_service}, version {version}
module_id is set to about.labels.key/value, target_service is set to target.application, version is set to about.labels.key/value
505013
Module {prod_id} in slot {slot_number}(,)? application (changed from:)?(reloading)? {src_service}(,)? version {version}( to: {target_service} version {new_version_number})?
prod_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, src_service is set to principal.application, version is set to about.labels.key/value, target_service is set to target.application, new_version_number is set to about.labels.key/value
505013
Module {module_id} application changed from: {src_service} version {version} to: {target_service} version {new_version_number}
module_id is set to about.labels.key/value, src_service is set to principal.application, version is set to about.labels.key/value, target_service is set to target.application, new_version_number is set to about.labels.key/value
505014
Module {prod_id} in slot {slot_number}, application down {target_service}, version {version} {summary}
prod_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, target_service is set to target.application, version is set to about.labels.key/value, summary is set to security_result.summary
505014
Module {module_id}, application down {target_service}, version {version} {summary}
module_id is set to about.labels.key/value, target_service is set to target.application, version is set to about.labels.key/value, summary is set to security_result.summary
505015
Module {prod_id} in slot {slot_number}, application up {target_application}, version {version}
prod_id is set to about.labels.key/value, slot_number is set to about.labels.key/value, version is set to about.labels.key/value
505015
Module {module_id}, application up {target_service}, version {version}
module_id is set to about.labels.key/value, target_service is set to target.application, version is set to about.labels.key/value
507001
(?P<action>Terminating) (?P<protocol>TCP)-Proxy connection from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}- reassembly limit of {limit} bytes exceeded
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, limit is set to about.labels.key/value
507003
The flow of type {protocol} from the originating interface:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} (?P<action>terminated) by inspection engine, {summary}
action is set to security_result.action, protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
507003
{protocol} flow from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} (?P<action>terminated) by inspection engine, {summary}
action is set to security_result.action, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
508001
DCERPC {message_type} non-standard {version_type} version {version_number} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}, (?P<action>terminating) connection
action is set to security_result.action, message_type is set to about.labels.key/value, version_type is set to about.labels.key/value, version_number is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
508002
DCERPC response has low endpoint port {port_number} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}, (?P<action>terminating) connection
action is set to security_result.action, port_number is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
509001
Connection attempt from {src_interface_name}:{src_ip}/{src_port}( ((?:{outside_idfw_user})?(,)?(?:{outside_sg_info})?))? to {dst_interface_name}:{dst_ip}/{dst_port}( ((?:{inside_idfw_user})?(,)?(?:{inside_sg_info})?))? was prevented by no forward" command"
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, outside_idfw_user is set to about.labels.key/value, outside_sg_info is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, inside_idfw_user is set to about.labels.key/value, inside_sg_info is set to about.labels.key/value
520003
bad id in {summary} (id:<message_text>)
summary is set to security_result.summary
520010
Bad queue elem – {queue_pointer}: flink {forward_pointer}, blink {backward_pointer}, flink-blink {flink_blink_ptr}, blink-flink {blink_flink_ptr}
queue_pointer is set to about.labels.key/value, forward_pointer is set to about.labels.key/value, backward_pointer is set to about.labels.key/value, flink_blink_ptr is set to about.labels.key/value, blink_flink_ptr is set to about.labels.key/value
520013
Regular expression access check with bad list {acl_id}
acl_id is set to about.labels.key/value
520021
Error deleting trie entry, {summary}
summary is set to security_result.summary
520022
Error adding mask entry, {summary}
summary is set to security_result.summary
520023
Invalid pointer to head of tree, 0x {radix_node_ptr}
radix_node_ptr is set to about.labels.key/value
520024
Orphaned mask {orphaned_mask}, refcount= {radix_mask_ptrs} ref count at {radix_node_address}, next= {radix_node_nxt}
orphaned_mask is set to about.labels.key/value, radix_mask_ptrs is set to about.labels.key/value, radix_node_address is set to about.labels.key/value, radix_node_nxt is set to about.labels.key/value
520025
No memory for radix initialization: {summary}
summary is set to security_result.summary
602101
PMTU-D packet {no_of_bytes} bytes greater than effective mtu {mtu_number}(,)? dest_addr={dst_ip}, src_addr={src_ip}, prot={protocol}
no_of_bytes is set to about.labels.key/value, mtu_number is set to about.labels.key/value, dst_ip is set to target.ip, src_ip is set to principal.ip, protocol is set to network.ip_protocol
602103
(?P<category>IPSEC): Received an {protocol} Destination Unreachable from {src_ip} with suggested PMTU of {rcvd_mtu}; PMTU updated for SA with peer {dst_ip}, SPI {spi}, tunnel name {user_name}, old PMTU {old_mtu}, new PMTU {new_mtu}
category is set to security_result.category_details, protocol is set to network.ip_protocol, src_ip is set to principal.ip, rcvd_mtu is set to about.labels.key/value, dst_ip is set to target.ip, spi is set to about.labels.key/value, user_name is set to target.user.userid, old_mtu is set to about.labels.key/value, new_mtu is set to about.labels.key/value
602104
(?P<category>IPSEC): Received an {protocol} Destination Unreachable from {src_ip}, PMTU is unchanged because suggested PMTU of {rcvd_mtu} is equal to or greater than the current PMTU of {curr_mtu}, for SA with peer {dst_ip}, SPI {spi}, tunnel name {user_name}
category is set to security_result.category_details, protocol is set to network.ip_protocol, src_ip is set to principal.ip, rcvd_mtu is set to about.labels.key/value, curr_mtu is set to about.labels.key/value, dst_ip is set to target.ip, spi is set to about.labels.key/value, user_name is set to target.user.userid
602303, 602304
(?P<category>IPSEC): An (?P<direction>inbound|outbound|INBOUND|OUTBOUND|Inbound|Outbound) {tunnel_type} SA (SPI={spi}) between {src_ip} and {dst_ip} ({src_fwuser}) has been (?P<action_details>created|deleted)
category is set to security_result.category_details, direction is set to network.direction, action_details is set to security_result.action_details, tunnel_type is set to about.labels.key/value, spi is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value
602305
(?P<category>IPSEC): SA creation error, source {src_ip}, destination {dst_ip}, reason {summary}
category is set to security_result.category_details, src_ip is set to principal.ip, dst_ip is set to target.ip, summary is set to security_result.summary
602306
(?P<category>IPSEC): SA change peer IP error, SPI: <message_text>, (src {src_ip}, dest {dst_ip} is set to src {src_ip1}, dest: {dst_ip1}), reason {summary}
category is set to security_result.category_details, src_ip is set to principal.ip, dst_ip is set to target.ip, src_ip1 is set to principal.ip, dst_ip1 is set to target.ip, summary is set to security_result.summary
602306
%(?P<category>IPSEC): SA change peer IP error, SPI: <message_text>, (src {old_src_port}, dest {old_dst_port} is set to src {src_port}, dest: {dst_port}), reason {summary}
category is set to security_result.category_details, old_src_port is set to principal.labels.key/value, old_dst_port is set to target.labels.key/value, src_port is set to principal.port, dst_port is set to target.port, summary is set to security_result.summary
603101
PPTP received out of seq or duplicate pkt, tnl_id={tunnel_id}, sess_id={session_id}, seq={sequence_number}
tunnel_id is set to about.labels.key/value, session_id is set to network.session_id, sequence_number is set to about.labels.key/value
603102
PPP virtual interface {interface_name} - user: {user_name} aaa authentication {status}
interface_name is set to about.labels.key/value, user_name is set to target.user.userid, status is set to about.labels.key/value
603104
PPTP Tunnel created, tunnel_id is {tunnel_id}, remote_peer_ip is {dst_ip}, ppp_virtual_interface_id is {ppp_virtual_interface_id}, client_dynamic_ip is {dst_ip1}, username is {user_name}, MPPE_key_strength is {mppe_key_strength}
tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip, ppp_virtual_interface_id is set to about.labels.key/value, dst_ip1 is set to target.ip, user_name is set to target.user.userid, mppe_key_strength is set to about.labels.key/value
603105
PPTP Tunnel deleted, tunnel_id = {tunnel_id}, remote_peer_ip= {dst_ip}
tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip
603106
L2TP Tunnel created, tunnel_id is {tunnel_id}, remote_peer_ip is {dst_ip}, ppp_virtual_interface_id is {ppp_virtual_interface_id}, client_dynamic_ip is {dst_ip1}, username is {user_name}
tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip, ppp_virtual_interface_id is set to about.labels.key/value, dst_ip1 is set to target.ip, user_name is set to target.user.userid
603107
L2TP Tunnel deleted, tunnel_id = {tunnel_id}, remote_peer_ip = {dst_ip}
tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip
603108
Built PPTP Tunnel at {interface_name}, tunnel-id = {tunnel_id}, remote-peer = {dst_ip}, virtual-interface = {virtual_interface_number}, client-dynamic-ip = {dst_ip1}, username = {user_name}, MPPE-key-strength = {mppe_key_strength}
interface_name is set to about.labels.key/value, tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip, virtual_interface_number is set to about.labels.key/value, dst_ip1 is set to target.ip, user_name is set to target.user.userid, mppe_key_strength is set to about.labels.key/value
603109
Teardown PPPOE Tunnel at {interface_name}, tunnel-id = {tunnel_id}, remote-peer = {dst_ip}
interface_name is set to about.labels.key/value, tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip
603110
Failed to establish L2TP session, tunnel_id = {tunnel_id}, remote_peer_ip ={dst_ip}, user = {user_name}. Multiple sessions per tunnel are not supported
tunnel_id is set to about.labels.key/value, dst_ip is set to target.ip, user_name is set to target.user.userid
604101
DHCP client interface {interface_name}: Allocated ip = {dst_ip}, mask = {netmask}, gw = {gateway_address}
interface_name is set to about.labels.key/value, dst_ip is set to target.ip, netmask is set to about.labels.key/value, gateway_address is set to about.labels.key/value
604102
DHCP client interface {interface_name}: address released
interface_name is set to about.labels.key/value
604103
DHCP daemon interface {interface_name}: address granted {dst_mac} ({dst_ip})
interface_name is set to about.labels.key/value, dst_mac is set to target.mac, dst_ip is set to target.ip
604104
DHCP daemon interface {interface_name}: address released {build_number} ({dst_ip})
interface_name is set to about.labels.key/value, build_number is set to about.labels.key/value, dst_ip is set to target.ip
604105
{category}: Unable to send DHCP reply to client {dst_mac} on interface {interface_name}. Reply exceeds options field size ({options_field_size}) by {number_of_octets} octets
category is set to security_result.category_details, dst_mac is set to target.mac, interface_name is set to about.labels.key/value, options_field_size is set to about.labels.key/value, number_of_octets is set to about.labels.key/value
604201
DHCPv6 PD client on interface {interface_name} received delegated prefix {prefix} from DHCPv6 PD server {sname} with preferred lifetime {preferred_lifetime} seconds and valid lifetime (<|){lease_time_seconds}(|>) seconds
interface_name is set to about.labels.key/value, prefix is set to about.labels.key/value, sname is set to network.dhcp.sname, preferred_lifetime is set to about.labels.key/value, lease_time_seconds is set to network.dhcp.lease_time_seconds
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604202
DHCPv6 PD client on interface {interface_name} releasing delegated prefix {prefix} received from DHCPv6 PD server {sname}
interface_name is set to about.labels.key/value, prefix is set to about.labels.key/value, sname is set to network.dhcp.sname
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604203
DHCPv6 PD client on interface {interface_name} renewed delegated prefix {prefix} from DHCPv6 PD server {sname} with preferred lifetime {preferred_lifetime} seconds and valid lifetime (<|){lease_time_seconds}(|>) seconds
interface_name is set to about.labels.key/value, prefix is set to about.labels.key/value, sname is set to network.dhcp.sname, preferred_lifetime is set to about.labels.key/value, lease_time_seconds is set to network.dhcp.lease_time_seconds
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604204
DHCPv6 delegated prefix {prefix} got expired on interface {interface_name}, received from DHCPv6 PD server {sname}
prefix is set to about.labels.key/value, interface_name is set to about.labels.key/value, sname is set to network.dhcp.sname
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604205
DHCPv6 client on interface {interface_name} allocated address (<|){dst_ip}(|>) from DHCPv6 server {sname} with preferred lifetime {preferred_lifetime} seconds and valid lifetime (<|){lease_time_seconds}(|>) seconds
interface_name is set to about.labels.key/value, dst_ip is set to target.ip, sname is set to network.dhcp.sname, preferred_lifetime is set to about.labels.key/value, lease_time_seconds is set to network.dhcp.lease_time_seconds
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604206
DHCPv6 client on interface {interface_name} releasing address (<|){dst_ip}(|>) received from DHCPv6 server {sname}
interface_name is set to about.labels.key/value, dst_ip is set to target.ip, sname is set to network.dhcp.sname
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604207
DHCPv6 client on interface {interface_name} renewed address (<|){dst_ip}(|>) from DHCPv6 server {sname} with preferred lifetime {preferred_lifetime} seconds and valid lifetime (<|){lease_time_seconds}(|>) seconds
interface_name is set to about.labels.key/value, dst_ip is set to target.ip, sname is set to network.dhcp.sname, preferred_lifetime is set to about.labels.key/value, lease_time_seconds is set to network.dhcp.lease_time_secondsif ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
604208
DHCPv6 client address (<|){dst_ip}(|>) got expired on interface {interface_name}, received from DHCPv6 server {sname}
dst_ip is set to target.ip, interface_name is set to about.labels.key/value, sname is set to network.dhcp.sname
if ([sysloghost] != "" or ![is_not_src_ip]) then,
"event.idm.read_only_udm.network.application_protocol" is set to "DHCP"
605004, 605005
Login (?P<action>denied|permitted) from {src_ip}(/{src_port})? to ({interface_name}:)?{dst_ip}(/{target_service})? for user {user_name}
action is set to security_result.action, src_ip is set to principal.ip, src_port is set to principal.port, interface_name is set to about.labels.key/value, dst_ip is set to target.ip, target_service is set to target.application, user_name is set to target.user.userid
if [dst_port] == "ssh", then "dst_port" is set to "22"
else if [dst_port] == "https", then "dst_port" is set to "443"
606001, 606002
ASDM session number {session_id} from {src_ip} (started|ended)
session_id is set to network.session_id, src_ip is set to principal.ip, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
606003
ASDM logging session number {session_id} from {dst_ip} started( <message_text> session ID assigned)?
session_id is set to network.session_id, dst_ip is set to target.ip
606004
ASDM logging session number {session_id} from {dst_ip} ended
session_id is set to network.session_id, dst_ip is set to target.ip
607001
Pre-allocate (?P<application_protocol>SIP) {connection_type} secondary channel for {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip} from <message_text> message
application_protocol is set to network.application_protocol, connection_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
607002
{action_class}: (?P<action_details>Dropped|Dropped connection for|Reset connection for|Masked header flags for) SIP {req_resp} {info} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}; {summary}
action_details is set to security_result.action_details, action_class is set to about.labels.key/value, req_resp is set to about.labels.key/value, info is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
607003
{action_class}: Received SIP {req_resp} {info} from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}; {summary}
action_class is set to about.labels.key/value, req_resp is set to about.labels.key/value, info is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
607004
Phone Proxy: (?P<action>Dropping) SIP message from {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}/{dst_port} with source MAC {src_mac} due to secure phone database mismatch
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, src_mac is set to principal.mac
608001
Pre-allocate Skinny {connection_type} secondary channel for {src_interface_name}:{src_ip}(/{src_port})? to {dst_interface_name}:{dst_ip}(/{dst_port})? from {summary}
connection_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
608002, 608003
Dropping Skinny message for {input_interface}:{src_ip}(/{src_port})? to {output_interface}:{dst_ip}/{dst_port}, SCCP Prefix length {prefix_length} too (small|large)
input_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, output_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, prefix_length is set to about.labels.key/value
608004
Dropping Skinny message for {input_interface}:{src_ip}(/{src_port})? to {output_interface}:{dst_ip}/{dst_port}, message id {message_id} not allowed
input_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, output_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, message_id is set to about.labels.key/value
608005
Dropping Skinny message for {input_interface}:{src_ip}(/{src_port})? to {output_interface}:{dst_ip}/{dst_port}, message id {message_id} registration not complete
input_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, output_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, message_id is set to about.labels.key/value
610001
NTP daemon interface {interface_name}: Packet (?P<action>denied) from {dst_ip}
action is set to security_result.action, interface_name is set to about.labels.key/value, dst_ip is set to target.ip
610002
NTP daemon interface {interface_name}: Authentication failed for packet from {dst_ip}
interface_name is set to about.labels.key/value, dst_ip is set to target.ip
610,101
Authorization failed: Cmd: {command} Cmdtype: {command_modifier}
command is set to target.process.command_line, command_modifier is set to about.labels.key/value
611101
User authentication (?P<action>succeeded): IP( address)?(,|:) {dst_ip}(,|:) Uname: {user_name}
action is set to security_result.action, dst_ip is set to target.ip, user_name is set to target.user.userid, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
611102
User authentication (?P<action>failed): IP( address)?(=|:) {dst_ip},, Uname: {user_name}
action is set to security_result.action, dst_ip is set to target.ip, user_name is set to target.user.userid, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
611103
User logged out: Uname: {user_name}
user_name is set to target.user.userid, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
611301
(?P<category>VPNClient): NAT configured for Client Mode with no split tunneling: NAT address: {mapped_address}
category is set to security_result.category_details, mapped_address is set to about.labels.key/value
611303
(?P<category>VPNClient): NAT configured for Client Mode with split tunneling: NAT address: {mapped_address} Split Tunnel Networks: {dst_ip}/{netmask}
category is set to security_result.category_details, mapped_address is set to about.labels.key/value, dst_ip is set to target.ip, netmask is set to about.labels.key/value
611304
(?P<category>VPNClient): NAT exemption configured for Network Extension Mode with split tunneling: Split Tunnel Networks: {dst_ip}/{netmask}
category is set to security_result.category_details, dst_ip is set to target.ip, netmask is set to about.labels.key/value
611305
(?P<category>VPNClient): DHCP Policy installed: Primary DNS: {dst_ip} Secondary DNS: {dst_ip1} Primary WINS: {src_ip} Secondary WINS: {src_ip1}
category is set to security_result.category_details, dst_ip is set to target.ip, dst_ip1 is set to target.ip, src_ip is set to principal.ip, src_ip1 is set to principal.ip
611307
(?P<category>VPNClient): Head end: {dst_ip}
category is set to security_result.category_details, dst_ip is set to target.ip
611309
(?P<category>VPNClient): Disconnecting from head end and uninstalling previously downloaded policy: Head End: {dst_ip}
category is set to security_result.category_details, dst_ip is set to target.ip
611310, 611311
(?P<category>VPNClient): XAUTH (?P<action>Succeeded|Failed): Peer: {src_ip}
category is set to security_result.category_details, action is set to security_result.action, src_ip is set to principal.ip, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
611312
(?P<category>VPNClient): Backup Server List: {summary}
category is set to security_result.category_details, summary is set to security_result.summary
611313
(?P<category>VPNClient): Backup Server List Error: {summary}
category is set to security_result.category_details, summary is set to security_result.summary
611314
(?P<category>VPNClient): Load Balancing Cluster with Virtual IP: {dst_ip} has redirected the to server {dst_ip1}
category is set to security_result.category_details, dst_ip is set to target.ip, dst_ip1 is set to target.ip
611315
(?P<category>VPNClient): Disconnecting from Load Balancing Cluster member {dst_ip}
category is set to security_result.category_details, dst_ip is set to target.ip
611318
VPNClient: User Authentication Enabled: Auth Server IP: {dst_ip} Auth Server Port: {dst_port} Idle Timeout: {idle_timeout}
dst_ip is set to target.ip, dst_port is set to target.port, idle_timeout is set to about.labels.key/value
612001
Auto Update succeeded:{target_file_full_path}, version:{version}
target_file_full_path is set to target.file.full_path, version is set to about.labels.key/value
612002
Auto Update failed:{target_file_full_path}, version:{version}, reason:{summary}
target_file_full_path is set to target.file.full_path, version is set to about.labels.key/value, summary is set to security_result.summary
612003
Auto Update failed to contact:{redirect_url}, reason:{summary}
redirect_url is set to target.url, summary is set to security_result.summary
613001
Checksum Failure in database in area {area} Link State Id {dst_ip} Old Checksum {old_checksum} New Checksum {new_checksum}
area is set to about.labels.key/value, dst_ip is set to target.ip, old_checksum is set to about.labels.key/value, new_checksum is set to about.labels.key/value
613002, 613102
interface {dst_interface_name} has zero bandwidth
dst_interface_name is set to target.labels.key/value
613003
{dst_ip} {netmask} changed from area {src_area} to area {dst_area}
dst_ip is set to target.ip, netmask is set to about.labels.key/value, src_area is set to principal.labels.key/value, dst_area is set to target.labels.key/value
613007
area {area} lsid {src_ip} mask {netmask} type<message_text>
area is set to about.labels.key/value, src_ip is set to principal.ip, netmask is set to about.labels.key/value
613013
OSPF LSID {src_ip} adv {dst_ip}<message_text>gateway {gateway_address}<message_text>{dst_ip1}/{netmask}<message_text>
src_ip is set to principal.ip, dst_ip is set to target.ip, gateway_address is set to about.labels.key/value, dst_ip1 is set to target.ip, netmask is set to about.labels.key/value
613014
Base topology enabled on interface {dst_interface_name} attached to MTR compatible mode area {area}
dst_interface_name is set to target.labels.key/value, area is set to about.labels.key/value
613015
Process 1 flushes LSA ID {src_ip} type-<message_text>adv-rtr {dst_ip}<message_text>
src_ip is set to principal.ip, dst_ip is set to target.ip
613016
Area {area} router-LSA of length {sent_bytes} bytes plus update overhead bytes is too large to flood
area is set to about.labels.key/value, sent_bytes is set to network.sent_bytes
613017
Bad LSA mask:<message_text>LSID {src_ip} Mask {netmask} from {dst_ip}
src_ip is set to principal.ip, netmask is set to about.labels.key/value, dst_ip is set to target.ip
613025
Invalid build flag number for LSA {src_ip},<message_text>
src_ip is set to principal.ip
613027
OSPF process {process_number} removed from interface {dst_interface_name}
process_number is set to about.labels.key/value, dst_interface_name is set to target.labels.key/value
613028
Unrecognized virtual interface {dst_interface_name}. Treat it as loopback stub route
dst_interface_name is set to target.labels.key/value
613034
Neighbor {dst_ip} not configured
dst_ip is set to target.ip
613035
Could not allocate or find neighbor {dst_ip}
dst_ip is set to target.ip
613040
OSPF-1 Area {area}: Router {dst_ip} originating invalid type number LSA, ID {src_ip}, Metric {metric1} on Link ID {dst_ip1} Link Type {link_type}
area is set to about.labels.key/value, dst_ip is set to target.ip, src_ip is set to principal.ip, metric1 is set to about.labels.key/value, dst_ip1 is set to target.ip, link_type is set to about.labels.key/value
613041
OSPF-100 Areav {area}: LSA ID {src_ip}, Type {type}, Adv-rtr {dst_ip}, LSA counter DoNotAge
area is set to about.labels.key/value, src_ip is set to principal.ip, type is set to about.labels.key/value, dst_ip is set to target.ip
613042
OSPF process {process_number} lacks forwarding address for type 7 LSA {src_ip} in NSSA <message_text>
process_number is set to about.labels.key/value, src_ip is set to principal.ip
613101
Checksum Failure in database in area {area} Link State Id {state_id} Old Checksum {old_checksum} New Checksum {new_checksum}
area is set to about.labels.key/value, state_id is set to about.labels.key/value, old_checksum is set to about.labels.key/value, new_checksum is set to about.labels.key/value
613103
<message_text> changed from area {old_area_id_str} to area {new_area_id_str}
old_area_id_str is set to about.labels.key/value, new_area_id_str is set to about.labels.key/value
613104
Unrecognized virtual interface {interface_name}
interface_name is set to about.labels.key/value
614001
Split DNS: request patched from server: {dst_ip} to server: {dst_ip1}
dst_ip is set to target.ip, dst_ip1 is set to target.ip
614002
Split DNS: reply from server:{dst_ip} reverse patched back to original server:{dst_ip1}
dst_ip is set to target.ip, dst_ip1 is set to target.ip
616001
Pre-allocate MGCP {data_channel} connection for {input_interface}:{src_ip} to {output_interface}:{dst_ip}/{dst_port} from {message_type} message
data_channel is set to about.labels.key/value, input_interface is set to about.labels.key/value, src_ip is set to principal.ip, output_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, message_type is set to about.labels.key/value
617001
GTPv version {message_type} from {src_interface_name}:{src_ip}/{src_port} not accepted by {dst_interface_name}:{dst_ip}/{dst_port}
message_type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
617002
Removing v1 PDP Context with TID {tid_value} from GGSN {ggsn_ip_address} and SGSN {sgsn_ip_address}, Reason: {summary} or Removing v1 primary PDP Context with TID tid from GGSN {ggsn_ip_address_} and SGSN {sgsn_ip_address_}, Reason: <message_text>
tid_value is set to about.labels.key/value, ggsn_ip_address is set to about.labels.key/value, sgsn_ip_address is set to about.labels.key/value, summary is set to security_result.summary, ggsn_ip_address_ is set to about.labels.key/value, sgsn_ip_address_ is set to about.labels.key/value
617003
GTP Tunnel created from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
617004
GTP connection created for response from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
617100
Teardown {num_conns} connection(s|) for user {dst_ip}
num_conns is set to about.labels.key/value, dst_ip is set to target.ip
618001
Denied STUN packet {message_type} from (<|){ingress_interface}(|>):(<|){src_ip}(|>)/(<|){src_port}(|>) to (<|){egress_interface}(|>):(<|){dst_ip}(|>)/(<|){dst_port}(|>) for connection (<|){session_id}(>|), {summary}
message_type is set to about.labels.key/value, ingress_interface is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, egress_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, session_id is set to network.session_id, summary is set to security_result.summary
620001
Pre-allocate CTIQBE (RTP|RTCP) secondary channel for {dst_interface_name}:{dst_ip}(/{dst_port})? to {src_interface_name}:{src_ip}(/{src_port})? from {summary}
dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, summary is set to security_result.summary
620002
Unsupported CTIQBE version: hex: from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
621001, 621002
Interface {interface_name} does not support multicast, not enabled
interface_name is set to about.labels.key/value
621006
Mrib disconnected, ({dst_ip},{dst_ip1}) event cancelled
dst_ip is set to target.ip, dst_ip1 is set to target.ip
621007
Bad register from {interface_name}:{src_ip} to {dst_ip} for <message_text>
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
622001
(?P<action_details>Adding|Removing) tracked route <message_text>, distance {distance1}, table {route_table_name}, on interface {interface_name}
action_details is set to security_result.action_details, distance1 is set to about.labels.key/value, route_table_name is set to about.labels.key/value, interface_name is set to about.labels.key/value
622101
Starting regex table compilation for {match_command}; table entries = {table_entries} entries
match_command is set to about.labels.key/value, table_entries is set to about.labels.key/value
622102
Completed regex table compilation for {match_command}; table size = {table_size} bytes
match_command is set to about.labels.key/value, table_size is set to about.labels.key/value
702305
(?P<category>IPSEC): An (?P<direction>inbound|outbound|INBOUND|OUTBOUND|Inbound|Outbound) {tunnel_type} SA (SPI={spi}) between {src_ip} and {dst_ip} ({src_fwuser}) is rekeying due to sequence number rollover
category is set to security_result.category_details, direction is set to network.direction, tunnel_type is set to about.labels.key/value, spi is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value
709008
(Primary|Secondary) Configuration sync in progress. Command: {command} executed from <message_text> will not be replicated to or executed by the standby unit
command is set to target.process.command_line
710003
(?P<protocol>TCP|UDP) access denied by ACL from {src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
711002
Task ran for {elapsed_time} msec(s)?, (P|p)rocess = {target_process_name}, PC = {instruction_pointer}(,)? Trace(be|)back ={traceback}
elapsed_time is set to about.labels.key/value, target_process_name is set to target.process.pid, instruction_pointer is set to about.labels.key/value, traceback is set to about.labels.key/value
711004
Task ran for {elapsed_time} msec, Process = {target_process_name}, PC = {instruction_pointer}, Call stack = {stack_call}
elapsed_time is set to about.labels.key/value, target_process_name is set to target.process.pid, instruction_pointer is set to about.labels.key/value, stack_call is set to about.labels.key/value
713004
device scheduled for reboot or shutdown, IKE key acquire message on interface {interface_number}, for Peer {dst_ip} ignored
interface_number is set to about.labels.key/value, dst_ip is set to target.ip
713201
Duplicate Phase {phase} packet detected. {action_details}
phase is set to about.labels.key/value, action_details is set to security_result.action_details
713202
Duplicate {dst_ip} packet detected
dst_ip is set to target.ip
713006
Failed to obtain state for message Id {message_id}, Peer Address: {dst_ip}
message_id is set to about.labels.key/value, dst_ip is set to target.ip
713010
IKE area: failed to find centry for message Id {message_id}
message_id is set to about.labels.key/value
713012
Unknown protocol ({protocol}). Not adding SA w/spi=SPI {spi}
protocol is set to network.ip_protocol, spi is set to about.labels.key/value
713014
Unknown Domain of Interpretation (DOI): {domain_of_interpretation}
domain_of_interpretation is set to about.labels.key/value
713016
(Group = {g_ip}, IP = {src_ip}, )?Unknown identification type, Phase (1 or )?2, Type {id_type}
id_type is set to about.labels.key/value, g_ip is mapped to principal.nat_ip, src_ip is mapped to principal.ip
713017
Identification type not supported, Phase 1 or 2, Type {id_type}
id_type is set to about.labels.key/value
713018
Unknown ID type during find of group name for certs, Type {id_type}
id_type is set to about.labels.key/value
713022
No Group found matching {peer_id} or {dst_ip} for Pre-shared key peer {dst_ip1}
peer_id is set to about.labels.key/value, dst_ip is set to target.ip, dst_ip1 is set to target.ip
713032, 713033
Received invalid (remote|local) Proxy Range {dst_ip}-{dst_ip1}
dst_ip is set to target.ip, dst_ip1 is set to target.ip
713041
IKE Initiator:<message_text>Intf {dst_interface_name}, IKE Peer {dst_ip}local Proxy Address {local_proxy_addr}, remote Proxy Address {remote_proxy_addr},Crypto map ({crypto_map_tag})
dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, local_proxy_addr is set to principal.ip, remote_proxy_addr is set to target.ip, crypto_map_
713042
IKE Initiator unable to find policy: Intf {dst_interface_name}, Src: {src_ip}, Dst: {dst_ip}
dst_interface_name is set to target.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
713043
<message_text>address {dst_ip} session already in progress
dst_ip is set to target.ip
713048
Error processing payload: Payload ID: {payload_id}
payload_id is set to about.labels.key/value
713049
(Group = {group_name}, IP = {dst_ip}, )?Security negotiation complete for {tunnel_type} (Group )?({group_name})s+(Initiator|Responder), Inbound SPI= {initiator_spi}, Outbound SPI= {responder_spi}
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, tunnel_type is set to about.labels.key/value, group_name is set to target.user.group_identifiers, initiator_spi is set to about.labels.key/value, responder_spi is set to about.labels.key/value
713050
Connection terminated for peer {dst_ip}. Reason: termination reason Remote Proxy {remote_proxy_addr}, Local Proxy {local_proxy_addr}
dst_ip is set to target.ip, remote_proxy_addr is set to target.ip, local_proxy_addr is set to principal.ip
713056
Tunnel rejected: SA ({sa_name}) not found for group ({group_name})!
sa_name is set to about.labels.key/value, group_name is set to target.user.group_identifiers
713060
Tunnel Rejected: User ({user_name}) not member of group ({group_name}), group-lock check failed
user_name is set to target.user.userid, group_name is set to target.user.group_identifiers
713061
Tunnel rejected: Crypto Map Policy not found for Src:{src_ip}, Dst: {dst_ip}!
src_ip is set to principal.ip, dst_ip is set to target.ip
713062
IKE Peer address same as our interface address {dst_ip}
dst_ip is set to target.ip
713063
IKE Peer address not configured for destination {dst_ip}
dst_ip is set to target.ip
713065
IKE Remote Peer did not negotiate the following: {proposal_attribute}
proposal_attribute is set to about.labels.key/value
713068
Received non-routine Notify message: {notify_type}({notify_value})
notify_type is set to about.labels.key/value, notify_value is set to about.labels.key/value
713072
Password for user ({user_name}) too long, truncating to {truncated_length} characters
user_name is set to target.user.userid, truncated_length is set to about.labels.key/value
713073
(Group = {group_name}, IP = {dst_ip}, )?Responder forcing change of <message_text> rekeying duration from {end_time} to {start_time} seconds
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, end_time is set to about.labels.key/value, start_time is set to about.labels.key/value
713074
(Group = {group_name}, IP = {dst_ip}, )?Responder forcing change of (IPsec|IPSec) rekeying duration from {end_time} to {start_time} Kbs
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, end_time is set to about.labels.key/value, start_time is set to about.labels.key/value
713075, 713076
(Group = {group_name}, IP = {dst_ip}, )?Overriding Initiator()?'s (IPsec|IPSec) rekeying duration from {end_time} to {start_time} (seconds|Kbs)
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, end_time is set to about.labels.key/value, start_time is set to about.labels.key/value
713078
Temp buffer for building mode config attributes exceeded: bufsize {available_size}, used {used_value}
available_size is set to about.labels.key/value, used_value is set to about.labels.key/value
713081
Unsupported certificate encoding type {encoding_type}
encoding_type is set to about.labels.key/value
713084
Received invalid phase 1 port value ({dst_port}) in ID payload
dst_port is set to target.port
713085
Received invalid phase 1 protocol ({protocol}) in ID payload
protocol is set to network.ip_protocol
713088
Set Cert filehandle failure: no (IPsec|IPSec) SA in group {group_name}
group_name is set to target.user.group_identifiers
713098
Aborting: No identity cert specified in (IPsec|IPSec) SA ({sa_name})!
sa_name is set to about.labels.key/value
713102
Phase 1 ID Data length {packet_length} too long - reject tunnel!
packet_length is set to about.labels.key/value
713107
{dst_ip} request attempt failed!
dst_ip is set to target.ip
713112
Failed to process CONNECTED notify (SPI {spi_value})!
spi_value is set to about.labels.key/value
713118
Detected invalid Diffie-Helmann {group_name}, in IKE area
group_name is set to target.user.group_identifiers
713119
Group {group_name} IP {dst_ip} PHASE 1 COMPLETED
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip
713119
Group = {group_name}, IP = {dst_ip}, PHASE 1 COMPLETED
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip
713120
PHASE 2 COMPLETED (msgid={message_id})
message_id is set to about.labels.key/value
713122
(IP = {dst_ip}, )?Keep-alives configured {keepalive_type} but peer( {dst_ip})?( does not)? support keep-alives<message_text>
dst_ip is set to target.ip, keepalive_type is set to about.labels.key/value, dst_ip is set to target.ip
713123
IKE lost contact with remote peer, deleting connection (keepalive type: {keepalive_type})
keepalive_type is set to about.labels.key/value
713124
Received DPD sequence number {rcv_sequence} in {summary}
rcv_sequence is set to about.labels.key/value, summary is set to security_result.summary
713128
Connection attempt to VCPIP redirected to VCA peer {dst_ip} via load balancing
dst_ip is set to target.ip
713129
Received unexpected Transaction Exchange payload type: {payload_id}
payload_id is set to about.labels.key/value
713130
Received unsupported transaction mode attribute: {attribute_id}
attribute_id is set to about.labels.key/value
713131
Received unknown transaction mode attribute: {attribute_id}
attribute_id is set to about.labels.key/value
713132
Cannot obtain an {dst_ip} for remote peer
dst_ip is set to target.ip
713133
Mismatch: Overriding phase 2 DH Group(DH group {group_name}) with phase 1 group(DH group {group_number}())?
group_name is set to target.user.group_identifiers, group_number is set to about.labels.key/value
713135
message received, redirecting tunnel to {dst_ip}
dst_ip is set to target.ip
713136
IKE session establishment timed out( {ike_state_name})?, aborting!
ike_state_name is set to about.labels.key/value
713137
Reaper overriding refCnt( {ref_count})? and tunnelCnt( {tunnel_count})? -- deleting SA!
ref_count is set to about.labels.key/value, tunnel_count is set to about.labels.key/value
713138
Group {group_name} not found and BASE GROUP default preshared key not configured
group_name is set to target.user.group_identifiers
713139
{group_name} not found, using BASE GROUP default preshared key
group_name is set to target.user.group_identifiers
713141
Client-reported firewall does not match configured firewall: {action} tunnel. Received -- Vendor: {vendor_id}, Product {product_id}, Caps: {capability_value}. Expected -- Vendor: {expected_vendor_id}, Product: {expected_product_id}, Caps: {expected_capability_value}
action is set to security_result.action, vendor_id is set to about.labels.key/value, product_id is set to about.labels.key/value, capability_value is set to about.labels.key/value, expected_vendor_id is set to about.labels.key/value, expected_product_id is set to about.labels.key/value, expected_capability_value is set to about.labels.key/value
713142
Client did not report firewall in use, but there is a configured firewall: {action} tunnel. Expected -- Vendor: {expected_vendor_id}, Product {expected_product_id}, Caps: {expected_capability_value}
action is set to security_result.action, expected_vendor_id is set to about.labels.key/value, expected_product_id is set to about.labels.key/value, expected_capability_value is set to about.labels.key/value
713144
Ignoring received malformed firewall record; reason -{summary}
summary is set to security_result.summary
713269
Detected Hardware Client in network extension mode, adding static route for address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713145
Detected Hardware Client in network extension mode, adding static route for address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713270
Could not add route for Hardware Client in network extension mode, address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713271
Terminating tunnel to Hardware Client in network extension mode, deleting static route for address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713272
Terminating tunnel to Hardware Client in network extension mode, unable to delete static route for address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713146
Could not add route for Hardware Client in network extension mode, address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713147
Terminating tunnel to Hardware Client in network extension mode, deleting static route for address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713148
Terminating tunnel to Hardware Client in network extension mode, unable to delete static route for address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713149
Hardware client security attribute {attribute_name} was enabled but not requested
attribute_name is set to about.labels.key/value
713152
Unable to obtain any rules from filter {acl_id} to send to client for CPP, (?P<action>terminating) connection
action is set to security_result.action, acl_id is set to about.labels.key/value
713154
DNS lookup for {peer_description} Server {server_name} failed!
peer_description is set to about.labels.key/value, server_name is set to about.labels.key/value
713155
DNS lookup for Primary VPN Server {server_name} successfully resolved after a previous failure. Resetting any Backup Server init
server_name is set to about.labels.key/value
713156
Initializing Backup Server {dst_ip}
dst_ip is set to target.ip
713157
Timed out on initial contact to server {dst_ip} Tunnel could not be established
dst_ip is set to target.ip
713161
Remote user (session Id -{session_id}) network access has been (?P<action>restricted) by the Firewall Server
action is set to security_result.action, session_id is set to network.session_id
713162, 713163
Remote user (session Id -{session_id}) has been (?P<action>rejected|terminated) by the Firewall Server
action is set to security_result.action, session_id is set to network.session_id
713176
{device_type} memory resources are critical, IKE key acquire message on interface {interface_number}, for Peer {dst_ip} ignored
device_type is set to about.labels.key/value, interface_number is set to about.labels.key/value, dst_ip is set to target.ip
713177
Received remote Proxy Host FQDN in ID Payload: Host Name: {target_hostname} Address {dst_ip}, Protocol {protocol}, Port {dst_port}
target_hostname is set to target.hostname, dst_ip is set to target.ip, protocol is set to network.ip_protocol, dst_port is set to target.port
713179
IKE AM Initiator received a packet from its peer without a {payload_type} payload
payload_type is set to about.labels.key/value
713184
Client Type: {client_type} Client Application Version: {version}
client_type is set to about.labels.key/value, version is set to about.labels.key/value
713186
Invalid secondary domain name list received from the authentication server. List Received: {list_text} Character {index} ({value}) is illegal
list_text is set to about.labels.key/value, index is set to about.labels.key/value, value is set to about.labels.key/value
713189
Attempted to assign network or broadcast {src_ip}, removing ({dst_ip}) from pool
src_ip is set to principal.ip, dst_ip is set to target.ip
713193
Received packet with missing payload, Expected payload: {payload_id}
payload_id is set to about.labels.key/value
713194
Sending (IKE|IPsec) Delete With Reason message: {summary}
summary is set to security_result.summary
713196
Remote L2L Peer {dst_ip} initiated a tunnel with same outer and inner addresses. Peer could be Originate Only - Possible misconfiguration!
dst_ip is set to target.ip
713197
The configured Confidence Interval of {interval} seconds is invalid for this {tunnel_type} connection. Enforcing the second default
interval is set to about.labels.key/value, tunnel_type is set to about.labels.key/value
713198
User Authorization failed: {user_name} User authorization failed. Username could not be found in the certificate
user_name is set to target.user.userid
713199
Reaper corrected an SA that has not decremented the concurrent IKE negotiations counter ({counter_value})!
counter_value is set to about.labels.key/value
713205
Could not add static route for client address: {dst_ip}
dst_ip is set to target.ip
713208
Cannot create dynamic rule for Backup L2L entry rule {rule_id}
rule_id is set to about.labels.key/value
713265
Adding static route for L2L peer coming in on a dynamic map. address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713266
Could not add route for L2L peer coming in on a dynamic map. address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713267
Deleting static route for L2L peer that came in on a dynamic map. address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713268
Could not delete route for L2L peer that came in on a dynamic map. address: {dst_ip}, mask:/{prefix_length}
dst_ip is set to target.ip, prefix_length is set to about.labels.key/value
713211
Adding static route for L2L peer coming in on a dynamic map. address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713212
Could not add route for L2L peer coming in on a dynamic map. address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713213
Deleting static route for L2L peer that came in on a dynamic map. address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713214
Could not delete route for L2L peer that came in on a dynamic map. address: {dst_ip}, mask: {netmask}
dst_ip is set to target.ip, netmask is set to about.labels.key/value
713215
No match against Client Type and Version rules. Client: {client_type} is( not)? allowed by default
client_type is set to about.labels.key/value
713216
Rule: {action} Client type]: {version} Client: {client_type} not allowed
action is set to security_result.action, version is set to about.labels.key/value, client_type is set to about.labels.key/value
713216
Rule: {action} Client type]: {version} Client: {client_type} allowed
action is set to security_result.action, version is set to about.labels.key/value, client_type is set to about.labels.key/value
713217
Skipping unrecognized rule: action: {action} client type: {client_type} client version: {version}
action is set to security_result.action, client_type is set to about.labels.key/value, version is set to about.labels.key/value
713226
Connection failed with peer {dst_ip}, no trust-point defined in tunnel-group {tunnel_group}
dst_ip is set to target.ip, tunnel_group is set to target.group.group_display_name
713227
Rejecting new (IPsec|IPSec) SA negotiation for peer {dst_ip}. A negotiation was already in progress for local Proxy {local_proxy_addr}/{local_netmask}, remote Proxy {remote_proxy_addr}/{remote_netmask}
dst_ip is set to target.ip, local_proxy_addr is set to principal.ip, local_netmask is set to about.labels.key/value, remote_proxy_addr is set to target.ip, remote_netmask is set to about.labels.key/value
713228
Group = {group_name}, Username = {user_name}, IP = {dst_ip}(,)? Assigned private IP address {dst_ip1} to remote user
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, dst_ip1 is set to target.ip
713229
Auto Update - Notification to client {dst_ip} of update string: {summary}
dst_ip is set to target.ip, summary is set to security_result.summary
713230
Internal Error, ike_lock trying to lock bit that is already locked for type {semaphore}
semaphore is set to about.labels.key/value
713231
Internal Error, ike_lock trying to unlock bit that is not locked for type {semaphore}
semaphore is set to about.labels.key/value
713232
SA lock refCnt = {sa_lock_value}, bitmask = {bitmask_hex}, p1_decrypt_cb = {p1_decrypt_cb}, qm_decrypt_cb = {qm_decrypt_cb}, qm_hash_cb = {qm_hash_cb}, qm_spi_ok_cb = {qm_spi_ok_cb}, qm_dh_cb = {qm_dh_cb}, qm_secret_key_cb = {qm_secret_key_cb}, qm_encrypt_cb = {qm_encrypt_cb}
sa_lock_value is set to about.labels.key/value, bitmask_hex is set to about.labels.key/value, p1_decrypt_cb is set to about.labels.key/value, qm_decrypt_cb is set to about.labels.key/value, qm_hash_cb is set to about.labels.key/value, qm_spi_ok_cb is set to about.labels.key/value, qm_dh_cb is set to about.labels.key/value, qm_secret_key_cb is set to about.labels.key/value, qm_encrypt_cb is set to about.labels.key/value
713237
ACL update ({access_list}) received during re-key re-authentication will not be applied to the tunnel
access_list is set to about.labels.key/value
713239
{dst_ip}: Tunnel Rejected: The maximum tunnel count allowed has been reached
dst_ip is set to target.ip
713240
Received DH key with bad length: received length={message_length} expected length={expected_msg_length}
message_length is set to about.labels.key/value, expected_msg_length is set to about.labels.key/value
713241
IE Browser Proxy Method {setting_number} is Invalid
setting_number is set to about.labels.key/value
713243
{summary} Unable to find the requested certificate
summary is set to security_result.summary
713244
{summary} Received Legacy Authentication Method(LAM) type {lam_type} is different from the last type received {last_lam_type}
summary is set to security_result.summary, lam_type is set to about.labels.key/value, last_lam_type is set to about.labels.key/value
713245
{summary} Unknown Legacy Authentication Method(LAM) type {lam_type} received
summary is set to security_result.summary, lam_type is set to about.labels.key/value
713246
{summary} Unknown Legacy Authentication Method(LAM) attribute type {lam_type} received
summary is set to security_result.summary, lam_type is set to about.labels.key/value
713247
{summary} Unexpected error: in Next Card Code mode while not doing SDI
summary is set to security_result.summary
713248
{summary} Rekey initiation is being disabled during CRACK authentication
summary is set to security_result.summary
713249
<message_text> Received unsupported authentication results: {summary}
summary is set to security_result.summary
713250
{summary} Received unknown Internal Address attribute: {attribute}
summary is set to security_result.summary, attribute is set to about.labels.key/value
713251
{summary} Received authentication failure message
summary is set to security_result.summary
713252
Group = {group_name}, Username = {user_name}, IP = {dst_ip}, Integrity Firewall Server is not available. VPN Tunnel creation rejected for client
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
713253
Group = {group_name}, Username = {user_name}, IP = {dst_ip}, Integrity Firewall Server is not available. Entering ALLOW mode. VPN Tunnel created for client
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
713254
Group = {group_name}, Username = {user_name}, IP = {dst_ip}, Invalid {protocol} port = {dst_port}, valid range is {port_range} , except port 4500, which is reserved for <message_text>
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, protocol is set to network.ip_protocol, dst_port is set to target.port, port_range is set to about.labels.key/value
713255
IP = {dst_ip}, Received ISAKMP Aggressive Mode message 1 with unknown tunnel group name {group_name}
dst_ip is set to target.ip, group_name is set to target.user.group_identifiers
713256
IP = {dst_ip}, Sending spoofed ISAKMP Aggressive Mode message 2 due to receipt of unknown tunnel group. Aborting connection
dst_ip is set to target.ip
713257
Phase {mismatch_phase} failure:Mismatched attribute types for class {attribute_class}:Rcv'd: {attribute_received} Cfg'd: {attribute_configured}
mismatch_phase is set to about.labels.key/value, attribute_class is set to about.labels.key/value, attribute_received is set to about.labels.key/value, attribute_configured is set to about.labels.key/value
713258
IP = {dst_ip}, Attempting to establish a phase2 tunnel on {src_interface_name} interface but phase1 tunnel is on {dst_interface_name} interface. Tearing down old phase1 tunnel due to a potential routing change
dst_ip is set to target.ip, src_interface_name is set to principal.labels.key/value, dst_interface_name is set to target.labels.key/value
713259
Group = {group_name}, Username = {user_name}, IP = {dst_ip}, Session is being torn down. Reason: {summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, summary is set to security_result.summary
713260
Output interface {dst_interface_name} to peer was not found
dst_interface_name is set to target.labels.key/value
713261
IPV6 address on output interface {dst_interface_name} was not found
dst_interface_name is set to target.labels.key/value
713262
Rejecting new IPSec SA negotiation for peer {dst_ip}. A negotiation was already in progress for local Proxy {local_proxy_addr}/{local_prefix_length}, remote Proxy {remote_proxy_addr}/{remote_prefix_length}
dst_ip is set to target.ip, local_proxy_addr is set to principal.ip, local_prefix_length is set to about.labels.key/value, remote_proxy_addr is set to target.ip, remote_prefix_length is set to about.labels.key/value
713274
(Deleting|Could not delete) static route for client address: {dst_ip} {dst_ip1} address of client whose route is being removed
dst_ip is set to target.ip, dst_ip1 is set to target.ip
713275
IKEv1 Unsupported certificate keytype {keytype} found at trustpoint {trustpoint}
keytype is set to about.labels.key/value, trustpoint is set to about.labels.key/value
713276
Dropping new negotiation - IKEv1 in-negotiation context limit of {limit} reached
limit is set to about.labels.key/value
716001
Group {group_name} User {user_name} IP {dst_ip} WebVPN session started
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716002
Group {group_policy} User {user_name} IP {src_ip} WebVPN session terminated: User requested
group_policy is set to about.labels.key/value, user_name is set to target.user.userid, src_ip is set to principal.ip, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
716003
Group {group_name} User {user_name} IP ip WebVPN access "(?P<action>GRANTED): {redirect_url}"
action is set to security_result.action, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, redirect_url is set to target.url
716004
Group {group_name} User {user_name} WebVPN access (?P<action>DENIED) to specified location: {redirect_url}
action is set to security_result.action, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, redirect_url is set to target.url
716005
Group {group_name} User {user_name} WebVPN ACL Parse Error: {summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, summary is set to security_result.summary
716006
Group {group_name} User {user_name} WebVPN session terminated. Idle timeout
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid
716007
Group {group_name} User {user_name} WebVPN Unable to create session
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid
716009
Group {group_name} User {user_name} WebVPN session not allowed. WebVPN ACL parse error
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid
716022
Unable to connect to proxy server {summary}
summary is set to security_result.summary
716023
Group {group_name} User {user_name} Session could not be established: session limit of {maximum_sessions} reached
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, maximum_sessions is set to about.labels.key/value
716038
Group {group_name} User {user_name} IP {dst_ip} Authentication: successful, Session Type: WebVPN
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to principal.ip
716039
Authentication: rejected, group = {group_name} user = {user_name}, Session Type: {session_type}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, session_type is set to about.labels.key/value, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
716039
Group <{group_name}> User {user_name} IP <{src_ip}> Authentication: rejected, Session Type: {session_type}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, src_ip is set to principal.ip, session_type is set to about.labels.key/value
716040
Reboot pending, new sessions disabled. (?P<action>Denied) {user_name} login
action is set to security_result.action, user_name is set to target.user.userid
716041
access-list {acl_id} action url {redirect_url} hit_cnt {hit_count}
acl_id is set to about.labels.key/value, redirect_url is set to target.url, hit_count is set to about.labels.key/value
716042
access-list {acl_id} action (?P<protocol>tcp) {src_interface_name}/{src_ip} ({src_port}) - {dst_interface_name}/{dst_ip} ({dst_port}) hit-cnt {hit_count}
protocol is set to network.ip_protocol, acl_id is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, hit_count is set to about.labels.key/value
716043
Group {group_name}, User {user_name}, IP {dst_ip}: WebVPN Port Forwarding Java applet started. Created new hosts file mappings
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716044
Group {group_name} User {user_name} IP {dst_ip} AAA parameter {parameter_name} value {parameter_value} out of range
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, parameter_name is set to about.labels.key/value, parameter_value is set to about.labels.key/value
716045
Group {group_name} User {user_name} IP {dst_ip} AAA parameter {parameter_name} value invalid
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, parameter_name is set to about.labels.key/value
716046
Group {group_name} User {user_name} IP {dst_ip} User ACL {access_list_entry} from AAA doesn't exist on the device, terminating connection
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, access_list_entry is set to about.labels.key/value
716047
Group {group_name} User {user_name} IP {dst_ip} User ACL {access_list_entry} from AAA ignored, AV-PAIR ACL used instead
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, access_list_entry is set to about.labels.key/value
716048
Group {group_name} User {user_name} IP {dst_ip} No memory to parse ACL
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716049
Group {group_name} User {user_name} IP {dst_ip} Empty SVC ACL
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716050
Error adding to ACL: {ace_command_line}
ace_command_line is set to about.labels.key/value
716051
Group {group_name} User {user_name} IP {dst_ip} Error adding dynamic ACL for user
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716052
Group {group_name} User {user_name} IP {dst_ip} Pending session terminated
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716053, 716054
SSO Server (added|deleted): name: {server_name} Type: {server_type}
server_name is set to about.labels.key/value, server_type is set to about.labels.key/value
716055
Group {group_name} User {user_name} IP {dst_ip} Authentication to SSO server name: {server_name} type {server_type} succeeded
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, server_name is set to about.labels.key/value, server_type is set to about.labels.key/value
716056
Group {group_name} User {user_name} IP {dst_ip} Authentication to SSO server name: {server_name} type {server_type} failed reason: {summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, server_name is set to about.labels.key/value, server_type is set to about.labels.key/value, summary is set to security_result.summary
716057
Group {group_name} User {user_name} IP {dst_ip} Session terminated, no {license_type} license available
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, license_type is set to about.labels.key/value
716058
Group {group_name} User {user_name} IP {dst_ip} AnyConnect session lost connection. Waiting to resume
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716059
Group {group_name} User {user_name} IP {dst_ip} AnyConnect session resumed. Connection from {src_ip}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, src_ip is set to principal.ip
716060
Group {group_name} User {user_name} IP {dst_ip} Terminated AnyConnect session in inactive state to accept a new connection. License limit reached
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716061
Group {group_name} User {user_name} IP {dst_ip} IPv6 User Filter {dst_ip1} configured for AnyConnect. This setting has been deprecated, terminating connection
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, dst_ip1 is set to target.ip
716500, 716501
internal error in: {function}: Fiber library cannot (attach|locate) AK47 instance
function is set to about.labels.key/value
716502
internal error in: {function}: Fiber library cannot allocate default arena
function is set to about.labels.key/value
716503, 716504
internal error in: {function}: Fiber library cannot allocate fiber (stacks|descriptors) pool
function is set to about.labels.key/value
716505
internal error in: {function}: Fiber has joined fiber in unfinished state
function is set to about.labels.key/value
716508, 716509, 716510
internal error in: {function}: Fiber scheduler is scheduling (finished|alien|rotten) fiber. Cannot (continue|continuing) terminating
function is set to about.labels.key/value
716512
internal error in: {function}: Fiber has joined fiber waited upon by someone else
function is set to about.labels.key/value
716513
internal error in: {function}: Fiber in callback blocked on other channel
function is set to about.labels.key/value
716515
internal error in: {function}: OCCAM failed to allocate memory for AK47 instance
function is set to about.labels.key/value
716516
internal error in: {function}: OCCAM has corrupted ROL array. Cannot continue terminating
function is set to about.labels.key/value
716517
internal error in: {function}: OCCAM cached block has no associated arena
function is set to about.labels.key/value
716518
internal error in: {function}: OCCAM pool has no associated arena
function is set to about.labels.key/value
716519
internal error in: {function}: OCCAM has corrupted pool list. Cannot continue terminating
function is set to about.labels.key/value
716520
internal error in: {function}: OCCAM pool has no block list
function is set to about.labels.key/value
716521
internal error in: {function}: OCCAM no realloc allowed in named pool
function is set to about.labels.key/value
716522
internal error in: {function}: OCCAM corrupted standalone block
function is set to about.labels.key/value
716600
Rejected {received_kb}KB Hostscan data from IP (<)?{src_ip}(>)?. Hostscan results exceed (default|configured) limit of {configured_kb}KB
received_kb is set to about.labels.key/value, src_ip is set to principal.ip, configured_kb is set to about.labels.key/value
716601
Rejected {received_kb} KB Hostscan data from IP {src_ip}. System-wide limit on the amount of Hostscan data stored on FTD exceeds the limit of {configured_kb} KB
received_kb is set to about.labels.key/value, src_ip is set to principal.ip, configured_kb is set to about.labels.key/value
716602
Memory allocation error. Rejected {received_kb} KB Hostscan data from IP {src_ip}
received_kb is set to about.labels.key/value, src_ip is set to principal.ip
717002
Certificate enrollment failed for trustpoint {trustpoint_name}. Reason:{summary}
trustpoint_name is set to about.labels.key/value, summary is set to security_result.summary
717003
Certificate received from Certificate Authority for trustpoint {trustpoint_name}
trustpoint_name is set to about.labels.key/value
717004, 717006
PKCS #12 (import|export) failed for trustpoint {trustpoint_name}
trustpoint_name is set to about.labels.key/value
717005, 717007
PKCS #12 (import|export) succeeded for trustpoint {trustpoint_name}
trustpoint_name is set to about.labels.key/value
717008
Insufficient memory to {target_process_name}
target_process_name is set to target.process.pid
717009
Certificate validation failed. Reason:{summary}
summary is set to security_result.summary
717010
CRL polling failed for trustpoint {trustpoint_name}
trustpoint_name is set to about.labels.key/value
717012
Failed to refresh CRL cache entry from the server for trustpoint {trustpoint_name} at {time_of_failure}
trustpoint_name is set to about.labels.key/value, time_of_failure is set to about.labels.key/value
717013
Removing a cached CRL to accommodate an incoming CRL. Issuer: {issuer}
issuer is set to about.labels.key/value
717014
Unable to cache a CRL received from <message_text> due to size limitations (CRL size = {crl_size}, available cache space = {cache_space})
crl_size is set to about.labels.key/value, cache_space is set to about.labels.key/value
717015
CRL received from {issuer} is too large to process (CRL size = {crl_size}, maximum CRL size = {max_crl_size})
issuer is set to about.labels.key/value, crl_size is set to about.labels.key/value, max_crl_size is set to about.labels.key/value
717016
Removing expired CRL from the CRL cache. Issuer: {issuer}
issuer is set to about.labels.key/value
717017
Failed to query CA certificate for trustpoint {trustpoint_name} from {enrollment_url}
trustpoint_name is set to about.labels.key/value, enrollment_url is set to about.labels.key/value
717018
CRL received from {issuer} has too many entries to process (number of entries = {number_of_entries}, maximum number allowed = {max_allowed})
issuer is set to about.labels.key/value, number_of_entries is set to about.labels.key/value, max_allowed is set to about.labels.key/value
717019
Failed to insert CRL for trustpoint {trustpoint_name}. Reason: {summary}
trustpoint_name is set to about.labels.key/value, summary is set to security_result.summary
717020
Failed to install device certificate for trustpoint {label}. Reason: {summary}
label is set to about.labels.key/value, summary is set to security_result.summary
717021
Certificate data could not be verified. Locate Reason:{summary} serial number: {serial_number}, subject name: {subject_name}, key length {length} bits
summary is set to security_result.summary, serial_number is set to about.labels.key/value, subject_name is set to about.labels.key/value, length is set to about.labels.key/value
717022
Certificate was successfully validated. {certificate_identifiers}
certificate_identifiers is set to about.labels.key/value
717023
SSL failed to set device certificate for trustpoint {trustpoint_name}. Reason: {summary}
trustpoint_name is set to about.labels.key/value, summary is set to security_result.summary
717024
Checking CRL from trustpoint: {trustpoint_name} for {summary}
trustpoint_name is set to about.labels.key/value, summary is set to security_result.summary
717025
Validating certificate chain containing {number_of_certs} certificate
number_of_certs is set to about.labels.key/value
717026
Name lookup failed for hostname {target_hostname} during PKI operation
target_hostname is set to target.hostname
717027
Certificate chain failed validation. {summary}
summary is set to security_result.summary
717028
Certificate chain was successfully validated {info}
info is set to about.labels.key/value
717029
Identified client certificate within certificate chain. serial number: {serial_number}, subject name: {subject_name}
serial_number is set to about.labels.key/value, subject_name is set to about.labels.key/value
717030
Found a suitable trustpoint {trustpoint_name} to validate certificate
trustpoint_name is set to about.labels.key/value
717031
Failed to find a suitable trustpoint for the issuer: {issuer} Reason: {summary}
issuer is set to about.labels.key/value, summary is set to security_result.summary
717035
OCSP status is being checked for certificate. {certificate_identifiers}
certificate_identifiers is set to about.labels.key/value
717036
Looking for a tunnel group match based on certificate maps for peer certificate with {certificate_identifiers}
certificate_identifiers is set to about.labels.key/value
717037
Tunnel group search using certificate maps failed for peer certificate: {certificate_identifiers}
certificate_identifiers is set to about.labels.key/value
717038
Tunnel group match found. Tunnel Group: {tunnel_group},Peer certificate: {certificate_identifiers}
tunnel_group is set to target.group.group_display_name, certificate_identifiers is set to about.labels.key/value
717039
Local CA Server internal error detected: {error_message}
error_message is set to security_result.description
717040
Local CA Server has failed and is being disabled. Reason: {summary}
summary is set to security_result.summary
717041
Local CA Server event: {info}
info is set to about.labels.key/value
717042
Failed to enable Local CA Server.Reason: {summary}
summary is set to security_result.summary
717043
Local CA Server certificate enrollment related info for user: {user_name}. Info: {info}
user_name is set to target.user.userid, info is set to about.labels.key/value
717044
Local CA server certificate enrollment related error for user: {user_name}. Error: {error_message}
user_name is set to target.user.userid, error_message is set to security_result.description
717045
Local CA Server CRL info: {info}
info is set to about.labels.key/value
717046
Local CA Server CRL error: {error_message}
error_message is set to security_result.description
717047
(Revoked|Unrevoked) certificate issued to user: {user_name}, with serial number {serial_number}
user_name is set to target.user.userid, serial_number is set to about.labels.key/value
717049
Local CA Server certificate is due to expire in {days_left} days and a replacement certificate is available for export
days_left is set to about.labels.key/value
717050
SCEP Proxy: Processed request type {request_type} from IP {src_ip}, User {user_name}, TunnelGroup {tunnel_group}, GroupPolicy {group_name} to CA IP {dst_ip}
request_type is set to about.labels.key/value, src_ip is set to principal.ip, user_name is set to target.user.userid, tunnel_group is set to target.group.group_display_name, group_name is set to target.user.group_identifiers, dst_ip is set to target.ip
717051
SCEP Proxy: Denied processing the request type {request_type} received from IP {src_ip}, User {user_name}, TunnelGroup {tunnel_group}, GroupPolicy {group_name} to CA {dst_ip}. Reason: {summary}
request_type is set to about.labels.key/value, src_ip is set to principal.ip, user_name is set to target.user.userid, tunnel_group is set to target.group.group_display_name, group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, summary is set to security_result.summary
717052
Group {group_name} User {user_name} IP {dst_ip} Session disconnected due to periodic certificate authentication failure. Subject Name {subject_name} Issuer Name {issuer} Serial Number {serial_number}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, serial_number is set to about.labels.key/value
717053
Group {group_name} User {user_name} IP {dst_ip} Periodic certificate authentication succeeded. Subject Name {subject_name} Issuer Name {issuer} Serial Number {serial_number}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, serial_number is set to about.labels.key/value
717054
The {type} certificate in the trustpoint {trustpoint_name} is due to expire in {days_left} days. Expiration {expiration} Subject Name {subject_name} Issuer Name {issuer} Serial Number {serial_number}
type is set to about.labels.key/value, trustpoint_name is set to about.labels.key/value, days_left is set to about.labels.key/value, expiration is set to about.labels.key/value, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, serial_number is set to about.labels.key/value
717055
The {type} certificate in the trustpoint {trustpoint_name} has expired. Expiration {expiration} Subject Name {subject_name} Issuer Name {issuer}( Serial Number {serial_number})?
type is set to about.labels.key/value, trustpoint_name is set to about.labels.key/value, expiration is set to about.labels.key/value, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, serial_number is set to about.labels.key/value
717056
Attempting {type} revocation check from {src_interface_name}:{src_ip}/{src_port} to {dst_ip}/{dst_port} using {protocol}
type is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, protocol is set to network.ip_protocol
717059
Peer certificate with serial number: (<|){serial_number}(>|), subject: (<|){subject_name}(>|), issuer: (<|){issuer}(>|) matched the configured certificate map {map_name}
serial_number is set to about.labels.key/value, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, map_name is set to about.labels.key/value
717060
Peer certificate with serial number: (<|){serial_number}(>|), subject: (<|){subject_name}(>|), issuer: (<|){issuer}(>|) failed to match the configured certificate map {map_name}
serial_number is set to about.labels.key/value, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, map_name is set to about.labels.key/value
717061
Starting {protocol} certificate enrollment for the trustpoint {trustpoint_name} with the CA {dst_ip}. Request Type {request_type} Mode {mode}
protocol is set to network.ip_protocol, trustpoint_name is set to about.labels.key/value, dst_ip is set to target.ip, request_type is set to about.labels.key/value, mode is set to about.labels.key/value
717062
{protocol} Certificate enrollment succeeded for the trustpoint {trustpoint_name} with the CA {dst_ip}. Received a new certificate with Subject Name {subject_name} Issuer Name {issuer} Serial Number {serial_number}
protocol is set to network.ip_protocol, trustpoint_name is set to about.labels.key/value, dst_ip is set to target.ip, subject_name is set to about.labels.key/value, issuer is set to about.labels.key/value, serial_number is set to about.labels.key/value
717063
{protocol} Certificate enrollment failed for the trustpoint {trustpoint_name} with the CA {dst_ip}
protocol is set to network.ip_protocol, trustpoint_name is set to about.labels.key/value, dst_ip is set to target.ip
717064
Keypair {key_name} in the trustpoint {trustpoint_name} is regenerated for {mode} {protocol} certificate renewal
key_name is set to about.labels.key/value, trustpoint_name is set to about.labels.key/value, mode is set to about.labels.key/value, protocol is set to network.ip_protocol
718001
Internal interprocess communication queue send failure: code {error_code}
error_code is set to security_result.description
718002
Create peer {dst_ip} failure, already at maximum of {no_of_peers}
dst_ip is set to target.ip, no_of_peers is set to about.labels.key/value
718003
Got unknown peer message {message_id} from {dst_ip}, local version {local_version_number}, remote version {remote_version_number}
message_id is set to about.labels.key/value, dst_ip is set to target.ip, local_version_number is set to about.labels.key/value, remote_version_number is set to about.labels.key/value
718004
Got unknown internal message {message_id}
message_id is set to about.labels.key/value
718005
Fail to send to {dst_ip}, port {dst_port}
dst_ip is set to target.ip, dst_port is set to target.port
718006
Invalid load balancing state transition cur={current_state}][event={message_id}]
current_state is set to about.labels.key/value, message_id is set to about.labels.key/value
718007, 718008
Socket (bind|open) failure {error_code}]:{summary}
error_code is set to security_result.description, summary is set to security_result.summary
718009, 718011
Send HELLO (request|response) failure to {dst_ip}
dst_ip is set to target.ip
718010, 718012
Sent HELLO (request|response) to {dst_ip}
dst_ip is set to target.ip
718013
Peer {dst_ip} is not answering HELLO
dst_ip is set to target.ip
718014
Primary peer {dst_ip} is not answering HELLO
dst_ip is set to target.ip
718015, 718016
Received HELLO (request|response) from {dst_ip}
dst_ip is set to target.ip
718017
Got timeout for unknown peer {src_ip} msg type {message_type}
src_ip is set to principal.ip, message_type is set to about.labels.key/value
718018
Send KEEPALIVE request failure to {dst_ip}
dst_ip is set to target.ip
718019
Sent KEEPALIVE request to {dst_ip}
dst_ip is set to target.ip
718020
Send KEEPALIVE response failure to {dst_ip}
dst_ip is set to target.ip
718021
Sent KEEPALIVE response to {dst_ip}
dst_ip is set to target.ip
718022
Received KEEPALIVE request from {src_ip}
src_ip is set to principal.ip
718023
Received KEEPALIVE response from {src_ip}
src_ip is set to principal.ip
718025
Sent CFG UPDATE to {dst_ip}
dst_ip is set to target.ip
718026
Received CFG UPDATE from {src_ip}
src_ip is set to principal.ip
718029
Sent OOS indicator to {dst_ip}
dst_ip is set to target.ip
718034
Sent TOPOLOGY indicator to {dst_ip}
dst_ip is set to target.ip
718035
Received TOPOLOGY indicator from {src_ip}
src_ip is set to principal.ip
718036
Process timeout for req-type {type_value}, exid {exchange_id}, peer {src_ip}
type_value is set to about.labels.key/value, exchange_id is set to about.labels.key/value, src_ip is set to principal.ip
718024
Send CFG UPDATE failure to {dst_ip}
dst_ip is set to target.ip
718027
Received unexpected KEEPALIVE request from {dst_ip}
dst_ip is set to target.ip
718028
Send OOS indicator failure to {dst_ip}
dst_ip is set to target.ip
718030
Received planned OOS from {dst_ip}
dst_ip is set to target.ip
718031
Received OOS obituary for {dst_ip}
dst_ip is set to target.ip
718032
Received OOS indicator from {dst_ip}
dst_ip is set to target.ip
718033
Send TOPOLOGY indicator failure to {dst_ip}
dst_ip is set to target.ip
718037
Primary processed {number_of_timeouts} timeouts
number_of_timeouts is set to about.labels.key/value
718038
Secondary processed {number_of_timeouts} timeouts
number_of_timeouts is set to about.labels.key/value
718039
Process dead peer {dst_ip}
dst_ip is set to target.ip
718040
Timed-out exchange ID {exchange_id} not found
exchange_id is set to about.labels.key/value
718041
Timeout msgType={message_type}] processed with no callback
message_type is set to about.labels.key/value
718042
Unable to ARP for {dst_ip}
dst_ip is set to target.ip
718043
(Updating|Removing) duplicate peer entry {dst_ip}
dst_ip is set to target.ip
718044, 718045
(Deleted|Created) peer {dst_ip}
dst_ip is set to target.ip
718047
Fail to create group policy {policy_name}
policy_name is set to target.resource.name
718046
Create group policy {policy_name}
policy_name is set to target.resource.name
718048, 718050
(Create|Delete) of secure tunnel failure for peer {dst_ip}
dst_ip is set to target.ip
718051, 718049
(Deleted|Created) secure tunnel to peer {dst_ip}
dst_ip is set to target.ip
718052
Received GRAT-ARP from duplicate primary {dst_mac}
dst_mac is set to target.mac
718053
Detected duplicate primary, mastership stolen {dst_mac}
dst_mac is set to target.mac
718054
Detected duplicate primary {dst_mac} and going to secondary
dst_mac is set to target.mac
718055
Detected duplicate primary {dst_mac} and staying PRIMARY
dst_mac is set to target.mac
718056
Deleted primary peer, IP {src_ip}
src_ip is set to principal.ip
718057
Queue send failure from ISR, msg type {error_code}
error_code is set to security_result.description
718058
State machine return code: {action_routine},{return_code}
action_routine is set to about.labels.key/value, return_code is set to security_result.description
718059
State machine function trace: state={state_name}, event={event_name}, func={action_routine}
state_name is set to about.labels.key/value, event_name is set to about.labels.key/value, action_routine is set to about.labels.key/value
718060
Inbound socket select fail: context={context_id}
context_id is set to about.labels.key/value
718061
Inbound socket read fail: context={context_id}
context_id is set to about.labels.key/value
718062
Inbound thread is awake (context={context_id})
context_id is set to about.labels.key/value
718063
Interface {interface_name} is down
interface_name is set to about.labels.key/value
718064
Admin. interface {interface_name} is down
interface_name is set to about.labels.key/value
718065
Cannot continue to run (public=(up|down), private=(up|down), enable={lb_state}, master={dst_ip}, session=(Enable|Disable))
lb_state is set to about.labels.key/value, dst_ip is set to target.ip
718066
Cannot add secondary address to interface {interface_name}, ip {dst_ip}
interface_name is set to about.labels.key/value, dst_ip is set to target.ip
718067
Cannot delete secondary address to interface {interface_name}, ip {dst_ip}
interface_name is set to about.labels.key/value, dst_ip is set to target.ip
718068
Start VPN Load Balancing in context {context_id}
context_id is set to about.labels.key/value
718069
Stop VPN Load Balancing in context {context_id}
context_id is set to about.labels.key/value
718070
Reset VPN Load Balancing in context {context_id}
context_id is set to about.labels.key/value
718071
Terminate VPN Load Balancing in context {context_id}
context_id is set to about.labels.key/value
718072
Becoming primary of Load Balancing in context {context_id}
context_id is set to about.labels.key/value
718073
Becoming secondary of Load Balancing in context {context_id}
context_id is set to about.labels.key/value
718074
Fail to create access list for peer {context_id}
context_id is set to about.labels.key/value
718075
Peer {dst_ip} access list not set
dst_ip is set to target.ip
718076
Fail to create tunnel group for peer {dst_ip}
dst_ip is set to target.ip
718077
Fail to delete tunnel group for peer {dst_ip}
dst_ip is set to target.ip
718078
Fail to create crypto map for peer {dst_ip}
dst_ip is set to target.ip
718079
Fail to delete crypto map for peer {dst_ip}
dst_ip is set to target.ip
718080
Fail to create crypto policy for peer {dst_ip}
dst_ip is set to target.ip
718081
Fail to delete crypto policy for peer {dst_ip}
dst_ip is set to target.ip
718082
Fail to create crypto ipsec for peer {dst_ip}
dst_ip is set to target.ip
718083
Fail to delete crypto ipsec for peer {dst_ip}
dst_ip is set to target.ip
718084
(Public|cluster|Cluster) IP not on the same subnet: public {dst_ip}, mask {netmask}, cluster {dst_ip1}
dst_ip is set to target.ip, netmask is set to about.labels.key/value, dst_ip1 is set to target.ip
718085
Interface {interface_name} has no IP address defined
interface_name is set to about.labels.key/value
718086
Fail to install LB NP rules: type {rule_type}, dst {interface_name}, port {dst_port}
rule_type is set to about.labels.key/value, interface_name is set to about.labels.key/value, dst_port is set to target.port
718087
Fail to delete LB NP rules: type {rule_type}, rule {rule_id}
rule_type is set to about.labels.key/value, rule_id is set to about.labels.key/value
718088
Possible VPN LB misconfiguration. Offending device MAC {mac_address}
mac_address is set to about.labels.key/value
719001
Email Proxy session could not be established: session limit of {maximum_sessions} has been reached
maximum_sessions is set to about.labels.key/value
719002
Email Proxy session {session_pointer} from {src_ip} has been terminated due to {summary} error
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip, summary is set to security_result.summary
719003
Email Proxy session {session_pointer} resources have been freed for {src_ip}
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip
719004
Email Proxy session {session_pointer} has been successfully established for {src_ip}
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip
719005
FSM <message_text> has been created using {protocol} for session {session_pointer} from {src_ip}
protocol is set to network.ip_protocol, session_pointer is set to about.labels.key/value, src_ip is set to principal.ip
719006
Email Proxy session {session_pointer} has timed out for {src_ip} because of network congestion
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip
719007
Email Proxy session {session_pointer} cannot be found for {src_ip}
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip
719010
{protocol} Email Proxy feature is disabled on interface {interface_name}
protocol is set to network.ip_protocol, interface_name is set to about.labels.key/value
719011
{protocol} Email Proxy feature is enabled on interface {interface_name}
protocol is set to network.ip_protocol, interface_name is set to about.labels.key/value
719012
Email Proxy server listening on port {dst_port} for mail protocol {protocol}
dst_port is set to target.port, protocol is set to network.ip_protocol
719013
Email Proxy server closing port {dst_port} for mail protocol {protocol}
dst_port is set to target.port, protocol is set to network.ip_protocol
719014
Email Proxy is changing listen port from {old_dst_port} to {dst_port} for mail protocol {protocol}
old_dst_port is set to target.labels.key/value, dst_port is set to target.port, protocol is set to network.ip_protocol
719015
Parsed emailproxy session {session_pointer} from {src_ip} username: mailuser = {mail_user}, vpnuser = {vpn_user}, mailserver = {mail_server}
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip, mail_user is set to about.labels.key/value, vpn_user is set to about.labels.key/value, mail_server is set to about.labels.key/value
719016
Parsed emailproxy session {session_pointer} from {src_ip} password: mailpass = {mail_password}, vpnpass= {vpn_password}
session_pointer is set to about.labels.key/value, src_ip is set to principal.ip, mail_password is set to about.labels.key/value, vpn_password is set to about.labels.key/value
719017
WebVPN user: {user_name} invalid dynamic ACL
user_name is set to target.user.userid
719018
WebVPN user: {user_name} ACL ID {acl_id} not found
user_name is set to target.user.userid, acl_id is set to about.labels.key/value
719019
WebVPN user: {user_name} authorization failed
user_name is set to target.user.userid
719020
WebVPN user {user_name} authorization completed successfully
user_name is set to target.user.userid
719021
WebVPN user: {user_name} is not checked against ACL
user_name is set to target.user.userid
719022
WebVPN user {user_name} has been authenticated
user_name is set to target.user.userid
719023
WebVPN user {user_name} has not been successfully authenticated. Access denied
user_name is set to target.user.userid
719024
Email Proxy piggyback auth fail: session = {session_pointer} user={user_name} addr={src_ip}
session_pointer is set to about.labels.key/value, user_name is set to target.user.userid, src_ip is set to principal.ip
719025
Email Proxy DNS name resolution failed for {target_hostname}
target_hostname is set to target.hostname
719026
Email Proxy DNS name {target_hostname} resolved to {dst_ip}
target_hostname is set to target.hostname, dst_ip is set to target.ip
720014
(VPN-(Primary|Secondary)) Phase 2 connection entry (msg_id={message_id}, my cookie={my_cookie}, his cookie={his_cookie}) contains no SA list
message_id is set to about.labels.key/value, my_cookie is set to about.labels.key/value, his_cookie is set to about.labels.key/value
720015
(VPN-(Primary|Secondary)) Cannot found Phase 1 SA for Phase 2 connection entry (msg_id={message_id},my cookie={my_cookie}, his cookie={his_cookie})
message_id is set to about.labels.key/value, my_cookie is set to about.labels.key/value, his_cookie is set to about.labels.key/value
720016
(VPN-(Primary|Secondary)) Failed to initialize default timer {index}
index is set to about.labels.key/value
720018
(VPN-(Primary|Secondary)) Failed to get a buffer from the underlying core high availability subsystem. Error code {error_code}
error_code is set to security_result.description
720021
(VPN-(Primary|Secondary)) HA non-block send failed for peer msg {message_id}. HA error {error_code}
message_id is set to about.labels.key/value, error_code is set to security_result.description
720022
(VPN-(?P<unit_name>Primary|Secondary)) Cannot find trustpoint {trustpoint_name}
unit_name is set to about.labels.key/value, trustpoint_name is set to about.labels.key/value
720023
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Peer is (not )?present
unit_name is set to about.labels.key/value
720024
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Control channel is {status}
unit_name is set to about.labels.key/value, status is set to about.labels.key/value
720025
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Data channel is {status}
unit_name is set to about.labels.key/value, status is set to about.labels.key/value
720026
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Current progression is being aborted
unit_name is set to about.labels.key/value
720027
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: My state {current_state}
unit_name is set to about.labels.key/value, current_state is set to about.labels.key/value
720028
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Peer state {current_state}
unit_name is set to about.labels.key/value, current_state is set to about.labels.key/value
720029
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Start VPN bulk sync state
unit_name is set to about.labels.key/value
720030
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Stop bulk sync state
unit_name is set to about.labels.key/value
720031
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: Invalid event received. event={event_id}
unit_name is set to about.labels.key/value, event_id is set to about.labels.key/value
720032
(VPN-(?P<unit_name>Primary|Secondary)) HA status callback: id={id}, seq={sequence_number}, grp={group_number}, event={current_event}, op={operand}, my={current_state}, peer={peer_state}
unit_name is set to about.labels.key/value, id is set to about.labels.key/value, sequence_number is set to about.labels.key/value, group_number is set to about.labels.key/value, current_event is set to about.labels.key/value, operand is set to about.labels.key/value, current_state is set to about.labels.key/value, peer_state is set to about.labels.key/value
720033
(VPN-(?P<unit_name>Primary|Secondary)) Failed to queue add to message queue
unit_name is set to about.labels.key/value
720034
(VPN-(?P<unit_name>Primary|Secondary)) Invalid type ({message_type}) for message handler
unit_name is set to about.labels.key/value, message_type is set to about.labels.key/value
720035
(VPN-(?P<unit_name>Primary|Secondary)) Fail to look up CTCP flow handle
unit_name is set to about.labels.key/value
720036
(VPN-(?P<unit_name>Primary|Secondary)) Failed to process state update message from( the active)? peer
unit_name is set to about.labels.key/value
720037
(VPN-(?P<unit_name>Primary|Secondary)) HA progression callback: id={id},seq={sequence_number},grp={group_number},event={current_event},op={operand},my={current_state},peer={peer_state}
unit_name is set to about.labels.key/value, id is set to about.labels.key/value, sequence_number is set to about.labels.key/value, group_number is set to about.labels.key/value, current_event is set to about.labels.key/value, operand is set to about.labels.key/value, current_state is set to about.labels.key/value, peer_state is set to about.labels.key/value
720038
(VPN-(?P<unit_name>Primary|Secondary)) Corrupted( peer)? message (from active unit|buffer)
unit_name is set to about.labels.key/value
720039
(VPN-(?P<unit_name>Primary|Secondary)) VPN failover client is transitioning to active state
unit_name is set to about.labels.key/value
720040
(VPN-(?P<unit_name>Primary|Secondary)) VPN failover client is transitioning to standby state
unit_name is set to about.labels.key/value
720041
(VPN-(?P<unit_name>Primary|Secondary)) Sending {message_type} message {message_id} to standby unit
unit_name is set to about.labels.key/value, message_type is set to about.labels.key/value, message_id is set to about.labels.key/value
720042
(VPN-(?P<unit_name>Primary|Secondary)) Receiving {message_type} message {message_id} from active unit
unit_name is set to about.labels.key/value, message_type is set to about.labels.key/value, message_id is set to about.labels.key/value
720043
(VPN-(?P<unit_name>Primary|Secondary)) Failed to send {message_type} message id to standby unit
unit_name is set to about.labels.key/value, message_type is set to about.labels.key/value
720044
(VPN-(?P<unit_name>Primary|Secondary)) Failed to receive message from active unit
unit_name is set to about.labels.key/value
720045
(VPN-(?P<unit_name>Primary|Secondary)) Start bulk syncing of state information on standby unit
unit_name is set to about.labels.key/value
720046
(VPN-(?P<unit_name>Primary|Secondary)) End bulk syncing of state information on standby unit
unit_name is set to about.labels.key/value
720047
(VPN-(?P<unit_name>Primary|Secondary)) Failed to sync SDI node secret file for server {dst_ip} on the standby unit
unit_name is set to about.labels.key/value, dst_ip is set to target.ip
720048
(VPN-(?P<unit_name>Primary|Secondary)) FSM action trace begin: state={current_state}, last event={event_name}, func={function}
unit_name is set to about.labels.key/value, current_state is set to about.labels.key/value, event_name is set to about.labels.key/value, function is set to about.labels.key/value
720049
(VPN-(?P<unit_name>Primary|Secondary)) FSM action trace end: state={current_state}, last event={event_name}, return={return_code}, func={function}
unit_name is set to about.labels.key/value, current_state is set to about.labels.key/value, event_name is set to about.labels.key/value, return_code is set to security_result.description, function is set to about.labels.key/value
720050
(VPN-(?P<unit_name>Primary|Secondary)) Failed to remove timer. ID = {message_id}
unit_name is set to about.labels.key/value, message_id is set to about.labels.key/value
720051
(VPN-(?P<unit_name>Primary|Secondary)) Failed to add new SDI node secret file for server {dst_ip} on the standby unit
unit_name is set to about.labels.key/value, dst_ip is set to target.ip
720052
(VPN-(?P<unit_name>Primary|Secondary)) Failed to delete SDI node secret file for server {dst_ip} on the standby unit
unit_name is set to about.labels.key/value, dst_ip is set to target.ip
720053
(VPN-(?P<unit_name>Primary|Secondary)) Failed to add cTCP IKE rule during bulk sync, peer={dst_ip}, port={dst_port}
unit_name is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
720054
(VPN-(?P<unit_name>Primary|Secondary)) Failed to add new cTCP record, peer={dst_ip}, port={dst_port}
unit_name is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
720055
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover can only be run in single/non-transparent mode
unit_name is set to about.labels.key/value
720056
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover Message Thread is being disabled
unit_name is set to about.labels.key/value
720057
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover Message Thread is enabled
unit_name is set to about.labels.key/value
720058
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover Timer Thread is disabled
unit_name is set to about.labels.key/value
720059
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover Timer Thread is enabled
unit_name is set to about.labels.key/value
720060
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover Sync Thread is disabled
unit_name is set to about.labels.key/value
720061
(VPN-(?P<unit_name>Primary|Secondary)) VPN Stateful failover Sync Thread is enabled
unit_name is set to about.labels.key/value
720062
(VPN-(?P<unit_name>Primary|Secondary)) Active unit started bulk sync of state information to( the)? standby unit
unit_name is set to about.labels.key/value
720063
(VPN-(?P<unit_name>Primary|Secondary)) Active unit completed bulk sync of state information to standby
unit_name is set to about.labels.key/value
720064
(VPN-(?P<unit_name>Primary|Secondary)) Failed to update cTCP database record for peer={dst_ip}, port={dst_port} during bulk sync
unit_name is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
720065
(VPN-(?P<unit_name>Primary|Secondary)) Failed to add new cTCP IKE rule, peer={dst_ip}, port={dst_port}
unit_name is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
720066
(VPN-(?P<unit_name>Primary|Secondary)) Failed to activate IKE database
unit_name is set to about.labels.key/value
720067
(VPN-(?P<unit_name>Primary|Secondary)) Failed to deactivate IKE database
unit_name is set to about.labels.key/value
720068
(VPN-(?P<unit_name>Primary|Secondary)) Failed to parse peer message
unit_name is set to about.labels.key/value
720069
(VPN-(?P<unit_name>Primary|Secondary)) Failed to activate cTCP database
unit_name is set to about.labels.key/value
720070
(VPN-(?P<unit_name>Primary|Secondary)) Failed to deactivate cTCP database
unit_name is set to about.labels.key/value
720071
(VPN-(?P<unit_name>Primary|Secondary)) Failed to update cTCP dynamic data
unit_name is set to about.labels.key/value
720072
Timeout waiting for Integrity Firewall Server {dst_interface_name},{dst_ip}] to become available
dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
720073
VPN Session failed to replicate - ACL {acl_name} not found
acl_name is set to about.labels.key/value
721001
({device_type}) WebVPN Failover SubSystem started successfully.({device_type}) either WebVPN-primary or WebVPN-secondary
device_type is set to about.labels.key/value, device_type is set to about.labels.key/value
721002
({device_type}) HA status change: event {current_event}, my state {current_state}, peer state {peer_state}
device_type is set to about.labels.key/value, current_event is set to about.labels.key/value, current_state is set to about.labels.key/value, peer_state is set to about.labels.key/value
721003
({device_type}) HA progression change: event {current_event}, my state {current_state}, peer state {peer_state}
device_type is set to about.labels.key/value, current_event is set to about.labels.key/value, current_state is set to about.labels.key/value, peer_state is set to about.labels.key/value
721004
({device_type}) Create access list {access_list_name} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value
721005
({device_type}) Fail to create access list {access_list_name} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value
721006
({device_type}) Update access list {access_list_name} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value
721007
({device_type}) Fail to update access list {access_list_name} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value
721008
({device_type}) Delete access list {access_list_name} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value
721009
({device_type}) Fail to delete access list {access_list_name} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value
721010
({device_type}) Add access list rule {access_list_name}, line {line_number} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value, line_number is set to about.labels.key/value
721011
({device_type}) Fail to add access list rule {access_list_name}, line {line_number} on standby unit
device_type is set to about.labels.key/value, access_list_name is set to about.labels.key/value, line_number is set to about.labels.key/value
721012
({device_type}) Enable APCF XML file {target_file_full_path} on the standby unit
device_type is set to about.labels.key/value, target_file_full_path is set to target.file.full_path
721013
({device_type}) Fail to enable APCF XML file {target_file_full_path} on the standby unit
device_type is set to about.labels.key/value, target_file_full_path is set to target.file.full_path
721014
({device_type}) Disable APCF XML file {target_file_full_path} on the standby unit
device_type is set to about.labels.key/value, target_file_full_path is set to target.file.full_path
721015
({device_type}) Fail to disable APCF XML file {target_file_full_path} on the standby unit
device_type is set to about.labels.key/value, target_file_full_path is set to target.file.full_path
721016
({device_type}) WebVPN session for client user {user_name}, IP {dst_ip} has been created
device_type is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip
721017
({device_type}) Fail to create WebVPN session for user {user_name}, IP {dst_ip}
device_type is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip
721018
({device_type}) WebVPN session for client user {user_name}, IP(v4)? {dst_ip} has been deleted
device_type is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip
721019
({device_type}) Fail to delete WebVPN session for client user {user_name}, IP {dst_ip}
device_type is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip
722006
Group {group_name} User {user_name} IP {dst_ip} Invalid address {invalid_ip} assigned to SVC connection
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, invalid_ip is set to about.labels.key/value
722015
Group {group_name} User {user_name} IP {dst_ip} Unknown SVC frame type: {frame_type}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, frame_type is set to about.labels.key/value
722016
Group {group_name} User {user_name} IP {dst_ip} Bad SVC frame length: {frame_length} expected: {frame_expected_length}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, frame_length is set to about.labels.key/value, frame_expected_length is set to about.labels.key/value
722018
Group {group_name} User {user_name} IP {dst_ip} Bad SVC protocol version: {svc_version}, expected: {svc_expected_version}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, svc_version is set to about.labels.key/value, svc_expected_version is set to about.labels.key/value
722020, 722041
TunnelGroup {tunnel_group} GroupPolicy {group_policy} User {user_name} IP {dst_ip} {summary}
tunnel_group is set to target.group.group_display_name, group_policy is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip, summary is set to security_result.summary
722022
Group (<)?%{DATA:src_group_name}(>)? User (<)?%{DATA:src_username}(>)? IP (<)?%{IPORHOST:src_ip}(>)? %{WORD:protocol} SVC connection established  <message_text> compression
src_group_name is set to principal.user.group_identifiers, src_username is set to principal.user.userid, src_ip is set to principal.ip, protocol is set to network.ip_protocol, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
722023
Group (<)?%{DATA:src_group_name}(>)? User (<)?%{DATA:src_username}(>)? IP (<)?%{IPORHOST:src_ip}(>)? %{WORD:protocol} SVC connection terminated  <message_text> compression
src_group_name is set to principal.user.group_identifiers, src_username is set to principal.user.userid, src_ip is set to principal.ip, protocol is set to network.ip_protocol, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
722012
Group (<)?%{DATA:src_group_name}(>)? User (<)?%{DATA:src_username}(>)? IP (<)?%{IPORHOST:src_ip}(>)? SVC Message: %{DATA:message_id}/NOTICE: %{GREEDYDATA:summary}
if message_id is equal to 14 then src_group_name is set to target.user.group_identifiers, src_username is set to target.user.userid, src_ip is set to target.ip, protocol is set to network.ip_protocol, summary is set to security_result.summary, metadata.event_type UDM is set to USER_LOGOUT, extensions.auth.type UDM is set to VPN, if sysloghost is a valid IP, it is set to target.ip otherwise, it is set to target.hostname, if message_id is not equal to 14 then src_group_name is set to principal.user.group_identifiers, src_username is set to principal.user.userid, src_ip is set to principal.ip, protocol is set to network.ip_protocol, summary is set to security_result.summary, metadata.event_type is set to NETWORK_CONNECTION, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
722028
Group (<)?%{DATA:src_group_name}(>)? User (<)?%{DATA:src_username}(>)? IP (<)?%{IPORHOST:src_ip}(>)? %{WORD:protocol} SVC connection closed.
src_group_name is set to principal.user.group_identifiers, src_username is set to principal.user.userid, src_ip is set to principal.ip, protocol is set to network.ip_protocol, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
722035, 722036
Group {group_name} User {user_name} IP {dst_ip} <message_text> large packet {received_bytes}(threshold {threshold})
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, received_bytes is set to network.received_bytes, threshold is set to about.labels.key/value
722044
Group {group_name} User {user_name} IP {dst_ip} Unable to request {ip_version} address for SSL tunnel
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, ip_version is set to about.labels.key/value
722051
Group (<)?{group_name}(>)? User (<)?{user_name}(>)? IP (<)?{dst_ip}(>)? IPv4 Address (<)?{src_ip1}(>)? IPv6 address (<)?{src_ip2}(>)? assigned to session
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, dst_ip1 is set to principal.ip, dst_ip2 is set to principal.ip
722053
Group {group_policy} User {user_name} IP {dst_ip} Unknown client {user_agent} connection
group_policy is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip, user_agent is set to network.http.user_agent
722054
Group {group_policy} User {user_name} IP {dst_ip} SVC (?P<action>terminating) connection: Failed to install Redirect URL: {redirect_url} Redirect ACL: non_exist for {dst_ip1}
action is set to security_result.action, group_policy is set to about.labels.key/value, user_name is set to target.user.userid, dst_ip is set to target.ip, redirect_url is set to target.url, dst_ip1 is set to target.ip
722055
Group {group_name} User {user_name} IP {dst_ip} Client Type: {user_agent}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, user_agent is set to network.http.user_agent
722056
Unsupported AnyConnect client connection rejected from {dst_ip}. Client info: {user_agent}. Reason: {summary}
dst_ip is set to target.ip, user_agent is set to network.http.user_agent, summary is set to security_result.summary
723001, 723002
Group {group_name}, User {user_name}, IP {dst_ip}: WebVPN Citrix ICA connection {session_id} is (?P<action>up|down)
action is set to security_result.action, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, session_id is set to network.session_id
723014
Group {group_name}, User {user_name}, IP {dst_ip}: WebVPN Citrix {protocol} connection {session_id} to server {server_identifier} on channel {channel_id} initiated
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, protocol is set to network.ip_protocol, session_id is set to network.session_id, server_identifier is set to about.labels.key/value, channel_id is set to about.labels.key/value
725001
Starting SSL handshake with <message_text> {interface_name}:{src_ip}(/{src_port})? to {dst_ip}/{dst_port} for {protocol} session
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, protocol is set to network.ip_protocol
725001
Starting SSL handshake with <message_text> {interface_name}:{src_ip}/{src_port} for {protocol} session
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, protocol is set to network.ip_protocol
725002
Device completed SSL handshake with <message_text> {interface_name}:{src_ip}(/{src_port})? to {dst_ip}/{dst_port} for {version_protocol} session
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, version_protocol is set to network.tls.version_protocol
725002
Device completed SSL handshake with <message_text> {interface_name}:{src_ip}/{src_port}( for {version_protocol} session)?
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, version_protocol is set to network.tls.version_protocol
725003, 725005
SSL <message_text> {interface_name}:{src_ip}/{src_port}( to {dst_ip}/{dst_port})? request<message_text>
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
725004
Device requesting certificate from SSL <message_text> {interface_name}:{src_ip}(/{src_port})? to {dst_ip}/{dst_port} for authentication
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
725006
Device failed SSL handshake with <message_text> {interface_name}:{src_ip}/{src_port}( to {dst_ip}/{dst_port})?
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
725007
SSL session with <message_text> {interface_name}:{src_ip}/{src_port}( to {dst_ip}/{dst_port})? terminated
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
725008
SSL <message_text> {interface_name}:{src_ip}(/{src_port})? to {dst_ip}/{dst_port}<message_text>
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
725009
Device proposes the following <message_text> cipher((s))?( to)? <message_text> {interface_name}:{src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
725016
Device selects trust-point {trust_point} for <message_text> {interface_name}:{src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
trust_point is set to about.labels.key/value, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
726001
Inspected (?P<im_protocol>MSN IM|YAHOO IM) {target_service} Session between Client {user_name} and {user_name_} Packet flow from {src_interface_name}:/{src_ip}(/{src_port})? to {dst_interface_name}:/{dst_ip}/{dst_port} Action: {action} Matched Class {class_map_id} {class_map_name}
im_protocol is set to about.labels.key/value, target_service is set to target.application, user_name is set to target.user.userid, user_name_ is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, action is set to security_result.action, class_map_id is set to about.labels.key/value, class_map_name is set to about.labels.key/value
730004
Group {group_name} User {user_name} IP {src_ip} VLAN ID {vlan_id} from AAA ignored
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, src_ip is set to principal.ip, vlan_id is set to about.labels.key/value
730005
Group {group_name} User {user_name} {src_ip} VLAN Mapping error. VLAN {vlan_id} may be out of range, unassigned to any interface or assigned to multiple interfaces
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, src_ip is set to principal.ip, vlan_id is set to about.labels.key/value
730008
Group {group_name}, User {user_name}, IP {dst_ip}, VLAN MAPPING timeout waiting NACApp
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
730009
Group {group_name}, User {user_name}, IP {dst_ip}, CAS {src_ip1}, capacity exceeded, (?P<action>terminating) connection
action is set to security_result.action, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, src_ip1 is set to principal.ip
731001, 731002
NAC policy <message_text>: name:{policy_name} Type:{policy_type}
policy_name is set to target.resource.name, policy_type is set to about.labels.key/value
731003
nac-policy <message_text>: name:{policy_name} Type:{policy_type}
policy_name is set to target.resource.name, policy_type is set to about.labels.key/value
732001
Group {group_name}, User {user_name}, IP {dst_ip}, Fail to parse NAC-SETTINGS {nac_settings_id} , (?P<action>terminating) connection
action is set to security_result.action, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, nac_settings_id is set to about.labels.key/value
732002
Group {group_name}, User {user_name}, IP {dst_ip}, NAC-SETTINGS {nac_settings_id} from AAA ignored, existing NAC-SETTINGS {settingsid_in_use} used instead
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, nac_settings_id is set to about.labels.key/value, settingsid_in_use is set to about.labels.key/value
732003
Group {group_name}, User {user_name}, IP {dst_ip}, NAC-SETTINGS {nac_settings_id} from AAA is invalid, {action} connection
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, nac_settings_id is set to about.labels.key/value, action is set to security_result.action
733100
<message_text> drop rate(-)?{rate_id} exceeded. Current burst rate is {current_burst_rate} per second, max configured rate is {max_burst_rate}; Current average rate is {current_average_rate} per second, max configured rate is {max_average_val}; Cumulative total count is {total_cnt}
rate_id is set to about.labels.key/value, current_burst_rate is set to about.labels.key/value, max_burst_rate is set to about.labels.key/value, current_average_rate is set to about.labels.key/value, max_average_val is set to about.labels.key/value, total_cnt is set to about.labels.key/value
733101
<message_text> {dst_ip} (?P<tag>is targeted|is attacking). Current burst rate is {current_burst_rate} per second, max configured rate is {max_burst_rate}; Current average rate is {current_average_rate} per second, max configured rate is {max_average_val}; Cumulative total count is {total_cnt}
, dst_ip is set to target.ip, current_burst_rate is set to about.labels.key/value, max_burst_rate is set to about.labels.key/value, current_average_rate is set to about.labels.key/value, max_average_val is set to about.labels.key/value, total_cnt is set to about.labels.key/value
733102, 733103
Threat-detection <message_text> host {target_hostname} <message_text> shun list
target_hostname is set to target.hostname
734001
{category}: User {src_username}, Addr {src_ip}, Connection {connection} : The following DAP records were selected for this connection: {record_names}
category is set to security_result.category_details, src_username is set to principal.user.userid, src_ip is set to principal.ip, connection is set to about.labels.key/value, record_names is set to about.labels.key/value
734002
{category}: User {src_username}, Addr {src_ip}: Connection (?P<action>terminated) by the following DAP records: {record_names}
action is set to security_result.action, category is set to security_result.category_details, src_username is set to principal.user.userid, src_ip is set to principal.ip, record_names is set to about.labels.key/value
734003
{category}: User {src_username}, Addr {src_ip}: Session Attribute: {attribute}
category is set to security_result.category_details, src_username is set to principal.user.userid, src_ip is set to principal.ip, attribute is set to about.labels.key/value
734004
{category}: Processing error: {internal_error_code}
category is set to security_result.category_details, internal_error_code is set to about.labels.key/value
735001, 735002
{category}: Cooling Fan {device_number_markings}: {summary}
category is set to security_result.category_details, device_number_markings is set to about.labels.key/value, summary is set to security_result.summary
735003, 735004
{category}: Power Supply {device_number_markings}: {summary}
category is set to security_result.category_details, device_number_markings is set to about.labels.key/value, summary is set to security_result.summary
735007
{category}: CPU {device_number_markings} : Temp: {temperature_value} {units}, {summary}
category is set to security_result.category_details, device_number_markings is set to about.labels.key/value, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value, summary is set to security_result.summary
735008
{category}: Chassis Ambient {device_number_markings} : Temp: {temperature_value} {units}, {summary}
category is set to security_result.category_details, device_number_markings is set to about.labels.key/value, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value, summary is set to security_result.summary
735014 and 735013
Voltage Channel {voltage_channel_number}: {summary}
voltage_channel_number is set to about.labels.key/value, summary is set to security_result.summary
735016
Chassis Ambient {chassis_sensor_number} : Temp: {temperature_value} {units}, <message_text>
chassis_sensor_number is set to about.labels.key/value, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value
735019, 735018 and 735017
Power Supply {power_supply_number} : Temp: {temperature_value} {units}, {summary}
power_supply_number is set to about.labels.key/value, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value, summary is set to security_result.summary
735012 and 735011
Power Supply {voltage_channel_number}: {summary}
voltage_channel_number is set to about.labels.key/value, summary is set to security_result.summary
735015 and 735020
CPU {cpu_number}: Temp: {temperature_value} {units}(,|) {summary}
cpu_number is set to target.asset.hardware.serial_number, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value, summary is set to security_result.summary
735021
Chassis {chassis_sensor_number}: Temp: {temperature_value} {units} {summary}
chassis_sensor_number is set to about.labels.key/value, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value, summary is set to security_result.summary
735026, 735025 and 735024
IO Hub {io_hub_number} : Temp: {temperature_value} {units}, {summary}
io_hub_number is set to about.labels.key/value, temperature_value is set to about.labels.key/value, units is set to about.labels.key/value, summary is set to security_result.summary
735027
CPU {cpu_number} Voltage Regulator is running beyond the max thermal operating temperature and the device will be shutting down immediately. The chassis and CPU need to be inspected immediately for ventilation issues
cpu_number is set to target.asset.hardware.serial_number
737002
{category}: Session= {session_id},Received unknown message {num} variables
category is set to security_result.category_details, session_id is set to network.session_id, num is set to about.labels.key/value
737005, 737003 and 737004
{category}: Session= {session_id}, DHCP configured,<message_text>tunnel-group {tunnel_group}
category is set to security_result.category_details, session_id is set to network.session_id, tunnel_group is set to target.group.group_display_name
737006, 737007
{category}: Session= {session_id}, Local pool request <message_text> for tunnel-group {tunnel_group}
category is set to security_result.category_details, session_id is set to network.session_id, tunnel_group is set to target.group.group_display_name
737008
{category}: Session= {session_id}, '{tunnel_group}' not found
category is set to security_result.category_details, session_id is set to network.session_id, tunnel_group is set to target.group.group_display_name
737009, 737010
{category}: Session= {session_id}, AAA assigned address {dst_ip}, request <message_text>
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737011
{category}: Session= {session_id}, AAA assigned {dst_ip}, not permitted, retrying
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737012
{category}: Session= {session_id}, Address assignment failed
category is set to security_result.category_details, session_id is set to network.session_id
737013
{category}: Session= {session_id}, Error freeing address {dst_ip}, not found
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737014, 737015
{category}: Session= {session_id}, Freeing <message_text> address {dst_ip}
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737016
{category}: Session= {session_id}, Freeing local pool {pool_name} address {dst_ip}
category is set to security_result.category_details, session_id is set to network.session_id, pool_name is set to about.labels.key/value, dst_ip is set to target.ip
737017
{category}: Session= {session_id}, DHCP request attempt {num} <message_text>
category is set to security_result.category_details, session_id is set to network.session_id, num is set to about.labels.key/value
737019
{category}: Session= {session_id}, Unable to get address from group-policy or tunnel-group local pools
category is set to security_result.category_details, session_id is set to network.session_id
737023
{category}: Session= {session_id}, Unable to allocate memory to store local pool address {dst_ip}
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737024
{category}: Session= {session_id}, Client requested address {dst_ip}, already in use, retrying
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
73702
{category}:Session= {session_id}, Duplicate local pool address found, {dst_ip} in quarantine
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737026
{category}:Session= {session_id}, Client assigned {dst_ip} from local pool {pool_name}
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip, pool_name is set to about.labels.key/value
737027
{category}:Session= {session_id}, No data for address request
category is set to security_result.category_details, session_id is set to network.session_id
737028, 737030, 737032
{category}:Session= {session_id}, Unable to <message_text> {dst_ip} <message_text> standby: {summary}
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip, summary is set to security_result.summary
737029, 737031
{category}:Session= {session_id}, <message_text> {dst_ip} <message_text> standby
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737033
{category}:Session= {session_id}, Unable to assign {addr_allocator} provided IP address {dst_ip} to client. This IP address has already been assigned by {previous_addr_allocator}
category is set to security_result.category_details, session_id is set to network.session_id, addr_allocator is set to about.labels.key/value, dst_ip is set to target.ip, previous_addr_allocator is set to about.labels.key/value
737038
{category}:Session={session_id}, specified address {dst_ip} was in-use, trying to get another
category is set to security_result.category_details, session_id is set to network.session_id, dst_ip is set to target.ip
737402
{category}:Pool={pool_name}, Failed to return {dst_ip} to pool <message_text>. Reason: {summary}
category is set to security_result.category_details, pool_name is set to about.labels.key/value, dst_ip is set to target.ip, summary is set to security_result.summary
741000
Coredump filesystem image created on {created_directory} -size {file_size_mb} MB
created_directory is set to about.labels.key/value, file_size_mb is set to about.labels.key/value
741001
Coredump filesystem image on {created_directory} - resized from variable {previous_file_size_mb} MB to variable {file_size_mb} MB
created_directory is set to about.labels.key/value, previous_file_size_mb is set to about.labels.key/value, file_size_mb is set to about.labels.key/value
741002
Coredump log and filesystem contents cleared on {created_directory}
created_directory is set to about.labels.key/value
741003
Coredump filesystem and its contents removed on {created_directory}
created_directory is set to about.labels.key/value
741006
Unable to write Coredump Helper configuration, reason {summary}
summary is set to security_result.summary
742003, 742004
failed to <message_text> primary key for password encryption, reason {summary}
summary is set to security_result.summary
742005
cipher text {encrypted_pass} is not compatible with the configured primary key or the cipher text has been tampered with
encrypted_pass is set to about.labels.key/value
742008
password {encrypted_pass} decryption failed due to decoding error
encrypted_pass is set to about.labels.key/value
742010
encrypted password {encrypted_pass} is not well formed
encrypted_pass is set to about.labels.key/value
743000
The PCI device with vendor ID: {vendor_id} device ID: {device_id} located at <message_text>
vendor_id is set to about.labels.key/value, device_id is set to target.resource.product_object_id
"target.resource.resource_type" is set to "DEVICE"
"device_id" is set to "target.resource.product_object_id"
743004
System is not fully operational - PCI device with vendor ID {vendor_id}({vendor_name}), device ID {device_id}({device_name}) not found
vendor_id is set to about.labels.key/value, vendor_name is set to about.labels.key/value, device_id is set to target.resource.product_object_id, device_name is set to about.labels.key/value
"target.resource.resource_type" is set to "DEVICE"
"device_id" is set to "target.resource.product_object_id"
743010
EOBC RPC server failed to start for client module {user_name}
user_name is set to target.user.userid
743011
EOBC RPC call failed, return code {return_code} string
return_code is set to security_result.description
746004
<message_text>: Total number of activated user groups exceeds the {max_groups} groups for this platform
max_groups is set to about.labels.key/value
747029
<message_text>: Unit {unit_name} is quitting due to Cluster Control Link down
unit_name is set to about.labels.key/value
746005
<message_text>: The AD Agent<message_text>{dst_ip} cannot be reached - {summary}
dst_ip is set to target.ip, summary is set to security_result.summary
746007
<message_text>: NetBIOS response failed from User {user_name} at {dst_ip}
user_name is set to target.user.userid, dst_ip is set to target.ip
746011
Total number of users created exceeds the maximum number of {max_users} for this platform
max_users is set to about.labels.key/value
746012, 746013
<message_text>: <message_text> IP-User mapping {dst_ip} - {src_fwuser}\{user_name} -{summary}
dst_ip is set to target.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, user_name is set to target.user.userid, summary is set to security_result.summary
746014
<message_text>: FQDN] {target_hostname} address {dst_ip} obsolete
target_hostname is set to target.hostname, dst_ip is set to target.ip
if [target_hostname] != "" and [sysloghost] != "" then
"event.idm.read_only_udm.network.application_protocol" is set to "DNS"
"network.dns.questions.name" is set to "%{target_hostname}"
746015
<message_text>: FQDN] {target_hostname} resolved {dst_ip}
target_hostname is set to target.hostname, dst_ip is set to target.ip
if [target_hostname] != "" and [sysloghost] != "" then
"event.idm.read_only_udm.network.application_protocol" is set to "DNS"
"network.dns.questions.name" is set to "%{target_hostname}""
746016
<message_text>: DNS lookup failed, reason: {summary}
summary is set to security_result.summary
746018
<message_text>: Update import-user {src_fwuser}{group_name} done
src_fwuser is set to principal.user.userid/principal.labels.key/value, group_name is set to target.user.group_identifiers
746017
<message_text>: Update import-user {src_fwuser}<message_text>{group_name}
src_fwuser is set to principal.user.userid/principal.labels.key/value, group_name is set to target.user.group_identifiers
746010
<message_text>: update import-user {src_fwuser} {group_name} -{summary}
src_fwuser is set to principal.user.userid/principal.labels.key/value, group_name is set to target.user.group_identifiers, summary is set to security_result.summary
746019
<message_text>:<message_text> mapping {dst_ip} - {src_fwuser}\{user_name} failed
dst_ip is set to target.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value, user_name is set to target.user.userid
747001
<message_text>: Recovered from state machine event queue depleted. Event ({event_id},<message_text>) dropped. Current state {state_name}<message_text>
event_id is set to about.labels.key/value, state_name is set to about.labels.key/value
747003
<message_text>: Recovered from state machine failure to process event ({event_id},<message_text>) at {state_name}
event_id is set to about.labels.key/value, state_name is set to about.labels.key/value
747004
<message_text>: state machine changed from state {state_name} to {final_state_name}
state_name is set to about.labels.key/value, final_state_name is set to about.labels.key/value
747008
<message_text>: New cluster member {member_name} with serial number {serial_number_a} rejected due to name conflict with existing unit with serial number {serial_number_b}
member_name is set to about.labels.key/value, serial_number_a is set to about.labels.key/value, serial_number_b is set to about.labels.key/value
747009
<message_text>: Fatal error due to failure to create RPC server for module {module_name}
module_name is set to about.labels.key/value
747010
<message_text>: RPC call failed, message {summary}, return code {return_code}
summary is set to security_result.summary, return_code is set to security_result.description
747012, 747013
<message_text>: Failed to <message_text> global object id {hex_id} in domain {target_hostname} <message_text> peer {unit_name}, continuing operation
hex_id is set to about.labels.key/value, target_hostname is set to target.hostname, unit_name is set to about.labels.key/value
747014
<message_text>: Failed to <message_text> global object id {hex_id} in domain {target_hostname}, continuing operation
hex_id is set to about.labels.key/value, target_hostname is set to target.hostname
747015
<message_text>: Forcing stray member {unit_name} to leave the cluster
unit_name is set to about.labels.key/value
747016
<message_text>: Found a split cluster with both {unit_name_a} and {unit_name_b} as primary units. Primary role retained by {unit_name_a_}, {unit_name_b_} will leave, then join as a secondary
unit_name_a is set to about.labels.key/value, unit_name_b is set to about.labels.key/value, unit_name_a_ is set to about.labels.key/value, unit_name_b_ is set to about.labels.key/value
747017
<message_text>: Failed to enroll unit {unit_name} due to maximum member limit {limit_value} reached
unit_name is set to about.labels.key/value, limit_value is set to about.labels.key/value
747018
<message_text>: State progression failed due to timeout in module {module_name}
module_name is set to about.labels.key/value
747019
<message_text>: New cluster member {member_name} rejected due to Cluster Control Link IP subnet mismatch ({dst_ip}/<message_text> on new unit, {dst_ip1}/<message_text> on local unit)
member_name is set to about.labels.key/value, dst_ip is set to target.ip, dst_ip1 is set to target.ip
747020
<message_text>: New cluster member {unit_name} rejected due to encryption license mismatch
unit_name is set to about.labels.key/value
747021
<message_text>: Primary unit {unit_name} is quitting due to interface health check failure on {interface_name}
unit_name is set to about.labels.key/value, interface_name is set to about.labels.key/value
747022
<message_text>: Asking secondary unit {unit_name} to quit because it failed interface health check <message_text> times, rejoin will be attempted after <message_text> min. Failed interface: {interface_name}
unit_name is set to about.labels.key/value, interface_name is set to about.labels.key/value
747025
<message_text>: New cluster member {unit_name} rejected due to firewall mode mismatch
unit_name is set to about.labels.key/value
747026
<message_text>: New cluster member {unit_name} rejected due to cluster interface name mismatch ({new_interface_name} on new unit, {old_interface_name} on local unit)
unit_name is set to about.labels.key/value, new_interface_name is set to about.labels.key/value, old_interface_name is set to about.labels.key/value
747027
<message_text>: Failed to enroll unit {unit_name} due to insufficient size of cluster pool {pool_name} in {context_name}
unit_name is set to about.labels.key/value, pool_name is set to about.labels.key/value, context_name is set to about.labels.key/value
747028
<message_text>: New cluster member {unit_name} rejected due to interface mode mismatch ({new_mode_name} on new unit, {old_mode_name} on local unit)
unit_name is set to about.labels.key/value, new_mode_name is set to about.labels.key/value, old_mode_name is set to about.labels.key/value
747030
<message_text>: Asking secondary unit {unit_name} to quit because it failed interface health check <message_text> times (last failure on {interface_name}), Clustering must be manually enabled on the unit to re-join
unit_name is set to about.labels.key/value, interface_name is set to about.labels.key/value
747031
<message_text>: Platform mismatch between cluster primary ({cluster_platform}) and joining unit {unit_name} ({unit_platform})<message_text>
cluster_platform is set to about.labels.key/value, unit_name is set to about.labels.key/value, unit_platform is set to about.labels.key/value
747032
<message_text>: Service module mismatch between cluster primary ({cluster_platform}) and joining unit {unit_name} ({unit_platform})in slot {slot_number}<message_text>
cluster_platform is set to about.labels.key/value, unit_name is set to about.labels.key/value, unit_platform is set to about.labels.key/value, slot_number is set to about.labels.key/value
747033
<message_text>: Interface mismatch between cluster primary and joining unit {unit_name}<message_text>
unit_name is set to about.labels.key/value
747034, 747035
Unit {unit_name} is quitting due to Cluster Control Link down<message_text>
unit_name is set to about.labels.key/value
747037
Asking secondary Unit {unit_name} to quit due to its Security Service Module health check failure {number_of_health_check_failure} times, and its Security Service Module state is <message_text>
unit_name is set to about.labels.key/value, number_of_health_check_failure is set to about.labels.key/value
747038
Asking secondary Unit {unit_name} to quit due to Security Service Module health check failure {number_of_health_check_failure} times, and its Security Service Card Module is <message_text>
unit_name is set to about.labels.key/value, number_of_health_check_failure is set to about.labels.key/value
747040, 747039
Unit {unit_name} is quitting due to system failure for {number_of_health_check_failure}<message_text>
unit_name is set to about.labels.key/value, number_of_health_check_failure is set to about.labels.key/value
747041
Primary Unit {unit_name} is quitting due to interface health check failure on {number_of_health_check_failure}<message_text>
unit_name is set to about.labels.key/value, number_of_health_check_failure is set to about.labels.key/value
747042
<message_text>: Primary received the config hash string request message from an unknown member with id {cluster_member_id}
cluster_member_id is set to about.labels.key/value
747043
<message_text>: Get config hash string from primary error: ret_code {return_code}, string_len {string_len}
if [return_code] == "0" then "security_result.description" is set to "OK"
else if [return_code] == "1" then "security_result.description" is set to "Failed",
string_len is set to about.labels.key/value
747044
Configuration Hash string verification {summary}
summary is set to security_result.summary
748001
Module {slot_number} in chassis {chassis_number} is leaving the cluster due to a chassis configuration change
slot_number is set to about.labels.key/value, chassis_number is set to about.labels.key/value
748004, 748003
Module {slot_number} in chassis {chassis_number} is <message_text> the cluster due to a chassis
slot_number is set to about.labels.key/value, chassis_number is set to about.labels.key/value
748005
Failed to bundle the ports for module {slot_number} in chassis {chassis_number}; clustering is disabled
slot_number is set to about.labels.key/value, chassis_number is set to about.labels.key/value
748006
Asking module {slot_number} in chassis {chassis_number} to leave the cluster due to a port bundling failure
slot_number is set to about.labels.key/value, chassis_number is set to about.labels.key/value
748007
Failed to de-bundle the ports for module {slot_number} in chassis {chassis_number}; traffic may be black holed
slot_number is set to about.labels.key/value, chassis_number is set to about.labels.key/value
748100
{target_service} application status is changed from {old_status} to {new_status}
target_service is set to target.application, old_status is set to about.labels.key/value, new_status is set to about.labels.key/value
748101
Peer unit (<|){unit_id}(>|) reported its {target_service} application status is {status}
unit_id is set to about.labels.key/value, target_service is set to target.application, status is set to about.labels.key/value
748102
Primary unit (<|){unit_id}(>|) is quitting due to {target_service} Application health check failure, and primary's application state is {status}
unit_id is set to about.labels.key/value, target_service is set to target.application, status is set to about.labels.key/value
748103
Asking secondary unit (<|){unit_id}(>|) to quit due to {target_service} Application health check failure, and secondary's application state is {status}
unit_id is set to about.labels.key/value, target_service is set to target.application, status is set to about.labels.key/value
748201
{target_service} application on module {module_id} in chassis {chassis_number} is {status}
target_service is set to target.application, module_id is set to about.labels.key/value, chassis_number is set to about.labels.key/value, status is set to about.labels.key/value
748202
Module {module_id} in chassis {chassis_number} is leaving the cluster due to {target_service} application failure
module_id is set to about.labels.key/value, chassis_number is set to about.labels.key/value, target_service is set to target.application
748203
Module {module_id} in chassis {chassis_number} is re-joining the cluster due to a service chain application recovery
module_id is set to about.labels.key/value, chassis_number is set to about.labels.key/value
750001
Local:{src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} Received request to <message_text>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid
750002
Local:{src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username}( IKEv2)? Received a IKE_INIT_SA request
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid
750003
Local: {src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} Negotiation aborted due to ERROR:{summary}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid, summary is set to security_result.summary
750004
Local: {src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} Sending COOKIE challenge to throttle possible DoS
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid
750005
Local: {src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} (IPsec|IPSec) rekey collision detected. I am lowest nonce initiator, deleting SA with inbound SPI {spi}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid, spi is set to about.labels.key/value
750006
Local: {src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} SA UP. Reason:{summary}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid, summary is set to security_result.summary
750007
Local: {src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} SA DOWN. Reason:{summary}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid, summary is set to security_result.summary
750008
Local: {src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} SA rejected due to system resource low
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid
750009
Local:{src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{src_username} SA request rejected due to CAC limit reached: Rejection reason:{summary}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid, summary is set to security_result.summary
750010
Local:{src_ip}(:{src_port})? Remote:{dst_ip}(:{dst_port})? Username:{src_username} IKEv2 (L|l)?ocal throttle-request queue depth threshold of {threshold} reached;<message_text>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, src_username is set to principal.user.userid, threshold is set to about.labels.key/value
750011
Tunnel Rejected: Selected IKEv2 encryption algorithm \({ikev2_encry_algo}\) is not strong enough to secure proposed (IPsec|IPSEC) encryption algorithm \({ipsec_encry_algo}\)
ikev2_encry_algo is set to about.labels.key/value, ipsec_encry_algo is set to about.labels.key/value
750012
(Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} IKEv2 )?Selected IKEv2 encryption algorithm ({ikev2_encry_algo}) is not strong enough to secure proposed (IPsec|IPSEC) encryption algorithm ({ipsec_encry_algo})
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, ikev2_encry_algo is set to about.labels.key/value, ipsec_encry_algo is set to about.labels.key/value
750013
IKEv2 SA (iSPI <{initiator_spi}> rRSP <{responder_spi}>) Peer Moved: Previous <{dst_ip}>:<{prev_remote_port}>/<{src_ip}>:<{prev_local_port}>. Updated <{dst_ip1}>:<{dst_port}>/<{src_ip1}>:<{src_port}>
initiator_spi is set to about.labels.key/value, responder_spi is set to about.labels.key/value, dst_ip is set to target.ip, prev_remote_port is set to about.labels.key/value, src_ip is set to principal.ip, prev_local_port is set to about.labels.key/value, dst_ip1 is set to target.ip, dst_port is set to target.port, src_ip1 is set to principal.ip, src_port is set to principal.port
750014
Local:<{src_ip}>:<{src_port}> Remote:<{dst_ip}>(:<{dst_port}>)? Username:<{user_name}> IKEv2 Session aborted. Reason: <message_text>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
750015
Local:<{src_ip}>:<{src_port}> Remote:<{dst_ip}>(:<{dst_port}>)? Username:<{user_name}> IKEv2 deleting IPSec SA. Reason: invalid SPI notification received for SPI <message_text>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
751001
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Failed to complete Diffie-Hellman operation. Error: {summary}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, summary is set to security_result.summary
751002
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name}( IKEv2)? No pre(-)?shared key or trustpoint configured for self in tunnel group {tunnel_group}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, tunnel_group is set to target.group.group_display_name
751004
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} No remote authentication method configured for peer in tunnel group {tunnel_group}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, tunnel_group is set to target.group.group_display_name
751005
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} AnyConnect client reconnect authentication failed. Session ID: {session_id}, Error: {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, session_id is set to network.session_id, error is set to about.labels.key/value
751006
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Certificate authentication failed. Error: {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, error is set to about.labels.key/value
751007
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Configured attribute not supported for IKEv2. Attribute: {attribute}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, attribute is set to about.labels.key/value
751008
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Group={tunnel_group}, Tunnel rejected: IKEv2 not enabled in group policy
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, tunnel_group is set to target.group.group_display_name
751009
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Unable to find tunnel group for peer
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
751010
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Unable to determine (self-authentication|self auth) method. No crypto map setting or tunnel group found
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
751011
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Failed user authentication. Error: {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, error is set to about.labels.key/value
751012
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Failure occurred during Configuration Mode processing. Error: {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, error is set to about.labels.key/value
751013
Local:{src_ip}:{src_port} Remote:{dst_ip}(:{dst_port})? Username:{user_name} Failed to process Configuration Payload request for attribute {attribute_id}. Error: {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, attribute_id is set to about.labels.key/value, error is set to about.labels.key/value
751014
Local:{src_ip}:{src_port} Remote {dst_ip}(:{dst_port})? Username:{user_name} Warning Configuration Payload request for attribute {attribute_id} could not be processed. Error: {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, attribute_id is set to about.labels.key/value, error is set to about.labels.key/value
751015
Local:{src_ip}:{src_port} Remote {dst_ip}(:{dst_port})? Username:{user_name} SA request rejected by CAC. Reason: {summary}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, summary is set to security_result.summary
751016
Local:{src_ip}:{src_port} Remote {dst_ip}(:{dst_port})? Username:{user_name} L2L peer initiated a tunnel with the same outer and inner addresses. <message_text>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
751017
Local:{src_ip}:{src_port} Remote {dst_ip}(:{dst_port})? Username:{user_name} Configuration Error {error}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, error is set to about.labels.key/value
751018
Terminating the (?P<target_service>VPN) connection attempt from {attempted_group}. Reason: This connection is group locked to {locked_group}
target_service is set to target.application, attempted_group is set to about.labels.key/value, locked_group is set to about.labels.key/value
751019
Local:{src_ip} Remote:{dst_ip} Username:{user_name} Failed to obtain an {license_type} license. Maximum license limit {limit} exceeded
src_ip is set to principal.ip, dst_ip is set to target.ip, user_name is set to target.user.userid, license_type is set to about.labels.key/value, limit is set to about.labels.key/value
751020
Local:{src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{user_name} An <message_text> remote access connection failed. <message_text>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
751021
Local:{src_ip} :{src_port} Remote:{dst_ip} :{dst_port} Username:{user_name} (?P<version_protocol>IKEv1|IKEv2) with {encryption_type} encryption is not supported with this version of the AnyConnect Client. Please upgrade to the latest Anyconnect Client
version_protocol is set to network.tls.version_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, encryption_type is set to about.labels.key/value
751022
Local: {src_ip} Remote: {dst_ip} Username:{user_name} Tunnel rejected: Crypto Map Policy not found for remote traffic selector <message_text>
src_ip is set to principal.ip, dst_ip is set to target.ip, user_name is set to target.user.userid
751023
Local {src_ip} :{src_port} Remote: {dst_ip} :{dst_port} Username:{user_name} Unknown client connection
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid
751024
Local:{src_ip} Remote:{dst_ip} Username:{user_name} IKEv2 IPv6 User Filter tempipv6 configured. This setting has been deprecated, (?P<action>terminating) connection
action is set to security_result.action, src_ip is set to principal.ip, dst_ip is set to target.ip, user_name is set to target.user.userid
751025
Local:{src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{user_name} Group:{group_policy} IPv4 Address={assigned_IPv4_addr} IPv6 address={assigned_IPv6_addr} assigned to session
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, group_policy is set to about.labels.key/value, assigned_IPv4_addr is set to about.labels.key/value, assigned_IPv6_addr is set to about.labels.key/value
751026
Local: {src_ip}:{src_port} Remote: {dst_ip}:{dst_port} Username: {user_name} IKEv2 Client OS: {target_platform} Client: {client_name} {client_version}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, target_platform is set to target.platform, client_name is set to about.labels.key/value, client_version is set to about.labels.key/value
751027
Local:{src_ip}:{src_port} Remote:{dst_ip}:{dst_port} Username:{user_name} IKEv2 Received INVALID_SELECTORS Notification from peer. Peer received a packet (SPI={spi} ). The decapsulated inner packet <message_text> match the negotiated policy in the SA. Packet destination {dst_ip1}, port <message_text>, source {src_ip1}, port <message_text>, protocol {protocol}
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, spi is set to about.labels.key/value, dst_ip1 is set to target.ip, src_ip1 is set to principal.ip, protocol is set to network.ip_protocol
751028
Local:<{src_ip}:{src_port}> Remote:<{dst_ip}:{dst_port}> Username:<{user_name}> IKEv2 Overriding configured keepalive values of threshold:<{config_threshold}>/retry:<{config_retry}> to threshold:<{applied_threshold}>/retry:<{applied_retry}>
src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port, user_name is set to target.user.userid, config_threshold is set to about.labels.key/value, config_retry is set to about.labels.key/value, applied_threshold is set to about.labels.key/value, applied_retry is set to about.labels.key/value
752003, 752004
Tunnel Manager dispatching a KEY_ACQUIRE message to (?P<version_protocol>IKEv1|IKEv2).Map Tag = {map_tag}.Map Sequence Number = {sequence_number}
version_protocol is set to network.tls.version_protocol, map_, sequence_number is set to about.labels.key/value
752005
Tunnel Manager failed to dispatch a KEY_ACQUIRE message. Memory may be low.Map Tag = {map_tag}.Map Sequence Number = {sequence_number}
map_, sequence_number is set to about.labels.key/value
752006
Tunnel Manager failed to dispatch a KEY_ACQUIRE message.Probable mis-configuration of the crypto map or tunnel-group.Map Tag = {map_tag}.Map Sequence Number = {sequence_number}(, SRC Addr: {src_ip} port: {src_port} Dst Addr: {dst_ip} port: {dst_port})?
map_, sequence_number is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
752007
Tunnel Manager failed to dispatch a KEY_ACQUIRE message. Entry already in Tunnel Manager.Map Tag = {map_tag}.Map Sequence Number = {sequence_number}
map_, sequence_number is set to about.labels.key/value
752012
(?P<version_protocol>IKEv1|IKEv2) was unsuccessful at setting up a tunnel.Map Tag = {map_tag}.Map Sequence Number = {sequence_number}
version_protocol is set to network.tls.version_protocol, map_, sequence_number is set to about.labels.key/value
752013, 752014
Tunnel Manager dispatching a KEY_ACQUIRE message to (?P<version_protocol>IKEv1|IKEv2) after a failed attempt.(.)?Map Tag = {map_tag}.Map Sequence Number = {sequence_number}
version_protocol is set to network.tls.version_protocol, map_, sequence_number is set to about.labels.key/value
752015
Tunnel Manager has failed to establish an L2L SA.All configured IKE versions failed to establish the tunnel.Map Tag= {map_tag}.Map Sequence Number = {sequence_number}
map_, sequence_number is set to about.labels.key/value
752016
{version_protocol} was successful at setting up a tunnel.Map Tag = {map_tag}.Map Sequence Number = {sequence_number}
version_protocol is set to network.tls.version_protocol, map_, sequence_number is set to about.labels.key/value
752017
IKEv2 Backup L2L tunnel initiation denied on interface {interface_name} matching crypto map {crypto_map_name}, sequence number {sequence_number}. Unsupported configuration
interface_name is set to about.labels.key/value, crypto_map_name is set to about.labels.key/value, sequence_number is set to about.labels.key/value
753001
Unexpected (?P<version_protocol>IKEv2) packet received from <{dst_ip}>:<{dst_port}>. Error: <{summary}>
version_protocol is set to network.tls.version_protocol, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
767001
{inspect_name}: Dropping an unsupported <message_text> from {src_interface_name}:IP {src_ip} to {dst_interface_name}:IP {dst_ip} (fail-close)
inspect_name is set to about.labels.key/value, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
768001
QUOTA: {resource} utilization is high: requested {number_requested}, current {current_number}, warning level {warning_level}
resource is set to target.resource.name, number_requested is set to about.labels.key/value, current_number is set to about.labels.key/value, warning_level is set to about.labels.key/value
768002
QUOTA: {resource} quota exceeded: requested {number_requested}, current {current_number}, limit {resource_limit}
resource is set to target.resource.name, number_requested is set to about.labels.key/value, current_number is set to about.labels.key/value, resource_limit is set to about.labels.key/value
768003
QUOTA: management session quota exceeded for user {user_name}: {current_number} 3, user {resource_limit} 3
user_name is set to target.user.userid, current_number is set to about.labels.key/value, resource_limit is set to about.labels.key/value
768004
QUOTA: management session quota exceeded for ssh/telnet/http protocol: {current_number} 2, protocol {resource_limit} 2
current_number is set to about.labels.key/value, resource_limit is set to about.labels.key/value
769001
UPDATE: ASA image {src_file_full_path} was added to system boot list
src_file_full_path is set to src.file.full_path
769002, 769003
UPDATE: ASA image {src_file_full_path} was <message_text> to {target_file_full_path}
src_file_full_path is set to src.file.full_path, target_file_full_path is set to target.file.full_path
769004
UPDATE: ASA image {src_file_full_path} failed verification, reason: {summary}
src_file_full_path is set to src.file.full_path, summary is set to security_result.summary
769005
UPDATE: ASA image {target_file_full_path} passed image verification
target_file_full_path is set to target.file.full_path
769006
UPDATE: ASA boot system image {image_name} was not found on disk
image_name is set to about.labels.key/value
769007
UPDATE: Image version is {version_number}
version_number is set to about.labels.key/value
769009
UPDATE: Image booted {image_name} is different from boot images
image_name is set to about.labels.key/value
770001
{resource} resource allocation is more than the permitted list of {limit} for this platform. If this condition persists, the ASA will be rebooted
resource is set to target.resource.name, limit is set to about.labels.key/value
770002
{resource} resource allocation is more than the permitted {limit} for this platform. ASA will be rebooted
resource is set to target.resource.name, limit is set to about.labels.key/value
770003
{resource} resource allocation is less than the minimum requirement of {value} for this platform. If this condition persists, performance will be lower than normal
resource is set to target.resource.name, value is set to about.labels.key/value
771002
CLOCK: System clock set, source: {source} , IP {dst_ip} , before: {before_time} , after: {after_time}
source is set to about.labels.key/value, dst_ip is set to target.ip, before_time is set to about.labels.key/value, after_time is set to about.labels.key/value
771001
CLOCK: System clock set, source: {source} , before: {before_time} , after: {after_time}
source is set to about.labels.key/value, before_time is set to about.labels.key/value, after_time is set to about.labels.key/value
772002
PASSWORD: console login warning, user {user_name} , cause: {summary}
user_name is set to target.user.userid, summary is set to security_result.summary
772003, 772004
PASSWORD: {session_type} login failed, user {user_name} , IP {src_ip} , cause: {summary}
session_type is set to about.labels.key/value, user_name is set to target.user.userid, src_ip is set to principal.ip, summary is set to security_result.summary, if sysloghost is a valid IP, it's set to target.ip; otherwise, it's set to target.hostname.
772005, 772006
{action_details}: user {user_name} {action} authentication
action_details is set to security_result.action_details, user_name is set to target.user.userid, action is set to security_result.action
774002
POST: error {error}, func {function} , engine {target_service} , algorithm {algorithm} , mode {mode} , dir {dir} , key len {length}
error is set to about.labels.key/value, function is set to about.labels.key/value, target_service is set to target.application, algorithm is set to about.labels.key/value, mode is set to about.labels.key/value, dir is set to about.labels.key/value, length is set to about.labels.key/value
775001
(?P<target_service>Scansafe): {protocol} connection {session_id} from {interface_name}:{src_ip}(/{src_port})? (idfw_user )] to {interface_name_}:{dst_ip}/{dst_port} redirected to {primary_server_interface_name} :{dst_ip1}
target_service is set to target.application, protocol is set to network.ip_protocol, session_id is set to network.session_id, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, interface_name_ is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, primary_server_interface_name is set to about.labels.key/value, dst_ip1 is set to target.ip
775002
Reason - {protocol} connection {session_id} from {interface_name}:{src_ip}(/{src_port})? (idfw_user )] to {interface_name_}:{dst_ip}/{dst_port} is action locally
protocol is set to network.ip_protocol, session_id is set to network.session_id, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, interface_name_ is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
775003
(?P<target_service>Scansafe):{protocol} connection {session_id} from {interface_name} :{src_ip}(/{src_port})? (idfw_user )] to {interface_name_} :{dst_ip}/{dst_port} is whitelisted
target_service is set to target.application, protocol is set to network.ip_protocol, session_id is set to network.session_id, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, interface_name_ is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
775004, 775005
(?P<target_service>Scansafe): Primary server {dst_ip} is <message_text>
target_service is set to target.application, dst_ip is set to target.ip
775006
Primary server {primary_server_interface_name} :{dst_ip} is not reachable and backup server {backup_server_interface_name} :{dst_ip1} <message_text>
primary_server_interface_name is set to about.labels.key/value, dst_ip is set to target.ip, backup_server_interface_name is set to about.labels.key/value, dst_ip1 is set to target.ip
775007
(?P<target_service>Scansafe): Primary {primary_server_interface_name} :{dst_ip} and backup {backup_server_interface_name} :{dst_ip1} <message_text>
target_service is set to target.application, primary_server_interface_name is set to about.labels.key/value, dst_ip is set to target.ip, backup_server_interface_name is set to about.labels.key/value, dst_ip1 is set to target.ip
776001
CTS SXP: Configured source IP {src_ip} {error}
src_ip is set to principal.ip, error is set to about.labels.key/value
776002
CTS SXP: Invalid message from peer {src_ip} : {error}
src_ip is set to principal.ip, error is set to about.labels.key/value
776003
CTS SXP: Connection with peer {src_ip} failed: {error}
src_ip is set to principal.ip, error is set to about.labels.key/value
776005
CTS SXP: Binding {dst_ip} - {sg_name} from {src_ip} instance {connection_instance_num}{error}
dst_ip is set to target.ip, sg_name is set to about.labels.key/value, src_ip is set to principal.ip, connection_instance_num is set to about.labels.key/value, error is set to about.labels.key/value
776006
CTS SXP: Internal error: {error}
error is set to about.labels.key/value
776007
CTS SXP: Connection with peer {src_ip} (instance {connection_instance_num}) state changed from {original_state} to {final_state}
src_ip is set to principal.ip, connection_instance_num is set to about.labels.key/value, original_state is set to about.labels.key/value, final_state is set to about.labels.key/value
776008
CTS SXP: Connection with {src_ip} (instance {connection_instance_num}) state changed from {original_state} to {final_state}
src_ip is set to principal.ip, connection_instance_num is set to about.labels.key/value, original_state is set to about.labels.key/value, final_state is set to about.labels.key/value
776010
CTS SXP: SXP default source IP is changed {src_ip} {src_ip1}
src_ip is set to principal.ip, src_ip1 is set to principal.ip
776020
CTS SXP: Unable to locate egress interface to peer {dst_ip},
dst_ip is set to target.ip
776201
CTS PAC: CTS PAC for Server {dst_ip}, A-ID {issuer} will expire in {days_left} days
dst_ip is set to target.ip, issuer is set to about.labels.key/value, days_left is set to about.labels.key/value
776202
CTS PAC for Server {dst_ip}, A-ID {issuer} has expired
dst_ip is set to target.ip, issuer is set to about.labels.key/value
776203
Unable to retrieve CTS Environment data due to: {summary}
summary is set to security_result.summary
776251
CTS SGT-MAP: Binding {dst_ip} - {sg_name} from {source_name} added to binding manager
dst_ip is set to target.ip, sg_name is set to about.labels.key/value, source_name is set to about.labels.key/value
776252
CTS SGT-MAP: CTS SGT-MAP: Binding {dst_ip} - {sg_name} from {source_name} deleted from binding manager.
dst_ip is set to target.ip, sg_name is set to about.labels.key/value, source_name is set to about.labels.key/value
776253
CTS SGT-MAP: Binding {dst_ip} - {new_sg_name} from {source_name} changed from old sgt: {old_sg_name} from old source {old_source_name}
dst_ip is set to target.ip, new_sg_name is set to about.labels.key/value, source_name is set to about.labels.key/value, old_sg_name is set to about.labels.key/value, old_source_name is set to about.labels.key/value
776254
CTS SGT-MAP: Binding manager unable to {action_details} Binding {dst_ip} - {sg_name} from {source_name}
action_details is set to security_result.action_details, dst_ip is set to target.ip, sg_name is set to about.labels.key/value, source_name is set to about.labels.key/value
776301
CTS Policy: Security-group tag {sgt} is mapped to security-group name {sg_name}
sgt is set to about.labels.key/value, sg_name is set to about.labels.key/value
776302
CTS Policy: Unknown security-group tag {sgt} referenced in policies
sgt is set to about.labels.key/value
776303
CTS Policy: Security-group name {sg_name} is resolved to security-group tag {sgt}
sg_name is set to about.labels.key/value, sgt is set to about.labels.key/value
776304
CTS Policy: Unresolved security-group name {sg_name} referenced, policies based on this name will be inactive
sg_name is set to about.labels.key/value
776307
CTS Policy: Security-group name for security-group tag {sgt} renamed from {old_sg_name} to {new_sg_name}
sgt is set to about.labels.key/value, old_sg_name is set to about.labels.key/value, new_sg_name is set to about.labels.key/value
776308
CTS Policy: Previously unknown security-group tag {sgt} is now mapped to security-group name {sg_name}
sgt is set to about.labels.key/value, sg_name is set to about.labels.key/value
776309
CTS Policy: Previously known security-group tag {sgt} is now unknown
sgt is set to about.labels.key/value
776310
CTS Policy: Security-group name {sg_name} remapped from security-group tag {old_sgt} to {new_sgt}
sg_name is set to about.labels.key/value, old_sgt is set to about.labels.key/value, new_sgt is set to about.labels.key/value
776311
CTS Policy: Previously unresolved security-group name {sg_name} is now resolved to security-group tag {sgt}
sg_name is set to about.labels.key/value, sgt is set to about.labels.key/value
776312
CTS Policy: Previously resolved security-group name {sg_name} is now unresolved, policies based on this name will be deactivated
sg_name is set to about.labels.key/value
776313
CTS Policy: Failure to update policies for security-group {sg_name}-{sgt}
sg_name is set to about.labels.key/value, sgt is set to about.labels.key/value
778001
VXLAN: Invalid VXLAN segment-id {segment_id} for {protocol} from {src_interface_name}:({src_ip}/{src_port}) to {dst_interface_name}:({dst_ip}/{dst_port})
segment_id is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
778002
VXLAN: There is no VNI interface for segment-id {segment_id}
segment_id is set to about.labels.key/value
778003
VXLAN: Invalid VXLAN segment-id {segment_id} for {protocol} from {src_interface_name}:({src_ip}//{src_port}) to {dst_interface_name}:({dst_ip}//{dst_port}) in FP
segment_id is set to about.labels.key/value, protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
778004
VXLAN: Invalid VXLAN header for {protocol} from {src_interface_name}:({src_ip}/{src_port}) to {dst_interface_name}:({dst_ip}/{dst_port}) in FP
protocol is set to network.ip_protocol, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
778005
VXLAN: Packet with VXLAN segment-id {segment_id} from {interface_name} is denied by FP L2 check
segment_id is set to about.labels.key/value, interface_name is set to about.labels.key/value
778006
VXLAN: Invalid VXLAN UDP checksum from {src_interface_name}:({src_ip}/{src_port}) to {dst_interface_name}:({dst_ip}/{dst_port}) in FP
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
778007
VXLAN: Packet from {interface_name} :{src_ip}(/{src_port})? to {dst_ip}/{dst_port} was discarded due to invalid NVE peer
interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
779001
STS: Out-tag lookup failed for in-tag {segment_id} of {protocol} from {interface_name} :{src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
segment_id is set to about.labels.key/value, protocol is set to network.ip_protocol, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
779002
STS: STS and NAT locate different egress interface for segment-id {segment_id}, {protocol} from {interface_name} :{src_ip}(/{src_port})? to {dst_ip}(/{dst_port})?
segment_id is set to about.labels.key/value, protocol is set to network.ip_protocol, interface_name is set to about.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
779003, 779004
STS: Failed to <message_text> tag-switching table - {summary}
summary is set to security_result.summary
779005
STS: Failed to parse tag-switching request from http - {summary}
summary is set to security_result.summary
779006
STS: Failed to save tag-switching table to flash - {summary}
summary is set to security_result.summary
779007
STS: Failed to replicate tag-switching table to peer - {summary}
summary is set to security_result.summary
780001, 780002, 780003, 780004
RULE ENGINE: <message_text> compilation for <message_text> transaction - {summary}
summary is set to security_result.summary
785001
Clustering: Ownership for existing flow from (<|){src_interface_name}(>|):(<|){src_ip}(>|)/(<|){src_port}(>|) to (<|){dst_interface_name}(>|):(<|){dst_ip}(>|)/(<|){dst_port}(>|) moved from unit (<|){old_owner_unit_id}(>|) at site (<|){old_site_id}(>|) to (<|){new_owner_unit_id}(>|) at site <message_text> due to {summary}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, old_owner_unit_id is set to about.labels.key/value, old_site_id is set to about.labels.key/value, new_owner_unit_id is set to about.labels.key/value, summary is set to security_result.summary
802005
IP {src_ip} Received MDM request {summary}
src_ip is set to principal.ip, summary is set to security_result.summary
802006
IP {src_ip} MDM request details has been rejected: {summary}
src_ip is set to principal.ip, summary is set to security_result.summary
805001
Flow offloaded: connection {session_id} {src_interface_name}:{src_ip}/{src_port} (<message_text>) {dst_interface_name}:{dst_ip}/{dst_port} <message_text>
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
805,002,805,003
Flow is no longer offloaded: connection {session_id} {src_interface_name}:{src_ip}/{src_port} (<message_text>) {dst_interface_name}:{dst_ip}/{dst_port} <message_text>
session_id is set to network.session_id, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
840001
Failed to create the backup for an IKEv2 session (<|){src_ip}(>|), (<|){dst_ip}(>|)
src_ip is set to principal.ip, dst_ip is set to target.ip
850001
SNORT ID ({instance_or_process_id}) Automatic-Application-Bypass due to delay of (<|){timeout_delay}(>|)ms (threshold (<|){threshold}(>|)ms) with {info}
instance_or_process_id is set to about.labels.key/value, timeout_delay is set to about.labels.key/value, threshold is set to about.labels.key/value, info is set to about.labels.key/value
850002
SNORT ID ({instance_or_process_id}) Automatic-Application-Bypass due to SNORT not responding to traffics for (<|){delay}(>|)ms(threshold (<|){threshold}(>|)ms)
instance_or_process_id is set to about.labels.key/value, delay is set to about.labels.key/value, threshold is set to about.labels.key/value
8300001
VPN session redistribution {action_details}
action_details is set to security_result.action_details
8300002
Moved (<|){active_sessions}(>|) sessions to {member_name}
active_sessions is set to about.labels.key/value, member_name is set to about.labels.key/value
8300003
Failed to send session redistribution message to {member_name}
member_name is set to about.labels.key/value
8300004
(<|){action_details}(>|) request to move (<|){active_sessions}(>|) sessions from (<|){member_name}(>|) to {member_name_2}
action_details is set to security_result.action_details, active_sessions is set to about.labels.key/value, member_name is set to about.labels.key/value, member_name_2 is set to about.labels.key/value
8300005
Failed to receive session move response from {member_name}
member_name is set to about.labels.key/value
108006
Detected ESMTP size violation from {src_interface_name}:{src_ip}(|{src_port})? to {dst_interface_name}:{dst_ip}(|{dst_port})?;{summary}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, summary is set to security_result.summary
111009
User {user_name} executed cmd:{command}
user_name is set to target.user.userid, command is set to target.process.command_line
113028
Extraction of username from VPN client certificate has {status}. Request {request_id}]
status is set to about.labels.key/value, request_id is set to about.labels.key/value
304005
URL Server {dst_ip} <message_text> <message_text> URL {url}
dst_ip is set to target.ip, url is set to about.labels.key/value
333004, 333005, 333006, 333007, 333008
{protocol}-SQ response .* - context:{session_id}
protocol is set to network.ip_protocol, session_id is set to network.session_id
335007
NAC Default ACL not configured - {dst_ip}
dst_ip is set to target.ip
419003
Cleared {protocol} urgent flag from {dst_interface_name}:{src_ip}/{src_port} to {src_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, dst_interface_name is set to target.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, src_interface_name is set to principal.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
421004
Failed to inject {protocol} packet from {src_ip}/{src_port} to {dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_ip is set to target.ip, dst_port is set to target.port
609001, 609002
(?P<action>Built|Teardown) local-host {src_interface_name}:{src_ip}( duration {duration})?
action is set to security_result.action, src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, duration is set to network.session_duration
702307
(?P<category>IPSEC): An (?P<direction>inbound|outbound|INBOUND|OUTBOUND|Inbound|Outbound) {tunnel_type} SA (SPI={spi}) between {src_ip} and {dst_ip} ({src_fwuser}) is rekeying due to data rollover
category is set to security_result.category_details, direction is set to network.direction, tunnel_type is set to about.labels.key/value, spi is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip, src_fwuser is set to principal.user.userid/principal.labels.key/value
703001
H.225 message received from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port} is using an unsupported {version_number}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, version_number is set to about.labels.key/value
703002
Received H.225 Release Complete with newConnectionNeeded for {src_interface_name}:{src_ip} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
703008
Allowing early-message:<message_text>from {src_interface_name}:{src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_interface_name is set to principal.labels.key/value, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
709001
FO replication failed: cmd={command} returned={return_code}
command is set to target.process.command_line, return_code is set to security_result.description
709002
FO unreplicable: cmd={command}
command is set to target.process.command_line
710001
(?P<protocol>TCP) access requested from {src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
710002
(?P<protocol>TCP|UDP) access permitted from {src_ip}/{src_port} to {dst_interface_name}:{dst_ip}(/{dst_port})?
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
710004
(?P<protocol>TCP) connection limit exceeded from {src_ip}/{src_port} to {input_interface}:{dst_ip}/{dst_port} (current connections/connection limit = {current_connections}/{connection_limit})
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, input_interface is set to about.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port, current_connections is set to about.labels.key/value, connection_limit is set to about.labels.key/value
710005
(?P<protocol>TCP|UDP|SCTP) request discarded from {src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
710006
{protocol} request discarded from {src_ip} to {dst_interface_name}:{dst_ip}
protocol is set to network.ip_protocol, src_ip is set to principal.ip, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip
710007
NAT-T keepalive received from {src_ip}/{src_port} to {dst_interface_name}:{dst_ip}/{dst_port}
src_ip is set to principal.ip, src_port is set to principal.port, dst_interface_name is set to target.labels.key/value, dst_ip is set to target.ip, dst_port is set to target.port
711003
Unknown/Invalid interface identifier({vpifnum}) detected
vpifnum is set to about.labels.key/value
711006
CPU profiling has started for {number_of_sample} samples. Reason: {summary}
number_of_sample is set to about.labels.key/value, summary is set to security_result.summary
713024
Group {group_name}, IP {src_ip}, Received local Proxy Host data in ID Payload: Address {dst_ip}, Protocol {protocol}, Port {dst_port}
group_name is set to target.user.group_identifiers, src_ip is set to principal.ip, dst_ip is set to target.ip, protocol is set to network.ip_protocol, dst_port is set to target.port
713025
Received remote Proxy Host data in ID Payload: Address {dst_ip}, Protocol {protocol}, Port {dst_port}
dst_ip is set to target.ip, protocol is set to network.ip_protocol, dst_port is set to target.port
713028
Received local Proxy Range data in ID Payload: Addresses {dst_ip}- {dst_ip1}, Protocol {protocol}, Port {dst_port}
dst_ip is set to target.ip, dst_ip1 is set to target.ip, protocol is set to network.ip_protocol, dst_port is set to target.port
713029
Received remote Proxy Range data in ID Payload: Addresses {dst_ip}-{dst_ip}, Protocol {protocol}, Port {dst_port}
dst_ip is set to target.ip, dst_ip is set to target.ip, protocol is set to network.ip_protocol, dst_port is set to target.port
713034
Received local IP Proxy Subnet data in ID Payload: Address {dst_ip}, Mask {netmask}, Protocol {protocol}, Port {dst_port}
dst_ip is set to target.ip, netmask is set to about.labels.key/value, protocol is set to network.ip_protocol, dst_port is set to target.port
713035
Group {group_name} IP {dst_ip} Received remote IP Proxy Subnet data in ID Payload: Address {dst_ip1}, Mask {netmask}, Protocol {protocol}, Port {dst_port}
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, dst_ip1 is set to target.ip, netmask is set to about.labels.key/value, protocol is set to network.ip_protocol, dst_port is set to target.port
713039
Send failure: Bytes ({sent_bytes}), Peer: {dst_ip}
sent_bytes is set to network.sent_bytes, dst_ip is set to target.ip
713040
Could not find connection entry and can not encrypt: msgid {message_id}
message_id is set to about.labels.key/value
713052
User ({user_name}) authenticated.
user_name is set to target.user.userid
713066
IKE Remote Peer configured for SA: {sa_name}
sa_name is set to about.labels.key/value
713099
Tunnel Rejected: Received NONCE length {nonce_length} is out of range!
nonce_length is set to about.labels.key/value
713104
Attempt to get Phase 1 ID data failed while {hash_computation}
hash_computation is set to about.labels.key/value
713113
Deleting IKE SA with associated (IPsec|IPSec) connection entries. IKE peer: {dst_ip}, SA address: {internal_sa_address}, tunnel count: {tunnel_count}
dst_ip is set to target.ip, internal_sa_address is set to about.labels.key/value, tunnel_count is set to about.labels.key/value
713114
Connection entry ({src_ip}) points to IKE SA ({src_ip1}) for peer {dst_ip}, but cookies don't match
src_ip is set to principal.ip, src_ip1 is set to principal.ip, dst_ip is set to target.ip
713117
Received Invalid SPI notify (SPI {spi_value})!
spi_value is set to about.labels.key/value
713121
Keep-alive type for this connection: {keepalive_type}
keepalive_type is set to about.labels.key/value
713143
Processing firewall record. Vendor: {vendor_id}, Product: {product_id}, Caps: {capability_value}, Version Number: {version_number}, Version String: {version_text}
vendor_id is set to about.labels.key/value, product_id is set to about.labels.key/value, capability_value is set to about.labels.key/value, version_number is set to about.labels.key/value, version_text is set to about.labels.key/value
713160
Remote user (session Id -{session_id}) has been granted access by the Firewall Server
session_id is set to network.session_id
713169
IKE Received delete for rekeyed SA IKE peer: {dst_ip}, SA address: {internal_sa_address}, tunnelCnt: {tunnel_count}
dst_ip is set to target.ip, internal_sa_address is set to about.labels.key/value, tunnel_count is set to about.labels.key/value
713170
Group {group_name} IP {dst_ip} IKE Received delete for rekeyed centry IKE peer: {dst_ip1}, centry address: {internal_address}, msgid: {message_id}
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, dst_ip1 is set to target.ip, internal_address is set to about.labels.key/value, message_id is set to about.labels.key/value
713187
Tunnel Rejected: IKE peer does not match remote peer as defined in L2L policy IKE peer address: {dst_ip}, Remote peer address: {dst_ip1}
dst_ip is set to target.ip, dst_ip1 is set to target.ip
713190
Got bad refCnt ({ref_count_value}) assigning {dst_ip1} ({dst_ip})
ref_count_value is set to about.labels.key/value, dst_ip1 is set to target.ip, dst_ip is set to target.ip
713204
Adding static route for client address: {dst_ip}
dst_ip is set to target.ip
713221
Static Crypto Map check, checking map = {crypto_map_tag}, seq = {seq_number}.*
crypto_map_, seq_number is set to about.labels.key/value
713222
Group( =)? {group_name}(,)?( Username( =)? {user_name}(,)?)? IP( =)? {dst_ip1}(,)? Static Crypto Map check, map = {crypto_map_tag}, seq = {seq_number}, ACL does not match proxy IDs src:{src_ip} dst:{dst_ip}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip1 is set to target.ip, crypto_map_, seq_number is set to about.labels.key/value, src_ip is set to principal.ip, dst_ip is set to target.ip
713223
Static Crypto Map check, map = {crypto_map_tag}, seq = {seq_number}, no ACL configured
crypto_map_, seq_number is set to about.labels.key/value
713225
(Group = {group_name}, IP = {dst_ip}, )?(IKEv1], )?Static Crypto Map check, map {crypto_map_tag}, seq = {seq_number} is a successful match
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, crypto_map_, seq_number is set to about.labels.key/value
713233
(VPN-<message_text>) Remote network ({dst_ip}) validated for network extension mode
dst_ip is set to target.ip
713234
(VPN-<message_text>) Remote network ({dst_ip}) from network extension mode client mismatches AAA configuration ({aaa_ip})
dst_ip is set to target.ip, aaa_ip is set to about.labels.key/value
713263
Received local IP Proxy Subnet data in ID Payload: Address {dst_ip}, Mask/{netmask}, Protocol {protocol}, Port {port}
dst_ip is set to target.ip, netmask is set to about.labels.key/value, protocol is set to network.ip_protocol, port is set to about.labels.key/value
713264
Received (local IP|remote IP) Proxy Subnet data in ID Payload: Address {dst_ip}, Mask/{netmask}, Protocol {protocol}, Port {port}
dst_ip is set to target.ip, netmask is set to about.labels.key/value, protocol is set to network.ip_protocol, port is set to about.labels.key/value
713273
(Deleting|Could not delete) static route for client address: {dst_ip} {dst_ip1} address of client whose route is being removed
dst_ip is set to target.ip, dst_ip1 is set to target.ip
714002
IKE Initiator starting QM: msg id = {message_id}
message_id is set to about.labels.key/value
714003
IKE Responder starting QM: msg id = {message_id}
message_id is set to about.labels.key/value
714006
IKE Initiator sending <message_text> QM pkt: msg id = {message_id}
message_id is set to about.labels.key/value
714005
IKE Responder sending 2nd QM pkt: msg id = {message_id}
message_id is set to about.labels.key/value
715004
subroutine {subroutine_name} Send failure: RetCode ({return_code})
subroutine_name is set to about.labels.key/value, return_code is set to security_result.description
715005
subroutine {subroutine_name} Bad message code: Code ({return_code})
subroutine_name is set to about.labels.key/value, return_code is set to security_result.description
715006
IKE got SPI from key engine: SPI ={spi_value}
spi_value is set to about.labels.key/value
715007
IKE got a KEY_ADD msg for SA: SPI ={spi_value}
spi_value is set to about.labels.key/value
715008
Could not delete SA {internal_sa_address}, refCnt = {ref_cnt}, caller = {calling_subroutine_address}
internal_sa_address is set to about.labels.key/value, ref_cnt is set to about.labels.key/value, calling_subroutine_address is set to about.labels.key/value
715009
IKE Deleting SA: Remote Proxy {src_ip}, Local Proxy {src_ip1}
src_ip is set to principal.ip, src_ip1 is set to principal.ip
715013
Tunnel negotiation in progress for destination {dst_ip}, discarding data
dst_ip is set to target.ip
715018
IP Range type id was loaded: Direction {ipsec_direction}, From: {from}, Through: {through}
ipsec_direction is set to about.labels.key/value, from is set to about.labels.key/value, through is set to about.labels.key/value
715019
Group {group_name} Username {user_name} IP {dst_ip} IKEGetUserAttributes: Attribute name ={attribute_name}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, attribute_name is set to about.labels.key/value
715020
construct_cfg_set: Attribute name ={attribute_name}
attribute_name is set to about.labels.key/value
715027, 715028
(IP = {dst_ip},)?<message_text>SA Proposal {chosen_proposal}, Transform {chosen_transform} acceptableMatches global <message_text> entry {crypto_map_index}
dst_ip is set to target.ip, chosen_proposal is set to about.labels.key/value, chosen_transform is set to about.labels.key/value, crypto_map_index is set to about.labels.key/value
715031
Obtained IP addr ({src_ip}) prior to initiating Mode Cfg (XAuth {x_auth})
src_ip is set to principal.ip, x_auth is set to about.labels.key/value
715032
Sending subnet mask ({subnet_mask}) to remote client
subnet_mask is set to about.labels.key/value
715033
Processing CONNECTED notify (MsgId {message_id})
message_id is set to about.labels.key/value
715035
Starting IOS keepalive monitor: seconds {seconds}
seconds is set to about.labels.key/value
715036
Sending keep-alive of type {notify_type} (seq number {seq_number})
notify_type is set to about.labels.key/value, seq_number is set to about.labels.key/value
715037
Unknown IOS Vendor ID version: {cisco_ios_version}
cisco_ios_version is set to about.labels.key/value
715038
{spoof_action} {spoofing_info} Vendor ID payload (version: {cisco_ios_version}, capabilities: {capabilities})
spoof_action is set to about.labels.key/value, spoofing_info is set to about.labels.key/value, cisco_ios_version is set to about.labels.key/value, capabilities is set to about.labels.key/value
715040
Deleting active auth handle during SA deletion: handle = {internal_authentication_handle}
internal_authentication_handle is set to about.labels.key/value
715041
Received keep-alive of type {keepalive_type}, not the negotiated type
keepalive_type is set to about.labels.key/value
715042
IKE received response of type {failure_type} to a request from the {dst_ip} utility
failure_type is set to about.labels.key/value, dst_ip is set to target.ip
715046
(Group = {group_name},)?(Username = {user_name},)?IP = {dst_ip}, constructing {payload_description} payload
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, payload_description is set to about.labels.key/value
715047
processing {payload_description} payload
payload_description is set to about.labels.key/value
715051
Received unexpected TLV type {tlv_type} while processing FWTYPE ModeCfg Reply
tlv_type is set to about.labels.key/value
715053
MODE_CFG: Received request for {info}
info is set to about.labels.key/value
715054
MODE_CFG: Received {attribute_name} reply: {summary}
attribute_name is set to about.labels.key/value, summary is set to security_result.summary
715060
Dropped received IKE fragment. Reason: {summary}
summary is set to security_result.summary
715064
IKE Peer included IKE fragmentation capability flags: Main Mode: {main_mode} Aggressive Mode: {aggressive_mode}
main_mode is set to about.labels.key/value, aggressive_mode is set to about.labels.key/value
715065
IKE {state_machine} {subtype} FSM error history (struct {data_structure_address}) {state_name},
state_machine is set to about.labels.key/value, subtype is set to about.labels.key/value, data_structure_address is set to about.labels.key/value, state_name is set to about.labels.key/value
715068
QM IsRekeyed: duplicate sa found by {address}, deleting old sa
address is set to about.labels.key/value
715069
Invalid ESP SPI size of {spi_size}
spi_size is set to about.labels.key/value
715070
Invalid IPComp SPI size of {spi_size}
spi_size is set to about.labels.key/value
715072
Received proposal with unknown protocol ID {version_protocol}
version_protocol is set to network.tls.version_protocol
715074
Could not retrieve authentication attributes for peer {dst_ip}
dst_ip is set to target.ip
715075
Group = {group_name}, IP = {dst_ip}(,)? Received keep-alive of type {message_type}(seq number {seq_number})
group_name is set to target.user.group_identifiers, dst_ip is set to target.ip, message_type is set to about.labels.key/value, seq_number is set to about.labels.key/value
715078
Received {attribute} LAM attribute
attribute is set to about.labels.key/value
716010
Group {group_name} User {user_name} Browse network
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid
716011
Group {group_name} User {user_name} Browse domain {domain_name}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, domain_name is set to about.labels.key/value
716012, 716019, 716020
Group {group_name} User {user_name} (Create|Remove|Browse) directory {directory}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, directory is set to about.labels.key/value
716013, 716014
Group {group_name} User {user_name} (Close|View|Remove) file {target_file_full_path}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, target_file_full_path is set to target.file.full_path
716016
Group {group_name} User {user_name} Rename file {old_filename} to {new_filename}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, old_filename is set to about.labels.key/value, new_filename is set to about.labels.key/value
716017, 716018
Group {group_name} User {user_name} (Create|Modify) file {target_file_full_path}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, target_file_full_path is set to target.file.full_path
716021
File access (?P<action>DENIED), {target_file_full_path}
action is set to security_result.action, target_file_full_path is set to target.file.full_path
716024
Group {group_name} User {user_name} Unable to browse the network.Error:{summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, summary is set to security_result.summary
716025
Group {group_name} User {user_name} Unable to browse domain {domain_name}. Error:{summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, domain_name is set to about.labels.key/value, summary is set to security_result.summary
716026
Group {group_name} User {user_name} Unable to browse directory {directory}. Error:{summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, directory is set to about.labels.key/value, summary is set to security_result.summary
716027, 716028, 716029, 716030
Group {group_name} User {user_name} Unable to (?P<action_details>view|remove|rename|modify|create) file {target_file_full_path}. Error:{summary}
action_details is set to security_result.action_details, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, target_file_full_path is set to target.file.full_path, summary is set to security_result.summary
716031
Group {group_name} User {user_name} Unable to (?P<action_details>view|remove|rename|modify|create) file {target_file_full_path}. Error:{summary}
action_details is set to security_result.action_details, group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, target_file_full_path is set to target.file.full_path, summary is set to security_result.summary
716032
Group {group_name} User {user_name} Unable to (create|remove) folder {folder}. Error:{summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, folder is set to about.labels.key/value, summary is set to security_result.summary
716033
Group {group_name} User {user_name} Unable to (create|remove) folder {folder}. Error:{summary}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, folder is set to about.labels.key/value, summary is set to security_result.summary
716034
Group {group_name} User {user_name} Unable to (write to|read) file {target_file_full_path}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, target_file_full_path is set to target.file.full_path
716035
Group {group_name} User {user_name} Unable to (write to|read) file {target_file_full_path}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, target_file_full_path is set to target.file.full_path
716036
Group {group_name} User <message_text> File Access: User {user_name} logged into the {dst_ip} server
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716037
Group {group_name} User <message_text> File Access: User {user_name} failed to login into the {dst_ip} server
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip
716603
Received {received_kb} KB Hostscan data from IP (<)?{src_ip}(>)?
received_kb is set to about.labels.key/value, src_ip is set to principal.ip
722029
Group {group_name} User {user_name} IP {dst_ip} SVC Session Termination: Conns: {number_of_connections}, DPD Conns: {dpd_conns}, Comp resets: {compression_resets}, Dcmp resets: {decompression_resets}
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, number_of_connections is set to about.labels.key/value, dpd_conns is set to about.labels.key/value, compression_resets is set to about.labels.key/value, decompression_resets is set to about.labels.key/value
722030, 722031
Group {group_name} User {user_name} IP {dst_ip} SVC Session Termination: <message_text>: {received_bytes}(+{ctrl_bytes}) bytes, {data_pkts}(+{ctrl_pkts}) packets, {drop_pkts} drops
group_name is set to target.user.group_identifiers, user_name is set to target.user.userid, dst_ip is set to target.ip, received_bytes is set to network.received_bytes, ctrl_bytesis set to about.labels.key/value, data_pkts is set to about.labels.key/value, drop_pkts is set to about.labels.key/value
317078
(Deleted|Added) {protocol} route {dst_ip} {subnet_mask} via {gateway_address} <message_text> on <message_text>
protocol is set to network.ip_protocol, dst_ip is set to target.ip, gateway_address is set to about.labels.key/value, subnet_mask is set to about.labels.key/value
302037
Built (?P<direction>inbound|outbound) IPINIP connection {session_id} from {outside_interface}:{outside_ip}/{outside_mapped_ip}\s*(?:{outside_idfw_user_new})? to {inside_interface_name}:{inside_ip}/{inside_mapped_ip}\s*((({inside_idfw_user_new})?\s*(\[\({test_user}\)\]))|(({inside_idfw_user_new})$))
direction is set to network.direction, conn_id is set to network.session_id, outside_interface is set to additional.fields[outside_interface], outside_idfw_user is set to principal.user.userid, inside_interface_name is set to additional.fields[inside_interface_name], inside_idfw_user is set to target.user.userid, if direction is inbound then outside_ip, outside_mapped_ip, inside_ip and inside_mapped_ip raw log fields is mapped to principal.ip, principal.nat_ip, target.ip and target.nat_ip UDM fields respectively else outside_ip, outside_mapped_ip, inside_ip and inside_mapped_ip raw log fields is mapped to target.ip, target.nat_ip, principal.ip and principal.nat_ip UDM fields respectively.
302037
Built (?P<direction>inbound|outbound) IPINIP connection {session_id} from {outside_interface}:{outside_ip}/{outside_port}\s*(?:{outside_idfw_user_new})? to {inside_interface_name}:{inside_ip}/{inside_port}\s*((({inside_idfw_user_new})?\s*(\[\({test_user}\)\]))|(({inside_idfw_user_new})$))
direction is set to network.direction, conn_id is set to network.session_id, outside_interface is set to additional.fields[outside_interface], outside_port is set to principal.port, outside_idfw_user is set to principal.user.userid, inside_interface_name is set to additional.fields[inside_interface_name], inside_port is set to target.port, inside_idfw_user is set to target.user.userid, if direction is inbound then outside_ip and inside_ip raw log fields is mapped to principal.ip and target.ip UDM fields respectively else outside_ip and inside_ip raw log fields is mapped to target.ip and principal.ip UDM fields respectively.
Field mapping reference: Message IDs to UDM event type
The following table lists the Cisco message IDs and the corresponding UDM event types:
Message IDs
UDM event type
"722053", "725001", "725002", "725003", "725004", "725005", "725007", "725016", "726001", "750001", "750002", "750003", "750004", "750005", "750006", "750007", "750008", "750009", "750010", "750014", "750015", "751001", "751002", "751004", "751005", "751006", "751007", "751008", "751009", "751010", "751011", "751012", "751013", "751014", "751015", "751016", "751017", "751020", "751021", "751022", "751023", "751024", "751025", "751026", "751027", "751028", "753001", "775001", "775002", "775003", "106001", "106002", "106006", "106007", "106010", "106011", "106012", "106013", "106014", "106015", "106016", "106017", "106018", "106020", "106021", "106022", "106023", "106025", "106026", "106027", "106100", "106102", "108002", "108004", "108007", "109001", "109002", "109003", "109005", "109007", "109008", "109010", "109023", "109024", "109025", "109028", "109034", "109039", "110002", "110003", "110004", "113042", "201003", "201010", "201011", "201012", "202005", "202010", "210005", "210007", "210008", "210010", "212004", "212006", "302003", "302004", "302012", "302017", "302018", "302020", "302021", "302022", "302024", "302026", "302027", "302033", "302034", "302035", "302036", "302303", "302305", "302306", "302311", "313004", "304001", "304002", "305005", "305006", "305009", "305010", "305011", "305012", "305013", "305014", "305016", "305017", "305018", "313005", "313008", "313009", "314001", "314002", "322004", "324000", "324001", "324002", "324003", "324004", "324005", "324007", "331001", "331002", "332003", "334001", "334002", "334003", "334004", "334005", "334006", "334007", "334008", "334009", "335001", "335002", "335003", "335004", "335005", "335006", "335008", "335009", "335012", "337000", "337001", "337005", "338001", "338002", "338003", "338004", "338005", "338006", "338007", "338008", "338101", "338102", "338103", "338104", "338201", "338202", "338203", "338204", "338301", "340001", "340002", "400000", "400001", "400002", "400003", "400004", "400005", "400006", "400007", "400008", "400009", "400010", "400011", "400012", "400013", "400014", "400015", "400016", "400017", "400018", "400019", "400020", "400021", "400022", "400023", "400024", "400025", "400026", "400027", "400028", "400029", "400030", "400031", "400032", "400033", "400034", "400035", "400036", "400037", "400038", "400039", "400040", "400041", "400042", "400043", "400044", "400045", "400046", "400047", "400048", "400049", "400050", "401004", "402114", "402115", "402116", "402117", "402118", "402119", "402120", "402121", "402122", "402130", "403109", "405001", "405101", "405102", "405103", "405104", "405105", "405201", "406002", "407001", "407002", "407003", "409005", "409007", "410001", "410002", "410003", "410004", "415001", "415002", "415003", "415004", "415005", "415006", "415007", "415008", "415009", "415010", "415011", "415012", "415013", "415014", "415015", "415016", "415017", "415018", "415019", "415020", "416001", "418001", "419001", "419002", "419003", "419004", "419006", "420001", "420002", "420003", "420006", "421001", "421002", "421007", "423001", "423002", "423003", "423004", "423005", "424001", "424002", "428002", "429001", "429002", "429003", "429005", "429006", "429007", "4302310", "431001", "431002", "434001", "434002", "434003", "434004", "434007", "446003", "447001", "448001", "450001", "507001", "507003", "508001", "508002", "509001", "602303", "602304", "602305", "602306", "607001", "607002", "607003", "607004", "608001", "608002", "608003", "608004", "608005", "613013", "616001", "617001", "617003", "617004", "618001", "620001", "620002", "710003", "713032", "713033", "302013", "302015", "778001", "778003", "778004", "778006", "778007", "779001", "779002", "805001", "805002", "805003", "722022", "722023", "722028", "722012", "302037"
NETWORK_CONNECTION
"722053", "725001", "725002", "725003", "725004", "725005", "725007", "725016", "726001", "750001", "750002", "750003", "750004", "750005", "750006", "750007", "750008", "750009", "750010", "750014", "750015", "751001", "751002", "751004", "751005", "751006", "751007", "751008", "751009", "751010", "751011", "751012", "751013", "751014", "751015", "751016", "751017", "751020", "751021", "751022", "751023", "751024", "751025", "751026", "751027", "751028", "753001", "775001", "775002", "775003", "106001", "106002", "106006", "106007", "106010", "106011", "106012", "106013", "106014", "106015", "106016", "106017", "106018", "106020", "106021", "106022", "106023", "106025", "106026", "106027", "106100", "106102", "108002", "108004", "108007", "109007", "109008", "109010", "109023", "109024", "109025", "109028", "109034", "109039", "110002", "110003", "110004", "113042", "201003", "201010", "201011", "201012", "202005", "202010", "210005", "210007", "210008", "210010", "212004", "212006", "302003", "302004", "302012", "302017", "302018", "302020", "302021", "302022", "302024", "302026", "302027", "302033", "302034", "302035", "302036", "302303", "302305", "302306", "302311", "313004", "304001", "304002", "305005", "305006", "305009", "305010", "305011", "305012", "305013", "305014", "305016", "305017", "305018", "313005", "313008", "313009", "314001", "314002", "322004", "324000", "324001", "324002", "324003", "324004", "324005", "324007", "331001", "331002", "332003", "334001", "334002", "334003", "334004", "334005", "334006", "334007", "334008", "334009", "335001", "335002", "335003", "335004", "335005", "335006", "335008", "335009", "335012", "337000", "337001", "337005", "338001", "338002", "338003", "338004", "338005", "338006", "338007", "338008", "338101", "338102", "338103", "338104", "338201", "338202", "338203", "338204", "338301", "340001", "340002", "400000", "400001", "400002", "400003", "400004", "400005", "400006", "400007", "400008", "400009", "400010", "400011", "400012", "400013", "400014", "400015", "400016", "400017", "400018", "400019", "400020", "400021", "400022", "400023", "400024", "400025", "400026", "400027", "400028", "400029", "400030", "400031", "400032", "400033", "400034", "400035", "400036", "400037", "400038", "400039", "400040", "400041", "400042", "400043", "400044", "400045", "400046", "400047", "400048", "400049", "400050", "401004", "402114", "402115", "402116", "402117", "402118", "402119", "402120", "402121", "402122", "402130", "403109", "405001", "405101", "405102", "405103", "405104", "405105", "405201", "406002", "407001", "407002", "407003", "409005", "409007", "410001", "410002", "410003", "410004", "415001", "415002", "415003", "415004", "415005", "415006", "415007", "415008", "415009", "415010", "415011", "415012", "415013", "415014", "415015", "415016", "415017", "415018", "415019", "415020", "416001", "418001", "419001", "419002", "419003", "419004", "419006", "420001", "420002", "420003", "420006", "421001", "421002", "421007", "423001", "423002", "423003", "423004", "423005", "424001", "424002", "428002", "429001", "429002", "429003", "429005", "429006", "429007", "4302310", "431001", "431002", "434001", "434002", "434003", "434004", "434007", "446003", "447001", "448001", "450001", "507001", "507003", "508001", "508002", "509001", "602303", "602304", "602305", "602306", "607001", "607002", "607003", "607004", "608001", "608002", "608003", "608004", "608005", "613013", "616001", "617001", "617003", "617004", "618001", "620001", "620002", "710003", "713032", "713033", "302013", "302015", "778001", "778003", "778004", "778006", "778007", "779001", "779002", "805001", "805002", "805003", "106103", "108003", "317078", "324303"
NETWORK_UNCATEGORIZED
"101001", "101002", "101003", "101004", "101005", "103001", "103002", "103003", "103004", "103005", "103006", "103007", "103008", "104001", "104002", "104003", "104004", "104500", "104501", "104502", "105001", "105002", "105003", "105004", "105005", "105007", "105008", "105009", "105010", "105011", "105020", "105021", "105031", "105032", "105033", "105034", "105035", "105036", "105037", "105038", "105039", "105040", "105041", "105042", "105043", "105044", "105045", "105046", "105047", "105048", "105050", "105500", "105501", "105502", "105503", "105506", "105507", "105508", "105520", "105521", "105522", "105523", "105524", "105524", "105525", "105526", "105527", "105528", "105529", "105530", "105531", "105532", "105533", "105534", "105535", "105536", "105537", "109012", "109013", "109016", "109018", "109019", "109020", "109022", "109026", "109029", "109031", "109032", "109035", "109036", "109037", "109038", "109040", "111001", "111002", "111003", "111004", "111005", "111007", "111111", "112001", "113001", "114006", "114007", "114008", "114009", "114010", "114011", "114012", "114013", "114014", "114015", "114016", "114017", "114018", "114019", "114020", "114021", "114022", "114023", "115000", "115001", "115002", "120001", "120002", "120003", "120004", "120005", "120006", "120007", "120008", "120009", "120010", "120011", "120012", "121001", "121002", "121003", "199001", "199002", "199003", "199005", "199010", "199011", "199012", "199020", "199021", "199027", "210020", "210021", "211003", "211004", "212001", "212002", "212003", "212005", "212009", "212010", "212011", "213001", "213002", "213003", "213004", "213007", "214001", "215001", "216001", "216002", "216003", "216004", "216005", "218001", "218002", "218003", "218004", "218005", "219002", "216002", "216003", "216004", "216005", "218001", "218002", "218003", "218004", "218005", "219002", "722016", "722017", "722018", "722019", "722020", "722021", "722039", "722040", "722043", "722044", "722055", "730004", "730005", "730008", "730009", "732001", "732002", "732003", "733100", "733101", "733102", "733103", "735001", "735002", "735003", "735004", "735005", "735006", "735007", "735008", "735009", "735010", "735011", "735012", "735013", "735014", "735015", "735016", "735017", "735018", "735019", "735020", "735021", "735022", "735023", "735024", "735025", "735026", "735027", "735028", "735029", "736001", "737002", "737003", "737004", "737005", "737006", "737007", "737008", "737012", "737017", "737018", "737019", "737027", "737034", "741005", "741006", "742001", "742002", "742003", "742004", "742005", "742006", "742007", "742008", "742009", "742010", "746016", "747007", "747008", "747009", "747010", "747011", "747012", "747013", "747014", "747015", "747016", "747017", "747018", "747020", "747021", "747022", "747023", "747024", "747025", "747026", "747027", "747028", "747029", "747030", "747031", "747032", "747033", "747034", "747035", "747036", "747037", "747038", "747039", "747040", "747041", "747042", "748001", "748002", "748003", "748004", "748005", "748006", "748007", "748008", "748009", "748202", "748203", "750011", "750012", "751018", "751019", "768001", "768002", "768003", "768004", "770001", "770002", "770003", "772003", "772004", "775004", "775005", "775006", "775007", "776001", "776002", "776003", "776004", "776005", "776007", "776008", "776010", "105538", "105539", "105540", "105541", "105542", "105543", "105544", "105545", "105546", "105547", "105548", "105549", "105550", "105551", "109011", "113006", "113012", "113013", "113018", "113020", "113021", "113022", "113024", "113025", "113026", "113027", "113040", "114001", "114002", "114003", "113014", "113045", "302019", "302302", "304006", "304008", "315004", "318006", "318007", "318008", "318009", "318108", "318109", "318110", "318111", "318112", "318113", "318114", "318115", "318116", "318117", "318118", "318119", "318120", "318121", "318122", "318123", "318126", "320001", "321001", "321002", "321003", "321004", "321005", "321006", "321007", "322001", "323001", "323002", "323003", "323004", "323005", "323006", "323007", "324008", "324010", "324011", "324301", "325001", "325002", "325004", "325005", "325006", "326001", "326002", "326004", "326008", "326009", "326010", "326011", "326012", "326013", "326014", "326015", "326016", "326026", "326027", "326028", "328001", "328002", "329001", "333001", "333002", "333003", "333009", "333010", "335010", "335011", "335013", "335014", "336001", "336002", "336003", "336004", "336005", "336006", "336007", "336008", "336009", "336010", "336011", "336012", "336013", "336014", "336015", "336016", "336019", "338304", "338305", "338306", "338307", "338310", "339001", "339002", "339005", "341001", "341002", "341003", "341004", "341005", "341006", "341007", "341008", "341010", "341011", "342002", "342006", "342008", "401002", "401003", "401005", "402123", "402124", "402125", "402126", "402127", "402128", "402129", "402140", "402141", "402142", "402143", "402144", "402145", "402146", "402147", "402149", "402150", "403101", "403102", "403104", "403106", "403107", "403108", "403110", "403500", "403501", "403502", "403503", "403507", "405106", "406001", "408002", "408003", "408101", "408102", "409001", "409008", "409014", "409015", "409016", "409017", "409023", "409101", "409102", "409103", "409104", "409105", "409106", "409107", "409108", "409109", "409110", "409111", "409112", "409113", "409114", "409115", "409116", "409117", "409128", "411001", "411002", "411003", "411004", "411005", "412002", "413001", "413002", "413003", "413004", "413005", "413005", "413006", "413007", "413008", "414001", "414002", "414006", "414007", "414008", "417004", "417006", "418018", "420007", "421006", "422004", "422005", "425001", "425002", "425003", "425004", "425005", "425006", "426001", "426002", "426003", "426004", "426101", "426102", "426103", "426104", "429004", "429008", "444004", "444005", "444007", "444008", "444009", "444100", "444101", "444102", "444103", "444104", "444105", "444106", "444107", "444108", "444109", "444110", "444111", "444302", "444303", "444304", "444305", "444306", "446001", "500001", "500002", "502101", "502102", "502111", "502112", "503001", "503002", "503003", "503004", "503005", "503101", "504001", "504002", "505007", "505007", "505008", "505008", "505009", "505010", "505011", "505012", "505012", "505013", "505013", "505014", "505014", "505015", "505015", "505016", "505016", "506001", "507002", "603101", "603102", "603103", "604105", "606001", "606002", "606003", "606004", "610001", "610002", "610101", "611104", "611301", "611302", "611303", "611304", "611305", "611306", "611307", "611308", "611309", "611310", "611311", "611312", "611313", "611314", "611315", "611316", "611317", "611318", "611319", "611320", "611321", "611322", "611323", "612001", "612002", "612003", "613001", "613002", "613004", "613005", "613006", "613011", "613014", "613017", "613018", "613019", "613027", "613028", "613030", "613032", "613035", "613036", "613037", "613038", "613039", "613101", "613103", "615001", "615002", "617002", "622001", "622101", "622102", "709007", "709008", "711002", "711004", "711005", "713004", "713201", "713202", "713008", "713009", "713010", "713012", "713014", "713016", "713017", "713018", "713020", "713048", "713049", "713056", "713060", "713061", "713065", "713068", "713072", "713073", "713074", "713075", "713076", "713078", "713081", "713084", "713085", "713086", "713088", "713092", "713098", "713102", "713105", "713107", "713109", "713112", "713115", "713118", "713119", "713120", "713122", "713124", "713127", "713128", "713129", "713131", "713133", "713134", "713136", "713137", "713138", "713139", "713140", "713141", "713142", "713144", "713149", "713152", "713159", "713161", "713162", "713163", "713165", "713166", "713167", "713168", "713172", "713179", "713184", "713186", "713193", "713194", "713195", "713197", "713198", "713199", "713206", "713207", "713208", "713209", "713210", "713215", "713216", "713217", "713219", "713220", "713230", "713231", "713232", "713235", "713237", "713238", "713240", "713241", "713242", "713243", "713244", "713245", "713246", "713247", "713248", "713249", "713250", "713251", "713257", "713260", "713130", "713275", "713276", "713900", "713901", "713902", "713903", "713904", "713905", "716005", "716009", "716022", "716023", "716041", "716043", "716048", "716049", "716050", "716053", "716054", "716055", "716057", "716058", "716059", "716060", "716061", "716500", "716501", "716502", "716503", "716504", "716505", "716506", "716507", "716508", "716509", "716510", "716512", "716513", "716515", "716516", "716517", "716518", "716519", "716520", "716521", "716522", "716525", "716526", "716527", "716528", "716600", "716601", "716602", "717001", "717002", "717003", "717004", "717005", "717006", "717007", "717008", "717009", "717010", "717011", "717012", "717013", "717014", "717015", "717016", "717017", "717018", "717019", "717020", "717021", "717022", "717023", "717026", "717027", "717028", "717031", "717033", "717035", "717037", "717039", "717040", "717042", "717043", "717044", "717046", "717047", "717048", "717049", "717054", "717055", "717057", "717058", "717059", "717060", "717061", "717062", "717063", "717064", "720022", "720023", "720024", "720025", "720026", "720027", "720028", "720029", "720030", "720032", "720033", "720035", "720036", "720037", "720038", "720039", "720040", "720043", "720044", "720045", "720046", "720055", "720056", "720057", "720058", "720059", "720060", "720061", "720062", "720063", "720065", "720066", "720067", "720068", "720069", "720070", "720071", "720072", "720073", "721001", "721002", "721003", "721004", "721005", "721006", "721007", "721008", "721009", "721010", "721011", "721012", "721013", "721014", "721015", "718004", "718005", "718006", "718007", "718008", "718037", "718038", "718039", "718040", "718057", "718060", "718061", "718062", "718063", "718064", "718068", "718069", "718070", "718071", "718072", "718073", "718074", "718075", "718085", "718086", "718087", "719001", "719002", "719003", "719004", "719008", "719010", "719011", "719012", "719013", "719014", "719017", "719018", "719019", "719020", "719021", "719022", "719023", "719024", "719025", "719026", "720001", "720002", "720003", "720004", "720005", "720006", "720007", "720008", "720009", "720010", "720011", "720012", "720013", "720014", "720015", "720016", "720017", "720018", "720019", "720020", "720021", "722026", "722027", "722046", "722047", "722048", "722049", "722050", "747004", "748100", "748101", "748102", "748103", "748201", "769001", "769002", "769003", "769004", "769005", "769006", "402131", "403504", "420004", "420005", "502103", "776201", "776202", "776203", "776204", "776303", "776304", "776309", "776310", "776311", "776312", "776313", "802005", "802006", "850001", "850002", "8300002", "8300003", "8300004", "8300005"
STATUS_UPDATE
111010
SETTING_MODIFICATION
"113019", "315011", "611103", "716002", "722012"
USER_LOGOUT
"113023", "713121", "715036", "715075"
STATUS_HEARTBEAT
"113015", "113004", "113005", "113010", "113011", "113039", "605005", "605004", "611101", "611102", "716038", "716039", "716040"
USER_LOGIN
"111009", "111008", "113003", "113008", "113009", "713130", "725006", "746012", "746013", "746017", "746018", "746019"
USER_UNCATEGORIZED
"303002", "303004", "303005"
NETWORK_FTP
"746014", "746015"
NETWORK_DNS
"604201", "604202", "604203", "604204", "604205", "604206", "604207", "604208"
NETWORK_DHCP
The other Cisco message IDs that are not listed in this table are set to GENERIC_EVENT. Also, if a mandatory field is missing for a message ID, it is set to GENERIC_EVENT.
GENERIC_EVENT
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
