# Collect Wiz logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/wiz-io/  
**Scraped:** 2026-03-05T09:30:19.273587Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Wiz logs
Supported in:
Google secops
SIEM
This document explains how to ingest Wiz logs to Google Security Operations.
The parser transforms raw JSON formatted logs from Wiz into a Unified Data Model
(UDM). It first initializes default values for UDM fields, then parses the JSON
message, extracts relevant fields like user information, location, device
details, and security outcomes. Wiz is a cloud security platform that delivers
agentless, end-to-end visibility and risk prioritization across Google Cloud,
AWS, Azure, OCI, and Kubernetes environments.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to Wiz
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
and save the file in a secure
location.
Configure the integration in Wiz
Sign in to the
Wiz
web UI.
Go to the
Connect to Wiz
page.
Click
Google Cloud Chronicle
.
Select the
Scope
.
Enter your Google SecOps Customer ID.
Enter your Google SecOps instance Endpoint address.
Canada
:
https://northamerica-northeast2-malachiteingestion-pa.googleapis.com
Dammam
:
https://me-central2-malachiteingestion-pa.googleapis.com
Europe Multi-Region
:
https://europe-malachiteingestion-pa.googleapis.com
Frankfurt
:
https://europe-west3-malachiteingestion-pa.googleapis.com
London
:
https://europe-west2-malachiteingestion-pa.googleapis.com
Mumbai
:
https://asia-south1-malachiteingestion-pa.googleapis.com
Singapore
:
https://asia-southeast1-malachiteingestion-pa.googleapis.com
Sydney
:
https://australia-southeast1-malachiteingestion-pa.googleapis.com
Tel Aviv
:
https://me-west1-malachiteingestion-pa.googleapis.com
Tokyo
:
https://asia-northeast1-malachiteingestion-pa.googleapis.com
United States Multi-Region
:
https://malachiteingestion-pa.googleapis.com
Zurich
:
https://europe-west6-malachiteingestion-pa.googleapis.com
Upload the
Ingestion Authentication File
.
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
action
metadata.product_event_type
Direct mapping when eventType is empty.
action
principal.application
Direct mapping when action is
Report
and serviceAccount.name is not empty.
actionParameters.groups
security_result.detection_fields.value
The parser iterates through each group in actionParameters.groups and maps it to a separate detection_fields entry with key
service_account_group
.
actionParameters.input.patch.portalVisitHistory.dateTime
additional.fields.value.string_value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the dateTime field, mapping it to a separate additional.fields entry with key
dateTime {index}
.
actionParameters.input.patch.portalVisitHistory.id
principal.resource.attribute.labels.value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the id field, mapping it to a separate principal.resource.attribute.labels entry with key
id {index}
.
actionParameters.input.patch.portalVisitHistory.name
principal.resource.attribute.labels.value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the name field, mapping it to a separate principal.resource.attribute.labels entry with key
name {index}
.
actionParameters.input.patch.portalVisitHistory.resourceName
principal.resource.attribute.labels.value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the resourceName field, mapping it to a separate principal.resource.attribute.labels entry with key
resourceName {index}
.
actionParameters.input.patch.portalVisitHistory.resourceType
principal.resource.attribute.labels.value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the resourceType field, mapping it to a separate principal.resource.attribute.labels entry with key
resourceType {index}
.
actionParameters.input.patch.portalVisitHistory.ruleType
principal.resource.attribute.labels.value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the ruleType field, mapping it to a separate principal.resource.attribute.labels entry with key
ruleType {index}
.
actionParameters.input.patch.portalVisitHistory.type
additional.fields.value.string_value
The parser iterates through each item in actionParameters.input.patch.portalVisitHistory and extracts the type field, mapping it to a separate additional.fields entry with key
type {index}
.
actionParameters.name
target.user.user_display_name
Direct mapping when actionParameters.name is not empty.
actionParameters.products
security_result.detection_fields.value
The parser iterates through each product in actionParameters.products (excluding empty strings and
*
) and maps it to a separate detection_fields entry with key
service_account_product
.
actionParameters.role
target.user.attribute.roles.name
Direct mapping when actionParameters.role is not empty.
actionParameters.scopes
security_result.detection_fields.value
The parser iterates through each scope in actionParameters.scopes and maps it to a separate detection_fields entry with key
service_account_scope
.
actionParameters.selection
additional.fields.value.list_value.values.string_value
The parser iterates through each item in actionParameters.selection.preferences and maps it to a separate string_value entry within additional.fields.value.list_value.values.
actionParameters.userEmail
target.user.email_addresses
Extracted using a grok pattern and mapped when not empty.
actionParameters.userID
target.user.userid
Direct mapping when actionParameters.userID is not empty.
actor.displayName
target.user.user_display_name
Direct mapping when actor.displayName is not empty and not
unknown
.
actor.id
target.user.userid
Direct mapping when actor.id is not empty.
authenticationContext.authenticationProvider
security_result.detection_fields.value
Mapped to a detection_fields entry with key
authenticationProvider
when not empty.
authenticationContext.credentialProvider
security_result.detection_fields.value
Mapped to a detection_fields entry with key
credentialProvider
when not empty.
authenticationContext.credentialType
extensions.auth.mechanism
Used to derive the value for extensions.auth.mechanism based on specific values.
authenticationContext.externalSessionId
network.parent_session_id
Direct mapping when not empty and not
unknown
.
client.device
principal.asset.type
Used to derive the value for principal.asset.type based on specific values.
client.geographicalContext.city
principal.location.city
Direct mapping when not empty.
client.geographicalContext.country
principal.location.country_or_region
Direct mapping when not empty.
client.geographicalContext.geolocation.lat
principal.location.region_latitude
Direct mapping when not empty.
client.geographicalContext.geolocation.lon
principal.location.region_longitude
Direct mapping when not empty.
client.geographicalContext.postalCode
additional.fields.value.string_value
Mapped to an additional.fields entry with key
Postal code
when not empty.
client.geographicalContext.state
principal.location.state
Direct mapping when not empty.
client.ipAddress
principal.asset.ip
Merged with principal.ip and principal.asset.ip when not empty.
client.ipAddress
principal.ip
Merged with principal.ip and principal.asset.ip when not empty.
client.userAgent.browser
target.resource.attribute.labels.value
Mapped to a target.resource.attribute.labels entry with key
Browser
when not empty.
client.userAgent.os
principal.platform
Used to derive the value for principal.platform based on specific values.
client.userAgent.rawUserAgent
network.http.user_agent
Direct mapping when not empty.
debugContext.debugData.behaviors
security_result.description
Direct mapping when not empty.
debugContext.debugData.deviceFingerprint
target.asset.asset_id
Mapped to target.asset.asset_id with prefix
device_finger_print:
when not empty.
debugContext.debugData.dtHash
security_result.detection_fields.value
Mapped to a detection_fields entry with key
dtHash
when not empty.
debugContext.debugData.factor
security_result.detection_fields.value
Mapped to a detection_fields entry with key
factor
when not empty.
debugContext.debugData.promptingPolicyTypes
security_result.detection_fields.value
Mapped to a detection_fields entry with key
promptingPolicyTypes
when not empty.
debugContext.debugData.requestUri
extensions.auth.auth_details
Direct mapping when not empty.
eventType
metadata.event_type
Used to derive the value for metadata.event_type based on specific values.
eventType
metadata.product_event_type
Direct mapping when not empty.
outcome.reason
security_result.category_details
Direct mapping when not empty.
outcome.result
security_result.action
Mapped to security_result.action after normalization based on specific values.
requestId
metadata.product_log_id
Direct mapping when not empty.
serviceAccount.name
principal.application
Direct mapping when action is
Report
and serviceAccount.name is not empty.
sourceIP
principal.asset.ip
Extracted using a grok pattern and merged with principal.ip and principal.asset.ip when not empty and valid.
sourceIP
principal.ip
Extracted using a grok pattern and merged with principal.ip and principal.asset.ip when not empty and valid.
status
security_result.summary
Direct mapping when not empty.
timestamp
metadata.event_timestamp
Converted to timestamp format and mapped when not empty.
user.id
target.user.userid
Direct mapping when actionParameters.userID is empty and user.id is not empty.
user.name
target.user.user_display_name
Direct mapping when actionParameters.name is empty and user.name is not empty.
userAgent
network.http.user_agent
Direct mapping when client.userAgent.rawUserAgent is empty and userAgent is not empty.
extensions.auth.type
Set to
AUTHTYPE_UNSPECIFIED
when has_user is true and action is
Login
.
metadata.product_name
Set to
WIZ_IO
.
metadata.vendor_name
Set to
WIZ_IO
.
network.http.parsed_user_agent
Derived from user_agent_value by converting it to parseduseragent.
security_result.severity
Derived from severity based on specific values, defaulting to
LOW
.
Need more help?
Get answers from Community members and Google SecOps professionals.
