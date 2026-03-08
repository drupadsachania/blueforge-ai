# Collect Splunk CIM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/splunk/  
**Scraped:** 2026-03-05T09:18:06.073225Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Splunk CIM logs
Supported in:
Google secops
SIEM
This document describes how you can collect Splunk Common Information Model (CIM) logs by configuring Splunk
and a Google Security Operations forwarder. This document also lists the supported log types
and supported Splunk versions.
For more information, see
Data ingestion to Google Security Operations
.
Overview
The following deployment architecture diagram shows how Splunk agents are configured to send logs to Google Security Operations. Each customer deployment might
differ from this representation and might be more complex.
The architecture diagram shows the following components:
Data source
: The system to be monitored in which Splunk is installed.
Splunk
: Collects information from the data source and forwards the information to Google Security Operations forwarder.
Google Security Operations forwarder
: A lightweight
software component, deployed in the customer's network to forward the logs to Google Security Operations.
Google Security Operations
: Retains and analyzes the logs from
the Fleet server.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with
SPLUNK
ingestion label.
Before you begin
Use Splunk version 5.0 that Google Security Operations parser supports.
Ensure that all systems in the deployment architecture are configured
in the UTC time zone.
Configure a Splunk agent and a Google Security Operations forwarder
Set up Splunk Enterprise
.
Install a CIM compliant agent from
Splunkbase
.
Set up a Google Security Operations forwarder
.
Configure Google Security Operations forwarder to push the logs into the Google Security Operations system. The following is an example of a Google Security Operations forwarder configuration:
- splunk:
      common:
        enabled: true
        data_type: SPLUNK
        batch_n_seconds: 10
        batch_n_bytes: 819200
      url: <SPLUNK_URL>
      query_cim: true
      is_ignore_cert: true
      query_string: datamodel Network_Traffic All_Traffic flat
Considerations for writing Splunk search queries
Splunk has its own search language, which is similar to SQL. Make sure you use the correct syntax for your search query. Consider the following search characteristics when you create a query:
Escape character
If a string value contains a double quotation mark
"
, use backslash characters to escape the quotation mark. Otherwise, the search misinterprets the end of the string value.
For example: To search a string
WHERE _raw="The user "vpatel" isn't authenticated."
,
you must use the sequence
\"
to search for a literal double quotation mark.
Write the search string in the following format:
WHERE _raw="The user \"vpatel\" isn't authenticated."
To escape a backslash character
\
, use the sequence
\\
to search for a backslash.
For example, if there is a string like
C:\user\abc
then this must be written as
C:\\user\\abc
.
Syntactically incorrect search
If a section of the query is invalid, the entire query is not evaluated and an error message appears.
Consider the following example in which the search mode option is missing in the query:
multisearch [|datamodel Network_Traffic All_Traffic] [|datamodel Network_Sessions All_Sessions flat]
In this example, the search mode option is missing in the query. This results in the following error:
Error in 'multisearch' command: Multisearch sub searches might only contain purely streaming operations. The search job has failed due to an error.
Support for multiple data models
Splunk supports a single large query that spans data models. The following search query extracts data from multiple data models:
multisearch [|datamodel Network_Traffic All_Traffic flat] [|datamodel Network_Sessions All_Sessions flat]
Here are the components of this query that spans data models:
Multisearch
: The query must start with the word
multisearch
. A query for a data model must be enclosed within square brackets
[ ]
and start with a pipe
|
character.
Network_Traffic
: The name of the data model.
All_Traffic
: Dataset of
Network_Traffic
data model.
flat
: Search mode. The other options are
search
and
acceleration_search
.
We recommend using the following Splunk query for multiple data model search:
multisearch [|datamodel Network_Traffic All_Traffic flat] [|datamodel Network_Sessions All_Sessions flat]
Supported log types and data models
Splunk data model
Supported
Alerts
Yes
Application State (deprecated)
No
Authentication
Yes
Certificates
Yes
Change
Yes
Change Analysis (deprecated)
No
Data Access
Yes
Databases
Yes
Data Loss Prevention
Yes
Email
Yes
Endpoint
Yes
Event Signatures
Yes
Interprocess Messaging
Yes
Intrusion Detection
Yes
Inventory
Yes
Java Virtual Machines (JVM)
Yes
Malware
Yes
Network Resolution (DNS)
Yes
Network Sessions
Yes
Network Traffic
Yes
Performance
Yes
Splunk Audit Logs
Yes
Ticket Management
Yes
Updates
Yes
Vulnerabilities
Yes
Web
Yes
Supported Splunk CIM log formats
The Splunk CIM parser supports logs in JSON format.
Supported Splunk CIM sample logs
JSON
{
  "Channel": "Microsoft-Windows-Sysmon/Operational",
  "Computer": "dhcp-ad01.testdhcp2.local",
  "EventChannel": "Microsoft-Windows-Sysmon/Operational",
  "EventCode": "5",
  "EventData_Xml": "<Data Name='RuleName'>-<\\/Data><Data Name='UtcTime'>2021-10-22 06:38:15.540<\\/Data><Data Name='ProcessGuid'>{8AE2CCCF-5C56-6172-84FE-000000001500}<\\/Data><Data Name='ProcessId'>5616<\\/Data><Data Name='Image'>C:\\\\Program Files\\\\Splunk\\\\bin\\\\splunk-optimize.exe<\\/Data>",
  "EventDescription": "Process terminated",
  "EventID": "5",
  "EventRecordID": "157268",
  "Guid": "'{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'",
  "Image": "C:\\\\Program Files\\\\Splunk\\\\bin\\\\splunk-optimize.exe",
  "Keywords": "0x8000000000000000",
  "Level": "4",
  "Name": "'Microsoft-Windows-Sysmon'",
  "Opcode": "0",
  "ProcessGuid": "{8AE2CCCF-5C56-6172-84FE-000000001500}",
  "ProcessID": "'2888'",
  "ProcessId": "5616",
  "RecordID": "157268",
  "RecordNumber": "157268",
  "RuleName": "-",
  "SecurityID": "S-1-5-18",
  "SystemTime": "'2021-10-22T06:38:15.548776000Z'",
  "System_Props_Xml": "<Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'/><EventID>5<\\/EventID><Version>3<\\/Version><Level>4<\\/Level><Task>5<\\/Task><Opcode>0<\\/Opcode><Keywords>0x8000000000000000<\\/Keywords><TimeCreated SystemTime='2021-10-22T06:38:15.548776000Z'/><EventRecordID>157268<\\/EventRecordID><Correlation/><Execution ProcessID='2888' ThreadID='3648'/><Channel>Microsoft-Windows-Sysmon/Operational<\\/Channel><Computer>dhcp-ad01.testdhcp2.local<\\/Computer><Security UserID='S-1-5-18'/>",
  "Task": "5",
  "ThreadID": "'3648'",
  "TimeCreated": "2021-10-22T06:38:15.548776000Z",
  "UserID": "'S-1-5-18'",
  "UtcTime": "2021-10-22 06:38:15.540",
  "Version": "3",
  "_raw": "<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Sysmon' Guid='{5770385F-C22A-43E0-BF4C-06F5698FFBD9}'/><EventID>5<\\/EventID><Version>3<\\/Version><Level>4<\\/Level><Task>5<\\/Task><Opcode>0<\\/Opcode><Keywords>0x8000000000000000<\\/Keywords><TimeCreated SystemTime='2021-10-22T06:38:15.548776000Z'/><EventRecordID>157268<\\/EventRecordID><Correlation/><Execution ProcessID='2888' ThreadID='3648'/><Channel>Microsoft-Windows-Sysmon/Operational<\\/Channel><Computer>dhcp-ad01.testdhcp2.local<\\/Computer><Security UserID='S-1-5-18'/><\\/System><EventData><Data Name='RuleName'>-<\\/Data><Data Name='UtcTime'>2021-10-22 06:38:15.540<\\/Data><Data Name='ProcessGuid'>{8AE2CCCF-5C56-6172-84FE-000000001500}<\\/Data><Data Name='ProcessId'>5616<\\/Data><Data Name='Image'>C:\\\\Program Files\\\\Splunk\\\\bin\\\\splunk-optimize.exe<\\/Data><\\/EventData><\\/Event>",
  "_time": "2021-10-22T12:08:15.540+0530",
  "action": "blocked",
  "date_hour": "6",
  "date_mday": "22",
  "date_minute": "38",
  "date_month": "october",
  "date_second": "15",
  "date_wday": "friday",
  "date_year": "2021",
  "date_zone": "0",
  "dest": "dummy.domain.com",
  "dvc_nt_host": "DHCP-AD01",
  "event_id": "157268",
  "eventtype": [
    "endpoint_services_processes",
    "ms-sysmon-process",
    "windows_event_signature"
  ],
  "host": "DHCP-AD01",
  "id": "157268",
  "index": "main",
  "linecount": "1",
  "os": "Microsoft Windows",
  "process": "C:\\\\Program Files\\\\Splunk\\\\bin\\\\splunk-optimize.exe",
  "process_exec": "splunk-optimize.exe",
  "process_guid": "{8AE2CCCF:5C56:6172:84FE-000000001500}",
  "process_id": "5616",
  "process_name": "splunk-optimize.exe",
  "process_path": "C:\\\\Program Files\\\\Splunk\\\\bin\\\\splunk-optimize.exe",
  "punct": "<_='://../////'><><_='--'_='{----}'/><><\\/><><\\/><><",
  "signature": "Process terminated",
  "signature_id": "5",
  "source": "XmlWinEventLog:Microsoft-Windows-Sysmon/Operational",
  "sourcetype": "XmlWinEventLog",
  "splunk_server": "dhcp-ad01",
  "tag": [
    "process",
    "report",
    "track_event_signatures"
  ],
  "tag2001:db8::eventtype": [
    "process",
    "report",
    "track_event_signatures"
  ],
  "timeendpos": "671",
  "timestartpos": "648",
  "user_id": "'dummy-user-id'",
  "vendor_product": "Microsoft Sysmon"
}
Field mapping reference
This section explains how the Google Security Operations parser maps Splunk log fields to Google Security Operations Unified Data Model (UDM) fields for the data sets. For more information, see Splunk document for
version 5.0.1
.
Alerts
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Alerts:
Log field
UDM mapping
app
observer.application
description
security_result.description
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_type
target.resource.resource_type
id
metadata.product_log_id
mitre_technique_id
security_result.detection_fields.labels.key/value
severity
security_result.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
security_result.rule_name
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_type
principal.resource.resource_type
tag
about.labels.key/value (deprecated)
additional.fields
type
security_result.alert_state
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_name
principal.user.userid
user_priority
principal.user.attribute.label.key/value
vendor_account
about.labels.key/value (deprecated)
additional.fields
vendor_region
about.location.country_or_region
Authentication
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Authentication:
Log field
UDM mapping
action
security_result.action_details
security_result.action
app
target.application
authentication_method
about.labels.key/value (deprecated)
additional.fields
authentication_service
extension.auth.auth_details
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_nt_domain
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
reason
security_result.summary
response_time
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_nt_domain
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_user
principal.user.user_display_name
src_user_bunit
principal.labels.key/value (deprecated)
additional.fields
src_user_category
principal.labels.key/value (deprecated)
additional.fields
src_user_id
principal.user.userid
src_user_priority
principal.labels.key/value (deprecated)
additional.fields
src_user_role
principal.user.attribute.roles.name (repeated)
src_user_type
principal.user.attribute.roles.type
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_agent
network.http.user_agent
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_id
principal.user.userid
user_priority
principal.user.attribute.label.key/value
user_role
principal.user.attribute.roles.name (repeated)
user_type
principal.user.attribute.roles.type
vendor_account
about.labels.key/value (deprecated)
additional.fields
All_Certificates
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Certificates:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_port
target.port
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
response_time
about.labels.key/value (deprecated)
additional.fields
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_port
principal.port
src_priority
principal.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
transport
network.ip_protocol
SSL
The following table lists the log fields and corresponding UDM mappings for the Splunk data set SSL:
Log field
UDM mapping
ssl_end_time
network.tls.server.certificate.not_after
ssl_engine
about.labels.key/value (deprecated)
additional.fields
ssl_hash
about.labels.key/value (deprecated)
additional.fields
ssl_is_valid
about.labels.key/value (deprecated)
additional.fields
ssl_issuer
network.tls.server.certificate.issuer
ssl_issuer_common_name
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_email
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_email_domain
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_locality
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_organization
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_state
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_street
about.labels.key/value (deprecated)
additional.fields
ssl_issuer_unit
about.labels.key/value (deprecated)
additional.fields
ssl_name
about.labels.key/value (deprecated)
additional.fields
ssl_policies
about.labels.key/value (deprecated)
additional.fields
ssl_publickey
about.labels.key/value (deprecated)
additional.fields
ssl_publickey_algorithm
about.labels.key/value (deprecated)
additional.fields
ssl_serial
network.tls.server.certificate.serial
ssl_session_id
network.session_id
ssl_signature_algorithm
about.labels.key/value (deprecated)
additional.fields
ssl_start_time
network.tls.server.certificate.not_before
ssl_subject
network.tls.server.certificate.subject
ssl_subject_common_name
about.labels.key/value (deprecated)
additional.fields
ssl_subject_email
about.labels.key/value (deprecated)
additional.fields
ssl_subject_email_domain
about.labels.key/value (deprecated)
additional.fields
ssl_subject_locality
about.labels.key/value (deprecated)
additional.fields
ssl_subject_organization
about.labels.key/value (deprecated)
additional.fields
ssl_subject_state
about.labels.key/value (deprecated)
additional.fields
ssl_subject_street
about.labels.key/value (deprecated)
additional.fields
ssl_subject_unit
about.labels.key/value (deprecated)
additional.fields
ssl_validity_window
about.labels.key/value (deprecated)
additional.fields
ssl_version
network.tls.server.certificate.version
All_Changes
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Changes:
Log field
UDM mapping
action
security_result.action_details
security_result.action
change_type
security_result.category_details
command
principal.process.command_line
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dvc
principal.asset.hostname, principal.asset.ip
object
target.resource.name
object_attrs
about.labels.key/value (deprecated)
additional.fields
object_category
about.labels.key/value (deprecated)
additional.fields
object_id
target.user.product_object_id
object_path
target.file.full_path
result
metadata.description
result_id
metadata.product_event_type
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
user
target.user.userid
user_agent
network.http.user_agent
user_name
principal.user.user_display_name, target.labels.key/value
user_type
principal.user.attribute.roles.type, target.user.attribute.roles.type
vendor_account
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
vendor_region
about.location.country_or_region
Account_Management
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Account_Management:
Log field
UDM mapping
dest_nt_domain
target.administrative_domain
src_nt_domain
principal.administrative_domain
src_user
principal.user.userid
src_user_bunit
principal.labels.key/value (deprecated)
additional.fields
src_user_category
principal.labels.key/value (deprecated)
additional.fields
src_user_priority
principal.labels.key/value (deprecated)
additional.fields
src_user_name
principal.labels.key/value (deprecated)
additional.fields
src_user_type
principal.user.attribute.roles.type
Instance_Changes
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Instance_Changes:
Log field
UDM mapping
image_id
principal.asset_id
instance_type
about.labels.key/value (deprecated)
additional.fields
network_Changes
The following table lists the log fields and corresponding UDM mappings for the Splunk data set network_Changes:
Log field
UDM mapping
dest_ip_range
target.labels.key/value (deprecated)
additional.fields
dest_port_range
target.labels.key/value (deprecated)
additional.fields
direction
network.direction
protocol
network.ip_protocol
rule_action
security_result.action_details
security_result.action
src_ip_range
principal.labels.key/value (deprecated)
additional.fields
src_port_range
principal.labels.key/value (deprecated)
additional.fields
Data_Access
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Data_Access:
Log field
UDM mapping
action
security_result.action_details
security_result.action
app
target.application
app_id
metadata.product_log_id
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_name
target.administrative_domain
dest_url
target.url
dvc
principal.asset.hostname, principal.asset.ip
email
principal.user.email_addresses
object
target.resource.name
object_category
about.labels.key/value (deprecated)
additional.fields
object_id
target.user.product_object_id
object_path
target.file.full_path
object_size
target.file.size
owner
about.labels.key/value (deprecated)
additional.fields
owner_email
about.labels.key/value (deprecated)
additional.fields
owner_id
principal.user.userid
parent_object
target.resource.parent
parent_object_id
about.labels.key/value (deprecated)
additional.fields
parent_object_category
about.labels.key/value (deprecated)
additional.fields
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
tenant_id
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_agent
network.http.user_agent
user_group
principal.user.group_identifiers(repeated)
user_role
principal.user.attribute.roles.name (repeated)
vendor_product
about.labels.key/value (deprecated)
additional.fields
vendor_product_id
about.labels.key/value (deprecated)
additional.fields
All_Databases
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Databases:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
object
target.resource.name
response_time
about.labels.key/value (deprecated)
additional.fields
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
Database_Instance
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Database_Instance:
Log field
UDM mapping
instance_name
target.resource.attributes.key/value
instance_version
target.resource.attributes.key/value
process_limit
about.labels.key/value (deprecated)
additional.fields
session_limit
about.labels.key/value (deprecated)
additional.fields
Database_Query
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Database_Query:
Log field
UDM mapping
query
about.labels.key/value (deprecated)
additional.fields
query_id
about.labels.key/value (deprecated)
additional.fields
query_time
about.labels.key/value (deprecated)
additional.fields
records_affected
about.labels.key/value (deprecated)
additional.fields
Instance_Stats
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Instance_Stats:
Log field
UDM mapping
availability
about.labels.key/value (deprecated)
additional.fields
avg_executions
about.labels.key/value (deprecated)
additional.fields
dump_area_used
about.labels.key/value (deprecated)
additional.fields
instance_reads
about.labels.key/value (deprecated)
additional.fields
instance_writes
about.labels.key/value (deprecated)
additional.fields
number_of_users
about.labels.key/value (deprecated)
additional.fields
processes
about.labels.key/value (deprecated)
additional.fields
sessions
about.labels.key/value (deprecated)
additional.fields
sga_buffer_cache_size
about.labels.key/value (deprecated)
additional.fields
sga_buffer_hit_limit
about.labels.key/value (deprecated)
additional.fields
sga_data_dict_hit_ratio
about.labels.key/value (deprecated)
additional.fields
sga_fixed_area_size
about.labels.key/value (deprecated)
additional.fields
sga_free_memory
about.labels.key/value (deprecated)
additional.fields
sga_library_cache_size
about.labels.key/value (deprecated)
additional.fields
sga_redo_log_buffer_size
about.labels.key/value (deprecated)
additional.fields
sga_shared_pool_size
about.labels.key/value (deprecated)
additional.fields
sga_sql_area_size
about.labels.key/value (deprecated)
additional.fields
start_time
about.labels.key/value (deprecated)
additional.fields
tablespace_used
about.labels.key/value (deprecated)
additional.fields
Session_Info
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Session_Info:
Log field
UDM mapping
buffer_cache_hit_ratio
about.labels.key/value (deprecated)
additional.fields
commits
about.labels.key/value (deprecated)
additional.fields
cpu_used
about.labels.key/value (deprecated)
additional.fields
cursor
about.labels.key/value (deprecated)
additional.fields
elapsed_time
about.labels.key/value (deprecated)
additional.fields
logical_reads
about.labels.key/value (deprecated)
additional.fields
machine
about.hostname
memory_sorts
about.labels.key/value (deprecated)
additional.fields
physical_reads
about.labels.key/value (deprecated)
additional.fields
seconds_in_wait
about.labels.key/value (deprecated)
additional.fields
session_id
network.session_id
session_status
about.labels.key/value (deprecated)
additional.fields
table_scans
about.labels.key/value (deprecated)
additional.fields
wait_state
about.labels.key/value (deprecated)
additional.fields
wait_time
about.labels.key/value (deprecated)
additional.fields
Lock_Info
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Lock_Info:
Log field
UDM mapping
last_call_minute
about.labels.key/value (deprecated)
additional.fields
lock_mode
about.labels.key/value (deprecated)
additional.fields
lock_session_id
about.labels.key/value (deprecated)
additional.fields
logon_time
about.labels.key/value (deprecated)
additional.fields
obj_name
about.labels.key/value (deprecated)
additional.fields
os_pid
target.process.pid
serial_num
target.resource.product_object_id
Tablespace
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Tablespace:
Log field
UDM mapping
free_bytes
about.file.size
tablespace_name
about.resource.name
tablespace_reads
about.labels.key/value (deprecated)
additional.fields
tablespace_status
about.labels.key/value (deprecated)
additional.fields
tablespace_writes
about.labels.key/value (deprecated)
additional.fields
Query_Stats
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Query_Stats:
Log field
UDM mapping
indexes_hit
about.labels.key/value (deprecated)
additional.fields
query_plan_hit
about.labels.key/value (deprecated)
additional.fields
stored_procedures_called
about.labels.key/value (deprecated)
additional.fields
tables_hit
about.labels.key/value (deprecated)
additional.fields
DLP_Incidents
The following table lists the log fields and corresponding UDM mappings for the Splunk data set DLP_Incidents:
Log field
UDM mapping
action
security_result.action_details
security_result.action
app
target.application
category
security_result.category_details
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_zone
target.location.country_or_origin
dlp_type
about.labels.key/value (deprecated)
additional.fields
dvc
principal.asset.hostname, principal.asset.ip
dvc_bunit
about.labels.key/value (deprecated)
additional.fields
dvc_category
about.labels.key/value (deprecated)
additional.fields
dvc_priority
about.labels.key/value (deprecated)
additional.fields
dvc_zone
principal.asset.location.country_or_region
object
target.resource.name
object_category
about.labels.key/value (deprecated)
additional.fields
object_path
target.file.full_path
severity
security_result.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_user
principal.user.user_display_name
src_user_bunit
principal.labels.key/value (deprecated)
additional.fields
src_user_category
principal.labels.key/value (deprecated)
additional.fields
src_user_priority
principal.labels.key/value (deprecated)
additional.fields
src_zone
principal.location.country_or_origin
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
All_Email
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Email:
Log field
UDM mapping
action
security_result.action_details
security_result.action
delay
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
file_hash
about.file.sha256, about.file.md5, about.file.sha1
file_name
about.labels.key/value (deprecated)
additional.fields
file_size
about.file.size
internal_message_id
metadata.product_log_id
message_id
network.email.mail_id
message_info
about.labels.key/value (deprecated)
additional.fields
orig_dest
target.labels.key/value (deprecated)
additional.fields
orig_recipient
about.labels.key/value (deprecated)
additional.fields
orig_src
network.email.from
process
principal.process.command_line
process_id
principal.process.pid
protocol
network.application_protocol
recipient
network.email.to
recipient_count
about.labels.key/value (deprecated)
additional.fields
recipient_domain
about.labels.key/value (deprecated)
additional.fields
recipient_status
about.labels.key/value (deprecated)
additional.fields
response_time
about.labels.key/value (deprecated)
additional.fields
retries
about.labels.key/value (deprecated)
additional.fields
return_addr
about.labels.key/value (deprecated)
additional.fields
size
about.labels.key/value (deprecated)
additional.fields
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_user
principal.user.email_addresses
src_user_bunit
principal.labels.key/value (deprecated)
additional.fields
src_user_category
principal.labels.key/value (deprecated)
additional.fields
src_user_domain
principal.administrative_domain
src_user_priority
principal.labels.key/value (deprecated)
additional.fields
status_code
about.labels.key/value (deprecated)
additional.fields
subject
network.email.subject(repeated)
tag
about.labels.key/value (deprecated)
additional.fields
url
about.url
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
xdelay
about.labels.key/value (deprecated)
additional.fields
xref
about.labels.key/value (deprecated)
additional.fields
Filtering
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Filtering:
Log field
UDM mapping
filter_action
about.labels.key/value (deprecated)
additional.fields
filter_score
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_extra
about.labels.key/value (deprecated)
additional.fields
signature_id
metadata.product_event_type
Ports
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Ports:
Log field
UDM mapping
creation_time
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_port
target.port
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
dest_should_timesync
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
process_guid
principal.process.product_specific_process_id
process_id
principal.process.pid
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_port
principal.port
src_requires_av
principal.labels.key/value (deprecated)
additional.fields
src_should_timesync
principal.labels.key/value (deprecated)
additional.fields
src_should_update
principal.labels.key/value (deprecated)
additional.fields
state
about.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
transport
network.ip_protocol
transport_dest_port
target.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
Processes
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Processes:
Log field
UDM mapping
action
security_result.action_details
security_result.action
cpu_load_percent
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_is_expected
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
dest_should_timesync
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
mem_used
about.labels.key/value (deprecated)
additional.fields
original_file_name
src.file.full_path
os
principal.asset.platform_software.platform_version
parent_process
about.labels.key/value (deprecated)
additional.fields
parent_process_exec
about.labels.key/value (deprecated)
additional.fields
parent_process_id
principal.process.parent_process.parent_pid
parent_process_guid
principal.process.parent_process.product_specific_process_id
parent_process_name
about.labels.key/value (deprecated)
additional.fields
parent_process_path
principal.process.parent_process.command_line
process
about.labels.key/value (deprecated)
additional.fields
process_current_directory
about.labels.key/value (deprecated)
additional.fields
process_exec
about.labels.key/value (deprecated)
additional.fields
process_hash
principal.process.file.sha256/principal.process.file.md5/principal..process.file.sha1
process_guid
principal.process.product_specific_process_id
process_id
principal.process.pid
process_integrity_level
security_result.severity
process_name
principal.process.command_line
process_path
principal.process.file.full_path
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_id
principal.user.userid
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
Services
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Services:
Log field
UDM mapping
description
security_result.description
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_is_expected
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
dest_should_timesync
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
process_guid
principal.process.product_specific_process_id
process_id
principal.process.pid
service
target.application
service_dll
about.labels.key/value (deprecated)
additional.fields
service_dll_path
about.file.full_path
service_dll_hash
about.labels.key/value (deprecated)
additional.fields
service_dll_signature_exists
about.labels.key/value (deprecated)
additional.fields
service_dll_signature_verified
about.labels.key/value (deprecated)
additional.fields
service_exec
target.process.file.full_path
service_hash
about.labels.key/value (deprecated)
additional.fields
service_id
about.labels.key/value (deprecated)
additional.fields
service_name
about.labels.key/value (deprecated)
additional.fields
service_path
about.labels.key/value (deprecated)
additional.fields
service_signature_exists
about.labels.key/value (deprecated)
additional.fields
service_signature_verified
about.labels.key/value (deprecated)
additional.fields
start_mode
about.labels.key/value (deprecated)
additional.fields
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
Filesystem
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Filesystem:
Log field
UDM mapping
action
security_result.action_details
security_result.action
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
dest_should_timesync
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
file_access_time
about.labels.key/value (deprecated)
additional.fields
file_create_time
target.asset.attribute.creation_time
file_hash
target.file.sha256, target.file.md5, target.file.sha1
file_modify_time
about.labels.key/value (deprecated)
additional.fields
file_name
about.labels.key/value (deprecated)
additional.fields
file_path
target.file.full_path
file_acl
about.labels.key/value (deprecated)
additional.fields
file_size
target.file.size
process_guid
principal.process.product_specific_process_id
process_id
principal.process.pid
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
Registry
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Registry:
Log field
UDM mapping
action
security_result.action_details
security_result.action
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
dest_should_timesync
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
process_guid
principal.process.product_specific_process_id
process_id
principal.process.pid
registry_hive
about.labels.key/value (deprecated)
additional.fields
registry_path
about.labels.key/value (deprecated)
additional.fields
registry_key_name
target.registry.registry_key
registry_value_data
target.registry.registry_value_data
registry_value_name
target.registry.registry_value_name
registry_value_text
about.labels.key/value (deprecated)
additional.fields
registry_value_type
about.labels.key/value (deprecated)
additional.fields
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
Signatures
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Signatures:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
tag
about.labels.key/value (deprecated)
additional.fields
Signatures_vendor_product
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Signatures_vendor_product:
Log field
UDM mapping
vendor_product
about.labels.key/value (deprecated)
additional.fields
All_Interprocess_Messaging
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Interprocess_Messaging:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
endpoint
about.labels.key/value (deprecated)
additional.fields
endpoint_version
about.labels.key/value (deprecated)
additional.fields
message
about.labels.key/value (deprecated)
additional.fields
message_consumed_time
about.labels.key/value (deprecated)
additional.fields
message_correlation_id
about.labels.key/value (deprecated)
additional.fields
message_delivered_time
about.labels.key/value (deprecated)
additional.fields
message_delivery_mode
about.labels.key/value (deprecated)
additional.fields
message_expiration_time
about.labels.key/value (deprecated)
additional.fields
message_id
metadata.product.log_id
message_priority
about.labels.key/value (deprecated)
additional.fields
message_properties
about.labels.key/value (deprecated)
additional.fields
message_received_time
about.labels.key/value (deprecated)
additional.fields
message_redelivered
about.labels.key/value (deprecated)
additional.fields
message_reply_dest
target.labels.key/value (deprecated)
additional.fields
message_type
about.labels.key/value (deprecated)
additional.fields
parameters
about.labels.key/value (deprecated)
additional.fields
payload
about.labels.key/value (deprecated)
additional.fields
payload_type
about.labels.key/value (deprecated)
additional.fields
request_payload
about.labels.key/value (deprecated)
additional.fields
request_payload_type
about.labels.key/value (deprecated)
additional.fields
request_sent_time
about.labels.key/value (deprecated)
additional.fields
response_code
network.http.response_code
response_payload_type
about.labels.key/value (deprecated)
additional.fields
response_received_time
about.labels.key/value (deprecated)
additional.fields
response_time
about.labels.key/value (deprecated)
additional.fields
return_message
about.labels.key/value (deprecated)
additional.fields
rpc_protocol
network.application_protocol
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
IDS_Attacks
The following table lists the log fields and corresponding UDM mappings for the Splunk data set IDS_Attacks:
Log field
UDM mapping
action
security_result.action_details
security_result.action
category
security_result.category_details
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dvc
principal.asset.hostname, principal.asset.ip
dvc_bunit
about.labels.key/value (deprecated)
additional.fields
dvc_category
about.labels.key/value (deprecated)
additional.fields
dvc_priority
about.labels.key/value (deprecated)
additional.fields
file_hash
target.file.sha256, target.file.md5, target.file.sha1
file_name
about.labels.key/value (deprecated)
additional.fields
file_path
target.file.full_path
ids_type
about.labels.key/value (deprecated)
additional.fields
severity
security_result.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_port
principal.port
tag
about.labels.key/value (deprecated)
additional.fields
transport
network.ip_protocol
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
DS_Attacks
The following table lists the log fields and corresponding UDM mappings for the Splunk data set DS_Attacks:
Log field
UDM mapping
dest_port
target.port
All_Inventory
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Inventory:
Log field
UDM mapping
description
security_result.description
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
enabled
about.labels.key/value (deprecated)
additional.fields
family
about.labels.key/value (deprecated)
additional.fields
hypervisor_id
about.labels.key/value (deprecated)
additional.fields
serial
principal.asset.hardware.serial_number
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
version
about.labels.key/value (deprecated)
additional.fields
CPU
The following table lists the log fields and corresponding UDM mappings for the Splunk data set CPU:
Log field
UDM mapping
cpu_cores
principal.asset.hardware.cpu_number_cores
cpu_count
about.labels.key/value (deprecated)
additional.fields
cpu_mhz
principal.asset.hardware.cpu_clock_speed
cpu_load_mhz
principal.asset.hardware.cpu_clock_speed
cpu_load_percent
about.labels.key/value (deprecated)
additional.fields
cpu_time
about.labels.key/value (deprecated)
additional.fields
cpu_user_percent
about.labels.key/value (deprecated)
additional.fields
Memory
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Memory:
Log field
UDM mapping
mem
principal.asset.hardware.ram
heap_committed
about.labels.key/value (deprecated)
additional.fields
heap_initial
about.labels.key/value (deprecated)
additional.fields
heap_max
about.labels.key/value (deprecated)
additional.fields
heap_used
about.labels.key/value (deprecated)
additional.fields
non_heap_committed
about.labels.key/value (deprecated)
additional.fields
non_heap_initial
about.labels.key/value (deprecated)
additional.fields
non_heap_max
about.labels.key/value (deprecated)
additional.fields
non_heap_used
about.labels.key/value (deprecated)
additional.fields
objects_pending
about.labels.key/value (deprecated)
additional.fields
mem
principal.asset.hardware.ram
mem_committed
about.labels.key/value (deprecated)
additional.fields
mem_free
about.labels.key/value (deprecated)
additional.fields
mem_used
about.labels.key/value (deprecated)
additional.fields
swap
about.labels.key/value (deprecated)
additional.fields
swap_free
about.labels.key/value (deprecated)
additional.fields
swap_used
about.labels.key/value (deprecated)
additional.fields
network
The following table lists the log fields and corresponding UDM mappings for the Splunk data set network:
Log field
UDM mapping
dest_ip
target.ip
dns
about.labels.key/value (deprecated)
additional.fields
inline_nat
about.labels.key/value (deprecated)
additional.fields
interface
about.labels.key/value (deprecated)
additional.fields
ip
principal.asset.ip
lb_method
about.labels.key/value (deprecated)
additional.fields
mac
principal.asset.mac
name
principal.resource.name
node
about.labels.key/value (deprecated)
additional.fields
node_port
target.port
src_ip
principal.ip
vip_port
about.labels.key/value (deprecated)
additional.fields
thruput
about.labels.key/value (deprecated)
additional.fields
thruput_max
about.labels.key/value (deprecated)
additional.fields
OS
The following table lists the log fields and corresponding UDM mappings for the Splunk data set OS:
Log field
UDM mapping
os
principal.asset.platform_software.platform_version
committed_memory
about.labels.key/value (deprecated)
additional.fields
cpu_time
about.labels.key/value (deprecated)
additional.fields
free_physical_memory
about.labels.key/value (deprecated)
additional.fields
free_swap
about.labels.key/value (deprecated)
additional.fields
max_file_descriptors
about.labels.key/value (deprecated)
additional.fields
open_file_descriptors
about.labels.key/value (deprecated)
additional.fields
os
principal.asset.platform_software.platform_version
os_architecture
about.labels.key/value (deprecated)
additional.fields
os_version
about.labels.key/value (deprecated)
additional.fields
physical_memory
about.labels.key/value (deprecated)
additional.fields
swap_space
about.labels.key/value (deprecated)
additional.fields
system_load
about.labels.key/value (deprecated)
additional.fields
total_processors
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
Storage
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Storage:
Log field
UDM mapping
array
about.labels.key/value (deprecated)
additional.fields
blocksize
about.labels.key/value (deprecated)
additional.fields
cluster
about.resource.resource_type = "CLUSTER"
fd_max
about.labels.key/value (deprecated)
additional.fields
latency
about.labels.key/value (deprecated)
additional.fields
mount
principal.resource.attribute.labels.key/value
parent
principal.resource.parent
read_blocks
about.labels.key/value (deprecated)
additional.fields
read_latency
about.labels.key/value (deprecated)
additional.fields
read_ops
about.labels.key/value (deprecated)
additional.fields
storage
about.labels.key/value (deprecated)
additional.fields
write_blocks
about.labels.key/value (deprecated)
additional.fields
write_latency
about.labels.key/value (deprecated)
additional.fields
write_ops
about.labels.key/value (deprecated)
additional.fields
array
about.labels.key/value (deprecated)
additional.fields
blocksize
about.labels.key/value (deprecated)
additional.fields
cluster
about.resource.resource_type = "CLUSTER"
fd_max
about.labels.key/value (deprecated)
additional.fields
fd_used
about.labels.key/value (deprecated)
additional.fields
latency
about.labels.key/value (deprecated)
additional.fields
mount
about.labels.key/value (deprecated)
additional.fields
parent
principal.resource.parent
read_blocks
about.labels.key/value (deprecated)
additional.fields
read_latency
about.labels.key/value (deprecated)
additional.fields
read_ops
about.labels.key/value (deprecated)
additional.fields
storage
about.labels.key/value (deprecated)
additional.fields
storage_free
about.labels.key/value (deprecated)
additional.fields
storage_free_percent
about.labels.key/value (deprecated)
additional.fields
storage_used
about.labels.key/value (deprecated)
additional.fields
storage_used_percent
about.labels.key/value (deprecated)
additional.fields
write_blocks
about.labels.key/value (deprecated)
additional.fields
write_latency
about.labels.key/value (deprecated)
additional.fields
write_ops
about.labels.key/value (deprecated)
additional.fields
error_code
security_result.description
operation
about.labels.key/value (deprecated)
additional.fields
storage_name
about.resource.name
User
The following table lists the log fields and corresponding UDM mappings for the Splunk data set User:
Log field
UDM mapping
interactive
about.labels.key/value (deprecated)
additional.fields
password
about.labels.key/value (deprecated)
additional.fields
shell
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_id
principal.user.userid
user_priority
principal.user.attribute.label.key/value
Virtual_OS
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Virtual_OS:
Log field
UDM mapping
hypervisor
about.labels.key/value (deprecated)
additional.fields
Snapshot
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Snapshot:
Log field
UDM mapping
size
about.file.size
snapshot
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
JVM
The following table lists the log fields and corresponding UDM mappings for the Splunk data set JVM:
Log field
UDM mapping
jvm_description
security_result.description
tag
about.labels.key/value (deprecated)
additional.fields
Threading
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Threading:
Log field
UDM mapping
cm_enabled
about.labels.key/value (deprecated)
additional.fields
cm_supported
about.labels.key/value (deprecated)
additional.fields
cpu_time_enabled
about.labels.key/value (deprecated)
additional.fields
cpu_time_supported
about.labels.key/value (deprecated)
additional.fields
current_cpu_time
about.labels.key/value (deprecated)
additional.fields
current_user_time
about.labels.key/value (deprecated)
additional.fields
daemon_thread_count
about.labels.key/value (deprecated)
additional.fields
omu_supported
about.labels.key/value (deprecated)
additional.fields
peak_thread_count
about.labels.key/value (deprecated)
additional.fields
synch_supported
about.labels.key/value (deprecated)
additional.fields
thread_count
about.labels.key/value (deprecated)
additional.fields
threads_started
about.labels.key/value (deprecated)
additional.fields
Runtime
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Runtime:
Log field
UDM mapping
process_name
principal.process.command_line
start_time
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
version
about.labels.key/value (deprecated)
additional.fields
Compilation
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Compilation:
Log field
UDM mapping
compilation_time
about.labels.key/value (deprecated)
additional.fields
Classloading
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Classloading:
Log field
UDM mapping
current_loaded
about.labels.key/value (deprecated)
additional.fields
total_loaded
about.labels.key/value (deprecated)
additional.fields
total_unloaded
about.labels.key/value (deprecated)
additional.fields
Malware_Attacks
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Malware_Attacks:
Log field
UDM mapping
action
security_result.action_details
security_result.action
category
security_result.category_details
date
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_nt_domain
target.administrative_domain
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
file_hash
target.file.sha256, target.file.md5, target.file.sha1
file_name
about.labels.key/value (deprecated)
additional.fields
file_path
target.file.full_path
severity
security_result.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_user
principal.user.user_display_name
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
url
about.url
vendor_product
about.labels.key/value (deprecated)
additional.fields
Malware_Operations
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Malware_Operations:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_nt_domain
target.labels.key/value (deprecated)
additional.fields
dest_nt_domain
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_requires_av
target.labels.key/value (deprecated)
additional.fields
product_version
about.labels.key/value (deprecated)
additional.fields
signature_version
security_result.rule_version
tag
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
Malware_Operations
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Malware_Operations:
Log field
UDM mapping
dest_category
target.labels.key/value (deprecated)
additional.fields
DNS
The following table lists the log fields and corresponding UDM mappings for the Splunk data set DNS:
Log field
UDM mapping
additional_answer_count
about.labels.key/value (deprecated)
additional.fields
answer
network.dns.answer.data
answer_count
about.labels.key/value (deprecated)
additional.fields
authority_answer_count
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_port
target.port
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
message_type
about.labels.key/value (deprecated)
additional.fields
name
about.labels.key/value (deprecated)
additional.fields
query
network.dns.questions.name
query_count
about.labels.key/value (deprecated)
additional.fields
query_type
network.dns.questions.type
record_type
network.dns.answer.type(uint32)
reply_code
about.labels.key/value (deprecated)
additional.fields
reply_code_id
network.dns.response_code
response_time
about.labels.key/value (deprecated)
additional.fields
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_port
principal.port
src_priority
principal.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
transaction_id
network.dns.id
transport
network.ip_protocol
ttl
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
All_Sessions
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Sessions:
Log field
UDM mapping
action
security_result.action_details
security_result.action
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_dns
target.labels.key/value (deprecated)
additional.fields
dest_ip
network.dhcp.ciaddr
dest_mac
network.dhcp.chaddr
dest_nt_host
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
duration
network.session_duration
response_time
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_dns
principal.labels.key/value (deprecated)
additional.fields
src_ip
principal.ip
src_mac
principal.mac
src_nt_host
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
DHCP
The following table lists the log fields and corresponding UDM mappings for the Splunk data set DHCP:
Log field
UDM mapping
lease_duration
network.dhcp.lease_time_second
lease_scope
about.labels.key/value (deprecated)
additional.fields
All_Traffic
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Traffic:
Log field
UDM mapping
action
security_result.action_details
security_result.action
app
network.application_protocol
bytes
about.labels.key/value (deprecated)
additional.fields
bytes_in
network.received_bytes
bytes_out
network.sent_bytes
channel
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_interface
target.labels.key/value (deprecated)
additional.fields
dest_ip
target.ip
dest_mac
target.mac
dest_port
target.port
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_translated_ip
target.nat_ip
dest_translated_port
target.nat_port
dest_zone
target.location.country_or_origin
direction
network.direction
duration
network.session_duration
dvc
principal.asset.hostname, principal.asset.ip
dvc_bunit
about.labels.key/value (deprecated)
additional.fields
dvc_category
about.labels.key/value (deprecated)
additional.fields
dvc_ip
about.labels.key/value (deprecated)
additional.fields
dvc_mac
principal.asset.mac
dvc_priority
about.labels.key/value (deprecated)
additional.fields
dvc_zone
principal.asset.location.country_or_region
flow_id
about.labels.key/value (deprecated)
additional.fields
icmp_code
about.labels.key/value (deprecated)
additional.fields
icmp_type
about.labels.key/value (deprecated)
additional.fields
packets
about.labels.key/value (deprecated)
additional.fields
packets_in
about.labels.key/value (deprecated)
additional.fields
packets_out
about.labels.key/value (deprecated)
additional.fields
protocol
about.labels.key/value (deprecated)
additional.fields
protocol_version
about.labels.key/value (deprecated)
additional.fields
response_time
about.labels.key/value (deprecated)
additional.fields
rule
security_result.rule_id
session_id
network.session_id
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_interface
principal.labels.key/value (deprecated)
additional.fields
src_ip
principal.ip
src_mac
principal.mac
src_port
principal.port
src_priority
principal.labels.key/value (deprecated)
additional.fields
src_translated_ip
principal.nat_ip
src_translated_port
principal.nat_port
src_zone
principal.location.country_or_origin
ssid
about.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
tcp_flag
about.labels.key/value (deprecated)
additional.fields
transport
network.ip_protocol
tos
about.labels.key/value (deprecated)
additional.fields
ttl
network.dns.additional.ttl
user
principal.user.userid
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_account
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
vlan
about.labels.key/value (deprecated)
additional.fields
wifi
about.labels.key/value (deprecated)
additional.fields
All_Performance
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Performance:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_should_timesync
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
hypervisor_id
about.labels.key/value (deprecated)
additional.fields
resource_type
about.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
Facilities
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Facilities:
Log field
UDM mapping
fan_speed
about.labels.key/value (deprecated)
additional.fields
power
about.labels.key/value (deprecated)
additional.fields
temperature
about.labels.key/value (deprecated)
additional.fields
Timesync
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Timesync:
Log field
UDM mapping
action
security_result.action_details
security_result.action
Uptime
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Uptime:
Log field
UDM mapping
uptime
about.labels.key/value (deprecated)
additional.fields
View_Activity
The following table lists the log fields and corresponding UDM mappings for the Splunk data set View_Activity:
Log field
UDM mapping
app
target.application
spent
about.labels.key/value (deprecated)
additional.fields
uri
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
view
about.labels.key/value (deprecated)
additional.fields
Datamodel_Acceleration
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Datamodel_Acceleration:
Log field
UDM mapping
access_count
about.labels.key/value (deprecated)
additional.fields
access_time
about.labels.key/value (deprecated)
additional.fields
app
target.application
buckets
about.labels.key/value (deprecated)
additional.fields
buckets_size
about.labels.key/value (deprecated)
additional.fields
complete
about.labels.key/value (deprecated)
additional.fields
cron
about.labels.key/value (deprecated)
additional.fields
datamodel
about.labels.key/value (deprecated)
additional.fields
digest
about.labels.key/value (deprecated)
additional.fields
earliest
about.labels.key/value (deprecated)
additional.fields
is_inprogress
about.labels.key/value (deprecated)
additional.fields
last_error
about.labels.key/value (deprecated)
additional.fields
last_sid
about.labels.key/value (deprecated)
additional.fields
latest
about.labels.key/value (deprecated)
additional.fields
mod_time
about.labels.key/value (deprecated)
additional.fields
retention
about.labels.key/value (deprecated)
additional.fields
size
about.file.size
summary_id
about.labels.key/value (deprecated)
additional.fields
Search_Activity
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Search_Activity:
Log field
UDM mapping
host
about.hostname
info
about.labels.key/value (deprecated)
additional.fields
search
about.labels.key/value (deprecated)
additional.fields
search_et
about.labels.key/value (deprecated)
additional.fields
search_lt
about.labels.key/value (deprecated)
additional.fields
search_type
about.labels.key/value (deprecated)
additional.fields
source
principal.labels.key/value (deprecated)
additional.fields
sourcetype
principal.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
Scheduler_Activity
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Scheduler_Activity:
Log field
UDM mapping
app
target.application
host
about.hostname
savedsearch_name
about.labels.key/value (deprecated)
additional.fields
sid
about.labels.key/value (deprecated)
additional.fields
source
principal.labels.key/value (deprecated)
additional.fields
sourcetype
principal.labels.key/value (deprecated)
additional.fields
splunk_server
principal.ip, principal.hostname
status
security_result.summary
user
principal.user.user_display_name
Web_Service_Errors
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Web_Service_Errors:
Log field
UDM mapping
host
about.hostname
source
principal.labels.key/value (deprecated)
additional.fields
sourcetype
principal.labels.key/value (deprecated)
additional.fields
event_id
security_result.rule_name
Modular_Actions
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Modular_Actions:
Log field
UDM mapping
action_mode
about.labels.key/value (deprecated)
additional.fields
action_status
about.labels.key/value (deprecated)
additional.fields
app
target.application
duration
network.session_duration
component
about.labels.key/value (deprecated)
additional.fields
orig_rid
about.labels.key/value (deprecated)
additional.fields
orig_sid
about.labels.key/value (deprecated)
additional.fields
rid
about.labels.key/value (deprecated)
additional.fields
search_name
about.labels.key/value (deprecated)
additional.fields
action_name
security_result.action_details
signature
metadata.description
sid
about.labels.key/value (deprecated)
additional.fields
user
about.labels.key/value (deprecated)
additional.fields
All_Ticket_Management
The following table lists the log fields and corresponding UDM mappings for the Splunk data set All_Ticket_Management:
Log field
UDM mapping
affect_dest
target.labels.key/value (deprecated)
additional.fields
comments
about.labels.key/value (deprecated)
additional.fields
description
security_result.description
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
priority
security_result.priority_details
severity
security_result.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
splunk_id
about.labels.key/value (deprecated)
additional.fields
splunk_realm
about.labels.key/value (deprecated)
additional.fields
src_user
principal.user.user_display_name
src_user_bunit
principal.labels.key/value (deprecated)
additional.fields
src_user_category
principal.labels.key/value (deprecated)
additional.fields
src_user_priority
principal.labels.key/value (deprecated)
additional.fields
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
ticket_id
target.user.attribute.label.ley/value
time_submitted
principal.user.attribute.creation_time
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
Change
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Change:
Log field
UDM mapping
change
about.labels.key/value (deprecated)
additional.fields
Incident
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Incident:
Log field
UDM mapping
incident
about.labels.key/value (deprecated)
additional.fields
Problem
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Problem:
Log field
UDM mapping
problem
about.labels.key/value (deprecated)
additional.fields
Updates
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Updates:
Log field
UDM mapping
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_should_update
target.labels.key/value (deprecated)
additional.fields
dvc
principal.asset.hostname, principal.asset.ip
file_hash
target.file.sha256, target.file.md5, target.file.sha1
file_name
about.labels.key/value (deprecated)
additional.fields
severity
security_result.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
status
security_result.summary
tag
about.labels.key/value (deprecated)
additional.fields
vendor_product
about.labels.key/value (deprecated)
additional.fields
Vulnerabilities
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Vulnerabilities:
Log field
UDM mapping
bugtraq
about.labels.key/value (deprecated)
additional.fields
category
security_result.category_details
cert
about.labels.key/value (deprecated)
additional.fields
cve
vulnerabilites.cve_description
cvss
vulnerabilites.cvss_base_score
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dvc
principal.asset.hostname, principal.asset.ip
dvc_bunit
about.labels.key/value (deprecated)
additional.fields
dvc_category
about.labels.key/value (deprecated)
additional.fields
dvc_priority
about.labels.key/value (deprecated)
additional.fields
msft
about.labels.key/value (deprecated)
additional.fields
mskb
about.labels.key/value (deprecated)
additional.fields
severity
extensions.vulns.vulnerabilites.severity
severity_id
about.labels.key/value (deprecated)
additional.fields
signature
metadata.description
signature_id
metadata.product_event_type
tag
about.labels.key/value (deprecated)
additional.fields
url
extensions.vulns.vulnerabilites.about.url
user
extensions.vulns.vulnerabilites.about.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
xref
about.labels.key/value (deprecated)
additional.fields
Web
The following table lists the log fields and corresponding UDM mappings for the Splunk data set Web:
Log field
UDM mapping
action
security_result.action_details
security_result.action
app
target.application
bytes
about.labels.key/value (deprecated)
additional.fields
bytes_in
network.received_bytes
bytes_out
network.sent_bytes
cached
about.labels.key/value (deprecated)
additional.fields
category
security_result.category_details
cookie
about.labels.key/value (deprecated)
additional.fields
dest
target.ip
target.hostname
target.labels.key/value (deprecated)
dest_bunit
target.labels.key/value (deprecated)
additional.fields
dest_category
target.labels.key/value (deprecated)
additional.fields
dest_priority
target.labels.key/value (deprecated)
additional.fields
dest_port
target.port
duration
network.session_duration
http_content_type
about.labels.key/value (deprecated)
additional.fields
http_method
network.http.method
http_referrer
network.http.referral_url
http_referrer_domain
about.labels.key/value (deprecated)
additional.fields
http_user_agent
network.http.user_agent
http_user_agent_length
about.labels.key/value (deprecated)
additional.fields
response_time
about.labels.key/value (deprecated)
additional.fields
site
about.labels.key/value (deprecated)
additional.fields
src
principal.ip
principal.hostname
principal.labels.key/value (deprecated)
src_bunit
principal.labels.key/value (deprecated)
additional.fields
src_category
principal.labels.key/value (deprecated)
additional.fields
src_priority
principal.labels.key/value (deprecated)
additional.fields
status
network.http.response_code
tag
about.labels.key/value (deprecated)
additional.fields
uri_path
about.labels.key/value (deprecated)
additional.fields
uri_query
about.labels.key/value (deprecated)
additional.fields
url
about.url
url_domain
about.asset.network_domain
url_length
about.labels.key/value (deprecated)
additional.fields
user
principal.user.user_display_name
user_bunit
about.labels.key/value (deprecated)
additional.fields
user_category
principal.user.attribute.labels.key/value
user_priority
principal.user.attribute.label.key/value
vendor_product
about.labels.key/value (deprecated)
additional.fields
UDM event types
The following table lists the Splunk tags and the corresponding UDM event types:
Data model
Splunk tags
UDM event type
Alerts
alert
STATUS_UPDATE
Authentication
authentication
USER_UNCATEGORIZED
Certificate
certificate
NETWORK_UNCATEGORIZED
Change
change
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Data Access
data, access
USER_RESOURCE_ACCESS
Databases
database
USER_RESOURCE_ACCESS
Databases
database, instance, stats
STATUS_UPDATE
Databases
database, instance, status
STATUS_UPDATE
Databases
database, instance, lock
STATUS_UPDATE
Databases
database, query
STATUS_UPDATE
Databases
database, query, tablespace
STATUS_UPDATE
Databases
database, query, stats
STATUS_UPDATE
Data Loss Prevention
dlp, incident
SCAN_UNCATEGORIZED
Email
email
EMAIL_UNCATEGORIZED
Email
email, delivery
EMAIL_TRANSACTION
Endpoint
listening, port
SERVICE_UNSPECIFIED
Endpoint
process, report
PROCESS_UNCATEGORIZED
Endpoint
service, report
SERVICE_UNSPECIFIED
Endpoint
endpoint, filesystem
FILE_UNCATEGORIZED
Endpoint
endpoint, registry
REGISTRY_UNCATEGORIZED
Event Signature
track_event_signature
STATUS_UPDATE
Inter Process Messaging
messaging
STATUS_UPDATE
Instrusion Detection
ids, attack
SERVICE_UNSPECIFIED
Inventory
inventory
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Java Virtual Machine (JVM)
jvm
SYSTEM_AUDIT_LOG_UNCATEGORIZED
Malware
malware
STATUS_UPDATE
Network Resolution(DNS)
network, resolution, dns
NETWORK_DNS
Network Sessions
network, session
NETWORK_CONNECTION
Network Sessions
network, session, dhcp
NETWORK_DHCP
Network Traffic
network, communicate
NETWORK_CONNECTION
Performance
performance
SERVICE_UNSPECIFIED
Splunk Audit Logs
modaction
STATUS_UPDATE
Ticket Management
ticketing
STATUS_UPDATE
Ticket Management
ticketing, change
STATUS_UPDATE
Updates
update
STATUS_UPDATE
Vulnerabilities
report, vulnerabilites
SCAN_UNCATEGORIZED
Web
web
NETWORK_UNCATEGORIZED
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
