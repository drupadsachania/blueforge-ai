# Collect Google Kubernetes Engine logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/kubernetes-node/  
**Scraped:** 2026-03-05T09:17:23.994977Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Kubernetes Engine logs
Supported in:
Google secops
SIEM
This document describes how you can collect Google Kubernetes Engine logs by setting up
a Google SecOps feed and how log fields map to Google SecOps Unified
Data Model (UDM) fields. This document also lists the supported log types and event
types for Google Kubernetes Engine.
For more information, see
Data ingestion to Google SecOps
.
A typical deployment consists of Google Kubernetes Engine and the Google SecOps
feed configured to send logs to Google SecOps. Each customer deployment
might differ and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Google Kubernetes Engine
. The Google Kubernetes Engine platform from which you collect logs.
Google SecOps
. Google SecOps retains and analyzes the logs from
Google Kubernetes Engine.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the Google Kubernetes Engine parser
with the following ingestion label:
KUBERNETES_NODE
Before you begin
Ensure that you have a Google Administrator account.
Verify whether you have the required permissions to perform the following tasks:
Create or access a Google Cloud project.
Enable the Google Kubernetes Engine cluster. For more information, see
Deploy an app to a GKE cluster
Ensure that all systems in the deployment architecture are configured
in the UTC time zone.
Verify the log types that the Google SecOps parser supports. For information
about supported Google Kubernetes Engine resource types, see
Supported Google Kubernetes Engine resource types
.
Configure Google Cloud for ingestion
To ingest KUBERNETES_NODE logs to Google SecOps, follow the steps on the
Ingest Google Cloud data to Google SecOps
page.
If you encounter issues when you ingest KUBERNETES_NODE logs,
contact Google Security Operations support
.
If you encounter issues when you create feeds, contact
Google Security Operations support
.
Supported Google Kubernetes Engine resource types
The following table lists the resources types that the Google Kubernetes Engine parser supports:
Resource type
Display name
gke_cluster
GKE Cluster Operations
k8s_cluster
Kubernetes Cluster
gke_nodepool
GKE Node Pool
K8s_container
GKE Container logs
k8s_node
GKE Node Pool logs
k8s_pod
GKE Pod logs
k8s_service
GKE service logs
k8s_control_plane_component
Kubernetes Control Plane Component
audited_resource
Kubernetes Audited Resource
generic_node
Generic Node Resource
Supported Google Kubernetes Engine log formats
The Google Kubernetes Engine parser supports logs in JSON format.
Supported Google Kubernetes Engine sample logs
JSON:
{
  "protoPayload": {
    "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
    "authenticationInfo": {
      "principalEmail": "user@dummy.com"
    },
    "requestMetadata": {
      "callerIp": "198.51.100.1",
      "callerSuppliedUserAgent": "google-cloud-sdk gcloud/415.0.0 command/gcloud.beta.container.clusters.create invocation-id/077f3f1330ae433a8c7d13161bbcc643 environment/None environment-version/None interactive/True from-script/False python/3.9.12 term/ (Windows NT 10.0.22621),gzip(gfe)",
      "requestAttributes": {
        "time": "2023-01-25T06:43:46.203881095Z",
        "auth": {}
      },
      "destinationAttributes": {}
    },
    "serviceName": "container.googleapis.com",
    "methodName": "google.container.v1beta1.ClusterManager.CreateCluster",
    "authorizationInfo": [
      {
        "permission": "container.clusters.create",
        "granted": true,
        "resourceAttributes": {}
      }
    ],
    "resourceName": "projects/sccfindings29396/zones/us-east1-d/clusters/gke",
    "request": {
      "cluster": {
        "subnetwork": "projects/sccfindings29396/regions/us-east1/subnetworks/default",
        "name": "gke",
        "networkConfig": {},
        "defaultMaxPodsConstraint": {},
        "monitoringConfig": {
          "componentConfig": {
            "enableComponents": [
              "SYSTEM_COMPONENTS"
            ]
          }
        },
        "shieldedNodes": {},
        "loggingConfig": {
          "componentConfig": {
            "enableComponents": [
              "SYSTEM_COMPONENTS",
              "WORKLOADS"
            ]
          }
        },
        "initialClusterVersion": "1.24.8-gke.2000",
        "locations": [
          "us-east1-d"
        ],
        "nodePools": [
          {
            "maxPodsConstraint": {},
            "management": {
              "autoRepair": true,
              "autoUpgrade": true
            },
            "config": {
              "diskType": "pd-standard",
              "machineType": "e2-medium",
              "oauthScopes": [
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring",
                "https://www.googleapis.com/auth/service.management.readonly",
                "https://www.googleapis.com/auth/servicecontrol",
                "https://www.googleapis.com/auth/trace.append"
              ],
              "metadata": {
                "disable-legacy-endpoints": "true"
              },
              "imageType": "COS_CONTAINERD",
              "diskSizeGb": 30
            },
            "upgradeSettings": {
              "maxSurge": 1
            },
            "name": "default-pool",
            "initialNodeCount": 1
          }
        ],
        "network": "projects/sccfindings29396/global/networks/default",
        "releaseChannel": {
          "channel": "REGULAR"
        },
        "ipAllocationPolicy": {
          "useIpAliases": true
        },
        "addonsConfig": {
          "gcePersistentDiskCsiDriverConfig": {
            "enabled": true
          },
          "httpLoadBalancing": {},
          "networkPolicyConfig": {
            "disabled": true
          },
          "horizontalPodAutoscaling": {}
        },
        "masterAuthorizedNetworksConfig": {}
      },
      "@type": "type.googleapis.com/google.container.v1alpha1.CreateClusterRequest",
      "parent": "projects/sccfindings29396/locations/us-east1-d"
    },
    "response": {
      "selfLink": "https://container.googleapis.com/v1alpha1/projects/165675416793/zones/us-east1-d/operations/operation-1674629028274-a0ec9b53",
      "status": "RUNNING",
      "operationType": "CREATE_CLUSTER",
      "targetLink": "https://container.googleapis.com/v1alpha1/projects/165675416793/zones/us-east1-d/clusters/gke",
      "@type": "type.googleapis.com/google.container.v1alpha1.Operation",
      "startTime": "2023-01-25T06:43:48.274343825Z",
      "name": "operation-1674629028274-a0ec9b53"
    },
    "resourceLocation": {
      "currentLocations": [
        "us-east1-d"
      ]
    },
    "policyViolationInfo": {
      "orgPolicyViolationInfo": {}
    }
  },
  "insertId": "6dqtvadkv96",
  "resource": {
    "type": "gke_cluster",
    "labels": {
      "project_id": "sccfindings29396",
      "cluster_name": "dummy_customer_name",
      "location": "us-east1-d"
    }
  },
  "timestamp": "2023-01-25T06:43:48.355321416Z",
  "severity": "NOTICE",
  "logName": "projects/sccfindings29396/logs/cloudaudit.googleapis.com%2Factivity",
  "operation": {
    "id": "operation-1674629028274-a0ec9b53",
    "producer": "container.googleapis.com",
    "first": true
  },
  "receiveTimestamp": "2023-01-25T06:43:48.837791874Z"
}
Field mapping reference
The following sections explain how the Google Security Operations parser maps Google Kubernetes Engine
log fields to Google Security Operations Unified Data Model (UDM) fields.
Field mapping reference: KUBERNETES_NODE event identifier to UDM event type
The following table lists the
KUBERNETES_NODE
event identifiers and their corresponding
UDM event types. The mapping to an UDM event type is based on the
protopayload.methodname
log field, which is considered as the event identifier.
Event identifier
Event type
io.k8s.migration.v1alpha1.storagestates.status.update
USER_RESOURCE_UPDATE_CONTENT
io.k8s.get
USER_RESOURCE_ACCESS
google.container.v1beta1.ClusterManager.CreateCluster
RESOURCE_CREATION
io.k8s.core.v1.configmaps.patch
USER_RESOURCE_UPDATE_CONTENT
io.k8s.node.v1.runtimeclasses.watch
RESOURCE_READ
io.k8s.core.v1.endpoints.update
USER_RESOURCE_UPDATE_CONTENT
io.k8s.coordination.v1.leases.update
RESOURCE_WRITTEN
google.container.v1beta1.ClusterManager.UpdateCluster
USER_RESOURCE_UPDATE_CONTENT
io.k8s.core.v1.configmaps.update
USER_RESOURCE_UPDATE_CONTENT
google.container.v1.ClusterManager.CreateNodePool
RESOURCE_CREATION
google.container.v1.ClusterManager.CreateCluster
USER_RESOURCE_CREATION
google.container.v1.ClusterManager.DeleteCluster
RESOURCE_DELETION
loginservice.login
USER_LOGIN
loginservice.govattackwarning
USER_LOGIN
loginservice.accountdisabled
USER_LOGIN
loginservice.accountdisabledspammingthroughrelay
USER_LOGIN
loginservice.suspiciouslogin
USER_LOGIN
loginservice.suspiciousloginlesssecureapp
USER_LOGIN
loginservice.suspiciousprogrammaticlogin
USER_LOGIN
AuthorizeUser
USER_LOGIN
loginservice.logout
USER_LOGOUT
adminservice.changepassword
USER_CHANGE_PASSWORD
adminservice.create
USER_RESOURCE_CREATION
adminservice.add
USER_RESOURCE_CREATION
accesscontextmanager.create
USER_RESOURCE_CREATION
adminservice.createaccess
USER_RESOURCE_UPDATE_PERMISSIONS
adminservice.enforce
USER_RESOURCE_UPDATE_PERMISSIONS
adminservice.systemdefinedruleupdated
USER_RESOURCE_UPDATE_PERMISSIONS
adminservice.changetwostepverificationfrequency
USER_RESOURCE_UPDATE_PERMISSIONS
adminservice.suspenduser
USER_RESOURCE_UPDATE_PERMISSIONS
adminservice.assignrole
USER_RESOURCE_UPDATE_PERMISSIONS
adminservice.unassignrole
USER_RESOURCE_UPDATE_PERMISSIONS
setiampolicy
USER_RESOURCE_UPDATE_PERMISSIONS
checkinvitationrequired
USER_RESOURCE_UPDATE_PERMISSIONS
setiampermissions
USER_RESOURCE_UPDATE_PERMISSIONS
setorgpolicy
USER_RESOURCE_UPDATE_PERMISSIONS
storage.objects.delete
USER_RESOURCE_DELETION
storage.objects.update
USER_RESOURCE_UPDATE_CONTENT
attachcloudlink
USER_RESOURCE_UPDATE_CONTENT
jobservice.cancel
USER_UNCATEGORIZED
updatebrand
USER_RESOURCE_UPDATE_CONTENT
updateclient
USER_RESOURCE_UPDATE_CONTENT
assignprojecttobillingaccount
USER_RESOURCE_UPDATE_CONTENT
jobservice.insert
RESOURCE_WRITTEN
jobservice.jobcompleted
RESOURCE_WRITTEN
If the
protoPayload.methodName
log field starts with
clustermanager
followed by any number of characters and ends with
setnodepoolmanagement
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field starts with
clustermanager
followed by any number of characters and ends with
updatecomponentconfig
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field starts with
instance
followed by any number of characters  and ends with
set
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field starts with
instance
followed by any number of characters  and ends with
reset
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field starts with
instance
followed by any number of characters  and ends with
resize
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field starts with
iam.admin
followed by any number of characters and ends with
create
, then the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
USER_UNCATEGORIZED
If the
protoPayload.methodName
log field starts with
iam.admin
followed by any number of characters and ends with
delete
, then the
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
USER_UNCATEGORIZED
If the
protoPayload.methodName
log field starts with
adminservice
,
membershipsservice
,
accesscontextmanager
,
servicemanager
,
serviceusage
,
services
,
projects
, or
clustermanager
followed by any number of characters and ends with
update
,
change
,
activate
,
deactivate
,
enable
,
disable
,
replace
, or
set
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field contains
delete
or
remove
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_DELETION
.
USER_RESOURCE_DELETION
If the
protoPayload.methodName
log field contains
submit
or
update
or
patch
or
ingest
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_WRITTEN
.
USER_RESOURCE_WRITTEN
If the
protoPayload.methodName
log field starts with
imageannotator.batch
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_WRITTEN
.
USER_RESOURCE_WRITTEN
If the
protoPayload.methodName
log field ends with
scheduledsnapshots
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_WRITTEN
.
USER_RESOURCE_WRITTEN
If the
protoPayload.methodName
log field contains
compute.disks.insert
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_WRITTEN
.
USER_RESOURCE_WRITTEN
If the
protoPayload.methodName
log field contains
compute.disks.add
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_WRITTEN
.
USER_RESOURCE_WRITTEN
If the
protoPayload.methodName
log field contains
compute.disks.setlabels
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_WRITTEN
.
USER_RESOURCE_WRITTEN
If the
protoPayload.methodName
log field contains
insert
or
create
or
recreate
or
add
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_CREATION
.
USER_RESOURCE_CREATION
If the
protoPayload.methodName
log field starts with
compute
followed by any number of characters and ends with
migrate
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_CREATION
.
USER_RESOURCE_CREATION
If the
protoPayload.methodName
log field contains
get
or
list
or
watch
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
protoPayload.methodName
log field starts with
cloudsql
followed by any number of characters and ends with
connect
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
protoPayload.methodName
log field contains
create
or
Create
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_CREATION
.
USER_RESOURCE_CREATION
If the
protoPayload.methodName
log field contains
get
or
Get
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
protoPayload.methodName
log field starts with
jobservice
or
JobService
followed by Query
or
query
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
protoPayload.methodName
log field contains
list
or
List
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
protoPayload.methodName
log field ends with
watch
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
protoPayload.methodName
log field ends with
IngestMessage
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field ends with
UpdateAgent
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field contains
bigquery and ends with
InsertJob
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field ends with
MetricService.CreateTimeSeries
,
then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
protoPayload.methodName
log field ends with
update
,
then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
STATUS_UPDATE
If the
protoPayload.methodName
log field ends with
status.patch
,
then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
NETWORK_CONNECTION
The following table lists the
KUBERNETES_NODE
event identifiers and their corresponding
UDM event types for mappings that aren't based on the
protopayload.methodname
log field.
Event Identifier
Event Type
If the
daemon
log field is equal to
smtpd
, then the
metadata.event_type
UDM field is set to
EMAIL_UNCATEGORIZED
.
EMAIL_UNCATEGORIZED
If the
path
log field is not empty, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
NETWORK_HTTP
If the
htttpRequest.serverIp
or
httpRequest.remoteIp
log field is not empty, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
NETWORK_HTTP
If the
htttpRequest.requestMethod
log field is equal to
POST
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_UPDATE_CONTENT
.
USER_RESOURCE_UPDATE_CONTENT
If the
htttpRequest.requestMethod
log field is equal to
GET
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
USER_RESOURCE_ACCESS
If the
htttpRequest.requestMethod
log field is equal to
DELETE
, then the
metadata.event_type
UDM field is set to
USER_RESOURCE_DELETION
.
USER_RESOURCE_DELETION
If the
resource.type
log field is equal to
k8s_container
and the
jsonPayload.protocol
log field is matched with regular expression
HTTP
, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
NETWORK_HTTP
If the
resource.type
log field is equal to
k8s_container
and the
jsonPayload.protocol
log field does not match with regular expression
HTTP
and the
jsonPayload.response_code
log field is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
NETWORK_CONNECTION
Field mapping reference: KUBERNETES_NODE Common Fields
The following table lists the common fields of the
KUBERNETES_NODE
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
insertId
metadata.product_log_id
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
CLUSTER
.
resource.type
target.resource.resource_subtype
resource.labels.project_id
target.resource_ancestors.product_object_id
resource.labels.cluster_name
target.resource.name
If the
resource.type
log field value is equal to
k8s_cluster
,
then the
resource.labels.cluster_name
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
gke_cluster
and
protoPayload.resourceName
is
not
empty, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
gke_cluster
, then the
resource.labels.cluster_name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resource.labels.cluster_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
resource.labels.location
target.resource.attributes.cloud.availability_zone
resource.labels.nodepool_name
target.resource.name
If the
resource.type
log field value is equal to
gke_nodepool
and
protoPayload.resourceName
is
not
empty, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
gke_nodepool
,
then the
resource.labels.nodepool_name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resource.labels.nodepool_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
resource.labels.component_location
target.resource.attribute.labels [component_location]
resource.labels.component_name
target.resource_ancestors.labels [component_name]
If the
resource.type
log field value is equal to
k8s_control_plane_component
and
protoPayload.resourceName
is
not
empty, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_control_plane_component
,
then the
resource.labels.component_name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resource.labels.component_name
log field is mapped to the
target.resource_ancestors.labels.value
UDM field.
resource.labels.pod_name
target.resource_ancestors.name
If the
resource.type
log field value is equal to
k8s_pod
and
protoPayload.resourceName
is
not
empty, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_pod
,
then the
resource.labels.pod_name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resource.labels.pod_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
resource.labels.container_name
target.resource.name
If the
resource.type
log field value is equal to
k8s_container
and
protoPayload.resourceName
is
not
empty, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
,
then the
resource.labels.container_name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resource.labels.container_name
log field is mapped to the
target.resource_ancestors.labels.value
UDM field.
resource.labels.namespace_name
target.namespace
resource.labels.node_name
target.resource.name
If the
resource.type
log field value is equal to
k8s_node
and
protoPayload.resourceName
is
not
empty, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_node
,
then the
resource.labels.node_name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resource.labels.node_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
protoPayload.resourceName
target.resource.name
If the
resource.type
log field value is equal to
audited_resource
, then the
protoPayload.resourceName
log field is mapped to the
target.resource.name
UDM field.
timestamp
metadata.event_timestamp
severity
security_result.severity
The
security_result.severity
UDM field is set to one of the following values:
CRITICAL
if the
severity
field is equal to
CRITICAL
.
ERROR
if the
severity
field is equal to
ERROR
.
HIGH
if the
severity
field is equal to
ALERT
or
EMERGENCY
.
INFORMATIONAL
if the
severity
field is equal to
INFO
or
NOTICE
.
LOW
if the
severity
field is equal to
DEBUG
.
MEDIUM
if the
severity
field is equal to
WARNING
.
UNKNOWN_SEVERITY
if the
severity
field is equal to any other value.
logName
metadata.url_back_to_product
receiveTimestamp
metadata.collected_timestamp
httpRequest.latency
about.labels [httprequest_latency]
(deprecated)
httpRequest.latency
additional.fields [httprequest_latency]
httpRequest.protocol
network.application_protocol
httpRequest.remoteIp
principal.ip
If the
x_forwarded_for
log field value is empty or the
jsonPayload.httpRequest.x-forwarded-for
log field array has one value, then the
httpRequest.remoteIp
log field is mapped to the
principal.ip
UDM field.
httpRequest.remoteIp
intermediary.ip
If the
x_forwarded_for
log field value is
not
empty or the
jsonPayload.httpRequest.x-forwarded-for
log field array has more than one value, then the
httpRequest.remoteIp
log field is mapped to the
intermediary.ip
UDM field.
httpRequest.remoteIp
principal.port
httpRequest.requestMethod
network.http.method
httpRequest.requestSize
network.sent_bytes
httpRequest.requestUrl
target.url
httpRequest.responseSize
network.received_bytes
httpRequest.serverIp
target.ip
httpRequest.serverIp
target.port
httpRequest.status
network.http.response_code
httpRequest.userAgent
network.http.user_agent
protoPayload.request.subjects.name
target.user.attribute.labels [subject_name]
protoPayload.request.subjects.kind
target.user.attribute.labels [subject_kind]
textPayload
principal.ip
Used a Grok pattern to extract
principal_ip
from the
textPayload
log field and mapped to the
principal.ip
UDM field.
textPayload
target.ip
Used a Grok pattern to extract
target_ip
from the
textPayload
log field and mapped to the
target.ip
UDM field.
textPayload
network.http.method
If the
network.http.method
UDM field is
not
empty, then
network_method
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
network_method
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
network.http.method
UDM field.
textPayload
target.url
If the
target.url
UDM field is
not
empty, then
target_url
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
target_url
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
target.url
UDM field.
textPayload
network.application_protocol
If the
network.application_protocol
UDM field is
not
empty, then
network_application_protocol
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
network_application_protocol
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
network.application_protocol
UDM field.
textPayload
network.application_protocol_version
If the
network.application_protocol_version
UDM field is
not
empty, then
network_application_protocol_version
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
network_application_protocol_version
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
network.application_protocol_version
UDM field.
textPayload
network.http.response_code
If the
network.http.response_code
UDM field is
not
empty, then
network_http_response_code
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
network_http_response_code
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
network.http.response_code
UDM field.
textPayload
target.hostname
If the
target.hostname
UDM field is
not
empty, then
target_hostname
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
target_hostname
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
target.hostname
UDM field.
textPayload
network.http.user_agent
If the
network.http.user_agent
UDM field is
not
empty, then
network_http_user_agent
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
network_http_user_agent
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
network.http.user_agent
UDM field.
textPayload
target.port
If the
target.port
UDM field is
not
empty, then
target_port
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
target_port
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
target.port
UDM field.
textPayload
network.session_id
If the
network.session_id
UDM field is
not
empty, then
network_session_id
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
additional.fields
UDM field.
Else,
network_session_id
is extracted from the
textPayload
log field using a Grok pattern and mapped to the
network.session_id
UDM field.
jsonPayload.metadata.errorCause
security_result.detection_fields[metadata_error_cause]
jsonPayload.metadata.errorMessage
security_result.detection_fields[metadata_error_message]
labels.authorization.k8s.io/decision
security_result.action_details
security_result.action
If the
labels.authorization.k8s.io/decision
log field value is equal to
allow
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
labels.authorization.k8s.io/decision
log field value is equal to
forbid
, then the
security_result.action
UDM field is set to
BLOCK
.
Field mapping reference: KUBERNETES_NODE log fields to UDM fields
The following table lists the log fields of the
KUBERNETES_NODE
log type and their corresponding UDM fields.
Resource types
Log field
UDM mapping
Logic
k8s_container
labels.upstream_host
about.ip
k8s_pod
labels.activity_type_name
about.labels [activity_type_name]
(deprecated)
k8s_pod
labels.activity_type_name
additional.fields [activity_type_name]
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.requestMetadata.requestAttributes.time
about.labels [caller_network_request_time]
(deprecated)
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.requestMetadata.requestAttributes.time
additional.fields [caller_network_request_time]
duration
about.labels [duration]
(deprecated)
duration
additional.fields [duration]
k8s_node
jsonPayload.action
about.labels [jsonpayload_action]
(deprecated)
k8s_node
jsonPayload.action
additional.fields [jsonpayload_action]
k8s_cluster, k8s_pod, k8s_node
jsonPayload.apiVersion
about.labels [jsonpayload_api_version]
(deprecated)
k8s_cluster, k8s_pod, k8s_node
jsonPayload.apiVersion
additional.fields [jsonpayload_api_version]
gke_nodepool, k8s_pod, k8s_cluster
jsonPayload.@type
about.labels [jsonpayload_at_type]
(deprecated)
gke_nodepool, k8s_pod, k8s_cluster
jsonPayload.@type
additional.fields [jsonpayload_at_type]
k8s_container
jsonPayload.chartVersion
about.labels [jsonpayload_chart_version]
(deprecated)
k8s_container
jsonPayload.chartVersion
additional.fields [jsonpayload_chart_version]
k8s_container
jsonPayload.clusterDistribution
about.labels [jsonpayload_cluster_distribution]
(deprecated)
k8s_container
jsonPayload.clusterDistribution
additional.fields [jsonpayload_cluster_distribution]
k8s_container
jsonPayload.componentName
about.labels [jsonpayload_component_name]
(deprecated)
k8s_container
jsonPayload.componentName
additional.fields [jsonpayload_component_name]
k8s_container
jsonPayload.componentVersion
about.labels [jsonpayload_component_version]
(deprecated)
k8s_container
jsonPayload.componentVersion
additional.fields [jsonpayload_component_version]
k8s_container
jsonPayload.coresPerReplica
about.labels [jsonpayload_cores_per_replica]
(deprecated)
k8s_container
jsonPayload.coresPerReplica
additional.fields [jsonpayload_cores_per_replica]
k8s_cluster
jsonPayload.eventTime
about.labels [jsonpayload_event_time]
(deprecated)
k8s_cluster
jsonPayload.eventTime
additional.fields [jsonpayload_event_time]
k8s_container
jsonPayload.includeUnschedulableNodes
about.labels [jsonpayload_include_unschedulable_nodes]
(deprecated)
k8s_container
jsonPayload.includeUnschedulableNodes
additional.fields [jsonpayload_include_unschedulable_nodes]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.kind
about.labels [jsonpayload_kind]
(deprecated)
k8s_pod, k8s_cluster, k8s_node
jsonPayload.kind
additional.fields [jsonpayload_kind]
k8s_container
jsonPayload.log
about.labels [jsonpayload_log]
(deprecated)
k8s_container
jsonPayload.log
additional.fields [jsonpayload_log]
k8s_container
jsonPayload.logtag
about.labels [jsonpayload_logtag]
(deprecated)
k8s_container
jsonPayload.logtag
additional.fields [jsonpayload_logtag]
k8s_container
jsonPayload.preventSinglePointFailure
about.labels [jsonpayload_prevent_single_point_failure]
(deprecated)
k8s_container
jsonPayload.preventSinglePointFailure
additional.fields [jsonpayload_prevent_single_point_failure]
k8s_cluster
jsonPayload.status.measureTime
about.labels [jsonpayload_status_measure_time]
(deprecated)
k8s_cluster
jsonPayload.status.measureTime
additional.fields [jsonpayload_status_measure_time]
k8s_node
jsonPayload.SYSLOG_FACILITY
about.labels [jsonpayload_syslog_facility]
(deprecated)
k8s_node
jsonPayload.SYSLOG_FACILITY
additional.fields [jsonpayload_syslog_facility]
k8s_node
jsonPayload.SYSLOG_IDENTIFIER
about.labels [jsonpayload_syslog_identifier]
(deprecated)
k8s_node
jsonPayload.SYSLOG_IDENTIFIER
additional.fields [jsonpayload_syslog_identifier]
k8s_node
jsonPayload.SYSLOG_TIMESTAMP
about.labels [jsonpayload_syslog_timestamp]
(deprecated)
k8s_node
jsonPayload.SYSLOG_TIMESTAMP
additional.fields [jsonpayload_syslog_timestamp]
k8s_container
jsonPayload.timestamp
about.labels [jsonpayload_timestamp]
(deprecated)
k8s_container
jsonPayload.timestamp
additional.fields [jsonpayload_timestamp]
k8s_pod, k8s_cluster, k8s_node, k8s_container
jsonPayload.type
about.labels [jsonpayload_type]
(deprecated)
k8s_pod, k8s_cluster, k8s_node, k8s_container
jsonPayload.type
additional.fields [jsonpayload_type]
k8s_container
jsonPayload.v
about.labels [jsonpayload_v]
(deprecated)
k8s_container
jsonPayload.v
additional.fields [jsonpayload_v]
k8s_container
labels.protocol
about.labels [labels_protocol]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.lastTimestamp
about.labels [last_timestamp]
(deprecated)
k8s_pod, k8s_cluster, k8s_node
jsonPayload.lastTimestamp
additional.fields [last_timestamp]
k8s_container
jsonPayload.localTimestamp
about.labels [local_timestamp]
(deprecated)
k8s_container
jsonPayload.localTimestamp
additional.fields [local_timestamp]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.managedFields.apiVersion
about.labels [managed_fields_api_version]
k8s_cluster
protoPayload.request.metadata.managedFields.apiVersion
about.labels [managed_fields_api_version]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.managedFields.fieldsType
about.labels [managed_fields_fields_type]
k8s_cluster
protoPayload.request.metadata.managedFields.manager
about.labels [managed_fields_manager]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.managedFields.operation
about.labels [managed_fields_operation]
k8s_cluster
protoPayload.request.metadata.managedFields.operation
about.labels [managed_fields_operation]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.managedFields.time
about.labels [managed_fields_time]
k8s_cluster
protoPayload.request.metadata.managedFields.time
about.labels [managed_fields_time]
(deprecated)
k8s_cluster
protoPayload.request.metadata.managedFields.time
additional.fields [managed_fields_time]
k8s_cluster
protoPayload.request.metadata.managedFields.fieldsType
about.labels [managed_fields_type]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.name
about.labels [metadata_name]
(deprecated)
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.name
additional.fields [metadata_name]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.namespace
about.labels [metadata_namespace]
(deprecated)
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.namespace
additional.fields [metadata_namespace]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.resourceVersion
about.labels [metadata_resourceversion]
(deprecated)
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.resourceVersion
additional.fields [metadata_resourceversion]
k8s_container
jsonPayload.nodesPerReplica
about.labels [nodes_per_replica]
(deprecated)
k8s_container
jsonPayload.nodesPerReplica
additional.fields [nodes_per_replica]
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.first
about.labels [operation_first]
(deprecated)
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.first
additional.fields [operation_first]
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.id
about.labels [operation_id]
(deprecated)
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.id
additional.fields [operation_id]
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.last
about.labels [operation_last]
(deprecated)
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.last
additional.fields [operation_last]
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.producer
about.labels [operation_producer]
(deprecated)
gke_cluster, gke_nodepool, k8s_pod, k8s_cluster, k8s_node
operation.producer
additional.fields [operation_producer]
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.@type
about.labels [protopayload_at_type]
(deprecated)
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.@type
additional.fields [protopayload_at_type]
k8s_cluster
protoPayload.request.spec.acquireTime
about.labels [protopayload_req_spec_acquire_time]
(deprecated)
k8s_cluster
protoPayload.request.spec.acquireTime
additional.fields [protopayload_req_spec_acquire_time]
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.request.@type
about.labels [protopayload_request_at_type]
(deprecated)
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.request.@type
additional.fields [protopayload_request_at_type]
k8s_cluster
protoPayload.response.metadata.managedFields.fieldsType
about.labels [protopayload_res_meta_field_type]
(deprecated)
k8s_cluster
protoPayload.response.metadata.managedFields.fieldsType
additional.fields [protopayload_res_meta_field_type]
k8s_cluster
protoPayload.request.metadata.annotations.control-plane.alpha.kubernetes.io/leader
about.labels [req_annotations_control_panel_kubernetes_leader]
(deprecated)
k8s_cluster
protoPayload.request.metadata.annotations.control-plane.alpha.kubernetes.io/leader
additional.fields [req_annotations_control_panel_kubernetes_leader]
gke_cluster
protoPayload.response.startTime
about.labels [res_start_time]
(deprecated)
gke_cluster
protoPayload.response.startTime
additional.fields [res_start_time]
k8s_pod, k8s_cluster
protoPayload.response.metadata.annotations.control-plane.alpha.kubernetes.io/leader
about.labels [resp_metadata_annotations_control-plane.alpha.kubernetes.io/leader]
(deprecated)
k8s_pod, k8s_cluster
protoPayload.response.metadata.annotations.control-plane.alpha.kubernetes.io/leader
additional.fields [resp_metadata_annotations_control-plane.alpha.kubernetes.io/leader]
k8s_cluster
protoPayload.response.metadata.managedFields.manager
about.labels [resp_metadata_managedFields_manager]
k8s_cluster
protoPayload.response.metadata.managedFields.operation
about.labels [resp_metadata_managedFields_operation]
k8s_cluster
protoPayload.response.metadata.managedFields.time
about.labels [resp_metadata_managedFields_time]
k8s_cluster
protoPayload.response.metadata.managedFields.apiVersion
about.labels [resp_metadata_managed_api_version]
k8s_cluster
protoPayload.response.spec.acquireTime
about.labels [resp_spec_acquire_time]
(deprecated)
k8s_cluster
protoPayload.response.spec.acquireTime
additional.fields [resp_spec_acquire_time]
k8s_cluster
protoPayload.response.spec.groups
about.labels [resp_spec_groups]
gke_cluster, gke_nodepool, k8s_cluster
protoPayload.response.@type
about.labels [response_type]
(deprecated)
gke_cluster, gke_nodepool, k8s_cluster
protoPayload.response.@type
additional.fields [response_type]
start_time
about.labels [start_time]
(deprecated)
start_time
additional.fields [start_time]
gke_cluster, gke_nodepool, k8s_control_plane_component, k8s_pod, k8s_cluster, k8s_node, k8s_container, k8s_service
textPayload
about.labels [textpayload]
(deprecated)
gke_cluster, gke_nodepool, k8s_control_plane_component, k8s_pod, k8s_cluster, k8s_node, k8s_container, k8s_service
textPayload
additional.fields [textpayload]
upstream_service_time
about.labels [upstream_service_time]
(deprecated)
upstream_service_time
additional.fields [upstream_service_time]
x_carbon_log_ext1
about.labels [x_carbon_log_ext1]
(deprecated)
x_carbon_log_ext1
additional.fields [x_carbon_log_ext1]
k8s_container
labels.upstream_host
about.port
k8s_pod, k8s_cluster, k8s_node
jsonPayload.reportingInstance
about.resource.name
k8s_pod, k8s_cluster, k8s_node
jsonPayload.reportingComponent
about.resource.resource_subtype
gke_cluster
protoPayload.response.selfLink
about.url
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.managedFields.manager
about.user.user_display_name
x_forwarded_for
src.ip
The first value of the
x_forwarded_for
log field array is mapped to
src.ip
and
principal.ip
UDM fields.
x_forwarded_for
principal.ip
The first value of the
x_forwarded_for
log field array is mapped to
src.ip
and
principal.ip
UDM fields.
x_forwarded_for
intermediary.ip
The second and all other successive values of the
x_forwarded_for
log field array is mapped to the
intermediary.ip
UDM field.
jsonPayload.httpRequest.x-forwarded-for
src.ip
The first value of the
jsonPayload.httpRequest.x-forwarded-for
log field array is mapped to
src.ip
UDM field.
jsonPayload.httpRequest.x-forwarded-for
principal.ip
The second value of the
jsonPayload.httpRequest.x-forwarded-for
log field array is mapped to
principal.ip
UDM field.
jsonPayload.httpRequest.x-forwarded-for
intermediary.ip
The third and all other successive values of the
jsonPayload.httpRequest.x-forwarded-for
log field array is mapped to
intermediary.ip
UDM field.
jsonPayload.authority
principal.administrative_domain
jsonPayload.path
target.file.full_path
k8s_pod, k8s_cluster, k8s_node, k8s_container, k8s_control_plane_component
jsonPayload.message
metadata.description
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.methodName
metadata.product_event_type
request_id
metadata.product_log_id
protocol
network.application_protocol
k8s_node
jsonPayload.connection.direction
network.direction
The
network.direction
UDM field is set to one of the following values:
OUTBOUND
if the
jsonPayload.connection.direction
field is equal to
egress
.
INBOUND
if the
jsonPayload.connection.direction
field is equal to
ingress
.
k8s_container
labels.upstream_cluster
network.direction
k8s_container
jsonPayload.request_length
network.received_bytes
k8s_container
jsonPayload.request_uri
principal.url
k8s_container
jsonPayload.request_method
network.http.method
k8s_container
jsonPayload.remote_addr
principal.ip
k8s_container
jsonPayload.server_protocol
network.application_protocol
Extracted
application_protocol
from
jsonPayload.server_protocol
log field using Grok pattern and mapped it to the
network.application_protocol
UDM field.
k8s_container
jsonPayload.server_protocol
network.application_protocol_version
Extracted
application_protocol_version
from
jsonPayload.server_protocol
log field using Grok pattern and mapped it to the
network.application_protocol_version
UDM field.
k8s_container
jsonPayload.status
network.http.response_code
k8s_container
jsonPayload.http_host
principal.hostname
k8s_container
jsonPayload.http_host
principal.asset.hostname
k8s_container
jsonPayload.http_user_agent
network.http.user_agent
k8s_container
jsonPayload.ssl_protocol
network.tls.version
k8s_container
jsonPayload.remote_user
principal.user.userid
k8s_container
jsonPayload.upstream_addr
target.ip
Extracted
ip
from
jsonPayload.upstream_addr
log field using Grok pattern and mapped it to the
target.ip
UDM field.
k8s_container
jsonPayload.upstream_addr
target.port
Extracted
port
from
jsonPayload.upstream_addr
log field using Grok pattern and mapped it to the
target.port
UDM field.
k8s_container
jsonPayload.http_referrer
network.http.referral_url
k8s_container
jsonPayload.bytes_sent
network.sent_bytes
k8s_container
jsonPayload.server_port
target.nat_port
k8s_container
jsonPayload.upstream_response_time
additional.fields[jsonpayload_upstream_response_time]
k8s_container
jsonPayload.msec
additional.fields[jsonpayload_msec]
k8s_container
jsonPayload.upstream_connect_time
additional.fields[jsonpayload_upstream_connect_time]
k8s_container
jsonPayload.body_bytes_sent
additional.fields[jsonpayload_body_bytes_sent]
k8s_container
jsonPayload.request_time
additional.fields[jsonpayload_request_time]
k8s_container
jsonPayload.http_method
additional.fields[jsonpayload_http_method]
k8s_container
jsonPayload.http_version
additional.fields[jsonpayload_http_version]
k8s_container
jsonPayload.response_code
additional.fields[jsonpayload_response_code]
upstream_cluster
network.direction
The
network.direction
UDM field is set to one of the following values:
INBOUND
if the
upstream_cluster
field is equal to
Inbound
or
inbound
.
OUTBOUND
if the
labels.upstream_cluster
field is not empty.
labels.upstream_cluster
network.direction
The
network.direction
UDM field is set to one of the following values:
INBOUND
if the
upstream_cluster
field is equal to
Inbound
or
inbound
.
OUTBOUND
if the
labels.upstream_cluster
field is not empty.
method
network.http.method
k8s_cluster
protoPayload.request.spec.nonResourceAttributes.verb
network.http.method
k8s_container
jsonPayload.http.req.method
network.http.method
k8s_container
jsonPayload.http.req.path
network.http.referral_url
k8s_cluster
protoPayload.request.spec.nonResourceAttributes.path
network.http.referral_url
response_code
network.http.response_code
gke_nodepool, k8s_cluster, audited_resource
protoPayload.status.code
network.http.response_code
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.requestMetadata.callerSuppliedUserAgent
network.http.user_agent
user_agent
network.http.user_agent
k8s_node
jsonPayload.connection.protocol
network.ip_protocol
bytes_received
network.received_bytes
k8s_container
duration
network.received_bytes
bytes_sent
network.sent_bytes
k8s_container
labels.total_sent_bytes
network.sent_bytes
k8s_container
jsonPayload.session
network.session_id
k8s_container
labels.service_authentication_policy
network.tls.cipher
authority
principal.administrative_domain
k8s_container
labels.source_principal
principal.administrative_domain
k8s_container
labels.source_app
principal.application
k8s_container
jsonPayload.hostname
principal.hostname
k8s_container
labels.source_name
principal.hostname
k8s_pod, k8s_node
jsonPayload.source.host
principal.hostname
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.requestMetadata.callerIp
principal.ip
k8s_node
jsonPayload.connection.src_ip
principal.ip
k8s_container
labels.source_ip
principal.ip
k8s_node
jsonPayload._CAP_EFFECTIVE
principal.labels [jsonpayload_cap_effective]
(deprecated)
k8s_node
jsonPayload._CAP_EFFECTIVE
additional.fields [jsonpayload_cap_effective]
k8s_container
jsonPayload.currency
principal.labels [jsonpayload_currency]
(deprecated)
k8s_container
jsonPayload.currency
additional.fields [jsonpayload_currency]
k8s_container
jsonPayload.envTime
principal.labels [jsonpayload_env_time]
(deprecated)
k8s_container
jsonPayload.envTime
additional.fields [jsonpayload_env_time]
k8s_node
jsonPayload._GID
principal.labels [jsonpayload_gid]
(deprecated)
k8s_node
jsonPayload._GID
additional.fields [jsonpayload_gid]
k8s_container
jsonPayload.http.req.id
principal.labels [jsonpayload_http_req_id]
(deprecated)
k8s_container
jsonPayload.http.req.id
additional.fields [jsonpayload_http_req_id]
k8s_node
jsonPayload._SELINUX_CONTEXT
principal.labels [jsonpayload_selinux_context]
(deprecated)
k8s_node
jsonPayload._SELINUX_CONTEXT
additional.fields [jsonpayload_selinux_context]
k8s_node
jsonPayload._SOURCE_REALTIME_TIMESTAMP
principal.labels [jsonpayload_source_realtime_timestamp]
(deprecated)
k8s_node
jsonPayload._SOURCE_REALTIME_TIMESTAMP
additional.fields [jsonpayload_source_realtime_timestamp]
k8s_node
jsonPayload._STREAM_ID
principal.labels [jsonpayload_stream_id]
(deprecated)
k8s_node
jsonPayload._STREAM_ID
additional.fields [jsonpayload_stream_id]
k8s_container
jsonPayload.traceLevel
principal.labels [jsonpayload_trace_level]
(deprecated)
k8s_container
jsonPayload.traceLevel
additional.fields [jsonpayload_trace_level]
k8s_node
jsonPayload._TRANSPORT
principal.labels [jsonpayload_transport]
(deprecated)
k8s_node
jsonPayload._TRANSPORT
additional.fields [jsonpayload_transport]
k8s_node
jsonPayload._UID
principal.labels [jsonpayload_uid]
(deprecated)
k8s_node
jsonPayload._UID
additional.fields [jsonpayload_uid]
audited_resource
protoPayload.request.filter
principal.labels [protopayload_request_filter]
(deprecated)
audited_resource
protoPayload.request.filter
additional.fields [protopayload_request_filter]
audited_resource
protoPayload.request.requests.features.type
principal.labels [protopayload_requests_features_type]
gke_cluster, gke_nodepool
protoPayload.requestMetadata.requestAttributes.reason
principal.labels [request_attributes_reason]
(deprecated)
gke_cluster, gke_nodepool
protoPayload.requestMetadata.requestAttributes.reason
additional.fields [request_attributes_reason]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.source.component
principal.labels [source_component]
(deprecated)
k8s_pod, k8s_cluster, k8s_node
jsonPayload.source.component
additional.fields [source_component]
k8s_container
labels.source_version
principal.labels [source_version]
k8s_container
labels.source_workload
principal.labels [source_workload]
k8s_node
jsonPayload.src.workload_kind
principal.labels [src_workload_kind]
(deprecated)
k8s_node
jsonPayload.src.workload_kind
additional.fields [src_workload_kind]
k8s_node
jsonPayload.src.workload_name
principal.labels [src_workload_name]
(deprecated)
k8s_node
jsonPayload.src.workload_name
additional.fields [src_workload_name]
k8s_node
jsonPayload._SYSTEMD_CGROUP
principal.labels [systemd_cgroup]
(deprecated)
k8s_node
jsonPayload._SYSTEMD_CGROUP
additional.fields [systemd_cgroup]
k8s_node
jsonPayload._SYSTEMD_INVOCATION_ID
principal.labels [systemd_invocation_id]
(deprecated)
k8s_node
jsonPayload._SYSTEMD_INVOCATION_ID
additional.fields [systemd_invocation_id]
k8s_node
jsonPayload._SYSTEMD_SLICE
principal.labels [systemd_slice]
(deprecated)
k8s_node
jsonPayload._SYSTEMD_SLICE
additional.fields [systemd_slice]
k8s_node
jsonPayload._SYSTEMD_UNIT
principal.labels [systemd_unit ]
(deprecated)
k8s_node
jsonPayload._SYSTEMD_UNIT
additional.fields [systemd_unit ]
audited_resource
protoPayload.requestMetadata.callerNetwork
principal.labels [caller_network]
(deprecated)
audited_resource
protoPayload.requestMetadata.callerNetwork
additional.fields [caller_network]
k8s_node
jsonPayload.src.namespace
additional.fields[src_namespace]
k8s_node
jsonPayload.src.pod_namespace
additional.fields[src_pod_namespace]
k8s_container
labels.source_namespace
additional.fields[labels_source_namespace]
k8s_node
jsonPayload.connection.src_port
principal.port
k8s_container
labels.source_port
principal.port
k8s_node
jsonPayload._CMDLINE
principal.process.command_line
k8s_node
jsonPayload._EXE
principal.process.file.full_path
k8s_node
jsonPayload._COMM
principal.process.file.names
k8s_node
jsonPayload._PID
principal.process.pid
k8s_node
jsonPayload._BOOT_ID
principal.resource_ancestors.attribute.labels [jsonpayload_boot_id]
k8s_container
jsonPayload.releaseTrain
principal.resource_ancestors.attribute.labels [release_train]
gke_cluster
protoPayload.request.cluster.initialClusterVersion
principal.resource_ancestors.attribute.labels [req_cls_initial_cluster_version]
gke_cluster
protoPayload.request.cluster.locations
principal.resource_ancestors.attribute.labels [req_cls_locations]
gke_cluster
protoPayload.request.cluster.location
principal.resource_ancestors.attribute.labels [req_cluster_location]
k8s_node
jsonPayload.src.pod_name
principal.resource_ancestors.name
k8s_node
jsonPayload._HOSTNAME
principal.resource_ancestors.name
gke_cluster
protoPayload.request.cluster.loggingConfig.componentConfig.enableComponents
principal.resource.attribute.labels [cluster_loggingConfig_componentConfig_enableComponents]
gke_cluster
protoPayload.request.cluster.monitoringConfig.componentConfig.enableComponents
principal.resource.attribute.labels [cluster_monitoringConfig_componentConfig_enableComponents]
k8s_node
jsonPayload.count
principal.resource.attribute.labels [jsonpayload_count]
k8s_container
jsonPayload.region
principal.resource.attribute.labels [jsonpayload_region]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.metadata.creationTimestamp
principal.resource.attribute.labels [metadata_creation_time_stamp]
k8s_pod
protoPayload.metadata.creationTimestamp
principal.resource.attribute.labels [req_creation_timestamp]
k8s_container
labels.source_canonical_revision
principal.resource.attribute.labels [source_canonical_revision]
k8s_container
labels.source_canonical_service
principal.resource.attribute.labels [source_canonical_service]
k8s_node
jsonPayload._MACHINE_ID
principal.resource.product_object_id
gke_cluster, gke_nodepool, k8s_cluster,  audited_resource
protoPayload.authorizationInfo.granted
principal.user.attribute.labels [authorization_granted]
audited_resource
protoPayload.request.pageToken
principal.user.attribute.labels [protopayload_request_page_token]
audited_resource
protoPayload.request.pageSize
principal.user.attribute.labels [req_page_size]
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.authorizationInfo.permission
principal.user.attribute.permissions.name
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.authenticationInfo.principalEmail
principal.user.email_addresses
If the
protoPayload.authenticationInfo.principalEmail
log field value is matched with regular expression
.
@.
, then the following fields are mapped:
The
protoPayload.authenticationInfo.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
The
DATA:user_id@GREEDYDATA
log field is mapped to the
protoPayload.authenticationInfo.principalEmail
UDM field.
The
user_id
log field is mapped to the
principal.user.userid
UDM field.
Else, the
protoPayload.authenticationInfo.principalEmail
log field is mapped to the
principal.user.userid
UDM field.
audited_resource
protoPayload.authenticationInfo.serviceAccountDelegationInfo.firstPartyPrincipal.principalEmail
principal.user.email_addresses
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.authenticationInfo.principalEmail
principal.user.userid
If the
protoPayload.authenticationInfo.principalEmail
log field value is matched with regular expression
.
@.
, then the following fields are mapped:
The
protoPayload.authenticationInfo.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
The
DATA:user_id@GREEDYDATA
log field is mapped to the
protoPayload.authenticationInfo.principalEmail
UDM field.
The
user_id
log field is mapped to the
principal.user.userid
UDM field.
Else, the
protoPayload.authenticationInfo.principalEmail
log field is mapped to the
principal.user.userid
UDM field.
k8s_container
labels.mesh_uid
principal.user.userid
k8s_cluster
protoPayload.request.metadata.uid
principal.user.userid
If the
principal.user.userid
log field value is
not
empty, then the
protoPayload.request.metadata.uid
log field is mapped to the
principal.user.userid
UDM field.
Else, the
protoPayload.request.metadata.uid
log field is mapped to the
principal.labels
UDM field.
audited_resource
protoPayload.authenticationInfo.principalSubject
principal.user.userid
k8s_cluster
labels.authorization.k8s.io/decision
security_result.action
k8s_container
labels.connection_state
security_result.action
The
security_result.action
UDM field is set to one of the following values:
ALLOW
if the
labels.connection_state
field is equal to
OPEN
or
CONNECTED
.
BLOCK
if the
labels.connection_state
field is equal to
CLOSE
.
k8s_node
jsonPayload.disposition
security_result.action_details
k8s_cluster
labels.authorization.k8s.io/reason
security_result.action_details
gke_nodepool, k8s_cluster, audited_resource
protoPayload.status.message
security_result.description
gke_cluster
protoPayload.response.status
security_result.description
k8s_pod
labels.logMessage
security_result.description
k8s_pod
labels.errorGroupId
security_result.detection_fields [error_group_id]
k8s_pod
jsonPayload.errorEvent.eventTime
security_result.detection_fields [jsonpayload_error_event_event_time]
k8s_pod
jsonPayload.errorEvent.message
security_result.detection_fields [jsonpayload_error_event_message]
k8s_pod
jsonPayload.errorEvent.serviceContext.service
security_result.detection_fields [jsonpayload_error_event_service_context_service]
k8s_pod
jsonPayload.errorGroup
security_result.detection_fields [jsonpayload_error_group]
k8s_pod
jsonPayload.errorEvent.serviceContext.resourceType
security_result.detection_fields [jsonpayload_error_service_context_resource_type]
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.resourceName
security_result.detection_fields [protopayload_resource_name]
audited_resource
protoPayload.authenticationInfo.serviceAccountKeyName
security_result.detection_fields [service_account_key_name]
k8s_node
jsonPayload.PRIORITY
security_result.priority_details
k8s_node
jsonPayload.policies.namespace
security_result.rule_labels [policy_namespace]
k8s_node
jsonPayload.policies.name
security_result.rule_name
response_flags
security_result.summary
k8s_pod, k8s_cluster, k8s_node
jsonPayload.reason
security_result.summary
k8s_container
sourceLocation.function
src.application
k8s_node, k8s_container, k8s_control_plane_component
sourceLocation.file
src.file.full_path
k8s_node, k8s_container, k8s_control_plane_component
sourceLocation.line
src.labels [source_location_line]
(deprecated)
k8s_node, k8s_container, k8s_control_plane_component
sourceLocation.line
additional.fields [source_location_line]
k8s_container
labels.destination_principal
target.administrative_domain
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.serviceName
target.application
k8s_container
labels.destination_app
target.application
k8s_container
labels.destination_canonical_service
target.application
audited_resource
resource.labels.service
target.application
x_downstream_host
target.asset.attribute.labels [x_downstream_host]
k8s_container
labels.path
target.file.full_path
path
target.file.full_path
k8s_container
labels.destination_service_host
target.hostname
k8s_node
jsonPayload.connection.dest_ip
target.ip
k8s_container
labels.destination_ip
target.ip
upstream_host
target.ip
k8s_node
jsonPayload.dest.workload_name
target.labels [dest_workload_name]
(deprecated)
k8s_node
jsonPayload.dest.workload_name
additional.fields [dest_workload_name]
k8s_container
labels.destination_name
target.labels [destination_name]
k8s_container
labels.destination_version
target.labels [destination_version]
k8s_container
labels.destination_workload
target.labels [destination_workload]
audited_resource
protoPayload.numResponseItems
target.labels [num_response_items]
(deprecated)
audited_resource
protoPayload.numResponseItems
additional.fields [num_response_items]
gke_cluster
protoPayload.request.update.desiredLoggingConfig.componentConfig.enableComponents
target.labels [req_update_desiredLoggingConfig_componentConfig_enableComponents]
(deprecated)
gke_cluster
protoPayload.request.update.desiredLoggingConfig.componentConfig.enableComponents
additional.fields [req_update_desiredLoggingConfig_componentConfig_enableComponents]
k8s_cluster
protoPayload.response.spec.nonResourceAttributes.path
target.labels [resp_spec_non_resource_attributes_path]
(deprecated)
k8s_cluster
protoPayload.response.spec.nonResourceAttributes.path
additional.fields [resp_spec_non_resource_attributes_path]
k8s_cluster
protoPayload.response.spec.nonResourceAttributes.verb
target.labels [resp_spec_non_resource_attributes_verb]
(deprecated)
k8s_cluster
protoPayload.response.spec.nonResourceAttributes.verb
additional.fields [resp_spec_non_resource_attributes_verb]
x_b3_parentspanid
target.labels [x_b3_parent_span_id]
(deprecated)
x_b3_parentspanid
additional.fields [x_b3_parent_span_id]
x_b3_sampled
target.labels [x_b3_sample_d]
(deprecated)
x_b3_sampled
additional.fields [x_b3_sample_d]
x_b3_span_id
target.labels [x_b3_span_id]
(deprecated)
x_b3_span_id
additional.fields [x_b3_span_id]
x_b3_trace_id
target.labels [x_b3_trace_id]
(deprecated)
x_b3_trace_id
additional.fields [x_b3_trace_id]
k8s_node
jsonPayload.dest.pod_namespace
additional.fields[dest_pod_namespace]
k8s_node
jsonPayload.dest.namespace
additional.fields[dest_namespace]
k8s_container
labels.destination_namespace
additional.fields[labels_destination_namespace]
k8s_cluster
protoPayload.request.metadata.namespace
additional.fields[request_metadata_namespace]
k8s_container
labels.destination_ip
target.port
upstream_host
target.port
k8s_node
jsonPayload.connection.dest_port
target.port
k8s_container
labels.destination_port
target.port
k8s_control_plane_component, k8s_node, k8s_container
jsonPayload.pid
target.process.pid
k8s_pod
labels.deploymentVersion
target.resource_ancestors.attribute.labels [deployment_version]
k8s_container
labels.k8s-pod/kubernetes_io/cluster-service
target.resource_ancestors.attribute.labels [pod_cluster_service]
k8s_container
labels.k8s-pod/component
target.resource_ancestors.attribute.labels [pod_component]
k8s_container
labels.k8s-pod/controller-revision-hash
target.resource_ancestors.attribute.labels [pod_controller_revision_hash]
k8s_container
labels.k8s-pod/dsName
target.resource_ancestors.attribute.labels [pod_ds_name]
k8s_container
labels.k8s-pod/hub.gke.io/project
target.resource_ancestors.attribute.labels [pod_gke_project]
k8s_container
labels.k8s-pod/security_istio_io/tlsMode
target.resource_ancestors.attribute.labels [pod_security_tls_mode]
k8s_container
labels.k8s-pod/service_istio_io/canonical-name
target.resource_ancestors.attribute.labels [pod_service_canonical_name]
k8s_container
labels.k8s-pod/pod-template-generation
target.resource_ancestors.attribute.labels [pod_template_generation]
gke_cluster
protoPayload.request.cluster.network
target.resource_ancestors.attribute.labels [req_cls_network]
gke_cluster
protoPayload.request.cluster.nodePools.management.autoRepair
target.resource_ancestors.attribute.labels [req_clsNodePools_autorepair]
gke_cluster
protoPayload.request.cluster.nodePools.autoscaling.enabled
target.resource_ancestors.attribute.labels [req_clsNodePools_autoscaling_enabled]
gke_cluster
protoPayload.request.cluster.nodePools.autoscaling.maxNodeCount
target.resource_ancestors.attribute.labels [req_clsNodePools_autoscaling_max_node_cnt]
gke_cluster
protoPayload.request.cluster.nodePools.autoscaling.minNodeCount
target.resource_ancestors.attribute.labels [req_clsNodePools_autoscaling_min_node_cnt]
gke_cluster
protoPayload.request.cluster.nodePools.management.autoUpgrade
target.resource_ancestors.attribute.labels [req_clsNodePools_autoupgrade]
gke_cluster
protoPayload.request.cluster.nodePools.config.diskSizeGb
target.resource_ancestors.attribute.labels [req_clsNodePools_config_disksize]
gke_cluster
protoPayload.request.cluster.nodePools.config.diskType
target.resource_ancestors.attribute.labels [req_clsNodePools_config_diskType]
gke_cluster
protoPayload.request.cluster.nodePools.config.imageType
target.resource_ancestors.attribute.labels [req_clsNodePools_config_imagetype]
gke_cluster
protoPayload.request.cluster.nodePools.config.machineType
target.resource_ancestors.attribute.labels [req_clsNodePools_config_machinetype]
gke_cluster
protoPayload.request.cluster.nodePools.config.metadata.disable-legacy-endpoints
target.resource_ancestors.attribute.labels [req_clsNodePools_config_metadata_disable-legacy-endpoints]
gke_cluster
protoPayload.request.cluster.nodePools.config.oauthScopes
target.resource_ancestors.attribute.labels [req_clsNodePools_config_oauth_scopes]
gke_cluster
protoPayload.request.cluster.nodePools.upgradeSettings.maxSurge
target.resource_ancestors.attribute.labels [req_clsNodePools_upgradeSettings_maxSurge]
gke_cluster
protoPayload.request.cluster.nodePools.initialNodeCount
target.resource_ancestors.attribute.labels [req_clsterNodePools_autoscaling_initial_node_cnt]
gke_nodepool
protoPayload.request.nodePool.maxPodsConstraint
target.resource_ancestors.attribute.labels [req_node_pool_name]
gke_cluster
protoPayload.request.cluster.nodePools.name
target.resource_ancestors.name
gke_cluster, gke_nodepool, k8s_cluster, audited_resource
protoPayload.authorizationInfo.resource
target.resource_ancestors.name
k8s_node
jsonPayload.dest.workload_kind
target.resource_ancestors.name
gke_cluster, audited_resource
protoPayload.request.parent
target.resource_ancestors.name
k8s_container
jsonPayload.nodeName
target.resource_ancestors.name
If the
resource.type
log field value is equal to
k8s_container
, then the
jsonPayload.nodeName
log field is mapped to the
target.resource_ancestors.name
UDM field.
k8s_container
labels.instance_name
target.resource_ancestors.name
gke_cluster
protoPayload.request.cluster.subnetwork
target.resource_ancestors.name
k8s_container
labels.requested_server_name
target.resource_ancestors.name
k8s_pod
labels.deploymentAppId
target.resource_ancestors.name
k8s_node
jsonPayload.dest.pod_name
target.resource_ancestors.name
k8s_container
labels.compute.googleapis.com/resource_name
target.resource_ancestors.name
gke_cluster, gke_nodepool
protoPayload.resourceLocation.currentLocations
target.resource.attribute.cloud.availability_zone
If the
index
log field value is equal to
0
, then the
protoPayload.resourceLocation.currentLocations
log field is mapped to the
token_target.resource.attribute.cloud.availability_zone
UDM field.
Else, the
protoPayload.resourceLocation.currentLocations
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
k8s_cluster
protoPayload.response.metadata.creationTimestamp
target.resource.attribute.creation_time
k8s_container
labels.agent_version
target.resource.attribute.labels [agent_version]
k8s_container
labels.connection_id
target.resource.attribute.labels [connection_id]
k8s_container
labels.k8s-pod/container-watcher-unique-id
target.resource.attribute.labels [container_watcher_unique_id]
k8s_container
labels.destination_canonical_revision
target.resource.attribute.labels [destination_canonical_revision]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.involvedObject.apiVersion
target.resource.attribute.labels [jsonpayload_involved_object_apiVersion]
k8s_pod
jsonPayload.involvedObject.fieldPath
target.resource.attribute.labels [jsonpayload_involved_object_field_path]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.involvedObject.kind
target.resource.attribute.labels [jsonpayload_involved_object_kind]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.involvedObject.name
target.resource.attribute.labels [jsonpayload_involved_object_name]
If the
resource.type
log field value is equal to
k8s_cluster
, then the
jsonPayload.involvedObject.name
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
k8s_pod, k8s_cluster
jsonPayload.involvedObject.namespace
target.resource.attribute.labels [jsonpayload_involved_object_namespace]
k8s_pod, k8s_cluster
jsonPayload.involvedObject.resourceVersion
target.resource.attribute.labels [jsonpayload_involved_object_resourceVersion]
k8s_pod, k8s_cluster, k8s_node
jsonPayload.involvedObject.uid
target.resource.attribute.labels [jsonpayload_involved_object_uid]
k8s_container
labels.destination_service_name
target.resource.attribute.labels [labels_destination_service_name]
k8s_container
labels.k8s-pod/app
target.resource.attribute.labels [labels_k8s_pod_app]
k8s_container
labels.k8s-pod/k8s-app
target.resource.attribute.labels [labels_k8s_pod_k8s_app]
k8s_container
labels.k8s-pod/name
target.resource.attribute.labels [labels_k8s_pod_name]
k8s_container
labels.k8s-pod/clm_test
target.resource.attribute.labels [clm_test]
k8s_container
labels.log_sampled
target.resource.attribute.labels [labels_log_sampled]
k8s_container
labels.request_id
target.resource.attribute.labels [labels_request_id]
k8s_container
labels.response_flag
target.resource.attribute.labels [labels_response_flag]
k8s_container
labels.x_carbon_log_ext1
target.resource.attribute.labels [labels_x_carbon_log_ext1]
k8s_container
labels.gke.googleapis.com/log_type
target.resource.attribute.labels [log_type]
gke_cluster
protoPayload.metadata.operationType
target.resource.attribute.labels [metadata_operationType]
k8s_pod
labels.clouderrorreporting.googleapis.com/notification_trigger_error_ingestion_time
target.resource.attribute.labels [notification_trigger_error_ingestion_time]
k8s_pod
labels.notificationType
target.resource.attribute.labels [notification_type]
gke_cluster, audited_resource
protoPayload.request.name
target.resource.attribute.labels [proto_req_name]
k8s_cluster
protoPayload.request.metadata.name
target.resource.attribute.labels [protopayload_metadata_name]
k8s_cluster
protoPayload.request.metadata.resourceVersion
target.resource.attribute.labels [protopayload_metadata_resourceversion]
gke_cluster
protoPayload.request.cluster.binaryAuthorization.evaluationMode
target.resource.attribute.labels [protopayload_request_cluster_binary_auth_eval_mode]
audited_resource
protoPayload.request.contentType
target.resource.attribute.labels [protopayload_request_content_type]
k8s_cluster
protoPayload.request.kind
target.resource.attribute.labels [protopayload_request_kind]
gke_cluster
protoPayload.request.cluster.addonsConfig.gcePersistentDiskCsiDriverConfig.enabled
target.resource.attribute.labels [req_cls_addonsConfig_gcePersistentDiskCsiDriverConfig_enabled]
gke_cluster
protoPayload.request.cluster.releaseChannel.channel
target.resource.attribute.labels [req_cls_channel]
gke_cluster
protoPayload.request.cluster.enableKubernetesAlpha
target.resource.attribute.labels [req_cls_enableKubernetesAlpha]
gke_cluster
protoPayload.request.cluster.ipAllocationPolicy.stackType
target.resource.attribute.labels [req_cls_ipAllocationPolicy_stackType]
gke_cluster
protoPayload.request.cluster.addonsConfig.networkPolicyConfig.disabled
target.resource.attribute.labels [req_cls_policy_config_disabled]
gke_nodepool
protoPayload.request.nodePool.config.diskSizeGb
target.resource.attribute.labels [req_node_pool_config_diskSizeGb]
gke_nodepool
protoPayload.request.nodePool.config.diskType
target.resource.attribute.labels [req_node_pool_config_diskType]
gke_nodepool
protoPayload.request.nodePool.config.imageType
target.resource.attribute.labels [req_node_pool_config_imageType]
gke_nodepool
protoPayload.request.nodePool.config.machineType
target.resource.attribute.labels [req_node_pool_config_machineType]
gke_nodepool
protoPayload.request.nodePool.config.metadata.disable-legacy-endpoints
target.resource.attribute.labels [req_node_pool_config_metadata_disable_legacy_endpoints]
gke_nodepool
protoPayload.request.nodePool.config.oauthScopes
target.resource.attribute.labels [req_node_pool_config_oauth_scopes]
gke_nodepool
protoPayload.request.nodePool.networkConfig.enablePrivateNodes
target.resource.attribute.labels [req_node_pool_enable_private_nodes]
gke_nodepool
protoPayload.request.nodePool.initialNodeCount
target.resource.attribute.labels [req_node_pool_initial_node_cnt]
gke_nodepool
protoPayload.request.nodePool.management.autoRepair
target.resource.attribute.labels [req_node_pool_management_auto_repair]
gke_nodepool
protoPayload.request.nodePool.management.autoUpgrade
target.resource.attribute.labels [req_node_pool_management_auto_upgrade]
gke_nodepool
protoPayload.request.nodePool.upgradeSettings.maxSurge
target.resource.attribute.labels [req_node_pool_upgrade_settings_max_surge]
gke_nodepool
protoPayload.request.nodePool.upgradeSettings.strategy
target.resource.attribute.labels [req_node_pool_upgrade_settings_strategy]
gke_nodepool
protoPayload.request.nodePool.version
target.resource.attribute.labels [req_nodepool_version]
gke_cluster
protoPayload.request.cluster.ipAllocationPolicy.useIpAliases
target.resource.attribute.labels [requ_cls_ipAllocationPolicy_useIpAliases]
gke_cluster
protoPayload.request.cluster.networkConfig.datapathProvider
target.resource.attribute.labels [requ_cls_networkConfig_datapathProvider]
gke_cluster
protoPayload.request.cluster.nodePools.upgradeSettings.strategy
target.resource.attribute.labels [requ_cls_nodePools_upgradeSettings_strategy]
requested_server_name
target.resource.attribute.labels [requested_server_name]
gke_cluster
protoPayload.response.name
target.resource.attribute.labels [res_name]
gke_cluster
protoPayload.response.operationType
target.resource.attribute.labels [res_operation_type]
k8s_cluster
protoPayload.response.apiVersion
target.resource.attribute.labels [resp_api_version]
k8s_cluster
protoPayload.response.kind
target.resource.attribute.labels [resp_kind]
k8s_cluster
protoPayload.response.metadata.name
target.resource.attribute.labels [resp_metadata_name]
k8s_cluster
protoPayload.response.metadata.namespace
target.resource.attribute.labels [resp_metadata_namespace]
k8s_cluster
protoPayload.response.metadata.resourceVersion
target.resource.attribute.labels [resp_metadata_resource_version]
k8s_cluster
protoPayload.response.metadata.uid
target.resource.attribute.labels [resp_metadata_uid]
k8s_container
labels.response_details
target.resource.attribute.labels [response_details]
k8s_container
labels.route_name
target.resource.attribute.labels [route_name]
k8s_container
labels.k8s-pod/pod-template-hash
target.resource.attribute.labels [template_hash]
audited_resource
resource.labels.method
target.resource.attribute.labels [rc_method]
k8s_cluster
protoPayload.request.status.conditions.reason
target.resource.attribute.permissions.description
gke_cluster
protoPayload.request.cluster.name
target.resource.name
k8s_node
jsonPayload.node_name
target.resource.name
If the
resource.type
log field value is equal to
k8s_node
, then the
jsonPayload.node_name
log field is mapped to the
target.resource.name
UDM field.
k8s_container
jsonPayload.azureResourceID
target.resource.product_object_id
gke_cluster
protoPayload.response.targetLink
target.url
k8s_cluster
protoPayload.request.spec.leaseTransitions
target.user.attribute.labels [request_lease_transitions]
k8s_cluster
protoPayload.request.spec.holderIdentity
target.user.attribute.labels [request_spec_holderIdentity]
k8s_cluster
protoPayload.request.spec.renewTime
target.user.attribute.labels [request_spec_renew_time]
k8s_cluster
protoPayload.request.spec.resourceAttributes.group
target.user.attribute.labels [request_spec_resource_group]
k8s_cluster
protoPayload.request.spec.resourceAttributes.verb
target.user.attribute.labels [request_spec_resource_verb]
k8s_cluster
protoPayload.request.spec.resourceAttributes.version
target.user.attribute.labels [request_spec_resource_version]
k8s_cluster
protoPayload.request.spec.resourceAttributes.resource
target.user.attribute.labels [request_spec_resource]
k8s_cluster
protoPayload.request.spec.uid
target.user.attribute.labels [request_spec_uid]
k8s_cluster
protoPayload.request.spec.user
target.user.attribute.labels [request_spec_user]
k8s_cluster
protoPayload.request.spec.leaseDurationSeconds
target.user.attribute.labels [request_spec._ease_duration_sec]
k8s_cluster
protoPayload.request.status.allowed
target.user.attribute.labels [request_status_allowed]
k8s_cluster
protoPayload.response.spec.leaseTransitions
target.user.attribute.labels [res_lease_transitions]
k8s_cluster
protoPayload.response.spec.holderIdentity
target.user.attribute.labels [resp_spec_holderIdentity]
k8s_cluster
protoPayload.response.spec.leaseDurationSeconds
target.user.attribute.labels [resp_spec_lease_duration_sec]
k8s_cluster
protoPayload.response.spec.renewTime
target.user.attribute.labels [resp_spec_renew_time]
k8s_cluster
protoPayload.response.spec.resourceAttributes.group
target.user.attributes.labels [resp_resource_attributes_group]
k8s_cluster
protoPayload.response.spec.resourceAttributes.resource
target.user.attributes.labels [resp_resource_attributes_resource]
k8s_cluster
protoPayload.response.spec.resourceAttributes.verb
target.user.attributes.labels [resp_resource_attributes_verb]
k8s_cluster
protoPayload.response.spec.resourceAttributes.version
target.user.attributes.labels [resp_resource_attributes_version]
k8s_cluster
protoPayload.request.spec.groups
target.user.group_identifiers
k8s_cluster
protoPayload.response.spec.user
target.user.user_display_name
k8s_cluster
protoPayload.response.spec.uid
target.user.userid
k8s_cluster
jsonPayload.vulnerability.cveId
extensions.vulns.vulnerabilities.cve_id
k8s_cluster
jsonPayload.vulnerability.cvssScore
extensions.vulns.vulnerabilities.cvss_base_score
k8s_cluster
jsonPayload.vulnerability.cvssVector
extensions.vulns.vulnerabilities.cvss_vector
k8s_cluster
jsonPayload.vulnerability.description
extensions.vulns.vulnerabilities.description
k8s_cluster
jsonPayload.vulnerability.severity
extensions.vulns.vulnerabilities.severity
k8s_cluster
jsonPayload.vulnerability.severity
extensions.vulns.vulnerabilities.severity_details
k8s_cluster
jsonPayload.vulnerability.cpeUri
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_cpe_uri]
k8s_cluster
jsonPayload.vulnerability.fixedCpeUri
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_fixed_cpe_uri]
k8s_cluster
jsonPayload.vulnerability.relatedUrls
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_related_urls]
k8s_cluster
jsonPayload.vulnerability.packageName
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_package_name]
k8s_cluster
jsonPayload.vulnerability.packageType
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_package_type]
k8s_cluster
jsonPayload.vulnerability.fixedPackage
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_fixed_package]
k8s_cluster
jsonPayload.vulnerability.fixedPackageVersion
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_fixed_package_version]
k8s_cluster
jsonPayload.vulnerability.affectedImages
extensions.vulns.vulnerabilities.about.security_result.detection_fields [vulnerability_affected_images]
k8s_cluster
jsonPayload.vulnerability.affectedPackageVersion
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_affected_package_version]
generic_node
resource.labels.node_id
target.resource.product_object_id
generic_node
resource.labels.namespace
additional.fields[namespace]
generic_node
labels.bp_csoc
additional.fields[bp_csoc]
generic_node
labels.bp_env_id
additional.fields[bp_env_id]
generic_node
labels.chronicle_log_tag
additional.fields[chronicle_log_tag]
generic_node
labels.cloud.region
additional.fields[cloud.region]
generic_node
labels.host.name
additional.fields[host.name]
generic_node
labels.log.file.name
additional.fields[log.file.name]
generic_node
labels.log_type
additional.fields[log_type]
generic_node
labels.os.type
additional.fields[os.type]
k8s_container
jsonPayload.downstream_local_address
intermediary.ip
If the
resource.type
log field value is equal to
k8s_container
, then
ip_address
is extracted from the
jsonPayload.downstream_local_address
log field using a Grok pattern and mapped to the
intermediary.ip
UDM field.
k8s_container
jsonPayload.downstream_local_address
intermediary.port
If the
resource.type
log field value is equal to
k8s_container
, then
port
is extracted from the
jsonPayload.downstream_local_address
log field using a Grok pattern and mapped to the
intermediary.port
UDM field.
k8s_container
jsonPayload.response_code
network.http.response_code
If the
resource.type
log field value is equal to
k8s_container
,
and if the
jsonPayload.status
log field value is empty, then the
jsonPayload.response_code
log field is mapped to the
network.http.response_code
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
,
and if the
jsonPayload.status
log field value is
not
empty, then the
additional.fields.key
UDM field is set to
response_code
and the
jsonPayload.response_code
log field value is mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.upstream_local_address
additional.fields[upstream_local_address]
k8s_container
jsonPayload.start_time
additional.fields[start_time]
k8s_container
jsonPayload.downstream_remote_address
principal.ip
If the
resource.type
log field value is equal to
k8s_container
, then
ip_address
is extracted from the
jsonPayload.downstream_remote_address
log field using a Grok pattern and mapped to the
principal.ip
UDM field.
k8s_container
jsonPayload.downstream_remote_address
principal.port
If the
resource.type
log field value is equal to
k8s_container
and the UDM field
principal.port
is empty, then
port
is extracted from the
jsonPayload.downstream_remote_address
log field using a Grok pattern and mapped to the
principal.port
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the UDM field
principal.port
is
not
empty, then the
additional.fields.key
UDM field is set to
downstream_remote_address
and the
port
is extracted from the
jsonPayload.downstream_remote_address
log field using a Grok pattern and mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.upstream_host
target.ip
If the
resource.type
log field value is equal to
k8s_container
, then
ip_address
is extracted from the
jsonPayload.upstream_host
log field using a Grok pattern and mapped to the
target.ip
UDM field.
k8s_container
jsonPayload.upstream_host
target.port
If the
resource.type
log field value is equal to
k8s_container
and the UDM field
target.port
is empty, then
port
is extracted from the
jsonPayload.upstream_host
log field using a Grok pattern and mapped to the
target.port
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the UDM field
target.port
is
not
empty, then the
additional.fields.key
UDM field is set to
upstream_host
and the
port
is extracted from the
jsonPayload.upstream_host
log field using a Grok pattern and mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.duration
network.session_duration
k8s_container
jsonPayload.bytes_received
network.received_bytes
If the
resource.type
log field value is equal to
k8s_container
and the log field
bytes_received
is empty, then the
jsonPayload.bytes_received
log field is mapped to the
network.received_bytes
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the UDM field
received_bytes
is
not
empty, then the
additional.fields.key
UDM field is set to
bytes_received
and the
jsonPayload.bytes_received
log field value is mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.response_flags
security_result.detection_fields[response_flags]
k8s_container
jsonPayload.upstream_cluster
target.resource_ancestors.name
k8s_container
jsonPayload.upstream_cluster
target.resource_ancestors.resource_type
If the
resource.type
log field value is equal to
k8s_container
and the log field
jsonPayload.upstream_cluster
is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
k8s_container
jsonPayload.user_agent
network.http.user_agent
If the
resource.type
log field value is equal to
k8s_container
and the log field
jsonPayload.http_user_agent
is empty, then the
jsonPayload.user_agent
log field is mapped to the
network.http.user_agent
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the log field
jsonPayload.http_user_agent
is
not
empty, then the
additional.fields.key
UDM field is set to
user_agent
and the
jsonPayload.user_agent
log field value is mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.route_name
additional.fields[route_name]
k8s_container
jsonPayload.protocol
network.application_protocol
If the
resource.type
log field value is equal to
k8s_container
and the log field
jsonPayload.server_protocol
is empty, then the
jsonPayload.protocol
log field is mapped to the
network.application_protocol
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the log field
jsonPayload.server_protocol
is
not
empty, then the
additional.fields.key
UDM field is set to
protocol
and the
jsonPayload.protocol
log field value is mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.requested_server_name
network.tls.client.server_name
k8s_container
jsonPayload.method
network.http.method
If the
resource.type
log field value is equal to
k8s_container
and the UDM field
network.http.method
is empty, then the
jsonPayload.method
log field is mapped to the
network.http.method
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the UDM field
network.http.method
is
not
empty, then the
additional.fields.key
UDM field is set to
method
and the
jsonPayload.method
log field value is mapped to the
additional.fields.value.string_value
UDM field.
k8s_container
jsonPayload.response_code_details
additional.fields[response_code_details]
k8s_container
jsonPayload.x_forwarded_for
principal.ip
k8s_container
jsonPayload.upstream_service_time
additional.fields[upstream_service_time_ms]
k8s_container
jsonPayload.msg
metadata.description
k8s_container
jsonPayload.caller
additional.fields [caller]
k8s_container
jsonPayload.json.repo
about.resource.name
k8s_container
jsonPayload.json.pull
about.resource.attribute.labels [pull]
k8s_container
jsonPayload.requested_server_name
target.hostname
If the
resource.type
log field value is equal to
k8s_container
and the log field
labels.destination_service_host
is empty, then the
jsonPayload.requested_server_name
log field is mapped to the
target.hostname
UDM field.
Else, if the
resource.type
log field value is equal to
k8s_container
and the UDM field
destination_service_host
is
not
empty, then the
jsonPayload.requested_server_name
log field is mapped to the
network.tls.client.server_name
UDM field.
k8s_container
jsonPayload.system
target.url
k8s_container
jsonPayload.source
principal.ip
k8s_container
jsonPayload.auditType.actionI18nKey
additional.fields[actionI18nKey]
k8s_container
jsonPayload.auditType.category
security_result.category_details
k8s_container
jsonPayload.auditType.categoryI18nKey
security_result.category_details
k8s_container
jsonPayload.auditType.level
additional.fields[level]
k8s_container
jsonPayload.auditType.action
additional.fields[action]
k8s_container
jsonPayload.auditType.area
additional.fields[area]
k8s_container
jsonPayload.date
additional.fields[date]
k8s_container
jsonPayload.affectedObjects
security_result.detection_fields
If the
jsonPayload.affectedObjects
log field value is
not
empty
then,
Iterate through log field
jsonPayload.affectedObjects
, then
security_result.detection_fields.key
UDM field is set to
affected_object_%{index}_type
and
security_result.detection_fields.value
is mapped to the
value.type
log field
and
security_result.detection_fields.key
UDM field is set to
affected_object_%{index}_name
and
security_result.detection_fields.value
is mapped to the
value.name
log field.
What's next
Data ingestion to Google SecOps
Need more help?
Get answers from Community members and Google SecOps professionals.
