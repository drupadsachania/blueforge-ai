# Collect Edgio WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/edgio-waf/  
**Scraped:** 2026-03-05T09:54:56.938131Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Edgio WAF logs
Supported in:
Google secops
SIEM
This guide explains how to ingest Edgio Web Application Firewall (WAF) logs to
Google Security Operations using Google Cloud Storage. Edgio's Real-Time Log Delivery
(RTLD) service can automatically deliver compressed WAF log data directly to a
Cloud Storage bucket, which Google SecOps can then ingest
for analysis and monitoring.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
Privileged access to Google Cloud Platform.
Privileged access to Edgio Console.
An active Edgio property with WAF enabled.
Configure a Google Cloud Storage bucket
Sign in to the
Google Cloud console
.
Go to
Cloud Storage
>
Buckets
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a unique bucket name (for example,
edgio-waf-logs
).
Location type
: Select
Region
or
Multi-region
based on your requirements.
Location
: Select the location closest to your Edgio deployment.
Storage class
: Select
Standard
.
Access control
: Select
Uniform
.
Encryption
: Select
Google-owned and Google-managed encryption key
.
Click
Create
.
Configure bucket permissions for Edgio
In the
Google Cloud console
, go to your newly created bucket.
Click
Permissions
.
Click
Grant Access
.
In the
New principals
field, add:
real-time-log-delivery@durable-firefly-334516.iam.gserviceaccount.com
In the
Select a role
list, select
Storage Object Creator
.
Click
Save
.
Configure Edgio Real-Time Log Delivery
Sign in to the
Edgio Console
.
Select your
private space
or
organization
.
Select the required
property
.
From the left pane, select the required
environment
.
From the left pane, click
Realtime Log Delivery
.
Click
+ New Log Delivery Profile
.
Select
WAF
as the log type.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps WAF Logs
).
Destination
: Select
Google Cloud Storage
.
Bucket
: Enter your GCS bucket name (for example,
edgio-waf-logs
).
Prefix
: Optional. Enter a prefix for log organization (for example,
waf/
).
Log Format
: Select
JSON
(default).
Downsample the Logs
: Leave unchecked for full log delivery.
In the
Fields
section, ensure all required fields are selected. Key fields include:
account_number
action_type
client_city
client_country_code
client_ip
client_tls_ja3_md5
host
referer
rule_message
rule_tags
server_port
sub_events
sub_events_count
timestamp
URL
user_agent
uuid
waf_instance_name
waf_profile_name
waf_profile_type
Click
Save
.
Configure a feed in Google SecOps to ingest Edgio WAF logs
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed (for example,
Edgio WAF Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
Edgio WAF
as the
Log type
.
Click
Get Service Account
.
Copy the service account email displayed.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Enter your Cloud Storage bucket URI (format:
gs://edgio-waf-logs/waf/
).
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
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
Grant permissions to the Google SecOps service account
Return to the
Google Cloud console
.
Go to your Cloud Storage bucket.
Click
Permissions
.
Click
Grant Access
.
In the
New principals
field, paste the service account email you copied from Google SecOps.
In the
Select a role
list, select
Storage Object Viewer
.
If you selected delete options in the feed configuration, also grant
Storage Object Admin
.
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
