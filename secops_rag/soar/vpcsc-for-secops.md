# Configure VPC Service Controls for Google Security Operations

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/vpcsc-for-secops/  
**Scraped:** 2026-03-05T09:46:10.157661Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure VPC Service Controls for Google Security Operations
Supported in:
Google secops
Google Cloud VPC Service Controls lets you set up a service perimeter to guard against data exfiltration.
Configure Google Security Operations with
VPC Service Controls
so that
Google SecOps can access resources and services outside its service perimeter.
Before you begin
Make sure that you have the
required roles to configure VPC Service Controls
at the organization level.
Limitations
VPC Service Controls supports only Google Cloud Identity authentication and Google SecOps Bring Your Own Identity (BYOID) and Workforce Identity Federation.
Google SecOps
feature RBAC
must be enabled to use VPC Service Controls.
VPC Service Controls supports only Google SecOps
chronicle.googleapis.com
and
chronicleservicemanager.googleapis.com
APIs. You can continue to use other Google SecOps APIs, but you might need to configure special rules to continue to use them, and the data and services using those other APIs aren't protected by VPC Service Controls perimeter restrictions.
VPC Service Controls supports export of Google SecOps Unified Data Model (UDM) data only to a
self-managed BigQuery project
or using
Advanced BigQuery Export
. You can continue to use other Google SecOps export methods, but you might need to configure special rules to continue to use them, and exporting data using those methods isn't protected by VPC Service Controls perimeter restrictions. For more information, reach out to your Google SecOps representative.
VPC Service Controls doesn't support
Cloud Monitoring
. However, to prevent non-compliant access, you can revoke permissions to view Cloud Monitoring data. You can continue to use Cloud Monitoring, but you might need to configure special rules to continue to use it, and the data transmission isn't protected by the VPC Service Controls perimeter restrictions. For more information, reach out to your Google SecOps representative.
VPC Service Controls doesn't support
Looker
dashboards. VPC Service Controls supports only Google SecOps
Dashboards
. You can continue to use Looker dashboards, but you might need to configure special rules to continue to use them, and Looker dashboards aren't protected by VPC Service Controls perimeter restrictions.
VPC Service Controls doesn't support legacy and third-party connectors. You need to create the Cloud Storage feeds with the
GOOGLE_CLOUD_STORAGE_V2
source type using v2 connectors. You can continue to use feeds created with legacy and third-party connectors, but you might need to configure special rules to continue to use them, and the use of feeds created with them isn't protected by VPC Service Controls perimeter restrictions.
VPC Service Controls doesn't support Google SecOps
Security Validation
to test your security by simulating attacks in your Google Cloud environment. You can continue to use Security Validation, but you might need to configure special rules to continue to use it, and the use of Security Validation isn't protected by VPC Service Controls perimeter restrictions.
VPC Service Controls doesn't support DataTap.
If you use
customer-managed encryption keys (CMEK)
, Google strongly recommends that you either keep your
Cloud Key Management Service
project in the same perimeter as your Google Cloud project or keep your keys inside the Google Cloud project itself. If you have a requirement to keep CMEKs and your Google Cloud project in different VPC Service Controls perimeters, please reach out to your Google SecOps representative.
Configure the ingress and egress rules
Configure
ingress and egress rules
based on the service perimeter configuration. For more information, see
Service perimeter overview
.
If you encounter issues with VPC Service Controls, use the VPC Service Controls violation analyzer to debug and analyze the issue. For more information, see
Diagnose an access denial in violation analyzer
.
Configure rules for SOAR
This section describes how to configure VPC Service Controls for the SOAR side of the platform.
Complete the following tasks for the Google Cloud user account that you specified when you set up Google SecOps:
Configure the following ingress rules:
-
ingressFrom
:
identityType
:
ANY_SERVICE_ACCOUNT
sources
:
-
accessLevel
:
"*"
ingressTo
:
operations
:
-
serviceName
:
secretmanager.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
projects/
PROJECT_NUMBER
-
ingressFrom
:
identities
:
-
serviceAccount
:
chronicle-soar-provisioning-service@system.gserviceaccount.com
sources
:
-
accessLevel
:
"*"
ingressTo
:
operations
:
-
serviceName
:
binaryauthorization.googleapis.com
methodSelectors
:
-
method
:
"*"
-
serviceName
:
monitoring.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
projects/
PROJECT_NUMBER
Replace the following:
PROJECT_NUMBER
: your Google Cloud bring your own project (BYOP) project number
Configure the following egress rule:
-
egressTo
:
operations
:
-
serviceName
:
binaryauthorization.googleapis.com
methodSelectors
:
-
method
:
"*"
-
serviceName
:
monitoring.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
projects/soar-infra-
SOAR_REGION_ID
egressFrom
:
identities
:
-
serviceAccount
:
chronicle-soar-provisioning-service@system.gserviceaccount.com
sources
:
-
resource
:
projects/
PROJECT_NUMBER
Replace the following:
SOAR_REGION_ID
: the code that Google assigns based on the SOAR region, which you can get from your Google SecOps representative
PROJECT_NUMBER
: your Google Cloud bring your own project (BYOP) project number
Configure rule for SIEM
This section describes how to configure VPC Service Controls for the SIEM side of the platform.
Configure the following egress rule for the Google Cloud user account that you specified when you set up Google SecOps:
-
egressTo
:
operations
:
-
serviceName
:
pubsub.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
projects/389186463911
egressFrom
:
identities
:
-
user
:
"*"
sources
:
-
resource
:
PROJECT_NUMBER
Replace the following:
PROJECT_NUMBER
: your Google Cloud bring your own project (BYOP) project number
Configure rules for Google SecOps with Security Command Center
This section describes how to configure VPC Service Controls for Google SecOps with Security Command Center.
Complete the following tasks for the Google Cloud user account that you specified when you set up Google SecOps:
Configure the following ingress rule:
-
ingressFrom
:
identityType
:
ANY_IDENTITY
sources
:
-
accessLevel
:
"*"
ingressTo
:
operations
:
-
serviceName
:
pubsub.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
projects/
PROJECT_NUMBER
Replace the following:
PROJECT_NUMBER
: your Google Cloud bring your own project (BYOP) project number
Configure the following egress rule:
-
egressTo
:
operations
:
-
serviceName
:
pubsub.googleapis.com
methodSelectors
:
-
method
:
"*"
-
serviceName
:
securitycenter.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
"*"
egressFrom
:
identities
:
-
serviceAccount
:
service-org-
GOOGLE_ORGANIZATION_NUMBER
@gcp-sa-chronicle-soar.iam.gserviceaccount.com
sources
:
-
resource
:
projects/
PROJECT_NUMBER
Replace the following:
GOOGLE_ORGANIZATION_NUMBER
: your Google Cloud organization number
PROJECT_NUMBER
: your Google Cloud bring your own project (BYOP) project number
Configure rule for customer-managed encryption keys
This section describes how to configure VPC Service Controls for Google SecOps with customer-managed encryption keys (
CMEKs
). CMEKs are encryption keys that you own, manage, and store in
Cloud Key Management Service
.
Configure the following ingress rule:
-
ingressFrom
:
identities
:
-
serviceAccount
:
service-
SECRET_MANAGER_PROJECT_NUMBER
@gcp-sa-secretmanager.iam.gserviceaccount.com
sources
:
-
accessLevel
:
"*"
ingressTo
:
operations
:
-
serviceName
:
secretmanager.googleapis.com
methodSelectors
:
-
method
:
"*"
resources
:
-
projects/
PROJECT_NUMBER
Replace the following:
SECRET_MANAGER_PROJECT_NUMBER
: the project that Google uses to store secrets for some ingestion features, which you can get from your Google SecOps representative
PROJECT_NUMBER
: your Google Cloud bring your own project (BYOP) project number
What's next
Learn more about
VPC Service Controls
.
See the Google Security Operations entry in the
VPC Service Controls supported products table
.
