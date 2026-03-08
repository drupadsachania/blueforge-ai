# Collect Compute Engine context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/collect-compute-context-logs/  
**Scraped:** 2026-03-05T09:22:33.124241Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Compute Engine context logs
This document describes how fields of Compute Engine context logs map to Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
GCP_COMPUTE_CONTEXT
ingestion label.
For information about other context parsers that Google SecOps supports, see
Google SecOps context parsers
.
Supported Compute Engine log formats
The Compute Engine parser supports logs in JSON format.
Supported Compute Engine sample logs
JSON:
{
  "name": "//compute.googleapis.com/projects/cbnp-197-is-33543/regions/us-central1/forwardingRules/http",
  "assetType": "compute.googleapis.com/ForwardingRule",
  "resource": {
    "version": "v1",
    "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/compute/v1/rest",
    "discoveryName": "ForwardingRule",
    "parent": "//cloudresourcemanager.googleapis.com/projects/935379092450",
    "data": {
      "IPAddress": "198.51.100.0",
      "IPProtocol": "TCP",
      "creationTimestamp": "2023-05-16T03:04:12.424-07:00",
      "description": "",
      "fingerprint": "dummyfingerprint",
      "id": "1771600259555716083",
      "labelFingerprint": "42WmSpB8rSM=",
      "loadBalancingScheme": "EXTERNAL",
      "name": "http",
      "networkTier": "STANDARD",
      "portRange": "80-80",
      "region": "https://www.googleapis.com/compute/v1/projects/cbnp-197-is-33543/regions/us-central1",
      "selfLink": "https://www.googleapis.com/compute/v1/projects/cbnp-197-is-33543/regions/us-central1/forwardingRules/http",
      "target": "https://www.googleapis.com/compute/v1/projects/cbnp-197-is-33543/regions/us-central1/targetPools/lb1"
    }
  },
  "ancestors": [
    "projects/935379092450",
    "folders/934037626760",
    "organizations/595779152576"
  ]
}
Field mapping reference
The following table explains how the Google SecOps parser maps Compute Engine context logs fields to Google SecOps Unified Data Model (UDM) fields.
Log field
UDM mapping
Logic
metadata.entity_type
The
metadata.entity_type
UDM field is set to
ASSET
.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP Compute Context
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
entity.asset.attribute.cloud.environment
The
entity.asset.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.discoveryDocumentUri
entity.asset.attribute.labels[discovery_document]
resource.discoveryName
entity.asset.attribute.labels[discovery_name]
name
entity.resource.name
assetType
entity.asset.category
resource.version
metadata.product_version
resource.parent
entity.asset.attribute.labels[parent]
resource.data.serviceName
entity.application
resource.data.cpuPlatform
entity.asset.hardware.cpu_platform
resource.data.minCpuPlatform
entity.asset.attribute.labels[min_cpu_platform]
resource.data.properties.minCpuPlatform
entity.asset.attribute.labels[min_cpu_platform]
resource.data.host
entity.asset.attribute.labels[host]
resource.data.hostname
entity.hostname
resource.data.IPAddress
entity.ip
resource.data.region
entity.asset.location.name
resource.data.protocol
entity.network.application_protocol
If the
resource.data.protocol
log field value is equal to
HTTP
then, the
entity.network.application_protocol
UDM field is set to
HTTP
.
Else, If
resource.data.protocol
log field value is equal to
HTTPS
or the
resource.data.protocol
log field value is equal to
HTTP2
then, the
entity.network.application_protocol
UDM field is set to
HTTPS
.
Else, If
resource.data.protocol
log field value is equal to
GRPC
then, the
entity.network.application_protocol
UDM field is set to
RPC
.
resource.data.direction
entity.network.direction
If the
resource.data.direction
log field value is equal to
INGRESS
then, the
entity.network.direction
UDM field is set to
INBOUND
.
Else, If
resource.data.direction
log field value is equal to
EGRESS
then, the
entity.network.direction
UDM field is set to
OUTBOUND
.
Else
resource.data.direction
log field is mapped to the
entity.asset.attribute.labels.direction
UDM field.
resource.data.filter.direction
entity.network.direction
If the
resource.data.filter.direction
log field value is equal to
INGRESS
then, the
entity.network.direction
UDM field is set to
INBOUND
.
Else, If
resource.data.filter.direction
log field value is equal to
EGRESS
then, the
entity.network.direction
UDM field is set to
OUTBOUND
.
Else
resource.data.filter.direction
log field is mapped to the
entity.asset.attribute.labels.filter_direction
UDM field.
resource.data.IPProtocol
entity.network.ip_protocol
If the
resource.data.IPProtocol
log field value is equal to
TCP
then, the
entity.network.ip_protocol
UDM field is set to
TCP
.
Else, If
resource.data.IPProtocol
log field value is equal to
UDP
then, the
entity.network.ip_protocol
UDM field is set to
UDP
.
Else, If
resource.data.IPProtocol
log field value is equal to
ESP
then, the
entity.network.ip_protocol
UDM field is set to
ESP
.
Else, If
resource.data.IPProtocol
log field value is equal to
SCTP
then, the
entity.network.ip_protocol
UDM field is set to
SCTP
.
Else, If
resource.data.IPProtocol
log field value is equal to
ICMP
then, the
entity.network.ip_protocol
UDM field is set to
ICMP
.
Else, If
resource.data.IPProtocol
log field value is equal to
UDP
then, the
entity.network.ip_protocol
UDM field is set to
UDP
.
resource.data.protocol
entity.network.ip_protocol
If the
resource.data.protocol
log field value is equal to
TCP
then, the
entity.network.ip_protocol
UDM field is set to
TCP
.
Else, If
resource.data.IPProtocol
log field value is equal to
UDP
then, the
entity.network.ip_protocol
UDM field is set to
UDP
.
resource.data.minTlsVersion
entity.network.tls.version
resource.data.port
entity.port
ancestors
entity.asset.attribute.labels[ancestors]
resource.data.parent
entity.asset.attribute.labels[data_parent]
bucketName
entity.asset.attribute.labels[bucket_name]
resource.data.distributionPolicy.zones.zone
entity.asset.attribute.labels[distribution_policy_zone]
Iterate through
resource.data.distributionPolicy.zones.zone
,
If the
resource.data.distributionPolicy.zones.zone
log field value is
not
empty then,
resource.data.distributionPolicy.zones.zone
log field is mapped to the
entity.asset.attribute.labels.distribution_policy
zone
%{index}
UDM field.
resource.data.usageExportLocation.bucketName
entity.asset.attribute.labels[usage_export_location_bucket_name]
resource.data.creationTimestamp
entity.asset.attribute.creation_time
resource.data.accelerators.acceleratorCount
entity.asset.attribute.labels[accelerator_count]
Iterate through
resource.data.accelerators
,
If the
resource.data.accelerators.acceleratorCount
log field value is
not
empty then,
resource.data.accelerators.acceleratorCount
log field is mapped to the
entity.asset.attribute.labels.accelerator
count
%{index}
UDM field.
resource.data.accelerators.acceleratorType
entity.asset.attribute.labels[accelerator_type]
Iterate through
resource.data.accelerators
,
If the
resource.data.accelerators.acceleratorType
log field value is
not
empty then,
resource.data.accelerators.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.accelerator
type
%{index}
UDM field.
resource.data.adaptiveProtectionConfig.layer7DdosDefenseConfig.enable
entity.asset.attribute.labels[adaptive_protection_config_layer_7ddos_defense_config_enable]
resource.data.adaptiveProtectionConfig.layer7DdosDefenseConfig.ruleVisibility
entity.asset.attribute.labels[adaptive_protection_config_layer_7ddos_defense_config_rule_visibility]
resource.data.addressType
entity.asset.attribute.labels[address_type]
resource.data.adminEnabled
entity.asset.attribute.labels[admin_enabled]
resource.data.advancedOptionsConfig.jsonCustomConfig.contentTypes
entity.asset.attribute.labels[advanced_options_config_json_custom_config_content_types]
Iterate through
resource.data.advancedOptionsConfig.jsonCustomConfig.contentTypes
,
If the
resource.data.advancedOptionsConfig.jsonCustomConfig.contentTypes
log field value is
not
empty then,
resource.data.advancedOptionsConfig.jsonCustomConfig.contentTypes
log field is mapped to the
entity.asset.attribute.labels.advanced_options_config_json_custom_config_content
types
%{index}
UDM field.
resource.data.advancedOptionsConfig.jsonParsing
entity.asset.attribute.labels[advanced_options_config_json_parsing]
resource.data.advancedOptionsConfig.logLevel
entity.asset.attribute.labels[advanced_options_config_log_level]
resource.data.appEngine.service
entity.asset.attribute.labels[app_engine_service]
resource.data.appEngine.urlMask
entity.asset.attribute.labels[app_engine_url_mask]
resource.data.appEngine.version
entity.asset.attribute.labels[app_engine_version]
resource.data.architecture
entity.asset.attribute.labels[architecture]
resource.data.assuredCount
entity.asset.attribute.labels[assured_count]
resource.data.autoCreated
entity.asset.attribute.labels[auto_created]
resource.data.autoRenew
entity.asset.attribute.labels[auto_renew]
resource.data.autoscalingPolicy.maxNodes
entity.asset.attribute.labels[autoscaling_policy_max_nodes]
resource.data.autoscalingPolicy.minNodes
entity.asset.attribute.labels[autoscaling_policy_min_nodes]
resource.data.autoscalingPolicy.mode
entity.asset.attribute.labels[autoscaling_policy_mode]
resource.data.bandwidth
entity.asset.attribute.labels[bandwidth]
resource.data.candidateSubnets
entity.asset.attribute.labels[candidate_subnet]
Iterate through
resource.data.candidateSubnets
,
If the
resource.data.candidateSubnets
log field value is
not
empty then,
resource.data.candidateSubnets
log field is mapped to the
entity.asset.attribute.labels.candidate
subnet
%{index}
UDM field.
resource.data.category
entity.asset.attribute.labels[category]
resource.data.certificateMap
entity.asset.attribute.labels[certificate_map]
resource.data.certificate
entity.asset.attribute.labels[certificate]
resource.data.chainName
entity.asset.attribute.labels[chain_name]
resource.data.checkIntervalSec
entity.asset.attribute.labels[check_interval_sec]
resource.data.circuitInfos.customerDemarcId
entity.asset.attribute.labels[circuitInfos_customer_demarc_id]
Iterate through
resource.data.circuitInfos.customerDemarcId
,
If the
resource.data.circuitInfos.customerDemarcId
log field value is
not
empty then,
resource.data.circuitInfos.customerDemarcId
log field is mapped to the
entity.asset.attribute.labels.circuitInfos_customer_demarc
id
%{index}
UDM field.
resource.data.circuitInfos.googleCircuitId
entity.asset.attribute.labels[circuitInfos_google_circuit_id]
Iterate through
resource.data.circuitInfos.googleCircuitId
,
If the
resource.data.circuitInfos.googleCircuitId
log field value is
not
empty then,
resource.data.circuitInfos.googleCircuitId
log field is mapped to the
entity.asset.attribute.labels.circuit_infos_google_circuit
id
%{index}
UDM field.
resource.data.circuitInfos.googleDemarcId
entity.asset.attribute.labels[circuitInfos_google_demarc_id]
Iterate through
resource.data.circuitInfos.googleDemarcId
,
If the
resource.data.circuitInfos.googleDemarcId
log field value is
not
empty then,
resource.data.circuitInfos.googleDemarcId
log field is mapped to the
entity.asset.attribute.labels.circuitInfos_google_demarc
id
%{index}
UDM field.
resource.data.cloudFunction.urlMask
entity.asset.attribute.labels[cloud_function_url_mask]
resource.data.cloudFunction.function
entity.asset.attribute.labels[cloud_function]
resource.data.cloudRun.service
entity.asset.attribute.labels[cloud_run_service]
resource.data.cloudRun.tag
entity.asset.attribute.labels[cloud_run_tag]
resource.data.cloudRun.urlMask
entity.asset.attribute.labels[cloud_run_url_mask]
resource.data.cloudRouterIpAddress
entity.asset.attribute.labels[cloud_router_ip_address]
resource.data.cloudRouterIpv6Address
entity.asset.attribute.labels[cloud_router_ipv6_address]
resource.data.commitment
entity.asset.attribute.labels[commitment]
resource.data.commonInstanceMetadata.fingerprint
entity.asset.attribute.labels[common_instance_metadata_fingerprint]
resource.data.commonInstanceMetadata.items.key
entity.asset.attribute.labels[common_instance_metadata_items]
resource.data.commonInstanceMetadata.items.value
entity.asset.attribute.labels[common_instance_metadata_items]
resource.data.commonInstanceMetadata.kind
entity.asset.attribute.labels[common_instance_metadata_kind]
resource.data.configurationConstraints.bgpMd5
entity.asset.attribute.labels[configuration_constraints_bgp_md5]
resource.data.configurationConstraints.bgpPeerAsnRanges.max
entity.asset.attribute.labels[configuration_constraints_bgp_peer_asn_ranges_max]
Iterate through
resource.data.configurationConstraints.bgpPeerAsnRanges.max
,
If the
resource.data.configurationConstraints.bgpPeerAsnRanges.max
log field value is
not
empty then,
resource.data.configurationConstraints.bgpPeerAsnRanges.max
log field is mapped to the
entity.asset.attribute.labels.configuration_constraints_bgp_peer_asn_ranges
max
%{index}
UDM field.
resource.data.configurationConstraints.bgpPeerAsnRanges.min
entity.asset.attribute.labels[configuration_constraints_bgp_peer_asn_ranges_min]
Iterate through
resource.data.configurationConstraints.bgpPeerAsnRanges.min
,
If the
resource.data.configurationConstraints.bgpPeerAsnRanges.min
log field value is
not
empty then,
resource.data.configurationConstraints.bgpPeerAsnRanges.min
log field is mapped to the
entity.asset.attribute.labels.configuration_constraints_bgp_peer_asn_ranges
min
%{index}
UDM field.
resource.data.connectionPreference
entity.asset.attribute.labels[connection_preference]
resource.data.count
entity.asset.attribute.labels[count]
resource.data.cpuOvercommitType
entity.asset.attribute.labels[cpu_overcommit_type]
resource.data.creationSizeBytes
entity.asset.attribute.labels[creation_size_bytes]
resource.data.customFeatures
entity.asset.attribute.labels[custom_feature]
Iterate through
resource.data.customFeatures
,
If the
resource.data.customFeatures
log field value is
not
empty then,
resource.data.customFeatures
log field is mapped to the
entity.asset.attribute.labels.custom
feature
%{index}
UDM field.
resource.data.customerName
entity.asset.attribute.labels[customer_name]
resource.data.customerRouterIpAddress
entity.asset.attribute.labels[customer_router_ip_address]
resource.data.customerRouterIpv6Address
entity.asset.attribute.labels[customer_router_ipv6_address]
resource.data.dataplaneVersion
entity.asset.attribute.labels[dataplane_version]
resource.data.ddosProtectionConfig.ddosProtection
entity.asset.attribute.labels[ddos_protection_config_ddos_protection]
resource.data.defaultNetworkTier
entity.asset.attribute.labels[default_network_tier]
resource.data.defaultPort
entity.asset.attribute.labels[default_port]
resource.data.defaultServiceAccount
entity.asset.attribute.labels[default_service_account]
resource.data.defaultRouteAction.corsPolicy.allowCredentials
entity.asset.attribute.labels[default_route_action_cors_policy_allow_credentials]
resource.data.defaultRouteAction.corsPolicy.allowHeaders
entity.asset.attribute.labels[default_route_action_cors_policy_allow_headers]
Iterate through
resource.data.defaultRouteAction.corsPolicy.allowHeaders
,
If the
resource.data.defaultRouteAction.corsPolicy.allowHeaders
log field value is
not
empty then,
resource.data.defaultRouteAction.corsPolicy.allowHeaders
log field is mapped to the
entity.asset.attribute.labels.default_route_action_cors_policy_allow
headers
%{index}
UDM field.
resource.data.defaultRouteAction.corsPolicy.allowMethods
entity.asset.attribute.labels[default_route_action_cors_policy_allow_methods]
Iterate through
resource.data.defaultRouteAction.corsPolicy.allowMethods
,
If the
resource.data.defaultRouteAction.corsPolicy.allowMethods
log field value is
not
empty then,
resource.data.defaultRouteAction.corsPolicy.allowMethods
log field is mapped to the
entity.asset.attribute.labels.default_route_action_cors_policy_allow
methods
%{index}
UDM field.
resource.data.defaultRouteAction.corsPolicy.allowOriginRegexes
entity.asset.attribute.labels[default_route_action_cors_policy_allow_origin_regexes]
Iterate through
resource.data.defaultRouteAction.corsPolicy.allowOriginRegexes
,
If the
resource.data.defaultRouteAction.corsPolicy.allowOriginRegexes
log field value is
not
empty then,
resource.data.defaultRouteAction.corsPolicy.allowOriginRegexes
log field is mapped to the
entity.asset.attribute.labels.default_route_action_cors_policy_allow_origin
regexes
%{index}
UDM field.
resource.data.defaultRouteAction.corsPolicy.allowOrigins
entity.asset.attribute.labels[default_route_action_cors_policy_allow_origins]
Iterate through
resource.data.defaultRouteAction.corsPolicy.allowOrigins
,
If the
resource.data.defaultRouteAction.corsPolicy.allowOrigins
log field value is
not
empty then,
resource.data.defaultRouteAction.corsPolicy.allowOrigins
log field is mapped to the
entity.asset.attribute.labels.default_route_action_cors_policy_allow
origins
%{index}
UDM field.
resource.data.defaultRouteAction.corsPolicy.disabled
entity.asset.attribute.labels[default_route_action_cors_policy_disabled]
resource.data.defaultRouteAction.corsPolicy.exposeHeaders
entity.asset.attribute.labels[default_route_action_cors_policy_expose_headers]
Iterate through
resource.data.defaultRouteAction.corsPolicy.exposeHeaders
,
If the
resource.data.defaultRouteAction.corsPolicy.exposeHeaders
log field value is
not
empty then,
resource.data.defaultRouteAction.corsPolicy.exposeHeaders
log field is mapped to the
entity.asset.attribute.labels.default_route_action_cors_policy_expose
headers
%{index}
UDM field.
resource.data.defaultRouteAction.corsPolicy.maxAge
entity.asset.attribute.labels[default_route_action_cors_policy_max_age]
resource.data.defaultRouteAction.faultInjectionPolicy.abort.httpStatus
entity.security_result.rule_labels[default_route_action_fault_injection_policy_abort_http_status]
resource.data.defaultRouteAction.faultInjectionPolicy.abort.percentage
entity.security_result.rule_labels[default_route_action_fault_injection_policy_abort_percentage]
resource.data.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos
entity.security_result.rule_labels[default_route_action_fault_injection_policy_delay_fixed_delay_nanos]
resource.data.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds
entity.security_result.rule_labels[default_route_action_fault_injection_policy_delay_fixed_delay_seconds]
resource.data.defaultRouteAction.faultInjectionPolicy.delay.percentage
entity.security_result.rule_labels[default_route_action_fault_injection_policy_delay_percentage]
resource.data.defaultRouteAction.maxStreamDuration.nanos
entity.asset.attribute.labels[default_route_action_max_stream_duration_nanos]
resource.data.defaultRouteAction.maxStreamDuration.seconds
entity.asset.attribute.labels[default_route_action_max_stream_duration_seconds]
resource.data.defaultRouteAction.requestMirrorPolicy.backendService
entity.asset.attribute.labels[default_route_action_request_mirror_policy_backend_service]
resource.data.defaultRouteAction.retryPolicy.numRetries
entity.security_result.rule_labels[default_route_action_retry_policy_num_retries]
resource.data.defaultRouteAction.retryPolicy.perTryTimeout.nanos
entity.security_result.rule_labels[default_route_action_retry_policy_per_try_timeout_nanos]
resource.data.defaultRouteAction.retryPolicy.perTryTimeout.seconds
entity.security_result.rule_labels[default_route_action_retry_policy_per_try_timeout_seconds]
resource.data.defaultRouteAction.retryPolicy.retryConditions
entity.security_result.rule_labels[default_route_action_retry_policy_retry_conditions]
Iterate through
resource.data.defaultRouteAction.retryPolicy.retryConditions
,
If the
resource.data.defaultRouteAction.retryPolicy.retryConditions
log field value is
not
empty then,
resource.data.defaultRouteAction.retryPolicy.retryConditions
log field is mapped to the
entity.security_result.rule_labels.default_route_action_retry_policy_retry
conditions
%{index}
UDM field.
resource.data.defaultRouteAction.timeout.nanos
entity.asset.attribute.labels[default_route_action_timeout_nanos]
resource.data.defaultRouteAction.timeout.seconds
entity.asset.attribute.labels[default_route_action_timeout_seconds]
resource.data.defaultRouteAction.urlRewrite.hostRewrite
entity.asset.attribute.labels[default_route_action_url_rewrite_host_rewrite]
resource.data.defaultRouteAction.urlRewrite.pathPrefixRewrite
entity.asset.attribute.labels[default_route_action_url_rewrite_path_prefix_rewrite]
resource.data.defaultRouteAction.urlRewrite.pathTemplateRewrite
entity.asset.attribute.labels[default_route_action_url_rewrite_path_template_rewrite]
resource.data.defaultRouteAction.weightedBackendServices.backendService
entity.asset.attribute.labels[default_route_action_weighted_backend_services_backend_service]
Iterate through
resource.data.defaultRouteAction.weightedBackendServices
,
If the
resource.data.defaultRouteAction.weightedBackendServices.backendService
log field value is
not
empty then,
resource.data.defaultRouteAction.weightedBackendServices.backendService
log field is mapped to the
entity.asset.attribute.labels.default_route_action_weighted_backend_services_backend
service
%{index}
UDM field.
resource.data.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_request_headers_to_add_header_name]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_request_headers_to_add_header_value]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_request_headers_to_add_replace]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_request_headers_to_remove]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_response_headers_to_add_header_name]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_response_headers_to_add_header_value]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_response_headers_to_add_replace]
resource.data.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[default_route_action_weighted_backend_services_header_action_response_headers_to_remove]
resource.data.defaultRouteAction.weightedBackendServices.weight
entity.asset.attribute.labels[default_route_action_weighted_backend_services_weight]
Iterate through
resource.data.defaultRouteAction.weightedBackendServices
,
If the
resource.data.defaultRouteAction.weightedBackendServices.weight
log field value is
not
empty then,
resource.data.defaultRouteAction.weightedBackendServices.weight
log field is mapped to the
entity.asset.attribute.labels.default_route_action_weighted_backend_services
weight
%{index}
UDM field.
resource.data.defaultService
entity.asset.attribute.labels[default_service]
resource.data.defaultUrlRedirect.hostRedirect
entity.asset.attribute.labels[default_url_redirect_host_redirect]
resource.data.defaultUrlRedirect.httpsRedirect
entity.asset.attribute.labels[default_url_redirect_https_redirect]
resource.data.defaultUrlRedirect.pathRedirect
entity.asset.attribute.labels[default_url_redirect_path_redirect]
resource.data.defaultUrlRedirect.prefixRedirect
entity.asset.attribute.labels[default_url_redirect_prefix_redirect]
resource.data.defaultUrlRedirect.redirectResponseCode
entity.asset.attribute.labels[default_url_redirect_redirect_response_code]
resource.data.defaultUrlRedirect.stripQuery
entity.asset.attribute.labels[default_url_redirect_strip_query]
resource.data.detailedStatus
entity.asset.attribute.labels[detailed_status]
resource.data.disks.diskCount
entity.asset.attribute.labels[disk_count]
Iterate through
resource.data.disks
,
If the
resource.data.disks.diskCount
log field value is
not
empty then,
resource.data.disks.diskCount
log field is mapped to the
entity.asset.attribute.labels.disk
count
%{index}
UDM field.
resource.data.disks.diskSizeGb
entity.asset.attribute.labels[disk_size_gb]
Iterate through
resource.data.disks.diskSizeGb
,
If the
resource.data.disks.diskSizeGb
log field value is
not
empty then,
resource.data.disks.diskSizeGb
log field is mapped to the
entity.asset.attribute.labels.disk_size
gb
%{index}
UDM field.
resource.data.diskSizeGb
entity.asset.attribute.labels[disk_size_gb]
resource.data.disks.diskType
entity.asset.attribute.labels[disk_type]
Iterate through
resource.data.disks
,
If the
resource.data.disks.diskType
log field value is
not
empty then,
resource.data.disks.diskType
log field is mapped to the
entity.asset.attribute.labels.disk
type
%{index}
UDM field.
resource.data.downloadBytes
entity.asset.attribute.labels[download_bytes]
resource.data.nats.drainNatIps
entity.asset.attribute.labels[nat_drain_nat_ip]
resource.data.edgeAvailabilityDomain
entity.asset.attribute.labels[edge_availability_domain]
resource.data.nats.enableDynamicPortAllocation
entity.asset.attribute.labels[nat_enable_dynamic_port_allocation]
resource.data.nats.enableEndpointIndependentMapping
entity.asset.attribute.labels[enable_endpoint_independent_mapping]
resource.data.enableProxyProtocol
entity.asset.attribute.labels[enable_proxy_protocol]
resource.data.enable
entity.asset.attribute.labels[enable]
resource.data.enabledFeatures
entity.asset.attribute.labels[enabled_feature]
Iterate through
resource.data.enabledFeatures
,
If the
resource.data.enabledFeatures
log field value is
not
empty then,
resource.data.enabledFeatures
log field is mapped to the
entity.asset.attribute.labels.enabled
feature
%{index}
UDM field.
resource.data.encryptedInterconnectRouter
entity.asset.attribute.labels[encrypted_interconnect_router]
resource.data.encryption
entity.asset.attribute.labels[encryption]
resource.data.nats.endpointTypes
entity.asset.attribute.labels[nat_endpoint_types]
resource.data.endTimestamp
entity.asset.attribute.labels[end_timestamp]
resource.data.expectedOutages.affectedCircuits
entity.asset.attribute.labels[expected_outages_affected_circuits]
resource.data.expectedOutages.description
entity.asset.attribute.labels[expected_outages_description]
Iterate through
resource.data.expectedOutages.description
,
If the
resource.data.expectedOutages.description
log field value is
not
empty then,
resource.data.expectedOutages.description
log field is mapped to the
entity.asset.attribute.labels.expected_outages
description
%{index}
UDM field.
resource.data.expectedOutages.endTime
entity.asset.attribute.labels[expected_outages_end_time]
Iterate through
resource.data.expectedOutages.endTime
,
If the
resource.data.expectedOutages.endTime
log field value is
not
empty then,
resource.data.expectedOutages.endTime
log field is mapped to the
entity.asset.attribute.labels.expected_outages_end
time
%{index}
UDM field.
resource.data.expectedOutages.issueType
entity.asset.attribute.labels[expected_outages_issue_type]
Iterate through
resource.data.expectedOutages.issueType
,
If the
resource.data.expectedOutages.issueType
log field value is
not
empty then,
resource.data.expectedOutages.issueType
log field is mapped to the
entity.asset.attribute.labels.expected_outages_issue
type
%{index}
UDM field.
resource.data.expectedOutages.name
entity.asset.attribute.labels[expected_outages_name]
Iterate through
resource.data.expectedOutages.name
,
If the
resource.data.expectedOutages.name
log field value is
not
empty then,
resource.data.expectedOutages.name
log field is mapped to the
entity.asset.attribute.labels.expected_outages
name
%{index}
UDM field.
resource.data.expectedOutages.source
entity.asset.attribute.labels[expected_outages_source]
Iterate through
resource.data.expectedOutages.source
,
If the
resource.data.expectedOutages.source
log field value is
not
empty then,
resource.data.expectedOutages.source
log field is mapped to the
entity.asset.attribute.labels.expected_outages
source
%{index}
UDM field.
resource.data.expectedOutages.startTime
entity.asset.attribute.labels[expected_outages_start_time]
Iterate through
resource.data.expectedOutages.startTime
,
If the
resource.data.expectedOutages.startTime
log field value is
not
empty then,
resource.data.expectedOutages.startTime
log field is mapped to the
entity.asset.attribute.labels.expected_outages_start
time
%{index}
UDM field.
resource.data.expectedOutages.state
entity.asset.attribute.labels[expected_outages_state]
Iterate through
resource.data.expectedOutages.state
,
If the
resource.data.expectedOutages.state
log field value is
not
empty then,
resource.data.expectedOutages.state
log field is mapped to the
entity.asset.attribute.labels.expected_outages
state
%{index}
UDM field.
resource.data.expireTime
entity.asset.attribute.labels[expire_time]
resource.data.usageExportLocation.reportNamePrefix
entity.asset.attribute.labels[export_location_reportname_prefix]
resource.data.filter.cidrRanges
entity.asset.attribute.labels[filter_cidr_ranges]
Iterate through
resource.data.filter.cidrRanges
,
If the
resource.data.filter.cidrRanges
log field value is
not
empty then,
resource.data.filter.cidrRanges
log field is mapped to the
entity.asset.attribute.labels.filter_cidr
ranges
%{index}
UDM field.
resource.data.filter.IPProtocols
entity.asset.attribute.labels[filter_ip_protocol]
Iterate through
resource.data.filter.IPProtocols
,
If the
resource.data.filter.IPProtocols
log field value is
not
empty then,
resource.data.filter.IPProtocols
log field is mapped to the
entity.asset.attribute.labels.filter_ip
protocol
%{index}
UDM field.
resource.data.fingerprint
entity.asset.attribute.labels[fingerprint]
resource.data.googleReferenceId
entity.asset.attribute.labels[google_reference_id]
resource.data.groupPlacementPolicy.availabilityDomainCount
entity.security_result.rule_labels[group_placement_policy_availability_domain_count]
resource.data.groupPlacementPolicy.collocation
entity.security_result.rule_labels[group_placement_policy_collocation]
resource.data.groupPlacementPolicy.vmCount
entity.security_result.rule_labels[group_placement_policy_vm_count]
resource.data.grpcHealthCheck.portName
entity.asset.attribute.labels[grpc_health_check_port_name]
resource.data.grpcHealthCheck.portSpecification
entity.asset.attribute.labels[grpc_health_check_port_specification]
resource.data.grpcHealthCheck.port
entity.asset.attribute.labels[grpc_health_check_port]
resource.data.grpcHealthCheck.grpcServiceName
entity.asset.attribute.labels[grpc_health_check_service_name]
resource.data.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[header_action_request_headers_to_add_header_name]
Iterate through
resource.data.headerAction.requestHeadersToAdd
,
If the
resource.data.headerAction.requestHeadersToAdd.headerName
log field value is
not
empty then,
resource.data.headerAction.requestHeadersToAdd.headerName
log field is mapped to the
entity.asset.attribute.labels.header_action_request_headers_to_add_header
name
%{index}
UDM field.
resource.data.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[header_action_request_headers_to_add_header_value]
Iterate through
resource.data.headerAction.requestHeadersToAdd
,
If the
resource.data.headerAction.requestHeadersToAdd.headerValue
log field value is
not
empty then,
resource.data.headerAction.requestHeadersToAdd.headerValue
log field is mapped to the
entity.asset.attribute.labels.header_action_request_headers_to_add_header
value
%{index}
UDM field.
resource.data.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[header_action_request_headers_to_add_replace]
Iterate through
resource.data.headerAction.requestHeadersToAdd
,
If the
resource.data.headerAction.requestHeadersToAdd.replace
log field value is
not
empty then,
resource.data.headerAction.requestHeadersToAdd.replace
log field is mapped to the
entity.asset.attribute.labels.header_action_request_headers_to_add
replace
%{index}
UDM field.
resource.data.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[header_action_request_headers_to_remove]
Iterate through
resource.data.headerAction.requestHeadersToRemove
,
If the
resource.data.headerAction.requestHeadersToRemove
log field value is
not
empty then,
resource.data.headerAction.requestHeadersToRemove
log field is mapped to the
entity.asset.attribute.labels.header_action_request_headers_to
remove
%{index}
UDM field.
resource.data.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[header_action_response_headers_to_add_header_name]
Iterate through
resource.data.headerAction.responseHeadersToAdd
,
If the
resource.data.headerAction.responseHeadersToAdd.headerName
log field value is
not
empty then,
resource.data.headerAction.responseHeadersToAdd.headerName
log field is mapped to the
entity.asset.attribute.labels.header_action_response_headers_to_add_header
name
%{index}
UDM field.
resource.data.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[header_action_response_headers_to_add_header_value]
Iterate through
resource.data.headerAction.responseHeadersToAdd
,
If the
resource.data.headerAction.responseHeadersToAdd.headerValue
log field value is
not
empty then,
resource.data.headerAction.responseHeadersToAdd.headerValue
log field is mapped to the
entity.asset.attribute.labels.header_action_response_headers_to_add_header
value
%{index}
UDM field.
resource.data.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[header_action_response_headers_to_add_replace]
Iterate through
resource.data.headerAction.responseHeadersToAdd
,
If the
resource.data.headerAction.responseHeadersToAdd.replace
log field value is
not
empty then,
resource.data.headerAction.responseHeadersToAdd.replace
log field is mapped to the
entity.asset.attribute.labels.header_action_response_headers_to_add
replace
%{index}
UDM field.
resource.data.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[header_action_response_headers_to_remove]
Iterate through
resource.data.headerAction.responseHeadersToRemove
,
If the
resource.data.headerAction.responseHeadersToRemove
log field value is
not
empty then,
resource.data.headerAction.responseHeadersToRemove
log field is mapped to the
entity.asset.attribute.labels.header_action_response_headers_to
remove
%{index}
UDM field.
resource.data.healthyThreshold
entity.asset.attribute.labels[healthy_threshold]
resource.data.hostRules.description
entity.asset.attribute.labels[host_rule_description]
Iterate through
resource.data.hostRules
,
If the
resource.data.hostRules.description
log field value is
not
empty then,
resource.data.hostRules.description
log field is mapped to the
entity.asset.attribute.labels.host_rule
description
%{index}
UDM field.
resource.data.hostRules.hosts
entity.asset.attribute.labels[host_rule_host]
resource.data.hostRules.pathMatcher
entity.asset.attribute.labels[host_rule_path_marcher]
Iterate through
resource.data.hostRules
,
If the
resource.data.hostRules.pathMatcher
log field value is
not
empty then,
resource.data.hostRules.pathMatcher
log field is mapped to the
entity.asset.attribute.labels.host_rule_path
matcher
%{index}
UDM field.
resource.data.httpHealthCheck.host
entity.asset.attribute.labels[http_health_check_host]
resource.data.httpHealthCheck.portName
entity.asset.attribute.labels[http_health_check_port_name]
resource.data.httpHealthCheck.portSpecification
entity.asset.attribute.labels[http_health_check_port_specification]
resource.data.httpHealthCheck.port
entity.asset.attribute.labels[http_health_check_port]
resource.data.httpsHealthCheck.proxyHeader
entity.asset.attribute.labels[http_health_check_proxy_header]
resource.data.httpHealthCheck.requestPath
entity.asset.attribute.labels[http_health_check_request_path]
resource.data.httpsHealthCheck.response
entity.asset.attribute.labels[http_health_check_response]
resource.data.http2HealthCheck.host
entity.asset.attribute.labels[http2_health_check_host]
resource.data.http2HealthCheck.portName
entity.asset.attribute.labels[http2_health_check_port_name]
resource.data.http2HealthCheck.portSpecification
entity.asset.attribute.labels[http2_health_check_port_specification]
resource.data.http2HealthCheck.port
entity.asset.attribute.labels[http2_health_check_port]
resource.data.http2HealthCheck.proxyHeader
entity.asset.attribute.labels[http2_health_check_proxy_header]
resource.data.http2HealthCheck.requestPath
entity.asset.attribute.labels[http2_health_check_request_path]
resource.data.http2HealthCheck.response
entity.asset.attribute.labels[http2_health_check_response]
resource.data.nats.icmpIdleTimeoutSec
entity.asset.attribute.labels[nat_icmp_idle_timeout_sec]
resource.data.ikeVersion
entity.asset.attribute.labels[ike_version]
resource.data.inUseCount
entity.asset.attribute.labels[in_use_count]
resource.data.instanceSchedulePolicy.expirationTime
entity.security_result.rule_labels[instance_schedule_policy_expiration_time]
resource.data.instanceSchedulePolicy.startTime
entity.security_result.rule_labels[instance_schedule_policy_start_time]
resource.data.instanceSchedulePolicy.timeZone
entity.security_result.rule_labels[instance_schedule_policy_timezone]
resource.data.instanceSchedulePolicy.vmStartSchedule.schedule
entity.security_result.rule_labels[instance_schedule_policy_vm_start_schedule]
resource.data.instanceSchedulePolicy.vmStopSchedule.schedule
entity.security_result.rule_labels[instance_schedule_policy_vm_stop_schedule]
resource.data.interconnect
entity.asset.attribute.labels[interconnect]
resource.data.interconnectAttachments
entity.asset.attribute.labels[interconnect_attachments]
Iterate through
resource.data.interconnectAttachments
,
If the
resource.data.interconnectAttachments
log field value is
not
empty then,
resource.data.interconnectAttachments
log field is mapped to the
entity.asset.attribute.labels.interconnect
attachments
%{index}
UDM field.
resource.data.interconnectType
entity.asset.attribute.labels[interconnect_type]
resource.data.ipVersion
entity.asset.attribute.labels[ip_version]
resource.data.ipsecInternalAddresses
entity.asset.attribute.labels[ipsec_internal_addresses]
Iterate through
resource.data.ipsecInternalAddresses
,
If the
resource.data.ipsecInternalAddresses
log field value is
not
empty then,
resource.data.ipsecInternalAddresses
log field is mapped to the
entity.asset.attribute.labels.ipsec_internal
addresses
%{index}
UDM field.
resource.data.ipv6EndpointType
entity.asset.attribute.labels[ipv6_endpoint_type]
resource.data.labelFingerprint
entity.asset.attribute.labels[label_fingerprint]
resource.data.licenseCode
entity.asset.attribute.labels[license_code]
resource.data.licenseCodes
entity.asset.attribute.labels[license_codes]
Iterate through
resource.data.licenseCodes
,
If the
resource.data.licenseCodes
log field value is
not
empty then,
resource.data.licenseCodes
log field is mapped to the
entity.asset.attribute.labels.license
code
%{index}
UDM field.
resource.data.licenseResource.amount
entity.asset.attribute.labels[license_resource_amount]
resource.data.licenseResource.coresPerLicense
entity.asset.attribute.labels[license_resource_cores_rer_license]
resource.data.licenseResource.license
entity.asset.attribute.labels[license_resource
license]
resource.data.licenses
entity.asset.attribute.labels[licenses]
Iterate through
resource.data.licenses
,
If the
resource.data.licenses
log field value is
not
empty then,
resource.data.licenses
log field is mapped to the
entity.asset.attribute.labels.license%{index}
UDM field.
resource.data.linkType
entity.asset.attribute.labels[link_type]
resource.data.localTrafficSelector
entity.asset.attribute.labels[local_traffic_selector]
resource.data.locationHint
entity.asset.attribute.labels[location_hint]
resource.data.maintenancePolicy
entity.asset.attribute.labels[maintenance_policy]
resource.data.maintenanceWindow.maintenanceDuration.nanos
entity.asset.attribute.labels[maintenance_window_duration_nanos]
resource.data.maintenanceWindow.maintenanceDuration.seconds
entity.asset.attribute.labels[maintenance_window_duration_seconds]
resource.data.maintenanceWindow.startTime
entity.asset.attribute.labels[maintenance_window_start_time]
resource.data.managed.domains
entity.asset.attribute.labels[managed_domains]
Iterate through
resource.data.managed.domains
,
If the
resource.data.managed.domains
log field value is
not
empty then,
resource.data.managed.domains
log field is mapped to the
entity.asset.attribute.labels.managed
domains
%{index}
UDM field.
resource.data.managed.status
entity.asset.attribute.labels[managed_status]
resource.data.nats.maxPortsPerVm
entity.asset.attribute.labels[nat_min_ports_per_vm]
resource.data.md5AuthenticationKeys.key
entity.asset.attribute.labels[md5_authentication_keys_key]
Iterate through
resource.data.md5AuthenticationKeys.key
,
If the
resource.data.md5AuthenticationKeys.key
log field value is
not
empty then,
resource.data.md5AuthenticationKeys.key
log field is mapped to the
entity.asset.attribute.labels.md5_authentication_keys
key
%{index}
UDM field.
resource.data.md5AuthenticationKeys.name
entity.asset.attribute.labels[md5_authentication_keys_name]
Iterate through
resource.data.md5AuthenticationKeys.name
,
If the
resource.data.md5AuthenticationKeys.name
log field value is
not
empty then,
resource.data.md5AuthenticationKeys.name
log field is mapped to the
entity.asset.attribute.labels.md5_authentication_keys
name
%{index}
UDM field.
resource.data.mergeSourceCommitments
entity.asset.attribute.labels[merge_source_commitments]
Iterate through
resource.data.mergeSourceCommitments
,
If the
resource.data.mergeSourceCommitments
log field value is
not
empty then,
resource.data.mergeSourceCommitments
log field is mapped to the
entity.asset.attribute.labels.merge_source
commitments
%{index}
UDM field.
resource.data.nats.minPortsPerVm
entity.asset.attribute.labels[min_ports_per_vm]
resource.data.mirroredResources.tags
entity.asset.attribute.labels[mirrored_resource_tag]
Iterate through
resource.data.mirroredResources.tags
,
If the
resource.data.mirroredResources.tags
log field value is
not
empty then,
resource.data.mirroredResources.tags
log field is mapped to the
entity.asset.attribute.labels.mirrored_resource
tag
%{index}
UDM field.
resource.data.mtu
entity.asset.attribute.labels[mtu]
resource.data.nats.logConfig.enable
entity.asset.attribute.labels[nat_logconfig_enabled]
resource.data.nats.logConfig.filter
entity.asset.attribute.labels[nat_log_config_filter]
resource.data.nats.name
entity.asset.attribute.labels[nat_name]
resource.data.nats.autoNetworkTier
entity.asset.attribute.labels[nat_autoNetworkTier]
resource.data.nats.natIps
entity.asset.attribute.labels[nat_nat_ip]
resource.data.nats.rules.description
entity.security_result.rule_labels[nat_rule_descriptor]
resource.data.nats.rules.match
entity.security_result.rule_labels[nat_rule_match]
resource.data.nats.rules.ruleNumber
entity.security_result.rule_labels[nat_rule_number]
resource.data.nats.natIpAllocateOption
entity.asset.attribute.labels[natIp_allocate_option]
resource.data.networkEndpointType
entity.asset.attribute.labels[network_endpoint_type]
resource.data.networkTier
entity.asset.attribute.labels[network_tier]
resource.data.nodeTemplate
entity.asset.attribute.labels[node_template]
resource.data.nodeTypeFlexibility.cpus
entity.asset.attribute.labels[node_type_flexibility_cpus]
resource.data.nodeTypeFlexibility.localSsd
entity.asset.attribute.labels[node_type_flexibility_local_ssd]
resource.data.nodeTypeFlexibility.memory
entity.asset.attribute.labels[node_type_flexibility_memory]
resource.data.nodeType
entity.asset.attribute.labels[node_type]
resource.data.operationalStatus
entity.asset.attribute.labels[operational_status]
resource.data.pairingKey
entity.asset.attribute.labels[pairing_key]
resource.data.pathMatchers.defaultService
entity.asset.attribute.labels[parth_matchers_default_service]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultService
log field value is
not
empty then,
resource.data.pathMatchers.defaultService
log field is mapped to the
entity.asset.attribute.labels.parth_matchers_default
service
%{index}
UDM field.
resource.data.pathMatchers.description
entity.asset.attribute.labels[parth_matchers_description]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.description
log field value is
not
empty then,
resource.data.pathMatchers.description
log field is mapped to the
entity.asset.attribute.labels.parth_matchers
description
%{index}
UDM field.
resource.data.partnerAsn
entity.asset.attribute.labels[partner_asn]
resource.data.partnerMetadata.interconnectName
entity.asset.attribute.labels[partner_metadata_interconnect_name]
resource.data.partnerMetadata.partnerName
entity.asset.attribute.labels[partner_metadata_partner_name]
resource.data.partnerMetadata.portalUrl
entity.asset.attribute.labels[partner_metadata_portal_url]
resource.data.pathMatchers.name
entity.asset.attribute.labels[path_marchers_name]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.name
log field value is
not
empty then,
resource.data.pathMatchers.name
log field is mapped to the
entity.asset.attribute.labels.parth_matchers
name
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowCredentials
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_allow_credentials]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowCredentials
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowCredentials
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_cors_policy_allow
credentials
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowHeaders
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_allow_headers]
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowMethods
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_allow_methods]
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowOriginRegexes
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_allow_origin_regexes]
resource.data.pathMatchers.defaultRouteAction.corsPolicy.allowOrigins
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_allow_origins]
resource.data.pathMatchers.defaultRouteAction.corsPolicy.disabled
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_disabled]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.corsPolicy.disabled
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.corsPolicy.disabled
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_cors_policy
disabled
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.corsPolicy.exposeHeaders
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_expose_headers]
resource.data.pathMatchers.defaultRouteAction.corsPolicy.maxAge
entity.asset.attribute.labels[path_matchers_default_route_action_cors_policy_max_age]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.corsPolicy.maxAge
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.corsPolicy.maxAge
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_cors_policy_max
age
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.httpStatus
entity.security_result.rule_labels[path_matchers_default_route_action_fault_injection_policy_abort_http_status]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.httpStatus
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.httpStatus
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_fault_injection_policy_abort_http
status
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.percentage
entity.security_result.rule_labels[path_matchers_default_route_action_fault_injection_policy_abort_percentage]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.percentage
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.abort.percentage
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_fault_injection_policy_abort
percentage
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos
entity.security_result.rule_labels[path_matchers_default_route_action_fault_injection_policy_delay_fixed_delay_nanos]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.nanos
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_fault_injection_policy_delay_fixed_delay
nanos
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds
entity.security_result.rule_labels[path_matchers_default_route_action_fault_injection_policy_delay_fixed_delay_seconds]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.fixedDelay.seconds
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_fault_injection_policy_delay_fixed_delay
seconds
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.percentage
entity.security_result.rule_labels[path_matchers_default_route_action_fault_injection_policy_delay_percentage]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.percentage
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.faultInjectionPolicy.delay.percentage
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_fault_injection_policy_delay
percentage
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.maxStreamDuration.nanos
entity.asset.attribute.labels[path_matchers_default_route_action_max_stream_duration_nanos]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.maxStreamDuration.nanos
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.maxStreamDuration.nanos
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_max_stream_duration
nanos
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.maxStreamDuration.seconds
entity.asset.attribute.labels[path_matchers_default_route_action_max_stream_duration_seconds]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.maxStreamDuration.seconds
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.maxStreamDuration.seconds
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_max_stream_duration
seconds
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.requestMirrorPolicy.backendService
entity.asset.attribute.labels[path_matchers_default_route_action_request_mirror_policy_backend_service]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.requestMirrorPolicy.backendService
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.requestMirrorPolicy.backendService
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_request_mirror_policy_backend
service
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.retryPolicy.numRetries
entity.security_result.rule_labels[path_matchers_default_route_action_retry_policy_num_retries]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.retryPolicy.numRetries
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.retryPolicy.numRetries
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_retry_policy_num
retries
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.nanos
entity.security_result.rule_labels[path_matchers_default_route_action_retry_policy_per_try_timeout_nanos]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.nanos
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.nanos
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_retry_policy_per_try_timeout
nanos
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.seconds
entity.security_result.rule_labels[path_matchers_default_route_action_retry_policy_per_try_timeout_seconds]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.seconds
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.retryPolicy.perTryTimeout.seconds
log field is mapped to the
entity.security_result.rule_labels.path_matchers_default_route_action_retry_policy_per_try_timeout
seconds
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.retryPolicy.retryConditions
entity.security_result.rule_labels[path_matchers_default_route_action_retry_policy_retry_conditions]
resource.data.pathMatchers.defaultRouteAction.timeout.nanos
entity.asset.attribute.labels[path_matchers_default_route_action_timeout_nanos]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.timeout.nanos
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.timeout.nanos
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_timeout
nanos
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.timeout.seconds
entity.asset.attribute.labels[path_matchers_default_route_action_timeout_seconds]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.timeout.seconds
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.timeout.seconds
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_timeout
seconds
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.urlRewrite.hostRewrite
entity.asset.attribute.labels[path_matchers_default_route_action_url_rewrite_host_rewrite]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.urlRewrite.hostRewrite
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.urlRewrite.hostRewrite
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_url_rewrite_host
rewrite
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.urlRewrite.pathPrefixRewrite
entity.asset.attribute.labels[path_matchers_default_route_action_url_rewrite_path_prefix_rewrite]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.urlRewrite.pathPrefixRewrite
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.urlRewrite.pathPrefixRewrite
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_url_rewrite_path_prefix
rewrite
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.urlRewrite.pathTemplateRewrite
entity.asset.attribute.labels[path_matchers_default_route_action_url_rewrite_path_template_rewrite]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultRouteAction.urlRewrite.pathTemplateRewrite
log field value is
not
empty then,
resource.data.pathMatchers.defaultRouteAction.urlRewrite.pathTemplateRewrite
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_route_action_url_rewrite_path_template
rewrite
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_response_headers_to_add_header_name]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_response_headers_to_add_header_value]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_response_headers_to_add_replace]
resource.data.pathMatchers.defaultUrlRedirect.hostRedirect
entity.asset.attribute.labels[path_matchers_default_url_redirect_host_redirect]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultUrlRedirect.hostRedirect
log field value is
not
empty then,
resource.data.pathMatchers.defaultUrlRedirect.hostRedirect
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_url_redirect_host
redirect
%{index}
UDM field.
resource.data.pathMatchers.defaultUrlRedirect.httpsRedirect
entity.asset.attribute.labels[path_matchers_default_url_redirect_https_redirect]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultUrlRedirect.httpsRedirect
log field value is
not
empty then,
resource.data.pathMatchers.defaultUrlRedirect.httpsRedirect
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_url_redirect_https
redirect
%{index}
UDM field.
resource.data.pathMatchers.defaultUrlRedirect.pathRedirect
entity.asset.attribute.labels[path_matchers_default_url_redirect_path_redirect]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultUrlRedirect.pathRedirect
log field value is
not
empty then,
resource.data.pathMatchers.defaultUrlRedirect.pathRedirect
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_url_redirect_path
redirect
%{index}
UDM field.
resource.data.pathMatchers.defaultUrlRedirect.prefixRedirect
entity.asset.attribute.labels[path_matchers_default_url_redirect_prefix_redirect]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultUrlRedirect.prefixRedirect
log field value is
not
empty then,
resource.data.pathMatchers.defaultUrlRedirect.prefixRedirect
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_url_redirect_prefix
redirect
%{index}
UDM field.
resource.data.pathMatchers.defaultUrlRedirect.redirectResponseCode
entity.asset.attribute.labels[path_matchers_default_url_redirect_redirect_response_code]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultUrlRedirect.redirectResponseCode
log field value is
not
empty then,
resource.data.pathMatchers.defaultUrlRedirect.redirectResponseCode
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_url_redirect_redirect_response
code
%{index}
UDM field.
resource.data.pathMatchers.defaultUrlRedirect.stripQuery
entity.asset.attribute.labels[path_matchers_default_url_redirect_strip_query]
Iterate through
resource.data.pathMatchers
,
If the
resource.data.pathMatchers.defaultUrlRedirect.stripQuery
log field value is
not
empty then,
resource.data.pathMatchers.defaultUrlRedirect.stripQuery
log field is mapped to the
entity.asset.attribute.labels.path_matchers_default_url_redirect_strip
query
%{index}
UDM field.
resource.data.pathMatchers.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_header_action_request_headers_to_add_header_name]
resource.data.pathMatchers.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_header_action_request_headers_to_add_header_value]
resource.data.pathMatchers.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_header_action_request_headers_to_add_replace]
resource.data.pathMatchers.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[path_matchers_header_action_request_headers_to_remove]
resource.data.pathMatchers.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_header_action_response_headers_to_add_header_name]
resource.data.pathMatchers.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_header_action_response_headers_to_add_header_value]
resource.data.pathMatchers.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_header_action_response_headers_to_add_replace]
resource.data.pathMatchers.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[path_matchers_header_action_response_headers_to_remove]
resource.data.pathMatchers.pathRules.paths
entity.asset.attribute.labels[path_matchers_path_rules_paths]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.allowCredentials
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_allow_credentials]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.allowHeaders
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_allow_headers]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.allowMethods
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_allow_methods]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.allowOriginRegexes
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_allow_origin_regexes]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.allowOrigins
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_allow_origins]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.disabled
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_disabled]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.exposeHeaders
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_expose_headers]
resource.data.pathMatchers.pathRules.routeAction.corsPolicy.maxAge
entity.asset.attribute.labels[path_matchers_path_rules_route_action_cors_policy_max_age]
resource.data.pathMatchers.pathRules.routeAction.faultInjectionPolicy.abort.httpStatus
entity.security_result.rule_labels[path_matchers_path_rules_route_action_fault_injection_policy_abort_http_status]
resource.data.pathMatchers.pathRules.routeAction.faultInjectionPolicy.abort.percentage
entity.security_result.rule_labels[path_matchers_path_rules_route_action_fault_injection_policy_abort_percentage]
resource.data.pathMatchers.pathRules.routeAction.faultInjectionPolicy.delay.fixedDelay.nanos
entity.security_result.rule_labels[path_matchers_path_rules_route_action_fault_injection_policy_delay_fixed_delay_nanos]
resource.data.pathMatchers.pathRules.routeAction.faultInjectionPolicy.delay.fixedDelay.seconds
entity.security_result.rule_labels[path_matchers_path_rules_route_action_fault_injection_policy_delay_fixed_delay_seconds]
resource.data.pathMatchers.pathRules.routeAction.faultInjectionPolicy.delay.percentage
entity.security_result.rule_labels[path_matchers_path_rules_route_action_fault_injection_policy_delay_percentage]
resource.data.pathMatchers.pathRules.routeAction.maxStreamDuration.nanos
entity.asset.attribute.labels[path_matchers_path_rules_route_action_max_stream_duration_nanos]
resource.data.pathMatchers.pathRules.routeAction.maxStreamDuration.seconds
entity.asset.attribute.labels[path_matchers_path_rules_route_action_max_stream_duration_seconds]
resource.data.pathMatchers.pathRules.routeAction.requestMirrorPolicy.backendService
entity.asset.attribute.labels[path_matchers_path_rules_route_action_request_mirror_policy_backend_service]
resource.data.pathMatchers.pathRules.routeAction.retryPolicy.numRetries
entity.security_result.rule_labels[path_matchers_path_rules_route_action_retry_policy_num_retries]
resource.data.pathMatchers.pathRules.routeAction.retryPolicy.perTryTimeout.nanos
entity.security_result.rule_labels[path_matchers_path_rules_route_action_retry_policy_per_try_timeout_nanos]
resource.data.pathMatchers.pathRules.routeAction.retryPolicy.perTryTimeout.seconds
entity.security_result.rule_labels[path_matchers_path_rules_route_action_retry_policy_per_try_timeout_seconds]
resource.data.pathMatchers.pathRules.routeAction.retryPolicy.retryConditions
entity.security_result.rule_labels[path_matchers_path_rules_route_action_retry_policy_retry_conditions]
resource.data.pathMatchers.pathRules.routeAction.timeout.nanos
entity.asset.attribute.labels[path_matchers_path_rules_route_action_timeout_nanos]
resource.data.pathMatchers.pathRules.routeAction.timeout.seconds
entity.asset.attribute.labels[path_matchers_path_rules_route_action_timeout_seconds]
resource.data.pathMatchers.pathRules.routeAction.urlRewrite.hostRewrite
entity.asset.attribute.labels[path_matchers_path_rules_route_action_url_rewrite_host_rewrite]
resource.data.pathMatchers.pathRules.routeAction.urlRewrite.pathPrefixRewrite
entity.asset.attribute.labels[path_matchers_path_rules_route_action_url_rewrite_path_prefix_rewrite]
resource.data.pathMatchers.pathRules.routeAction.urlRewrite.pathTemplateRewrite
entity.asset.attribute.labels[path_matchers_path_rules_route_action_url_rewrite_path_template_rewrite]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.backendService
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_service]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_request_headers_to_add_header_name]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_request_headers_to_add_header_value]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_request_headers_to_add_replace]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_request_headers_to_remove]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_response_headers_to_add_header_name]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_response_headers_to_add_header_value]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_response_headers_to_add_replace]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_header_action_response_headers_to_remove]
resource.data.pathMatchers.pathRules.routeAction.weightedBackendServices.weight
entity.asset.attribute.labels[path_matchers_path_rules_route_action_weighted_backend_services_weight]
resource.data.pathMatchers.pathRules.service
entity.asset.attribute.labels[path_matchers_path_rules_service]
resource.data.pathMatchers.pathRules.urlRedirect.hostRedirect
entity.asset.attribute.labels[path_matchers_path_rules_url_redirect_host_redirect]
resource.data.pathMatchers.pathRules.urlRedirect.httpsRedirect
entity.asset.attribute.labels[path_matchers_path_rules_url_redirect_https_redirect]
resource.data.pathMatchers.pathRules.urlRedirect.pathRedirect
entity.asset.attribute.labels[path_matchers_path_rules_url_redirect_path_redirect]
resource.data.pathMatchers.pathRules.urlRedirect.prefixRedirect
entity.asset.attribute.labels[path_matchers_path_rules_url_redirect_prefix_redirect]
resource.data.pathMatchers.pathRules.urlRedirect.redirectResponseCode
entity.asset.attribute.labels[path_matchers_path_rules_url_redirect_redirect_response_code]
resource.data.pathMatchers.pathRules.urlRedirect.stripQuery
entity.asset.attribute.labels[path_matchers_path_rules_url_redirect_strip_query]
resource.data.pathMatchers.routeRules.description
entity.asset.attribute.labels[path_matchers_route_rules_description]
resource.data.pathMatchers.routeRules.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_route_rules_header_action_request_headers_to_add_header_name]
resource.data.pathMatchers.routeRules.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_route_rules_header_action_request_headers_to_add_header_value]
resource.data.pathMatchers.routeRules.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_route_rules_header_action_request_headers_to_add_replace]
resource.data.pathMatchers.routeRules.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[path_matchers_route_rules_header_action_request_headers_to_remove]
resource.data.pathMatchers.routeRules.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_route_rules_header_action_response_headers_to_add_header_name]
resource.data.pathMatchers.routeRules.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_route_rules_header_action_response_headers_to_add_header_value]
resource.data.pathMatchers.routeRules.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_route_rules_header_action_response_headers_to_add_replace]
resource.data.pathMatchers.routeRules.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[path_matchers_route_rules_header_action_response_headers_to_remove]
resource.data.pathMatchers.routeRules.matchRules.fullPathMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_full_path_match]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.exactMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_exact_match]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.headerName
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_header_name]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.invertMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_invert_match]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.prefixMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_prefix_match]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.presentMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_present_match]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.rangeMatch.rangeEnd
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_range_match_range_end]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.rangeMatch.rangeStart
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_range_match_range_start]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.regexMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_regex_match]
resource.data.pathMatchers.routeRules.matchRules.headerMatches.suffixMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_header_matches_suffix_match]
resource.data.pathMatchers.routeRules.matchRules.ignoreCase
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_ignore_case]
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.name
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_metadata_filters_filter_labels_name]
Iterate through
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels
,
If the
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.name
log field value is
not
empty and the
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.value
is
not
empty then,
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.value
log field is mapped to the
entity.asset.attribute.labels.path_matchers_route_rules_match_rules_metadata_filters
filter
%{resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.name}
UDM field.
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.value
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_metadata_filters_filter_labels_name]
Iterate through
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels
,
If the
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.name
log field value is
not
empty and the
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.value
is
not
empty then,
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.value
log field is mapped to the
entity.asset.attribute.labels.path_matchers_route_rules_match_rules_metadata_filters
filter
%{resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterLabels.name}
UDM field.
resource.data.pathMatchers.routeRules.matchRules.metadataFilters.filterMatchCriteria
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_metadata_filters_filter_match_criteria]
resource.data.pathMatchers.routeRules.matchRules.pathTemplateMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_path_template_match]
resource.data.pathMatchers.routeRules.matchRules.prefixMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_prefix_match]
resource.data.pathMatchers.routeRules.matchRules.queryParameterMatches.exactMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_query_parameter_matches_exact_match]
resource.data.pathMatchers.routeRules.matchRules.queryParameterMatches.name
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_query_parameter_matches_name]
resource.data.pathMatchers.routeRules.matchRules.queryParameterMatches.presentMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_query_parameter_matches_present_match]
resource.data.pathMatchers.routeRules.matchRules.queryParameterMatches.regexMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_query_parameter_matches_regex_match]
resource.data.pathMatchers.routeRules.matchRules.regexMatch
entity.asset.attribute.labels[path_matchers_route_rules_match_rules_regex_match]
resource.data.pathMatchers.routeRules.priority
entity.asset.attribute.labels[path_matchers_route_rules_priority]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.allowCredentials
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_allow_credentials]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.allowHeaders
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_allow_headers]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.allowMethods
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_allow_methods]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.allowOriginRegexes
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_allow_origin_regexes]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.allowOrigins
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_allow_origins]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.disabled
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_disabled]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.exposeHeaders
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_expose_headers]
resource.data.pathMatchers.routeRules.routeAction.corsPolicy.maxAge
entity.asset.attribute.labels[path_matchers_route_rules_route_action_cors_policy_max_age]
resource.data.pathMatchers.routeRules.routeAction.faultInjectionPolicy.abort.httpStatus
entity.security_result.rule_labels[path_matchers_route_rules_route_action_fault_injection_policy_abort_http_status]
resource.data.pathMatchers.routeRules.routeAction.faultInjectionPolicy.abort.percentage
entity.security_result.rule_labels[path_matchers_route_rules_route_action_fault_injection_policy_abort_percentage]
resource.data.pathMatchers.routeRules.routeAction.faultInjectionPolicy.delay.fixedDelay.nanos
entity.security_result.rule_labels[path_matchers_route_rules_route_action_fault_injection_policy_delay_fixed_delay_nanos]
resource.data.pathMatchers.routeRules.routeAction.faultInjectionPolicy.delay.fixedDelay.seconds
entity.security_result.rule_labels[path_matchers_route_rules_route_action_fault_injection_policy_delay_fixed_delay_seconds]
resource.data.pathMatchers.routeRules.routeAction.faultInjectionPolicy.delay.percentage
entity.security_result.rule_labels[path_matchers_route_rules_route_action_fault_injection_policy_delay_percentage]
resource.data.pathMatchers.routeRules.routeAction.maxStreamDuration.nanos
entity.asset.attribute.labels[path_matchers_route_rules_route_action_max_stream_duration_nanos]
resource.data.pathMatchers.routeRules.routeAction.maxStreamDuration.seconds
entity.asset.attribute.labels[path_matchers_route_rules_route_action_max_stream_duration_seconds]
resource.data.pathMatchers.routeRules.routeAction.requestMirrorPolicy.backendService
entity.asset.attribute.labels[path_matchers_route_rules_route_action_request_mirror_policy_backend_service]
resource.data.pathMatchers.routeRules.routeAction.retryPolicy.numRetries
entity.security_result.rule_labels[path_matchers_route_rules_route_action_retry_policy_num_retries]
resource.data.pathMatchers.routeRules.routeAction.retryPolicy.perTryTimeout.nanos
entity.security_result.rule_labels[path_matchers_route_rules_route_action_retry_policy_per_try_timeout_nanos]
resource.data.pathMatchers.routeRules.routeAction.retryPolicy.perTryTimeout.seconds
entity.security_result.rule_labels[path_matchers_route_rules_route_action_retry_policy_per_try_timeout_seconds]
resource.data.pathMatchers.routeRules.routeAction.retryPolicy.retryConditions
entity.security_result.rule_labels[path_matchers_route_rules_route_action_retry_policy_retry_conditions]
resource.data.pathMatchers.routeRules.routeAction.timeout.nanos
entity.asset.attribute.labels[path_matchers_route_rules_route_action_timeout_nanos]
resource.data.pathMatchers.routeRules.routeAction.timeout.seconds
entity.asset.attribute.labels[path_matchers_route_rules_route_action_timeout_seconds]
resource.data.pathMatchers.routeRules.routeAction.urlRewrite.hostRewrite
entity.asset.attribute.labels[path_matchers_route_rules_route_action_url_rewrite_host_rewrite]
resource.data.pathMatchers.routeRules.routeAction.urlRewrite.pathPrefixRewrite
entity.asset.attribute.labels[path_matchers_route_rules_route_action_url_rewrite_path_prefix_rewrite]
resource.data.pathMatchers.routeRules.routeAction.urlRewrite.pathTemplateRewrite
entity.asset.attribute.labels[path_matchers_route_rules_route_action_url_rewrite_path_template_rewrite]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.backendService
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_request_headers_to_add_header_name]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_request_headers_to_add_header_value]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_request_headers_to_add_replace]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_request_headers_to_remove]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_response_headers_to_add_header_name]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_response_headers_to_add_header_value]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_response_headers_to_add_replace]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_header_action_response_headers_to_remove]
resource.data.pathMatchers.routeRules.routeAction.weightedBackendServices.weight
entity.asset.attribute.labels[path_matchers_route_rules_route_action_weighted_backend_services_weight]
resource.data.pathMatchers.routeRules.service
entity.asset.attribute.labels[path_matchers_route_rules_service]
resource.data.pathMatchers.routeRules.urlRedirect.hostRedirect
entity.asset.attribute.labels[path_matchers_route_rules_url_redirect_host_redirect]
resource.data.pathMatchers.routeRules.urlRedirect.httpsRedirect
entity.asset.attribute.labels[path_matchers_route_rules_url_redirect_https_redirect]
resource.data.pathMatchers.routeRules.urlRedirect.pathRedirect
entity.asset.attribute.labels[path_matchers_route_rules_url_redirect_path_redirect]
resource.data.pathMatchers.routeRules.urlRedirect.prefixRedirect
entity.asset.attribute.labels[path_matchers_route_rules_url_redirect_prefix_redirect]
resource.data.pathMatchers.routeRules.urlRedirect.redirectResponseCode
entity.asset.attribute.labels[path_matchers_route_rules_url_redirect_redirect_response_code]
resource.data.pathMatchers.routeRules.urlRedirect.stripQuery
entity.asset.attribute.labels[path_matchers_route_rules_url_redirect_strip_query]
resource.data.plan
entity.asset.attribute.labels[plan]
resource.data.portName
entity.asset.attribute.labels[port
name]
resource.data.ports
entity.asset.attribute.labels[port]
Iterate through
resource.data.ports
,
If the
resource.data.ports
log field value is
not
empty then,
resource.data.ports
log field is mapped to the
entity.asset.attribute.labels.port%{index}
UDM field.
resource.data.prefixLength
entity.asset.attribute.labels[prefix_length]
resource.data.privateKey
entity.asset.attribute.labels[private_key]
resource.data.privateInterconnectInfo.tag8021q
entity.asset.attribute.labels[private_interconnect_info_tag_8021q]
resource.data.profile
entity.asset.attribute.labels[profile]
resource.data.provisionedLinkCount
entity.asset.attribute.labels[provisioned_link_count]
resource.data.proxyBind
entity.asset.attribute.labels[proxy_bind]
resource.data.proxyHeader
entity.asset.attribute.labels[proxy_header]
resource.data.pscData.consumerPscAddress
entity.asset.attribute.labels[psc_data_consumer_psc_address]
resource.data.pscData.pscConnectionId
entity.asset.attribute.labels[psc_data_psc_connection_id]
resource.data.pscData.pscConnectionStatus
entity.asset.attribute.labels[psc_data_psc_connection_status]
resource.data.pscServiceAttachmentId.high
entity.asset.attribute.labels[psc_service_attachment_id_high]
resource.data.pscServiceAttachmentId.low
entity.asset.attribute.labels[psc_service_attachment_id_low]
resource.data.pscTargetService
entity.asset.attribute.labels[psc_target_service]
resource.data.purpose
entity.asset.attribute.labels[purpose]
resource.data.quicOverride
entity.asset.attribute.labels[quic_override]
resource.data.quotas.limit
entity.asset.attribute.labels[quotas_limit]
Iterate through
resource.data.quotas.limit
,
If the
resource.data.quotas.limit
log field value is
not
empty then,
resource.data.quotas.limit
log field is mapped to the
entity.asset.attribute.labels.quotas
limit
%{index}
UDM field.
resource.data.quotas.metric
entity.asset.attribute.labels[quotas_metric]
Iterate through
resource.data.quotas.metric
,
If the
resource.data.quotas.metric
log field value is
not
empty then,
resource.data.quotas.metric
log field is mapped to the
entity.asset.attribute.labels.quotas
metric
%{index}
UDM field.
resource.data.quotas.owner
entity.asset.attribute.labels[quotas_owner]
Iterate through
resource.data.quotas.owner
,
If the
resource.data.quotas.owner
log field value is
not
empty then,
resource.data.quotas.owner
log field is mapped to the
entity.asset.attribute.labels.quotas
owner
%{index}
UDM field.
resource.data.quotas.usage
entity.asset.attribute.labels[quotas_usage]
Iterate through
resource.data.quotas.usage
,
If the
resource.data.quotas.usage
log field value is
not
empty then,
resource.data.quotas.usage
log field is mapped to the
entity.asset.attribute.labels.quotas
usage
%{index}
UDM field.
resource.data.recaptchaOptionsConfig.redirectSiteKey
entity.asset.attribute.labels[recaptcha_options_config_redirectsite_key]
Iterate through
resource.data.quotas.usage
,
If the
resource.data.quotas.usage
log field value is
not
empty then,
resource.data.quotas.usage
log field is mapped to the
entity.asset.attribute.labels.quotas
usage
%{index}
UDM field.
resource.data.reconcileConnections
entity.asset.attribute.labels[reconcile_connection]
resource.data.redundancyType
entity.asset.attribute.labels[redundancy_type]
resource.data.remoteTrafficSelector
entity.asset.attribute.labels[remote_traffic_selector]
resource.data.remoteLocation
entity.asset.attribute.labels[remote_location]
resource.data.remoteService
entity.asset.attribute.labels[remote_service]
resource.sata.requestPath
entity.asset.attribute.labels[request_path]
resource.data.requestedLinkCount
entity.asset.attribute.labels[requested_link_count]
resource.data.reservations.commitment
entity.asset.attribute.labels[reservations_commitment]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.commitment
log field value is
not
empty then,
resource.data.reservations.commitment
log field is mapped to the
entity.asset.attribute.labels.reservations
commitment
%{index}
UDM field.
resource.data.reservations.creationTimestamp
entity.asset.attribute.labels[reservations_creation_timestamp]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.creationTimestamp
log field value is
not
empty then,
resource.data.reservations.creationTimestamp
log field is mapped to the
entity.asset.attribute.labels.reservations_creation
timestamp
%{index}
UDM field.
resource.data.reservations.description
entity.asset.attribute.labels[reservations_description]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.description
log field value is
not
empty then,
resource.data.reservations.description
log field is mapped to the
entity.asset.attribute.labels.reservations
description
%{index}
UDM field.
resource.data.reservations.id
entity.asset.attribute.labels[reservations_id]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.id
log field value is
not
empty then,
resource.data.reservations.id
log field is mapped to the
entity.asset.attribute.labels.reservations
id
%{index}
UDM field.
resource.data.reservations.kind
entity.asset.attribute.labels[reservations_kind]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.kind
log field value is
not
empty then,
resource.data.reservations.kind
log field is mapped to the
entity.asset.attribute.labels.reservations
kind
%{index}
UDM field.
resource.data.reservations.name
entity.asset.attribute.labels[reservations_name]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.name
log field value is
not
empty then,
resource.data.reservations.name
log field is mapped to the
entity.asset.attribute.labels.reservations
name
%{index}
UDM field.
resource.data.reservations.resourceStatus.specificSkuAllocation.sourceInstanceTemplateId
entity.asset.attribute.labels[reservations_resource_status_specific_sku_allocation_source_instance_template_id]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.resourceStatus.specificSkuAllocation.sourceInstanceTemplateId
log field value is
not
empty then,
resource.data.reservations.resourceStatus.specificSkuAllocation.sourceInstanceTemplateId
log field is mapped to the
entity.asset.attribute.labels.reservations_resource_status_specific_sku_allocation_source_instance_template
id
%{index}
UDM field.
resource.data.reservations.satisfiesPzs
entity.asset.attribute.labels[reservations_satisfies_pzs]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.satisfiesPzs
log field value is
not
empty then,
resource.data.reservations.satisfiesPzs
log field is mapped to the
entity.asset.attribute.labels.reservations_satisfies
pzs
%{index}
UDM field.
resource.data.reservations.selfLink
entity.asset.attribute.labels[reservations_self_link]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.selfLink
log field value is
not
empty then,
resource.data.reservations.selfLink
log field is mapped to the
entity.asset.attribute.labels.reservations_self
link
%{index}
UDM field.
resource.data.reservations.shareSettings.shareType
entity.asset.attribute.labels[reservations_share_settings_share_type]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.shareSettings.shareType
log field value is
not
empty then,
resource.data.reservations.shareSettings.shareType
log field is mapped to the
entity.asset.attribute.labels.reservations_share_settings_share
type
%{index}
UDM field.
resource.data.reservations.specificReservation.assuredCount
entity.asset.attribute.labels[reservations_specific_reservation_assured_count]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservation.assuredCount
log field value is
not
empty then,
resource.data.reservations.specificReservation.assuredCount
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation_assured
count
%{index}
UDM field.
resource.data.reservations.specificReservation.count
entity.asset.attribute.labels[reservations_specific_reservation_count]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservation.count
log field value is
not
empty then,
resource.data.reservations.specificReservation.count
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation
count
%{index}
UDM field.
resource.data.reservations.specificReservation.instanceProperties.guestAccelerators.acceleratorCount
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_guest_accelerator_count]
resource.data.reservations.specificReservation.instanceProperties.guestAccelerators.acceleratorType
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_guest_accelerator_type]
resource.data.reservations.specificReservation.instanceProperties.localSsds.diskSizeGb
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_local_ssds_disk_size_gb]
resource.data.reservations.specificReservation.instanceProperties.localSsds.interface
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_local_ssds_interface]
resource.data.reservations.specificReservation.instanceProperties.locationHint
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_location_hint]
resource.data.reservations.specificReservation.instanceProperties.machineType
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_machine_type]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservation.instanceProperties.machineType
log field value is
not
empty then,
resource.data.reservations.specificReservation.instanceProperties.machineType
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation_instance_properties_machine
type
%{index}
UDM field.
resource.data.reservations.specificReservation.instanceProperties.minCpuPlatform
entity.asset.attribute.labels[reservations_specific_reservation_instance_properties_min_cpu_platform]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservation.instanceProperties.minCpuPlatform
log field value is
not
empty then,
resource.data.reservations.specificReservation.instanceProperties.minCpuPlatform
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation_instance_properties_min_cpu
platform
%{index}
UDM field.
resource.data.reservations.specificReservation.inUseCount
entity.asset.attribute.labels[reservations_specific_reservation_in_use_count]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservation.inUseCount
log field value is
not
empty then,
resource.data.reservations.specificReservation.inUseCount
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation_in_use
count
%{index}
UDM field.
resource.data.reservations.specificReservation.sourceInstanceTemplate
entity.asset.attribute.labels[reservations_specific_reservation_source_instance_template]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservation.sourceInstanceTemplate
log field value is
not
empty then,
resource.data.reservations.specificReservation.sourceInstanceTemplate
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation_source_instance
template
%{index}
UDM field.
resource.data.reservations.specificReservationRequired
entity.asset.attribute.labels[reservations_specific_reservation_required]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.specificReservationRequired
log field value is
not
empty then,
resource.data.reservations.specificReservationRequired
log field is mapped to the
entity.asset.attribute.labels.reservations_specific_reservation
required
%{index}
UDM field.
resource.data.reservations.status
entity.asset.attribute.labels[reservations_status]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.status
log field value is
not
empty then,
resource.data.reservations.status
log field is mapped to the
entity.asset.attribute.labels.reservations
status
%{index}
UDM field.
resource.data.reservations.zone
entity.asset.attribute.labels[reservations_zone]
Iterate through
resource.data.reservations
,
If the
resource.data.reservations.zone
log field value is
not
empty then,
resource.data.reservations.zone
log field is mapped to the
entity.asset.attribute.labels.reservations
zone
%{index}
UDM field.
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.backendService
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_service]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerName
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_request_headers_to_add_header_name]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.headerValue
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_request_headers_to_add_header_value]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToAdd.replace
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_request_headers_to_add_replace]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.requestHeadersToRemove
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_request_headers_to_remove]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.headerAction.responseHeadersToRemove
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_header_action_response_headers_to_remove]
resource.data.pathMatchers.defaultRouteAction.weightedBackendServices.weight
entity.asset.attribute.labels[path_matchers_default_route_action_weighted_backend_services_weight]
resource.data.name
entity.asset.hostname
resource.data.resourceRequirements.minGuestCpuCount
entity.asset.attribute.labels[resource_requirements_min_guest_cpu_count]
resource.data.resourceRequirements.minMemoryMb
entity.asset.attribute.labels[resource_requirements_min_memory_mb]
resource.data.resourceStatus.instanceSchedulePolicy.lastRunStartTime
entity.asset.attribute.labels[resource_status_instance_schedule_policy_last_run_starttime]
resource.data.resourceStatus.instanceSchedulePolicy.nextRunStartTime
entity.asset.attribute.labels[resource_status_instance_schedule_policy_next_run_starttime]
resource.data.resourceStatus.specificSkuAllocation.sourceInstanceTemplateId
entity.asset.attribute.labels[resource_status_specific_sku_allocation_source_instance_template_id]
resource.data.resources.acceleratorType
entity.asset.attribute.labels[resources_accelerator_type]
Iterate through
resource.data.resources
,
If the
resource.data.resources.acceleratorType
log field value is
not
empty then,
resource.data.resources.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.resources_accelerator
type
%{index}
UDM field.
resource.data.resources.amount
entity.asset.attribute.labels[resources_amount]
Iterate through
resource.data.resources
,
If the
resource.data.resources.amount
log field value is
not
empty then,
resource.data.resources.amount
log field is mapped to the
entity.asset.attribute.labels.resources
amount
%{index}
UDM field.
resource.data.resources.type
entity.asset.attribute.labels[resources_type]
Iterate through
resource.data.resources
,
If the
resource.data.resources.type
log field value is
not
empty then,
resource.data.resources.type
log field is mapped to the
entity.asset.attribute.labels.resources
type
%{index}
UDM field.
resource.data.satisfiesPzs
entity.asset.attribute.labels[satisfies_pzs]
resource.data.selfManaged.certificate
entity.asset.attribute.labels[self_managed_certificate]
resource.data.selfManaged.privateKey
entity.asset.attribute.labels[self_managed_private_key]
resource.data.serverBinding.type
entity.asset.attribute.labels[server_binding_type]
resource.data.shareSettings.shareType
entity.asset.attribute.labels[share_setting_share_type]
resource.data.sharedSecretHash
entity.asset.attribute.labels[shared_secret_hash]
resource.data.sharedSecret
entity.asset.attribute.labels[shared_secret]
resource.data.sizeGb
entity.asset.attribute.labels[size_gb]
resource.data.snapshotEncryptionKey.kmsKeyName
entity.asset.attribute.labels[snapshot_encryption_key_kms_key_name]
resource.data.snapshotEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[snapshot_encryption_key_kms_key_service_account]
resource.data.snapshotEncryptionKey.rawKey
entity.asset.attribute.labels[snapshot_encryption_key_raw_key]
resource.data.snapshotEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[snapshot_encryption_key_rsa_encrypted_key]
resource.data.snapshotEncryptionKey.sha256
entity.asset.attribute.labels[snapshot_encryption_key_sha_256]
resource.data.snapshotSchedulePolicy.schedule.dailySchedule.daysInCycle
entity.security_result.rule_labels[snapshot_schedule_policy_daily_schedule_days_In_cycle]
resource.data.snapshotSchedulePolicy.schedule.dailySchedule.duration
entity.security_result.rule_labels[snapshot_schedule_policy_daily_schedule_duration]
resource.data.snapshotSchedulePolicy.schedule.dailySchedule.startTime
entity.security_result.rule_labels[snapshot_schedule_policy_daily_schedule_start_time]
resource.data.snapshotSchedulePolicy.schedule.hourlySchedule.duration
entity.security_result.rule_labels[snapshot_schedule_policy_hourly_schedule_duration]
resource.data.snapshotSchedulePolicy.schedule.hourlySchedule.hoursInCycle
entity.security_result.rule_labels[snapshot_schedule_policy_hourly_schedule_hours_In_cycle]
resource.data.snapshotSchedulePolicy.schedule.hourlySchedule.startTime
entity.security_result.rule_labels[snapshot_schedule_policy_hourly_schedule_start_time]
resource.data.snapshotSchedulePolicy.retentionPolicy.maxRetentionDays
entity.security_result.rule_labels[snapshot_schedule_policy_retention_policy_max_retention_days]
resource.data.snapshotSchedulePolicy.retentionPolicy.onSourceDiskDelete
entity.security_result.rule_labels[snapshot_schedule_policy_retention_policy_onsource_disk_delete]
resource.data.snapshotSchedulePolicy.snapshotProperties.chainName
entity.security_result.rule_labels[snapshot_schedule_policy_snapshot_property_chain_name]
resource.data.snapshotSchedulePolicy.snapshotProperties.guestFlush
entity.security_result.rule_labels[snapshot_schedule_policy_snapshot_property_guest_flush]
resource.data.snapshotSchedulePolicy.snapshotProperties.storageLocations
entity.security_result.rule_labels[snapshot_schedule_policy_snapshot_property_storage_location]
Iterate through
resource.data.snapshotSchedulePolicy.snapshotProperties.storageLocations
,
If the
resource.data.snapshotSchedulePolicy.snapshotProperties.storageLocations
log field value is
not
empty then,
resource.data.snapshotSchedulePolicy.snapshotProperties.storageLocations
log field is mapped to the
entity.security_result.rule_labels.snapshot_schedule_policy_snapshot_property_storage
location
%{index}
UDM field.
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.day
entity.security_result.rule_labels[snapshot_schedule_policy_weekly_schedule_day_of_week_day]
Iterate through
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.day
,
If the
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.day
log field value is
not
empty then,
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.day
log field is mapped to the
entity.security_result.rule_labels.snapshot_schedule_policy_weekly_schedule_day_of_week
day
%{index}
UDM field.
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.duration
entity.security_result.rule_labels[snapshot_schedule_policy_weekly_schedule_day_of_week_duration]
Iterate through
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.duration
,
If the
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.duration
log field value is
not
empty then,
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.duration
log field is mapped to the
entity.security_result.rule_labels.snapshot_schedule_policy_weekly_schedule_day_of_week
duration
%{index}
UDM field.
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.startTime
entity.security_result.rule_labels[snapshot_schedule_policy_weekly_schedule_day_of_week_start_time]
Iterate through
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.startTime
,
If the
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.startTime
log field value is
not
empty then,
resource.data.snapshotSchedulePolicy.schedule.weeklySchedule.dayOfWeeks.startTime
log field is mapped to the
entity.security_result.rule_labels.snapshot_schedule_policy_weekly_schedule_day_of_week_start
time
%{index}
UDM field.
resource.data.snapshotType
entity.asset.attribute.labels[snapshot_type]
resource.data.sourceDiskEncryptionKey.kmsKeyName
entity.asset.attribute.labels[source_disk_encryption_key_kms_key_name]
resource.data.sourceDiskEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[source_disk_encryption_key_kms_key_service_account]
resource.data.sourceDiskEncryptionKey.rawKey
entity.asset.attribute.labels[source_disk_encryption_key_raw_key]
resource.data.sourceDiskEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[source_disk_encryption_key_rsa_encrypted_key]
resource.data.sourceDiskEncryptionKey.sha256
entity.asset.attribute.labels[source_disk_encryption_key_sha_256]
resource.data.specificReservation.sourceInstanceTemplate
entity.asset.attribute.labels[specific_reservation_source_instance_template]
resource.data.nats.rules.action.sourceNatActiveIps
entity.security_result.rule_labels[nat_rule_source_nat_activeIps]
resource.data.nats.rules.action.sourceNatDrainIps
entity.security_result.rule_labels[nat_rule_source_nat_drainIps]
resource.data.sourceSnapshotId
entity.asset.attribute.labels[source_snapshot_id]
resource.data.sourceSnapshot
entity.asset.attribute.labels[source_snapshot]
resource.data.sourceStorageObject
entity.asset.attribute.labels[source_storage_object]
resource.data.nats.sourceSubnetworkIpRangesToNat
entity.asset.attribute.labels[nat_source_subnetwork_Ip_ranges_to_nat]
resource.data.nats.subnetworks.secondaryIpRangeNames
entity.asset.attribute.labels[nats_subnetworks_source_Ip_ranges_to_nat]
resource.data.nats.subnetworks.sourceIpRangesToNat
entity.asset.attribute.labels[nats_subnetworks_secondary_Ip_range_names]
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorCount
entity.asset.attribute.labels[specific_reservation_instance_properties_guest_accelerator_count]
Iterate through
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorCount
,
If the
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorCount
log field value is
not
empty then,
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorCount
log field is mapped to the
entity.asset.attribute.labels.specific_reservation_instance_properties_guest_accelerator
count
%{index}
UDM field.
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorType
entity.asset.attribute.labels[specific_reservation_instance_properties_guest_accelerator_type]
Iterate through
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorType
,
If the
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorType
log field value is
not
empty then,
resource.data.specificReservation.instanceProperties.guestAccelerators.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.specific_reservation_instance_properties_guest_accelerator
type
%{index}
UDM field.
resource.data.specificReservation.instanceProperties.machineType
entity.asset.attribute.labels[specific_reservation_instance_properties_machine_type]
resource.data.specificReservation.instanceProperties.localSsds.diskSizeGb
entity.asset.attribute.labels[specific_reservation_instance_properties_local_ssd_disk_size_gb]
Iterate through
resource.data.specificReservation.instanceProperties.localSsds.diskSizeGb
,
If the
resource.data.specificReservation.instanceProperties.localSsds.diskSizeGb
log field value is
not
empty then,
resource.data.specificReservation.instanceProperties.localSsds.diskSizeGb
log field is mapped to the
entity.asset.attribute.labels.specific_reservation_instance_properties_local_ssd_disk_size
gb
%{index}
UDM field.
resource.data.specificReservation.instanceProperties.localSsds.interface
entity.asset.attribute.labels[specific_reservation_instance_properties_local_ssd_interface]
Iterate through
resource.data.specificReservation.instanceProperties.localSsds.interface
,
If the
resource.data.specificReservation.instanceProperties.localSsds.interface
log field value is
not
empty then,
resource.data.specificReservation.instanceProperties.localSsds.interface
log field is mapped to the
entity.asset.attribute.labels.specific_reservation_instance_properties_local_ssd
interface
%{index}
UDM field.
resource.data.specificReservation.instanceProperties.locationHint
entity.asset.attribute.labels[specific_reservation_instance_properties_location_hint]
resource.data.specificReservation.instanceProperties.minCpuPlatform
entity.asset.attribute.labels[specific_reservation_instance_properties_min_cpu_platform]
resource.data.specificReservation.count
entity.asset.attribute.labels[specific_reservation_count]
resource.data.specificReservation.inUseCount
entity.asset.attribute.labels[specific_reservation_in_use_count]
resource.data.specificReservation.assuredCount
entity.asset.attribute.labels[specific_reservation_assured_count]
resource.data.specificReservationRequired
entity.asset.attribute.labels[specific_reservation_required]
resource.data.splitSourceCommitment
entity.asset.attribute.labels[split_source_commitment]
resource.data.sslHealthCheck.portName
entity.asset.attribute.labels[ssl_health_check_port_name]
resource.data.sslHealthCheck.portSpecification
entity.asset.attribute.labels[ssl_health_check_port_specification]
resource.data.sslHealthCheck.port
entity.asset.attribute.labels[ssl_health_check_port]
resource.data.sslHealthCheck.proxyHeader
entity.asset.attribute.labels[ssl_health_check_proxy_header]
resource.data.sslHealthCheck.request
entity.asset.attribute.labels[ssl_health_check_request]
resource.data.sslHealthCheck.response
entity.asset.attribute.labels[ssl_health_check_response]
resource.data.sslPolicy
entity.asset.attribute.labels[ssl_policy]
resource.data.startTimestamp
entity.asset.attribute.labels[start_timestamp]
resource.data.state
entity.asset.attribute.labels[state]
resource.data.status
entity.asset.attribute.labels[status]
resource.data.storageBytesStatus
entity.asset.attribute.labels[storage_bytes_status]
resource.data.storageBytes
entity.asset.attribute.labels[storage_bytes]
resource.data.storageLocations
entity.asset.attribute.labels[storage_location]
Iterate through
resource.data.storageLocations
,
If the
resource.data.storageLocations
log field value is
not
empty then,
resource.data.storageLocations
log field is mapped to the
entity.asset.attribute.labels.storage
location
%{index}
UDM field.
resource.data.subjectAlternativeNames
entity.asset.attribute.labels[subject_alternative_names]
Iterate through
resource.data.subjectAlternativeNames
,
If the
resource.data.subjectAlternativeNames
log field value is
not
empty then,
resource.data.subjectAlternativeNames
log field is mapped to the
entity.asset.attribute.labels.subject_alternative
names
%{index}
UDM field.
resource.data.subnetLength
entity.asset.attribute.labels[subnet_length]
resource.data.nats.subnetworks.name
entity.asset.attribute.labels[nat_subnetwork_name]
resource.data.nats.tcpEstablishedIdleTimeoutSec
entity.asset.attribute.labels[nat_tcp_establishedIdle_timeout_sec]
resource.data.tcpHealthCheck.portName
entity.asset.attribute.labels[tcp_health_check_port_name]
resource.data.tcpHealthCheck.portSpecification
entity.asset.attribute.labels[tcp_health_check_port_specification]
resource.data.tcpHealthCheck.port
entity.asset.attribute.labels[tcp_health_check_port]
resource.data.tcpHealthCheck.proxyHeader
entity.asset.attribute.labels[tcp_health_check_proxy_header]
resource.data.tcpHealthCheck.request
entity.asset.attribute.labels[tcp_health_check_request]
resource.data.tcpHealthCheck.response
entity.asset.attribute.labels[tcp_health_check_response]
resource.data.nats.tcpTimeWaitTimeoutSec
entity.asset.attribute.labels[nat_tcp_timewait_timeout_sec]
resource.data.nats.tcpTransitoryIdleTimeoutSec
entity.asset.attribute.labels[nat_tcp_transitoryIdle_timeout_sec]
resource.data.tests.description
entity.asset.attribute.labels[tests_description]
Iterate through
resource.data.tests
,
If the
resource.data.tests.description
log field value is
not
empty then,
resource.data.tests.description
log field is mapped to the
entity.asset.attribute.labels.test
description
%{index}
UDM field.
resource.data.tests.expectedOutputUrl
entity.asset.attribute.labels[tests_expected_output_url]
Iterate through
resource.data.tests
,
If the
resource.data.tests.expectedOutputUrl
log field value is
not
empty then,
resource.data.tests.expectedOutputUrl
log field is mapped to the
entity.asset.attribute.labels.test_expected_output
url
%{index}
UDM field.
resource.data.tests.expectedRedirectResponseCode
entity.asset.attribute.labels[tests_expected_redirect_response_code]
Iterate through
resource.data.tests
,
If the
resource.data.tests.expectedRedirectResponseCode
log field value is
not
empty then,
resource.data.tests.expectedRedirectResponseCode
log field is mapped to the
entity.asset.attribute.labels.test_expected_redirect_response
code
%{index}
UDM field.
resource.data.tests.headers.name
entity.asset.attribute.labels[tests_headers_name]
resource.data.tests.host
entity.asset.attribute.labels[tests_host]
resource.data.tests.path
entity.asset.attribute.labels[tests_path]
resource.data.tests.service
entity.asset.attribute.labels[tests_service]
resource.data.timeoutSec
entity.asset.attribute.labels[timeout_sec]
resource.data.transferable
entity.asset.attribute.labels[transferable]
resource.data.type
entity.asset.attribute.labels[type]
resource.data.nats.udpIdleTimeoutSec
entity.asset.attribute.labels[nat_udpIdle_timeout_sec]
resource.data.unhealthyThreshold
entity.asset.attribute.labels[unhealthy_threshold]
resource.data.urlMap
entity.asset.attribute.labels[url_map]
resource.data.vlanTag8021q
entity.asset.attribute.labels[vlan_tag_8021q]
resource.data.vmDnsSetting
entity.asset.attribute.labels[vm_dns_setting]
resource.data.xpnProjectStatus
entity.asset.attribute.labels[xpn_project_status]
resource.data.advancedMachineFeatures.enableNestedVirtualization
entity.asset.attribute.labels[advanced_machine_features_enable_nested_virtualization]
resource.data.properties.advancedMachineFeatures.enableNestedVirtualization
entity.asset.attribute.labels[advanced_machine_features_enable_nested_virtualization]
resource.data.advancedMachineFeatures.enableUefiNetworking
entity.asset.attribute.labels[advanced_machine_features_enable_uefi_networking]
resource.data.properties.advancedMachineFeatures.enableUefiNetworking
entity.asset.attribute.labels[advanced_machine_features_enable_uefi_networking]
resource.data.advancedMachineFeatures.threadsPerCore
entity.asset.attribute.labels[advanced_machine_features_threads_per_core]
resource.data.properties.advancedMachineFeatures.threadsPerCore
entity.asset.attribute.labels[advanced_machine_features_threads_per_core]
resource.data.advancedMachineFeatures.visibleCoreCount
entity.asset.attribute.labels[advanced_machine_features_visible_core_count]
resource.data.properties.advancedMachineFeatures.visibleCoreCount
entity.asset.attribute.labels[advanced_machine_features_visible_core_count]
resource.data.affinityCookieTtlSec
entity.asset.attribute.labels[affinity_cookie_ytl_sec]
resource.data.allPorts
entity.asset.attribute.labels[all_ports]
resource.data.allowGlobalAccess
entity.asset.attribute.labels[allow_global_access]
resource.data.allowPscGlobalAccess
entity.asset.attribute.labels[allow_psc_global_access]
resource.data.allowed.IPProtocol
entity.asset.attribute.labels[allowed_IP_protocol]
Iterate through
resource.data.allowed.IPProtocol
,
If the
resource.data.allowed.IPProtocol
log field value is equal to
TCP
or the
resource.data.allowed.IPProtocol
log field value is equal to
6
then, the
entity.network.ip_protocol
UDM field is set to
TCP
.
Else, If
resource.data.allowed.IPProtocol
log field value is equal to
UDP
or the
resource.data.allowed.IPProtocol
log field value is equal to
17
then, the
entity.network.ip_protocol
UDM field is set to
UDP
.
Else, If
resource.data.allowed.IPProtocol
log field value is equal to
ESP
or the
resource.data.allowed.IPProtocol
log field value is equal to
50
then, the
entity.network.ip_protocol
UDM field is set to
ESP
.
Else, If
resource.data.allowed.IPProtocol
log field value is equal to
SCTP
or the
resource.data.allowed.IPProtocol
log field value is equal to
132
then, the
entity.network.ip_protocol
UDM field is set to
SCTP
.
Else, If
resource.data.allowed.IPProtocol
log field value is equal to
ICMP
or the
resource.data.allowed.IPProtocol
log field value is equal to
1
then, the
entity.network.ip_protocol
UDM field is set to
ICMP
.
Else the
entity.network.ip_protocol
UDM field is set to
UNKNOWN_IP_PROTOCOL
.
resource.data.allowed.IPProtocol
log field is mapped to the
entity.asset.attribute.labels.allowed_IP
protocol
%{index}
UDM field.
resource.data.allowed.ports
entity.asset.attribute.labels[allowed_ports]
resource.data.archiveSizeBytes
entity.asset.attribute.labels[archive_size_bytes]
resource.data.asPaths.asLists
entity.asset.attribute.labels[as_paths_as_lists]
resource.data.asPaths.pathSegmentType
entity.asset.attribute.labels[as_paths_segment_type]
Iterate through
resource.data.asPaths.pathSegmentType
,
If the
resource.data.asPaths.pathSegmentType
log field value is
not
empty then,
resource.data.asPaths.pathSegmentType
log field is mapped to the
entity.asset.attribute.labels.as_paths_segment
type
%{index}
UDM field.
resource.data.associations.attachmentTarget
entity.asset.attribute.labels[associations_attachment_target]
Iterate through
resource.data.associations
,
If the
resource.data.associations.attachmentTarget
log field value is
not
empty then,
resource.data.associations.attachmentTarget
log field is mapped to the
entity.asset.attribute.labels.associations_attachment
target
%{index}
UDM field.
resource.data.associations.displayName
entity.asset.attribute.labels[associations_display_name]
Iterate through
resource.data.associations
,
If the
resource.data.associations.displayName
log field value is
not
empty then,
resource.data.associations.displayName
log field is mapped to the
entity.asset.attribute.labels.associations_display
name
%{index}
UDM field.
resource.data.associations.firewallPolicyId
entity.asset.attribute.labels[associations_firewall_policy_id]
Iterate through
resource.data.associations
,
If the
resource.data.associations.firewallPolicyId
log field value is
not
empty then,
resource.data.associations.firewallPolicyId
log field is mapped to the
entity.asset.attribute.labels.associations_firewall_policy
id
%{index}
UDM field.
resource.data.associations.name
entity.asset.attribute.labels[associations_name]
Iterate through
resource.data.associations
,
If the
resource.data.associations.attachmentTarget
log field value is
not
empty then,
resource.data.associations.attachmentTarget
log field is mapped to the
entity.asset.attribute.labels.associations
name
%{index}
UDM field.
resource.data.associations.shortName
entity.asset.attribute.labels[associations_short_name]
Iterate through
resource.data.associations
,
If the
resource.data.associations.shortName
log field value is
not
empty then,
resource.data.associations.shortName
log field is mapped to the
entity.asset.attribute.labels.associations_short
name
%{index}
UDM field.
resource.data.asyncPrimaryDisk.diskId
entity.asset.attribute.labels[async_primary_disk_Id]
resource.data.asyncPrimaryDisk.disk
entity.asset.attribute.labels[async_primary_disk]
resource.data.autoHealingPolicies.healthCheck
entity.security_result.rule_labels[auto_healing_policies_health_check]
Iterate through
resource.data.autoHealingPolicies.healthCheck
,
If the
resource.data.autoHealingPolicies.healthCheck
log field value is
not
empty then,
resource.data.autoHealingPolicies.healthCheck
log field is mapped to the
entity.security_result.rule_labels.auto_healing_policies_health
check
%{index}
UDM field.
resource.data.autoHealingPolicies.initialDelaySec
entity.security_result.rule_labels[auto_healing_policies_initial_delay_sec]
Iterate through
resource.data.autoHealingPolicies.initialDelaySec
,
If the
resource.data.autoHealingPolicies.initialDelaySec
log field value is
not
empty then,
resource.data.autoHealingPolicies.initialDelaySec
log field is mapped to the
entity.security_result.rule_labels.auto_healing_policies_initial_delay
sec
%{index}
UDM field.
resource.data.autoscalingPolicy.coolDownPeriodSec
entity.security_result.rule_labels[autoscaling_policy_cool_down_period_sec]
resource.data.autoscalingPolicy.cpuUtilization.predictiveMethod
entity.security_result.rule_labels[autoscaling_policy_cpu_utilization_predictive_method]
resource.data.autoscalingPolicy.cpuUtilization.utilizationTarget
entity.security_result.rule_labels[autoscaling_policy_cpu_utilization_utilization_target]
resource.data.autoscalingPolicy.customMetricUtilizations.filter
entity.security_result.rule_labels[autoscaling_policy_custom_metric_utilizations_filter]
Iterate through
resource.data.autoscalingPolicy.customMetricUtilizations.filter
,
If the
resource.data.autoscalingPolicy.customMetricUtilizations.filter
log field value is
not
empty then,
resource.data.autoscalingPolicy.customMetricUtilizations.filter
log field is mapped to the
entity.security_result.rule_labels.autoscaling_policy_custom_metric_utilizations
filter
%{index}
UDM field.
resource.data.autoscalingPolicy.customMetricUtilizations.metric
entity.security_result.rule_labels[autoscaling_policy_custom_metric_utilizations_metric]
Iterate through
resource.data.autoscalingPolicy.customMetricUtilizations.metric
,
If the
resource.data.autoscalingPolicy.customMetricUtilizations.metric
log field value is
not
empty then,
resource.data.autoscalingPolicy.customMetricUtilizations.metric
log field is mapped to the
entity.security_result.rule_labels.autoscaling_policy_custom_metric_utilizations
metric
%{index}
UDM field.
resource.data.autoscalingPolicy.customMetricUtilizations.singleInstanceAssignment
entity.security_result.rule_labels[autoscaling_policy_custom_metric_utilizations_single_instance_assignment]
Iterate through
resource.data.autoscalingPolicy.customMetricUtilizations.singleInstanceAssignment
,
If the
resource.data.autoscalingPolicy.customMetricUtilizations.singleInstanceAssignment
log field value is
not
empty then,
resource.data.autoscalingPolicy.customMetricUtilizations.singleInstanceAssignment
log field is mapped to the
entity.security_result.rule_labels.autoscaling_policy_custom_metric_utilizations_single_instance
assignment
%{index}
UDM field.
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTargetType
entity.security_result.rule_labels[autoscaling_policy_custom_metric_utilizations_utilization_target_type]
Iterate through
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTargetType
,
If the
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTargetType
log field value is
not
empty then,
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTargetType
log field is mapped to the
entity.security_result.rule_labels.autoscaling_policy_custom_metric_utilizations_utilization_target
type
%{index}
UDM field.
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTarget
entity.security_result.rule_labels[autoscaling_policy_custom_metric_utilizations_utilization_target]
Iterate through
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTarget
,
If the
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTarget
log field value is
not
empty then,
resource.data.autoscalingPolicy.customMetricUtilizations.utilizationTarget
log field is mapped to the
entity.security_result.rule_labels.autoscaling_policy_custom_metric_utilizations_utilization
target
%{index}
UDM field.
resource.data.autoscalingPolicy.loadBalancingUtilization.utilizationTarget
entity.security_result.rule_labels[autoscaling_policy_load_balancing_utilization_utilization_target]
resource.data.autoscalingPolicy.maxNumReplicas
entity.security_result.rule_labels[autoscaling_policy_max_num_replicas]
resource.data.autoscalingPolicy.minNumReplicas
entity.security_result.rule_labels[autoscaling_policy_min_num_replicas]
resource.data.autoscalingPolicy.scaleInControl.maxScaledInReplicas.calculated
entity.security_result.rule_labels[autoscaling_policy_scale_in_control_max_scaled_in_replicas_calculated]
resource.data.autoscalingPolicy.scaleInControl.maxScaledInReplicas.fixed
entity.security_result.rule_labels[autoscaling_policy_scale_in_control_max_scaled_in_replicas_fixed]
resource.data.autoscalingPolicy.scaleInControl.maxScaledInReplicas.percent
entity.security_result.rule_labels[autoscaling_policy_scale_in_control_max_scaled_in_replicas_percent]
resource.data.autoscalingPolicy.scaleInControl.timeWindowSec
entity.security_result.rule_labels[autoscaling_policy_scale_in_control_time_window_sec]
resource.data.autoscalingPolicy.scalingSchedules.description
entity.security_result.rule_labels[autoscaling_policy_scaling_schedules_description]
resource.data.autoscalingPolicy.scalingSchedules.disabled
entity.security_result.rule_labels[autoscaling_policy_scaling_schedules_disabled]
resource.data.autoscalingPolicy.scalingSchedules.durationSec
entity.security_result.rule_labels[autoscaling_policy_scaling_schedules_duration_sec]
resource.data.autoscalingPolicy.scalingSchedules.minRequiredReplicas
entity.security_result.rule_labels[autoscaling_policy_scaling_schedules_min_required_replicas]
resource.data.autoscalingPolicy.scalingSchedules.schedule
entity.security_result.rule_labels[autoscaling_policy_scaling_schedules_schedule]
resource.data.autoscalingPolicy.scalingSchedules.timeZone
entity.security_result.rule_labels[autoscaling_policy_scaling_schedules_time_zone]
resource.data.backends.balancingMode
entity.asset.attribute.labels[backends_balancing_mode]
Iterate through
resource.data.backends
,
If the
resource.data.backends.balancingMode
log field value is
not
empty then,
resource.data.backends.balancingMode
log field is mapped to the
entity.asset.attribute.labels.backends_balancing
mode
%{index}
UDM field.
resource.data.backends.capacityScaler
entity.asset.attribute.labels[backends_capacity_scaler]
Iterate through
resource.data.backends
,
If the
resource.data.backends.capacityScaler
log field value is
not
empty then,
resource.data.backends.capacityScaler
log field is mapped to the
entity.asset.attribute.labels.backends_capacity
scaler
%{index}
UDM field.
resource.data.backends.description
entity.asset.attribute.labels[backends_description]
Iterate through
resource.data.backends
,
If the
resource.data.backends.description
log field value is
not
empty then,
resource.data.backends.description
log field is mapped to the
entity.asset.attribute.labels.backends
description
%{index}
UDM field.
resource.data.backends.failover
entity.asset.attribute.labels[backends_failover]
Iterate through
resource.data.backends
,
If the
resource.data.backends.failover
log field value is
not
empty then,
resource.data.backends.failover
log field is mapped to the
entity.asset.attribute.labels.backends
failover
%{index}
UDM field.
resource.data.backends.group
entity.asset.attribute.labels[backends_group]
Iterate through
resource.data.backends
,
If the
resource.data.backends.group
log field value is
not
empty then,
resource.data.backends.group
log field is mapped to the
entity.asset.attribute.labels.backends
group
%{index}
UDM field.
resource.data.backends.maxConnectionsPerEndpoint
entity.asset.attribute.labels[backends_max_cnnections_per_endpoint]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxConnectionsPerEndpoint
log field value is
not
empty then,
resource.data.backends.maxConnectionsPerEndpoint
log field is mapped to the
entity.asset.attribute.labels.backends_max_cnnections_per
endpoint
%{index}
UDM field.
resource.data.backends.maxConnectionsPerInstance
entity.asset.attribute.labels[backends_max_cnnections_per_instance]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxConnectionsPerInstance
log field value is
not
empty then,
resource.data.backends.maxConnectionsPerInstance
log field is mapped to the
entity.asset.attribute.labels.backends_max_cnnections_per
instance
%{index}
UDM field.
resource.data.backends.maxConnections
entity.asset.attribute.labels[backends_max_cnnections]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxConnections
log field value is
not
empty then,
resource.data.backends.maxConnections
log field is mapped to the
entity.asset.attribute.labels.backends_max
cnnections
%{index}
UDM field.
resource.data.backends.maxRatePerEndpoint
entity.asset.attribute.labels[backends_max_rate_per_endpoint]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxRatePerEndpoint
log field value is
not
empty then,
resource.data.backends.maxRatePerEndpoint
log field is mapped to the
entity.asset.attribute.labels.backends_max_rate_per
endpoint
%{index}
UDM field.
resource.data.backends.maxRatePerInstance
entity.asset.attribute.labels[backends_max_rate_per_instance]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxRatePerInstance
log field value is
not
empty then,
resource.data.backends.maxRatePerInstance
log field is mapped to the
entity.asset.attribute.labels.backends_max_rate_per
instance
%{index}
UDM field.
resource.data.backends.maxRate
entity.asset.attribute.labels[backends_max_rate]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxRate
log field value is
not
empty then,
resource.data.backends.maxRate
log field is mapped to the
entity.asset.attribute.labels.backends_max
rate
%{index}
UDM field.
resource.data.backends.maxUtilization
entity.asset.attribute.labels[backends_max_utilization]
Iterate through
resource.data.backends
,
If the
resource.data.backends.maxUtilization
log field value is
not
empty then,
resource.data.backends.maxUtilization
log field is mapped to the
entity.asset.attribute.labels.backends_max
utilization
%{index}
UDM field.
resource.data.backupPool
entity.asset.attribute.labels[backup_pool]
resource.data.baseForwardingRule
entity.asset.attribute.labels[base_forwarding_rule]
resource.data.canIpForward
entity.asset.attribute.labels[can_ip_forward]
resource.data.properties.canIpForward
entity.asset.attribute.labels[can_ip_forward]
resource.data.cdnPolicy.bypassCacheOnRequestHeaders.headerName
entity.security_result.rule_labels[cdn_policy_bypass_cache_on_request_header_Name]
Iterate through
resource.data.cdnPolicy.bypassCacheOnRequestHeaders.headerName
,
If the
resource.data.cdnPolicy.bypassCacheOnRequestHeaders.headerName
log field value is
not
empty then,
resource.data.cdnPolicy.bypassCacheOnRequestHeaders.headerName
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_bypass_cache_on_request_header
Name
%{index}
UDM field.
resource.data.cdnPolicy.cacheKeyPolicy.includeHost
entity.security_result.rule_labels[cdn_policy_cache_key_policy_include_host]
resource.data.cdnPolicy.cacheKeyPolicy.includeHttpHeaders
entity.security_result.rule_labels[cdn_policy_cache_key_policy_include_http_headers]
Iterate through
resource.data.cdnPolicy.cacheKeyPolicy.includeHttpHeaders
,
If the
resource.data.cdnPolicy.cacheKeyPolicy.includeHttpHeaders
log field value is
not
empty then,
resource.data.cdnPolicy.cacheKeyPolicy.includeHttpHeaders
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_cache_key_policy_include_http
headers
%{index}
UDM field.
resource.data.cdnPolicy.cacheKeyPolicy.includeNamedCookies
entity.security_result.rule_labels[cdn_policy_cache_key_policy_include_named_cookies]
Iterate through
resource.data.cdnPolicy.cacheKeyPolicy.includeNamedCookies
,
If the
resource.data.cdnPolicy.cacheKeyPolicy.includeNamedCookies
log field value is
not
empty then,
resource.data.cdnPolicy.cacheKeyPolicy.includeNamedCookies
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_cache_key_policy_include_named
cookies
%{index}
UDM field.
resource.data.cdnPolicy.cacheKeyPolicy.includeProtocol
entity.security_result.rule_labels[cdn_policy_cache_key_policy_include_protocol]
resource.data.cdnPolicy.cacheKeyPolicy.includeQueryString
entity.security_result.rule_labels[cdn_policy_cache_key_policy_include_query_string]
resource.data.cdnPolicy.cacheKeyPolicy.queryStringBlacklist
entity.security_result.rule_labels[cdn_policy_cache_key_policy_query_string_blacklist]
Iterate through
resource.data.cdnPolicy.cacheKeyPolicy.queryStringBlacklist
,
If the
resource.data.cdnPolicy.cacheKeyPolicy.queryStringBlacklist
log field value is
not
empty then,
resource.data.cdnPolicy.cacheKeyPolicy.queryStringBlacklist
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_cache_key_policy_query_string
blacklist
%{index}
UDM field.
resource.data.cdnPolicy.cacheKeyPolicy.queryStringWhitelist
entity.security_result.rule_labels[cdn_policy_cache_key_policy_query_string_whitelist]
Iterate through
resource.data.cdnPolicy.cacheKeyPolicy.queryStringWhitelist
,
If the
resource.data.cdnPolicy.cacheKeyPolicy.queryStringWhitelist
log field value is
not
empty then,
resource.data.cdnPolicy.cacheKeyPolicy.queryStringWhitelist
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_cache_key_policy_query_string
whitelist
%{index}
UDM field.
resource.data.cdnPolicy.cacheMode
entity.security_result.rule_labels[cdn_policy_cache_mode]
resource.data.cdnPolicy.clientTtl
entity.security_result.rule_labels[cdn_policy_client_ttl]
resource.data.cdnPolicy.defaultTtl
entity.security_result.rule_labels[cdn_policy_default_ttl]
resource.data.cdnPolicy.maxTtl
entity.security_result.rule_labels[cdn_policy_max_ttl]
resource.data.cdnPolicy.negativeCachingPolicy.code
entity.security_result.rule_labels[cdn_policy_negative_caching_policy_code]
Iterate through
resource.data.cdnPolicy.negativeCachingPolicy.code
,
If the
resource.data.cdnPolicy.negativeCachingPolicy.code
log field value is
not
empty then,
resource.data.cdnPolicy.negativeCachingPolicy.code
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_negative_caching_policy
code
%{index}
UDM field.
resource.data.cdnPolicy.negativeCachingPolicy.ttl
entity.security_result.rule_labels[cdn_policy_negative_caching_policy_ttl]
Iterate through
resource.data.cdnPolicy.negativeCachingPolicy.ttl
,
If the
resource.data.cdnPolicy.negativeCachingPolicy.ttl
log field value is
not
empty then,
resource.data.cdnPolicy.negativeCachingPolicy.ttl
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_negative_caching_policy
ttl
%{index}
UDM field.
resource.data.cdnPolicy.negativeCaching
entity.security_result.rule_labels[cdn_policy_negative_caching]
resource.data.cdnPolicy.requestCoalescing
entity.security_result.rule_labels[cdn_policy_request_coalescing]
resource.data.cdnPolicy.serveWhileStale
entity.security_result.rule_labels[cdn_policy_serve_while_stale]
resource.data.cdnPolicy.signedUrlCacheMaxAgeSec
entity.security_result.rule_labels[cdn_policy_signed_url_cache_max_age_sec]
resource.data.cdnPolicy.signedUrlKeyNames
entity.security_result.rule_labels[cdn_policy_signed_url_key_names]
Iterate through
resource.data.cdnPolicy.signedUrlKeyNames
,
If the
resource.data.cdnPolicy.signedUrlKeyNames
log field value is
not
empty then,
resource.data.cdnPolicy.signedUrlKeyNames
log field is mapped to the
entity.security_result.rule_labels.cdn_policy_signed_url_key
names
%{index}
UDM field.
resource.data.circuitBreakers.maxConnections
entity.asset.attribute.labels[circuit_breakers_max_connections]
resource.data.circuitBreakers.maxPendingRequests
entity.asset.attribute.labels[circuit_breakers_max_pending_requests]
resource.data.circuitBreakers.maxRequestsPerConnection
entity.asset.attribute.labels[circuit_breakers_max_requests_per_connection]
resource.data.circuitBreakers.maxRequests
entity.asset.attribute.labels[circuit_breakers_max_requests]
resource.data.circuitBreakers.maxRetries
entity.asset.attribute.labels[circuit_breakers_max_retries]
resource.data.compressionMode
entity.asset.attribute.labels[compression_mode]
resource.data.confidentialInstanceConfig.enableConfidentialCompute
entity.asset.attribute.labels[confidential_instance_config_enable_confidential_compute]
resource.data.properties.confidentialInstanceConfig.enableConfidentialCompute
entity.asset.attribute.labels[confidential_instance_config_enable_confidential_compute]
resource.data.connectionDraining.drainingTimeoutSec
entity.asset.attribute.labels[connection_draining_draining_timeout_sec]
resource.data.connectionTrackingPolicy.connectionPersistenceOnUnhealthyBackends
entity.security_result.rule_labels[connection_tracking_policy_connection_persistence_on_unhealthy_backends]
resource.data.connectionTrackingPolicy.enableStrongAffinity
entity.security_result.rule_labels[connection_tracking_policy_enable_strong_affinity]
resource.data.connectionTrackingPolicy.idleTimeoutSec
entity.security_result.rule_labels[connection_tracking_policy_idle_timeout_sec]
resource.data.connectionTrackingPolicy.trackingMode
entity.security_result.rule_labels[connection_tracking_policy_tracking_mode]
resource.data.consistentHash.httpCookie.name
entity.asset.attribute.labels[consistent_hash_http_cookie_name]
resource.data.consistentHash.httpCookie.path
entity.asset.attribute.labels[consistent_hash_http_cookie_path]
resource.data.consistentHash.httpCookie.ttl.nanos
entity.asset.attribute.labels[consistent_hash_http_cookie_ttl_nanos]
resource.data.consistentHash.httpCookie.ttl.seconds
entity.asset.attribute.labels[consistent_hash_http_cookie_ttl_seconds]
resource.data.consistentHash.httpHeaderName
entity.asset.attribute.labels[consistent_hash_http_header_name]
resource.data.consistentHash.minimumRingSize
entity.asset.attribute.labels[consistent_hash_minimum_ring_size]
resource.data.currentActions.abandoning
entity.asset.attribute.labels[current_actions_abandoning]
resource.data.currentActions.creatingWithoutRetries
entity.asset.attribute.labels[current_actions_creating_without_retries]
resource.data.currentActions.creating
entity.asset.attribute.labels[current_actions_creating]
resource.data.currentActions.deleting
entity.asset.attribute.labels[current_actions_deleting]
resource.data.currentActions.none
entity.asset.attribute.labels[current_actions_none]
resource.data.currentActions.recreating
entity.asset.attribute.labels[current_actions_recreating]
resource.data.currentActions.refreshing
entity.asset.attribute.labels[current_actions_refreshing]
resource.data.currentActions.restarting
entity.asset.attribute.labels[current_actions_restarting]
resource.data.currentActions.resuming
entity.asset.attribute.labels[current_actions_resuming]
resource.data.currentActions.starting
entity.asset.attribute.labels[current_actions_starting]
resource.data.currentActions.stopping
entity.asset.attribute.labels[current_actions_stopping]
resource.data.currentActions.suspending
entity.asset.attribute.labels[current_actions_suspending]
resource.data.currentActions.verifying
entity.asset.attribute.labels[current_actions_verifying]
resource.data.customRequestHeaders
entity.asset.attribute.labels[custom_request_headers]
Iterate through
resource.data.cdnPolicy.customRequestHeaders
,
If the
resource.data.cdnPolicy.customRequestHeaders
log field value is
not
empty then,
resource.data.cdnPolicy.customRequestHeaders
log field is mapped to the
entity.asset.attribute.labels.custom_request
headers
%{index}
UDM field.
resource.data.customResponseHeaders
entity.asset.attribute.labels[custom_response_headers]
Iterate through
resource.data.cdnPolicy.customResponseHeaders
,
If the
resource.data.cdnPolicy.customResponseHeaders
log field value is
not
empty then,
resource.data.cdnPolicy.customResponseHeaders
log field is mapped to the
entity.asset.attribute.labels.custom_response
headers
%{index}
UDM field.
resource.data.deletionProtection
entity.asset.attribute.labels[deletion_protection]
resource.data.denied.IPProtocol
entity.asset.attribute.labels[denied_ip_protocol]
Iterate through
resource.data.denied.IPProtocol
,
If the
resource.data.denied.IPProtocol
log field value is
not
empty then,
resource.data.denied.IPProtocol
log field is mapped to the
entity.asset.attribute.labels.denied_IP
protocol
%{index}
UDM field.
resource.data.denied.ports
entity.asset.attribute.labels[denied_ports]
resource.data.deprecated.deleted
entity.asset.attribute.labels[deprecated_deleted]
resource.data.deprecated.deprecated
entity.asset.attribute.labels[deprecated_deprecated]
resource.data.deprecated.obsolete
entity.asset.attribute.labels[deprecated_obsolete]
resource.data.deprecated.replacement
entity.asset.attribute.labels[deprecated_replacement]
resource.data.deprecated.state
entity.asset.attribute.labels[deprecated_state]
resource.data.properties.description
entity.asset.attribute.labels[description]
resource.data.destinationRanges
entity.asset.attribute.labels[destination_ranges]
Iterate through
resource.data.destinationRanges
,
If the
resource.data.destinationRanges
log field value is
not
empty then,
resource.data.destinationRanges
log field is mapped to the
entity.asset.attribute.labels.destination
ranges
%{index}
UDM field.
resource.data.disabled
entity.asset.attribute.labels[disabled]
resource.data.diskEncryptionKey.sha256
entity.asset.attribute.labels[disk_encryption_key_sha256]
resource.data.diskEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disk_encryption_kms_key_name]
resource.data.diskEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disk_encryption_kms_key_service_account]
resource.data.diskEncryptionKey.rawKey
entity.asset.attribute.labels[disk_encryption_raw_key]
resource.data.diskEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disk_encryption_rsa_encrypted_key]
resource.data.disks.architecture
entity.asset.attribute.labels[disks_architecture]
resource.data.properties.disks.architecture
entity.asset.attribute.labels[disks_architecture]
resource.data.disks.autoDelete
entity.asset.attribute.labels[disks_auto_delete]
resource.data.properties.disks.autoDelete
entity.asset.attribute.labels[disks_auto_delete]
resource.data.disks.boot
entity.asset.attribute.labels[disks_boot]
resource.data.properties.disks.boot
entity.asset.attribute.labels[disks_boot]
resource.data.disks.deviceName
entity.asset.attribute.labels[disks_device_name]
resource.data.properties.disks.deviceName
entity.asset.attribute.labels[disks_device_name]
resource.data.disks.diskEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disks_disk_encryption_key_kms_key_name]
resource.data.properties.disks.diskEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disks_disk_encryption_key_kms_key_name]
resource.data.disks.diskEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disks_disk_encryption_key_kms_key_service_account]
resource.data.properties.disks.diskEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disks_disk_encryption_key_kms_key_service_account]
resource.data.disks.diskEncryptionKey.rawKey
entity.asset.attribute.labels[disks_disk_encryption_key_raw_key]
resource.data.properties.disks.diskEncryptionKey.rawKey
entity.asset.attribute.labels[disks_disk_encryption_key_raw_key]
resource.data.disks.diskEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disks_disk_encryption_key_rsa_encrypted_key]
resource.data.properties.disks.diskEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disks_disk_encryption_key_rsa_encrypted_key]
resource.data.disks.diskEncryptionKey.sha256
entity.asset.attribute.labels[disks_disk_encryption_key_sha256]
resource.data.properties.disks.diskEncryptionKey.sha256
entity.asset.attribute.labels[disks_disk_encryption_key_sha256]
resource.data.disks.diskSizeGb
entity.asset.attribute.labels[disks_disk_size_gb]
resource.data.properties.disks.diskSizeGb
entity.asset.attribute.labels[disks_disk_size_gb]
resource.data.disks.forceAttach
entity.asset.attribute.labels[disks_force_attach]
resource.data.properties.disks.forceAttach
entity.asset.attribute.labels[disks_force_attach]
resource.data.disks.guestOsFeatures.type
entity.asset.attribute.labels[disks_guest_os_features_type]
resource.data.properties.disks.guestOsFeatures.type
entity.asset.attribute.labels[disks_guest_os_features_type]
resource.data.disks.index
entity.asset.attribute.labels[disks_index]
resource.data.properties.disks.index
entity.asset.attribute.labels[disks_index]
resource.data.disks.initializeParams.architecture
entity.asset.attribute.labels[disks_initialize_params_architecture]
resource.data.properties.disks.initializeParams.architecture
entity.asset.attribute.labels[disks_initialize_params_architecture]
resource.data.disks.initializeParams.description
entity.asset.attribute.labels[disks_initialize_params_description]
resource.data.properties.disks.initializeParams.description
entity.asset.attribute.labels[disks_initialize_params_description]
resource.data.disks.initializeParams.diskSizeGb
entity.asset.attribute.labels[disks_initialize_params_disk_size_gb]
resource.data.properties.disks.initializeParams.diskSizeGb
entity.asset.attribute.labels[disks_initialize_params_disk_size_gb]
resource.data.disks.initializeParams.diskType
entity.asset.attribute.labels[disks_initialize_params_disk_type]
resource.data.properties.disks.initializeParams.diskType
entity.asset.attribute.labels[disks_initialize_params_disk_type]
resource.data.disks.initializeParams.labels
entity.asset.attribute.labels[disks_initialize_params_labels]
resource.data.properties.disks.initializeParams.labels
entity.asset.attribute.labels[disks_initialize_params_labels]
resource.data.disks.initializeParams.licenses
entity.asset.attribute.labels[disks_initialize_params_licenses]
resource.data.properties.disks.initializeParams.licenses
entity.asset.attribute.labels[disks_initialize_params_licenses]
resource.data.disks.initializeParams.onUpdateAction
entity.asset.attribute.labels[disks_initialize_params_on_update_action]
resource.data.properties.disks.initializeParams.onUpdateAction
entity.asset.attribute.labels[disks_initialize_params_on_update_action]
resource.data.disks.initializeParams.provisionedIops
entity.asset.attribute.labels[disks_initialize_params_provisioned_iops]
resource.data.properties.disks.initializeParams.provisionedIops
entity.asset.attribute.labels[disks_initialize_params_provisioned_iops]
resource.data.disks.initializeParams.provisionedThroughput
entity.asset.attribute.labels[disks_initialize_params_provisioned_throughput]
resource.data.properties.disks.initializeParams.provisionedThroughput
entity.asset.attribute.labels[disks_initialize_params_provisioned_throughput]
resource.data.disks.initializeParams.replicaZones
entity.asset.attribute.labels[disks_initialize_params_replica_zones]
resource.data.properties.disks.initializeParams.replicaZones
entity.asset.attribute.labels[disks_initialize_params_replica_zones]
resource.data.disks.initializeParams.resourceManagerTags
entity.asset.attribute.labels[disks_initialize_params_resource_manager_tags]
resource.data.properties.disks.initializeParams.resourceManagerTags
entity.asset.attribute.labels[disks_initialize_params_resource_manager_tags]
resource.data.disks.initializeParams.sourceImageEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_kms_key_name]
resource.data.properties.disks.initializeParams.sourceImageEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_kms_key_name]
resource.data.disks.initializeParams.sourceImageEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_kms_key_service_account]
resource.data.properties.disks.initializeParams.sourceImageEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_kms_key_service_account]
resource.data.disks.initializeParams.sourceImageEncryptionKey.rawKey
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_raw_key]
resource.data.properties.disks.initializeParams.sourceImageEncryptionKey.rawKey
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_raw_key]
resource.data.disks.initializeParams.sourceImageEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_rsa_encrypted_key]
resource.data.properties.disks.initializeParams.sourceImageEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_rsa_encrypted_key]
resource.data.disks.initializeParams.sourceImageEncryptionKey.sha256
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_sha256]
resource.data.properties.disks.initializeParams.sourceImageEncryptionKey.sha256
entity.asset.attribute.labels[disks_initialize_params_source_image_encryption_key_sha256]
resource.data.disks.initializeParams.sourceImage
entity.asset.attribute.labels[disks_initialize_params_source_image]
resource.data.properties.disks.initializeParams.sourceImage
entity.asset.attribute.labels[disks_initialize_params_source_image]
resource.data.disks.initializeParams.sourceSnapshotEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_kms_key_name]
resource.data.properties.disks.initializeParams.sourceSnapshotEncryptionKey.kmsKeyName
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_kms_key_name]
resource.data.disks.initializeParams.sourceSnapshotEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_kms_key_service_account]
resource.data.properties.disks.initializeParams.sourceSnapshotEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_kms_key_service_account]
resource.data.disks.initializeParams.sourceSnapshotEncryptionKey.rawKey
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_raw_key]
resource.data.properties.disks.initializeParams.sourceSnapshotEncryptionKey.rawKey
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_raw_key]
resource.data.disks.initializeParams.sourceSnapshotEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_rsa_encrypted_key]
resource.data.properties.disks.initializeParams.sourceSnapshotEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_rsa_encrypted_key]
resource.data.disks.initializeParams.sourceSnapshotEncryptionKey.sha256
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_sha256]
resource.data.properties.disks.initializeParams.sourceSnapshotEncryptionKey.sha256
entity.asset.attribute.labels[disks_initialize_params_source_snapshot_encryption_key_sha256]
resource.data.disks.initializeParams.sourceSnapshot
entity.asset.attribute.labels[disks_initialize_params_source_snapshot]
resource.data.properties.disks.initializeParams.sourceSnapshot
entity.asset.attribute.labels[disks_initialize_params_source_snapshot]
resource.data.disks.interface
entity.asset.attribute.labels[disks_interface]
resource.data.properties.disks.interface
entity.asset.attribute.labels[disks_interface]
resource.data.disks.licenses
entity.asset.attribute.labels[disks_licenses]
resource.data.properties.disks.licenses
entity.asset.attribute.labels[disks_licenses]
resource.data.disks.mode
entity.asset.attribute.labels[disks_mode]
resource.data.properties.disks.mode
entity.asset.attribute.labels[disks_mode]
resource.data.disks.savedState
entity.asset.attribute.labels[disks_saved_state]
resource.data.properties.disks.savedState
entity.asset.attribute.labels[disks_saved_state]
resource.data.disks.shieldedInstanceInitialState.dbs.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbs_content]
resource.data.properties.disks.shieldedInstanceInitialState.dbs.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbs_content]
resource.data.disks.shieldedInstanceInitialState.dbs.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbs_file_type]
resource.data.properties.disks.shieldedInstanceInitialState.dbs.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbs_file_type]
resource.data.disks.shieldedInstanceInitialState.dbxs.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbxs_content]
resource.data.properties.disks.shieldedInstanceInitialState.dbxs.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbxs_content]
resource.data.disks.shieldedInstanceInitialState.dbxs.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbxs_file_type]
resource.data.properties.disks.shieldedInstanceInitialState.dbxs.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_dbxs_file_type]
resource.data.disks.shieldedInstanceInitialState.keks.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_keks_content]
resource.data.properties.disks.shieldedInstanceInitialState.keks.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_keks_content]
resource.data.disks.shieldedInstanceInitialState.keks.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_keks_file_type]
resource.data.properties.disks.shieldedInstanceInitialState.keks.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_keks_file_type]
resource.data.disks.shieldedInstanceInitialState.pk.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_pk_content]
resource.data.properties.disks.shieldedInstanceInitialState.pk.content
entity.asset.attribute.labels[disks_shielded_instance_initial_state_pk_content]
resource.data.disks.shieldedInstanceInitialState.pk.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_pk_file_type]
resource.data.properties.disks.shieldedInstanceInitialState.pk.fileType
entity.asset.attribute.labels[disks_shielded_instance_initial_state_pk_file_type]
resource.data.disks.source
entity.asset.attribute.labels[disks_source]
resource.data.properties.disks.source
entity.asset.attribute.labels[disks_source]
resource.data.disks.type
entity.asset.attribute.labels[disks_type]
resource.data.properties.disks.type
entity.asset.attribute.labels[disks_type]
resource.data.displayDevice.enableDisplay
entity.asset.attribute.labels[display_device_enable_display]
resource.data.distributionPolicy.targetShape
entity.asset.attribute.labels[distribution_policy_target_shape]
resource.data.edgeSecurityPolicy
entity.asset.attribute.labels[edge_security_policy]
resource.data.enableCDN
entity.asset.attribute.labels[enable_cdn]
resource.data.failoverPolicy.disableConnectionDrainOnFailover
entity.asset.attribute.labels[failover_policy_disable_connection_drain_on_failover]
resource.data.failoverPolicy.dropTrafficIfUnhealthy
entity.asset.attribute.labels[failover_policy_drop_traffic_if_unhealthy]
resource.data.failoverPolicy.failoverRatio
entity.asset.attribute.labels[failover_policy_failover_ratio]
resource.data.failoverRatio
entity.asset.attribute.labels[failover_ration]
resource.data.family
entity.asset.attribute.labels[family]
resource.data.guestAccelerators.acceleratorCount
entity.asset.attribute.labels[guest_accelerators_accelerator_count]
Iterate through
resource.data.guestAccelerators.acceleratorCount
,
If the
resource.data.guestAccelerators.acceleratorCount
log field value is
not
empty then,
resource.data.guestAccelerators.acceleratorCount
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
count
%{index}
UDM field.
Iterate through
resource.data.properties.guestAccelerators.acceleratorCount
,
If the
resource.data.properties.guestAccelerators.acceleratorCount
log field value is
not
empty then,
resource.data.properties.guestAccelerators.acceleratorCount
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
count
%{index}
UDM field.
resource.data.properties.guestAccelerators.acceleratorType
entity.asset.attribute.labels[guest_accelerators_accelerator_count]
Iterate through
resource.data.guestAccelerators.acceleratorCount
,
If the
resource.data.guestAccelerators.acceleratorCount
log field value is
not
empty then,
resource.data.guestAccelerators.acceleratorCount
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
count
%{index}
UDM field.
Iterate through
resource.data.properties.guestAccelerators.acceleratorCount
,
If the
resource.data.properties.guestAccelerators.acceleratorCount
log field value is
not
empty then,
resource.data.properties.guestAccelerators.acceleratorCount
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
count
%{index}
UDM field.
resource.data.guestAccelerators.acceleratorType
entity.asset.attribute.labels[guest_accelerators_accelerator_type]
Iterate through
resource.data.guestAccelerators.acceleratorType,
If the
resource.data.guestAccelerators.acceleratorType
log field value is
not
empty then,
resource.data.guestAccelerators.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
type
%{index}
UDM field.
Iterate through
resource.data.properties.guestAccelerators.acceleratorType
,
If the
resource.data.properties.guestAccelerators.acceleratorType
log field value is
not
empty then,
resource.data.properties.guestAccelerators.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
type
%{index}
UDM field.
resource.data.properties.guestAccelerators.acceleratorType
entity.asset.attribute.labels[guest_accelerators_accelerator_type]
Iterate through
resource.data.guestAccelerators.acceleratorType
,
If the
resource.data.guestAccelerators.acceleratorType
log field value is
not
empty then,
resource.data.guestAccelerators.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
type
%{index}
UDM field.
Iterate through
resource.data.properties.guestAccelerators.acceleratorType
,
If the
resource.data.properties.guestAccelerators.acceleratorType
log field value is
not
empty then,
resource.data.properties.guestAccelerators.acceleratorType
log field is mapped to the
entity.asset.attribute.labels.guest_accelerators_accelerator
type
%{index}
UDM field.
resource.data.guestOsFeatures.type
entity.asset.attribute.labels[guest_os_features_type]
Iterate through
resource.data.guestOsFeatures
,
If the
resource.data.guestOsFeatures.type
log field value is
not
empty then,
resource.data.guestOsFeatures.type
log field is mapped to the
entity.asset.attribute.labels.guest_os_features
type
%{index}
UDM field.
resource.data.healthChecks
entity.asset.attribute.labels[health_checks]
Iterate through
resource.data.healthChecks
,
If the
resource.data.healthChecks
log field value is
not
empty then,
resource.data.healthChecks
log field is mapped to the
entity.asset.attribute.labels.health
checks
%{index}
UDM field.
resource.data.iap.enabled
entity.asset.attribute.labels[iap_enabled]
resource.data.iap.oauth2ClientId
entity.asset.attribute.labels[iap_oauth2_client_id]
resource.data.iap.oauth2ClientSecretSha256
entity.asset.attribute.labels[iap_oauth2_client_secret_sha256]
resource.data.iap.oauth2ClientSecret
entity.asset.attribute.labels[iap_oauth2_client_secret]
resource.data.imageEncryptionKey.sha256
entity.asset.attribute.labels[image_encryption_key_sha256]
resource.data.imageEncryptionKey.kmsKeyName
entity.asset.attribute.labels[image_encryption_kms_key_name]
resource.data.imageEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[image_encryption_kms_key_service_account]
resource.data.imageEncryptionKey.rawKey
entity.asset.attribute.labels[image_encryption_raw_key]
resource.data.imageEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[image_encryption_rsa_encrypted_key]
resource.data.isMirroringCollector
entity.asset.attribute.labels[is_mirroring_collector]
resource.data.keyRevocationActionType
entity.asset.attribute.labels[key_revocation_action_type]
resource.data.properties.keyRevocationActionType
entity.asset.attribute.labels[key_revocation_action_type]
resource.data.lastAttachTimestamp
entity.asset.attribute.labels[last_attach_timestamp]
resource.data.lastDetachTimestamp
entity.asset.attribute.labels[last_detach_timestamp]
resource.data.lastStartTimestamp
entity.asset.last_boot_time
resource.data.lastStopTimestamp
entity.asset.attribute.labels[last_stop_timestamp]
resource.data.lastSuspendedTimestamp
entity.asset.attribute.labels[last_suspended_timestamp]
resource.data.listManagedInstancesResults
entity.asset.attribute.labels[list_managed_instances_results]
resource.data.loadBalancingScheme
entity.asset.attribute.labels[load_balancing_scheme]
resource.data.localityLbPolicies.customPolicy.data
entity.asset.attribute.labels[locality_lb_policies_custom_policy_data]
Iterate through
resource.data.localityLbPolicies
,
If the
resource.data.localityLbPolicies.customPolicy.data
log field value is
not
empty then,
resource.data.localityLbPolicies.customPolicy.data
log field is mapped to the
entity.asset.attribute.labels.locality_lb_policies_custom_policy
data
%{index}
UDM field.
resource.data.localityLbPolicies.customPolicy.name
entity.asset.attribute.labels[locality_lb_policies_custom_policy_name]
Iterate through
resource.data.localityLbPolicies
,
If the
resource.data.localityLbPolicies.customPolicy.name
log field value is
not
empty then,
resource.data.localityLbPolicies.customPolicy.name
log field is mapped to the
entity.asset.attribute.labels.locality_lb_policies_custom_policy
name
%{index}
UDM field.
resource.data.localityLbPolicies.policy.name
entity.asset.attribute.labels[locality_lb_policies_policy_name]
Iterate through
resource.data.localityLbPolicies
,
If the
resource.data.localityLbPolicies.policy.name
log field value is
not
empty then,
resource.data.localityLbPolicies.policy.name
log field is mapped to the
entity.asset.attribute.labels.locality_lb_policies_policy
name
%{index}
UDM field.
resource.data.localityLbPolicy
entity.asset.attribute.labels[locality_lb_policy]
resource.data.logConfig.enable
entity.asset.attribute.labels[log_config_enable]
resource.data.logConfig.optionalFields
entity.asset.attribute.labels[log_config_optional_fields]
Iterate through
resource.data.logConfig.optionalFields
,
If the
resource.data.logConfig.optionalFields
log field value is
not
empty then,
resource.data.logConfig.optionalFields
log field is mapped to the
entity.asset.attribute.labels.log_config_optional
fields
%{index}
UDM field.
resource.data.logConfig.optionalMode
entity.asset.attribute.labels[log_config_optional_mode]
resource.data.logConfig.sampleRate
entity.asset.attribute.labels[log_config_sample_rate]
resource.data.logConfig.metadata
entity.asset.attribute.labels[log_config_metadata]
resource.data.machineType
entity.asset.hardware.model
If the
resource.data.machineType
log field value is
not
empty then, The
machine_type
field is extracted from
resource.data.machineType
log field using the Grok pattern.
Else, If
resource.data.properties.machineType
log field value then, The
machine_type
field is extracted from
resource.data.properties.machineType
log field using the Grok pattern.
If the
machine_type
log field value is
not
empty then,
machine_type
log field is mapped to the
entity.asset.hardware.model
UDM field.
resource.data.properties.machineType
entity.asset.hardware.model
If the
resource.data.machineType
log field value is
not
empty then, The
machine_type
field is extracted from
resource.data.machineType
log field using the Grok pattern.
Else, If
resource.data.properties.machineType
log field value then, The
machine_type
field is extracted from
resource.data.properties.machineType
log field using the Grok pattern.
If the
machine_type
log field value is
not
empty then,
machine_type
log field is mapped to the
entity.asset.hardware.model
UDM field.
resource.data.maxStreamDuration.nanos
entity.asset.attribute.labels[max_stream_duration_nanos]
resource.data.maxStreamDuration.seconds
entity.asset.attribute.labels[max_stream_duration_seconds]
resource.data.metadataFilters.filterLabels.name
entity.asset.attribute.labels[metadata_filters_filter_labels_name]
Iterate through
resource.data.metadataFilters.filterLabels.name
,
If the
resource.data.metadataFilters.filterLabels.name
log field value is
not
empty then,
resource.data.metadataFilters.filterLabels.value
log field is mapped to the
entity.asset.attribute.labels.%{resource.data.metadataFilters.filterLabels.name}
UDM field.
resource.data.metadataFilters.filterLabels.value
entity.asset.attribute.labels[metadata_filters_filter_labels_value]
Iterate through
resource.data.metadataFilters.filterLabels.name
,
If the
resource.data.metadataFilters.filterLabels.name
log field value is
not
empty then,
resource.data.metadataFilters.filterLabels.value
log field is mapped to the
entity.asset.attribute.labels.%{resource.data.metadataFilters.filterLabels.name}
UDM field.
resource.data.metadataFilters.filterMatchCriteria
entity.asset.attribute.labels[metadata_filters_filter_match_criteria]
Iterate through
resource.data.metadataFilters.filterMatchCriteria
,
If the
resource.data.metadataFilters.filterMatchCriteria
log field value is
not
empty then,
resource.data.metadataFilters.filterMatchCriteria
log field is mapped to the
entity.asset.attribute.labels.metadata_filters_filter_match
criteria
%{index}
UDM field.
resource.data.metadata.fingerprint
entity.asset.attribute.labels[metadata_fingerprint]
resource.data.properties.metadata.fingerprint
entity.asset.attribute.labels[metadata_fingerprint]
resource.data.metadata.items.key
entity.asset.attribute.labels[metadata_items_key]
Iterate through
resource.data.metadata.items.key
,
If the
resource.data.metadata.items.key
log field value is
not
empty then,
resource.data.metadata.items.value
log field is mapped to the
entity.asset.attribute.labels.%{resource.data.metadata.items.key}
UDM field.
Iterate through
resource.data.properties.metadata.items.key
,
If the
resource.data.properties.metadata.items.key
log field value is
not
empty then,
resource.data.properties.metadata.items.value
log field is mapped to the
entity.asset.attribute.labels.%{resource.data.properties.metadata.items.key}
UDM field.
resource.data.properties.metadata.items.key
entity.asset.attribute.labels[metadata_items_key]
Iterate through
resource.data.metadata.items.key
,
If the
resource.data.metadata.items.key
log field value is
not
empty then,
resource.data.metadata.items.value
log field is mapped to the
entity.asset.attribute.labels.%{resource.data.metadata.items.key}
UDM field.
Iterate through
resource.data.properties.metadata.items.key
,
If the
resource.data.properties.metadata.items.key
log field value is
not
empty then,
resource.data.properties.metadata.items.value
log field is mapped to the
entity.asset.attribute.labels.%{resource.data.properties.metadata.items.key}
UDM field.
resource.data.metadata.kind
entity.asset.attribute.labels[metadata_kind]
resource.data.properties.metadata.kind
entity.asset.attribute.labels[metadata_kind]
resource.data.metadatas
entity.asset.attribute.labels[metadatas]
resource.data.networkPerformanceConfig.totalEgressBandwidthTier
entity.asset.attribute.labels[network_performance_config_total_egress_bandwidth_tier]
resource.data.properties.networkPerformanceConfig.totalEgressBandwidthTier
entity.asset.attribute.labels[network_performance_config_total_egress_bandwidth_tier]
resource.data.nextHopVpnTunnel
entity.asset.attribute.labels[next_hop_vpn_tunnel]
resource.data.noAutomateDnsZone
entity.asset.attribute.labels[no_automate_dns_zone]
resource.data.options
entity.asset.attribute.labels[options]
resource.data.outlierDetection.baseEjectionTime.nanos
entity.asset.attribute.labels[outlier_detection_base_ejection_time_nanos]
resource.data.outlierDetection.baseEjectionTime.seconds
entity.asset.attribute.labels[outlier_detection_base_ejection_time_seconds]
resource.data.outlierDetection.consecutiveErrors
entity.asset.attribute.labels[outlier_detection_consecutive_errors]
resource.data.outlierDetection.consecutiveGatewayFailure
entity.asset.attribute.labels[outlier_detection_consecutive_gateway_failure]
resource.data.outlierDetection.enforcingConsecutiveErrors
entity.asset.attribute.labels[outlier_detection_enforcing_consecutive_errors]
resource.data.outlierDetection.enforcingConsecutiveGatewayFailure
entity.asset.attribute.labels[outlier_detection_enforcing_consecutive_gateway_failure]
resource.data.outlierDetection.enforcingSuccessRate
entity.asset.attribute.labels[outlier_detection_enforcing_success_rate]
resource.data.outlierDetection.interval.nanos
entity.asset.attribute.labels[outlier_detection_interval_nanos]
resource.data.outlierDetection.interval.seconds
entity.asset.attribute.labels[outlier_detection_interval_seconds]
resource.data.outlierDetection.maxEjectionPercent
entity.asset.attribute.labels[outlier_detection_max_ejection_percent]
resource.data.outlierDetection.successRateMinimumHosts
entity.asset.attribute.labels[outlier_detection_success_rate_minimum_hosts]
resource.data.outlierDetection.successRateRequestVolume
entity.asset.attribute.labels[outlier_detection_success_rate_request_volume]
resource.data.outlierDetection.successRateStdevFactor
entity.asset.attribute.labels[outlier_detection_success_rate_stdev_factor]
resource.data.physicalBlockSizeBytes
entity.asset.attribute.labels[physical_block_size_bytes]
resource.data.portRange
entity.asset.attribute.labels[port_range]
resource.data.properties.privateIpv6GoogleAccess
entity.asset.attribute.labels[private_ipv6_google_access]
resource.data.provisionedIops
entity.asset.attribute.labels[provisioned_iops]
resource.data.provisionedThroughput
entity.asset.attribute.labels[provisioned_throughput]
resource.data.proxyBind
entity.asset.attribute.labels[proxy_bind]
resource.data.pscConnectionId
entity.asset.attribute.labels[psc_connection_id]
resource.data.pscConnectionStatus
entity.asset.attribute.labels[psc_connection_status]
resource.data.rawDisk.containerType
entity.asset.attribute.labels[raw_disk_container_type]
resource.data.rawDisk.sha1Checksum
entity.asset.attribute.labels[raw_disk_sha1_checksum]
resource.data.rawDisk.source
entity.asset.attribute.labels[raw_disk_source]
resource.data.recommendedSize
entity.asset.attribute.labels[recommended_size]
resource.data.replicaZones
entity.asset.attribute.labels[replica_zones]
Iterate through
resource.data.replicaZones
,
If the
resource.data.replicaZones
log field value is
not
empty then,
resource.data.replicaZones
log field is mapped to the
entity.asset.attribute.labels.replica
zones
%{index}
UDM field.
resource.data.requestPath
entity.asset.attribute.labels[request_path]
resource.data.reservationAffinity.consumeReservationType
entity.asset.attribute.labels[reservation_affinity_consume_reservation_type]
resource.data.properties.reservationAffinity.consumeReservationType
entity.asset.attribute.labels[reservation_affinity_consume_reservation_type]
resource.data.reservationAffinity.key
entity.asset.attribute.labels[reservation_affinity_key]
resource.data.properties.reservationAffinity.key
entity.asset.attribute.labels[reservation_affinity_key]
resource.data.reservationAffinity.values
entity.asset.attribute.labels[reservation_affinity_values]
resource.data.properties.reservationAffinity.values
entity.asset.attribute.labels[reservation_affinity_values]
resource.data.resourceStatus.asyncPrimaryDisk.state
entity.asset.attribute.labels[resource_status_async_primary_disk_state]
resource.data.resourceStatus.physicalHost
entity.asset.attribute.labels[resource_status_physical_host]
resource.data.routeStatus
entity.asset.attribute.labels[route_status]
resource.data.routeType
entity.asset.attribute.labels[route_type]
resource.data.ruleTupleCount
entity.asset.attribute.labels[rule_tuple_count]
resource.data.scalingScheduleStatus.lastStartTime
entity.asset.attribute.labels[scaling_schedule_status_last_start_time]
resource.data.scalingScheduleStatus.nextStartTime
entity.asset.attribute.labels[scaling_schedule_status_next_start_time]
resource.data.scalingScheduleStatus.state
entity.asset.attribute.labels[scaling_schedule_status_state]
resource.data.scheduling.automaticRestart
entity.asset.attribute.labels[scheduling_automatic_restart]
resource.data.properties.scheduling.automaticRestart
entity.asset.attribute.labels[scheduling_automatic_restart]
resource.data.scheduling.instanceTerminationAction
entity.asset.attribute.labels[scheduling_instance_termination_action]
resource.data.properties.scheduling.instanceTerminationAction
entity.asset.attribute.labels[scheduling_instance_termination_action]
resource.data.scheduling.locationHint
entity.asset.attribute.labels[scheduling_location_hint]
resource.data.properties.scheduling.locationHint
entity.asset.attribute.labels[scheduling_location_hint]
resource.data.scheduling.minNodeCpus
entity.asset.attribute.labels[scheduling_min_node_cpus]
resource.data.properties.scheduling.minNodeCpus
entity.asset.attribute.labels[scheduling_min_node_cpus]
resource.data.scheduling.nodeAffinities.key
entity.asset.attribute.labels[scheduling_node_affinities_key]
resource.data.properties.scheduling.nodeAffinities.key
entity.asset.attribute.labels[scheduling_node_affinities_key]
resource.data.scheduling.nodeAffinities.operator
entity.asset.attribute.labels[scheduling_node_affinities_operator]
resource.data.properties.scheduling.nodeAffinities.operator
entity.asset.attribute.labels[scheduling_node_affinities_operator]
resource.data.scheduling.nodeAffinities.values
entity.asset.attribute.labels[scheduling_node_affinities_values]
resource.data.properties.scheduling.nodeAffinities.values
entity.asset.attribute.labels[scheduling_node_affinities_values]
resource.data.scheduling.onHostMaintenance
entity.asset.attribute.labels[scheduling_on_host_maintenance]
resource.data.properties.scheduling.onHostMaintenance
entity.asset.attribute.labels[scheduling_on_host_maintenance]
resource.data.scheduling.preemptible
entity.asset.attribute.labels[scheduling_preemptible]
resource.data.properties.scheduling.preemptible
entity.asset.attribute.labels[scheduling_preemptible]
resource.data.scheduling.provisioningModel
entity.asset.attribute.labels[scheduling_provisioning_model]
resource.data.properties.scheduling.provisioningModel
entity.asset.attribute.labels[scheduling_provisioning_model]
resource.data.securityPolicy
entity.asset.attribute.labels[security_policy]
resource.data.securitySettings.clientTlsPolicy
entity.asset.attribute.labels[security_settings_client_tls_policy]
resource.data.securitySettings.subjectAltNames
entity.asset.attribute.labels[security_settings_subject_alt_names]
Iterate through
resource.data.securitySettings.subjectAltNames
,
If the
resource.data.securitySettings.subjectAltNames
log field value is
not
empty then,
resource.data.securitySettings.subjectAltNames
log field is mapped to the
entity.asset.attribute.labels.security_settings_subject_alt
names
%{index}
UDM field.
resource.data.serviceAccounts.email
relations.entity.user.email_addresses
resource.data.properties.serviceAccounts.email
relations.entity.user.email_addresses
relations.entity.user.account_type
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
resource.data.serviceAccounts.scopes
relations.entity.user.attribute.labels[service_accounts_scopes]
resource.data.properties.serviceAccounts.scopes
relations.entity.user.attribute.labels[service_accounts_scopes]
resource.data.serviceBindings
entity.asset.attribute.labels[service_bindings]
Iterate through
resource.data.serviceBindings
,
If the
resource.data.serviceBindings
log field value is
not
empty then,
resource.data.serviceBindings
log field is mapped to the
entity.asset.attribute.labels.service
bindings
%{index}
UDM field.
resource.data.serviceDirectoryRegistrations.namespace
entity.asset.attribute.labels[service_irectory_egistrations_namespace]
Iterate through
resource.data.serviceDirectoryRegistrations.namespace
,
If the
resource.data.serviceDirectoryRegistrations.namespace
log field value is
not
empty then,
resource.data.serviceDirectoryRegistrations.namespace
log field is mapped to the
entity.asset.attribute.labels.service_directory_registrations
namespace
%{index}
UDM field.
resource.data.serviceDirectoryRegistrations.serviceDirectoryRegion
entity.asset.attribute.labels[service_irectory_egistrations_service_directory_region]
Iterate through
resource.data.serviceDirectoryRegistrations.serviceDirectoryRegion
,
If the
resource.data.serviceDirectoryRegistrations.serviceDirectoryRegion
log field value is
not
empty then,
resource.data.serviceDirectoryRegistrations.serviceDirectoryRegion
log field is mapped to the
entity.asset.attribute.labels.service_directory_registrations_service_directory
region
%{index}
UDM field.
resource.data.serviceDirectoryRegistrations.service
entity.asset.attribute.labels[service_irectory_egistrations_service]
Iterate through
resource.data.serviceDirectoryRegistrations.service
,
If the
resource.data.serviceDirectoryRegistrations.service
log field value is
not
empty then,
resource.data.serviceDirectoryRegistrations.service
log field is mapped to the
entity.asset.attribute.labels.service_directory_registrations
service
%{index}
UDM field.
resource.data.serviceLabel
entity.asset.attribute.labels[service_label]
resource.data.sessionAffinity
entity.asset.attribute.labels[session_affinity]
resource.data.shieldedInstanceConfig.enableIntegrityMonitoring
entity.asset.attribute.labels[shielded_instance_config_enable_integrity_monitoring]
resource.data.properties.shieldedInstanceConfig.enableIntegrityMonitoring
entity.asset.attribute.labels[shielded_instance_config_enable_integrity_monitoring]
resource.data.shieldedInstanceConfig.enableSecureBoot
entity.asset.attribute.labels[shielded_instance_config_enable_secure_boot]
resource.data.properties.shieldedInstanceConfig.enableSecureBoot
entity.asset.attribute.labels[shielded_instance_config_enable_secure_boot]
resource.data.shieldedInstanceConfig.enableVtpm
entity.asset.attribute.labels[shielded_instance_config_enable_vtpm]
resource.data.properties.shieldedInstanceConfig.enableVtpm
entity.asset.attribute.labels[shielded_instance_config_enable_vtpm]
resource.data.shieldedInstanceInitialState.dbs.content
entity.asset.attribute.labels[shielded_instance_initial_state_dbs_content]
Iterate through
resource.data.shieldedInstanceInitialState.dbs.content
,
If the
resource.data.shieldedInstanceInitialState.dbs.content
log field value is
not
empty then,
resource.data.shieldedInstanceInitialState.dbs.content
log field is mapped to the
entity.asset.attribute.labels.shielded_instance_initial_state_dbs
content
%{index}
UDM field.
resource.data.shieldedInstanceInitialState.dbs.fileType
entity.asset.attribute.labels[shielded_instance_initial_state_dbs_file_type]
Iterate through
resource.data.shieldedInstanceInitialState.dbs.fileType
,
If the
resource.data.shieldedInstanceInitialState.dbs.fileType
log field value is
not
empty then,
resource.data.shieldedInstanceInitialState.dbs.fileType
log field is mapped to the
entity.asset.attribute.labels.shielded_instance_initial_state_dbs_file
type
%{index}
UDM field.
resource.data.shieldedInstanceInitialState.dbxs.content
entity.asset.attribute.labels[shielded_instance_initial_state_dbxs_content]
Iterate through
resource.data.shieldedInstanceInitialState.dbxs.content
,
If the
resource.data.shieldedInstanceInitialState.dbxs.content
log field value is
not
empty then,
resource.data.shieldedInstanceInitialState.dbxs.content
log field is mapped to the
entity.asset.attribute.labels.shielded_instance_initial_state_dbxs
content
%{index}
UDM field.
resource.data.shieldedInstanceInitialState.dbxs.fileType
entity.asset.attribute.labels[shielded_instance_initial_state_dbxs_file_type]
Iterate through
resource.data.shieldedInstanceInitialState.dbxs.fileType
,
If the
resource.data.shieldedInstanceInitialState.dbxs.fileType
log field value is
not
empty then,
resource.data.shieldedInstanceInitialState.dbxs.fileType
log field is mapped to the
entity.asset.attribute.labels.shielded_instance_initial_state_dbxs_file
type
%{index}
UDM field.
resource.data.shieldedInstanceInitialState.keks.content
entity.asset.attribute.labels[shielded_instance_initial_state_keks_content]
Iterate through
resource.data.shieldedInstanceInitialState.keks.content
,
If the
resource.data.shieldedInstanceInitialState.keks.content
log field value is
not
empty then,
resource.data.shieldedInstanceInitialState.keks.content
log field is mapped to the
entity.asset.attribute.labels.shielded_instance_initial_state_keks
content
%{index}
UDM field.
resource.data.shieldedInstanceInitialState.keks.fileType
entity.asset.attribute.labels[shielded_instance_initial_state_keks_file_type]
Iterate through
resource.data.shieldedInstanceInitialState.keks.fileType
,
If the
resource.data.shieldedInstanceInitialState.keks.fileType
log field value is
not
empty then,
resource.data.shieldedInstanceInitialState.keks.fileType
log field is mapped to the
entity.asset.attribute.labels.shielded_instance_initial_state_keks_file
type
%{index}
UDM field.
resource.data.shieldedInstanceInitialState.pk.content
entity.asset.attribute.labels[shielded_instance_initial_state_pk_content]
resource.data.shieldedInstanceInitialState.pk.fileType
entity.asset.attribute.labels[shielded_instance_initial_state_pk_file_type]
resource.data.shieldedInstanceIntegrityPolicy.updateAutoLearnPolicy
entity.asset.attribute.labels[shielded_instance_integrity_policy_update_auto_learn_policy]
resource.data.shortName
entity.asset.attribute.labels[short_name]
resource.data.sourceDiskEncryptionKey.sha256
entity.asset.attribute.labels[source_disk_encryption_key_sha256]
resource.data.sourceDiskEncryptionKey.kmsKeyName
entity.asset.attribute.labels[source_disk_encryption_kms_key_name]
resource.data.sourceDiskEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[source_disk_encryption_kms_key_service_account]
resource.data.sourceDiskEncryptionKey.rawKey
entity.asset.attribute.labels[source_disk_encryption_raw_key]
resource.data.sourceDiskEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[source_disk_encryption_rsa_encrypted_key]
resource.data.sourceDiskId
entity.asset.attribute.labels[source_disk_id]
resource.data.sourceDisk
entity.asset.attribute.labels[source_disk]
resource.data.sourceImageEncryptionKey.sha256
entity.asset.attribute.labels[source_image_encryption_key_sha256]
resource.data.sourceImageEncryptionKey.kmsKeyName
entity.asset.attribute.labels[source_image_encryption_kms_key_name]
resource.data.sourceImageEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[source_image_encryption_kms_key_service_account]
resource.data.sourceImageEncryptionKey.rawKey
entity.asset.attribute.labels[source_image_encryption_raw_key]
resource.data.sourceImageEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[source_image_encryption_rsa_encrypted_key]
resource.data.sourceImageId
entity.asset.attribute.labels[source_image_id]
resource.data.sourceImage
entity.asset.attribute.labels[source_image]
resource.data.sourceIpRanges
entity.asset.attribute.labels[source_ip_ranges]
Iterate through
resource.data.sourceIpRanges
,
If the
resource.data.sourceIpRanges
log field value is
not
empty then,
resource.data.sourceIpRanges
log field is mapped to the
entity.asset.attribute.labels.source_ip
ranges
%{index}
UDM field.
resource.data.sourceMachineImageEncryptionKey.kmsKeyName
entity.asset.attribute.labels[source_machine_image_encryption_key_kms_key_name]
resource.data.sourceMachineImageEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[source_machine_image_encryption_key_kms_key_service_account]
resource.data.sourceMachineImageEncryptionKey.rawKey
entity.asset.attribute.labels[source_machine_image_encryption_key_raw_key]
resource.data.sourceMachineImageEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[source_machine_image_encryption_key_rsa_encrypted_key]
resource.data.sourceMachineImageEncryptionKey.sha256
entity.asset.attribute.labels[source_machine_image_encryption_key_sha256]
resource.data.sourceMachineImage
entity.asset.attribute.labels[source_machine_image]
resource.data.sourceRanges
entity.asset.attribute.labels[source_ranges]
Iterate through
resource.data.sourceRanges
,
If the
resource.data.sourceRanges
log field value is
not
empty then,
resource.data.sourceRanges
log field is mapped to the
entity.asset.attribute.labels.source
ranges
%{index}
UDM field.
resource.data.sourceServiceAccounts
entity.asset.attribute.labels[source_service_accounts]
Iterate through
resource.data.sourceServiceAccounts
,
If the
resource.data.sourceServiceAccounts
log field value is
not
empty then,
resource.data.sourceServiceAccounts
log field is mapped to the
entity.asset.attribute.labels.source_service
accounts
%{index}
UDM field.
resource.data.sourceSnapshotEncryptionKey.sha256
entity.asset.attribute.labels[source_snapshot_encryption_key_sha256]
resource.data.sourceSnapshotEncryptionKey.kmsKeyName
entity.asset.attribute.labels[source_snapshot_encryption_kms_key_name]
resource.data.sourceSnapshotEncryptionKey.kmsKeyServiceAccount
entity.asset.attribute.labels[source_snapshot_encryption_kms_key_service_account]
resource.data.sourceSnapshotEncryptionKey.rawKey
entity.asset.attribute.labels[source_snapshot_encryption_raw_key]
resource.data.sourceSnapshotEncryptionKey.rsaEncryptedKey
entity.asset.attribute.labels[source_snapshot_encryption_rsa_encrypted_key]
resource.data.sourceTags
entity.asset.attribute.labels[source_tags]
Iterate through
resource.data.sourceTags
,
If the
resource.data.sourceTags
log field value is
not
empty then,
resource.data.sourceTags
log field is mapped to the
entity.asset.attribute.labels.source
tags
%{index}
UDM field.
resource.data.sourceType
entity.asset.attribute.labels[source_type]
resource.data.startRestricted
entity.asset.attribute.labels[start_restricted]
resource.data.statefulPolicy.preservedState.disks.autoDelete
entity.security_result.rule_labels[stateful_policy_preserved_state_disks_auto_delete]
resource.data.status.autoscaler
entity.asset.attribute.labels[status_autoscaler]
resource.data.statusDetails.message
entity.asset.attribute.labels[status_details_message]
Iterate through
resource.data.statusDetails.message
,
If the
resource.data.statusDetails.message
log field value is
not
empty then,
resource.data.statusDetails.message
log field is mapped to the
entity.asset.attribute.labels.status_details
message
%{index}
UDM field.
resource.data.statusDetails.type
entity.asset.attribute.labels[status_details_type]
Iterate through
resource.data.statusDetails.type
,
If the
resource.data.statusDetails.type
log field value is
not
empty then,
resource.data.statusDetails.type
log field is mapped to the
entity.asset.attribute.labels.status_details
type
%{index}
UDM field.
resource.data.status.isStable
entity.asset.attribute.labels[status_is_stable]
resource.data.statusMessage
entity.asset.attribute.labels[status_message]
resource.data.status.stateful.hasStatefulConfig
entity.asset.attribute.labels[status_stateful_has_stateful_config]
resource.data.status.stateful.perInstanceConfigs.allEffective
entity.asset.attribute.labels[status_stateful_per_instance_configs_all_effective]
resource.data.status.versionTarget.isReached
entity.asset.attribute.labels[status_version_target_is_reached]
resource.data.subsetting.policy
entity.asset.attribute.labels[subsetting_policy]
resource.data.tags.fingerprint
entity.asset.attribute.labels[tags_fingerprint]
resource.data.properties.tags.fingerprint
entity.asset.attribute.labels[tags_fingerprint]
resource.data.tags.items
entity.asset.attribute.labels[tags_items]
Iterate through
resource.data.tags.items
,
If the
resource.data.tags.items
log field value is
not
empty then,
resource.data.tags.items
log field is mapped to the
entity.asset.attribute.labels.tags
items
%{index}
UDM field.
Iterate through
resource.data.properties.tags.items
,
If the
resource.data.properties.tags.items
log field value is
not
empty then,
resource.data.properties.tags.items
log field is mapped to the
entity.asset.attribute.labels.tags
items
%{index}
UDM field.
resource.data.properties.tags.items
entity.asset.attribute.labels[tags_items]
Iterate through
resource.data.tags.items
,
If the
resource.data.tags.items
log field value is
not
empty then,
resource.data.tags.items
log field is mapped to the
entity.asset.attribute.labels.tags
items
%{index}
UDM field.
Iterate through
resource.data.properties.tags.items
,
If the
resource.data.properties.tags.items
log field value is
not
empty then,
resource.data.properties.tags.items
log field is mapped to the
entity.asset.attribute.labels.tags
items
%{index}
UDM field.
resource.data.targetPools
entity.asset.attribute.labels[target_pools]
Iterate through
resource.data.targetPools
,
If the
resource.data.targetPools
log field value is
not
empty then,
resource.data.targetPools
log field is mapped to the
entity.asset.attribute.labels.target
pools
%{index}
UDM field.
resource.data.targetServiceAccounts
entity.asset.attribute.labels[target_service_accounts]
Iterate through
resource.data.targetServiceAccounts
,
If the
resource.data.targetServiceAccounts
log field value is
not
empty then,
resource.data.targetServiceAccounts
log field is mapped to the
entity.asset.attribute.labels.target_service
accounts
%{index}
UDM field.
resource.data.targetService
entity.asset.attribute.labels[target_service]
resource.data.targetSize
entity.asset.attribute.labels[target_size]
resource.data.targetTags
entity.asset.attribute.labels[target_tags]
Iterate through
resource.data.targetTags
,
If the
resource.data.targetTags
log field value is
not
empty then,
resource.data.targetTags
log field is mapped to the
entity.asset.attribute.labels.target
tags
%{index}
UDM field.
resource.data.updatePolicy.instanceRedistributionType
entity.security_result.rule_labels[update_policy_instance_redistribution_type]
resource.data.updatePolicy.maxSurge.calculated
entity.security_result.rule_labels[update_policy_max_surge_calculated]
resource.data.updatePolicy.maxSurge.fixed
entity.security_result.rule_labels[update_policy_max_surge_fixed]
resource.data.updatePolicy.maxSurge.percent
entity.security_result.rule_labels[update_policy_max_surge_percent]
resource.data.updatePolicy.maxUnavailable.calculated
entity.security_result.rule_labels[update_policy_max_unavailable_calculated]
resource.data.updatePolicy.maxUnavailable.fixed
entity.security_result.rule_labels[update_policy_max_unavailable_fixed]
resource.data.updatePolicy.maxUnavailable.percent
entity.security_result.rule_labels[update_policy_max_unavailable_percent]
resource.data.updatePolicy.minimalAction
entity.security_result.rule_labels[update_policy_minimal_action]
resource.data.updatePolicy.mostDisruptiveAllowedAction
entity.security_result.rule_labels[update_policy_most_disruptive_allowed_action]
resource.data.updatePolicy.replacementMethod
entity.security_result.rule_labels[update_policy_replacement_method]
resource.data.updatePolicy.type
entity.security_result.rule_labels[update_policy_type]
resource.data.domainNames
entity.asset.attribute.labels[domain_name]
Iterate through
resource.data.domainNames
,
If the
resource.data.domainNames
log field value is
not
empty then,
resource.data.domainNames
log field is mapped to the
entity.asset.attribute.labels.domain
name
%{index}
UDM field.
resource.data.baseInstanceName
entity.asset.attribute.labels[base_instance_name]
resource.data.id
entity.asset.product_object_id
resource.data.rules.action
entity.security_result.action_details
resource.data.warnings.message
entity.security_result.description
resource.data.warnings.key
entity.security_result.detection_fields [warnings_key]
resource.data.warnings.data.key
entity.security_result.detection_fields [warnings_data_key]
Iterate through
resource.data.warnings.data.value
,
If the
resource.data.warnings.data.value
log field value is
not
empty then,
resource.data.warnings.data.value
log field is mapped to the
entity.security_result.detection_fields .%{resource.data.warnings.data.key}
UDM field.
resource.data.warnings.data.value
entity.security_result.detection_fields [warnings_data_key]
Iterate through
resource.data.warnings.data.value
,
If the
resource.data.warnings.data.value
log field value is
not
empty then,
resource.data.warnings.data.value
log field is mapped to the
entity.security_result.detection_fields .%{resource.data.warnings.data.key}
UDM field.
resource.data.warnings.code
entity.security_result.detection_fields [code]
resource.data.priority
entity.security_result.priority_details
resource.data.rules.priority
entity.security_result.priority_details
resource.data.collectorIlb.canonicalUrl
entity.security_result.rule_id
resource.data.sourceSnapshotSchedulePolicyId
entity.security_result.rule_id
resource.data.asyncPrimaryDisk.consistencyGroupPolicyId
entity.security_result.rule_id
resource.data.sourceConsistencyGroupPolicyId
entity.security_result.rule_id
resource.data.rules.match.config.srcIpRanges
entity.security_result.rule_labels[config_srcIp_ranges]
Iterate through
resource.data.rules.match.config.srcIpRanges
,
If the
resource.data.rules.match.config.srcIpRanges
log field value is
not
empty then,
resource.data.rules.match.config.srcIpRanges
log field is mapped to the
entity.security_result.rule_labels.rules_match_config_srcIp
ranges
%{index}
UDM field.
resource.data.rules.match.expr.description
entity.security_result.rule_labels[rule_match_expression_desciption]
resource.data.rules.match.expr.location
entity.security_result.rule_labels[rule_match_expression_location]
resource.data.rules.match.expr.title
entity.security_result.rule_labels[rule_match_expression_title]
resource.data.rules.match.expr.expression
entity.security_result.rule_labels[rule_match_expression]
resource.data.rules.headerAction.requestHeadersToAdds.headerName
entity.security_result.rule_labels[header_action_request_headers_to_adds_header_name]
Iterate through
resource.data.rules.headerAction.requestHeadersToAdds
,
If the
resource.data.rules.headerAction.requestHeadersToAdds.headerName
log field value is
not
empty then,
resource.data.rules.headerAction.requestHeadersToAdds.headerName
log field is mapped to the
entity.security_result.rule_labels.header_action_request_headers_to_adds_header
name
%{index}
UDM field.
resource.data.rules.headerAction.requestHeadersToAdds.headerValue
entity.security_result.rule_labels[header_action_request_headers_to_adds_header_value]
Iterate through
resource.data.rules.headerAction.requestHeadersToAdds
,
If the
resource.data.rules.headerAction.requestHeadersToAdds.headerValue
log field value is
not
empty then,
resource.data.rules.headerAction.requestHeadersToAdds.headerValue
log field is mapped to the
entity.security_result.rule_labels.header_action_request_headers_to_adds_header
value
%{index}
UDM field.
resource.data.rules.kind
entity.security_result.rule_labels[rule_kind]
resource.data.rules.preconfiguredWafConfig.exclusions.requestCookiesToExclude.op
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_cookies_to_exclude_op]
resource.data.rules.preconfiguredWafConfig.exclusions.requestCookiesToExclude.val
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_cookies_to_exclude_val]
resource.data.rules.preconfiguredWafConfig.exclusions.requestHeadersToExclude.op
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_header_to_exclude_op]
resource.data.rules.preconfiguredWafConfig.exclusions.requestHeadersToExclude.val
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_header_to_exclude_val]
resource.data.rules.preconfiguredWafConfig.exclusions.requestQueryParamsToExclude.op
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_query_param_to_exclude_op]
resource.data.rules.preconfiguredWafConfig.exclusions.requestQueryParamsToExclude.val
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_query_param_to_exclude_val]
resource.data.rules.preconfiguredWafConfig.exclusions.requestUrisToExclude.op
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_uris_to_exclude_op]
resource.data.rules.preconfiguredWafConfig.exclusions.requestUrisToExclude.val
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_req_uris_to_exclude_val]
resource.data.rules.preconfiguredWafConfig.exclusions.targetRuleIds
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_target_rule_id]
resource.data.rules.preconfiguredWafConfig.exclusions.targetRuleSet
entity.security_result.rule_labels[rule_preconfigured_wafconfig_execusion_target_rule_set]
resource.data.rules.preview
entity.security_result.rule_labels[rule_preview]
resource.data.rules.rateLimitOptions.banDurationSec
entity.security_result.rule_labels[rate_limit_options_ban_duration_sec]
resource.data.rules.rateLimitOptions.banThreshold.count
entity.security_result.rule_labels[rate_limit_options_ban_threshold_count]
resource.data.rules.rateLimitOptions.banThreshold.intervalSec
entity.security_result.rule_labels[rate_limit_options_ban_threshold_intervalsec]
resource.data.rules.rateLimitOptions.conformAction
entity.security_result.rule_labels[rate_limit_options_conform_action]
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs.enforceOnKeyType
entity.security_result.rule_labels[rate_limit_options_enforce_on_key_config_enforce_on_key_type]
Iterate through
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs
,
If the
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs.enforceOnKeyType
log field value is
not
empty then,
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs.enforceOnKeyType
log field is mapped to the
entity.security_result.rule_labels.rate_limit_options_enforce_on_key_config_enforce_on_key
type
%{index}
UDM field.
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs.enforceOnKeyName
entity.security_result.rule_labels[rate_limit_options_enforce_on_key_config_enforce_on_key_name]
Iterate through
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs
,
If the
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs.enforceOnKeyName
log field value is
not
empty then,
resource.data.rules.rateLimitOptions.enforceOnKeyConfigs.enforceOnKeyName
log field is mapped to the
entity.security_result.rule_labels.rate_limit_options_enforce_on_key_config_enforce_on_key
name
%{index}
UDM field.
resource.data.rules.rateLimitOptions.enforceOnKeyName
entity.security_result.rule_labels[rate_limit_options_enforce_on_key_name]
resource.data.rules.rateLimitOptions.enforceOnKey
entity.security_result.rule_labels[rate_limit_options_enforce_on_key]
resource.data.rules.rateLimitOptions.exceedAction
entity.security_result.rule_labels[rate_limit_options_exceed_action]
resource.data.rules.rateLimitOptions.exceedRedirectOptions.target
entity.security_result.rule_labels[rate_limit_options_exceed_redirection_options_target]
resource.data.rules.rateLimitOptions.exceedRedirectOptions.type
entity.security_result.rule_labels[rate_limit_options_exceed_redirection_options_type]
resource.data.rules.rateLimitOptions.rateLimitThreshold.count
entity.security_result.rule_labels[rate_limit_options_rate_limit_threshold_count]
resource.data.rules.rateLimitOptions.rateLimitThreshold.intervalSec
entity.security_result.rule_labels[rate_limit_options_rate_limit_threshold_intervalsec]
resource.data.rules.redirectOptions.target
entity.security_result.rule_labels[rule_redirection_option_target]
resource.data.rules.redirectOptions.type
entity.security_result.rule_labels[rule_redirection_option_type]
resource.data.rules.match.versionedExpr
entity.security_result.rule_labels[rule_match_versioned_expr]
resource.data.rules.description
entity.security_result.rule_labels[rules_description]
resource.data.rules.direction
entity.security_result.rule_labels[rules_direction]
resource.data.rules.disabled
entity.security_result.rule_labels[rules_disabled]
resource.data.rules.enableLogging
entity.security_result.rule_labels[rules_enable_logging]
resource.data.rules.match.destAddressGroups
entity.security_result.rule_labels[rules_match_dest_address_groups]
Iterate through
resource.data.rules.match.destAddressGroups
,
If the
resource.data.rules.match.destAddressGroups
log field value is
not
empty then,
resource.data.rules.match.destAddressGroups
log field is mapped to the
entity.security_result.rule_labels.rules_match_dest_address
groups
%{index}
UDM field.
resource.data.rules.match.destFqdns
entity.security_result.rule_labels[rules_match_dest_fqdns]
Iterate through
resource.data.rules.match.destFqdns
,
If the
resource.data.rules.match.destFqdns
log field value is
not
empty then,
resource.data.rules.match.destFqdns
log field is mapped to the
entity.security_result.rule_labels.rules_match_dest
fqdns
%{index}
UDM field.
resource.data.rules.match.destIpRanges
entity.security_result.rule_labels[rules_match_dest_ip_ranges]
Iterate through
resource.data.rules.match.destIpRanges
,
If the
resource.data.rules.match.destIpRanges
log field value is
not
empty then,
resource.data.rules.match.destIpRanges
log field is mapped to the
entity.security_result.rule_labels.rules_match_dest_ip
ranges
%{index}
UDM field.
resource.data.rules.match.destRegionCodes
entity.security_result.rule_labels[rules_match_dest_region_codes]
Iterate through
resource.data.rules.match.destRegionCodes
,
If the
resource.data.rules.match.destRegionCodes
log field value is
not
empty then,
resource.data.rules.match.destRegionCodes
log field is mapped to the
entity.security_result.rule_labels.rules_match_dest_region
codes
%{index}
UDM field.
resource.data.rules.match.destThreatIntelligences
entity.security_result.rule_labels[rules_match_dest_threat_intelligences]
Iterate through
resource.data.rules.match.destThreatIntelligences
,
If the
resource.data.rules.match.destThreatIntelligences
log field value is
not
empty then,
resource.data.rules.match.destThreatIntelligences
log field is mapped to the
entity.security_result.rule_labels.rules_match_dest_threat
intelligences
%{index}
UDM field.
resource.data.rules.match.layer4Configs.ipProtocol
entity.security_result.rule_labels[rules_match_layer4_configs_ip_protocol]
Iterate through
resource.data.rules.match.layer4Configs
,
If the
resource.data.rules.match.layer4Configs.ipProtocol
log field value is
not
empty then,
resource.data.rules.match.layer4Configs.ipProtocol
log field is mapped to the
entity.security_result.rule_labels.rules_match_layer4_configs_ip
protocol
%{index}
UDM field.
resource.data.rules.match.layer4Configs.ports
entity.security_result.rule_labels[rules_match_layer4_configs_ports]
Iterate through
resource.data.rules.match.destIpRanges
,
If the
resource.data.rules.match.destIpRanges
log field value is
not
empty then,
resource.data.rules.match.destIpRanges
log field is mapped to the
entity.security_result.rule_labels.rules_match_layer4_configs
ports
%{index}
UDM field.
resource.data.rules.match.srcAddressGroups
entity.security_result.rule_labels[rules_match_src_address_groups]
Iterate through
resource.data.rules.match.srcAddressGroups
,
If the
resource.data.rules.match.srcAddressGroups
log field value is
not
empty then,
resource.data.rules.match.srcAddressGroups
log field is mapped to the
entity.security_result.rule_labels.rules_match_src_address
groups
%{index}
UDM field.
resource.data.rules.match.srcFqdns
entity.security_result.rule_labels[rules_match_src_fqdns]
Iterate through
resource.data.rules.match.srcFqdns
,
If the
resource.data.rules.match.srcFqdns
log field value is
not
empty then,
resource.data.rules.match.srcFqdns
log field is mapped to the
entity.security_result.rule_labels.rules_match_src
fqdns
%{index}
UDM field.
resource.data.rules.match.srcIpRanges
entity.security_result.rule_labels[rules_match_src_ip_ranges]
Iterate through
resource.data.rules.match.srcIpRanges
,
If the
resource.data.rules.match.srcIpRanges
log field value is
not
empty then,
resource.data.rules.match.srcIpRanges
log field is mapped to the
entity.security_result.rule_labels.rules_match_src_ip
ranges
%{index}
UDM field.
resource.data.rules.match.srcRegionCodes
entity.security_result.rule_labels[rules_match_src_region_codes]
Iterate through
resource.data.rules.match.srcRegionCodes
,
If the
resource.data.rules.match.srcRegionCodes
log field value is
not
empty then,
resource.data.rules.match.srcRegionCodes
log field is mapped to the
entity.security_result.rule_labels.rules_match_src_region
codes
%{index}
UDM field.
resource.data.rules.match.srcSecureTags.name
entity.security_result.rule_labels[rules_match_src_secure_tags_name]
Iterate through
resource.data.rules.match.srcSecureTags
,
If the
resource.data.rules.match.srcSecureTags.name
log field value is
not
empty then,
resource.data.rules.match.srcSecureTags.name
log field is mapped to the
entity.security_result.rule_labels.rules_match_src_secure_tags
name
%{index}
UDM field.
resource.data.rules.match.srcSecureTags.state
entity.security_result.rule_labels[rules_match_src_secure_tags_state]
Iterate through
resource.data.rules.match.srcSecureTags
,
If the
resource.data.rules.match.srcSecureTags.state
log field value is
not
empty then,
resource.data.rules.match.srcSecureTags.state
log field is mapped to the
entity.security_result.rule_labels.rules_match_src_secure_tags
state
%{index}
UDM field.
resource.data.rules.match.srcThreatIntelligences
entity.security_result.rule_labels[rules_match_src_threat_intelligences]
Iterate through
resource.data.rules.match.srcThreatIntelligences
,
If the
resource.data.rules.match.srcThreatIntelligences
log field value is
not
empty then,
resource.data.rules.match.srcThreatIntelligences
log field is mapped to the
entity.security_result.rule_labels.rules_match_src_threat
intelligences
%{index}
UDM field.
resource.data.rules.ruleTupleCount
entity.security_result.rule_labels[rules_rule_tuple_count]
Iterate through
resource.data.rules.match.ruleTupleCount
,
If the
resource.data.rules.match.ruleTupleCount
log field value is
not
empty then,
resource.data.rules.match.ruleTupleCount
log field is mapped to the
entity.security_result.rule_labels.rules_rule_tuple
count
%{index}
UDM field.
resource.data.rules.targetSecureTags.name
entity.security_result.rule_labels[rules_target_secure_tags_name]
Iterate through
resource.data.rules.targetSecureTags
,
If the
resource.data.rules.targetSecureTags.name
log field value is
not
empty then,
resource.data.rules.targetSecureTags.name
log field is mapped to the
entity.security_result.rule_labels.rules_target_secure_tags
name
%{index}
UDM field.
resource.data.rules.targetSecureTags.state
entity.security_result.rule_labels[rules_target_secure_tags_state]
Iterate through
resource.data.rules.targetSecureTags
,
If the
resource.data.rules.targetSecureTags.state
log field value is
not
empty then,
resource.data.rules.targetSecureTags.state
log field is mapped to the
entity.security_result.rule_labels.rules_target_secure_tags
state
%{index}
UDM field.
resource.data.rules.targetServiceAccounts
entity.security_result.rule_labels[rules_target_service_accounts]
Iterate through
resource.data.rules.targetServiceAccounts
,
If the
resource.data.rules.targetServiceAccounts
log field value is
not
empty then,
resource.data.rules.targetServiceAccounts
log field is mapped to the
entity.security_result.rule_labels.rules_target_service
accounts
%{index}
UDM field.
resource.data.collectorIlb.url
entity.security_result.rule_name
resource.data.rules.ruleName
entity.security_result.rule_name
resource.data.sourceSnapshotSchedulePolicy
entity.security_result.rule_name
resource.data.serverTlsPolicy
entity.security_result.rule_name
resource.data.natPolicy
entity.security_result.rule_name
resource.data.authorizationPolicy
entity.security_result.rule_name
resource.data.serverTlsPolicy
entity.security_result.rule_name
resource.data.disks.initializeParams.resourcePolicies
entity.security_result.rule_name
resource.data.properties.disks.initializeParams.resourcePolicies
entity.security_result.rule_name
resource.data.resourcePolicies
entity.security_result.rule_name
resource.data.properties.resourcePolicies
entity.security_result.rule_name
resource.data.reservations.resourcePolicies
entity.security_result.rule_name
resource.data.asyncPrimaryDisk.consistencyGroupPolicy
entity.security_result.rule_name
resource.data.sourceConsistencyGroupPolicy
entity.security_result.rule_name
entity.security_result.rule_name
If the
resource.data.autoscalingPolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Auto Scaling Policy
.
If the
resource.data.autoHealingPolicies
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Auto Healing Policy
.
If the
resource.data.connectionTrackingPolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Connection Tracking Policy
.
If the
resource.data.cdnPolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
CDN Policy
.
If the
resource.data.statefulPolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Stateful Policy
.
If the
resource.data.snapshotSchedulePolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Snapshot Schedule Policy
.
If the
resource.data.instanceSchedulePolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Instance Schedule Policy
.
If the
resource.data.groupPlacementPolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Group Placement Policy
.
If the
resource.data.updatePolicy
log field value is
not
empty then, the
entity.security_result.rule_name
UDM field is set to
Update Policy for Managed Instance Group
.
resource.data.instanceGroup
entity.url
resource.data.backendService
entity.asset.attribute.labels[backend_service]
resource.data.networkInterfaces.networkIP
entity.asset.ip
resource.data.properties.networkInterfaces.networkIPresource.data.networkInterfaces.ipv6Address
entity.asset.ip
resource.data.properties.networkInterfaces.ipv6Addressresource.data.networkInterfaces.ipv6AccessConfigs.externalIpv6
entity.asset.ip
resource.data.properties.networkInterfaces.ipv6AccessConfigs.externalIpv6resource.data.networkInterfaces.accessConfigs.externalIpv6
entity.asset.ip
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6
entity.asset.ip
resource.data.interfaces.ipAddressresource.data.bgpPeers.peerIpAddressresource.data.interfaces.ipRangeresource.data.vpnInterfaces.ipAddressresource.data.peerIp
entity.asset.ip
resource.data.networkInterfaces.accessConfigs.natIP
entity.asset.nat_ip
resource.data.properties.networkInterfaces.accessConfigs.natIPresource.data.networkInterfaces.ipv6AccessConfigs.natIP
entity.asset.nat_ip
resource.data.properties.networkInterfaces.ipv6AccessConfigs.natIP
entity.asset.nat_ip
resource.data.connectedEndpoints.pscConnectionId
entity.asset.attribute.labels[connected_endpoint_psc_connection_id]
resource.data.bgp.advertiseMode
entity.asset.attribute.labels[advertise_mode]
resource.data.bgpPeers.advertisedGroups
entity.asset.attribute.labels[advertised_group]
Iterate through
resource.data.bgpPeers.advertisedGroups
,
If the
resource.data.bgpPeers.advertisedGroups
log field value is
not
empty then,
resource.data.bgpPeers.advertisedGroups
log field is mapped to the
entity.asset.attribute.labels.advertised
group
%{index}
UDM field.
resource.data.bgp.advertisedGroups
entity.asset.attribute.labels[advertised_groups]
Iterate through
resource.data.bgp.advertisedGroups
,
If the
resource.data.bgp.advertisedGroups
log field value is
not
empty then,
resource.data.bgp.advertisedGroups
log field is mapped to the
entity.asset.attribute.labels.advertised
groups
%{index}
UDM field.
resource.data.bgpPeers.advertisedIpRanges.range
entity.asset.attribute.labels[advertised_ip_range]
Iterate through
resource.data.bgpPeers.advertisedIpRanges.range
,
If the
resource.data.bgpPeers.advertisedIpRanges.range
log field value is
not
empty then,
resource.data.bgpPeers.advertisedIpRanges.range
log field is mapped to the
entity.asset.attribute.labels.advertised_ip
range
%{index}
UDM field.
resource.data.bgpPeers.advertisedRoutePriority
entity.asset.attribute.labels[advertised_rought_priority]
Iterate through
resource.data.bgpPeers.advertisedRoutePriority
,
If the
resource.data.bgpPeers.advertisedRoutePriority
log field value is
not
empty then,
resource.data.bgpPeers.advertisedRoutePriority
log field is mapped to the
entity.asset.attribute.labels.advertised_rought_priority
UDM field.
resource.data.bgp.advertisedIpRanges.description
entity.asset.attribute.labels[advertisedIp_ranges_description]
Iterate through
resource.data.bgp.advertisedIpRanges.description
,
If the
resource.data.bgp.advertisedIpRanges.description
log field value is
not
empty then,
resource.data.bgp.advertisedIpRanges.description
log field is mapped to the
entity.asset.attribute.labels.advertisedIp_ranges
description
%{index}
UDM field.
resource.data.bgp.advertisedIpRanges.range
entity.asset.attribute.labels[advertisedIp_ranges]
Iterate through
resource.data.bgp.advertisedIpRanges.range
,
If the
resource.data.bgp.advertisedIpRanges.range
log field value is
not
empty then,
resource.data.bgp.advertisedIpRanges.range
log field is mapped to the
entity.asset.attribute.labels.advertisedIp
ranges
%{index}
UDM field.
resource.data.bgpPeers.advertisedIpRanges.description
entity.asset.attribute.labels[advertize_ip_range_description]
Iterate through
resource.data.bgpPeers.advertisedIpRanges.description
,
If the
resource.data.bgpPeers.advertisedIpRanges.description
log field value is
not
empty then,
resource.data.bgpPeers.advertisedIpRanges.description
log field is mapped to the
entity.asset.attribute.labels.advertize_ip_range
description
%{index}
UDM field.
resource.data.bgpPeers.advertiseMode
entity.asset.attribute.labels[advertize_mode]
Iterate through
resource.data.bgpPeers.advertiseMode
,
If the
resource.data.bgpPeers.advertiseMode
log field value is
not
empty then,
resource.data.bgpPeers.advertiseMode
log field is mapped to the
entity.asset.attribute.labels.advertize_mode
UDM field.
resource.data.bgpPeers.bfd.multiplier
entity.asset.attribute.labels[bdf_multiplier]
Iterate through
resource.data.bgpPeers.bfd.multiplier
,
If the
resource.data.bgpPeers.bfd.multiplier
log field value is
not
empty then,
resource.data.bgpPeers.bfd.multiplier
log field is mapped to the
entity.asset.attribute.labels.bdf_multiplier
UDM field.
resource.data.bgp.asn
entity.asset.attribute.labels[bgp_asn]
resource.data.bgpPeers.enable
entity.asset.attribute.labels[bgppeers_enable]
Iterate through
resource.data.bgpPeers.enable
,
If the
resource.data.bgpPeers.enable
log field value is
not
empty then,
resource.data.bgpPeers.enable
log field is mapped to the
entity.asset.attribute.labels.bgppeers_enable
UDM field.
resource.data.bgpPeers.peerIpv6NexthopAddress
entity.asset.attribute.labels[bpeerIpv6_nexthop_address]
Iterate through
resource.data.bgpPeers.peerIpv6NexthopAddress
,
If the
resource.data.bgpPeers.peerIpv6NexthopAddress
log field value is
not
empty then,
resource.data.bgpPeers.peerIpv6NexthopAddress
log field is mapped to the
entity.asset.attribute.labels.bpeerIpv6_nexthop_address
UDM field.
resource.data.consumerAcceptLists.connectionLimit
entity.asset.attribute.labels[consumer_accept_lists_connection_limit]
resource.data.consumerAcceptLists.networkUrl
entity.asset.attribute.labels[consumer_accept_lists_network_url]
resource.data.bgpPeers.enableIpv6
entity.asset.attribute.labels[enable_Ipv6]
Iterate through
resource.data.bgpPeers.enableIpv6
,
If the
resource.data.bgpPeers.enableIpv6
log field value is
not
empty then,
resource.data.bgpPeers.enableIpv6
log field is mapped to the
entity.asset.attribute.labels.enable_Ipv6
UDM field.
resource.data.vpnInterfaces.interconnectAttachment
entity.asset.attribute.labels[interconnect_attachment]
resource.data.interfaces.id
entity.asset.attribute.labels[interface_id]
resource.data.bgpPeers.interfaceName
entity.asset.attribute.labels[interface_name]
Iterate through
resource.data.bgpPeers.interfaceName
,
If the
resource.data.bgpPeers.interfaceName
log field value is
not
empty then,
resource.data.bgpPeers.interfaceName
log field is mapped to the
entity.asset.attribute.labels.interface_name
UDM field.
resource.data.bgpPeers.ipAddress
entity.asset.attribute.labels[ip_address]
Iterate through
resource.data.bgpPeers.ipAddress
,
If the
resource.data.bgpPeers.ipAddress
log field value is
not
empty then,
resource.data.bgpPeers.ipAddress
log field is mapped to the
entity.asset.attribute.labels.ip_address
UDM field.
resource.data.bgpPeers.ipv6NexthopAddress
entity.asset.attribute.labels[ipv6_nexthop_address]
Iterate through
resource.data.bgpPeers.ipv6NexthopAddress
,
If the
resource.data.bgpPeers.ipv6NexthopAddress
log field value is
not
empty then,
resource.data.bgpPeers.ipv6NexthopAddress
log field is mapped to the
entity.asset.attribute.labels.ipv6_nexthop_address
UDM field.
resource.data.bgp.keepaliveInterval
entity.asset.attribute.labels[keepalive_interval]
resource.data.interfaces.linkedInterconnectAttachment
entity.asset.attribute.labels[linked_interconnect_attachment]
Iterate through
resource.data.interfaces.linkedInterconnectAttachment
,
If the
resource.data.interfaces.linkedInterconnectAttachment
log field value is
not
empty then,
resource.data.interfaces.linkedInterconnectAttachment
log field is mapped to the
entity.asset.attribute.labels.linked_interconnect_attachment
UDM field.
resource.data.interfaces.linkedVpnTunnel
entity.asset.attribute.labels[linked_vpn_tunnel]
Iterate through
resource.data.interfaces.linkedVpnTunnel
,
If the
resource.data.interfaces.linkedVpnTunnel
log field value is
not
empty then,
resource.data.interfaces.linkedVpnTunnel
log field is mapped to the
entity.asset.attribute.labels.linked_vpn_tunnel
UDM field.
resource.data.bgpPeers.managementType
entity.asset.attribute.labels[bgp_peers_managment_type]
Iterate through
resource.data.bgpPeers.managementType
,
If the
resource.data.bgpPeers.managementType
log field value is
not
empty then,
resource.data.bgpPeers.managementType
log field is mapped to the
entity.asset.attribute.labels.bgp_peers_managment_type
UDM field.
resource.data.bgpPeers.routerApplianceInstance
entity.asset.attribute.labels[bgp_peers_router_appliance_instance]
Iterate through
resource.data.bgpPeers.routerApplianceInstance
,
If the
resource.data.bgpPeers.routerApplianceInstance
log field value is
not
empty then,
resource.data.bgpPeers.routerApplianceInstance
log field is mapped to the
entity.asset.attribute.labels.bgp_peers_router_appliance_instance
UDM field.
resource.data.interfaces.managementType
entity.asset.attribute.labels[interface_managment_type]
Iterate through
resource.data.interfaces.managementType
,
If the
resource.data.interfaces.managementType
log field value is
not
empty then,
resource.data.interfaces.managementType
log field is mapped to the
entity.asset.attribute.labels.interface_managment_type
UDM field.
resource.data.bgpPeers.md5AuthenticationKeyName
entity.asset.attribute.labels[md5_authentication_key_name]
Iterate through
resource.data.bgpPeers.md5AuthenticationKeyName
,
If the
resource.data.bgpPeers.md5AuthenticationKeyName
log field value is
not
empty then,
resource.data.bgpPeers.md5AuthenticationKeyName
log field is mapped to the
entity.asset.attribute.labels.md5_authentication_key_name
UDM field.
resource.data.bgpPeers.customLearnedRoutePriority
entity.asset.attribute.labels[custom_learned_route_priority]
Iterate through
resource.data.bgpPeers.customLearnedRoutePriority
,
If the
resource.data.bgpPeers.customLearnedRoutePriority
log field value is
not
empty then,
resource.data.bgpPeers.customLearnedRoutePriority
log field is mapped to the
entity.asset.attribute.labels.custom_learned_route_priority
UDM field.
resource.data.bgpPeers.customLearnedIpRanges.range
entity.asset.attribute.labels[custom_learned_ip_range]
Iterate through
resource.data.bgpPeers.customLearnedIpRanges.range
,
If the
resource.data.bgpPeers.customLearnedIpRanges.range
log field value is
not
empty then,
resource.data.bgpPeers.customLearnedIpRanges.range
log field is mapped to the
entity.asset.attribute.labels.custom_learned_ip
range
%{index}
UDM field.
resource.data.bgpPeers.bfd.minReceiveInterval
entity.asset.attribute.labels[min_receive_interval]
Iterate through
resource.data.bgpPeers.bfd.minReceiveInterval
,
If the
resource.data.bgpPeers.bfd.minReceiveInterval
log field value is
not
empty then,
resource.data.bgpPeers.bfd.minReceiveInterval
log field is mapped to the
entity.asset.attribute.labels.min_receive_interval
UDM field.
resource.data.bgpPeers.bfd.minTransmitInterval
entity.asset.attribute.labels[min_transmit_interval]
Iterate through
resource.data.bgpPeers.bfd.minTransmitInterval
,
If the
resource.data.bgpPeers.bfd.minTransmitInterval
log field value is
not
empty then,
resource.data.bgpPeers.bfd.minTransmitInterval
log field is mapped to the
entity.asset.attribute.labels.min_transmit_interval
UDM field.
resource.data.bgpPeers.peerAsn
entity.asset.attribute.labels[peer_asn]
Iterate through
resource.data.bgpPeers.peerAsn
,
If the
resource.data.bgpPeers.peerAsn
log field value is
not
empty then,
resource.data.bgpPeers.peerAsn
log field is mapped to the
entity.asset.attribute.labels.peer_asn
UDM field.
resource.data.peerExternalGatewayInterface
entity.asset.attribute.labels[peer_external_gateway_interface]
resource.data.interfaces.privateIpAddress
entity.asset.attribute.labels[private_ip_address]
Iterate through
resource.data.interfaces.privateIpAddress
,
If the
resource.data.interfaces.privateIpAddress
log field value is
not
empty then,
resource.data.interfaces.privateIpAddress
log field is mapped to the
entity.asset.attribute.labels.private_ip_address
UDM field.
resource.data.vpnGatewayInterface
entity.asset.attribute.labels[pvn_gateway_interface]
resource.data.interfaces.redundantInterface
entity.asset.attribute.labels[redundant_interface]
Iterate through
resource.data.interfaces.redundantInterface
,
If the
resource.data.interfaces.redundantInterface
log field value is
not
empty then,
resource.data.interfaces.redundantInterface
log field is mapped to the
entity.asset.attribute.labels.redundant_interface
UDM field.
resource.data.bgpPeers.bfd.sessionInitializationMode
entity.asset.attribute.labels[sessionInitialization_mode]
Iterate through
resource.data.bgpPeers.bfd.sessionInitializationMode
,
If the
resource.data.bgpPeers.bfd.sessionInitializationMode
log field value is
not
empty then,
resource.data.bgpPeers.bfd.sessionInitializationMode
log field is mapped to the
entity.asset.attribute.labels.sessionInitialization_mode
UDM field.
resource.data.stackType
entity.asset.attribute.labels[stack_type]
resource.data.connectedEndpoints.status
entity.asset.attribute.labels[connected_endpoint_status]
resource.data.connectedEndpoints.consumerNetwork
entity.asset.attribute.labels[connected_endpoint_consumer_network]
resource.data.interfaces.subnetwork
entity.asset.attribute.labels[subnetwork]
Iterate through
resource.data.interfaces.subnetwork
,
If the
resource.data.interfaces.subnetwork
log field value is
not
empty then,
resource.data.interfaces.subnetwork
log field is mapped to the
entity.asset.attribute.labels.subnetwork
UDM field.
resource.data.sourceInstanceParams.diskConfigs.autoDelete
entity.asset.attribute.labels[disk_config_auto_delete]
resource.data.sourceInstanceParams.diskConfigs.customImage
entity.asset.attribute.labels[disk_config_custom_image]
resource.data.sourceInstanceParams.diskConfigs.deviceName
entity.asset.attribute.labels[disk_config_device_name]
resource.data.sourceInstanceParams.diskConfigs.instantiateFrom
entity.asset.attribute.labels[disk_config_instantiate_from]
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
entity.asset.attribute.labels[network_interfaces_access_configs_external_ipv6_prefix_length]
Iterate through
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
,
If the
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
,
If the
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
entity.asset.attribute.labels[network_interfaces_access_configs_external_ipv6_prefix_length]
Iterate through
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
,
If the
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
,
If the
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
resource.data.networkInterfaces.accessConfigs.kind
entity.asset.attribute.labels[network_interfaces_access_configs_kind]
resource.data.properties.networkInterfaces.accessConfigs.kind
entity.asset.attribute.labels[network_interfaces_access_configs_kind]
resource.data.networkInterfaces.accessConfigs.name
entity.asset.attribute.labels[network_interfaces_access_configs_name]
Iterate through
resource.data.networkInterfaces.accessConfigs.name
,
If the
resource.data.networkInterfaces.accessConfigs.name
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.name
,
If the
resource.data.properties.networkInterfaces.accessConfigs.name
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
name
%{index}
UDM field.
resource.data.properties.networkInterfaces.accessConfigs.name
entity.asset.attribute.labels[network_interfaces_access_configs_name]
Iterate through
resource.data.networkInterfaces.accessConfigs.name
,
If the
resource.data.networkInterfaces.accessConfigs.name
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.name
,
If the
resource.data.properties.networkInterfaces.accessConfigs.name
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
name
%{index}
UDM field.
resource.data.networkInterfaces.accessConfigs.networkTier
entity.asset.attribute.labels[network_interfaces_access_configs_network_tier]
Iterate through
resource.data.networkInterfaces.accessConfigs.networkTier
,
If the
resource.data.networkInterfaces.accessConfigs.networkTier
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_network
tier
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.networkTier
,
If the
resource.data.properties.networkInterfaces.accessConfigs.networkTier
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_network
tier
%{index}
UDM field.
resource.data.properties.networkInterfaces.accessConfigs.networkTier
entity.asset.attribute.labels[network_interfaces_access_configs_network_tier]
Iterate through
resource.data.networkInterfaces.accessConfigs.networkTier
,
If the
resource.data.networkInterfaces.accessConfigs.networkTier
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_network
tier
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.networkTier
,
If the
resource.data.properties.networkInterfaces.accessConfigs.networkTier
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_network
tier
%{index}
UDM field.
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
entity.asset.attribute.labels[network_interfaces_access_configs_public_ptr_domain_name]
Iterate through
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
,
If the
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_public_ptr_domain
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
,
If the
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_public_ptr_domain
name
%{index}
UDM field.
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
entity.asset.attribute.labels[network_interfaces_access_configs_public_ptr_domain_name]
Iterate through
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
,
If the
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.publicPtrDomainName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_public_ptr_domain
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
,
If the
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.publicPtrDomainName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_public_ptr_domain
name
%{index}
UDM field.
resource.data.networkInterfaces.accessConfigs.setPublicPtr
entity.asset.attribute.labels[network_interfaces_access_configs_set_public_ptr]
Iterate through
resource.data.networkInterfaces.accessConfigs.setPublicPtr
,
If the
resource.data.networkInterfaces.accessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_set_public
ptr
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
,
If the
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_set_public
ptr
%{index}
UDM field.
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
entity.asset.attribute.labels[network_interfaces_access_configs_set_public_ptr]
Iterate through
resource.data.networkInterfaces.accessConfigs.setPublicPtr
,
If the
resource.data.networkInterfaces.accessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_set_public
ptr
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
,
If the
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs_set_public
ptr
%{index}
UDM field.
resource.data.networkInterfaces.accessConfigs.type
entity.asset.attribute.labels[network_interfaces_access_configs_type]
Iterate through
resource.data.networkInterfaces.accessConfigs
,
If the
resource.data.networkInterfaces.accessConfigs.type
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
type
%{index}
UDM field.
Iterate through
resource.data.networkInterfaces.accessConfigs
,
If the
resource.data.properties.networkInterfaces.accessConfigs.type
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
type
%{index}
UDM field.
resource.data.properties.networkInterfaces.accessConfigs.type
entity.asset.attribute.labels[network_interfaces_access_configs_type]
Iterate through
resource.data.networkInterfaces.accessConfigs
,
If the
resource.data.networkInterfaces.accessConfigs.type
log field value is
not
empty then,
resource.data.networkInterfaces.accessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
type
%{index}
UDM field.
Iterate through
resource.data.networkInterfaces.accessConfigs
,
If the
resource.data.properties.networkInterfaces.accessConfigs.type
log field value is
not
empty then,
resource.data.properties.networkInterfaces.accessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_access_configs
type
%{index}
UDM field.
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
entity.asset.attribute.labels[network_interfaces_alias_ip_ranges_ip_cidr_range]
Iterate through
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
,
If the
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
log field value is
not
empty then,
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_ip_cidr
range
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
,
If the
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
log field value is
not
empty then,
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_ip_cidr
range
%{index}
UDM field.
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
entity.asset.attribute.labels[network_interfaces_alias_ip_ranges_ip_cidr_range]
Iterate through
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
,
If the
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
log field value is
not
empty then,
resource.data.networkInterfaces.aliasIpRanges.ipCidrRange
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_ip_cidr
range
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
,
If the
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
log field value is
not
empty then,
resource.data.properties.networkInterfaces.aliasIpRanges.ipCidrRange
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_ip_cidr
range
%{index}
UDM field.
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
entity.asset.attribute.labels[network_interfaces_alias_ip_ranges_subnetwork_range_name]
Iterate through
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
,
If the
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field value is
not
empty then,
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_subnetwork_range
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
,
If the
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field value is
not
empty then,
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_subnetwork_range
name
%{index}
UDM field.
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
entity.asset.attribute.labels[network_interfaces_alias_ip_ranges_subnetwork_range_name]
Iterate through
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
,
If the
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field value is
not
empty then,
resource.data.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_subnetwork_range
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
,
If the
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field value is
not
empty then,
resource.data.properties.networkInterfaces.aliasIpRanges.subnetworkRangeName
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_alias_ip_ranges_subnetwork_range
name
%{index}
UDM field.
resource.data.networkInterfaces.fingerprint
entity.asset.attribute.labels[network_interfaces_fingerprint]
resource.data.properties.networkInterfaces.fingerprint
entity.asset.attribute.labels[network_interfaces_fingerprint]
resource.data.networkInterfaces.internalIpv6PrefixLength
entity.asset.attribute.labels[network_interfaces_internal_ipv6_prefix_length]
resource.data.properties.networkInterfaces.internalIpv6PrefixLength
entity.asset.attribute.labels[network_interfaces_internal_ipv6_prefix_length]
resource.data.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_external_ipv6_prefix_length]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
resource.data.properties.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_external_ipv6_prefix_length]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.externalIpv6PrefixLength
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_external_ipv6_prefix
length
%{index}
UDM field.
resource.data.networkInterfaces.ipv6AccessConfigs.kind
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_kind]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs.kind
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.kind
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.kind
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
kind
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
kind
%{index}
UDM field.
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_kind]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs.kind
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.kind
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.kind
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
kind
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.kind
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
kind
%{index}
UDM field.
resource.data.networkInterfaces.ipv6AccessConfigs.name
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_name]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs.name
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.name
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
name
%{index}
UDM field.
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_name]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs.name
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.name
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
name
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.name
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
name
%{index}
UDM field.
resource.data.networkInterfaces.ipv6AccessConfigs.networkTier
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_network_tier]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.networkTier
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_network
tier
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.networkTier
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_network
tier
%{index}
UDM field.
resource.data.properties.networkInterfaces.ipv6AccessConfigs.networkTier
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_network_tier]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.networkTier
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_network
tier
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.networkTier
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.networkTier
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_network
tier
%{index}
UDM field.
resource.data.networkInterfaces.ipv6AccessConfigs.publicPtrDomainName
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_public_ptr_domain_name]
resource.data.properties.networkInterfaces.ipv6AccessConfigs.publicPtrDomainName
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_public_ptr_domain_name]
resource.data.networkInterfaces.ipv6AccessConfigs.setPublicPtr
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_set_public_ptr]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_set_public
ptr
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_set_public
ptr
%{index}
UDM field.
resource.data.properties.networkInterfaces.ipv6AccessConfigs.setPublicPtr
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_set_public_ptr]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_set_public
ptr
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.setPublicPtr
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs_set_public
ptr
%{index}
UDM field.
resource.data.networkInterfaces.ipv6AccessConfigs.type
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_type]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs.type
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.type
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
type
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
type
%{index}
UDM field.
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
entity.asset.attribute.labels[network_interfaces_ipv6_access_configs_type]
Iterate through
resource.data.networkInterfaces.ipv6AccessConfigs.type
,
If the
resource.data.networkInterfaces.ipv6AccessConfigs.type
log field value is
not
empty then,
resource.data.networkInterfaces.ipv6AccessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
type
%{index}
UDM field.
Iterate through
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
,
If the
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
log field value is
not
empty then,
resource.data.properties.networkInterfaces.ipv6AccessConfigs.type
log field is mapped to the
entity.asset.attribute.labels.network_interfaces_ipv6_access_configs
type
%{index}
UDM field.
resource.data.networkInterfaces.ipv6AccessType
entity.asset.attribute.labels[network_interfaces_ipv6_access_type]
resource.data.properties.networkInterfaces.ipv6AccessType
entity.asset.attribute.labels[network_interfaces_ipv6_access_type]
resource.data.networkInterfaces.kind
entity.asset.attribute.labels[network_interfaces_kind]
resource.data.properties.networkInterfaces.kind
entity.asset.attribute.labels[network_interfaces_kind]
resource.data.networkInterfaces.networkAttachment
entity.asset.attribute.labels[network_interfaces_network_attachment]
resource.data.properties.networkInterfaces.networkAttachment
entity.asset.attribute.labels[network_interfaces_network_attachment]
resource.data.networkInterfaces.nicType
entity.asset.attribute.labels[network_interfaces_nic_type]
resource.data.properties.networkInterfaces.nicType
entity.asset.attribute.labels[network_interfaces_nic_type]
resource.data.networkInterfaces.queueCount
entity.asset.attribute.labels[network_interfaces_queue_count]
resource.data.properties.networkInterfaces.queueCount
entity.asset.attribute.labels[network_interfaces_queue_count]
resource.data.networkInterfaces.stackType
entity.asset.attribute.labels[network_interfaces_stack_type]
resource.data.properties.networkInterfaces.stackType
entity.asset.attribute.labels[network_interfaces_stack_type]
resource.data.networkInterfaces.subnetwork
entity.asset.attribute.labels[network_interfaces_subnetwork]
resource.data.properties.networkInterfaces.subnetwork
entity.asset.attribute.labels[network_interfaces_subnetwork]
resource.data.versions.name
entity.asset.attribute.labels[versions_name]
Iterate through
resource.data.versions.name
,
If the
resource.data.versions.name
log field value is
not
empty then,
resource.data.versions.name
log field is mapped to the
entity.asset.attribute.labels.versions
name
%{index}
UDM field.
resource.data.versions.targetSize.calculated
entity.asset.attribute.labels[versions_target_size_calculated]
Iterate through
resource.data.versions.targetSize.calculated
,
If the
resource.data.versions.targetSize.calculated
log field value is
not
empty then,
resource.data.versions.targetSize.calculated
log field is mapped to the
entity.asset.attribute.labels.versions_target_size
calculated
%{index}
UDM field.
resource.data.versions.targetSize.fixed
entity.asset.attribute.labels[versions_target_size_fixed]
Iterate through
resource.data.versions.targetSize.fixed
,
If the
resource.data.versions.targetSize.fixed
log field value is
not
empty then,
resource.data.versions.targetSize.fixed
log field is mapped to the
entity.asset.attribute.labels.versions_target_size
fixed
%{index}
UDM field.
resource.data.versions.targetSize.percent
entity.asset.attribute.labels[versions_target_size_percent]
Iterate through
resource.data.versions.targetSize.percent
,
If the
resource.data.versions.targetSize.percent
log field value is
not
empty then,
resource.data.versions.targetSize.percent
log field is mapped to the
entity.asset.attribute.labels.versions_target_size
percent
%{index}
UDM field.
resource.data.targetVpnGateway
entity.asset.attribute.labels[target_vpn_gateway]
resource.data.vpnGateway
entity.asset.attribute.labels[vpn_gateway]
resource.data.peerGcpGateway
entity.asset.attribute.labels[peer_gcp_gateway]
resource.data.router
entity.asset.attribute.labels[router]
resource.data.tunnels
entity.asset.attribute.labels[tunnels]
resource.data.forwardingRules
entity.asset.attribute.labels[forwarding_rules]
resource.data.service
entity.asset.attribute.labels[service]
resource.data.sslCertificates
entity.asset.attribute.labels[ssl_certificates]
resource.data.instance
entity.asset.attribute.labels[instance]
resource.data.connectedEndpoints.endpoint
entity.asset.attribute.labels[connected_endpoint_endpoint]
resource.data.natSubnets
entity.asset.attribute.labels[nat_subnet]
resource.data.consumerRejectLists
entity.asset.attribute.labels[consumer_reject_list]
resource.data.consumerAcceptLists.projectIdOrNum
entity.asset.attribute.labels[consumer_accept_list_project_id_or_num]
resource.data.rules.targetResources
entity.asset.attribute.labels[rules_target_resource]
resource.data.network.url
entity.asset.attribute.labels[network_url]
resource.data.mirroredResources.subnetworks.url
entity.asset.attribute.labels[mirrored_resources_subnetwork_url]
resource.data.mirroredResources.instances.url
entity.asset.attribute.labels[mirrored_resources_instance_url]
resource.data.interfaces.name
entity.asset.attribute.labels[interface_name]
resource.data.bgpPeers.name
entity.asset.attribute.labels[bgp_peer_name]
resource.data.instances
entity.asset.attribute.labels[instances]
resource.data.users
entity.asset.attribute.labels[users]
resource.data.sourceInstance
entity.asset.attribute.labels[source_instance]
resource.data.peerExternalGateway
entity.asset.attribute.labels[peer_ex_gateway_label]
resource.data.networkInterfaces.name
entity.asset.attribute.labels[network_interfaces_name]
resource.data.properties.networkInterfaces.name
entity.asset.attribute.labels[network_interfaces_name]
resource.data.disks.initializeParams.diskName
entity.asset.attribute.labels[disks_initialize_params_disk_name]
resource.data.properties.disks.initializeParams.diskName
entity.asset.attribute.labels[disks_initialize_params_disk_name]
resource.data.serviceAccounts.email
relations.entity.resource.name
resource.data.properties.serviceAccounts.email
relations.entity.resource.name
resource.data.vpnInterfaces.id
entity.asset.attribute.labels[vpn_interface_id]
resource.data.network.canonicalUrl
entity.asset.attribute.labels[network_canonical_url]
resource.data.mirroredResources.subnetworks.canonicalUrl
entity.asset.attribute.labels[mirrored_resources_subnetwork_canonical_url]
resource.data.mirroredResources.instances.canonicalUrl
entity.asset.attribute.labels[mirrored_resources_instance_canonical_url]
resource.data.target
entity.asset.attribute.labels[target]
resource.data.vpnInterfaces.id
entity.asset.attribute.labels[vpn_interface_id]
resource.data.instanceTemplate
entity.asset.attribute.labels[instance_template]
resource.data.versions.instanceTemplate
entity.asset.attribute.labels[versions_instance_template]
resource.data.networkInterfaces.network
entity.asset.attribute.labels[network_interfaces_network]
resource.data.properties.networkInterfaces.network
entity.asset.attribute.labels[network_interfaces_network]
entity.asset.attribute.labels[network_interfaces_network]
resource.data.selfLink
entity.url
resource.data.googleIpAddress
entity.asset.attribute.labels[google_ip_address]
resource.data.nocContactEmail
entity.asset.attribute.labels[noc_contact_email]
resource.data.peerIpAddress
entity.asset.attribute.labels[peer_ip_address]
resource.data.kind
entity.asset.attribute.labels[kind]
If the
assetType
log field value is
not
empty then,
resource.data.kind
log field is mapped to the
entity.asset.attribute.labels.kind
UDM field.
resource.data.description
metadata.description
resource.data.namedPorts.name
entity.asset.attribute.labels[named_ports_name]
resource.data.namedPorts.port
entity.asset.attribute.labels[named_ports_port]
resource.data.network
entity.asset.attribute.labels[network]
resource.data.zone
entity.resource.attribute.cloud.availability_zone
resource.data.size
entity.asset.attribute.labels[size]
resource.data.subnetwork
entity.asset.attribute.labels[subnetwork]
resource.data.ipCidrRange
entity.asset.attribute.labels[ip_cidr_range]
resource.data.gatewayAddress
entity.nat_ip
resource.data.gatewayIPv4
entity.nat_ip
resource.data.address
entity.nat_ip
resource.data.privateIpGoogleAccess
entity.asset.attribute.labels[private_ip_google_access]
resource.data.secondaryIpRanges.rangeName
entity.asset.attribute.labels[secondary_ip_range_name]
resource.data.secondaryIpRanges.ipCidrRange
entity.asset.attribute.labels[secondary_ip_cidr_range]
resource.data.enableFlowLogs
entity.asset.attribute.labels[enable_flow_logs]
resource.data.privateIpv6GoogleAccess
entity.asset.attribute.labels[private_ipv6_google_access]
resource.data.ipv6CidrRange
entity.asset.attribute.labels[ipv6_cidr_range]
resource.data.externalIpv6Prefix
entity.asset.attribute.labels[external_ipv6_prefix]
resource.data.internalIpv6Prefix
entity.asset.attribute.labels[internal_ipv6_prefix]
resource.data.role
entity.asset.attribute.labels[role]
resource.data.logConfig.aggregationInterval
entity.asset.attribute.labels[log_config_aggregation_interval]
resource.data.logConfig.flowSampling
entity.asset.attribute.labels[log_config_flow_sampling]
resource.data.logConfig.metadataFields
entity.asset.attribute.labels[log_config_metadata_fields]
Iterate through
resource.data.logConfig.metadataFields
,
If the
resource.data.logConfig.metadataFields
log field value is
not
empty then,
resource.data.logConfig.metadataFields
log field is mapped to the
entity.asset.attribute.labels.log_config_metadata
fields
%{index}
UDM field.
resource.data.logConfig.filterExpr
entity.asset.attribute.labels[log_config_filter_expr]
resource.data.ipv6AccessType
entity.asset.attribute.labels[ipv6_access_type]
resource.data.selfLinkWithId
entity.asset.attribute.labels[self_link_with_id]
resource.data.autoCreateSubnetworks
entity.asset.attribute.labels[auto_create
subnetworks]
resource.data.subnetworks
entity.asset.attribute.labels[subnetworks]
Iterate through
resource.data.subnetworks
,
If the
resource.data.subnetworks
log field value is
not
empty then,
resource.data.subnetworks
log field is mapped to the
entity.asset.attribute.labels.subnetworks%{index}
UDM field.
resource.data.peerings.name
entity.asset.attribute.labels[peerings_name]
Iterate through
resource.data.peerings.name
,
If the
resource.data.peerings.name
log field value is
not
empty then,
resource.data.peerings.name
log field is mapped to the
entity.asset.attribute.labels.peerings
name
%{index}
UDM field.
resource.data.peerings.network
entity.asset.attribute.labels[peerings_network]
Iterate through
resource.data.peerings.network
,
If the
resource.data.peerings.network
log field value is
not
empty then,
resource.data.peerings.network
log field is mapped to the
entity.asset.attribute.labels.peerings
network
%{index}
UDM field.
resource.data.peerings.state
entity.asset.attribute.labels[peerings_state]
Iterate through
resource.data.peerings.state
,
If the
resource.data.peerings.state
log field value is
not
empty then,
resource.data.peerings.state
log field is mapped to the
entity.asset.attribute.labels.peerings
state
%{index}
UDM field.
resource.data.peerings.stateDetails
entity.asset.attribute.labels[peerings_state_details]
Iterate through
resource.data.peerings.stateDetails
,
If the
resource.data.peerings.stateDetails
log field value is
not
empty then,
resource.data.peerings.stateDetails
log field is mapped to the
entity.asset.attribute.labels.peerings_state
details
%{index}
UDM field.
resource.data.peerings.autoCreateRoutes
entity.asset.attribute.labels[peerings_auto_create_routes]
Iterate through
resource.data.peerings.autoCreateRoutes
,
If the
resource.data.peerings.autoCreateRoutes
log field value is
not
empty then,
resource.data.peerings.autoCreateRoutes
log field is mapped to the
entity.asset.attribute.labels.peerings_auto_create
routes
%{index}
UDM field.
resource.data.peerings.exportCustomRoutes
entity.asset.attribute.labels[peerings_export_custom_routes]
Iterate through
resource.data.peerings.exportCustomRoutes
,
If the
resource.data.peerings.exportCustomRoutes
log field value is
not
empty then,
resource.data.peerings.exportCustomRoutes
log field is mapped to the
entity.asset.attribute.labels.peerings_export_custom
routes
%{index}
UDM field.
resource.data.peerings.importCustomRoutes
entity.asset.attribute.labels[peerings_import_custom_routes]
Iterate through
resource.data.peerings.importCustomRoutes
,
If the
resource.data.peerings.importCustomRoutes
log field value is
not
empty then,
resource.data.peerings.importCustomRoutes
log field is mapped to the
entity.asset.attribute.labels.peerings_import_custom
routes
%{index}
UDM field.
resource.data.peerings.exchangeSubnetRoutes
entity.asset.attribute.labels[peerings_exchange_subnet_routes]
Iterate through
resource.data.peerings.exchangeSubnetRoutes
,
If the
resource.data.peerings.exchangeSubnetRoutes
log field value is
not
empty then,
resource.data.peerings.exchangeSubnetRoutes
log field is mapped to the
entity.asset.attribute.labels.peerings_exchange_subnet
routes
%{index}
UDM field.
resource.data.peerings.exportSubnetRoutesWithPublicIp
entity.asset.attribute.labels[peerings_export_subnet_routes_with_public_ip]
Iterate through
resource.data.peerings.exportSubnetRoutesWithPublicIp
,
If the
resource.data.peerings.exportSubnetRoutesWithPublicIp
log field value is
not
empty then,
resource.data.peerings.exportSubnetRoutesWithPublicIp
log field is mapped to the
entity.asset.attribute.labels.peerings_export_subnet_routes_with_public
ip
%{index}
UDM field.
resource.data.peerings.importSubnetRoutesWithPublicIp
entity.asset.attribute.labels[peerings_import_subnet_routes_with_public_ip]
Iterate through
resource.data.peerings.importSubnetRoutesWithPublicIp
,
If the
resource.data.peerings.importSubnetRoutesWithPublicIp
log field value is
not
empty then,
resource.data.peerings.importSubnetRoutesWithPublicIp
log field is mapped to the
entity.asset.attribute.labels.peerings_import_subnet_routes_with_public
ip
%{index}
UDM field.
resource.data.peerings.peerMtu
entity.asset.attribute.labels[peerings_peer_mtu]
Iterate through
resource.data.peerings.peerMtu
,
If the
resource.data.peerings.peerMtu
log field value is
not
empty then,
resource.data.peerings.peerMtu
log field is mapped to the
entity.asset.attribute.labels.peerings_peer
mtu
%{index}
UDM field.
resource.data.peerings.stackType
entity.asset.attribute.labels[peerings_statck_type]
Iterate through
resource.data.peerings.stackType
,
If the
resource.data.peerings.stackType
log field value is
not
empty then,
resource.data.peerings.stackType
log field is mapped to the
entity.asset.attribute.labels.peerings_statck
type
%{index}
UDM field.
resource.data.routingConfig.routingMode
entity.asset.attribute.labels[routing_config_mode]
resource.data.firewallPolicy
entity.asset.attribute.labels[firewall_policy]
resource.data.networkFirewallPolicyEnforcementOrder
entity.asset.attribute.labels[network_firewall_policy_enforcement_order]
resource.data.enableUlaInternalIpv6
entity.asset.attribute.labels[enable_ula_internal_ipv6]
resource.data.internalIpv6Range
entity.asset.attribute.labels[internal_ipv6_range]
resource.data.IPv4Range
entity.asset.attribute.labels[ipv4
range]
resource.data.tags
entity.asset.attribute.labels[tags]
Iterate through
resource.data.tags
,
If the
resource.data.tags
log field value is
not
empty then,
resource.data.tags
log field is mapped to the
entity.asset.attribute.labels.tags%{index}
UDM field.
resource.data.destRange
entity.asset.attribute.labels[dest_range]
resource.data.nextHopInstance
entity.asset.attribute.labels[next_hop_instance]
resource.data.nextHopIp
entity.asset.attribute.labels[next_hop_ip]
resource.data.nextHopNetwork
entity.asset.attribute.labels[next_hop_network]
resource.data.nextHopGateway
entity.asset.attribute.labels[next_hop_gateway]
resource.data.nextHopPeering
entity.asset.attribute.labels[next_hop_peering]
resource.data.nextHopIlb
entity.asset.attribute.labels[next_hop_ilb]
resource.data.disks.kind
entity.asset.attribute.labels[disks_kind]
resource.data.properties.disks.kind
entity.asset.attribute.labels[disks_kind]
relations.entity.resource.resource_subtype
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.resource.resource_subtype
UDM field is set to
Service Account
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.resource.resource_subtype
UDM field is set to
Service Account
.
relations.entity.resource.resource_type
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.resource.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.resource.resource_type
UDM field is set to
SERVICE_ACCOUNT
.
If the
asset_type
log field value matches the regular expression pattern
Instance
or the
assetType
log field value matches the regular expression pattern
Instance
then, the
entity.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
relations.entity.resource.attribute.cloud.environment
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
relations.entity.user.attribute.cloud.environment
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.user.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.entity.user.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
relations.relationship
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.relationship
UDM field is set to
ADMINISTERS
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.relationship
UDM field is set to
ADMINISTERS
.
relations.entity_type
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.entity_type
UDM field is set to
USER
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.entity_type
UDM field is set to
USER
.
entity.asset.deployment_status
If the
resource.data.status
log field value contain one of the following values:
RUNNING
PROVISIONING
STAGING
STOPPING
SUSPENDING
SUSPENDED
REPAIRING
TERMINATED
then, the
entity.asset.deployment_status
UDM field is set to
ACTIVE
.
Else the
entity.asset.deployment_status
UDM field is set to
DEPLOYMENT_STATUS_UNSPECIFIED
.
entity.asset.attribute.cloud.availability_zone
The
region
,
zone_suffix
and
project_id
fields is extracted from
name
log field using the Grok pattern. The
entity.asset.attribute.cloud.availability_zone
UDM field is set to
%{region}-%{zone_suffix}
.
relations.direction
Iterate through
resource.data.serviceAccounts
,
If the
resource.data.serviceAccounts.email
log field value is
not
empty then, the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
Iterate through
resource.data.properties.serviceAccounts
,
If the
resource.data.properties.serviceAccounts.email
log field value is
not
empty then, the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
