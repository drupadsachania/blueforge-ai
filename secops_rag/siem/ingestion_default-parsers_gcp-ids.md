# Collect Google Cloud IDS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-ids/  
**Scraped:** 2026-03-05T09:25:08.548718Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud IDS logs
This document describes how you can collect Google Cloud IDS logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of Google Cloud IDS logs map to Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Google Cloud IDS logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Google Cloud IDS logs
: The Google Cloud IDS logs that are
enabled for ingestion to Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Google Cloud IDS.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_IDS
ingestion label.
Before you begin
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Configure Google Cloud to ingest Google Cloud IDS logs
To ingest Google Cloud IDS logs to Google Security Operations, follow the steps on the
Ingest Google Cloud logs to Google Security Operations
page.
If you encounter issues when you ingest Google Cloud IDS logs,
contact Google Security Operations support
.
Supported Google Cloud IDS log formats
The Google Cloud IDS parser supports logs in JSON format.
Supported Google Cloud IDS sample logs
JSON:
{
  "insertId": "5cb7ac422679042bcd8f0a84700c23c0-1@a1",
  "jsonPayload": {
    "alert_severity": "INFORMATIONAL",
    "alert_time": "2021-09-08T12:10:19Z",
    "application": "ssl",
    "category": "protocol-anomaly",
    "destination_ip_address": "198.51.100.0",
    "destination_port": "443",
    "details": "This signature detects suspicious and non-RFC compliant SSL traffic on port 443. This could be associated with applications sending non SSL traffic using port 443 or indicate possible malicious activity.",
    "direction": "client-to-server",
    "ip_protocol": "tcp",
    "name": "Non-RFC Compliant SSL Traffic on Port 443",
    "network": "abcd-prod-pod111-shared",
    "repeat_count": "1",
    "session_id": "1457377",
    "source_ip_address": "198.51.100.0",
    "source_port": "62543",
    "threat_id": "56112",
    "type": "vulnerability",
    "uri_or_filename": ""
  },
  "logName": "projects/abcd-prod-mnop-pod555-infra/logs/ids.googleapis.com%2Fthreat",
  "receiveTimestamp": "2021-09-08T12:10:23.953458826Z",
  "resource": {
    "labels": {
      "id": "abcd-prod-mnop-pod555-cloudidsendpoint-info",
      "location": "us-central1-a",
      "resource_container": "projects/158110290042"
    },
    "type": "ids.googleapis.com/Endpoint"
  },
  "timestamp": "2021-09-08T12:10:19Z"
}
Field mapping reference
Field mapping reference: GCP_IDS
The following table lists the log fields of the
GCP_IDS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
insertId
metadata.product_log_id
jsonPayload.alert_severity
security_result.severity
jsonPayload.alert_time
metadata.event_timestamp
jsonPayload.application
principal.application
If the
jsonPayload.direction
log field value is equal to
server-to-client
, then the
jsonPayload.application
log field is mapped to the
principal.application
UDM field.
jsonPayload.application
target.application
If the
jsonPayload.direction
log field value is equal to
client-to-server
or the
logName
log field value matches the regular expression pattern
traffic
, then the
jsonPayload.application
log field is mapped to the
target.application
UDM field.
jsonPayload.category
security_result.category_details
jsonPayload.cves
extensions.vulns.vulnerabilities.cve_id
If the
jsonPayload.cves
log field value is
not
empty, then the
jsonPayload.cves
log field is mapped to the
extensions.vulns.vulnerabilities.cve_id
UDM field.
jsonPayload.destination_ip_address
target.ip
jsonPayload.destination_port
target.port
jsonPayload.details
extensions.vulns.vulnerabilities.description
If the
jsonPayload.cves
log field value is
not
empty, then the
jsonPayload.details
log field is mapped to the
extensions.vulns.vulnerabilities.description
UDM field.
jsonPayload.direction
network.direction
If the
jsonPayload.direction
log field value is equal to
client-to-server
, then the
network.direction
UDM field is set to
OUTBOUND
.
Else, if the
jsonPayload.direction
log field value is equal to
server-to-client
, then the
network.direction
UDM field is set to
INBOUND
.
jsonPayload.elapsed_time
network.session_duration.seconds
jsonPayload.ip_protocol
network.ip_protocol
If the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ICMP
.
1
ICMP
ICMPV6
58
1.0
58.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
IGMP
.
2
IGMP
2.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
TCP
.
6
TCP
6.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
UDP
.
17
UDP
17.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
IP6IN4
.
41
IP6IN4
41.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
GRE
.
47
GRE
47.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ESP
.
50
ESP
50.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
EIGRP
.
88
EIGRP
88.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ETHERIP
.
97
ETHERIP
97.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
PIM
.
103
PIM
103.0
Else, if the
jsonPayload.ip_protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
VRRP
.
112
VRRP
112.0
jsonPayload.name
security_result.threat_name
jsonPayload.network
target.resource.name
If the
jsonPayload.direction
log field value is equal to
client-to-server
or the
logName
log field value matches the regular expression pattern
traffic
, then the
jsonPayload.network
log field is mapped to the
target.resource.name
UDM field.
jsonPayload.network
principal.resource.name
If the
jsonPayload.direction
log field value is equal to
server-to-client
, then the
jsonPayload.network
log field is mapped to the
principal.resource.name
UDM field.
target.resource.resource_type
If the
jsonPayload.direction
log field value is equal to
client-to-server
or the
logName
log field value matches the regular expression pattern
traffic
, then the
target.resource.resource_type
UDM field is set to
VPC_NETWORK
.
principal.resource.resource_type
If the
jsonPayload.direction
log field value is equal to
server-to-client
, then the
principal.resource.resource_type
UDM field is set to
VPC_NETWORK
.
jsonPayload.repeat_count
security_result.detection_fields[repeat_count]
jsonPayload.session_id
network.session_id
jsonPayload.source_ip_address
principal.ip
jsonPayload.source_port
principal.port
jsonPayload.start_time
about.labels[start_time]
(deprecated)
jsonPayload.start_time
additional.fields[start_time]
jsonPayload.threat_id
security_result.threat_id
jsonPayload.total_bytes
about.labels[total_bytes]
(deprecated)
jsonPayload.total_bytes
additional.fields[total_bytes]
jsonPayload.total_packets
about.labels[total_packets]
(deprecated)
jsonPayload.total_packets
additional.fields[total_packets]
jsonPayload.type
security_result.detection_fields[type]
jsonPayload.uri_or_filename
target.file.full_path
logName
security_result.category_details
receiveTimestamp
metadata.collected_timestamp
resource.labels.id
observer.resource.product_object_id
resource.labels.location
observer.location.name
resource.labels.resource_container
observer.resource.name
resource.type
observer.resource.resource_subtype
timestamp
metadata.event_timestamp
If the
logName
log field value matches the regular expression pattern
traffic
, then the
timestamp
log field is mapped to the
metadata.event_timestamp
UDM field.
observer.resource.resource_type
The
observer.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
observer.resource.attribute.cloud.environment
The
observer.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
security_result.category
If the
jsonPayload.category
log field value is equal to
dos
, then the
security_result.category
UDM field is set to
NETWORK_DENIAL_OF_SERVICE
.
Else, if the
jsonPayload.category
log field value is equal to
info-leak
, then the
security_result.category
UDM field is set to
NETWORK_SUSPICIOUS
.
Else, if the
jsonPayload.category
log field value is equal to
protocol-anomaly
, then the
security_result.category
UDM field is set to
NETWORK_MALICIOUS
.
Else, if the
jsonPayload.category
log field value contains one of the following values, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
backdoor
spyware
trojan
extensions.vulns.vulnerabilities.vendor
if the
jsonPayload.cves
log field value is
not
empty, then the
extensions.vulns.vulnerabilities.vendor
UDM field is set to
GCP_IDS
.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP_IDS
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
metadata.event_type
If the
jsonPayload.cves
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
SCAN_VULN_NETWROK
.
Else, if the
jsonPayload.source_ip_address
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
SCAN_NETWORK
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
