# Collect Google Cloud Kubernetes Context logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/cloud/context-parsers/gcp-kubernetes-context/  
**Scraped:** 2026-03-05T09:17:17.276020Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Cloud Kubernetes Context logs
This document describes how fields of Google Cloud Kubernetes Context logs map to Google Security Operations Unified Data Model (UDM) fields.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GCP_KUBERNETES_CONTEXT
ingestion label.
For information about other context parsers that Google SecOps supports, see
Google SecOps context parsers
.
Supported Google Cloud Kubernetes Context logs log formats
The Google Cloud Kubernetes Context logs parser supports logs in JSON format.
Supported Google Cloud Kubernetes Context logs sample logs
JSON:
{
  "name": "//container.googleapis.com/projects/chronicle-dpa-test/locations/us-west2/clusters/us-west2-looker-composer-13ff96ad-gke/k8s/namespaces/composer-2-0-25-airflow-2-2-5-13ff96ad/apps/deployments/airflow-scheduler",
  "assetType": "apps.k8s.io/Deployment",
  "resource": {
    "version": "v1",
    "discoveryDocumentUri": "https://raw.githubusercontent.com/kubernetes/kubernetes/master/api/openapi-spec/swagger.json",
    "discoveryName": "io.k8s.api.apps.v1.Deployment",
    "parent": "//container.googleapis.com/projects/chronicle-dpa-test/locations/us-west2/clusters/us-west2-looker-composer-13ff96ad-gke/k8s/namespaces/composer-2-0-25-airflow-2-2-5-13ff96ad",
    "data": {
      "metadata": {
        "annotations": {
          "deployment.kubernetes.io/revision": "2"
        },
        "clusterName": "",
        "creationTimestamp": "2023-04-04T09:31:48Z",
        "generateName": "",
        "generation": 2,
        "labels": {
          "run": "airflow-scheduler"
        },
        "name": "airflow-scheduler",
        "namespace": "composer-2-0-25-airflow-2-2-5-13ff96ad",
        "resourceVersion": "16338",
        "selfLink": "",
        "uid": "805b92ef-6616-4e05-86c6-4ba3101dffa9"
      },
      "spec": {
        "minReadySeconds": 0,
        "paused": false,
        "progressDeadlineSeconds": 600,
        "replicas": 1,
        "revisionHistoryLimit": 10,
        "selector": {
          "matchLabels": {
            "run": "airflow-scheduler"
          }
        },
        "strategy": {
          "rollingUpdate": {
            "maxSurge": 1,
            "maxUnavailable": 1
          },
          "type": "RollingUpdate"
        },
        "template": {
          "metadata": {
            "annotations": {
              "cluster-autoscaler.kubernetes.io/safe-to-evict": "true"
            },
            "clusterName": "",
            "creationTimestamp": null,
            "generateName": "",
            "generation": 0,
            "labels": {
              "composer-system-pod": "true",
              "run": "airflow-scheduler"
            },
            "name": "",
            "namespace": "",
            "resourceVersion": "",
            "selfLink": "",
            "uid": ""
          },
          "spec": {
            "containers": [
              {
                "args": [
                  "scheduler"
                ],
                "env": [
                  {
                    "name": "AIRFLOW_LOOKER_GCP_REGION",
                    "value": "us-west2"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_MODEL_FILES_GCS_BUCKET",
                    "value": "composer-gcs-model-files-582699623097"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_SA_ETL_BQ_DATASET",
                    "value": "looker_system_activity"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_SCHEDULE_INTERVAL",
                    "value": "@daily"
                  },
                  {
                    "name": "CLOUDSDK_METRICS_ENVIRONMENT",
                    "value": "2.2.5+composer"
                  },
                  {
                    "name": "GCS_BUCKET",
                    "value": "us-west2-looker-composer-13ff96ad-bucket"
                  },
                  {
                    "name": "AIRFLOW_HOME",
                    "value": "/etc/airflow"
                  },
                  {
                    "name": "DAGS_FOLDER",
                    "value": "/home/airflow/gcs/dags"
                  },
                  {
                    "name": "SQL_HOST",
                    "value": "198.51.100.0"
                  },
                  {
                    "name": "SQL_DATABASE",
                    "value": "composer-2-0-25-airflow-2-2-5-13ff96ad"
                  },
                  {
                    "name": "SQL_USER",
                    "value": "root"
                  },
                  {
                    "name": "SQL_PASSWORD",
                    "value": "",
                    "valueFrom": {
                      "secretKeyRef": {
                        "key": "sql_password",
                        "localObjectReference": {
                          "name": "airflow-secrets"
                        }
                      }
                    }
                  },
                  {
                    "name": "GCSFUSE_EXTRACTED",
                    "value": "TRUE"
                  },
                  {
                    "name": "COMPOSER_VERSION",
                    "value": "2.0.25"
                  },
                  {
                    "name": "AIRFLOW__WEBSERVER__BASE_URL",
                    "value": "https://485fdbb7327b42c59ac3907f4753cc05-dot-us-west2.composer.googleusercontent.com"
                  },
                  {
                    "name": "SQL_SUBNET",
                    "value": ""
                  },
                  {
                    "name": "AIRFLOW__CORE__SQL_ALCHEMY_CONN",
                    "value": "postgresql+psycopg2://$(SQL_USER):$(SQL_PASSWORD)@198.51.100.0:3306/$(SQL_DATABASE)"
                  },
                  {
                    "name": "AIRFLOW__CORE__FERNET_KEY",
                    "value": "",
                    "valueFrom": {
                      "secretKeyRef": {
                        "key": "fernet_key",
                        "localObjectReference": {
                          "name": "airflow-secrets"
                        }
                      }
                    }
                  },
                  {
                    "name": "GCP_PROJECT",
                    "value": "chronicle-dpa-test"
                  },
                  {
                    "name": "COMPOSER_LOCATION",
                    "value": "us-west2"
                  },
                  {
                    "name": "COMPOSER_GKE_ZONE",
                    "value": ""
                  },
                  {
                    "name": "COMPOSER_GKE_NAME",
                    "value": "us-west2-looker-composer-13ff96ad-gke"
                  },
                  {
                    "name": "AUTOGKE",
                    "value": "TRUE"
                  },
                  {
                    "name": "COMPOSER_GKE_LOCATION",
                    "value": "us-west2"
                  },
                  {
                    "name": "COMPOSER_PYTHON_VERSION",
                    "value": "3"
                  },
                  {
                    "name": "COMPOSER_ENVIRONMENT",
                    "value": "looker-composer"
                  },
                  {
                    "name": "COMPOSER_VERSIONED_NAMESPACE",
                    "value": "composer-2-0-25-airflow-2-2-5-13ff96ad"
                  },
                  {
                    "name": "GKE_CLUSTER_NAME",
                    "value": "us-west2-looker-composer-13ff96ad-gke"
                  },
                  {
                    "name": "POD_NAME",
                    "value": "",
                    "valueFrom": {
                      "fieldRef": {
                        "apiVersion": "v1",
                        "fieldPath": "metadata.name"
                      }
                    }
                  },
                  {
                    "name": "CONTAINER_NAME",
                    "value": "airflow-scheduler"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_SA_ETL_BQ_DATASET",
                    "value": "looker_system_activity"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_GCP_REGION",
                    "value": "us-west2"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_MODEL_FILES_GCS_BUCKET",
                    "value": "composer-gcs-model-files-582699623097"
                  },
                  {
                    "name": "AIRFLOW_LOOKER_SCHEDULE_INTERVAL",
                    "value": "@daily"
                  }
                ],
                "image": "us-west2-docker.pkg.dev/chronicle-dpa-test/composer-images-us-west2-looker-composer-13ff96ad-gke/2ea83cca-ed14-47b2-a3ef-804cae0f7cb3",
                "imagePullPolicy": "IfNotPresent",
                "livenessProbe": {
                  "failureThreshold": 6,
                  "handler": {
                    "exec": {
                      "command": [
                        "/var/local/scheduler_checker.py"
                      ]
                    }
                  },
                  "initialDelaySeconds": 120,
                  "periodSeconds": 60,
                  "successThreshold": 1,
                  "timeoutSeconds": 30
                },
                "name": "airflow-scheduler",
                "resources": {
                  "limits": {
                    "cpu": "2125m",
                    "ephemeral-storage": "1945Mi",
                    "memory": "2176Mi"
                  },
                  "requests": {
                    "cpu": "2125m",
                    "ephemeral-storage": "1945Mi",
                    "memory": "2176Mi"
                  }
                },
                "stdin": false,
                "stdinOnce": false,
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "tty": false,
                "volumeMounts": [
                  {
                    "mountPath": "/etc/airflow/airflow_cfg",
                    "name": "airflow-config",
                    "readOnly": false,
                    "subPath": "",
                    "subPathExpr": ""
                  },
                  {
                    "mountPath": "/home/airflow/gcs",
                    "name": "gcsdir",
                    "readOnly": false,
                    "subPath": "",
                    "subPathExpr": ""
                  },
                  {
                    "mountPath": "/home/airflow/container-comms",
                    "name": "container-comms",
                    "readOnly": false,
                    "subPath": "",
                    "subPathExpr": ""
                  },
                  {
                    "mountPath": "/home/airflow/gcsfuse",
                    "mountPropagation": "HostToContainer",
                    "name": "gcsfuse",
                    "readOnly": false,
                    "subPath": "",
                    "subPathExpr": ""
                  }
                ],
                "workingDir": ""
              },
              {
                "args": [
                  "/home/airflow/gcs"
                ],
                "env": [
                  {
                    "name": "GCS_BUCKET",
                    "value": "us-west2-looker-composer-13ff96ad-bucket"
                  },
                  {
                    "name": "SQL_DATABASE",
                    "value": "composer-2-0-25-airflow-2-2-5-13ff96ad"
                  },
                  {
                    "name": "SQL_USER",
                    "value": "root"
                  },
                  {
                    "name": "SQL_PASSWORD",
                    "value": "",
                    "valueFrom": {
                      "secretKeyRef": {
                        "key": "sql_password",
                        "localObjectReference": {
                          "name": "airflow-secrets"
                        }
                      }
                    }
                  },
                  {
                    "name": "COMPOSER_GKE_ZONE",
                    "value": ""
                  },
                  {
                    "name": "COMPOSER_GKE_NAME",
                    "value": "us-west2-looker-composer-13ff96ad-gke"
                  },
                  {
                    "name": "SQL_SUBNET",
                    "value": ""
                  },
                  {
                    "name": "AUTOGKE",
                    "value": "TRUE"
                  },
                  {
                    "name": "COMPOSER_GKE_LOCATION",
                    "value": "us-west2"
                  }
                ],
                "image": "us-docker.pkg.dev/cloud-airflow-releaser/gcs-syncd/gcs-syncd:cloud_composer_service_2022-08-23-RC2",
                "imagePullPolicy": "IfNotPresent",
                "name": "gcs-syncd",
                "resources": {
                  "limits": {
                    "cpu": "375m",
                    "ephemeral-storage": "102Mi",
                    "memory": "384Mi"
                  },
                  "requests": {
                    "cpu": "375m",
                    "ephemeral-storage": "102Mi",
                    "memory": "384Mi"
                  }
                },
                "stdin": false,
                "stdinOnce": false,
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "tty": false,
                "volumeMounts": [
                  {
                    "mountPath": "/home/airflow/gcs",
                    "name": "gcsdir",
                    "readOnly": false,
                    "subPath": "",
                    "subPathExpr": ""
                  }
                ],
                "workingDir": ""
              }
            ],
            "dnsPolicy": "ClusterFirst",
            "hostIPC": false,
            "hostNetwork": false,
            "hostPID": false,
            "hostname": "",
            "nodeName": "",
            "priorityClassName": "",
            "restartPolicy": "Always",
            "schedulerName": "default-scheduler",
            "securityContext": {},
            "serviceAccount": "",
            "serviceAccountName": "",
            "subdomain": "",
            "terminationGracePeriodSeconds": 30,
            "tolerations": [
              {
                "effect": "NoSchedule",
                "key": "kubernetes.io/arch",
                "operator": "Equal",
                "value": "amd64"
              }
            ],
            "volumes": [
              {
                "name": "airflow-config",
                "volumeSource": {
                  "configMap": {
                    "defaultMode": 420,
                    "localObjectReference": {
                      "name": "airflow-configmap"
                    }
                  }
                }
              },
              {
                "name": "gcsdir",
                "volumeSource": {
                  "emptyDir": {
                    "medium": ""
                  }
                }
              },
              {
                "name": "container-comms",
                "volumeSource": {
                  "hostPath": {
                    "path": "/var/composer/gcs_mount_status",
                    "type": ""
                  }
                }
              },
              {
                "name": "gcsfuse",
                "volumeSource": {
                  "hostPath": {
                    "path": "/var/composer/gcs_mount",
                    "type": ""
                  }
                }
              }
            ]
          }
        }
      },
      "status": {
        "availableReplicas": 1,
        "conditions": [
          {
            "lastTransitionTime": "2023-04-04T09:31:48Z",
            "lastUpdateTime": "2023-04-04T09:31:48Z",
            "message": "Deployment has minimum availability.",
            "reason": "MinimumReplicasAvailable",
            "status": "True",
            "type": "Available"
          },
          {
            "lastTransitionTime": "2023-04-04T09:31:48Z",
            "lastUpdateTime": "2023-04-04T09:38:49Z",
            "message": "ReplicaSet \\"airflow-scheduler-5569f66584\\" has successfully progressed.",
            "reason": "NewReplicaSetAvailable",
            "status": "True",
            "type": "Progressing"
          }
        ],
        "observedGeneration": 2,
        "readyReplicas": 1,
        "replicas": 1,
        "unavailableReplicas": 0,
        "updatedReplicas": 1
      }
    }
  },
  "ancestors": [
    "projects/582699623097",
    "organizations/383339652788"
  ]
}
Field mapping reference
This section explains how the Google SecOps parser maps Google Cloud Kubernetes Context logs fields to Google SecOps UDM fields.
Log field
UDM mapping
Logic
resource.data.autoscaling.autoprovisioningNodePoolDefaults.serviceAccount
entity.email
resource.data.config.serviceAccount
entity.email
resource.data.spec.hostname
entity.hostname
resource.data.metadata.labels.kubernetes.io/hostname
entity.hostname
resource.data.privateClusterConfig.privateEndpoint
entity.ip
If the
assetType
log field value is equal to
container.googleapis.com/Cluster
, then
temp_ip
field is extracted from the
resource.data.privateClusterConfig.privateEndpoint
log field using Grok pattern, and the
temp_ip
field value is mapped to the
entity.ip
UDM field.
resource.data.spec.loadBalancerIP
entity.ip
If the
assetType
log field value is equal to
k8s.io/Service
, then
temp_ip
field is extracted from the
resource.data.spec.loadBalancerIP
log field using Grok pattern, and the
temp_ip
field value is mapped to the
entity.ip
UDM field.
resource.data.status.hostIP
entity.ip
If the
assetType
log field value is equal to
k8s.io/Pod
, then
temp_ip
field is extracted from the
resource.data.status.hostIP
log field using Grok pattern, and the
temp_ip
field value is mapped to the
entity.ip
UDM field.
resource.data.networkConfig.podIpv4CidrBlock
entity.ip
If the
assetType
log field value is equal to
container.googleapis.com/NodePool
, then
temp_ip
field is extracted from the
resource.data.networkConfig.podIpv4CidrBlock
log field using Grok pattern, and the
temp_ip
field value is mapped to the
entity.ip
UDM field.
resource.data.spec.podCIDRs
entity.ip
If the
assetType
log field value is equal to
container.googleapis.com/NodePool
, then
temp_ip
field is extracted from the
resource.data.spec.podCIDRs
log field using Grok pattern, and the
temp_ip
field value is mapped to the
entity.ip
UDM field.
resource.data.location
entity.location.name
resource.data.metadata.labels.topology.kubernetes.io/region
entity.location.name
resource.data.metadata.labels.failure-domain.beta.kubernetes.io/region
entity.location.name
If the
resource.data.metadata.labels.topology.kubernetes.io/region
log field value is empty, then the
resource.data.metadata.labels.failure-domain.beta.kubernetes.io/region
log field is mapped to the
entity.location.name
UDM field.
resource.location
entity.location.name
resource.data.metadata.namespace
entity.namespace
resource.data.privateClusterConfig.publicEndpoint
entity.nat_ip
resource.data.status.nodeInfo.operatingSystem
entity.platform
If one of the following conditions is met, then the entity.platform UDM field is set to
LINUX
:
If the
resource.data.status.nodeInfo.operatingSystem
log field value is
not
empty and the
resource.data.status.nodeInfo.operatingSystem
log field value matches the regular expression pattern
linux
If the
resource.data.spec.nodeSelector.beta.kubernetes.io/os
log field value is
not
empty and the
resource.data.spec.nodeSelector.beta.kubernetes.io/os
log field value matches the regular expression pattern
linux
If the
resource.data.spec.nodeSelector.kubernetes.io/os
log field value is
not
empty and the
resource.data.spec.nodeSelector.kubernetes.io/os
log field value matches the regular expression pattern
linux
If the
resource.data.metadata.labels.kubernetes.io/os
log field value is
not
empty and the
resource.data.metadata.labels.kubernetes.io/os
log field value matches the regular expression pattern
linux
If the
resource.data.metadata.labels.beta.kubernetes.io/os
log field value is
not
empty and the
resource.data.metadata.labels.beta.kubernetes.io/os
log field value matches the regular expression pattern
linux
If the entity.platform UDM field is not mapped then the
entity.resource.attribute.labels[kubernetes_operatingSystem]
UDM fields is mapped to one of the following log field:
resource.data.status.nodeInfo.operatingSystem
log field if the
resource.data.status.nodeInfo.operatingSystem
log field value is
not
empty
resource.data.spec.nodeSelector.beta.kubernetes.io/os
log field if the
resource.data.spec.nodeSelector.beta.kubernetes.io/os
log field value is
not
empty
resource.data.spec.nodeSelector.kubernetes.io/os
log field if the
resource.data.spec.nodeSelector.kubernetes.io/os
log field value is
not
empty
resource.data.metadata.labels.kubernetes.io/os
log field if the
resource.data.metadata.labels.kubernetes.io/os
log field value is
not
empty
resource.data.metadata.labels.beta.kubernetes.io/os
log field if the
resource.data.metadata.labels.beta.kubernetes.io/os
log field value is
not
empty
resource.data.spec.nodeSelector.beta.kubernetes.io/os
entity.platform
resource.data.spec.nodeSelector.kubernetes.io/os
entity.platform
resource.data.metadata.labels.kubernetes.io/os
entity.platform
resource.data.metadata.labels.beta.kubernetes.io/os
entity.platform
resource.data.nodePools.locations
entity.resource_ancestors.attribute.cloud.availability_zone
resource.data.spec.template.spec.volumes.name
entity.resource_ancestors.name
resource.data.spec.volumes.name
entity.resource_ancestors.name
resource.data.nodePools.name
entity.resource_ancestors.name
resource.data.network
entity.resource_ancestors.name
resource.data.nodePools.config.oauthScopes
entity.resource_ancestors.attribute.permissions.name
entity.resource_ancestors.resource_type
If the
resource.data.nodePools.name
log field value is
not
empty, then the
entity.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
If the
resource.data.network
log field value is
not
empty, then the
entity.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
resource.data.metadata.labels.topology.kubernetes.io/zone
entity.resource.attribute.cloud.availability_zone
resource.data.metadata.labels.failure-domain.beta.kubernetes.io/zone
entity.resource.attribute.cloud.availability_zone
If the
resource.data.metadata.labels.topology.kubernetes.io/zone
log field value is empty, then the
resource.data.metadata.labels.failure-domain.beta.kubernetes.io/zone
log field is mapped to the
entity.resource.attribute.cloud.availability_zone
UDM field.
resource.data.locations
entity.resource.attribute.cloud.availability_zone
If the first value of the
resource.data.spec.containers.ports.protocol
log field value is equal to
TCP
or
UDP
, then the
resource.data.spec.containers.ports.protocol
log field is mapped to the
relations.entity.network.ip_protocol
UDM field.
Else, the
resource.data.spec.containers.ports.protocol
log field is mapped to the
relations.entity.resource.attribute.labels[spec_containers_ports_protocol]
UDM field.
entity.resource.attribute.cloud.environment
The
entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.data.metadata.creationTimestamp
entity.resource.attribute.creation_time
resource.data.roleRef.name
entity.resource.attribute.roles.name
name
entity.resource.name
resource.data.config.oauthScopes
entity.resource.attribute.permissions.name
resource.data.autoscaling.autoprovisioningNodePoolDefaults.oauthScopes
entity.resource.attribute.permissions.name
assetType
entity.resource.resource_subtype
entity.resource.resource_type
If the
assetType
log field value is equal to
container.googleapis.com/Cluster
or
container.googleapis.com/NodePool
, then the
entity.resource.resource_type
UDM field is set to
CLUSTER
.
Else, if the
assetType
log field value is equal to
k8s.io/Node
, then the
entity.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else, if the
assetType
log field value is equal to
k8s.io/Pod
, then the
entity.resource.resource_type
UDM field is set to
POD
.
Else, if the
assetType
log field value is equal to
networking.k8s.io/NetworkPolicy
, then the
entity.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
Else, if the
assetType
log field value is equal to
rbac.authorization.k8s.io/ClusterRole
or
rbac.authorization.k8s.io/ClusterRoleBinding
or
rbac.authorization.k8s.io/Role
or
rbac.authorization.k8s.io/RoleBinding
, then the
entity.resource.resource_type
UDM field is set to
SETTING
.
Else, the
entity.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
resource.data.spec.priority
entity.security_result.priority_details
If the
resource.data.spec.priority
log field value is
not
empty and the
resource.data.spec.priorityClassName
log field value is
not
empty, then the
resource.data.spec.priority - resource.data.spec.priorityClassName
log field is mapped to the
entity.security_result.priority_details
UDM field.
Else, if the
resource.data.spec.priority
log field value is
not
empty, then the
resource.data.spec.priorityClassName
log field is mapped to the
entity.security_result.priority_details
UDM field.
Else, if the
resource.data.spec.priorityClassName
log field value is
not
empty, then the
resource.data.spec.priority
log field is mapped to the
entity.security_result.priority_details
UDM field.
resource.data.spec.priorityClassName
entity.security_result.priority_details
resource.data.metadata.selfLink
entity.url
resource.data.selfLink
entity.url
resource.data.spec.serviceAccountName
entity.user.userid
resource.data.createTime
metadata.creation_timestamp
resource.data.metadata.annotations.kubernetes.io/deprecation
metadata.description
metadata.entity_type
The
metadata.entity_type
UDM field is set to
RESOURCE
.
resource.data.metadata.uid
metadata.product_entity_id
The
resource.data.metadata.uid
log field is mapped to the
metadata.product_entity_id
UDM field.
If the
resource.data.metadata.uid
log field value is empty, then the
resource.data.id
log field is mapped to the
metadata.product_entity_id
UDM field.
If the
resource.data.id
log field value is empty, then the
resource.data.name
log field is mapped to the
entity.resource.product_object_id
UDM field.
resource.data.id
metadata.product_entity_id
resource.data.name
metadata.product_entity_id
resource.data.spec.providerID
entity.resource.product_object_id
If the
metadata.product_entity_id
UDM field value is empty and the
entity.resource.product_object_id
UDM field value is empty, then the
resource.data.spec.providerID
log field is mapped to the
entity.resource.product_object_id
UDM field.
Else, the
resource.data.spec.providerID
log field is mapped to the
entity.resource.attribute.labels.spec_providerID
UDM field.
metadata.product_name
The
metadata.product_name
UDM field is set to
GCP Kubernetes
.
resource.version
metadata.product_version
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Cloud Platform
.
relations.entity_type
The
relations.entity_type
UDM field is set to
RESOURCE
if the value of the following log fields are not empty:
ancestors
resource.data.metadata.clusterName
resource.data.spec.containers.name
resource.data.spec.template.spec.containers.name
resource.data.spec.template.metadata.clusterName
resource.data.status.containerStatuses.name
resource.data.status.initContainerStatuses.name
resource.data.spec.initContainers.name
resource.data.spec.template.spec.initContainers.name
resource.data.metadata.ownerReferences.name
resource.data.spec.containers.workingDir
relations.entity.file.full_path
resource.data.spec.template.spec.containers.workingDir
relations.entity.file.full_path
resource.data.spec.initContainers.workingDir
relations.entity.file.full_path
resource.data.spec.template.spec.initContainers.workingDir
relations.entity.file.full_path
relations.direction
The
relations.direction
UDM field is set to
UNIDIRECTIONAL
if the value of the following log fields are not empty:
ancestors
resource.data.metadata.clusterName
resource.data.spec.containers.name
resource.data.spec.template.spec.containers.name
resource.data.spec.template.metadata.clusterName
resource.data.status.containerStatuses.name
resource.data.status.initContainerStatuses.name
resource.data.spec.initContainers.name
resource.data.spec.template.spec.initContainers.name
resource.data.metadata.ownerReferences.name
resource.data.spec.containers.ports.protocol
relations.entity.network.ip_protocol
If the
index
log field value is equal to
0
and the
resource.data.spec.containers.ports.protocol
log field value is equal to
TCP
or
UDP
, then the
resource.data.spec.containers.ports.protocol
log field is mapped to the
relations.entity.network.ip_protocol
UDM field.
Else, the
resource.data.spec.containers.ports.protocol
log field is mapped to the
relations.entity.resource.attribute.labels.spec_containers_ports
protocol
%index
UDM field.
relations.entity.resource_ancestors.attribute.cloud.environment
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
resource.parent
log field value does not contain the
res_type
field value, then the
relations.entity.resource_ancestors.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
ancestors
relations.entity.resource_ancestors.name
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
resource.parent
log field value does not contain the
res_type
field value, then the
ancestors
log field is mapped to the
relations.entity.resource_ancestors.name
UDM field.
relations.entity.resource_ancestors.resource_subtype
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
resource.parent
log field value does not contain the
res_type
field value, then the
res_type
field is mapped to the
relations.entity.resource_ancestors.resource_subtype
UDM field.
relations.entity.resource_ancestors.resource_type
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
resource.parent
log field value does not contain the
res_type
field value, then the
relations.entity.resource_ancestors.resource_type
UDM field is set to
CLOUD_PROJECT
.
relations.entity.resource.attribute.cloud.environment
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
resource.parent
log field value does not contain the
res_type
field value, then the
relations.entity.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
resource.parent
relations.entity.resource.name
resource.data.metadata.clusterName
relations.entity.resource.name
resource.data.spec.containers.name
relations.entity.resource.name
resource.data.spec.template.spec.containers.name
relations.entity.resource.name
resource.data.spec.template.metadata.clusterName
relations.entity.resource.name
resource.data.status.containerStatuses.name
relations.entity.resource.name
resource.data.status.initContainerStatuses.name
relations.entity.resource.name
resource.data.spec.initContainers.name
relations.entity.resource.name
resource.data.spec.template.spec.initContainers.name
relations.entity.resource.name
resource.data.metadata.ownerReferences.name
relations.entity.resource.name
resource.data.status.containerStatuses.containerID
relations.entity.resource.product_object_id
The
container_id
field is extracted from the
Resource.data.status.containerStatuses.containerID
log field using Grok pattern.
If the
container_id
field value is
not
empty, then the
container_id
field is mapped to the
relations.entity.resource.product_object_id
UDM field.
resource.data.status.initContainerStatuses.containerID
relations.entity.resource.product_object_id
The
container_id
field is extracted from the
Resource.data.status.initContainerStatuses.containerID
log field using Grok pattern.
If the
container_id
field value is
not
empty, then the
container_id
field is mapped to the
relations.entity.resource.product_object_id
UDM field.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
if the value of the following log fields are not empty:
ancestors
resource.data.metadata.clusterName
resource.data.spec.containers.name
resource.data.spec.template.spec.containers.name
resource.data.spec.template.metadata.clusterName
resource.data.status.containerStatuses.name
resource.data.status.initContainerStatuses.name
resource.data.spec.initContainers.name
resource.data.spec.template.spec.initContainers.name
resource.data.metadata.ownerReferences.name
relations.entity.resource.resource_type
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
res_type
field value is
not
empty and the
resource.parent
log field value contains
res_type
field value, then the
relations.entity.resource.resource_type
UDM field is set to
CLOUD_PROJECT
.
relations.entity.resource.resource_subtype
The
res_type
field is extracted from the
ancestors
log field using Grok pattern.
If the
res_type
field value is
not
empty and the
resource.parent
log field value contains
res_type
field value, then the
res_type
field is mapped to the
relations.entity.resource.resource_subtype
UDM field.
updateTime
entity.resource.attribute.last_update_time
resource.data.nodePools.autoscaling.autoprovisioned
entity.resource_ancestors.attribute.labels[nodePools_autoscaling_autoprovisioned]
resource.data.nodePools.autoscaling.enabled
entity.resource_ancestors.attribute.labels[nodePools_autoscaling_enabled]
resource.data.nodePools.autoscaling.maxNodeCount
entity.resource_ancestors.attribute.labels[nodePools_autoscaling_maxNodeCount]
resource.data.nodePools.config.diskSizeGb
entity.resource_ancestors.attribute.labels[nodePools_config_diskSizeGb]
resource.data.nodePools.config.diskType
entity.resource_ancestors.attribute.labels[nodePools_config_diskType]
resource.data.nodePools.config.imageType
entity.resource_ancestors.attribute.labels[nodePools_config_imageType]
resource.data.nodePools.config.machineType
entity.resource_ancestors.attribute.labels[nodePools_config_machineType]
resource.data.nodePools.config.metadata.disable-legacy-endpoints
entity.resource_ancestors.attribute.labels[nodePools_config_metadata_disable-legacy-endpoints]
resource.data.nodePools.config.reservationAffinity.consumeReservationType
entity.resource_ancestors.attribute.labels[nodePools_config_reservationAffinity_consumeReservationType]
resource.data.nodePools.config.serviceAccount
entity.resource_ancestors.attribute.labels[nodePools_config_serviceAccount]
resource.data.nodePools.config.shieldedInstanceConfig.enableIntegrityMonitoring
entity.resource_ancestors.attribute.labels[nodePools_config_shieldedInstanceConfig_enableIntegrityMonitoring]
resource.data.nodePools.config.shieldedInstanceConfig.enableSecureBoot
entity.resource_ancestors.attribute.labels[nodePools_config_shieldedInstanceConfig_enableSecureBoot]
resource.data.nodePools.config.workloadMetadataConfig.mode
entity.resource_ancestors.attribute.labels[nodePools_config_workloadMetadataConfig_mode]
resource.data.nodePools.etag
entity.resource_ancestors.attribute.labels[nodePools_etag]
resource.data.nodePools.initialNodeCount
entity.resource_ancestors.attribute.labels[nodePools_initialNodeCount]
resource.data.nodePools.instanceGroupUrls
entity.resource_ancestors.attribute.labels[nodePools_instanceGroupUrls]
resource.data.nodePools.management.autoRepair
entity.resource_ancestors.attribute.labels[nodePools_management_autoRepair]
resource.data.nodePools.management.autoUpgrade
entity.resource_ancestors.attribute.labels[nodePools_management_autoUpgrade]
resource.data.nodePools.maxPodsConstraint.maxPodsPerNode
entity.resource_ancestors.attribute.labels[nodePools_maxPodsConstraint_maxPodsPerNode]
resource.data.nodePools.networkConfig.enablePrivateNodes
entity.resource_ancestors.attribute.labels[nodePools_networkConfig_enablePrivateNodes]
resource.data.nodePools.networkConfig.podIpv4CidrBlock
entity.resource_ancestors.attribute.labels[nodePools_networkConfig_podIpv4CidrBlock]
resource.data.nodePools.networkConfig.podRange
entity.resource_ancestors.attribute.labels[nodePools_networkConfig_podRange]
resource.data.nodePools.podIpv4CidrSize
entity.resource_ancestors.attribute.labels[nodePools_podIpv4CidrSize]
resource.data.nodePools.selfLink
entity.resource_ancestors.attribute.labels[nodePools_selfLink]
resource.data.nodePools.status
entity.resource_ancestors.attribute.labels[nodePools_status]
resource.data.nodePools.upgradeSettings.maxSurge
entity.resource_ancestors.attribute.labels[nodePools_upgradeSettings_maxSurge]
resource.data.nodePools.upgradeSettings.strategy
entity.resource_ancestors.attribute.labels[nodePools_upgradeSettings_strategy]
resource.data.nodePools.version
entity.resource_ancestors.attribute.labels[nodePools_version]
resource.data.spec.volumes.volumeSource.configMap.defaultMode
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_configMap_defaultMode]
resource.data.spec.volumes.volumeSource.configMap.items.key
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_configMap_items_key]
resource.data.spec.volumes.volumeSource.configMap.items.path
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_configMap_items_path]
resource.data.spec.volumes.volumeSource.configMap.localObjectReference.name
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_configMap_localObjRef_name]
resource.data.spec.volumes.volumeSource.configMap.optional
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_configMap_optional]
resource.data.spec.volumes.volumeSource.emptyDir.medium
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_emptyDir_medium]
resource.data.spec.volumes.volumeSource.hostPath.path
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_hostPath_path]
resource.data.spec.volumes.volumeSource.hostPath.type
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_hostPath_type]
resource.data.spec.volumes.volumeSource.persistentVolumeClaim.claimName
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_persistentVolumeClaim_claimName]
resource.data.spec.volumes.volumeSource.persistentVolumeClaim.readOnly
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_persistentVolumeClaim_readOnly]
resource.data.spec.volumes.volumeSource.projected.defaultMode
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_projected_defaultMode]
resource.data.spec.volumes.volumeSource.projected.sources.configMap.items.key
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_projected_sources_configMap_items_key]
resource.data.spec.volumes.volumeSource.projected.sources.configMap.items.path
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_projected_sources_configMap_items_path]
resource.data.spec.volumes.volumeSource.projected.sources.configMap.localObjectReference.name
entity.resource_ancestors.attribute.labels[spec_vols_volSource_proj_src_configMap_localObjRef_name]
resource.data.spec.volumes.volumeSource.projected.sources.downwardAPI.items.fieldRef.apiVersion
entity.resource_ancestors.attribute.labels[spec_vol_volSource_proj_src_downwardAPI_items_fieldRef_apiVersion]
resource.data.spec.volumes.volumeSource.projected.sources.downwardAPI.items.fieldRef.fieldPath
entity.resource_ancestors.attribute.labels[spec_vols_voSource_proj_src_downwardAPI_items_fieldRef_fieldPath]
resource.data.spec.volumes.volumeSource.projected.sources.downwardAPI.items.path
entity.resource_ancestors.attribute.labels[spec_vols_volSource_proj_src_downwardAPI_items_path]
resource.data.spec.volumes.volumeSource.projected.sources.serviceAccountToken.audience
entity.resource_ancestors.attribute.labels[spec_vols_volSource_proj_src_serviceAccountToken_audience]
resource.data.spec.volumes.volumeSource.projected.sources.serviceAccountToken.expirationSeconds
entity.resource_ancestors.attribute.labels[spec_vols_volSource_proj_src_serviceAccountToken_expirationSeconds]
resource.data.spec.volumes.volumeSource.projected.sources.serviceAccountToken.path
entity.resource_ancestors.attribute.labels[spec_vols_volSource_proj_sources_serviceAccountToken_path]
resource.data.spec.volumes.volumeSource.secret.defaultMode
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_secret_defaultMode]
resource.data.spec.volumes.volumeSource.secret.optional
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_secret_optional]
resource.data.spec.volumes.volumeSource.secret.secretName
entity.resource_ancestors.attribute.labels[spec_volumes_volumeSource_secret_secretName]
resource.data.spec.template.spec.volumes.volumeSource.configMap.defaultMode
entity.resource_ancestors.attribute.labels[tsvv_configMap_defaultMode]
resource.data.spec.template.spec.volumes.volumeSource.configMap.localObjectReference.name
entity.resource_ancestors.attribute.labels[tsvv_configMap_localObjectReference_name]
resource.data.spec.template.spec.volumes.volumeSource.configMap.optional
entity.resource_ancestors.attribute.labels[tsvv_configMap_optional]
resource.data.spec.template.spec.volumes.volumeSource.emptyDir.medium
entity.resource_ancestors.attribute.labels[tsvv_emptyDir_medium]
resource.data.spec.template.spec.volumes.volumeSource.hostPath.path
entity.resource_ancestors.attribute.labels[tsvv_hostPath_path]
resource.data.spec.template.spec.volumes.volumeSource.hostPath.type
entity.resource_ancestors.attribute.labels[tsvv_hostPath_type]
resource.data.spec.template.spec.volumes.volumeSource.projected.defaultMode
entity.resource_ancestors.attribute.labels[tsvv_projected_defaultMode]
resource.data.spec.template.spec.volumes.volumeSource.projected.sources.serviceAccountToken.audience
entity.resource_ancestors.attribute.labels[tsvv_proj_sources_serviceAccountToken_audience]
resource.data.spec.template.spec.volumes.volumeSource.projected.sources.serviceAccountToken.expirationSeconds
entity.resource_ancestors.attribute.labels[tsvv_projected_sources_serviceAccountToken_expirationSeconds]
resource.data.spec.template.spec.volumes.volumeSource.projected.sources.serviceAccountToken.path
entity.resource_ancestors.attribute.labels[tsvv_projected_sources_serviceAccountToken_path]
resource.data.spec.template.spec.volumes.volumeSource.secret.defaultMode
entity.resource_ancestors.attribute.labels[tsvv_secret_defaultMode]
resource.data.spec.template.spec.volumes.volumeSource.secret.optional
entity.resource_ancestors.attribute.labels[tsvv_secret_optional]
resource.data.spec.template.spec.volumes.volumeSource.secret.secretName
entity.resource_ancestors.attribute.labels[tsvv_secret_secretName]
resource.data.networkConfig.datapathProvider
entity.resource_ancestors.attribute.labels[networkConfig_datapathProvider]
resource.data.networkConfig.enableIntraNodeVisibility
entity.resource_ancestors.attribute.labels[networkConfig_enableIntraNodeVisibility]
resource.data.networkConfig.enablePrivateNodes
entity.resource_ancestors.attribute.labels[networkConfig_enablePrivateNodes]
resource.data.networkConfig.network
entity.resource_ancestors.attribute.labels[networkConfig_network]
resource.data.networkConfig.podRange
entity.resource_ancestors.attribute.labels[networkConfig_podRange]
resource.data.networkConfig.subnetwork
entity.resource_ancestors.attribute.labels[networkConfig_subnetwork]
resource.data.addonsConfig.dnsCacheConfig.enabled
entity.resource.attribute.labels[addonsConfig_dnsCacheConfig_enabled]
resource.data.addonsConfig.gcePersistentDiskCsiDriverConfig.enabled
entity.resource.attribute.labels[addonsConfig_gcePersistentDiskCsiDriverConfig_enabled]
resource.data.addonsConfig.gcpFilestoreCsiDriverConfig.enabled
entity.resource.attribute.labels[addonsConfig_gcpFilestoreCsiDriverConfig_enabled]
resource.data.addonsConfig.kubernetesDashboard.disabled
entity.resource.attribute.labels[addonsConfig_kubernetesDashboard_disabled]
resource.data.addonsConfig.networkPolicyConfig.disabled
entity.resource.attribute.labels[addonsConfig_networkPolicyConfig_disabled]
resource.data.aggregationRule.clusterRoleSelectors.matchLabels.rbac.authorization.k8s.io/aggregate-to-admin
entity.resource.attribute.labels[clusterRoleSelectors_rbac_authorization_k8s.io_aggregate-to-admin]
resource.data.aggregationRule.clusterRoleSelectors.matchLabels.rbac.authorization.k8s.io/aggregate-to-edit
entity.resource.attribute.labels[clusterRoleSelectors_rbac_authorization_k8s.io_aggregate-to-edit]
resource.data.aggregationRule.clusterRoleSelectors.matchLabels.rbac.authorization.k8s.io/aggregate-to-view
entity.resource.attribute.labels[clusterRoleSelectors_authorization_k8s.io_aggregate-to-view]
resource.data.spec.template.metadata.annotations.cluster-autoscaler.kubernetes.io/safe-to-evict
entity.resource.attribute.labels[annotations_cluster-autoscaler_kubernetes.io_safe-to-evict]
resource.data.metadata.annotations.container.googleapis.com/instance_id
entity.resource.attribute.labels[annotations_container_googleapis_com_instance_id]
resource.data.metadata.annotations.csi.volume.kubernetes.io/nodeid
entity.resource.attribute.labels[annotations_csi_volume_kubernetes.io_nodeid]
resource.data.metadata.annotations.node.alpha.kubernetes.io/ttl
entity.resource.attribute.labels[annotations_node_alpha_kubernetes.io_ttl]
resource.data.metadata.annotations.node.gke.io/last-applied-node-labels
entity.resource.attribute.labels[annotations_node_gke.io_last-applied-node-labels]
resource.data.metadata.annotations.node.gke.io/last-applied-node-taints
entity.resource.attribute.labels[annotations_node_gke.io_last-applied-node-taints]
resource.data.metadata.annotations.volumes.kubernetes.io/controller-managed-attach-detach
entity.resource.attribute.labels[annotations_volumes_k8s.io_controller-managed-attach-detach]
resource.data.autopilot.enabled
entity.resource.attribute.labels[autopilot_enabled]
resource.data.autoscaling.autoprovisioned
entity.resource.attribute.labels[autoscaling_autoprovisioned]
resource.data.autoscaling.autoprovisioningNodePoolDefaults.imageType
entity.resource.attribute.labels[autoscaling_autoprovisioningNodePoolDefaults_imageType]
resource.data.autoscaling.autoprovisioningNodePoolDefaults.management.autoRepair
entity.resource.attribute.labels[autoscaling_autoprovisioningNodePoolDefaults_management_autoRepair]
resource.data.autoscaling.autoprovisioningNodePoolDefaults.management.autoUpgrade
entity.resource.attribute.labels[autoscaling_autoprovisioningNodePoolDefaults_management_autoUpgrade]
resource.data.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.maxSurge
entity.resource.attribute.labels[autoscaling_autoprovisioningNodePoolDefaults_upgradeSettings_maxSurge]
resource.data.autoscaling.autoprovisioningNodePoolDefaults.upgradeSettings.strategy
entity.resource.attribute.labels[autoscaling_autoprovisioningNodePoolDefaults_upgradeSettings_strategy]
resource.data.autoscaling.autoscalingProfile
entity.resource.attribute.labels[autoscaling_autoscalingProfile]
resource.data.autoscaling.enabled
entity.resource.attribute.labels[autoscaling_enabled]
resource.data.autoscaling.enableNodeAutoprovisioning
entity.resource.attribute.labels[autoscaling_enableNodeAutoprovisioning]
resource.data.autoscaling.maxNodeCount
entity.resource.attribute.labels[autoscaling_maxNodeCount]
resource.data.autoscaling.resourceLimits.maximum
entity.resource.attribute.labels[autoscaling_resourceLimits_maximum]
resource.data.autoscaling.resourceLimits.resourceType
entity.resource.attribute.labels[autoscaling_resourceLimits_resourceType]
resource.data.binaryAuthorization.evaluationMode
entity.resource.attribute.labels[binaryAuthorization_evaluationMode]
resource.data.clusterIpv4Cidr
entity.resource.attribute.labels[clusterIpv4Cidr]
resource.data.config.diskSizeGb
entity.resource.attribute.labels[config_diskSizeGb]
resource.data.config.diskType
entity.resource.attribute.labels[config_diskType]
resource.data.config.imageType
entity.resource.attribute.labels[config_imageType]
resource.data.config.machineType
entity.resource.attribute.labels[config_machineType]
resource.data.config.metadata.disable-legacy-endpoints
entity.resource.attribute.labels[config_metadata_disable-legacy-endpoints]
resource.data.config.reservationAffinity.consumeReservationType
entity.resource.attribute.labels[config_reservationAffinity_consumeReservationType]
resource.data.config.shieldedInstanceConfig.enableIntegrityMonitoring
entity.resource.attribute.labels[config_shieldedInstanceConfig_enableIntegrityMonitoring]
resource.data.config.shieldedInstanceConfig.enableSecureBoot
entity.resource.attribute.labels[config_shieldedInstanceConfig_enableSecureBoot]
resource.data.config.workloadMetadataConfig.mode
entity.resource.attribute.labels[config_workloadMetadataConfig_mode]
resource.data.currentMasterVersion
entity.resource.attribute.labels[currentMasterVersion]
resource.data.currentNodeCount
entity.resource.attribute.labels[currentNodeCount]
resource.data.databaseEncryption.state
entity.resource.attribute.labels[databaseEncryption_state]
resource.data.defaultMaxPodsConstraint.maxPodsPerNode
entity.resource.attribute.labels[defaultMaxPodsConstraint_maxPodsPerNode]
resource.data.maxPodsConstraint.maxPodsPerNode
entity.resource.attribute.labels[maxPodsConstraint_maxPodsPerNode]
resource.data.metadata.annotations.deployment.kubernetes.io/desired-replicas
entity.resource.attribute.labels[deployment_kubernetes.io_desired-replicas]
resource.data.metadata.annotations.deployment.kubernetes.io/max-replicas
entity.resource.attribute.labels[deployment_kubernetes.io_max-replicas]
resource.data.metadata.annotations.deployment.kubernetes.io/revision
entity.resource.attribute.labels[deployment_kubernetes.io_revision]
resource.discoveryDocumentUri
entity.resource.attribute.labels[discovery_document]
resource.discoveryName
entity.resource.attribute.labels[discovery_name]
resource.data.endpoint
entity.resource.attribute.labels[endpoint]
resource.data.etag
entity.resource.attribute.labels[etag]
resource.data.initialClusterVersion
entity.resource.attribute.labels[initialClusterVersion]
resource.data.initialNodeCount
entity.resource.attribute.labels[initialNodeCount]
resource.data.ipAllocationPolicy.clusterIpv4CidrBlock
entity.resource.attribute.labels[ipAllocationPolicy_clusterIpv4CidrBlock]
resource.data.ipAllocationPolicy.clusterSecondaryRangeName
entity.resource.attribute.labels[ipAllocationPolicy_clusterSecondaryRangeName]
resource.data.ipAllocationPolicy.servicesIpv4CidrBlock
entity.resource.attribute.labels[ipAllocationPolicy_servicesIpv4CidrBlock]
resource.data.ipAllocationPolicy.servicesSecondaryRangeName
entity.resource.attribute.labels[ipAllocationPolicy_servicesSecondaryRangeName]
resource.data.ipAllocationPolicy.stackType
entity.resource.attribute.labels[ipAllocationPolicy_stackType]
resource.data.ipAllocationPolicy.useIpAliases
entity.resource.attribute.labels[ipAllocationPolicy_useIpAliases]
resource.data.labelFingerprint
entity.resource.attribute.labels[labelFingerprint]
resource.data.loggingConfig.componentConfig.enableComponents
entity.resource.attribute.labels[loggingConfig_componentConfig_enableComponents]
resource.data.loggingService
entity.resource.attribute.labels[loggingService]
resource.data.management.autoRepair
entity.resource.attribute.labels[management_autoRepair]
resource.data.management.autoUpgrade
entity.resource.attribute.labels[management_autoUpgrade]
resource.data.masterAuth.clusterCaCertificate
entity.resource.attribute.labels[masterAuth_clusterCaCertificate]
resource.data.masterAuthorizedNetworksConfig.enabled
entity.resource.attribute.labels[masterAuthorizedNetworksConfig_enabled]
resource.data.masterAuthorizedNetworksConfig.gcpPublicCidrsAccessEnabled
entity.resource.attribute.labels[masterAuthorizedNetworksConfig_gcpPublicCidrsAccessEnabled]
resource.data.metadata.annotations.batch.kubernetes.io/job-tracking
entity.resource.attribute.labels[metadata_annotations_batch_kubernetes.io/job-tracking]
resource.data.metadata.annotations.bundling-component
entity.resource.attribute.labels[metadata_annotations_bundling-component]
resource.data.metadata.annotations.cloud.google.com/neg
entity.resource.attribute.labels[metadata_annotations_cloud_google_com/neg]
resource.data.metadata.annotations.cluster-autoscaler.kubernetes.io/safe-to-evict
entity.resource.attribute.labels[metadata_annotations_cluster-autoscaler_kubernetes.io/safe-to-evict]
resource.data.metadata.annotations.components.gke.io/component-name
entity.resource.attribute.labels[metadata_annotations_components_gke.io/component-name]
resource.data.metadata.annotations.components.gke.io/component-version
entity.resource.attribute.labels[metadata_annotations_components_gke.io/component-version]
resource.data.metadata.annotations.components.gke.io/layer
entity.resource.attribute.labels[metadata_annotations_components_gke.io/layer]
resource.data.metadata.annotations.composer.cloud.google.com/running-task
entity.resource.attribute.labels[metadata_annotations_composer_cloud_google_com/running-task]
resource.data.metadata.annotations.composer.cloud.google.com/template-version
entity.resource.attribute.labels[metadata_annotations_composer_cloud_google_com/template-version]
resource.data.metadata.annotations.configHash
entity.resource.attribute.labels[metadata_annotations_configHash]
resource.data.metadata.annotations.container.seccomp.security.alpha.kubernetes.io/gke-metrics-agent
entity.resource.attribute.labels[metadata_annotations_container_seccomp_sec_alpha_gke-metrics-agent]
resource.data.metadata.annotations.container.seccomp.security.alpha.kubernetes.io/metrics-server-nanny
entity.resource.attribute.labels[metadata_annotations_container_seccomp_sec_alpha_metrics-server-nanny]
resource.data.metadata.annotations.container.seccomp.security.alpha.kubernetes.io/metrics-server
entity.resource.attribute.labels[metadata_annotations_container_seccomp_sec_alpha_metrics-server]
resource.data.metadata.annotations.credential-normal-mode
entity.resource.attribute.labels[metadata_annotations_credential-normal-mode]
resource.data.metadata.annotations.EnableNodeJournal
entity.resource.attribute.labels[metadata_annotations_EnableNodeJournal]
resource.data.metadata.annotations.kubernetes.io/config.hash
entity.resource.attribute.labels[metadata_annotations_kubernetes.io/config_hash]
resource.data.metadata.annotations.kubernetes.io/config.mirror
entity.resource.attribute.labels[metadata_annotations_kubernetes.io/config_mirror]
resource.data.metadata.annotations.kubernetes.io/config.seen
entity.resource.attribute.labels[metadata_annotations_kubernetes.io/config_seen]
resource.data.metadata.annotations.kubernetes.io/config.source
entity.resource.attribute.labels[metadata_annotations_kubernetes.io/config_source]
resource.data.metadata.annotations.monitoring.gke.io/path
entity.resource.attribute.labels[metadata_annotations_monitoring_gke.io/path]
resource.data.metadata.annotations.orphanDependents
entity.resource.attribute.labels[metadata_annotations_orphanDependents]
resource.data.metadata.annotations.prometheus.io/port
entity.resource.attribute.labels[metadata_annotations_prometheus.io/port]
resource.data.metadata.annotations.prometheus.io/scrape
entity.resource.attribute.labels[metadata_annotations_prometheus.io/scrape]
resource.data.metadata.annotations.rbac.authorization.kubernetes.io/autoupdate
entity.resource.attribute.labels[metadata_annotations_rbac_authorization_kubernetes.io/autoupdate]
resource.data.metadata.annotations.scheduler.alpha.kubernetes.io/critical-pod
entity.resource.attribute.labels[metadata_annotations_scheduler_alpha_kubernetes.io/critical-pod]
resource.data.metadata.annotations.seccomp.security.alpha.kubernetes.io/pod
entity.resource.attribute.labels[metadata_annotations_seccomp_security_alpha_kubernetes.io/pod]
resource.data.metadata.annotations.SystemOnlyLogging
entity.resource.attribute.labels[metadata_annotations_SystemOnlyLogging]
resource.data.metadata.generateName
entity.resource.attribute.labels[metadata_generateName]
resource.data.metadata.generation
entity.resource.attribute.labels[metadata_generation]
resource.data.metadata.labels.addon.gke.io/node-local-dns-ds-ready
entity.resource.attribute.labels[metadata_labels_addon_gke.io/node-local-dns-ds-ready]
resource.data.metadata.labels.addonmanager.kubernetes.io/mode
entity.resource.attribute.labels[metadata_labels_addonmanager_kubernetes.io/mode]
resource.data.metadata.labels.app
entity.resource.attribute.labels[metadata_labels_app]
resource.data.metadata.labels.beta.kubernetes.io/arch
entity.resource.attribute.labels[metadata_labels_beta_kubernetes.io/arch]
resource.data.metadata.labels.beta.kubernetes.io/instance-type
entity.resource.attribute.labels[metadata_labels_beta_kubernetes.io/instance-type]
resource.data.metadata.labels.cloud.google.com/gke-boot-disk
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-boot-disk]
resource.data.metadata.labels.cloud.google.com/gke-container-runtime
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-container-runtime]
resource.data.metadata.labels.cloud.google.com/gke-cpu-scaling-level
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-cpu-scaling-level]
resource.data.metadata.labels.cloud.google.com/gke-logging-variant
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-logging-variant]
resource.data.metadata.labels.cloud.google.com/gke-max-pods-per-node
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-max-pods-per-node]
resource.data.metadata.labels.cloud.google.com/gke-netd-ready
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-netd-ready]
resource.data.metadata.labels.cloud.google.com/gke-nodepool
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-nodepool]
resource.data.metadata.labels.cloud.google.com/gke-os-distribution
entity.resource.attribute.labels[metadata_labels_cloud_google_com/gke-os-distribution]
resource.data.metadata.labels.cloud.google.com/machine-family
entity.resource.attribute.labels[metadata_labels_cloud_google_com/machine-family]
resource.data.metadata.labels.cloud.google.com/private-node
entity.resource.attribute.labels[metadata_labels_cloud_google_com/private-node]
resource.data.metadata.labels.component
entity.resource.attribute.labels[metadata_labels_component]
resource.data.metadata.labels.composer-component
entity.resource.attribute.labels[metadata_labels_composer-component]
resource.data.metadata.labels.composer-system-pod
entity.resource.attribute.labels[metadata_labels_composer-system-pod]
resource.data.metadata.labels.control-plane
entity.resource.attribute.labels[metadata_labels_control-plane]
resource.data.metadata.labels.controller-revision-hash
entity.resource.attribute.labels[metadata_labels_controller-revision-hash]
resource.data.metadata.labels.controller-uid
entity.resource.attribute.labels[metadata_labels_controller-uid]
resource.data.metadata.labels.gke-app
entity.resource.attribute.labels[metadata_labels_gke-app]
resource.data.metadata.labels.iam.gke.io/gke-metadata-server-enabled
entity.resource.attribute.labels[metadata_labels_iam_gke.io/gke-metadata-server-enabled]
resource.data.metadata.labels.job-name
entity.resource.attribute.labels[metadata_labels_job-name]
resource.data.metadata.labels.k8s-app
entity.resource.attribute.labels[metadata_labels_k8s-app]
resource.data.metadata.labels.kubernetes.io/metadata.name
entity.resource.attribute.labels[metadata_labels_k8s.io/metadata_name]
resource.data.metadata.labels.kubernetes.io/arch
entity.resource.attribute.labels[metadata_labels_kubernetes.io/arch]
resource.data.metadata.labels.kubernetes.io/bootstrapping
entity.resource.attribute.labels[metadata_labels_kubernetes.io/bootstrapping]
resource.data.metadata.labels.kubernetes.io/cluster-service
entity.resource.attribute.labels[metadata_labels_kubernetes.io/cluster-service]
resource.data.metadata.labels.kubernetes.io/name
entity.resource.attribute.labels[metadata_labels_kubernetes.io/name]
resource.data.metadata.labels.name
entity.resource.attribute.labels[metadata_labels_name]
resource.data.metadata.labels.node.kubernetes.io/instance-type
entity.resource.attribute.labels[metadata_labels_node_kubernetes.io/instance-type]
resource.data.metadata.labels.node.kubernetes.io/masq-agent-ds-ready
entity.resource.attribute.labels[metadata_labels_node_kubernetes.io/masq-agent-ds-ready]
resource.data.metadata.labels.nodeType
entity.resource.attribute.labels[metadata_labels_nodeType]
resource.data.metadata.labels.pod-template-generation
entity.resource.attribute.labels[metadata_labels_pod-template-generation]
resource.data.metadata.labels.pod-template-hash
entity.resource.attribute.labels[metadata_labels_pod-template-hash]
resource.data.metadata.labels.provider
entity.resource.attribute.labels[metadata_labels_provider]
resource.data.metadata.labels.run
entity.resource.attribute.labels[metadata_labels_run]
resource.data.metadata.labels.statefulset.kubernetes.io/pod-name
entity.resource.attribute.labels[metadata_labels_statefulset_kubernetes.io/pod-name]
resource.data.metadata.labels.tier
entity.resource.attribute.labels[metadata_labels_tier]
resource.data.metadata.labels.topology.gke.io/zone
entity.resource.attribute.labels[metadata_labels_topology_gke.io/zone]
resource.data.metadata.labels.version
entity.resource.attribute.labels[metadata_labels_version]
resource.data.metadata.managedFields.apiVersion
entity.resource.attribute.labels[metadata_managedFields_apiVersion]
resource.data.metadata.managedFields.fieldsType
entity.resource.attribute.labels[metadata_managedFields_fieldsType]
resource.data.metadata.managedFields.fieldsV1.Raw
entity.resource.attribute.labels[metadata_managedFields_fieldsV1_Raw]
resource.data.metadata.managedFields.manager
entity.resource.attribute.labels[metadata_managedFields_manager]
resource.data.metadata.managedFields.operation
entity.resource.attribute.labels[metadata_managedFields_operation]
resource.data.metadata.managedFields.subresource
entity.resource.attribute.labels[metadata_managedFields_subresource]
resource.data.metadata.managedFields.time
entity.resource.attribute.labels[metadata_managedFields_time]
resource.data.metadata.name
entity.resource.attribute.labels[metadata_name]
resource.data.metadata.resourceVersion
entity.resource.attribute.labels[metadata_resourceVersion]
resource.data.monitoringConfig.advancedDatapathObservabilityConfig.relayMode
entity.resource.attribute.labels[monitoringConfig_advancedDatapathObservabilityConfig_relayMode]
resource.data.monitoringConfig.componentConfig.enableComponents
entity.resource.attribute.labels[monitoringConfig_componentConfig_enableComponents]
resource.data.monitoringService
entity.resource.attribute.labels[monitoringService]
resource.data.nodePoolDefaults.nodeConfigDefaults.loggingConfig.variantConfig.variant
entity.resource.attribute.labels[nodeConfigDefaults_loggingConfig_variantConfig_variant]
resource.data.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey
entity.resource.attribute.labels[template_pdside_podAntiAffinity_topologyKey]
resource.data.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values
entity.resource.attribute.labels[template_pdside_podAntiAffinity_matchExp_values]
resource.data.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key
entity.resource.attribute.labels[template_pdside_podAntiAffinity_matchExp_key]
resource.data.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator
entity.resource.attribute.labels[template_pdside_podAntiAffinity_matchExp_operator]
resource.data.spec.template.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight
entity.resource.attribute.labels[template_pdside_podAntiAffinity_weight]
resource.data.podIpv4CidrSize
entity.resource.attribute.labels[podIpv4CidrSize]
resource.data.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.key
entity.resource.attribute.labels[pdside_podAntiAffinity_matchExp_key]
resource.data.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.operator
entity.resource.attribute.labels[pdside_podAntiAffinity_matchExp_operator]
resource.data.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.labelSelector.matchExpressions.values
entity.resource.attribute.labels[pdside_podAntiAffinity_matchExp_values]
resource.data.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.podAffinityTerm.topologyKey
entity.resource.attribute.labels[pdside_podAntiAffinity_topologyKey]
resource.data.spec.affinity.podAntiAffinity.preferredDuringSchedulingIgnoredDuringExecution.weight
entity.resource.attribute.labels[pdside_podAntiAffinity_weight]
resource.data.privateClusterConfig.enablePrivateNodes
entity.resource.attribute.labels[privateClusterConfig_enablePrivateNodes]
resource.data.privateClusterConfig.masterIpv4CidrBlock
entity.resource.attribute.labels[privateClusterConfig_masterIpv4CidrBlock]
resource.data.privateClusterConfig.peeringName
entity.resource.attribute.labels[privateClusterConfig_peeringName]
resource.data.metadata.labels.rbac.authorization.k8s.io/aggregate-to-admin
entity.resource.attribute.labels[rbac_authorization_k8s.io_aggregate-to-admin]
resource.data.metadata.labels.rbac.authorization.k8s.io/aggregate-to-edit
entity.resource.attribute.labels[rbac_authorization_k8s.io_aggregate-to-edit]
resource.data.metadata.labels.rbac.authorization.k8s.io/aggregate-to-view
entity.resource.attribute.labels[rbac_authorization_k8s.io_aggregate-to-view]
resource.data.releaseChannel.channel
entity.resource.attribute.labels[releaseChannel_channel]
resource.data.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.key
entity.resource.attribute.labels[rdside_labelSelector_matchExp_key]
resource.data.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.operator
entity.resource.attribute.labels[rdside_labelSelector_matchExp_operator]
resource.data.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.labelSelector.matchExpressions.values
entity.resource.attribute.labels[rdside_labelSelector_matchExp_values]
resource.data.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.key
entity.resource.attribute.labels[rdside_nodeSelector_matchFields_key]
resource.data.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.operator
entity.resource.attribute.labels[rdside_nodeSelector_matchFields_operator]
resource.data.spec.affinity.nodeAffinity.requiredDuringSchedulingIgnoredDuringExecution.nodeSelectorTerms.matchFields.values
entity.resource.attribute.labels[rdside_nodeSelector_matchFields_values]
resource.data.spec.affinity.podAntiAffinity.requiredDuringSchedulingIgnoredDuringExecution.topologyKey
entity.resource.attribute.labels[rdside_topologykey]
resource.data.name
entity.resource.attribute.labels[resource_name]
resource.data.resourceLabels.goog-composer-environment-uuid
entity.resource.attribute.labels[resourceLabels_goog-composer-environment-uuid]
resource.data.resourceLabels.goog-composer-environment
entity.resource.attribute.labels[resourceLabels_goog-composer-environment]
resource.data.resourceLabels.goog-composer-location
entity.resource.attribute.labels[resourceLabels_goog-composer-location]
resource.data.resourceLabels.goog-composer-version
entity.resource.attribute.labels[resourceLabels_goog-composer-version]
resource.data.resourceLabels.label
entity.resource.attribute.labels[resourceLabels_label]
resource.data.roleRef.apiGroup
entity.resource.attribute.labels[roleRef_apiGroup]
resource.data.roleRef.kind
entity.resource.attribute.labels[roleRef_kind]
resource.data.spec.selector.matchLabels.pod-template-hash
entity.resource.attribute.labels[selector_matchLabels_pod-template-hash]
resource.data.servicesIpv4Cidr
entity.resource.attribute.labels[servicesIpv4Cidr]
resource.data.shieldedNodes.enabled
entity.resource.attribute.labels[shieldedNodes_enabled]
resource.data.spec.activeDeadlineSeconds
entity.resource.attribute.labels[spec_activeDeadlineSeconds]
resource.data.spec.backoffLimit
entity.resource.attribute.labels[spec_backoffLimit]
resource.data.spec.clusterIP
entity.resource.attribute.labels[spec_clusterIP]
resource.data.spec.completionMode
entity.resource.attribute.labels[spec_completionMode]
resource.data.spec.completions
entity.resource.attribute.labels[spec_completions]
resource.data.spec.enableServiceLinks
entity.resource.attribute.labels[spec_enableServiceLinks]
resource.data.spec.externalID
entity.resource.attribute.labels[spec_externalID]
resource.data.spec.externalName
entity.resource.attribute.labels[spec_externalName]
resource.data.spec.finalizers
entity.resource.attribute.labels[spec_finalizers]
resource.data.spec.healthCheckNodePort
entity.resource.attribute.labels[spec_healthCheckNodePort]
resource.data.spec.hostIPC
entity.resource.attribute.labels[spec_hostIPC]
resource.data.spec.hostNetwork
entity.resource.attribute.labels[spec_hostNetwork]
resource.data.spec.hostPID
entity.resource.attribute.labels[spec_hostPID]
resource.data.spec.minReadySeconds
entity.resource.attribute.labels[spec_minReadySeconds]
resource.data.spec.nodeName
entity.resource.attribute.labels[spec_nodeName]
resource.data.spec.nodeSelector.addon.gke.io/node-local-dns-ds-ready
entity.resource.attribute.labels[spec_nodeSelector_addon_gke.io/node-local-dns-ds-ready]
resource.data.spec.nodeSelector.cloud.google.com/gke-netd-ready
entity.resource.attribute.labels[spec_nodeSelector_cloud_google_com/gke-netd-ready]
resource.data.spec.nodeSelector.iam.gke.io/gke-metadata-server-enabled
entity.resource.attribute.labels[spec_nodeSelector_iam_gke.io/gke-metadata-server-enabled]
resource.data.spec.nodeSelector.node.kubernetes.io/masq-agent-ds-ready
entity.resource.attribute.labels[spec_nodeSelector_node_kubernetes.io/masq-agent-ds-ready]
resource.data.spec.parallelism
entity.resource.attribute.labels[spec_parallelism]
resource.data.spec.paused
entity.resource.attribute.labels[spec_paused]
resource.data.spec.ports.name
entity.resource.attribute.labels[spec_ports_name]
resource.data.spec.ports.nodePort
entity.resource.attribute.labels[spec_ports_nodePort]
resource.data.spec.ports.port
entity.resource.attribute.labels[spec_ports_port]
resource.data.spec.ports.protocol
entity.resource.attribute.labels[spec_ports_protocol]
resource.data.spec.ports.targetPort
entity.resource.attribute.labels[spec_ports_targetPort]
resource.data.spec.progressDeadlineSeconds
entity.resource.attribute.labels[spec_progressDeadlineSeconds]
resource.data.spec.publishNotReadyAddresses
entity.resource.attribute.labels[spec_publishNotReadyAddresses]
resource.data.spec.replicas
entity.resource.attribute.labels[spec_replicas]
resource.data.spec.revisionHistoryLimit
entity.resource.attribute.labels[spec_revisionHistoryLimit]
resource.data.spec.schedulerName
entity.resource.attribute.labels[spec_schedulerName]
resource.data.spec.securityContext.fsGroup
entity.resource.attribute.labels[spec_securityContext_fsGroup]
resource.data.spec.securityContext.runAsGroup
entity.resource.attribute.labels[spec_securityContext_runAsGroup]
resource.data.spec.securityContext.runAsNonRoot
entity.resource.attribute.labels[spec_securityContext_runAsNonRoot]
resource.data.spec.securityContext.runAsUser
entity.resource.attribute.labels[spec_securityContext_runAsUser]
resource.data.spec.securityContext.supplementalGroups
entity.resource.attribute.labels[spec_securityContext_supplementalGroups]
resource.data.spec.selector.app
entity.resource.attribute.labels[spec_selector_app]
resource.data.spec.selector.k8s-app
entity.resource.attribute.labels[spec_selector_k8s-app]
resource.data.spec.selector.matchLabels.app
entity.resource.attribute.labels[spec_selector_matchLabels_app]
resource.data.spec.selector.matchLabels.component
entity.resource.attribute.labels[spec_selector_matchLabels_component]
resource.data.spec.selector.matchLabels.control-plane
entity.resource.attribute.labels[spec_selector_matchLabels_control-plane]
resource.data.spec.selector.matchLabels.controller-uid
entity.resource.attribute.labels[spec_selector_matchLabels_controller-uid]
resource.data.spec.selector.matchLabels.gke-app
entity.resource.attribute.labels[spec_selector_matchLabels_gke-app]
resource.data.spec.selector.matchLabels.k8s-app
entity.resource.attribute.labels[spec_selector_matchLabels_k8s-app]
resource.data.spec.selector.matchLabels.run
entity.resource.attribute.labels[spec_selector_matchLabels_run]
resource.data.spec.selector.matchLabels.version
entity.resource.attribute.labels[spec_selector_matchLabels_version]
resource.data.spec.selector.run
entity.resource.attribute.labels[spec_selector_run]
resource.data.spec.sessionAffinity
entity.resource.attribute.labels[spec_sessionAffinity]
resource.data.spec.strategy.rollingUpdate.maxSurge
entity.resource.attribute.labels[spec_strategy_rollingUpdate_maxSurge]
resource.data.spec.strategy.rollingUpdate.maxUnavailable
entity.resource.attribute.labels[spec_strategy_rollingUpdate_maxUnavailable]
resource.data.spec.strategy.type
entity.resource.attribute.labels[spec_strategy_type]
resource.data.spec.subdomain
entity.resource.attribute.labels[spec_subdomain]
resource.data.spec.suspend
entity.resource.attribute.labels[spec_suspend]
resource.data.spec.template.metadata.annotations.components.gke.io/component-name
entity.resource.attribute.labels[spec_template_metadata_annotations_components_gke.io/component-name]
resource.data.spec.template.metadata.annotations.components.gke.io/component-version
entity.resource.attribute.labels[spec_template_metadata_annotations_components_gke.io/component-version]
resource.data.spec.template.metadata.annotations.prometheus.io/port
entity.resource.attribute.labels[spec_template_metadata_annotations_prometheus.io/port]
resource.data.spec.template.metadata.annotations.prometheus.io/scrape
entity.resource.attribute.labels[spec_template_metadata_annotations_prometheus.io/scrape]
resource.data.spec.template.metadata.annotations.scheduler.alpha.kubernetes.io/critical-pod
entity.resource.attribute.labels[spec_template_metadata_annotations_scheduler_alpha_k8s/critical-pod]
resource.data.spec.template.metadata.annotations.seccomp.security.alpha.kubernetes.io/pod
entity.resource.attribute.labels[spec_template_metadata_annotations_seccomp_sec_alpha_k8s_pod]
resource.data.spec.template.metadata.creationTimestamp
entity.resource.attribute.labels[spec_template_metadata_creationTimestamp]
resource.data.spec.template.metadata.generateName
entity.resource.attribute.labels[spec_template_metadata_generateName]
resource.data.spec.template.metadata.generation
entity.resource.attribute.labels[spec_template_metadata_generation]
resource.data.spec.template.metadata.labels.app
entity.resource.attribute.labels[spec_template_metadata_labels_app]
resource.data.spec.template.metadata.labels.component
entity.resource.attribute.labels[spec_template_metadata_labels_component]
resource.data.spec.template.metadata.labels.composer-component
entity.resource.attribute.labels[spec_template_metadata_labels_composer-component]
resource.data.spec.template.metadata.labels.composer-system-pod
entity.resource.attribute.labels[spec_template_metadata_labels_composer-system-pod]
resource.data.spec.template.metadata.labels.control-plane
entity.resource.attribute.labels[spec_template_metadata_labels_control-plane]
resource.data.spec.template.metadata.labels.controller-uid
entity.resource.attribute.labels[spec_template_metadata_labels_controller-uid]
resource.data.spec.template.metadata.labels.gke-app
entity.resource.attribute.labels[spec_template_metadata_labels_gke-app]
resource.data.spec.template.metadata.labels.job-name
entity.resource.attribute.labels[spec_template_metadata_labels_job-name]
resource.data.spec.template.metadata.labels.k8s-app
entity.resource.attribute.labels[spec_template_metadata_labels_k8s-app]
resource.data.spec.template.metadata.labels.kubernetes.io/cluster-service
entity.resource.attribute.labels[spec_template_metadata_labels_kubernetes.io/cluster-service]
resource.data.spec.template.metadata.labels.name
entity.resource.attribute.labels[spec_template_metadata_labels_name]
resource.data.spec.template.metadata.labels.run
entity.resource.attribute.labels[spec_template_metadata_labels_run]
resource.data.spec.template.metadata.labels.version
entity.resource.attribute.labels[spec_template_metadata_labels_version]
resource.data.spec.template.metadata.name
entity.resource.attribute.labels[spec_template_metadata_name]
resource.data.spec.template.metadata.namespace
entity.resource.attribute.labels[spec_template_metadata_namespace]
resource.data.spec.template.metadata.resourceVersion
entity.resource.attribute.labels[spec_template_metadata_resourceVersion]
resource.data.spec.template.metadata.selfLink
entity.resource.attribute.labels[spec_template_metadata_selfLink]
resource.data.spec.template.metadata.uid
entity.resource.attribute.labels[spec_template_metadata_uid]
resource.data.spec.template.spec.hostIPC
entity.resource.attribute.labels[spec_template_spec_hostIPC]
resource.data.spec.template.spec.hostname
entity.resource.attribute.labels[spec_template_spec_hostname]
resource.data.spec.template.spec.hostNetwork
entity.resource.attribute.labels[spec_template_spec_hostNetwork]
resource.data.spec.template.spec.hostPID
entity.resource.attribute.labels[spec_template_spec_hostPID]
resource.data.spec.template.spec.nodeName
entity.resource.attribute.labels[spec_template_spec_nodeName]
resource.data.spec.template.spec.nodeSelector.beta.kubernetes.io/os
entity.resource.attribute.labels[spec_template_spec_nodeSelector_beta_kubernetes.io/os]
resource.data.spec.template.spec.nodeSelector.kubernetes.io/os
entity.resource.attribute.labels[spec_template_spec_nodeSelector_kubernetes.io/os]
resource.data.spec.template.spec.priorityClassName
entity.resource.attribute.labels[spec_template_spec_priorityClassName]
resource.data.spec.template.spec.schedulerName
entity.resource.attribute.labels[spec_template_spec_schedulerName]
resource.data.spec.template.spec.securityContext.fsGroup
entity.resource.attribute.labels[spec_template_spec_securityContext_fsGroup]
resource.data.spec.template.spec.securityContext.runAsGroup
entity.resource.attribute.labels[spec_template_spec_securityContext_runAsGroup]
resource.data.spec.template.spec.securityContext.runAsUser
entity.resource.attribute.labels[spec_template_spec_securityContext_runAsUser]
resource.data.spec.template.spec.securityContext.supplementalGroups
entity.resource.attribute.labels[spec_template_spec_securityContext_supplementalGroups]
resource.data.spec.template.spec.serviceAccount
entity.resource.attribute.labels[spec_template_spec_serviceAccount]
resource.data.spec.template.spec.serviceAccountName
entity.resource.attribute.labels[spec_template_spec_serviceAccountName]
resource.data.spec.template.spec.subdomain
entity.resource.attribute.labels[spec_template_spec_subdomain]
resource.data.spec.template.spec.terminationGracePeriodSeconds
entity.resource.attribute.labels[spec_template_spec_terminationGracePeriodSeconds]
resource.data.spec.template.spec.tolerations.effect
entity.resource.attribute.labels[spec_template_spec_tolerations_effect]
resource.data.spec.template.spec.tolerations.key
entity.resource.attribute.labels[spec_template_spec_tolerations_key]
resource.data.spec.template.spec.tolerations.operator
entity.resource.attribute.labels[spec_template_spec_tolerations_operator]
resource.data.spec.template.spec.tolerations.value
entity.resource.attribute.labels[spec_template_spec_tolerations_value]
resource.data.spec.template.spec.topologySpreadConstraints.labelSelector.matchLabels.k8s-app
entity.resource.attribute.labels[spec_template_spec_topology_matchLabels_k8s-app]
resource.data.spec.template.spec.topologySpreadConstraints.maxSkew
entity.resource.attribute.labels[spec_template_spec_topologySpreadConstraints_maxSkew]
resource.data.spec.template.spec.topologySpreadConstraints.topologyKey
entity.resource.attribute.labels[spec_template_spec_topology_topologyKey]
resource.data.spec.template.spec.topologySpreadConstraints.whenUnsatisfiable
entity.resource.attribute.labels[spec_template_spec_topologyConst_whenUnsatisfiable]
resource.data.spec.terminationGracePeriodSeconds
entity.resource.attribute.labels[spec_terminationGracePeriodSeconds]
resource.data.spec.tolerations.effect
entity.resource.attribute.labels[spec_tolerations_effect]
resource.data.spec.tolerations.key
entity.resource.attribute.labels[spec_tolerations_key]
resource.data.spec.tolerations.operator
entity.resource.attribute.labels[spec_tolerations_operator]
resource.data.spec.tolerations.tolerationSeconds
entity.resource.attribute.labels[spec_tolerations_tolerationSeconds]
resource.data.spec.tolerations.value
entity.resource.attribute.labels[spec_tolerations_value]
resource.data.spec.topologySpreadConstraints.labelSelector.matchLabels.k8s-app
entity.resource.attribute.labels[spec_topologySpreadConstraints_labelSelector_matchLabels_k8s-app]
resource.data.spec.topologySpreadConstraints.maxSkew
entity.resource.attribute.labels[spec_topologySpreadConstraints_maxSkew]
resource.data.spec.topologySpreadConstraints.topologyKey
entity.resource.attribute.labels[spec_topologySpreadConstraints_topologyKey]
resource.data.spec.topologySpreadConstraints.whenUnsatisfiable
entity.resource.attribute.labels[spec_topologySpreadConstraints_whenUnsatisfiable]
resource.data.spec.type
entity.resource.attribute.labels[spec_type]
resource.data.spec.unschedulable
entity.resource.attribute.labels[spec_unschedulable]
resource.data.status.active
entity.resource.attribute.labels[status_active]
resource.data.status.addresses.address
entity.resource.attribute.labels[status_addresses_address]
resource.data.status.addresses.type
entity.resource.attribute.labels[status_addresses_address]
resource.data.status.allocatable.attachable-volumes-gce-pd
entity.resource.attribute.labels[status_allocatable_attachable-volumes-gce-pd]
resource.data.status.allocatable.cpu
entity.resource.attribute.labels[status_allocatable_cpu]
resource.data.status.allocatable.ephemeral-storage
entity.resource.attribute.labels[status_allocatable_ephemeral-storage]
resource.data.status.allocatable.hugepages-1Gi
entity.resource.attribute.labels[status_allocatable_hugepages-1Gi]
resource.data.status.allocatable.hugepages-2Mi
entity.resource.attribute.labels[status_allocatable_hugepages-2Mi]
resource.data.status.allocatable.memory
entity.resource.attribute.labels[status_allocatable_memory]
resource.data.status.allocatable.pods
entity.resource.attribute.labels[status_allocatable_pods]
resource.data.status.availableReplicas
entity.resource.attribute.labels[status_availableReplicas]
resource.data.status.capacity.attachable-volumes-gce-pd
entity.resource.attribute.labels[status_capacity_attachable-volumes-gce-pd]
resource.data.status.capacity.cpu
entity.resource.attribute.labels[status_capacity_cpu]
resource.data.status.capacity.ephemeral-storage
entity.resource.attribute.labels[status_capacity_ephemeral-storage]
resource.data.status.capacity.hugepages-1Gi
entity.resource.attribute.labels[status_capacity_hugepages-1Gi]
resource.data.status.capacity.hugepages-2Mi
entity.resource.attribute.labels[status_capacity_hugepages-2Mi]
resource.data.status.capacity.memory
entity.resource.attribute.labels[status_capacity_memory]
resource.data.status.capacity.pods
entity.resource.attribute.labels[status_capacity_pods]
resource.data.status.completedIndexes
entity.resource.attribute.labels[status_completedIndexes]
resource.data.status.completionTime
entity.resource.attribute.labels[status_completionTime]
resource.data.status.conditions.lastProbeTime
entity.resource.attribute.labels[status_conditions_lastProbeTime]
resource.data.status.conditions.lastTransitionTime
entity.resource.attribute.labels[status_conditions_lastTransitionTime]
resource.data.status.conditions.lastUpdateTime
entity.resource.attribute.labels[status_conditions_lastUpdateTime]
resource.data.status.conditions.message
entity.resource.attribute.labels[status_conditions_message]
resource.data.status.conditions.reason
entity.resource.attribute.labels[status_conditions_reason]
resource.data.status.conditions.status
entity.resource.attribute.labels[status_conditions_status]
resource.data.status.conditions.type
entity.resource.attribute.labels[status_conditions_type]
resource.data.status.daemonEndpoints.kubeletEndpoint.Port
entity.resource.attribute.labels[status_daemonEndpoints_kubeletEndpoint_Port]
resource.data.status.failed
entity.resource.attribute.labels[status_failed]
resource.data.status.fullyLabeledReplicas
entity.resource.attribute.labels[status_fullyLabeledReplicas]
resource.data.status.images.names
entity.resource.attribute.labels[status_images_names]
resource.data.status.images.sizeBytes
entity.resource.attribute.labels[status_images_sizeBytes]
resource.data.status.message
entity.resource.attribute.labels[status_message]
resource.data.status.nodeInfo.architecture
entity.resource.attribute.labels[status_nodeInfo_architecture]
resource.data.status.nodeInfo.bootID
entity.resource.attribute.labels[status_nodeInfo_bootID]
resource.data.status.nodeInfo.containerRuntimeVersion
entity.resource.attribute.labels[status_nodeInfo_containerRuntimeVersion]
resource.data.status.nodeInfo.kernelVersion
entity.resource.attribute.labels[status_nodeInfo_kernelVersion]
resource.data.status.nodeInfo.kubeletVersion
entity.resource.attribute.labels[status_nodeInfo_kubeletVersion]
resource.data.status.nodeInfo.kubeProxyVersion
entity.resource.attribute.labels[status_nodeInfo_kubeProxyVersion]
resource.data.status.nodeInfo.machineID
entity.resource.attribute.labels[status_nodeInfo_machineID]
resource.data.status.nodeInfo.osImage
entity.resource.attribute.labels[status_nodeInfo_osImage]
resource.data.status.nominatedNodeName
entity.resource.attribute.labels[status_nominatedNodeName]
resource.data.status.observedGeneration
entity.resource.attribute.labels[status_observedGeneration]
resource.data.status.phase
entity.resource.attribute.labels[status_phase]
resource.data.status.podIP
entity.resource.attribute.labels[status_podIP]
resource.data.status.podIPs.ip
entity.resource.attribute.labels[status_podIPs_ip]
resource.data.status.qosClass
entity.resource.attribute.labels[status_qosClass]
resource.data.status.ready
entity.resource.attribute.labels[status_ready]
resource.data.status.readyReplicas
entity.resource.attribute.labels[status_readyReplicas]
resource.data.status.reason
entity.resource.attribute.labels[status_reason]
resource.data.status.replicas
entity.resource.attribute.labels[status_replicas]
resource.data.status.startTime
entity.resource.attribute.labels[status_startTime]
resource.data.status.succeeded
entity.resource.attribute.labels[status_succeeded]
resource.data.status.unavailableReplicas
entity.resource.attribute.labels[status_unavailableReplicas]
resource.data.status.updatedReplicas
entity.resource.attribute.labels[status_updatedReplicas]
resource.data.status.volumesAttached.devicePath
entity.resource.attribute.labels[status_volumesAttached_devicePath]
resource.data.status.volumesAttached.name
entity.resource.attribute.labels[status_volumesAttached_name]
resource.data.status.volumesInUse
entity.resource.attribute.labels[status_volumesInUse]
resource.data.status
entity.resource.attribute.labels[status]
resource.data.subjects.apiGroup
entity.resource.attribute.labels[subjects_apiGroup]
resource.data.subjects.kind
entity.resource.attribute.labels[subjects_kind]
resource.data.subjects.name
entity.resource.attribute.labels[subjects_name]
resource.data.subjects.namespace
entity.resource.attribute.labels[subjects_namespace]
resource.data.subnetwork
entity.resource.attribute.labels[subnetwork]
resource.data.spec.template.metadata.labels.pod-template-hash
entity.resource.attribute.labels[template_metadata_labels_pod-template-hash]
resource.data.upgradeSettings.maxSurge
entity.resource.attribute.labels[upgradeSettings_maxSurge]
resource.data.upgradeSettings.strategy
entity.resource.attribute.labels[upgradeSettings_strategy]
resource.data.version
entity.resource.attribute.labels[version]
resource.data.verticalPodAutoscaling.enabled
entity.resource.attribute.labels[verticalPodAutoscaling_enabled]
resource.data.workloadIdentityConfig.workloadPool
entity.resource.attribute.labels[workloadIdentityConfig_workloadPool]
resource.data.rules.apiGroups
entity.security_result.rule_labels[apiGroups]
resource.data.autoscaling.locationPolicy
entity.security_result.rule_labels[autoscaling_locationPolicy]
resource.data.maintenancePolicy.resourceVersion
entity.security_result.rule_labels[maintenancePolicy_resourceVersion]
resource.data.maintenancePolicy.window.recurringWindow.recurrence
entity.security_result.rule_labels[maintenancePolicy_window_recurringWindow_recurrence]
resource.data.maintenancePolicy.window.recurringWindow.window.endTime
entity.security_result.rule_labels[maintenancePolicy_window_recurringWindow_window_endTime]
resource.data.maintenancePolicy.window.recurringWindow.window.startTime
entity.security_result.rule_labels[maintenancePolicy_window_recurringWindow_window_startTime]
resource.data.metadata.annotations.EnablePodSecurityPolicy
entity.security_result.rule_labels[metadata_annotations_EnablePodSecurityPolicy]
resource.data.nodePools.autoscaling.locationPolicy
entity.security_result.rule_labels[nodePools_autoscaling_locationPolicy]
resource.data.rules.nonResourceURLs
entity.security_result.rule_labels[nonResourceURLs]
resource.data.rules.resourceNames
entity.security_result.rule_labels[resourceNames]
resource.data.rules.resources
entity.security_result.rule_labels[resources]
resource.data.spec.dnsPolicy
entity.security_result.rule_labels[spec_dnsPolicy]
resource.data.spec.externalTrafficPolicy
entity.security_result.rule_labels[spec_externalTrafficPolicy]
resource.data.spec.preemptionPolicy
entity.security_result.rule_labels[spec_preemptionPolicy]
resource.data.spec.restartPolicy
entity.security_result.rule_labels[spec_restartPolicy]
resource.data.spec.template.spec.dnsPolicy
entity.security_result.rule_labels[spec_template_spec_dnsPolicy]
resource.data.spec.template.spec.restartPolicy
entity.security_result.rule_labels[spec_template_spec_restartPolicy]
resource.data.rules.verbs
entity.security_result.rule_labels[verbs]
resource.data.spec.serviceAccount
entity.user.attribute.labels[spec_serviceAccount]
resource.data.spec.containers.ports.containerPort
relations.entity.resource.attribute.labels[spec_containers_ports_containerPort]
resource.data.spec.initContainers.imagePullPolicy
relations.entity.security_result.rule_labels[spec_initContainers_imagePullPolicy]
resource.data.metadata.ownerReferences.apiVersion
relations.entity.resource.attribute.labels[metadata_ownerReferences_apiVersion]
resource.data.metadata.ownerReferences.blockOwnerDeletion
relations.entity.resource.attribute.labels[metadata_ownerReferences_blockOwnerDeletion]
resource.data.metadata.ownerReferences.controller
relations.entity.resource.attribute.labels[metadata_ownerReferences_controller]
resource.data.metadata.ownerReferences.kind
relations.entity.resource.attribute.labels[metadata_ownerReferences_kind]
resource.data.metadata.ownerReferences.uid
relations.entity.resource.attribute.labels[metadata_ownerReferences_uid]
resource.data.spec.containers.args
relations.entity.resource.attribute.labels[spec_containers_args]
resource.data.spec.containers.command
relations.entity.resource.attribute.labels[spec_containers_command]
resource.data.spec.containers.env.name
relations.entity.resource.attribute.labels[spec_containers_env_name]
resource.data.spec.containers.env.value
relations.entity.resource.attribute.labels[spec_containers_env_value]
resource.data.spec.containers.env.valueFrom.configMapKeyRef.key
relations.entity.resource.attribute.labels[spec_containers_env_valueFrom_configMapKeyRef_key]
resource.data.spec.containers.env.valueFrom.configMapKeyRef.name
relations.entity.resource.attribute.labels[spec_containers_env_valueFrom_configMapKeyRef_name]
resource.data.spec.containers.env.valueFrom.fieldRef.apiVersion
relations.entity.resource.attribute.labels[spec_containers_env_valueFrom_fieldRef_apiVersion]
resource.data.spec.containers.env.valueFrom.fieldRef.fieldPath
relations.entity.resource.attribute.labels[spec_containers_env_valueFrom_fieldRef_fieldPath]
resource.data.spec.containers.env.valueFrom.secretKeyRef.key
relations.entity.resource.attribute.labels[spec_containers_env_valueFrom_secretKeyRef_key]
resource.data.spec.containers.env.valueFrom.secretKeyRef.localObjectReference.name
relations.entity.resource.attribute.labels[spec_containers_env_valueFrom_secretKeyRef_localObjRef_name]
resource.data.spec.containers.image
relations.entity.resource.attribute.labels[spec_containers_image]
resource.data.spec.containers.lifecycle.postStart.exec.command
relations.entity.resource.attribute.labels[spec_containers_lifecycle_postStart_exec_command]
resource.data.spec.containers.lifecycle.preStop.exec.command
relations.entity.resource.attribute.labels[spec_containers_lifecycle_preStop_exec_command]
resource.data.spec.containers.livenessProbe.failureThreshold
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_failureThreshold]
resource.data.spec.containers.livenessProbe.handler.exec.command
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_exec_command]
resource.data.spec.containers.livenessProbe.handler.httpGet.host
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_httpGet_host]
resource.data.spec.containers.livenessProbe.handler.httpGet.httpHeaders.name
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_httpGet_httpHeaders_name]
resource.data.spec.containers.livenessProbe.handler.httpGet.httpHeaders.value
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_httpGet_httpHeaders_value]
resource.data.spec.containers.livenessProbe.handler.httpGet.path
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_httpGet_path]
resource.data.spec.containers.livenessProbe.handler.httpGet.port
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_httpGet_port]
resource.data.spec.containers.livenessProbe.handler.httpGet.scheme
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_httpGet_scheme]
resource.data.spec.containers.livenessProbe.handler.tcpSocket.host
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_tcpSocket_host]
resource.data.spec.containers.livenessProbe.handler.tcpSocket.port
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_handler_tcpSocket_port]
resource.data.spec.containers.livenessProbe.initialDelaySeconds
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_initialDelaySeconds]
resource.data.spec.containers.livenessProbe.periodSeconds
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_periodSeconds]
resource.data.spec.containers.livenessProbe.successThreshold
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_successThreshold]
resource.data.spec.containers.livenessProbe.timeoutSeconds
relations.entity.resource.attribute.labels[spec_containers_livenessProbe_timeoutSeconds]
resource.data.spec.containers.ports.hostIP
relations.entity.resource.attribute.labels[spec_containers_ports_hostIP]
resource.data.spec.containers.ports.hostPort
relations.entity.resource.attribute.labels[spec_containers_ports_hostPort]
resource.data.spec.containers.ports.name
relations.entity.resource.attribute.labels[spec_containers_ports_name]
resource.data.spec.containers.readinessProbe.failureThreshold
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_failureThreshold]
resource.data.spec.containers.readinessProbe.handler.httpGet.host
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_handler_httpGet_host]
resource.data.spec.containers.readinessProbe.handler.httpGet.httpHeaders.name
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_handler_httpGet_httpHeaders_name]
resource.data.spec.containers.readinessProbe.handler.httpGet.httpHeaders.value
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_handler_httpGet_httpHeaders_value]
resource.data.spec.containers.readinessProbe.handler.httpGet.path
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_handler_httpGet_path]
resource.data.spec.containers.readinessProbe.handler.httpGet.port
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_handler_httpGet_port]
resource.data.spec.containers.readinessProbe.handler.httpGet.scheme
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_handler_httpGet_scheme]
resource.data.spec.containers.readinessProbe.initialDelaySeconds
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_initialDelaySeconds]
resource.data.spec.containers.readinessProbe.periodSeconds
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_periodSeconds]
resource.data.spec.containers.readinessProbe.successThreshold
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_successThreshold]
resource.data.spec.containers.readinessProbe.timeoutSeconds
relations.entity.resource.attribute.labels[spec_containers_readinessProbe_timeoutSeconds]
resource.data.spec.containers.resources.limits.cpu
relations.entity.resource.attribute.labels[spec_containers_resources_limits_cpu]
resource.data.spec.containers.resources.limits.ephemeral-storage
relations.entity.resource.attribute.labels[spec_containers_resources_limits_ephemeral-storage]
resource.data.spec.containers.resources.limits.memory
relations.entity.resource.attribute.labels[spec_containers_resources_limits_memory]
resource.data.spec.containers.resources.requests.cpu
relations.entity.resource.attribute.labels[spec_containers_resources_requests_cpu]
resource.data.spec.containers.resources.requests.ephemeral-storage
relations.entity.resource.attribute.labels[spec_containers_resources_requests_ephemeral-storage]
resource.data.spec.containers.resources.requests.memory
relations.entity.resource.attribute.labels[spec_containers_resources_requests_memory]
resource.data.spec.containers.securityContext.allowPrivilegeEscalation
relations.entity.resource.attribute.labels[spec_containers_securityContext_allowPrivilegeEscalation]
resource.data.spec.containers.securityContext.capabilities.add
relations.entity.resource.attribute.labels[spec_containers_securityContext_capabilities_add]
resource.data.spec.containers.securityContext.capabilities.drop
relations.entity.resource.attribute.labels[spec_containers_securityContext_capabilities_drop]
resource.data.spec.containers.securityContext.privileged
relations.entity.resource.attribute.labels[spec_containers_securityContext_privileged]
resource.data.spec.containers.securityContext.readOnlyRootFilesystem
relations.entity.resource.attribute.labels[spec_containers_securityContext_readOnlyRootFilesystem]
resource.data.spec.containers.securityContext.runAsGroup
relations.entity.resource.attribute.labels[spec_containers_securityContext_runAsGroup]
resource.data.spec.containers.securityContext.runAsNonRoot
relations.entity.resource.attribute.labels[spec_containers_securityContext_runAsNonRoot]
resource.data.spec.containers.securityContext.runAsUser
relations.entity.resource.attribute.labels[spec_containers_securityContext_runAsUser]
resource.data.spec.containers.startupProbe.failureThreshold
relations.entity.resource.attribute.labels[spec_containers_startupProbe_failureThreshold]
resource.data.spec.containers.startupProbe.handler.exec.command
relations.entity.resource.attribute.labels[spec_containers_startupProbe_handler_exec_command]
resource.data.spec.containers.startupProbe.initialDelaySeconds
relations.entity.resource.attribute.labels[spec_containers_startupProbe_initialDelaySeconds]
resource.data.spec.containers.startupProbe.periodSeconds
relations.entity.resource.attribute.labels[spec_containers_startupProbe_periodSeconds]
resource.data.spec.containers.startupProbe.successThreshold
relations.entity.resource.attribute.labels[spec_containers_startupProbe_successThreshold]
resource.data.spec.containers.startupProbe.timeoutSeconds
relations.entity.resource.attribute.labels[spec_containers_startupProbe_timeoutSeconds]
resource.data.spec.containers.stdin
relations.entity.resource.attribute.labels[spec_containers_stdin]
resource.data.spec.containers.stdinOnce
relations.entity.resource.attribute.labels[spec_containers_stdinOnce]
resource.data.spec.containers.terminationMessagePath
relations.entity.resource.attribute.labels[spec_containers_terminationMessagePath]
resource.data.spec.containers.tty
relations.entity.resource.attribute.labels[spec_containers_tty]
resource.data.spec.containers.volumeMounts.mountPath
relations.entity.resource.attribute.labels[spec_containers_volumeMounts_mountPath]
resource.data.spec.containers.volumeMounts.mountPropagation
relations.entity.resource.attribute.labels[spec_containers_volumeMounts_mountPropagation]
resource.data.spec.containers.volumeMounts.name
relations.entity.resource.attribute.labels[spec_containers_volumeMounts_name]
resource.data.spec.containers.volumeMounts.readOnly
relations.entity.resource.attribute.labels[spec_containers_volumeMounts_readOnly]
resource.data.spec.containers.volumeMounts.subPath
relations.entity.resource.attribute.labels[spec_containers_volumeMounts_subPath]
resource.data.spec.containers.volumeMounts.subPathExpr
relations.entity.resource.attribute.labels[spec_containers_volumeMounts_subPathExpr]
resource.data.spec.initContainers.command
relations.entity.resource.attribute.labels[spec_initContainers_command]
resource.data.spec.initContainers.env.name
relations.entity.resource.attribute.labels[spec_initContainers_env_name]
resource.data.spec.initContainers.env.value
relations.entity.resource.attribute.labels[spec_initContainers_env_value]
resource.data.spec.initContainers.env.valueFrom.configMapKeyRef.key
relations.entity.resource.attribute.labels[spec_initContainers_env_valueFrom_configMapKeyRef_key]
resource.data.spec.initContainers.env.valueFrom.configMapKeyRef.name
relations.entity.resource.attribute.labels[spec_initContainers_env_valueFrom_configMapKeyRef_name]
resource.data.spec.initContainers.image
relations.entity.resource.attribute.labels[spec_initContainers_image]
resource.data.spec.initContainers.resources.requests.cpu
relations.entity.resource.attribute.labels[spec_initContainers_resources_requests_cpu]
resource.data.spec.initContainers.resources.requests.memory
relations.entity.resource.attribute.labels[spec_initContainers_resources_requests_memory]
resource.data.spec.initContainers.securityContext.capabilities.add
relations.entity.resource.attribute.labels[spec_initContainers_securityContext_capabilities_add]
resource.data.spec.initContainers.securityContext.privileged
relations.entity.resource.attribute.labels[spec_initContainers_securityContext_privileged]
resource.data.spec.initContainers.stdin
relations.entity.resource.attribute.labels[spec_initContainers_stdin]
resource.data.spec.initContainers.stdinOnce
relations.entity.resource.attribute.labels[spec_initContainers_stdinOnce]
resource.data.spec.initContainers.terminationMessagePath
relations.entity.resource.attribute.labels[spec_initContainers_terminationMessagePath]
resource.data.spec.initContainers.tty
relations.entity.resource.attribute.labels[spec_initContainers_tty]
resource.data.spec.initContainers.volumeMounts.mountPath
relations.entity.resource.attribute.labels[spec_initContainers_volumeMounts_mountPath]
resource.data.spec.initContainers.volumeMounts.mountPropagation
relations.entity.resource.attribute.labels[spec_initContainers_volumeMounts_mountPropagation]
resource.data.spec.initContainers.volumeMounts.name
relations.entity.resource.attribute.labels[spec_initContainers_volumeMounts_name]
resource.data.spec.initContainers.volumeMounts.readOnly
relations.entity.resource.attribute.labels[spec_initContainers_volumeMounts_readOnly]
resource.data.spec.initContainers.volumeMounts.subPath
relations.entity.resource.attribute.labels[spec_initContainers_volumeMounts_subPath]
resource.data.spec.initContainers.volumeMounts.subPathExpr
relations.entity.resource.attribute.labels[spec_initContainers_volumeMounts_subPathExpr]
resource.data.spec.podCIDR
entity.resource.attribute.labels[spec_podCIDR]
resource.data.spec.template.spec.containers.args
relations.entity.resource.attribute.labels[sts_containers_args]
resource.data.spec.template.spec.containers.command
relations.entity.resource.attribute.labels[sts_containers_command]
resource.data.spec.template.spec.containers.env.name
relations.entity.resource.attribute.labels[sts_containers_env_name]
resource.data.spec.template.spec.containers.env.value
relations.entity.resource.attribute.labels[sts_containers_env_value]
resource.data.spec.template.spec.containers.env.valueFrom.fieldRef.apiVersion
relations.entity.resource.attribute.labels[sts_containers_env_valueFrom_fieldRef_apiVersion]
resource.data.spec.template.spec.containers.env.valueFrom.fieldRef.fieldPath
relations.entity.resource.attribute.labels[sts_containers_env_valueFrom_fieldRef_fieldPath]
resource.data.spec.template.spec.containers.env.valueFrom.secretKeyRef.key
relations.entity.resource.attribute.labels[sts_containers_env_valueFrom_secretKeyRef_key]
resource.data.spec.template.spec.containers.env.valueFrom.secretKeyRef.localObjectReference.name
relations.entity.resource.attribute.labels[sts_containers_env_valueFrom_secretKeyRef_localObjRef_name]
resource.data.spec.template.spec.containers.image
relations.entity.resource.attribute.labels[sts_containers_image]
resource.data.spec.template.spec.containers.lifecycle.preStop.exec.command
relations.entity.resource.attribute.labels[sts_containers_lifecycle_preStop_exec_command]
resource.data.spec.template.spec.containers.livenessProbe.failureThreshold
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_failureThreshold]
resource.data.spec.template.spec.containers.livenessProbe.handler.exec.command
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_handler_exec_command]
resource.data.spec.template.spec.containers.livenessProbe.handler.httpGet.host
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_handler_httpGet_host]
resource.data.spec.template.spec.containers.livenessProbe.handler.httpGet.path
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_handler_httpGet_path]
resource.data.spec.template.spec.containers.livenessProbe.handler.httpGet.port
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_handler_httpGet_port]
resource.data.spec.template.spec.containers.livenessProbe.handler.httpGet.scheme
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_handler_httpGet_scheme]
resource.data.spec.template.spec.containers.livenessProbe.initialDelaySeconds
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_initialDelaySeconds]
resource.data.spec.template.spec.containers.livenessProbe.periodSeconds
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_periodSeconds]
resource.data.spec.template.spec.containers.livenessProbe.successThreshold
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_successThreshold]
resource.data.spec.template.spec.containers.livenessProbe.timeoutSeconds
relations.entity.resource.attribute.labels[sts_containers_livenessProbe_timeoutSeconds]
resource.data.spec.template.spec.containers.ports.containerPort
relations.entity.resource.attribute.labels[sts_containers_ports_containerPort]
resource.data.spec.template.spec.containers.ports.hostIP
relations.entity.resource.attribute.labels[sts_containers_ports_hostIP]
resource.data.spec.template.spec.containers.ports.hostPort
relations.entity.resource.attribute.labels[sts_containers_ports_hostPort]
resource.data.spec.template.spec.containers.ports.name
relations.entity.resource.attribute.labels[sts_containers_ports_name]
resource.data.spec.template.spec.containers.ports.protocol
relations.entity.resource.attribute.labels[sts_containers_ports_protocol]
resource.data.spec.template.spec.containers.readinessProbe.failureThreshold
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_failureThreshold]
resource.data.spec.template.spec.containers.readinessProbe.handler.httpGet.host
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_handler_httpGet_host]
resource.data.spec.template.spec.containers.readinessProbe.handler.httpGet.path
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_handler_httpGet_path]
resource.data.spec.template.spec.containers.readinessProbe.handler.httpGet.port
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_handler_httpGet_port]
resource.data.spec.template.spec.containers.readinessProbe.handler.httpGet.scheme
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_handler_httpGet_scheme]
resource.data.spec.template.spec.containers.readinessProbe.initialDelaySeconds
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_initialDelaySeconds]
resource.data.spec.template.spec.containers.readinessProbe.periodSeconds
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_periodSeconds]
resource.data.spec.template.spec.containers.readinessProbe.successThreshold
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_successThreshold]
resource.data.spec.template.spec.containers.readinessProbe.timeoutSeconds
relations.entity.resource.attribute.labels[sts_containers_readinessProbe_timeoutSeconds]
resource.data.spec.template.spec.containers.resources.limits.cpu
relations.entity.resource.attribute.labels[sts_containers_resources_limits_cpu]
resource.data.spec.template.spec.containers.resources.limits.ephemeral-storage
relations.entity.resource.attribute.labels[sts_containers_resources_limits_ephemeral-storage]
resource.data.spec.template.spec.containers.resources.limits.memory
relations.entity.resource.attribute.labels[sts_containers_resources_limits_memory]
resource.data.spec.template.spec.containers.resources.requests.cpu
relations.entity.resource.attribute.labels[sts_containers_resources_requests_cpu]
resource.data.spec.template.spec.containers.resources.requests.ephemeral-storage
relations.entity.resource.attribute.labels[sts_containers_resources_requests_ephemeral-storage]
resource.data.spec.template.spec.containers.resources.requests.memory
relations.entity.resource.attribute.labels[sts_containers_resources_requests_memory]
resource.data.spec.template.spec.containers.securityContext.allowPrivilegeEscalation
relations.entity.resource.attribute.labels[sts_containers_securityContext_allowPrivilegeEscalation]
resource.data.spec.template.spec.containers.securityContext.capabilities.add
relations.entity.resource.attribute.labels[sts_containers_securityContext_capabilities_add]
resource.data.spec.template.spec.containers.securityContext.capabilities.drop
relations.entity.resource.attribute.labels[sts_containers_securityContext_capabilities_drop]
resource.data.spec.template.spec.containers.securityContext.readOnlyRootFilesystem
relations.entity.resource.attribute.labels[sts_containers_securityContext_readOnlyRootFilesystem]
resource.data.spec.template.spec.containers.securityContext.runAsGroup
relations.entity.resource.attribute.labels[sts_containers_securityContext_runAsGroup]
resource.data.spec.template.spec.containers.securityContext.runAsUser
relations.entity.resource.attribute.labels[sts_containers_securityContext_runAsUser]
resource.data.spec.template.spec.containers.startupProbe.failureThreshold
relations.entity.resource.attribute.labels[sts_containers_startupProbe_failureThreshold]
resource.data.spec.template.spec.containers.startupProbe.handler.exec.command
relations.entity.resource.attribute.labels[sts_containers_startupProbe_handler_exec_command]
resource.data.spec.template.spec.containers.startupProbe.initialDelaySeconds
relations.entity.resource.attribute.labels[sts_containers_startupProbe_initialDelaySeconds]
resource.data.spec.template.spec.containers.startupProbe.periodSeconds
relations.entity.resource.attribute.labels[sts_containers_startupProbe_periodSeconds]
resource.data.spec.template.spec.containers.startupProbe.successThreshold
relations.entity.resource.attribute.labels[sts_containers_startupProbe_successThreshold]
resource.data.spec.template.spec.containers.startupProbe.timeoutSeconds
relations.entity.resource.attribute.labels[sts_containers_startupProbe_timeoutSeconds]
resource.data.spec.template.spec.containers.stdin
relations.entity.resource.attribute.labels[sts_containers_stdin]
resource.data.spec.template.spec.containers.stdinOnce
relations.entity.resource.attribute.labels[sts_containers_stdinOnce]
resource.data.spec.template.spec.containers.terminationMessagePath
relations.entity.resource.attribute.labels[sts_containers_terminationMessagePath]
resource.data.spec.template.spec.containers.tty
relations.entity.resource.attribute.labels[sts_containers_tty]
resource.data.spec.template.spec.containers.volumeMounts.mountPath
relations.entity.resource.attribute.labels[sts_containers_volumeMounts_mountPath]
resource.data.spec.template.spec.containers.volumeMounts.mountPropagation
relations.entity.resource.attribute.labels[sts_containers_volumeMounts_mountPropagation]
resource.data.spec.template.spec.containers.volumeMounts.name
relations.entity.resource.attribute.labels[sts_containers_volumeMounts_name]
resource.data.spec.template.spec.containers.volumeMounts.readOnly
relations.entity.resource.attribute.labels[sts_containers_volumeMounts_readOnly]
resource.data.spec.template.spec.containers.volumeMounts.subPath
relations.entity.resource.attribute.labels[sts_containers_volumeMounts_subPath]
resource.data.spec.template.spec.containers.volumeMounts.subPathExpr
relations.entity.resource.attribute.labels[sts_containers_volumeMounts_subPathExpr]
resource.data.spec.template.spec.initContainers.args
relations.entity.resource.attribute.labels[sts_initContainers_args]
resource.data.spec.template.spec.initContainers.command
relations.entity.resource.attribute.labels[sts_initContainers_command]
resource.data.spec.template.spec.initContainers.image
relations.entity.resource.attribute.labels[sts_initContainers_image]
resource.data.spec.template.spec.initContainers.stdin
relations.entity.resource.attribute.labels[sts_initContainers_stdin]
resource.data.spec.template.spec.initContainers.stdinOnce
relations.entity.resource.attribute.labels[sts_initContainers_stdinOnce]
resource.data.spec.template.spec.initContainers.terminationMessagePath
relations.entity.resource.attribute.labels[sts_initContainers_terminationMessagePath]
resource.data.spec.template.spec.initContainers.tty
relations.entity.resource.attribute.labels[sts_initContainers_tty]
resource.data.spec.template.spec.initContainers.volumeMounts.mountPath
relations.entity.resource.attribute.labels[sts_initContainers_volumeMounts_mountPath]
resource.data.spec.template.spec.initContainers.volumeMounts.name
relations.entity.resource.attribute.labels[sts_initContainers_volumeMounts_name]
resource.data.spec.template.spec.initContainers.volumeMounts.readOnly
relations.entity.resource.attribute.labels[sts_initContainers_volumeMounts_readOnly]
resource.data.spec.template.spec.initContainers.volumeMounts.subPath
relations.entity.resource.attribute.labels[sts_initContainers_volumeMounts_subPath]
resource.data.spec.template.spec.initContainers.volumeMounts.subPathExpr
relations.entity.resource.attribute.labels[sts_initContainers_volumeMounts_subPathExpr]
resource.data.status.containerStatuses.image
relations.entity.resource.attribute.labels[status_containerStatuses_image]
resource.data.status.containerStatuses.imageID
relations.entity.resource.attribute.labels[status_containerStatuses_imageID]
resource.data.status.containerStatuses.lastState.terminated.containerID
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_containerID]
resource.data.status.containerStatuses.lastState.terminated.exitCode
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_exitCode]
resource.data.status.containerStatuses.lastState.terminated.finishedAt
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_finishedAt]
resource.data.status.containerStatuses.lastState.terminated.message
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_message]
resource.data.status.containerStatuses.lastState.terminated.reason
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_reason]
resource.data.status.containerStatuses.lastState.terminated.signal
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_signal]
resource.data.status.containerStatuses.lastState.terminated.startedAt
relations.entity.resource.attribute.labels[status_containerStatuses_lastState_terminated_startedAt]
resource.data.status.containerStatuses.ready
relations.entity.resource.attribute.labels[status_containerStatuses_ready]
resource.data.status.containerStatuses.restartCount
relations.entity.resource.attribute.labels[status_containerStatuses_restartCount]
resource.data.status.containerStatuses.started
relations.entity.resource.attribute.labels[status_containerStatuses_started]
resource.data.status.containerStatuses.state.running.startedAt
relations.entity.resource.attribute.labels[status_containerStatuses_state_running_startedAt]
resource.data.status.containerStatuses.state.terminated.containerID
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_containerID]
resource.data.status.containerStatuses.state.terminated.exitCode
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_exitCode]
resource.data.status.containerStatuses.state.terminated.finishedAt
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_finishedAt]
resource.data.status.containerStatuses.state.terminated.message
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_message]
resource.data.status.containerStatuses.state.terminated.reason
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_reason]
resource.data.status.containerStatuses.state.terminated.signal
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_signal]
resource.data.status.containerStatuses.state.terminated.startedAt
relations.entity.resource.attribute.labels[status_containerStatuses_state_terminated_startedAt]
resource.data.status.initContainerStatuses.image
relations.entity.resource.attribute.labels[status_initContainerStatuses_image]
resource.data.status.initContainerStatuses.imageID
relations.entity.resource.attribute.labels[status_initContainerStatuses_imageID]
resource.data.status.initContainerStatuses.ready
relations.entity.resource.attribute.labels[status_initContainerStatuses_ready]
resource.data.status.initContainerStatuses.restartCount
relations.entity.resource.attribute.labels[status_initContainerStatuses_restartCount]
resource.data.status.initContainerStatuses.state.terminated.containerID
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_containerID]
resource.data.status.initContainerStatuses.state.terminated.exitCode
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_exitCode]
resource.data.status.initContainerStatuses.state.terminated.finishedAt
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_finishedAt]
resource.data.status.initContainerStatuses.state.terminated.message
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_message]
resource.data.status.initContainerStatuses.state.terminated.reason
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_reason]
resource.data.status.initContainerStatuses.state.terminated.signal
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_signal]
resource.data.status.initContainerStatuses.state.terminated.startedAt
relations.entity.resource.attribute.labels[status_initContainerStatuses_state_terminated_startedAt]
resource.data.spec.containers.imagePullPolicy
relations.entity.security_result.rule_labels[spec_containers_imagePullPolicy]
resource.data.spec.containers.terminationMessagePolicy
relations.entity.security_result.rule_labels[spec_containers_terminationMessagePolicy]
resource.data.spec.initContainers.terminationMessagePolicy
relations.entity.security_result.rule_labels[spec_initContainers_terminationMessagePolicy]
resource.data.spec.template.spec.containers.imagePullPolicy
relations.entity.security_result.rule_labels[sts_containers_imagePullPolicy]
resource.data.spec.template.spec.containers.terminationMessagePolicy
relations.entity.security_result.rule_labels[sts_containers_terminationMessagePolicy]
resource.data.spec.template.spec.initContainers.imagePullPolicy
relations.entity.security_result.rule_labels[sts_initContainers_imagePullPolicy]
resource.data.spec.template.spec.initContainers.terminationMessagePolicy
relations.entity.security_result.rule_labels[sts_initContainers_terminationMessagePolicy]
