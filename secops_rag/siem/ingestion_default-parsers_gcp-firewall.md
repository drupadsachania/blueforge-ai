# Collect Google Cloud Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-firewall/  
**Scraped:** 2026-03-05T09:17:14.567007Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud Firewall logs
Supported in:
Google secops
SIEM
This document describes how you can collect Google Cloud Firewall logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of Google Cloud Firewall logs map to Google Security Operations Unified Data Model (UDM) fields.
This document also lists the supported Google Cloud Firewall version.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Google Cloud Firewall logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Google Cloud Firewall logs
: The Google Cloud Firewall logs that are
enabled for ingestion to Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Google Cloud Firewall.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_FIREWALL
ingestion label.
Before you begin
Ensure that you are using Google Cloud Firewall version 1.
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Configure Google Cloud to ingest Google Cloud Firewall logs
To ingest Google Cloud Firewall logs to Google Security Operations, follow the steps on the
Ingest Google Cloud logs to Google Security Operations
page.
If you encounter issues when you ingest Google Cloud Firewall logs,
contact Google Security Operations support
.
Supported Google Cloud Firewall log formats
The Google Cloud Firewall parser supports logs in JSON format.
Supported Google Cloud Firewall sample logs
JSON:
{
  "insertId": "1o2en3g1af0lkj",
  "jsonPayload": {
    "connection": {
      "dest_ip": "198.51.100.0",
      "dest_port": 22,
      "protocol": 6,
      "src_ip": "198.51.100.1",
      "src_port": 43144
    },
    "disposition": "ALLOWED",
    "instance": {
      "project_id": "logging-271618",
      "region": "us-central1",
      "vm_name": "elastic-siem-01",
      "zone": "us-central1-a"
    },
    "remote_location": {
      "city": "Adana",
      "continent": "Asia",
      "country": "tur",
      "region": "Adana"
    },
    "rule_details": {
      "action": "ALLOW",
      "direction": "INGRESS",
      "ip_port_info": [
        {
          "ip_protocol": "TCP",
          "port_range": [
            "22"
          ]
        }
      ],
      "priority": 65534,
      "reference": "network:default/firewall:default-allow-ssh",
      "source_range": [
        "0.0.0.0/0"
      ]
    },
    "vpc": {
      "project_id": "logging-271618",
      "subnetwork_name": "default",
      "vpc_name": "default"
    }
  },
  "logName": "projects/logging-271618/logs/compute.googleapis.com%2Ffirewall",
  "receiveTimestamp": "2020-04-14T09:00:11.292726397Z",
  "resource": {
    "labels": {
      "location": "us-central1-a",
      "project_id": "logging-271618",
      "subnetwork_id": "4738025575977389850",
      "subnetwork_name": "default"
    },
    "type": "gce_subnetwork"
  },
  "timestamp": "2020-04-14T09:00:05.889200827Z"
}
Field mapping reference
The following table lists the log fields of the
GCP_FIREWALL
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
receiveTimestamp
metadata.collected_timestamp
timestamp
metadata.event_timestamp
logName
metadata.product_event_type
metadata.event_type
If the
jsonPayload.connection.src_ip
log field value is
not
empty and the
jsonPayload.connection.dest_ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
jsonPayload.connection.src_ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
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
GCP Firewall
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
jsonPayload.rule_details.direction
network.direction
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
network.direction
UDM field is set to
OUTBOUND
.
Else, if the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
network.direction
UDM field is set to
INBOUND
.
jsonPayload.connection.protocol
network.ip_protocol
If the
jsonPayload.connection.protocol
log field value is equal to
6
, then the
network.ip_protocol
UDM field is set to
TCP
.
If the
jsonPayload.connection.protocol
log field value is equal to
17
, then the
network.ip_protocol
UDM field is set to
UDP
.
If the
jsonPayload.connection.protocol
log field value is equal to
1
, then the
network.ip_protocol
UDM field is set to
ICMP
.
If the
jsonPayload.connection.protocol
log field value is equal to
2
, then the
network.ip_protocol
UDM field is set to
IGMP
.
jsonPayload.connection.src_ip
principal.ip
jsonPayload.remote_location.continent
principal.labels[remote_location_continent]
(deprecated)
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_location.continent
log field is mapped to the
principal.labels.remote_location_continent
UDM field.
jsonPayload.remote_location.continent
additional.fields[remote_location_continent]
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_location.continent
log field is mapped to the
additional.fields.remote_location_continent
UDM field.
jsonPayload.remote_location.city
principal.location.city
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_location.city
log field is mapped to the
principal.location.city
UDM field.
jsonPayload.remote_location.country
principal.location.country_or_region
If the
jsonPayload.remote_location.country
log field value is
not
empty or the
jsonPayload.remote_location.region
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_location.country jsonPayload.remote_location.region
log field is mapped to the
principal.location.country_or_region
UDM field.
jsonPayload.remote_location.region
principal.location.country_or_region
If the
jsonPayload.remote_location.country
log field value is
not
empty or the
jsonPayload.remote_location.region
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_location.country jsonPayload.remote_location.region
log field is mapped to the
principal.location.country_or_region
UDM field.
jsonPayload.instance.region
principal.location.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.instance.region
log field is mapped to the
principal.location.name
UDM field.
jsonPayload.remote_instance.region
principal.location.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_instance.region
log field is mapped to the
principal.location.name
UDM field.
jsonPayload.connection.src_port
principal.port
resource.labels.location
principal.resource_ancestors.attribute.cloud.availability_zone
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
resource.labels.location
log field is mapped to the
principal.resource_ancestors.attribute.cloud.availability_zone
UDM field.
jsonPayload.vpc.vpc_name
principal.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.vpc.vpc_name
log field is mapped to the
principal.resource_ancestors.name
UDM field.
jsonPayload.vpc.subnetwork_name
principal.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.vpc.subnetwork_name
log field is mapped to the
principal.resource_ancestors.name
UDM field.
jsonPayload.remote_vpc.vpc_name
principal.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_vpc.vpc_name
log field is mapped to the
principal.resource_ancestors.name
UDM field.
jsonPayload.remote_vpc.subnetwork_name
principal.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_vpc.subnetwork_name
log field is mapped to the
principal.resource_ancestors.name
UDM field.
jsonPayload.vpc.project_id
principal.resource_ancestors.product_object_id
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.vpc.project_id
log field is mapped to the
principal.resource_ancestors.product_object_id
UDM field.
jsonPayload.remote_vpc.project_id
principal.resource_ancestors.product_object_id
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_vpc.project_id
log field is mapped to the
principal.resource_ancestors.product_object_id
UDM field.
resource.labels.subnetwork_id
principal.resource_ancestors.product_object_id
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
resource.labels.subnetwork_id
log field is mapped to the
principal.resource_ancestors.product_object_id
UDM field.
resource.type
principal.resource_ancestors.resource_subtype
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
resource.type
log field is mapped to the
principal.resource_ancestors.resource_subtype
UDM field.
principal.resource_ancestors.resource_type
If the
jsonPayload.vpc.vpc_name
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
principal.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
If the
jsonPayload.vpc.project_id
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
If the
jsonPayload.remote_vpc.vpc_name
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
principal.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
If the
jsonPayload.remote_vpc.project_id
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
jsonPayload.instance.zone
principal.resource.attribute.cloud.availability_zone
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.instance.zone
log field is mapped to the
principal.resource.attribute.cloud.availability_zone
UDM field.
jsonPayload.remote_instance.zone
principal.resource.attribute.cloud.availability_zone
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_instance.zone
log field is mapped to the
principal.resource.attribute.cloud.availability_zone
UDM field.
jsonPayload.instance.vm_name
principal.resource.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.instance.vm_name
log field is mapped to the
principal.resource.name
UDM field.
jsonPayload.remote_instance.vm_name
principal.resource.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.remote_instance.vm_name
log field is mapped to the
principal.resource.name
UDM field.
principal.resource.resource_type
If the
jsonPayload.instance.vm_name
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.remote_instance.vm_name
log field value is
not
empty the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
security_result.action
If the
jsonPayload.rule_details.disposition
log field value is equal to
ALLOWED
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
jsonPayload.rule_details.disposition
log field value is equal to
DENIED
, then the
security_result.action
UDM field is set to
BLOCK
.
jsonPayload.disposition
security_result.action_details
jsonPayload.rule_details.reference
security_result.description
jsonPayload.rule_details.priority
security_result.priority_details
resource.labels.firewall_rule_id
security_result.rule_id
jsonPayload.rule_details.action
security_result.rule_labels[rule_details_action]
jsonPayload.rule_details.destination_address_groups
security_result.rule_labels[rule_details_destination_address_groups]
jsonPayload.rule_details.destination_fqdn
security_result.rule_labels[rule_details_destination_fqdn]
jsonPayload.rule_details.destination_range
security_result.rule_labels[rule_details_destination_range]
jsonPayload.rule_details.destination_region_code
security_result.rule_labels[rule_details_destination_region_code]
jsonPayload.rule_details.destination_threat_intelligence
security_result.rule_labels[rule_details_destination_threat_intelligence]
jsonPayload.rule_details.ip_port_info.ip_protocol
security_result.rule_labels[rule_details_ip_port_info_ip_protocol]
jsonPayload.rule_details.ip_port_info.port_range
security_result.rule_labels[rule_details_ip_port_info_port_range]
jsonPayload.rule_details.source_address_groups
security_result.rule_labels[rule_details_source_address_groups]
jsonPayload.rule_details.source_fqdn
security_result.rule_labels[rule_details_source_fqdn]
jsonPayload.rule_details.source_range
security_result.rule_labels[rule_details_source_range]
jsonPayload.rule_details.source_region_code
security_result.rule_labels[rule_details_source_region_code]
jsonPayload.rule_details.source_service_account
security_result.rule_labels[rule_details_source_service_account]
jsonPayload.rule_details.source_tag
security_result.rule_labels[rule_details_source_tag]
jsonPayload.rule_details.source_threat_intelligence
security_result.rule_labels[rule_details_source_threat_intelligence]
jsonPayload.rule_details.target_service_account
security_result.rule_labels[rule_details_target_service_account]
jsonPayload.rule_details.target_tag
security_result.rule_labels[rule_details_target_tag]
security_result.rule_name
Extracted
rule_name
from
jsonPayload.rule_details.reference
using Grok pattern and mapped it to the
security_result.rule_name
UDM field.
jsonPayload.connection.dest_ip
target.ip
jsonPayload.remote_location.continent
target.labels[remote_location_continent]
(deprecated)
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_location.continent
log field is mapped to the
target.labels.remote_location_continent
UDM field.
jsonPayload.remote_location.continent
additional.fields[remote_location_continent]
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_location.continent
log field is mapped to the
additional.fields.remote_location_continent
UDM field.
jsonPayload.remote_location.city
target.location.city
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_location.city
log field is mapped to the
target.location.city
UDM field.
jsonPayload.remote_location.country
target.location.country_or_region
If the
jsonPayload.remote_location.country
log field value is
not
empty or the
jsonPayload.remote_location.region
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_location.country jsonPayload.remote_location.region
log field is mapped to the
target.location.country_or_region
UDM field.
jsonPayload.remote_location.region
target.location.country_or_region
If the
jsonPayload.remote_location.country
log field value is
not
empty or the
jsonPayload.remote_location.region
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_location.country jsonPayload.remote_location.region
log field is mapped to the
target.location.country_or_region
UDM field.
jsonPayload.instance.region
target.location.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.instance.region
log field is mapped to the
target.location.name
UDM field.
jsonPayload.remote_instance.region
target.location.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_instance.region
log field is mapped to the
target.location.name
UDM field.
jsonPayload.connection.dest_port
target.port
resource.labels.location
target.resource_ancestors.attribute.cloud.availability_zone
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
resource.labels.location
log field is mapped to the
target.resource_ancestors.attribute.cloud.availability_zone
UDM field.
jsonPayload.vpc.vpc_name
target.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.vpc.vpc_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
jsonPayload.vpc.subnetwork_name
target.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.vpc.subnetwork_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
jsonPayload.remote_vpc.vpc_name
target.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_vpc.vpc_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
jsonPayload.remote_vpc.subnetwork_name
target.resource_ancestors.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_vpc.subnetwork_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
jsonPayload.vpc.project_id
target.resource_ancestors.product_object_id
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.vpc.project_id
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field.
jsonPayload.remote_vpc.project_id
target.resource_ancestors.product_object_id
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_vpc.project_id
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field.
resource.labels.subnetwork_id
target.resource_ancestors.product_object_id
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
resource.labels.subnetwork_id
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field.
resource.type
target.resource_ancestors.resource_subtype
target.resource_ancestors.resource_type
If the
jsonPayload.remote_vpc.vpc_name
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
If the
jsonPayload.remote_vpc.project_id
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
If the
jsonPayload.vpc.vpc_name
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
If the
jsonPayload.vpc.project_id
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
jsonPayload.instance.zone
target.resource.attribute.cloud.availability_zone
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.instance.zone
log field is mapped to the
target.resource.attribute.cloud.availability_zone
UDM field.
jsonPayload.remote_instance.zone
target.resource.attribute.cloud.availability_zone
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_instance.zone
log field is mapped to the
target.resource.attribute.cloud.availability_zone
UDM field.
jsonPayload.instance.vm_name
target.resource.name
If the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
jsonPayload.instance.vm_name
log field is mapped to the
target.resource.product_object_id
UDM field.
jsonPayload.remote_instance.vm_name
target.resource.name
If the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
jsonPayload.remote_instance.vm_name
log field is mapped to the
target.resource.name
UDM field.
target.resource.resource_type
If the
jsonPayload.remote_instance.vm_name
log field value is
not
empty and the
jsonPayload.rule_details.direction
log field value is equal to
EGRESS
, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.instance.vm_name
log field value is
not
empty the
jsonPayload.rule_details.direction
log field value is equal to
INGRESS
, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
