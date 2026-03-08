# Collect Cloud Load Balancing logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-loadbalancing/  
**Scraped:** 2026-03-05T09:17:18.526184Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cloud Load Balancing logs
Supported in:
Google secops
SIEM
This document describes how you can collect Cloud Load Balancing logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields map to Google Security Operations Unified Data Model (UDM) fields.
This document also lists the supported Cloud Load Balancing version.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Cloud Load Balancing logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Cloud Load Balancing logs
: The Cloud Load Balancing logs that are
enabled for ingestion to Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Cloud Load Balancing.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_LOADBALANCING
ingestion label.
Before you begin
Ensure that you are using Cloud Load Balancing version 1.
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Configure Google Cloud to ingest Cloud Load Balancing logs
To ingest Cloud Load Balancing logs to Google Security Operations, follow the steps on the
Ingest Google Cloud logs to Google Security Operations
page.
If you encounter issues when you ingest Cloud Load Balancing logs,
contact Google Security Operations support
.
Supported Google Cloud Load Balancing log formats
The Google Cloud Load Balancing parser supports logs in JSON format.
Supported Google Cloud Load Balancing sample logs
JSON:
{
  "httpRequest": {
    "latency": "0.058927s",
    "referer": "http://dummy_referer/console/",
    "remoteIp": "198.51.100.1",
    "requestMethod": "GET",
    "requestSize": "257",
    "requestUrl": "https://34.1.0.35/console/",
    "responseSize": "1467",
    "status": 302,
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/192.168.51.1 Safari/537.36"
  },
  "insertId": "1vzs264g1u90hp5",
  "jsonPayload": {
    "@type": "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry",
    "statusDetails": "handled_by_identity_aware_proxy"
  },
  "logName": "projects/prj-p-shared-base-327317/logs/requests",
  "receiveTimestamp": "2022-01-11T13:01:35.721191239Z",
  "resource": {
    "labels": {
      "backend_service_name": "dummy-service",
      "forwarding_rule_name": "fe-p-siemplify-01",
      "project_id": "dummyproject_id",
      "target_proxy_name": "dummy-proxy",
      "url_map_name": "dummy-url",
      "zone": "global"
    },
    "type": "http_load_balancer"
  },
  "severity": "INFO",
  "spanId": "9ced8a16edbf8818",
  "timestamp": "2022-01-11T13:01:34.487354Z",
  "trace": "projects/prj-p-shared-base-327317/traces/82254a9f2b743f83c0c0543c0ece2b1a"
}
Field mapping reference
This section explains how the Google Security Operations parser maps Google Cloud Load Balancing fields to Google Security Operations Unified Data Model (UDM) fields.
Field mapping reference: GCP_LOADBALANCING log fields to UDM fields
The following table lists the log fields of the
GCP_LOADBALANCING
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
receiveTimestamp
metadata.collected_timestamp
timestamp
metadata.event_timestamp
metadata.event_type
If the following values are
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
httpRequest.remoteIp
jsonPayload.remoteIp
jsonPayload.connection.clientIp
jsonPayload.clientInstance.vmIp
httpRequest.serverIp
jsonPayload.connection.serverIp
jsonPayload.serverInstance.vmIp
Else, if the following values are
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UNCATEGORIZED
.
httpRequest.remoteIp
jsonPayload.remoteIp
jsonPayload.connection.clientIp
jsonPayload.clientInstance.vmIp
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
logName
metadata.product_event_type
insertId
metadata.product_log_id
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP Load Balancing
.
httpRequest.protocol
network.application_protocol
If the
httpRequest.requestUrl
log field value matches the regular expression
https
or the
httpRequest.protocol
log field value matches the regular expression
HTTPS
, then the
network.application_protocol
UDM field is set to
HTTPS
.
Else, if the
httpRequest.requestUrl
log field value matches the regular expression
http
or the
httpRequest.protocol
log field value matches the regular expression
HTTP
, then the
network.application_protocol
UDM field is set to
HTTP
.
jsonPayload.clientLocation.asn
network.asn
httpRequest.requestMethod
network.http.method
httpRequest.referer
network.http.referral_url
httpRequest.status
network.http.response_code
httpRequest.userAgent
network.http.user_agent
jsonPayload.connection.protocol
network.ip_protocol
If the
jsonPayload.connection.protocol
log field value is equal to
0
, then the
network.ip_protocol
UDM field is set to
UNKNOWN_IP_PROTOCOL
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
1
, then the
network.ip_protocol
UDM field is set to
ICMP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
2
, then the
network.ip_protocol
UDM field is set to
IGMP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
6
, then the
network.ip_protocol
UDM field is set to
TCP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
17
, then the
network.ip_protocol
UDM field is set to
UDP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
41
, then the
network.ip_protocol
UDM field is set to
IP6IN4
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
47
, then the
network.ip_protocol
UDM field is set to
GRE
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
50
, then the
network.ip_protocol
UDM field is set to
ESP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
58
, then the
network.ip_protocol
UDM field is set to
ICMP6
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
88
, then the
network.ip_protocol
UDM field is set to
EIGRP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
97
, then the
network.ip_protocol
UDM field is set to
ETHERIP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
103
, then the
network.ip_protocol
UDM field is set to
PIM
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
112
, then the
network.ip_protocol
UDM field is set to
VRRP
.
Else, if the
jsonPayload.connection.protocol
log field value is equal to
132
, then the
network.ip_protocol
UDM field is set to
SCTP
.
httpRequest.responseSize
network.received_bytes
jsonPayload.bytesReceived
network.received_bytes
jsonPayload.packetsReceived
network.received_packets
httpRequest.requestSize
network.sent_bytes
jsonPayload.packetsSent
network.sent_packets
jsonPayload.bytesSent
network.sent_packets
jsonPayload.rtt
network.session_duration.seconds
Grok: Extracted
sec
from the log field
jsonPayload.rtt
and mapped it to the
network.session_duration.seconds
UDM field.
jsonPayload.rtt
network.session_duration.nanos
Grok: Extracted
nano
from the log field
jsonPayload.rtt
and mapped it to the
network.session_duration.nanos
UDM field.
jsonPayload.tls.cipher
network.tls.cipher
jsonPayload.securityPolicyRequestData.tlsJa3Fingerprint
network.tls.client.ja3
jsonPayload.securityPolicyRequestData.tlsJa4Fingerprint
additional.fields[tlsJa4Fingerprint]
jsonPayload.tls.protocol
network.tls.next_protocol
httpRequest.remoteIp
principal.ip
If the
httpRequest.remoteIp
log field value is
not
empty, then
Grok: Extracted
ip
and
port
from the log field
httpRequest.remoteIp
and mapped it to the
principal.ip
and
principal.port
UDM field respectively.
jsonPayload.remoteIp
principal.ip
If the
jsonPayload.remoteIp
log field value is
not
empty, then
Grok: Extracted
ip
and
port
from the log field
jsonPayload.remoteIp
and mapped it to the
principal.ip
and
principal.port
UDM field respectively.
jsonPayload.connection.clientIp
principal.ip
clientInstance.vmIp
principal.ip
jsonPayload.clientLocation.city
principal.location.city
jsonPayload.clientLocation.regionCode
principal.location.country_or_region
jsonPayload.securityPolicyRequestData.remoteIpInfo.regionCode
principal.location.name
jsonPayload.clientLocation.subRegion
principal.location.state
jsonPayload.connection.clientPort
principal.port
jsonPayload.clientGkeDetails.cluster.clusterLocation
principal.resource_ancestors.attribute.cloud.availability_zone
jsonPayload.clientVpc.projectId
principal.resource_ancestors.name
jsonPayload.clientVpc.vpc
principal.resource_ancestors.name
jsonPayload.clientVpc.subnetwork
principal.resource_ancestors.name
jsonPayload.clientGkeDetails.cluster.cluster
principal.resource_ancestors.name
jsonPayload.clientGkeDetails.pod.pod
principal.resource_ancestors.name
jsonPayload.clientGkeDetails.service.service
principal.resource_ancestors.name
jsonPayload.clientInstance.projectId
principal.resource_ancestors.product_object_id
principal.resource_ancestors.resource_subtype
If the
jsonPayload.clientVpc.projectId
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
clientVpc_projectId
.
If the
jsonPayload.clientVpc.vpc
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
clientVpc_vpc
.
If the
jsonPayload.clientVpc.subnetwork
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
clientVpc_subnetwork
.
If the
jsonPayload.clientGkeDetails.cluster.cluster
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
clientGkeDetails_cluster
.
If the
jsonPayload.clientGkeDetails.pod.pod
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
clientGkeDetails_pod
.
If the
jsonPayload.clientGkeDetails.service.service
log field value is
not
empty, then the
principal.resource_ancestors.resource_subtype
UDM field is set to
clientGkeDetails_service
.
principal.resource_ancestors.resource_type
If the
jsonPayload.clientVpc.projectId
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
If the
jsonPayload.clientVpc.vpc
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.clientVpc.subnetwork
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.clientGkeDetails.cluster.cluster
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
If the
jsonPayload.clientGkeDetails.pod.pod
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.clientGkeDetails.service.service
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
BACKEND_SERVICE
.
jsonPayload.clientInstance.zone
principal.resource.attribute.cloud.availability_zone
jsonPayload.clientInstance.vm
principal.resource.name
principal.resource.resource_subtype
If the
jsonPayload.clientInstance.vm
log field value is
not
empty, then the
principal.resource.resource_subtype
UDM field is set to
client_instance_vm
.
principal.resource.resource_type
If the
jsonPayload.clientInstance.vm
log field value is
not
empty, then the
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
security_result.action
If the
jsonPayload.enforcedSecurityPolicy.configuredAction
log field value is equal to
DENY
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
jsonPayload.enforcedSecurityPolicy.configuredAction
log field value is equal to
ALLOW
, then the
security_result.action
UDM field is set to
ALLOW
.
If the
jsonPayload.previewSecurityPolicy.configuredAction
log field value is equal to
DENY
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
jsonPayload.previewSecurityPolicy.configuredAction
log field value is equal to
ALLOW
, then the
security_result.action
UDM field is set to
ALLOW
.
If the
jsonPayload.enforcedEdgeSecurityPolicy.configuredAction
log field value is equal to
DENY
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
jsonPayload.enforcedEdgeSecurityPolicy.configuredAction
log field value is equal to
ALLOW
, then the
security_result.action
UDM field is set to
ALLOW
.
If the
jsonPayload.previewEdgeSecurityPolicy.configuredAction
log field value is equal to
DENY
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
jsonPayload.previewEdgeSecurityPolicy.configuredAction
log field value is equal to
ALLOW
, then the
security_result.action
UDM field is set to
ALLOW
.
jsonPayload.enforcedSecurityPolicy.configuredAction
security_result.action_details
jsonPayload.previewSecurityPolicy.configuredAction
security_result.action_details
jsonPayload.enforcedEdgeSecurityPolicy.configuredAction
security_result.action_details
jsonPayload.previewEdgeSecurityPolicy.configuredAction
security_result.action_details
jsonPayload.enforcedSecurityPolicy.outcome
security_result.outcomes[jsonpayload_enforcedsecuritypolicy_outcome]
jsonPayload.enforcedSecurityPolicy.priority
security_result.priority_details
jsonPayload.previewSecurityPolicy.priority
security_result.priority_details
jsonPayload.enforcedEdgeSecurityPolicy.priority
security_result.priority_details
jsonPayload.previewEdgeSecurityPolicy.priority
security_result.priority_details
jsonPayload.enforcedSecurityPolicy.name
security_result.rule_name
jsonPayload.securityPolicyRequestData.recaptchaActionToken.score
security_result.risk_score
If the
jsonPayload.securityPolicyRequestData.recaptchaActionToken.score
log field value is
not
empty, then the
jsonPayload.securityPolicyRequestData.recaptchaActionToken.score
log field is mapped to the
security_result.risk_score
UDM field.
jsonPayload.securityPolicyRequestData.recaptchaSessionToken.score
security_result.risk_score
If the
jsonPayload.securityPolicyRequestData.recaptchaSessionToken.score
log field value is
not
empty, then the
jsonPayload.securityPolicyRequestData.recaptchaSessionToken.score
log field is mapped to the
security_result.risk_score
UDM field.
jsonPayload.previewSecurityPolicy.name
security_result.rule_name
jsonPayload.enforcedEdgeSecurityPolicy.name
security_result.rule_name
jsonPayload.previewEdgeSecurityPolicy.name
security_result.rule_name
security_result.severity
If the
severity
log field value matches the regular expression
DEFAULT or DEBUG or INFO or NOTICE
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
severity
log field value matches the regular expression
WARNING or ERROR
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value matches the regular expression
CRITICAL or ALERT or EMERGENCY
, then the
security_result.severity
UDM field is set to
HIGH
.
severity
security_result.severity_details
jsonPayload.statusDetails
security_result.summary
jsonPayload.proxyStatus
security_result.summary
resource.labels.backend_service_name
target.application
resource.labels.backend_name
target.group.group_display_name
resource.labels.backend_group_name
target.group.group_display_name
httpRequest.serverIp
target.ip
jsonPayload.connection.serverIp
target.ip
serverInstance.vmIp
target.ip
jsonPayload.connection.serverPort
target.port
resource.labels.backend_scope
target.resource_ancestors.attribute.cloud.availability_zone
If the
resource.labels.backend_target_name
log field value is
not
empty, then the
resource.labels.backend_scope
log field is mapped to the
target.resource_ancestors.attribute.cloud.availability_zone
UDM field.
jsonPayload.serverInstance.zone
target.resource_ancestors.attribute.cloud.availability_zone
If the
jsonPayload.serverInstance.vm
log field value is
not
empty, then the
jsonPayload.serverInstance.zone
log field is mapped to the
target.resource_ancestors.attribute.cloud.availability_zone
UDM field.
jsonPayload.serverGkeDetails.cluster.clusterLocation
target.resource_ancestors.attribute.cloud.availability_zone
If the
jsonPayload.serverGkeDetails.cluster.cluster
log field value is
not
empty, then the
jsonPayload.serverGkeDetails.cluster.clusterLocation
log field is mapped to the
target.resource_ancestors.attribute.cloud.availability_zone
UDM field.
resource.labels.backend_zone
target.resource_ancestors.attribute.cloud.availability_zone
If the
resource.labels.backend_zone
log field value is
not
empty, then the
resource.labels.backend_zone
log field is mapped to the
target.resource_ancestors.attribute.cloud.availability_zone
UDM field.
resource.labels.backend_target_name
target.resource_ancestors.name
jsonPayload.serverInstance.vm
target.resource_ancestors.name
jsonPayload.serverGkeDetails.cluster.cluster
target.resource_ancestors.name
jsonPayload.serverGkeDetails.pod.pod
target.resource_ancestors.name
jsonPayload.serverGkeDetails.service.service
target.resource_ancestors.name
resource.labels.network_name
target.resource_ancestors.name
resource.labels.project_id
target.resource_ancestors.product_object_id
jsonPayload.serverInstance.projectId
target.resource_ancestors.product_object_id
If the
jsonPayload.serverInstance.vm
log field value is
not
empty, then the
jsonPayload.serverInstance.projectId
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field.
resource.labels.project
target.resource_ancestors.product_object_id
resource.labels.backend_target_type
target.resource_ancestors.resource_subtype
If the
resource.labels.backend_target_name
log field value is
not
empty, then the
resource.labels.backend_target_type
log field is mapped to the
target.resource_ancestors.resource_subtype
UDM field.
If the
jsonPayload.serverInstance.vm
log field value is
not
empty, then the
target.resource_ancestors.resource_subtype
UDM field is set to
serverInstance_vm
.
If the
jsonPayload.serverGkeDetails.cluster.cluster
log field value is
not
empty, then the
target.resource_ancestors.resource_subtype
UDM field is set to
serverGkeDetails_cluster
.
If the
jsonPayload.serverGkeDetails.pod.pod
log field value is
not
empty, then the
target.resource_ancestors.resource_subtype
UDM field is set to
serverGkeDetails_pod
.
If the
jsonPayload.serverGkeDetails.service.service
log field value is
not
empty, then the
target.resource_ancestors.resource_subtype
UDM field is set to
serverGkeDetails_service
.
If the
resource.labels.network_name
log field value is
not
empty, then the
target.resource_ancestors.resource_subtype
UDM field is set to
network_name
.
target.resource_ancestors.resource_type
If the
resource.labels.backend_target_name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
BACKEND_SERVICE
.
If the
jsonPayload.serverInstance.vm
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.serverGkeDetails.cluster.cluster
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
If the
jsonPayload.serverGkeDetails.pod.pod
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
jsonPayload.serverGkeDetails.service.service
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
BACKEND_SERVICE
.
If the
resource.labels.network_name
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
resource.labels.region
target.resource.attribute.cloud.availability_zone
resource.labels.endpoint_zone
target.resource.attribute.cloud.availability_zone
resource.labels.zone
target.resource.attribute.cloud.availability_zone
target.resource.attribute.cloud.environment
The
target.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.labels.load_balancer_name
target.resource.name
resource.type
target.resource.resource_subtype
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
DEVICE
.
httpRequest.requestUrl
target.url
jsonPayload.backendTargetProjectNumber
about.labels[backend_target_project_number]
(deprecated)
jsonPayload.backendTargetProjectNumber
additional.fields[backend_target_project_number]
jsonPayload.cacheDecision
about.labels[cache_decision]
jsonPayload.cacheId
about.labels[cache_id]
(deprecated)
jsonPayload.cacheId
additional.fields[cache_id]
jsonPayload.endTime
about.labels[end_time]
(deprecated)
jsonPayload.endTime
additional.fields[end_time]
jsonPayload.@type
about.labels[metadata_type]
(deprecated)
jsonPayload.@type
additional.fields[metadata_type]
spanId
about.labels[span_id]
(deprecated)
spanId
additional.fields[span_id]
jsonPayload.startTime
about.labels[start_time]
(deprecated)
jsonPayload.startTime
additional.fields[start_time]
traceSampled
about.labels[trace_sampled]
(deprecated)
traceSampled
additional.fields[trace_sampled]
trace
about.labels[trace]
(deprecated)
trace
additional.fields[trace]
jsonPayload.clientLocation.continent
principal.labels[client_loacation_continent]
(deprecated)
jsonPayload.clientLocation.continent
additional.fields[client_loacation_continent]
jsonPayload.networkTier.networkTier
principal.labels[network_tier]
(deprecated)
jsonPayload.networkTier.networkTier
additional.fields[network_tier]
jsonPayload.clientGkeDetails.pod.podNamespace
principal.resource_ancestors.attribute.labels[pod_namespace]
jsonPayload.clientGkeDetails.service.serviceNamespace
principal.resource_ancestors.attribute.labels[service_namespace]
jsonPayload.clientInstance.region
principal.resource.attribute.labels[client_instance_region]
resource.labels.forwarding_rule_name
security_result.rule_labels[forwarding_rule_name]
jsonPayload.enforcedSecurityPolicy.matchedFieldName
security_result.rule_labels[matched_field_name]
jsonPayload.enforcedSecurityPolicy.matchedFieldType
security_result.rule_labels[matched_field_type]
jsonPayload.enforcedSecurityPolicy.matchedFieldValue
security_result.rule_labels[matched_field_value]
jsonPayload.enforcedSecurityPolicy.matchedLength
security_result.rule_labels[matched_length]
jsonPayload.enforcedSecurityPolicy.preconfiguredExprIds
security_result.rule_labels[preconfigured_expr_ids]
jsonPayload.enforcedSecurityPolicy.threatIntelligence.categories
security_result.rule_labels[threat_intelligence_category]
resource.labels.backend_group_scope
target.group.attribute.labels[backend_group_scope]
resource.labels.backend_group_type
target.group.attribute.labels[backend_group_type]
resource.labels.backend_type
target.group.attribute.labels[backend_type]
resource.labels.forwarding_rule_network_tier
target.labels[forwarding_rule_network_tier]
(deprecated)
resource.labels.forwarding_rule_network_tier
additional.fields[forwarding_rule_network_tier]
httpRequest.cacheFillBytes
target.labels[http_request_cache_fill_bytes]
(deprecated)
httpRequest.cacheFillBytes
additional.fields[http_request_cache_fill_bytes]
httpRequest.cacheHit
target.labels[http_request_cache_hit]
(deprecated)
httpRequest.cacheHit
additional.fields[http_request_cache_hit]
httpRequest.cacheLookup
target.labels[http_request_cache_lookup]
(deprecated)
httpRequest.cacheLookup
additional.fields[http_request_cache_lookup]
httpRequest.cacheValidatedWithOriginServer
target.labels[http_request_cache_validated_with_origin_server]
(deprecated)
httpRequest.cacheValidatedWithOriginServer
additional.fields[http_request_cache_validated_with_origin_server]
httpRequest.latency
target.labels[http_request_latency]
(deprecated)
httpRequest.latency
additional.fields[http_request_latency]
resource.labels.primary_target_pool
target.labels[primary_target_pool]
(deprecated)
resource.labels.primary_target_pool
additional.fields[primary_target_pool]
resource.labels.target_pool
target.labels[target_pool]
(deprecated)
resource.labels.target_pool
additional.fields[target_pool]
resource.labels.target_proxy_name
target.labels[target_proxy_name]
(deprecated)
resource.labels.target_proxy_name
additional.fields[target_proxy_name]
resource.labels.url_map_name
target.labels[url_map_name]
(deprecated)
resource.labels.url_map_name
additional.fields[url_map_name]
resource.labels.backend_failover_configuration
target.resource_ancestors.attribute.labels[backend_failover_configuration]
resource.labels.backend_network_name
target.resource_ancestors.attribute.labels[backend_network_name]
resource.labels.backend_scope_type
target.resource_ancestors.attribute.labels[backend_scope_type]
resource.labels.backend_subnetwork_name
target.resource_ancestors.attribute.labels[backend_subnetwork_name]
jsonPayload.serverInstance.region
target.resource_ancestors.attribute.labels[client_instance_region]
jsonPayload.serverGkeDetails.pod.podNamespace
target.resource_ancestors.attribute.labels[pod_namespace]
jsonPayload.serverGkeDetails.service.serviceNamespace
target.resource_ancestors.attribute.labels[service_namespace]
resource.labels.matched_url_path_rule
target.resource.attribute.labels[matched_url_path_rule]
resource.labels.loadbalancing_scheme_name
target.resource.attribute.labels[loadbalancing_scheme_name]
jsonPayload.enforcedSecurityPolicy.rateLimitAction.key
security_result.rule_labels[enforcedsecuritypolicy_ratelimitaction_key]
jsonPayload.enforcedSecurityPolicy.rateLimitAction.outcome
security_result.rule_labels[enforcedsecuritypolicy_ratelimitaction_outcome]
jsonPayload.enforcedSecurityPolicy.adaptiveProtection.autoDeployAlertId
security_result.rule_labels[adaptiveprotection_autodeployalertid]
jsonPayload.previewSecurityPolicy.rateLimitAction.key
security_result.rule_labels[previewsecuritypolicy_ratelimitaction_key]
jsonPayload.previewSecurityPolicy.rateLimitAction.outcome
security_result.rule_labels[previewsecuritypolicy_ratelimitaction_outcome]
jsonPayload.previewSecurityPolicy.outcome
security_result.outcomes[previewsecuritypolicy_outcome]
jsonPayload.previewSecurityPolicy.preconfiguredExprIds
security_result.rule_labels[previewsecuritypolicy_preconfigured_expr_ids]
jsonPayload.enforcedEdgeSecurityPolicy.outcome
security_result.outcomes[enforcededgesecuritypolicy_outcome]
jsonPayload.previewEdgeSecurityPolicy.outcome
security_result.outcomes[previewedgesecuritypolicy_outcome]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
