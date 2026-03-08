# Collect SonicWall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/sonic-firewall/  
**Scraped:** 2026-03-05T10:00:25.889430Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect SonicWall logs
Supported in:
Google secops
SIEM
This document describes how you can collect SonicWall logs by
using a Google Security Operations forwarder.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser with the
SONIC_FIREWALL
ingestion label.
Configure SonicWall security appliance
Sign in to the
SonicWall
console.
Go to
Log
>
Syslog
.
In the
Syslog servers
section, click
Add
. The
Add syslog server
window appears.
In the
Name
or
IP address
field, provide the Google Security Operations forwarder hostname or IP address.
If your syslog configuration doesn't use the default 514 port, in the
Port number
field, specify the port number.
Click
Ok
.
Click
Accept
to save all the syslog server settings.
Configure Google Security Operations forwarder and syslog to ingest SonicWall logs
Go to
SIEM Settings
>
Forwarders
.
Click
Add new forwarder
.
In the
Forwarder Name
field, enter a unique name for the forwarder.
Click
Submit
. The forwarder is added and the
Add collector configuration
window appears.
In the
Collector name
field, type a name.
Select
SonicWall
as the
Log type
.
Select
Syslog
as the
Collector type
.
Configure the following mandatory input parameters:
Protocol
: specify the connection protocol the collector will use to listen for syslog data.
Address
: specify the target IP address or hostname where the collector resides and listens for syslog data.
Port
: specify the target port where the collector resides and listens for syslog data.
Click
Submit
.
For more information about Google Security Operations forwarders, see
Google Security Operations forwarders documentation
.
For information about requirements for each forwarder type, see
Forwarder configuration by type
.
If you encounter issues when you create forwarders,
contact Google Security Operations support
.
Field mapping reference
This parser extracts key-value pairs from SonicWall firewall syslog messages, normalizes various fields like timestamps, IP addresses, and ports, and maps them to the UDM format.  It handles both IPv4 and IPv6 addresses, distinguishes between allowed and blocked events, and extracts security-relevant details like rule names and descriptions.
Supported SonicWall sample logs
Standard firewall event
{
"type"
:
"SONIC_FIREWALL"
,
"log"
:
"<134> id=SONICWALL_FIREWALL\n"
"      sn=DEADD00D1234\n"
"      time=\"2020-04-08 13:28:45\"\n"
"      fw=192.0.2.1\n"
"      pri=6\n"
"      c=1024\n"
"      gcat=2\n"
"      m=97\n"
"      msg=\"Web site hit\"\n"
"      srcMac=00:00:5E:00:53:01\n"
"      src=192.0.2.10:12345:X0\n"
"      srcZone=LAN\n"
"      natSrc=192.0.2.10:12345\n"
"      dstMac=00:00:5E:00:53:02\n"
"      dst=198.51.100.20:443:X0\n"
"      dstZone=WAN\n"
"      natDst=198.51.100.20:443\n"
"      proto=tcp/https\n"
"      sent=1247\n"
"      rcvd=59996\n"
"      rule=\"14 (LAN->WAN)\"\n"
"      app=49175\n"
"      appName=\"General HTTP\"\n"
"      op=1\n"
"      dstname=sanitized-host.com\n"
"      arg=/sanitized/path/file.cab?id=REDACTED\n"
"      code=27\n"
"      Category=\"Information Technology/Computers\"\n"
"      n=3451648"
}
SSL-VPN session event
{
"type"
:
"SONIC_FIREWALL"
,
"log"
:
"<181>SSLVPN: id=sslvpn\n"
"      sn=DEADD00D1234\n"
"      time=\"2020-04-10 10:07:11\"\n"
"      vp_time=\"2020-04-10 08:07:11 UTC\"\n"
"      fw=192.0.2.1\n"
"      pri=5\n"
"      m=2\n"
"      c=102\n"
"      src=203.0.113.50\n"
"      dst=192.0.2.1\n"
"      user=\"internal_user@company.com\"\n"
"      usr=\"internal_user@company.com\"\n"
"      msg=\"NetExtender disconnected\"\n"
"      rule=access-policy\n"
"      duration=731\n"
"      bytesIn=47360\n"
"      bytesOut=10\n"
"      agent=\"SonicWALL NetExtender for Windows (REDACTED)\""
}
Advanced threat/app control
{
"type"
:
"SONIC_FIREWALL"
,
"log"
:
"<129> id=PD_Firewall sn=DEADD00D1234 time=\"2024-03-06 12:33:40\"\n"
"      fw=192.0.2.1 pri=1 c=0 m=1154 msg=\"Application Control Detection\n"
"      Alert: PROTOCOLS DNS Protocol -- Standard Query A\" sid=5183\n"
"      appcat=\"PROTOCOLS DNS Protocol -- Standard Query A\" appid=1283 catid=74\n"
"      n=3235773 src=192.0.2.15:58482:X0 dst=203.0.113.1:53:X2\n"
"      srcMac=00:00:5E:00:53:03 dstMac=00:00:5E:00:53:04 proto=udp/dns\n"
"      fw_action=\"NA\""
}
UDM mapping table
Log field
UDM mapping
Logic
agent
event.idm.read_only_udm.network.http.user_agent
The value of the
agent
field is assigned to the UDM field.
appcat
event.idm.read_only_udm.security_result.summary
The value of the
appcat
field is assigned to the UDM field. If
appcat
contains "PROXY-ACCESS",
event.idm.read_only_udm.security_result.category
is set to "POLICY_VIOLATION" and
event.idm.read_only_udm.security_result.action
is set to "BLOCK".
appid
event.idm.read_only_udm.security_result.rule_id
The value of the
appid
field is assigned to the UDM field.
arg
event.idm.read_only_udm.target.resource.name
The value of the
arg
field is assigned to the UDM field.
avgThroughput
event.idm.read_only_udm.target.resource.attribute.labels
A label with key "avgThroughput" and value from the
avgThroughput
field is added to the UDM field.
bytesIn
event.idm.read_only_udm.network.received_bytes
The value of the
bytesIn
field is converted to an unsigned integer and assigned to the UDM field.
bytesOut
event.idm.read_only_udm.network.sent_bytes
The value of the
bytesOut
field is converted to an unsigned integer and assigned to the UDM field.
bytesTotal
event.idm.read_only_udm.target.resource.attribute.labels
A label with key "bytesTotal" and value from the
bytesTotal
field is added to the UDM field.
Category
event.idm.read_only_udm.security_result.category_details
The value of the
Category
field is assigned to the UDM field.
cdur
event.idm.read_only_udm.security_result.detection_fields
A detection field with key "Connection Duration (milli seconds)" and value from the
cdur
field is added to the UDM field.
dst
event.idm.read_only_udm.target.ip
,
event.idm.read_only_udm.target.port
The IP and port are extracted from the
dst
field. If
dstV6
is not empty, the IP is extracted from
dstV6
instead.
dstMac
event.idm.read_only_udm.target.mac
The value of the
dstMac
field is assigned to the UDM field.
dstV6
event.idm.read_only_udm.target.ip
The IP is extracted from the
dstV6
field.
dstname
event.idm.read_only_udm.target.hostname
If
dstname
is not an IP address, its value is assigned to the UDM field.
duration
event.idm.read_only_udm.network.session_duration.seconds
The value of the
duration
field is converted to an integer and assigned to the UDM field.
fw
event.idm.read_only_udm.principal.ip
The value of the
fw
field is assigned to the UDM field. If
fw
contains "-", a label with key "fw" and value from the
fw
field is added to
event.idm.read_only_udm.additional.fields
.
fw_action
event.idm.read_only_udm.security_result.action_details
,
event.idm.read_only_udm.security_result.summary
,
event.idm.read_only_udm.security_result.action
The value of the
fw_action
field is assigned to
event.idm.read_only_udm.security_result.action_details
. If
fw_action
is "drop",
event.idm.read_only_udm.security_result.action
is set to "BLOCK" and
event.idm.read_only_udm.security_result.summary
is set to the value of
msg
.
gw
event.idm.read_only_udm.intermediary.ip
The IP address is extracted from the
gw
field and assigned to the UDM field.
id
event.idm.read_only_udm.principal.hostname
,
event.idm.read_only_udm.principal.asset.hostname
The value of the
id
field is assigned to both UDM fields.
maxThroughput
event.idm.read_only_udm.target.resource.attribute.labels
A label with key "maxThroughput" and value from the
maxThroughput
field is added to the UDM field.
msg
event.idm.read_only_udm.security_result.summary
,
event.idm.read_only_udm.metadata.description
If
fw_action
is not "drop" or
appcat
is empty, the value of the
msg
field is assigned to
event.idm.read_only_udm.security_result.summary
. Otherwise, it's assigned to
event.idm.read_only_udm.metadata.description
.
natDst
event.idm.read_only_udm.target.nat_ip
The IP address is extracted from the
natDst
field and assigned to the UDM field.
natSrc
event.idm.read_only_udm.principal.nat_ip
The IP address is extracted from the
natSrc
field and assigned to the UDM field.
note
event.idm.read_only_udm.security_result.description
The value of the
note
field, after extracting
dstip
,
srcip
,
gw
, and
sec_desc
, is assigned to the UDM field.
packetsIn
event.idm.read_only_udm.target.resource.attribute.labels
A label with key "packetsIn" and value from the
packetsIn
field is added to the UDM field.
packetsOut
event.idm.read_only_udm.target.resource.attribute.labels
A label with key "packetsOut" and value from the
packetsOut
field is added to the UDM field.
packetsTotal
event.idm.read_only_udm.target.resource.attribute.labels
A label with key "packetsTotal" and value from the
packetsTotal
field is added to the UDM field.
pri
event.idm.read_only_udm.security_result.severity
The value of the
pri
field determines the value of the UDM field: 0, 1, 2 -> CRITICAL; 3 -> ERROR; 4 -> MEDIUM; 5, 7 -> LOW; 6 -> INFORMATIONAL.
proto
event.idm.read_only_udm.network.ip_protocol
,
event.idm.read_only_udm.network.application_protocol
,
event.idm.read_only_udm.metadata.event_type
If
proto
contains "udp", the UDM
ip_protocol
is set to "UDP" and
event_type
is set to "NETWORK_CONNECTION". If
proto
contains "https", the UDM
application_protocol
is set to "HTTPS".
rcvd
event.idm.read_only_udm.network.received_bytes
The value of the
rcvd
field is converted to an unsigned integer and assigned to the UDM field.
rule
event.idm.read_only_udm.security_result.rule_name
The value of the
rule
field is assigned to the UDM field.
sec_desc
event.idm.read_only_udm.security_result.description
The value of the
sec_desc
field is assigned to the UDM field.
sent
event.idm.read_only_udm.network.sent_bytes
The value of the
sent
field is converted to an unsigned integer and assigned to the UDM field.
sess
event.idm.read_only_udm.security_result.detection_fields
A detection field with key "Session Type" and value from the
sess
field is added to the UDM field.
sn
event.idm.read_only_udm.additional.fields
A label with key "SN" and value from the
sn
field is added to the UDM field.
spkt
event.idm.read_only_udm.network.sent_packets
The value of the
spkt
field is converted to an integer and assigned to the UDM field.
src
event.idm.read_only_udm.principal.ip
,
event.idm.read_only_udm.principal.port
The IP and port are extracted from the
src
field. If
srcV6
is not empty, the IP is extracted from
srcV6
instead.
srcMac
event.idm.read_only_udm.principal.mac
The value of the
srcMac
field is assigned to the UDM field.
srcV6
event.idm.read_only_udm.principal.ip
The IP is extracted from the
srcV6
field.
srcip
event.idm.read_only_udm.additional.fields
,
event.idm.read_only_udm.principal.ip
If
srcip
contains "-", a label with key "srcip" and value from the
srcip
field is added to
event.idm.read_only_udm.additional.fields
. Otherwise, the value of
srcip
is assigned to
event.idm.read_only_udm.principal.ip
.
time
event.idm.read_only_udm.metadata.event_timestamp
The value of the
time
field is parsed and converted to a timestamp, which is then assigned to the UDM field.
type
event.idm.read_only_udm.network.ip_protocol
If
proto
field is "icmp", the UDM field is set to "ICMP".
user/usr
event.idm.read_only_udm.principal.user.email_addresses
,
event.idm.read_only_udm.principal.user.user_display_name
,
event.idm.read_only_udm.principal.user.userid
If
user
is empty, the value of
usr
is used instead. If the value contains "@" it is treated as an email address and added to
email_addresses
. If it contains a space, it's treated as a display name. Otherwise, it's treated as a userid.
vpnpolicy
event.idm.read_only_udm.security_result.detection_fields
A detection field with key "vpnpolicy" and value from the
vpnpolicy
field is added to the UDM field.  Hardcoded to "SonicWall". Hardcoded to "Firewall". Hardcoded to "SONIC_FIREWALL". Determined by logic based on the values of other fields. Defaults to "GENERIC_EVENT", can be "STATUS_UPDATE", "NETWORK_CONNECTION", or "NETWORK_HTTP".
Need more help?
Get answers from Community members and Google SecOps professionals.
