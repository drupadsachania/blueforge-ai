# Collect Fortinet Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-firewall/  
**Scraped:** 2026-03-05T09:47:50.797323Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet Firewall logs
Supported in:
Google secops
SIEM
This document explains how to export Fortinet Firewall logs by setting up the Bindplane agent and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Fortinet Firewall and the Bindplane agent configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Fortinet Firewall
: The platform from which you collect logs.
Bindplane agent
: The Bindplane agent fetches logs from Fortinet Firewall and sends logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. 
The information in this document applies to the parser with the FORTINET_FIREWALL label.
Install and configure the feed
Use FortiOS 7.6.2 or later and verify that you
have set up your FortiGate for initial management access to the platform. For more information, see
Set up Fortigate
.
Make sure that all systems in the deployment architecture are configured
in the UTC time zone.
Configure syslog on the Fortigate platform:
To configure syslog, use the following steps:
Log in to the FortiGate platform.
Select
Log & Report
to expand the menu.
Select
Log Settings
.
Turn on the
Send Logs to Syslog
toggle.
Enter the
Syslog Collector IP address
.
Select
Apply
. For information about configuration, see
Configure Syslog on FortiGate From the GUI
.
Forward logs to Google SecOps using the Bindplane agent
Install and set up a
Linux Virtual Machine
.
Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see the
Bindplane agent installation and configuration instructions
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
UDM Mapping Table
Field mapping reference: Fortinet_Firewall - Common Fields
The following table lists common fields of the
Common Schema Field Mapping
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Fortinet
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Fortigate
.
filehash
about.file.sha256
If the
filehash
log field value matches the regular expression pattern
(?<_hash>^[0-9a-f]+$)
then,
filehash
log field is mapped to the
about.file.sha256
UDM field.
Else,
filehash
log field is mapped to the
about.file.full_path
UDM field.
nat
about.nat_ip
pdstport
additional.fields[pdstport]
subject
about.process.command_line
process
about.process.product_specific_process_id
policy_id
about.resource.product_object_id
The
about.resource.resource_type
UDM field is set to
FIREWALL_RULE
.
policymode
about.resource.resource_subtype
psrcport
additional.fields[psrcport]
appact
additional.fields[appact]
appcat
additional.fields[appcat]
applist
additional.fields[applist]
apprisk
additional.fields[apprisk]
authproto
additional.fields[authproto]
bandwidth
additional.fields[bandwidth]
bibandwidthavailable
additional.fields[bibandwidthavailable]
bibandwidthused
additional.fields[bibandwidthused]
cfgattr
additional.fields[cfgattr]
cfgpath
additional.fields[cfgpath]
chgheaders
additional.fields[chgheaders]
column
additional.fields[column]
comment
additional.fields[comment]
core
additional.fields[core]
count
additional.fields[count]
countapp
additional.fields[countapp]
countips
additional.fields[countips]
cpu
additional.fields[cpu]
crl
additional.fields[crl]
datarange
additional.fields[datarange]
dint
additional.fields[dint]
disk
additional.fields[disk]
disklograte
additional.fields[disklograte]
dlpextra
additional.fields[dlpextra]
docsource
additional.fields[docsource]
domainfilteridx
additional.fields[domainfilteridx]
domainfilterlist
additional.fields[domainfilterlist]
downbandwidthmeasured
additional.fields[downbandwidthmeasured]
ds
additional.fields[ds]
dst_int
additional.fields[dst_int]
dstdevtype
additional.fields[dstdevtype]
dstfamily
additional.fields[dstfamily]
dstssid
additional.fields[dstssid]
dstunauthusersource
additional.fields[dstunauthusersource]
dtlexp
additional.fields[dtlexp]
eapoltype
additional.fields[eapoltype]
emsconnection
additional.fields[emsconnection]
emstag
additional.fields[emstag]
emstag2
additional.fields[emstag2]
encrypt
additional.fields[encrypt]
encryption
additional.fields[encryption]
epoch
additional.fields[epoch]
error_num
additional.fields[error_num]
espauth
additional.fields[espauth]
esptransform
additional.fields[esptransform]
eventId
additional.fields[eventId]
expiry
additional.fields[expiry]
extension
additional.fields[extension]
extinvalid
additional.fields[extinvalid]
exttotal
additional.fields[exttotal]
failuredev
additional.fields[failuredev]
fams_pause
additional.fields[fams_pause]
fazlograte
additional.fields[fazlograte]
fctemsname
additional.fields[fctemsname]
fctemssn
additional.fields[fctemssn]
fctuid
additional.fields[fctuid]
field
additional.fields[field]
frametype
additional.fields[frametype]
freediskstorage
additional.fields[freediskstorage]
from_vcluster
additional.fields[from_vcluster]
from6
additional.fields[from6]
ftlkintf
additional.fields[ftlkintf]
fwdsrv
additional.fields[fwdsrv]
fwserver_name
additional.fields[fwserver_name]
green
additional.fields[green]
handshake
additional.fields[handshake]
headerteid
additional.fields[headerteid]
helthchekck
additional.fields[helthchekck]
hseid
additional.fields[hseid]
iaid
additional.fields[iaid]
icmpcode
additional.fields[icmpcode]
icmpid
additional.fields[icmpid]
icmptype
additional.fields[icmptype]
identifier
additional.fields[identifier]
ietype
additional.fields[ietype]
interface
additional.fields[interface]
intf
additional.fields[intf]
invalidmac
additional.fields[invalidmac]
iptype
additional.fields[iptype]
itype
additional.fields[itype]
jittter
additional.fields[jittter]
keyword
additional.fields[keyword]
latency
additional.fields[latency]
limit
additional.fields[limit]
line
additional.fields[line]
linked-nsapi
additional.fields[linked-nsapi]
localdevcount
additional.fields[localdevcount]
log
additional.fields[log]
logid
additional.fields[logid]
logsrc
additional.fields[logsrc]
mem
additional.fields[mem]
member
additional.fields[member]
meshmode
additional.fields[meshmode]
message
additional.fields[message]
messageid
additional.fields[messageid]
mitm
additional.fields[mitm]
model
additional.fields[model]
modul
additional.fields[modul]
moscodec
additional.fields[moscodec]
mosvalue
additional.fields[mosvalue]
mpsk
additional.fields[mpsk]
msg-type
additional.fields[msg-type]
msgtypename
additional.fields[msgtypename]
mtu
additional.fields[mtu]
nai
additional.fields[nai]
nsapi
additional.fields[nsapi]
probeproto
additional.fields[probeproto]
proto
additional.fields[proto]
protocol
additional.fields[protocol]
proxyapptype
additional.fields[proxyapptype]
rcvdpkt
additional.fields[rcvdpkt]
red_conserve_mode
additional.fields[red_conserve_mode]
sentpkt
additional.fields[sentpkt]
service
additional.fields[service]
shaperdroprcvdbyte
additional.fields[shaperdroprcvdbyte]
shaperdropsentbyte
additional.fields[shaperdropsentbyte]
shaperrcvdname
additional.fields[shaperrcvdname]
shapersentname
additional.fields[shapersentname]
shapingpolicyid
additional.fields[shapingpolicyid]
shapingpolicyname
additional.fields[shapingpolicyname]
srcserver
additional.fields[srcserver]
sysuptime
additional.fields[sysuptime]
trandisp
additional.fields[trandisp]
ui
additional.fields[ui]
vpntype
additional.fields[vpntype]
vwlid
additional.fields[vwlid]
wanin
additional.fields[wanin]
waninfo
additional.fields[waninfo]
adminprof
additional.fields[adminprof]
authserver
extensions.auth.auth_details
If the
authserver
log field value is
not
empty
then,
authserver
log field is mapped to the
extensions.auth.auth_details
UDM field.
Else, if the
domainctrlauthstate
log field value is
not
empty
then,
domainctrlauthstate
log field is mapped to the
extensions.auth.auth_details
UDM field.
domainctrlauthstate
extensions.auth.auth_details
If the
authserver
log field value is
not
empty
then,
authserver
log field is mapped to the
extensions.auth.auth_details
UDM field.
Else, if the
domainctrlauthstate
log field value is
not
empty
then,
domainctrlauthstate
log field is mapped to the
extensions.auth.auth_details
UDM field.
extensions.auth.type
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
action
log field value contain one of the following values
tunnel-down
tunnel-up
ssl-new-con
or the
action
log field value is equal to
negotiate
and the
locip
log field value is
not
empty
or the
remip
log field value is
not
empty
then, the
extensions.auth.type
UDM field is set to
VPN
. Else, if the
action
log field value is equal to
tunnel-stats
and the
locip
log field value is
not
empty
or the
remip
log field value is
not
empty
then, the
extensions.auth.type
UDM field is set to
VPN
. Else, if the
type
log field value is equal to
event
and the
ui
log field value is
not
empty
or the
remip
log field value is
not
empty
then, the
extensions.auth.type
UDM field is set to
VPN
. Else, if the
action
log field value is equal to
tunnel-stats
then, the
extensions.auth.type
UDM field is set to
VPN
.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
action
log field value matches the regular expression pattern
.*SSO.*
then, the
extensions.auth.type
UDM field is set to
SSO
. Else, the
extensions.auth.type
UDM field is set to
VPN
.
gatewayid
intermediary.asset_id
If the
gatewayid
log field value is
not
empty
then,
Fortinet:gatewayid
log field is mapped to the
intermediary.asset_id
UDM field.
Else, if the
domainctrlname
log field value is
not
empty
then,
Fortinet:domainctrlname
log field is mapped to the
intermediary.asset_id
UDM field.
Else, if the
devintfname
log field value is
not
empty
then,
Fortinet:devintfname
log field is mapped to the
intermediary.asset_id
UDM field.
domainctrlname
intermediary.asset_id
If the
gatewayid
log field value is
not
empty
then,
Fortinet:gatewayid
log field is mapped to the
intermediary.asset_id
UDM field.
Else, if the
domainctrlname
log field value is
not
empty
then,
Fortinet:domainctrlname
log field is mapped to the
intermediary.asset_id
UDM field.
Else, if the
devintfname
log field value is
not
empty
then,
Fortinet:devintfname
log field is mapped to the
intermediary.asset_id
UDM field.
devintfname
intermediary.asset_id
If the
gatewayid
log field value is
not
empty
then,
Fortinet:gatewayid
log field is mapped to the
intermediary.asset_id
UDM field.
Else, if the
domainctrlname
log field value is
not
empty
then,
Fortinet:domainctrlname
log field is mapped to the
intermediary.asset_id
UDM field.
Else, if the
devintfname
log field value is
not
empty
then,
Fortinet:devintfname
log field is mapped to the
intermediary.asset_id
UDM field.
authserevr
about.hostname
monitor-name
intermediary.asset.hostname
old_value
intermediary.domain.name
domainctrldomain
intermediary.hostname
If the
dvchost
log field value is
not
empty
then,
dvchost
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
domainctrldomain
log field value is
not
empty
then,
domainctrldomain
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
temp_data
log field value is
not
empty
then, The
ts
and
device_name
fields is extracted from
temp_data
log field using the Grok pattern. if the
device_name
log field value is
not
empty
then,
device_name
log field is mapped to the
intermediary.hostname
UDM field.
dvchost
intermediary.hostname
If the
dvchost
log field value is
not
empty
then,
dvchost
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
domainctrldomain
log field value is
not
empty
then,
domainctrldomain
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
temp_data
log field value is
not
empty
then, The
ts
and
device_name
fields is extracted from
temp_data
log field using the Grok pattern. if the
device_name
log field value is
not
empty
then,
device_name
log field is mapped to the
intermediary.hostname
UDM field.
devname
intermediary.hostname
If the
dvchost
log field value is
not
empty
then,
dvchost
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
domainctrldomain
log field value is
not
empty
then,
domainctrldomain
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
temp_data
log field value is
not
empty
then, The
ts
and
device_name
fields is extracted from
temp_data
log field using the Grok pattern. if the
device_name
log field value is
not
empty
then,
device_name
log field is mapped to the
intermediary.hostname
UDM field.
fortihost
intermediary.ip
If the
fortihost
log field value is
not
empty
then, The
fortihost_ip
field is extracted from
fortihost
log field using the Grok pattern. if the
fortihost_ip
log field value is
not
empty
then,
fortihost_ip
extracted field is mapped to the
intermediary.ip
UDM field.
If the
domainctrlip
log field value is
not
empty
then, The
valid_domainctrlip
field is extracted from
domainctrlip
log field using the Grok pattern. if the
valid_domainctrlip
log field value is
not
empty
then,
valid_domainctrlip
extracted field is mapped to the
intermediary.ip
UDM field.
domainctrlip
intermediary.ip
ha_group
intermediary.asset.attribute.labels[ha_group]
ha_prio
intermediary.asset.attribute.labels[ha_prio]
ha_role
intermediary.asset.attribute.labels[ha_role]
monitor-type
intermediary.asset.attribute.labels[monitor-type]
metadata.event_type
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. if the
subtype
log field value is equal to
webfilter
and if the
service
log field value contain one of the following values
HTTPS
HTTP
then, the
metadata.event_type
UDM field is set to
NETWORK_HTTP
. Else, if the
subtype
log field value contain one of the following values
virus
ips
anomaly
or the
utmevent
log field value is equal to
appfirewall
and the
subtype
log field value is
not
equal to
system
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else if the
subtype
log field value is equal to
vpn
and
type
is equal to
event
and if the
action
log field value contain one of the following values
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else, if the
type
log field value is equal to
dns
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
then, the
metadata.event_type
UDM field is set to
NETWORK_DNS
.
Else, if the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, the
metadata.event_type
UDM field is set to
NETWORK_DHCP
.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
action
log field value matches the regular expression pattern
.
logoff.
or the
action
log field value is equal to
authentication
and the
status
log field value is equal to
logout
or the
action
log field value is equal to
auth-logout
and the
status
log field value is equal to
logout
then, the
metadata.event_type
UDM field is set to
USER_LOGOUT
. if the
action
log field value matches the regular expression pattern
.
logon.
or the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
login
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
user_id
log field value is
not
empty
and the
user_email
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
USER_CREATION
. Else, the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
If the
event_name
log field value contain one of the following values
LogSpyware
LogPredictiveMachineLearning
or the
subtype
log field value contain one of the following values
LogSpyware
LogPredictiveMachineLearning
endpoint
system
then, the
metadata.event_type
UDM field is set to
SCAN_UNCATEGORIZED
.
If the
user
log field value does not contain one of the following values
Empty
N/A
and if the
metadata.event_type
log field value is equal to
GENERIC_EVENT
then, if the
subtype
log field value is equal to
vpn
and
type
is equal to
event
and if the
action
log field value contain one of the following values
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
If the
File_name
log field value is
not
empty
or the
Object
log field value is
not
empty
or the
Objekt
log field value is
not
empty
or the
Infected_Resource
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
PROCESS_UNCATEGORIZED
.=
If the
metadata.event_type
log field value matches the regular expression pattern
GENERIC_EVENT
and if the
srcip
log field value is
not
empty
and the
dstip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
. Else, if the
srcip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
. Else, if the
action
log field value is equal to
Delete
then, the
metadata.event_type
UDM field is set to
USER_DELETION
. if the
action
log field value is equal to
Edit
then, the
metadata.event_type
UDM field is set to
DEVICE_CONFIG_UPDATE
.
logdesc
metadata.description
Message Description
with related to
logid
log field is mapped to
metadata.description
.
For more information, see the
Fortinet Log Messages Reference
.
type
metadata.description
Message Description
with related to
logid
log field is mapped to
metadata.description
.
For more information, see the
Fortinet Log Messages Reference
.
subtype
metadata.description
Message Description
with related to
logid
log field is mapped to
metadata.description
.
For more information, see the
Fortinet Log Messages Reference
.
msg
metadata.description
Message Description
with related to
logid
log field is mapped to
metadata.description
.
For more information, see the
Fortinet Log Messages Reference
.
eventtime
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
timestamp
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
date
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
time
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
logtime
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
syslogtime
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
tz
metadata.event_timestamp
If the
eventtime
log field value is
not
empty
then, The
eventtime1
field is extracted from
eventtime
log field using the Grok pattern. if the
eventtime1
log field value is
not
empty
then,
eventtime1
extracted field is mapped to the
metadata.event_timestamp
UDM field. Else,
eventtime
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
timestamp
log field value is
not
empty
then,
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
syslogtime
log field value is
not
empty
then,The
syslogtime
field is extracted from raw log using the Grok pattern and it is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.event_timestamp
UDM field.
Else, if the
date
log field value is
not
empty
and the
time
log field value is
not
empty
then,
%{date} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
time
metadata.ingested_timestamp
If the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.ingested_timestamp
UDM field.
date
metadata.ingested_timestamp
If the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.ingested_timestamp
UDM field.
tz
metadata.ingested_timestamp
If the
date
log field value is
not
empty
and the
time
log field value is
not
empty
and the
tz
log field value is
not
empty
then,
%{date} %{time} %{tz}
log field is mapped to the
metadata.ingested_timestamp
UDM field.
type
metadata.product_event_type
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
subtype
metadata.product_event_type
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
connection_type
metadata.product_event_type
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
eventsubtype
metadata.product_event_type
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
logid
metadata.product_log_id
If the
logid
log field value is
not
empty
then,
logid
log field is mapped to the
metadata.product_log_id
UDM field.
Else, if the
event_id
log field value is
not
empty
then,
event_id
log field is mapped to the
metadata.product_log_id
UDM field.
event_id
metadata.product_log_id
If the
logid
log field value is
not
empty
then,
logid
log field is mapped to the
metadata.product_log_id
UDM field.
Else, if the
event_id
log field value is
not
empty
then,
event_id
log field is mapped to the
metadata.product_log_id
UDM field.
version
metadata.product_version
If the
device_version
log field value is
not
empty
then,
device_version
extracted field is mapped to the
metadata.product_version
UDM field.
Else,
version
log field is mapped to the
metadata.product_version
UDM field.
device_version
metadata.product_version
If the
device_version
log field value is
not
empty
then,
device_version
extracted field is mapped to the
metadata.product_version
UDM field.
Else,
version
log field is mapped to the
metadata.product_version
UDM field.
metadata.log_type
The
metadata.log_type
UDM field is set to
FORTINET_FIREWALL
.
ref
metadata.url_back_to_product
authproto
network.application_protocol
service
network.application_protocol
protocol
network.application_protocol
proxyapptype
network.application_protocol
c-ggsn
network.carrier_name
attachment
network.dhcp.file
lease
network.dhcp.lease_time_seconds
network.dhcp.type
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, the
network.dhcp.type
UDM field is set to
ACK
and the
network.application_protocol
UDM field is set to
DHCP
.
ip
network.dhcp.yiaddr
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
ip
log field is mapped to the
network.dhcp.yiaddr
UDM field.
assigned
network.dhcp.yiaddr
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
ip
log field is mapped to the
network.dhcp.yiaddr
UDM field.
dir
network.direction
If the
direction
log field value contain one of the following values
incoming
inbound
response
then, the
network.direction
UDM field is set to
INBOUND
.
Else, if the
direction
log field value contain one of the following values
outgoing
outbound
request
session_origin
then, the
network.direction
UDM field is set to
OUTBOUND
.
ddnsserver
network.dns.additional.name
ipaddr
network.dns.answers.data
If the
ipaddr
log field value is
not
empty
then,
Iterate through log field
ipaddr
, then
ipaddr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addr
log field value is
not
empty
then,
Iterate through log field
addr
, then
addr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addrgrp
log field value is
not
empty
then,
addrgrp
log field is mapped to the
network.dns.answers.data
UDM field.
addr
network.dns.answers.data
If the
ipaddr
log field value is
not
empty
then,
Iterate through log field
ipaddr
, then
ipaddr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addr
log field value is
not
empty
then,
Iterate through log field
addr
, then
addr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addrgrp
log field value is
not
empty
then,
addrgrp
log field is mapped to the
network.dns.answers.data
UDM field.
addrgrp
network.dns.answers.data
If the
ipaddr
log field value is
not
empty
then,
Iterate through log field
ipaddr
, then
ipaddr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addr
log field value is
not
empty
then,
Iterate through log field
addr
, then
addr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addrgrp
log field value is
not
empty
then,
addrgrp
log field is mapped to the
network.dns.answers.data
UDM field.
addr_type
network.dns.answers.type
qclass
network.dns.questions.class
If the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
qclass
log field value is equal to
IN
then, the
network.dns.questions.class
UDM field is set to
1
.
qname
network.dns.questions.name
fqdn
network.dns.questions.name
qtypeval
network.dns.questions.type
from
network.email.from
If the
from
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.from
UDM field.
Else, if the
sender
log field value matches the regular expression pattern
(^.+@.+$)
then,
sender
log field is mapped to the
network.email.from
UDM field.
sender
network.email.from
If the
from
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.from
UDM field.
Else, if the
sender
log field value matches the regular expression pattern
(^.+@.+$)
then,
sender
log field is mapped to the
network.email.from
UDM field.
to
network.email.to
If the
to
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.to
UDM field.
Else, if the
recipient
log field value matches the regular expression pattern
(^.+@.+$)
then,
recipient
log field is mapped to the
network.email.to
UDM field.
recipient
network.email.to
If the
to
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.to
UDM field.
Else, if the
recipient
log field value matches the regular expression pattern
(^.+@.+$)
then,
recipient
log field is mapped to the
network.email.to
UDM field.
httpmethod
network.http.method
If the
httpmethod
log field value is
not
empty
then,
httpmethod
log field is mapped to the
network.http.method
UDM field.
Else, if the
message_type
log field value is
not
empty
then,
message_type
log field is mapped to the
network.http.method
UDM field.
message_type
network.http.method
If the
httpmethod
log field value is
not
empty
then,
httpmethod
log field is mapped to the
network.http.method
UDM field.
Else, if the
message_type
log field value is
not
empty
then,
message_type
log field is mapped to the
network.http.method
UDM field.
agent
network.http.parsed_user_agent
referralurl
network.http.referral_url
httpcode
network.http.response_code
agent
network.http.user_agent
If the
agent
log field value is
not
empty
then,
agent
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
chgheaders
log field value is
not
empty
then,
chgheaders
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
method
log field value is
not
empty
then,
method
log field is mapped to the
network.http.user_agent
UDM field.
chgheaders
network.http.user_agent
If the
agent
log field value is
not
empty
then,
agent
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
chgheaders
log field value is
not
empty
then,
chgheaders
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
method
log field value is
not
empty
then,
method
log field is mapped to the
network.http.user_agent
UDM field.
method
network.http.user_agent
If the
agent
log field value is
not
empty
then,
agent
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
chgheaders
log field value is
not
empty
then,
chgheaders
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
method
log field value is
not
empty
then,
method
log field is mapped to the
network.http.user_agent
UDM field.
service
network.ip_protocol
proto
network.ip_protocol
protocol
network.ip_protocol
probeproto
network.ip_protocol
domainctrlprotocoltype
network.ip_protocol
ip_protocol
network.ip_protocol
poolname
network.ip_subnet_range
If the
portbegin
log field value is
not
empty
and the
portend
log field value is
not
empty
then,
%{portbegin}/%{portend}
log field is mapped to the
network.ip_subnet_range
UDM field.
Else,
poolname
log field is mapped to the
network.ip_subnet_range
UDM field.
portbegin
network.ip_subnet_range
If the
portbegin
log field value is
not
empty
and the
portend
log field value is
not
empty
then,
%{portbegin}/%{portend}
log field is mapped to the
network.ip_subnet_range
UDM field.
Else,
poolname
log field is mapped to the
network.ip_subnet_range
UDM field.
portend
network.ip_subnet_range
If the
portbegin
log field value is
not
empty
and the
portend
log field value is
not
empty
then,
%{portbegin}/%{portend}
log field is mapped to the
network.ip_subnet_range
UDM field.
Else,
poolname
log field is mapped to the
network.ip_subnet_range
UDM field.
rcvdbyte
network.received_bytes
If the
rcvdbyte
log field value is
not
empty
then,
rcvdbyte
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
rcvddelta
log field value is
not
empty
then,
rcvddelta
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
lanin
log field value is
not
empty
then,
lanin
log field is mapped to the
network.received_bytes
UDM field.
rcvddelta
network.received_bytes
If the
rcvdbyte
log field value is
not
empty
then,
rcvdbyte
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
rcvddelta
log field value is
not
empty
then,
rcvddelta
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
lanin
log field value is
not
empty
then,
lanin
log field is mapped to the
network.received_bytes
UDM field.
lanin
network.received_bytes
If the
rcvdbyte
log field value is
not
empty
then,
rcvdbyte
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
rcvddelta
log field value is
not
empty
then,
rcvddelta
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
lanin
log field value is
not
empty
then,
lanin
log field is mapped to the
network.received_bytes
UDM field.
rcvdpkt
network.received_packets
If the
rcvdpkt
log field value is
not
empty
then,
rcvdpkt
log field is mapped to the
network.received_packets
UDM field.
Else, if the
rcvdpktdelta
log field value is
not
empty
then,
rcvdpktdelta
log field is mapped to the
network.received_packets
UDM field.
rcvdpktdelta
network.received_packets
If the
rcvdpkt
log field value is
not
empty
then,
rcvdpkt
log field is mapped to the
network.received_packets
UDM field.
Else, if the
rcvdpktdelta
log field value is
not
empty
then,
rcvdpktdelta
log field is mapped to the
network.received_packets
UDM field.
c-bytes
network.sent_bytes
If the
sentbyte
log field value is
not
empty
then,
sentbyte
log field is mapped to the
network.sent_bytes
UDM field.
Else, if the
c-bytes
log field value is
not
empty
then,
c-bytes
log field is mapped to the
network.sent_bytes
UDM field.
Else,
lanout
log field is mapped to the
network.sent_bytes
UDM field.
sentbyte
network.sent_bytes
If the
sentbyte
log field value is
not
empty
then,
sentbyte
log field is mapped to the
network.sent_bytes
UDM field.
Else, if the
c-bytes
log field value is
not
empty
then,
c-bytes
log field is mapped to the
network.sent_bytes
UDM field.
Else,
lanout
log field is mapped to the
network.sent_bytes
UDM field.
lanout
network.sent_bytes
If the
sentbyte
log field value is
not
empty
then,
sentbyte
log field is mapped to the
network.sent_bytes
UDM field.
Else, if the
c-bytes
log field value is
not
empty
then,
c-bytes
log field is mapped to the
network.sent_bytes
UDM field.
Else,
lanout
log field is mapped to the
network.sent_bytes
UDM field.
sentpkt
network.sent_packets
If the
sentpkt
log field value is
not
empty
then,
sentpkt
log field is mapped to the
network.sent_packets
UDM field.
Else,
eapolcnt
log field is mapped to the
network.sent_packets
UDM field.
eapolcnt
network.sent_packets
If the
sentpkt
log field value is
not
empty
then,
sentpkt
log field is mapped to the
network.sent_packets
UDM field.
Else,
eapolcnt
log field is mapped to the
network.sent_packets
UDM field.
durationdelta
network.session_duration
If the
duration
log field value does not contain one of the following values
Empty
0
then,
duration
log field is mapped to the
network.session_duration
UDM field.
Else, if the
durationdelta
log field value is
not
empty
then,
durationdelta
log field is mapped to the
network.session_duration
UDM field.
Else, if the
live
log field value is
not
empty
then,
live
log field is mapped to the
network.session_duration
UDM field.
Else, if the
totalsession
log field value is
not
empty
then,
totalsession
log field is mapped to the
network.session_duration
UDM field.
live
network.session_duration
If the
duration
log field value does not contain one of the following values
Empty
0
then,
duration
log field is mapped to the
network.session_duration
UDM field.
Else, if the
durationdelta
log field value is
not
empty
then,
durationdelta
log field is mapped to the
network.session_duration
UDM field.
Else, if the
live
log field value is
not
empty
then,
live
log field is mapped to the
network.session_duration
UDM field.
Else, if the
totalsession
log field value is
not
empty
then,
totalsession
log field is mapped to the
network.session_duration
UDM field.
duration
network.session_duration
If the
duration
log field value does not contain one of the following values
Empty
0
then,
duration
log field is mapped to the
network.session_duration
UDM field.
Else, if the
durationdelta
log field value is
not
empty
then,
durationdelta
log field is mapped to the
network.session_duration
UDM field.
Else, if the
live
log field value is
not
empty
then,
live
log field is mapped to the
network.session_duration
UDM field.
Else, if the
totalsession
log field value is
not
empty
then,
totalsession
log field is mapped to the
network.session_duration
UDM field.
totalsession
network.session_duration
If the
duration
log field value does not contain one of the following values
Empty
0
then,
duration
log field is mapped to the
network.session_duration
UDM field.
Else, if the
durationdelta
log field value is
not
empty
then,
durationdelta
log field is mapped to the
network.session_duration
UDM field.
Else, if the
live
log field value is
not
empty
then,
live
log field is mapped to the
network.session_duration
UDM field.
Else, if the
totalsession
log field value is
not
empty
then,
totalsession
log field is mapped to the
network.session_duration
UDM field.
sessionid
network.session_id
If the
sessionid
log field value is
not
empty
then,
sessionid
log field is mapped to the
network.session_id
UDM field.
Else, if the
session_id
log field value is
not
empty
then,
session_id
log field is mapped to the
network.session_id
UDM field.
Else, if the
netid
log field value is
not
empty
then,
netid
log field is mapped to the
network.session_id
UDM field.
session_id
network.session_id
If the
sessionid
log field value is
not
empty
then,
sessionid
log field is mapped to the
network.session_id
UDM field.
Else, if the
session_id
log field value is
not
empty
then,
session_id
log field is mapped to the
network.session_id
UDM field.
Else, if the
netid
log field value is
not
empty
then,
netid
log field is mapped to the
network.session_id
UDM field.
netid
network.session_id
If the
sessionid
log field value is
not
empty
then,
sessionid
log field is mapped to the
network.session_id
UDM field.
Else, if the
session_id
log field value is
not
empty
then,
session_id
log field is mapped to the
network.session_id
UDM field.
Else, if the
netid
log field value is
not
empty
then,
netid
log field is mapped to the
network.session_id
UDM field.
cipher
network.tls.cipher
scertissuer
network.tls.client.certificate.issuer
If the
scertissuer
log field value is
not
empty
then,
scertissuer
log field is mapped to the
network.tls.client.certificate.issuer
UDM field.
Else, if the
issuer
log field value is
not
empty
then,
issuer
log field is mapped to the
network.tls.client.certificate.issuer
UDM field.
issuer
network.tls.client.certificate.issuer
If the
scertissuer
log field value is
not
empty
then,
scertissuer
log field is mapped to the
network.tls.client.certificate.issuer
UDM field.
Else, if the
issuer
log field value is
not
empty
then,
issuer
log field is mapped to the
network.tls.client.certificate.issuer
UDM field.
incidentserialno
network.tls.client.certificate.serial
If the
incidentserialno
log field value is
not
empty
then,
incidentserialno
log field is mapped to the
network.tls.client.certificate.serial
UDM field.
Else, if the
cert
log field value is
not
empty
then,
cert
log field is mapped to the
network.tls.client.certificate.serial
UDM field.
cert
network.tls.client.certificate.serial
If the
incidentserialno
log field value is
not
empty
then,
incidentserialno
log field is mapped to the
network.tls.client.certificate.serial
UDM field.
Else, if the
cert
log field value is
not
empty
then,
cert
log field is mapped to the
network.tls.client.certificate.serial
UDM field.
certhash
network.tls.client.certificate.sha256
scertcname
network.tls.client.certificate.subject
If the
scertcname
log field value is
not
empty
then,
scertcname
log field is mapped to the
network.tls.client.certificate.subject
UDM field.
Else, if the
certdesc
log field value is
not
empty
then,
certdesc
log field is mapped to the
network.tls.client.certificate.subject
UDM field.
certdesc
network.tls.client.certificate.subject
If the
scertcname
log field value is
not
empty
then,
scertcname
log field is mapped to the
network.tls.client.certificate.subject
UDM field.
Else, if the
certdesc
log field value is
not
empty
then,
certdesc
log field is mapped to the
network.tls.client.certificate.subject
UDM field.
cert-type
network.tls.client.certificate.version
vd
principal.administrative_domain
If the
admin
log field value is
not
empty
then,
admin
log field is mapped to the
principal.administrative_domain
UDM field.
Else, if the
vd
log field value is
not
empty
then,
vd
log field is mapped to the
principal.administrative_domain
UDM field.
admin
principal.administrative_domain
If the
admin
log field value is
not
empty
then,
admin
log field is mapped to the
principal.administrative_domain
UDM field.
Else, if the
vd
log field value is
not
empty
then,
vd
log field is mapped to the
principal.administrative_domain
UDM field.
clientcert
principal.artifact.last_https_certificate
chassisid
principal.asset_id
If the
clientdeviceid
log field value is
not
empty
then,
Fortinet:%{clientdeviceid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
chassisid
log field value is
not
empty
then,
Fortinet:%{chassisid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
deviceExternalId
log field value is
not
empty
then,
Fortinet:%{deviceExternalId}
log field is mapped to the
principal.asset_id
UDM field.
clientdeviceid
principal.asset_id
If the
clientdeviceid
log field value is
not
empty
then,
Fortinet:%{clientdeviceid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
chassisid
log field value is
not
empty
then,
Fortinet:%{chassisid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
deviceExternalId
log field value is
not
empty
then,
Fortinet:%{deviceExternalId}
log field is mapped to the
principal.asset_id
UDM field.
deviceExternalId
principal.asset_id
If the
clientdeviceid
log field value is
not
empty
then,
Fortinet:%{clientdeviceid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
chassisid
log field value is
not
empty
then,
Fortinet:%{chassisid}
log field is mapped to the
principal.asset_id
UDM field.
Else, if the
deviceExternalId
log field value is
not
empty
then,
Fortinet:%{deviceExternalId}
log field is mapped to the
principal.asset_id
UDM field.
chassisid
principal.asset.asset_id
If the
clientdeviceid
log field value is
not
empty
then,
Fortinet:%{clientdeviceid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
chassisid
log field value is
not
empty
then,
Fortinet:%{chassisid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
deviceExternalId
log field value is
not
empty
then,
Fortinet:%{deviceExternalId}
log field is mapped to the
principal.asset.asset_id
UDM field.
clientdeviceid
principal.asset.asset_id
If the
clientdeviceid
log field value is
not
empty
then,
Fortinet:%{clientdeviceid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
chassisid
log field value is
not
empty
then,
Fortinet:%{chassisid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
deviceExternalId
log field value is
not
empty
then,
Fortinet:%{deviceExternalId}
log field is mapped to the
principal.asset.asset_id
UDM field.
deviceExternalId
principal.asset.asset_id
If the
clientdeviceid
log field value is
not
empty
then,
Fortinet:%{clientdeviceid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
chassisid
log field value is
not
empty
then,
Fortinet:%{chassisid}
log field is mapped to the
principal.asset.asset_id
UDM field.
Else, if the
deviceExternalId
log field value is
not
empty
then,
Fortinet:%{deviceExternalId}
log field is mapped to the
principal.asset.asset_id
UDM field.
clientdeviceems
principal.asset.attribute.labels[clientdeviceems]
clientdevicemanageable
principal.asset.attribute.labels[clientdevicemanageable]
clientdeviceowner
principal.asset.attribute.labels[clientdeviceowner]
clientdevicetags
principal.asset.attribute.labels[clientdevicetags]
manuf
principal.asset.attribute.labels[manuf]
srcintf
principal.asset.attribute.labels[srcintf]
srcintfrole
principal.asset.attribute.labels[srcintfrole]
srcmacvendor
principal.asset.attribute.labels[srcmacvendor]
srcssid
principal.asset.attribute.labels[srcssid]
ssid
principal.asset.attribute.labels[ssid]
versionmax
principal.asset.attribute.labels[versionmax]
versionmin
principal.asset.attribute.labels[versionmin]
srchwvendor
principal.asset.hardware.manufacturer
If the
srchwvendor
log field value is
not
empty
then,
srchwvendor
log field is mapped to the
principal.asset.hardware.manufacturer
UDM field.
Else, if the
srcmacvendor
log field value is
not
empty
then,
srcmacvendor
log field is mapped to the
principal.asset.hardware.manufacturer
UDM field.
srcmacvendor
principal.asset.hardware.manufacturer
If the
srchwvendor
log field value is
not
empty
then,
srchwvendor
log field is mapped to the
principal.asset.hardware.manufacturer
UDM field.
Else, if the
srcmacvendor
log field value is
not
empty
then,
srcmacvendor
log field is mapped to the
principal.asset.hardware.manufacturer
UDM field.
peer
principal.asset.hardware.model
srchwversion
principal.asset.hardware.model
If the
srchwversion
log field value is
not
empty
then,
srchwversion
log field is mapped to the
principal.asset.hardware.model
UDM field.
devid
intermediary.asset.hardware.serial_number
If the
devid
log field value is
not
empty
and if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then,
devid
log field is mapped to the
principal.asset.hardware.serial_number
UDM field. Else,
devid
log field is mapped to the
intermediary.asset.hardware.serial_number
UDM field.
hostname
principal.asset.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.asset.hostname
UDM field.
srcname
principal.asset.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.asset.hostname
UDM field.
name
principal.asset.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.asset.hostname
UDM field.
client_addr
principal.asset.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.asset.hostname
UDM field.
banned_src
principal.asset.ip
remote
principal.asset.ip
user_email
principal.asset.ip
userfrom
principal.asset.ip
loc_ip
principal.asset.ip
srcregion
principal.asset.location.country_or_region
tamac
principal.asset.mac
saasname
principal.asset.software.description
saasapp
principal.asset.software.name
devtype
principal.asset.category
new_value
principal.domain.name
sender
principal.email
file
principal.file.full_path
checksum
principal.file.sha256
filesize
principal.file.size
filetype
principal.file.mime_type
adgroup
principal.group.group_display_name
groupid
principal.group.product_object_id
hostname
principal.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
client_addr
log field value is
not
empty
then,
client_addr
log field is mapped to the
principal.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.hostname
UDM field.
srcname
principal.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
client_addr
log field value is
not
empty
then,
client_addr
log field is mapped to the
principal.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.hostname
UDM field.
name
principal.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
client_addr
log field value is
not
empty
then,
client_addr
log field is mapped to the
principal.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.hostname
UDM field.
client_addr
principal.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
client_addr
log field value is
not
empty
then,
client_addr
log field is mapped to the
principal.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.hostname
UDM field.
ui
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
saddr
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
srcremote
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
shost
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
user
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
ip
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
locip
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
banned_src
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
local
principal.ip
user_email
principal.ip
userfrom
principal.ip
loc_ip
principal.ip
forwardedfor
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
ui
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
ip
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
user
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
locip
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
srccity
principal.ip_location.city
srccountry
principal.location.country_or_region
If the
srccountry
log field value is
not
empty
and the
srccountry
log field value is
not
equal to
Reserved
then,
srccountry
log field is mapped to the
principal.location.country_or_region
UDM field.
uli
principal.location.name
mac
principal.mac
If the
srcmac
log field value is
not
empty
then,
srcmac
log field is mapped to the
principal.mac
UDM field and
srcmac
log field is mapped to the
principal.asset.mac
UDM field.
Else, if the
mac
log field value is
not
empty
then,
mac
log field is mapped to the
principal.mac
UDM field and
mac
log field is mapped to the
principal.asset.mac
UDM field.
srcmac
principal.mac
If the
srcmac
log field value is
not
empty
then,
srcmac
log field is mapped to the
principal.mac
UDM field and
srcmac
log field is mapped to the
principal.asset.mac
UDM field.
Else, if the
mac
log field value is
not
empty
then,
mac
log field is mapped to the
principal.mac
UDM field and
mac
log field is mapped to the
principal.asset.mac
UDM field.
transip
principal.nat_ip
transport
principal.nat_port
principal.platform
If the
osname
log field value matches the regular expression pattern
(?i)WINDOWS
then, the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
osname
log field value matches the regular expression pattern
(?i)ANDROID
then, the
principal.platform
UDM field is set to
ANDROID
.
Else, if the
osname
log field value matches the regular expression pattern
(?i)LINUX
then, the
principal.platform
UDM field is set to
LINUX
.
Else, if the
osname
log field value matches the regular expression pattern
(?i)MAC
then, the
principal.platform
UDM field is set to
MAC
.
srcswversion
principal.platform_version
If the
osname
log field value matches the regular expression pattern
(?i)WINDOWS
and if the
osversion
log field value is
not
empty
then,
osversion
log field is mapped to the
principal.platform_version
UDM field.
If the
srcswversion
log field value is
not
empty
then,
srcswversion
log field is mapped to the
principal.platform_version
UDM field.
If the
os
log field value matches the regular expression pattern
.
Windows.
then, The
os_version
field is extracted from
os
log field using the Grok pattern.
os_version
log field is mapped to the
principal.platform_version
UDM field.
osversion
principal.platform_version
If the
osname
log field value matches the regular expression pattern
(?i)WINDOWS
and if the
osversion
log field value is
not
empty
then,
osversion
log field is mapped to the
principal.platform_version
UDM field.
If the
srcswversion
log field value is
not
empty
then,
srcswversion
log field is mapped to the
principal.platform_version
UDM field.
If the
os
log field value matches the regular expression pattern
.
Windows.
then, The
os_version
field is extracted from
os
log field using the Grok pattern.
os_version
log field is mapped to the
principal.platform_version
UDM field.
src_port
principal.port
If the
src_port
log field value is
not
empty
then,
src_port
log field is mapped to the
principal.port
UDM field.
Else, if the
remport
log field value is
not
empty
then,
remport
log field is mapped to the
principal.port
UDM field.
Else, if the
srcport
log field value is
not
empty
then,
srcport
log field is mapped to the
principal.port
UDM field.
Else, if the
port
log field value is
not
empty
then,
port
log field is mapped to the
principal.port
UDM field.
remport
principal.port
If the
src_port
log field value is
not
empty
then,
src_port
log field is mapped to the
principal.port
UDM field.
Else, if the
remport
log field value is
not
empty
then,
remport
log field is mapped to the
principal.port
UDM field.
Else, if the
srcport
log field value is
not
empty
then,
srcport
log field is mapped to the
principal.port
UDM field.
Else, if the
port
log field value is
not
empty
then,
port
log field is mapped to the
principal.port
UDM field.
port
principal.port
If the
src_port
log field value is
not
empty
then,
src_port
log field is mapped to the
principal.port
UDM field.
Else, if the
remport
log field value is
not
empty
then,
remport
log field is mapped to the
principal.port
UDM field.
Else, if the
srcport
log field value is
not
empty
then,
srcport
log field is mapped to the
principal.port
UDM field.
Else, if the
port
log field value is
not
empty
then,
port
log field is mapped to the
principal.port
UDM field.
srcport
principal.port
If the
src_port
log field value is
not
empty
then,
src_port
log field is mapped to the
principal.port
UDM field.
Else, if the
remport
log field value is
not
empty
then,
remport
log field is mapped to the
principal.port
UDM field.
Else, if the
srcport
log field value is
not
empty
then,
srcport
log field is mapped to the
principal.port
UDM field.
Else, if the
port
log field value is
not
empty
then,
port
log field is mapped to the
principal.port
UDM field.
srcname
principal.process.command_line
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is equal to
appfirewall
and the
subtype
log field value is
not
equal to
system
then,
srcname
log field is mapped to the
principal.process.command_line
UDM field.
pid
principal.process.pid
advpnsc
principal.resource.attribute.labels[advpnsc]
assignip
principal.resource.attribute.labels[assignip]
cloudaction
principal.resource.attribute.labels[cloudaction]
cookies
principal.resource.attribute.labels[cookies]
init
principal.resource.attribute.labels[init]
initiator
principal.resource.attribute.labels[initiator]
login
principal.resource.attribute.labels[login]
nextstat
principal.resource.attribute.labels[nextstat]
outintf
principal.resource.attribute.labels[outintf]
ratemethod
principal.resource.attribute.labels[ratemethod]
rcvdbyte
principal.resource.attribute.labels[rcvdbyte]
reqtype
principal.resource.attribute.labels[reqtype]
role
principal.resource.attribute.labels[role]
servername
principal.resource.attribute.labels[servername]
serverresponsetime
principal.resource.attribute.labels[serverresponsetime]
serviceid
principal.resource.attribute.labels[serviceid]
src_int
principal.resource.attribute.labels[src_int]
srcdomain
principal.resource.attribute.labels[srcdomain]
srcfamily
principal.resource.attribute.labels[srcfamily]
srcreputation
principal.resource.attribute.labels[srcreputation]
srcthreatfeed
principal.resource.attribute.labels[srcthreatfeed]
stage
principal.resource.attribute.labels[stage]
tunnelid
principal.resource.attribute.labels[tunnelid]
tunneltype
principal.resource.attribute.labels[tunneltype]
unauthuser
principal.resource.attribute.labels[unauthuser]
useralt
principal.resource.attribute.labels[useralt]
vd
principal.resource.attribute.labels[vd]
vpntunnel
principal.resource.attribute.labels[vpntunnel]
xauthgroup
principal.resource.attribute.labels[xauthgroup]
xauthuser
principal.resource.attribute.labels[xauthuser]
clouddevice
principal.resource.name
If the
clouddevice
log field value is
not
empty
then,
clouddevice
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
servername
log field value is
not
empty
then,
servername
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
src_int
log field value is
not
empty
then,
src_int
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
srcdomain
log field value is
not
empty
then,
srcdomain
log field is mapped to the
principal.resource.name
UDM field.
servername
principal.resource.name
If the
clouddevice
log field value is
not
empty
then,
clouddevice
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
servername
log field value is
not
empty
then,
servername
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
src_int
log field value is
not
empty
then,
src_int
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
srcdomain
log field value is
not
empty
then,
srcdomain
log field is mapped to the
principal.resource.name
UDM field.
src_int
principal.resource.name
If the
clouddevice
log field value is
not
empty
then,
clouddevice
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
servername
log field value is
not
empty
then,
servername
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
src_int
log field value is
not
empty
then,
src_int
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
srcdomain
log field value is
not
empty
then,
srcdomain
log field is mapped to the
principal.resource.name
UDM field.
srcdomain
principal.resource.name
If the
clouddevice
log field value is
not
empty
then,
clouddevice
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
servername
log field value is
not
empty
then,
servername
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
src_int
log field value is
not
empty
then,
src_int
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
srcdomain
log field value is
not
empty
then,
srcdomain
log field is mapped to the
principal.resource.name
UDM field.
cldobjid
principal.resource.product_object_id
If the
srcuuid
log field value is
not
empty
then,
srcuuid
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
serveraddr
log field value is
not
empty
then,
serveraddr
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
cldobjid
log field value is
not
empty
then,
cldobjid
log field is mapped to the
principal.resource.product_object_id
UDM field.
If the
cldobjid
log field value is
not
empty
or the
serveraddr
log field value is
not
empty
or the
srcuuid
log field value is
not
empty
then, the
principal.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
serveraddr
principal.resource.product_object_id
If the
srcuuid
log field value is
not
empty
then,
srcuuid
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
serveraddr
log field value is
not
empty
then,
serveraddr
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
cldobjid
log field value is
not
empty
then,
cldobjid
log field is mapped to the
principal.resource.product_object_id
UDM field.
If the
cldobjid
log field value is
not
empty
or the
serveraddr
log field value is
not
empty
or the
srcuuid
log field value is
not
empty
then, the
principal.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
srcuuid
principal.resource.product_object_id
If the
srcuuid
log field value is
not
empty
then,
srcuuid
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
serveraddr
log field value is
not
empty
then,
serveraddr
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
cldobjid
log field value is
not
empty
then,
cldobjid
log field is mapped to the
principal.resource.product_object_id
UDM field.
If the
cldobjid
log field value is
not
empty
or the
serveraddr
log field value is
not
empty
or the
srcuuid
log field value is
not
empty
then, the
principal.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
new_status
principal.user.attribute.labels[new_status]
old_status
principal.user.attribute.labels[old_status]
passwd
principal.user.attribute.labels[passwd]
peer_notif
principal.user.attribute.labels[peer_notif]
profiletype
principal.user.attribute.labels[profiletype]
ulimcc
principal.user.attribute.labels[ulimcc]
ulimnc
principal.user.attribute.labels[ulimnc]
user_data
principal.user.attribute.labels[user_data]
useractivity
principal.user.attribute.labels[useractivity]
group
principal.user.group_identifiers
If the
group
log field value is
not
empty
and the
group
log field value is
not
equal to
N/A
then,
group
log field is mapped to the
principal.user.group_identifiers
UDM field.
Else, if the
community
log field value is
not
empty
then,
community
log field is mapped to the
principal.user.group_identifiers
UDM field.
community
principal.user.group_identifiers
If the
group
log field value is
not
empty
and the
group
log field value is
not
equal to
N/A
then,
group
log field is mapped to the
principal.user.group_identifiers
UDM field.
Else, if the
community
log field value is
not
empty
then,
community
log field is mapped to the
principal.user.group_identifiers
UDM field.
msisdn
principal.user.phone_numbers
If the
msisdn
log field value is
not
empty
then,
msisdn
log field is mapped to the
principal.user.phone_numbers
UDM field.
Else, if the
phone
log field value is
not
empty
then,
phone
log field is mapped to the
principal.user.phone_numbers
UDM field.
phone
principal.user.phone_numbers
If the
msisdn
log field value is
not
empty
then,
msisdn
log field is mapped to the
principal.user.phone_numbers
UDM field.
Else, if the
phone
log field value is
not
empty
then,
phone
log field is mapped to the
principal.user.phone_numbers
UDM field.
user
principal.user.user_display_name
If the
user
log field value does not contain one of the following values
Empty
N/A
then,
user
log field is mapped to the
principal.user.user_display_name
UDM field.
Else, if the
cn
log field value is
not
empty
then,
cn
log field is mapped to the
principal.user.user_display_name
UDM field.
If the
suser
log field value is
not
empty
and the
suser
log field value does not match the regular expression pattern
^{
then,
suser
log field is mapped to the
principal.user.user_display_name
UDM field.
cn
principal.user.user_display_name
If the
user
log field value does not contain one of the following values
Empty
N/A
then,
user
log field is mapped to the
principal.user.user_display_name
UDM field.
Else, if the
cn
log field value is
not
empty
then,
cn
log field is mapped to the
principal.user.user_display_name
UDM field.
If the
suser
log field value is
not
empty
and the
suser
log field value does not match the regular expression pattern
^{
then,
suser
log field is mapped to the
principal.user.user_display_name
UDM field.
suser
principal.user.user_display_name
If the
user
log field value does not contain one of the following values
Empty
N/A
then,
user
log field is mapped to the
principal.user.user_display_name
UDM field.
Else, if the
cn
log field value is
not
empty
then,
cn
log field is mapped to the
principal.user.user_display_name
UDM field.
If the
suser
log field value is
not
empty
and the
suser
log field value does not match the regular expression pattern
^{
then,
suser
log field is mapped to the
principal.user.user_display_name
UDM field.
user
principal.user.userid
If the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
then,
initiator
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
then,
login
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
then,
unauthuser
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
vd
log field is mapped to the
principal.user.userid
UDM field.
vd
principal.user.userid
If the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
then,
initiator
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
then,
login
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
then,
unauthuser
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
vd
log field is mapped to the
principal.user.userid
UDM field.
clouduser
principal.user.userid
If the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
then,
initiator
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
then,
login
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
then,
unauthuser
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
vd
log field is mapped to the
principal.user.userid
UDM field.
initiator
principal.user.userid
If the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
then,
initiator
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
then,
login
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
then,
unauthuser
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
vd
log field is mapped to the
principal.user.userid
UDM field.
login
principal.user.userid
If the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
then,
initiator
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
then,
login
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
then,
unauthuser
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
vd
log field is mapped to the
principal.user.userid
UDM field.
unauthuser
principal.user.userid
If the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
then,
initiator
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
then,
login
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
then,
unauthuser
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
vd
log field is mapped to the
principal.user.userid
UDM field.
botnetdomain
security_result.about.hostname
botnetip
security_result.about.ip
security_result.action
If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then, the
security_result.action
UDM field is set to
BLOCK
.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then, the
security_result.action
UDM field is set to
BLOCK
.
Else, If the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.action
UDM field is set to
FAIL
.
If the
operation
log field value is
not
empty
and if the
operation
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
edit
then, the
security_result.action
UDM field is set to
ALLOW
. Else, if the
operation
log field value contain one of the following values
deny
dropped
blocked
then, the
security_result.action
UDM field is set to
BLOCK
. Else, if the
operation
log field value is equal to
timeout
then, the
security_result.action
UDM field is set to
FAIL
.
Else, if the
icbaction
log field value is
not
empty
then, if the
icbaction
log field value matches the regular expression pattern
allow
then, the
security_result.action
UDM field is set to
ALLOW
. Else, if the
icbaction
log field value matches the regular expression pattern
block
then, the
security_result.action
UDM field is set to
BLOCK
. Else, if the
icbaction
log field value matches the regular expression pattern
fail
then, the
security_result.action
UDM field is set to
BLOCK
.
operation
security_result.action_details
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
icbaction
security_result.action_details
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
action
security_result.action_details
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
utmaction
security_result.action_details
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
attackid
security_result.attack_details.tactics.id
attack
security_result.attack_details.tactics.name
attackcontextid
security_result.attack_details.techniques.id
attackcontext
security_result.attack_details.techniques.name
craction
security_result.about.labels[craction]
incidentserialno
security_result.about.labels[incidentserialno]
accessctrl
security_result.detection_fields[accessctrl]
accessproxy
security_result.detection_fields[accessproxy]
acct_stat
security_result.detection_fields[acct_stat]
acktime
security_result.detection_fields[acktime]
activity
security_result.detection_fields[activity]
activitycategory
security_result.detection_fields[activitycategory]
age
security_result.detection_fields[age]
alarmid
security_result.detection_fields[alarmid]
antiphishdc
security_result.detection_fields[antiphishdc]
antiphishrule
security_result.detection_fields[antiphishrule]
ap
security_result.detection_fields[ap]
apn
security_result.detection_fields[apn]
app-type
security_result.detection_fields[app-type]
apperror
security_result.detection_fields[apperror]
appid
security_result.detection_fields[appid]
apscan
security_result.detection_fields[apscan]
apsn
security_result.detection_fields[apsn]
apstatus
security_result.detection_fields[apstatus]
aptype
security_result.detection_fields[aptype]
attack
security_result.detection_fields[attack]
attackid
security_result.detection_fields[attackid]
auditid
security_result.detection_fields[auditid]
auditreporttype
security_result.detection_fields[auditreporttype]
audittime
security_result.detection_fields[audittime]
authalgo
security_result.detection_fields[authalgo]
authgrp
security_result.detection_fields[authgrp]
authid
security_result.detection_fields[authid]
authserver
security_result.detection_fields[authserver]
banword
security_result.detection_fields[banword]
bssid
security_result.detection_fields[bssid]
c-bytes
security_result.detection_fields[c-bytes]
c-ggsn-teid
security_result.detection_fields[c-ggsn-teid]
c-gsn
security_result.detection_fields[c-gsn]
c-pkts
security_result.detection_fields[c-pkts]
c-sgsn-teid
security_result.detection_fields[c-sgsn-teid]
c-sgsn
security_result.detection_fields[c-sgsn]
call_id
security_result.detection_fields[call_id]
carrier_ep
security_result.detection_fields[carrier_ep]
cat
security_result.detection_fields[cat]
catdesc
security_result.detection_fields[catdesc]
cc
security_result.detection_fields[cc]
ccertissuer
security_result.detection_fields[ccertissuer]
cdrcontent
security_result.detection_fields[cdrcontent]
centralnatid
security_result.detection_fields[centralnatid]
cfgtid
security_result.detection_fields[cfgtid]
cfgtxpower
security_result.detection_fields[cfgtxpower]
cfseid
security_result.detection_fields[cfseid]
cfseidaddr
security_result.detection_fields[cfseidaddr]
cggsn6
security_result.detection_fields[cggsn6]
cgsn6
security_result.detection_fields[cgsn6]
channel
security_result.detection_fields[channel]
channeltype
security_result.detection_fields[channeltype]
clashtunnelidx
security_result.detection_fields[clashtunnelidx]
client_addr
security_result.detection_fields[client_addr]
command
security_result.detection_fields[command]
configcountry
security_result.detection_fields[configcountry]
connector
security_result.detection_fields[connector]
conserve
security_result.detection_fields[conserve]
constraint
security_result.detection_fields[constraint]
contentdisarmed
security_result.detection_fields[contentdisarmed]
contentencoding
security_result.detection_fields[contentencoding]
contenttype
security_result.detection_fields[contenttype]
countav
security_result.detection_fields[countav]
countcasb
security_result.detection_fields[countcasb]
countcifs
security_result.detection_fields[countcifs]
countdlp
security_result.detection_fields[countdlp]
countdns
security_result.detection_fields[countdns]
countemail
security_result.detection_fields[countemail]
countff
security_result.detection_fields[countff]
counticap
security_result.detection_fields[counticap]
countsctpf
security_result.detection_fields[countsctpf]
countssh
security_result.detection_fields[countssh]
countssl
security_result.detection_fields[countssl]
countvpatch
security_result.detection_fields[countvpatch]
countwaf
security_result.detection_fields[countwaf]
countweb
security_result.detection_fields[countweb]
criticalcount
security_result.detection_fields[criticalcount]
crlevel
security_result.detection_fields[crlevel]
csgsn6
security_result.detection_fields[csgsn6]
cveid
security_result.detection_fields[cveid]
daemon
security_result.detection_fields[daemon]
desc
security_result.detection_fields[desc]
deviceSeverity
security_result.detection_fields[deviceSeverity]
direction
security_result.detection_fields[direction]
domainctrlauthtype
security_result.detection_fields[domainctrlauthtype]
dstcountry
security_result.detection_fields[dstcountry]
dstinetsvc
security_result.detection_fields[dstinetsvc]
eventtype
security_result.detection_fields[eventtype]
filehashsrc
security_result.detection_fields[filehashsrc]
filtertype
security_result.detection_fields[filtertype]
fsaverdict
security_result.detection_fields[fsaverdict]
highcount
security_result.detection_fields[highcount]
icbaction
security_result.detection_fields[icbaction]
imei-sv
security_result.detection_fields[imei-sv]
imsi
security_result.detection_fields[imsi]
in_spi
security_result.detection_fields[in_spi]
inbandwidthavailable
security_result.detection_fields[inbandwidthavailable]
inbandwidthused
security_result.detection_fields[inbandwidthused]
infectedfilelevel
security_result.detection_fields[infectedfilelevel]
informationsource
security_result.detection_fields[informationsource]
keyalgo
security_result.detection_fields[keyalgo]
keysize
security_result.detection_fields[keysize]
kind
security_result.detection_fields[kind]
kxcurve
security_result.detection_fields[kxcurve]
kxproto
security_result.detection_fields[kxproto]
lanin
security_result.detection_fields[lanin]
lanout
security_result.detection_fields[lanout]
level
security_result.detection_fields[level]
live
security_result.detection_fields[live]
lowcount
security_result.detection_fields[lowcount]
malforn_data
security_result.detection_fields[malforn_data]
mediumcount
security_result.detection_fields[mediumcount]
mgmtcnt
security_result.detection_fields[mgmtcnt]
mode
security_result.detection_fields[mode]
msg
security_result.detection_fields[msg]
neighbor
security_result.detection_fields[neighbor]
networktransfertime
security_result.detection_fields[networktransfertime]
newchannel
security_result.detection_fields[newchannel]
newchassisid
security_result.detection_fields[newchassisid]
newslot
security_result.detection_fields[newslot]
newvalue
security_result.detection_fields[newvalue]
noise
security_result.detection_fields[noise]
notafter
security_result.detection_fields[notafter]
notbefore
security_result.detection_fields[notbefore]
numpassmember
security_result.detection_fields[numpassmember]
oldchannel
security_result.detection_fields[oldchannel]
oldchassisid
security_result.detection_fields[oldchassisid]
oldslot
security_result.detection_fields[oldslot]
oldvalue
security_result.detection_fields[oldvalue]
oldwprof
security_result.detection_fields[oldwprof]
onwire
security_result.detection_fields[onwire]
operation
security_result.detection_fields[operation]
operdrmamode
security_result.detection_fields[operdrmamode]
opertxpower
security_result.detection_fields[opertxpower]
out_spi
security_result.detection_fields[out_spi]
outbandwidthavailable
security_result.detection_fields[outbandwidthavailable]
outbandwidthused
security_result.detection_fields[outbandwidthused]
packetloss
security_result.detection_fields[packetloss]
parameters
security_result.detection_fields[parameters]
passedcount
security_result.detection_fields[passedcount]
pathname
security_result.detection_fields[pathname]
phase2_name
security_result.detection_fields[phase2_name]
policyid
security_result.detection_fields[policyid]
poluuid
security_result.detection_fields[poluuid]
processtime
security_result.detection_fields[processtime]
qclass
security_result.detection_fields[qclass]
qtype
security_result.detection_fields[qtype]
qtypeval
security_result.detection_fields[qtypeval]
quarskip
security_result.detection_fields[quarskip]
quotaexceeded
security_result.detection_fields[quotaexceeded]
quotamax
security_result.detection_fields[quotamax]
quotatype
security_result.detection_fields[quotatype]
quotaused
security_result.detection_fields[quotaused]
radioband
security_result.detection_fields[radioband]
radioid
security_result.detection_fields[radioid]
radioidclosest
security_result.detection_fields[radioidclosest]
radioiddetected
security_result.detection_fields[radioiddetected]
rai
security_result.detection_fields[rai]
rat-type
security_result.detection_fields[rat-type]
rate
security_result.detection_fields[rate]
rawdata
security_result.detection_fields[rawdata]
rawdataid
security_result.detection_fields[rawdataid]
rcode
security_result.detection_fields[rcode]
rcvddelta
security_result.detection_fields[rcvddelta]
rcvdpktdelta
security_result.detection_fields[rcvdpktdelta]
reason
security_result.detection_fields[reason]
remotetunnelid
security_result.detection_fields[remotetunnelid]
remotewtptime
security_result.detection_fields[remotewtptime]
replydstintf
security_result.detection_fields[replydstintf]
replysrcintf
security_result.detection_fields[replysrcintf]
reporttype
security_result.detection_fields[reporttype]
reqlength
security_result.detection_fields[reqlength]
reqtime
security_result.detection_fields[reqtime]
respfinishtime
security_result.detection_fields[respfinishtime]
san
security_result.detection_fields[san]
scantime
security_result.detection_fields[scantime]
scheme
security_result.detection_fields[scheme]
scope
security_result.detection_fields[scope]
security
security_result.detection_fields[security]
icbconfidence
security_result.detection_fields[icbconfidence]
selection
security_result.detection_fields[selection]
sensitivity
security_result.detection_fields[sensitivity]
sentdelta
security_result.detection_fields[sentdelta]
sentpktdelta
security_result.detection_fields[sentpktdelta]
seq
security_result.detection_fields[seq]
seqnum
security_result.detection_fields[seqnum]
serial
security_result.detection_fields[serial]
serialno
security_result.detection_fields[serialno]
setuprate
security_result.detection_fields[setuprate]
shaperperipdropbyte
security_result.detection_fields[shaperperipdropbyte]
shaperperipname
security_result.detection_fields[shaperperipname]
sharename
security_result.detection_fields[sharename]
signal
security_result.detection_fields[signal]
size
security_result.detection_fields[size]
ski
security_result.detection_fields[ski]
slamap
security_result.detection_fields[slamap]
slatargetid
security_result.detection_fields[slatargetid]
slctdrmamode
security_result.detection_fields[slctdrmamode]
slot
security_result.detection_fields[slot]
sn
security_result.detection_fields[sn]
snclosest
security_result.detection_fields[snclosest]
sndetected
security_result.detection_fields[sndetected]
snetwork
security_result.detection_fields[snetwork]
sni
security_result.detection_fields[sni]
snmeshparent
security_result.detection_fields[snmeshparent]
snprev
security_result.detection_fields[snprev]
snr
security_result.detection_fields[snr]
source_mac
security_result.detection_fields[source_mac]
speedtestserver
security_result.detection_fields[speedtestserver]
spi
security_result.detection_fields[spi]
srccountry
security_result.detection_fields[srccountry]
srcinetsvc
security_result.detection_fields[srcinetsvc]
srcname
security_result.detection_fields[srcname]
sscname
security_result.detection_fields[sscname]
sslaction
security_result.detection_fields[sslaction]
stacount
security_result.detection_fields[stacount]
stamac
security_result.detection_fields[stamac]
state
security_result.detection_fields[state]
status
security_result.detection_fields[status]
statuscode
security_result.detection_fields[statuscode]
stitch
security_result.detection_fields[stitch]
stitchaction
security_result.detection_fields[stitchaction]
subaction
security_result.detection_fields[subaction]
submodule
security_result.detection_fields[submodule]
subservice
security_result.detection_fields[subservice]
switchaclid
security_result.detection_fields[switchaclid]
switchautoip
security_result.detection_fields[switchautoip]
switchid
security_result.detection_fields[switchid]
switchinterface
security_result.detection_fields[switchinterface]
switchl2capacity
security_result.detection_fields[switchl2capacity]
switchl2count
security_result.detection_fields[switchl2count]
switchmirrorsession
security_result.detection_fields[switchmirrorsession]
switchphysicalport
security_result.detection_fields[switchphysicalport]
switchproto
security_result.detection_fields[switchproto]
switchsysteminterface
security_result.detection_fields[switchsysteminterface]
switchtrunk
security_result.detection_fields[switchtrunk]
switchtrunkinterface
security_result.detection_fields[switchtrunkinterface]
sync_status
additional.fields[sync_status]
sync_type
additional.fields[sync_type]
tcpnrt
security_result.detection_fields[tcpnrt]
tcporgrtrs
security_result.detection_fields[tcporgrtrs]
tcprplrtrs
security_result.detection_fields[tcprplrtrs]
tcprst
security_result.detection_fields[tcprst]
tcpsrt
security_result.detection_fields[tcpsrt]
tcpsynackrtrs
security_result.detection_fields[tcpsynackrtrs]
tcpsynrtrs
security_result.detection_fields[tcpsynrtrs]
tenantmatch
security_result.detection_fields[tenantmatch]
threattype
security_result.detection_fields[threattype]
ticket
security_result.detection_fields[ticket]
timeoutdelete
security_result.detection_fields[timeoutdelete]
tlsver
security_result.detection_fields[tlsver]
to6
security_result.detection_fields[to6]
total
security_result.detection_fields[total]
trace_id
security_result.detection_fields[trace_id]
transid
security_result.detection_fields[transid]
translationid
security_result.detection_fields[translationid]
trigger
security_result.detection_fields[trigger]
trueclntip
security_result.detection_fields[trueclntip]
u-bytes
security_result.detection_fields[u-bytes]
u-ggsn-teid
security_result.detection_fields[u-ggsn-teid]
u-ggsn
security_result.detection_fields[u-ggsn]
u-gsn
security_result.detection_fields[u-gsn]
u-pkts
security_result.detection_fields[u-pkts]
u-sgsn-teid
security_result.detection_fields[u-sgsn-teid]
u-sgsn
security_result.detection_fields[u-sgsn]
ufseid
security_result.detection_fields[ufseid]
ufseidaddr
security_result.detection_fields[ufseidaddr]
uggsn6
security_result.detection_fields[uggsn6]
ugsn6
security_result.detection_fields[ugsn6]
unauthusersource
security_result.detection_fields[unauthusersource]
upbandwidthmeasured
security_result.detection_fields[upbandwidthmeasured]
upgradedevice
security_result.detection_fields[upgradedevice]
upteid
security_result.detection_fields[upteid]
urlfilteridx
security_result.detection_fields[urlfilteridx]
urlfilterlist
security_result.detection_fields[urlfilterlist]
urlrisk
security_result.detection_fields[urlrisk]
urlsource
security_result.detection_fields[urlsource]
urltype
security_result.detection_fields[urltype]
used
security_result.detection_fields[used]
usgsn6
security_result.detection_fields[usgsn6]
utmaction
security_result.detection_fields[utmaction]
vap
security_result.detection_fields[vap]
vapmode
security_result.detection_fields[vapmode]
vcluster_member
security_result.detection_fields[vcluster_member]
vcluster_state
security_result.detection_fields[vcluster_state]
vcluster
security_result.detection_fields[vcluster]
vdname
security_result.detection_fields[vdname]
vendor
security_result.detection_fields[vendor]
vendorurl
security_result.detection_fields[vendorurl]
videocategoryid
security_result.detection_fields[videocategoryid]
videocategoryname
security_result.detection_fields[videocategoryname]
videochannelid
security_result.detection_fields[videochannelid]
videodesc
security_result.detection_fields[videodesc]
videoid
security_result.detection_fields[videoid]
videoinfosource
security_result.detection_fields[videoinfosource]
videotitle
security_result.detection_fields[videotitle]
violations
security_result.detection_fields[violations]
vip
security_result.detection_fields[vip]
virus
security_result.detection_fields[virus]
viruscat
security_result.detection_fields[viruscat]
vlan
security_result.detection_fields[vlan]
voip_proto
security_result.detection_fields[voip_proto]
vrf
security_result.detection_fields[vrf]
vulncat
security_result.detection_fields[vulncat]
vulncnt
security_result.detection_fields[vulncnt]
vulnid
security_result.detection_fields[vulnid]
vulnname
security_result.detection_fields[vulnname]
vulnresult
security_result.detection_fields[vulnresult]
vwlname
security_result.detection_fields[vwlname]
vwlquality
security_result.detection_fields[vwlquality]
vwlservice
security_result.detection_fields[vwlservice]
vwpvlanid
security_result.detection_fields[vwpvlanid]
wanoptapptype
security_result.detection_fields[wanoptapptype]
wanout
security_result.detection_fields[wanout]
weakwepiv
security_result.detection_fields[weakwepiv]
webmailprovider
security_result.detection_fields[webmailprovider]
wscode
security_result.detection_fields[wscode]
xid
security_result.detection_fields[xid]
dtype
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
category
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
cat
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
attack
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
catdesc
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
filtercat
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
icbverdict
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
infection
security_result.category_details
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
auditscore
security_result.confidence
If the
auditscore
log field value is
not
empty
and if the
auditscore
log field value <=
33
then, the
security_result.confidence
UDM field is set to
LOW_CONFIDENCE
. Else, if the
auditscore
log field value <
67
then, the
security_result.confidence
UDM field is set to
MEDIUM_CONFIDENCE
. Else, if the
auditscore
log field value >=
67
then, the
security_result.confidence
UDM field is set to
HIGH_CONFIDENCE
.
path
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
result
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
reason
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
fortiguardresp
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
malform_desc
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
msg
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
catdesc
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
dstreputation
security_result.risk_score
attackid
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
cat
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
ruleid
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
appid
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
policyid
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
poluuid
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
policytype
security_result.rule_type
If the
policytype
log field value is
not
empty
then,
policytype
log field is mapped to the
security_result.rule_type
UDM field.
Else, if the
eventtype
log field value is
not
empty
then,
eventtype
log field is mapped to the
security_result.rule_type
UDM field.
Else, if the
filtertype
log field value is
not
empty
then,
filtertype
log field is mapped to the
security_result.rule_type
UDM field.
eventtype
security_result.rule_type
If the
policytype
log field value is
not
empty
then,
policytype
log field is mapped to the
security_result.rule_type
UDM field.
Else, if the
eventtype
log field value is
not
empty
then,
eventtype
log field is mapped to the
security_result.rule_type
UDM field.
Else, if the
filtertype
log field value is
not
empty
then,
filtertype
log field is mapped to the
security_result.rule_type
UDM field.
filtertype
security_result.rule_type
If the
policytype
log field value is
not
empty
then,
policytype
log field is mapped to the
security_result.rule_type
UDM field.
Else, if the
eventtype
log field value is
not
empty
then,
eventtype
log field is mapped to the
security_result.rule_type
UDM field.
Else, if the
filtertype
log field value is
not
empty
then,
filtertype
log field is mapped to the
security_result.rule_type
UDM field.
crlevel
security_result.severity
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
level
security_result.severity
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
deviceSeverity
security_result.severity
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
fsaverdict
security_result.severity
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
infectedfilelevel
security_result.severity
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
crscore
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
level
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
error
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
deviceSeverity
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
icbseverity
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
msg
security_result.summary
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
attack
security_result.summary
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
mode
security_result.summary
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
reason
security_result.summary
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
virus
security_result.summary
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
catdesc
security_result.summary
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
msg
security_result.rule_name
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
app-ctrl
then,
msg
log field is mapped to the
security_result.rule_name
UDM field.
If the
policyname
log field value is
not
empty
then,
policyname
log field is mapped to the
security_result.rule_name
UDM field.
policyname
security_result.rule_name
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
app-ctrl
then,
msg
log field is mapped to the
security_result.rule_name
UDM field.
If the
policyname
log field value is
not
empty
then,
policyname
log field is mapped to the
security_result.rule_name
UDM field.
dstthreatfeed
security_result.threat_feed_name
attackid
security_result.threat_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
virusid
log field value is
not
empty
then,
virusid
log field is mapped to the
security_result.threat_id
UDM field. if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attackid
log field is mapped to the
security_result.threat_id
UDM field.
virusid
security_result.threat_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
virusid
log field value is
not
empty
then,
virusid
log field is mapped to the
security_result.threat_id
UDM field. if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attackid
log field is mapped to the
security_result.threat_id
UDM field.
attack
security_result.threat_name
If the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.threat_name
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
virus
then,
virus
log field is mapped to the
security_result.threat_name
UDM field.
virus
security_result.threat_name
If the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.threat_name
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
virus
then,
virus
log field is mapped to the
security_result.threat_name
UDM field.
cpdlisrteid
target.asset.attribute.labels[cpdlisrteid]
cpdlteid
target.asset.attribute.labels[cpdlteid]
cpteid
target.asset.attribute.labels[cpteid]
dhost
target.asset.attribute.labels[dhost]
dst_host
target.asset.attribute.labels[dst_host]
dstauthserver
target.asset.attribute.labels[dstauthserver]
dstintf
target.asset.attribute.labels[dstintf]
dstintfrole
target.asset.attribute.labels[dstintfrole]
dstserver
target.asset.attribute.labels[dstserver]
hostname
target.asset.attribute.labels[hostname]
server
target.asset.attribute.labels[server]
cpulteid
target.asset.type
If the
cpulteid
log field value is
not
empty
then, the
target.asset.type
UDM field is set to
SERVER
.
dsthwversion
target.asset.hardware.model
oldsn
target.asset.hardware.serial_number
dstserver
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
dst_host
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
dhost
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
hostname
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
dstauthserver
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
server
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
devname
target.asset.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.asset.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.asset.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.asset.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.asset.hostname
UDM field. Else,
devname
log field is mapped to the
target.asset.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.asset.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.asset.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.asset.hostname
UDM field.
locip
target.asset.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
dstip
target.asset.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
tunnelip
target.asset.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
cpaddr
target.asset.ip
cpaddr6
target.asset.ip
cpuladdr
target.asset.ip
cpuladdr6
target.asset.ip
cpdladdr
target.asset.ip
cpdladdr6
target.asset.ip
cpdlisraddr
target.asset.ip
cpdlisraddr6
target.asset.ip
filename
target.file.full_path
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
filename
log field value is
not
empty
then,
filename
log field is mapped to the
target.file.full_path
UDM field.
matchfiletype
target.file.mime_type
If the
matchfiletype
log field value is
not
empty
then,
matchfiletype
log field is mapped to the
target.file.mime_type
UDM field.
Else, if the
icbfiletype
log field value is
not
empty
then,
icbfiletype
log field is mapped to the
target.file.mime_type
UDM field.
Else, if the
infectedfiletype
log field value is
not
empty
then,
infectedfiletype
log field is mapped to the
target.file.mime_type
UDM field.
icbfiletype
target.file.mime_type
If the
matchfiletype
log field value is
not
empty
then,
matchfiletype
log field is mapped to the
target.file.mime_type
UDM field.
Else, if the
icbfiletype
log field value is
not
empty
then,
icbfiletype
log field is mapped to the
target.file.mime_type
UDM field.
Else, if the
infectedfiletype
log field value is
not
empty
then,
infectedfiletype
log field is mapped to the
target.file.mime_type
UDM field.
infectedfiletype
target.file.mime_type
If the
matchfiletype
log field value is
not
empty
then,
matchfiletype
log field is mapped to the
target.file.mime_type
UDM field.
Else, if the
icbfiletype
log field value is
not
empty
then,
icbfiletype
log field is mapped to the
target.file.mime_type
UDM field.
Else, if the
infectedfiletype
log field value is
not
empty
then,
infectedfiletype
log field is mapped to the
target.file.mime_type
UDM field.
infectedfilename
target.file.names
If the
infectedfilename
log field value is
not
empty
then,
infectedfilename
log field is mapped to the
target.file.names
UDM field.
If the
matchfilename
log field value is
not
empty
then,
matchfilename
log field is mapped to the
target.file.names
UDM field.
If the
icbfileid
log field value is
not
empty
then,
icbfileid
log field is mapped to the
target.file.names
UDM field.
matchfilename
target.file.names
If the
infectedfilename
log field value is
not
empty
then,
infectedfilename
log field is mapped to the
target.file.names
UDM field.
If the
matchfilename
log field value is
not
empty
then,
matchfilename
log field is mapped to the
target.file.names
UDM field.
If the
icbfileid
log field value is
not
empty
then,
icbfileid
log field is mapped to the
target.file.names
UDM field.
icbfileid
target.file.names
If the
infectedfilename
log field value is
not
empty
then,
infectedfilename
log field is mapped to the
target.file.names
UDM field.
If the
matchfilename
log field value is
not
empty
then,
matchfilename
log field is mapped to the
target.file.names
UDM field.
If the
icbfileid
log field value is
not
empty
then,
icbfileid
log field is mapped to the
target.file.names
UDM field.
hash
target.file.sha256
If the
hash
log field value is
not
empty
then,
hash
log field is mapped to the
target.file.sha256
UDM field.
Else, if the
analyticscksum
log field value is
not
empty
then,
analyticscksum
log field is mapped to the
target.file.sha256
UDM field.
analyticscksum
target.file.sha256
If the
hash
log field value is
not
empty
then,
hash
log field is mapped to the
target.file.sha256
UDM field.
Else, if the
analyticscksum
log field value is
not
empty
then,
analyticscksum
log field is mapped to the
target.file.sha256
UDM field.
infectedfilesize
target.file.size
analyticssubmit
target.file.tags
dstserver
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
dst_host
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
dhost
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
hostname
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
dstauthserver
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
server
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
dstname
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
host
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
remip
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
srcip
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
src
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
msg
principal.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
remip
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
forwardedfor
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
srcip
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
src
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
msg
principal.asset.ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
remip
target.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
locip
target.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
dstip
target.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
remip
target.asset.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
rem_ip
target.asset.ip
tunnelip
target.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
daddr
target.ip
end-usr-address
target.ip
endusraddress6
target.ip
rem_ip
target.ip
gateway
target.ip
opercountry
target.ip_location.country_or_region
dstcity
target.location.city
dstcountry
target.location.country_or_region
If the
dstcountry
log field value is
not
empty
and the
dstcountry
log field value is
not
equal to
Reserved
then,
dstcountry
log field is mapped to the
target.location.country_or_region
UDM field.
Else, if the
dstregion
log field value is
not
empty
then,
dstregion
log field is mapped to the
target.location.country_or_region
UDM field.
dstregion
target.location.country_or_region
If the
dstcountry
log field value is
not
empty
and the
dstcountry
log field value is
not
equal to
Reserved
then,
dstcountry
log field is mapped to the
target.location.country_or_region
UDM field.
Else, if the
dstregion
log field value is
not
empty
then,
dstregion
log field is mapped to the
target.location.country_or_region
UDM field.
dstmacAddress
target.mac
If the
dstmac
log field value is
not
empty
then, The
dstmacAddress
field is extracted from
dstmac
log field using the Grok pattern. if the
dstmacAddress
log field value is
not
empty
then,
dstmacAddress
extracted field is mapped to the
target.mac
UDM field and
dstmacAddress
extracted field is mapped to the
target.asset.mac
UDM field.
tranip
target.nat_ip
dsthwvendor
target.resource.attribute.labels[dsthwvendor]
request_name
target.resource.attribute.labels[request_name]
requesttype
target.resource.attribute.labels[requesttype]
resplength
target.resource.attribute.labels[resplength]
resptime
target.resource.attribute.labels[resptime]
resptype
target.resource.attribute.labels[resptype]
rssi
target.resource.attribute.labels[rssi]
rsso_key
target.resource.attribute.labels[rsso_key]
to_vcluster
target.resource.attribute.labels[to_vcluster]
tranport
target.nat_port
target.platform
If the
dstosname
log field value is equal to
WINDOWS
then, the
target.platform
UDM field is set to
WINDOWS
.
If the
dstosname
log field value contain one of the following values
Debian
DEBIAN
then, the
target.platform
UDM field is set to
LINUX
.
dstswversion
target.platform_version
dst_port
target.port
If the
dst_port
log field value does not contain one of the following values
Empty
N/A
then,
dst_port
log field is mapped to the
target.port
UDM field.
Else, if the
locport
log field value is
not
empty
then,
locport
log field is mapped to the
target.port
UDM field.
Else, if the
dstport
log field value is
not
empty
then,
dstport
log field is mapped to the
target.port
UDM field.
locport
target.port
If the
dst_port
log field value does not contain one of the following values
Empty
N/A
then,
dst_port
log field is mapped to the
target.port
UDM field.
Else, if the
locport
log field value is
not
empty
then,
locport
log field is mapped to the
target.port
UDM field.
Else, if the
dstport
log field value is
not
empty
then,
dstport
log field is mapped to the
target.port
UDM field.
dstport
target.port
If the
dst_port
log field value does not contain one of the following values
Empty
N/A
then,
dst_port
log field is mapped to the
target.port
UDM field.
Else, if the
locport
log field value is
not
empty
then,
locport
log field is mapped to the
target.port
UDM field.
Else, if the
dstport
log field value is
not
empty
then,
dstport
log field is mapped to the
target.port
UDM field.
to_vcluster
target.resource.resource_type
If the
to_vcluster
log field value does not contain one of the following values
Empty
N/A
then, the
target.resource.resource_type
UDM field is set to
CLUSTER
.
duid
target.user.attribute.labels[duid]
dstuser
target.user.attribute.labels[dstuser]
name
target.user.attribute.labels[name]
cfgobj
target.user.attribute.labels[cfgobj]
profile
target.resource.name
If the
profile
log field value is
not
empty
then,
profile
log field is mapped to the
target.resource.name
UDM field and the
target.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
dstuuid
target.resource.product_object_id
If the
dstuuid
log field value is
not
empty
then,
dstuuid
log field is mapped to the
target.resource.product_object_id
UDM field.
Else, if the
realserverid
log field value is
not
empty
then,
realserverid
log field is mapped to the
target.resource.product_object_id
UDM field.
realserverid
target.resource.product_object_id
If the
dstuuid
log field value is
not
empty
then,
dstuuid
log field is mapped to the
target.resource.product_object_id
UDM field.
Else, if the
realserverid
log field value is
not
empty
then,
realserverid
log field is mapped to the
target.resource.product_object_id
UDM field.
url
target.url
If the
url
log field value is
not
empty
and the
url
log field value is
not
equal to
N/A
then,
url
log field is mapped to the
target.url
UDM field.
dstunauthuser
target.user.user_display_name
If the
dstunauthuser
log field value is
not
empty
then,
dstunauthuser
log field is mapped to the
target.user.user_display_name
UDM field.
Else,
duser
log field is mapped to the
target.user.user_display_name
UDM field.
duser
target.user.user_display_name
If the
dstunauthuser
log field value is
not
empty
then,
dstunauthuser
log field is mapped to the
target.user.user_display_name
UDM field.
Else,
duser
log field is mapped to the
target.user.user_display_name
UDM field.
dstuser
target.user.userid
If the
duid
log field value is
not
empty
then, The
temp_duid
field is extracted from
duid
log field using the Grok pattern. if the
temp_duid
log field value is
not
empty
then,
temp_duid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
dstuser
log field value is
not
empty
then,
dstuser
log field is mapped to the
target.user.userid
UDM field.
Else, if the
request
log field value is
not
empty
and the
request
log field value matches the regular expression pattern
duid
then, The
d_uid
field is extracted from
request
log field using the Grok pattern. if the
d_uid
log field value is
not
empty
then,
d_uid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value matches the regular expression pattern
(?i)user
then,
name
log field is mapped to the
target.user.userid
UDM field.
Else, if the
cfgpath
log field value is equal to
system.admin
then,
cfgobj
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value matches the regular expression pattern
.
logon.
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
cfgobj
target.user.userid
If the
duid
log field value is
not
empty
then, The
temp_duid
field is extracted from
duid
log field using the Grok pattern. if the
temp_duid
log field value is
not
empty
then,
temp_duid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
dstuser
log field value is
not
empty
then,
dstuser
log field is mapped to the
target.user.userid
UDM field.
Else, if the
request
log field value is
not
empty
and the
request
log field value matches the regular expression pattern
duid
then, The
d_uid
field is extracted from
request
log field using the Grok pattern. if the
d_uid
log field value is
not
empty
then,
d_uid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value matches the regular expression pattern
(?i)user
then,
name
log field is mapped to the
target.user.userid
UDM field.
Else, if the
cfgpath
log field value is equal to
system.admin
then,
cfgobj
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value matches the regular expression pattern
.
logon.
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
duid
target.user.userid
If the
duid
log field value is
not
empty
then, The
temp_duid
field is extracted from
duid
log field using the Grok pattern. if the
temp_duid
log field value is
not
empty
then,
temp_duid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
dstuser
log field value is
not
empty
then,
dstuser
log field is mapped to the
target.user.userid
UDM field.
Else, if the
request
log field value is
not
empty
and the
request
log field value matches the regular expression pattern
duid
then, The
d_uid
field is extracted from
request
log field using the Grok pattern. if the
d_uid
log field value is
not
empty
then,
d_uid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value matches the regular expression pattern
(?i)user
then,
name
log field is mapped to the
target.user.userid
UDM field.
Else, if the
cfgpath
log field value is equal to
system.admin
then,
cfgobj
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value matches the regular expression pattern
.
logon.
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
name
target.user.userid
If the
duid
log field value is
not
empty
then, The
temp_duid
field is extracted from
duid
log field using the Grok pattern. if the
temp_duid
log field value is
not
empty
then,
temp_duid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
dstuser
log field value is
not
empty
then,
dstuser
log field is mapped to the
target.user.userid
UDM field.
Else, if the
request
log field value is
not
empty
and the
request
log field value matches the regular expression pattern
duid
then, The
d_uid
field is extracted from
request
log field using the Grok pattern. if the
d_uid
log field value is
not
empty
then,
d_uid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value matches the regular expression pattern
(?i)user
then,
name
log field is mapped to the
target.user.userid
UDM field.
Else, if the
cfgpath
log field value is equal to
system.admin
then,
cfgobj
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value matches the regular expression pattern
.
logon.
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
deviceExternalId
about.asset.asset_id
If the
deviceExternalId
log field value is
not
empty
then,
%{device_vendor}.%{device_product}:%{deviceExternalId}
log field is mapped to the
about.asset.asset_id
UDM field.
UDM Mapping Delta
UDM Mapping Delta reference: Fortinet_Firewall
The following table lists delta between Default parser of
FORTINET FIREWALL
and premium version of
FORTINET FIREWALL
.
Default UDM Mapping
Log Field
Premium Mapping Delta
about.file.full_path
filehash
If the
filehash
log field value matches the regular expression pattern
(?<_hash>^[0-9a-f]+$)
then,
filehash
log field is mapped to the
about.file.sha256
UDM field.
Else,
filehash
log field is mapped to the
about.file.full_path
UDM field.
about.file.sha256
filehash
If the
filehash
log field value matches the regular expression pattern
(?<_hash>^[0-9a-f]+$)
then,
filehash
log field is mapped to the
about.file.sha256
UDM field.
Else,
filehash
log field is mapped to the
about.file.full_path
UDM field.
principal.resource.attribute.labels
init
Updated one condition to remove the unnecessary value like "N/A".
principal.resource.attribute.labels
vpntunnel
Updated one condition to remove the unnecessary value like "N/A".
principal.resource.attribute.labels
rcvdbyte
Updated one condition to remove the unnecessary value like "N/A".
security_result.description
utmaction
Updated the mapping from
security_result.description
to
security_result.action
UDM field.
security_result.detection_fields
dstinetsvc
Updated one condition to remove the unnecessary value like "N/A".
security_result.detection_fields
dstintf
Updated the mapping from
security_result.detection_fields
to
target.asset.attribute.labels
UDM field.
security_result.detection_fields
dstintfrole
Updated the mapping from
security_result.detection_fields
to
target.asset.attribute.labels
UDM field.
security_result.detection_fields
srcintf
Updated the mapping from
security_result.detection_fields
to
principal.asset.attribute.labels
UDM field.
security_result.detection_fields
srcintfrole
Updated the mapping from
security_result.detection_fields
to
principal.asset.attribute.labels
UDM field.
security_result.detection_fields
xid
Updated one condition to remove the unnecessary value like "N/A".
additional.fields
policyid
Updated the mapping from
additional.fields
to
security_result.detection_fields
UDM field.
additional.fields
poluuid
Updated the mapping from
additional.fields
to
security_result.detection_fields
UDM field.
principal.ip
ui
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
saddr
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
shost
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
user
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
locip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
remip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
srcip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
src
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
msg
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
srcremote
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
forwardedfor
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
userfrom
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.ip
loc_ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to the
prin_ip
log field value then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
principal.asset.ip
ui
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
user
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
locip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
remip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
srcip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
src
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
msg
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
forwardedfor
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
userfrom
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
principal.asset.ip
loc_ip
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
then,
prin_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
user
log field value does not contain one of the following values
Empty
N/A
then, The
user_ip
field is extracted from
user
log field using the Grok pattern. if the
user_ip
log field value is
not
empty
then,
user_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
and if the
ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
N/A
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
log field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then, The
valid_locip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is equal to
outbound
then,
valid_locip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_locip
log field is mapped to the
target.asset.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.asset.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
and
user_id
fields is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
user_email
extracted fields are mapped to the
principal.asset.ip
UDM field.
target.ip
locip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
target.ip
dstip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
target.ip
remip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
target.ip
tunnelip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
target.ip
rem_ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
target.asset.ip
locip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
target.asset.ip
dstip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
target.asset.ip
remip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
target.asset.ip
tunnelip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
target.asset.ip
rem_ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.asset.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.asset.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.asset.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.asset.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.asset.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.asset.ip
UDM field.
security_result.rule_version
srchwversion
Updated the mapping from
security_result.rule_version
to
principal.asset.hardware.model
UDM field.
security_result.rule_version
dsthwversion
Updated the mapping from
security_result.rule_version
to
target.asset.hardware.model
UDM field.
metadata.description
desc
Updated the mapping from
metadata.description
to
security_result.detection_fields
UDM field.
principal.resource.attribute.labels
srchwvendor
Updated the mapping from
principal.resource.attribute.labels
to
principal.asset.hardware.manufacturer
UDM field.
security_result.action_details
operation
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
security_result.action_details
icbaction
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
security_result.action_details
action
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
security_result.action_details
utmaction
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and the
action
log field value matches the regular expression pattern
(?i)accept
or
(?i)close
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
If the
action
log field value is
not
empty
then,
action
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
utmaction
log field value is
not
empty
then,
utmaction
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
operation
log field value is
not
empty
then,
operation
log field is mapped to the
security_result.action_details
UDM field.
Else, if the
icbaction
log field value is
not
empty
then,
icbaction
log field is mapped to the
security_result.action_details
UDM field.
security_result.action
If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then, the
security_result.action
UDM field is set to
BLOCK
.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then, the
security_result.action
UDM field is set to
BLOCK
.
Else, If the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.action
UDM field is set to
FAIL
.
If the
operation
log field value is
not
empty
and if the
operation
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
edit
then, the
security_result.action
UDM field is set to
ALLOW
. Else, if the
operation
log field value contain one of the following values
deny
dropped
blocked
then, the
security_result.action
UDM field is set to
BLOCK
. Else, if the
operation
log field value is equal to
timeout
then, the
security_result.action
UDM field is set to
FAIL
.
Else, if the
icbaction
log field value is
not
empty
then, if the
icbaction
log field value matches the regular expression pattern
allow
then, the
security_result.action
UDM field is set to
ALLOW
. Else, if the
icbaction
log field value matches the regular expression pattern
block
then, the
security_result.action
UDM field is set to
BLOCK
. Else, if the
icbaction
log field value matches the regular expression pattern
fail
then, the
security_result.action
UDM field is set to
BLOCK
.
security_result.severity_details
crscore
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.severity_details
level
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.severity_details
error
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.severity_details
deviceSeverity
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.severity_details
icbseverity
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.category_details
dtype
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
category
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
cat
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
attack
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
catdesc
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
filtercat
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
icbverdict
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
security_result.category_details
infection
If the
catdesc
log field value is
not
empty
then,
catdesc
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
category
log field value is
not
empty
then,
category
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
filtercat
log field value is
not
empty
then,
filtercat
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
dtype
log field value is
not
empty
then,
dtype
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
icbverdict
log field value is
not
empty
then,
icbverdict
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
infection
log field value is
not
empty
then,
infection
log field is mapped to the
security_result.category_details
UDM field.
Else, if the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.category_details
UDM field.
metadata.product_event_type
type
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
metadata.product_event_type
subtype
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
metadata.product_event_type
connection_type
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
metadata.product_event_type
eventsubtype
If
logid
log field value is not
empty
and is available in the
documentation
, then values of
Type
and
Category
are mapped to
metadata.product_event_type
.
Else, if the
logid
is not documented, it is mapped according to the following logic:
If the
connection_type
log field value is
not
empty
then,
%{type} - %{subtype} - %{connection_type}
log field is mapped to the
metadata.product_event_type
UDM field.
Else,
%{type} - %{subtype}
log field is mapped to the
metadata.product_event_type
UDM field.
If the
eventsubtype
log field value is
not
empty
then,
eventsubtype
log field is mapped to the
metadata.product_event_type
UDM field.
metadata.event_type
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. if the
subtype
log field value is equal to
webfilter
and if the
service
log field value contain one of the following values
HTTPS
HTTP
then, the
metadata.event_type
UDM field is set to
NETWORK_HTTP
. Else, if the
subtype
log field value contain one of the following values
virus
ips
anomaly
or the
utmevent
log field value is equal to
appfirewall
and the
subtype
log field value is
not
equal to
system
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else if the
subtype
log field value is equal to
vpn
and
type
is equal to
event
and if the
action
log field value contain one of the following values
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else, if the
type
log field value is equal to
dns
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
then, the
metadata.event_type
UDM field is set to
NETWORK_DNS
.
Else, if the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, the
metadata.event_type
UDM field is set to
NETWORK_DHCP
.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
action
log field value matches the regular expression pattern
.
logoff.
or the
action
log field value is equal to
authentication
and the
status
log field value is equal to
logout
or the
action
log field value is equal to
auth-logout
and the
status
log field value is equal to
logout
then, the
metadata.event_type
UDM field is set to
USER_LOGOUT
. if the
action
log field value matches the regular expression pattern
.
logon.
or the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
login
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
user_id
log field value is
not
empty
and the
user_email
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
USER_CREATION
. Else, the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
If the
event_name
log field value contain one of the following values
LogSpyware
LogPredictiveMachineLearning
or the
subtype
log field value contain one of the following values
LogSpyware
LogPredictiveMachineLearning
endpoint
system
then, the
metadata.event_type
UDM field is set to
SCAN_UNCATEGORIZED
.
If the
user
log field value does not contain one of the following values
Empty
N/A
and if the
metadata.event_type
log field value is equal to
GENERIC_EVENT
then, if the
subtype
log field value is equal to
vpn
and
type
is equal to
event
and if the
action
log field value contain one of the following values
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
If the
File_name
log field value is
not
empty
or the
Object
log field value is
not
empty
or the
Objekt
log field value is
not
empty
or the
Infected_Resource
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
PROCESS_UNCATEGORIZED
.=
If the
metadata.event_type
log field value matches the regular expression pattern
GENERIC_EVENT
and if the
srcip
log field value is
not
empty
and the
dstip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
. Else, if the
srcip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
. Else, if the
action
log field value is equal to
Delete
then, the
metadata.event_type
UDM field is set to
USER_DELETION
. if the
action
log field value is equal to
Edit
then, the
metadata.event_type
UDM field is set to
DEVICE_CONFIG_UPDATE
.
security_result.description
path
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.description
result
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.description
reason
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.description
fortiguardresp
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.description
malform_desc
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.description
msg
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.description
catdesc
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
additional.fields
ssid
Updated the mapping from
additional.fields
to
principal.asset.attribute.labels
UDM field.
additional.fields[audittime]
audittime
Updated the mapping from
additional.fields
to
security_result.detection_fields
UDM field.
security_result.severity
crlevel
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
security_result.severity
level
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
security_result.severity
deviceSeverity
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
security_result.severity
fsaverdict
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
security_result.severity
infectedfilelevel
If the
logid
log field value is not
empty
and is available in the
documentation
, then based on the value of
Severity
, the
security_result.severity
field will be mapped as per the following logic:
If the
severity_value
log field value is
empty
, then the
security_result.severity
field will be mapped as per the following logic:
If the
severity
log field value is
not
empty
and if the
severity
log field value contain one of the following values
0
1
2
3
LOW
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
severity
log field value contain one of the following values
4
5
6
MEDIUM
SUBSTANTIAL
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
severity
log field value contain one of the following values
7
8
HIGH
SEVERE
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
severity
log field value contain one of the following values
9
10
VERY-HIGH
CRITICAL
then, the
security_result.severity
UDM field is set to
CRITICAL
. Else, if the
severity
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
crlevel
log field value is
not
empty
and if the
crlevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
crlevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
deviceSeverity
log field value is
not
empty
and if the
deviceSeverity
log field value is equal to
warning
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
deviceSeverity
log field value is equal to
notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
deviceSeverity
log field value contain one of the following values
information
info
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
deviceSeverity
log field value is equal to
error
then, the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
fsaverdict
log field value is
not
empty
and if the
fsaverdict
log field value matches the regular expression pattern
low risk
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
fsaverdict
log field value matches the regular expression pattern
med risk
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
fsaverdict
log field value matches the regular expression pattern
high risk
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
fsaverdict
log field value matches the regular expression pattern
clear
then, the
security_result.severity
UDM field is set to
NONE
.
Else, if the
infectedfilelevel
log field value is
not
empty
and if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Low
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Medium
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)High
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
infectedfilelevel
log field value matches the regular expression pattern
(?i)Critical
then, the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
level
log field value is
not
empty
and if the
level
log field value matches the regular expression pattern
(?i)(error)
then, the
security_result.severity
UDM field is set to
ERROR
. Else, if the
level
log field value matches the regular expression pattern
(?i)(warning)
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if the
level
log field value matches the regular expression pattern
(?i)notice
then, the
security_result.severity
UDM field is set to
LOW
. Else, if the
level
log field value matches the regular expression pattern
(?i)(information|info)
then, the
security_result.severity
UDM field is set to
INFORMATIONAL
. Else, if the
level
log field value matches the regular expression pattern
(?i)(critical|alert)
then, the
security_result.severity
UDM field is set to
CRITICAL
.
principal.hostname
authserver
about.hostname
UDM Refresher Mapping Delta
UDM Refresher Mapping Delta reference: Fortinet_Firewall
The following table lists delta between Current parser of
FORTINET FIREWALL
and New version of
FORTINET FIREWALL
.
New UDM Mapping
Raw Log Field
Current Mapping Delta
additional.fields[dstintf]
dstintf
target.asset.attribute.labels[dstintf]
additional.fields[dstintfrole]
dstintfrole
target.asset.attribute.labels[dstintfrole]
additional.fields[remotetunnelid]
remotetunnelid
security_result.detection_fields[remotetunnelid]
additional.fields[replydstintf]
replydstintf
security_result.detection_fields[replydstintf]
additional.fields[replysrcintf]
replysrcintf
security_result.detection_fields[replysrcintf]
additional.fields[checksum]
checksum
principal.file.sha256
additional.fields[community]
community
principal.user.group_identifiers
If the
group
log field value is
not
empty
and the
group
log field value is
not
equal to
N/A
then,
group
log field is mapped to the
principal.user.group_identifiers
UDM field.
Else, if the
community
log field value is
not
empty
then,
community
log field is mapped to the
principal.user.group_identifiers
UDM field.
additional.fields[cookies]
cookies
principal.resource.attribute.labels[cookies]
additional.fields[dstuuid]
dstuuid
target.resource.product_object_id
If the
dstuuid
log field value is
not
empty
then,
dstuuid
log field is mapped to the
target.resource.product_object_id
UDM field.
Else, if the
realserverid
log field value is
not
empty
then,
realserverid
log field is mapped to the
target.resource.product_object_id
UDM field.
additional.fields[nextstat]
nextstat
principal.resource.attribute.labels[nextstat]
additional.fields[outintf]
outintf
principal.resource.attribute.labels[outintf]
additional.fields[poolname]
poolname
network.ip_subnet_range
If the
portbegin
log field value is
not
empty
and the
portend
log field value is
not
empty
then,
%{portbegin}/%{portend}
log field is mapped to the
network.ip_subnet_range
UDM field.
Else,
poolname
log field is mapped to the
network.ip_subnet_range
UDM field.
additional.fields[portbegin]
portbegin
network.ip_subnet_range
If the
portbegin
log field value is
not
empty
and the
portend
log field value is
not
empty
then,
%{portbegin}/%{portend}
log field is mapped to the
network.ip_subnet_range
UDM field.
Else,
poolname
log field is mapped to the
network.ip_subnet_range
UDM field.
additional.fields[portend]
portend
network.ip_subnet_range
If the
portbegin
log field value is
not
empty
and the
portend
log field value is
not
empty
then,
%{portbegin}/%{portend}
log field is mapped to the
network.ip_subnet_range
UDM field.
Else,
poolname
log field is mapped to the
network.ip_subnet_range
UDM field.
additional.fields[profile]
profile
target.resource.name
If the
profile
log field value is
not
empty
then,
profile
log field is mapped to the
target.resource.name
UDM field and the
target.resource.resource_type
UDM field is set to
ACCESS_POLICY
additional.fields[ratemethod]
ratemethod
principal.resource.attribute.labels[ratemethod]
additional.fields[reqtype]
reqtype
principal.resource.attribute.labels[reqtype]
additional.fields[src_int]
src_int
principal.resource.name
If the
clouddevice
log field value is
not
empty
then,
clouddevice
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
servername
log field value is
not
empty
then,
servername
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
src_int
log field value is
not
empty
then,
src_int
log field is mapped to the
principal.resource.name
UDM field.
Else, if the
srcdomain
log field value is
not
empty
then,
srcdomain
log field is mapped to the
principal.resource.name
UDM field.
additional.fields[srcuuid]
srcuuid
principal.resource.product_object_id
If the
srcuuid
log field value is
not
empty
then,
srcuuid
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
serveraddr
log field value is
not
empty
then,
serveraddr
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
cldobjid
log field value is
not
empty
then,
cldobjid
log field is mapped to the
principal.resource.product_object_id
UDM field.
If the
cldobjid
log field value is
not
empty
or the
serveraddr
log field value is
not
empty
or the
srcuuid
log field value is
not
empty
then, the
principal.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
additional.fields[ssid]
ssid
principal.asset.attribute.labels[ssid]
extensions.auth.auth_type
domainctrlauthtype
security_result.detection_fields[domainctrlauthtype]
extensions.vulns.vulnerabilities.cve_id
cveid
security_result.detection_fields[cveid]
extensions.vulns.vulnerabilities.name
vulnname
security_result.detection_fields[vulnname]
extensions.vulns.vulnerabilities.vendor_vulnerability_id
vulnid
security_result.detection_fields[vulnid]
network.email.subject
subject
about.process.command_line
additional.fields[addrgrp]
addrgrp
network.dns.answers.data
If the
ipaddr
log field value is
not
empty
then,
Iterate through log field
ipaddr
, then
ipaddr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addr
log field value is
not
empty
then,
Iterate through log field
addr
, then
addr
log field is mapped to the
network.dns.answers.data
UDM field.
If the
addrgrp
log field value is
not
empty
then,
addrgrp
log field is mapped to the
network.dns.answers.data
UDM field.
security_result.detection_fields[appcat]
appcat
additional.fields[appcat]
additional.fields[addr_type]
addr_type
network.dns.answers.type
principal.asset.attribute.labels[ha_group]
ha_group
intermediary.asset.attribute.labels[ha_group]
principal.asset.attribute.labels[ha_role]
ha_role
intermediary.asset.attribute.labels[ha_role]
principal.asset.attribute.labels[mastersrcmac]
mastersrcmac
principal.mac
target.asset.attribute.labels[peer]
peer
principal.asset.hardware.model
principal.domain.name
srcdomain
principal.resource.name
principal.nat_ip
nat
about.nat_ip
additional.fields[init]
init
principal.resource.attribute.labels[init]
additional.fields[profiletype]
profiletype
principal.user.attribute.labels[profiletype]
principal.user.attribute.labels[unauthusersource]
unauthusersource
security_result.detection_fields[unauthusersource]
security_result.detection_fields[craction]
craction
security_result.about.labels[craction]
security_result.detection_fields[appact]
appact
additional.fields[appact]
security_result.detection_fields[appid]
appid
security_result.rule_id
security_result.detection_fields[applist]
applist
additional.fields[applist]
security_result.detection_fields[apprisk]
apprisk
additional.fields[apprisk]
security_result.detection_fields[attachment]
attachment
network.dhcp.file
security_result.detection_fields[attackcontext]
attackcontext
security_result.attack_details.techniques.name
security_result.detection_fields[attackcontextid]
attackcontextid
security_result.attack_details.techniques.id
security_result.detection_fields[c-bytes]
c-bytes
network.sent_bytes
If the
sentbyte
log field value is
not
empty
then,
sentbyte
log field is mapped to the
network.sent_bytes
UDM field.
Else, if the
c-bytes
log field value is
not
empty
then,
c-bytes
log field is mapped to the
network.sent_bytes
UDM field.
Else,
lanout
log field is mapped to the
network.sent_bytes
UDM field.
security_result.detection_fields[c-ggsn]
c-ggsn
network.carrier_name
security_result.detection_fields[cat]
cat
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field. if the
attackid
log field value is
not
empty
then,
attackid
log field is mapped to the
security_result.rule_id
UDM field. if the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
then,
cat
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
then,
ruleid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
then,
appid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
then,
policyid
log field is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
then,
poluuid
log field is mapped to the
security_result.rule_id
UDM field.
security_result.detection_fields[chgheaders]
chgheaders
network.http.user_agent
additional.fields[chgheaders]
If the
agent
log field value is
not
empty
then,
agent
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
chgheaders
log field value is
not
empty
then,
chgheaders
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
method
log field value is
not
empty
then,
method
log field is mapped to the
network.http.user_agent
UDM field.
security_result.detection_fields[crscore]
crscore
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.detection_fields[domainfilterlist]
domainfilterlist
additional.fields[domainfilterlist]
security_result.detection_fields[eapolcnt]
eapolcnt
network.sent_packets
If the
sentpkt
log field value is
not
empty
then,
sentpkt
log field is mapped to the
network.sent_packets
UDM field.
Else,
eapolcnt
log field is mapped to the
network.sent_packets
UDM field.
security_result.detection_fields[eventtype]
eventtype
security_result.rule_type
security_result.detection_fields[eventtype]
security_result.verdict_info.source_provider
filehashsrc
security_result.detection_fields[filehashsrc]
security_result.detection_fields[httpmethod]
httpmethod
network.http.method
If the
httpmethod
log field value is
not
empty
then,
httpmethod
log field is mapped to the
network.http.method
UDM field.
Else, if the
message_type
log field value is
not
empty
then,
message_type
log field is mapped to the
network.http.method
UDM field.
security_result.detection_fields[icbseverity]
icbseverity
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.detection_fields[new_value]
new_value
principal.domain.name
security_result.detection_fields[old_value]
old_value
intermediary.domain.name
security_result.detection_fields[request_name]
request_name
target.resource.attribute.labels[request_name]
security_result.detection_fields[resplength]
resplength
target.resource.attribute.labels[resplength]
security_result.detection_fields[resptime]
resptime
target.resource.attribute.labels[resptime]
security_result.detection_fields[resptype]
resptype
target.resource.attribute.labels[resptype]
security_result.detection_fields[totalsession]
totalsession
network.session_duration
If the
duration
log field value does not contain one of the following values
Empty
0
then,
duration
log field is mapped to the
network.session_duration
UDM field.
Else, if the
durationdelta
log field value is
not
empty
then,
durationdelta
log field is mapped to the
network.session_duration
UDM field.
Else, if the
live
log field value is
not
empty
then,
live
log field is mapped to the
network.session_duration
UDM field.
Else, if the
totalsession
log field value is
not
empty
then,
totalsession
log field is mapped to the
network.session_duration
UDM field.
security_result.detection_fields[versionmax]
versionmax
principal.asset.attribute.labels[versionmax]
security_result.detection_fields[versionmin]
versionmin
principal.asset.attribute.labels[versionmin]
security_result.detection_fields[vwlid]
vwlid
additional.fields[vwlid]
security_result.detection_fields[wanin]
wanin
additional.fields[wanin]
security_result.outcomes[cloudaction]
cloudaction
principal.resource.attribute.labels[cloudaction]
security_result.outcomes[error]
error
security_result.severity_details
If the
level
log field value is
not
empty
then,
level
log field is mapped to the
security_result.severity_details
UDM field.
If the
crscore
log field value is
not
empty
then,
crscore
log field is mapped to the
security_result.severity_details
UDM field.
If the
deviceSeverity
log field value is
not
empty
then,
deviceSeverity
log field is mapped to the
security_result.severity_details
UDM field.
If the
level
log field value is
not
empty
and if the
level
log field value is equal to
error
and the
error
log field value is
not
empty
then,
error
log field is mapped to the
security_result.severity_details
UDM field. Else,
level: %{level}
log field is mapped to the
security_result.severity_details
UDM field.
If the
icbseverity
log field value is
not
empty
then,
icbseverity
log field is mapped to the
security_result.severity_details
UDM field.
security_result.outcomes[vulnresult]
vulnresult
security_result.detection_fields[vulnresult]
security_result.rule_labels[policymode]
policymode
about.resource.resource_subtype
security_result.detection_fields[message_type]
message_type
network.http.method
If the
httpmethod
log field value is
not
empty
then,
httpmethod
log field is mapped to the
network.http.method
UDM field.
Else, if the
message_type
log field value is
not
empty
then,
message_type
log field is mapped to the
network.http.method
UDM field.
security_result.threat_feed_name
srcthreatfeed
principal.resource.attribute.labels[srcthreatfeed]
security_results.detection_fields[peer_notif]
peer_notif
principal.user.attribute.labels[peer_notif]
security_results.detection_fields[serverresponsetime]
serverresponsetime
principal.resource.attribute.labels[serverresponsetime]
security_results.detection_fields[serviceid]
serviceid
principal.resource.attribute.labels[serviceid]
security_results.detection_fields[stage]
stage
principal.resource.attribute.labels[stage]
security_results.detection_fields[useractivity]
useractivity
principal.user.attribute.labels[useractivity]
security_results.outcomes[acktime]
acktime
security_result.detection_fields[acktime]
security_results.outcomes[activity]
activity
security_result.detection_fields[activity]
target.asset.attribute.labels[domainctrlauthstate]
domainctrlauthstate
extensions.auth.auth_details
If the
authserver
log field value is
not
empty
then,
authserver
log field is mapped to the
extensions.auth.auth_details
UDM field.
Else, if the
domainctrlauthstate
log field value is
not
empty
then,
domainctrlauthstate
log field is mapped to the
extensions.auth.auth_details
UDM field.
target.asset.attribute.labels[dstfamily]
dstfamily
additional.fields[dstfamily]
target.asset.attribute.labels[dstserver]
dstserver
target.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
then,
devname
log field is mapped to the
target.hostname
UDM field.
Else, if the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstserver
log field value does not contain one of the following values
Empty
0
1
then,
dstserver
log field is mapped to the
target.hostname
UDM field.
If the
dst_host
log field value does not contain one of the following values
Empty
N/A
then,
dst_host
log field is mapped to the
target.hostname
UDM field.
If the
dhost
log field value is
not
empty
then,
dhost
log field is mapped to the
target.hostname
UDM field.
If the
hostname
log field value is
not
empty
then,
hostname
log field is mapped to the
target.hostname
UDM field.
If the
dstauthserver
log field value is
not
empty
then,
dstauthserver
log field is mapped to the
target.hostname
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
server
log field value is
not
empty
then,
server
log field is mapped to the
target.hostname
UDM field. Else,
devname
log field is mapped to the
target.hostname
UDM field.
If the
dstname
log field value is
not
empty
then,
dstname
log field is mapped to the
target.hostname
UDM field.
If the
host
log field value is
not
empty
then,
host
log field is mapped to the
target.hostname
UDM field.
If the
action
log field value is equal to
login
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
target.hostname
UDM field.
target.asset.attribute.labels[dstssid]
dstssid
additional.fields[dstssid]
target.asset.attribute.labels[dstunauthusersource]
dstunauthusersource
additional.fields[dstunauthusersource]
target.asset.attribute.labels[masterdstmac]
masterdstmac
target.mac
target.asset.attribute.labels[oldsn]
oldsn
target.asset.hardware.serial_number
target.asset.category
dstdevtype
additional.fields[dstdevtype]
target.file.full_path
file
principal.file.full_path
target.file.full_path
pathname
security_result.detection_fields[pathname]
target.file.size
filesize
principal.file.size
principal.asset.attribute.labels[ha_prio]
ha-prio
intermediary.asset.attribute.labels[ha_prio]
target.resource.attribute.label[from_vcluster]
from_vcluster
additional.fields[from_vcluster]
target.resource.attribute.labels[domainctrlip]
domainctrlip
intermediary.ip
target.resource.parent.product_object_id
to_vcluster
target.resource.attribute.labels[to_vcluster]
target.resource.product_object_id
alarmid
security_result.detection_fields[alarmid]
target.user.attribute.labels[new_status]
new_status
principal.user.attribute.labels[new_status]
target.user.attribute.labels[old_status]
old_status
principal.user.attribute.labels[old_status]
target.user.attribute.labels[passwd]
passwd
principal.user.attribute.labels[passwd]
target.user.attribute.labels[vcluster_state]
vcluster_state
security_result.detection_fields[vcluster_state]
target.user.group_identifiers
adgroup
principal.group.group_display_name
principal.resource.attribute.labels[tunneltype]
additional.fields[tunneltype]
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
and the
tunneltype
log field value is
not
one of the following
Empty
N/A
then, map the key
tunneltype
and value from the
tunneltype
log field to the
principal.resource.attribute.labels
UDM field.
Else, map the key
tunneltype
and value from the
tunneltype
log field to the
additional.fields
UDM field.
tunneltype
principal.resource.attribute.labels[tunneltype]
intermediary.asset.attribute.labels[vd]
target.asset.attribute.labels[vd]
If the
vd
log field value is
not
empty
then, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then, map the key
vd
and value from the
vd
log field to the
target.asset.attribute
UDM field.
Else, map the key
vd
and value from the
vd
log field to the
intermediary.asset.attribute
UDM field.
vd
principal.administrative_domain
If the
admin
log field value is
not
empty
then, map the
admin
log field value to the
principal.administrative_domain
UDM field.
Else, if the
vd
log field value is
not
empty
then, map the
vd
log field value to the
principal.administrative_domain
UDM field.
intermediary.asset.hardware.serial_number
principal.asset.hardware.serial_number
If the
deviceExternalId
log field value is
not
empty
then, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then, map the
deviceExternalId
log field value to the
principal.asset.hardware.serial_number
UDM field.
Else, map the
deviceExternalId
log field value to the
intermediary.asset.hardware.serial_number
UDM field.
deviceExternalId
about.asset.asset_id
If the
deviceExternalId
log field value is
not
empty
then,
%{device_vendor}.%{device_product}:%{deviceExternalId}
log field is mapped to the
about.asset.asset_id
UDM field.
intermediary.hostname
target.hostname
target.asset.attribute.labels[devname]
additional.fields[devname]
If the
devname
log field value is
not
empty
then, check if the
devname
log field value has a length between 0 and 255 characters.
If true, and if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then, map the
devname
log field value to the
target.hostname
UDM field.
Else (if not type event and subtype system), map the
devname
log field value to the
intermediary.hostname
UDM field.
If the length check is false (more than 255 characters), and if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then, map the key
devname
and value from the
devname
log field to the
target.asset.attribute.labels
UDM field.
Else, map the key
devname
and value from the
devname
log field to the
additional.fields
UDM field.
devname
intermediary.hostname
If the
dvchost
log field value is
not
empty
then,
dvchost
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
domainctrldomain
log field value is
not
empty
then,
domainctrldomain
log field is mapped to the
intermediary.hostname
UDM field.
Else, if the
temp_data
log field value is
not
empty
then, The
ts
and
device_name
fields is extracted from
temp_data
log field using the Grok pattern. if the
device_name
log field value is
not
empty
then,
device_name
log field is mapped to the
intermediary.hostname
UDM field.
metadata.event_type
If the
type
log field value is equal to
traffic
and the
subtype
log field value is one of the following
Empty
forward
local
system
http-transaction
multicast
sniffer
ztna
or the
type
log field value is equal to
utm
and the
subtype
log field value is one of the following
webfilter
app-ctrl
ssl
voip
ips
anomaly
waf
or the
type
log field value is equal to
event
and the
subtype
log field value is one of the following
wad
system
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Within this block, if the
subtype
log field value is equal to
webfilter
and the
service
log field value is one of the following
HTTPS
HTTP
then, the
metadata.event_type
UDM field is set to
NETWORK_HTTP
. Else, if the
subtype
log field value is one of the following
ips
anomaly
or the
utmevent
log field value is equal to
appfirewall
and the
subtype
log field value is
not
equal to
system
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else if the
subtype
log field value is equal to
vpn
and the
type
log field value is equal to
event
then, if the
action
log field value is one of the following
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else if the
type
log field value is equal to
dns
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
then, the
metadata.event_type
UDM field is set to
NETWORK_DNS
.
Else if the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and the
dhcp_msg
log field value is equal to
Ack
then, the
metadata.event_type
UDM field is set to
NETWORK_DHCP
.
Else if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
then, if the
action
log field value matches the regular expression pattern
.*logoff.*
or the
action
log field value is equal to
authentication
and the
status
log field value is equal to
logout
or the
action
log field value is equal to
auth-logout
and the
status
log field value is equal to
logout
then, the
metadata.event_type
UDM field is set to
USER_LOGOUT
. If the
action
log field value matches the regular expression pattern
.*logon.*
or the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else if the
action
log field value is equal to
login
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
then, if the
user_id
log field value is
not
empty
or the
user_email
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
USER_CREATION
. Else, the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
Else if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
cifs-auth-fail
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else if the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
then, the
metadata.event_type
UDM field is set to
SCAN_FILE
.
Else if the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
file-filter
then, the
metadata.event_type
UDM field is set to
SCAN_FILE
.
Else if the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
icap
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else if the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virtual-patch
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
If the
event_name
log field value is one of the following
LogSpyware
LogPredictiveMachineLearning
or the
subtype
log field value is one of the following
endpoint
system
then, the
metadata.event_type
UDM field is set to
SCAN_UNCATEGORIZED
.
If the
user
log field value is
not
empty
and is
not
equal to
N/A
and the
metadata.event_type
UDM field is currently
GENERIC_EVENT
then, if the
subtype
log field value is equal to
vpn
and the
type
log field value is equal to
event
then, if the
action
log field value is one of the following
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
. Else (if not type event and subtype vpn), the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
If the
File_name
log field value is
not
empty
or the
Object
log field value is
not
empty
or the
Objekt
log field value is
not
empty
or the
Infected_Resource
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
PROCESS_UNCATEGORIZED
.
If the
metadata.event_type
UDM field currently matches
GENERIC_EVENT
then, if the
srcip
log field value is
not
empty
and the
dstip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
. Else, if the
srcip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
. Else, if the
action
log field value is equal to
Delete
then, the
metadata.event_type
UDM field is set to
USER_DELETION
. Additionally, if the
action
log field value is equal to
Edit
then, the
metadata.event_type
UDM field is set to
DEVICE_CONFIG_UPDATE
.
If the
metadata.event_type
UDM field is still
GENERIC_EVENT
after the above checks, it is set to
STATUS_UPDATE
.
If the
dir
log field value is
not
empty
or the
direction
log field value is
not
empty
and the
direction
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
metadata.event_type
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. if the
subtype
log field value is equal to
webfilter
and if the
service
log field value contain one of the following values
HTTPS
HTTP
then, the
metadata.event_type
UDM field is set to
NETWORK_HTTP
. Else, if the
subtype
log field value contain one of the following values
virus
ips
anomaly
or the
utmevent
log field value is equal to
appfirewall
and the
subtype
log field value is
not
equal to
system
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else if the
subtype
log field value is equal to
vpn
and
type
is equal to
event
and if the
action
log field value contain one of the following values
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
Else, if the
type
log field value is equal to
dns
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
then, the
metadata.event_type
UDM field is set to
NETWORK_DNS
.
Else, if the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, the
metadata.event_type
UDM field is set to
NETWORK_DHCP
.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and if the
action
log field value matches the regular expression pattern
.*logoff.*
or the
action
log field value is equal to
authentication
and the
status
log field value is equal to
logout
or the
action
log field value is equal to
auth-logout
and the
status
log field value is equal to
logout
then, the
metadata.event_type
UDM field is set to
USER_LOGOUT
. if the
action
log field value matches the regular expression pattern
.*logon.*
or the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
login
then, the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
user_id
log field value is
not
empty
and the
user_email
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
USER_CREATION
. Else, the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
If the
event_name
log field value contain one of the following values
LogSpyware
LogPredictiveMachineLearning
or the
subtype
log field value contain one of the following values
LogSpyware
LogPredictiveMachineLearning
endpoint
system
then, the
metadata.event_type
UDM field is set to
SCAN_UNCATEGORIZED
.
If the
user
log field value does not contain one of the following values
Empty
N/A
and if the
metadata.event_type
log field value is equal to
GENERIC_EVENT
then, if the
subtype
log field value is equal to
vpn
and
type
is equal to
event
and if the
action
log field value contain one of the following values
tunnel-up
tunnel-down
then, the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
. Else the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
If the
File_name
log field value is
not
empty
or the
Object
log field value is
not
empty
or the
Objekt
log field value is
not
empty
or the
Infected_Resource
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
PROCESS_UNCATEGORIZED
.
If the
metadata.event_type
log field value matches the regular expression pattern
GENERIC_EVENT
and if the
srcip
log field value is
not
empty
and the
dstip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
. Else, if the
srcip
log field value is
not
empty
then, the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
. Else, if the
action
log field value is equal to
Delete
then, the
metadata.event_type
UDM field is set to
USER_DELETION
. if the
action
log field value is equal to
Edit
then, the
metadata.event_type
UDM field is set to
DEVICE_CONFIG_UPDATE
.
target.application
network.application_protocol
additional.fields
If the
app
log field value is
not
empty
then, map its value to the
target.application
UDM field.
Else, if the
service
log field value is
not
empty
then, the
service
log field value is converted to uppercase. If the uppercase
service
value is one of
DNS
DHCP
SMB
HTTPS
HTTP
then, map the original
service
log field value to the
network.application_protocol
UDM field. Else, map the original
service
log field value to the
target.application
UDM field. In both conditions for the
service
field, also map the key
application_protocol
and the original
service
log field value to the
additional.fields
UDM field.
Else, if (the
type
log field value is equal to
dns
and the
subtype
log field value is one of
dns-query
dns-response
) OR (the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
) then, map the static value
DNS
to the
network.application_protocol
UDM field.
Else, if the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
then, map the static value
DHCP
to the
network.application_protocol
UDM field.
Else, if the
authproto
log field value is
not
empty
then, map its value to the
network.application_protocol
UDM field.
Else, if the
protocol
log field value is
not
empty
then, map its value to the
network.application_protocol
UDM field.
Else, if the
proxyapptype
log field value is
not
empty
then, map its value to the
network.application_protocol
UDM field.
Additionally, if the
type
log field value is equal to
event
and the
method
log field value is
not
empty
then, map the
method
log field value to the
network.application_protocol
UDM field.
service
target.application
network.application_protocol
additional.fields
If the
service
log field value is
not
empty
then, if the
service
value is one of
DNS
DHCP
SMB
HTTPS
HTTP
then, map the
service
log field value to the
network.application_protocol
UDM field. Else, map the
service
log field value to the
target.application
UDM field. In both conditions for the
service
field, also map the key
application_protocol
and the
service
log field value to the
additional.fields
UDM field.
Else, if (the
type
log field value is equal to
dns
and the
subtype
log field value is one of
dns-query
dns-response
) OR (the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
) then, map the static value
DNS
to the
network.application_protocol
UDM field.
Else, if the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
then, map the static value
DHCP
to the
network.application_protocol
UDM field.
Else, if the
authproto
log field value is
not
empty
then, map its value to the
network.application_protocol
UDM field.
Else, if the
protocol
log field value is
not
empty
and the
protocol
log field value is
not
equal to
udp
and the
protocol
log field value is
not
equal to
tcp
then, map the
protocol
log field value to the
network.application_protocol
UDM field.
Else, if the
proxyapptype
log field value is
not
empty
then, map its value to the
network.application_protocol
UDM field.
metadata.ingested_timestamp
The parser no longer populates the
metadata.ingested_timestamp
UDM field. This field is system-populated by Google SecOps at the time of ingestion. It represents the GMT timestamp when the event was ingested (received) by Google Security Operations.
date
time
tz
metadata.ingested_timestamp
If the
date
log field value is
not
empty
and the
tz
log field value is
not
empty
and the
time
log field value is
not
empty
then, concatenate the
date
,
time
, and
tz
log field values (separated by spaces) and map the result to the
metadata.ingested_timestamp
UDM field.
network.application_protocol
If the
type
log field value is equal to
event
and the
method
log field value is
not
empty
, then the
method
log field value is mapped to the
network.application_protocol
UDM field.
method
network.http.user_agent
If the
agent
log field value is
not
empty
then,
agent
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
chgheaders
log field value is
not
empty
then,
chgheaders
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
method
log field value is
not
empty
then,
method
log field is mapped to the
network.http.user_agent
UDM field.
network.dhcp.client_identifier
If the
duid
log field value is
not
empty
, the
duid
field is extracted from the
duid
log field using a Grok pattern. If the extracted
duid
value is
not
empty
, this extracted value is mapped to the
network.dhcp.client_identifier
UDM field.
duid
target.user.userid
If the
duid
log field value is
not
empty
then, The
temp_duid
field is extracted from
duid
log field using the Grok pattern. if the
temp_duid
log field value is
not
empty
then,
temp_duid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
dstuser
log field value is
not
empty
then,
dstuser
log field is mapped to the
target.user.userid
UDM field.
Else, if the
request
log field value is
not
empty
and the
request
log field value matches the regular expression pattern
duid
then, The
d_uid
field is extracted from
request
log field using the Grok pattern. if the
d_uid
log field value is
not
empty
then,
d_uid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value matches the regular expression pattern
(?i)user
then,
name
log field is mapped to the
target.user.userid
UDM field.
Else, if the
cfgpath
log field value is equal to
system.admin
then,
cfgobj
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value matches the regular expression pattern
.
logon.
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
network.dhcp.type
security_result.outcomes[dhcp_msg]
network.application_protocol
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and the
dhcp_msg
log field value is equal to
Ack
then, the
network.dhcp.type
UDM field is set to
ACK
and the
network.application_protocol
UDM field is set to
DHCP
.
The key
dhcp_msg
and the value from the
dhcp_msg
log field are mapped to the
security_result.outcomes
UDM field.
dhcp_msg
network.dns.questions.class
If the
type
log field value is equal to
dns
and the
subtype
log field value is one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
, then the following mappings are applied based on the
qclass
log field value:
- If the
qclass
log field value is equal to
IN
then, the
network.dns.questions.class
UDM field is set to
1
.
- Else, if the
qclass
log field value is equal to
CH
then, the
network.dns.questions.class
UDM field is set to
3
.
- Else, if the
qclass
log field value is equal to
HS
then, the
network.dns.questions.class
UDM field is set to
4
.
qclass
network.dns.questions.class
If the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
qclass
log field value is equal to
IN
then, the
network.dns.questions.class
UDM field is set to
1
.
network.email.from
additional.fields[suser]
If the
suser
log field value matches the email regular expression
(^.+@.+S)
and its length is less than or equal to 256 characters, then the
suser
log field value is mapped to the
network.email.from
UDM field.
Else, the key
suser
and the value from the
suser
log field are mapped to the
additional.fields
UDM field.
suser
principal.user.user_display_name
If the
user
log field value does not contain one of the following values
Empty
N/A
then,
user
log field is mapped to the
principal.user.user_display_name
UDM field.
Else, if the
cn
log field value is
not
empty
then,
cn
log field is mapped to the
principal.user.user_display_name
UDM field.
If the
suser
log field value is
not
empty
and the
suser
log field value does not match the regular expression pattern
^{
then,
suser
log field is mapped to the
principal.user.user_display_name
UDM field.
network.email.to
additional.fields
target.user.userid
target.user.attribute.labels
If the
to
log field value matches the email regular expression pattern
(^.+@.+S)
:
If the length of the
to
log field value is less than or equal to 256, map the
to
log field value to the
network.email.to
UDM field.
Else (if the length is greater than 256), map the key
to
and the value from the
to
log field to the
additional.fields
UDM field.
Else if the
to
log field value is not
empty
and not equal to
N/A
:
If the length of the
to
log field value is less than or equal to 256, map the
to
log field value to the
target.user.userid
UDM field.
Else (if the length is greater than 256), map the key
to
and the value from the
to
log field to the
target.user.attribute.labels
UDM field.
to
network.email.to
If the
to
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.to
UDM field.
Else, if the
recipient
log field value matches the regular expression pattern
(^.+@.+$)
then,
recipient
log field is mapped to the
network.email.to
UDM field.
principal.ip
principal.user.email_addresses
principal.user.userid
principal.user.attribute.labels
target.user.userid
target.user.attribute.labels
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and the
msg
log field value is
not
empty
, then:
The
src_ip
field is extracted from the
msg
log field using a Grok pattern.
If the extracted
src_ip
is not empty, it is mapped to the
principal.ip
UDM field.
Else, if the
user_email
log field value matches the email regular expression pattern
(^.+@.+S)
and its length is less than or equal to 256, the
user_email
log field value is mapped to the
principal.user.email_addresses
UDM field.
Else, if the
user_id
log field value is
not
empty
, the
user_id
log field value is mapped to the
principal.user.userid
UDM field.
If the
clouduser
log field value is
not
empty
:
If the length of the
clouduser
log field value is less than or equal to 256, the
clouduser
log field value is mapped to the
principal.user.userid
UDM field.
Else, the key
clouduser
and the value from the
clouduser
log field are mapped to the
principal.user.attribute.labels
UDM field.
If the
user
log field value is
not
empty
and not equal to
N/A
:
If the length of the
user
log field value is less than or equal to 256:
If the
metadata.event_type
log field value starts with "USER_", the
user
log field value is mapped to the
target.user.userid
UDM field.
Else, the
user
log field value is mapped to the
principal.user.userid
UDM field.
Else (if the length of
user
is greater than 256):
If the
metadata.event_type
log field value starts with "USER_", the key
user
and the value from the
user
log field are mapped to the
target.user.attribute.labels
UDM field.
Else, the key
user
and the value from the
user
log field are mapped to the
principal.user.attribute.labels
UDM field.
Else if the
unauthuser
log field value is
not
empty
:
If the length of the
unauthuser
log field value is less than or equal to 256, the
unauthuser
log field value is mapped to the
principal.user.userid
UDM field.
Else, the key
unauthuser
and the value from the
unauthuser
log field are mapped to the
principal.user.attribute.labels
UDM field.
Else if the
initiator
log field value is
not
empty
:
If the length of the
initiator
log field value is less than or equal to 256, the
initiator
log field value is mapped to the
principal.user.userid
UDM field.
Else, the key
initiator
and the value from the
initiator
log field are mapped to the
principal.user.attribute.labels
UDM field.
Else if the
login
log field value is
not
empty
:
If the length of the
login
log field value is less than or equal to 256, the
login
log field value is mapped to the
principal.user.userid
UDM field.
Else, the key
login
and the value from the
login
log field are mapped to the
principal.user.attribute.labels
UDM field.
user
initiator
login
unauthuser
clouduser
principal.user.userid
If the
user
log field value is
not
empty
and is
not
equal to
N/A
, map the
user
log field value to the
principal.user.userid
UDM field.
Else, if the
initiator
log field value is
not
empty
, map the
initiator
log field value to the
principal.user.userid
UDM field.
Else, if the
login
log field value is
not
empty
, map the
login
log field value to the
principal.user.userid
UDM field.
Else, if the
unauthuser
log field value is
not
empty
, map the
unauthuser
log field value to the
principal.user.userid
UDM field.
security_result.summary
security_result.rule_name
If the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
then:
If the
eventtype
log field value is
not
empty
and is equal to
ftgd_blk
, the
security_result.summary
UDM field is set to
Blocked URL
.
If the
msg
log field value is
not
empty
, the
msg
log field value is mapped to the
security_result.summary
UDM field.
Else, if the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
and the
msg
log field value is
not
empty
and is equal to
File is infected.
, the concatenated value of
msg
and
virus
log fields, separated by "- ", is mapped to the
security_result.summary
UDM field.
Else, if (the
type
log field value is equal to
utm
OR
anomaly
) and (the
subtype
log field value is equal to
ips
OR
anomaly
) and the
attack
log field value is
not
empty
, the
attack
log field value is mapped to the
security_result.summary
UDM field.
Else, if the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
and the
msg
log field value is
not
empty
, the
msg
log field value is mapped to the
security_result.rule_name
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
, the
msg
log field value is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
, the
mode
log field value is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
, key-value pairs are extracted from it. If the resulting
mode
field is
not
empty
, its value is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
, the
reason
field is extracted using a Grok pattern. If the extracted
reason
is not an empty string or a single space, the
reason
value is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
, the
msg
log field value is mapped to the
security_result.summary
UDM field.
msg
attack
mode
reason
virus
security_result.summary
security_result.rule_name
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
webfilter
and if the
eventtype
log field value is equal to
ftgd_blk
then, the
security_result.summary
UDM field is set to
Blocked URL
.
msg
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
virus
and if the
msg
log field value is equal to
File is infected.
then,
%{msg}- %{virus}
log field is mapped to the
security_result.summary
UDM field. Else, if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attack
log field is mapped to the
security_result.summary
UDM field.
Else, if the
logdesc
log field value matches the regular expression pattern
GUI_ENTRY_DELETION
then,
msg
log field is mapped to the
security_result.summary
UDM field.
Else, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
changes
log field value is
not
empty
then, if the
mode
log field value is
not
empty
then,
mode
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg_data
log field value is
not
empty
then, if the
reason
log field value is
not
empty then,
reason
log field is mapped to the
security_result.summary
UDM field.
Else, if the
msg
log field value is
not
empty
then,
msg
log field is mapped to the
security_result.summary
UDM field.
network.session_duration.seconds
If the
duration
log field value is
not
empty
, then the
duration
log field value is mapped to the
network.session_duration.seconds
UDM field.
duration
network.session_duration.seconds
If the
duration
log field value does not contain one of the following values
Empty
0
then,
duration
log field is mapped to the
network.session_duration
UDM field.
Else, if the
durationdelta
log field value is
not
empty
then,
durationdelta
log field is mapped to the
network.session_duration
UDM field.
Else, if the
live
log field value is
not
empty
then,
live
log field is mapped to the
network.session_duration
UDM field.
Else, if the
totalsession
log field value is
not
empty
then,
totalsession
log field is mapped to the
network.session_duration
UDM field.
network.email.to
additional.fields
network.smtp.mail_from
If the
from
log field value matches the email regular expression pattern
(^.+@.+S)
:
If the length of the
from
log field value is less than or equal to 256, map the
from
log field value to the
network.email.to
UDM field.
Else (if the length is greater than 256), map the key
from
and the value from the
from
log field to the
additional.fields
UDM field.
Else if the
sender
log field value matches the email regular expression pattern
(^.+@.+S)
:
If the length of the
sender
log field value is less than or equal to 256, map the
sender
log field value to the
network.smtp.mail_from
UDM field.
sender
network.email.from
If the
from
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.from
UDM field.
Else, if the
sender
log field value matches the regular expression pattern
(^.+@.+$)
then,
sender
log field is mapped to the
network.email.from
UDM field.
network.smtp.rcpt_to
If the
recipient
log field value is
not
empty
and matches the email regular expression pattern
(^.+@.+S)
and its length is less than or equal to 256, then the
recipient
log field value is mapped to the
network.smtp.rcpt_to
UDM field.
recipient
network.email.to
If the
to
log field value matches the regular expression pattern
(^.+@.+$)
then,
to
log field is mapped to the
network.email.to
UDM field.
Else, if the
recipient
log field value matches the regular expression pattern
(^.+@.+$)
then,
recipient
log field is mapped to the
network.email.to
UDM field.
principal.location.country_or_region
principal.asset.attribute.labels
If the
srccountry
log field value is
not
empty
, then the
srccountry
log field value is mapped to the
principal.location.country_or_region
UDM field. Additionally, if the
srcregion
log field value is
not
empty
, the key
srcregion
and the value from the
srcregion
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else (if
srccountry
is empty), the
srcregion
log field value is mapped to the
principal.location.country_or_region
UDM field.
srcregion
principal.asset.location.country_or_region
principal.asset.hardware.manufacturer
principal.asset.attribute.labels
If the
srchwvendor
log field value is
not
empty
, then the
srchwvendor
log field value is mapped to the
principal.asset.hardware.manufacturer
UDM field. Additionally, if the
srcmacvendor
log field value is
not
empty
, the key
srcmacvendor
and the value from the
srcmacvendor
log field are mapped to the
principal.asset.attribute.labels
UDM field.
srchwvendor
srcmacvendor
principal.asset.hardware.manufacturer
If the
srchwvendor
log field value is
not
empty
then,
srchwvendor
log field is mapped to the
principal.asset.hardware.manufacturer
UDM field.
Else, if the
srcmacvendor
log field value is
not
empty
then,
srcmacvendor
log field is mapped to the
principal.asset.hardware.manufacturer
UDM field.
principal.asset.hostname
principal.asset.attribute.labels
If the
type
log field value is equal to
event
and the
subtype
log field value contain one of the following values
ha
router
and if the
devintfname
log field value is
not
empty
then, the concatenated value "Fortinet:" and the
devintfname
log field value is mapped to the
principal.asset.hostname
UDM field.
If (the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
) OR (the
type
log field value is equal to
utm
and the
subtype
log field value contain one of the following values
webfilter
app-ctrl
virus
ssl
voip
ips
anomaly
waf
) OR (the
type
log field value is equal to
event
and the
subtype
log field value contain one of the following values
vpn
wad
) OR (the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
) then:
- If the
srcname
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.asset.hostname
UDM field.
- Else, the key
srcname
and the value from the
srcname
log field are mapped to the
principal.asset.attribute.labels
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and the
dhcp_msg
log field value is equal to
Ack
then:
- If the
hostname
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.asset.hostname
UDM field.
- Else, the key
hostname
and the value from the
hostname
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
then:
- If the
devname
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.asset.hostname
UDM field.
- Else, the key
devname
and the value from the
devname
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
name
log field value is
not
empty
and not equal to
N/A
and the
logdesc
log field value does not match the regular expression pattern
(?i)user
then:
- If the
name
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.asset.hostname
UDM field.
- Else, the key
name
and the value from the
name
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
client_addr
log field value is
not
empty
then:
- If the
client_addr
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.asset.hostname
UDM field.
- Else, the key
client_addr
and the value from the
client_addr
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
shost
log field value is
not
empty
then:
- If the
shost
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.asset.hostname
UDM field.
- Else, the key
shost
and the value from the
shost
log field are mapped to the
principal.asset.attribute.labels
UDM field.
devintfname
srcname
hostname
devname
name
client_addr
shost
principal.asset.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.asset.hostname
UDM field.
principal.hostname
principal.asset.attribute.labels
If the
type
log field value is equal to
event
and the
subtype
log field value contain one of the following values
ha
router
and if the
devintfname
log field value is
not
empty
then, the concatenated value "Fortinet:" and the
devintfname
log field value is mapped to the
principal.hostname
UDM field.
If (the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
) OR (the
type
log field value is equal to
utm
and the
subtype
log field value contain one of the following values
webfilter
app-ctrl
virus
ssl
voip
ips
anomaly
waf
) OR (the
type
log field value is equal to
event
and the
subtype
log field value contain one of the following values
vpn
wad
) OR (the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
) then:
- If the
srcname
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.hostname
UDM field.
- Else, the key
srcname
and the value from the
srcname
log field are mapped to the
principal.asset.attribute.labels
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and the
dhcp_msg
log field value is equal to
Ack
then:
- If the
hostname
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.hostname
UDM field.
- Else, the key
hostname
and the value from the
hostname
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
then:
- If the
devname
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.hostname
UDM field.
- Else, the key
devname
and the value from the
devname
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
name
log field value is
not
empty
and not equal to
N/A
and the
logdesc
log field value does not match the regular expression pattern
(?i)user
then:
- If the
name
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.hostname
UDM field.
- Else, the key
name
and the value from the
name
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
client_addr
log field value is
not
empty
then:
- If the
client_addr
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.hostname
UDM field.
- Else, the key
client_addr
and the value from the
client_addr
log field are mapped to the
principal.asset.attribute.labels
UDM field.
Else if the
shost
log field value is
not
empty
then:
- If the
shost
log field value matches the regular expression pattern
(^.{0,255}$)
, it is mapped to the
principal.hostname
UDM field.
- Else, the key
shost
and the value from the
shost
log field are mapped to the
principal.asset.attribute.labels
UDM field.
devintfname
srcname
hostname
devname
name
client_addr
shost
principal.hostname
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.hostname
UDM field.
principal.asset.category
principal.resource.attribute.labels
If the
devtype
log field value is
empty
, then the
srcfamily
log field value is mapped to the
principal.asset.category
UDM field.
Else, the key
srcfamily
and the value from the
srcfamily
log field are mapped to the
principal.resource.attribute.labels[srcfamily]
UDM field.
srcfamily
principal.resource.attribute.labels[srcfamily]
principal.resource.attribute.labels
additional.fields
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
and the
tunnelid
log field value is not
empty
and not equal to
N/A
, then map the key
tunnelid
and the value from the
tunnelid
log field to the
principal.resource.attribute.labels
UDM field.
Else, map the key
tunnelid
and the value from the
tunnelid
log field to the
additional.fields
UDM field.
tunnelid
principal.resource.attribute.labels[tunnelid]
principal.resource.attribute.labels
additional.fields
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
and the
vpntunnel
log field value is not
empty
and not equal to
N/A
, then map the key
vpntunnel
and the value from the
vpntunnel
log field to the
principal.resource.attribute.labels
UDM field.
Else, map the key
vpntunnel
and the value from the
vpntunnel
log field to the
additional.fields
UDM field.
vpntunnel
principal.resource.attribute.labels[vpntunnel]
principal.resource.attribute.labels
target.user.attribute.labels
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
and the
xauthgroup
log field value is not
empty
and not equal to
N/A
, then map the key
xauthgroup
and the value from the
xauthgroup
log field to the
principal.resource.attribute.labels
UDM field.
Else, map the key
xauthgroup
and the value from the
xauthgroup
log field to the
target.user.attribute.labels
UDM field.
xauthgroup
principal.resource.attribute.labels[xauthgroup]
principal.resource.attribute.labels
target.user.attribute.labels
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
and the
xauthuser
log field value is not
empty
and not equal to
N/A
, then map the key
xauthuser
and the value from the
xauthuser
log field to the
principal.resource.attribute.labels
UDM field.
Else, map the key
xauthuser
and the value from the
xauthuser
log field to the
target.user.attribute.labels
UDM field.
xauthuser
principal.resource.attribute.labels[xauthuser]
target.user.group_identifiers
principal.user.group_identifiers
If the
group
log field value is
not
empty
and is
not
equal to
N/A
then:
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
, map the
group
log field value to the
target.user.group_identifiers
UDM field.
Else, map the
group
log field value to the
principal.user.group_identifiers
UDM field.
group
principal.user.group_identifiers
If the
group
log field value is
not
empty
and is
not
equal to
N/A
, map the
group
log field value to the
principal.user.group_identifiers
UDM field.
security_result.description
If the
reason
log field value is not equal to
N/A
and is not
empty
, then the
reason
log field value is mapped to the
security_result.description
UDM field.
reason
security_result.description
If the
utmaction
log field value matches the regular expression pattern
(?i)block
and if the
action
log field value matches the regular expression pattern
(?i)accept
or the
action
log field value matches the regular expression pattern
(?i)close
then,
UTMAction: %{utmaction}
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
reason
log field value is
not
equal to
N/A
and the
reason
log field value is
not
empty
then,
reason
log field is mapped to the
security_result.description
UDM field. if the
subtype
log field value is equal to
webfilter
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
type
log field value is equal to
dns
and the
subtype
log field value contain one of the following values
dns-query
dns-response
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
dns
and if the
catdesc
log field value is
not
empty
then,
%{msg} - URL Category: %{catdesc}
log field is mapped to the
security_result.description
UDM field.
Else, if the
fortiguardresp
log field value is
not
empty
then,
fortiguardresp
log field is mapped to the
security_result.description
UDM field.
Else, if the
malform_desc
log field value is
not
empty
then,
malform_desc
log field is mapped to the
security_result.description
UDM field.
Else, if the
result
log field value does not contain one of the following values
Empty
N/A
then,
result
log field is mapped to the
security_result.description
UDM field.
Else, if the
path
log field value is
not
empty
then,
path
log field is mapped to the
security_result.description
UDM field.
Else, If the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
forward
and if the
action
log field value matches the regular expression pattern
(?i)timeout
then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value is equal to
local
and if the
action
log field value matches the regular expression pattern
timeout
and
rcvdpkt
> 0 then, the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value contain one of the following values
accept
passthrough
pass
permit
detected
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
auth-logon
client-rst
server-rst
start
or the
utmaction
log field value contain one of the following values
accept
allow
passthrough
pass
detected
permit
close
tunnel-down
tunnel-stats
tunnel-up
ssl-new-con
or the
status
log field value is equal to
success
or the
outcome
log field value is equal to
REDIRECTED_USER_MAY_PROCEED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Success|Success)
or the
cs2
log field value matches the regular expression pattern
Allow
then, the
security_result.description
UDM field is set to
Action: ALLOW
.
Else, if the
action
log field value contain one of the following values
deny
dropped
blocked
block
timeout
negotiate
ssl-login-fail
clear_session
or the
utmaction
log field value contain one of the following values
deny
dropped
blocked
timeout
negotiate
ssl-login-fail
clear_session
deny
dropped
blocked
block
timeout
negotiate
or the
status
log field value is equal to
failure
or the
status
log field value is equal to
failed
or the
outcome
log field value is equal to
BLOCKED
or the
categoryOutcome
log field value matches the regular expression pattern
(/Failure|Failed)
or the
cs2
log field value matches the regular expression pattern
Denied
then, the
security_result.description
UDM field is set to
Action: BLOCK
.
Else, if the
outcome
log field value matches the regular expression pattern
Failure
then, the
security_result.description
UDM field is set to
Action: FAIL
.
security_result.rule_id
security_result.rule_labels
If the
policyid
log field value is
not
empty
and not equal to
0
, then the
policyid
log field value is mapped to the
security_result.rule_id
UDM field. In this case, if the
poluuid
log field value is also
not
empty
, the key
poluuid
and the value from the
poluuid
log field are mapped to the
security_result.rule_labels
UDM field.
Else, if the
attackid
log field value is
not
empty
, the
attackid
log field value is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
, the
poluuid
log field value is mapped to the
security_result.rule_id
UDM field.
Else, if the
ruleid
log field value is
not
empty
, the
ruleid
log field value is mapped to the
security_result.rule_id
UDM field.
Additionally, if the
policy_id
log field value is
not
empty
, the
policy_id
log field value is mapped to the
security_result.rule_id
UDM field.
attackid
ruleid
policyid
poluuid
policy_id
security_result.rule_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
then:
If the
policyid
log field value is
not
empty
, it is mapped to the
security_result.rule_id
UDM field.
If the
attackid
log field value is
not
empty
, it is mapped to the
security_result.rule_id
UDM field.
If the
subtype
log field value is equal to
webfilter
and the
cat
log field value is
not
empty
, the
cat
log field value is mapped to the
security_result.rule_id
UDM field.
If the
security_result.rule_id
UDM field is not already populated:
If the
ruleid
log field value is
not
empty
, it is mapped to the
security_result.rule_id
UDM field.
Else, if the
appid
log field value is
not
empty
, it is mapped to the
security_result.rule_id
UDM field.
Else, if the
policyid
log field value is
not
empty
, it is mapped to the
security_result.rule_id
UDM field.
Else, if the
poluuid
log field value is
not
empty
, it is mapped to the
security_result.rule_id
UDM field.
security_result.threat_id
If the
virusid
log field value is
not
empty
then, the
security_result.threat_id
UDM field is set to the value of
virusid
.
If the
attackid
log field value is
not
empty
then, the
security_result.threat_id
UDM field is set to the value of
attackid
.
attackid
virusid
security_result.threat_id
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
virusid
log field value is
not
empty
then,
virusid
log field is mapped to the
security_result.threat_id
UDM field. if the
subtype
log field value is equal to
ips
or the
subtype
log field value is equal to
anomaly
then,
attackid
log field is mapped to the
security_result.threat_id
UDM field.
security_result.threat_name
If the
attack
log field value is
not
empty
then, the
security_result.threat_name
UDM field is set to the value of
attack
.
If the
virus
log field value is
not
empty
then, the
security_result.threat_name
UDM field is set to the value of
virus
.
attack
virus
security_result.threat_name
If the
attack
log field value is
not
empty
then,
attack
log field is mapped to the
security_result.threat_name
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
virus
then,
virus
log field is mapped to the
security_result.threat_name
UDM field.
security_result.rule_labels
additional.fields[name]
If the
name
log field value is
not
empty
and is
not
equal to
N/A
, then the logic is applied as follows:
If the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
then, map the key
name
and the value from the
name
log field to the
security_result.rule_labels
UDM field.
Else, map the key
name
and the value from the
name
log field to the
additional.fields
UDM field.
name
target.user.userid
principal.hostname
principal.asset.hostname
If the
duid
log field value is
not
empty
then, The
temp_duid
field is extracted from
duid
log field using the Grok pattern. if the
temp_duid
log field value is
not
empty
then,
temp_duid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
dstuser
log field value is
not
empty
then,
dstuser
log field is mapped to the
target.user.userid
UDM field.
Else, if the
request
log field value is
not
empty
and the
request
log field value matches the regular expression pattern
duid
then, The
d_uid
field is extracted from
request
log field using the Grok pattern. if the
d_uid
log field value is
not
empty
then,
d_uid
extracted field is mapped to the
target.user.userid
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value matches the regular expression pattern
(?i)user
then,
name
log field is mapped to the
target.user.userid
UDM field.
Else, if the
cfgpath
log field value is equal to
system.admin
then,
cfgobj
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value is equal to
auth-logon
and the
status
log field value is equal to
logon
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
Else, if the
action
log field value matches the regular expression pattern
.
logon.
and if the
user
log field value is
not
empty
and the
user
log field value is
not
equal to
N/A
then,
user
log field is mapped to the
target.user.userid
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.asset.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.asset.hostname
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then,
hostname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
utmevent
log field value is
not
equal to
appfirewall
and the
subtype
log field value is equal to
system
and the
srcname
log field value is
not
empty
then,
srcname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
devname
log field value is
not
empty
then,
devname
log field is mapped to the
principal.hostname
UDM field.
Else, if the
name
log field value is
not
empty
and the
name
log field value is
not
equal to
N/A
and if the
logdesc
log field value does not match the regular expression pattern
(?i)user
then,
name
log field is mapped to the
principal.hostname
UDM field.
Else, if the
client_addr
log field value is
not
empty
then,
client_addr
log field is mapped to the
principal.hostname
UDM field.
Else, if the
shost
log field value is
not
empty
then,
shost
log field is mapped to the
principal.hostname
UDM field.
network.email.to
additional.fields
target.user.userid
target.user.attribute.labels
If the
duser
log field value matches the regular expression pattern
(^.+@.+$)
then, the logic is applied as follows:
If the
duser
log field value matches the regular expression pattern
(^.{0,256}$)
then, the
network.email.to
UDM field is set to the value of
duser
.
Else, map the key
duser
and the value from the
duser
log field to the
additional.fields
UDM field.
Else, if the
duser
log field value is
not
empty
and is
not
equal to
N/A
then, the logic is applied as follows:
If the
duser
log field value matches the regular expression pattern
(^.{0,256}$)
then, the
target.user.userid
UDM field is set to the value of
duser
.
Else, map the key
duser
and the value from the
duser
log field to the
target.user.attribute.labels
UDM field.
duser
target.user.user_display_name
If the
dstunauthuser
log field value is
empty
then, the
target.user.user_display_name
UDM field is set to the value of
duser
.
target.asset.hostname
target.asset.attribute.labels
intermediary.hostname
additional.fields
If the
dstname
log field value is
not
empty
, then the logic is applied as follows:
If the
dstname
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
dstname
.
Else, map the key
dstname
and the value from the
dstname
log field to the
target.asset.attribute.labels
UDM field.
Else, if the
dst_host
log field value is
not
empty
and is
not
equal to
N/A
, then the logic is applied as follows:
If the
dst_host
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
dst_host
.
Else, map the key
dst_host
and the value from the
dst_host
log field to the
target.asset.attribute.labels
UDM field.
Else, if the
hostname
log field value is
not
empty
, then the logic is applied as follows:
If the
hostname
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
hostname
.
Else, map the key
hostname
and the value from the
hostname
log field to the
target.asset.attribute.labels
UDM field.
Else, if the
dstauthserver
log field value is
not
empty
, then the logic is applied as follows:
If the
dstauthserver
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
dstauthserver
.
Else, map the key
dstauthserver
and the value from the
dstauthserver
log field to the
target.asset.attribute.labels
UDM field.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
and the
server
log field value is
not
empty
, then the logic is applied as follows:
If the
server
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
server
.
Else, map the key
server
and the value from the
server
log field to the
target.asset.attribute.labels
UDM field.
If the
host
log field value is
not
empty
, then the logic is applied as follows:
If the
host
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
host
.
Else, map the key
host
and the value from the
host
log field to the
target.asset.attribute.labels
UDM field.
If the
domainctrldomain
log field value is
not
empty
, then the logic is applied as follows:
If the
domainctrldomain
log field value matches the regular expression pattern
(^.{0,255}$)
then, the
target.asset.hostname
UDM field is set to the value of
domainctrldomain
.
Else, map the key
domainctrldomain
and the value from the
domainctrldomain
log field to the
target.asset.attribute.labels
UDM field.
If the
devname
log field value is
not
empty
, then the logic is applied as follows:
If the
devname
log field value matches the regular expression pattern
(^.{0,255}$)
then, the logic is applied as follows:
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then, the
target.asset.hostname
UDM field is set to the value of
devname
.
Else, the
intermediary.hostname
UDM field is set to the value of
devname
.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
system
then, map the key
devname
and the value from the
devname
log field to the
target.asset.attribute.labels
UDM field.
Else, map the key
devname
and the value from the
devname
log field to the
additional.fields
UDM field.
devname
dhost
domainctrldomain
dst_host
dstauthserver
dstname
dstserver
dvchost
host
hostname
server
target.asset.hostname
intermediary.hostname
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
empty
forward
local
system
OR the
type
log field value is equal to
utm
and the
subtype
log field value contain one of the following values
webfilter
app-ctrl
virus
ssl
voip
ips
anomaly
waf
OR the
type
log field value is equal to
event
and the
subtype
log field value contain one of the following values
vpn
wad
OR the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
then, the logic is applied as follows:
If the
subtype
log field value is equal to
vpn
then, the
target.asset.hostname
UDM field is set to the value of
devname
.
Else, if the
action
log field value is equal to
login
and the
devname
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
devname
.
Else, if the
dstserver
log field value is
not
equal to
0
or
1
or
empty
then, the
target.asset.hostname
UDM field is set to the value of
dstserver
.
Else, if the
dst_host
log field value is
not
equal to
N/A
or
empty
then, the
target.asset.hostname
UDM field is set to the value of
dst_host
.
Else, if the
dhost
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
dhost
.
Else, if the
hostname
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
hostname
.
Else, if the
dstauthserver
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
dstauthserver
.
Else, if the
type
log field value is equal to
event
and the
subtype
log field value is equal to
user
then, the logic is applied as follows:
If the
server
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
server
.
Else, the
target.asset.hostname
UDM field is set to the value of
devname
.
Else, if the
dstname
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
dstname
.
If the
host
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
host
.
If the
action
log field value is equal to
login
and the
devname
log field value is
not
empty
then, the
target.asset.hostname
UDM field is set to the value of
devname
.
If the
dvchost
log field value is
not
empty
then, the
intermediary.hostname
UDM field is set to the value of
dvchost
.
Else, if the
devname
log field value is
not
empty
then, the
intermediary.hostname
UDM field is set to the value of
devname
.
Else, if the
domainctrldomain
log field value is
not
empty
then, the
intermediary.hostname
UDM field is set to the value of
domainctrldomain
.
target.ip
principal.ip
If the
dstip
log field value is
not
empty
and is
not
equal to
N/A
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
dstip
.
If the
vipincomingip
log field value is
not
empty
and is
not
equal to
N/A
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
vipincomingip
.
If the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
OR the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
then, the logic is applied as follows:
If the
subtype
log field value is equal to
vpn
then, the logic is applied as follows:
If the
tunnelip
log field value is
not
equal to
N/A
or
empty
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
tunnelip
.
If the
remip
log field value is
not
empty
OR the
locip
log field value is
not
empty
, and they contain valid IP addresses, then the logic is applied as follows:
If the
dir
log field value is equal to
outbound
then, the
target.ip
UDM field is set to the value of
remip
and the
principal.ip
UDM field is set to the value of
locip
.
Else, the
principal.ip
UDM field is set to the value of
remip
and the
target.ip
UDM field is set to the value of
locip
.
If the
gateway
log field value is
not
empty
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
gateway
.
If the
daddr
log field value is
not
empty
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
daddr
.
If the
end-usr-address
log field value is
not
empty
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
end-usr-address
.
If the
endusraddress6
log field value is
not
empty
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
endusraddress6
.
If the
rem_ip
log field value is
not
empty
and contains a valid IP address, then the
target.ip
UDM field is set to the value of
rem_ip
.
daddr
dstip
end-usr-address
endusraddress6
gateway
locip
rem_ip
remip
tunnelip
vipincomingip
target.ip
principal.ip
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_local_ip
log field value is
not
empty
then,
valid_local_ip
log field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
log field is mapped to the
target.ip
UDM field.
If the
dstip
log field value is
not
empty
and the
dstip
log field value is
not
equal to
N/A
then, The
dst_ip
field is extracted from
dstip
log field using the Grok pattern. if the
dst_ip
log field value is
not
empty
then,
dst_ip
extracted field is mapped to the
target.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
log field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
log field is mapped to the
target.ip
UDM field. Else,
valid_remip
log field is mapped to the
principal.ip
UDM field.
If the
ui
log field value is
not
empty
then, The
prin_ip
field is extracted from
ui
log field using the Grok pattern. The
desc
and
prin_ip
fields is extracted from
ui
log field using the Grok pattern. if the
prin_ip
log field value is
not
empty
and the
ip
log field value is
not
equal to
the
prin_ip
log field value
then,
prin_ip
extracted field is mapped to the
principal.ip
UDM field.
Iterate through log field
forwardedfor
, then
if the
index
value is equal to
0
then,
forwardedfor
log field is mapped to the
principal.ip
UDM field.
Else,
forwardedfor
log field is mapped to the
principal.nat_ip
UDM field.
If the
saddr
log field value is
not
empty
then, The
valid_saddr
field is extracted from
saddr
log field using the Grok pattern.
valid_saddr
log field is mapped to the
principal.ip
UDM field.
Else, if
srcremote
log field value is
not
empty
then, The
valid_srcremote
field is extracted from
srcremote
log field using the Grok pattern.
valid_srcremote
log field is mapped to the
principal.ip
UDM field.
Else, if
host
log field value is
not
empty
then, The
valid_shost
field is extracted from
shost
log field using the Grok pattern. if the
valid_shost
log field value is
not
empty
then,
valid_shost
log field is mapped to the
principal.ip
UDM field.
Else, if
user
log field value does not contain one of the following values
Empty
N/A
then, The
valid_user_ip
field is extracted from
user
log field using the Grok pattern. if the
valid_user_ip
log field value is
not
empty
then,
valid_user_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
subtype
log field value contain one of the following values
endpoint
system
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
event
and the
dhcp_msg
log field value is
not
empty
and if the
dhcp_msg
log field value is equal to
Ack
then, The
valid_ip
field is extracted from
ip
log field using the Grok pattern.
valid_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and the
locip
log field value is
not
empty
then, The
valid_local_ip
field is extracted from
locip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
then,
valid_local_ip
extracted field is mapped to the
principal.ip
UDM field. Else,
valid_local_ip
extracted field is mapped to the
target.ip
UDM field.
If the
srcip
log field value is
not
empty
then, The
src_ip
field is extracted from
srcip
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
Else, if the
src
log field value is
not
empty
then, The
src_ip
field is extracted from
src
log field using the Grok pattern.
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
action
log field value is equal to
Add
and the
subtype
log field value is equal to
Admin
and if the
msg
log field value is
not
empty
then, The
src_ip
field is extracted from
msg
log field using the Grok pattern. if the
src_ip
log field value is
not
empty
then,
src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
banned_src
log field value is
not
empty
then, The
banned_src_ip
field is extracted from
banned_src
log field using the Grok pattern.
banned_src_ip
extracted field is mapped to the
principal.ip
UDM field.
If the
type
log field value is equal to
traffic
and the
subtype
log field value contain one of the following values
Empty
forward
local
system
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
webfilter
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
app-ctrl
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
vpn
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
virus
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ssl
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
voip
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
ips
or the
type
log field value is equal to
event
and the
subtype
log field value is equal to
wad
or the
type
log field value is equal to
anomaly
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
anomaly
or the
type
log field value is equal to
utm
and the
subtype
log field value is equal to
waf
and if the
subtype
log field value is equal to
vpn
and if the
tunnelip
log field value does not contain one of the following values
Empty
N/A
then, The
tunnel_ip
field is extracted from
tunnelip
log field using the Grok pattern. if the
tunnel_ip
log field value is
not
empty
then,
tunnel_ip
extracted field is mapped to the
target.ip
UDM field. if the
remip
log field value is
not
empty
then, The
valid_remip
field is extracted from
remip
log field using the Grok pattern. if the
dir
log field value is
not
empty
and the
dir
log field value is equal to
outbound
and if the
valid_remip
log field value is
not
empty
then,
valid_remip
extracted field is mapped to the
target.ip
UDM field. Else,
valid_remip
extracted field is mapped to the
principal.ip
UDM field.
user_email
extracted fields are mapped to the
principal.ip
UDM field.
Need more help?
Get answers from Community members and Google SecOps professionals.
