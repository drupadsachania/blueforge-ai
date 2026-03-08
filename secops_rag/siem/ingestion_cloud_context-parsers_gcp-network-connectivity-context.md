# Collect Network Connectivity Center context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/gcp-network-connectivity-context/  
**Scraped:** 2026-03-05T09:17:51.668096Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Network Connectivity Center context logs
This document describes how fields of Network Connectivity Center context logs map to Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
GCP_NETWORK_CONNECTIVITY_CONTEXT
ingestion label.
For information about other context parsers that Google SecOps supports, see
Google SecOps context parsers
.
Supported Network Connectivity Center log formats
The Network Connectivity Center parser supports logs in JSON format.
Supported Network Connectivity Center sample logs
JSON:
{
  "name": "//networkconnectivity.googleapis.com/projects/chronicle-dpa-test/locations/global/hubs/test-hub",
  "assetType": "networkconnectivity.googleapis.com/Hub",
  "resource": {
    "version": "v1",
    "discoveryDocumentUri": "https://networkconnectivity.googleapis.com/$discovery/rest",
    "discoveryName": "Hub",
    "parent": "//cloudresourcemanager.googleapis.com/projects/582699623097",
    "data": {
      "createTime": "2023-04-11T05:55:13.736577927Z",
      "name": "projects/chronicle-dpa-test/locations/global/hubs/test-hub",
      "state": "ACTIVE",
      "uniqueId": "3d6022bc-9306-4f4d-9d79-07b86836dee5",
      "updateTime": "2023-04-11T05:55:16.814218398Z"
    }
  },
  "ancestors": [
    "projects/582699623097",
    "organizations/383339652788"
  ]
}
Field mapping reference
The following table explains how the Google SecOps parser maps Network Connectivity Center context logs fields to Google SecOps Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
entity.resource.attribute.cloud.environment
The
entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
entity.resource_ancestors.attribute.cloud.environment
If the
resource.data.network
log field value is
not
empty, then the
entity.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
entity.resource_ancestors.resource_type
If the
resource.data.network
log field value is
not
empty, then the
entity.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
resource.data.createTime
entity.resource.attribute.creation_time
resource.discoveryDocumentUri
entity.resource.attribute.labels [discovery_document]
resource.discoveryName
entity.resource.attribute.labels [discovery_name]
resource.data.ipCidrRange
entity.resource.attribute.labels [ipcidr
range]
resource.data.overlaps
entity.resource.attribute.labels [overlaps]
If the
resource.data.overlaps
log field value is
not
empty, then the
resource.data.overlaps
log field is mapped to the
entity.resource.attribute.labels.overlaps%{index}
UDM field.
resource.data.peering
entity.resource.attribute.labels [peering]
resource.data.prefixLength
entity.resource.attribute.labels [prefix_length]
resource.data.description
metadata.description
metadata.product_entity_id
The
obj_id
is extracted from the
Resource.data.name
log field using Grok pattern, and the the
obj_id
log field value is
not
empty and the
resource.data.uniqueId
log field value is empty, then the
obj_id
log field is mapped to the
entity.resource.product_object_id
UDM field.
metadata.entity_type
The
metadata.entity_type
UDM field is set to
RESOURCE
.
resource.data.locationId
entity.location.name
resource.data.name
entity.resource.attribute.labels [resource_name]
resource.data.state
entity.resource.attribute.labels [resource_state]
resource.data.targetCidrRange
entity.resource.attribute.labels [target_cidr_range]
If the
resource.data.targetCidrRange
log field value is
not
empty, then the
resource.data.targetCidrRange
log field is mapped to the
entity.resource.attribute.labels.target_cidr
range
%{index}
UDM field.
resource.data.usage
entity.resource.attribute.labels [usage]
resource.data.updateTime
entity.resource.attribute.last_update_time
name
entity.resource.name
resource.data.network
entity.resource_ancestors.name
resource.data.uniqueId
entity.resource.product_object_id
assetType
entity.resource.resource_subtype
entity.resource.resource_type
The
entity.resource.resource_type
UDM field is set to
DEVICE
.
resource.version
metadata.product_version
relations.direction
If the
ancestors
log field value is
not
empty or the
resource.data.hub
log field value is
not
empty or the
resource.data.users
log field value is
not
empty or the
resource.data.routingVpcs.uri
log field value is
not
empty or the
resource.data.linkedVpnTunnels.uris
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.uris
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.virtualMachine
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.ipAddress
log field value is
not
empty, then the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
relations.entity_type
If the
ancestors
log field value is
not
empty or the
resource.data.hub
log field value is
not
empty or the
resource.data.users
log field value is
not
empty or the
resource.data.routingVpcs.uri
log field value is
not
empty or the
resource.data.linkedVpnTunnels.uris
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.uris
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.virtualMachine
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.ipAddress
log field value is
not
empty, then the
relations.entity_type
UDM field is set to
RESOURCE
.
resource.data.linkedRouterApplianceInstances.instances.ipAddress
relations.entity.ip
relations.entity.resource_ancestors.attribute.cloud.environment
If the
resource.parent
log field value not contains the
ancestors
log field value or the
resource.data.linkedVpnTunnels.vpcNetwork
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.vpcNetwork
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.vpcNetwork
log field value is
not
empty, then the
relations.entity.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
ancestors
relations.entity.resource_ancestors.name
If the
resource.parent
log field value not contains the
ancestors
log field value or the
resource.data.linkedVpnTunnels.vpcNetwork
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.vpcNetwork
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.vpcNetwork
log field value is
not
empty, then the
ancestors
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.linkedVpnTunnels.vpcNetwork
relations.entity.resource_ancestors.name
resource.data.linkedInterconnectAttachments.vpcNetwork
relations.entity.resource_ancestors.name
resource.data.linkedRouterApplianceInstances.vpcNetwork
relations.entity.resource_ancestors.name
relations.entity.resource_ancestors.resource_type
If the
resource.parent
log field value not contains the
ancestors
log field value or the
resource.data.linkedVpnTunnels.vpcNetwork
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.vpcNetwork
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.vpcNetwork
log field value is
not
empty, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
relations.entity.resource_ancestors.resource_subtype
The
res_type
is extracted from the
ancestors
log field using a Grok pattern, and if the
res_type
log field value is
not
empty
and the
resource.parent
log field value not contains the
ancestors
log field value, then the
res_type
log field is mapped to the
relations.entity.resource_ancestors.resource_subtype
UDM field.
relations.entity.resource.resource_subtype
The
res_type
is extracted from the
ancestors
log field using a Grok pattern, and if the
res_type
log field value is
not
empty
and the
resource.parent
log field value contains the
ancestors
log field value, then the
res_type
log field is mapped to the
relations.entity.resource_ancestors.resource_subtype
UDM field.
if the
resource.data.hub
log field value is
not
empty, then the
relations.entity.resource.resource_subtype
UDM field is set to
HUB
.
relations.entity.resource.attribute.cloud.environment
If the
resource.parent
log field value contains the
ancestors
log field value or the
resource.data.hub
log field value is
not
empty or the
resource.data.users
log field value is
not
empty or the
resource.data.routingVpcs.uri
log field value is
not
empty or the
resource.data.linkedVpnTunnels.uris
log field value is
not
empty or the
resource.data.linkedVpnTunnels.uris
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.uris
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.virtualMachine
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.ipAddress
log field value is
not
empty, then the
relations.entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.data.linkedVpnTunnels.siteToSiteDataTransfer
relations.entity.resource.attribute.labels [vpntunnel_sitetosite_data_transfer]
If the
resource.data.linkedVpnTunnels.siteToSiteDataTransfer
log field value is
not
empty, then the
resource.data.linkedVpnTunnels.siteToSiteDataTransfer
log field is mapped to the
relations.entity.resource.attribute.labels.value
UDM field.
resource.data.linkedInterconnectAttachments.siteToSiteDataTransfer
relations.entity.resource.attribute.labels [attachments_sitetosite_data_transfer]
If the
resource.data.linkedInterconnectAttachments.siteToSiteDataTransfer
log field value is
not
empty, then the
resource.data.linkedInterconnectAttachments.siteToSiteDataTransfer
log field is mapped to the
relations.entity.resource.attribute.labels.value
UDM field.
resource.data.linkedRouterApplianceInstances.siteToSiteDataTransfer
relations.entity.resource.attribute.labels [routerapplliances_sitetosite_data_transfer]
If the
resource.data.linkedRouterApplianceInstances.siteToSiteDataTransfer
log field value is
not
empty, then the
resource.data.linkedRouterApplianceInstances.siteToSiteDataTransfer
log field is mapped to the
relations.entity.resource.attribute.labels.value
UDM field.
resource.data.hub
relations.entity.resource.name
If the
resource.parent
log field value contains the
ancestors
log field value, then the
resource.parent
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.routingVpcs.uri
relations.entity.resource.name
resource.data.linkedVpnTunnels.uris
relations.entity.resource.name
resource.data.linkedInterconnectAttachments.uris
relations.entity.resource.name
resource.data.linkedRouterApplianceInstances.instances.virtualMachine
relations.entity.resource.name
resource.data.users
relations.entity.resource.name
resource.parent
relations.entity.resource.name
relations.entity.resource.resource_type
If the
resource.data.hub
log field value is
not
empty or the
resource.data.users
log field value is
not
empty or the
resource.data.linkedVpnTunnels.uris
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.uris
log field value is
not
empty, then the
relations.entity.resource.resource_type
UDM field is set to
DEVICE
.
If the
resource.parent
log field value contains the
ancestors
log field value, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
If the
resource.data.routingVpcs.uri
log field value is
not
empty, then the
relations.entity.resource.resource_type
UDM field is set to
VPC_NETWORK
.
If the
resource.data.linkedRouterApplianceInstances.instances.virtualMachine
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.ipAddress
log field value is
not
empty, then the
relations.entity.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
relations.relationship
If the
ancestors
log field value is
not
empty or the
resource.data.hub
log field value is
not
empty or the
resource.data.users
log field value is
not
empty or the
resource.data.routingVpcs.uri
log field value is
not
empty or the
resource.data.linkedVpnTunnels.uris
log field value is
not
empty or the
resource.data.linkedInterconnectAttachments.uris
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.virtualMachine
log field value is
not
empty or the
resource.data.linkedRouterApplianceInstances.instances.ipAddress
log field value is
not
empty, then the
relations.relationship
UDM field is set to
MEMBER
.
resource.data.routingVpcs.requiredForNewSiteToSiteDataTransferSpokes
relations.entity.resource.attribute.labels [required_for_new_site_to_site_data_transfer_spokes]
