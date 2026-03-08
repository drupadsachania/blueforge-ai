# Collect Anomali ThreatStream IOC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/anomali-ioc/  
**Scraped:** 2026-03-05T09:49:43.671562Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Anomali ThreatStream IOC logs
Supported in:
Google secops
SIEM
This document explains how to ingest Anomali ThreatStream IOC logs to Google Security Operations using an API. The parser transforms the IOC data from either JSON or CEF format into a unified data model (UDM). The code first attempts to parse the input as JSON, and if unsuccessful, checks for the "CEF:" prefix to process it as a CEF message, extracting IOC attributes and mapping them to UDM fields.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to an
Anomali ThreatStream
enterprise tenant
Create a dedicated API user
Sign in to
ThreatStream
. Switch to the
Classic UI
if you are on Anomali Enterprise.
Go to
Administration
>
Users
.
Click
+ Add User
(or select an existing service account).
Complete the following details:
Email
: Service account email address (for example,
anomali_ioc_secops@example.com
).
Auth Source
: Select
Standard
.
User Type
: Select
API User
.
Role
: Select
Read Only
(sufficient to
list
indicators).
Click
Save
.
An activation email is sent to the new account; complete the activation.
Generate API key
Sign in to the
ThreatStream
as the
API user
.
Go to
profile avatar
>
My API Keys
.
Click
Generate New Key
.
Enter a
Description
(for example,
Google SecOps export
).
Click
Save
.
Copy and save the key value displayed under
Key
in a secure location. The 
key value is not displayed again.
Recommended: Allowlist collector IP
Go to
Administration
>
Organization Settings
.
Select the
IP Allowlist
tab.
Click
+ Add
.
Enter your Google SecOps tenant address and click
Save
.
Set up feeds
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed (for example,
Anomali TS IOC
).
Select
Third Party API
as the
Source type
.
Select the
Anomali
log type.
Click
Next
.
Specify values for the following input parameters:
Username
: Enter the newly created API user.
Secret
: Enter the generated
API Key
copied earlier.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label applied to the events from this feed.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log field
UDM mapping
Logic
obj.asn
entity.administrative_domain
The asn field in the raw log is mapped to the administrative_domain field in the UDM entity object.
obj.confidence
ioc.confidence_score
The confidence field in the raw log is mapped to the confidence_score field in the UDM ioc object.
obj.country
entity.location.country_or_region
The country field in the raw log is mapped to the country_or_region field in the UDM entity object.
obj.created_ts
entity.metadata.creation_timestamp
The created_ts field in the raw log is mapped to the creation_timestamp field in the UDM entity object.
obj.created_ts
ioc.active_timerange.start
The created_ts field in the raw log is mapped to the start field in the UDM ioc object.
obj.created_ts
entity.metadata.threat.first_discovered_time
The created_ts field in the raw log is mapped to the first_discovered_time field in the UDM threat object.
obj.expiration_ts
entity.metadata.interval.end_time
The expiration_ts field in the raw log is mapped to the end_time field in the UDM entity object.
obj.expiration_ts
ioc.active_timerange.end
The expiration_ts field in the raw log is mapped to the end field in the UDM ioc object.
obj.id
entity.metadata.product_entity_id
The id field in the raw log is mapped to the product_entity_id field in the UDM entity object.
obj.ip
entity.entity.ip
The ip field in the raw log is merged to the ip field in the UDM entity object.
obj.ip
ioc.ip_and_ports.ip_address
The ip field in the raw log is mapped to the ip_address field in the UDM ioc object.
obj.itype
ioc.categorization
The itype field in the raw log is mapped to the categorization field in the UDM ioc object.
obj.itype
entity.metadata.threat.category_details
The itype field in the raw log is merged to the category_details field in the UDM threat object.
obj.latitude
entity.entity.location.region_latitude
The latitude field in the raw log is mapped to the region_latitude field in the UDM entity object.
obj.longitude
entity.entity.location.region_longitude
The longitude field in the raw log is mapped to the region_longitude field in the UDM entity object.
obj.meta.detail2
ioc.description
The detail2 field in the raw log is mapped to the description field in the UDM ioc object.
obj.meta.detail2
entity.metadata.threat.description
The detail2 field in the raw log is mapped to the description field in the UDM threat object.
obj.meta.severity
ioc.raw_severity
The severity field in the raw log is mapped to the raw_severity field in the UDM ioc object.
obj.meta.severity
entity.metadata.threat.severity
The severity field in the raw log is mapped to the severity field in the UDM threat object. If the severity is "very-high", it is mapped to "CRITICAL".
obj.meta.severity
entity.metadata.threat.severity_details
The severity field in the raw log is mapped to the severity_details field in the UDM threat object.
obj.modified_ts
entity.metadata.threat.last_updated_time
The modified_ts field in the raw log is mapped to the last_updated_time field in the UDM threat object.
obj.org
entity.entity.administrative_domain
The org field in the raw log is mapped to the administrative_domain field in the UDM entity object.
obj.resource_uri
entity.metadata.threat.url_back_to_product
The resource_uri field in the raw log is mapped to the url_back_to_product field in the UDM threat object.
obj.retina_confidence
entity.metadata.threat.confidence_score
The retina_confidence field in the raw log is mapped to the confidence_score field in the UDM threat object.
obj.source
ioc.feed_name
The source field in the raw log is mapped to the feed_name field in the UDM ioc object.
obj.source
entity.metadata.threat.threat_name
The source field in the raw log is mapped to the threat_name field in the UDM threat object.
obj.status
entity.metadata.threat.threat_status
The status field in the raw log is mapped to the threat_status field in the UDM threat object.
obj.subtype
entity.entity.file.sha1
The subtype field in the raw log is mapped to the sha1 field in the UDM entity object if the subtype is "SHA1".
obj.subtype
entity.entity.file.sha256
The subtype field in the raw log is mapped to the sha256 field in the UDM entity object if the subtype is "SHA256".
obj.tags
entity.metadata.source_labels
The tags field in the raw log is mapped to the source_labels field in the UDM entity object.
obj.tags.id
entity.metadata.source_labels
The id field in the tags array of the raw log is mapped to the source_labels field in the UDM entity object.
obj.tags.name
entity.metadata.source_labels
The name field in the tags array of the raw log is mapped to the source_labels field in the UDM entity object.
obj.threatscore
entity.metadata.threat.risk_score
The threatscore field in the raw log is mapped to the risk_score field in the UDM threat object.
obj.threat_type
entity.metadata.threat.detection_fields
The threat_type field in the raw log is mapped to the detection_fields field in the UDM threat object.
obj.type
entity.entity.file.md5
The type field in the raw log is mapped to the md5 field in the UDM entity object if the type is "md5".
obj.type
entity.entity.hostname
The type field in the raw log is mapped to the hostname field in the UDM entity object if the type is "domain".
obj.type
entity.entity.ip
The type field in the raw log is merged to the ip field in the UDM entity object if the type is "ip" or "ipv6".
obj.type
entity.entity.url
The type field in the raw log is mapped to the url field in the UDM entity object if the type is "url" or "string".
obj.type
entity.entity.user.email_addresses
The type field in the raw log is merged to the email_addresses field in the UDM entity object if the type is "email".
obj.type
entity.metadata.entity_type
The type field in the raw log is mapped to the entity_type field in the UDM entity object. If the type is "ip" or "ipv6", it is mapped to "IP_ADDRESS". If the type is "domain", it is mapped to "DOMAIN_NAME". If the type is "md5" or the itype field contains "md5", it is mapped to "FILE". If the type is "url" or "string", it is mapped to "URL". If the type is "email", it is mapped to "USER". Otherwise, it is mapped to "UNKNOWN_ENTITYTYPE".
obj.uuid
entity.additional.fields
The uuid field in the raw log is mapped to the fields field in the UDM entity object.
obj.value
entity.entity.ip
The value field in the raw log is merged to the ip field in the UDM entity object if the type field is "ip" and the ip field is empty.
obj.value
entity.entity.ip
The value field in the raw log is merged to the ip field in the UDM entity object if the ip_field_not_exists field is true and the value field is an IP address.
obj.value
entity.entity.url
The value field in the raw log is mapped to the url field in the UDM entity object if the type field is "url" or "string".
obj.value
ioc.domain_and_ports.domain
The value field in the raw log is mapped to the domain field in the UDM ioc object if the type field is not "ip".
obj.value
ioc.ip_and_ports.ip_address
The value field in the raw log is mapped to the ip_address field in the UDM ioc object if the type field is "ip" and the ip field is empty.
cn1
ioc.confidence_score
The cn1 field in the raw log is mapped to the confidence_score field in the UDM ioc object.
cn2
entity.metadata.threat.rule_id
The cn2 field in the raw log is mapped to the rule_id field in the UDM threat object.
cs1
ioc.raw_severity
The cs1 field in the raw log is mapped to the raw_severity field in the UDM ioc object.
cs2
entity.metadata.threat.threat_name
The cs2 field in the raw log is mapped to the threat_name field in the UDM threat object.
cs3
entity.metadata.threat.threat_status
The cs3 field in the raw log is mapped to the threat_status field in the UDM threat object. If the cs3 field is "active", it is mapped to "ACTIVE". If the cs3 field is "cleared", it is mapped to "CLEARED". If the cs3 field is "falsePositive" or "falsepos", it is mapped to "FALSE_POSITIVE". If the cs3 field is "threat_status_unspecified", it is mapped to "THREAT_STATUS_UNSPECIFIED".
cs4
entity.entity.administrative_domain
The cs4 field in the raw log is mapped to the administrative_domain field in the UDM entity object.
cs5
ioc.description
The cs5 field in the raw log is mapped to the description field in the UDM ioc object.
cs5
entity.metadata.threat.detection_fields
The cs5 field in the raw log is mapped to the detection_fields field in the UDM threat object.
cs5
entity.metadata.threat.description
The cs5 field in the raw log is mapped to the description field in the UDM threat object.
cs6
entity.metadata.threat.category_details
The cs6 field in the raw log is merged to the category_details field in the UDM threat object.
device_product
entity.metadata.product_name
The device_product field in the raw log is mapped to the product_name field in the UDM entity object.
device_vendor
entity.metadata.vendor_name
The device_vendor field in the raw log is mapped to the vendor_name field in the UDM entity object.
device_version
entity.metadata.product_version
The device_version field in the raw log is mapped to the product_version field in the UDM entity object.
msg
entity.metadata.threat.summary
The msg field in the raw log is mapped to the summary field in the UDM threat object.
shost
entity.entity.hostname
The shost field in the raw log is mapped to the hostname field in the UDM entity object.
shost
entity.entity.url
The shost field in the raw log is mapped to the url field in the UDM entity object.
shost
ioc.domain_and_ports.domain
The shost field in the raw log is mapped to the domain field in the UDM ioc object.
src
entity.entity.ip
The src field in the raw log is merged to the ip field in the UDM entity object.
src
ioc.ip_and_ports.ip_address
The src field in the raw log is mapped to the ip_address field in the UDM ioc object.
entity.metadata.threat.confidence
HIGH_CONFIDENCE
The confidence field in the UDM threat object is set to "HIGH_CONFIDENCE" if the confidence_score field is greater than or equal to 75.
entity.metadata.threat.confidence
LOW_CONFIDENCE
The confidence field in the UDM threat object is set to "LOW_CONFIDENCE" if the confidence_score field is less than or equal to 50.
entity.metadata.threat.confidence
MEDIUM_CONFIDENCE
The confidence field in the UDM threat object is set to "MEDIUM_CONFIDENCE" if the confidence_score field is greater than 50 and less than or equal to 74.
entity.metadata.threat.confidence
UNKNOWN_CONFIDENCE
The confidence field in the UDM threat object is set to "UNKNOWN_CONFIDENCE" if the confidence_score field is not a valid integer.
entity.metadata.vendor_name
ANOMALI_IOC
The vendor_name field in the UDM entity object is set to "ANOMALI_IOC".
Need more help?
Get answers from Community members and Google SecOps professionals.
