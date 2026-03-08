# Collect Signal Sciences WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/signal-sciences-waf/  
**Scraped:** 2026-03-05T09:28:14.359616Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Signal Sciences WAF logs
Supported in:
Google secops
SIEM
This document explains how to ingest Signal Sciences WAF logs to
Google Security Operations using Google Cloud Storage. The parser transforms
Signal Sciences logs from their JSON format into Chronicle's Unified Data Model
(UDM). It handles two primary message structures: "RPC.PreRequest/PostRequest"
messages are parsed using Grok patterns, while other messages are processed as
JSON objects, extracting relevant fields and mapping them to the UDM schema.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
VPC Flow is set up and active in your Google Cloud environment
Privileged access to Signal Sciences WAF
Create a Google Cloud Storage Bucket
Sign in to the Google Cloud console.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
On the
Create a bucket
page, enter your bucket information. After each of the following steps, click
Continue
to proceed to the next step:
In the
Get started
section, do the following:
Enter a unique name that meets the bucket name requirements (for example,
vpcflow-logs
).
To enable hierarchical namespace, click the expander arrow to expand the
Optimize for file oriented and data-intensive workloads
section, and then select
Enable Hierarchical namespace on this bucket
.
To add a bucket label, click the expander arrow to expand the
Labels
section.
Click
Add label
, and specify a key and a value for your label.
In the
Choose where to store your data
section, do the following:
Select a
Location type
.
Use the location type's menu to select a
Location
where object data within your bucket will be permanently stored.
To set up cross-bucket replication, expand the
Set up cross-bucket replication
section.
In the
Choose a storage class for your data
section, either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management of your bucket's data.
In the
Choose how to control access to objects
section, select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the expander arrow labeled
Data encryption
, and select a
Data encryption method
.
Click
Create
.
Configure a Signal Sciences WAF API key
Sign in to the
Signal Sciences WAF
web UI.
Go to
My Profile
>
API Access Tokens
.
Click
Add API access token
.
Provide a unique, descriptive name (for example,
Google SecOps
).
Click
Create API access token
.
Copy and save the token in a secure location.
Click
I understand
to finish creating the token.
Deploy a script on a Linux host to pull logs from Signal Sciences and store it in Google Cloud
Sign in to the
Linux host
using SSH.
Install python lib to store the Signal Sciences WAF JSON to a Cloud Storage bucket:
pip
install
google-cloud-storage
Set this
env variable
to call the JSON file that has the credentials from Google Cloud:
export
GOOGLE_APPLICATION_CREDENTIALS
=
"path/to/your/service-account-key.json"
Configure the following env variables because this information must not be hardcoded:
export
SIGSCI_EMAIL
=
<Signal_Sciences_account_email>
export
SIGSCI_TOKEN
=
<Signal_Sciences_API_token>
export
SIGSCI_CORP
=
<Corporation_name_in_Signal_Sciences>
Run the following script:
import sys
import requests
import os
import calendar
import json
from datetime import datetime, timedelta
from google.cloud import storage

# Check if all necessary environment variables are set

if 'SIGSCI_EMAIL' not in os.environ or 'SIGSCI_TOKEN' not in os.environ or 'SIGSCI_CORP' not in os.environ:
print("ERROR: You need to define SIGSCI_EMAIL, SIGSCI_TOKEN, and SIGSCI_CORP environment variables.")
print("Please fix and run again. Existing...")
sys.exit(1)  # Exit if environment variables are not set

# Define the Google Cloud Storage bucket name and output file name

bucket_name = 'Your_GCS_Bucket'  # Replace with your GCS bucket name
output_file_name = 'signal_sciences_logs.json'

# Initialize Google Cloud Storage client

storage_client = storage.Client()

# Function to upload data to Google Cloud Storage

def upload_to_gcs(bucket_name, data, destination_blob_name):
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_string(data, content_type='application/json')
    print(f"Data uploaded to {destination_blob_name} in bucket {bucket_name}")

# Signal Sciences API information

api_host = 'https://dashboard.signalsciences.net'
# email = 'user@domain.com'  # Signal Sciences account email
# token = 'XXXXXXXX-XXXX-XXX-XXXX-XXXXXXXXXXXX'  # API token for authentication
# corp_name = 'Domain'  # Corporation name in Signal Sciences
# site_names = ['testenv']  # Replace with your actual site names

# List of comma-delimited sites that you want to extract data from

site_names = [ 'site123', 'site345' ]        # Define all sites to pull logs from

email = os.environ.get('SIGSCI_EMAIL')       # Signal Sciences account email
token = os.environ.get('SIGSCI_TOKEN')       # API token for authentication
corp_name = os.environ.get('SIGSCI_CORP')    # Corporation name in Signal Sciences

# Calculate the start and end timestamps for the previous hour in UTC

until_time = datetime.utcnow().replace(minute=0, second=0, microsecond=0)
from_time = until_time - timedelta(hours=1)
until_time = calendar.timegm(until_time.utctimetuple())
from_time = calendar.timegm(from_time.utctimetuple())

# Prepare HTTP headers for the API request

headers = {
    'Content-Type': 'application/json',
    'x-api-user': email,
    'x-api-token': token
}

# Collect logs for each site

collected_logs = []

for site_name in site_names:
    url = f"{api_host}/api/v0/corps/{corp_name}/sites/{site_name}/feed/requests?from={from_time}&until={until_time}"
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error fetching logs: {response.text}", file=sys.stderr)
            break

        # Parse the JSON response

        data = response.json()
        collected_logs.extend(data['data'])  # Add the log messages to our list

        # Pagination: check if there is a next page

        next_url = data.get('next', {}).get('uri')
        if not next_url:
            break
        url = api_host + next_url

# Convert the collected logs to a newline-delimited JSON string

json_data = '\n'.join(json.dumps(log) for log in collected_logs)

# Save the newline-delimited JSON data to a GCS bucket

upload_to_gcs(bucket_name, json_data, output_file_name)
Set up feeds
To configure a feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
Signal Sciences WAF Logs
).
Select
Google Cloud Storage
as the
Source type
.
Select
Signal Sciences WAF
as the
Log type
.
Click
Get Service Account
as the
Chronicle Service Account
.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Google Cloud storage bucket URL in
gs://my-bucket/<value>/
format. This URL must end with a trailing forward slash (/).
URI Is A
: Select
Directory which includes subdirectories
.
Source deletion options
: Select the deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
UDM mapping table
Log Field
UDM Mapping
Logic
CLIENT-IP
target.ip
Extracted from the
CLIENT-IP
header field.
CLIENT-IP
target.port
Extracted from the
CLIENT-IP
header field.
Connection
security_result.about.labels
The value is taken from the raw log
Connection
field and mapped to
security_result.about.labels
.
Content-Length
security_result.about.labels
The value is taken from the raw log
Content-Length
field and mapped to
security_result.about.labels
.
Content-Type
security_result.about.labels
The value is taken from the raw log
Content-Type
field and mapped to
security_result.about.labels
.
created
metadata.event_timestamp
The value is taken from the raw log
created
field and mapped to
metadata.event_timestamp
.
details.headersIn
security_result.about.resource.attribute.labels
The value is taken from the raw log
details.headersIn
field and mapped to
security_result.about.resource.attribute.labels
.
details.headersOut
security_result.about.resource.attribute.labels
The value is taken from the raw log
details.headersOut
field and mapped to
security_result.about.resource.attribute.labels
.
details.id
principal.process.pid
The value is taken from the raw log
details.id
field and mapped to
principal.process.pid
.
details.method
network.http.method
The value is taken from the raw log
details.method
field and mapped to
network.http.method
.
details.protocol
network.application_protocol
The value is taken from the raw log
details.protocol
field and mapped to
network.application_protocol
.
details.remoteCountryCode
principal.location.country_or_region
The value is taken from the raw log
details.remoteCountryCode
field and mapped to
principal.location.country_or_region
.
details.remoteHostname
target.hostname
The value is taken from the raw log
details.remoteHostname
field and mapped to
target.hostname
.
details.remoteIP
target.ip
The value is taken from the raw log
details.remoteIP
field and mapped to
target.ip
.
details.responseCode
network.http.response_code
The value is taken from the raw log
details.responseCode
field and mapped to
network.http.response_code
.
details.responseSize
network.received_bytes
The value is taken from the raw log
details.responseSize
field and mapped to
network.received_bytes
.
details.serverHostname
principal.hostname
The value is taken from the raw log
details.serverHostname
field and mapped to
principal.hostname
.
details.serverName
principal.asset.network_domain
The value is taken from the raw log
details.serverName
field and mapped to
principal.asset.network_domain
.
details.tags
security_result.detection_fields
The value is taken from the raw log
details.tags
field and mapped to
security_result.detection_fields
.
details.tlsCipher
network.tls.cipher
The value is taken from the raw log
details.tlsCipher
field and mapped to
network.tls.cipher
.
details.tlsProtocol
network.tls.version
The value is taken from the raw log
details.tlsProtocol
field and mapped to
network.tls.version
.
details.userAgent
network.http.user_agent
The value is taken from the raw log
details.userAgent
field and mapped to
network.http.user_agent
.
details.uri
network.http.referral_url
The value is taken from the raw log
details.uri
field and mapped to
network.http.referral_url
.
eventType
metadata.product_event_type
The value is taken from the raw log
eventType
field and mapped to
metadata.product_event_type
.
headersIn
security_result.about.labels
The value is taken from the raw log
headersIn
field and mapped to
security_result.about.labels
.
headersOut
security_result.about.labels
The value is taken from the raw log
headersOut
field and mapped to
security_result.about.labels
.
id
principal.process.pid
The value is taken from the raw log
id
field and mapped to
principal.process.pid
.
message
metadata.description
The value is taken from the raw log
message
field and mapped to
metadata.description
.
method
network.http.method
The value is taken from the raw log
method
field and mapped to
network.http.method
.
ModuleVersion
metadata.ingestion_labels
The value is taken from the raw log
ModuleVersion
field and mapped to
metadata.ingestion_labels
.
msgData.actions
security_result.action
The value is taken from the raw log
msgData.actions
field and mapped to
security_result.action
.
msgData.changes
target.resource.attribute.labels
The value is taken from the raw log
msgData.changes
field and mapped to
target.resource.attribute.labels
.
msgData.conditions
security_result.description
The value is taken from the raw log
msgData.conditions
field and mapped to
security_result.description
.
msgData.detailLink
network.http.referral_url
The value is taken from the raw log
msgData.detailLink
field and mapped to
network.http.referral_url
.
msgData.name
target.resource.name
The value is taken from the raw log
msgData.name
field and mapped to
target.resource.name
.
msgData.reason
security_result.summary
The value is taken from the raw log
msgData.reason
field and mapped to
security_result.summary
.
msgData.sites
network.http.user_agent
The value is taken from the raw log
msgData.sites
field and mapped to
network.http.user_agent
.
protocol
network.application_protocol
The value is taken from the raw log
protocol
field and mapped to
network.application_protocol
.
remoteCountryCode
principal.location.country_or_region
The value is taken from the raw log
remoteCountryCode
field and mapped to
principal.location.country_or_region
.
remoteHostname
target.hostname
The value is taken from the raw log
remoteHostname
field and mapped to
target.hostname
.
remoteIP
target.ip
The value is taken from the raw log
remoteIP
field and mapped to
target.ip
.
responseCode
network.http.response_code
The value is taken from the raw log
responseCode
field and mapped to
network.http.response_code
.
responseSize
network.received_bytes
The value is taken from the raw log
responseSize
field and mapped to
network.received_bytes
.
serverHostname
principal.hostname
The value is taken from the raw log
serverHostname
field and mapped to
principal.hostname
.
serverName
principal.asset.network_domain
The value is taken from the raw log
serverName
field and mapped to
principal.asset.network_domain
.
tags
security_result.detection_fields
The value is taken from the raw log
tags
field and mapped to
security_result.detection_fields
.
timestamp
metadata.event_timestamp
The value is taken from the raw log
timestamp
field and mapped to
metadata.event_timestamp
.
tlsCipher
network.tls.cipher
The value is taken from the raw log
tlsCipher
field and mapped to
network.tls.cipher
.
tlsProtocol
network.tls.version
The value is taken from the raw log
tlsProtocol
field and mapped to
network.tls.version
.
URI
target.url
The value is taken from the raw log
URI
field and mapped to
target.url
.
userAgent
network.http.user_agent
The value is taken from the raw log
userAgent
field and mapped to
network.http.user_agent
.
uri
network.http.referral_url
The value is taken from the raw log
uri
field and mapped to
network.http.referral_url
.
X-ARR-SSL
network.tls.client.certificate.issuer
The value is extracted from the
X-ARR-SSL
header field using grok and kv filters.
metadata.event_type
The event type is determined by the parser based on the presence of target and principal information. If both target and principal are present, the event type is
NETWORK_HTTP
. If only principal is present, the event type is
STATUS_UPDATE
. Otherwise, the event type is
GENERIC_EVENT
.
metadata.log_type
The value is hardcoded to
SIGNAL_SCIENCES_WAF
.
metadata.product_name
The value is hardcoded to
Signal Sciences WAF
.
metadata.vendor_name
The value is hardcoded to
Signal Sciences
.
principal.asset.hostname
The value is taken from the
principal.hostname
field.
target.asset.hostname
The value is taken from the
target.hostname
field.
target.asset.ip
The value is taken from the
target.ip
field.
target.user.user_display_name
The value is extracted from the
message_data
field using a grok filter.
target.user.userid
The value is extracted from the
message_data
field using a grok filter.
Need more help?
Get answers from Community members and Google SecOps professionals.
