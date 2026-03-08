# Collect Apigee logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-apigee-x/  
**Scraped:** 2026-03-05T09:47:35.492019Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Apigee logs
Supported in:
Google secops
SIEM
This document describes how you can collect Apigee logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of Apigee logs map to Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Apigee logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Apigee logs
: The Apigee logs that are
enabled for ingestion to Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Apigee.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_APIGEE_X
ingestion label.
Before you begin
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Before starting, confirm that you have either
Log Collection with MessageLogging Policy
or
(Legacy) Log Collection with ServiceCallout Policy
set up.
To setup up Log Collection with MessageLogging Policy, follow the steps in the
Apigee Google Cloud Integration guide
.
Configure Google Cloud to ingest Apigee logs
To ingest Apigee logs to Google Security Operations, follow the steps on the
Ingest Google Cloud logs to Google Security Operations
page.
If you encounter issues when you ingest Apigee logs, contact
Google Security Operations support
.
Supported Apigee log formats
The Apigee parser supports logs in JSON format.
Supported Apigee Sample Logs
JSON
{
    "insertId": "12wnv8zf7np8nh",
    "jsonPayload": {
      "proxy.name": "myproxy",
      "app.name": "",
      "environment.name": "test-env",
      "system.region.name": "us-west1",
      "developer.email": "",
      "target.country": "",
      "request.content-length": "",
      "client.state": "",
      "response.status.code": "200",
      "request.content-type": "",
      "response.content-type": "application/xml; charset\u003dutf-8",
      "proxy.revision": "6",
      "response.content-length": "141",
      "proxy.proxyendpoint.name": "default",
      "organization.name": "test-dummy-57377",
      "error.state": "",
      "error": "false",
      "fault.name": "",
      "client.locality": "",
      "target.state": "",
      "proxy.pathsuffix": "",
      "client.port": "50386",
      "system.uuid": "7f2fde33-5f39-4866-a073-e6c31a4664e2",
      "target.scheme": "https",
      "request.user-agent": "curl/8.5.0",
      "target.locality": "",
      "messageid": "f8093238-2f51-42ab-ae44-dec9f451c7474",
      "target.port": "443",
      "target.ip": "198.51.100.0",
      "apiproduct.name": "",
      "request.url": "https://",
      "request.x-cloud-trace-context": "e3d3fea1742455ede2dad1d975361511/11739831648342702971",
      "request.httpversion": "1.1",
      "target.host": "mocktarget.apigee.net",
      "target.url": "https://mocktarget.apigee.net/xml",
      "proxy.basepath": "/myproxy",
      "target.cn": "mocktarget.apigee.net",
      "client.country": "",
      "client.cn": "",
      "cachehit": "",
      "target.organization": "",
      "client.ip": "198.51.100.0",
      "system.timestamp": "1754652492121",
      "request.host": "",
      "request.verb": "GET",
      "request.x-b3-traceid": "31339f721d4be35ff2932fa471979252",
      "client.scheme": "https",
      "error.message": ""
    },
    "resource": {
      "type": "api",
      "labels": {
        "project_id": "test-dummy-57377",
        "version": "",
        "location": "",
        "method": "",
        "service": ""
      }
    },
    "timestamp": "2025-08-08T11:28:12.203938277Z",
    "severity": "INFO",
    "logName": "projects/test-dummy-57377/logs/apigee-secops-integration-test-env",
    "receiveTimestamp": "2025-08-08T11:28:12.203938277Z"
  }
Field mapping reference
This section explains how the Google SecOps parser maps Apigee logs fields to Google Security Operations Unified Data Model (UDM) fields.
Field mapping reference: GCP_APIGEE_X Log Collection with MessageLogging Policy logs
The following table lists the log fields of the
GCP_APIGEE_X
Log Collection with MessageLogging Policy log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
insertId
metadata.product_log_id
jsonPayload.request.queryparams.count
target.resource.attribute.labels[json_payload_request_queryparams_count]
jsonPayload.request.uri
target.resource.name
target.resource.resource_type
If the
jsonPayload.request.uri
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
jsonPayload.target.host
target.hostname
jsonPayload.log.sni_host
target.hostname
jsonPayload.target.host
target.asset.hostname
jsonPayload.log.sni_host
target.asset.hostname
jsonPayload.target.sent.start.timestamp
target.resource.attribute.labels[json_payload_target_sent_start_timestamp]
jsonPayload.response.reason.phrase
security_result.summary
jsonPayload.response.reason
security_result.summary
jsonPayload.target.cn
target.resource.attribute.labels[json_payload_target_cn]
jsonPayload.target.port
target.port
jsonPayload.request.path
target.resource.attribute.labels[json_payload_request_path]
jsonPayload.target.ip
target.ip
jsonPayload.request.queryparam.param_name
target.resource.attribute.labels[json_payload_request_queryparams_param_name]
jsonPayload.request.queryparam.param_name.values
target.resource.attribute.labels[json_payload_request_queryparams_param_values]
jsonPayload.client.sent.end.timestamp
principal.resource.attribute.labels[client sent end timestamp]
jsonPayload.response.content
security_result.description
jsonPayload.target.organization
target.resource_ancestors.name
jsonPayload.log.organization
target.resource_ancestors.name
target.resource_ancestors.resource_type
If the
jsonPayload.target.organization
log field value is
not
empty or the
jsonPayload.log.organization
log field value is
not
empty, then the
target.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
jsonPayload.target.organization.unit
target.resource_ancestors.attribute.labels[json_payload_target_organization_unit]
jsonPayload.proxy.client.ip
src.ip
jsonPayload.error.content
security_result.about.resource.attribute.labels[error_content]
jsonPayload.response.headers.names
target.resource.attribute.labels[response_headers_names]
jsonPayload.error.state
security_result.about.resource.attribute.labels[state]
jsonPayload.proxy.pathsuffix
intermediary.resource.attribute.labels[pathsuffix]
jsonPayload.log.proxy_basepath
intermediary.resource.attribute.labels[pathsuffix]
jsonPayload.messageid
metadata.product_event_type
jsonPayload.request.verb
network.http.method
jsonPayload.response.status.code
network.http.response_code
jsonPayload.log.status
network.http.response_code
jsonPayload.response.code
network.http.response_code
jsonPayload.request.transportid
target.resource.attribute.labels[json_payload_request_transport_id]
jsonPayload.request.content
target.resource.attribute.labels[json_payload_request_content]
jsonPayload.client.received.start.timestamp
principal.resource.attribute.labels[client_received_start_timestamp]
jsonPayload.target.basepath
target.resource.attribute.labels[basepath]
jsonPayload.proxy.url
intermediary.url
jsonPayload.request.url
target.resource.attribute.labels[json_payload_request_url]
jsonPayload.client.sent.start.timestamp
principal.resource.attribute.labels[json_payload_client_sent_start_timestamp]
jsonPayload.client.received.end.timestamp
principal.resource.attribute.labels[client end timestamp]
jsonPayload.target.sent.end.timestamp
target.resource.attribute.labels[json_payload_target_sent_end_timestamp]
jsonPayload.apigee.metrics.policy..timeTaken
security_result.rule_labels[apigee_metrics_policy_time_taken]
jsonPayload.target.scheme
target.network.application_protocol
jsonPayload.request.queryparams.names
target.resource.attribute.labels[json_payload_request_queryparams_names]
jsonPayload.request.version
target.resource.attribute.labels[json_payload_request_version]
jsonPayload.request.httpversion
target.resource.attribute.labels[json_payload_request_version]
jsonPayload.system.timestamp
additional.fields[jsonPayload_system_timestamp]
jsonPayload.client.scheme
principal.network.application_protocol
jsonPayload.request.header.header_name
target.resource.attribute.labels[json_payload_request_header_name]
jsonPayload.request.header.header_name.values
target.resource.attribute.labels[request_header_name_values]
jsonPayload.target.url
target.url
jsonPayload.url
target.url
jsonPayload.response.header.header_name.values
target.resource.attribute.labels[response_header_name_values]
jsonPayload.request.querystring
target.resource.attribute.labels[json_payload_request_querystring]
jsonPayload.response.headers.count
target.resource.attribute.labels[response_headers_count]
principal.resource.resource_type
If the
resource.type
log field value is equal to
gce_instance
, then the
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
resource.type
principal.resource.resource_subtype
resource.labels.instance_id
principal.resource.product_object_id
resource.labels.project_id
principal.resource_ancestors.product_object_id
principal.resource_ancestors.resource_type
The
if the
resource.labels.project_id
log field value is
not
empty, then principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
resource.labels.zone
principal.resource.attribute.cloud.availability_zone
timestamp
metadata.event_timestamp
severity
security_result.severity
If the
severity
log field value is equal to
ERROR
, then the
severity
log field is mapped to the
security_result.severity
UDM field.
severity
security_result.severity_details
logName
security_result.category_details
logName
principal.resource.attribute.labels[Log Name]
receiveTimestamp
metadata.collected_timestamp
jsonPayload.client.ip
principal.ip
jsonPayload.log.origin_address
principal.ip
jsonPayload.client.host
principal.ip
jsonPayload.request.formparam.param_name.values
target.resource.attribute.labels[json_payload_request_form_param_name_values]
jsonPayload.request.formparam.param_name
target.resource.attribute.labels[json_payload_request_form_param_name]
jsonPayload.request.formparams.count
target.resource.attribute.labels[json_payload_request_form_params_count]
jsonPayload.request.formparams.names
target.resource.attribute.labels[json_payload_request_form_params_names]
jsonPayload.request.formstring
target.resource.attribute.labels[json_payload_request_form_string]
jsonPayload.response.transport.message
target.resource.attribute.labels[response_transport_message]
jsonPayload.response.header.header_name
target.resource.attribute.labels[response_header_name]
jsonPayload.apigee.metrics.policy.policy_name.timeTaken
security_result.rule_labels[apigee_metrics_policy_policy_name_timeTaken]
jsonPayload.apiproduct.operation
intermediary.resource.attribute.labels[api_product_operation]
jsonPayload.apiproduct.operation.resource
intermediary.resource.attribute.labels[api_product_operation_resource]
jsonPayload.apiproduct.operation.methods
intermediary.resource.attribute.labels[api_product_operation_methods]
jsonPayload.apiproduct.operation.attributes.key_name
intermediary.resource.attribute.labels[api_product_operation_attributes_key_name]
jsonPayload.proxy.name
intermediary.resource.name
jsonPayload.proxy.revision
intermediary.resource.attribute.labels[json_payload_proxy_revision]
jsonPayload.apiproxy.basepath
intermediary.resource.attribute.labels[json_payload_api_proxy_basepath]
jsonPayload.client.cn
principal.resource.attribute.labels[json_payload_client_cn]
jsonPayload.client.country
principal.location.country_or_region
jsonPayload.client.email.address
principal.email
jsonPayload.client.locality
principal.location.city
jsonPayload.client.organization
principal.resource_ancestors.name
principal.resource_ancestors.resource_type
If the
jsonPayload.client.organization
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
jsonPayload.client.organization.unit
principal.resource_ancestors.attribute.labels[client_organization_unit]
jsonPayload.client.port
principal.port
jsonPayload.client.received.end.time
principal.resource.attribute.labels[client_received_end_time]
jsonPayload.client.received.start.time
principal.resource.attribute.labels[client_received_start_time]
jsonPayload.client.sent.end.time
principal.resource.attribute.labels[client_sent_end_time]
jsonPayload.client.sent.start.time
principal.resource.attribute.labels[client_sent_start_time]
jsonPayload.client.ssl.enabled
principal.resource.attribute.labels[client_ssl_enabled]
jsonPayload.client.state
principal.resource.attribute.labels[client_state]
jsonPayload.current.flow.name
additional.fields[current_flow_name]
jsonPayload.current.flow.description
additional.fields[current_flow_description]
jsonPayload.environment.name
additional.fields[environment_name]
jsonPayload.error
security_result.about.resource.attribute.labels[jsonPayload_error]
jsonPayload.error.message
security_result.about.resource.attribute.labels[message]
jsonPayload.error.status.code
security_result.about.resource.attribute.labels[jsonPayload_error_status_code]
jsonPayload.error.reason.phrase
security_result.about.resource.attribute.labels[jsonPayload_error_reason_phrase]
jsonPayload.error.transport.message
security_result.about.resource.attribute.labels[jsonPayload_error_transport_message]
jsonPayload.error.header.header_name
security_result.about.resource.attribute.labels[error_header_name]
jsonPayload.fault.name
security_result.about.resource.attribute.labels[fault_name]
jsonPayload.fault.reason
security_result.about.resource.attribute.labels[fault_reason]
If the
jsonPayload.error.faultReason
log field value is empty, then the
jsonPayload.fault.reason
log field is mapped to the
security_result.description
UDM field.
Else, the
jsonPayload.fault.reason
log field is mapped to the
security_result.about.resource.attribute.labels.fault_reason
UDM field.
jsonPayload.fault.category
security_result.category_details
jsonPayload.fault.subcategory
security_result.category_details
jsonPayload.literal_value
additional.fields[jsonPayload_literal_value]
jsonPayload.graphql
additional.fields[graphql]
jsonPayload.graphql.fragment
additional.fields[graphql_fragment]
jsonPayload.graphql.fragment.count
additional.fields[graphql_fragment_count]
jsonPayload.graphql.fragment.INDEX.selectionSet.INDEX
additional.fields[graphql_fragment_INDEX_selectionSet_INDEX]
jsonPayload.graphql.fragment.INDEX.selectionSet.INDEX.name
additional.fields[graphql_fragment_INDEX_selectionSet_INDEX_name]
jsonPayload.graphql.fragment.INDEX.selectionSet.count
additional.fields[graphql_fragment_INDEX_selectionSet_count]
jsonPayload.graphql.fragment.INDEX.selectionSet.name
additional.fields[graphql_fragment_INDEX_selectionSet_name]
jsonPayload.graphql.operation
additional.fields[graphql_operation]
jsonPayload.graphql.operation.name
additional.fields[graphql_operation_name]
jsonPayload.graphql.operation.operationType
additional.fields[graphql_operation_operationType]
jsonPayload.graphql.operation.selectionSet
additional.fields[graphql_operation_selectionSet]
jsonPayload.graphql.operation.selectionSet.count
additional.fields[graphql_operation_selectionSet_count]
jsonPayload.graphql.operation.selectionSet.name
additional.fields[graphql_operation_selectionSet_name]
jsonPayload.graphql.operation.selectionSet.INDEX
additional.fields[graphql_operation_selectionSet_INDEX]
jsonPayload.graphql.operation.selectionSet.INDEX.name
additional.fields[graphql_operation_selectionSet_INDEX_name]
jsonPayload.graphql.operation.selectionSet.INDEX.[selectionSet]
additional.fields[graphql_operation_selectionSet_INDEX_selectionSet]
jsonPayload.graphql.operation.selectionSet.INDEX.directive
additional.fields[graphql_operation_selectionSet_INDEX_directive]
jsonPayload.graphql.operation.selectionSet.INDEX.directive.count
additional.fields[graphql_operation_selectionSet_INDEX_directive_count]
jsonPayload.graphql.operation.selectionSet.INDEX.directive.INDEX
additional.fields[graphql_operation_selectionSet_INDEX_directive_INDEX]
jsonPayload.graphql.operation.selectionSet.INDEX.directive.INDEX.argument.INDEX
additional.fields[graphql_operation_selectionSet_INDEX_directive_INDEX_argument_INDEX]
jsonPayload.graphql.operation.selectionSet.INDEX.directive.INDEX.argument.INDEX.name
additional.fields[graphql_operation_selectionSet_INDEX_directive_INDEX_argument_INDEX_name]
jsonPayload.graphql.operation.selectionSet.INDEX.directive.INDEX.argument.INDEX.value
additional.fields[graphql_operation_selectionSet_INDEX_directive_INDEX_argument_INDEX_value]
jsonPayload.graphql.operation.selectionSet.INDEX.directive.name
additional.fields[graphql_operation_selectionSet_INDEX_directive_name]
jsonPayload.graphql.operation.variableDefinitions
additional.fields[graphql_operation_variableDefinitions]
jsonPayload.graphql.operation.variableDefinitions.count
additional.fields[graphql_operation_variableDefinitions_count]
jsonPayload.graphql.operation.variableDefinitions.INDEX
additional.fields[graphql_operation_variableDefinitions_INDEX]
jsonPayload.graphql.operation.variableDefinitions.INDEX.name
additional.fields[graphql_operation_variableDefinitions_INDEX_name]
jsonPayload.graphql.operation.variableDefinitions.INDEX.type
additional.fields[graphql_operation_variableDefinitions_INDEX_type]
jsonPayload.is.error
security_result.about.resource.attribute.labels[is_error]
jsonPayload.loadbalancing.failedservers
intermediary.resource.attribute.labels[loadbalancing_failed_servers]
jsonPayload.loadbalancing.isfallback
intermediary.resource.attribute.labels[loadbalancing_is_fallback]
jsonPayload.loadbalancing.targetserver
intermediary.resource.attribute.labels[loadbalancing_target_server]
jsonPayload.message
additional.fields[jsonPayload_message]
jsonPayload.message.content
additional.fields[message_content]
jsonPayload.message.formparam.param_name
additional.fields[message_formparam_param_name]
jsonPayload.message.formparam.param_name.values
additional.fields[message_formparam_param_name_values]
jsonPayload.message.formparam.param_name.values.count
additional.fields[message_formparam_param_name_values_count]
jsonPayload.message.formparams.count
additional.fields[message_formparams_count]
jsonPayload.message.formparams.names
additional.fields[message_formparams_names]
jsonPayload.message.formstring
additional.fields[message_formstring]
jsonPayload.message.header.header_name
additional.fields[message_header_header_name]
jsonPayload.message.header.header_name.N
additional.fields[message_header_header_name_N]
jsonPayload.message.header.header_name.values
additional.fields[message_header_header_name_values]
jsonPayload.message.header.header_name.values.count
additional.fields[message_header_header_name_values_count]
jsonPayload.message.header.header_name.values.string
additional.fields[message_header_header_name_values_string]
jsonPayload.message.headers.count
additional.fields[message_headers_count]
jsonPayload.message.headers.names
additional.fields[message_headers_names]
jsonPayload.message.path
additional.fields[message_path]
jsonPayload.message.queryparam.param_name
additional.fields[message_queryparam_param_name]
jsonPayload.message.queryparam.param_name.N
additional.fields[message_queryparam_param_name_N]
jsonPayload.message.queryparam.param_name.values
additional.fields[message_queryparam_param_name_values]
jsonPayload.message.queryparam.param_name.values.count
additional.fields[message_queryparam_param_name_values_count]
jsonPayload.message.queryparams.count
additional.fields[message_queryparams_count]
jsonPayload.message.queryparams.names
additional.fields[message_queryparams_names]
jsonPayload.message.querystring
additional.fields[message_querystring]
jsonPayload.message.status.code
additional.fields[message_status_code]
jsonPayload.message.transport.message
additional.fields[message_transport_message]
jsonPayload.message.uri
additional.fields[message_uri]
jsonPayload.message.verb
additional.fields[message_verb]
jsonPayload.message.version
additional.fields[message_version]
jsonPayload.mint.limitscheck.is_request_blocked
additional.fields[mint_limitscheck_is_request_blocked]
jsonPayload.mint.limitscheck.is_subscription_found
additional.fields[mint_limitscheck_is_subscription_found]
jsonPayload.mint.limitscheck.prepaid_developer_balance
additional.fields[mint_limitscheck_prepaid_developer_balance]
jsonPayload.mint.limitscheck.prepaid_developer_currency
additional.fields[mint_limitscheck_prepaid_developer_currency]
jsonPayload.mint.limitscheck.purchased_product_name
additional.fields[mint_limitscheck_purchased_product_name]
jsonPayload.mint.limitscheck.status_message
additional.fields[mint_limitscheck_status_message]
jsonPayload.mint.mintng_consumption_pricing_rates
additional.fields[mint_mintng_consumption_pricing_rates]
jsonPayload.mint.mintng_consumption_pricing_type
additional.fields[mint_mintng_consumption_pricing_type]
jsonPayload.mint.mintng_currency
additional.fields[mint_mintng_currency]
jsonPayload.mint.mintng_dev_share
additional.fields[mint_mintng_dev_share]
jsonPayload.mint.mintng_is_apiproduct_monetized
additional.fields[mint_mintng_is_apiproduct_monetized]
jsonPayload.mint.mintng_price
additional.fields[mint_mintng_price]
jsonPayload.mint.mintng_price_multiplier
additional.fields[mint_mintng_price_multiplier]
jsonPayload.mint.mintng_rate
additional.fields[mint_mintng_rate]
jsonPayload.mint.mintng_rate_before_multipliers
additional.fields[mint_mintng_rate_before_multipliers]
jsonPayload.mint.mintng_rate_plan_id
additional.fields[mint_mintng_rate_plan_id]
jsonPayload.mint.mintng_revenue_share_rates
additional.fields[mint_mintng_revenue_share_rates]
jsonPayload.mint.mintng_revenue_share_type
additional.fields[mint_mintng_revenue_share_type]
jsonPayload.mint.mintng_tx_success
additional.fields[mint_mintng_tx_success]
jsonPayload.mint.prepaid_updated_developer_usage
additional.fields[mint_prepaid_updated_developer_usage]
jsonPayload.mint.rateplan_end_time_ms
additional.fields[mint_rateplan_end_time_ms]
jsonPayload.mint.rateplan_start_time_ms
additional.fields[mint_rateplan_start_time_ms]
jsonPayload.mint.status
additional.fields[mint_status]
jsonPayload.mint.status_code
additional.fields[mint_status_code]
jsonPayload.mint.subscription_end_time_ms
additional.fields[mint_subscription_end_time_ms]
jsonPayload.mint.subscription_start_time_ms
additional.fields[mint_subscription_start_time_ms]
jsonPayload.mint.tx_success_result
additional.fields[mint_tx_success_result]
jsonPayload.organization.name
principal.resource_ancestors.name
principal.resource_ancestors.resource_type
If the
jsonPayload.organization.name
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
jsonPayload.proxy.basepath
intermediary.resource.attribute.labels[proxy_basepath]
jsonPayload.proxy
intermediary.resource.attribute.labels[proxy]
jsonPayload.proxy.proxyendpoint.name
intermediary.resource.attribute.labels[proxy_endpoint_name]
jsonPayload.publishmessage.message.id
additional.fields[publishmessage_message_id]
jsonPayload.ratelimit.policy_name.allowed.count
security_result.rule_labels[ratelimit_policy_name_allowed_count]
jsonPayload.ratelimit.policy_name.used.count
security_result.rule_labels[ratelimit_policy_name_used_count]
jsonPayload.ratelimit.policy_name.available.count
security_result.rule_labels[ratelimit_policy_name_available_count]
jsonPayload.ratelimit.policy_name.exceed.count
security_result.rule_labels[ratelimit_policy_name_exceed_count]
jsonPayload.ratelimit.policy_name.total.exceed.count
security_result.rule_labels[ratelimit_policy_name_total_exceed_count]
jsonPayload.ratelimit.policy_name.expiry.time
security_result.rule_labels[ratelimit_policy_name_expiry_time]
jsonPayload.ratelimit.policy_name.identifier
security_result.rule_id
jsonPayload.ratelimit.policy_name.class
security_result.rule_labels[ratelimit_policy_name_class]
jsonPayload.ratelimit.policy_name.class.allowed.count
security_result.rule_labels[ratelimit_policy_name_class_allowed_count]
jsonPayload.ratelimit.policy_name.class.used.count
security_result.rule_labels[ratelimit_policy_name_class_used_count]
jsonPayload.ratelimit.policy_name.class.available.count
security_result.rule_labels[ratelimit_policy_name_class_available_count]
jsonPayload.ratelimit.policy_name.class.exceed.count
security_result.rule_labels[ratelimit_policy_name_class_exceed_count]
jsonPayload.ratelimit.policy_name.class.total.exceed.count
security_result.rule_labels[ratelimit_policy_name_class_total_exceed_count]
jsonPayload.ratelimit.policy_name.failed
security_result.rule_labels[ratelimit_policy_name_failed]
jsonPayload.request
target.resource.attribute.labels[request]
jsonPayload.request.formparam.param_name.values.count
target.resource.attribute.labels[request_formparam_name_values_count]
jsonPayload.request.formparam.param_name.N
target.resource.attribute.labels[request_formparam_name_N]
jsonPayload.request.grpc.rpc.name
target.resource.attribute.labels[request_grpc_rpc_name]
jsonPayload.request.grpc.service.name
target.resource.attribute.labels[request_grpc_service_name]
jsonPayload.request.header.header_name.N
target.resource.attribute.labels[request_header_name_N]
jsonPayload.request.header.header_name.values.count
target.resource.attribute.labels[request_header_name_values_count]
jsonPayload.request.header.header_name.values.string
target.resource.attribute.labels[request_header_name_values_string]
jsonPayload.request.headers.count
target.resource.attribute.labels[request_headers_count]
jsonPayload.request.headers.names
target.resource.attribute.labels[request_headers_names]
jsonPayload.request.queryparam.param_name.N
target.resource.attribute.labels[request_queryparam_name_N]
jsonPayload.request.queryparam.param_name.values.count
target.resource.attribute.labels[request_queryparam_name_values_count]
jsonPayload.request.transport.message
target.resource.attribute.labels[request_transport_message]
jsonPayload.response
target.resource.attribute.labels[response]
jsonPayload.response.header.header_name.values.count
target.resource.attribute.labels[response_header_name_values_count]
jsonPayload.response.header.header_name.values.string
target.resource.attribute.labels[response_header_name_values_string]
jsonPayload.response.header.header_name.N
target.resource.attribute.labels[response_header_name_N]
jsonPayload.system.interface.interface_name
intermediary.ip
intermediary.resource_ancestors.resource_type
If the
jsonPayload.system.pod.name
log field value is
not
empty, then the
intermediary.resource_ancestors.resource_type
UDM field is set to
POD
.
jsonPayload.system.pod.name
intermediary.resource_ancestors.name
jsonPayload.system.region.name
intermediary.location.country_or_region
jsonPayload.system.time
intermediary.resource.attribute.labels[system_time]
jsonPayload.system.time.year
intermediary.resource.attribute.labels[system_time_year]
jsonPayload.system.time.month
intermediary.resource.attribute.labels[system_time_month]
jsonPayload.system.time.day
intermediary.resource.attribute.labels[system_time_day]
jsonPayload.system.time.dayofweek
intermediary.resource.attribute.labels[system_time_dayofweek]
jsonPayload.system.time.hour
intermediary.resource.attribute.labels[system_time_hour]
jsonPayload.system.time.minute
intermediary.resource.attribute.labels[system_time_minute]
jsonPayload.system.time.second
intermediary.resource.attribute.labels[system_time_second]
jsonPayload.system.time.millisecond
intermediary.resource.attribute.labels[system_time_millisecond]
jsonPayload.system.time.zone
intermediary.resource.attribute.labels[system_time_zone]
jsonPayload.system.uuid
intermediary.resource.attribute.labels[system_uuid]
jsonPayload.target.copy.pathsuffix
target.resource.attribute.labels[target_copy_pathsuffix]
jsonPayload.target.copy.queryparams
target.resource.attribute.labels[target_copy_queryparams]
jsonPayload.target.country
target.location.country_or_region
jsonPayload.target.email.address
target.user.email_addresses
jsonPayload.developer.email
target.user.email_addresses
jsonPayload.target.expectedcn
target.resource.attribute.labels[target_expectedcn]
jsonPayload.target.locality
target.location.city
jsonPayload.target.name
target.resource.attribute.labels[target_name]
jsonPayload.target.received.end.time
target.resource.attribute.labels[target_received_end_time]
jsonPayload.target.received.start.time
target.resource.attribute.labels[target_received_start_time]
jsonPayload.target.received.start.timestamp
target.resource.attribute.labels[target_received_start_timestamp]
jsonPayload.target.sent.end.time
target.resource.attribute.labels[target_sent_end_time]
jsonPayload.target.sent.start.time
target.resource.attribute.labels[target_sent_start_time]
jsonPayload.target.ssl.enabled
target.resource.attribute.labels[target_ssl_enabled]
jsonPayload.target.state
target.resource.attribute.labels[target_state]
jsonPayload.variable.expectedcn
additional.fields[variable_expectedcn]
jsonPayload.request.host
target.resource.attribute.labels[json_payload_request_host]
jsonPayload.request_msg.header.host
target.resource.attribute.labels[json_payload_request_host]
jsonPayload.request.user-agent
network.http.user_agent
jsonPayload.request.header.user-agent
network.http.user_agent
jsonPayload.request.x-b3-traceid
target.resource.attribute.labels[json_payload_request_x_b3_traceid]
jsonPayload.request.header.x-b3-traceid
target.resource.attribute.labels[json_payload_request_x_b3_traceid]
jsonPayload.request.header.x-cloud-trace-context
target.resource.attribute.labels[json_payload_request_x_cloud_trace_context]
jsonPayload.request.x-cloud-trace-context
target.resource.attribute.labels[json_payload_request_x_cloud_trace_context]
jsonPayload.apiproduct.name
intermediary.resource.attribute.labels[jsonPayload_api_product_name]
jsonPayload.app.name
target.application
jsonPayload.developer.app.name
target.application
jsonPayload.cachehit
additional.fields[jsonPayload_cachehit]
Field mapping reference: GCP_APIGEE_X Log Collection with ServiceCallout Policy logs
The following table lists the log fields of the
GCP_APIGEE_X
(Legacy) Log Collection with ServiceCallout Policy log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
jsonPayload.proxyResponseCode
intermediary.network.http.response_code
jsonPayload.apiProxy
intermediary.resource.name
jsonPayload.apiproxy
intermediary.resource.name
intermediary.resource.resource_type
If the
jsonPayload.apiproxy
log field value is
not
empty or the
jsonPayload.apiProxy
log field value is
not
empty, then the
intermediary.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
intermediary.resource.attribute.cloud.environment
If the
jsonPayload.apiproxy
log field value is
not
empty or the
jsonPayload.apiProxy
log field value is
not
empty, then the
intermediary.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
jsonPayload.apiProduct
intermediary.resource.attribute.labels[json_payload_api_product]
jsonPayload.apiProxyRevision
intermediary.resource.attribute.labels[json_payload_api_proxy_revision]
jsonPayload.proxyRequestReceived
intermediary.resource.attribute.labels[json_payload_proxy_request_received]
jsonPayload.proxyResponseSent
intermediary.resource.attribute.labels[json_payload_proxy_response_sent]
receiveTimestamp
metadata.collected_timestamp
timestamp
metadata.event_timestamp
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_RESOURCE_ACCESS
.
insertId
metadata.product_log_id
jsonPayload.correlationId
metadata.product_event_type
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP APIGEE X
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
jsonPayload.verb
network.http.method
labels.application
principal.application
jsonPayload.ax_resolved_client_ip
principal.ip
resource.labels.zone
principal.resource.attribute.cloud.availability_zone
principal.resource.resource_type
If the
resource.type
log field value is equal to
gce_instance
, then the
principal.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
resource.type
principal.resource.resource_subtype
resource.labels.instance_id
principal.resource.product_object_id
resource.labels.project_id
principal.resource_ancestors.product_object_id
principal.resource_ancestors.resource_type
If the
resource.labels.project_id
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
jsonPayload.organization
principal.resource_ancestors.name
principal.resource_ancestors.resource_type
If the
jsonPayload.organization
log field value is
not
empty, then the
principal.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
jsonPayload.clientReceived
principal.resource.attribute.labels[json_payload_client_received]
jsonPayload.clientSent
principal.resource.attribute.labels[json_payload_client_sent]
logName
principal.resource.attribute.labels[Log Name]
resource.labels.project_id
principal.resource.attribute.labels[Project Id]
jsonPayload.clientId
principal.user.userid
logName
security_result.category_details
jsonPayload.faultName
security_result.description
severity
security_result.severity
If the
severity
log field value is equal to
ERROR
, then the
severity
log field is mapped to the
security_result.severity
UDM field.
Else, if the
severity
log field value is equal to
INFO
or
NOTICE
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
severity
log field value is equal to
WARNING
or
NOTICE
, then the
security_result.severity
UDM field is set to
MEDIUM
.
severity
security_result.severity_details
jsonPayload.targetResponseCode
target.network.http.response_code
jsonPayload.requestUri
target.resource.name
target.resource.resource_type
If the
jsonPayload.requestUri
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
jsonPayload.requestUrl
target.url
jsonPayload.targetResponseReceived
target.resource.attribute.labels[json_payload_target_request_received]
jsonPayload.targetRequestSent
target.resource.attribute.labels[json_payload_target_request_sent]
jsonPayload.bot_reason
additional.fields[json_payload_bot_reason]
jsonPayload.count_distinct_bot
additional.fields[json_payload_count_distinct_bot]
jsonPayload.developerApp
additional.fields[json_payload_developer_app]
jsonPayload.developerId
additional.fields[json_payload_developer_id]
jsonPayload.minute
additional.fields[json_payload_minute]
jsonPayload.environment
additional.fields[json_payload_environment]
jsonPayload.sum_bot_traffic
additional.fields[json_payload_sum_bot_traffic]
partialSuccess
additional.fields[partial_success]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
