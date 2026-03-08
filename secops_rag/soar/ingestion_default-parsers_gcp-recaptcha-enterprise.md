# Collect reCAPTCHA Enterprise logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-recaptcha-enterprise/  
**Scraped:** 2026-03-05T09:59:31.860413Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect reCAPTCHA Enterprise logs
Supported in:
Google secops
SIEM
This document describes how you can collect reCAPTCHA Enterprise logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of reCAPTCHA Enterprise logs map to Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations overview
.
A typical deployment consists of reCAPTCHA Enterprise logs that are enabled for ingestion to Google Security Operations. Each customer deployment might differ and might be more complex.
Consider a deployment that contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
reCAPTCHA Enterprise logs
: The reCAPTCHA Enterprise logs that are
enabled for ingestion to Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from reCAPTCHA Enterprise.
You need to use an ingestion label to identify the parser which normalizes raw log data to structured UDM format. This document applies to the parser with the
GCP_RECAPTCHA_ENTERPRISE
ingestion label.
Before you begin
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Ensure that you have enabled
platform logging for reCAPTCHA Enterprise
specifically for the following:
Assessment logs
Annotation logs
Configure Google Cloud for ingestion
To ingest reCAPTCHA Enterprise logs to Google Security Operations, follow the steps on the
Ingest Google Cloud data to Google Security Operations
page.
If you encounter issues when you ingest reCAPTCHA Enterprise logs,
contact Google Security Operations support
.
Field mapping reference
Field mapping reference: reCAPTCHA Enterprise - Assessment
The following table lists the log fields of the
Assessment
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.product_name
The
metadata.product_name
UDM field is set to
reCAPTCHA
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
metadata.event_type
The
metadata.event_type
UDM field is set to
USER_UNCATEGORIZED
.
jsonPayload.@type
metadata.product_event_type
jsonPayload.name
security_result.detection_fields[json_payload_name]
insertId
metadata.product_log_id
timestamp
metadata.event_timestamp
logName
metadata.url_back_to_product
The
https://console.cloud.google.com/logs?%{logName}
field is mapped to the
metadata.url_back_to_product
UDM field.
receiveTimestamp
metadata.collected_timestamp
resource.labels.key_id
target.resource.product_object_id
resource.type
target.resource.resource_subtype
resource.labels.location
target.location.name
resource.labels.resource_container
target.resource.attribute.labels[resource_labels_resource_container]
labels.backend_language
target.resource.attribute.labels[labels_backend_language]
labels.demo_key
target.resource.attribute.labels[labels_demo_key]
jsonPayload.event.userAgent
network.http.user_agent
jsonPayload.event.userIpAddress
principal.ip
principal.resource.resource_type
If
jsonPayload.event.token
log field value is
not
empty, then
principal.resource.resource_type
UDM field is set to
CREDENTIAL
.
jsonPayload.event.token
principal.resource.product_object_id
jsonPayload.event.siteKey
security_result.detection_fields[event_site_key]
jsonPayload.event.hashedAccountId
principal.user.attribute.labels[event_hashed_account_id]
jsonPayload.event.expectedAction
principal.user.attribute.labels[event_expected_action]
jsonPayload.tokenProperties.action
principal.resource.attribute.labels[token_properties_action]
jsonPayload.tokenProperties.createTime
principal.resource.attribute.creation_time
jsonPayload.tokenProperties.hostname
target.hostname
jsonPayload.tokenProperties.invalidReason
principal.resource.attribute.labels[token_properties_invalid_reason]
jsonPayload.tokenProperties.valid
principal.resource.attribute.labels[token_properties_valid]
jsonPayload.tokenProperties.androidPackageName
principal.resource.attribute.labels[token_properties_android_package_name]
jsonPayload.tokenProperties.iosBundleId
principal.resource.attribute.labels[token_properties_ios_bundle_id]
security_result.verdict_info.verdict_type
If the
jsonPayload.riskAnalysis.reasons
log field value is
not
empty, then the
security_result.verdict_info.verdict_type
UDM field is set to
PROVIDER_ML_VERDICT
.
jsonPayload.riskAnalysis.reasons
security_result.verdict_info.category_details
If the
index
value is equal to
0
, then the
jsonPayload.riskAnalysis.reasons
log field is mapped to the
security_result.verdict_info.category_details
UDM field.
Else, the
jsonPayload.riskAnalysis.reasons
log field is mapped to the
security_result.detection_fields.risk_analysis_reasons
UDM field.
jsonPayload.riskAnalysis.reasons
security_result.detection_fields[risk_analysis_reasons]
If the
index
value is equal to
0
, then the
jsonPayload.riskAnalysis.reasons
log field is mapped to the
security_result.verdict_info.category_details
UDM field.
Else, the
jsonPayload.riskAnalysis.reasons
log field is mapped to the
security_result.detection_fields.risk_analysis_reasons
UDM field.
jsonPayload.riskAnalysis.score
security_result.risk_score
jsonPayload.riskAnalysis.extendedVerdictReasons
security_result.detection_fields[risk_analysis_extended_verdict_reasons]
jsonPayload.event.express
additional.fields[event_express]
jsonPayload.event.requestedUri
target.url
jsonPayload.event.wafTokenAssessment
security_result.detection_fields[event_waf_token_assessment]
jsonPayload.event.ja3
network.tls.client.ja3
jsonPayload.event.headers
additional.fields[event_headers_%{index}]
The
jsonPayload.event.headers
log field is mapped to the
additional.fields[event_headers_%{index}]
UDM field.
jsonPayload.event.firewallPolicyEvaluation
additional.fields[event_firewall_policy_evaluation]
jsonPayload.event.userInfo.createAccountTime
principal.user.attribute.creation_time
jsonPayload.event.userInfo.accountId
principal.user.userid
If the
jsonPayload.event.userInfo.accountId
log field value is
not
empty, then the
jsonPayload.event.userInfo.accountId
log field is mapped to the
principal.user.userid
UDM field.
Else, the
jsonPayload.event.transactionData.user.accountId
log field is mapped to the
principal.user.userid
UDM field.
jsonPayload.event.userInfo.userIds.email
principal.user.email_addresses
jsonPayload.event.userInfo.userIds.phoneNumber
principal.user.phone_numbers
jsonPayload.event.userInfo.userIds.username
principal.user.user_display_name
If the
index
value is equal to
0
, then the
jsonPayload.event.userInfo.userIds.username
log field is mapped to the
principal.user.user_display_name
UDM field.
Else, the
jsonPayload.event.userInfo.userIds.username
log field is mapped to the
principal.user.attribute.labels.event_user_info_user_ids_username
UDM field.
jsonPayload.event.userInfo.userIds.username
principal.user.attribute.labels[event_user_info_user_ids_username]
If the
index
value is equal to
0
, then the
jsonPayload.event.userInfo.userIds.username
log field is mapped to the
principal.user.user_display_name
UDM field.
Else, the
jsonPayload.event.userInfo.userIds.username
log field is mapped to the
principal.user.attribute.labels.event_user_info_user_ids_username
UDM field.
jsonPayload.event.transactionData.transactionId
security_result.detection_fields[event_transaction_data_transaction_id]
jsonPayload.event.transactionData.paymentMethod
security_result.detection_fields[event_transaction_data_payment_method]
jsonPayload.event.transactionData.cardBin
security_result.detection_fields[event_transaction_data_card_bin]
jsonPayload.event.transactionData.cardLastFour
security_result.detection_fields[event_transaction_data_card_last_four]
jsonPayload.event.transactionData.currencyCode
security_result.detection_fields[event_transaction_data_currency_code]
jsonPayload.event.transactionData.value
security_result.detection_fields[event_transaction_data_value]
jsonPayload.event.transactionData.shippingValue
security_result.detection_fields[event_transaction_data_shipping_value]
jsonPayload.event.transactionData.shippingAddress.recipient
principal.user.attribute.labels[event_transaction_data_shipping_address_recipient]
jsonPayload.event.transactionData.shippingAddress.address
principal.user.personal_address.name
If the
index
value is equal to
0
, then the
jsonPayload.event.transactionData.shippingAddress.address
log field is mapped to the
principal.user.personal_address.name
UDM field.
Else, the
jsonPayload.event.transactionData.shippingAddress.address
log field is mapped to the
principal.user.attribute.labels.event_transaction_data_shipping_address_address
UDM field.
jsonPayload.event.transactionData.shippingAddress.address
principal.user.attribute.labels[event_transaction_data_shipping_address_address]
If the
index
value is equal to
0
, then the
jsonPayload.event.transactionData.shippingAddress.address
log field is mapped to the
principal.user.personal_address.name
UDM field.
Else, the
jsonPayload.event.transactionData.shippingAddress.address
log field is mapped to the
principal.user.attribute.labels.event_transaction_data_shipping_address_address
UDM field.
jsonPayload.event.transactionData.shippingAddress.locality
principal.user.personal_address.city
jsonPayload.event.transactionData.shippingAddress.administrativeArea
principal.user.personal_address.state
jsonPayload.event.transactionData.shippingAddress.regionCode
principal.user.personal_address.country_or_region
jsonPayload.event.transactionData.shippingAddress.postalCode
principal.user.attribute.labels[event_transaction_data_shipping_address_postal_code]
jsonPayload.event.transactionData.billingAddress.recipient
about.user.attribute.labels[event_transaction_data_billing_address_recipient]
jsonPayload.event.transactionData.billingAddress.address
about.user.personal_address.name
If the
index
value is equal to
0
, then the
jsonPayload.event.transactionData.billingAddress.address
log field is mapped to the
about.user.personal_address.name
UDM field.
Else, the
jsonPayload.event.transactionData.billingAddress.address
log field is mapped to the
about.user.attribute.labels.event_transaction_data_billing_address_address
UDM field.
jsonPayload.event.transactionData.billingAddress.address
about.user.attribute.labels[event_transaction_data_billing_address_address]
If the
index
value is equal to
0
, then the
jsonPayload.event.transactionData.billingAddress.address
log field is mapped to the
about.user.personal_address.name
UDM field.
Else, the
jsonPayload.event.transactionData.billingAddress.address
log field is mapped to the
about.user.attribute.labels.event_transaction_data_billing_address_address
UDM field.
jsonPayload.event.transactionData.billingAddress.locality
about.user.personal_address.city
jsonPayload.event.transactionData.billingAddress.administrativeArea
about.user.personal_address.state
jsonPayload.event.transactionData.billingAddress.regionCode
about.user.personal_address.country_or_region
jsonPayload.event.transactionData.billingAddress.postalCode
about.user.attribute.labels[event_transaction_data_billing_address_postal_code]
jsonPayload.event.transactionData.user.accountId
principal.user.userid
If the
jsonPayload.event.userInfo.accountId
log field value is
not
empty, then the
jsonPayload.event.userInfo.accountId
log field is mapped to the
principal.user.userid
UDM field.
Else, the
jsonPayload.event.transactionData.user.accountId
log field is mapped to the
principal.user.userid
UDM field.
jsonPayload.event.transactionData.user.creationMs
principal.user.attribute.creation_time
jsonPayload.event.transactionData.user.email
principal.user.email_addresses
jsonPayload.event.transactionData.user.emailVerified
principal.user.attribute.labels[event_transaction_data_user_email_verified]
jsonPayload.event.transactionData.user.phoneNumber
principal.user.phone_numbers
jsonPayload.event.transactionData.user.phoneVerified
principal.user.attribute.labels[event_transaction_data_user_phone_verified]
jsonPayload.event.transactionData.merchants.accountId
about.user.userid
jsonPayload.event.transactionData.merchants.creationMs
about.user.attribute.creation_time
jsonPayload.event.transactionData.merchants.email
about.user.email_addresses
jsonPayload.event.transactionData.merchants.emailVerified
about.user.attribute.labels[event_transaction_data_merchants_email_verified]
jsonPayload.event.transactionData.merchants.phoneNumber
about.user.phone_numbers
jsonPayload.event.transactionData.merchants.phoneVerified
about.user.attribute.labels[event_transaction_data_merchants_phone_verified]
jsonPayload.event.transactionData.gatewayInfo.name
security_result.detection_fields[event_transaction_data_gateway_info_name]
jsonPayload.event.transactionData.gatewayInfo.gatewayResponseCode
security_result.detection_fields[event_transaction_data_gateway_info_gateway_response_code]
jsonPayload.event.transactionData.gatewayInfo.avsResponseCode
security_result.detection_fields[event_transaction_data_gateway_info_avs_response_code]
jsonPayload.event.transactionData.gatewayInfo.cvvResponseCode
security_result.detection_fields[event_transaction_data_gateway_info_cvv_response_code]
jsonPayload.event.transactionData.items.name
security_result.detection_fields[event_transaction_data_items_name]
jsonPayload.event.transactionData.items.value
security_result.detection_fields[event_transaction_data_items_value]
jsonPayload.event.transactionData.items.quantity
security_result.detection_fields[event_transaction_data_items_quantity]
jsonPayload.event.transactionData.items.merchantAccountId
security_result.detection_fields[event_transaction_data_items_merchant_account_id]
jsonPayload.accountVerification.endpoints.requestToken
principal.user.attribute.labels[account_verification_endpoint_request_token]
jsonPayload.accountVerification.endpoints.lastVerificationTime
principal.user.attribute.labels[account_verification_endpoint_last_verification_time]
jsonPayload.accountVerification.endpoints.emailAddress
principal.user.email_addresses
jsonPayload.accountVerification.endpoints.phoneNumber
principal.user.phone_numbers
jsonPayload.accountVerification.languageCode
additional.fields[account_verification_language_code]
security_result.action
If the
jsonPayload.accountVerification.latestVerificationResult
log field value is equal to
SUCCESS_USER_VERIFIED
, then the
security_result.action
UDM field is set to
CHALLENGE
.
Else, if the
jsonPayload.accountVerification.latestVerificationResult
log field value is equal to
ERROR_USER_NOT_VERIFIED
, then the
security_result.action
UDM field is set to
FAIL
.
Else, if the
jsonPayload.accountVerification.latestVerificationResult
log field value is equal to
ERROR_RECIPIENT_NOT_ALLOWED
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, if the
jsonPayload.accountVerification.latestVerificationResult
log field value is equal to
ERROR_VERDICT_MISMATCH
, then the
security_result.action
UDM field is set to
ALLOW_WITH_MODIFICATION
.
Else, the
security_result.action
UDM field is set to
UNKNOWN_ACTION
.
jsonPayload.accountVerification.latestVerificationResult
security_result.action_details
jsonPayload.accountDefenderAssessment.labels
security_result.detection_fields[account_defender_assessment_labels]
jsonPayload.privatePasswordLeakVerification.lookupHashPrefix
principal.user.attribute.labels[private_password_leak_verification_lookup_hash_prefix]
jsonPayload.privatePasswordLeakVerification.encryptedUserCredentialsHash
principal.user.attribute.labels[private_password_leak_verification_encrypted_user_credentials_hash]
jsonPayload.privatePasswordLeakVerification.encryptedLeakMatchPrefixes
principal.user.attribute.labels[private_password_leak_verification_encrypted_leak_match_prefixes]
jsonPayload.privatePasswordLeakVerification.reencryptedUserCredentialsHash
principal.user.attribute.labels[private_password_leak_verification_reencrypted_user_credentials_hash]
network.http.response_code
If the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
0
, then the
network.http.response_code
UDM field is set to
200
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value contains one of the following values, then the
network.http.response_code
UDM field is set to
400
.
9
11
3
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
16
, then the
network.http.response_code
UDM field is set to
401
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
7
, then the
network.http.response_code
UDM field is set to
403
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
5
, then the
network.http.response_code
UDM field is set to
404
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value contains one of the following values, then the
network.http.response_code
UDM field is set to
409
.
10
6
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
8
, then the
network.http.response_code
UDM field is set to
429
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
1
, then the
network.http.response_code
UDM field is set to
499
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value contains one of the following values, then the
network.http.response_code
UDM field is set to
500
.
13
15
2
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
12
, then the
network.http.response_code
UDM field is set to
501
.
Else, if the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
14
, then the
network.http.response_code
UDM field is set to
503
.
Else the
jsonPayload.firewallPolicyAssessment.error.code
log field value is equal to
4
, then the
network.http.response_code
UDM field is set to
504
.
jsonPayload.firewallPolicyAssessment.error.message
security_result.detection_fields[firewall_policy_assessment_error_message]
jsonPayload.firewallPolicyAssessment.error.details
security_result.detection_fields[firewall_policy_assessment_error_details]
jsonPayload.fraudPreventionAssessment.transactionRisk
security_result.detection_fields[fraud_prevention_assessment_transaction_risk]
jsonPayload.fraudPreventionAssessment.stolenInstrumentVerdict.risk
security_result.detection_fields[fraud_prevention_assessment_stolen_instrument_verdict_risk]
jsonPayload.fraudPreventionAssessment.cardTestingVerdict.risk
security_result.detection_fields[fraud_prevention_assessment_card_testing_erdict_risk]
jsonPayload.fraudPreventionAssessment.behavioralTrustVerdict.trust
security_result.detection_fields[fraud_prevention_assessment_behavioral_trust_verdict_trust]
jsonPayload.fraudSignals.userSignals.activeDaysLowerBound
security_result.detection_fields[fraud_signals_user_signals_active_days_lower_bound]
jsonPayload.fraudSignals.userSignals.syntheticRisk
security_result.detection_fields[fraud_signals_user_signals_synthetic_risk]
jsonPayload.fraudSignals.cardSignals.cardLabels
security_result.detection_fields[fraud_signals_card_signals_card_labels]
jsonPayload.firewallPolicyAssessment.firewallPolicy.name
intermediary.resource.name
intermediary.resource.resource_type
If the
jsonPayload.firewallPolicyAssessment.firewallPolicy.name
log field value is
not
empty, then the
intermediary.resource.resource_type
UDM field is set to
FIREWALL_RULE
.
jsonPayload.firewallPolicyAssessment.firewallPolicy.description
intermediary.resource.attribute.labels[firewall_policy_assessment_description]
jsonPayload.firewallPolicyAssessment.firewallPolicy.path
intermediary.resource.attribute.labels[firewall_policy_assessment_path]
jsonPayload.firewallPolicyAssessment.firewallPolicy.conditions
intermediary.resource.attribute.labels[firewall_policy_assessment_conditions]
security_result.action
If the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.allow
log field value is
not
empty, then the
security_result.action
UDM field is set to
ALLOW
.
security_result.action
If the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.block
log field value is
not
empty, then the
security_result.action
UDM field is set to
BLOCK
.
security_result.action
If the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.redirect
log field value is
not
empty, then the
security_result.action
UDM field is set to
CHALLENGE
.
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.substitute.path
target.url_metadata.last_final_url
If the
index
value is equal to
0
, then the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.substitute.path
log field is mapped to the
target.url_metadata.last_final_url
UDM field.
Else, the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.substitute.path
log field is mapped to the
intermediary.resource.attribute.labels.firewall_policy_assessment_firewall_policy_actions_substitute_path
UDM field.
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.substitute.path
intermediary.resource.attribute.labels[firewall_policy_assessment_firewall_policy_actions_substitute_path]
If the
index
value is equal to
0
, then the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.substitute.path
log field is mapped to the
target.url_metadata.last_final_url
UDM field.
Else, the
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.substitute.path
log field is mapped to the
intermediary.resource.attribute.labels.firewall_policy_assessment_firewall_policy_actions_substitute_path
UDM field.
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.setHeader.key
intermediary.resource.attribute.labels[firewall_policy_assessment_firewall_policy_actions_set_header_key]
jsonPayload.firewallPolicyAssessment.firewallPolicy.actions.setHeader.value
intermediary.resource.attribute.labels[firewall_policy_assessment_firewall_policy_actions_set_header_value]
Field mapping reference: reCAPTCHA Enterprise - Annotation
The following table lists the log fields of the
Annotation
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.product_name
The
metadata.product_name
UDM field is set to
reCAPTCHA
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
jsonPayload.@type
metadata.product_event_type
insertId
metadata.product_log_id
timestamp
metadata.event_timestamp
logName
metadata.url_back_to_product
The
https://console.cloud.google.com/logs?%{logName}
field is mapped to the
metadata.url_back_to_product
UDM field.
receiveTimestamp
metadata.collected_timestamp
jsonPayload.name
security_result.detection_fields[json_payload_name]
resource.labels.key_id
target.resource.product_object_id
resource.type
target.resource.resource_subtype
resource.labels.location
target.location.name
resource.labels.resource_container
target.resource.attribute.labels[resource_labels_resource_container]
labels.backend_language
target.resource.attribute.labels[labels_backend_language]
labels.demo_key
target.resource.attribute.labels[labels_demo_key]
security_result.verdict_info.verdict_response
If the
jsonPayload.annotation
log field value is equal to
LEGITIMATE
, then the
security_result.verdict_info.verdict_response
UDM field is set to
BENIGN
.
Else, if the
jsonPayload.annotation
log field value is equal to
FRAUDULENT
, then the
security_result.verdict_info.verdict_response
UDM field is set to
MALICIOUS
.
Else, the
jsonPayload.annotation
log field value is equal to
ANNOTATION_UNSPECIFIED
, then the
security_result.verdict_info.verdict_response
UDM field is set to
VERDICT_RESPONSE_UNSPECIFIED
.
jsonPayload.reasons
security_result.verdict_info.category_details
If the
index
value is equal to
0
, then the
jsonPayload.reasons
log field is mapped to the
security_result.verdict_info.category_details
UDM field.
Else, the
jsonPayload.reasons
log field is mapped to the
security_result.detection_fields.reasons
UDM field.
jsonPayload.reasons
security_result.detection_fields[reasons]
If the
index
value is equal to
0
, then the
jsonPayload.reasons
log field is mapped to the
security_result.verdict_info.category_details
UDM field.
Else, the
jsonPayload.reasons
log field is mapped to the
security_result.detection_fields.reasons
UDM field.
jsonPayload.accountId
target.user.userid
jsonPayload.hashedAccountId
target.user.attribute.labels[hashed_account_id]
jsonPayload.transactionEvent.eventType
security_result.detection_fields[transaction_event_event_type]
jsonPayload.transactionEvent.reason
security_result.detection_fields[transaction_event_reason]
jsonPayload.transactionEvent.value
security_result.detection_fields[transaction_event_value]
jsonPayload.transactionEvent.eventTime
security_result.detection_fields[transaction_event_event_time]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
