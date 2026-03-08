# Collect Zscaler Deception logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/zscaler-deception/  
**Scraped:** 2026-03-05T09:49:01.397149Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Zscaler Deception logs
Supported in:
Google secops
SIEM
This document describes how you can export Zscaler Deception logs by setting up a BindPlane agent and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps
.
A typical deployment consists of Zscaler Deception and the BindPlane agent configured to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Zscaler Deception
: The platform from which you collect logs.
BindPlane Agent
: The BindPlane agent fetches logs from Zscaler Deception and sends logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
ZSCALER_DECEPTION
ingestion label.
Before you begin
Ensure that you have access to the Zscaler Deception console. For more information, see
Zscaler Deception Help
Ensure that you are using Zscaler Deception 2024 or later.
Ensure that all systems in the deployment architecture are configured with the UTC time zone.
Ensure that the
Service Connector
is configured that communicates with the Zscaler Deception Admin Portal and sends event logs. For more information about
Service Connector
, see
About Service Connectors
.
Configure a Service Connector to Forward Events to BindPlane Agent
Use the following steps to configure a Service Connector to forward events to a BindPlane Agent:
In the Zscaler Deception Admin Portal, go to
Orchestrate
>
SIEM Integrations
.
Click
Add Integration
, and select
Syslog
from the menu.
In the
Syslog Details
window, enter the details.
Enter a name for the Syslog SIEM integration in the
Name
field.
Select
Enable
under
Enabled
to activate SIEM integration.
Select a
Service Connector
from the menu:
If you select a
Service Connector
that is configured in the Zscaler Deception Administrator Portal, the administrator portal sends logs to Syslog.
If you select a
Service Connector
that is configured on a
Decoy Connector
, the selected
Decoy Connector
sends logs to Syslog.
Select
Events
to forward Zscaler Deception events in the
Type of logs
menu.
Select enable in
Include Safe Events
to forward the events that are marked as
safe
to Syslog.
In the
Filter
field, enter a query to send only filtered event logs to Syslog. If left blank, all event logs are sent. To learn how to build queries, see
Understanding and Building Queries
.
Enter the IP address of the Linux Virtual Machine in the
Host
field.
Enter the port number that the Linux Virtual Machine is listening to in the
Port
field.
Select the protocol used to forward Zscaler Deception events in the
Transport
menu.
Select a facility code in the
Facility
menu. Each event is labeled with a facility code, indicating the type of software generating the event logs.
Select a severity level in the
Severity
menu. Each event is labeled with a severity, indicating the severity of the tool generating the event logs.
Enter a log identifier in the
App Name
field.
Click
Save
.
For more information about how to configure a Service Connector, see the
SIEM Configuration Guide for Syslog
.
Forward Logs to Google SecOps using BindPlane Agent
Install and set up a
Linux Virtual Machine
.
Install and configure the BindPlane Agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the BindPlane Agent, see
the BindPlane Agent installation and configuration instructions
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Field mapping reference
Field mapping reference: Event Identifier to Event Type
The following table lists the
ZSCALER_DECEPTION
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
amqp
USER_RESOURCE_ACCESS
aws
USER_STATS
azure
USER_STATS
credtheft
ACL_VIOLATION
custom
USER_STATS
email
EMAIL_TRANSACTION
endpoint
NETWORK_MALICIOUS
itdr
NETWORK_MALICIOUS
ransomware
NETWORK_MALICIOUS
filetheft
USER_RESOURCE_ACCESS
ACL_VIOLATION
mitm
NETWORK_CONNECTION
mongodb
USER_RESOURCE_ACCESS
network
NETWORK_SUSPICIOUS
postgresql
USER_RESOURCE_ACCESS
QOS
USER_RESOURCE_ACCESS
recon
NETWORK_RECON
scada
USER_RESOURCE_ACCESS
ssh
telnet
web
windows
NETWORK_MALICIOUS
Field mapping reference: ZSCALER_DECEPTION - Common Fields
The following table lists common fields of the
ZSCALER_DECEPTION
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.product_name
Json dataendthe
metadata.product_name
UDM field is set to
Deception
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Zscaler
.
timestamp
metadata.event_timestamp
Field mapping reference: ZSCALER_DECEPTION - amqp
The following table lists the raw log fields for the
amqp
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
network.application_protocol
If the
type
log field value is equal to
amqp
, then the
network.application_protocol
UDM field is set to
AMQP
.
amqp.connection_id
network.session_id
amqp.user
principal.user.userid
amqp.vhost
target.hostname
amqp.node
target.resource.name
target.resource.resource_type
If the
amqp.node
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
CLUSTER
.
amqp.channel
additional.fields[amqp_channel]
amqp.exchange
additional.fields[amqp_exchange]
amqp.payload
additional.fields[amqp_payload]
amqp.queue
additional.fields[amqp_queue]
amqp.routed_queues
additional.fields[amqp_routed_queues]
The
amqp.routed_queues
log field is mapped to the
additional.fields.value.string_value
UDM field.
amqp.routing_keys
additional.fields[amqp_routing_keys]
The
amqp.routing_keys
log field is mapped to the
additional.fields.value.string_value
UDM field.
Field mapping reference: ZSCALER_DECEPTION - aws
The following table lists the raw log fields for the
aws
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
aws.event_id
metadata.product_log_id
aws.user_agent
network.http.user_agent
aws.error_message
security_result.description
decoy.s3.dataset
security_result.rule_set
aws.error_code
security_result.summary
aws.aws_region
target.location.country_or_region
aws.vpc_endpoint_id
target.resource_ancestors.product_object_id
target.resource_ancestors.resource_type
If the
aws.vpc_endpoint_id
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
aws.recipient_account_id
target.resource.product_object_id
target.resource.resource_type
If the
aws.recipient_account_id
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
aws.event_name
additional.fields[aws_event_name]
aws.event_source
additional.fields[aws_event_source]
aws.event_type
additional.fields[aws_event_type]
aws.readonly
additional.fields[aws_readonly]
aws.request_id
additional.fields[aws_request_id]
decoy.public
additional.fields[decoy_public]
Field mapping reference: ZSCALER_DECEPTION - azure
The following table lists the raw log fields for the
azure
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
azure.caller_ip_address.port
principal.port
decoy.dataset
security_result.rule_set
decoy.storage_account
target.resource.name
target.resource.resource_type
If the
decoy.storage_account
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
decoy.public
additional.fields[decoy_public]
decoy.storage_account_container.dataset
additional.fields[decoy_storage_account_container_dataset]
Field mapping reference: ZSCALER_DECEPTION - credtheft
The following table lists the raw log fields for the
credtheft
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
credtheft.logon_process_name
extensions.auth.auth_details
extensions.auth.mechanism
If the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)interactive
, then the
extensions.auth.mechanism
UDM field is set to
INTERACTIVE
.
Else, if the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)network
, then the
extensions.auth.mechanism
UDM field is set to
NETWORK
.
Else, if the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)batch
, then the
extensions.auth.mechanism
UDM field is set to
BATCH
.
Else, if the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)service
, then the
extensions.auth.mechanism
UDM field is set to
SERVICE
.
Else, if the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)remoteinteractive
, then the
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
Else, if the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)unlock
, then the
extensions.auth.mechanism
UDM field is set to
UNLOCK
.
Else, if the
credtheft.logon_type
log field value matches the regular expression pattern
(?i)cached
, then the
extensions.auth.mechanism
UDM field is set to
CACHED_INTERACTIVE
.
Else, if the
credtheft.logon_type
log field value is
not
empty, then the
extensions.auth.mechanism
UDM field is set to
MECHANISM_OTHER
.
credtheft.event_id
metadata.description
metadata.event_type
If (the
credtheft.ip_address
log field value is
not
empty or the
credtheft.workstation
log field value is
not
empty or the
credtheft.workstation_name
log field value is
not
empty) and (the
credtheft.username
log field value is
not
empty or the
credtheft.subject_user_name
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
type
metadata.product_event_type
credtheft.event_record_id
metadata.product_log_id
credtheft.authentication_package_name
principal.application
credtheft.subject_domain_name
principal.domain.name
credtheft.workstation
principal.hostname
If the
credtheft.workstation
log field value is
not
empty, then the
credtheft.workstation
log field is mapped to the
principal.hostname
UDM field.
credtheft.workstation_name
principal.hostname
If the
credtheft.workstation_name
log field value is
not
empty, then the
credtheft.workstation_name
log field is mapped to the
principal.hostname
UDM field.
credtheft.ip_address
principal.ip
credtheft.ip_port
principal.port
credtheft.trigger_properties
principal.resource.attribute.labels[credtheft_trigger_properties]
credtheft.service_name
principal.resource.name
principal.resource.resource_type
If the
credtheft.service_name
log field value is
not
empty, then the
principal.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
credtheft.subject_logon_id
principal.user.product_object_id
credtheft.subject_user_sid
principal.user.windows_sid
security_result.action
If the
credtheft.status
log field value matches the regular expression pattern
(?i)successful
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
credtheft.status
log field value matches the regular expression pattern
(?i)failed
, then the
security_result.action
UDM field is set to
FAIL
.
Else, if the
credtheft.status
log field value matches the regular expression pattern
(?i)denied
, then the
security_result.action
UDM field is set to
BLOCK
.
credtheft.status
security_result.action_details
credtheft.operation_type
security_result.action_details
security_result.category
The
security_result.category
UDM field is set to
NETWORK_MALICIOUS
.
credtheft.access_list
security_result.detection_fields[credtheft_access_list]
credtheft.access_mask
security_result.detection_fields[credtheft_access_mask]
credtheft.ticket_encryption_type
security_result.detection_fields[credtheft_ticket_encryption_type]
credtheft.ticket_options
security_result.detection_fields[credtheft_ticket_options]
decoy.ad.asrep_roastable
security_result.detection_fields[decoy_ad_asrep_roastable]
decoy.ad.can_password_expire
security_result.detection_fields[decoy_ad_can_password_expire]
credtheft.target_domain_name
target.domain.name
credtheft.target_server_name
target.domain.name_server
credtheft.object_server
target.domain.name_server
credtheft.properties
target.resource.attribute.labels[credtheft_properties]
credtheft.sub_status
target.resource.attribute.labels[credtheft_sub_status]
credtheft.object_name
target.resource.name
credtheft.object_type
target.resource.resource_subtype
target.resource.resource_type
If the
credtheft.object_type
log field value matches the regular expression pattern
(?i)user
, then the
target.resource.resource_type
UDM field is set to
USER
.
Else, if the
credtheft.object_type
log field value matches the regular expression pattern
(?i)computer
, then the
target.resource.resource_type
UDM field is set to
DEVICE
.
decoy.ad.profile_path
target.user.attribute.labels[decoy_ad_profile_path]
decoy.ad.group_memberships
target.user.group_identifiers
The
decoy.ad.group_memberships
log field is mapped to the
target.user.group_identifiers
UDM field.
credtheft.target_user_name
target.user.user_display_name
credtheft.username
target.user.userid
credtheft.subject_user_name
target.user.userid
credtheft.handle_id
additional.fields[credtheft_handle_id]
credtheft.pre_auth_type
additional.fields[credtheft_pre_auth_type]
credtheft.system_time
additional.fields[credtheft_system_time]
decoy.ad.ou
additional.fields[decoy_ad_ou]
Field mapping reference: ZSCALER_DECEPTION - custom
The following table lists the raw log fields for the
custom
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
custom.dataset
principal.security_result.rule_set
custom.protocol
security_result.detection_fields[custom_protocol]
decoy.custom.protocol
security_result.detection_fields[decoy_custom_protocol]
decoy.custom.dataset
target.security_result.rule_set
custom.is_binary_request
additional.fields[custom_is_binary_request]
custom.is_binary_response
additional.fields[custom_is_binary_response]
custom.request
additional.fields[custom_request]
custom.response
additional.fields[custom_response]
Field mapping reference: ZSCALER_DECEPTION - email
The following table lists the raw log fields for the
email
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
email.evidence_id
network.email.mail_id
email.subject
network.email.subject
email.body.attachments
additional.fields[email_body_attachments]
The
email.body.attachments
log field is mapped to the
additional.fields.value.string_value
UDM field.
email.body.html
additional.fields[email_body_html]
The
email.body.html
log field is mapped to the
additional.fields.value.string_value
UDM field.
email.body.plain
additional.fields[email_body_plain]
The
email.body.plain
log field is mapped to the
additional.fields.value.string_value
UDM field.
Field mapping reference: ZSCALER_DECEPTION - endpoint, itdr, ransomware
The following table lists the raw log fields for the
endpoint
,
itdr
and
ransomware
log types and their corresponding UDM fields.
Log field
UDM mapping
Logic
attacker.event_name
metadata.description
psexec.event_name
metadata.description
triage.event_name
metadata.description
session_enumeration.type
metadata.description
metadata.event_type
If the
attacker.domain_name
log field value is
not
empty and at least one of the following log field is
not
empty, then the
metadata.event_type
UDM field is set to
PROCESS_TERMINATION
.
fake_process.process_id
pwsh.path
pwsh.script_block_id
pwsh.script_block_text
decoy.command_line
decoy.file_name
decoy.process_id
Else, if the
attacker.domain_name
log field value is
not
empty and at least one of the following log field is
not
empty, then the
metadata.event_type
UDM field is set to
PROCESS_LAUNCH
.
psexec.files_and_pipe_names
psexec.md5
psexec.sha1
psexec.sha256
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)read
, then the
metadata.event_type
UDM field is set to
FILE_READ
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)write or modify or encrypt
, then the
metadata.event_type
UDM field is set to
FILE_MODIFICATION
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)create
, then the
metadata.event_type
UDM field is set to
FILE_CREATION
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)delete
, then the
metadata.event_type
UDM field is set to
FILE_DELETION
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)open
, then the
metadata.event_type
UDM field is set to
FILE_OPEN
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)sync
, then the
metadata.event_type
UDM field is set to
FILE_SYNC
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)copy
, then the
metadata.event_type
UDM field is set to
FILE_COPY
.
Else, if the
file.name
log field value is
not
empty and the
attacker.domain_name
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)move
, then the
metadata.event_type
UDM field is set to
FILE_MOVE
.
Else, if the
attacker.user_name
log field value is
not
empty and (the
message
log field value matches the regular expression pattern
(cbf or imc).)
, then the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
Else, if the
attacker.domain_name
log field value is
not
empty and the
session_enumeration.network_address
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
attacker.domain_name
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
SCAN_HOST
.
Else, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
type
metadata.product_event_type
triage.incident_id
metadata.product_log_id
session_enumeration.endpoint
network.session_id
attacker.domain_name
principal.domain.name
If the
attacker.domain_name
log field value is
not
empty, then the
attacker.domain_name
log field is mapped to the
principal.domain.name
UDM field.
attacker.process.domain_name
principal.domain.name
If the
attacker.process.domain_name
log field value is
not
empty, then the
attacker.process.domain_name
log field is mapped to the
principal.domain.name
UDM field.
attacker.machine_name
principal.hostname
attacker.session_id
principal.network.session_id
attacker.command_line
principal.process.command_line
If the
attacker.command_line
log field value is
not
empty, then the
attacker.command_line
log field is mapped to the
principal.process.command_line
UDM field.
attacker.process.command_line
principal.process.command_line
If the
attacker.process.command_line
log field value is
not
empty, then the
attacker.process.command_line
log field is mapped to the
principal.process.command_line
UDM field.
attacker.process.path
principal.process.file.full_path
attacker.process.md5
principal.process.file.md5
attacker.process.sha1
principal.process.file.sha1
attacker.process.sha256
principal.process.file.sha256
attacker.process.parent_info.command_line
principal.process.parent_process.command_line
attacker.process.parent_info.path
principal.process.parent_process.file.full_path
attacker.process.parent_info.md5
principal.process.parent_process.file.md5
attacker.process.parent_info.sha1
principal.process.parent_process.file.sha1
attacker.process.parent_info.sha256
principal.process.parent_process.file.sha256
attacker.process.parent_info.id
principal.process.parent_process.pid
attacker.process.parent_info.parent
principal.process.parent_process.product_specific_process_id
The
Deception:attacker.process.parent_info.parent
log field is mapped to the
principal.process.parent_process.product_specific_process_id
UDM field.
attacker.process.id
principal.process.pid
attacker.process.user_groups
principal.user.group_identifiers
The
attacker.process.user_groups
log field is mapped to the
principal.user.group_identifiers
UDM field.
attacker.process.user_ou
principal.user.group_identifiers
The
attacker.process.user_groups
log field is mapped to the
principal.user.group_identifiers
UDM field and the
attacker.process.user_ou
log field is mapped to the
principal.user.group_identifiers
UDM field.
attacker.process.user_name
principal.user.user_display_name
attacker.user_name
principal.user.userid
If the
attacker.user_name
log field value is
not
empty, then the
attacker.user_name
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
attacker.username
log field value is
not
empty, then the
attacker.user_name
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zcc_user
log field value is
not
empty, then the
attacker.user_name
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zia_user
log field value is
not
empty, then the
attacker.user_name
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zpa_user
log field value is
not
empty, then the
attacker.user_name
log field is mapped to the
additional.fields
UDM field.
attacker.username
principal.user.userid
If the
attacker.user_name
log field value is
not
empty, then the
attacker.username
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.username
log field value is
not
empty, then the
attacker.username
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
attacker.zcc_user
log field value is
not
empty, then the
attacker.username
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zia_user
log field value is
not
empty, then the
attacker.username
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zpa_user
log field value is
not
empty, then the
attacker.username
log field is mapped to the
additional.fields
UDM field.
attacker.zcc_user
principal.user.userid
If the
attacker.user_name
log field value is
not
empty, then the
attacker.zcc_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.username
log field value is
not
empty, then the
attacker.zcc_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zcc_user
log field value is
not
empty, then the
attacker.zcc_user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
attacker.zia_user
log field value is
not
empty, then the
attacker.zcc_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zpa_user
log field value is
not
empty, then the
attacker.zcc_user
log field is mapped to the
additional.fields
UDM field.
attacker.zia_user
principal.user.userid
If the
attacker.user_name
log field value is
not
empty, then the
attacker.zia_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.username
log field value is
not
empty, then the
attacker.zia_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zcc_user
log field value is
not
empty, then the
attacker.zia_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zia_user
log field value is
not
empty, then the
attacker.zia_user
log field is mapped to the
principal.user.userid
UDM field.
Else, if the
attacker.zpa_user
log field value is
not
empty, then the
attacker.zia_user
log field is mapped to the
additional.fields
UDM field.
attacker.zpa_user
principal.user.userid
If the
attacker.user_name
log field value is
not
empty, then the
attacker.zpa_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.username
log field value is
not
empty, then the
attacker.zpa_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zcc_user
log field value is
not
empty, then the
attacker.zpa_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zia_user
log field value is
not
empty, then the
attacker.zpa_user
log field is mapped to the
additional.fields
UDM field.
Else, if the
attacker.zpa_user
log field value is
not
empty, then the
attacker.zpa_user
log field is mapped to the
principal.user.userid
UDM field.
attacker.process.user_sid
principal.user.windows_sid
fake_process.action
security_result.action_details
security_result.category
If the
type
log field value matches the regular expression pattern
ransomware
, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
cbf.is_ad_decoy_credential
security_result.detection_fields[cbf_is_ad_decoy_credential]
file.operation_string
security_result.detection_fields[file_operation_string]
file.operation
security_result.detection_fields[file_operation]
kerberoast.is_decoy
security_result.detection_fields[kerberoast_is_decoy]
mitm.query
security_result.detection_fields[mitm_query]
mitm.technique
security_result.detection_fields[mitm_technique]
monitor_accounts.win_event_id
security_result.detection_fields[monitor_accounts_win_event_id]
triage.reason
security_result.summary
monitor_accounts.failure_reason
security_result.summary
cbf.target_domain_name
target.domain.name
fake_process.domain_name
target.domain.name
imc.target_domain_name
target.domain.name
psexec.domain_name
target.domain.name
monitor_accounts.target_domain_name
target.domain.name
file.name
target.file.full_path
psexec.machine_name
target.hostname
triage.machine_name
target.hostname
monitor_accounts.workstation_name
target.hostname
session_enumeration.network_address
target.ip
dcshadow.network_address
target.ip
dcsync.network_address
target.ip
zerologon.network_address
target.ip
monitor_accounts.ip_address
target.ip
fake_process.session_id
target.network.session_id
decoy.session_id
target.network.session_id
monitor_accounts.ip_port
target.port
fake_process.command_line
target.process.command_line
pwsh.script_block_text
target.process.command_line
decoy.command_line
target.process.command_line
pwsh.path
target.process.file.full_path
decoy.file_name
target.process.file.full_path
psexec.md5
target.process.file.md5
psexec.files_and_pipe_names
target.process.file.names
The
psexec.files_and_pipe_names
log field is mapped to the
target.process.file.names
UDM field.
psexec.sha1
target.process.file.sha1
psexec.sha256
target.process.file.sha256
fake_process.parent_process_id
target.process.parent_process.pid
fake_process.process_id
target.process.pid
pwsh.script_block_id
target.process.pid
decoy.process_id
target.process.pid
ad_enumeration.attribute_list
target.resource.attribute.labels[ad_enumeration_attribute_list]
ad_enumeration.scope_of_search_string
target.resource.attribute.labels[ad_enumeration_scope_of_search_string]
ad_enumeration.scope_of_search
target.resource.attribute.labels[ad_enumeration_scope_of_search]
ad_enumeration.search_filter
target.resource.attribute.labels[ad_enumeration_search_filter]
ad_enumeration.distinguished_name
target.resource.name
kerberoast.spn
target.resource.name
psexec.service_name
target.resource.name
ad_enumeration.type
target.resource.resource_subtype
target.resource.resource_type
If the
ad_enumeration.distinguished_name
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
Else, if the
kerberoast.spn
log field value is
not
empty or the
psexec.service_name
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
monitor_accounts.is_decoy
target.user.attribute.labels[monitor_accounts_is_decoy]
monitor_accounts.is_privileged
target.user.attribute.labels[monitor_accounts_is_privileged]
monitor_accounts.logon_process_name
target.user.attribute.labels[monitor_accounts_logon_process_name]
monitor_accounts.logon_type
target.user.attribute.labels[monitor_accounts_logon_type]
fake_process.user_groups
target.user.group_identifiers
fake_process.user_ou
target.user.group_identifiers
psexec.user_groups
target.user.group_identifiers
psexec.user_ou
target.user.group_identifiers
cbf.target_user_name
target.user.userid
fake_process.username
target.user.userid
imc.target_user_name
target.user.userid
psexec.user_name
target.user.userid
monitor_accounts.target_user_name
target.user.userid
fake_process.user_sid
target.user.windows_sid
psexec.user_sid
target.user.windows_sid
monitor_accounts.target_sid
target.user.windows_sid
attacker.logon_type
additional.fields[attacker_logon_type]
attacker.process.exit_code
additional.fields[attacker_process_exit_code]
attacker.process.name
additional.fields[attacker_process_name]
attacker.process.parent_info.domain_name
additional.fields[attacker_process_parent_info_domain_name]
attacker.process.parent_info.name
additional.fields[attacker_process_parent_info_name]
attacker.process.parent_info.tree
additional.fields[attacker_process_parent_info_tree]
The
attacker.process.parent_info.tree
log field is mapped to the
additional.fields.value.string_value
UDM field.
attacker.process.parent_info.user_groups
additional.fields[attacker_process_parent_info_user_groups]
attacker.process.parent_info.user_name
additional.fields[attacker_process_parent_info_user_name]
attacker.process.parent_info.user_ou
additional.fields[attacker_process_parent_info_user_ou]
attacker.process.parent_info.user_sid
additional.fields[attacker_process_parent_info_user_sid]
attacker.process.parent
additional.fields[attacker_process_parent]
attacker.process.tree
additional.fields[attacker_process_tree]
The
attacker.process.tree
log field is mapped to the
additional.fields.value.string_value
UDM field.
fake_process.exit_code
additional.fields[fake_process_exit_code]
fake_process.process_name
additional.fields[fake_process_process_name]
landmine.version
additional.fields[landmine_version]
monitor_accounts.auth_package
additional.fields[monitor_accounts_auth_package]
monitor_accounts.status
additional.fields[monitor_accounts_status]
monitor_accounts.sub_status_parsed
additional.fields[monitor_accounts_sub_status_parsed]
monitor_accounts.sub_status
additional.fields[monitor_accounts_sub_status]
pwsh.message_number
additional.fields[pwsh_message_number]
pwsh.message_total
additional.fields[pwsh_message_total]
Field mapping reference: ZSCALER_DECEPTION - filetheft
The following table lists the raw log fields for the
filetheft
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
filetheft.useragent
network.http.user_agent
filetheft.filename
target.file.full_path
filetheft.file_uuid
additional.fields[filetheft_file_uuid]
Field mapping reference: ZSCALER_DECEPTION - mitm
The following table lists the raw log fields for the
mitm
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
network.application_protocol
The
network.application_protocol
UDM field is set to
DNS
.
mitm.answer
network.dns.answers.data
mitm.qtype
network.dns.questions.type
mitm.server
principal.hostname
mitm.hostname
target.hostname
Field mapping reference: ZSCALER_DECEPTION - mongodb
The following table lists the raw log fields for the
mongodb
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
mongodb.message
metadata.description
type
metadata.product_event_type
mongodb.execution_time
network.session_duration.seconds
mongodb.connection_id
network.session_id
mongodb.command
security_result.detection_fields[mongodb_command]
mongodb.object
additional.fields[mongodb_object]
mongodb.protocol
additional.fields[mongodb_protocol]
Field mapping reference: ZSCALER_DECEPTION - network
The following table lists the raw log fields for the
network
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
rfb.authentication_method
extensions.auth.auth_details
ssh.auth_success
extensions.auth.auth_details
extensions.auth.mechanism
If the
mysql.username
log field value is
not
empty, then the
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
Else, if the
ntlm.username
log field value is
not
empty, then the
extensions.auth.mechanism
UDM field is set to
INTERACTIVE
.
Else, if the
radius.username
log field value is
not
empty, then the
extensions.auth.mechanism
UDM field is set to
REMOTE
.
Else, if the
rfb.authentication_method
log field value is
not
empty, then the
extensions.auth.mechanism
UDM field is set to
REMOTE_INTERACTIVE
.
socks.bound
intermediary.hostname
socks.bound_p
intermediary.port
snmp.display_string
metadata.description
syslog.message
metadata.description
threat.event_type
metadata.description
metadata.event_type
If (the
ntlm.hostname
log field value is
not
empty or the
radius.mac
log field value is
not
empty or the
radius.remote_ip
log field value is
not
empty) and (the
ntlm.username
log field value is
not
empty or the
radius.username
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
message
log field value matches the regular expression pattern
smtp.
, then the
metadata.event_type
UDM field is set to
EMAIL_TRANSACTION
.
Else, if the
message
log field value matches the regular expression pattern
(dnp3 or modbus or scan or snmp or syslog or tunnel).
, then the
metadata.event_type
UDM field is set to
USER_STATS
.
Else, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
type
metadata.product_event_type
threat.tx_id
metadata.product_log_id
network.application_protocol
If the
message
log field value matches the regular expression pattern
dce_rpc.
, then the
network.application_protocol
UDM field is set to
DCERPC
.
Else, if the
message
log field value matches the regular expression pattern
dnp3.
, then the
network.application_protocol
UDM field is set to
DNP3
.
Else, if the
message
log field value matches the regular expression pattern
dns.
, then the
network.application_protocol
UDM field is set to
DNS
.
Else, if the
message
log field value matches the regular expression pattern
mqtt.
, then the
network.application_protocol
UDM field is set to
MQTT
.
Else, if the
message
log field value matches the regular expression pattern
rdp.
, then the
network.application_protocol
UDM field is set to
RDP
.
Else, if the
message
log field value matches the regular expression pattern
sip.
, then the
network.application_protocol
UDM field is set to
SIP
.
Else, if the
message
log field value matches the regular expression pattern
smb.
, then the
network.application_protocol
UDM field is set to
SMB
.
Else, if the
message
log field value matches the regular expression pattern
smtp.
, then the
network.application_protocol
UDM field is set to
SMTP
.
Else, if the
message
log field value matches the regular expression pattern
snmp.
, then the
network.application_protocol
UDM field is set to
SNMP
.
Else, if the
message
log field value matches the regular expression pattern
ssh.
, then the
network.application_protocol
UDM field is set to
SSH
.
mqtt.proto_version
network.application_protocol_version
rdp.client_build
network.application_protocol_version
snmp.version
network.application_protocol_version
ssh.version
network.application_protocol_version
network.direction
If the
ssh.direction
log field value matches the regular expression pattern
(?i)INBOUND
, then the
network.direction
UDM field is set to
INBOUND
.
Else, if the
ssh.direction
log field value matches the regular expression pattern
(?i)OUTBOUND
, then the
network.direction
UDM field is set to
OUTBOUND
.
dns.answers
network.dns.answers.data
dns.TTLs
network.dns.answers.ttl
dns.trans_id
network.dns.id
dns.qclass
network.dns.questions.class
dns.query
network.dns.questions.name
dns.qtype
network.dns.questions.type
dns.RA
network.dns.recursion_available
dns.RD
network.dns.recursion_desired
dns.AA
network.dns.response
dns.rcode
network.dns.response_code
dns.rejected
network.dns.truncated
smtp.cc
network.email.cc
smtp.mailfrom
network.email.from
smtp.in_reply_to
network.email.reply_to
smtp.reply_to
network.email.reply_to
smtp.subject
network.email.subject
smtp.to
network.email.to
ftp.command
network.ftp.command
sip.method
network.http.method
sip.status_code
network.http.response_code
sip.user_agent
network.http.user_agent
network.ip_protocol
If the
dns.proto
log field value matches the regular expression pattern
(?i)tcp
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
dns.proto
log field value matches the regular expression pattern
(?i)udp
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
dns.proto
log field value matches the regular expression pattern
(?i)icmp
, then the
network.ip_protocol
UDM field is set to
ICMP
.
Else, if the
network.protocol
log field value matches the regular expression pattern
(?i)tcp
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
network.protocol
log field value matches the regular expression pattern
(?i)udp
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
network.protocol
log field value matches the regular expression pattern
(?i)icmp
, then the
network.ip_protocol
UDM field is set to
ICMP
.
Else, if the
syslog.proto
log field value matches the regular expression pattern
(?i)tcp
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
syslog.proto
log field value matches the regular expression pattern
(?i)udp
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
syslog.proto
log field value matches the regular expression pattern
(?i)icmp
, then the
network.ip_protocol
UDM field is set to
ICMP
.
network.tunnel_parents
network.parent_session_id
network.duration
network.session_duration
network.connection_uid
network.session_id
threat.flow_id
network.session_id
smtp.helo
network.smtp.helo
network.smtp.is_tls
If the
smtp.tls
log field value matches the regular expression pattern
(?i)true
, then the
network.smtp.is_tls
UDM field is set to
true
.
smtp.from
network.smtp.mail_from
smtp.rcptto
network.smtp.rcpt_to
ssl.cipher
network.tls.cipher
ssl.established
network.tls.established
ssl.resumed
network.tls.resumed
ssl.issuer
network.tls.server.certificate.issuer
ssl.subject
network.tls.server.certificate.subject
ssl.version
network.tls.version
rdp.client_dig_product_id
principal.asset.product_object_id
ntlm.domainname
principal.domain.name
threat.alert.gid
principal.group.product_object_id
ntlm.hostname
principal.hostname
rdp.client_name
principal.hostname
radius.remote_ip
principal.ip
smtp.x_originating_ip
principal.ip
radius.mac
principal.mac
network.orig_bytes
principal.network.sent_bytes
network.orig_pkts
principal.network.sent_packets
rfb.client_major_version
principal.platform_version
The
rfb.client_major_version rfb.client_minor_version
log field is mapped to the
principal.platform_version
UDM field.
rfb.client_minor_version
principal.platform_version
The
rfb.client_major_version rfb.client_minor_version
log field is mapped to the
principal.platform_version
UDM field.
irc.command
principal.process.command_line
ftp.password
principal.user.attribute.labels[ftp_password]
mysql.password
principal.user.attribute.labels[mysql_password]
socks.password
principal.user.attribute.labels[socks_password]
ftp.user
principal.user.userid
irc.user
principal.user.userid
kerberos.client
principal.user.userid
mqtt.client_id
principal.user.userid
mysql.username
principal.user.userid
rdp.cookie
principal.user.userid
socks.user
principal.user.userid
security_result.action
If the
rdp.result
log field value matches the regular expression pattern
(?i)(allow or success)
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
rdp.result
log field value matches the regular expression pattern
(?i)(fail)
, then the
security_result.action
UDM field is set to
FAIL
.
Else, if the
rdp.result
log field value matches the regular expression pattern
(?i)(denied or block)
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
radius.result
log field value matches the regular expression pattern
(?i)(allow or success)
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
radius.result
log field value matches the regular expression pattern
(?i)(fail)
, then the
security_result.action
UDM field is set to
FAIL
.
Else, if the
radius.result
log field value matches the regular expression pattern
(?i)(denied or block)
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
threat.alert.action
log field value matches the regular expression pattern
(?i)(allow or success)
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
threat.alert.action
log field value matches the regular expression pattern
(?i)(fail)
, then the
security_result.action
UDM field is set to
FAIL
.
Else, if the
threat.alert.action
log field value matches the regular expression pattern
(?i)(denied or block)
, then the
security_result.action
UDM field is set to
BLOCK
.
radius.result
security_result.action_details
rdp.result
security_result.action_details
smb_files.action
security_result.action_details
tunnel.action
security_result.action_details
threat.alert.category
security_result.category_details
kerberos.error_msg
security_result.description
sip.warning
security_result.description
dce_rpc.operation
security_result.detection_fields[dce_rpc_operation]
file.analyzers
security_result.detection_fields[file_analyzers]
mqtt.granted_qos_level
security_result.detection_fields[mqtt_granted_qos_level]
mqtt.qos_val
security_result.detection_fields[mqtt_qos_val]
rdp.cert_count
security_result.detection_fields[rdp_cert_count]
rdp.cert_permanent
security_result.detection_fields[rdp_cert_permanent]
rdp.cert_type
security_result.detection_fields[rdp_cert_type]
rdp.encryption_level
security_result.detection_fields[rdp_encryption_level]
rdp.encryption_method
security_result.detection_fields[rdp_encryption_method]
rdp.security_protocol
security_result.detection_fields[rdp_security_protocol]
ssh.auth_attempts
security_result.detection_fields[ssh_auth_attempts]
ssh.cipher_alg
security_result.detection_fields[ssh_cipher_alg]
ssh.client
security_result.detection_fields[ssh_client]
ssh.compression_alg
security_result.detection_fields[ssh_compression_alg]
ssh.host_key_alg
security_result.detection_fields[ssh_host_key_alg]
ssh.host_key
security_result.detection_fields[ssh_host_key]
ssh.kex_alg
security_result.detection_fields[ssh_kex_alg]
ssh.mac_alg
security_result.detection_fields[ssh_mac_alg]
ssh.server
security_result.detection_fields[ssh_server]
ssl.cert_chain_fuids
security_result.detection_fields[ssl_cert_chain_fuids]
ssl.client_cert_chain_fuids
security_result.detection_fields[ssl_client_cert_chain_fuids]
ssl.validation_status
security_result.detection_fields[ssl_validation_status]
syslog.facility
security_result.detection_fields[syslog_facility]
threat.alert.rev
security_result.detection_fields[threat_alert_rev]
threat.alert.signature_id
security_result.rule_id
decoy.smb.dataset
security_result.rule_labels[decoy_smb_dataset]
The
decoy.smb.dataset
log field is mapped to the
security_result.rule_labels
UDM field.
threat.alert.signature
security_result.rule_name
decoy.ftp.dataset
security_result.rule_set
security_result.severity
If the
syslog.severity
log field value matches the regular expression pattern
(?i)Low
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
syslog.severity
log field value matches the regular expression pattern
(?i)Informational
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
syslog.severity
log field value matches the regular expression pattern
(?i)Medium
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
syslog.severity
log field value matches the regular expression pattern
(?i)Critical
, then the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
syslog.severity
log field value matches the regular expression pattern
(?i)High
, then the
security_result.severity
UDM field is set to
HIGH
.
Else, if the
syslog.severity
log field value matches the regular expression pattern
(?i)ERROR
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
threat.alert.severity
log field value matches the regular expression pattern
4 or 5
, then the
security_result.severity
UDM field is set to
HIGH
.
Else, if the
threat.alert.severity
log field value matches the regular expression pattern
1 or 2
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
threat.alert.severity
log field value matches the regular expression pattern
3
, then the
security_result.severity
UDM field is set to
MEDIUM
.
syslog.severity
security_result.severity_details
threat.alert.severity
security_result.severity_details
security_result.summary
If the
kerberos.error_code
log field value is equal to
1
, then the
security_result.summary
UDM field is set to
KDC_ERR_NAME_EXP
.
Else, if the
kerberos.error_code
log field value is equal to
2
, then the
security_result.summary
UDM field is set to
KDC_ERR_SERVICE_EXP
.
Else, if the
kerberos.error_code
log field value is equal to
3
, then the
security_result.summary
UDM field is set to
KDC_ERR_BAD_PVNO
.
Else, if the
kerberos.error_code
log field value is equal to
4
, then the
security_result.summary
UDM field is set to
KDC_ERR_C_OLD_MAST_KVNO
.
Else, if the
kerberos.error_code
log field value is equal to
5
, then the
security_result.summary
UDM field is set to
KDC_ERR_S_OLD_MAST_KVNO
.
Else, if the
kerberos.error_code
log field value is equal to
6
, then the
security_result.summary
UDM field is set to
KDC_ERR_C_PRINCIPAL_UNKNOWN
.
Else, if the
kerberos.error_code
log field value is equal to
7
, then the
security_result.summary
UDM field is set to
KDC_ERR_S_PRINCIPAL_UNKNOWN
.
Else, if the
kerberos.error_code
log field value is equal to
8
, then the
security_result.summary
UDM field is set to
KDC_ERR_PRINCIPAL_NOT_UNIQUE
.
Else, if the
kerberos.error_code
log field value is equal to
9
, then the
security_result.summary
UDM field is set to
KDC_ERR_NULL_KEY
.
Else, if the
kerberos.error_code
log field value is equal to
10
, then the
security_result.summary
UDM field is set to
KDC_ERR_CANNOT_POSTDATE
.
Else, if the
kerberos.error_code
log field value is equal to
11
, then the
security_result.summary
UDM field is set to
KDC_ERR_NEVER_VALID
.
Else, if the
kerberos.error_code
log field value is equal to
12
, then the
security_result.summary
UDM field is set to
KDC_ERR_POLICY
.
Else, if the
kerberos.error_code
log field value is equal to
13
, then the
security_result.summary
UDM field is set to
KDC_ERR_BADOPTION
.
Else, if the
kerberos.error_code
log field value is equal to
14
, then the
security_result.summary
UDM field is set to
KDC_ERR_ETYPE_NOSUPP
.
Else, if the
kerberos.error_code
log field value is equal to
15
, then the
security_result.summary
UDM field is set to
KDC_ERR_SUMTYPE_NOSUPP
.
Else, if the
kerberos.error_code
log field value is equal to
16
, then the
security_result.summary
UDM field is set to
KDC_ERR_PADATA_TYPE_NOSUPP
.
Else, if the
kerberos.error_code
log field value is equal to
17
, then the
security_result.summary
UDM field is set to
KDC_ERR_TRTYPE_NOSUPP
.
Else, if the
kerberos.error_code
log field value is equal to
18
, then the
security_result.summary
UDM field is set to
KDC_ERR_CLIENT_REVOKED
.
Else, if the
kerberos.error_code
log field value is equal to
19
, then the
security_result.summary
UDM field is set to
KDC_ERR_SERVICE_REVOKED
.
Else, if the
kerberos.error_code
log field value is equal to
20
, then the
security_result.summary
UDM field is set to
KDC_ERR_TGT_REVOKED
.
Else, if the
kerberos.error_code
log field value is equal to
21
, then the
security_result.summary
UDM field is set to
KDC_ERR_CLIENT_NOTYET
.
Else, if the
kerberos.error_code
log field value is equal to
22
, then the
security_result.summary
UDM field is set to
KDC_ERR_SERVICE_NOTYET
.
Else, if the
kerberos.error_code
log field value is equal to
23
, then the
security_result.summary
UDM field is set to
KDC_ERR_KEY_EXPIRED
.
Else, if the
kerberos.error_code
log field value is equal to
24
, then the
security_result.summary
UDM field is set to
KDC_ERR_PREAUTH_FAILED
.
Else, if the
kerberos.error_code
log field value is equal to
25
, then the
security_result.summary
UDM field is set to
KDC_ERR_PREAUTH_REQUIRED
.
Else, if the
kerberos.error_code
log field value is equal to
26
, then the
security_result.summary
UDM field is set to
KDC_ERR_SERVER_NOMATCH
.
Else, if the
kerberos.error_code
log field value is equal to
27
, then the
security_result.summary
UDM field is set to
KDC_ERR_MUST_USE_USER2USER
.
Else, if the
kerberos.error_code
log field value is equal to
28
, then the
security_result.summary
UDM field is set to
KDC_ERR_PATH_NOT_ACCEPTED
.
Else, if the
kerberos.error_code
log field value is equal to
29
, then the
security_result.summary
UDM field is set to
KDC_ERR_SVC_UNAVAILABLE
.
Else, if the
kerberos.error_code
log field value is equal to
31
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BAD_INTEGRITY
.
Else, if the
kerberos.error_code
log field value is equal to
32
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_TKT_EXPIRED
.
Else, if the
kerberos.error_code
log field value is equal to
33
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_TKT_NYV
.
Else, if the
kerberos.error_code
log field value is equal to
34
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_REPEAT
.
Else, if the
kerberos.error_code
log field value is equal to
35
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_NOT_US
.
Else, if the
kerberos.error_code
log field value is equal to
36
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADMATCH
.
Else, if the
kerberos.error_code
log field value is equal to
37
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_SKEW
.
Else, if the
kerberos.error_code
log field value is equal to
38
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADADDR
.
Else, if the
kerberos.error_code
log field value is equal to
39
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADVERSION
.
Else, if the
kerberos.error_code
log field value is equal to
40
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_MSG_TYPE
.
Else, if the
kerberos.error_code
log field value is equal to
41
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_MODIFIED
.
Else, if the
kerberos.error_code
log field value is equal to
42
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADORDER
.
Else, if the
kerberos.error_code
log field value is equal to
44
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADKEYVER
.
Else, if the
kerberos.error_code
log field value is equal to
45
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_NOKEY
.
Else, if the
kerberos.error_code
log field value is equal to
46
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_MUT_FAIL
.
Else, if the
kerberos.error_code
log field value is equal to
47
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADDIRECTION
.
Else, if the
kerberos.error_code
log field value is equal to
48
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_METHOD
.
Else, if the
kerberos.error_code
log field value is equal to
49
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_BADSEQ
.
Else, if the
kerberos.error_code
log field value is equal to
50
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_INAPP_CKSUM
.
Else, if the
kerberos.error_code
log field value is equal to
51
, then the
security_result.summary
UDM field is set to
KRB_AP_PATH_NOT_ACCEPTED
.
Else, if the
kerberos.error_code
log field value is equal to
52
, then the
security_result.summary
UDM field is set to
KRB_ERR_RESPONSE_TOO_BIG
.
Else, if the
kerberos.error_code
log field value is equal to
60
, then the
security_result.summary
UDM field is set to
KRB_ERR_GENERIC
.
Else, if the
kerberos.error_code
log field value is equal to
61
, then the
security_result.summary
UDM field is set to
KRB_ERR_FIELD_TOOLONG
.
Else, if the
kerberos.error_code
log field value is equal to
62
, then the
security_result.summary
UDM field is set to
KDC_ERROR_CLIENT_NOT_TRUSTED
.
Else, if the
kerberos.error_code
log field value is equal to
63
, then the
security_result.summary
UDM field is set to
KDC_ERROR_KDC_NOT_TRUSTED
.
Else, if the
kerberos.error_code
log field value is equal to
64
, then the
security_result.summary
UDM field is set to
KDC_ERROR_INVALID_SIG
.
Else, if the
kerberos.error_code
log field value is equal to
65
, then the
security_result.summary
UDM field is set to
KDC_ERR_KEY_TOO_WEAK
.
Else, if the
kerberos.error_code
log field value is equal to
66
, then the
security_result.summary
UDM field is set to
KDC_ERR_CERTIFICATE_MISMATCH
.
Else, if the
kerberos.error_code
log field value is equal to
67
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_NO_TGT
.
Else, if the
kerberos.error_code
log field value is equal to
68
, then the
security_result.summary
UDM field is set to
KDC_ERR_WRONG_REALM
.
Else, if the
kerberos.error_code
log field value is equal to
69
, then the
security_result.summary
UDM field is set to
KRB_AP_ERR_USER_TO_USER_REQUIRED
.
Else, if the
kerberos.error_code
log field value is equal to
70
, then the
security_result.summary
UDM field is set to
KDC_ERR_CANT_VERIFY_CERTIFICATE
.
Else, if the
kerberos.error_code
log field value is equal to
71
, then the
security_result.summary
UDM field is set to
KDC_ERR_INVALID_CERTIFICATE
.
Else, if the
kerberos.error_code
log field value is equal to
72
, then the
security_result.summary
UDM field is set to
KDC_ERR_REVOKED_CERTIFICATE
.
Else, if the
kerberos.error_code
log field value is equal to
73
, then the
security_result.summary
UDM field is set to
KDC_ERR_REVOCATION_STATUS_UNKNOWN
.
Else, if the
kerberos.error_code
log field value is equal to
74
, then the
security_result.summary
UDM field is set to
KDC_ERR_REVOCATION_STATUS_UNAVAILABLE
.
Else, if the
kerberos.error_code
log field value is equal to
75
, then the
security_result.summary
UDM field is set to
KDC_ERR_CLIENT_NAME_MISMATCH
.
Else, if the
kerberos.error_code
log field value is equal to
76
, then the
security_result.summary
UDM field is set to
KDC_ERR_KDC_NAME_MISMATCH
.
pe.machine
target.asset.asset_id
The
Zscaler:pe.machine
log field is mapped to the
target.asset.asset_id
UDM field.
target.file.file_type
If the
pe.is_exe
log field value is equal to
true
, then the
target.file.file_type
UDM field is set to
FILE_TYPE_PE_EXE
.
smb_files.times.created
target.file.first_submission_time
file.source
target.file.full_path
smb_files.path
target.file.full_path
smb_mapping.path
target.file.full_path
smb_files.times.accessed
target.file.last_analysis_time
smb_files.times.changed
target.file.last_modification_time
If the
smb_files.times.modified
log field value is
not
empty, then the
smb_files.times.modified
log field is mapped to the
target.file.last_modification_time
UDM field.
Else, if the
smb_files.times.changed
log field value is
not
empty, then the
smb_files.times.changed
log field is mapped to the
target.file.last_modification_time
UDM field.
smb_files.times.modified
target.file.last_modification_time
If the
smb_files.times.modified
log field value is
not
empty, then the
smb_files.times.modified
log field is mapped to the
target.file.last_modification_time
UDM field.
file.md5
target.file.md5
file.mime_type
target.file.mime_type
smb_files.name
target.file.names
pe.compile_ts
target.file.pe_file.compilation_time
pe.section_names
target.file.pe_file.section.name
The
pe.section_names
log field is mapped to the
target.file.pe_file.section.name
UDM field.
file.sha1
target.file.sha1
file.total_bytes
target.file.size
smb_files.size
target.file.size
socks.request
target.hostname
scan.ips
target.ip
The
scan.ips
log field is mapped to the
target.ip
UDM field.
network.resp_bytes
target.network.sent_bytes
network.resp_pkts
target.network.sent_packets
target.platform
If the
pe.os
log field value matches the regular expression pattern
(?i)Win
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
pe.os
log field value matches the regular expression pattern
(?i)Lin
, then the
principal.platform
UDM field is set to
LINUX
.
Else, if the
pe.os
log field value matches the regular expression pattern
(?i)(Mac or iOS)
, then the
principal.platform
UDM field is set to
MAC
.
rfb.server_major_version
target.platform_version
The
rfb.server_major_version rfb.server_minor_version
log field is mapped to the
target.platform_version
UDM field.
rfb.server_minor_version
target.platform_version
The
rfb.server_major_version rfb.server_minor_version
log field is mapped to the
target.platform_version
UDM field.
scan.ports
target.port
If the
index
log field value is equal to
0
, then the
scan.ports
log field is mapped to the
target.port
UDM field.
Else, the
scan.ports
log field is mapped to the
additional.fields.value.string_value
UDM field.
socks.request_p
target.port
The
socks.request_p
log field is mapped to the
target.port
UDM field.
dce_rpc.endpoint
target.resource_ancestors.name
target.resource_ancestors.resource_type
If the
dce_rpc.endpoint
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
BACKEND_SERVICE
.
rfb.height
target.resource.attribute.labels[rfb_height]
rfb.width
target.resource.attribute.labels[rfb_width]
dce_rpc.named_pipe
target.resource.name
kerberos.service
target.resource.name
rfb.desktop_name
target.resource.name
target.resource.resource_type
If the
dce_rpc.named_pipe
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
PIPE
.
Else, if the
kerberos.service
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
Else, if the
rfb.desktop_name
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
DEVICE
.
sip.uri
target.url
ntlm.username
target.user.userid
radius.username
target.user.userid
dce_rpc.rtt
additional.fields[dce_rpc_rtt]
decoy.ftp.banner
additional.fields[decoy_ftp_banner]
dnp3.fc_reply
additional.fields[dnp3_fc_reply]
dnp3.fc_request
additional.fields[dnp3_fc_request]
dnp3.iin
additional.fields[dnp3_iin]
dns.qclass_name
additional.fields[dns_qclass_name]
dns.qtype_name
additional.fields[dns_qtype_name]
dns.rcode_name
additional.fields[dns_rcode_name]
dns.rtt
additional.fields[dns_rtt]
dns.saw_query
additional.fields[dns_saw_query]
dns.saw_reply
additional.fields[dns_saw_reply]
dns.TC
additional.fields[dns_tc]
dns.total_answers
additional.fields[dns_total_answers]
dns.total_replies
additional.fields[dns_total_replies]
dns.Z
additional.fields[dns_z]
file.depth
additional.fields[file_depth]
file.duration
additional.fields[file_duration]
file.is_orig
additional.fields[file_is_orig]
file.missing_bytes
additional.fields[file_missing_bytes]
file.overflow_bytes
additional.fields[file_overflow_bytes]
file.seen_bytes
additional.fields[file_seen_bytes]
file.timedout
additional.fields[file_timedout]
file.uid
additional.fields[file_uid]
ftp.arg
additional.fields[ftp_arg]
ftp.data_channel.passive
additional.fields[ftp_data_channel_passive]
ftp.reply_code
additional.fields[ftp_reply_code]
ftp.reply_msg
additional.fields[ftp_reply_msg]
irc.addl
additional.fields[irc_addl]
irc.nick
additional.fields[irc_nick]
irc.value
additional.fields[irc_value]
kerberos.cipher
additional.fields[kerberos_cipher]
kerberos.forwardable
additional.fields[kerberos_forwardable]
kerberos.from
additional.fields[kerberos_from]
kerberos.logged
additional.fields[kerberos_logged]
kerberos.renewable
additional.fields[kerberos_renewable]
kerberos.request_type
additional.fields[kerberos_request_type]
kerberos.success
additional.fields[kerberos_success]
kerberos.till
additional.fields[kerberos_till]
modbus.func
additional.fields[modbus_func]
mqtt.ack
additional.fields[mqtt_ack]
mqtt.action
additional.fields[mqtt_action]
mqtt.connect_status
additional.fields[mqtt_connect_status]
mqtt.from_client
additional.fields[mqtt_from_client]
mqtt.message_type
additional.fields[mqtt_message_type]
mqtt.payload_len
additional.fields[mqtt_payload_len]
mqtt.payload
additional.fields[mqtt_payload]
mqtt.retain
additional.fields[mqtt_retain]
mqtt.status
additional.fields[mqtt_status]
mqtt.topic
additional.fields[mqtt_topic]
mqtt.topics
additional.fields[mqtt_topics]
mysql.arg
additional.fields[mysql_arg]
mysql.cmd
additional.fields[mysql_cmd]
mysql.response
additional.fields[mysql_response]
mysql.rows
additional.fields[mysql_rows]
network.conn_state
additional.fields[network_conn_state]
network.connection_uids
additional.fields[network_connection_uids]
The
network.connection_uids
log field is mapped to the
additional.fields.value.string_value
UDM field.
network.history
additional.fields[network_history]
network.icmp_type
additional.fields[network_icmp_type]
network.local_orig
additional.fields[network_local_orig]
network.local_resp
additional.fields[network_local_resp]
network.missed_bytes
additional.fields[network_missed_bytes]
network.orig_ip_bytes
additional.fields[network_orig_ip_bytes]
network.resp_ip_bytes
additional.fields[network_resp_ip_bytes]
network.service
additional.fields[network_service]
ntlm.done
additional.fields[ntlm_done]
ntlm.status
additional.fields[ntlm_status]
pe.has_cert_table
additional.fields[pe_has_cert_table]
pe.has_debug_data
additional.fields[pe_has_debug_data]
pe.has_export_table
additional.fields[pe_has_export_table]
pe.has_import_table
additional.fields[pe_has_import_table]
pe.is_64bit
additional.fields[pe_is_64bit]
pe.subsystem
additional.fields[pe_subsystem]
pe.uses_aslr
additional.fields[pe_uses_aslr]
pe.uses_code_integrity
additional.fields[pe_uses_code_integrity]
pe.uses_dep
additional.fields[pe_uses_dep]
pe.uses_seh
additional.fields[pe_uses_seh]
radius.connect_info
additional.fields[radius_connect_info]
radius.logged
additional.fields[radius_logged]
rdp.desktop_height
additional.fields[rdp_desktop_height]
rdp.desktop_width
additional.fields[rdp_desktop_width]
rdp.keyboard_layout
additional.fields[rdp_keyboard_layout]
rdp.requested_color_depth
additional.fields[rdp_requested_color_depth]
rfb.auth
additional.fields[rfb_auth]
rfb.done
additional.fields[rfb_done]
rfb.share_flag
additional.fields[rfb_share_flag]
scan.type
additional.fields[scan_type]
sip.call_id
additional.fields[sip_call_id]
sip.content_type
additional.fields[sip_content_type]
sip.date
additional.fields[sip_date]
sip.reply_to
additional.fields[sip_reply_to]
sip.request_body_len
additional.fields[sip_request_body_len]
sip.request_from
additional.fields[sip_request_from]
sip.request_path
additional.fields[sip_request_path]
The
sip.request_path
log field is mapped to the
additional.fields.value.string_value
UDM field.
sip.request_to
additional.fields[sip_request_to]
sip.response_body_len
additional.fields[sip_response_body_len]
sip.response_from
additional.fields[sip_response_from]
sip.response_path
additional.fields[sip_response_path]
The
sip.response_path
log field is mapped to the
additional.fields.value.string_value
UDM field.
sip.response_to
additional.fields[sip_response_to]
sip.seq
additional.fields[sip_seq]
sip.status_msg
additional.fields[sip_status_msg]
sip.subject
additional.fields[sip_subject]
sip.trans_depth
additional.fields[sip_trans_depth]
smb_mapping.share_type
additional.fields[smb_mapping_share_type]
smtp.date
additional.fields[smtp_date]
smtp.first_received
additional.fields[smtp_first_received]
smtp.has_client_activity
additional.fields[smtp_has_client_activity]
smtp.last_reply
additional.fields[smtp_last_reply]
smtp.msg_id
additional.fields[smtp_msg_id]
smtp.path_list
additional.fields[smtp_path_list]
smtp.process_received_from
additional.fields[smtp_process_received_from]
smtp.second_received
additional.fields[smtp_second_received]
smtp.trans_depth
additional.fields[smtp_trans_depth]
smtp.user_agent
additional.fields[smtp_user_agent]
snmp.duration
additional.fields[snmp_duration]
snmp.get_bulk_requests
additional.fields[snmp_get_bulk_requests]
snmp.get_requests
additional.fields[snmp_get_requests]
snmp.get_responses
additional.fields[snmp_get_responses]
snmp.set_requests
additional.fields[snmp_set_requests]
snmp.up_since
additional.fields[snmp_up_since]
socks.status
additional.fields[socks_status]
socks.version
additional.fields[socks_version]
tunnel.tunnel_type
additional.fields[tunnel_tunnel_type]
Field mapping reference: ZSCALER_DECEPTION - postgresql
The following table lists the raw log fields for the
postgresql
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
postgresql.message
metadata.description
type
metadata.product_event_type
postgresql.user
principal.user.userid
postgresql.error_severity
security_result.severity_details
postgresql.state_code
security_result.detection_fields[postgresql_state_code]
postgresql.application_name
target.application
postgresql.session_id
target.network.session_id
postgresql.statement
target.process.command_line
postgresql.pid
target.process.pid
postgresql.vpid
target.process.product_specific_process_id
The
Deception:postgresql.vpid
log field is mapped to the
target.process.product_specific_process_id
UDM field.
postgresql.dbname
target.resource.name
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
DATABASE
.
postgresql.password
additional.fields[postgresql_password]
postgresql.vxid
additional.fields[postgresql_vxid]
Field mapping reference: ZSCALER_DECEPTION - QOS
The following table lists the raw log fields for the
QOS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
type
metadata.product_event_type
qos.message
metadata.description
Field mapping reference: ZSCALER_DECEPTION - recon
The following table lists the raw log fields for the
recon
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
recon.cve_type
extensions.vulns.vulnerabilities.about.security_result.detection_fields[recon_cve_type]
recon.cve_name
extensions.vulns.vulnerabilities.cve_description
recon.cve_id
extensions.vulns.vulnerabilities.cve_id
timestamp(Europe/Amsterdam)
metadata.event_timestamp
metadata.event_type
If (the
recon.http_x_forwarded_for
log field value is
not
empty or the
attacker.ip
log field value is
not
empty or the
attacker.name
log field value is
not
empty) and (the
decoy.ip
log field value is
not
empty or the
recon.host
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
recon.http_x_forwarded_for
log field value is
not
empty or the
attacker.ip
log field value is
not
empty or the
attacker.name
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
USER_STATS
.
type
metadata.product_event_type
id
metadata.product_log_id
recon.bytes_sent
network.sent_bytes
attacker.name
principal.hostname
recon.http_x_forwarded_for
principal.ip
attacker.ip
principal.ip
recon.scheme
principal.network.application_protocol
If the
recon.scheme
log field value contain one of the following values, then the
recon.scheme
log field is mapped to the
principal.network.application_protocol
UDM field.
AFP
APPC
AMQP
ATOM
BEEP
BITCOIN
BIT_TORRENT
CFDP
COAP
DCERPC
DDS
DEVICE_NET
DHCP
DNS
E_DONKEY
ENRP
FAST_TRACK
FINGER
FREENET
FTAM
GOPHER
HL7
H323
HTTP
HTTPS
IRCP
KADEMLIA
KRB5
LDAP
LPD
MIME
MODBUS
MQTT
NETCONF
NFS
NIS
NNTP
NTCIP
NTP
OSCAR
PNRP
QUIC
RDP
RELP
RIP
RLOGIN
RPC
RTMP
RTP
RTPS
RTSP
SAP
SDP
SIP
SLP
SMB
SMTP
SNTP
SSH
SSMS
STYX
TCAP
TDS
TOR
TSP
VTP
WHOIS
WEB_DAV
X400
X500
XMPP
attacker.id
principal.network.dns.id
recon.method
principal.network.http.method
recon.http_referrer
principal.network.http.referral_url
recon.status
principal.network.http.response_code
recon.user_agent.string
principal.network.http.user_agent
If the
recon.user_agent.string
log field value is
not
empty or the
recon.user_agent.string
log field value is
not
equal to
$
, then the
recon.user_agent.string
log field is mapped to the
principal.network.http.user_agent
UDM field.
principal.platform
If the
recon.user_agent.os.family
log field value matches the regular expression pattern
(?i)WIN
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
recon.user_agent.os.family
log field value matches the regular expression pattern
(?i)LIN
, then the
principal.platform
UDM field is set to
LINUX
.
Else, if the
recon.user_agent.os.family
log field value matches the regular expression pattern
(?i)(MAC or iOS)
, then the
principal.platform
UDM field is set to
MAC
.
recon.user_agent.os.patch
principal.platform_patch_level
recon.user_agent.os.major
principal.platform_version
The
recon.user_agent.os.major recon.user_agent.os.minor
log field is mapped to the
principal.platform_version
UDM field.
recon.user_agent.os.minor
principal.platform_version
The
recon.user_agent.os.major recon.user_agent.os.minor
log field is mapped to the
principal.platform_version
UDM field.
attacker.port
principal.port
attacker.threat_parse_ids
principal.security_result.detection_fields[attacker_threat_parse_ids]
The
attacker.threat_parse_ids
log field is mapped to the
security_result.detection_fields
UDM field.
attacker.score
principal.security_result.risk_score
recon.uri
principal.url
recon.post_data.username
principal.user.email_addresses
mitre_ids
security_result.attack_details.techniques.id
The
mitre_ids
log field is mapped to the
security_result.attack_details.techniques.id
UDM field.
abuseip.abuseConfidenceScore
security_result.confidence_score
is_itdr
security_result.detection_fields[is_itdr]
kill_chain_phase
security_result.detection_fields[kill_chain_phase]
threat_parse_ids
security_result.detection_fields[threat_parse_ids]
The
threat_parse_ids
log field is mapped to the
security_result.detection_fields
UDM field.
whitelisted
security_result.detection_fields[whitelisted]
updated_on
security_result.last_updated_time
score
security_result.risk_score
decoy.recon.dataset_type
security_result.rule_labels[decoy_recon_dataset_type]
decoy.recon.dataset
security_result.rule_set
severity
security_result.severity
If the
severity
log field value contain one of the following values, then the
severity
log field is mapped to the
security_result.severity
UDM field.
LOW
MEDIUM
HIGH
CRITICAL
severity
security_result.severity_details
abuseip.ipAddress
src.artifact.ip
abuseip.lastReportedAt
src.artifact.last_seen_time
abuseip.countryCode
src.artifact.location.country_or_region
recon.server_name
target.domain.whois_server
decoy.group
target.group.group_display_name
recon.host
target.hostname
decoy.ip
target.ip
target.network.application_protocol
The
app_proto
field is extracted from
recon.server_protocol
log field using the Grok pattern.
If the
app_proto
log field value contain one of the following values, then the
app_proto
extracted field is mapped to the
target.network.application_protocol
UDM field.
AFP
APPC
AMQP
ATOM
BEEP
BITCOIN
BIT_TORRENT
CFDP
COAP
DCERPC
DDS
DEVICE_NET
DHCP
DNS
E_DONKEY
ENRP
FAST_TRACK
FINGER
FREENET
FTAM
GOPHER
HL7
H323
HTTP
HTTPS
IRCP
KADEMLIA
KRB5
LDAP
LPD
MIME
MODBUS
MQTT
NETCONF
NFS
NIS
NNTP
NTCIP
NTP
OSCAR
PNRP
QUIC
RDP
RELP
RIP
RLOGIN
RPC
RTMP
RTP
RTPS
RTSP
SAP
SDP
SIP
SLP
SMB
SMTP
SNTP
SSH
SSMS
STYX
TCAP
TDS
TOR
TSP
VTP
WHOIS
WEB_DAV
X400
X500
XMPP
target.network.application_protocol_version
The
proto_version
field is extracted from
recon.server_protocol
log field using the Grok pattern.
If the
proto_version
log field value is
not
empty, then the
proto_version
extracted field is mapped to the
target.network.application_protocol_version
UDM field.
decoy.name
target.resource.name
decoy.id
target.resource.product_object_id
decoy.type
target.resource.resource_subtype
decoy.client.id
target.user.product_object_id
decoy.client.name
target.user.user_display_name
recon.http_basicauth_user
target.user.userid
version
additional.fields[
version
]
abuseip.ipVersion
additional.fields[abuseip_ipversion]
abuseip.isPublic
additional.fields[abuseip_ispublic]
abuseip.isWhitelisted
additional.fields[abuseip_iswhitelisted]
abuseip.totalReports
additional.fields[abuseip_total_reports]
decoy.appliance.id
additional.fields[decoy_appliance_id]
decoy.appliance.name
additional.fields[decoy_appliance_name]
decoy.network_name
additional.fields[decoy_network_name]
decoy.recon.server_type
additional.fields[decoy_recon_server_type]
decoy.vlan_id
additional.fields[decoy_vlan_id]
heatmap_per_week_15_min
additional.fields[heatmap_per_week_15_min]
indexed_on
additional.fields[indexed_on]
recon.content_length
additional.fields[recon_content_length]
recon.post_data.password
additional.fields[recon_post_data_password]
recon.post_data
additional.fields[recon_post_data]
recon.query_string
additional.fields[recon_query_string]
recon.request_body
additional.fields[recon_request_body]
recon.request_length
additional.fields[recon_request_length]
recon.request_time
additional.fields[recon_request_time]
recon.request_uri
additional.fields[recon_request_uri]
recon.request
additional.fields[recon_request]
recon.user_agent.family
additional.fields[recon_user_agent_family]
recon.user_agent.major
additional.fields[recon_user_agent_major]
recon.user_agent.minor
additional.fields[recon_user_agent_minor]
recon.user_agent.patch
additional.fields[recon_user_agent_patch]
record_type
additional.fields[record_type]
update_id
additional.fields[update_id]
Field mapping reference: ZSCALER_DECEPTION - scada
The following table lists the raw log fields for the
scada
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
scada.event_type
metadata.description
type
metadata.product_event_type
decoy.scada.dataset
security_result.rule_set
scada.data_type
additional.fields[scada_data_type]
scada.request
additional.fields[scada_request]
scada.response
additional.fields[scada_response]
Field mapping reference: ZSCALER_DECEPTION - ssh, telnet
The following table lists the raw log fields for the
ssh
and
telnet
log types and their corresponding UDM fields.
Log field
UDM mapping
Logic
extensions.auth.mechanism
If the
linux.remote_host
log field value is
not
empty, then the
extensions.auth.mechanism
UDM field is set to
REMOTE
.
metadata.event_type
If the
linux.remote_host
log field value is
not
empty and the
linux.user
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
type
metadata.product_event_type
linux.read_bytes
network.received_bytes
linux.written_bytes
network.sent_bytes
linux.remote_host
principal.ip
linux.vpid
principal.process.pid
linux.owner_id
principal.user.product_object_id
linux.user
principal.user.userid
If the
linux.remote_host
log field value is
not
empty, then the
linux.user
log field is mapped to the
target.user.userid
UDM field.
Else, the
linux.user
log field is mapped to the
principal.user.userid
UDM field.
linux.password
security_result.detection_fields[linux_password]
linux.new_path
target.file.full_path
linux.mode
target.file.security_result.detection_fields[linux_mode]
linux.group_id
target.group.product_object_id
target.platform
If the
decoy.ssh.ostype
log field value matches the regular expression pattern
(?i)Win
, then the
target.platform
UDM field is set to
WINDOWS
.
Else, if the
decoy.ssh.ostype
log field value matches the regular expression pattern
(?i)Lin
, then the
target.platform
UDM field is set to
LINUX
.
Else, if the
decoy.ssh.ostype
log field value matches the regular expression pattern
(?i)(Mac or iOS)
, then the
target.platform
UDM field is set to
MAC
.
If the
decoy.telnet.ostype
log field value matches the regular expression pattern
(?i)Win
, then the
target.platform
UDM field is set to
WINDOWS
.
Else, if the
decoy.telnet.ostype
log field value matches the regular expression pattern
(?i)Lin
, then the
target.platform
UDM field is set to
LINUX
.
Else, if the
decoy.telnet.ostype
log field value matches the regular expression pattern
(?i)(Mac or iOS)
, then the
target.platform
UDM field is set to
MAC
.
linux.command_line
target.process.command_line
linux.path
target.process.file.full_path
linux.ppid
target.process.parent_process.pid
linux.pid
target.process.pid
linux.process_name
target.process.product_specific_process_id
The
Deception:linux.process_name
log field is mapped to the
target.process.product_specific_process_id
UDM field.
linux.container_name
target.resource.name
target.resource.resource_type
If the
linux.container_name
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
CONTAINER
.
linux.connection_info
additional.fields[linux_connection_info]
linux.flags
additional.fields[linux_flags]
linux.info
additional.fields[linux_info]
linux.parent_process_name
additional.fields[linux_parent_process_name]
Field mapping reference: ZSCALER_DECEPTION - web
The following table lists the raw log fields for the
web
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
web.cve_type
extensions.vulns.vulnerabilities.about.security_result.detection_fields[web_cve_type]
web.cve_name
extensions.vulns.vulnerabilities.cve_description
web.cve_id
extensions.vulns.vulnerabilities.cve_id
metadata.event_type
If the
web.http_x_forwarded_for
log field value is
not
empty and (the
web.http_basicauth_user
log field value is
not
empty or the
web.post_data.username
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
type
metadata.product_event_type
web.bytes_sent
network.sent_bytes
web.http_x_forwarded_for
principal.ip
web.scheme
principal.network.application_protocol
If the
web.scheme
log field value contain one of the following values, then the
web.scheme
log field is mapped to the
principal.network.application_protocol
UDM field.
AFP
APPC
AMQP
ATOM
BEEP
BITCOIN
BIT_TORRENT
CFDP
COAP
DCERPC
DDS
DEVICE_NET
DHCP
DNS
E_DONKEY
ENRP
FAST_TRACK
FINGER
FREENET
FTAM
GOPHER
HL7
H323
HTTP
HTTPS
IRCP
KADEMLIA
KRB5
LDAP
LPD
MIME
MODBUS
MQTT
NETCONF
NFS
NIS
NNTP
NTCIP
NTP
OSCAR
PNRP
QUIC
RDP
RELP
RIP
RLOGIN
RPC
RTMP
RTP
RTPS
RTSP
SAP
SDP
SIP
SLP
SMB
SMTP
SNTP
SSH
SSMS
STYX
TCAP
TDS
TOR
TSP
VTP
WHOIS
WEB_DAV
X400
X500
XMPP
web.method
principal.network.http.method
web.http_referrer
principal.network.http.referral_url
web.status
principal.network.http.response_code
web.user_agent.string
principal.network.http.user_agent
principal.platform
If the
web.user_agent.os.family
log field value matches the regular expression pattern
(?i)Win
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
web.user_agent.os.family
log field value matches the regular expression pattern
(?i)Lin
, then the
principal.platform
UDM field is set to
LINUX
.
Else, if the
web.user_agent.os.family
log field value matches the regular expression pattern
(?i)(Mac or iOS)
, then the
principal.platform
UDM field is set to
MAC
.
web.user_agent.os.patch
principal.platform_patch_level
web.user_agent.os.major
principal.platform_version
The
web.user_agent.os.major web.user_agent.os.minor
log field is mapped to the
principal.platform_version
UDM field.
web.user_agent.os.minor
principal.platform_version
The
web.user_agent.os.major web.user_agent.os.minor
log field is mapped to the
principal.platform_version
UDM field.
web.uri
principal.url
decoy.web.dataset_type
security_result.rule_labels[decoy_web_dataset_type]
decoy.web.dataset
security_result.rule_set
web.host
target.hostname
target.network.application_protocol
The
app_proto
field is extracted from
web.server_protocol
log field using the Grok pattern.
If the
app_proto
log field value contain one of the following values, then the
app_proto
extracted field is mapped to the
target.network.application_protocol
UDM field.
AFP
APPC
AMQP
ATOM
BEEP
BITCOIN
BIT_TORRENT
CFDP
COAP
DCERPC
DDS
DEVICE_NET
DHCP
DNS
E_DONKEY
ENRP
FAST_TRACK
FINGER
FREENET
FTAM
GOPHER
HL7
H323
HTTP
HTTPS
IRCP
KADEMLIA
KRB5
LDAP
LPD
MIME
MODBUS
MQTT
NETCONF
NFS
NIS
NNTP
NTCIP
NTP
OSCAR
PNRP
QUIC
RDP
RELP
RIP
RLOGIN
RPC
RTMP
RTP
RTPS
RTSP
SAP
SDP
SIP
SLP
SMB
SMTP
SNTP
SSH
SSMS
STYX
TCAP
TDS
TOR
TSP
VTP
WHOIS
WEB_DAV
X400
X500
XMPP
web.post_data.username
target.user.email_addresses
web.http_basicauth_user
target.user.userid
decoy.web.server_type
additional.fields[decoy_web_server_type]
web.content_length
additional.fields[web_content_length]
web.post_data.password
additional.fields[web_post_data_password]
web.post_data
additional.fields[web_post_data]
web.query_string
additional.fields[web_query_string]
web.request_body
additional.fields[web_request_body]
web.request_length
additional.fields[web_request_length]
web.request_time
additional.fields[web_request_time]
web.request_uri
additional.fields[web_request_uri]
web.request
additional.fields[web_request]
web.user_agent.family
additional.fields[web_user_agent_family]
web.user_agent.major
additional.fields[web_user_agent_major]
web.user_agent.minor
additional.fields[web_user_agent_minor]
web.user_agent.patch
additional.fields[web_user_agent_patch]
Field mapping reference: ZSCALER_DECEPTION - windows
The following table lists the raw log fields for the
windows
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.event_type
If the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)read
, then the
metadata.event_type
UDM field is set to
FILE_READ
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)write or modify or encrypt
, then the
metadata.event_type
UDM field is set to
FILE_MODIFICATION
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)create
, then the
metadata.event_type
UDM field is set to
FILE_CREATION
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)delete
, then the
metadata.event_type
UDM field is set to
FILE_DELETION
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)open
, then the
metadata.event_type
UDM field is set to
FILE_OPEN
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)sync
, then the
metadata.event_type
UDM field is set to
FILE_SYNC
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)copy
, then the
metadata.event_type
UDM field is set to
FILE_COPY
.
Else, if the
file.path
log field value is
not
empty and the
attacker.domain
log field value is
not
empty, then if the
file.operation
log field value matches the regular expression pattern
(?i)move
, then the
metadata.event_type
UDM field is set to
FILE_MOVE
.
Else, if the
attacker.domain
log field value is
not
empty and (the
powershell.path
log field value is
not
empty or the
powershell.script_block_id
log field value is
not
empty or the
powershell.script_block_text
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
PROCESS_TERMINATION
.
Else, if the
attacker.domain
log field value is
not
empty and (the
smb.path
log field value is
not
empty or the
smb.file_name
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
FILE_READ
.
Else, if the
attacker.domain
log field value is
not
empty and the
network.destination.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, if the
attacker.domain
log field value is
not
empty and (the
wmi_process.command_line
log field value is
not
empty or the
wmi_process.created_process_id
log field value is
not
empty), then the
metadata.event_type
UDM field is set to
PROCESS_LAUNCH
.
Else, if the
attacker.domain
log field value is
not
empty and the
windows.base_vm_ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_STARTUP
.
Else, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
type
metadata.product_event_type
windows.incident_id
metadata.product_log_id
network.application_protocol
If the
message
log field value matches the regular expression pattern
ldap.
, then the
network.application_protocol
UDM field is set to
LDAP
.
Else, if the
message
log field value matches the regular expression pattern
rdp.
, then the
network.application_protocol
UDM field is set to
RDP
.
Else, if the
message
log field value matches the regular expression pattern
smb.
, then the
network.application_protocol
UDM field is set to
SMB
.
smb.session_guid
network.session_id
winrm.activity_id
network.session_id
attacker.process.domain_name
principal.domain.name
attacker.domain
principal.hostname
attacker.process.session_id
principal.network.session_id
attacker.process.command_line
principal.process.command_line
attacker.process.md5
principal.process.file.md5
attacker.process.sha1
principal.process.file.sha1
attacker.process.sha256
principal.process.file.sha256
attacker.process.parent
principal.process.parent_process.pid
attacker.process.id
principal.process.pid
psexec.service_name
principal.resource.name
principal.resource.resource_type
If the
psexec.service_name
log field value is
not
empty, then the
principal.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
attacker.process.user_groups
principal.user.group_identifiers
The
attacker.process.user_groups
log field is mapped to the
principal.user.group_identifiers
UDM field.
attacker.process.user_ou
principal.user.group_identifiers
The
attacker.process.user_groups
log field is mapped to the
principal.user.group_identifiers
UDM field and the
attacker.process.user_ou
log field is mapped to the
principal.user.group_identifiers
UDM field.
attacker.process.user_name
principal.user.user_display_name
attacker.user
principal.user.userid
attacker.process.user_sid
principal.user.windows_sid
attacker.process.exit_code
security_result.detection_fields[attacker_process_exit_code]
file.operation_string
security_result.detection_fields[file_operation_string]
file.operation
security_result.detection_fields[file_operation]
mssql.data_sensitivity_information
security_result.detection_fields[mssql_data_sensitivity_information]
mssql.is_column_permission
security_result.detection_fields[mssql_is_column_permission]
decoy.smb.dataset
security_result.rule_set
smb.disconnect_reason
security_result.summary
network.source.hostname
src.hostname
network.source.ip
src.ip
network.source.port
src.port
wmi_process.client_machine_fqdn
target.domain.name
mssql.server_instance_name
target.domain.name_server
file.path
target.file.full_path
smb.path
target.file.full_path
psexec.md5
target.file.md5
file.file_name
target.file.names
psexec.file_and_pipe_names
target.file.names
The
psexec.file_and_pipe_names
log field is mapped to the
target.file.names
UDM field.
smb.file_name
target.file.names
psexec.sha1
target.file.sha1
psexec.sha256
target.file.sha256
mssql.host_name
target.hostname
network.destination.hostname
target.hostname
wmi_process.client_machine
target.hostname
windows.base_vm_ip
target.ip
mssql.client_ip
target.ip
network.destination.ip
target.ip
mssql.duration_milliseconds
target.network.session_duration.seconds
mssql.session_id
target.network.session_id
rdp.session_id
target.network.session_id
smb.connection_guid
target.network.session_id
target.platform
If the
decoy.vm.os
log field value matches the regular expression pattern
(?i)Win
, then the
target.platform
UDM field is set to
WINDOWS
.
Else, if the
decoy.vm.os
log field value matches the regular expression pattern
(?i)Lin
, then the
target.platform
UDM field is set to
LINUX
.
Else, if the
decoy.vm.os
log field value matches the regular expression pattern
(?i)(Mac or iOS)
, then the
target.platform
UDM field is set to
MAC
.
network.destination.port
target.port
wmi_process.command_line
target.process.command_line
powershell.script_block_text
target.process.command_line
powershell.path
target.process.file.full_path
wmi_process.client_process_id
target.process.parent_process.pid
wmi_process.created_process_id
target.process.pid
powershell.script_block_id
target.process.product_specific_process_id
The
Deception:powershell.script_block_id
log field is mapped to the
target.process.product_specific_process_id
UDM field.
mssql.database_principal_id
target.resource_ancestors.attribute.labels[mssql_database_principal_id]
mssql.database_principal_name
target.resource_ancestors.attribute.labels[mssql_database_principal_name]
target.resource_ancestors.resource_type
If the
mssql.database_name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
DATABASE
.
ldap.attribute_list
target.resource.attribute.labels[ldap_attribute_list]
The
ldap.attribute_list
log field is mapped to the
target.resource.attribute.labels
UDM field.
ldap.distinguished_name
target.resource.attribute.labels[ldap_distinguished_name]
ldap.scope_of_search_string
target.resource.attribute.labels[ldap_scope_of_search_string]
ldap.scope_of_search
target.resource.attribute.labels[ldap_scope_of_search]
ldap.search_filter
target.resource.attribute.labels[ldap_search_filter]
decoy.vm.name
target.resource.name
mssql.database_name
target.resource.name
decoy.vm.id
target.resource.product_object_id
smb.tree_connect_guid
target.resource.product_object_id
target.resource.resource_type
If the
decoy.vm.id
log field value is
not
empty or the
decoy.vm.name
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
attacker.process.name
additional.fields[attacker_process_name]
attacker.process.thread_id
additional.fields[attacker_process_thread_id]
attacker.process.tree
additional.fields[attacker_process_tree]
The
attacker.process.tree
log field is mapped to the
additional.fields.value.string_value
UDM field.
mssql.action_id
additional.fields[mssql_action_id]
mssql.action_string
additional.fields[mssql_action_string]
mssql.additional_information
additional.fields[mssql_additional_information]
mssql.affected_rows
additional.fields[mssql_affected_rows]
mssql.application_name
additional.fields[mssql_application_name]
mssql.audit_schema_version
additional.fields[mssql_audit_schema_version]
mssql.class_type_string
additional.fields[mssql_class_type_string]
mssql.class_type
additional.fields[mssql_class_type]
mssql.connection_id
additional.fields[mssql_connection_id]
mssql.event_time
additional.fields[mssql_event_time]
mssql.object_id
additional.fields[mssql_object_id]
mssql.object_name
additional.fields[mssql_object_name]
mssql.permission_bitmask
additional.fields[mssql_permission_bitmask]
mssql.response_rows
additional.fields[mssql_response_rows]
mssql.schema_name
additional.fields[mssql_schema_name]
mssql.sequence_group_id
additional.fields[mssql_sequence_group_id]
mssql.sequence_number
additional.fields[mssql_sequence_number]
mssql.server_principal_id
additional.fields[mssql_server_principal_id]
mssql.server_principal_name
additional.fields[mssql_server_principal_name]
mssql.server_principal_sid
additional.fields[mssql_server_principal_sid]
mssql.session_server_principal_name
additional.fields[mssql_session_server_principal_name]
mssql.statement
additional.fields[mssql_statement]
mssql.succeeded
additional.fields[mssql_succeeded]
mssql.target_database_principal_id
additional.fields[mssql_target_database_principal_id]
mssql.target_database_principal_name
additional.fields[mssql_target_database_principal_name]
mssql.target_server_principal_id
additional.fields[mssql_target_server_principal_id]
mssql.target_server_principal_name
additional.fields[mssql_target_server_principal_name]
mssql.target_server_principal_sid
additional.fields[mssql_target_server_principal_sid]
mssql.transaction_id
additional.fields[mssql_transaction_id]
mssql.user_defined_event_id
additional.fields[mssql_user_defined_event_id]
mssql.user_defined_information
additional.fields[mssql_user_defined_information]
powershell.message_number
additional.fields[powershell_message_number]
powershell.message_total
additional.fields[powershell_message_total]
rdp.activity_id
additional.fields[rdp_activity_id]
smb.lease_id
additional.fields[smb_lease_id]
smb.open_guid
additional.fields[smb_open_guid]
smb.share_guid
additional.fields[smb_share_guid]
wmi_process.client_process_creation_time
additional.fields[wmi_process_client_process_creation_time]
wmi_process.correlation_id
additional.fields[wmi_process_correlation_id]
wmi_process.created_process_creation_time
additional.fields[wmi_process_created_process_creation_time]
wmi_process.group_operation_id
additional.fields[wmi_process_group_operation_id]
wmi_process.is_local
additional.fields[wmi_process_is_local]
wmi_process.operation_id
additional.fields[wmi_process_operation_id]
Need more help?
Get answers from Community members and Google SecOps professionals.
