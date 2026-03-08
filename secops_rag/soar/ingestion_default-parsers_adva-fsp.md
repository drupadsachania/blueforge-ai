# Collect ADVA Fiber Service Platform logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/adva-fsp/  
**Scraped:** 2026-03-05T09:49:22.212490Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ADVA Fiber Service Platform logs
Supported in:
Google secops
SIEM
This document explains how to ingest ADVA Fiber Service Platform (ADVA FSP) logs to Google Security Operations using Bindplane. The parser extracts fields from the switch and router syslog messages, converting them into key-value pairs. It then maps these extracted fields and their values to corresponding fields within the Chronicle UDM schema, enriching the data for security analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A Windows 2012 SP2 or later or Linux host with
systemd
If running behind a proxy, ensure firewall ports are open per the Bindplane agent requirements
Privileged access to the ADVA FSP device management console
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the 
system where Bindplane will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open the
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Additional installation resources
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file. The following are two working receiver options; choose the one that matches how your device sends logs:
Option A - UDP log receiver (simple UDP)
receivers
:
udplog
:
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'ADVA_FSP'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/adva-fsp
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Option B - Syslog receiver (recommended for strict syslog framing)
receivers
:
syslog
:
tcp
:
listen_address
:
"0.0.0.0:514"
protocol
:
rfc5424
# or rfc3164 if your device uses BSD syslog
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
customer_id
:
<
CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
log_type
:
'ADVA_FSP'
raw_log_field
:
body
ingestion_labels
:
source
:
'adva-fsp'
env
:
'production'
service
:
pipelines
:
logs/adva-fsp
:
receivers
:
-
syslog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<CUSTOMER_ID>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding on ADVA FSP
Sign in to the
ADVA FSP Management Console
.
Go to
Node
>
General
>
Controls
.
In the
Remote Event Recipients (SysLog)
section, click
Add
.
Provide the following configuration details:
IPv4/v6 Address
: Enter the Bindplane agent IP address.
Port
: Enter the Bindplane agent port number (for example,
514
).
Protocol
: Select
UDP
or
TCP
, depending on your actual Bindplane agent configuration.
Message Extension
: Optional: Click
Add User Label
to include additional identifiers in messages.
Click
Save
to activate the configuration.
UDM Mapping Table
Log field
UDM mapping
Logic
ACCESSORDER
additional.fields.value.string_value
The value is taken from the ACCESSORDER field in the raw log.
ADDRESS
principal.ip
The value is taken from the ADDRESS field in the raw log and parsed as an IP address.
ADMINSTATE
additional.fields.value.string_value
The value is taken from the ADMINSTATE field in the raw log.
AISCLIENTMDLEVEL
additional.fields.value.string_value
The value is taken from the AISCLIENTMDLEVEL field in the raw log.
AISGENENABLED
additional.fields.value.string_value
The value is taken from the AISGENENABLED field in the raw log.
AISPRIORITY
additional.fields.value.string_value
The value is taken from the AISPRIORITY field in the raw log.
AISTXPERIOD
additional.fields.value.string_value
The value is taken from the AISTXPERIOD field in the raw log.
AISTRIGGERTYPES
additional.fields.value.string_value
The value is taken from the AISTRIGGERTYPES field in the raw log.
BUFFERSIZE
additional.fields.value.string_value
The value is taken from the BUFFERSIZE field in the raw log.
CCIENABLED
additional.fields.value.string_value
The value is taken from the CCIENABLED field in the raw log.
CCMINTERFACESTATUSTLVCONTROL
additional.fields.value.string_value
The value is taken from the CCMINTERFACESTATUSTLVCONTROL field in the raw log.
CCMLTMPRIORITY
additional.fields.value.string_value
The value is taken from the CCMLTMPRIORITY field in the raw log.
CFMTAGETHERTYPE
additional.fields.value.string_value
The value is taken from the CFMTAGETHERTYPE field in the raw log.
CIR
additional.fields.value.string_value
The value is taken from the CIR field in the raw log.
COS
additional.fields.value.string_value
The value is taken from the COS field in the raw log.
CT
metadata.description
The value is taken from the CT field in the raw log.
DESTBMAC
target.mac
The value is taken from the DESTBMAC field in the raw log and parsed as a MAC address.
DHCPCIDENABLED
additional.fields.value.string_value
The value is taken from the DHCPCIDENABLED field in the raw log.
DHCPENABLED
additional.fields.value.string_value
The value is taken from the DHCPENABLED field in the raw log.
DHCPHOSTNAME
network.dhcp.client_hostname
The value is taken from the DHCPHOSTNAME field in the raw log.
DHCPHOSTNAMEENABLED
additional.fields.value.string_value
The value is taken from the DHCPHOSTNAMEENABLED field in the raw log.
DHCPHOSTNAMETYPE
additional.fields.value.string_value
The value is taken from the DHCPHOSTNAMETYPE field in the raw log.
DHCPLOGSERVERENABLED
additional.fields.value.string_value
The value is taken from the DHCPLOGSERVERENABLED field in the raw log.
DHCPNTPSERVERENABLED
additional.fields.value.string_value
The value is taken from the DHCPNTPSERVERENABLED field in the raw log.
DHCPV6CIDENABLED
additional.fields.value.string_value
The value is taken from the DHCPV6CIDENABLED field in the raw log.
DHCPV6ENABLED
additional.fields.value.string_value
The value is taken from the DHCPV6ENABLED field in the raw log.
DHCPV6ROLE
additional.fields.value.string_value
The value is taken from the DHCPV6ROLE field in the raw log.
DHCPVENDORINFOTYPE
additional.fields.value.string_value
The value is taken from the DHCPVENDORINFOTYPE field in the raw log.
DIR
additional.fields.value.string_value
The value is taken from the DIR field in the raw log.
DIRECTION
network.direction
The value is set to "OUTBOUND" if the DIRECTION field in the raw log is "UP" (case-insensitive), "INBOUND" if it is "DOWN", and is left empty otherwise.
ENCAPSULATIONTYPE
additional.fields.value.string_value
The value is taken from the ENCAPSULATIONTYPE field in the raw log.
GUARANTEEDA2NBW
additional.fields.value.string_value
The value is taken from the GUARANTEEDA2NBW field in the raw log.
HCOSMGMTENABLED
additional.fields.value.string_value
The value is taken from the HCOSMGMTENABLED field in the raw log.
INT
additional.fields.value.string_value
The value is taken from the INT field in the raw log.
IPMODE
additional.fields.value.string_value
The value is taken from the IPMODE field in the raw log.
IPV6ADDR
principal.ip
The value is taken from the IPV6ADDR field in the raw log and parsed as an IP address.
IPV6ADDRPREFIXLENGTH
additional.fields.value.string_value
The value is taken from the IPV6ADDRPREFIXLENGTH field in the raw log.
IPV6MTU
additional.fields.value.string_value
The value is taken from the IPV6MTU field in the raw log.
ITAG
additional.fields.value.string_value
The value is taken from the ITAG field in the raw log.
ITAGENABLED
additional.fields.value.string_value
The value is taken from the ITAGENABLED field in the raw log.
LBMTXDESTTYPE
additional.fields.value.string_value
The value is taken from the LBMTXDESTTYPE field in the raw log.
LBMTXNUMMSGS
additional.fields.value.string_value
The value is taken from the LBMTXNUMMSGS field in the raw log.
LBMTXVLANDROPENABLE
additional.fields.value.string_value
The value is taken from the LBMTXVLANDROPENABLE field in the raw log.
LBMTXVLANPRIORITY
additional.fields.value.string_value
The value is taken from the LBMTXVLANPRIORITY field in the raw log.
LLRESPONDERENABLED
additional.fields.value.string_value
The value is taken from the LLRESPONDERENABLED field in the raw log.
LLVIDLIST
additional.fields.value.string_value
The value is taken from the LLVIDLIST field in the raw log.
LMDUALENDEDCOUNTALLPRIOS
additional.fields.value.string_value
The value is taken from the LMDUALENDEDCOUNTALLPRIOS field in the raw log.
LMINPROFILEONLY
additional.fields.value.string_value
The value is taken from the LMINPROFILEONLY field in the raw log.
LMRXCOUNTALLPRIOS
additional.fields.value.string_value
The value is taken from the LMRXCOUNTALLPRIOS field in the raw log.
LMTXCOUNTALLPRIOS
additional.fields.value.string_value
The value is taken from the LMTXCOUNTALLPRIOS field in the raw log.
LOC
additional.fields.value.string_value
The value is taken from the LOC field in the raw log.
LOCN
additional.fields.value.string_value
The value is taken from the LOCN field in the raw log.
LOGINTIMEOUT
additional.fields.value.string_value
The value is taken from the LOGINTIMEOUT field in the raw log.
LOOPBACKBLOCKINGENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKBLOCKINGENABLED field in the raw log.
LOOPBACKCONFIG
additional.fields.value.string_value
The value is taken from the LOOPBACKCONFIG field in the raw log.
LOOPBACKDESTMAC
target.mac
The value is taken from the LOOPBACKDESTMAC field in the raw log and parsed as a MAC address.
LOOPBACKDESTMACCONTROL
additional.fields.value.string_value
The value is taken from the LOOPBACKDESTMACCONTROL field in the raw log.
LOOPBACKINNERVLAN1
additional.fields.value.string_value
The value is taken from the LOOPBACKINNERVLAN1 field in the raw log.
LOOPBACKINNERVLAN1ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKINNERVLAN1ENABLED field in the raw log.
LOOPBACKINNERVLAN2
additional.fields.value.string_value
The value is taken from the LOOPBACKINNERVLAN2 field in the raw log.
LOOPBACKINNERVLAN2ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKINNERVLAN2ENABLED field in the raw log.
LOOPBACKINNERVLAN3
additional.fields.value.string_value
The value is taken from the LOOPBACKINNERVLAN3 field in the raw log.
LOOPBACKINNERVLAN3ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKINNERVLAN3ENABLED field in the raw log.
LOOPBACKOUTERITAG1
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERITAG1 field in the raw log.
LOOPBACKOUTERITAG1ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERITAG1ENABLED field in the raw log.
LOOPBACKOUTERITAG2
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERITAG2 field in the raw log.
LOOPBACKOUTERITAG2ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERITAG2ENABLED field in the raw log.
LOOPBACKOUTERITAG3
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERITAG3 field in the raw log.
LOOPBACKOUTERITAG3ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERITAG3ENABLED field in the raw log.
LOOPBACKOUTERVLAN1
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERVLAN1 field in the raw log.
LOOPBACKOUTERVLAN1ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERVLAN1ENABLED field in the raw log.
LOOPBACKOUTERVLAN2
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERVLAN2 field in the raw log.
LOOPBACKOUTERVLAN2ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERVLAN2ENABLED field in the raw log.
LOOPBACKOUTERVLAN3
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERVLAN3 field in the raw log.
LOOPBACKOUTERVLAN3ENABLED
additional.fields.value.string_value
The value is taken from the LOOPBACKOUTERVLAN3ENABLED field in the raw log.
LOOPBACKSOURCEMAC
principal.mac
The value is taken from the LOOPBACKSOURCEMAC field in the raw log and parsed as a MAC address.
LOOPBACKSWAPSADA
additional.fields.value.string_value
The value is taken from the LOOPBACKSWAPSADA field in the raw log.
LOOPBACKTIMER
additional.fields.value.string_value
The value is taken from the LOOPBACKTIMER field in the raw log.
LOWESTPRIODEFECT
additional.fields.value.string_value
The value is taken from the LOWESTPRIODEFECT field in the raw log.
LTMTXDESTTYPE
additional.fields.value.string_value
The value is taken from the LTMTXDESTTYPE field in the raw log.
LTMTXEGRESSID
metadata.product_log_id
The value is taken from the LTMTXEGRESSID field in the raw log.
LTMTXFLAGS
additional.fields.value.string_value
The value is taken from the LTMTXFLAGS field in the raw log.
LTMTXTTL
additional.fields.value.string_value
The value is taken from the LTMTXTTL field in the raw log.
MT
additional.fields.value.string_value
The value is taken from the MT field in the raw log.
MAXIMUMA2NBW
additional.fields.value.string_value
The value is taken from the MAXIMUMA2NBW field in the raw log.
MVAL
additional.fields.value.string_value
The value is taken from the MVAL field in the raw log.
NAME
additional.fields.value.string_value
The value is taken from the NAME field in the raw log.
NC
additional.fields.value.string_value
The value is taken from the NC field in the raw log.
PORTEID
additional.fields.value.string_value
The value is taken from the PORTEID field in the raw log.
PORTLLENABLED
additional.fields.value.string_value
The value is taken from the PORTLLENABLED field in the raw log.
PRIMARYSERVER
target.ip
The value is taken from the PRIMARYSERVER field in the raw log and parsed as an IP address.
PRIMARYVID
additional.fields.value.string_value
The value is taken from the PRIMARYVID field in the raw log.
QUEUEPROFILEID
additional.fields.value.string_value
The value is taken from the QUEUEPROFILEID field in the raw log.
RXSHAPEREID
additional.fields.value.string_value
The value is taken from the RXSHAPEREID field in the raw log.
SATRESPONDENABLED
additional.fields.value.string_value
The value is taken from the SATRESPONDENABLED field in the raw log.
SE
additional.fields.value.string_value
The value is taken from the SE field in the raw log.
SHAREDVIM
additional.fields.value.string_value
The value is taken from the SHAREDVIM field in the raw log.
SVLANENABLED
additional.fields.value.string_value
The value is taken from the SVLANENABLED field in the raw log.
SVLANID
additional.fields.value.string_value
The value is taken from the SVLANID field in the raw log.
SYSLOCATION
principal.location.country_or_region
The value is taken from the SYSLOCATION field in the raw log.
THVAL
additional.fields.value.string_value
The value is taken from the THVAL field in the raw log.
TYPE
additional.fields.value.string_value
The value is taken from the TYPE field in the raw log.
USERACCESSTYPE
additional.fields.value.string_value
The value is taken from the USERACCESSTYPE field in the raw log.
USERAUTHKEY
additional.fields.value.string_value
The value is taken from the USERAUTHKEY field in the raw log.
USERAUTHKEYLOCAL
additional.fields.value.string_value
The value is taken from the USERAUTHKEYLOCAL field in the raw log.
USERAUTHPROTOCOL
additional.fields.value.string_value
The value is taken from the USERAUTHPROTOCOL field in the raw log.
USERENGINEID
additional.fields.value.string_value
The value is taken from the USERENGINEID field in the raw log.
USERKEYSLOCAL
additional.fields.value.string_value
The value is taken from the USERKEYSLOCAL field in the raw log.
USERNAME
principal.user.userid
The value is taken from the USERNAME field in the raw log.
USERPRIVKEY
additional.fields.value.string_value
The value is taken from the USERPRIVKEY field in the raw log.
USERPRIVKEYLOCAL
additional.fields.value.string_value
The value is taken from the USERPRIVKEYLOCAL field in the raw log.
USERPRIVPROTOCOL
additional.fields.value.string_value
The value is taken from the USERPRIVPROTOCOL field in the raw log.
USERSECURITYLEVEL
additional.fields.value.string_value
The value is taken from the USERSECURITYLEVEL field in the raw log.
USERSECURITYNAME
principal.user.user_display_name
The value is taken from the USERSECURITYNAME field in the raw log.
application
principal.application
The value is taken from the application field extracted by the grok parser.
description
security_result.description
The value is taken from the description field extracted by the grok parser.
metadata.description
The value is set to "Backup NTP Server Failed" if the CT field in the raw log is "Backup NTP Server Failed".
metadata.event_timestamp.seconds
The value is taken from the timestamp field extracted by the grok parser and converted to epoch seconds.
metadata.event_type
The value is set based on the following logic:
- NETWORK_DHCP if network_dhcp_present is true and either principal_present or target_present is true.
- NETWORK_CONNECTION if target_present and principal_present are both true.
- USER_RESOURCE_ACCESS if user_present is true.
- STATUS_UPDATE if principal_present is true.
- GENERIC_EVENT otherwise.
metadata.product_log_id
The value is taken from the LTMTXEGRESSID field in the raw log.
metadata.product_name
The value is set to "ADVA_FSP".
metadata.vendor_name
The value is set to "ADVA_FSP".
network.application_protocol
The value is set to "DHCP" if network_dhcp_present is true and either principal_present or target_present is true.
principal.hostname
The value is taken from the principal_hostname field extracted by the grok parser, with underscores removed.
principal.ip
The value is taken from the IPADDR field in the raw log and parsed as an IP address.
timestamp.seconds
The value is taken from the timestamp field extracted by the grok parser and converted to epoch seconds.
Need more help?
Get answers from Community members and Google SecOps professionals.
