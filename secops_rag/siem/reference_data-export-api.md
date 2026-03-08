# Data Export

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/data-export-api/  
**Scraped:** 2026-03-05T09:37:42.358440Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Data Export
Supported in:
Google secops
SIEM
Data Export enables customers to export raw log data from their Google Security Operations account to their Google Cloud Storage buckets and manage existing export requests.
Data Export is designed for small volume, point-in-time data exports. This API isn't intended for large-scale continuous data transfers, system-wide backups, or long-term archiving. Because export jobs run in the backend system, anticipate potential delays in accessing your data after an export request is made.
You can export a maximum of 10 TB per
CreateDataExport
request. This data is stored compressed (the 10TB limit), but is exported uncompressed. The size of the exported data may not match this 10TB limit, but transfers that exceed it must be split.
Before exporting data from Google SecOps, customers must create their own Google Cloud Storage bucket (make sure that the bucket is not publicly accessible) and grant
malachite-data-export-batch@prod.google.com
the following roles for that Google Cloud Storage bucket:
storageObjectAdmin
legacyBucketReader
Use the Google Cloud console or
command-line tool
to issue the following commands:
gcloud storage buckets add-iam-policy-binding gs://<your-bucket-name> --member=user:malachite-data-export-batch@prod.google.com --role=roles/storage.objectAdmin
gcloud storage buckets add-iam-policy-binding gs://<your-bucket-name> --member=user:malachite-data-export-batch@prod.google.com --role=roles/storage.legacyBucketReader
Get API authentication credentials
Your Cloud Storage representative will provide you with a
Google Developer
Service Account
Credential to enable the API client to communicate with the API.
You also must provide the Auth Scope when initializing your API client. OAuth 2.0 uses
a scope to limit an application's access to an account. When an application requests a scope,
the access token issued to the application is limited to the scope granted.
Use the following scope to initialize your Backstory API client:
https://www.googleapis.com/auth/chronicle-backstory
Python example
The following Python example demonstrates how to use the OAuth2 credentials
and HTTP client using
google.oauth2
and
googleapiclient
.
# Imports required for the sample - Google Auth and API Client Library Imports.
# Get these packages from https://pypi.org/project/google-api-python-client/ or run $ pip
# install google-api-python-client from your terminal
from google.auth.transport import requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/chronicle-backstory']

# The apikeys-demo.json file contains the customer's OAuth 2 credentials.
# SERVICE_ACCOUNT_FILE is the full path to the apikeys-demo.json file
# ToDo: Replace this with the full path to your OAuth2 credentials
SERVICE_ACCOUNT_FILE = '/customer-keys/apikeys-demo.json'

# Create a credential using the Google Developer Service Account Credential and Backstory API
# Scope.
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build a requests Session Object to make authorized OAuth requests.
http_session = requests.AuthorizedSession(credentials)

# Your endpoint GET|POST|PATCH|etc. code will vary below

# Reference List example (for US region)
url = 'https://backstory.googleapis.com/v2/lists/COLDRIVER_SHA256'

# You might need another regional endpoint for your API call; see
# https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints

# requests GET example
response = http_session.request("GET", url)

# POST example uses json
body = {
  "foo": "bar"
}
response = http_session.request("POST", url, json=body)

# PATCH example uses params and json
params = {
  "foo": "bar"
}
response = http_session.request("PATCH", url, params=params, json=body)

# For more complete examples, see:
# https://github.com/chronicle/api-samples-python/
Data Export API reference
The following sections describe the Backstory Data Export API methods.
CreateDataExport
Creates a new data export. You can export a maximum of 10 TB of compressed data per request. A maximum of three requests can be in process at any time. Depending on its size and start time, a data export typically takes several minutes to several hours to complete.
Request
Following is a use case for a request.
Request Body
{
  "startTime": "Start, inclusive time from the time range",
  "endTime": "Last, exclusive time from the time range",
  "logType": "An individual log type or 'ALL_TYPES' for all log types",
  "gcsBucket": "Path to the customer-provided Google Cloud Storage bucket in projects/<project-id>/buckets/<bucket-name>" format,
}
Parameters
Parameter Name
Type
Description
startTime
google.protobuf.Timestamp
(Optional): Start, inclusive time from the time range.
If not specified, the value is UNIX epoch time starting on January 1st, 1970 at UTC.
endTime
google.protobuf.Timestamp
(Optional): Last, exclusive time from the time range.
If not specified, the value is the current timestamp.
logType
string
(Required): Individual log type or
ALL_TYPES
for all log types.
gcsBucket
string
(Required): Path to the customer-provided Google Cloud Storage bucket in:  \
projects/<project-id>/buckets/ \
<bucket-name>" format
Sample Request
https://backstory.googleapis.com/v1/tools/dataexport
{
  "startTime": "2020-03-01T00:00:00Z",
  "endTime": "2020-03-15T00:00:00Z",
  "logType": "CB_EDR",
  "gcsBucket": "projects/chronicle-test/buckets/dataexport-test-bucket"
}
Sample Response
{
  "dataExportId": "d828bcec-21d3-4ecd-910e-0a934f0bd074",
  "startTime": "2020-03-01T00:00:00Z",
  "endTime": "2020-03-15T00:00:00Z",
  "logType": "CB_EDR",
  "gcsBucket": "projects/chronicle-test/buckets/dataexport-test-bucket",
  "dataExportStatus": {"stage": "IN_QUEUE"}
}
GetDataExport
Returns an existing data export.
Request
GET https://backstory.googleapis.com/v1/tools/dataexport/{data_export_id}
Parameters
Parameter Name
Type
Description
dataExportId
string
UUID representing the data export request.
Sample Request
https://backstory.googleapis.com/v1/tools/dataexport/{data_export_id}
Sample Response
{
  "dataExportId": "d828bcec-21d3-4ecd-910e-0a934f0bd074",
  "startTime": "2020-03-01T00:00:00Z",
  "endTime": "2020-03-15T00:00:00Z",
  "logType": "CB_EDR",
  "gcsBucket": "projects/chronicle-test/buckets/dataexport-test-bucket",
  "dataExportStatus": {"stage": "IN_QUEUE"}
}
CancelDataExport
Cancels an existing data export request.
Request
POST https://backstory.googleapis.com/v1/tools/dataexport/{data_export_id}:cancel
Request Body
{
  "dataExportId": "The UUID representing the data export request to be canceled"
}
Parameters
Parameter Name
Type
Description
dataExportId
string
UUID representing the data export request to be canceled.
Sample Request
https://backstory.googleapis.com/v1/tools/dataexport/d828bcec-21d3-4ecd-910e-0a934f0bd074:cancel
Sample Response
{
  "dataExportId": "d828bcec-21d3-4ecd-910e-0a934f0bd074",
  "startTime": "2020-03-01T00:00:00Z",
  "endTime": "2020-03-15T00:00:00Z",
  "logType": "CB_EDR",
  "gcsBucket": "projects/chronicle-test/buckets/dataexport-test-bucket",
  "dataExportStatus": {"stage": "CANCELLED"}
}
