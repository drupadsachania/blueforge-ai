# Collect Google Cloud Run functions context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/gcp-cloud-functions-context/  
**Scraped:** 2026-03-05T09:48:08.319232Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud Run functions context logs
This document describes how fields of Google Cloud Run functions context logs map to Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_CLOUD_FUNCTIONS_CONTEXT
ingestion label.
For information about other context parsers that Google SecOps supports, see
Google SecOps context parsers
.
Supported Google Cloud Run functions context logs log formats
The Google Cloud Run functions context logs parser supports logs in JSON format.
Supported Google Cloud Run functions context logs sample logs
JSON:
{
  "name": "//cloudfunctions.googleapis.com/projects/cspm-32817/locations/asia-south1/functions/GetNSPAAlertsFunction-asia-south1",
  "assetType": "cloudfunctions.googleapis.com/CloudFunction",
  "resource": {
    "version": "v1",
    "discoveryDocumentUri": "https://cloudfunctions.googleapis.com/$discovery/rest",
    "discoveryName": "CloudFunction",
    "parent": "//cloudresourcemanager.googleapis.com/projects/1063885730524",
    "data": {
      "availableMemoryMb": 256,
      "buildId": "843ffd9a-eab1-4022-8d0f-256e55d110d3",
      "buildName": "projects/1063885730524/locations/asia-south1/builds/843ffd9a-eab1-4022-8d0f-256e55d110d3",
      "dockerRegistry": "CONTAINER_REGISTRY",
      "entryPoint": "google_cloud_function_handler",
      "eventTrigger": {
        "eventType": "google.pubsub.topic.publish",
        "failurePolicy": {},
        "resource": "projects/cspm-32817/topics/GetNSPAAlerts-asia-south1",
        "service": "pubsub.googleapis.com"
      },
      "ingressSettings": "ALLOW_ALL",
      "labels": {
        "deployment-tool": "console-cloud"
      },
      "maxInstances": 3000,
      "name": "projects/cspm-32817/locations/asia-south1/functions/GetNSPAAlertsFunction-asia-south1",
      "runtime": "python37",
      "serviceAccountEmail": "dummy@user.com",
      "sourceArchiveUrl": "gs://cloudfunctionscrest/GetNetskopeSecurityPostureAssessmentFunction (2).zip",
      "status": "ACTIVE",
      "timeout": "300s",
      "updateTime": "2023-04-21T13:33:30.711Z",
      "versionId": "1"
    }
  },
  "ancestors": [
    "projects/1063885730524",
    "organizations/595779152576"
  ]
}
Field mapping reference
This section explains how the Google SecOps parser maps Google Cloud Run functions context logs fields to Google SecOps UDM fields.
Log field
UDM mapping
Logic
entity.relations.resource.resource_type
The
entity.relations.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
entity.relations.resource.resource_subtype
The
entity.relations.resource.resource_subtype
UDM field is set to
project
.
entity.relations.resource_ancestors.resource_type
If the
ancestor
log field value matches the regular expression pattern
organizations
, then the
entity.relations.resource_ancestors.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
Else, if the
ancestor
log field value matches the regular expression pattern
folders
, then the
entity.relations.resource_ancestors.resource_type
UDM field is set to
STORAGE_OBJECT
.
entity.relations.resource_ancestors.resource_subtype
If the
ancestor
log field value matches the regular expression pattern
organizations
, then the
entity.relations.resource_ancestors.resource_subtype
UDM field is set to
organizations
.
Else, if the
ancestor
log field value matches the regular expression pattern
folders
, then the
entity.relations.resource_ancestors.resource_subtype
UDM field is set to
folders
.
entity.relations.relationship
The
entity.relations.relationship
UDM field is set to
MEMBER
.
resource.parent, ancestors[]
entity.relations.entity.resource.name
If the
resource.parent
log field value is empty, then the
ancestors.0
log field is mapped to the
relations.entity.resource.name
UDM field.
ancestors[]
entity.relations.entity.resource_ancestors.name
If the
ancestor
log field value is not a substring of
resource.parent
log field value, then the
ancestors
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
entity.relations.entity_type
The
entity.relations.entity_type
UDM field is set to
RESOURCE
.
entity.relations.direction
The
entity.relations.direction
UDM field is set to
UNIDIRECTIONAL
.
entity.metadata.vendor_name
The
entity.metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
resource.version
entity.metadata.product_version
entity.metadata.product_name
The
entity.metadata.product_name
UDM field is set to
GCP Cloud Functions
.
entity.metadata.entity_type
The
entity.metadata.entity_type
UDM field is set to
RESOURCE
.
resource.data.description
entity.metadata.description
resource.data.serviceAccountEmail, resource.data.serviceConfig.serviceAccountEmail
entity.entity.user.email_addresses
resource.data.httpsTrigger.url, resource.data.serviceConfig.uri
entity.entity.url
resource.data.stateMessages.type
entity.entity.threat.summary
resource.data.stateMessages.severity
entity.entity.threat.product_severity
resource.data.stateMessages.message
entity.entity.threat.description
entity.entity.resource.resource_type
The
entity.entity.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
assetType
entity.entity.resource.resource_subtype
resource.data.name
entity.entity.resource.product_object_id
name
entity.entity.resource.name
resource.data.updateTime
entity.entity.resource.attribute.last_update_time
resource.data.network
entity.entity.resource.attribute.labels[vpc_network]
resource.data.vpcConnector, resource.data.serviceConfig.vpcConnector
entity.entity.resource.attribute.labels[vpc_connector]
resource.data.vpcConnectorEgressSettings, resource.data.serviceConfig.vpcConnectorEgressSettings
entity.entity.resource.attribute.labels[vpc_connector_egress_settings]
resource.data.versionId
entity.entity.resource.attribute.labels[version_id]
resource.data.timeout, resource.data.serviceConfig.timeoutSeconds
entity.entity.resource.attribute.labels[timeout]
resource.data.buildConfig.source.storageSource.object
entity.entity.resource.attribute.labels[storage_source_object]
resource.data.buildConfig.source.storageSource.generation
entity.entity.resource.attribute.labels[storage_source_generation]
resource.data.buildConfig.source.storageSource.bucket
entity.entity.resource.attribute.labels[storage_source_bucket]
resource.data.sourceUploadUrl
entity.entity.resource.attribute.labels[source_upload_url]
resource.data.sourceToken
entity.entity.resource.attribute.labels[source_token]
resource.data.sourceRepository.url
entity.entity.resource.attribute.labels[source_repo_url]
resource.data.sourceRepository.deployedUrl
entity.entity.resource.attribute.labels[source_repo_deployed_url]
resource.data.sourceArchiveUrl
entity.entity.resource.attribute.labels[source_archive_url]
resource.data.serviceConfig.service
entity.entity.resource.attribute.labels[service_config_service]
resource.data.serviceConfig.revision
entity.entity.resource.attribute.labels[service_config_revision]
resource.data.serviceConfig.maxInstanceRequestConcurrency
entity.entity.resource.attribute.labels[service_config_max_instance_request_concurrency]
resource.data.serviceConfig.availableCpu
entity.entity.resource.attribute.labels[service_config_available_cpu]
resource.data.serviceConfig.allTrafficOnLatestRevision
entity.entity.resource.attribute.labels[service_config_all_traffic_on_latest_revision]
resource.data.httpsTrigger.securityLevel, resource.data.serviceConfig.securityLevel
entity.entity.resource.attribute.labels[security_level]
resource.data.secretVolumes.versions.version, resource.data.serviceConfig.secretVolumes.versions.version
entity.entity.resource.attribute.labels[secret_vol_ver_version]
resource.data.secretVolumes.versions.path, resource.data.serviceConfig.secretVolumes.versions.path
entity.entity.resource.attribute.labels[secret_vol_ver_path]
resource.data.secretVolumes.secret, resource.data.serviceConfig.secretVolumes.secret
entity.entity.resource.attribute.labels[secret_vol_secret]
resource.data.secretVolumes.projectId, resource.data.serviceConfig.secretVolumes.projectId
entity.entity.resource.attribute.labels[secret_vol_project_id]
resource.data.secretVolumes.mountPath, resource.data.serviceConfig.secretVolumes.mountPath
entity.entity.resource.attribute.labels[secret_vol_mount_path]
resource.data.secretEnvironmentVariables.version, resource.data.serviceConfig.secretEnvironmentVariables.version
entity.entity.resource.attribute.labels[secret_env_var_version]
resource.data.secretEnvironmentVariables.secret, resource.data.serviceConfig.secretEnvironmentVariables.secret
entity.entity.resource.attribute.labels[secret_env_var_secret]
resource.data.secretEnvironmentVariables.projectId, resource.data.serviceConfig.secretEnvironmentVariables.projectId
entity.entity.resource.attribute.labels[secret_env_var_project_id]
resource.data.secretEnvironmentVariables.key, resource.data.serviceConfig.secretEnvironmentVariables.key
entity.entity.resource.attribute.labels[secret_env_var_key]
resource.data.runtime, resource.data.buildConfig.runtime
entity.entity.resource.attribute.labels[runtime]
resource.data.buildConfig.sourceProvenance.resolvedStorageSource.object
entity.entity.resource.attribute.labels[resolved_storage_source_object]
resource.data.buildConfig.sourceProvenance.resolvedStorageSource.generation
entity.entity.resource.attribute.labels[resolved_storage_source_generation]
resource.data.buildConfig.sourceProvenance.resolvedStorageSource.bucket
entity.entity.resource.attribute.labels[resolved_storage_source_bucket]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.tagName
entity.entity.resource.attribute.labels[resolved_repo_source_tag_name]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.repoName
entity.entity.resource.attribute.labels[resolved_repo_source_repo_name]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.projectId
entity.entity.resource.attribute.labels[resolved_repo_source_project_id]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.invertRegex
entity.entity.resource.attribute.labels[resolved_repo_source_invert_regex]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.dir
entity.entity.resource.attribute.labels[resolved_repo_source_dir]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.commitSha
entity.entity.resource.attribute.labels[resolved_repo_source_commit_sha]
resource.data.buildConfig.sourceProvenance.resolvedRepoSource.branchName
entity.entity.resource.attribute.labels[resolved_repo_source_branch_name]
resource.data.buildConfig.source.repoSource.tagName
entity.entity.resource.attribute.labels[repo_source_tag_name]
resource.data.buildConfig.source.repoSource.repoName
entity.entity.resource.attribute.labels[repo_source_repo_name]
resource.data.buildConfig.source.repoSource.projectId
entity.entity.resource.attribute.labels[repo_source_project_id]
resource.data.buildConfig.source.repoSource.invertRegex
entity.entity.resource.attribute.labels[repo_source_invert_regex]
resource.data.buildConfig.source.repoSource.dir
entity.entity.resource.attribute.labels[repo_source_dir]
resource.data.buildConfig.source.repoSource.commitSha
entity.entity.resource.attribute.labels[repo_source_commit_sha]
resource.data.buildConfig.source.repoSource.branchName
entity.entity.resource.attribute.labels[repo_source_branch_name]
resource.data.minInstances, resource.data.serviceConfig.minInstanceCount
entity.entity.resource.attribute.labels[min_instance]
resource.data.maxInstances, resource.data.serviceConfig.maxInstanceCount
entity.entity.resource.attribute.labels[max_instance]
resource.data.kmsKeyName
entity.entity.resource.attribute.labels[kms_key_name]
resource.data.ingressSettings, resource.data.serviceConfig.ingressSettings
entity.entity.resource.attribute.labels[ingress_settings]
resource.data.buildConfig.environmentVariables.GOOGLE_FUNCTION_SOURCE
entity.entity.resource.attribute.labels[GOOGLE_FUNCTION_SOURCE]
resource.data.labels.goog-managed-by
entity.entity.resource.attribute.labels[goog-managed-by]
resource.data.status, resource.data.state
entity.entity.resource.attribute.labels[function_status]
resource.data.eventTrigger.trigger
entity.entity.resource.attribute.labels[event_trigger_trigger]
resource.data.eventTrigger.triggerRegion
entity.entity.resource.attribute.labels[event_trigger_trigger_reason]
resource.data.eventTrigger.service
entity.entity.resource.attribute.labels[event_trigger_service]
resource.data.eventTrigger.serviceAccountEmail
entity.entity.resource.attribute.labels[event_trigger_service_account_email]
resource.data.eventTrigger.retryPolicy
entity.entity.resource.attribute.labels[event_trigger_retry_policy]
resource.data.eventTrigger.resource
entity.entity.resource.attribute.labels[event_trigger_resource]
resource.data.eventTrigger.pubsubTopic
entity.entity.resource.attribute.labels[event_trigger_pubsub_topic]
resource.data.eventTrigger.eventFilters.value
entity.entity.resource.attribute.labels[event_trigger_evt_filter_value]
resource.data.eventTrigger.eventFilters.operator
entity.entity.resource.attribute.labels[event_trigger_evt_filter_operator]
resource.data.eventTrigger.eventFilters.attribute
entity.entity.resource.attribute.labels[event_trigger_evt_filter_attribute]
resource.data.eventTrigger.eventType
entity.entity.resource.attribute.labels[event_trigger_event_type]
resource.data.eventTrigger.channel
entity.entity.resource.attribute.labels[event_trigger_channel]
resource.data.environment
entity.entity.resource.attribute.labels[environment]
resource.data.entryPoint, resource.data.buildConfig.entryPoint
entity.entity.resource.attribute.labels[entry_point]
resource.data.dockerRepository, resource.data.buildConfig.dockerRepository
entity.entity.resource.attribute.labels[docker_repository]
resource.data.dockerRegistry, resource.data.buildConfig.dockerRegistry
entity.entity.resource.attribute.labels[docker_registry]
resource.discoveryName
entity.entity.resource.attribute.labels[discovery_name]
resource.discoveryDocumentUri
entity.entity.resource.attribute.labels[discovery_document_uri]
resource.data.labels.deployment-tool
entity.entity.resource.attribute.labels[deployment_tool]
resource.data.buildWorkerPool, resource.data.buildConfig.workerPool
entity.entity.resource.attribute.labels[build_worker_pool]
resource.data.buildName, resource.data.buildConfig.build
entity.entity.resource.attribute.labels[build_name]
resource.data.buildId
entity.entity.resource.attribute.labels[build_id]
resource.data.availableMemoryMb, resource.data.serviceConfig.availableMemory
entity.entity.resource.attribute.labels[available_memory]
entity.entity.resource.attribute.cloud.environment
The
entity.entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.data.environmentVariables.TAXII_VERSION, resource.data.serviceConfig.environmentVariables.TAXII_VERSION
entity.enity.resource.attribute.labels[TAXII_VERSION]
resource.data.environmentVariables.TAXII_USERNAME, resource.data.serviceConfig.environmentVariables.TAXII_USERNAME
entity.enity.resource.attribute.labels[TAXII_USERNAME]
resource.data.environmentVariables.TAXII_PASSWORD_SECRET_PATH, resource.data.serviceConfig.environmentVariables.TAXII_PASSWORD_SECRET_PATH
entity.enity.resource.attribute.labels[TAXII_PASSWORD_SECRET_PATH]
resource.data.environmentVariables.TAXII_DISCOVERY_URL, resource.data.serviceConfig.environmentVariables.TAXII_DISCOVERY_URL
entity.enity.resource.attribute.labels[TAXII_DISCOVERY_URL]
resource.data.environmentVariables.CHRONICLE_SERVICE_ACCOUNT, resource.data.serviceConfig.environmentVariables.CHRONICLE_SERVICE_ACCOUNT
entity.enity.resource.attribute.labels[CHRONICLE_SERVICE_ACCOUNT]
resource.data.environmentVariables.CHRONICLE_CUSTOMER_ID, resource.data.serviceConfig.environmentVariables.CHRONICLE_CUSTOMER_ID
entity.enity.resource.attribute.labels[CHRONICLE_CUSTOMER_ID]
