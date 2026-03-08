# Use ingestion scripts deployed as Cloud Run functions

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-using-cloud-functions/  
**Scraped:** 2026-03-05T09:16:38.834524Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use ingestion scripts deployed as Cloud Run functions
Supported in:
Google secops
SIEM
Google Security Operations has provided a set of ingestion scripts, written in Python,
that are intended to be deployed as Cloud Run functions. These scripts enable you
to ingest data from the following log sources, listed by name and log type.
Armis Google SecOps Integration
Aruba Central (
ARUBA_CENTRAL
)
Azure Event Hub (configurable log type)
Box (
BOX
)
Citrix Cloud audit logs (
CITRIX_MONITOR
)
Citrix session metadata (
CITRIX_SESSION_METADATA
)
Cloud Storage (configurable log type)
Duo Activity (
DUO_ACTIVITY
)
Duo Admin (
DUO_ADMIN
)
MISP (
MISP_IOC
)
OneLogin (
ONELOGIN_SSO
)
OneLogin user context (
ONELOGIN_USER_CONTEXT
)
Proofpoint (configurable log type)
Pub/Sub (configurable log type)
Slack audit logs (
SLACK_AUDIT
)
STIX/TAXII threat intelligence (
STIX
)
Tenable.io (
TENABLE_IO
)
Trend Micro Cloud App Security (configurable log type)
Trend Micro Vision One audit logs (
TREND_MICRO_VISION_AUDIT
)
These scripts are located in the Google SecOps
GitHub repository
.
Known limitation:
When these scripts are used in a
stateless
environment such as Cloud Run functions, they may not send all logs to
Google SecOps because they lack checkpoint functionality.
Google SecOps has tested the scripts with the
Python 3.9
runtime
.
Before you begin
Read the following resources that provide context and background information
that enable you to use the Google SecOps ingestion scripts effectively.
Deploying Cloud Run functions
for
information about how to deploy Cloud Run functions from your local machine.
Creating and accessing secrets
explains how to use Secret Manager. You will need this to store and
access the Google SecOps service account JSON file.
Install the Google Cloud CLI
. You will use this to
deploy the Cloud Run function.
Google Cloud Pub/Sub  documentation
if you
plan to ingest data from Pub/Sub.
Assemble the files for a single log type
Each sub-directory in
Google SecOps
GitHub
contains files that
ingest data for a single Google SecOps log type. The script connects to a
single source device and then sends raw logs to Google SecOps using the
Ingestion API. We recommend that you deploy each log type as a separate
Cloud Run function. Access the scripts in the Google SecOps GitHub
repository. Each sub-directory in GitHub contains the following files specific
to the log type it ingests.
main.py
is the ingestion script specific to the log type. It connects to
the source device and ingests data to Google SecOps.
.env.yml
stores configuration required by the Python script and is
specific to the deployment. You modify this file to set configuration
parameters required by the ingestion script.
README.md
provides information about configuration parameters.
Requirements.txt
defines the dependencies required by the ingestion
script. In addition, the
common
folder contains utility functions that all
ingestion scripts depend on.
Perform the following steps to assemble the files that ingest data for a single
log type:
Create a deployment directory to store the files for the Cloud Run function.
This will contain all files needed for the deployment.
Copy all files from the GitHub sub-directory of the selected log type,
for example OneLogin User Context, to this deployment directory.
Copy the
common
folder and all contents to the deployment directory.
The contents of the directory will look similar to the following:
one_login_user
├─common
│
├─__init__.py
│
├─auth.py
│
├─env_constants.py
│
├─ingest.py
│
├─status.py
│
└─utils.py
├─env.yml
├─main.py
└─requirements.txt
Configure the scripts
Launch a Cloud Shell session.
Connect with SSH to a Google Cloud Linux VM. See
Connect to Linux VMs using
Google tools
.
Upload the ingestion scripts by clicking
more_vert
More
>
Upload
or
Download
to move your files or folders to or from Cloud Shell.
Files and folders can only be uploaded to and downloaded from your home directory.
For more options to transfer files between Cloud Shell and your local workstation,
see [Upload and download files and folders from Cloud Shell](/shell/docs/uploading-and-downloading-files#upload_and_download_files_and_folders.
Edit the
.env.yml
file for the function and populate the required
environment variables. The following table lists runtime environment
variables common to all ingestion scripts.
Variable name
Description
Required
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) customer ID.
Yes
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) region.
Yes
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Contents of the Chronicle (Google SecOps) service account JSON file.
Yes
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with asset namespaces
.
No
None
No
Each script requires environment variables specific to the script. See
Configuration parameters by log
type
for details about the environment variables required by each log type.
Environment variables marked as
Secret = Yes
must be configured as secrets in
Secret Manager. See
Secret Manager
pricing
for information on the cost of using
Secret Manager.
See
Creating and accessing
secrets
for
detailed instructions.
After the secrets are created in Secret Manager, use the secret
resource name as the value for environment variables. For example:
projects/{project_id}/secrets/{secret_id}/versions/{version_id}
, where
{project_id}
,
{secret_id}
, and
{version_id}
are specific to your
environment.
Set up a scheduler or trigger
All scripts, except Pub/Sub, are implemented to collect the data at
periodic intervals from a source device. You must set up a trigger using
Cloud Scheduler to fetch data over time. The ingestion script for Pub/Sub
continuously monitors the Pub/Sub subscription. For more information,
see
Running services on a schedule
and
Using Pub/Sub to trigger a Cloud Run function
.
Deploy the Cloud Run function
Launch a Cloud Shell   session.
Connect via SSH to a Google Cloud Linux VM. See
Connect to Linux VMs using Google tools
.
Change to the directory where you copied ingestion scripts.
Execute the following command to deploy the Cloud Run function.
gcloud functions deploy <FUNCTION NAME> --service-account
<SERVICE_ACCOUNT_EMAIL> --entry-point main --trigger-http
--runtime python39 --env-vars-file .env.yml
Replace
<FUNCTION_NAME>
with the name you define for the
Cloud Run function.
Replace
<SERVICE_ACCOUNT_EMAIL>
with the email address of the service
account you want your Cloud Run function to use.
account you want your Cloud Run function to use.
If you don't change directory to the location of the files, make
sure to use the
--source
option to specify the location of the
deployment scripts.
The service account running your Cloud Run function must have the
Cloud Functions Invoker
(
roles/cloudfunctions.invoker
)
and
Secret Manager Secret Accessor
(
roles/secretmanager.secretAccessor
)
roles.
View runtime logs
The ingestion scripts print runtime messages to
stdout
. Cloud Run functions
provides a mechanism to view log messages.
Configuration parameters by log type
Armis Google SecOps Integration
This script collects the data using API calls from the Armis platform for different
 types of events like alerts, activities, devices, and vulnerabilities.
 The collected data is ingested into Google SecOps and parsed by the corresponding parsers.
Script flow
Following is the flow of the script:
Verify environment variables.
Deploy the script to Cloud Run functions.
Collect data using the ingestion script.
Ingest collected data into Google SecOps.
Parse collected data through corresponding parsers in Google SecOps.
Use a script to collect and ingest data into Google SecOps
Verify environment variables.
Variable
Description
Required
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) customer ID.
Yes
-
No
CHRONICLE_REGION
Chronicle (Google SecOps) region.
Yes
US
Yes
CHRONICLE_SERVICE_ACCOUNT
Contents of the Chronicle (Google SecOps) service account JSON file.
Yes
-
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with.
No
-
No
POLL_INTERVAL
Frequency interval at which the function executes to get additional
Frequency interval at which the function executes to get additional
  log data (in minutes). This duration must be the same as the Cloud Scheduler job interval.
Yes
10
No
ARMIS_SERVER_URL
Server URL of Armis platform.
Yes
-
No
ARMIS_API_SECRET_KEY
Secret key required to authenticate.
Yes
-
Yes
HTTPS_PROXY
Proxy server URL.
No
-
No
CHRONICLE_DATA_TYPE
Chronicle (Google SecOps) data type to push data into the Google SecOps.
Yes
-
No
Set up the directory.
Create a new directory for the Cloud Run functions deployment and add to it
a
common
directory and the contents of the ingestion script (
armis
).
Set the required runtime environment variables.
Define the required environment variables in the
.env.yml
file.
Use secrets.
Environment variables marked as secret must be configured as secrets in the Secret Manager.
For more information on how to create secrets, see
Create a secret
.
After creating the secrets in Secret Manager, use the secret's resource
name as the value for environment variables. For example:
CHRONICLE_SERVICE_ACCOUNT: projects/{project_id}/secrets/{secret_id}/versions/{version_id}
Configure the namespace.
Set the
CHRONICLE_NAMESPACE
environment variable to configure the namespace. The Chronicle (Google SecOps) logs are ingested into the namespace.
Deploy the Cloud Run functions.
Run the following command from inside the previously created directory to deploy the cloud function.
gcloud functions deploy <FUNCTION NAME> --gen2 --entry-point main --trigger-http --runtime python39 --env-vars-file .env.yml
Cloud Run functions default specifications.
Variable
Default
Description
Memory
256 MB
None
None
Timedout
60 seconds
None
None
Region
us-central1
None
None
Minimum Instances
0
None
None
Maximum Instances
100
None
None
For more information on how to configure these variables, see
Configure
Cloud Run functions
.
Fetch historical data.
To fetch historical data and continue collecting real-time data:
Configure the
POLL_INTERVAL
environment variable in minutes for which the historical data needs to be fetched.
Trigger the function using a scheduler or manually by running the command in Google Cloud CLI after configuring Cloud Run functions.
Aruba Central
This script fetches audit logs from the Aruba Central platform and ingests them
into Google SecOps with the
ARUBA_CENTRAL
log type. For information about
how the library can be used, see the
pycentral Python
SDK
.
Define the following environment variables in the
.env.yml
file.
Variable
Description
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
CHronicle (Google SecOps) service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Chronicle (Google SecOps) namespaces, see
Work with asset namespaces
.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
10
No
ARUBA_CLIENT_ID
Aruba Central API gateway client ID.
None
No
ARUBA_CLIENT_SECRET_SECRET_PATH
Aruba Central API gateway client secret.
None
Yes
ARUBA_USERNAME
Username of Aruba Central platform.
None
No
ARUBA_PASSWORD_SECRET_PATH
Password of Aruba Central platform.
None
Yes
ARUBA_BASE_URL
Base URL of Aruba Central API gateway.
None
No
ARUBA_CUSTOMER_ID
Customer ID of Aruba Central platform.
None
No
Azure Event Hub
Unlike other ingestion scripts, this script uses Azure functions to fetch events
from Azure Event Hub. An Azure function triggers itself whenever a new event is
added into a bucket, and each event is gradually ingested into
Google SecOps.
Steps to deploy Azure functions:
Download the data connector file named
Azure_eventhub_API_function_app.json
from the repository.
Sign in to your Microsoft Azure portal.
Navigate to Microsoft
Sentinel > Select your workspace from the list >
Select Data Connector
in the configuration section, and do the following:
Set the following flag as true in the URL:
feature.BringYourOwnConnector=true
. For example:
https://portal.azure.com/?feature.BringYourOwnConnector=true&...
1.  Find the
import
button on the page and import the data
            connector file downloaded in step 1.
Click the
Deploy to Azure
button to deploy your function, and follow the
steps mentioned on the same page.
Select the preferred
Subscription
,
Resource group
, and
Location
and provide the required values.
Click
Review + Create
.
Click
Create
to deploy.
Box
This script gets details about events that happen within Box and ingests them
into Google SecOps with the
BOX
log type. The data provide insights into CRUD operations on objects in the Box environment. For information about Box events, see the
Box events API
.
Define the following environment variables in the
.env.yml
file. For more
information about the Box Client ID, Client Secret, and Subject ID, see
Client
Credentials
Grant
.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
5
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
CHronicle (Google SecOps) service account JSON file.
None
Yes
BOX_CLIENT_ID
Client ID of Box platform, available in Box developer console.
None
No
BOX_CLIENT_SECRET
Path to the secret in Secret Manager that stores the client
secret of Box platform used for authentication.
None
Yes
BOX_SUBJECT_ID
Box User ID or Enterprise ID.
None
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
      information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
Citrix Cloud audit logs
This script collects Citrix Cloud audit logs and ingests them into
Google SecOps with the
CITRIX_MONITOR
log type. These logs help identify
activities performed in the Citrix Cloud environment by providing information
about what changed, who changed it, when it was changed, and so forth. For more
information, see the
Citrix Cloud SystemLog
API
.
Define the following environment variables in the
.env.yml
file. For
information about Citrix Client IDs and Client Secrets, see
Getting started
with Citrix
APIs
.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle
(Google SecOps) service account JSON file.
None
Yes
CITRIX_CLIENT_ID
Citrix API Client ID.
None
No
CITRIX_CLIENT_SECRET
Path to the secret in Secret Manager that stores the Citrix API
Client Secret used for authentication.
None
Yes
CITRIX_CUSTOMER_ID
Citrix CustomerID.
None
No
POLL_INTERVAL
Frequency interval at which additional log data is collected (in
minutes). This duration must be the same as the Cloud Scheduler job
interval.
30
No
URL_DOMAIN
Citrix Cloud Endpoint.
None
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Chronicle (Google SecOps) namespaces, see
Work with asset namespaces
.
None
No
Citrix session metadata
This script collects Citrix session metadata from Citrix environments and ingests it into Google SecOps with the
CITRIX_MONITOR
log type. The data includes
user login details, session duration, session creation time, session ending time,
and other metadata related to session. For more information, see the
Citrix Monitor Service API
.
Define the following environment variables in the
.env.yml
file. For
information about Citrix Client IDs and Client Secrets, see
Getting started
with Citrix
APIs
.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
URL_DOMAIN
Citrix URL domain.
None
No
CITRIX_CLIENT_ID
Citrix Client ID.
None
No
CITRIX_CLIENT_SECRET
Path to the secret in Secret Manager that stores the Citrix
Client Secret used for authentication.
None
Yes
CITRIX_CUSTOMER_ID
Citrix customer ID.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
30
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with
asset namespaces
.
None
No
Cloud Storage
This script fetches system logs from Cloud Storage and ingests them into
Google SecOps with a configurable value for the log type. For details, see
the
Google Cloud Python client
library
.
Define the following environment variables in the
.env.yml
file. Google Cloud
has security-relevant logs from which some log types are not exportable directly
to Google SecOps. For more information, see
Security logs
analytics
.
Variable
Description
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps) service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get additional log data (in minutes). This duration must be the same as the Cloud Scheduler job interval.
60
No
GCS_BUCKET_NAME
Name of the Cloud Storage bucket from which to fetch the data.
None
No
GCP_SERVICE_ACCOUNT_SECRET_PATH
Path to the secret in Secret Manager that stores the Google Cloud Service Account JSON file.
None
Yes
CHRONICLE_DATA_TYPE
Log type to push data into the Chronicle (Google SecOps) instance.
None
No
Duo Activity
This script fetches Duo Activity logs from Duo Admin and ingests them into
Google SecOps with the
DUO_ACTIVITY
log type. For more information, see the
Duo Admin API
.
Define the following environment variables in the
.env.yml
file.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
, and
northamerica-northeast2
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
BACKSTORY_API_V1_URL
The URL path of Duo Security API. For more information about downloading
      JSON file that contains the DUO Admin API integration key,
      see
Duo Admin documentation
.
None
Yes
DUO_SECRET_KEY
The DUO secret key required to fetch logs from the DUO API. See Duo
      Admin documentation for instructions about downloading the JSON file that
      contains the Duo Admin API integration key, Duo Admin API secret key, and
      the Duo Admin API hostname.
None
Yes
DUO_INTEGRATION_KEY
The DUO integration key required to fetch logs from the DUO API. See
      Duo Admin documentation for instructions about downloading the JSON file
      that contains the Duo Admin API integration key, Duo Admin API secret key,
      and the Duo Admin API hostname.
None
Yes
LOG_FETCH_DURATION
The duration for which the logs are fetched.
1
No
CHECKPOINT_FILE_PATH
The path of file where the checkpoint timestamp of last ingested log is stored.
checkpoint.json
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
Duo Admin
The script gets events from Duo Admin related to CRUD operations performed on
various objects such as user account and security. The events are ingested into
Google SecOps with the
DUO_ADMIN
log type. For more information, see the
Duo Admin API
.
Define the following environment variables in the
.env.yml
file.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
None
No
DUO_API_DETAILS
Path to the secret in Secret Manager that stores the Duo account
JSON file. This contains the Duo Admin API integration key, Duo Admin
API secret key, and the Duo Admin API hostname. For example:
{
"ikey": "abcd123",
"skey": "def345",
"api_host": "abc-123"
}
See Duo Admin documentation for instructions about downloading
the JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
MISP
This script fetches threat relation information from MISP, an open source threat
intelligence and sharing platform, and ingests it into Google SecOps with
the
MISP_IOC
log type. For more information, see the
MISP Events
API
.
Define the following environment variables in the
.env.yml
file.
Variable
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
5
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
ORG_NAME
Organization name for filtering events.
None
No
API_KEY
Path to the secret in Secret Manager that stores the API key for
used authentication.
None
Yes
TARGET_SERVER
The IP address of the MISP instance that you created.
None
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
      information about Google SecOps namespaces, see
Work with
      asset namespaces
.
None
No
OneLogin Events
This script gets events from a OneLogin environment and ingests them into
Google SecOps with the
ONELOGIN_SSO
log type. These events provide
information such as operations on user accounts. For more information, see the
OneLogin Events
API
.
Define the following environment variables in the
.env.yml
file. For
information about OneLogin Client IDs and Client Secrets, see
Working with API
Credentials
.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
5
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
CLIENT_ID
Client ID of OneLogin platform.
None
No
CLIENT_SECRET
Path to the secret in Secret Manager that stores the client
secret of OneLogin platform used for authentication.
None
Yes
TOKEN_ENDPOINT
The URL to request an Access Token.
https://api.us.onelogin.com/auth/oauth2/v2/token
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with
asset namespaces
.
None
No
OneLogin user context
This script gets data related to user accounts from a OneLogin environment and
ingests it into Google SecOps with the
ONELOGIN_USER_CONTEXT
log type.
For more information, see the
OneLogin User
API
.
Define the following environment variables in the
.env.yml
file. For
information about OneLogin Client IDs and Client Secrets, see
Working with API
Credentials
.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
CHronicle (Google SecOps) instance customer ID.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
30
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
CLIENT_ID
Client ID of OneLogin platform.
None
No
CLIENT_SECRET
Path to the secret in Secret Manager that stores the client
secret of OneLogin platform used for authentication.
None
Yes
TOKEN_ENDPOINT
The URL to request an Access Token.
https://api.us.onelogin.com/auth/oauth2/v2/token
No
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with
asset namespaces
.
None
No
Proofpoint
This script fetches data on users targeted by attacks from a particular organization within a given time period and ingests that data into Google SecOps. For information about the API used, see the
People API
.
Define the following environment variables in the
.env.yml
file. For details about getting the Proofpoint service principal and Proofpoint secret, see the
Providing proofpoint TAP credentials to Arctic Wolf configuration guide
.
Variable
Description
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps) service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get additional log data (in minutes). This duration must be the same as the Cloud Scheduler job interval.
360
No
CHRONICLE_DATA_TYPE
Log type to push data into the Chronicle (Google SecOps) instance.
None
No
PROOFPOINT_SERVER_URL
Base URL of Proofpoint Server API gateway.
None
No
PROOFPOINT_SERVICE_PRINCIPLE
Username of Proofpoint platform. This is typically the service principal.
None
No
PROOFPOINT_SECRET
Path of the Secret Manager with the version, where the password of Proofpoint platform is stored.
None
Yes
PROOFPOINT_RETRIEVAL_RANGE
Number indicating from how many days the data should be retrieved. Accepted values are 14, 30, and 90.
None
No
Pub/Sub
This script collects messages from Pub/Sub subscriptions and ingests the
data to Google SecOps. It continuously monitors the subscription gateway
and ingests newer messages when they appear. For more information, see the
following documents:
Create and use subscriptions
Pub/Sub Triggers
Pub/Sub Message API
This ingestion script requires that you set variables in both the
.env.yml
file and the Cloud Scheduler job.
Define the following environment variables in the
.env.yml
file.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps)
service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with
Asset Namespaces
.
None
No
Set the following variables in the Cloud Scheduler
Message body
field
as a JSON formatted string. See
creating the
Cloud Scheduler
for more information
about the
Message body
field.
Variable name
Description
Default Value
Secret
PROJECT_ID
Pub/Sub project ID. See
creating and managing projects
for
information about the project Id.
None
No
SUBSCRIPTION_ID
Pub/Sub Subscription ID.
None
No
CHRONICLE_DATA_TYPE
Ingestion label for the log type provided while pushing data to Chronicle (Google SecOps). See
Supported default parsers
for a list of supported log types.
None
No
Here is an example JSON formatted string for the
Message body
field.
{ "PROJECT_ID":"projectid-0000","SUBSCRIPTION_ID":"subscription-id","CHRONICLE_DATA_TYPE":"SQUID_PROXY"}
Slack audit logs
This script gets audit logs from a Slack Enterprise Grid organization and
ingests them into Google SecOps with the
SLACK_AUDIT
log type. For more
information, see
Slack Audit Logs
API
.
Define the following environment variables in the
.env.yml
file.
Variable name
Description
Default Value
Secret
CHRONICLE_CUSTOMER_ID
Chronnicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the
Chronicle (Google SecOps) service account JSON file.
None
Yes
POLL_INTERVAL
Frequency interval at which the function executes to get
additional log data (in minutes). This duration must be the same as
the Cloud Scheduler job interval.
5
No
SLACK_ADMIN_TOKEN
Path to the secret in Secret Manager that stores the Slack
Authentication token.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For
information about Google SecOps namespaces, see
Work with
asset namespaces
.
None
No
STIX/TAXII
This script pulls indicators from STIX/TAXII server and ingests them into
Google SecOps. For more information refer to the
STIX/TAXII API
documentation
.
Define the following environment variables in
.env.yml
file.
Variable Name
Description
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps) service account JSON file.
None
Yes
POLL_INTERVAL
Frequency interval (in minutes) at which the function executes. This duration must be same as the Cloud Scheduler job.
60
No
TAXII_VERSION
The STIX/TAXII version to use. Possible options are 1.1, 2.0, 2.1
None
No
TAXII_DISCOVERY_URL
Discovery URL of TAXII server.
None
No
TAXII_COLLECTION_NAMES
Collections (CSV) from which to fetch the data. Leave empty to fetch data from all of the collections.
None
No
TAXII_USERNAME
Username required for authentication, if any.
None
No
TAXII_PASSWORD_SECRET_PATH
Password required for authentication, if any.
None
Yes
Tenable.io
This script fetches asset and vulnerability data from the Tenable.io platform
and ingests it into Google SecOps with the
TENABLE_IO
log type. For
information about the library used, see the
pyTenable Python
SDK
.
Define the following environment variables in the
.env.yml
file. For details
about asset and vulnerability data, see the Tenable.io API:
Export
assets
and
Export
vulnerabilities
.
Variable
Description
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps) service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get additional log data (in minutes). This duration must be the same as the Cloud Scheduler job interval.
360
No
TENABLE_ACCESS_KEY
The access key used for authentication.
None
No
TENABLE_SECRET_KEY_PATH
Path of the Google Secret Manager with the version, where the password for Tenable Server is stored.
None
Yes
TENABLE_DATA_TYPE
Type of data to ingest in Google SecOps. Possible Values: ASSETS, VULNERABILITIES.
ASSETS, VULNERABILITIES
No
TENABLE_VULNERABILITY
The state of the vulnerabilities you want the export to include. Possible values: `OPEN`, `REOPENED`, and `FIXED`.
OPEN, REOPENED
No
Trend Micro Cloud App Security
This script fetches security logs from the Trend Micro platform and ingests them
into Google SecOps. For information about the API used, see the
security
logs
API
.
Define the following environment variables in the
.env.yml
file.
Variable
Description
Default
Secret
CHRONICLE_CUSTOMER_ID
Chronicle (Google SecOps) instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps) service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get additional log data (in minutes). This duration must be the same as the Cloud Scheduler job interval.
10
No
CHRONICLE_DATA_TYPE
Log type to push data into the Chronicle (Google SecOps) instance.
None
No
TREND_MICRO_AUTHENTICATION_TOKEN
Path of the Google Secret Manager with the version, where the authentication token for Trend Micro Server is stored.
None
Yes
TREND_MICRO_SERVICE_URL
Service URL of the Cloud App Security service.
None
No
TREND_MICRO_SERVICE
The name of the protected service, whose logs to retrieve. Supports comma-separated values. Possible values: exchange, sharepoint, onedrive, dropbox, box, googledrive, gmail, teams, exchangeserver, salesforce_sandbox, salesforce_production, teams_chat.
exchange, sharepoint, onedrive, dropbox, box, googledrive, gmail, teams, exchangeserver, salesforce_sandbox, salesforce_production, teams_chat
No
TREND_MICRO_EVENT
The type of the security event, whose logs to retrieve. Supports comma-separated values. Possible values: securityrisk, virtualanalyzer, ransomware, dlp.
securityrisk, virtualanalyzer, ransomware, dlp
No
Trend Micro Vision One
This script retrieves the audit logs of Trend Micro Vision One and ingests them
into the Google SecOps with the log type
TREND_MICRO_VISION_AUDIT
. For
information about the API used, see the
audit logs
API
.
Define the following environment variables in the
.env.yml
file.
Variable
Description
Default
Secret
TREND_MICRO_VISION_AUDIT
Google SecOps instance customer ID.
None
No
CHRONICLE_REGION
Chronicle (Google SecOps) instance region.
us
Other valid values:
asia-northeast1
,
asia-south1
,
asia-southeast1
,
australia-southeast1
,
europe
,
europe-west2
,
europe-west3
,
europe-west6
,
europe-west9
,
europe-west12
,
me-central1
,
me-central2
,
me-west1
,
northamerica-northeast2
, and
southamerica-east1
.
No
CHRONICLE_SERVICE_ACCOUNT
Path to the secret in Secret Manager that stores the Chronicle (Google SecOps) service account JSON file.
None
Yes
CHRONICLE_NAMESPACE
The namespace that the Chronicle (Google SecOps) logs are labeled with. For information about Google SecOps namespaces, see
Work with asset namespaces
.
None
No
POLL_INTERVAL
Frequency interval at which the function executes to get additional log data (in minutes). This duration must be the same as the Cloud Scheduler job interval.
10
No
TREND_MICRO_AUTHENTICATION_TOKEN
Path of the Google Secret Manager with the version, where the authentication token for Trend Micro Server is stored.
None
Yes
TREND_MICRO_DOMAIN
Trend Micro Vision One region where the service endpoint is located.
None
No
Need more help?
Get answers from Community members and Google SecOps professionals.
