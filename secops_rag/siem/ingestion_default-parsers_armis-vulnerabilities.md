# Collect Armis Vulnerabilities logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/armis-vulnerabilities/  
**Scraped:** 2026-03-05T09:19:09.509376Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Armis Vulnerabilities logs
Supported in:
Google secops
SIEM
This document explains how to ingest Armis Vulnerabilities logs to Google Security Operations using Google Cloud Functions. The parser transforms raw JSON formatted security vulnerability logs into a structured format conforming to the Google SecOps UDM. It extracts various fields from the raw log, maps them to corresponding UDM fields, performs data type conversions, and structures the output for ingestion into the Google SecOps platform.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance with customer ID and service account credentials
Privileged access to Armis Centrix platform
Armis API Secret Key and Server URL
Access to Google Cloud with permissions to create Cloud Functions, Secret Manager secrets, and Cloud Scheduler jobs
Armis Asset Vulnerability Management (AVM) license or module access
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
customer ID
from the
Organization Details
section.
Get Google SecOps service account credentials
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
(service account JSON file).
Save the file securely as you will need to upload it to Google Secret Manager.
Get Armis API Secret Key
Sign in to the
Armis Centrix
platform.
Go to
Settings
>
API Management
.
Click
Create
if you need to generate a new API secret key.
Click
Show
to view the secret key.
Copy and save the secret key securely.
Configure Google Secret Manager
This section guides you through using
Google Secret Manager
to securely store the service account key required for the integration.
Add the Google SecOps service account secret
Sign in to the
Google Cloud console
.
Go to
Security
>
Secret Manager
.
Click
Create Secret
.
Provide the following configuration details:
Name
: Enter a name for the secret (for example,
secops-service-account
).
Secret value
: Upload the Google SecOps service account JSON file you downloaded earlier, or paste its contents directly.
Click
Create Secret
.
Copy
the
resource ID
of the created secret in the following format:
projects/{project_id}/secrets/{secret_id}/versions/{version_id}
Add the Armis API Secret Key secret
In
Secret Manager
, click
Create Secret
.
Provide the following configuration details:
Name
: Enter a name for the secret (for example,
armis-api-secret
).
Secret value
: Paste the Armis API Secret Key you obtained earlier.
Click
Create Secret
.
Copy
the
resource ID
of the created secret in the following format:
projects/{project_id}/secrets/{secret_id}/versions/{version_id}`
Download and prepare the ingestion script
Access the official Google SecOps ingestion scripts repository at https://github.com/chronicle/ingestion-scripts.
Download the contents of the
armis
directory from the repository.
Download the
common
directory from the repository (required dependency).
Create a new directory for the Cloud Function deployment on your local machine.
Copy the contents of both the
armis
and
common
directories into your deployment directory.
Configure environment variables
Open the
.env.yml
file in a text editor.
Edit the file with the following configuration:
CHRONICLE_CUSTOMER_ID
:
<
YOUR_CUSTOMER_ID
>
CHRONICLE_REGION
:
"us"
CHRONICLE_SERVICE_ACCOUNT
:
projects/{project_id}/secrets/{chronicle-secret-id}/versions/{version_id}
CHRONICLE_NAMESPACE
:
<
YOUR_NAMESPACE
>
POLL_INTERVAL
:
"10"
ARMIS_SERVER_URL
:
https://<your-armis-instance>.armis.com
ARMIS_API_SECRET_KEY
:
projects/{project_id}/secrets/{armis-secret-id}/versions/{version_id}
HTTPS_PROXY
:
CHRONICLE_DATA_TYPE
:
ARMIS_VULNERABILITIES
Replace the following values:
<YOUR_CUSTOMER_ID>
: Your Google SecOps customer ID
projects/{project_id}/secrets/{chronicle-secret-id}/versions/{version_id}
: The full resource ID path of your Google SecOps service account secret from Secret Manager
<YOUR_NAMESPACE>
: Optional namespace for Google Security Operations logs (for example,
armis-vulnerabilities
)
<your-armis-instance>
: Your Armis tenant subdomain (for example, if your URL is https://company.armis.com, use
company
)
projects/{project_id}/secrets/{armis-secret-id}/versions/{version_id}
: The full resource ID path of your Armis API secret from Secret Manager
Deploy the Cloud Function
Deploy using Cloud Function Gen2 (recommended)
Open
Cloud Shell
or your local terminal with gcloud CLI installed.
Navigate to the directory containing the ingestion script files.
Run the following command:
gcloud
functions
deploy
armis-vulnerabilities-ingestion
\
--gen2
\
--entry-point
main
\
--trigger-http
\
--runtime
python39
\
--env-vars-file
.env.yml
\
--memory
512MB
\
--timeout
3600s
\
--region
us-central1
Deploy using Cloud Function Gen1 (Alternative)
Run the following command:
gcloud
functions
deploy
armis-vulnerabilities-ingestion
\
--entry-point
main
\
--trigger-http
\
--runtime
python39
\
--env-vars-file
.env.yml
\
--memory
512MB
\
--timeout
540s
\
--region
us-central1
Create a Cloud Scheduler job
In the Google Cloud console, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Name
: Enter a name for the job (for example,
armis-vulnerabilities-scheduler
).
Region
: Select the same region as your Cloud Function (for example,
us-central1
).
Frequency
: Enter the schedule using cron syntax (for example,
*/10 * * * *
for every 10 minutes).
Timezone
: Select your preferred timezone (for example, UTC).
Click
Continue
.
Select
HTTP
as the target type.
Provide the following configuration details:
URL
: In the Cloud Functions console, go to your function's
TRIGGER
tab and copy the trigger URL. Paste it here.
HTTP method
: Select
POST
.
Click
Auth header
>
Add OIDC token
.
Select the
Service account
used by the Cloud Function.
Click
Create
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
affectedDevicesCount
read_only_udm.security_result.detection_fields.value
Direct mapping, converted to string.
attackComplexity
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
attackVector
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
availabilityImpact
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
avmRating
read_only_udm.security_result.detection_fields.value
Direct mapping.
botnets
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Concatenated into a single string if multiple botnets exist.
cisaDueDate
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
collection_time.nanos
read_only_udm.metadata.event_timestamp.nanos
Direct mapping.
collection_time.seconds
read_only_udm.metadata.event_timestamp.seconds
Direct mapping.
commonName
read_only_udm.extensions.vulns.vulnerabilities.name
Direct mapping.
confidentialityImpact
read_only_udm.security_result.detection_fields.value
Direct mapping.
cveUid
read_only_udm.extensions.vulns.vulnerabilities.cve_id
Direct mapping.
cvssScore
read_only_udm.extensions.vulns.vulnerabilities.cvss_base_score
Direct mapping, converted to float.
description
read_only_udm.metadata.description
Direct mapping.
epssPercentile
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping, converted to string.
epssScore
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping, converted to string.
exploitabilityScore
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping, converted to string.
firstReferencePublishDate
read_only_udm.extensions.vulns.vulnerabilities.first_found
Parsed to timestamp, handles formats with and without milliseconds.
firstWeaponizedReferencePublishDate
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
hasRansomware
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping, converted to string.
id
read_only_udm.metadata.product_log_id
Direct mapping.
impactScore
read_only_udm.security_result.detection_fields.value
Direct mapping, converted to string.
integrityImpact
read_only_udm.security_result.detection_fields.value
Direct mapping.
isWeaponized
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping, converted to string.
latestExploitUpdate
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
numOfExploits
read_only_udm.security_result.detection_fields.value
Direct mapping, converted to string.
numberOfThreatActors
read_only_udm.security_result.detection_fields.value
Direct mapping, converted to string.
orgPriorityManualChangeReason
read_only_udm.security_result.detection_fields.value
Direct mapping.
orgPriorityManualChangedBy
read_only_udm.principal.user.userid
Direct mapping.
orgPriorityManualUpdateTime
read_only_udm.principal.labels.value
Direct mapping.
privilegesRequired
read_only_udm.security_result.detection_fields.value
Direct mapping.
publishedDate
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
reportedByGoogleZeroDays
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping, converted to string.
scope
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
severity
read_only_udm.extensions.vulns.vulnerabilities.severity
Mapped to CRITICAL, HIGH, MEDIUM, LOW based on value, original value also mapped to severity_details.
status
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Direct mapping.
threatTags
read_only_udm.extensions.vulns.vulnerabilities.about.labels.value
Concatenated into a single string if multiple threat tags exist.
userInteraction
read_only_udm.about.labels.value
Direct mapping.
vulnerabilities_matches
read_only_udm.metadata.url_back_to_product
Direct mapping.
read_only_udm.metadata.event_type
Set to "GENERIC_EVENT".
read_only_udm.metadata.product_name
Set to "ARMIS".
read_only_udm.metadata.vendor_name
Set to "ARMIS".
read_only_udm.metadata.log_type
Set to "ARMIS_VULNERABILITIES".
read_only_udm.extensions.vulns.vulnerabilities.severity_details
"severity" field value is mapped to this field
Need more help?
Get answers from Community members and Google SecOps professionals.
