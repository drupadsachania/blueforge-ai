# Collect Cloud NAT logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloud-nat/  
**Scraped:** 2026-03-05T09:48:06.881673Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloud NAT logs
Supported in:
Google secops
SIEM
This document describes how you can collect Cloud NAT logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of Cloud NAT logs map into Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Cloud NAT logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Cloud NAT logs
: The Cloud NAT logs that are
enabled for ingestion into Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Cloud NAT.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information into this document applies to the parser
with the
GCP_CLOUD_NAT
ingestion label.
Before you begin
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Configure Google Cloud to ingest Cloud NAT logs
For more information on how to ingest logs to Google Security Operations, see
Ingest Google Cloud logs to Google Security Operations
.
If you encounter issues when you ingest Cloud NAT logs, contact
Google Security Operations support
.
Supported Cloud NAT log formats
The Cloud NAT parser supports logs in JSON format.
Supported Cloud NAT sample logs
JSON:
{
  "insertId": "1q5ys57f36f47d",
  "jsonPayload": {
    "endpoint": {
      "region": "us-central1",
      "project_id": "chronical-0001",
      "vm_name": "vm-1",
      "zone": "us-central1-a"
    },
    "connection": {
      "src_port": 100,
      "nat_port": 101,
      "dest_port": 102,
      "dest_ip": "198.51.100.15",
      "src_ip": "198.51.100.10",
      "protocol": 6,
      "nat_ip": "198.51.100.30"
    },
    "destination": {
      "geo_location": {
        "continent": "America",
        "asn": 54113,
        "country": "usa"
      }
    },
    "allocation_status": "OK",
    "gateway_identifiers": {
      "router_name": "test-rw",
      "gateway_name": "test-nat-vm",
      "region": "us-central1"
    },
    "vpc": {
      "subnetwork_name": "my-subnet-nat",
      "vpc_name": "test-vpc-nat",
      "project_id": "chronical-0001"
    }
  },
  "resource": {
    "type": "nat_gateway",
    "labels": {
      "region": "us-central1",
      "router_id": "8792319260929386950",
      "project_id": "chronical-0001",
      "gateway_name": "test-nat-vm"
    }
  },
  "timestamp": "2023-10-13T05:40:32.217836735Z",
  "labels": {
    "nat.googleapis.com/network_name": "test-vpc-nat",
    "nat.googleapis.com/router_name": "test-rw",
    "nat.googleapis.com/nat_ip": "198.51.100.0",
    "nat.googleapis.com/instance_name": "vm-1",
    "nat.googleapis.com/instance_zone": "us-central1-a",
    "nat.googleapis.com/subnetwork_name": "my-subnet-nat"
  },
  "logName": "projects/chronical-0001/logs/compute.googleapis.com%2Fnat_flows",
  "receiveTimestamp": "2023-10-13T05:40:44.062385884Z"
}
Field mapping reference
This section explains how the Google Security Operations parser maps Cloud NAT fields to Google Security Operations Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
metadata.event_type
The
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP Cloud NAT
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
receiveTimestamp
metadata.collected_timestamp
timestamp
metadata.event_timestamp
logName
security_result.category_details
insertId
metadata.product_log_id
network.direction
The
network.direction
UDM field is set to
OUTBOUND
.
network.ip_protocol
If the
jsonPayload.connection.protocol
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
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
IGMP
.
2
IGMP
2.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
TCP
.
6
TCP
6.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
UDP
.
17
UDP
17.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
IP6IN4
.
41
IP6IN4
41.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
GRE
.
47
GRE
47.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ESP
.
50
ESP
50.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
EIGRP
.
88
EIGRP
88.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
ETHERIP
.
97
ETHERIP
97.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
PIM
.
103
PIM
103.0
Else, if the
jsonPayload.connection.protocol
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
VRRP
.
112
VRRP
112.0
jsonPayload.connection.src_ip
principal.ip
jsonPayload.connection.src_port
principal.port
jsonPayload.connection.nat_ip
principal.nat_ip
jsonPayload.connection.nat_port
principal.nat_port
jsonPayload.vpc.project_id
intermediary.resource_ancestors.name
If the
jsonPayload.vpc.project_id
log field value is
not
empty, then the
//cloudresourcemanager.googleapis.com/projects/%{jsonPayload.vpc.project_id}
log field is mapped to the
intermediary.resource_ancestors.name
UDM field.
intermediary.resource_ancestors.resource_type
If the
jsonPayload.vpc.project_id
log field value is
not
empty, then the
intermediary.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
intermediary.resource_ancestors.attribute.cloud.environment
If the
jsonPayload.vpc.project_id
log field value is
not
empty, then the
intermediary.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.vpc.vpc_name
intermediary.resource_ancestors.name
intermediary.resource_ancestors.resource_type
If the
jsonPayload.vpc.vpc_name
log field value is
not
empty or the
jsonPayload.vpc.subnetwork_name
log field value is
not
empty, then the
intermediary.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
intermediary.resource_ancestors.attribute.cloud.environment
If the
jsonPayload.vpc.vpc_name
log field value is
not
empty or the
jsonPayload.vpc.subnetwork_name
log field value is
not
empty, then the
intermediary.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.vpc.subnetwork_name
intermediary.resource_ancestors.attribute.labels [vpc_subnetwork_name]
jsonPayload.gateway_identifiers.gateway_name
intermediary.resource.name
intermediary.resource.resource_type
If the
jsonPayload.gateway_identifiers.gateway_name
log field value is
not
empty or the
resource.type
log field value is
not
empty or the
resource.labels.region
log field value is
not
empty or the
jsonPayload.gateway_identifiers.router_name
log field value is
not
empty or the
resource.labels.router_id
log field value is
not
empty, then the
intermediary.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
resource.type
intermediary.resource.resource_subtype
jsonPayload.gateway_identifiers.region
intermediary.location.name
intermediary.resource.attribute.cloud.environment
If the
jsonPayload.gateway_identifiers.gateway_name
log field value is
not
empty or the
resource.type
log field value is
not
empty or the
resource.labels.region
log field value is
not
empty or the
jsonPayload.gateway_identifiers.router_name
log field value is
not
empty or the
resource.labels.router_id
log field value is
not
empty, then the
intermediary.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.labels.region
intermediary.resource.attribute.cloud.availability_zone
jsonPayload.gateway_identifiers.router_name
intermediary.resource.attribute.labels [gateway_identifiers_router_name]
resource.labels.router_id
intermediary.resource.attribute.labels [resource_labels_router_id]
jsonPayload.endpoint.project_id
principal.resource_ancestors.name
If the
jsonPayload.endpoint.project_id
log field value is
not
empty, then the
//cloudresourcemanager.googleapis.com/projects/%{jsonPayload.endpoint.project_id}
log field is mapped to the
principal.resource_ancestors.name
UDM field.
principal.resource_ancestors.resource_type
If the
jsonPayload.endpoint.project_id
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
principal.resource_ancestors.attribute.cloud.environment
If the
jsonPayload.endpoint.project_id
log field value is
not
empty, then the
principal.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.endpoint.vm_name
principal.hostname
jsonPayload.endpoint.vm_name
principal.asset.hostname
jsonPayload.endpoint.vm_name
principal.resource.name
principal.resource.resource_type
If the
jsonPayload.endpoint.vm_name
log field value is
not
empty or the
jsonPayload.endpoint.zone
log field value is
not
empty, then the
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
principal.resource.attribute.cloud.environment
If the
jsonPayload.endpoint.vm_name
log field value is
not
empty or the
jsonPayload.endpoint.zone
log field value is
not
empty, then the
principal.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.endpoint.zone
principal.resource.attribute.cloud.availability_zone
jsonPayload.endpoint.region
principal.location.name
jsonPayload.connection.dest_ip
target.ip
jsonPayload.connection.dest_port
target.port
jsonPayload.destination.geo_location.city
target.location.city
jsonPayload.destination.geo_location.country
target.location.country_or_region
jsonPayload.destination.geo_location.region
target.location.name
jsonPayload.destination.geo_location.continent
target.labels [destination_geo_location_continent]
(deprecated)
jsonPayload.destination.geo_location.continent
additional.fields [destination_geo_location_continent]
jsonPayload.destination.geo_location.asn
network.asn
jsonPayload.destination.instance.project_id
target.resource_ancestors.name
If the
jsonPayload.destination.instance.project_id
log field value is
not
empty, then the
//cloudresourcemanager.googleapis.com/projects/%{jsonPayload.destination.instance.project_id}
log field is mapped to the
target.resource_ancestors.name
UDM field.
target.resource_ancestors.resource_type
If the
jsonPayload.destination.instance.project_id
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
target.resource_ancestors.attribute.cloud.environment
If the
jsonPayload.destination.instance.project_id
log field value is
not
empty, then the
target.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.destination.instance.vm_name
target.hostname
jsonPayload.destination.instance.vm_name
target.asset.hostname
jsonPayload.destination.instance.vm_name
target.resource.name
target.resource.resource_type
If the
jsonPayload.destination.instance.vm_name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
target.resource.attribute.cloud.environment
If the
jsonPayload.destination.instance.vm_name
log field value is
not
empty, then the
target.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.destination.instance.zone
target.resource.attribute.cloud.availability_zone
jsonPayload.destination.instance.region
target.location.name
If the
jsonPayload.destination.geo_location.region
log field value is empty, then the
jsonPayload.destination.instance.region
log field is mapped to the
target.location.name
UDM field.
security_result.action
If the
jsonPayload.allocation_status
log field value is equal to
OK
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
jsonPayload.allocation_status
log field value is equal to
DROPPED
, then the
security_result.action
UDM field is set to
BLOCK
.
jsonPayload.allocation_status
security_result.action_details
labels
about.resource.attribute.labels
resource.labels.project_id
about.resource.attribute.labels [resource_project_id]
If the
resource.labels.project_id
log field value is
not
empty, then the
//cloudresourcemanager.googleapis.com/projects/%{resource.labels.project_id}
log field is mapped to the
about.resource.attribute.labels.resource_project_id
UDM field.
resource.labels.gateway_name
about.resource.attribute.labels [resource_gateway_name]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
