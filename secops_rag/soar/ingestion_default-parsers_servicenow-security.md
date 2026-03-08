# Collect ServiceNow Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-security/  
**Scraped:** 2026-03-05T10:00:10.746570Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ServiceNow Security logs
Supported in:
Google secops
SIEM
This document explains how to export ServiceNow Security events to Google Security Operations using outbound webhooks configured through Business Rules.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format.
Integration architecture
This integration uses ServiceNow Business Rules to push security events to Google SecOps in real-time:
ServiceNow Security Tables
    ↓ (Business Rules trigger on insert/update)
ServiceNow RESTMessageV2 API
    ↓ (HTTP POST)
Google Security Operations Webhook Endpoint
    ↓ (Parser: SERVICENOW_SECURITY)
Unified Data Model (UDM)
Integration characteristics:
Event-driven push
: Events sent immediately when created or updated
Real-time
: Low latency (seconds)
Selective export
: Configure which tables and events to export
Not bulk export
: Does not send historical data
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
A ServiceNow instance with
Security Incident Response (SIR)
plugin installed
A ServiceNow user account with the following roles:
admin
or
sn_si.admin
(to create Business Rules)
Access to
System Definition
>
Business Rules
Access to
System Definition
>
Script Includes
Privileged access to Google Google Cloud console (for API key creation)
ServiceNow Security tables for export
The following tables contain security-relevant data for SIEM analysis:
Table
API Name
Description
Priority
Security Incident
sn_si_incident
Security incidents, investigations
HIGH
Observable
sn_si_observable
IOCs: IP addresses, domains, file hashes
HIGH
System Log
syslog
Authentication events, login failures
MEDIUM
Audit
sys_audit
Field-level changes, permission modifications
MEDIUM
User Role Assignment
sys_user_has_role
Role grants/revocations
LOW
Security Finding
sn_si_finding
Security detections and findings
LOW
This guide provides Business Rule examples for the HIGH priority tables. You can extend the integration to additional tables using the same pattern.
Configure a feed in Google SecOps to ingest ServiceNow Security events
Set up the webhook feed
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
ServiceNow Security Events
).
Select
Webhook
as the
Source type
.
Select
ServiceNow Security
as the
Log type
.
Click
Next
.
Configure feed parameters
Specify values for the following input parameters:
Split delimiter
: Enter
\n
to separate log lines.
Asset namespace
: The
asset namespace
.
Ingestion labels
: Labels applied to all events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Generate secret key and retrieve endpoint URL
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and save the secret key in a secure location.
Go to the
Details
tab.
Copy the feed endpoint URL from the
Endpoint Information
field.
Example endpoint URL:
https://malachiteingestion-pa.googleapis.com/v2/unstructured/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/logTypes/SERVICENOW_SECURITY:import
Click
Done
.
Create API key for authentication
Go to the
Google Cloud console Credentials
page.
Click
Create credentials
, and then select
API key
.
Click
Restrict Key
.
Under
API restrictions
:
Select
Restrict key
.
Select
Google SecOps API
(Chronicle API).
Click
Save
.
Copy
the API key and save it in a secure location.
Configure ServiceNow integration credentials
Store the Google SecOps credentials as ServiceNow System Properties for secure access.
In ServiceNow, go to
System Properties
>
sys_properties.list
.
Click
New
.
Create the first property:
Name
:
x_chronicle.endpoint_url
Value
: Paste the feed endpoint URL from the previous step
Type
:
string
Click
Submit
.
Click
New
to create the second property:
Name
:
x_chronicle.api_key
Value
: Paste the Google Cloud API key
Type
:
password
(this encrypts the value)
Click
Submit
.
Click
New
to create the third property:
Name
:
x_chronicle.secret_key
Value
: Paste the Google SecOps feed secret key
Type
:
password
(this encrypts the value)
Click
Submit
.
Create reusable webhook utility Script Include
This Script Include provides a reusable function for sending events to Google SecOps from any Business Rule.
Go to
System Definition
>
Script Includes
.
Click
New
.
Provide the following configuration details:
Name
:
ChronicleWebhookUtil
API Name
:
ChronicleWebhookUtil
Client callable
: Unchecked
Active
: Checked
In the
Script
field, enter the following code:
var
ChronicleWebhookUtil
=
Class
.
create
();
ChronicleWebhookUtil
.
prototype
=
{
initialize
:
function
()
{
// Read credentials from System Properties
this
.
endpointURL
=
gs
.
getProperty
(
'x_chronicle.endpoint_url'
);
this
.
apiKey
=
gs
.
getProperty
(
'x_chronicle.api_key'
);
this
.
secretKey
=
gs
.
getProperty
(
'x_chronicle.secret_key'
);
},
sendEvent
:
function
(
eventData
,
eventType
)
{
try
{
// Validate credentials
if
(
!
this
.
endpointURL
||
!
this
.
apiKey
||
!
this
.
secretKey
)
{
gs
.
error
(
'[Chronicle] Missing configuration. Check System Properties: x_chronicle.*'
);
return
false
;
}
// Prepare payload
var
payload
=
{
event_type
:
eventType
,
timestamp
:
new
GlideDateTime
().
getDisplayValue
(),
data
:
eventData
,
source
:
"ServiceNow"
,
source_instance
:
gs
.
getProperty
(
'instance_name'
)
};
// Create REST message
var
request
=
new
sn_ws
.
RESTMessageV2
();
request
.
setEndpoint
(
this
.
endpointURL
+
'?key='
+
this
.
apiKey
);
request
.
setHttpMethod
(
'POST'
);
// Set headers
request
.
setRequestHeader
(
'Content-Type'
,
'application/json'
);
request
.
setRequestHeader
(
'x-chronicle-auth'
,
this
.
secretKey
);
// Set request body
request
.
setRequestBody
(
JSON
.
stringify
(
payload
));
// Execute request
var
response
=
request
.
execute
();
var
statusCode
=
response
.
getStatusCode
();
var
responseBody
=
response
.
getBody
();
// Check response
if
(
statusCode
==
200
||
statusCode
==
201
||
statusCode
==
204
)
{
gs
.
info
(
'[Chronicle] Event sent successfully: '
+
eventType
+
' | Status: '
+
statusCode
);
return
true
;
}
else
{
gs
.
error
(
'[Chronicle] Failed to send event: '
+
eventType
+
' | Status: '
+
statusCode
+
' | Response: '
+
responseBody
);
return
false
;
}
}
catch
(
ex
)
{
gs
.
error
(
'[Chronicle] Exception sending event: '
+
ex
.
message
);
return
false
;
}
},
type
:
'ChronicleWebhookUtil'
};
Click
Submit
.
Create Business Rules for event export
Business Rules automatically trigger when records are created or updated in ServiceNow tables. Create a Business Rule for each table you want to export to Google SecOps.
Business Rule: Security Incidents
This Business Rule exports security incident events to Google SecOps.
Go to
System Definition
>
Business Rules
.
Click
New
.
Provide the following configuration details:
When to run:
Field
Value
Name
Chronicle - Export Security Incident
Table
Security Incident [sn_si_incident]
Active
Checked
Advanced
Checked
When
after
Insert
Checked
Update
Checked
Delete
Optional (check to track deletions)
Order
100
Click the
Advanced
tab, go to the
Script
field, and enter the following code:
(
function
executeRule
(
current
,
previous
/*null when async*/
)
{
// Extract incident data
var
incidentData
=
{
sys_id
:
current
.
getValue
(
'sys_id'
),
number
:
current
.
getValue
(
'number'
),
short_description
:
current
.
getValue
(
'short_description'
),
description
:
current
.
getValue
(
'description'
),
state
:
current
.
getDisplayValue
(
'state'
),
priority
:
current
.
getDisplayValue
(
'priority'
),
severity
:
current
.
getDisplayValue
(
'severity'
),
risk_score
:
current
.
getValue
(
'risk_score'
),
category
:
current
.
getDisplayValue
(
'category'
),
subcategory
:
current
.
getDisplayValue
(
'subcategory'
),
assigned_to
:
current
.
getDisplayValue
(
'assigned_to'
),
assignment_group
:
current
.
getDisplayValue
(
'assignment_group'
),
caller
:
current
.
getDisplayValue
(
'caller'
),
affected_user
:
current
.
getDisplayValue
(
'affected_user'
),
opened_at
:
current
.
getValue
(
'opened_at'
),
closed_at
:
current
.
getValue
(
'closed_at'
),
resolved_at
:
current
.
getValue
(
'resolved_at'
),
sys_created_on
:
current
.
getValue
(
'sys_created_on'
),
sys_updated_on
:
current
.
getValue
(
'sys_updated_on'
),
sys_created_by
:
current
.
getValue
(
'sys_created_by'
),
sys_updated_by
:
current
.
getValue
(
'sys_updated_by'
),
work_notes
:
current
.
getValue
(
'work_notes'
),
close_notes
:
current
.
getValue
(
'close_notes'
)
};
// Send to Chronicle
var
chronicleUtil
=
new
ChronicleWebhookUtil
();
chronicleUtil
.
sendEvent
(
incidentData
,
'security_incident'
);
})(
current
,
previous
);
Click
Submit
.
Business Rule: Observables (IOCs)
This Business Rule exports observable data (IP addresses, domains, file hashes) to Google SecOps.
Go to
System Definition
>
Business Rules
.
Click
New
.
Provide the following configuration details:
Field
Value
Name
Chronicle - Export Observable
Table
Observable [sn_si_observable]
Active
Checked
Advanced
Checked
When
after
Insert
Checked
Update
Checked
Order
100
Click the
Advanced
tab, go to the
Script
field, and enter the following code:
(
function
executeRule
(
current
,
previous
)
{
var
observableData
=
{
sys_id
:
current
.
getValue
(
'sys_id'
),
value
:
current
.
getValue
(
'value'
),
type
:
current
.
getDisplayValue
(
'type'
),
finding
:
current
.
getDisplayValue
(
'finding'
),
sighting_count
:
current
.
getValue
(
'sighting_count'
),
notes
:
current
.
getValue
(
'notes'
),
security_tags
:
current
.
getValue
(
'security_tags'
),
mitre_technique
:
current
.
getDisplayValue
(
'mitre_technique'
),
mitre_tactic
:
current
.
getDisplayValue
(
'mitre_tactic'
),
mitre_malware
:
current
.
getDisplayValue
(
'mitre_malware'
),
sys_created_on
:
current
.
getValue
(
'sys_created_on'
),
sys_created_by
:
current
.
getValue
(
'sys_created_by'
)
};
var
chronicleUtil
=
new
ChronicleWebhookUtil
();
chronicleUtil
.
sendEvent
(
observableData
,
'observable'
);
})(
current
,
previous
);
Click
Submit
.
Business Rule: System Login Events
This Business Rule exports authentication and login events to Google SecOps.
Go to
System Definition
>
Business Rules
.
Click
New
.
Provide the following configuration details:
Field
Value
Name
Chronicle - Export System Log
Table
System Log [syslog]
Active
Checked
Advanced
Checked
When
after
Insert
Checked
Order
100
Condition
current.level == "error" || current.source.indexOf("login") != -1
Click the
Advanced
tab, go to the
Script
field, and enter the following code:
(
function
executeRule
(
current
,
previous
)
{
var
logData
=
{
sys_id
:
current
.
getValue
(
'sys_id'
),
level
:
current
.
getValue
(
'level'
),
source
:
current
.
getValue
(
'source'
),
message
:
current
.
getValue
(
'message'
),
sys_created_on
:
current
.
getValue
(
'sys_created_on'
),
sys_created_by
:
current
.
getValue
(
'sys_created_by'
)
};
var
chronicleUtil
=
new
ChronicleWebhookUtil
();
chronicleUtil
.
sendEvent
(
logData
,
'system_log'
);
})(
current
,
previous
);
Click
Submit
.
Business Rule: Audit Trail (Permission Changes)
This Business Rule exports field-level changes for audit trail purposes.
Go to
System Definition
>
Business Rules
.
Click
New
.
Provide the following configuration details:
Field
Value
Name
Chronicle - Export Audit Changes
Table
Audit [sys_audit]
Active
Checked
Advanced
Checked
When
after
Insert
Checked
Order
100
Condition
See the following script
Condition (filter critical changes only):
```javascript
current.tablename == 'sys_user_has_role' || current.tablename == 'sys_user_group_member' || current.tablename == 'sn_si_incident' || current.fieldname == 'active' || current.fieldname == 'locked_out'
```
Click the
Advanced
tab, go to the
Script
field, and enter the following code:
(
function
executeRule
(
current
,
previous
)
{
var
auditData
=
{
sys_id
:
current
.
getValue
(
'sys_id'
),
tablename
:
current
.
getValue
(
'tablename'
),
documentkey
:
current
.
getValue
(
'documentkey'
),
fieldname
:
current
.
getValue
(
'fieldname'
),
oldvalue
:
current
.
getValue
(
'oldvalue'
),
newvalue
:
current
.
getValue
(
'newvalue'
),
user
:
current
.
getDisplayValue
(
'user'
),
reason
:
current
.
getValue
(
'reason'
),
sys_created_on
:
current
.
getValue
(
'sys_created_on'
)
};
var
chronicleUtil
=
new
ChronicleWebhookUtil
();
chronicleUtil
.
sendEvent
(
auditData
,
'audit_change'
);
})(
current
,
previous
);
Click
Submit
.
Optional: Additional tables for export
User Role Assignment Changes
Export role grants and revocations for security auditing.
Create a Business Rule on the
sys_user_has_role
table:
(
function
executeRule
(
current
,
previous
)
{
var
roleData
=
{
sys_id
:
current
.
getValue
(
'sys_id'
),
user
:
current
.
getDisplayValue
(
'user'
),
role
:
current
.
getDisplayValue
(
'role'
),
granted_by
:
current
.
getDisplayValue
(
'granted_by'
),
state
:
current
.
getValue
(
'state'
),
sys_created_on
:
current
.
getValue
(
'sys_created_on'
)
};
var
chronicleUtil
=
new
ChronicleWebhookUtil
();
chronicleUtil
.
sendEvent
(
roleData
,
'role_assignment'
);
})(
current
,
previous
);
Security Findings
Export security detections and findings.
Create a Business Rule on the
sn_si_finding
table:
(
function
executeRule
(
current
,
previous
)
{
var
findingData
=
{
sys_id
:
current
.
getValue
(
'sys_id'
),
finding
:
current
.
getValue
(
'finding'
),
confidence
:
current
.
getValue
(
'confidence'
),
severity
:
current
.
getDisplayValue
(
'severity'
),
observable
:
current
.
getDisplayValue
(
'observable'
),
sys_created_on
:
current
.
getValue
(
'sys_created_on'
)
};
var
chronicleUtil
=
new
ChronicleWebhookUtil
();
chronicleUtil
.
sendEvent
(
findingData
,
'finding'
);
})(
current
,
previous
);
For more information about Google SecOps feeds, see
Google SecOps feeds documentation
. For information about requirements for each feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds,
contact Google SecOps support
.
UDM mapping table
ServiceNow Field
UDM Mapping
Logic
number
metadata.product_event_type
Incident or event number
short_description
security_result.summary
Brief description of the security event
severity
security_result.severity
Event severity level
priority
security_result.priority
Event priority
caller
principal.user.userid
User who reported or triggered the event
affected_user
target.user.userid
User affected by the security event
assigned_to
security_result.action_details
Analyst assigned to the incident
sys_created_on
metadata.event_timestamp
Event creation timestamp
value
(observable)
network.ip
or
network.dns.questions.name
Observable value (IP, domain, hash)
type
(observable)
security_result.detection_fields.value
Observable type (IP address, domain, file hash)
Need more help?
Get answers from Community members and Google SecOps professionals.
