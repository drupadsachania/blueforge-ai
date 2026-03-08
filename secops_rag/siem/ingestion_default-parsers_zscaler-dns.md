# Collect Zscaler DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-dns/  
**Scraped:** 2026-03-05T09:18:15.241365Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler DNS logs
Supported in:
Google secops
SIEM
This document describes how you can export Zscaler DNS logs by setting up a Google Security Operations feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Zscaler DNS and the Google SecOps Webhook feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler DNS
: The platform from which you collect logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Zscaler DNS and writes logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_DNS
ingestion label.
Before you begin
Ensure you have the following prerequisites:
Access to Zscaler Internet Access console. For more information, see
Secure Internet and SaaS Access ZIA Help
.
Zscaler DNS 2024 or later
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
Set up Zscaler DNS
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
NSS for DNS
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
DNS Logs
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
"zscalernss-dns"
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
"location"
:
"%s{elocation}"
,
"reqaction"
:
"%s{reqaction}"
,
"resaction"
:
"%s{resaction}"
,
"reqrulelabel"
:
"%s{reqrulelabel}"
,
"resrulelabel"
:
"%s{resrulelabel}"
,
"dns_reqtype"
:
"%s{reqtype}"
,
"dns_req"
:
"%s{req}"
,
"dns_resp"
:
"%s{res}"
,
"srv_dport"
:
"%d{sport}"
,
"durationms"
:
"%d{durationms}"
,
"clt_sip"
:
"%s{cip}"
,
"srv_dip"
:
"%s{sip}"
,
"category"
:
"%s{domcat}"
,
"respipcategory"
:
"%s{respipcat}"
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
Supported Zscaler DNS log formats
The Zscaler DNS parser supports logs in JSON format.
Supported Zscaler DNS Sample Logs
JSON
{
  "sourcetype": "zscalernss-dns",
  "event": {
    "srv_dport": "53",
    "durationms": "1306",
    "clt_sip": "1.1.1.1",
    "respipcategory": "Other",
    "datetime": "Sun Sep 18 22:41:05 2020",
    "reqaction": "Allow",
    "resaction": "Allow",
    "resrulelabel": "None",
    "category": "Finance",
    "devicehostname": "dummy_hostname",
    "user": "test.123@test.com",
    "location": "dummy",
    "deviceowner": "212582",
    "department": "Output%20Solutions",
    "reqrulelabel": "Default Firewall DNS Rule",
    "dns_reqtype": "SRV",
    "dns_req": "dummy.domains.com",
    "dns_resp": "NXDOMAIN",
    "srv_dip": "1.1.1.1"
  }
}
Field mapping reference
Field mapping reference: ZSCALER_DNS
The following table lists the log fields of the
ZSCALER_DNS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.event_type
The
metadata.event_type
UDM field is set to
NETWORK_DNS
.
metadata.product_name
The
metadata.product_name
UDM field is set to
DNS
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
metadata.description
If the
category
log field value is
not
empty and the
durationms
log field value is
not
empty, then the
NSSDNSLog | Duration: durationms ms | Category: category
log field is mapped to the
metadata.description
UDM field.
Else, if the
category
log field value is
not
empty, then the
DNS request to \category\
log field is mapped to the
metadata.description
UDM field.
recordid
metadata.product_log_id
datetime
metadata.event_timestamp
epochtime
metadata.event_timestamp
network.application_protocol
The
network.application_protocol
UDM field is set to
DNS
.
network.dns.response_code
If the
dns_resp
log field value is equal to
NOERROR
, then the
network.dns.response_code
UDM field is set to
0
.
Else, if the
dns_resp
log field value is equal to
FORMERR
, then the
network.dns.response_code
UDM field is set to
1
.
Else, if the
dns_resp
log field value is equal to
SERVFAIL
, then the
network.dns.response_code
UDM field is set to
2
.
Else, if the
dns_resp
log field value is equal to
NXDOMAIN
, then the
network.dns.response_code
UDM field is set to
3
.
Else, if the
dns_resp
log field value is equal to
NOTIMP
, then the
network.dns.response_code
UDM field is set to
4
.
Else, if the
dns_resp
log field value is equal to
REFUSED
, then the
network.dns.response_code
UDM field is set to
5
.
Else, if the
dns_resp
log field value is equal to
YXDOMAIN
, then the
network.dns.response_code
UDM field is set to
6
.
Else, if the
dns_resp
log field value is equal to
YXRRSET
, then the
network.dns.response_code
UDM field is set to
7
.
Else, if the
dns_resp
log field value is equal to
NXRRSET
, then the
network.dns.response_code
UDM field is set to
8
.
Else, if the
dns_resp
log field value is equal to
NOTAUTH
, then the
network.dns.response_code
UDM field is set to
9
.
Else, if the
dns_resp
log field value is equal to
NOTZONE
, then the
network.dns.response_code
UDM field is set to
10
.
dns_resp
network.dns.answers.data
network.dns.answers.type
If the
restype
log field value matches the regular expression pattern
ipv4
, then the
network.dns.answers.type
UDM field is set to
1
.
Else, if the
restype
log field value matches the regular expression pattern
ipv6
, then the
network.dns.answers.type
UDM field is set to
28
.
dns_req
network.dns.questions.name
network.dns.questions.type
If the
record_type
log field value is equal to
A
, then the
network.dns.questions.type
UDM field is set to
1
.
Else, if the
record_type
log field value is equal to
NS
, then the
network.dns.questions.type
UDM field is set to
2
.
Else, if the
record_type
log field value is equal to
MD
, then the
network.dns.questions.type
UDM field is set to
3
.
Else, if the
record_type
log field value is equal to
MF
, then the
network.dns.questions.type
UDM field is set to
4
.
Else, if the
record_type
log field value is equal to
CNAME
, then the
network.dns.questions.type
UDM field is set to
5
.
Else, if the
record_type
log field value is equal to
SOA
, then the
network.dns.questions.type
UDM field is set to
6
.
Else, if the
record_type
log field value is equal to
MB
, then the
network.dns.questions.type
UDM field is set to
7
.
Else, if the
record_type
log field value is equal to
MG
, then the
network.dns.questions.type
UDM field is set to
8
.
Else, if the
record_type
log field value is equal to
MR
, then the
network.dns.questions.type
UDM field is set to
9
.
Else, if the
record_type
log field value is equal to
NULL
, then the
network.dns.questions.type
UDM field is set to
10
.
Else, if the
record_type
log field value is equal to
WKS
, then the
network.dns.questions.type
UDM field is set to
11
.
Else, if the
record_type
log field value is equal to
PTR
, then the
network.dns.questions.type
UDM field is set to
12
.
Else, if the
record_type
log field value is equal to
HINFO
, then the
network.dns.questions.type
UDM field is set to
13
.
Else, if the
record_type
log field value is equal to
MINFO
, then the
network.dns.questions.type
UDM field is set to
14
.
Else, if the
record_type
log field value is equal to
MX
, then the
network.dns.questions.type
UDM field is set to
15
.
Else, if the
record_type
log field value is equal to
TXT
, then the
network.dns.questions.type
UDM field is set to
16
.
Else, if the
record_type
log field value is equal to
RP
, then the
network.dns.questions.type
UDM field is set to
17
.
Else, if the
record_type
log field value is equal to
AFSDB
, then the
network.dns.questions.type
UDM field is set to
18
.
Else, if the
record_type
log field value is equal to
X25
, then the
network.dns.questions.type
UDM field is set to
19
.
Else, if the
record_type
log field value is equal to
ISDN
, then the
network.dns.questions.type
UDM field is set to
20
.
Else, if the
record_type
log field value is equal to
RT
, then the
network.dns.questions.type
UDM field is set to
21
.
Else, if the
record_type
log field value is equal to
NSAP
, then the
network.dns.questions.type
UDM field is set to
22
.
Else, if the
record_type
log field value is equal to
NSAP-PTR
, then the
network.dns.questions.type
UDM field is set to
23
.
Else, if the
record_type
log field value is equal to
SIG
, then the
network.dns.questions.type
UDM field is set to
24
.
Else, if the
record_type
log field value is equal to
KEY
, then the
network.dns.questions.type
UDM field is set to
25
.
Else, if the
record_type
log field value is equal to
PX
, then the
network.dns.questions.type
UDM field is set to
26
.
Else, if the
record_type
log field value is equal to
GPOS
, then the
network.dns.questions.type
UDM field is set to
27
.
Else, if the
record_type
log field value is equal to
AAAA
, then the
network.dns.questions.type
UDM field is set to
28
.
Else, if the
record_type
log field value is equal to
LOC
, then the
network.dns.questions.type
UDM field is set to
29
.
Else, if the
record_type
log field value is equal to
NXT
, then the
network.dns.questions.type
UDM field is set to
30
.
Else, if the
record_type
log field value is equal to
EID
, then the
network.dns.questions.type
UDM field is set to
31
.
Else, if the
record_type
log field value is equal to
NIMLOC
, then the
network.dns.questions.type
UDM field is set to
32
.
Else, if the
record_type
log field value is equal to
SRV
, then the
network.dns.questions.type
UDM field is set to
33
.
Else, if the
record_type
log field value is equal to
ATMA
, then the
network.dns.questions.type
UDM field is set to
34
.
Else, if the
record_type
log field value is equal to
NAPTR
, then the
network.dns.questions.type
UDM field is set to
35
.
Else, if the
record_type
log field value is equal to
KX
, then the
network.dns.questions.type
UDM field is set to
36
.
Else, if the
record_type
log field value is equal to
CERT
, then the
network.dns.questions.type
UDM field is set to
37
.
Else, if the
record_type
log field value is equal to
A6
, then the
network.dns.questions.type
UDM field is set to
38
.
Else, if the
record_type
log field value is equal to
DNAME
, then the
network.dns.questions.type
UDM field is set to
39
.
Else, if the
record_type
log field value is equal to
SINK
, then the
network.dns.questions.type
UDM field is set to
40
.
Else, if the
record_type
log field value is equal to
OPT
, then the
network.dns.questions.type
UDM field is set to
41
.
Else, if the
record_type
log field value is equal to
APL
, then the
network.dns.questions.type
UDM field is set to
42
.
Else, if the
record_type
log field value is equal to
DS
, then the
network.dns.questions.type
UDM field is set to
43
.
Else, if the
record_type
log field value is equal to
SSHFP
, then the
network.dns.questions.type
UDM field is set to
44
.
Else, if the
record_type
log field value is equal to
IPSECKEY
, then the
network.dns.questions.type
UDM field is set to
45
.
Else, if the
record_type
log field value is equal to
RRSIG
, then the
network.dns.questions.type
UDM field is set to
46
.
Else, if the
record_type
log field value is equal to
NSEC
, then the
network.dns.questions.type
UDM field is set to
47
.
Else, if the
record_type
log field value is equal to
DNSKEY
, then the
network.dns.questions.type
UDM field is set to
48
.
Else, if the
record_type
log field value is equal to
DHCID
, then the
network.dns.questions.type
UDM field is set to
49
.
Else, if the
record_type
log field value is equal to
NSEC3
, then the
network.dns.questions.type
UDM field is set to
50
.
Else, if the
record_type
log field value is equal to
NSEC3PARAM
, then the
network.dns.questions.type
UDM field is set to
51
.
Else, if the
record_type
log field value is equal to
TLSA
, then the
network.dns.questions.type
UDM field is set to
52
.
Else, if the
record_type
log field value is equal to
SMIMEA
, then the
network.dns.questions.type
UDM field is set to
53
.
Else, if the
record_type
log field value is equal to
UNASSIGNED
, then the
network.dns.questions.type
UDM field is set to
54
.
Else, if the
record_type
log field value is equal to
HIP
, then the
network.dns.questions.type
UDM field is set to
55
.
Else, if the
record_type
log field value is equal to
NINFO
, then the
network.dns.questions.type
UDM field is set to
56
.
Else, if the
record_type
log field value is equal to
RKEY
, then the
network.dns.questions.type
UDM field is set to
57
.
Else, if the
record_type
log field value is equal to
TALINK
, then the
network.dns.questions.type
UDM field is set to
58
.
Else, if the
record_type
log field value is equal to
CDS
, then the
network.dns.questions.type
UDM field is set to
59
.
Else, if the
record_type
log field value is equal to
CDNSKEY
, then the
network.dns.questions.type
UDM field is set to
60
.
Else, if the
record_type
log field value is equal to
OPENPGPKEY
, then the
network.dns.questions.type
UDM field is set to
61
.
Else, if the
record_type
log field value is equal to
CSYNC
, then the
network.dns.questions.type
UDM field is set to
62
.
Else, if the
record_type
log field value is equal to
ZONEMD
, then the
network.dns.questions.type
UDM field is set to
63
.
Else, if the
record_type
log field value is equal to
SVCB
, then the
network.dns.questions.type
UDM field is set to
64
.
Else, if the
record_type
log field value is equal to
HTTPS
, then the
network.dns.questions.type
UDM field is set to
65
.
Else, if the
record_type
log field value is equal to
SPF
, then the
network.dns.questions.type
UDM field is set to
99
.
Else, if the
record_type
log field value is equal to
UINFO
, then the
network.dns.questions.type
UDM field is set to
100
.
Else, if the
record_type
log field value is equal to
UID
, then the
network.dns.questions.type
UDM field is set to
101
.
Else, if the
record_type
log field value is equal to
GID
, then the
network.dns.questions.type
UDM field is set to
102
.
Else, if the
record_type
log field value is equal to
UNSPEC
, then the
network.dns.questions.type
UDM field is set to
103
.
Else, if the
record_type
log field value is equal to
NID
, then the
network.dns.questions.type
UDM field is set to
104
.
Else, if the
record_type
log field value is equal to
L32
, then the
network.dns.questions.type
UDM field is set to
105
.
Else, if the
record_type
log field value is equal to
L64
, then the
network.dns.questions.type
UDM field is set to
106
.
Else, if the
record_type
log field value is equal to
LP
, then the
network.dns.questions.type
UDM field is set to
107
.
Else, if the
record_type
log field value is equal to
EUI48
, then the
network.dns.questions.type
UDM field is set to
108
.
Else, if the
record_type
log field value is equal to
EUI64
, then the
network.dns.questions.type
UDM field is set to
109
.
Else, if the
record_type
log field value is equal to
TKEY
, then the
network.dns.questions.type
UDM field is set to
249
.
Else, if the
record_type
log field value is equal to
TSIG
, then the
network.dns.questions.type
UDM field is set to
250
.
Else, if the
record_type
log field value is equal to
IXFR
, then the
network.dns.questions.type
UDM field is set to
251
.
Else, if the
record_type
log field value is equal to
AXFR
, then the
network.dns.questions.type
UDM field is set to
252
.
Else, if the
record_type
log field value is equal to
MAILB
, then the
network.dns.questions.type
UDM field is set to
253
.
Else, if the
record_type
log field value is equal to
MAILA
, then the
network.dns.questions.type
UDM field is set to
254
.
Else, if the
record_type
log field value is equal to
ALL
, then the
network.dns.questions.type
UDM field is set to
255
.
Else, if the
record_type
log field value is equal to
URI
, then the
network.dns.questions.type
UDM field is set to
256
.
Else, if the
record_type
log field value is equal to
CAA
, then the
network.dns.questions.type
UDM field is set to
257
.
Else, if the
record_type
log field value is equal to
AVC
, then the
network.dns.questions.type
UDM field is set to
258
.
Else, if the
record_type
log field value is equal to
DOA
, then the
network.dns.questions.type
UDM field is set to
259
.
Else, if the
record_type
log field value is equal to
AMTRELAY
, then the
network.dns.questions.type
UDM field is set to
260
.
Else, if the
record_type
log field value is equal to
TA
, then the
network.dns.questions.type
UDM field is set to
32768
.
Else, if the
record_type
log field value is equal to
DLV
, then the
network.dns.questions.type
UDM field is set to
32769
.
dns_reqtype
additional.fields[dns_reqtype]
http_code
network.http.response_code
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
.
durationms
network.session_duration.seconds
devicemodel
principal.asset.hardware.model
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
devicehostname
principal.asset.hostname
edevicehostname
principal.asset.hostname
principal.asset.platform_software.platform
If the
deviceostype
log field value matches the regular expression pattern
(?i)win
, then the
principal.asset.platform_software.platform
UDM field is set to
WINDOWS
.
Else, if the
deviceostype
log field value matches the regular expression pattern
(?i)lin
, then the
principal.asset.platform_software.platform
UDM field is set to
LINUX
.
deviceosversion
principal.asset.platform_software.platform_version
company
principal.user.company_name
department
principal.user.department
user
principal.user.email_addresses
If the
user
log field value matches the regular expression pattern
(^.@.$)
or the
login
log field value matches the regular expression pattern
(^.@.$)
, then if the
user
log field value is not empty, then the
user
log field is mapped to the
principal.user.email_addresses
UDM field.
login
principal.user.email_addresses
If the
user
log field value matches the regular expression pattern
(^.@.$)
or the
login
log field value matches the regular expression pattern
(^.@.$)
, then if the
user
log field value is not empty, then else, the
login
log field is mapped to the
principal.user.email_addresses
UDM field.
deviceowner
principal.asset.attribute.labels[deviceowner]
clt_sip
principal.ip
location
principal.location.name
reqrulelabel
security_result.rule_name
rule
security_result.rule_name
security_result.action
If the
reqaction
log field value matches the regular expression pattern
(?i)BLOCK
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
reqaction
log field value matches the regular expression pattern
(?i)ALLOW
, then the
security_result.action
UDM field is set to
ALLOW
.
reqaction
security_result.action_details
security_result.category
If the
category
log field value is
not
empty, then the
security_result.category
UDM field is set to
NETWORK_CATEGORIZED_CONTENT
.
category
security_result.category_details
resrulelabel
security_result.rule_name
security_result.action
If the
resaction
log field value matches the regular expression pattern
(?i)BLOCK
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
resaction
log field value matches the regular expression pattern
(?i)ALLOW
, then the
security_result.action
UDM field is set to
ALLOW
.
resaction
security_result.action_details
security_result.category
If the
respipcategory
log field value is
not
empty, then the
security_result.category
UDM field is set to
NETWORK_CATEGORIZED_CONTENT
.
respipcategory
security_result.category_details
ecs_slot
security_result.rule_labels [ecs_slot]
If the
dnsgw_slot
log field value is empty, then the
ecs_slot
log field is mapped to the
security_result.rule_name
UDM field.
dnsgw_slot
security_result.rule_name
If the
dnsgw_slot
log field value is
not
empty, then the
dnsgw_slot
log field is mapped to the
security_result.rule_name
UDM field.
ecs_slot
security_result.rule_name
If the
dnsgw_slot
log field value is
not
empty, then the
ecs_slot
log field is mapped to the
security_result.rule_labels
UDM field.
dnsapp
target.application
srv_dip
target.ip
srv_dport
target.port
datacentercity
target.location.city
datacentercountry
target.location.country_or_region
datacenter
target.location.name
cloudname
security_result.detection_fields[cloudname]
dnsappcat
security_result.detection_fields[dnsappcat]
ecs_prefix
security_result.detection_fields[ecs_prefix]
error
security_result.detection_fields[error]
istcp
security_result.detection_fields[istcp]
ocip
principal.ip
odevicehostname
principal.asset.hostname
odeviceowner
principal.asset.attribute.labels[odeviceowner]
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
security_result.category
If the
odomcat
log field value is
not
empty, then the
security_result.category
UDM field is set to
NETWORK_CATEGORIZED_CONTENT
.
odomcat
security_result.category_details
dnsgw_flags
security_result.detection_fields[dnsgw_flags]
dnsgw_srv_proto
security_result.detection_fields[dnsgw_srv_proto]
erulelabel
security_result.rule_labels [erulelabel]
ethreatname
security_result.threat_name
durationms
additional.fields[durationms]
If the
durationms
log field value is equal to
1
, then the
durationms
log field is mapped to the
additional.fields.durationms
UDM field.
sourcetype
additional.fields[sourcetype]
deviceappversion
principal.asset.software.version
devicetype
additional.fields[devicetype]
eedone
additional.fields[eedone]
tz
additional.fields[tz]
ss
additional.fields[ss]
mm
additional.fields[mm]
hh
additional.fields[hh]
dd
additional.fields[dd]
mth
additional.fields[mth]
yyyy
additional.fields[yyyy]
mon
additional.fields[mon]
day
additional.fields[day]
pcapid
about.file.full_path
Need more help?
Get answers from Community members and Google SecOps professionals.
