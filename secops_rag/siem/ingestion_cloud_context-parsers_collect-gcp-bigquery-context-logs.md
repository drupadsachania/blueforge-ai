# Collect Google Cloud BigQuery context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/collect-gcp-bigquery-context-logs/  
**Scraped:** 2026-03-05T09:17:11.819809Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud BigQuery context logs
This document describes how fields of Google Cloud BigQuery context logs map to Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_BIGQUERY_CONTEXT
ingestion label.
For information about other context parsers that Google SecOps supports, see
Google SecOps context parsers
.
Supported Google Cloud BigQuery context log formats
The Google Cloud BigQuery context parser supports logs in JSON format.
Supported Google Cloud BigQuery context sample logs
JSON:
{
  "name": "dummyname",
  "assetType": "bigquery.googleapis.com/Table",
  "resource": {
    "version": "v2",
    "discoveryDocumentUri": "https://www.googleapis.com/discovery/v1/apis/bigquery/v2/rest",
    "discoveryName": "Table",
    "parent": "//bigquery.googleapis.com/projects/smp-project-prod/datasets/dset_2021_ingest",
    "data": {
      "creationTime": "1624332841842",
      "description": "Output data from dataflow",
      "id": "dummy_id",
      "kind": "bigquery#table",
      "location": "US",
      "schema": {
        "fields": [
          {
            "description": "",
            "name": "ia_time",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "year_mth_id",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "new_mem_attr_id",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "etg_id",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "sev_level",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "tx_ind",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "tos_i_5",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "gbo",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "channel",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "formulary",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "outlier",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "complete",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "network_paid_status_id",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "provider_status_id",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "amt_req",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "amt_eqv",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "amt_pay",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "amt_np",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "scripts",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "days_sup",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "generic",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "script_gen",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "meta_file_name",
            "type": "TYPE_STRING"
          },
          {
            "description": "",
            "name": "bq_load_timestamp",
            "type": "TYPE_TIMESTAMP"
          }
        ]
      },
      "tableReference": {
        "datasetId": "dset_2021_ingest",
        "projectId": "smp-project-prod",
        "tableId": "l2_sample_202106_land"
      },
      "timePartitioning": {
        "type": "DAY"
      }
    }
  },
  "ancestors": [
    "projects/111111111180",
    "folders/111111111525",
    "folders/111111111900",
    "folders/111111111330",
    "organizations/111111111402"
  ]
}
Field mapping reference
This section explains how the Google SecOps parser maps Google Cloud BigQuery context fields to Google SecOps Unified Data Model (UDM) fields.
Field mapping reference: GCP_BIGQUERY_CONTEXT
The following table lists the log fields of the
GCP_BIGQUERY_CONTEXT
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
resource.data.location
entity.location.country_or_region
resource.data.creationTime
entity.resource.attribute.creation_time
resource.data.lastModifiedTime
entity.resource.attribute.last_update_time
name
entity.resource.name
resource.data.id
entity.resource.product_object_id
If the
assetType
log field value does
not
match the regular expression pattern
Model
, then the
resource.data.id
log field is mapped to the
entity.resource.product_object_id
UDM field.
resource.data.modelReference.projectId
entity.resource.product_object_id
If the
assetType
log field value matches the regular expression pattern
Model
, then the
resource.data.modelReference.projectId:resource.data.modelReference.datasetId.resource.data.modelReference.modelId
log field is mapped to the
entity.resource.product_object_id
UDM field.
resource.data.modelReference.datasetId
entity.resource.product_object_id
If the
assetType
log field value matches the regular expression pattern
Model
, then the
resource.data.modelReference.projectId:resource.data.modelReference.datasetId.resource.data.modelReference.modelId
log field is mapped to the
entity.resource.product_object_id
UDM field.
resource.data.modelReference.modelId
entity.resource.product_object_id
If the
assetType
log field value matches the regular expression pattern
Model
, then the
resource.data.modelReference.projectId:resource.data.modelReference.datasetId.resource.data.modelReference.modelId
log field is mapped to the
entity.resource.product_object_id
UDM field.
assetType
entity.resource.resource_subtype
entity.resource.resource_type
If the
assetType
log field value matches the regular expression pattern
Table
, then the
entity.resource.resource_type
UDM field is set to
TABLE
.
Else, if the
assetType
log field value matches the regular expression pattern
Dataset
, then the
entity.resource.resource_type
UDM field is set to
DATASET
.
Else, if the
assetType
log field value matches the regular expression pattern
Model
, then the
entity.resource.resource_type
UDM field is set to
TASK
.
entity.security_result.rule_name
If the
resource.data.view.privacyPolicy.aggregationThresholdPolicy.threshold
log field value is
not
empty, then the
entity.security_result.rule_name
UDM field is set to
privacy_policy
.
resource.data.description
metadata.description
metadata.entity_type
The
metadata.entity_type
UDM field is set to
RESOURCE
.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP BigQuery
.
resource.version
metadata.product_version
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
relations.direction
The
relations.direction
UDM field is set to
UNIDIRECTIONAL
if one of the following log field value is
not
empty:
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
resource.data.snapshotDefinition.baseTableReference.tableId
resource.data.cloneDefinition.baseTableReference.tableId
resource.data.linkedDatasetSource.sourceDataset.datasetId
resource.data.linkedDatasetSource.sourceDataset.projectId
resource.data.remoteModelInfo.connection
resource.data.externalDataConfiguration.sourceUris
resource.data.externalDataConfiguration.connectionId
resource.data.access.role
If the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
If the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
If the
resource.data.tableReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
Else, if the
resource.data.modelReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
Else, if the
resource.parent
log field value matches the regular expression pattern
projects
, then the
relations.direction
UDM field is set to
UNIDIRECTIONAL
.
relations.entity_type
The
relations.entity_type
UDM field is set to
RESOURCE
if one of the following log field value is
not
empty:
resource.parent
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
resource.data.snapshotDefinition.baseTableReference.tableId
resource.data.cloneDefinition.baseTableReference.tableId
resource.data.linkedDatasetSource.sourceDataset.datasetId
resource.data.linkedDatasetSource.sourceDataset.projectId
resource.data.remoteModelInfo.connection
resource.data.externalDataConfiguration.sourceUris
resource.data.externalDataConfiguration.connectionId
resource.data.access.role
If the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
relations.entity_type
UDM field is set to
RESOURCE
.
If the
resource.data.tableReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.entity_type
UDM field is set to
RESOURCE
.
If the
resource.data.modelReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.entity_type
UDM field is set to
RESOURCE
.
resource.data.access.domain
relations.entity.domain.name
resource.data.access.groupByEmail
relations.entity.group.email_addresses
resource.data.access.specialGroup
relations.entity.group.group_display_name
resource.data.snapshotDefinition.baseTableReference.projectId
relations.entity.resource_ancestors.name
If the
resource.data.snapshotDefinition.baseTableReference.projectId
log field value is
not
empty, then the
resource.data.snapshotDefinition.baseTableReference.projectId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.snapshotDefinition.baseTableReference.datasetId
relations.entity.resource_ancestors.name
If the
resource.data.snapshotDefinition.baseTableReference.datasetId
log field value is
not
empty, then the
resource.data.snapshotDefinition.baseTableReference.datasetId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.cloneDefinition.baseTableReference.projectId
relations.entity.resource_ancestors.name
If the
resource.data.cloneDefinition.baseTableReference.projectId
log field value is
not
empty, then the
resource.data.cloneDefinition.baseTableReference.projectId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.cloneDefinition.baseTableReference.datasetId
relations.entity.resource_ancestors.name
If the
resource.data.cloneDefinition.baseTableReference.datasetId
log field value is
not
empty, then the
resource.data.cloneDefinition.baseTableReference.datasetId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.trainingRuns.dataSplitResult.trainingTable.projectId
relations.entity.resource_ancestors.name
If the
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.trainingTable.projectId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.trainingRuns.dataSplitResult.trainingTable.datasetId
relations.entity.resource_ancestors.name
If the
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.trainingTable.datasetId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.trainingRuns.dataSplitResult.evaluationTable.projectId
relations.entity.resource_ancestors.name
If the
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.evaluationTable.projectId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.trainingRuns.dataSplitResult.evaluationTable.datasetId
relations.entity.resource_ancestors.name
If the
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.evaluationTable.datasetId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.trainingRuns.dataSplitResult.testTable.projectId
relations.entity.resource_ancestors.name
If the
resource.data.trainingRuns.dataSplitResult.testTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.testTable.projectId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
resource.data.trainingRuns.dataSplitResult.testTable.datasetId
relations.entity.resource_ancestors.name
If the
resource.data.trainingRuns.dataSplitResult.testTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.testTable.datasetId
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
relations.entity.resource_ancestors.resource_subtype
The
relations.entity.resource_ancestors.resource_subtype
UDM field is set to
projects
if one of the following log field value is
not
empty:
resource.data.snapshotDefinition.baseTableReference.projectId
resource.data.cloneDefinition.baseTableReference.projectId
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
The
relations.entity.resource_ancestors.resource_subtype
UDM field is set to
datasets
if one of the following log field value is
not
empty:
resource.data.snapshotDefinition.baseTableReference.datasetId
resource.data.cloneDefinition.baseTableReference.datasetId
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
relations.entity.resource_ancestors.resource_type
The
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
if one of the following log field value is
not
empty:
resource.data.snapshotDefinition.baseTableReference.projectId
resource.data.cloneDefinition.baseTableReference.projectId
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
The
relations.entity.resource_ancestors.resource_type
UDM field is set to
DATASET
if one of the following log field value is
not
empty:
resource.data.snapshotDefinition.baseTableReference.datasetId
resource.data.cloneDefinition.baseTableReference.datasetId
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
resource.data.snapshotDefinition.snapshotTime
relations.entity.resource.attribute.creation_time
resource.data.cloneDefinition.cloneTime
relations.entity.resource.attribute.creation_time
ancestors
relations.entity.resource.name
If the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
ancestors
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.parent
relations.entity.resource.name
resource.data.snapshotDefinition.baseTableReference.tableId
relations.entity.resource.name
If the
resource.data.snapshotDefinition.baseTableReference.tableId
log field value is
not
empty, then the
resource.data.snapshotDefinition.baseTableReference.tableId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.cloneDefinition.baseTableReference.tableId
relations.entity.resource.name
If the
resource.data.cloneDefinition.baseTableReference.tableId
log field value is
not
empty, then the
resource.data.cloneDefinition.baseTableReference.tableId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.datasetReference.projectId
relations.entity.resource.name
If the
resource.parent
log field value is
not
empty, then the
resource.data.datasetReference.projectId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.tableReference.datasetId
relations.entity.resource.name
If the
resource.parent
log field value is
not
empty, then the
resource.data.tableReference.datasetId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.modelReference.projectId
relations.entity.resource.name
If the
resource.parent
log field value is
not
empty, then the
resource.data.modelReference.projectId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.linkedDatasetSource.sourceDataset.datasetId
relations.entity.resource.name
If the
resource.data.linkedDatasetSource.sourceDataset.datasetId
log field value is
not
empty, then the
resource.data.linkedDatasetSource.sourceDataset.datasetId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.linkedDatasetSource.sourceDataset.projectId
relations.entity.resource.name
If the
resource.data.linkedDatasetSource.sourceDataset.projectId
log field value is
not
empty, then the
resource.data.linkedDatasetSource.sourceDataset.projectId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.remoteModelInfo.connection
relations.entity.resource.name
If the
resource.data.remoteModelInfo.connection
log field value is
not
empty, then the
resource.data.remoteModelInfo.connection
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
relations.entity.resource.name
If the
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
relations.entity.resource.name
If the
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.trainingRuns.dataSplitResult.testTable.tableId
relations.entity.resource.name
If the
resource.data.trainingRuns.dataSplitResult.testTable.tableId
log field value is
not
empty, then the
resource.data.trainingRuns.dataSplitResult.testTable.tableId
log field is mapped to the
relations.entity.resource.name
UDM field.
resource.data.externalDataConfiguration.connectionId
relations.entity.resource.product_object_id
If the
resource.data.externalDataConfiguration.connectionId
log field value is
not
empty, then the
resource.data.externalDataConfiguration.connectionId
log field is mapped to the
relations.entity.resource.product_object_id
UDM field.
resource.data.externalDataConfiguration.sourceFormat
relations.entity.resource.resource_subtype
If the
resource.data.externalDataConfiguration.connectionId
log field value is
not
empty, then the
resource.data.externalDataConfiguration.sourceFormat
log field is mapped to the
relations.entity.resource.resource_subtype
UDM field.
resource.data.remoteModelInfo.remoteServiceType
relations.entity.resource.resource_subtype
If the
resource.data.remoteModelInfo.connection
log field value is
not
empty, then the
resource.data.remoteModelInfo.remoteServiceType
log field is mapped to the
relations.entity.resource.resource_subtype
UDM field.
relations.entity.resource.resource_type
The
relations.entity.resource.resource_type
UDM field is set to
TABLE
if one of the following log field value is
not
empty:
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
resource.data.snapshotDefinition.baseTableReference.tableId
resource.data.cloneDefinition.baseTableReference.tableId
resource.data.externalDataConfiguration.connectionId
The
subtype
and
id
fields is extracted from
ancestors
log field using the Grok pattern.
If the
subtype
log field value is equal to
projects
and the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
subtype
log field value is equal to
folders
and the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
relations.entity.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
Else, if the
subtype
log field value is equal to
organizations
and the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
If the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.entity.resource.resource_type
UDM field is set to
DATASET
.
If the
resource.data.tableReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
resource.data.modelReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
Else, if the
resource.parent
log field value matches the regular expression pattern
projects
, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
If the
resource.data.linkedDatasetSource.sourceDataset.datasetId
log field value is
not
empty, then the
relations.entity.resource.resource_type
UDM field is set to
DATASET
.
If the
resource.data.linkedDatasetSource.sourceDataset.projectId
log field value is
not
empty, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
If the
resource.data.remoteModelInfo.connection
log field value is
not
empty, then the
relations.entity.resource.resource_type
UDM field is set to
TASK
.
resource.data.access.role
relations.entity.user.attribute.roles.name
resource.data.access.userByEmail
relations.entity.user.email_addresses
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
if one of the following log field value is
not
empty:
resource.parent
resource.data.trainingRuns.dataSplitResult.trainingTable.tableId
resource.data.trainingRuns.dataSplitResult.evaluationTable.tableId
resource.data.trainingRuns.dataSplitResult.testTable.tableId
resource.data.linkedDatasetSource.sourceDataset.datasetId
resource.data.linkedDatasetSource.sourceDataset.projectId
resource.data.remoteModelInfo.connection
resource.data.externalDataConfiguration.sourceUris
resource.data.externalDataConfiguration.connectionId
The
relations.relationship
UDM field is set to
DOWNLOADED_FROM
if one of the following log field value is
not
empty:
resource.data.snapshotDefinition.baseTableReference.tableId
resource.data.cloneDefinition.baseTableReference.tableId
If the
resource.parent
log field value does
not
match the regular expression pattern the
ancestors
, then the
relations.relationship
UDM field is set to
MEMBER
.
If the
resource.data.tableReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.relationship
UDM field is set to
MEMBER
.
If the
resource.data.modelReference.projectId
log field value is
not
empty and the
resource.parent
log field value matches the regular expression pattern
datasets
, then the
relations.relationship
UDM field is set to
MEMBER
.
If the
resource.data.access.role
log field value is
not
empty, then the
relations.relationship
UDM field is set to
OWNS
.
resource.data.hparamTrials.errorMessage
entity.security_result.outcomes[hparam_trials_error_message]
resource.data.hparamTrials.evaluationMetrics.regressionMetrics.meanAbsoluteError
entity.security_result.outcomes[hparam_trials_evaluation_regression_metrics_mean_absolute_error]
resource.data.hparamTrials.evaluationMetrics.regressionMetrics.meanSquaredError
entity.security_result.outcomes[hparam_trials_evaluation_regression_metrics_mean_squared_error]
resource.data.hparamTrials.evaluationMetrics.regressionMetrics.meanSquaredLogError
entity.security_result.outcomes[hparam_trials_evaluation_regression_metrics_mean_squared_log_error]
resource.data.hparamTrials.evaluationMetrics.regressionMetrics.medianAbsoluteError
entity.security_result.outcomes[hparam_trials_evaluation_regression_metrics_median_absolute_error]
resource.data.hparamTrials.evaluationMetrics.regressionMetrics.rSquared
entity.security_result.outcomes[hparam_trials_evaluation_regression_metrics_r_squared]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.regressionMetrics.meanAbsoluteError
entity.security_result.outcomes[hparam_trials_tuning_evaluation_regression_metrics_mean_absolute_error]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.regressionMetrics.meanSquaredError
entity.security_result.outcomes[hparam_trials_tuning_evaluation_regression_metrics_mean_squared_error]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.regressionMetrics.meanSquaredLogError
entity.security_result.outcomes[hparam_trials_tuning_evaluation_regression_metrics_mean_squared_log_error]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.regressionMetrics.medianAbsoluteError
entity.security_result.outcomes[hparam_trials_tuning_evaluation_regression_metrics_median_absolute_error]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.regressionMetrics.rSquared
entity.security_result.outcomes[hparam_trials_tuning_evaluation_regression_metrics_r_squared]
resource.data.trainingRuns.evaluationMetrics.regressionMetrics.meanAbsoluteError
entity.security_result.outcomes[trainingruns_evaluation_regression_metrics_mean_absolute_error]
resource.data.trainingRuns.evaluationMetrics.regressionMetrics.meanSquaredError
entity.security_result.outcomes[trainingruns_evaluation_regression_metrics_mean_squared_error]
resource.data.trainingRuns.evaluationMetrics.regressionMetrics.meanSquaredLogError
entity.security_result.outcomes[trainingruns_evaluation_regression_metrics_mean_squared_log_error]
resource.data.trainingRuns.evaluationMetrics.regressionMetrics.medianAbsoluteError
entity.security_result.outcomes[trainingruns_evaluation_regression_metrics_median_absolute_error]
resource.data.trainingRuns.evaluationMetrics.regressionMetrics.rSquared
entity.security_result.outcomes[trainingruns_evaluation_regression_metrics_r_squared]
resource.data.trainingRuns.trainingOptions.lossType
entity.security_result.outcomes[trainingruns_training_options_loss_type]
resource.data.trainingRuns.trainingOptions.minSplitLoss
entity.security_result.outcomes[trainingruns_training_options_min_split_loss]
resource.data.view.privacyPolicy.aggregationThresholdPolicy.privacyUnitColumns
entity.security_result.rule_labels[view_privacy_policy_aggregation_threshold_policy_privacy_unit_columns]
resource.data.view.privacyPolicy.aggregationThresholdPolicy.threshold
entity.security_result.rule_labels[view_privacy_policy_aggregation_threshold_policy_threshold]
resource.data.hparamTrials.hparams.labelClassWeights
entity.resource.attribute.labels[%{resource.data.hparamTrials.hparams.labelClassWeights.key}]
resource.data.labels.key/value
entity.resource.attribute.labels[%{resource.data.labels.key}]
resource.data.trainingRuns.trainingOptions.labelClassWeights
entity.resource.attribute.labels[%{resource.data.trainingRuns.trainingOptions.labelClassWeights.key}]
resource.data.clustering.fields
entity.resource.attribute.labels[clustering_fields]
resource.data.datasetReference.datasetId
entity.resource.attribute.labels[dataset_reference_datasetid]
resource.data.defaultCollation
entity.resource.attribute.labels[default_collation]
resource.data.defaultEncryptionConfiguration.kmsKeyName
entity.resource.attribute.labels[default_encryption_configuration_kms_key_name]
resource.data.defaultPartitionExpirationMs
entity.resource.attribute.labels[default_partition_expiration_ms]
resource.data.defaultRoundingMode
entity.resource.attribute.labels[default_rounding_mode]
resource.data.defaultTableExpirationMs
entity.resource.attribute.labels[default_table_expiration_ms]
resource.data.defaultTrialId
entity.resource.attribute.labels[default_trialid]
resource.discoveryDocumentUri
entity.resource.attribute.labels[discovery_document_uri]
resource.discoveryName
entity.resource.attribute.labels[discovery_name]
resource.data.encryptionConfiguration.kmsKeyName
entity.resource.attribute.labels[encryption_configuration_kms_key_name]
resource.data.etag
entity.resource.attribute.labels[etag]
resource.data.expirationTime
entity.resource.attribute.labels[expiration_time]
resource.data.externalDatasetReference.connection
entity.resource.attribute.labels[external_dataset_reference_connection]
resource.data.externalDatasetReference.externalSource
entity.resource.attribute.labels[external_dataset_reference_external_source]
resource.data.featureColumns.name
entity.resource.attribute.labels[feature_columns_name]
resource.data.featureColumns.type.typeKind
entity.resource.attribute.labels[feature_columns_type_type_kind]
resource.data.friendlyName
entity.resource.attribute.labels[friendly_name]
resource.data.hparamSearchSpaces.activationFn.candidates
entity.resource.attribute.labels[hparam_search_spaces_activation_fn_candidates]
resource.data.hparamSearchSpaces.batchSize.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_batch_size_candidates_candidates]
resource.data.hparamSearchSpaces.batchSize.range.max
entity.resource.attribute.labels[hparam_search_spaces_batch_size_range_max]
resource.data.hparamSearchSpaces.batchSize.range.min
entity.resource.attribute.labels[hparam_search_spaces_batch_size_range_min]
resource.data.hparamSearchSpaces.boosterType.candidates
entity.resource.attribute.labels[hparam_search_spaces_booster_type_candidates]
resource.data.hparamSearchSpaces.colsampleBylevel.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_colsample_bylevel_candidates_candidates]
resource.data.hparamSearchSpaces.colsampleBylevel.range.max
entity.resource.attribute.labels[hparam_search_spaces_colsample_bylevel_range_max]
resource.data.hparamSearchSpaces.colsampleBylevel.range.min
entity.resource.attribute.labels[hparam_search_spaces_colsample_bylevel_range_min]
resource.data.hparamSearchSpaces.colsampleBynode.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_colsample_bynode_candidates_candidates]
resource.data.hparamSearchSpaces.colsampleBynode.range.max
entity.resource.attribute.labels[hparam_search_spaces_colsample_bynode_range_max]
resource.data.hparamSearchSpaces.colsampleBynode.range.min
entity.resource.attribute.labels[hparam_search_spaces_colsample_bynode_range_min]
resource.data.hparamSearchSpaces.colsampleBytree.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_colsample_bytree_candidates_candidates]
resource.data.hparamSearchSpaces.colsampleBytree.range.max
entity.resource.attribute.labels[hparam_search_spaces_colsample_bytree_range_max]
resource.data.hparamSearchSpaces.colsampleBytree.range.min
entity.resource.attribute.labels[hparam_search_spaces_colsample_bytree_range_min]
resource.data.hparamSearchSpaces.dartNormalizeType.candidates
entity.resource.attribute.labels[hparam_search_spaces_dart_normalize_type_candidates]
resource.data.hparamSearchSpaces.dropout.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_dropout_candidates_candidates]
resource.data.hparamSearchSpaces.dropout.range.max
entity.resource.attribute.labels[hparam_search_spaces_dropout_range_max]
resource.data.hparamSearchSpaces.dropout.range.min
entity.resource.attribute.labels[hparam_search_spaces_dropout_range_min]
resource.data.hparamSearchSpaces.hiddenUnits.candidates.elements
entity.resource.attribute.labels[hparam_search_spaces_hidden_units_candidates_elements]
resource.data.hparamSearchSpaces.l1Reg.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_l_1_reg_candidates_candidates]
resource.data.hparamSearchSpaces.l1Reg.range.max
entity.resource.attribute.labels[hparam_search_spaces_l_1_reg_range_max]
resource.data.hparamSearchSpaces.l1Reg.range.min
entity.resource.attribute.labels[hparam_search_spaces_l_1_reg_range_min]
resource.data.hparamSearchSpaces.l2Reg.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_l_2_reg_candidates_candidates]
resource.data.hparamSearchSpaces.l2Reg.range.max
entity.resource.attribute.labels[hparam_search_spaces_l_2_reg_range_max]
resource.data.hparamSearchSpaces.l2Reg.range.min
entity.resource.attribute.labels[hparam_search_spaces_l_2_reg_range_min]
resource.data.hparamSearchSpaces.learnRate.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_learn_rate_candidates_candidates]
resource.data.hparamSearchSpaces.learnRate.range.max
entity.resource.attribute.labels[hparam_search_spaces_learn_rate_range_max]
resource.data.hparamSearchSpaces.learnRate.range.min
entity.resource.attribute.labels[hparam_search_spaces_learn_rate_range_min]
resource.data.hparamSearchSpaces.maxTreeDepth.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_max_tree_depth_candidates_candidates]
resource.data.hparamSearchSpaces.maxTreeDepth.range.max
entity.resource.attribute.labels[hparam_search_spaces_max_tree_depth_range_max]
resource.data.hparamSearchSpaces.maxTreeDepth.range.min
entity.resource.attribute.labels[hparam_search_spaces_max_tree_depth_range_min]
resource.data.hparamSearchSpaces.minSplitLoss.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_min_split_loss_candidates_candidates]
resource.data.hparamSearchSpaces.minSplitLoss.range.max
entity.resource.attribute.labels[hparam_search_spaces_min_split_loss_range_max]
resource.data.hparamSearchSpaces.minSplitLoss.range.min
entity.resource.attribute.labels[hparam_search_spaces_min_split_loss_range_min]
resource.data.hparamSearchSpaces.minTreeChildWeight.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_min_tree_child_weight_candidates_candidates]
resource.data.hparamSearchSpaces.minTreeChildWeight.range.max
entity.resource.attribute.labels[hparam_search_spaces_min_tree_child_weight_range_max]
resource.data.hparamSearchSpaces.minTreeChildWeight.range.min
entity.resource.attribute.labels[hparam_search_spaces_min_tree_child_weight_range_min]
resource.data.hparamSearchSpaces.numClusters.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_num_clusters_candidates_candidates]
resource.data.hparamSearchSpaces.numClusters.range.max
entity.resource.attribute.labels[hparam_search_spaces_num_clusters_range_max]
resource.data.hparamSearchSpaces.numClusters.range.min
entity.resource.attribute.labels[hparam_search_spaces_num_clusters_range_min]
resource.data.hparamSearchSpaces.numFactors.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_num_factors_candidates_candidates]
resource.data.hparamSearchSpaces.numFactors.range.max
entity.resource.attribute.labels[hparam_search_spaces_num_factors_range_max]
resource.data.hparamSearchSpaces.numFactors.range.min
entity.resource.attribute.labels[hparam_search_spaces_num_factors_range_min]
resource.data.hparamSearchSpaces.numParallelTree.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_num_parallel_tree_candidates_candidates]
resource.data.hparamSearchSpaces.numParallelTree.range.max
entity.resource.attribute.labels[hparam_search_spaces_num_parallel_tree_range_max]
resource.data.hparamSearchSpaces.numParallelTree.range.min
entity.resource.attribute.labels[hparam_search_spaces_num_parallel_tree_range_min]
resource.data.hparamSearchSpaces.optimizer.candidates
entity.resource.attribute.labels[hparam_search_spaces_optimizer_candidates]
resource.data.hparamSearchSpaces.subsample.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_subsample_candidates_candidates]
resource.data.hparamSearchSpaces.subsample.range.max
entity.resource.attribute.labels[hparam_search_spaces_subsample_range_max]
resource.data.hparamSearchSpaces.subsample.range.min
entity.resource.attribute.labels[hparam_search_spaces_subsample_range_min]
resource.data.hparamSearchSpaces.treeMethod.candidates
entity.resource.attribute.labels[hparam_search_spaces_tree_method_candidates]
resource.data.hparamSearchSpaces.walsAlpha.candidates.candidates
entity.resource.attribute.labels[hparam_search_spaces_wals_alpha_candidates_candidates]
resource.data.hparamSearchSpaces.walsAlpha.range.max
entity.resource.attribute.labels[hparam_search_spaces_wals_alpha_range_max]
resource.data.hparamSearchSpaces.walsAlpha.range.min
entity.resource.attribute.labels[hparam_search_spaces_wals_alpha_range_min]
resource.data.hparamTrials.endTimeMs
entity.resource.attribute.labels[hparam_trials_end_time_ms]
resource.data.hparamTrials.evalLoss
entity.resource.attribute.labels[hparam_trials_eval_loss]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.aic
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_fitting_metrics_aic]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasDrift
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_has_drift]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasHolidayEffect
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_has_holiday_effect]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasSpikesAndDips
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_has_spikes_and_dips]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasStepChanges
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_has_step_changes]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.logLikelihood
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_fitting_metrics_log_likelihood]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.seasonalPeriods
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_seasonal_periods]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.timeSeriesId
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_time_series_id]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.timeSeriesIds
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_time_series_ids]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.variance
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_fitting_metrics_variance]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.d
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_non_seasonal_order_d]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.p
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_non_seasonal_order_p]
resource.data.hparamTrials.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.q
entity.resource.attribute.labels[hparam_trials_evaluation_arima_forecasting_single_model_non_seasonal_order_q]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.accuracy
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_accuracy]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.f1Score
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_f_1_score]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.logLoss
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_log_loss]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.precision
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_precision]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.recall
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_recall]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.rocAuc
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_roc_auc]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.threshold
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_aggregate_classification_metrics_threshold]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.accuracy
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_accuracy]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.f1Score
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_f_1_score]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.falseNegatives
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_false_negatives]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.falsePositives
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_false_positives]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.positiveClassThreshold
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_positive_class_threshold]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.precision
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_precision]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.recall
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_recall]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.trueNegatives
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_true_negatives]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.truePositives
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_confusion_matrix_list_true_positives]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.negativeLabel
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_negative_label]
resource.data.hparamTrials.evaluationMetrics.binaryClassificationMetrics.positiveLabel
entity.resource.attribute.labels[hparam_trials_evaluation_binary_classification_positive_label]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.clusters.centroidId
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_clusters_centroid_id]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.clusters.count
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_clusters_count]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.clusters.featureValues.categoricalValue.categoryCounts.category
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_feature_values_categorical_value_counts_category]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.clusters.featureValues.categoricalValue.categoryCounts.count
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_feature_values_categorical_value_counts_count]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.clusters.featureValues.featureColumn
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_feature_values_feature_column]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.clusters.featureValues.numericalValue
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_feature_values_numerical_value]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.daviesBouldinIndex
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_davies_bouldin_index]
resource.data.hparamTrials.evaluationMetrics.clusteringMetrics.meanSquaredDistance
entity.resource.attribute.labels[hparam_trials_evaluation_clustering_metrics_mean_squared_distance]
resource.data.hparamTrials.evaluationMetrics.dimensionalityReductionMetrics.totalExplainedVarianceRatio
entity.resource.attribute.labels[hparam_trials_evaluation_dimensionality_reduction_metrics_total_explained_variance_ratio]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.accuracy
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_accuracy]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.f1Score
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_f_1_score]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.logLoss
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_log_loss]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.precision
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_precision]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.recall
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_recall]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.rocAuc
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_roc_auc]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.threshold
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_aggregate_classification_metrics_threshold]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.confidenceThreshold
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_confusion_matrix_list_confidence_threshold]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.actualLabel
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_confusion_matrix_list_rows_actual_label]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.entries.itemCount
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_confusion_matrix_list_rows_entries_item_count]
resource.data.hparamTrials.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.entries.predictedLabel
entity.resource.attribute.labels[hparam_trials_evaluation_multiclass_classification_confusion_matrix_list_rows_entries_predicted_label]
resource.data.hparamTrials.evaluationMetrics.rankingMetrics.averageRank
entity.resource.attribute.labels[hparam_trials_evaluation_ranking_metrics_average_rank]
resource.data.hparamTrials.evaluationMetrics.rankingMetrics.meanAveragePrecision
entity.resource.attribute.labels[hparam_trials_evaluation_ranking_metrics_mean_average_precision]
resource.data.hparamTrials.evaluationMetrics.rankingMetrics.meanSquaredError
entity.resource.attribute.labels[hparam_trials_evaluation_ranking_metrics_mean_squared_error]
resource.data.hparamTrials.evaluationMetrics.rankingMetrics.normalizedDiscountedCumulativeGain
entity.resource.attribute.labels[hparam_trials_evaluation_ranking_metrics_normalized_discounted_cumulative_gain]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.aic
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_fitting_metrics_aic]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasDrift
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_has_drift]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasHolidayEffect
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_has_holiday_effect]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasSpikesAndDips
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_has_spikes_and_dips]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasStepChanges
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_has_step_changes]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.logLikelihood
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_fitting_metrics_log_likelihood]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.seasonalPeriods
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_seasonal_periods]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.timeSeriesId
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_time_series_id]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.timeSeriesIds
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_time_series_ids]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.variance
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_fitting_metrics_variance]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.d
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_non_seasonal_order_d]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.p
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_non_seasonal_order_p]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.q
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_arima_forecasting_single_model_non_seasonal_order_q]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.accuracy
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_accuracy]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.f1Score
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_f_1_score]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.logLoss
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_log_loss]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.precision
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_precision]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.recall
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_recall]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.rocAuc
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_roc_auc]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.threshold
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_aggregate_classification_metrics_threshold]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.accuracy
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_accuracy]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.f1Score
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_f_1_score]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.falseNegatives
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_false_negatives]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.falsePositives
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_false_positives]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.positiveClassThreshold
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_positive_class_threshold]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.precision
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_precision]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.recall
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_recall]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.trueNegatives
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_true_negatives]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.truePositives
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_confusion_matrix_list_true_positives]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.negativeLabel
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_negative_label]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.binaryClassificationMetrics.positiveLabel
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_binary_classification_positive_label]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.clusters.centroidId
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_clusters_centroid_id]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.clusters.count
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_clusters_count]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.clusters.featureValues.categoricalValue.categoryCounts.category
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_feature_values_categorical_value_counts_category]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.clusters.featureValues.categoricalValue.categoryCounts.count
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_feature_values_categorical_value_counts_count]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.clusters.featureValues.featureColumn
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_feature_values_feature_column]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.clusters.featureValues.numericalValue
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_feature_values_numerical_value]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.daviesBouldinIndex
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_davies_bouldin_index]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.clusteringMetrics.meanSquaredDistance
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_clustering_metrics_mean_squared_distance]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.dimensionalityReductionMetrics.totalExplainedVarianceRatio
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_dimensionality_reduction_metrics_total_explained_variance_ratio]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.accuracy
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_accuracy]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.f1Score
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_f_1_score]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.logLoss
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_log_loss]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.precision
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_precision]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.recall
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_recall]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.rocAuc
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_roc_auc]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.threshold
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_aggregate_classification_metrics_threshold]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.confidenceThreshold
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_confusion_matrix_list_confidence_threshold]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.actualLabel
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_confusion_matrix_list_rows_actual_label]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.entries.itemCount
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_confusion_matrix_list_rows_entries_item_count]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.entries.predictedLabel
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_multiclass_classification_confusion_matrix_list_rows_entries_predicted_label]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.rankingMetrics.averageRank
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_ranking_metrics_average_rank]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.rankingMetrics.meanAveragePrecision
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_ranking_metrics_mean_average_precision]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.rankingMetrics.meanSquaredError
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_ranking_metrics_mean_squared_error]
resource.data.hparamTrials.hparamTuningEvaluationMetrics.rankingMetrics.normalizedDiscountedCumulativeGain
entity.resource.attribute.labels[hparam_trials_tuning_evaluation_ranking_metrics_normalized_discounted_cumulative_gain]
resource.data.hparamTrials.hparams.activationFn
entity.resource.attribute.labels[hparam_trials_hparams_activation_fn]
resource.data.hparamTrials.hparams.adjustStepChanges
entity.resource.attribute.labels[hparam_trials_hparams_adjust_step_changes]
resource.data.hparamTrials.hparams.approxGlobalFeatureContrib
entity.resource.attribute.labels[hparam_trials_hparams_approx_global_feature_contrib]
resource.data.hparamTrials.hparams.autoArimaMaxOrder
entity.resource.attribute.labels[hparam_trials_hparams_auto_arima_max_order]
resource.data.hparamTrials.hparams.autoArimaMinOrder
entity.resource.attribute.labels[hparam_trials_hparams_auto_arima_min_order]
resource.data.hparamTrials.hparams.autoArima
entity.resource.attribute.labels[hparam_trials_hparams_auto_arima]
resource.data.hparamTrials.hparams.autoClassWeights
entity.resource.attribute.labels[hparam_trials_hparams_auto_class_weights]
resource.data.hparamTrials.hparams.batchSize
entity.resource.attribute.labels[hparam_trials_hparams_batch_size]
resource.data.hparamTrials.hparams.boosterType
entity.resource.attribute.labels[hparam_trials_hparams_booster_type]
resource.data.hparamTrials.hparams.budgetHours
entity.resource.attribute.labels[hparam_trials_hparams_budget_hours]
resource.data.hparamTrials.hparams.calculatePValues
entity.resource.attribute.labels[hparam_trials_hparams_calculate_p_values]
resource.data.hparamTrials.hparams.categoryEncodingMethod
entity.resource.attribute.labels[hparam_trials_hparams_category_encoding_method]
resource.data.hparamTrials.hparams.cleanSpikesAndDips
entity.resource.attribute.labels[hparam_trials_hparams_clean_spikes_and_dips]
resource.data.hparamTrials.hparams.colsampleBylevel
entity.resource.attribute.labels[hparam_trials_hparams_colsample_bylevel]
resource.data.hparamTrials.hparams.colsampleBynode
entity.resource.attribute.labels[hparam_trials_hparams_colsample_bynode]
resource.data.hparamTrials.hparams.colsampleBytree
entity.resource.attribute.labels[hparam_trials_hparams_colsample_bytree]
resource.data.hparamTrials.hparams.dartNormalizeType
entity.resource.attribute.labels[hparam_trials_hparams_dart_normalize_type]
resource.data.hparamTrials.hparams.dataFrequency
entity.resource.attribute.labels[hparam_trials_hparams_data_frequency]
resource.data.hparamTrials.hparams.dataSplitColumn
entity.resource.attribute.labels[hparam_trials_hparams_data_split_column]
resource.data.hparamTrials.hparams.dataSplitEvalFraction
entity.resource.attribute.labels[hparam_trials_hparams_data_split_eval_fraction]
resource.data.hparamTrials.hparams.dataSplitMethod
entity.resource.attribute.labels[hparam_trials_hparams_data_split_method]
resource.data.hparamTrials.hparams.decomposeTimeSeries
entity.resource.attribute.labels[hparam_trials_hparams_decompose_time_series]
resource.data.hparamTrials.hparams.distanceType
entity.resource.attribute.labels[hparam_trials_hparams_distance_type]
resource.data.hparamTrials.hparams.dropout
entity.resource.attribute.labels[hparam_trials_hparams_dropout]
resource.data.hparamTrials.hparams.earlyStop
entity.resource.attribute.labels[hparam_trials_hparams_early_stop]
resource.data.hparamTrials.hparams.enableGlobalExplain
entity.resource.attribute.labels[hparam_trials_hparams_enable_global_explain]
resource.data.hparamTrials.hparams.feedbackType
entity.resource.attribute.labels[hparam_trials_hparams_feedback_type]
resource.data.hparamTrials.hparams.fitIntercept
entity.resource.attribute.labels[hparam_trials_hparams_fit_intercept]
resource.data.hparamTrials.hparams.hiddenUnits
entity.resource.attribute.labels[hparam_trials_hparams_hidden_units]
resource.data.hparamTrials.hparams.holidayRegion
entity.resource.attribute.labels[hparam_trials_hparams_holiday_region]
resource.data.hparamTrials.hparams.holidayRegions
entity.resource.attribute.labels[hparam_trials_hparams_holiday_regions]
resource.data.hparamTrials.hparams.horizon
entity.resource.attribute.labels[hparam_trials_hparams_horizon]
resource.data.hparamTrials.hparams.hparamTuningObjectives
entity.resource.attribute.labels[hparam_trials_hparams_hparam_tuning_objectives]
resource.data.hparamTrials.hparams.includeDrift
entity.resource.attribute.labels[hparam_trials_hparams_include_drift]
resource.data.hparamTrials.hparams.initialLearnRate
entity.resource.attribute.labels[hparam_trials_hparams_initial_learn_rate]
resource.data.hparamTrials.hparams.inputLabelColumns
entity.resource.attribute.labels[hparam_trials_hparams_input_label_columns]
resource.data.hparamTrials.hparams.instanceWeightColumn
entity.resource.attribute.labels[hparam_trials_hparams_instance_weight_column]
resource.data.hparamTrials.hparams.integratedGradientsNumSteps
entity.resource.attribute.labels[hparam_trials_hparams_integrated_gradients_num_steps]
resource.data.hparamTrials.hparams.itemColumn
entity.resource.attribute.labels[hparam_trials_hparams_item_column]
resource.data.hparamTrials.hparams.kmeansInitializationColumn
entity.resource.attribute.labels[hparam_trials_hparams_kmeans_initialization_column]
resource.data.hparamTrials.hparams.kmeansInitializationMethod
entity.resource.attribute.labels[hparam_trials_hparams_kmeans_initialization_method]
resource.data.hparamTrials.hparams.l1RegActivation
entity.resource.attribute.labels[hparam_trials_hparams_l_1_reg_activation]
resource.data.hparamTrials.hparams.l1Regularization
entity.resource.attribute.labels[hparam_trials_hparams_l_1_regularization]
resource.data.hparamTrials.hparams.l2Regularization
entity.resource.attribute.labels[hparam_trials_hparams_l_2_regularization]
resource.data.hparamTrials.hparams.learnRateStrategy
entity.resource.attribute.labels[hparam_trials_hparams_learn_rate_strategy]
resource.data.hparamTrials.hparams.learnRate
entity.resource.attribute.labels[hparam_trials_hparams_learn_rate]
resource.data.hparamTrials.hparams.lossType
entity.resource.attribute.labels[hparam_trials_hparams_loss_type]
resource.data.hparamTrials.hparams.maxIterations
entity.resource.attribute.labels[hparam_trials_hparams_max_iterations]
resource.data.hparamTrials.hparams.maxParallelTrials
entity.resource.attribute.labels[hparam_trials_hparams_max_parallel_trials]
resource.data.hparamTrials.hparams.maxTimeSeriesLength
entity.resource.attribute.labels[hparam_trials_hparams_max_time_series_length]
resource.data.hparamTrials.hparams.maxTreeDepth
entity.resource.attribute.labels[hparam_trials_hparams_max_tree_depth]
resource.data.hparamTrials.hparams.minRelativeProgress
entity.resource.attribute.labels[hparam_trials_hparams_min_relative_progress]
resource.data.hparamTrials.hparams.minSplitLoss
entity.resource.attribute.labels[hparam_trials_hparams_min_split_loss]
resource.data.hparamTrials.hparams.minTimeSeriesLength
entity.resource.attribute.labels[hparam_trials_hparams_min_time_series_length]
resource.data.hparamTrials.hparams.minTreeChildWeight
entity.resource.attribute.labels[hparam_trials_hparams_min_tree_child_weight]
resource.data.hparamTrials.hparams.modelRegistry
entity.resource.attribute.labels[hparam_trials_hparams_model_registry]
resource.data.hparamTrials.hparams.modelUri
entity.resource.attribute.labels[hparam_trials_hparams_model_uri]
resource.data.hparamTrials.hparams.nonSeasonalOrder.d
entity.resource.attribute.labels[hparam_trials_hparams_non_seasonal_order_d]
resource.data.hparamTrials.hparams.nonSeasonalOrder.p
entity.resource.attribute.labels[hparam_trials_hparams_non_seasonal_order_p]
resource.data.hparamTrials.hparams.nonSeasonalOrder.q
entity.resource.attribute.labels[hparam_trials_hparams_non_seasonal_order_q]
resource.data.hparamTrials.hparams.numClusters
entity.resource.attribute.labels[hparam_trials_hparams_num_clusters]
resource.data.hparamTrials.hparams.numFactors
entity.resource.attribute.labels[hparam_trials_hparams_num_factors]
resource.data.hparamTrials.hparams.numParallelTree
entity.resource.attribute.labels[hparam_trials_hparams_num_parallel_tree]
resource.data.hparamTrials.hparams.numPrincipalComponents
entity.resource.attribute.labels[hparam_trials_hparams_num_principal_components]
resource.data.hparamTrials.hparams.numTrials
entity.resource.attribute.labels[hparam_trials_hparams_num_trials]
resource.data.hparamTrials.hparams.optimizationStrategy
entity.resource.attribute.labels[hparam_trials_hparams_optimization_strategy]
resource.data.hparamTrials.hparams.optimizer
entity.resource.attribute.labels[hparam_trials_hparams_optimizer]
resource.data.hparamTrials.hparams.pcaExplainedVarianceRatio
entity.resource.attribute.labels[hparam_trials_hparams_pca_explained_variance_ratio]
resource.data.hparamTrials.hparams.pcaSolver
entity.resource.attribute.labels[hparam_trials_hparams_pca_solver]
resource.data.hparamTrials.hparams.sampledShapleyNumPaths
entity.resource.attribute.labels[hparam_trials_hparams_sampled_shapley_num_paths]
resource.data.hparamTrials.hparams.scaleFeatures
entity.resource.attribute.labels[hparam_trials_hparams_scale_features]
resource.data.hparamTrials.hparams.standardizeFeatures
entity.resource.attribute.labels[hparam_trials_hparams_standardize_features]
resource.data.hparamTrials.hparams.subsample
entity.resource.attribute.labels[hparam_trials_hparams_subsample]
resource.data.hparamTrials.hparams.tfVersion
entity.resource.attribute.labels[hparam_trials_hparams_tf_version]
resource.data.hparamTrials.hparams.timeSeriesDataColumn
entity.resource.attribute.labels[hparam_trials_hparams_time_series_data_column]
resource.data.hparamTrials.hparams.timeSeriesIdColumn
entity.resource.attribute.labels[hparam_trials_hparams_time_series_id_column]
resource.data.hparamTrials.hparams.timeSeriesIdColumns
entity.resource.attribute.labels[hparam_trials_hparams_time_series_id_columns]
resource.data.hparamTrials.hparams.timeSeriesLengthFraction
entity.resource.attribute.labels[hparam_trials_hparams_time_series_length_fraction]
resource.data.hparamTrials.hparams.timeSeriesTimestampColumn
entity.resource.attribute.labels[hparam_trials_hparams_time_series_timestamp_column]
resource.data.hparamTrials.hparams.treeMethod
entity.resource.attribute.labels[hparam_trials_hparams_tree_method]
resource.data.hparamTrials.hparams.trendSmoothingWindowSize
entity.resource.attribute.labels[hparam_trials_hparams_trend_smoothing_window_size]
resource.data.hparamTrials.hparams.userColumn
entity.resource.attribute.labels[hparam_trials_hparams_user_column]
resource.data.hparamTrials.hparams.vertexAiModelVersionAliases
entity.resource.attribute.labels[hparam_trials_hparams_vertex_ai_model_version_aliases]
resource.data.hparamTrials.hparams.walsAlpha
entity.resource.attribute.labels[hparam_trials_hparams_wals_alpha]
resource.data.hparamTrials.hparams.warmStart
entity.resource.attribute.labels[hparam_trials_hparams_warm_start]
resource.data.hparamTrials.hparams.xgboostVersion
entity.resource.attribute.labels[hparam_trials_hparams_xgboost_version]
resource.data.hparamTrials.startTimeMs
entity.resource.attribute.labels[hparam_trials_start_time_ms]
resource.data.hparamTrials.status
entity.resource.attribute.labels[hparam_trials_status]
resource.data.hparamTrials.trainingLoss
entity.resource.attribute.labels[hparam_trials_training_loss]
resource.data.hparamTrials.trialId
entity.resource.attribute.labels[hparam_trials_trial_id]
resource.data.isCaseInsensitive
entity.resource.attribute.labels[is_case_insensitive]
resource.data.kind
entity.resource.attribute.labels[kind]
resource.data.labelColumns.name
entity.resource.attribute.labels[label_columns_name]
resource.data.labelColumns.type.typeKind
entity.resource.attribute.labels[label_columns_type_type_kind]
resource.data.materializedView.enableRefresh
entity.resource.attribute.labels[materialized_view_enable_refresh]
resource.data.materializedView.lastRefreshTime
entity.resource.attribute.labels[materialized_view_last_refresh_time]
resource.data.materializedView.query
entity.resource.attribute.labels[materialized_view_query]
resource.data.materializedView.refreshIntervalMs
entity.resource.attribute.labels[materialized_view_refresh_interval_ms]
resource.data.materializedViewStatus.lastRefreshStatus.debugInfo
entity.resource.attribute.labels[materialized_view_status_last_refresh_status_debug_info]
resource.data.materializedViewStatus.lastRefreshStatus.location
entity.resource.attribute.labels[materialized_view_status_last_refresh_status_location]
resource.data.materializedViewStatus.lastRefreshStatus.message
entity.resource.attribute.labels[materialized_view_status_last_refresh_status_message]
resource.data.materializedViewStatus.lastRefreshStatus.reason
entity.resource.attribute.labels[materialized_view_status_last_refresh_status_reason]
resource.data.materializedViewStatus.refreshWatermark
entity.resource.attribute.labels[materialized_view_status_refresh_watermark]
resource.data.maxStaleness
entity.resource.attribute.labels[max_staleness]
resource.data.maxTimeTravelHours
entity.resource.attribute.labels[max_time_travel_hours]
resource.data.modelReference.modelId
entity.resource.attribute.labels[model_reference_modelid]
resource.data.modelType
entity.resource.attribute.labels[model_type]
resource.data.numBytes
entity.resource.attribute.labels[num_Bytes]
resource.data.numLongTermBytes
entity.resource.attribute.labels[num_long_term_bytes]
resource.data.numRows
entity.resource.attribute.labels[num_rows]
resource.data.optimalTrialIds
entity.resource.attribute.labels[optimal_trial_id]
resource.data.requirePartitionFilter
entity.resource.attribute.labels[require_partition_filter]
resource.data.satisfiesPzs
entity.resource.attribute.labels[satisfies_pzs]
resource.data.selfLink
entity.resource.attribute.labels[self_link]
resource.data.storageBillingModel
entity.resource.attribute.labels[storage_billing_model]
resource.data.streamingBuffer.estimatedBytes
entity.resource.attribute.labels[streaming_buffer_estimated_bytes]
resource.data.streamingBuffer.estimatedRows
entity.resource.attribute.labels[streaming_buffer_estimated_rows]
resource.data.streamingBuffer.oldestEntryTime
entity.resource.attribute.labels[streaming_buffer_oldest_entry_time]
resource.data.tableConstraints.foreignKeys.columnReferences.referencedColumn
entity.resource.attribute.labels[table_constraints_foreign_keys_column_references_referenced_column]
resource.data.tableConstraints.foreignKeys.columnReferences.referencingColumn
entity.resource.attribute.labels[table_constraints_foreign_keys_column_references_referencing_column]
resource.data.tableConstraints.foreignKeys.name
entity.resource.attribute.labels[table_constraints_foreign_keys_name]
resource.data.tableConstraints.foreignKeys.referencedTable.datasetId
entity.resource.attribute.labels[table_constraints_foreign_keys_referenced_table_dataset_id]
resource.data.tableConstraints.foreignKeys.referencedTable.projectId
entity.resource.attribute.labels[table_constraints_foreign_keys_referenced_table_project_id]
resource.data.tableConstraints.foreignKeys.referencedTable.tableId
entity.resource.attribute.labels[table_constraints_foreign_keys_referenced_table_table_id]
resource.data.tableConstraints.primaryKey.columns
entity.resource.attribute.labels[table_constraints_primary_key_columns]
resource.data.schema.fields.collation
entity.resource.attribute.labels[table_field_collation]
resource.data.schema.fields.defaultValueExpression
entity.resource.attribute.labels[table_field_default_value_expression]
resource.data.schema.fields.description
entity.resource.attribute.labels[table_field_description]
resource.data.schema.fields.maxLength
entity.resource.attribute.labels[table_field_max_length]
resource.data.schema.fields.mode
entity.resource.attribute.labels[table_field_mode]
resource.data.schema.fields.name
entity.resource.attribute.labels[table_field_name]
resource.data.schema.fields.policyTags.names[]
entity.resource.attribute.labels[table_field_policy_tags_names]
resource.data.schema.fields.precision
entity.resource.attribute.labels[table_field_precision]
resource.data.schema.fields.roundingMode
entity.resource.attribute.labels[table_field_rounding_mode]
resource.data.schema.fields.scale
entity.resource.attribute.labels[table_field_scale]
resource.data.schema.fields.type
entity.resource.attribute.labels[table_field_type]
resource.data.rangePartitioning.field
entity.resource.attribute.labels[table_range_partitioning_field]
resource.data.rangePartitioning.range.end
entity.resource.attribute.labels[table_range_partitioning_range_end]
resource.data.rangePartitioning.range.interval
entity.resource.attribute.labels[table_range_partitioning_range_interval]
resource.data.rangePartitioning.range.start
entity.resource.attribute.labels[table_range_partitioning_range_start]
resource.data.tableReference.tableId
entity.resource.attribute.labels[table_reference_table_id]
resource.data.timePartitioning.expirationMs
entity.resource.attribute.labels[table_time_partitioning_expiration_ms]
resource.data.timePartitioning.field
entity.resource.attribute.labels[table_time_partitioning_field]
resource.data.timePartitioning.requirePartitionFilter
entity.resource.attribute.labels[table_time_partitioning_require_partition_filter]
resource.data.timePartitioning.type
entity.resource.attribute.labels[table_time_partitioning_type]
resource.data.tags
entity.resource.attribute.labels[tags]
resource.data.trainingRuns.classLevelGlobalExplanations.classLabel
entity.resource.attribute.labels[trainingruns_class_level_global_explanations_class_label]
resource.data.trainingRuns.classLevelGlobalExplanations.explanations.attribution
entity.resource.attribute.labels[trainingruns_class_level_global_explanations_explanations_attribution]
resource.data.trainingRuns.classLevelGlobalExplanations.explanations.featureName
entity.resource.attribute.labels[trainingruns_class_level_global_explanations_explanations_feature_name]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.aic
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_fitting_metrics_aic]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasDrift
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_has_drift]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasHolidayEffect
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_has_holiday_effect]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasSpikesAndDips
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_has_spikes_and_dips]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.hasStepChanges
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_has_step_changes]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.logLikelihood
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_fitting_metrics_log_likelihood]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.seasonalPeriods
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_fitting_metrics_seasonal_periods]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.timeSeriesId
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_time_series_id]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.timeSeriesIds
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_time_series_ids]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.arimaFittingMetrics.variance
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_fitting_metrics_variance]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.d
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_non_seasonal_order_d]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.p
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_non_seasonal_order_p]
resource.data.trainingRuns.evaluationMetrics.arimaForecastingMetrics.arimaSingleModelForecastingMetrics.nonSeasonalOrder.q
entity.resource.attribute.labels[trainingruns_evaluation_arima_forecasting_single_model_non_seasonal_order_q]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.accuracy
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_accuracy]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.f1Score
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_f_1_score]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.logLoss
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_log_loss]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.precision
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_precision]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.recall
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_recall]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.rocAuc
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_roc_auc]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.aggregateClassificationMetrics.threshold
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_aggregate_classification_metrics_threshold]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.accuracy
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_accuracy]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.f1Score
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_f_1_score]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.falseNegatives
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_false_negatives]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.falsePositives
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_false_positives]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.positiveClassThreshold
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_positive_class_threshold]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.precision
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_precision]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.recall
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_recall]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.trueNegatives
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_true_negatives]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.binaryConfusionMatrixList.truePositives
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_confusion_matrix_list_true_positives]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.negativeLabel
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_negative_label]
resource.data.trainingRuns.evaluationMetrics.binaryClassificationMetrics.positiveLabel
entity.resource.attribute.labels[trainingruns_evaluation_binary_classification_positive_label]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.clusters.centroidId
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_clusters_centroid_id]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.clusters.count
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_clusters_count]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.clusters.featureValues.categoricalValue.categoryCounts.category
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_feature_values_categorical_value_counts_category]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.clusters.featureValues.categoricalValue.categoryCounts.count
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_feature_values_categorical_value_counts_count]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.clusters.featureValues.featureColumn
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_feature_values_feature_column]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.clusters.featureValues.numericalValue
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_feature_values_numerical_value]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.daviesBouldinIndex
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_davies_bouldin_index]
resource.data.trainingRuns.evaluationMetrics.clusteringMetrics.meanSquaredDistance
entity.resource.attribute.labels[trainingruns_evaluation_clustering_metrics_mean_squared_distance]
resource.data.trainingRuns.evaluationMetrics.dimensionalityReductionMetrics.totalExplainedVarianceRatio
entity.resource.attribute.labels[trainingruns_evaluation_dimensionality_reduction_metrics_total_explained_variance_ratio]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.accuracy
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_accuracy]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.f1Score
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_f_1_score]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.logLoss
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_log_loss]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.precision
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_precision]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.recall
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_recall]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.rocAuc
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_roc_auc]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.aggregateClassificationMetrics.threshold
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_aggregate_classification_metrics_threshold]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.confidenceThreshold
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_confusion_matrix_list_confidence_threshold]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.actualLabel
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_confusion_matrix_list_rows_actual_label]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.entries.itemCount
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_confusion_matrix_list_rows_entries_item_count]
resource.data.trainingRuns.evaluationMetrics.multiClassClassificationMetrics.confusionMatrixList.rows.entries.predictedLabel
entity.resource.attribute.labels[trainingruns_evaluation_multiclass_classification_confusion_matrix_list_rows_entries_predicted_label]
resource.data.trainingRuns.evaluationMetrics.rankingMetrics.averageRank
entity.resource.attribute.labels[trainingruns_evaluation_ranking_metrics_average_rank]
resource.data.trainingRuns.evaluationMetrics.rankingMetrics.meanAveragePrecision
entity.resource.attribute.labels[trainingruns_evaluation_ranking_metrics_mean_average_precision]
resource.data.trainingRuns.evaluationMetrics.rankingMetrics.meanSquaredError
entity.resource.attribute.labels[trainingruns_evaluation_ranking_metrics_mean_squared_error]
resource.data.trainingRuns.evaluationMetrics.rankingMetrics.normalizedDiscountedCumulativeGain
entity.resource.attribute.labels[trainingruns_evaluation_ranking_metrics_normalized_discounted_cumulative_gain]
resource.data.trainingRuns.modelLevelGlobalExplanation.classLabel
entity.resource.attribute.labels[trainingruns_model_level_global_explanation_class_label]
resource.data.trainingRuns.modelLevelGlobalExplanation.explanations.attribution
entity.resource.attribute.labels[trainingruns_model_level_global_explanation_explanations_attribution]
resource.data.trainingRuns.modelLevelGlobalExplanation.explanations.featureName
entity.resource.attribute.labels[trainingruns_model_level_global_explanation_explanations_feature_name]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.arimaCoefficients.autoRegressiveCoefficients
entity.resource.attribute.labels[trainingruns_results_arima_model_info_auto_regressive]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.arimaCoefficients.interceptCoefficient
entity.resource.attribute.labels[trainingruns_results_arima_model_info_intercept_coefficient]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.arimaCoefficients.movingAverageCoefficients
entity.resource.attribute.labels[trainingruns_results_arima_model_info_moving_average]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.arimaFittingMetrics.aic
entity.resource.attribute.labels[trainingruns_results_arima_model_info_fitting_metrics_aic]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.arimaFittingMetrics.logLikelihood
entity.resource.attribute.labels[trainingruns_results_arima_model_info_fitting_metrics_log_likelihood]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.arimaFittingMetrics.variance
entity.resource.attribute.labels[trainingruns_results_arima_model_info_fitting_metrics_variance]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.hasDrift
entity.resource.attribute.labels[trainingruns_results_arima_model_info_has_drift]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.hasHolidayEffect
entity.resource.attribute.labels[trainingruns_results_arima_model_info_has_holiday_effect]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.hasSpikesAndDips
entity.resource.attribute.labels[trainingruns_results_arima_model_info_has_spikes_and_dips]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.hasStepChanges
entity.resource.attribute.labels[trainingruns_results_arima_model_info_has_step_changes]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.nonSeasonalOrder.d
entity.resource.attribute.labels[trainingruns_results_arima_model_info_non_seasonal_order_d]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.nonSeasonalOrder.p
entity.resource.attribute.labels[trainingruns_results_arima_model_info_non_seasonal_order_p]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.nonSeasonalOrder.q
entity.resource.attribute.labels[trainingruns_results_arima_model_info_non_seasonal_order_q]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.seasonalPeriods
entity.resource.attribute.labels[trainingruns_results_arima_model_info_seasonal_periods]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.timeSeriesId
entity.resource.attribute.labels[trainingruns_results_arima_model_info_time_series_id]
resource.data.trainingRuns.results.arimaResult.arimaModelInfo.timeSeriesIds
entity.resource.attribute.labels[trainingruns_results_arima_model_info_time_series_ids]
resource.data.trainingRuns.results.arimaResult.seasonalPeriods
entity.resource.attribute.labels[trainingruns_results_arima_result_seasonal_periods]
resource.data.trainingRuns.results.clusterInfos.centroidId
entity.resource.attribute.labels[trainingruns_results_cluster_infos_centroid_id]
resource.data.trainingRuns.results.clusterInfos.clusterRadius
entity.resource.attribute.labels[trainingruns_results_cluster_infos_cluster_radius]
resource.data.trainingRuns.results.clusterInfos.clusterSize
entity.resource.attribute.labels[trainingruns_results_cluster_infos_cluster_size]
resource.data.trainingRuns.results.durationMs
entity.resource.attribute.labels[trainingruns_results_duration_ms]
resource.data.trainingRuns.results.evalLoss
entity.resource.attribute.labels[trainingruns_results_eval_loss]
resource.data.trainingRuns.results.index
entity.resource.attribute.labels[trainingruns_results_index]
resource.data.trainingRuns.results.learnRate
entity.resource.attribute.labels[trainingruns_results_learn_rate]
resource.data.trainingRuns.results.principalComponentInfos.cumulativeExplainedVarianceRatio
entity.resource.attribute.labels[trainingruns_results_principal_component_infos_cumulative_explained_variance_ratio]
resource.data.trainingRuns.results.principalComponentInfos.explainedVarianceRatio
entity.resource.attribute.labels[trainingruns_results_principal_component_infos_explained_variance_ratio]
resource.data.trainingRuns.results.principalComponentInfos.explainedVariance
entity.resource.attribute.labels[trainingruns_results_principal_component_infos_explained_variance]
resource.data.trainingRuns.results.principalComponentInfos.principalComponentId
entity.resource.attribute.labels[trainingruns_results_principal_component_infos_principal_component_id]
resource.data.trainingRuns.results.trainingLoss
entity.resource.attribute.labels[trainingruns_results_training_loss]
resource.data.trainingRuns.startTime
entity.resource.attribute.labels[trainingruns_start_time]
resource.data.trainingRuns.trainingOptions.activationFn
entity.resource.attribute.labels[trainingruns_training_options_activation_fn]
resource.data.trainingRuns.trainingOptions.adjustStepChanges
entity.resource.attribute.labels[trainingruns_training_options_adjust_step_changes]
resource.data.trainingRuns.trainingOptions.approxGlobalFeatureContrib
entity.resource.attribute.labels[trainingruns_training_options_approx_global_feature_contrib]
resource.data.trainingRuns.trainingOptions.autoArimaMaxOrder
entity.resource.attribute.labels[trainingruns_training_options_auto_arima_max_order]
resource.data.trainingRuns.trainingOptions.autoArimaMinOrder
entity.resource.attribute.labels[trainingruns_training_options_auto_arima_min_order]
resource.data.trainingRuns.trainingOptions.autoArima
entity.resource.attribute.labels[trainingruns_training_options_auto_arima]
resource.data.trainingRuns.trainingOptions.autoClassWeights
entity.resource.attribute.labels[trainingruns_training_options_auto_class_weights]
resource.data.trainingRuns.trainingOptions.batchSize
entity.resource.attribute.labels[trainingruns_training_options_batch_size]
resource.data.trainingRuns.trainingOptions.boosterType
entity.resource.attribute.labels[trainingruns_training_options_booster_type]
resource.data.trainingRuns.trainingOptions.budgetHours
entity.resource.attribute.labels[trainingruns_training_options_budget_hours]
resource.data.trainingRuns.trainingOptions.calculatePValues
entity.resource.attribute.labels[trainingruns_training_options_calculate_p_values]
resource.data.trainingRuns.trainingOptions.categoryEncodingMethod
entity.resource.attribute.labels[trainingruns_training_options_category_encoding_method]
resource.data.trainingRuns.trainingOptions.cleanSpikesAndDips
entity.resource.attribute.labels[trainingruns_training_options_clean_spikes_and_dips]
resource.data.trainingRuns.trainingOptions.colsampleBylevel
entity.resource.attribute.labels[trainingruns_training_options_colsample_bylevel]
resource.data.trainingRuns.trainingOptions.colsampleBynode
entity.resource.attribute.labels[trainingruns_training_options_colsample_bynode]
resource.data.trainingRuns.trainingOptions.colsampleBytree
entity.resource.attribute.labels[trainingruns_training_options_colsample_bytree]
resource.data.trainingRuns.trainingOptions.dartNormalizeType
entity.resource.attribute.labels[trainingruns_training_options_dart_normalize_type]
resource.data.trainingRuns.trainingOptions.dataFrequency
entity.resource.attribute.labels[trainingruns_training_options_data_frequency]
resource.data.trainingRuns.trainingOptions.dataSplitColumn
entity.resource.attribute.labels[trainingruns_training_options_data_split_column]
resource.data.trainingRuns.trainingOptions.dataSplitEvalFraction
entity.resource.attribute.labels[trainingruns_training_options_data_split_eval_fraction]
resource.data.trainingRuns.trainingOptions.dataSplitMethod
entity.resource.attribute.labels[trainingruns_training_options_data_split_method]
resource.data.trainingRuns.trainingOptions.decomposeTimeSeries
entity.resource.attribute.labels[trainingruns_training_options_decompose_time_series]
resource.data.trainingRuns.trainingOptions.distanceType
entity.resource.attribute.labels[trainingruns_training_options_distance_type]
resource.data.trainingRuns.trainingOptions.dropout
entity.resource.attribute.labels[trainingruns_training_options_dropout]
resource.data.trainingRuns.trainingOptions.earlyStop
entity.resource.attribute.labels[trainingruns_training_options_early_stop]
resource.data.trainingRuns.trainingOptions.enableGlobalExplain
entity.resource.attribute.labels[trainingruns_training_options_enable_global_explain]
resource.data.trainingRuns.trainingOptions.feedbackType
entity.resource.attribute.labels[trainingruns_training_options_feedback_type]
resource.data.trainingRuns.trainingOptions.fitIntercept
entity.resource.attribute.labels[trainingruns_training_options_fit_intercept]
resource.data.trainingRuns.trainingOptions.hiddenUnits
entity.resource.attribute.labels[trainingruns_training_options_hidden_units]
resource.data.trainingRuns.trainingOptions.holidayRegion
entity.resource.attribute.labels[trainingruns_training_options_holiday_region]
resource.data.trainingRuns.trainingOptions.holidayRegions
entity.resource.attribute.labels[trainingruns_training_options_holiday_regions]
resource.data.trainingRuns.trainingOptions.horizon
entity.resource.attribute.labels[trainingruns_training_options_horizon]
resource.data.trainingRuns.trainingOptions.hparamTuningObjectives
entity.resource.attribute.labels[trainingruns_training_options_hparam_tuning_objectives]
resource.data.trainingRuns.trainingOptions.includeDrift
entity.resource.attribute.labels[trainingruns_training_options_include_drift]
resource.data.trainingRuns.trainingOptions.initialLearnRate
entity.resource.attribute.labels[trainingruns_training_options_initial_learn_rate]
resource.data.trainingRuns.trainingOptions.inputLabelColumns
entity.resource.attribute.labels[trainingruns_training_options_input_label_columns]
resource.data.trainingRuns.trainingOptions.instanceWeightColumn
entity.resource.attribute.labels[trainingruns_training_options_instance_weight_column]
resource.data.trainingRuns.trainingOptions.integratedGradientsNumSteps
entity.resource.attribute.labels[trainingruns_training_options_integrated_gradients_num_steps]
resource.data.trainingRuns.trainingOptions.itemColumn
entity.resource.attribute.labels[trainingruns_training_options_item_column]
resource.data.trainingRuns.trainingOptions.kmeansInitializationColumn
entity.resource.attribute.labels[trainingruns_training_options_kmeans_initialization_column]
resource.data.trainingRuns.trainingOptions.kmeansInitializationMethod
entity.resource.attribute.labels[trainingruns_training_options_kmeans_initialization_method]
resource.data.trainingRuns.trainingOptions.l1RegActivation
entity.resource.attribute.labels[trainingruns_training_options_l_1_reg_activation]
resource.data.trainingRuns.trainingOptions.l1Regularization
entity.resource.attribute.labels[trainingruns_training_options_l_1_regularization]
resource.data.trainingRuns.trainingOptions.l2Regularization
entity.resource.attribute.labels[trainingruns_training_options_l_2_regularization]
resource.data.trainingRuns.trainingOptions.learnRateStrategy
entity.resource.attribute.labels[trainingruns_training_options_learn_rate_strategy]
resource.data.trainingRuns.trainingOptions.learnRate
entity.resource.attribute.labels[trainingruns_training_options_learn_rate]
resource.data.trainingRuns.trainingOptions.maxIterations
entity.resource.attribute.labels[trainingruns_training_options_max_iterations]
resource.data.trainingRuns.trainingOptions.maxParallelTrials
entity.resource.attribute.labels[trainingruns_training_options_max_parallel_trials]
resource.data.trainingRuns.trainingOptions.maxTimeSeriesLength
entity.resource.attribute.labels[trainingruns_training_options_max_time_series_length]
resource.data.trainingRuns.trainingOptions.maxTreeDepth
entity.resource.attribute.labels[trainingruns_training_options_max_tree_depth]
resource.data.trainingRuns.trainingOptions.minRelativeProgress
entity.resource.attribute.labels[trainingruns_training_options_min_relative_progress]
resource.data.trainingRuns.trainingOptions.minTimeSeriesLength
entity.resource.attribute.labels[trainingruns_training_options_min_time_series_length]
resource.data.trainingRuns.trainingOptions.minTreeChildWeight
entity.resource.attribute.labels[trainingruns_training_options_min_tree_child_weight]
resource.data.trainingRuns.trainingOptions.modelRegistry
entity.resource.attribute.labels[trainingruns_training_options_model_registry]
resource.data.trainingRuns.trainingOptions.modelUri
entity.resource.attribute.labels[trainingruns_training_options_model_uri]
resource.data.trainingRuns.trainingOptions.nonSeasonalOrder.d
entity.resource.attribute.labels[trainingruns_training_options_non_seasonal_order_d]
resource.data.trainingRuns.trainingOptions.nonSeasonalOrder.p
entity.resource.attribute.labels[trainingruns_training_options_non_seasonal_order_p]
resource.data.trainingRuns.trainingOptions.nonSeasonalOrder.q
entity.resource.attribute.labels[trainingruns_training_options_non_seasonal_order_q]
resource.data.trainingRuns.trainingOptions.numClusters
entity.resource.attribute.labels[trainingruns_training_options_num_clusters]
resource.data.trainingRuns.trainingOptions.numFactors
entity.resource.attribute.labels[trainingruns_training_options_num_factors]
resource.data.trainingRuns.trainingOptions.numParallelTree
entity.resource.attribute.labels[trainingruns_training_options_num_parallel_tree]
resource.data.trainingRuns.trainingOptions.numPrincipalComponents
entity.resource.attribute.labels[trainingruns_training_options_num_principal_components]
resource.data.trainingRuns.trainingOptions.numTrials
entity.resource.attribute.labels[trainingruns_training_options_num_trials]
resource.data.trainingRuns.trainingOptions.optimizationStrategy
entity.resource.attribute.labels[trainingruns_training_options_optimization_strategy]
resource.data.trainingRuns.trainingOptions.optimizer
entity.resource.attribute.labels[trainingruns_training_options_optimizer]
resource.data.trainingRuns.trainingOptions.pcaExplainedVarianceRatio
entity.resource.attribute.labels[trainingruns_training_options_pca_explained_variance_ratio]
resource.data.trainingRuns.trainingOptions.pcaSolver
entity.resource.attribute.labels[trainingruns_training_options_pca_solver]
resource.data.trainingRuns.trainingOptions.sampledShapleyNumPaths
entity.resource.attribute.labels[trainingruns_training_options_sampled_shapley_num_paths]
resource.data.trainingRuns.trainingOptions.scaleFeatures
entity.resource.attribute.labels[trainingruns_training_options_scale_features]
resource.data.trainingRuns.trainingOptions.standardizeFeatures
entity.resource.attribute.labels[trainingruns_training_options_standardize_features]
resource.data.trainingRuns.trainingOptions.subsample
entity.resource.attribute.labels[trainingruns_training_options_subsample]
resource.data.trainingRuns.trainingOptions.tfVersion
entity.resource.attribute.labels[trainingruns_training_options_tf_version]
resource.data.trainingRuns.trainingOptions.timeSeriesDataColumn
entity.resource.attribute.labels[trainingruns_training_options_time_series_data_column]
resource.data.trainingRuns.trainingOptions.timeSeriesIdColumn
entity.resource.attribute.labels[trainingruns_training_options_time_series_id_column]
resource.data.trainingRuns.trainingOptions.timeSeriesIdColumns
entity.resource.attribute.labels[trainingruns_training_options_time_series_id_columns]
resource.data.trainingRuns.trainingOptions.timeSeriesLengthFraction
entity.resource.attribute.labels[trainingruns_training_options_time_series_length_fraction]
resource.data.trainingRuns.trainingOptions.timeSeriesTimestampColumn
entity.resource.attribute.labels[trainingruns_training_options_time_series_timestamp_column]
resource.data.trainingRuns.trainingOptions.treeMethod
entity.resource.attribute.labels[trainingruns_training_options_tree_method]
resource.data.trainingRuns.trainingOptions.trendSmoothingWindowSize
entity.resource.attribute.labels[trainingruns_training_options_trend_smoothing_window_size]
resource.data.trainingRuns.trainingOptions.userColumn
entity.resource.attribute.labels[trainingruns_training_options_user_column]
resource.data.trainingRuns.trainingOptions.vertexAiModelVersionAliases
entity.resource.attribute.labels[trainingruns_training_options_vertex_ai_model_version_aliases]
resource.data.trainingRuns.trainingOptions.walsAlpha
entity.resource.attribute.labels[trainingruns_training_options_wals_alpha]
resource.data.trainingRuns.trainingOptions.warmStart
entity.resource.attribute.labels[trainingruns_training_options_warm_start]
resource.data.trainingRuns.trainingOptions.xgboostVersion
entity.resource.attribute.labels[trainingruns_training_options_xgboost_version]
resource.data.trainingRuns.trainingStartTime
entity.resource.attribute.labels[trainingruns_training_start_time]
resource.data.trainingRuns.vertexAiModelId
entity.resource.attribute.labels[trainingruns_vertex_ai_model_id]
resource.data.trainingRuns.vertexAiModelVersion
entity.resource.attribute.labels[trainingruns_vertex_ai_model_version]
resource.data.transformColumns.name
entity.resource.attribute.labels[transform_columns_name]
resource.data.transformColumns.transformSql
entity.resource.attribute.labels[transform_columns_transform_sql]
resource.data.transformColumns.type.typeKind
entity.resource.attribute.labels[transform_columns_type_type_kind]
resource.data.type
entity.resource.attribute.labels[type]
resource.data.view.query
entity.resource.attribute.labels[view_query]
resource.data.view.useLegacySql
entity.resource.attribute.labels[view_use_legacy_sql]
resource.data.view.userDefinedFunctionResources.inlineCode
entity.resource.attribute.labels[view_user_defined_function_resources_inline_code]
resource.data.view.userDefinedFunctionResources.resourceUri
entity.resource.attribute.labels[view_user_defined_function_resources_resource_uri]
resource.data.externalDataConfiguration.autodetect
relations.entity.resource.attribute.labels[external_data_configuration_autodetect]
resource.data.externalDataConfiguration.avroOptions.useAvroLogicalTypes
relations.entity.resource.attribute.labels[external_data_configuration_avro_options_use_avro_logical_types]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.columns.encoding
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_columns_encoding]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.columns.fieldName
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_columns_field_name]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.columns.onlyReadLatest
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_columns_only_read_latest]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.columns.qualifierEncoded
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_columns_qualifier_encoded]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.columns.qualifierString
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_columns_qualifier_string]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.columns.type
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_columns_type]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.encoding
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_encoding]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.familyId
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_family_id]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.onlyReadLatest
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_only_read_latest]
resource.data.externalDataConfiguration.bigtableOptions.columnFamilies.type
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_column_families_type]
resource.data.externalDataConfiguration.bigtableOptions.ignoreUnspecifiedColumnFamilies
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_ignore_unspecified_column_families]
resource.data.externalDataConfiguration.bigtableOptions.readRowkeyAsString
relations.entity.resource.attribute.labels[external_data_configuration_bigtable_options_read_rowkey_as_string]
resource.data.externalDataConfiguration.compression
relations.entity.resource.attribute.labels[external_data_configuration_compression]
resource.data.externalDataConfiguration.csvOptions.allowJaggedRows
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_allow_jagged_rows]
resource.data.externalDataConfiguration.csvOptions.allowQuotedNewlines
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_allow_quoted_newlines]
resource.data.externalDataConfiguration.csvOptions.encoding
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_encoding]
resource.data.externalDataConfiguration.csvOptions.fieldDelimiter
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_field_delimiter]
resource.data.externalDataConfiguration.csvOptions.preserveAsciiControlCharacters
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_preserve_ascii_control_characters]
resource.data.externalDataConfiguration.csvOptions.quote
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_quote]
resource.data.externalDataConfiguration.csvOptions.skipLeadingRows
relations.entity.resource.attribute.labels[external_data_configuration_csv_options_skip_leading_rows]
resource.data.externalDataConfiguration.decimalTargetTypes
relations.entity.resource.attribute.labels[external_data_configuration_decimal_target_types]
resource.data.externalDataConfiguration.fileSetSpecType
relations.entity.resource.attribute.labels[external_data_configuration_file_set_spec_type]
resource.data.externalDataConfiguration.googleSheetsOptions.range
relations.entity.resource.attribute.labels[external_data_configuration_google_sheets_options_range]
resource.data.externalDataConfiguration.googleSheetsOptions.skipLeadingRows
relations.entity.resource.attribute.labels[external_data_configuration_google_sheets_options_skip_leading_rows]
resource.data.externalDataConfiguration.hivePartitioningOptions.fields
relations.entity.resource.attribute.labels[external_data_configuration_hive_partitioning_options_fields]
resource.data.externalDataConfiguration.hivePartitioningOptions.mode
relations.entity.resource.attribute.labels[external_data_configuration_hive_partitioning_options_mode]
resource.data.externalDataConfiguration.hivePartitioningOptions.requirePartitionFilter
relations.entity.resource.attribute.labels[external_data_configuration_hive_partitioning_options_require_partition_filter]
resource.data.externalDataConfiguration.hivePartitioningOptions.sourceUriPrefix
relations.entity.resource.attribute.labels[external_data_configuration_hive_partitioning_options_source_uri_prefix]
resource.data.externalDataConfiguration.ignoreUnknownValues
relations.entity.resource.attribute.labels[external_data_configuration_ignore_unknown_values]
resource.data.externalDataConfiguration.jsonOptions.encoding
relations.entity.resource.attribute.labels[external_data_configuration_json_options_encoding]
resource.data.externalDataConfiguration.maxBadRecords
relations.entity.resource.attribute.labels[external_data_configuration_max_bad_records]
resource.data.externalDataConfiguration.metadataCacheMode
relations.entity.resource.attribute.labels[external_data_configuration_metadata_cache_mode]
resource.data.externalDataConfiguration.objectMetadata
relations.entity.resource.attribute.labels[external_data_configuration_object_metadata]
resource.data.externalDataConfiguration.parquetOptions.enableListInference
relations.entity.resource.attribute.labels[external_data_configuration_parquet_options_enable_list_inference]
resource.data.externalDataConfiguration.parquetOptions.enumAsString
relations.entity.resource.attribute.labels[external_data_configuration_parquet_options_enum_as_string]
resource.data.externalDataConfiguration.referenceFileSchemaUri
relations.entity.resource.attribute.labels[external_data_configuration_reference_file_schema_uri]
resource.data.externalDataConfiguration.schema.fields.collation
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_collation]
resource.data.externalDataConfiguration.schema.fields.defaultValueExpression
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_default_value_expression]
resource.data.externalDataConfiguration.schema.fields.description
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_description]
resource.data.externalDataConfiguration.schema.fields.maxLength
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_max_length]
resource.data.externalDataConfiguration.schema.fields.mode
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_mode]
resource.data.externalDataConfiguration.schema.fields.name
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_name]
resource.data.externalDataConfiguration.schema.fields.policyTags.names
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_policy_tags_names]
resource.data.externalDataConfiguration.schema.fields.precision
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_precision]
resource.data.externalDataConfiguration.schema.fields.roundingMode
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_rounding_mode]
resource.data.externalDataConfiguration.schema.fields.scale
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_scale]
resource.data.externalDataConfiguration.schema.fields.type
relations.entity.resource.attribute.labels[external_data_configuration_schema_fields_type]
resource.data.externalDataConfiguration.sourceUris
relations.entity.resource.attribute.labels[external_data_configuration_source_uris]
resource.data.remoteModelInfo.endpoint
relations.entity.resource.attribute.labels[remote_model_endpoint]
resource.data.remoteModelInfo.maxBatchingRows
relations.entity.resource.attribute.labels[remote_model_max_batching_rows]
resource.data.remoteModelInfo.remoteModelVersion
relations.entity.resource.attribute.labels[remote_model_version]
resource.data.access.dataset.dataset.datasetId
relations.entity.user.attribute.labels[access_dataset_dataset_datasetid]
resource.data.access.dataset.dataset.projectId
relations.entity.user.attribute.labels[access_dataset_dataset_projectid]
resource.data.access.dataset.targetTypes
relations.entity.user.attribute.labels[access_dataset_dataset_target_types]
resource.data.access.routine.datasetId
relations.entity.user.attribute.labels[access_routine_datasetid]
resource.data.access.routine.projectId
relations.entity.user.attribute.labels[access_routine_projectid]
resource.data.access.routine.routineId
relations.entity.user.attribute.labels[access_routine_routineid]
resource.data.access.view.datasetId
relations.entity.user.attribute.labels[access_view_datasetid]
resource.data.access.view.projectId
relations.entity.user.attribute.labels[access_view_projectid]
resource.data.access.view.tableId
relations.entity.user.attribute.labels[access_view_tableid]
resource.data.access.iamMember
relations.entity.user.attribute.labels[iam_member]
