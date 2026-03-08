# Collect Duo User context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-user-context/  
**Scraped:** 2026-03-05T09:23:36.747806Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Duo User context logs
Supported in:
Google secops
SIEM
This document explains how to ingest Duo User context logs to Google Security Operations using an API. The parser processes JSON data, mapping user information (including aliasing usernames to email addresses, groups, phone numbers, and device details) to the UDM and capturing user account status. It also handles nested data structures and performs several data transformations and merges to create the final UDM event.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to the
Duo Admin Panel
Configure the Admin API application and get the keys
Sign in to the
Duo Admin Panel
as an administrator.
In the left sidebar click
Applications
>
Manage Applications
.
Press the
Add Application
button.
In the search field, type
Admin API
and click
Add
next to
Duo Admin API
.
On the next screen, the following information is displayed:
Integration Key:
(a string such as
DIYYYYYYYYYYYYYY
).
Secret Key
: a 40-character string.
API hostname
: For example,
api-abcd1234.duosecurity.com
.
Copy and save the
Integration Key
,
Secret Key
and
API hostname
to a secure location.
Scroll to
Settings
and set
Permissions
to
Grant read resource
.
Click
Save Changes
.
Set up feeds
Go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Duo Users Logs
).
Select
Third Party API
as the
Source type
.
Select the
Duo User Context
log type.
Click
Next
.
Specify values for the following input parameters:
Username
: Enter the
Integration Key
copied earlier.
Secret
: Enter the
Secret Key
copied earlier.
API Hostname
: Provide the Duo API server URL (for example,
api-abcd1234.duosecurity.com
).
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
Log Field
UDM Mapping
Logic
access_device.browser
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the
access_device.browser
field or
surfaced_auth.access_device.browser
if the former is empty. The key is set to "access_device browser".
access_device.browser_version
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the
access_device.browser_version
field or
surfaced_auth.access_device.browser_version
if the former is empty. The key is set to "access_device browser_version".
access_device.ip.address
event.idm.entity.entity.ip
The value is taken directly from the
access_device.ip.address
field or
surfaced_auth.access_device.ip
if the former is empty.
access_device.location.city
event.idm.entity.entity.location.city
The value is taken directly from the
access_device.location.city
field or
surfaced_auth.access_device.location.city
if the former is empty.
access_device.location.country
event.idm.entity.entity.location.country_or_region
The value is taken directly from the
access_device.location.country
field or
surfaced_auth.access_device.location.country
if the former is empty.
access_device.location.state
event.idm.entity.entity.location.state
The value is taken directly from the
access_device.location.state
field or
surfaced_auth.access_device.location.state
if the former is empty.
access_device.os
event.idm.entity.entity.asset.platform_software.platform
The value is derived from the
access_device.os
field or
surfaced_auth.access_device.os
if the former is empty.  If the value matches (case-insensitive) "ios" or "mac", the UDM field is set to "MAC". If it matches "windows", the UDM field is set to "WINDOWS". If it matches "linux", the UDM field is set to "LINUX".
access_device.os_version
event.idm.entity.entity.asset.platform_software.platform_version
The value is taken directly from the
access_device.os_version
field or
surfaced_auth.access_device.os_version
if the former is empty.
action.details
event.idm.entity.sec_result.action_details
The value is taken from this field if
action
is empty.
action.name
event.idm.entity.sec_result.detection_fields.value
The value is taken directly from the field. The key is set to "action_name".
activity_id
event.idm.entity.sec_result.detection_fields.value
The value is taken directly from the field. The key is set to "activity_id".
actor.details.created
event.idm.entity.entity.user.attribute.labels.value
The value is taken directly from the field. The key is set to "created".
actor.details.email
event.idm.entity.entity.user.email_addresses
The value is taken directly from the field.
actor.details.groups.key
event.idm.entity.entity.user.group_identifiers
The value is taken directly from the field.
actor.details.groups.name
event.idm.entity.entity.user.group_identifiers
The value is taken directly from the field.
actor.details.last_login
event.idm.entity.entity.user.attribute.labels.value
The value is taken directly from the field. The key is set to "last_login".
actor.details.status
event.idm.entity.entity.user.attribute.labels.value
The value is taken directly from the field. The key is set to "status".
actor.key
event.idm.entity.entity.resource.product_object_id
The value is taken directly from the field.
actor.name
event.idm.entity.entity.user.user_display_name
The value is taken directly from the field or
surfaced_auth.user.name
if the former is empty.
actor.type
event.idm.entity.entity.user.attribute.labels.value
The value is taken directly from the field. The key is set to "actor type".
akey
event.idm.entity.metadata.product_entity_id
The value is taken directly from the field, or
sekey
if
akey
is empty.
application
event.idm.entity.entity.application
The value is taken directly from the field.
collection_time.seconds
,
create_time.seconds
event.idm.entity.metadata.collected_timestamp.seconds
,
event.timestamp.seconds
The greater value of
collection_time.seconds
and
create_time.seconds
is used for both
collected_timestamp.seconds
and the top-level
timestamp.seconds
.
collection_time.nanos
,
create_time.nanos
event.idm.entity.metadata.collected_timestamp.nanos
,
event.timestamp.nanos
The nanoseconds value corresponding to the greater of
collection_time.seconds
and
create_time.seconds
is used for both
collected_timestamp.nanos
and the top-level
timestamp.nanos
.
email
event.idm.entity.entity.user.email_addresses
The value is taken directly from the field.
explanations
event.idm.entity.entity.resource.attribute.labels
The key-value pairs within each object in the
explanations
array are converted into labels. The key for each label is prepended with "explanation ".
firstname
event.idm.entity.entity.user.first_name
The value is taken directly from the field.
from_common_netblock
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "from_common_netblock".
from_new_user
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "from_new_user".
groups.N.name
(N=0..10)
event.idm.entity.entity.user.group_identifiers
The value is taken directly from the field.
lastname
event.idm.entity.entity.user.last_name
The value is taken directly from the field.
low_risk_ip
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "low_risk_ip".
phones.0.model
event.idm.entity.relations.entity.asset.hardware.model
The value is taken directly from the field.
phones.0.number
event.idm.entity.entity.user.phone_numbers
The value is taken directly from the field.
phones.0.phone_id
event.idm.entity.relations.entity.asset.product_object_id
The value is taken directly from the field.
phones.0.platform
event.idm.entity.relations.entity.asset.hardware.manufacturer
The value is taken directly from the field.
priority_event
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "priority_event".
realname
event.idm.entity.entity.user.user_display_name
The value is taken directly from the field.
sekey
event.idm.entity.metadata.product_entity_id
The value is taken directly from the field if
akey
is empty.
state
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "state".
status
event.idm.entity.entity.user.attribute.labels.value
,
event.idm.entity.entity.user.user_authentication_status
The value is taken directly from the field. The key for the label is set to "status". The value is also used to determine the
user_authentication_status
. "active" and "bypass" map to "ACTIVE", "disabled" and "pending deletion" map to "SUSPENDED", and "locked out" maps to "NO_ACTIVE_CREDENTIALS".
surfaced_auth.access_device.browser
event.idm.entity.entity.resource.attribute.labels.value
The value is taken from this field if
access_device.browser
is empty. The key is set to "surfaced_auth access_device browser".
surfaced_auth.access_device.browser_version
event.idm.entity.entity.resource.attribute.labels.value
The value is taken from this field if
access_device.browser_version
is empty. The key is set to "surfaced_auth access_device browser_version".
surfaced_auth.access_device.ip
event.idm.entity.entity.ip
The value is taken from this field if
access_device.ip.address
is empty.
surfaced_auth.access_device.location.city
event.idm.entity.entity.location.city
The value is taken from this field if
access_device.location.city
is empty.
surfaced_auth.access_device.location.country
event.idm.entity.entity.location.country_or_region
The value is taken from this field if
access_device.location.country
is empty.
surfaced_auth.access_device.location.state
event.idm.entity.entity.location.state
The value is taken from this field if
access_device.location.state
is empty.
surfaced_auth.access_device.os
event.idm.entity.entity.asset.platform_software.platform
The value is taken from this field if
access_device.os
is empty. The logic for mapping to the UDM field is the same as for
access_device.os
.
surfaced_auth.access_device.os_version
event.idm.entity.entity.asset.platform_software.platform_version
The value is taken from this field if
access_device.os_version
is empty.
surfaced_auth.user.key
event.idm.entity.entity.user.userid
The value is taken from this field if
username
is empty.
surfaced_auth.user.name
event.idm.entity.entity.user.user_display_name
The value is taken from this field if
actor.name
is empty.
target.details.biometrics_status
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "biometrics_status".
target.details.country_code
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "country_code".
target.details.extension
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "extension".
target.details.manufacturer
event.idm.entity.entity.asset.hardware.manufacturer
The value is taken directly from the field.
target.details.model
event.idm.entity.entity.asset.hardware.model
The value is taken directly from the field.
target.details.number
event.idm.entity.entity.user.phone_numbers
The value is taken directly from the field.
target.details.os
event.idm.entity.entity.asset.software.name
The value is taken directly from the field.
target.details.os_version
event.idm.entity.entity.asset.software.version
The value is taken directly from the field.
target.details.passcode_status
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "passcode_status".
target.details.tampered_status
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "tampered_status".
target.key
event.idm.entity.entity.asset.asset_id
The value is taken directly from the field.
target.name
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "name".
target.type
event.idm.entity.entity.asset.attribute.labels.value
The value is taken directly from the field. The key is set to "type".
triage_event_uri
event.idm.entity.entity.url
The value is taken directly from the field.
triaged_as_interesting
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "triaged_as_interesting".
ts
event.timestamp.seconds
,
event.idm.entity.metadata.collected_timestamp.seconds
The timestamp is parsed from this field if present, using ISO8601 or RFC 3339 format.  The extracted seconds and nanoseconds are used for both the top-level
timestamp
and the
collected_timestamp
.
type
event.idm.entity.entity.resource.attribute.labels.value
The value is taken directly from the field. The key is set to "type".
user_id
event.idm.entity.metadata.product_entity_id
The value is taken directly from the field.
username
event.idm.entity.entity.user.userid
The value is taken directly from the field, or
surfaced_auth.user.key
if
username
is empty.
(Parser Logic)
event.idm.entity.metadata.vendor_name
Hardcoded to "Duo".
(Parser Logic)
event.idm.entity.metadata.product_name
Hardcoded to "Duo User Context".
(Parser Logic)
event.idm.entity.metadata.entity_type
Determined based on the presence of other fields.  If
user_present
is true, it's set to "USER".  If
asset_mid_present
is true, it's set to "ASSET". If
ip_present
is true, it's set to "IP_ADDRESS". If
resource_present
is true, it's set to "RESOURCE". Otherwise, it's set to "UNKNOWN_ENTITYTYPE".
(Parser Logic)
event.idm.entity.relations.entity_type
Set to "ASSET" if
phones[0]
is not empty.
(Parser Logic)
event.idm.entity.relations.relationship
Set to "OWNS" if
phones[0]
is not empty.
(Parser Logic)
event.idm.entity.relations.entity.asset.type
Set to "MOBILE" if
phones[0]
is not empty.
Need more help?
Get answers from Community members and Google SecOps professionals.
