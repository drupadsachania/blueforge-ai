# Collect Jenkins logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jenkins/  
**Scraped:** 2026-03-05T09:57:25.192445Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Jenkins logs
Supported in:
Google secops
SIEM
Overview
This parser extracts key information such as timestamps, user IDs, source IPs, actions, and object IDs from JSON and SYSLOG formatted logs. It uses grok patterns to match various log message formats, handling variations in structure, and populates a unified data model (UDM) with the extracted fields. The parser also categorizes events based on the presence of user or IP information.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Google Cloud IAM.
Privileged access to Google Cloud Storage.
Privileged access to Jenkins.
Create a Google Cloud Storage Bucket
Go to
Cloud Storage
.
Create a new bucket. Choose a unique name and appropriate region.
Ensure the bucket has proper access controls (for example, only authorized service accounts can write to it).
Create a Google Cloud Service account
Go to
IAM & Admin
>
Service Accounts
.
Create a new service account. Give it a descriptive name (for example,
jenkins-logs
).
Grant the service account the
Storage Object Creator
role on the GCS bucket you created in the previous step.
Create an SSH key for your service account:
Create and delete service account keys
.
Download a JSON key file for the service account.
Install Google Cloud Storage plugin in Jenkins
Go to
Manage Jenkins
>
Plugins
.
Select
Available plugins
.
Search for the
Google Cloud Storage
plugin.
Install the plugin and restart Jenkins if required.
Install Google OAuth Credentials Plugin in Jenkins
Go to
Manage Jenkins
>
Plugins
.
Select
Available plugins
Search for the
Google OAuth Credentials
plugin.
Install the plugin and restart Jenkins if required.
Configure Jenkins to authenticate with Google Cloud
Go to
Manage Jenkins
>
Credentials
>
System
.
Click
add
Add Credentials
.
Kind
: select
Google Service Account from private key
.
Project name
: set a name for the credentials.
Upload the JSON key file you obtained during the Google Cloud Service account creation.
Click
Create
.
Configure Jenkins logs to upload Google SecOps
In the Jenkins job configuration, add
Google Storage Build Log Upload
in post-build actions, with the following parameters:
Google Credentials
: The name of your Google credentials you created in the previous step.
Log Name
: The name of the file to store the Jenkins build log, under the specified storage path.
Storage Location
: The name of the bucket where you want to upload your logs. The bucket must be accessible to the service account you created.
Test the log upload.
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
field, enter a name for the feed; for example,
Jenkins Logs
.
Select
Google Cloud Storage V2
as the
Source type
.
Select
Jenkins
as the
Log type
.
Click
Get Service Account
as the
Chronicle Service Account
.
Specify values for the following input parameters:
Storage Bucket URI
: Google Cloud storage bucket URL in
gs://my-bucket/<value>/
format. This URL must end with a trailing forward slash (/).
Source deletion options
: select deletion option according to your preference.
Click
Create Feed
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
act
security_result.action_details
Extracted from
msg1
or
msg2
fields. Represents the action performed. Leading whitespace is removed.
data
principal.user.userid
OR
principal.ip
OR
metadata.description
If
data
matches an IP address pattern, it maps to
principal.ip
. If it matches a username pattern, it maps to
principal.user.userid
. Otherwise, it maps to
metadata.description
.
msg1
target.asset.product_object_id
OR
security_result.action_details
Used to extract
object
and
act
. If a
/
is present, it is split into
object
and
act
. If
»
is present, it is split into
object
and
act
. Otherwise, it is treated as
act
and potentially further parsed.
msg2
metadata.description
OR
security_result.action_details
If present, initially mapped to
metadata.description
. If it contains "completed:", the value after is extracted and mapped to
security_result.action_details
.
object
target.asset.product_object_id
Extracted from
msg1
. Represents the object acted upon.
object_id
target.resource.attribute.labels.value
Extracted from
object
if a
/
is present. Represents a more specific object identifier. The key is hardcoded as "Plugin Name".
src_ip
principal.ip
Extracted from
message
or
data
. Represents the source IP address.
user
principal.user.userid
Extracted from
message
or
data
. Represents the user associated with the event.
metadata.event_timestamp
Copied from the calculated
@timestamp
field.
metadata.event_type
Determined by parser logic. Set to
USER_UNCATEGORIZED
if
user
is present,
STATUS_UNCATEGORIZED
if
src_ip
is present, and
GENERIC_EVENT
otherwise.
metadata.product_name
Hardcoded as
Jenkins
.
metadata.product_version
Hardcoded as
Jenkins
.
metadata.vendor_name
Hardcoded as
JENKINS
.
metadata.event_timestamp
Constructed from
year
,
month
,
day
,
time
, and
ampm
fields.
Need more help?
Get answers from Community members and Google SecOps professionals.
