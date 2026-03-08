# Ingestion API

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api/  
**Scraped:** 2026-03-05T09:16:40.590966Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Ingestion API
Supported in:
Google secops
SIEM
This document explains how to use Backstory Ingestion to forward logs directly to your Google Security Operations instance, eliminating the need for additional hardware or software (for example, forwarders) in your environment.
The Ingestion method is a RESTful API with a JSON payload. Managed Security Service Providers (MSSPs) and
Technology Partners
can develop systems to call Ingestion directly and forward logs to Google SecOps.
The Ingestion supports:
UDM events
Unstructured logs
Log types retrieval
You can forward your data to Google SecOps using either of the following types of Ingestion endpoints:
Unified Data Model (UDM) event
Unstructured log
If you have formatted your log data using Google SecOps UDM, you can forward UDM events to your Google SecOps account using the UDM API endpoint. Since UDM events are standardized, Google SecOps is better able to process and interpret the data, increasing Google SecOps's ability to recognize security compromises and threats within your enterprise. See
Format log data as UDM
for information about converting raw logs to UDM.
You can also forward your data to Google SecOps as unstructured logs using the unstructured log API endpoints. Your unstructured log data is normalized within the Google SecOps infrastructure and made available to you through the Google SecOps UI. However, some information may be difficult to extract from the unstructured log data and might only be searchable using Raw Log Scan.
When the Ingestion API takes a batch of logs, it generates a
batch ID for those logs. If the batch ID of those logs is a duplicate of an
existing batch ID, then the new batch of logs is not forwarded to the
Google SecOps instance. The deduplication of the batch depends on the batch
ID, which is the same for different batches if the logs contained in those
batches are the same. Deduplication occurs across feeds when the Customer ID, raw log payload, and UDM data are identical for a customer. The Log Type is not included in the deduplication hash.
Whenever possible, we recommend forwarding your data to Google SecOps as UDM events.
Get API authentication credentials
Your Google Security Operations representative provides you with a
Google Developer
service account
credential to enable the API client to communicate with the API, and share its credentials (JSON key) so your API client can authenticate to the API.
You also must provide the Auth Scope when initializing your API client. OAuth 2.0 uses
a scope to limit an application's access to an account. When an application requests a scope,
the access token issued to the application is limited to the scope granted.
Use the following scope to initialize your Google API client:
https://www.googleapis.com/auth/malachite-ingestion
Python example
The following Python example demonstrates how to use OAuth 2.0 credentials and the
HTTP client, with
google.oauth2
and
googleapiclient
. Note, you may need
to use the OAuth 2.0 credentials contained in the
apikeys-demo.json
file.
# Imports required for the sample - Google Auth and API Client Library.
# Install these packages from https://pypi.org/project/google-api-python-client/
# or run from your terminal: pip install google-api-python-client
import json

from google.auth.transport import requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/malachite-ingestion']

# The apikeys-demo.json file contains the OAuth 2 credentials.
# ING_SERVICE_ACCOUNT_FILE is the full path to the ingestion apikeys.json file.
# ToDo: Replace with the full path to the OAuth 2.0 credentials file.
ING_SERVICE_ACCOUNT_FILE = '/customer-keys/apikeys.json'

# Customer ID is available at /settings/profile on your Google Security Operations.
CUSTOMER_ID=
CUSTOMER_ID
# Create a credential using an Ingestion Service Account Credential file
# and the Google Security Operations API Scope.
credentials = service_account.Credentials.from_service_account_file(ING_SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build a requests Session Object to make authorized OAuth requests.
http_session = requests.AuthorizedSession(credentials)

# UDM Event example (example: US region)
url = 'https://malachiteingestion-pa.googleapis.com/v2/udmevents:batchCreate'

# For other regions, you may need to use another regional endpoint for your API call; see
# https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints

# json_events are a collection of UDM events in (serialized) JSON format.

body = {
    "customerId": CUSTOMER_ID,
    "events": json.loads(json_events),
}
response = http_session.request("POST", url, json=body)

# For more complete examples, see:
# https://github.com/chronicle/api-samples-python/blob/master/ingestion/create_entities.py
# https://github.com/chronicle/api-samples-python/blob/master/ingestion/create_udm_events.py
# https://github.com/chronicle/api-samples-python/blob/master/ingestion/create_unstructured_log_entries.py
The Service Account Credential provided to you corresponds to one Google SecOps instance. The requests that are issued to the Ingestion API include a field,
customer_id
, which is a unique identifier for a Google SecOps instance. This is provided by your Google SecOps representative. The credential used when issuing requests and the unique identifier must correspond.
Regional Endpoints
Google SecOps provides regional endpoints for each API.
São Paulo
—
https://southamerica-east1-malachiteingestion-pa.googleapis.com
Canada
—
https://northamerica-northeast2-malachiteingestion-pa.googleapis.com
Dammam
—
https://me-central2-malachiteingestion-pa.googleapis.com
Doha
—
https://me-central1-malachiteingestion-pa.googleapis.com
Europe Multi-Region
—
https://europe-malachiteingestion-pa.googleapis.com
Frankfurt
—
https://europe-west3-malachiteingestion-pa.googleapis.com
Jakarta
—
https://asia-southeast2-malachiteingestion-pa.googleapis.com
Johannesburg
—
https://africa-south1-malachiteingestion-pa.googleapis.com
London
—
https://europe-west2-malachiteingestion-pa.googleapis.com
Mumbai
—
https://asia-south1-malachiteingestion-pa.googleapis.com
Paris
—
https://europe-west9-malachiteingestion-pa.googleapis.com
Warsaw
—
https://europe-central2-malachiteingestion-pa.googleapis.com
Singapore
—
https://asia-southeast1-malachiteingestion-pa.googleapis.com
Sydney
—
https://australia-southeast1-malachiteingestion-pa.googleapis.com
Tel Aviv
—
https://me-west1-malachiteingestion-pa.googleapis.com
Tokyo
—
https://asia-northeast1-malachiteingestion-pa.googleapis.com
Turin
—
https://europe-west12-malachiteingestion-pa.googleapis.com
United States Multi-Region
—
https://malachiteingestion-pa.googleapis.com
Zurich
—
https://europe-west6-malachiteingestion-pa.googleapis.com
Ingestion API reference
This sections describes how to use the Ingestion API methods.
udmevents
Use this method to forward UDM events to Google SecOps in batches.
The
udmevents
endpoint ingests pre-parsed telemetry that has been structured into UDM events. Because these events are already normalized, they bypass the internal Configuration-Based Normalizer (CBN) parsing layer and move directly to the indexing and rules engine. Use this ingestion path if you manage your own data transformation before transmission. This approach reduces end-to-end latency by eliminating your need for server-side parsing.
Request
POST https://malachiteingestion-pa.googleapis.com/v2/udmevents:batchCreate
Request body
The following example illustrates how you could format your log data using the
udmevents
API endpoint. It shows how to format your enterprise log data using UDM.
{
  "customer_id": "c8c65bfa-5f2c-42d4-9189-64bb7b939f2c",
  "events": [
    {
      "metadata": {
        "event_timestamp": "2019-10-22T12:00:00.000Z",
        "event_type": "USER_LOGIN",
        "product_name": "Acme SSO",
        "vendor_name": "Acme"
      },
      "principal": {
        "ip": [
          "10.1.2.3"
        ]
      },
      "target": {
        "application": "Acme Connect",
        "user": {
          "user_display_name": "Mary Jane",
          "userid": "mary@altostrat.com"
        }
      },
      "extensions": {
        "auth": {
          "type": "MACHINE",
          "mechanism": [
            "NETWORK"
          ]
        }
      }
    },
    {
      "metadata": {
        "event_timestamp": "2019-10-23T04:00:00.000Z",
        "event_type": "NETWORK_HTTP",
        "product_name": "Acme Proxy",
        "vendor_name": "Acme"
      },
      "network": {
        "http": {
          "method": "GET",
          "response_code": 200
        }
      },
      "principal": {
        "hostname": "host0",
        "ip": [
          "10.1.2.3"
        ],
        "port": 60000
      },
      "target": {
        "hostname": "www.altostrat.com",
        "ip": [
          "198.51.100.68"
        ],
        "port": 443,
        "url": "www.altostrat.com/images/logo.png"
      }
    }
  ]
}
Body parameters
Field
Value
Required
Description
customer_id
string
Yes
Unique identifier (UUID) corresponding to a particular Google SecOps instance. Provided by your Google SecOps representative.
events[]
array
Yes
Array of UDM events.
Response
You shouldn't receive a response unless there's an error in the method syntax.
unstructuredlogentries
Use this method to forward unstructured log entries to Google SecOps one batch at a time.
Each batch of log data has a maximum size limit of 1 MB (uncompressed). Use only one timestamp format per batch—either
ts_epoch_microseconds
or
ts_rfc3339
, but not both.
If no separate timestamp is provided, ensure that a timestamp is included within the
log_text
field.
Request
POST https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
Request body
The following example illustrates how you could format your log data using the unstructuredlogentries API endpoint. It shows how to format three BIND DNS logs.
When sending the timestamp as a separate name-value pair, use the same key for all entries in the batch. For example, in a single batch, don't use
ts_epoch_microseconds
for one entry and
ts_rfc3339
for another entry.
For example, this payload will return an error because it includes both
ts_epoch_microseconds
and
ts_rfc3339
.
{
  "customer_id": "c8c65bfa-5f2c-42d4-9189-64bb7b939f2c",
  "log_type": "BIND_DNS",
  "labels" : [
    {
      "key" : "key_name_one",
      "rbac_enabled" : "true",
      "value" : "value_one"
    },
    {
      "key" : "key_name_two",
      "rbac_enabled" : "true",
      "value" : "value_two"
    }
  ]
  "entries": [
    {
      "log_text": "26-Feb-2019 13:35:02.187 client 10.120.20.32#4238: query: altostrat.com IN A + (203.0.113.102)",
      "ts_epoch_microseconds": 1551188102187000
    },
    {
      "log_text": "26-Feb-2019 13:37:04.523 client 10.50.100.33#1116: query: examplepetstore.com IN A + (203.0.113.102)",
      "ts_rfc3339": "2019-26-02T13:37:04.523-08:00"
    },
    {
      "log_text": "26-Feb-2019 13:39:01.115 client 10.1.2.3#3333: query: www.example.com IN A + (203.0.113.102)"
    }
  ];
}
Body parameters
Field
Value
Required
Description
customer_id
string
Yes
Unique identifier (UUID) corresponding to a particular Google SecOps instance. Provided by your Google SecOps representative.
log_type
string
Yes
Identifies the log entries in the batch (for example,  WINDOWS_DNS).
namespace
string
Yes
User-configured environment namespace to identify the data domain the logs originated from. Use namespace as a tag to identify the appropriate data domain for indexing and enrichment functionality.
entries[]
array
Yes
Array of objects containing the fields for the raw log and its timestamp.
entries[].log_text
string
Yes
Text of the raw log entry. This shouldn't contain any binary data and should only use UTF-8 strings.
entries[].ts_epoch_microseconds
uint64
Optional
UNIX timestamp in microseconds associated with the log entry.
entries[].ts_rfc3339
string
Optional
Timestamp associated with the log entry in RFC 3339 format.
labels[]
array
Optional
Array of objects containing the key-value pairs for labels to be applied to the logs.
labels[].key
string
Optional
Name of a key for applying a label.
labels[].value
string
Optional
Value for applying a label.
Response
You shouldn't receive a response unless there's an error in the method syntax.
createentities
Creates entities. You are limited to 4 MB of data per request.
Request
POST https://malachiteingestion-pa.googleapis.com/v2/entities:batchCreate
Request body
{
  "customer_id": "<customer UUID>",
  "log_type": "<log type goes here>",
  "entities": [<array of Entities>],
}
Body parameters
Field
Value
Required
Description
customer_id
string
Yes
Unique identifier (UUID) corresponding to a particular Google SecOps instance. Provided by your Google SecOps representative.
log_type
string
Yes
Any log_type value returned by the logtypes endpoint.
entities[]
array
Yes
Array of Entities.
Sample request body
{
 "log_type": "AZURE_AD_CONTEXT",
 "entities": [{
   "metadata": {
      "collected_timestamp":"2021-11-14T15:30:18.142265Z",
      "entity_type": "USER",
      "vendor_name": "vendor",
      "product_name": "product"
   },
   "entity": {
      "user": {
        "userid": "johndoe",
        "product_object_id": "doejohn"
      }
   }
  },
  {
   "metadata": {
      "collected_timestamp":"2021-11-14T16:30:18.142265Z",
      "entity_type": "USER",
      "vendor_name": "vendor",
      "product_name": "product"
   },
   "entity": {
      "user": {
        "userid": "janedoe",
        "product_object_id": "doejane"
      }
   }
  }]
}
Response
Returns an empty JSON with 200 OK, indicating the operation has completed successfully.
logtypes
Use this method to retrieve a list of supported log types. The log types are formatted using the following fields:
Request
GET https://malachiteingestion-pa.googleapis.com/v2/logtypes
Response
The following example illustrates the format of the information returned when calling the logtypes API endpoint.
{
  "logtypes": [
    {
     "log_type": "BIND_DNS",
     "description": "BIND DNS Server"
    },
    {
      "log_type": "WINDOWS_DNS",
      "description": "Windows DNS"
    },
    {
      "log_type": "WINDOWS_DHCP",
      "description": "Windows DHCP"
    },
    {
      "log_type": "WINEVTLOG",
      "description": "Windows Event Log"
    }
  ]
}
Response fields
Field
Value
Description
logtypes[]
array
Returns an array of the supported log types.
logtypes[].log_type
string
Log type. Appears in the response only.
logtypes[].description
string
Human readable description of the log type. Appears in the response only.
logtypes[].index
uint64
Index of the log type. Appears in the response only.
Frequently asked questions
What is the maximum batch size (per HTTP request)?
4 MB when uncompressed (in case the incoming batch is compressed).
Can a customer create an allowlist to include certain public IP addresses that are allowed to connect to the collector API endpoint? Or do you support other forms of client authorization?
Google SecOps doesn't support IP allowlisting. Any client with a valid API key can connect.
Does the API endpoint vary depending on the region?
Yes. Your API endpoint will vary depending on where your customer account is provisioned. See
Regional Endpoints
.
What should the request timeout be?
Clients should use a request timeout of 90 seconds.
What should we do if an HTTP request fails? What are the error codes?
See
AIP-193 Errors
, specifically the following:
Clients should retry on 5XX errors with exponential backoff. The minimum delay should be 1s unless it is documented otherwise. For 429 errors, the client may retry with minimum 30s delay. For all other errors, retry may not be applicable.
Do you support standard HTTP GZIP compression (for example, Accept-Encoding: gzip header)?
Yes, Google SecOps supports standard HTTP GZIP compression.
What time format should my raw logs follow?
Most of the prebuilt parsers expect one of the following time formats:
RFC3339
,
UNIX
and
ISO8601
.
Is there a default timezone if it's missing in the raw log timestamp?
Most of the prebuilt parsers can extract timezone information correctly if it's included in raw logs. In raw logs where the timezone information is missing, the parser applies the
UTC
timezone to the timestamp in the raw log. This may cause the raw logs to appear as delayed or early during a UDM search. For this reason, it's recommended to include proper timezone information from the source while configuring the syslogs. This is especially important for logs ingested using the Ingestion API, Forwarder and Bindplane agents.
