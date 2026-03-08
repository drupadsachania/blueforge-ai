# Collect Trend Micro Vision One logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/trendmicro-vision-one/  
**Scraped:** 2026-03-05T09:29:30.004145Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Trend Micro Vision One logs
Supported in:
Google secops
SIEM
This document explains how to collect Trend Micro Vision One logs by setting up a Google Security Operations feed. The parser pushes alerts, event data, container vulnerabilities, activity data, and audit logs to AWS S3 buckets managed by Trend Micro. Google SecOps retrieves this data using data feeds approximately every 15 minutes. Unretrieved data in the S3 buckets is retained for 7 days before being purged.
You can create multiple feeds in Google SecOps and configure the data obtained using the feeds individually.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have privileged access to Trend Micro Vision One.
Configure Trend Vision One Data Export to Google SecOps
In the Trend Vision One console, generate the access key and specify the data to send to Google SecOps.
Go to
Workflow and Automation
>
Third-Party Integration
.
In the
Integration
column, click
Google Security Operations
.
Under
Access key
, click
Generate key
to generate the access key ID and secret access key. Save the access key ID and secret access key for later use.
Under
Data transfer
, turn on the toggle next to the data you want to send to S3 buckets. Whenever a data transfer is enabled, an S3 URI is generated and the data begins to be sent to the corresponding S3 bucket. Copy and store the S3 URI for later use.
For
Events
and
Activity data
, click
Edit
to modify the scope of the data.
To stop sending a type of data to Google SecOps, turn off the toggle next to the data.
Re-enabling the data transfer generates a new S3 URI. You need to configure a new feed in Google SecOps.
Configure a feed in Google SecOps to ingest the Trend Micro Vision One logs
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
field, enter a name for the feed; for example,
Trend Micro Vision One Workbench Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select the Trend Vision One data you want Google SecOps to ingest as the
Log type
. Available options include:
Trend Micro Vision One
Trend Micro Vision One Activity
Trend Micro Vision One Audit
Trend Micro Vision One Container Vulnerabilities
Trend Micro Vision One Detections
Trend Micro Vision One Observed Attack Techniques
Trend Micro Vision One Workbench
Click
Next
.
Specify values for the following input parameters:
S3 URI
: enter the S3 URI obtained in the
previous section
.
Source deletion options
: select
Never delete files
.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Access Key ID
: enter the User access key obtained in the
previous section
.
Secret Access Key
: enter the User secret key with access to the S3 bucket obtained in the
previous section
.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Repeat this process to add multiple feeds for all the Trend Vision One data types you want to ingest into Google SecOps.
Need more help?
Get answers from Community members and Google SecOps professionals.
