# Collect Google Cloud SQL logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-cloudsql/  
**Scraped:** 2026-03-05T09:17:22.574638Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud SQL logs
This document describes how you can export Cloud SQL logs by enabling Google Cloud
telemetry ingestion to Google Security Operations and how Cloud SQL logs fields map to
Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations overview
.
A typical deployment consists of Cloud SQL logs enabled for ingestion to
Google Security Operations. Each customer deployment might differ from this
representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs
Cloud SQL logs
: The Cloud SQL logs that are enabled for ingestion to Google Security Operations
Google Security Operations
: Retains and analyzes Cloud SQL logs and
Google Workspace audit logs
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with
GCP_CLOUDSQL
ingestion label.
Before you begin
Ensure that you have set up access control for your organization and resources
using Identity and Access Management (IAM). For more information about access control, see
Access control for organizations with IAM
.
Ensure that all systems in the deployment architecture are configured
in the UTC time zone.
Verify the methods that the Cloud SQL parser supports. The following table
lists the resources and methods supported by the Cloud SQL parser:
Resources
Methods
backupRun
get
insert
delete
list
databases
get
delete
insert
list
patch
update
instances
get
list
create
clone
delete
addServerCa
demoteMaster
export
failover
import
insert
listServerCas
patch
promoteReplica
query
resetSslConfig
restart
restoreBackup
rotateServerCa
startReplica
stopReplica
truncateLog
update
operations
get
list
projects.instances
rescheduleMaintenance
startExternalSync
verifyExternalSyncSettings
sslCerts
createEphemeral
delete
get
insert
list
tires
list
users
delete
get
insert
list
update
flags
list
Configure ingestion of Cloud SQL logs
To ingest Cloud SQL logs to Google Security Operations, follow the steps on the
Ingest Google Cloud logs to Google Security Operations
page.
If you encounter issues when you ingest  Cloud SQL logs,
contact Google Security Operations support
.
Supported Cloud SQL log formats
The Cloud SQL parser supports logs in JSON format.
Supported Cloud SQL sample logs
JSON
{
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "status": {},
    "authenticationInfo": {
      "principalEmail": "test.user@example.com"
    },
    "requestMetadata": {
      "callerIp": "198.51.100.0",
      "requestAttributes": {
        "time": "2023-05-18T06:16:08.481272Z",
        "auth": {}
      },
      "destinationAttributes": {}
    },
    "serviceName": "cloudsql.googleapis.com",
    "methodName": "cloudsql.backupRuns.list",
    "authorizationInfo": [
      {
        "resource": "projects/test-project/instances/test-instance",
        "permission": "cloudsql.backupRuns.list",
        "granted": true,
        "resourceAttributes": {
          "service": "sqladmin.googleapis.com",
          "name": "projects/test-project/instances/test-instance",
          "type": "sqladmin.googleapis.com/Instance"
        }
      }
    ],
    "resourceName": "projects/test-project/instances/test-instance",
    "request": {
      "instance": "test-instance",
      "maxResults": 1000,
      "project": "dummy-project",
      "@type": "type.googleapis.com/google.cloud.sql.v1beta4.SqlBackupRunsListRequest"
    }
  },
  "insertId": "9fsk13e6h22g",
  "resource": {
    "type": "cloudsql_database",
    "labels": {
      "database_id": "test-project:test-instance",
      "region": "us-central1",
      "project_id": "dummy-project"
    }
  },
  "timestamp": "2023-05-18T06:16:08.383405Z",
  "severity": "INFO",
  "logName": "projects/test-project/logs/cloudaudit.googleapis.com%2Fdata_access",
  "receiveTimestamp": "2023-05-18T06:16:08.563749821Z"
}
Field mapping reference
This section explains how the Google Security Operations parser maps Cloud SQL logs fields to Google Security Operations Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
protoPayload.request.spec.containers.0.args
about.file.capabilities_tags
protoPayload.metadata.backupCompletionTime
about.labels[backup_completion_time]
(deprecated)
protoPayload.metadata.backupCompletionTime
additional.fields[backup_completion_time]
protoPayload.metadata.backupStartTime
about.labels[backup_start_time]
(deprecated)
protoPayload.metadata.backupStartTime
additional.fields[backup_start_time]
protoPayload.request.objects.db
target.resource.attribute.labels.0.[database_name]
protoPayload.request.objects.object_type
target.resource.attribute.labels.0.[objects_type]
jsonPayload.executionState
target.resource.attribute.labels[execution_state]
protoPayload.request.body.failoverContext.kind
about.labels[fail_over_context_kind]
(deprecated)
protoPayload.request.body.failoverContext.kind
additional.fields[fail_over_context_kind]
protoPayload.request.body.failoverContext.settingsVersion
about.labels[fail_over_context_settings_version]
(deprecated)
protoPayload.request.body.failoverContext.settingsVersion
additional.fields[fail_over_context_settings_version]
protoPayload.request.filter
about.labels[filter]
(deprecated)
protoPayload.request.filter
additional.fields[filter]
labels.instance_id
about.labels[instance_id]
(deprecated)
labels.instance_id
additional.fields[instance_id]
labels.INSTANCE_UID
about.labels[instance_uid]
(deprecated)
labels.INSTANCE_UID
additional.fields[instance_uid]
labels.PROJECT_NUMBER
additional.fields[project_number]
labels.SOURCE_ID
additional.fields[source_id]
protoPayload.metadata.intents.intent
about.labels[intent]
resource.labels.job_id
target.resource.product_object_id
jsonPayload.jobName
target.resource.name
jsonPayload.@type
about.labels[jsonPayload_at_type]
(deprecated)
jsonPayload.@type
additional.fields[jsonPayload_at_type]
labels.LOG_BUCKET_NUM
about.labels[log_bucket_num]
(deprecated)
labels.LOG_BUCKET_NUM
additional.fields[log_bucket_num]
protoPayload.metadata.@type
about.labels[metadata_at_type]
(deprecated)
protoPayload.metadata.@type
additional.fields[metadata_at_type]
resource.labels.method
about.labels[method]
(deprecated)
resource.labels.method
additional.fields[method]
protoPayload.request.objects.name
target.resource.attribute.labels.0.[objects_name]
operation.first
about.labels[operation_first]
(deprecated)
operation.first
additional.fields[operation_first]
operation.id
about.labels[operation_id]
(deprecated)
operation.id
additional.fields[operation_id]
operation.last
about.labels[operation_last]
(deprecated)
operation.last
additional.fields[operation_last]
operation.producer
about.labels[operation_producer]
(deprecated)
operation.producer
additional.fields[operation_producer]
protoPayload.@type
about.labels[protopayload_at_type]
(deprecated)
protoPayload.@type
additional.fields[protopayload_at_type]
protoPayload.metadata.intents.diffs.newValue
about.labels[protoPayload.metadata.intents.diffs.property]
protoPayload.response.kind
about.labels[res_kind]
(deprecated)
protoPayload.response.kind
additional.fields[res_kind]
protoPayload.response.operationType
about.labels[res_operation_type]
(deprecated)
protoPayload.response.operationType
additional.fields[res_operation_type]
protoPayload.response.@type
about.labels[response_type]
(deprecated)
protoPayload.response.@type
additional.fields[response_type]
jsonPayload.resultState
target.resource.attribute.labels[result_state]
jsonPayload.scheduledTime
target.resource.attribute.labels[scheduled_time]
jsonPayload.status
target.resource.attribute.labels[status]
jsonPayload.targetType
target.resource.attribute.labels[target_type]
jsonPayload.trace_id
about.labels[trace_id]
(deprecated)
jsonPayload.trace_id
additional.fields[trace_id]
trace
about.labels[trace]
(deprecated)
trace
additional.fields[trace]
jsonPayload.urlsCrawledCount
target.resource.attribute.labels[urls_crwaled_count]
protoPayload.metadata.windowEndTime
about.labels[window_end_time]
(deprecated)
protoPayload.metadata.windowEndTime
additional.fields[window_end_time]
protoPayload.metadata.windowStartTime
about.labels[window_start_time]
(deprecated)
protoPayload.metadata.windowStartTime
additional.fields[window_start_time]
protoPayload.metadata.windowStatus
about.labels[window_status]
(deprecated)
protoPayload.metadata.windowStatus
additional.fields[window_status]
protoPayload.response.selfLink
about.url
receiveTimestamp
metadata.collected_timestamp
protoPayload.response.operationType
metadata.description
protoPayload.response.kind
metadata.description
protoPayload.metadata.message
metadata.description
metadata.description
Extracted
log_message
from
textPayload
log field using the Grok pattern, and the
log_message
extracted field is mapped to the
metadata.descriptiom
UDM field.
timestamp
metadata.event_timestamp
jsonPayload.event_timestamp_us
metadata.event_timestamp
protoPayload.metadata.projectMetadataDelta.addedMetadataKeys
metadata.ingestion_labels[project_metadata_keys_added]
protoPayload.metadata.projectMetadataDelta.deletedMetadataKeys
metadata.ingestion_labels[project_metadata_keys_deleted]
protoPayload.metadata.instanceMetadataDelta.addedMetadataKeys
metadata.ingestion_labels[instance_metadata_key_added]
protoPayload.metadata.instanceMetadataDelta.deletedMetadataKeys
metadata.ingestion_labels[instance_metadata_key_deleted]
protoPayload.metadata.instanceMetadataDelta.modifiedMetadataKeys
metadata.ingestion_labels[instance_metadata_key_modified]
protoPayload.metadata.projectMetadataDelta.modifiedMetadataKeys
metadata.ingestion_labels[project_metadata_keys_modified]
protoPayload.methodName
metadata.product_event_type
jsonPayload.event_subtype
metadata.product_event_type
jsonPayload._AUDIT_TYPE_NAME
metadata.product_event_type
insertId
metadata.product_log_id
metadata.product_name
If the
protoPayload.serviceName
log field value matches the regular expression
(compute.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Google Compute Engine
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(bigquery.googleapis.com)
, then the
metadata.product_name
UDM field is set to
BigQuery
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(admin.googleapis.com or login.googleapis.com or cloudidentity.googleapis.com)
, then the
metadata.product_name
UDM field is set to
G Suite
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(k8s.io)
, then the
metadata.product_name
UDM field is set to
Google Kubernetes Engine
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(servicemanagement.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Google Service Management
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(storage.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Google Cloud Storage
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(cloudsql.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Google Cloud SQL
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(dataproc.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Google Dataproc
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(iam.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Google Cloud IAM
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(accesscontextmanager.googleapis.com)
, then the
metadata.product_name
UDM field is set to
Context Manager API
.
Else, if the
protoPayload.serviceName
log field value matches the regular expression
(storage.googleapis.com)
, then if the
message
log field value matches the regular expression
dns.googleapis.com
then the
metadata.product_name
UDM field is set to
Google Cloud DNS
.
Else the
metadata.product_name
UDM field is set to
Google Cloud Platform
.
If the
resource.type
log field value matches the regular expression
gce_instance
, then the
metadata.product_name
UDM field is set to
GCP Compute Engine
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
protoPayload.metadata.request_id
network.community_id
protoPayload.request.direction
network.direction
If the
protoPayload.request.direction
log field value is equal to
INGRESS
, then the
network.direction
UDM field is set to
INBOUND
.
Else, if the
protoPayload.request.direction
log field value is equal to
EGRESS
, then the
network.direction
UDM field is set to
OUTBOUND
.
protoPayload.resourceOriginalState.direction
network.direction
If the
protoPayload.resourceOriginalState.direction
log field value is equal to
INGRESS
, then the
network.direction
UDM field is set to
INBOUND
.
Else, if the
protoPayload.resourceOriginalState.direction
log field value is equal to
EGRESS
, then the
network.direction
UDM field is set to
OUTBOUND
.
httpRequest.requestMethod
network.http.method
httpRequest.requestUrl
network.http.referral_url
protoPayload.resourceOriginalState.network
network.http.referral_url
httpRequest.status
network.http.response_code
protoPayload.response.code
network.http.response_code
protoPayload.status.code
network.http.response_code
If the
protoPayload.status.code
log field value is equal to
0
, then the
network.http.response_code
UDM field is set to
200
.
Else, if the
protoPayload.status.code
log field value is equal to
1
, then the
network.http.response_code
UDM field is set to
499
.
Else, if the
protoPayload.status.code
log field value contains one of the following values, then the
network.http.response_code
UDM field is set to
500
.
2
13
15
Else, if the
protoPayload.status.code
log field value contains one of the following values, then the
network.http.response_code
UDM field is set to
400
.
3
9
11
Else, if the
protoPayload.status.code
log field value is equal to
4
, then the
network.http.response_code
UDM field is set to
504
.
Else, if the
protoPayload.status.code
log field value is equal to
5
, then the
network.http.response_code
UDM field is set to
404
.
Else, if the
protoPayload.status.code
log field value contains one of the following values, then the
network.http.response_code
UDM field is set to
409
.
6
10
Else, if the
protoPayload.status.code
log field value is equal to
7
, then the
network.http.response_code
UDM field is set to
403
.
Else, if the
protoPayload.status.code
log field value is equal to
8
, then the
network.http.response_code
UDM field is set to
429
.
Else, if the
protoPayload.status.code
log field value is equal to
12
, then the
network.http.response_code
UDM field is set to
501
.
Else, if the
protoPayload.status.code
log field value is equal to
14
, then the
network.http.response_code
UDM field is set to
503
.
Else, if the
protoPayload.status.code
log field value is equal to
16
, then the
network.http.response_code
UDM field is set to
401
.
httpRequest.userAgent
network.http.user_agent
protoPayload.requestMetadata.callerSuppliedUserAgent
network.http.user_agent
jsonPayload.connection.protocol
network.ip_protocol
jsonPayload.current.ports.0.protocol
network.ip_protocol
httpRequest.responseSize
network.received_bytes
httpRequest.requestSize
network.sent_bytes
network.session_duration
The
log_message
field is extracted from
textPayload
log field using Grok pattern,
If the
log_message
field value matches the regular expression pattern
disconnection
, then the
session_time
field is extracted from
log_message
log field using Grok pattern, and the
session_time
field is mapped to the
network.session_duration
UDM field.
protoPayload.response.clientCert.certInfo.expirationTime
network.tls.client.certificate.not_after
protoPayload.response.clientCert.certInfo.createTime
network.tls.client.certificate.not_before
protoPayload.response.clientCert.certInfo.certSerialNumber
network.tls.client.certificate.serial
protoPayload.request.sha1Fingerprint
network.tls.client.certificate.sha1
protoPayload.response.clientCert.certInfo.sha1Fingerprint
network.tls.client.certificate.sha1
protoPayload.response.clientCert.certInfo.commonName
network.tls.client.certificate.subject
protoPayload.response.serverCaCert.expirationTime
network.tls.server.certificate.not_after
protoPayload.response.serverCaCert.createTime
network.tls.server.certificate.not_before
protoPayload.response.serverCaCert.certSerialNumber
network.tls.server.certificate.serial
protoPayload.response.serverCaCert.sha1Fingerprint
network.tls.server.certificate.sha1
protoPayload.response.serverCaCert.commonName
network.tls.server.certificate.subject
jsonPayload.queryName
principal.domain.name
jsonPayload._HOSTNAME
principal.hostname
principal.ip
If the
logName
log field value matches the regular expression pattern
mysql-general
, then the
src_ip
field is extracted from
textPayload
log field using Grok pattern, and the
src_ip
field is mapped to the
principal.ip
UDM field.
protoPayload.requestMetadata.callerIp
principal.ip
httpRequest.serverIp
principal.ip
jsonPayload.current.clusterIPs
principal.ip
protoPayload.requestMetadata.requestAttributes.reason
principal.labels[request_attributes_reason]
(deprecated)
protoPayload.requestMetadata.requestAttributes.reason
additional.fields[request_attributes_reason]
protoPayload.redactions.field
protoPayload.redactions.reason
protoPayload.redactions.type
principal.labels[protoPayload.redactions.field]
The value of the UDM field
principal.labels.value
is determined by combining the values of the log fields
protoPayload.redactions.reason
and
protoPayload.redactions.type
, which are separated by a
:
delimiter.
protoPayload.request.policy.bindings.members
principal.labels[req_bindings_members]
protoPayload.request.requestId
principal.labels[request_id]
(deprecated)
protoPayload.request.requestId
additional.fields[request_id]
protoPayload.requestMetadata.requestAttributes.time
principal.labels[request_attributes_time]
(deprecated)
protoPayload.requestMetadata.requestAttributes.time
additional.fields[request_attributes_time]
jsonPayload.sourceNetwork
principal.labels[source_network]
(deprecated)
jsonPayload.sourceNetwork
additional.fields[source_network]
protoPayload.request.metadata.namespace
additional.fields[request_metadata_namespace]
jsonPayload.connection.nat_port
principal.nat_port
jsonPayload.connection.src_port
principal.port
jsonPayload.current.ports.0.port
principal.port
principal.process.command_line
If the
logName
log field value matches the regular expression pattern
mysql-general
, then the
command
field is extracted from
textPayload
log field using Grok pattern, and the
command
field is mapped to the
principal.process.command_line
UDM field.
principal.process.pid
The
process_id
field is extracted from
textPayload
log field using Grok pattern, and the
process_id
field is mapped to the
principal.process.pid
UDM field.
protoPayload.request.properties.disks.0.type
principal.resource.attribute.labels[disks_type]
protoPayload.request.properties.disks.0.initializeParams.diskSizeGb
principal.resource.attribute.labels[disk_size_gb]
protoPayload.request.properties.disks.0.initializeParams.diskType
principal.resource.attribute.labels[disk_type]
protoPayload.request.properties.disks.0.initializeParams.guestOsFeatures.0.type
principal.resource.attribute.labels[guest_os_features_type]
protoPayload.request.properties.disks.0.initializeParams.labels.0.key
principal.resource.attribute.labels[protoPayload.request.properties.disks.0.initializeParams.labels.0.key]
protoPayload.request.properties.disks.0.initializeParams.labels.0.value
principal.resource.attribute.labels[protoPayload.request.properties.disks.0.initializeParams.labels.0.key]
protoPayload.request.properties.disks.0.initializeParams.sourceImage
principal.resource.attribute.labels[source_image]
protoPayload.resourceName
principal.resource.name
If the
protoPayload.methodName
log field value is equal to
cloudsql.instances.clone
, then the
protoPayload.resourceName
log field is mapped to the
principal.resource.name
UDM field.
protoPayload.resourceOriginalState.name
principal.resource.name
protoPayload.authorizationInfo.authorizationLoggingOptions.permissionType
principal.user.attribute.permissions.type
protoPayload.metadata.membershipDelta.roleDeltas.action
principal.user.attribute.roles.description
protoPayload.serviceData.policyDelta.bindingDeltas.action
principal.user.attribute.roles.description
protoPayload.metadata.event.eventType
principal.user.attribute.roles.description
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
ASSIGN_ROLE
, then the
protoPayload.metadata.event.eventType
log field is mapped to the
principal.user.attribute.roles.description
UDM field.
protoPayload.metadata.event.parameter.2.name
principal.user.attribute.roles.description
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
UPDATE_GROUP_MEMBER
, then the
protoPayload.metadata.event.parameter.2.name
log field is mapped to the
principal.user.attribute.roles.description
UDM field.
protoPayload.metadata.event.parameter.3.name
principal.user.attribute.roles.description
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
UPDATE_GROUP_MEMBER
, then the
protoPayload.metadata.event.parameter.3.name
log field is mapped to the
principal.user.attribute.roles.description
UDM field.
protoPayload.metadata.membershipDelta.roleDeltas.role
principal.user.attribute.roles.name
protoPayload.serviceData.policyDelta.bindingDeltas.role
principal.user.attribute.roles.name
protoPayload.metadata.event.parameter.0.value
principal.user.attribute.roles.name
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
ASSIGN_ROLE
, then the
protoPayload.metadata.event.parameter.0.value
log field is mapped to the
principal.user.attribute.roles.name
UDM field.
protoPayload.metadata.event.parameter.2.value
principal.user.attribute.roles.name
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
UPDATE_GROUP_MEMBER
, then the
protoPayload.metadata.event.parameter.2.value
log field is mapped to the
principal.user.attribute.roles.name
UDM field.
protoPayload.metadata.event.parameter.3.value
principal.user.attribute.roles.name
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
UPDATE_GROUP_MEMBER
, then the
protoPayload.metadata.event.parameter.3.value
log field is mapped to the
principal.user.attribute.roles.name
UDM field.
jsonPayload.actor.user
principal.user.email_addresses
protoPayload.authenticationInfo.principalEmail
principal.user.email_addresses
protoPayload.authenticationInfo.serviceAccountDelegationInfo.firstPartyPrincipal.principalEmail
principal.user.email_addresses
protoPayload.authenticationInfo.principalEmail
principal.user.userid
If the
protoPayload.authenticationInfo.principalEmail
log field value matches the regular expression pattern
.*@.*
, then the
user_id
field is extracted from
protoPayload.authenticationInfo.principalEmail
log field using Grok pattern, and the
user_id
field is mapped to the
principal.user.userid
UDM field.
Else, if the
protoPayload.authenticationInfo.principalSubject
log field value is
not
empty, then the
userid
field is extracted from
protoPayload.authenticationInfo.principalSubject
log field using Grok pattern, and the
userid
field is mapped to the
principal.user.userid
UDM field.
Else, the
protoPayload.authenticationInfo.principalEmail
log field is mapped to the
principal.user.userid
UDM field.
jsonPayload.actor.user
principal.user.userid
If the
jsonPayload.actor.user
log field value matches the regular expression pattern
.*@.*
, then the
user_id
field is extracted from
jsonPayload.actor.user
log field using Grok pattern, and the
user_id
field is mapped to the
principal.user.userid
UDM field.
Else, the
jsonPayload.actor.user
log field is mapped to the
principal.user.userid
UDM field.
protoPayload.authenticationInfo.principalSubject
principal.user.userid
principal.user.userid
If the
logName
log field value matches the regular expression pattern
postgres.log
, then the
userid
field is extracted from
textPayload
log field using Grok pattern, and the
userid
log field is mapped to the
principal.user.userid
UDM field.
If the
logName
log field value matches the regular expression pattern
mysql-general
, then the
user_id
field is extracted from
textPayload
log field using Grok pattern, and the
user_id
field is mapped to the
principal.user.userid
UDM field.
labels.pod-security.kubernetes.io/enforce-policy
security_result.about.resource.attribute.labels[labels_enforce_policy]
labels.mutation.webhook.admission.k8s.io/round_0_index_0
security_result.about.resource.attribute.labels[labels_round_0_index_0]
labels.authorization.k8s.io/decision
security_result.action
logName
security_result.category_details
protoPayload.request.status
security_result.description
protoPayload.status.message
security_result.description
labels.authorization.k8s.io/reason
security_result.description
textPayload
security_result.description
If the
resource.type
log field value is equal to
cloud_function
, then the
textPayload
log field is mapped to the
security_result.description
UDM field.
security_result.description
If the
logName
log field value matches the regular expression pattern
mysql.err
, then the
error_description
field is extracted from
textPayload
log field using Grok pattern, and the
error_description
field is mapped to the
security_result.description
UDM field.
protoPayload.serviceData.policyDelta.auditConfigDeltas.action
security_result.detection_fields[action]
protoPayload.request.cryptoKey.versionTemplate.algorithm
security_result.detection_fields[algorithm]
protoPayload.request.alloweds.IPProtocol
security_result.detection_fields[allowed_ipprotocol]
protoPayload.request.alloweds.ports
security_result.detection_fields[allowed_ports]
protoPayload.response.details.0.@type
security_result.detection_fields[details_type]
protoPayload.request.cryptoKey.nextRotationTime
security_result.detection_fields[next_rotation_time]
protoPayload.request.cryptoKey.versionTemplate.protectionLevel
security_result.detection_fields[protection_level]
protoPayload.request.cryptoKey.purpose
security_result.detection_fields[purpose]
protoPayload.authorizationInfo.resource
security_result.detection_fields[resource]
protoPayload.resourceOriginalState.direction
security_result.detection_fields[resource_original_state_direction]
protoPayload.resourceOriginalState.logConfig.enable
security_result.detection_fields[resource_original_state_log_config_enable]
protoPayload.request.cryptoKey.rotationPeriod
security_result.detection_fields[rotation_period]
protoPayload.serviceData.policyDelta.auditConfigDeltas.service
security_result.detection_fields[service]
protoPayload.response.details.0.violations.0.subject
security_result.detection_fields[violation_subject]
protoPayload.response.details.0.violations.0.type
security_result.detection_fields[violation_type]
protoPayload.metadata.dryRun
security_result.rule_type
severity
security_result.severity
If the
severity
log field value is equal to
CRITICAL
, then the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
severity
log field value is equal to
ERROR
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
severity
log field value contains one of the following values, then the
security_result.severity
UDM field is set to
HIGH
.
ALERT
EMERGENCY
else, if the
severity
log field value contains one of the following values, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
INFO
NOTICE
else, if the
severity
log field value is equal to
DEBUG
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
severity
log field value is equal to
WARNING
, then the
security_result.severity
UDM field is set to
MEDIUM
.
protoPayload.request.description
security_result.summary
protoPayload.response.message
security_result.summary
jsonPayload.summary
security_result.summary
protoPayload.serviceName
target.application
If the
logName
log field value matches the regular expression pattern
postgres.log
, then the
log_message
field is extracted from
textPayload
log field using Grok pattern, and if the
log_message
field value matches the regular expression pattern
connection authorized
, then the
app_name
field is extracted from
log_message
log field using Grok pattern, and the
app_name
log field is mapped to the
target.application
UDM field.
Else, the
protoPayload.serviceName
log field is mapped to the
target.application
UDM field.
protoPayload.metadata.device_id
target.asset.asset_id
jsonPayload._MACHINE_ID
target.asset.asset_id
protoPayload.request.instances.instance
target.asset.product_object_id
resource.labels.project_id
target.cloud.project.name
protoPayload.request.spec.containers.0.image
target.file.full_path
sourceLocation.function
target.file.full_path
protoPayload.metadata.event.parameter.1.value
target.group.email_addresses
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
ADD_GROUP_MEMBER or UPDATE_GROUP_MEMBER
, then if the
protoPayload.metadata.event.parameter.1
log field value is equal to
GROUP_EMAIL
, then the
protoPayload.metadata.event.parameter.1.value
log field is mapped to the
target.group.email_addresses
UDM field.
Else, the
protoPayload.metadata.event.parameter.1.value
log field is mapped to the
target.group.product_object_id
UDM field.
protoPayload.metadata.group
target.group.email_addresses
protoPayload.metadata.event.parameter.1.name
target.group.group_display_name
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
ADD_GROUP_MEMBER or UPDATE_GROUP_MEMBER
, then the
protoPayload.metadata.event.parameter.1.name
log field is mapped to the
target.group.group_display_name
UDM field.
protoPayload.metadata.event.parameter.1.value
target.group.product_object_id
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
ADD_GROUP_MEMBER or UPDATE_GROUP_MEMBER
, then if the
protoPayload.metadata.event.parameter.1
log field valuename log field value is equal to
GROUP_EMAIL
, then the
protoPayload.metadata.event.parameter.1.value
log field is mapped to the
target.group.email_addresses
UDM field.
Else, the
protoPayload.metadata.event.parameter.1.value
log field is mapped to the
target.group.product_object_id
UDM field.
protoPayload.requestMetadata.requestAttributes.host
target.hostname
The
log_message
field is extracted from
textPayload
log field using Grok pattern, if the
log_message
field value matches the regular expression pattern
disconnection
, then the
host
field is extracted from
log_message
log field using Grok pattern, and the
host
log field is mapped to the
target.hostname
UDM field.
httpRequest.remoteIp
target.ip
protoPayload.request.ip
target.ip
protoPayload.response.targetId
target.labels[target_id]
(deprecated)
protoPayload.response.targetId
additional.fields[target_id]
protoPayload.request.body.region
resource.labels.region
protoPayload.resourceLocation.currentLocations.0
target.location.country_or_region
If the
protoPayload.request.body.region
log field value is
not
empty, then the
protoPayload.request.body.region
log field is mapped to the
target.location.country_or_region
UDM field.
Else, if the
resource.labels.region
log field value is
not
empty, then the
resource.labels.region
log field is mapped to the
target.location.country_or_region
UDM field.
Else, if the
protoPayload.resourceLocation.currentLocations.0
log field value is
not
empty, then the
protoPayload.resourceLocation.currentLocations.0
log field is mapped to the
target.location.country_or_region
UDM field.
resource.labels.location
target.location.name
jsonPayload.connection.dest_port
target.port
The
log_message
field is extracted from
textPayload
log field using Grok pattern. If the
log_message
field value matches the regular expression pattern
disconnection
, then the
port
field is extracted from
log_message
log field using Grok pattern, and the
port
field is mapped to the
target.port
UDM field.
protoPayload.request.query
target.resource.attribute.labels[query]
protoPayload.request.spec.containers.0.command.0
target.process.command_line
resource.labels.project_id
target.resource_ancestors.name
protoPayload.response.targetProject
target.resource_ancestors.name
protoPayload.request.parent
target.resource_ancestors.name
protoPayload.authorizationInfo.resourceAttributes.name
target.resource_ancestors.name
protoPayload.response.instanceUid
target.resource_ancestors.product_object_id
protoPayload.authorizationInfo.0.resourceAttributes.type
target.resource_ancestors.resource_subtype
target.resource_ancestors.resource_type
If the
resource.labels.project_id
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
jsonPayload.resource.zone
target.resource.attribute.cloud.availability_zone
resource.labels.zone
target.resource.attribute.cloud.availability_zone
protoPayload.response.insertTime
target.resource.attribute.creation_time
protoPayload.requestMetadata.requestAttributes.auth.accessLevels
target.resource.attribute.labels[access_level]
labels.agent_version
target.resource.attribute.labels[agent_version]
protoPayload.request.date
target.resource.attribute.labels[audit_event_occurred]
protoPayload.request.auditId
target.resource.attribute.labels[audit_id]
protoPayload.authorizationInfo.granted
target.resource.attribute.labels[authorization_granted]
protoPayload.authorizationInfo.resourceAttributes.service
target.resource.attribute.labels[authorization_info_resource_service]
protoPayload.request.autoscalingPolicy.mode
target.resource.attribute.labels[autoscaling_policy_mode]
resource.labels.backend_service_id
target.resource.attribute.labels[backend_service_id]
resource.labels.backend_service_name
target.resource.attribute.labels[backend_service_name]
protoPayload.request.body.backendType
target.resource.attribute.labels[backend_type]
protoPayload.response.backupContext.kind
target.resource.attribute.labels[backup_context_kind]
protoPayload.response.backupContext.backupId
target.resource.attribute.labels[backup_id]
resource.labels.bucket_name
target.resource.attribute.labels[bucket_name]
protoPayload.response.clientCert.certInfo.instance
target.resource.attribute.labels[client_cert_instance]
protoPayload.response.clientCert.certInfo.kind
target.resource.attribute.labels[client_cert_kind]
protoPayload.response.clientCert.certInfo.selfLink
target.resource.attribute.labels[client_cert_self_link]
resource.labels.cluster_name
target.resource.attribute.labels[cluster_name]
protoPayload.request.body.commonName
target.resource.attribute.labels[common_name]
protoPayload.request.autoscalingPolicy.coolDownPeriodSec
target.resource.attribute.labels[cool_down_period]
protoPayload.request.body.databaseVersion
target.resource.attribute.labels[database_version]
protoPayload.request.database
target.resource.attribute.labels[database]
protoPayload.request.auditClass
target.resource.attribute.labels[audit_class]
protoPayload.request.databaseSessionId
target.resource.attribute.labels[database_session_id]
protoPayload.request.auditType
target.resource.attribute.labels[audit_type]
protoPayload.request.statementId
target.resource.attribute.labels[statement_id]
protoPayload.request.substatementId
target.resource.attribute.labels[sub_statement_id]
protoPayload.request.object
target.resource.attribute.labels[object]
protoPayload.request.objectType
target.resource.attribute.labels[object_type]
protoPayload.request.chunkCount
target.resource.attribute.labels[chunk_count]
protoPayload.request.chunkIndex
target.resource.attribute.labels[chunk_index]
protoPayload.request.statement
target.resource.attribute.labels[statement]
protoPayload.request.parameter
target.resource.attribute.labels[parameter]
protoPayload.request.priv_user
target.user.user_display_name
protoPayload.request.gcpIamAccount
target.resource.attribute.permissions.name
protoPayload.request.errCode
target.resource.attribute.labels[err_code]
protoPayload.request.host
target.hostname & target.asset.hostname
protoPayload.request.command
target.resource.attribute.labels[command]
protoPayload.request.denieds.0.IPProtocol
target.resource.attribute.labels[Denied Protocol]
protoPayload.request.destinationRanges
target.resource.attribute.labels[destination_ranges]
protoPayload.request.direction
target.resource.attribute.labels[direction]
protoPayload.request.spec.dnsPolicy
target.resource.attribute.labels[dns_policy]
resource.labels.email_id
target.resource.attribute.labels[email_id]
protoPayload.request.properties.confidentialInstanceConfig.enableConfidentialCompute
target.resource.attribute.labels[enable_confidential_compute]
labels.execution_id
target.resource.attribute.labels[execution_id]
protoPayload.request.body.exportContext.databases
target.resource.attribute.labels[export_context_databases]
protoPayload.request.body.exportContext.fileType
target.resource.attribute.labels[export_context_file_type]
protoPayload.request.body.exportContext.kind
target.resource.attribute.labels[export_context_kind]
protoPayload.request.body.exportContext.offload
target.resource.attribute.labels[export_context_offload]
resource.labels.forwarding_rule_name
target.resource.attribute.labels[forwarding_rule_name]
protoPayload.request.function.entryPoint
target.resource.attribute.labels[function_entry_point]
protoPayload.request.function.httpsTrigger.securityLevel
target.resource.attribute.labels[function_httptrigger_security_level]
protoPayload.request.function.runtime
target.resource.attribute.labels[function_runtime]
protoPayload.request.function.serviceAccountEmail
target.resource.attribute.labels[function_service_account_email]
protoPayload.request.function.sourceUploadUrl
target.resource.attribute.labels[function_source_upload_url]
protoPayload.request.function.timeout
target.resource.attribute.labels[function_time_out]
protoPayload.metadata.iapEnabled
target.resource.attribute.labels[iapEnabled]
protoPayload.request.spec.containers.0.imagePullPolicy
target.resource.attribute.labels[imagePullPolicy]
resource.labels.instance_group_manager_id
target.resource.attribute.labels[instance_group_manager_id]
resource.labels.instance_group_manager_name
target.resource.attribute.labels[instance_group_manager_name]
labels.instance_name
target.resource.attribute.labels[instance_name]
protoPayload.request.listManagedInstancesResults
target.resource.attribute.labels[managed_instances_result]
protoPayload.request.autoscalingPolicy.maxNumReplicas
target.resource.attribute.labels[max_replicas]
protoPayload.request.autoscalingPolicy.minNumReplicas
target.resource.attribute.labels[min_replicas]
protoPayload.request.msgType
target.resource.attribute.labels[msg_type]
protoPayload.request.spec.containers.0.name
target.resource.attribute.labels[name]
protoPayload.metadata.oauth_client_id
target.resource.attribute.labels[oauth_client_id]
protoPayload.response.operation.insertTime
target.resource.attribute.labels[operation_insert_time]
protoPayload.response.operation.instanceUid
target.resource.attribute.labels[operation_instance_uid]
protoPayload.response.operation.kind
target.resource.attribute.labels[operation_kind]
protoPayload.response.operation.name
target.resource.attribute.labels[operation_name]
protoPayload.response.operation.operationType
target.resource.attribute.labels[operation_operation_type]
protoPayload.response.operation.selfLink
target.resource.attribute.labels[operation_self_link]
protoPayload.response.operation.status
target.resource.attribute.labels[operation_status]
protoPayload.response.operation.targetId
target.resource.attribute.labels[operation_target_id]
protoPayload.response.operation.targetLink
target.resource.attribute.labels[operation_target_link]
protoPayload.response.operation.targetProject
target.resource.attribute.labels[operation_target_project]
protoPayload.response.operation.user
target.resource.attribute.labels[operation_user]
protoPayload.request.autoscalingPolicy.cpuUtilization.predictiveMethod
target.resource.attribute.labels[predictive_method]
protoPayload.request.labels.key
target.resource.attribute.labels[protoPayload.request.labels.key]
protoPayload.request.labels.value
target.resource.attribute.labels[protoPayload.request.labels.value]
protoPayload.request.queryId
target.resource.attribute.labels[query_id]
protoPayload.request.instance
target.resource.attribute.labels[req_body_instance]
protoPayload.request.maxResults
target.resource.attribute.labels[req_body_max_results]
protoPayload.request.body.name
target.resource.attribute.labels[req_body_name]
protoPayload.request.operation
target.resource.attribute.labels[req_body_operation]
protoPayload.request.body.project
target.resource.attribute.labels[req_body_project]
protoPayload.request.disabled
target.resource.attribute.labels[req_disabled]
protoPayload.request.logConfig.enable
target.resource.attribute.labels[req_logconfig_enable]
protoPayload.request.metadata.name
target.resource.attribute.labels[req_metadata_name]
protoPayload.request.name
target.resource.attribute.labels[req_name]
protoPayload.request.network
target.resource.attribute.labels[req_network]
protoPayload.request.apiVersion
target.resource.attribute.labels[req_api_version]
protoPayload.request.priority
target.resource.attribute.labels[Request Priority]
protoPayload.request.constraint
target.resource.attribute.labels[request_constraint]
protoPayload.request.policy.constraint
target.resource.attribute.labels[request_policy_constraint]
protoPayload.request.dataAccessed
target.resource.attribute.labels[request_data_accessed]
protoPayload.request.function.labels.deployment-tool
target.resource.attribute.labels[request_deployment_tool]
protoPayload.request.properties.description
target.resource.attribute.labels[request_description]
protoPayload.request.endTime
target.resource.attribute.labels[request_end_time]
protoPayload.request.policy.booleanPolicy.enforced
target.resource.attribute.labels[request_enforce_policy]
protoPayload.request.function.name
target.resource.attribute.labels[request_function_name]
protoPayload.request.kind
target.resource.attribute.labels[request_kind]
protoPayload.request.project
target.resource.attribute.labels[request_project]
protoPayload.request.location
target.resource.attribute.labels[request_location]
protoPayload.request.pageToken
target.resource.attribute.labels[request_page_token]
protoPayload.request.projectId
target.resource.attribute.labels[request_projectid]
protoPayload.request.startTime
target.resource.attribute.labels[request_start_time]
protoPayload.request.@type
target.resource.attribute.labels[request_type]
protoPayload.response.name
target.resource.attribute.labels[res_name]
protoPayload.response.status.conditions.message
target.resource.attribute.labels[res_status_conditions_message]
protoPayload.response.zone
target.resource.attribute.labels[res_zone]
resource.labels.service
target.resource.attribute.labels[resource_service]
protoPayload.response.booleanPolicy.enforced
target.resource.attribute.labels[response_enforce_policy]
resource.labels.scan_config
target.resource.attribute.labels[scan_config]
protoPayload.response.serverCaCert.instance
target.resource.attribute.labels[server_ca_cert_instance]
protoPayload.response.serverCaCert.kind
target.resource.attribute.labels[server_ca_cert_kind]
protoPayload.response.serverCaCert.selfLink
target.resource.attribute.labels[server_ca_cert_self_link]
protoPayload.request.properties.serviceAccounts.scopes
security_result.detection_fields[service_account_scope]
protoPayload.request.serviceAccounts.scopes
security_result.detection_fields[service_account_scope]
protoPayload.request.body.settings.activationPolicy
target.resource.attribute.labels[settings_activation_policy]
protoPayload.request.body.settings.activeDirectoryConfig.domain
target.resource.attribute.labels[settings_active_directory_config_domain]
protoPayload.request.body.settings.activeDirectoryConfig.kind
target.resource.attribute.labels[settings_active_directory_config_kind]
protoPayload.request.body.settings.authorizedGaeApplications
target.resource.attribute.labels[settings_authorized_gae_applications]
protoPayload.request.body.settings.availabilityType
target.resource.attribute.labels[settings_availability_type]
protoPayload.request.body.settings.backupConfiguration.backupRetentionSettings.retainedBackups
target.resource.attribute.labels[settings_backup_conf_backup_retention_settings_retained_backups]
protoPayload.request.body.settings.backupConfiguration.backupRetentionSettings.retentionUnit
target.resource.attribute.labels[settings_backup_conf_backup_retention_settings_retention_unit]
protoPayload.request.body.settings.backupConfiguration.binaryLogEnabled
target.resource.attribute.labels[settings_backup_conf_binary_log_enabled]
protoPayload.request.body.settings.backupConfiguration.enabled
target.resource.attribute.labels[settings_backup_conf_enabled]
protoPayload.request.body.settings.backupConfiguration.kind
target.resource.attribute.labels[settings_backup_conf_kind]
protoPayload.request.body.settings.backupConfiguration.location
target.resource.attribute.labels[settings_backup_conf_location]
protoPayload.request.body.settings.backupConfiguration.pointInTimeRecoveryEnabled
target.resource.attribute.labels[settings_backup_conf_point_in_time_recovery_enabled]
protoPayload.request.body.settings.backupConfiguration.replicationLogArchivingEnabled
target.resource.attribute.labels[settings_backup_conf_replication_log_archiving_enabled]
protoPayload.request.body.settings.backupConfiguration.startTime
target.resource.attribute.labels[settings_backup_conf_start_time]
protoPayload.request.body.settings.backupConfiguration.transactionLogRetentionDays
target.resource.attribute.labels[settings_backup_conf_transaction_log_retention_days]
protoPayload.request.body.settings.collation
target.resource.attribute.labels[settings_collation]
protoPayload.request.body.settings.connectorEnforcement
target.resource.attribute.labels[settings_connector_enforcement]
protoPayload.request.body.settings.crashSafeReplicationEnabled
target.resource.attribute.labels[settings_crash_safe_replication_enabled]
protoPayload.request.body.settings.dataDiskSizeGb
target.resource.attribute.labels[settings_data_disk_size_gb]
protoPayload.request.body.settings.dataDiskType
target.resource.attribute.labels[settings_data_disk_type]
protoPayload.request.body.settings.databaseFlags.name
target.resource.attribute.labels[settings_database_flags_name]
protoPayload.request.body.settings.databaseFlags.value
target.resource.attribute.labels[settings_database_flags_value]
protoPayload.request.body.settings.databaseReplicationEnabled
target.resource.attribute.labels[settings_database_replication_enabled]
protoPayload.request.body.settings.deletionProtectionEnabled
target.resource.attribute.labels[settings_deletion_protection_enabled]
protoPayload.request.body.settings.denyMaintenancePeriods.endDate
target.resource.attribute.labels[settings_deny_maintenance_periods_end_date]
protoPayload.request.body.settings.denyMaintenancePeriods.startDate
target.resource.attribute.labels[settings_deny_maintenance_periods_start_date]
protoPayload.request.body.settings.denyMaintenancePeriods.time
target.resource.attribute.labels[settings_deny_maintenance_periods_time]
protoPayload.request.body.settings.insightsConfig.queryInsightsEnabled
target.resource.attribute.labels[settings_insights_config_query_insights_enabled]
protoPayload.request.body.settings.insightsConfig.queryPlansPerMinute
target.resource.attribute.labels[settings_insights_config_query_plans_per_minute]
protoPayload.request.body.settings.insightsConfig.queryStringLength
target.resource.attribute.labels[settings_insights_config_query_string_length]
protoPayload.request.body.settings.insightsConfig.recordApplicationTags
target.resource.attribute.labels[settings_insights_config_record_application_tags]
protoPayload.request.body.settings.insightsConfig.recordClientAddress
target.resource.attribute.labels[settings_insights_config_record_client_address]
protoPayload.request.body.settings.ipConfiguration.allocatedIpRange
target.resource.attribute.labels[settings_ip_configuration_allocated_ip_range]
protoPayload.request.body.settings.ipConfiguration.authorizedNetworks.expirationTime
target.resource.attribute.labels[settings_ip_configuration_authorized_networks_expiration_time]
protoPayload.request.body.settings.ipConfiguration.authorizedNetworks.kind
target.resource.attribute.labels[settings_ip_configuration_authorized_networks_kind]
protoPayload.request.body.settings.ipConfiguration.authorizedNetworks.name
target.resource.attribute.labels[settings_ip_configuration_authorized_networks_name]
protoPayload.request.body.settings.ipConfiguration.authorizedNetworks.value
target.resource.attribute.labels[settings_ip_configuration_authorized_networks_value]
protoPayload.request.body.settings.ipConfiguration.ipv4Enabled
target.resource.attribute.labels[settings_ip_configuration_ipv4_enabled]
protoPayload.request.body.settings.ipConfiguration.privateNetwork
target.resource.attribute.labels[settings_ip_configuration_private_network]
protoPayload.request.body.settings.ipConfiguration.requireSsl
target.resource.attribute.labels[settings_ip_configuration_require_ssl]
protoPayload.request.body.settings.kind
target.resource.attribute.labels[settings_kind]
protoPayload.request.body.settings.locationPreference.followGaeApplication
target.resource.attribute.labels[settings_location_preference_follow_gae_application]
protoPayload.request.body.settings.locationPreference.kind
target.resource.attribute.labels[settings_location_preference_kind]
protoPayload.request.body.settings.locationPreference.secondaryZone
target.resource.attribute.labels[settings_location_preference_secondary_zone]
protoPayload.request.body.settings.locationPreference.zone
target.resource.attribute.labels[settings_location_preference_zone]
protoPayload.request.body.settings.maintenanceWindow.day
target.resource.attribute.labels[settings_maintenance_window_day]
protoPayload.request.body.settings.maintenanceWindow.hour
target.resource.attribute.labels[settings_maintenance_window_hour]
protoPayload.request.body.settings.maintenanceWindow.kind
target.resource.attribute.labels[settings_maintenance_window_kind]
protoPayload.request.body.settings.maintenanceWindow.updateTrack
target.resource.attribute.labels[settings_maintenance_window_update_track]
protoPayload.request.body.settings.passwordValidationPolicy.complexity
target.resource.attribute.labels[settings_password_validation_policy_complexity]
protoPayload.request.body.settings.passwordValidationPolicy.disallowUsernameSubstring
target.resource.attribute.labels[settings_password_validation_policy_disallow_username_substring]
protoPayload.request.body.settings.passwordValidationPolicy.enablePasswordPolicy
target.resource.attribute.labels[settings_password_validation_policy_enable_password_policy]
protoPayload.request.body.settings.passwordValidationPolicy.minLength
target.resource.attribute.labels[settings_password_validation_policy_min_length]
protoPayload.request.body.settings.passwordValidationPolicy.passwordChangeInterval
target.resource.attribute.labels[settings_password_validation_policy_password_change_interval]
protoPayload.request.body.settings.passwordValidationPolicy.reuseInterval
target.resource.attribute.labels[settings_password_validation_policy_reuse_interval]
protoPayload.request.body.settings.pricingPlan
target.resource.attribute.labels[settings_pricing_plan]
protoPayload.request.body.settings.replicationType
target.resource.attribute.labels[settings_replication_type]
protoPayload.request.body.settings.sqlServerAuditConfig.bucket
target.resource.attribute.labels[settings_sql_server_audit_config_bucket]
protoPayload.request.body.settings.sqlServerAuditConfig.kind
target.resource.attribute.labels[settings_sql_server_audit_config_kind]
protoPayload.request.body.settings.sqlServerAuditConfig.retentionInterval
target.resource.attribute.labels[settings_sql_server_audit_config_retention_interval]
protoPayload.request.body.settings.sqlServerAuditConfig.uploadInterval
target.resource.attribute.labels[settings_sql_server_audit_config_upload_interval]
protoPayload.request.body.settings.settingsVersion
target.resource.attribute.labels[settings_version]
protoPayload.request.sourceRanges
target.resource.attribute.labels[source_ranges]
protoPayload.request.cmd
target.resource.attribute.labels[sql_operation_type ]
protoPayload.request.body.settings.storageAutoResizeLimit
target.resource.attribute.labels[storage_auto_resize_limit]
protoPayload.request.body.settings.storageAutoResize
target.resource.attribute.labels[storage_auto_resize]
resource.labels.target_proxy_name
target.resource.attribute.labels[target_proxy_name]
protoPayload.request.spec.containers.0.terminationMessagePath
target.resource.attribute.labels[terminationMessagePath]
protoPayload.request.spec.containers.0.terminationMessagePolicy
target.resource.attribute.labels[terminationMessagePolicy]
protoPayload.request.threadId
target.resource.attribute.labels[thread_id]
protoPayload.request.body.settings.tier
target.resource.attribute.labels[tier]
protoPayload.request.body.settings.timeZone
target.resource.attribute.labels[time_zone]
protoPayload.request.body.truncateLogContext.kind
target.resource.attribute.labels[truncate_log_context_kind]
protoPayload.request.body.truncateLogContext.logType
target.resource.attribute.labels[truncate_log_context_log_type]
protoPayload.metadata.unsatisfied_access_levels
target.resource.attribute.labels[unsatisfied_access_levels]
resource.labels.url_map_name
target.resource.attribute.labels[url_map_name]
protoPayload.request.body.settings.userLabels
target.resource.attribute.labels[user_labels]
protoPayload.request.autoscalingPolicy.cpuUtilization.utilizationTarget
target.resource.attribute.labels[utilization_target]
protoPayload.authorizationInfo.permission
principal.user.attribute.permissions.name
protoPayload.serviceData.policyDelta.auditConfigDeltas.logType
target.resource.attribute.permissions.type
The
target.resource.attribute.permissions.name
UDM field is set to
logType
.
resource.labels.database_id
jsonPayload.resource.name
jsonPayload.accessApprovals.0
resource.labels.function_name
jsonPayload.name
protoPayload.request.body.cloneContext.destinationInstanceName
protoPayload.requestMetadata.callerNetwork
target.resource.name
Extracted
database_name
from
textPayload
log field using Grok pattern, and the
database_name
field is mapped to the
target.resource.name
UDM field.
If the
protoPayload.methodName
log field value is equal to
cloudsql.instances.clone
, then the
protoPayload.request.body.cloneContext.destinationInstanceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
logName
log field value matches the regular expression pattern
postgres.log
, then the
database_name
log field is mapped to the
target.resource.name
UDM field.
Else, if the
logName
log field value matches the regular expression pattern
mysql-general
, then the
resource.labels.database_id
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
cloud_function
and the
target.resource.name
log field value is empty, then the
resource.labels.function_name
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
security_scanner_scan_config
, then the
jsonPayload.name
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource_type
log field value matches the regular expression pattern
(project or organization)
and the
jsonPayload.@type
log field value is equal to
type.googleapis.com/google.cloud.audit.TransparencyLog
, then the
jsonPayload.accessApprovals.0
log field is mapped to the
target.resource.name
UDM field.
Else, the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
If the
protoPayload.resourceName
log field value matches the regular expression pattern
snapshots
, then the
protoPayload.requestMetadata.callerNetwork
log field is mapped to the
target.resource.name
UDM field.
If the
resource.type
log field value matches the regular expression pattern
gce_instance
, then the
//compute.googleapis.com/protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
resource.labels.instance_id
resource.labels.unique_id
protoPayload.request.resourceId
target.resource.product_object_id
If the
resource.labels.unique_id
log field value is
not
empty, then the
resource.labels.unique_id
log field is mapped to the
target.resource.product_object_id
UDM field.
Else, if the
resource.labels.unique_id
log field value is empty, then the
resource.labels.instance_id
log field is mapped to the
target.resource.product_object_id
UDM field.
If the
request.@type
log field value matches the regular expression pattern
RetrieveSqlEventGroupsRequest
, then the
protoPayload.request.resourceId
log field is mapped to the
target.resource.product_object_id
UDM field.
If the
resouce.type
log field value matches the regular expression pattern
cloud_scheduler_job
, then the
resource.labels.job_id
log field is mapped to the
target.resource.product_object_id
UDM field.
If the
resouce.type
log field value matches the regular expression pattern
gce_instance
, then the
resource.labels.instance_id
log field is mapped to the
target.resource.product_object_id
UDM field.
protoPayload.request.body.instanceUid
target.resource.product_object_id
protoPayload.request.id
target.resource.product_object_id
protoPayload.request.body.instanceType
resource.type
target.resource.resource_subtype
If the
resource.type
log field value is empty, then the
protoPayload.request.body.instanceType
log field is mapped to the
target.resource.resource_subtype
UDM field.
Else, the
resource.type
log field is mapped to the
target.resource.resource_subtype
UDM field.
jsonPayload.resource.type
target.resource.resource_subtype
target.resource.resource_type
If the
resource.type
log field value matches the regular expression pattern
gce_(firewall or forwarding_rule)
, then the
target.resource.resource_type
UDM field is set to
FIREWALL_RULE
.
Else, if the
resource.type
log field value matches the regular expression pattern
gce_(subnetwork or network)
, then the
target.resource.resource_type
UDM field is set to
VPC_NETWORK
.
Else, if the
resource.type
log field value matches the regular expression pattern
dataproc
, then the
target.resource.resource_type
UDM field is set to
CLUSTER
.
Else, if the
resource.type
log field value matches the regular expression pattern
k8s or gke_
, then the
target.resource.resource_type
UDM field is set to
CLUSTER
.
Else, if the
resource.type
log field value is equal to
gce_backend_service
, then the
target.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
Else, if the
resource.type
log field value matches the regular expression pattern
(gce_ or dns_query)
, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else, if the
resource.type
log field value matches the regular expression pattern
gcs_bucket
, then the
target.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
Else, if the
resource.type
log field value matches the regular expression pattern
bigquery
, then the
target.resource.resource_type
UDM field is set to
DATABASE
.
Else, if the
resource.type
log field value matches the regular expression pattern
cloudsql
, then the
target.resource.resource_type
UDM field is set to
DATABASE
.
Else, if the
resource.type
log field value matches the regular expression pattern
service_account
, then the
target.resource.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
Else, if the
resource.type
log field value matches the regular expression pattern
project
, then the
target.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
resource.type
log field value matches the regular expression pattern
organization
, then the
target.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
resource.type
log field value matches the regular expression pattern
cloud_function
, then the
target.resource.resource_type
UDM field is set to
FUNCTION
.
protoPayload.response.targetLink
target.url
protoPayload.request.httpRequest.url
target.url
protoPayload.request.body.exportContext.uri
target.url
jsonPayload.url
target.url
protoPayload.request.subjects.kind
target.user.attribute.labels[subject_kind]
protoPayload.request.subjects.name
target.user.attribute.labels[subject_name]
protoPayload.request.role.included_permissions
target.user.attribute.permissions.name
protoPayload.request.roleRef.kind
target.user.attribute.roles.description
protoPayload.request.policy.bindings.role
target.user.attribute.roles.name
protoPayload.request.roleRef.name
target.user.attribute.roles.name
target.user.attribute.roles.type
If the
protoPayload.request.roleRef.name
log field value matches the regular expression pattern
(?i)admin
, then the
target.user.attribute.roles.type
UDM field is set to
ADMINISTRATOR
.
protoPayload.request.properties.serviceAccounts.email
target.user.email_addresses
protoPayload.request.serviceAccounts.email
target.user.email_addresses
protoPayload.serviceData.policyDelta.bindingDeltas.member
target.user.email_addresses
protoPayload.serviceData.policyDelta.bindingDeltas.member
target.user.userid
protoPayload.response.user
target.user.userid
protoPayload.request.user
target.user.userid
protoPayload.metadata.event.parameter.1.value
protoPayload.metadata.event.parameter.0.value
target.user.userid
If the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(addgroupmember or updategroupmember or suspenduser or assignrole or unassignrole)
, then if the
protoPayload.metadata.event.eventName
log field value matches the regular expression pattern
ASSIGN_ROLE
, then the
protoPayload.metadata.event.parameter.1.value
log field is mapped to the
target.user.userid
UDM field.
Else, the
protoPayload.metadata.event.parameter.0.value
log field is mapped to the
target.user.userid
UDM field.
protoPayload.metadata.membershipDelta.member
target.user.userid
protoPayload.request.spec.enableServiceLinks
target.resource.attribute.labels[enableServiceLinks]
protoPayload.request.spec.terminationGracePeriodSeconds
target.resource.attribute.labels[protoPayload_request_spec_terminationGracePeriodSeconds]
protoPayload.request.spec.restartPolicy
target.resource.attribute.labels[restartPolicy]
resource.labels.database_id
target.resource.attribute.labels[database_id]
If the
logName
log field value does not matches the regular expression pattern
mysql-general
, then the
resource.labels.database_id
log field is mapped to the
target.resource.attribute.labels
UDM field.
protoPayload.request.spec.schedulerName
target.resource.attribute.labels[schedulerName]
protoPayload.request.body.instanceType
target.resource.attribute.labels[instance_type]
protoPayload.response.status
jsonPayload.operation
jsonPayload.MESSAGE
The following fields have been extracted from the
jsonPayload.MESSAGE
log field using a KV filter and then associated with their respective UDM fields.
The
auid
field is mapped to the
network.session_id
UDM field.
The
pid
field is mapped to the
principal.process.pid
UDM field.
The
uid
field is mapped to the
principal.user.userid
UDM field.
The
ppid
field is mapped to the
principal.process.parent_process.pid
UDM field.
The
exe
field is mapped to the
principal.process.command_line
UDM field.
The
exit
field is mapped to the
security_result.about.labels
UDM field. (deprecated)
The
exit
field is mapped to the
additional.fields
UDM field.
The
ses
field is mapped to the
network.session_id
UDM field.
metadata.event_type
If the
protoPayload.methodName
log field value matches the regular expression pattern
loginservice.(login or govattackwarning or accountdisabled or accountdisabledspammingthroughrelay or suspiciouslogin or suspiciousloginlesssecureapp or suspiciousprogrammaticlogin)
or the
protoPayload.methodName
log field value is equal to
AuthorizeUser
, then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
If the
resource.type
log field value contain one of the following values
cloudsql_database
alloydb.googleapis.com/Instance
and
textPayload
log field value matches the regular expression pattern
connection authorized|Logon
, then the
metadata.event_type
UDM field is set to
USER_LOGIN
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
loginservice.logout
, then the
metadata.event_type
UDM field is set to
USER_LOGOUT
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(changepassword)
, then the
metadata.event_type
UDM field is set to
USER_CHANGE_PASSWORD
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(create or add)
or the
protoPayload.methodName
log field value matches the regular expression pattern
accesscontextmanager.(create)
, the
metadata.event_type
UDM field is set to
USER_RESOURCE_CREATION
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
adminservice.(createaccess or enforce or systemdefinedruleupdated or changetwostepverificationfrequency or suspenduser or assignrole or unassignrole)
or the
protoPayload.methodName
log field value matches the regular expression pattern
(setiampolicy or checkinvitationrequired or setiampermissions or setorgpolicy)
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_PERMISSIONS
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
clustermanager.*.(setnodepoolmanagement or updatecomponentconfig)
or the
protoPayload.methodName
log field value matches the regular expression pattern
(instance.*).(set or reset or resize)
or the
protoPayload.methodName
log field value matches the regular expression pattern
attachcloudlink
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
iam.admin.*(create or delete)
or the
protoPayload.methodName
log field value matches the regular expression pattern
jobservice.(cancel)
, then the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
(adminservice or membershipsservice or accesscontextmanager or servicemanager or serviceusage or services or projects or clustermanager.*).(update or change or activate or deactivate or enable or disable or replace or set)
or the
protoPayload.methodName
log field value matches the regular expression pattern
update(brand or client)
or the
protoPayload.methodName
log field value matches the regular expression pattern
assignprojecttobillingaccount
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
.*(delete or remove).*
or the
protoPayload.methodName
log field value matches the regular expression pattern
.*(compute.disks.delete.*)
, then the
metadata.event_type
UDM field is set to
RESOURCE_DELETION
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
.*(submit or update or patch or ingest).*
or the
protoPayload.methodName
log field value matches the regular expression pattern
jobservice.(insert or jobcompleted)
or the
protoPayload.methodName
log field value matches the regular expression pattern
imageannotator.(batch).*
or the
protoPayload.methodName
log field value matches the regular expression pattern
.*(scheduledsnapshots or compute.disks.insert.* or compute.disks.add.* or compute.disks.setlabels.*)
, then the
metadata.event_type
UDM field is set to
RESOURCE_WRITTEN
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
.*(insert or create or recreate or add).*
or the
protoPayload.methodName
log field value matches the regular expression pattern
compute..*.(migrate)
, then the
metadata.event_type
UDM field is set to
RESOURCE_CREATION
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
.*(get or list or watch).*
or the
protoPayload.methodName
log field value matches the regular expression pattern
cloudsql..*.(connect)
, then
If the
principal.user.userid
log field value is
not
empty or the
principal.user.email_addresses
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
RESOURCE_READ
.
Else, if the
principal.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
(agents).(import)
, then the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
.
Else, if the
protoPayload.methodName
log field value matches the regular expression pattern
status.update
and the
principal.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, if the
principal.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, if the
resource_type
log field value is equal to
cloudsql_database
and if the
textPayload
log field value matches the regular expression pattern
.*(INSERT).*
then, the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
Else, if the
resource_type
log field value is equal to
cloudsql_database
and if the
textPayload
log field value matches the regular expression pattern
.*(SELECT).*
then, the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
labels._HOSTNAME
principal.hostname
If the
logName
log field value matches the regular expression pattern
sqlserver\.err
, the
labels._HOSTNAME
field is mapped to the
principal.hostname
UDM field.
labels._HOSTNAME
principal.asset.hostname
If the
logName
log field value matches the regular expression pattern
sqlserver\.err
, the
labels._HOSTNAME
field is mapped to the
principal.asset.hostname
UDM field.
textPayload
metadata.description
If the
logName
log field value matches the regular expression pattern
sqlserver\.err
, the
textPayload
field is mapped to the
metadata.description
UDM field.
target.user.userid
If the
logName
log field value matches the regular expression pattern
sqlserver\.err
, the
user_id
field is extracted from
textPayload
log field using Grok pattern, and the
user_id
field is mapped to the
target.user.userid
UDM field.
What's next
Data ingestion to Google Security Operations
