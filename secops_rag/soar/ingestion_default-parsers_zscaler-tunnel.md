# Collect Zscaler Tunnel logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-tunnel/  
**Scraped:** 2026-03-05T09:49:07.819303Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler Tunnel logs
Supported in:
Google secops
SIEM
This document explains how to export Zscaler Tunnel logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler Tunnel and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler Tunnel
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler Tunnel and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_TUNNEL
label.
Before you begin
Ensure you have the following prerequisites:
Access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Zscaler Tunnel version 1.0 or version 2.0
All systems in the deployment architecture are configured with the UTC time zone.
The API key which is needed to complete feed setup in Google Security Operations. For more information, see
Setting up API keys
.
Set up feeds
To configure this log type, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
Zscaler
feed pack.
Locate the required log type and click
Add New Feed
.
Enter values for the following input parameters:
Source Type
: Webhook (Recommended)
Split delimiter
: the character used to separate logs lines. Leave blank if no delimiter is used.
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
Create Feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
Set up Zscaler Tunnel
In Zscaler Internet Access console, go to
Administration
>
Nanolog Streaming Service
>
Cloud NSS Feeds
.
Click
Add Cloud NSS Feed
.
Enter a name for the feed in the
Feed Name
field.
Select
NSS for Tunnel
in
NSS Type
.
Select the status from the
Status
list to activate or deactivate the NSS feed.
Keep the value in the
SIEM Rate
drop-down as
Unlimited
. To suppress the output stream due to licensing or other constraints, change the value.
Select
Other
in the
SIEM Type
list.
Select
Disabled
in the
OAuth 2.0 Authentication
list.
Enter a size limit for an individual HTTP request payload to the SIEM's best practice in
Max Batch Size
(for example,
512 KB
).
Enter the HTTPS URL of the Chronicle API endpoint in the API URL in the following format:
https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
CHRONICLE_REGION
: region where your Google SecOps instance is hosted (for example,
US
).
GOOGLE_PROJECT_NUMBER
: BYOP project number (obtain this from C4).
LOCATION
: Google SecOps region (for example,
US
).
CUSTOMER_ID
: Google SecOps customer ID (obtain this from C4).
FEED_ID
: Feed ID shown on the Feed UI on the new webhook created.
Sample API URL:
https://us-chronicle.googleapis.com/v1alpha/projects/12345678910/locations/US/instances/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/feeds/yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy:importPushLogs
Click
Add HTTP Header
, and then add HTTP headers in the following format:
Header 1
:
Key1:
X-goog-api-key
and
Value1:
API Key generated on Google Cloud BYOP's API Credentials.
Header 2
:
Key2:
X-Webhook-Access-Key
and
Value2:
API secret key generated on webhook's "SECRET KEY".
Select
Tunnel
in the
Log Types
list.
Select
JSON
in the
Feed Output Type
list.
Disable
JSON Array Notation
.
Set
Feed Escape Character
to
, \ "
.
To add a new field to the
Feed Output Format,
select
Custom
in the
Feed Output Type
list.
Copy-paste the
Feed Output Format
and add new fields. Ensure the key names match the actual field names.
The following are the default
Feed Output Formats
:
For IKE Phase 1:
\
{
"sourcetype"
:
"zscalernss-tunnel"
,
"event"
:
\
{
"datetime"
:
"%s{datetime}"
,
"Recordtype"
:
"%s{tunnelactionname}"
,
"tunneltype"
:
"IPSEC IKEV %d{ikeversion}"
,
"user"
:
"%s{vpncredentialname}"
,
"location"
:
"%s{elocationname}"
,
"sourceip"
:
"%s{sourceip}"
,
"destinationip"
:
"%s{destvip}"
,
"sourceport"
:
"%d{srcport}"
,
"destinationport"
:
"%d{dstport}"
,
"lifetime"
:
"%d{lifetime}"
,
"ikeversion"
:
"%d{ikeversion}"
,
"spi_in"
:
"%lu{spi_in}"
,
"spi_out"
:
"%lu{spi_out}"
,
"algo"
:
"%s{algo}"
,
"authentication"
:
"%s{authentication}"
,
"authtype"
:
"%s{authtype}"
,
"recordid"
:
"%d{recordid}"
\
}
\
}
For IKE Phase 2:
\
{
"sourcetype"
:
"zscalernss-tunnel"
,
"event"
:
\
{
"datetime"
:
"%s{datetime}"
,
"Recordtype"
:
"%s{tunnelactionname}"
,
"tunneltype"
:
"IPSEC IKEV %d{ikeversion}"
,
"user"
:
"%s{vpncredentialname}"
,
"location"
:
"%s{elocationname}"
,
"sourceip"
:
"%s{sourceip}"
,
"destinationip"
:
"%s{destvip}"
,
"sourceport"
:
"%d{srcport}"
,
"sourceportstart"
:
"%d{srcportstart}"
,
"destinationportstart"
:
"%d{destportstart}"
,
"srcipstart"
:
"%s{srcipstart}"
,
"srcipend"
:
"%s{srcipend}"
,
"destinationipstart"
:
"%s{destipstart}"
,
"destinationipend"
:
"%s{destipend}"
,
"lifetime"
:
"%d{lifetime}"
,
"ikeversion"
:
"%d{ikeversion}"
,
"lifebytes"
:
"%d{lifebytes}"
,
"spi"
:
"%d{spi}"
,
"algo"
:
"%s{algo}"
,
"authentication"
:
"%s{authentication}"
,
"authtype"
:
"%s{authtype}"
,
"protocol"
:
"%s{protocol}"
,
"tunnelprotocol"
:
"%s{tunnelprotocol}"
,
"policydirection"
:
"%s{policydirection}"
,
"recordid"
:
"%d{recordid}"
\
}
\
}
For Tunnel Event:
\
{
"sourcetype"
:
"zscalernss-tunnel"
,
"event"
:
\
{
"datetime"
:
"%s{datetime}"
,
"Recordtype"
:
"%s{tunnelactionname}"
,
"tunneltype"
:
"%s{tunneltype}"
,
"user"
:
"%s{vpncredentialname}"
,
"location"
:
"%s{elocationname}"
,
"sourceip"
:
"%s{sourceip}"
,
"destinationip"
:
"%s{destvip}"
,
"sourceport"
:
"%d{srcport}"
,
"event"
:
"%s{event}"
,
"eventreason"
:
"%s{eventreason}"
,
"recordid"
:
"%d{recordid}"
\
}
\
}
For Sample:
\
{
"sourcetype"
:
"zscalernss-tunnel"
,
"event"
:
\
{
"datetime"
:
"%s{datetime}"
,
"Recordtype"
:
"%s{tunnelactionname}"
,
"tunneltype"
:
"%s{tunneltype}"
,
"user"
:
"%s{vpncredentialname}"
,
"location"
:
"%s{elocationname}"
,
"sourceip"
:
"%s{sourceip}"
,
"destinationip"
:
"%s{destvip}"
,
"sourceport"
:
"%d{srcport}"
,
"txbytes"
:
"%lu{txbytes}"
,
"rxbytes"
:
"%lu{rxbytes}"
,
"dpdrec"
:
"%d{dpdrec}"
,
"recordid"
:
"%d{recordid}"
\
}
\
}
Select the time zone for the
Time
field in the output file in the
Timezone
list. By default, the time zone is set to your organization's
time zone.
Review the configured settings.
Click
Save
to test connectivity. If the connection is successful, a green tick accompanied by the message
Test Connectivity Successful: OK (200)
appears.
For more information about Google SecOps feeds, see
Google SecOps feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Supported Zscaler Tunnel log formats
The Zscaler Tunnel parser supports logs in JSON format.
Supported Zscaler Tunnel sample logs
JSON
{
  "sourcetype": "zscalernss-tunnel",
  "event": {
    "datetime": "Sun Jan 21 06:17:00 2024",
    "Recordtype": "Tunnel Samples",
    "tunneltype": "IPSec IKEv2",
    "user": "dummy-user@dummydomain.net",
    "location": "PLWSE06",
    "sourceip": "198.51.100.0",
    "destinationip": "198.51.100.1",
    "sourceport": "0",
    "txbytes": "12560",
    "rxbytes": "0",
    "dpdrec": "0",
    "recordid": "7326416289073594372"
  }
}
UDM Mapping Table
Field mapping reference: ZSCALER_TUNNEL
The following table lists the log fields of the
ZSCALER_TUNNEL
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
algo
additional.fields[algo]
authtype
additional.fields[authtype]
authentication
additional.fields[authentication]
dd
additional.fields[dd]
day
additional.fields[day]
destinationportstart
additional.fields[destinationportstart]
dpdrec
additional.fields[dpdrec]
eventreason
additional.fields[eventreason]
hh
additional.fields[hh]
ikeversion
additional.fields[ikeversion]
lifebytes
additional.fields[lifebytes]
mm
additional.fields[mm]
mon
additional.fields[mon]
mth
additional.fields[mth]
olocationname
principal.location.name
ovpncredentialname
principal.user.userid
and
principal.user.email_addresses
if regular expression match
^.+@.+$
ss
additional.fields[ss]
sourcetype
additional.fields[sourcetype]
spi_in
additional.fields[spi_in]
spi_out
additional.fields[spi_out]
sourceportstart
additional.fields[sourceportstart]
tz
additional.fields[tz]
tunnelprotocol
additional.fields[tunnelprotocol]
tunneltype
additional.fields[tunneltype]
vendorname
additional.fields[vendorname]
yyyy
additional.fields[yyyy]
spi
additional.fields[spi]
event
metadata.description
datetime
metadata.event_timestamp
metadata.event_type
If (the
srcipstart
log field value is
not
empty or the
srcipend
log field value is
not
empty or the
sourceip
log field value is
not
empty) and (the
destinationipstart
log field value is
not
empty or the
destinationip
log field value is
not
empty or the
destinationipend
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
srcipstart
log field value is
not
empty or the
srcipend
log field value is
not
empty or the
sourceip
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
Recordtype
metadata.product_event_type
recordid
metadata.product_log_id
metadata.product_name
The
metadata.product_name
UDM field is set to
ZSCALER_TUNNEL
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
ZSCALER
.
network.direction
If the
policydirection
log field value matches the regular expression pattern
(?i)Inbound
, then the
network.direction
UDM field is set to
INBOUND
.
Else, if the
policydirection
log field value matches the regular expression pattern
(?i)Outbound
, then the
network.direction
UDM field is set to
OUTBOUND
.
protocol
network.ip_protocol
If the
protocol
log field value contain one of the following values, then the
protocol
log field is mapped to the
network.ip_protocol
UDM field.
TCP
EIGRP
ESP
ETHERIP
GRE
ICMP
IGMP
IP6IN4
PIM
UDP
VRRP
rxbytes
network.received_bytes
rxpackets
network.received_packets
txbytes
network.sent_bytes
txpackets
network.sent_packets
lifetime
network.session_duration.seconds
srcipstart
principal.ip
sourceip
principal.ip
srcipend
principal.ip
location
principal.location.name
sourceport
principal.port
user
principal.user.userid
and
principal.user.email_addresses
if regular expression match
^.+@.+$
destinationipstart
target.ip
destinationip
target.ip
destinationipend'
target.ip
destinationport
target.port
Need more help?
Get answers from Community members and Google SecOps professionals.
