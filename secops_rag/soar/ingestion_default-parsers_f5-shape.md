# Collect F5 Shape logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-shape/  
**Scraped:** 2026-03-05T09:55:32.194238Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect F5 Shape logs
Supported in:
Google secops
SIEM
This document explains how to ingest F5 Shape logs to Google Security Operations using Google Cloud Storage V2.
F5 Distributed Cloud Bot Defense (formerly Shape Security) protects applications from automated attacks by identifying and mitigating malicious bots. Bot Defense uses JavaScript and native Mobile SDKs to collect telemetry from client browsers and mobile devices, examining this telemetry before requests reach your application. The service provides integrated dashboards and reporting to view detailed information about analyzed traffic, including security events, access logs, and audit logs.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Privileged access to F5 Distributed Cloud Console
An F5 Distributed Cloud Account with Multi-Cloud Network Connect or Shared Configuration service access
Create Google Cloud Storage bucket
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
f5-xc-logs
).
Location type
Choose based on your needs (Region, Dual-region, Multi-region).
Location
Select the location (for example,
us-central1
).
Storage class
Standard (recommended for frequently accessed logs).
Access control
Uniform (recommended).
Protection tools
Optional: Enable object versioning or retention policy.
Click
Create
.
Generate F5 Shape API credentials
F5 Distributed Cloud uses API Certificates (mTLS) or API Tokens for authentication. API Certificates are recommended for enhanced security.
Create API Certificate
Sign in to the
F5 Distributed Cloud Console
.
From the Console home page, select
Administration
.
In the left navigation menu, go to
Personal Management
>
Credentials
.
Click
Add Credentials
.
In the
Metadata
section, enter a
Name
for your certificate (for example,
secops-integration
).
From the
Credential Type
list, select
API Certificate
.
Enter a
Password
and confirm it in the
Confirm Password
field.
Select an
Expiry Date
from the calendar list.
Click
Download
to generate and download the certificate in
.p12
file format.
Save the downloaded certificate file and password securely for later use.
Create GCP Cloud Credentials in F5 Distributed Cloud
F5 Distributed Cloud requires Google Cloud service account credentials to write logs to your GCS bucket.
Create Google Cloud service account
In the
GCP Console
, go to
IAM & Admin
>
Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter
f5-xc-log-writer
(or your preferred name).
Service account description
: Enter
Service account for F5 Distributed Cloud to write logs to GCS
.
Click
Create and Continue
.
In the
Grant this service account access to project
section:
Click
Select a role
.
Search for and select
Storage Object Admin
.
Click
Continue
.
Click
Done
.
Grant IAM permissions on GCS bucket
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (for example,
f5-xc-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
f5-xc-log-writer@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create service account key
In the
GCP Console
, go to
IAM & Admin
>
Service Accounts
.
Find the service account (for example,
f5-xc-log-writer
) and click it.
Go to the
Keys
tab.
Click
Add Key
>
Create new key
.
Select
JSON
as the key type.
Click
Create
.
The JSON key file will be downloaded automatically. Save this file securely.
Add Google Cloud Cloud Credentials to F5 Distributed Cloud
In the
F5 Distributed Cloud Console
, from the home page, select
Multi-Cloud Network Connect
or
Shared Configuration
.
In the left navigation menu, go to
Manage
>
Site Management
>
Cloud Credentials
.
Click
Add Cloud Credentials
.
In the
Metadata
section, enter a
Name
(for example,
gcp-secops-logs
).
From the
Cloud Credentials Type
list, select
GCP Credentials
.
In the
GCP Credentials
section, click
Configure
.
In the
Service Account Key
section:
From the
Secret Type
list, select
Blindfolded Secret
.
From the
Action
list, select
Blindfold New Secret
.
From the
Policy Type
list, select
Built-in
.
In the
Secret to Blindfold
field, paste the entire contents of the JSON key file you downloaded.
Click
Apply
.
Click
Save and Exit
.
Configure Global Log Receiver for GCS
F5 Distributed Cloud Global Log Receiver streams logs to GCS every 5 minutes in NDJSON format (newline-delimited JSON).
Create Global Log Receiver
In the
F5 Distributed Cloud Console
, from the home page, select
Multi-Cloud Network Connect
or
Shared Configuration
.
For
Multi-Cloud Network Connect
: Go to
Manage
>
Log Management
>
Global Log Receiver
.
For
Shared Configuration
: Go to
Manage
>
Global Log Receiver
.
Click
Add Global Log Receiver
.
In the
Metadata
section, enter a
Name
(for example,
secops-gcs-receiver
).
Optionally, add
Labels
and a
Description
.
From the
Log Type
list, select the log types you want to collect:
Request Logs
: HTTP access logs from load balancers
Security Events
: Bot Defense and WAF security events
Audit Logs
: Configuration and administrative audit logs
DNS Request Logs
: DNS query logs
From the
Log Message Selection
list:
If using
Multi-Cloud Network Connect
service, select
Select logs from current namespace
(system namespace).
If using
Shared Configuration
service, choose one of the following:
Select logs from current namespace
: Sends logs from the shared namespace only.
Select logs from all namespaces
: Sends logs from all namespaces.
Select logs in specific namespaces
: Enter specific namespace names and click
Add item
to add more.
From the
Receiver Configuration
list, select
GCP Bucket
.
In the
GCP Bucket
section, provide the following configuration:
GCP Bucket Name
: Enter your GCS bucket name (for example,
f5-xc-logs
).
GCP Cloud Credentials
: From the list, select the cloud credentials you created (for example,
gcp-secops-logs
).
Configure advanced settings (optional)
Click the
Show Advanced Fields
toggle.
In the
Batch Options
section, configure the following (optional):
Batch Timeout Options
: Select
Timeout Seconds
and enter a value (default:
300
seconds).
Batch Max Events
: Select
Max Events
and enter a value between 32 and 2000 (optional).
Batch Bytes
: Select
Max Bytes
and enter a value between 4096 and 1048576 (default:
10485760
bytes / 10 MB).
Complete and test the configuration
Click
Save and Exit
to create the Global Log Receiver.
In the
Global Log Receiver
list, find your receiver (for example,
secops-gcs-receiver
).
In the
Actions
column, click the three dots
...
and select
Test Connection
.
Wait for the test to complete. A success message indicates the connection is working.
Verify logs are being written to GCS:
Go to
Cloud Storage
>
Buckets
in the GCP Console.
Click your bucket name (for example,
f5-xc-logs
).
Within 5-10 minutes, you should see folders created with the following structure:
Daily folder:
YYYY-MM-DD/
Hourly subfolder:
YYYY-MM-DD/HH/
Log files:
YYYY-MM-DD/HH/logs_YYYYMMDDHHMMSS.ndjson.gz
Configure firewall allowlist
F5 Distributed Cloud requires specific IP ranges to be allowed in your firewall for log delivery.
Add the following IP address ranges to your firewall's allowlist:
193.16.236.64/29
185.160.8.152/29
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Get the service account email
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
F5 Distributed Cloud Bot Defense
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
F5_SHAPE
as the
Log type
.
Click
Get Service Account
. A unique service account email will be displayed, for example:
secops-12345678@secops-gcp-prod.iam.gserviceaccount.com
Copy the email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs://f5-xc-logs/
Replace
f5-xc-logs
with your actual GCS bucket name.
If you configured a specific prefix in the Global Log Receiver, include it in the path (for example,
gs://f5-xc-logs/bot-defense/
).
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days).
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (for example,
f5-xc-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email
Assign roles
: Select
Storage Object Viewer
Click
Save
.
UDM mapping table
Log field
UDM mapping
Logic
msg.requestHeaders.Proxy-Client-IP, msg.requestHeaders.WF-Forwarded-For, msg.requestHeaders.X-Forwarded-For, msg.requestHeaders.wl-proxy-client-ip, msg.hashedUserAgent, msg.transactionId, msg.hashedUsername, msg.dcgShapeFailedOn, ShapeShifterId, eventType, eventId, latRequest, latResponse, latTotal, latRspWait, count, latEccWait
additional.fields
Merged from labels created from various fields
intermediary
intermediary
Value copied directly if not empty
description
metadata.description
Value copied directly
target, has_principal_machine
metadata.event_type
Set to NETWORK_HTTP if target != "", else STATUS_UPDATE if has_principal_machine == true, else GENERIC_EVENT
app
network.application_protocol
Value uppercased
requestMethod, msg.method
network.http.method
Value from requestMethod if not empty, else msg.method
requestClientApplication, msg.requestHeaders.User-Agent
network.http.parsed_user_agent
Value from requestClientApplication if not empty, else msg.requestHeaders.User-Agent, converted to parsed user agent
requestContext, msg.requestHeaders.Referer
network.http.referral_url
Value from requestContext if not empty, else msg.requestHeaders.Referer
msg.sseResponseCode, prCode
network.http.response_code
Value from msg.sseResponseCode if not empty, else prCode, converted to integer
requestClientApplication, msg.requestHeaders.User-Agent
network.http.user_agent
Value from requestClientApplication if not empty, else msg.requestHeaders.User-Agent
requestHeader.x-shape-src-virtual
observer.ip
Value copied directly
principal
principal
Value copied directly
msg.host
principal.asset.hostname
Value copied directly
src, msg.src, msg.trueClientIP, requestHeader.X-Forwarded-For
principal.asset.ip
Value from src if not empty, else msg.src, else msg.trueClientIP, else first IP from X-Forwarded-For if != src
msg.host
principal.hostname
Value copied directly
src, msg.src, msg.trueClientIP, requestHeader.X-Forwarded-For
principal.ip
Value from src if not empty, else msg.src, else msg.trueClientIP, else first IP from X-Forwarded-For if != src
msg.requestHeaders
principal.resource.attribute.labels
Merged from key-value pairs in msg.requestHeaders
msg.uri
principal.url
Value copied directly
security_result
security_result
Value copied directly
deviceExternalId
security_result.about.asset_id
Value copied directly
flowLabel, agentLabel, requestHeader.Content-Length, requestHeader.Content-Type, requestHeader.Accept, requestHeader.Accept-Encoding, browserType, accountInfo, requestHeader.Via, asn, tid, ctag, requestHeader.Cache-Control, transactionResult
security_result.about.labels
Merged from labels created from various fields
act, msg.transactionResult
security_result.action
Set to ALLOW if act matches PASS and isAttack, else UNKNOWN_ACTION; or ALLOW if msg.transactionResult == Success, BLOCK if Failure
act, msg.transactionResult
security_result.action_details
Value from act if not empty, else msg.transactionResult
severity
security_result.severity
Set to HIGH if in Error, error, warning; CRITICAL if matches critical; MEDIUM if notice; LOW if in information, info, INFO
severity
security_result.severity_details
Value copied directly
attackCause
security_result.threat_name
Value copied directly
target
target
Value copied directly
appName
target.application
Value copied directly
dst, msg.dst
target.asset.ip
Value from dst if not empty, else msg.dst
dhost
target.hostname
Value copied directly
dst, msg.dst
target.ip
Value from dst if not empty, else msg.dst
countryName
target.location.country_or_region
Value copied directly
dpt
target.port
Converted to integer
msg.responseHeaders
target.resource.attribute.labels
Merged from key-value pairs in msg.responseHeaders
request
target.url
Value copied directly
requestHeader.X-Forwarded-For
intermediary.ip
Set to subsequent IPs from X-Forwarded-For array
metadata.product_name
Set to "Shape"
metadata.vendor_name
Set to "F5"
Need more help?
Get answers from Community members and Google SecOps professionals.
