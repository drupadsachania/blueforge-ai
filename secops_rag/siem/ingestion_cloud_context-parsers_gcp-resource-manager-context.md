# Collect Resource Manager context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/gcp-resource-manager-context/  
**Scraped:** 2026-03-05T09:16:56.665930Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Resource Manager context logs
This document describes how fields of Resource Manager context logs map to
Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_RESOURCE_MANAGER_CONTEXT
ingestion label.
For information about other context parsers that Google Security Operations supports, see
Google Security Operations context parsers
.
Supported Resource Manager context logs log formats
The Resource Manager context logs parser supports logs in JSON format.
Supported Resource Manager context logs sample logs
JSON:
{
  "name": "//cloudresourcemanager.googleapis.com/folders/722926615140",
  "assetType": "cloudresourcemanager.googleapis.com/Folder",
  "resource": {
    "version": "v2",
    "discoveryDocumentUri": "https://cloudresourcemanager.googleapis.com/$discovery/rest?version=v2",
    "discoveryName": "Folder",
    "parent": "//cloudresourcemanager.googleapis.com/organizations/299419016487",
    "data": {
      "createTime": "2022-06-08T22:40:08.491Z",
      "displayName": "OrgChangeSourceFolder",
      "lifecycleState": "ACTIVE",
      "name": "folders/dummy",
      "parent": "organizations/dummy"
    }
  },
  "ancestors": [
    "folders/722926615140",
    "organizations/299419016487"
  ]
}
Field mapping reference
The following table explains how the Google Security Operations parser maps Resource Manager context logs fields to Google Security Operations Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
resource.data.tagValueNamespacedName
entity.namespace
resource.data.namespacedName
entity.namespace
resource.data.createTime
entity.resource.attribute.creation_time
resource.data.updateTime
entity.resource.attribute.last_update_time
name
entity.resource.name
resource.data.name
entity.resource.name
resource.data.displayName
entity.resource.product_object_id
resource.data.projectId
entity.resource.product_object_id
entity.resource.resource_type
If the
assetType
matches the regular expression pattern
Project
, then the
entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
assetType
matches the regular expression pattern
Organizations
, then the
entity.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
assetType
matches the regular expression pattern
Folder
, then the
entity.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
Else, the
entity.resource.resource_type
UDM field is set to
SETTING
.
assetType
entity.resource.resource_subtype
resource.data.owner.directoryCustomerId
entity.user.userid
resource.data.directoryCustomerId
entity.user.userid
resource.data.description
metadata.description
metadata.entity_type
The
metadata.entity_type
UDM field is set to
RESOURCE
.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP Resource Manager
.
resource.version
metadata.product_version
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
relations.entity.resource_ancestors.attribute.cloud.environment
If the
ancestors
log field value is
not
empty or the
resource.parent
log field value is
not
empty or the
resource.data.parent.type
log field value is
not
empty, then the
relations.entity.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
ancestors
relations.entity.resource_ancestors.name
resource.data.parent.id
relations.entity.resource_ancestors.product_object_id
relations.entity.resource_ancestors.resource_type
If the
ancestors
matches the regular expression pattern
organizations
, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
ancestors
matches the regular expression pattern
projects
, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
ancestors
matches the regular expression pattern
folder
, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
STORAGE_OBJECT
.
resource.data.parent.type
relations.entity.resource_ancestors.resource_type
If the
resource.data.parent.type
matches the regular expression pattern
project
, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
resource.data.parent.type
matches the regular expression pattern
folder
, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
STORAGE_OBJECT
.
Else, if the
resource.data.parent.type
matches the regular expression pattern
organization
, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
resource.data.parent.type
log field value is
not
empty, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
SETTING
.
relations.entity.resource_ancestors.resource_subtype
If the
ancestors
matches the regular expression pattern
organizations
, then the
relations.entity.resource_ancestors.resource_subtype
UDM field is set to
organizations
.
Else, if the
ancestors
matches the regular expression pattern
projects
, then the
relations.entity.resource_ancestors.resource_subtype
UDM field is set to
projects
.
Else, if the
ancestors
matches the regular expression pattern
folder
, then the
relations.entity.resource_ancestors.resource_subtype
UDM field is set to
folders
.
resource.data.parent.type
relations.entity.resource_ancestors.resource_subtype
entity.resource.attribute.cloud.environment
The
entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
relations.entity_type
The
relations.entity_type
UDM field is set to
RESOURCE
.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
.
relations.direction
The
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
resource.parent
relations.entity.resource.name
resource.data.parent
relations.entity.resource.name
resource.data.labels
entity.resource.attribute.labels.key/value
resource.data.purposeData
entity.resource.attribute.labels.key/value
resource.discoveryDocumentUri
entity.resource.attribute.labels[discovery_document]
resource.discoveryName
entity.resource.attribute.labels[discovery_name]
resource.data.purpose
entity.resource.attribute.labels[purpose]
resource.data.deleteTime
entity.resource.attribute.last_update_time
resource.data.etag
entity.resource.attribute.labels[resource_etag]
resource.data.projectNumber
entity.resource.attribute.labels[resource_project_number]
resource.data.lifecycleState
entity.resource.attribute.labels[resource_state]
resource.data.state
entity.resource.attribute.labels[resource_state]
resource.data.tagValue
entity.resource.attribute.labels[resource_tag_value]
resource.data.shortName
entity.resource.attribute.labels[short_name]
Need more help?
Get answers from Community members and Google SecOps professionals.
