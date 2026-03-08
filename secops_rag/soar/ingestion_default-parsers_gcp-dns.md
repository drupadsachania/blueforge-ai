# Collect Google Cloud DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-dns/  
**Scraped:** 2026-03-05T09:48:00.005150Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud DNS logs
Supported in:
Google secops
SIEM
This document describes how you can collect Cloud DNS logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of Cloud DNS logs map to Google Security Operations Unified Data Model (UDM) fields.
This document also lists the supported Cloud DNS version.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Cloud DNS logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Cloud DNS logs
: The Cloud DNS logs that are
enabled for ingestion to Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Cloud DNS.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_DNS
ingestion label.
Before you begin
Ensure that you have set up
Google Cloud
.
Ensure that the Cloud DNS service is properly deployed and configured. For detailed setup
instructions, refer to the
Cloud DNS documentation
.
Ensure that you are using Cloud DNS version 1.
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Configure Google Cloud to ingest Cloud DNS logs
To ingest Cloud DNS logs to Google Security Operations, follow the steps on the
Ingest Google Cloud logs to Google Security Operations
page.
If you encounter issues when you ingest Cloud DNS logs,
contact Google Security Operations support
.
Supported Cloud DNS log formats
The Google Cloud DNS parser supports logs in both JSON format.
Supported Cloud DNS Sample Logs
JSON
{
    "insertId": "of4onjd9km0",
    "jsonPayload": {
      "authAnswer": true,
      "serverLatency": 0.0,
      "queryName": "dNs.DataSOfT.cLoUDnS.pH.",
      "vmProjectId": "abc12-123456",
      "vmZoneName": "us-central1-c",
      "vmInstanceName": "329088982544.vm-707dd8df-9e19-4537-410d-e2b5597f49b8",
      "authAnswer": true,
      "responseCode": "BADCOOKIE",
      "destinationIP": "198.51.100.5",
      "protocol": "UDP",
      "structuredRdata": [
        {
          "class": "IN",
          "ttl": "300",
          "domainName": "dummy.domain.name.com.",
          "rvalue": "198.51.100.4",
          "type": "A"
        }
      ],
      "queryType": "AAAA"
    },
    "resource": {
      "type": "dns_query",
      "labels": {
        "target_type": "public-zone",
        "location": "global",
        "source_type": "internet",
        "project_id": "chronical-34531",
        "target_name": "clouddns-zone"
      }
    },
    "timestamp": "2023-08-01T10:24:59.349280070Z",
    "severity": "INFO",
    "logName": "projects/chronical-34531/logs/dns.googleapis.com%2Fdns_queries",
    "receiveTimestamp": "2023-08-01T10:25:00.651062191Z"
  }
Field mapping reference
This section explains how the Google Security Operations parser maps Google Cloud DNS fields to Google Security Operations Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
alias_query_response_code
about.labels[alias_query_response_code]
(deprecated)
alias_query_response_code
additional.fields[alias_query_response_code]
egressError
about.labels[egress_error]
(deprecated)
egressError
additional.fields[egress_error]
healthyIps
about.ip
jsonPayload.serverLatency
about.labels[server_latency]
(deprecated)
jsonPayload.serverLatency
additional.fields[server_latency]
unHealthyIps
about.labels[un_healthy_ips]
(deprecated)
unHealthyIps
additional.fields[un_healthy_ips]
jsonPayload.responseCode
additional.fields[response_code]
jsonPayload.egressIP
intermediary.ip
receiveTimestamp
metadata.collected_timestamp
timestamp
metadata.event_timestamp
metadata.event_type
If the
jsonPayload.sourceIP
log field value is
not
empty and the
jsonPayload.queryName
log field value is
not
empty or does not contain an end period (.), then the
metadata.event_type
UDM field is set to
NETWORK_DNS
.
Else, if the
jsonPayload.sourceIP
log field value is
not
empty and the
jsonPayload.queryName
log field value is
not
empty or does not contain an end period (.), then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
insertId
metadata.product_log_id
metadata.product_name
The
metadata.product_name
UDM field is set to
Google Cloud DNS
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
resource.type
metadata.description
network.application_protocol
The
network.application_protocol
UDM field is set to
DNS
.
jsonPayload.structuredRdata.class
network.dns.answers.class
If the
jsonPayload.structuredRdata.class
log field value is equal to
IN
, then the
network.dns.answers.class
UDM field is set to
1
.
Else, if the
jsonPayload.structuredRdata.class
log field value is equal to
CH
, then the
network.dns.answers.class
UDM field is set to
3
.
Else, if the
jsonPayload.structuredRdata.class
log field value is equal to
HS
, then the
network.dns.answers.class
UDM field is set to
4
.
jsonPayload.rdata.class
network.dns.answers.class
If the
jsonPayload.rdata.class
log field value is equal to
IN
, then the
network.dns.answers.class
UDM field is set to
1
.
Else, if the
jsonPayload.rdata.class
log field value is equal to
CH
, then the
network.dns.answers.class
UDM field is set to
3
.
Else, if the
jsonPayload.rdata.class
log field value is equal to
HS
, then the
network.dns.answers.class
UDM field is set to
4
.
jsonPayload.structuredRdata.rvalue
network.dns.answers.data
jsonPayload.rdata.data
network.dns.answers.data
jsonPayload.structuredRdata.domainName
network.dns.answers.name
Extracted
domainName
from the
jsonPayload.structuredRdata.domainName
log field using the Grok pattern and mapped to the
network.dns.answers.name
UDM field.
jsonPayload.rdata.name
network.dns.answers.name
Extracted
domainName
from the
jsonPayload.rdata.name
log field using the Grok pattern and mapped to the
network.dns.answers.name
UDM field.
jsonPayload.structuredRdata.ttl
network.dns.answers.ttl
jsonPayload.rdata.ttl
network.dns.answers.ttl
jsonPayload.structuredRdata.type
network.dns.answers.type
If the
jsonPayload.structuredRdata.type
log field value is equal to
A
, then the
network.dns.answers.type
UDM field is set to
1
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NS
, then the
network.dns.answers.type
UDM field is set to
2
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MD
, then the
network.dns.answers.type
UDM field is set to
3
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MF
, then the
network.dns.answers.type
UDM field is set to
4
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
CNAME
, then the
network.dns.answers.type
UDM field is set to
5
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SOA
, then the
network.dns.answers.type
UDM field is set to
6
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MB
, then the
network.dns.answers.type
UDM field is set to
7
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MG
, then the
network.dns.answers.type
UDM field is set to
8
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MR
, then the
network.dns.answers.type
UDM field is set to
9
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NULL
, then the
network.dns.answers.type
UDM field is set to
10
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
WKS
, then the
network.dns.answers.type
UDM field is set to
11
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
PTR
, then the
network.dns.answers.type
UDM field is set to
12
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
HINFO
, then the
network.dns.answers.type
UDM field is set to
13
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MINFO
, then the
network.dns.answers.type
UDM field is set to
14
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MX
, then the
network.dns.answers.type
UDM field is set to
15
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
TXT
, then the
network.dns.answers.type
UDM field is set to
16
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
RP
, then the
network.dns.answers.type
UDM field is set to
17
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
AFSDB
, then the
network.dns.answers.type
UDM field is set to
18
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
X25
, then the
network.dns.answers.type
UDM field is set to
19
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
ISDN
, then the
network.dns.answers.type
UDM field is set to
20
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
RT
, then the
network.dns.answers.type
UDM field is set to
21
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NSAP
, then the
network.dns.answers.type
UDM field is set to
22
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NSAP-PTR
, then the
network.dns.answers.type
UDM field is set to
23
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SIG
, then the
network.dns.answers.type
UDM field is set to
24
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
KEY
, then the
network.dns.answers.type
UDM field is set to
25
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
PX
, then the
network.dns.answers.type
UDM field is set to
26
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
GPOS
, then the
network.dns.answers.type
UDM field is set to
27
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
AAAA
, then the
network.dns.answers.type
UDM field is set to
28
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
LOC
, then the
network.dns.answers.type
UDM field is set to
29
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NXT
, then the
network.dns.answers.type
UDM field is set to
30
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
EID
, then the
network.dns.answers.type
UDM field is set to
31
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NIMLOC
, then the
network.dns.answers.type
UDM field is set to
32
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SRV
, then the
network.dns.answers.type
UDM field is set to
33
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
ATMA
, then the
network.dns.answers.type
UDM field is set to
34
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NAPTR
, then the
network.dns.answers.type
UDM field is set to
35
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
KX
, then the
network.dns.answers.type
UDM field is set to
36
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
CERT
, then the
network.dns.answers.type
UDM field is set to
37
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
A6
, then the
network.dns.answers.type
UDM field is set to
38
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
DNAME
, then the
network.dns.answers.type
UDM field is set to
39
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SINK
, then the
network.dns.answers.type
UDM field is set to
40
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
OPT
, then the
network.dns.answers.type
UDM field is set to
41
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
APL
, then the
network.dns.answers.type
UDM field is set to
42
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
DS
, then the
network.dns.answers.type
UDM field is set to
43
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SSHFP
, then the
network.dns.answers.type
UDM field is set to
44
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
IPSECKEY
, then the
network.dns.answers.type
UDM field is set to
45
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
RRSIG
, then the
network.dns.answers.type
UDM field is set to
46
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NSEC
, then the
network.dns.answers.type
UDM field is set to
47
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
DNSKEY
, then the
network.dns.answers.type
UDM field is set to
48
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
DHCID
, then the
network.dns.answers.type
UDM field is set to
49
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NSEC3
, then the
network.dns.answers.type
UDM field is set to
50
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NSEC3PARAM
, then the
network.dns.answers.type
UDM field is set to
51
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
TLSA
, then the
network.dns.answers.type
UDM field is set to
52
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SMIMEA
, then the
network.dns.answers.type
UDM field is set to
53
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
UNASSIGN
, then the
network.dns.answers.type
UDM field is set to
54
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
HIP
, then the
network.dns.answers.type
UDM field is set to
55
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NINFO
, then the
network.dns.answers.type
UDM field is set to
56
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
RKEY
, then the
network.dns.answers.type
UDM field is set to
57
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
TALINK
, then the
network.dns.answers.type
UDM field is set to
58
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
CDS
, then the
network.dns.answers.type
UDM field is set to
59
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
CDNSKEY
, then the
network.dns.answers.type
UDM field is set to
60
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
OPENPGPK
, then the
network.dns.answers.type
UDM field is set to
61
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
CSYNC
, then the
network.dns.answers.type
UDM field is set to
62
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
ZONEMD
, then the
network.dns.answers.type
UDM field is set to
63
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SVCB
, then the
network.dns.answers.type
UDM field is set to
64
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
HTTPS
, then the
network.dns.answers.type
UDM field is set to
65
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
SPF
, then the
network.dns.answers.type
UDM field is set to
99
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
UINFO
, then the
network.dns.answers.type
UDM field is set to
100
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
UID
, then the
network.dns.answers.type
UDM field is set to
101
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
GID
, then the
network.dns.answers.type
UDM field is set to
102
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
UNSPEC
, then the
network.dns.answers.type
UDM field is set to
103
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
NID
, then the
network.dns.answers.type
UDM field is set to
104
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
L32
, then the
network.dns.answers.type
UDM field is set to
105
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
L64
, then the
network.dns.answers.type
UDM field is set to
106
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
LP
, then the
network.dns.answers.type
UDM field is set to
107
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
EUI48
, then the
network.dns.answers.type
UDM field is set to
108
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
EUI64
, then the
network.dns.answers.type
UDM field is set to
109
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
TKEY
, then the
network.dns.answers.type
UDM field is set to
249
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
TSIG
, then the
network.dns.answers.type
UDM field is set to
250
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
IXFR
, then the
network.dns.answers.type
UDM field is set to
251
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
AXFR
, then the
network.dns.answers.type
UDM field is set to
252
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MAILB
, then the
network.dns.answers.type
UDM field is set to
253
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
MAILA
, then the
network.dns.answers.type
UDM field is set to
254
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
ALL
, then the
network.dns.answers.type
UDM field is set to
255
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
URI
, then the
network.dns.answers.type
UDM field is set to
256
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
CAA
, then the
network.dns.answers.type
UDM field is set to
257
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
AVC
, then the
network.dns.answers.type
UDM field is set to
258
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
DOA
, then the
network.dns.answers.type
UDM field is set to
259
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
AMTRELAY
, then the
network.dns.answers.type
UDM field is set to
260
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
TA
, then the
network.dns.answers.type
UDM field is set to
32768
.
Else, if the
jsonPayload.structuredRdata.type
log field value is equal to
DLV
, then the
network.dns.answers.type
UDM field is set to
32769
.
jsonPayload.rdata.type
network.dns.answers.type
If the
jsonPayload.rdata.type
log field value is equal to
A
, then the
network.dns.answers.type
UDM field is set to
1
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NS
, then the
network.dns.answers.type
UDM field is set to
2
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MD
, then the
network.dns.answers.type
UDM field is set to
3
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MF
, then the
network.dns.answers.type
UDM field is set to
4
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
CNAME
, then the
network.dns.answers.type
UDM field is set to
5
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SOA
, then the
network.dns.answers.type
UDM field is set to
6
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MB
, then the
network.dns.answers.type
UDM field is set to
7
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MG
, then the
network.dns.answers.type
UDM field is set to
8
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MR
, then the
network.dns.answers.type
UDM field is set to
9
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NULL
, then the
network.dns.answers.type
UDM field is set to
10
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
WKS
, then the
network.dns.answers.type
UDM field is set to
11
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
PTR
, then the
network.dns.answers.type
UDM field is set to
12
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
HINFO
, then the
network.dns.answers.type
UDM field is set to
13
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MINFO
, then the
network.dns.answers.type
UDM field is set to
14
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MX
, then the
network.dns.answers.type
UDM field is set to
15
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
TXT
, then the
network.dns.answers.type
UDM field is set to
16
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
RP
, then the
network.dns.answers.type
UDM field is set to
17
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
AFSDB
, then the
network.dns.answers.type
UDM field is set to
18
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
X25
, then the
network.dns.answers.type
UDM field is set to
19
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
ISDN
, then the
network.dns.answers.type
UDM field is set to
20
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
RT
, then the
network.dns.answers.type
UDM field is set to
21
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NSAP
, then the
network.dns.answers.type
UDM field is set to
22
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NSAP-PTR
, then the
network.dns.answers.type
UDM field is set to
23
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SIG
, then the
network.dns.answers.type
UDM field is set to
24
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
KEY
, then the
network.dns.answers.type
UDM field is set to
25
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
PX
, then the
network.dns.answers.type
UDM field is set to
26
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
GPOS
, then the
network.dns.answers.type
UDM field is set to
27
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
AAAA
, then the
network.dns.answers.type
UDM field is set to
28
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
LOC
, then the
network.dns.answers.type
UDM field is set to
29
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NXT
, then the
network.dns.answers.type
UDM field is set to
30
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
EID
, then the
network.dns.answers.type
UDM field is set to
31
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NIMLOC
, then the
network.dns.answers.type
UDM field is set to
32
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SRV
, then the
network.dns.answers.type
UDM field is set to
33
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
ATMA
, then the
network.dns.answers.type
UDM field is set to
34
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NAPTR
, then the
network.dns.answers.type
UDM field is set to
35
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
KX
, then the
network.dns.answers.type
UDM field is set to
36
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
CERT
, then the
network.dns.answers.type
UDM field is set to
37
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
A6
, then the
network.dns.answers.type
UDM field is set to
38
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
DNAME
, then the
network.dns.answers.type
UDM field is set to
39
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SINK
, then the
network.dns.answers.type
UDM field is set to
40
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
OPT
, then the
network.dns.answers.type
UDM field is set to
41
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
APL
, then the
network.dns.answers.type
UDM field is set to
42
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
DS
, then the
network.dns.answers.type
UDM field is set to
43
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SSHFP
, then the
network.dns.answers.type
UDM field is set to
44
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
IPSECKEY
, then the
network.dns.answers.type
UDM field is set to
45
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
RRSIG
, then the
network.dns.answers.type
UDM field is set to
46
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NSEC
, then the
network.dns.answers.type
UDM field is set to
47
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
DNSKEY
, then the
network.dns.answers.type
UDM field is set to
48
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
DHCID
, then the
network.dns.answers.type
UDM field is set to
49
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NSEC3
, then the
network.dns.answers.type
UDM field is set to
50
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NSEC3PARAM
, then the
network.dns.answers.type
UDM field is set to
51
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
TLSA
, then the
network.dns.answers.type
UDM field is set to
52
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SMIMEA
, then the
network.dns.answers.type
UDM field is set to
53
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
UNASSIGN
, then the
network.dns.answers.type
UDM field is set to
54
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
HIP
, then the
network.dns.answers.type
UDM field is set to
55
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NINFO
, then the
network.dns.answers.type
UDM field is set to
56
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
RKEY
, then the
network.dns.answers.type
UDM field is set to
57
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
TALINK
, then the
network.dns.answers.type
UDM field is set to
58
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
CDS
, then the
network.dns.answers.type
UDM field is set to
59
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
CDNSKEY
, then the
network.dns.answers.type
UDM field is set to
60
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
OPENPGPK
, then the
network.dns.answers.type
UDM field is set to
61
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
CSYNC
, then the
network.dns.answers.type
UDM field is set to
62
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
ZONEMD
, then the
network.dns.answers.type
UDM field is set to
63
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SVCB
, then the
network.dns.answers.type
UDM field is set to
64
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
HTTPS
, then the
network.dns.answers.type
UDM field is set to
65
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
SPF
, then the
network.dns.answers.type
UDM field is set to
99
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
UINFO
, then the
network.dns.answers.type
UDM field is set to
100
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
UID
, then the
network.dns.answers.type
UDM field is set to
101
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
GID
, then the
network.dns.answers.type
UDM field is set to
102
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
UNSPEC
, then the
network.dns.answers.type
UDM field is set to
103
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
NID
, then the
network.dns.answers.type
UDM field is set to
104
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
L32
, then the
network.dns.answers.type
UDM field is set to
105
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
L64
, then the
network.dns.answers.type
UDM field is set to
106
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
LP
, then the
network.dns.answers.type
UDM field is set to
107
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
EUI48
, then the
network.dns.answers.type
UDM field is set to
108
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
EUI64
, then the
network.dns.answers.type
UDM field is set to
109
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
TKEY
, then the
network.dns.answers.type
UDM field is set to
249
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
TSIG
, then the
network.dns.answers.type
UDM field is set to
250
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
IXFR
, then the
network.dns.answers.type
UDM field is set to
251
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
AXFR
, then the
network.dns.answers.type
UDM field is set to
252
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MAILB
, then the
network.dns.answers.type
UDM field is set to
253
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
MAILA
, then the
network.dns.answers.type
UDM field is set to
254
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
ALL
, then the
network.dns.answers.type
UDM field is set to
255
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
URI
, then the
network.dns.answers.type
UDM field is set to
256
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
CAA
, then the
network.dns.answers.type
UDM field is set to
257
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
AVC
, then the
network.dns.answers.type
UDM field is set to
258
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
DOA
, then the
network.dns.answers.type
UDM field is set to
259
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
AMTRELAY
, then the
network.dns.answers.type
UDM field is set to
260
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
TA
, then the
network.dns.answers.type
UDM field is set to
32768
.
Else, if the
jsonPayload.rdata.type
log field value is equal to
DLV
, then the
network.dns.answers.type
UDM field is set to
32769
.
jsonPayload.authAnswer
network.dns.authoritative
If the
jsonPayload.authAnswer
log field value is equal to
true
, then the
network.dns.authoritative
UDM field is set to
test
.
jsonPayload.queryName
network.dns.questions.name
If the
jsonPayload.queryName
log field matches the regular expression pattern
%{WORD:part1}%{GREEDYDATA}\\\\%{WORD}%{GREEDYDATA:part2}
, then the extracted fields
part1
and
part2
are mapped to
the
network.dns.questions.name
UDM field.
Else, if the
jsonPayload.queryName
log field matches the regular expression pattern
(?P
.*)\.$
, then the extracted field
domain
is mapped to the
network.dns.questions.name
UDM field.
jsonPayload.queryType
network.dns.questions.type
If the
jsonPayload.queryType
log field value is equal to
A
, then the
network.dns.questions.type
UDM field is set to
1
.
Else, if the
jsonPayload.queryType
log field value is equal to
NS
, then the
network.dns.questions.type
UDM field is set to
2
.
Else, if the
jsonPayload.queryType
log field value is equal to
MD
, then the
network.dns.questions.type
UDM field is set to
3
.
Else, if the
jsonPayload.queryType
log field value is equal to
MF
, then the
network.dns.questions.type
UDM field is set to
4
.
Else, if the
jsonPayload.queryType
log field value is equal to
CNAME
, then the
network.dns.questions.type
UDM field is set to
5
.
Else, if the
jsonPayload.queryType
log field value is equal to
SOA
, then the
network.dns.questions.type
UDM field is set to
6
.
Else, if the
jsonPayload.queryType
log field value is equal to
MB
, then the
network.dns.questions.type
UDM field is set to
7
.
Else, if the
jsonPayload.queryType
log field value is equal to
MG
, then the
network.dns.questions.type
UDM field is set to
8
.
Else, if the
jsonPayload.queryType
log field value is equal to
MR
, then the
network.dns.questions.type
UDM field is set to
9
.
Else, if the
jsonPayload.queryType
log field value is equal to
NULL
, then the
network.dns.questions.type
UDM field is set to
10
.
Else, if the
jsonPayload.queryType
log field value is equal to
WKS
, then the
network.dns.questions.type
UDM field is set to
11
.
Else, if the
jsonPayload.queryType
log field value is equal to
PTR
, then the
network.dns.questions.type
UDM field is set to
12
.
Else, if the
jsonPayload.queryType
log field value is equal to
HINFO
, then the
network.dns.questions.type
UDM field is set to
13
.
Else, if the
jsonPayload.queryType
log field value is equal to
MINFO
, then the
network.dns.questions.type
UDM field is set to
14
.
Else, if the
jsonPayload.queryType
log field value is equal to
MX
, then the
network.dns.questions.type
UDM field is set to
15
.
Else, if the
jsonPayload.queryType
log field value is equal to
TXT
, then the
network.dns.questions.type
UDM field is set to
16
.
Else, if the
jsonPayload.queryType
log field value is equal to
RP
, then the
network.dns.questions.type
UDM field is set to
17
.
Else, if the
jsonPayload.queryType
log field value is equal to
AFSDB
, then the
network.dns.questions.type
UDM field is set to
18
.
Else, if the
jsonPayload.queryType
log field value is equal to
X25
, then the
network.dns.questions.type
UDM field is set to
19
.
Else, if the
jsonPayload.queryType
log field value is equal to
ISDN
, then the
network.dns.questions.type
UDM field is set to
20
.
Else, if the
jsonPayload.queryType
log field value is equal to
RT
, then the
network.dns.questions.type
UDM field is set to
21
.
Else, if the
jsonPayload.queryType
log field value is equal to
NSAP
, then the
network.dns.questions.type
UDM field is set to
22
.
Else, if the
jsonPayload.queryType
log field value is equal to
NSAP-PTR
, then the
network.dns.questions.type
UDM field is set to
23
.
Else, if the
jsonPayload.queryType
log field value is equal to
SIG
, then the
network.dns.questions.type
UDM field is set to
24
.
Else, if the
jsonPayload.queryType
log field value is equal to
KEY
, then the
network.dns.questions.type
UDM field is set to
25
.
Else, if the
jsonPayload.queryType
log field value is equal to
PX
, then the
network.dns.questions.type
UDM field is set to
26
.
Else, if the
jsonPayload.queryType
log field value is equal to
GPOS
, then the
network.dns.questions.type
UDM field is set to
27
.
Else, if the
jsonPayload.queryType
log field value is equal to
AAAA
, then the
network.dns.questions.type
UDM field is set to
28
.
Else, if the
jsonPayload.queryType
log field value is equal to
LOC
, then the
network.dns.questions.type
UDM field is set to
29
.
Else, if the
jsonPayload.queryType
log field value is equal to
NXT
, then the
network.dns.questions.type
UDM field is set to
30
.
Else, if the
jsonPayload.queryType
log field value is equal to
EID
, then the
network.dns.questions.type
UDM field is set to
31
.
Else, if the
jsonPayload.queryType
log field value is equal to
NIMLOC
, then the
network.dns.questions.type
UDM field is set to
32
.
Else, if the
jsonPayload.queryType
log field value is equal to
SRV
, then the
network.dns.questions.type
UDM field is set to
33
.
Else, if the
jsonPayload.queryType
log field value is equal to
ATMA
, then the
network.dns.questions.type
UDM field is set to
34
.
Else, if the
jsonPayload.queryType
log field value is equal to
NAPTR
, then the
network.dns.questions.type
UDM field is set to
35
.
Else, if the
jsonPayload.queryType
log field value is equal to
KX
, then the
network.dns.questions.type
UDM field is set to
36
.
Else, if the
jsonPayload.queryType
log field value is equal to
CERT
, then the
network.dns.questions.type
UDM field is set to
37
.
Else, if the
jsonPayload.queryType
log field value is equal to
A6
, then the
network.dns.questions.type
UDM field is set to
38
.
Else, if the
jsonPayload.queryType
log field value is equal to
DNAME
, then the
network.dns.questions.type
UDM field is set to
39
.
Else, if the
jsonPayload.queryType
log field value is equal to
SINK
, then the
network.dns.questions.type
UDM field is set to
40
.
Else, if the
jsonPayload.queryType
log field value is equal to
OPT
, then the
network.dns.questions.type
UDM field is set to
41
.
Else, if the
jsonPayload.queryType
log field value is equal to
APL
, then the
network.dns.questions.type
UDM field is set to
42
.
Else, if the
jsonPayload.queryType
log field value is equal to
DS
, then the
network.dns.questions.type
UDM field is set to
43
.
Else, if the
jsonPayload.queryType
log field value is equal to
SSHFP
, then the
network.dns.questions.type
UDM field is set to
44
.
Else, if the
jsonPayload.queryType
log field value is equal to
IPSECKEY
, then the
network.dns.questions.type
UDM field is set to
45
.
Else, if the
jsonPayload.queryType
log field value is equal to
RRSIG
, then the
network.dns.questions.type
UDM field is set to
46
.
Else, if the
jsonPayload.queryType
log field value is equal to
NSEC
, then the
network.dns.questions.type
UDM field is set to
47
.
Else, if the
jsonPayload.queryType
log field value is equal to
DNSKEY
, then the
network.dns.questions.type
UDM field is set to
48
.
Else, if the
jsonPayload.queryType
log field value is equal to
DHCID
, then the
network.dns.questions.type
UDM field is set to
49
.
Else, if the
jsonPayload.queryType
log field value is equal to
NSEC3
, then the
network.dns.questions.type
UDM field is set to
50
.
Else, if the
jsonPayload.queryType
log field value is equal to
NSEC3PARAM
, then the
network.dns.questions.type
UDM field is set to
51
.
Else, if the
jsonPayload.queryType
log field value is equal to
TLSA
, then the
network.dns.questions.type
UDM field is set to
52
.
Else, if the
jsonPayload.queryType
log field value is equal to
SMIMEA
, then the
network.dns.questions.type
UDM field is set to
53
.
Else, if the
jsonPayload.queryType
log field value is equal to
UNASSIGN
, then the
network.dns.questions.type
UDM field is set to
54
.
Else, if the
jsonPayload.queryType
log field value is equal to
HIP
, then the
network.dns.questions.type
UDM field is set to
55
.
Else, if the
jsonPayload.queryType
log field value is equal to
NINFO
, then the
network.dns.questions.type
UDM field is set to
56
.
Else, if the
jsonPayload.queryType
log field value is equal to
RKEY
, then the
network.dns.questions.type
UDM field is set to
57
.
Else, if the
jsonPayload.queryType
log field value is equal to
TALINK
, then the
network.dns.questions.type
UDM field is set to
58
.
Else, if the
jsonPayload.queryType
log field value is equal to
CDS
, then the
network.dns.questions.type
UDM field is set to
59
.
Else, if the
jsonPayload.queryType
log field value is equal to
CDNSKEY
, then the
network.dns.questions.type
UDM field is set to
60
.
Else, if the
jsonPayload.queryType
log field value is equal to
OPENPGPK
, then the
network.dns.questions.type
UDM field is set to
61
.
Else, if the
jsonPayload.queryType
log field value is equal to
CSYNC
, then the
network.dns.questions.type
UDM field is set to
62
.
Else, if the
jsonPayload.queryType
log field value is equal to
ZONEMD
, then the
network.dns.questions.type
UDM field is set to
63
.
Else, if the
jsonPayload.queryType
log field value is equal to
SVCB
, then the
network.dns.questions.type
UDM field is set to
64
.
Else, if the
jsonPayload.queryType
log field value is equal to
HTTPS
, then the
network.dns.questions.type
UDM field is set to
65
.
Else, if the
jsonPayload.queryType
log field value is equal to
SPF
, then the
network.dns.questions.type
UDM field is set to
99
.
Else, if the
jsonPayload.queryType
log field value is equal to
UINFO
, then the
network.dns.questions.type
UDM field is set to
100
.
Else, if the
jsonPayload.queryType
log field value is equal to
UID
, then the
network.dns.questions.type
UDM field is set to
101
.
Else, if the
jsonPayload.queryType
log field value is equal to
GID
, then the
network.dns.questions.type
UDM field is set to
102
.
Else, if the
jsonPayload.queryType
log field value is equal to
UNSPEC
, then the
network.dns.questions.type
UDM field is set to
103
.
Else, if the
jsonPayload.queryType
log field value is equal to
NID
, then the
network.dns.questions.type
UDM field is set to
104
.
Else, if the
jsonPayload.queryType
log field value is equal to
L32
, then the
network.dns.questions.type
UDM field is set to
105
.
Else, if the
jsonPayload.queryType
log field value is equal to
L64
, then the
network.dns.questions.type
UDM field is set to
106
.
Else, if the
jsonPayload.queryType
log field value is equal to
LP
, then the
network.dns.questions.type
UDM field is set to
107
.
Else, if the
jsonPayload.queryType
log field value is equal to
EUI48
, then the
network.dns.questions.type
UDM field is set to
108
.
Else, if the
jsonPayload.queryType
log field value is equal to
EUI64
, then the
network.dns.questions.type
UDM field is set to
109
.
Else, if the
jsonPayload.queryType
log field value is equal to
TKEY
, then the
network.dns.questions.type
UDM field is set to
249
.
Else, if the
jsonPayload.queryType
log field value is equal to
TSIG
, then the
network.dns.questions.type
UDM field is set to
250
.
Else, if the
jsonPayload.queryType
log field value is equal to
IXFR
, then the
network.dns.questions.type
UDM field is set to
251
.
Else, if the
jsonPayload.queryType
log field value is equal to
AXFR
, then the
network.dns.questions.type
UDM field is set to
252
.
Else, if the
jsonPayload.queryType
log field value is equal to
MAILB
, then the
network.dns.questions.type
UDM field is set to
253
.
Else, if the
jsonPayload.queryType
log field value is equal to
MAILA
, then the
network.dns.questions.type
UDM field is set to
254
.
Else, if the
jsonPayload.queryType
log field value is equal to
ALL
, then the
network.dns.questions.type
UDM field is set to
255
.
Else, if the
jsonPayload.queryType
log field value is equal to
URI
, then the
network.dns.questions.type
UDM field is set to
256
.
Else, if the
jsonPayload.queryType
log field value is equal to
CAA
, then the
network.dns.questions.type
UDM field is set to
257
.
Else, if the
jsonPayload.queryType
log field value is equal to
AVC
, then the
network.dns.questions.type
UDM field is set to
258
.
Else, if the
jsonPayload.queryType
log field value is equal to
DOA
, then the
network.dns.questions.type
UDM field is set to
259
.
Else, if the
jsonPayload.queryType
log field value is equal to
AMTRELAY
, then the
network.dns.questions.type
UDM field is set to
260
.
Else, if the
jsonPayload.queryType
log field value is equal to
TA
, then the
network.dns.questions.type
UDM field is set to
32768
.
Else, if the
jsonPayload.queryType
log field value is equal to
DLV
, then the
network.dns.questions.type
UDM field is set to
32769
.
jsonPayload.responseCode
network.dns.response_code
If the
jsonPayload.responseCode
log field value is equal to
FORMERR
, then the
network.dns.response_code
UDM field is set to
1
.
Else, if the
jsonPayload.responseCode
log field value is equal to
SERVFAIL
, then the
network.dns.response_code
UDM field is set to
2
.
Else, if the
jsonPayload.responseCode
log field value is equal to
NXDOMAIN
, then the
network.dns.response_code
UDM field is set to
3
.
Else, if the
jsonPayload.responseCode
log field value is equal to
NOTIMP
, then the
network.dns.response_code
UDM field is set to
4
.
Else, if the
jsonPayload.responseCode
log field value is equal to
REFUSED
, then the
network.dns.response_code
UDM field is set to
5
.
Else, if the
jsonPayload.responseCode
log field value is equal to
YXDOMAIN
, then the
network.dns.response_code
UDM field is set to
6
.
Else, if the
jsonPayload.responseCode
log field value is equal to
YXRRSET
, then the
network.dns.response_code
UDM field is set to
7
.
Else, if the
jsonPayload.responseCode
log field value is equal to
NXRRSET
, then the
network.dns.response_code
UDM field is set to
8
.
Else, if the
jsonPayload.responseCode
log field value is equal to
NOTAUTH
, then the
network.dns.response_code
UDM field is set to
9
.
Else, if the
jsonPayload.responseCode
log field value is equal to
NOTZONE
, then the
network.dns.response_code
UDM field is set to
10
.
Else, if the
jsonPayload.responseCode
log field value is equal to
DSOTYPENI
, then the
network.dns.response_code
UDM field is set to
11
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADVERS
, then the
network.dns.response_code
UDM field is set to
16
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADSIG
, then the
network.dns.response_code
UDM field is set to
16
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADKEY
, then the
network.dns.response_code
UDM field is set to
17
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADTIME
, then the
network.dns.response_code
UDM field is set to
18
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADMODE
, then the
network.dns.response_code
UDM field is set to
19
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADNAME
, then the
network.dns.response_code
UDM field is set to
20
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADALG
, then the
network.dns.response_code
UDM field is set to
21
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADTRUNC
, then the
network.dns.response_code
UDM field is set to
22
.
Else, if the
jsonPayload.responseCode
log field value is equal to
BADCOOKIE
, then the
network.dns.response_code
UDM field is set to
23
.
network.dns.truncated
If the
jsonPayload.rdata
log field value is
not
empty, then the
network.dns.truncated
UDM field is set to
true
.
jsonPayload.protocol
network.ip_protocol
If the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ICMP
.
1
ICMP
ICMPV6
58
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
IGMP
.
2
IGMP
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
TCP
.
6
TCP
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
UDP
.
17
UDP
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
IP6IN4
.
41
IP6IN4
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
GRE
.
47
GRE
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ESP
.
50
ESP
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
EIGRP
.
88
EIGRP
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ETHERIP
.
97
ETHERIP
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
PIM
.
103
PIM
Else, if the
jsonPayload.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
VRRP
.
112
VRRP
.
jsonPayload.sourceIP
principal.ip
jsonPayload.sourceNetwork
additional.fields[source_network]
resource.labels.location
principal.location.name
jsonPayload.vmZoneName
principal.resource.attribute.cloud.availability_zone
principal.resource.attribute.cloud.environment
The
principal.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
principal.cloud.environment
The
principal.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.labels.source_type
principal.resource.attribute.labels[source_type]
resource.labels.target_name
principal.resource.attribute.labels[target_name]
resource.labels.target_type
principal.resource.attribute.labels[target_type]
jsonPayload.vmInstanceName
principal.resource.name
Extracted
projectororg
from the
logName
log field using the Grok pattern.
If the
jsonPayload.vmInstanceName
log field value is
not
empty, then the
//compute.googleapis.com/projects/%{projectororg}/zones/%{resource.labels.location}/instances/%{jsonPayload.vmInstanceName}
field is mapped to the
principal.resource.name
UDM field.
logName
principal.resource.name
Extracted
projectororg
from the
logName
log field using the Grok pattern.
jsonPayload.vmInstanceIdString
principal.resource.id
If the
jsonPayload.vmInstanceIdString
log field value is
not
empty, then the
jsonPayload.vmInstanceIdString
log field is mapped to the
principal.resource.id
UDM field.
Else, if the
jsonPayload.vmInstanceId
log field value is
not
empty, then the
jsonPayload.vmInstanceId
log field is mapped to the
principal.resource.id
UDM field.
jsonPayload.vmInstanceId
principal.resource.id
If the
jsonPayload.vmInstanceIdString
log field value is
not
empty, then the
jsonPayload.vmInstanceIdString
log field is mapped to the
principal.resource.id
UDM field.
Else, if the
jsonPayload.vmInstanceId
log field value is
not
empty, then the
jsonPayload.vmInstanceId
log field is mapped to the
principal.resource.id
UDM field.
jsonPayload.vmInstanceIdString
principal.resource.product_object_id
If the
jsonPayload.vmInstanceIdString
log field value is
not
empty, then the
jsonPayload.vmInstanceIdString
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
jsonPayload.vmInstanceId
log field value is
not
empty, then the
jsonPayload.vmInstanceId
log field is mapped to the
principal.resource.product_object_id
UDM field.
jsonPayload.vmInstanceId
principal.resource.product_object_id
If the
jsonPayload.vmInstanceIdString
log field value is
not
empty, then the
jsonPayload.vmInstanceIdString
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, if the
jsonPayload.vmInstanceId
log field value is
not
empty, then the
jsonPayload.vmInstanceId
log field is mapped to the
principal.resource.product_object_id
UDM field.
jsonPayload.vmProjectId
principal.cloud.project.name
If the
jsonPayload.vmProjectId
log field value is
not
empty, then the
jsonPayload.vmProjectId
log field is mapped to the
principal.cloud.project.name
UDM field.
resource.labels.project_id
principal.cloud.project.name
If the
jsonPayload.vmProjectId
log field value is
empty
, then the
resource.labels.project_id
log field is mapped to the
principal.cloud.project.name
UDM field.
jsonPayload.vmProjectId
principal.resource_ancestors.name
resource.labels.project_id
principal.resource_ancestors.name
principal.resource_ancestors.resource_subtype
If the
jsonPayload.vmProjectId
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
Virtual Machine Project
.
If the
resource.labels.project_id
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
Project
.
principal.resource_ancestors.resource_type
If the
jsonPayload.vmProjectId
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
If the
resource.labels.project_id
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
resource.type
principal.resource.resource_subtype
principal.resource.resource_type
The
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
security_result.severity
If the
severity
log field value contains one of the following values, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
INFO
DEBUG
Else, if the
severity
log field value is equal to
NOTICE
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
severity
log field value is equal to
WARNING
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value is equal to
ERROR
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
severity
log field value contains one of the following values, then the
security_result.severity
UDM field is set to
CRITICAL
.
CRITICAL
ALERT
EMERGENCY
Else, if the
severity
log field value is equal to
DEFAULT
or the
severity
log field value is
not
empty, then the
security_result.severity
UDM field is set to
UNKNOWN_SEVERITY
.
severity
security_result.severity_details
jsonPayload.destinationIP
target.ip
target.resource.attribute.cloud.environment
The
target.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
