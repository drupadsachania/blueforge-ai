# Collect Zscaler Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-firewall/  
**Scraped:** 2026-03-05T09:18:16.310043Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler Firewall logs
Supported in:
Google secops
SIEM
This document describes how you can export Zscaler Firewall logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler Firewall and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler Firewall
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler Firewall and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_FIREWALL
ingestion label.
Before you begin
Ensure you have the following prerequisites:
Access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Zscaler Firewall 2024 or later
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
Set up Zscaler Firewall
In the Zscaler Internet Access console, click
Administration
>
Nanolog Streaming Service
>
Cloud NSS Feeds
and then click
Add Cloud NSS Feed
.
The
Add Cloud NSS Feed
window appears. In the
Add Cloud NSS Feed
window, enter the details.
Enter a name for the feed in the
Feed Name
field.
Select
NSS for Firewall
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
. For example, 512 KB.
Enter the HTTPS URL of the Chronicle API endpoint in the API URL in the following format:
https://<CHRONICLE_REGION>-chronicle.googleapis.com/v1alpha/projects/<GOOGLE_PROJECT_NUMBER>/locations/<LOCATION>/instances/<CUSTOMER_ID>/feeds/<FEED_ID>:importPushLogs
CHRONICLE_REGION
: Region where your Chronicle instance is hosted. For example, US.
GOOGLE_PROJECT_NUMBER
: BYOP project number. Obtain this from C4.
LOCATION
: Chronicle region. For example, US.
CUSTOMER_ID
: Chronicle customer ID. Obtain from C4.
FEED_ID
: Feed ID shown on Feed UI on the new webhook created
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
Firewall Logs
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
Following is the default
Feed Output Format
:
\
{
"sourcetype"
:
"zscalernss-fw"
,
"event"
:
\
{
"datetime"
:
"%s{time}"
,
"user"
:
"%s{elogin}"
,
"department"
:
"%s{edepartment}"
,
"locationname"
:
"%s{elocation}"
,
"cdport"
:
"%d{cdport}"
,
"csport"
:
"%d{csport}"
,
"sdport"
:
"%d{sdport}"
,
"ssport"
:
"%d{ssport}"
,
"csip"
:
"%s{csip}"
,
"cdip"
:
"%s{cdip}"
,
"ssip"
:
"%s{ssip}"
,
"sdip"
:
"%s{sdip}"
,
"tsip"
:
"%s{tsip}"
,
"tunsport"
:
"%d{tsport}"
,
"tuntype"
:
"%s{ttype}"
,
"action"
:
"%s{action}"
,
"dnat"
:
"%s{dnat}"
,
"stateful"
:
"%s{stateful}"
,
"aggregate"
:
"%s{aggregate}"
,
"nwsvc"
:
"%s{nwsvc}"
,
"nwapp"
:
"%s{nwapp}"
,
"proto"
:
"%s{ipproto}"
,
"ipcat"
:
"%s{ipcat}"
,
"destcountry"
:
"%s{destcountry}"
,
"avgduration"
:
"%d{avgduration}"
,
"rulelabel"
:
"%s{erulelabel}"
,
"inbytes"
:
"%ld{inbytes}"
,
"outbytes"
:
"%ld{outbytes}"
,
"duration"
:
"%d{duration}"
,
"durationms"
:
"%d{durationms}"
,
"numsessions"
:
"%d{numsessions}"
,
"ipsrulelabel"
:
"%s{ipsrulelabel}"
,
"threatcat"
:
"%s{threatcat}"
,
"threatname"
:
"%s{ethreatname}"
,
"deviceowner"
:
"%s{deviceowner}"
,
"devicehostname"
:
"%s{devicehostname}"
\
}
\
}
Select the timezone for the
Time
field in the output file in the
Timezone
list. By default, the timezone is set to your organization's
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
Supported Zscaler Firewall log formats
The Zscaler Firewall parser supports logs in JSON format.
Supported Zscaler Firewall Sample Logs
JSON:
{
  "sourcetype": "zscalernss-fw",
  "event": {
    "datetime": "Tue Apr 11 00:44:01 2023",
    "user": "abc@test.com",
    "department": "Optum%20Tech%20UHC%20Technology",
    "locationname": "Road%20Warrior",
    "cdport": "443",
    "csport": "50407",
    "sdport": "443",
    "ssport": "36223",
    "csip": "198.51.100.8",
    "cdip": "198.51.100.7",
    "ssip": "198.51.100.9",
    "sdip": "198.51.100.10",
    "tsip": "198.51.100.11",
    "tunsport": "0",
    "tuntype": "ZscalerClientConnector",
    "action": "Allow",
    "dnat": "No",
    "stateful": "Yes",
    "aggregate": "Yes",
    "nwsvc": "ZSCALER_PROXY_NW_SERVICES",
    "nwapp": "sharepoint_document",
    "proto": "TCP",
    "ipcat": "Miscellaneous or Unknown",
    "destcountry": "Other",
    "avgduration": "239296",
    "rulelabel": "Default%20Firewall%20Filtering%20Rule",
    "inbytes": "286134",
    "outbytes": "515005",
    "duration": "6461",
    "durationms": "6461000",
    "numsessions": "27",
    "ipsrulelabel": "None",
    "threatcat": "None",
    "threatname": "None",
    "deviceowner": "dummydeviceowner",
    "devicehostname": "dummyhostname"
  }
}
Field mapping reference
The following table lists the log fields of the
ZSCALER_FIREWALL
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
fwd_gw_name
intermediary.resource.name
intermediary.resource.resource_type
If the
fwd_gw_name
log field value is
not
empty or the
ofwd_gw_name
log field value is
not
empty, then the
intermediary.resource.resource_type
UDM field is set to
GATEWAY
.
ofwd_gw_name
intermediary.resource.name
ordr_rulename
security_result.rule_name
rdr_rulename
security_result.rule_name
rulelabel
security_result.rule_name
orulelabel
security_result.rule_name
erulelabel
security_result.rule_name
bypass_etime
metadata.collected_timestamp
datetime
metadata.event_timestamp
epochtime
metadata.event_timestamp
metadata.event_type
If the
sdport
log field value is equal to
80
or the
sdport
log field value is equal to
443
and the
csip
log field value is
not
empty or the
ocsip
log field value is
not
empty or the
devicename
log field value is
not
empty or the
odevicename
log field value is
not
empty and the
sdip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
Else, if the
csip
log field value is
not
empty or the
ocsip
log field value is
not
empty or the
devicename
log field value is
not
empty or the
odevicename
log field value is
not
empty and the
sdip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
csip
log field value is
not
empty or the
ocsip
log field value is
not
empty or the
devicename
log field value is
not
empty or the
odevicename
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
recordid
metadata.product_log_id
metadata.product_name
The
metadata.product_name
UDM field is set to
Firewall
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
proto
network.ip_protocol
If the
proto
log field value contain one of the following values, then the
proto
log field is mapped to the
network.ip_protocol
UDM field.
TCP
UDP
ICMP
GRE
IP6IN4
IGMP
inbytes
network.received_bytes
outbytes
network.sent_bytes
avgduration
network.session_duration.nanos
If the
durationms
log field value is empty and the
avgduration
log field value is
not
empty, then the
avgduration
log field is mapped to the
network.session_duration.nanos
UDM field.
durationms
network.session_duration.nanos
If the
durationms
log field value is
not
empty, then the
durationms
log field is mapped to the
network.session_duration.nanos
UDM field.
duration
network.session_duration.seconds
devicename
principal.asset.asset_id
If the
devicename
log field value is
not
empty, then the
Zscaler:devicename
log field is mapped to the
principal.asset.asset_id
UDM field.
devicemodel
principal.asset.hardware.model
devicehostname
principal.asset.hostname
If the
devicehostname
log field value is
not
empty, then the
devicehostname
log field is mapped to the
principal.asset.hostname
UDM field.
edevicehostname
principal.asset.hostname
If the
edevicehostname
log field value is
not
empty, then the
edevicehostname
log field is mapped to the
principal.asset.hostname
UDM field.
principal.asset.platform_software.platform
If the
deviceostype
log field value matches the regular expression pattern
(?i)iOS
, then the
principal.asset.platform_software.platform
UDM field is set to
IOS
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)Android
, then the
principal.asset.platform_software.platform
UDM field is set to
ANDROID
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)Windows
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)MAC
, then the
principal.asset.platform_software.platform
UDM field is set to
MAC
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)Other
, then the
principal.asset.platform_software.platform
UDM field is set to
UNKNOWN_PLATFORM
.
deviceosversion
principal.asset.platform_software.platform_version
external_deviceid
principal.asset.product_object_id
csip
principal.ip
tsip
principal.nat_ip
srcip_country
principal.location.country_or_region
location
principal.location.name
locationname
principal.location.name
ssip
intermediary.nat_ip
ssport
intermediary.nat_port
csport
principal.port
dept
principal.user.department
department
principal.user.department
login
principal.user.email_addresses
The
login
field is extracted from
login
log field using the Grok pattern, and the
login
log field is mapped to the
principal.user.email_addresses
UDM field.
user
principal.user.email_addresses
The
user
field is extracted from
user
log field using the Grok pattern, and the
user
log field is mapped to the
principal.user.email_addresses
UDM field.
deviceowner
principal.asset.attribute.labels[deviceowner]
security_result.action
If the
action
log field value matches the regular expression pattern
^Allow.*
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
action
log field value matches the regular expression pattern
^Drop.*
or
^Block.*
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
action
log field value is equal to
Reset
, then the
security_result.action
UDM field is set to
BLOCK
.
action
security_result.action_details
threat_severity,threat_score
security_result.severity
If the
threat_severity
log field value is one of the following:
CRITICAL
,
HIGH
,
MEDIUM
,
LOW
,
NONE
then, the
threat_severity
log field is mapped to the
security_result.severity
UDM field.
Else, if the
threat_score
log field value is equal to
0
then, the
security_result.severity
UDM field is set to
NONE
. Else, if
threat_score
log field value >
0
and the
threat_score
log field value <=
45
then, the
security_result.severity
UDM field is set to
LOW
. Else, if
threat_score
log field value >
45
and the
threat_score
log field value <
75
then, the
security_result.severity
UDM field is set to
MEDIUM
. Else, if
threat_score
log field value >=
75
and the
threat_score
log field value <
90
then, the
security_result.severity
UDM field is set to
HIGH
. Else, if
threat_score
log field value >=
90
and the
threat_score
log field value <=
100
then, the
security_result.severity
UDM field is set to
CRITICAL
.
threat_severity,threat_score
security_result.severity_details
If the
threat_score
log field value is
not
empty and the
threat_severity
log field value is
not
empty then,
%{threat_score} - %{threat_severity}
log field is mapped to the
security_result.severity_details
UDM field.
Else, if
threat_severity
log field value is
not
empty then,
threat_severity
log field is mapped to the
security_result.severity_details
UDM field.
Else, if
threat_score
log field value is
not
empty then,
threat_score
log field is mapped to the
security_result.severity_details
UDM field.
security_result.category
If the
ipcat
log field value is
not
empty or the
oipcat
log field value is
not
empty, then the
security_result.category
UDM field is set to
NETWORK_CATEGORIZED_CONTENT
.
ipcat
security_result.category_details
The
ipcat
log field is mapped to the
security_result.category_details
UDM field.
threatcat
security_result.category_details
If the
threatcat
log field value is
not
equal to
None
, then the
threatcat
log field is mapped to the
security_result.category_details
UDM field.
security_result.detection_fields[bypassed_session]
If the
bypassed_session
log field value is equal to
0
, then the
security_result.detection_fields.bypassed_session
UDM field is set to
the traffic did not bypass Zscaler Client Connector
.
Else, if the
bypassed_session
log field value is equal to
1
, then the
security_result.detection_fields.bypassed_session
UDM field is set to
the traffic bypassed Zscaler Client Connector
.
odevicehostname
principal.asset.hostname
If the
odevicehostname
log field value is
not
empty, then the
odevicehostname
log field is mapped to the
principal.asset.hostname
UDM field.
odevicename
principal.asset.asset_id
If the
odevicename
log field value is
not
empty, then the
Zscaler:odevicename
log field is mapped to the
principal.asset.asset_id
UDM field.
odeviceowner
principal.asset.attribute.labels[odeviceowner]
oipcat
security_result.category_details
oipsrulelabel
security_result.rule_name
If the
oipsrulelabel
log field value is
not
equal to
None
, then the
oipsrulelabel
log field is mapped to the
security_result.rule_name
UDM field.
numsessions
security_result.detection_fields[numsessions]
security_result.rule_labels [ips_custom_signature]
If the
ips_custom_signature
log field value is equal to
0
, then the
security_result.rule_labels.ips_custom_signature
UDM field is set to
non-custom IPS rule
.
Else, if the
ips_custom_signature
log field value is equal to
1
, then the
security_result.rule_labels.ips_custom_signature
UDM field is set to
custom IPS rule
.
ipsrulelabel
security_result.rule_name
If the
ipsrulelabel
log field value is
not
equal to
None
, then the
ipsrulelabel
log field is mapped to the
security_result.rule_name
UDM field.
threatname
security_result.threat_name
If the
threatname
log field value is
not
equal to
None
, then the
threatname
log field is mapped to the
security_result.threat_name
UDM field.
ethreatname
security_result.threat_name
If the
ethreatname
log field value is
not
equal to
None
, then the
ethreatname
log field is mapped to the
security_result.threat_name
UDM field.
nwapp
target.application
cdfqdn
target.domain.name
sdip
target.ip
datacentercity
target.location.city
destcountry
target.location.country_or_region
datacentercountry
target.location.country_or_region
datacenter
target.location.name
cdip
intermediary.ip
cdport
intermediary.port
sdport
target.port
odnatlabel
target.security_result.detection_fields[odnatlabel]
dnat
security_result.rule_labels[dnat]
dnatrulelabel
security_result.rule_name
odnatrulelabel
security_result.rule_name
aggregate
additional.fields[aggregate]
day
additional.fields[day]
dd
additional.fields[dd]
deviceappversion
principal.asset.software.version
eedone
additional.fields[eedone]
flow_type
additional.fields[flow_type]
hh
additional.fields[hh]
mm
additional.fields[mm]
mon
additional.fields[mon]
mth
additional.fields[mth]
nwsvc
additional.fields[nwsvc]
ocsip
principal.ip
ozpa_app_seg_name
additional.fields[ozpa_app_seg_name]
ss
additional.fields[ss]
sourcetype
additional.fields[sourcetype]
stateful
additional.fields[stateful]
tz
additional.fields[tz]
tuntype
additional.fields[traffic_forwarding_method]
tunsport
additional.fields[tunsport]
yyyy
additional.fields[yyyy]
zpa_app_seg_name
additional.fields[zpa_app_seg_name]
ztunnelversion
additional.fields[ztunnelversion]
Need more help?
Get answers from Community members and Google SecOps professionals.
