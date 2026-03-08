# Collect Google Cloud IAM context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/collect-gcp-iam-context-logs/  
**Scraped:** 2026-03-05T09:48:02.526179Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud IAM context logs
This document describes how fields of Google Cloud Identity and Access Management context logs map to Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_IAM_CONTEXT
ingestion label.
For information about other context parsers that Google SecOps supports, see
Google SecOps context parsers
.
Supported IAM log formats
The IAM parser supports logs in JSON format.
Supported IAM sample logs
JSON:
none
{  
  "name": "//iam.googleapis.com/projects/project_id/serviceAccounts/service_account_id",
  "asset_type": "iam.googleapis.com/ServiceAccount",
  "resource": {
    "version": "v1",
    "discovery_document_uri": "https://dummy.domain.com/$discovery/rest",
    "discovery_name": "ServiceAccount",
    "parent": "//cloudresourcemanager.googleapis.com/projects/project_number",
    "data": {
      "displayName": "Compute Engine default service account",
      "email": "dummy-compute@developer.domain.com",
      "name": "projects/project_id/serviceAccounts/project_number-compute@developer.gserviceaccount.com",
      "oauth2ClientId": "service_account_id",
      "projectId": "project_id",
      "uniqueId": "service_account_id"
    }
  },
  "AccessContextPolicy": null,
  "ancestors": [
    "projects/project_number",
    "folders/folders_id_1",
    "folders/folders_id_2",
    "folders/folders_id_3",
    "organizations/organizations_id"
  ]
}
Field mapping reference
This section explains how the Google SecOps parser maps Google Cloud Identity and Access Management context fields to Google SecOps Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
resource.data.groupTitle
entity.group.attribute.labels[group_title]
resource.data.groupName
entity.group.group_display_name
resource.data.projectId
entity.resource_ancestors.product_object_id
resource.data.name
entity.resource_ancestors.product_object_id
If the
assetType
log field value matches the regular expression pattern
Role
, then
Grok extracts
prnt_id
from the log field
resource.data.name
and maps it to the
entity.resource_ancestors.product_object_id
UDM field.
Else, if the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then
Grok extracts
project_id
from the log field
resource.data.name
and maps it to the
entity.resource_ancestors.product_object_id
UDM field.
entity.resource_ancestors.resource_subtype
If the
assetType
log field value matches the regular expression pattern
Role
and the
resource.data.name
log field value matches the regular expression pattern
organizations
, then the
entity.resource_ancestors.resource_subtype
UDM field is set to
organizations
.
Else, if the
assetType
log field value matches the regular expression pattern
Role
and the
resource.data.name
log field value matches the regular expression pattern
projects
, then the
entity.resource_ancestors.resource_subtype
UDM field is set to
projects
.
Else, if the
assetType
log field value matches the regular expression pattern
ServiceAccount
, then the
entity.resource_ancestors.resource_type
UDM field is set to
projects
.
entity.resource_ancestors.resource_type
If the
assetType
log field value matches the regular expression pattern
Role
and the
resource.data.name
log field value matches the regular expression pattern
organizations
, then the
entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
assetType
log field value matches the regular expression pattern
Role
and the
resource.data.name
log field value matches the regular expression pattern
projects
, then the
entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
assetType
log field value matches the regular expression pattern
ServiceAccount
, then the
entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
entity.resource.attribute.cloud.environment
The
entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.data.deleted
entity.resource.attribute.labels[deleted]
resource.data.disabled
entity.resource.attribute.labels[disabled]
resource.discoveryDocumentUri
entity.resource.attribute.labels[discovery_document_uri]
resource.discoveryName
entity.resource.attribute.labels[discovery_name]
resource.data.etag
entity.resource.attribute.labels[etag]
resource.data.name
entity.resource.attribute.labels[resource_name]
resource.data.stage
entity.resource.attribute.labels[stage]
resource.data.title
entity.resource.attribute.labels[title]
resource.data.includedPermissions
entity.resource.attribute.permissions.name
name
entity.resource.name
resource.data.name
entity.resource.product_object_id
If the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then
Grok extracts
account_id
from the log field
resource.data.name
and maps it to the
entity.resource.product_object_id
UDM field.
resource.data.name
entity.resource.product_object_id
If the
assetType
log field value matches the regular expression pattern
Role
, then
Grok extracts
res_name
from the log field
resource.data.name
and maps it to the
entity.resource.product_object_id
UDM field.
assetType
entity.resource.resource_subtype
entity.resource.resource_type
If the
assetType
log field value matches the regular expression pattern
Role
, then the
entity.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
Else, if the
assetType
log field value matches the regular expression pattern
ServiceAccount
, then the
entity.resource.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
entity.user.attribute.cloud.environment
If the
resource.discoveryName
log field value is equal to
ServiceAccount
, then the
entity.resource.resource_type
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.data.email
entity.user.email_addresses
resource.data.email
entity.user.userid
resource.data.oauth2ClientId
entity.user.attribute.labels[oauth2_client_id]
resource.data.displayName
entity.user.user_display_name
resource.data.uniqueId
entity.user.product_object_id
resource.data.description
metadata.description
metadata.entity_type
If the
assetType
log field value matches the regular expression pattern
Role
, then the
metadata.entity_type
UDM field is set to
RESOURCE
.
Else, if the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then the
metadata.entity_type
UDM field is set to
RESOURCE
.
Else, if the
assetType
log field value matches the regular expression pattern
ServiceAccount
, then the
metadata.entity_type
UDM field is set to
USER
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Identity and Access Management
.
resource.version
metadata.product_version
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google
.
relations.direction
The
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
relations.entity_type
The
relations.entity_type
UDM field is set to
RESOURCE
.
resource.data.validAfterTime
relations.entity.resource.attribute.creation_time
resource.data.keyAlgorithm
relations.entity.resource.attribute.labels[key_algorithm]
resource.data.keyOrigin
relations.entity.resource.attribute.labels[key_origin]
resource.data.keyType
relations.entity.resource.attribute.labels[key_type]
resource.data.privateKeyData
relations.entity.resource.attribute.labels[private_key_data]
resource.data.privateKeyType
relations.entity.resource.attribute.labels[private_key_type]
resource.data.publicKeyData
relations.entity.resource.attribute.labels[public_key_data]
resource.data.validBeforeTime
relations.entity.resource.attribute.labels[valid_before_time]
ancestors
relations.entity.resource.name
resource.parent
relations.entity.resource.name
resource.parent
relations.entity.resource.product_object_id
Grok extracts
id
from the log field
resource.parent
and maps it to the
relations.entity.resource.product_object_id
UDM field.
resource.data.name
relations.entity.resource.product_object_id
If the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then
Grok extracts
key
from the log field
resource.data.name
and maps it to the
relations.entity.resource.product_object_id
UDM field.
ancestors
relations.entity.resource.product_object_id
Grok extracts
id
from the log field
ancestors
and maps it to the
relations.entity.resource.product_object_id
UDM field.
ancestors
relations.entity.resource.resource_subtype
Grok extracts
subtype
from the log field
ancestors
and maps it to the
relations.entity.resource.resource_subtype
UDM field.
relations.entity.resource.resource_subtype
If the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then the
relations.entity.resource.resource_subtype
UDM field is set to
keys
.
If the
resource.parent
log field value matches the regular expression pattern
organizations
, then the
relations.entity.resource.resource_subtype
UDM field is set to
organizations
.
Else, if the
resource.parent
log field value matches the regular expression pattern
projects
, then the
relations.entity.resource.resource_subtype
UDM field is set to
projects
.
Else, if the
resource.parent
log field value matches the regular expression pattern
folders
, then the
relations.entity.resource.resource_subtype
UDM field is set to
folders
.
relations.entity.resource.resource_type
If the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then the
relations.entity.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
Else, if the
resource.parent
log field value matches the regular expression pattern
organizations
or the
ancestors
log field value matches the regular expression pattern
organization
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
resource.parent
log field value matches the regular expression pattern
projects
or the
ancestors
log field value matches the regular expression pattern
project
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
resource.parent
log field value matches the regular expression pattern
folders
or the
ancestors
log field value matches the regular expression pattern
folder
, then the
relations.entity.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
relations.relationship
If the
assetType
log field value matches the regular expression pattern
ServiceAccountKey
, then the
relations.relationship
UDM field is set to
OWNS
.
Else, the
relations.relationship
UDM field is set to
MEMBER
.
