# Collect AWS VPN logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-vpn/  
**Scraped:** 2026-03-05T09:50:50.625551Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS VPN logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS VPN logs to Google Security Operations. AWS VPN provides a secure connection between your on-premises network and your Amazon Virtual Private Cloud (VPC). By forwarding VPN logs to Google SecOps, you can analyze VPN connection activities, detect potential security risks, and monitor traffic patterns.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
Configure AWS IAM and S3
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save the bucket
Name
and
Region
for later use.
Create a user following this user guide:
Creating an IAM user
.
Select the created
User
.
Select the
Security credentials
tab.
Click
Create Access Key
in the
Access Keys
section.
Select
Third-party service
as the
Use case
.
Click
Next
.
Optional: add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
Access Key
and
Secret Access Key
for later use.
Click
Done
.
Select the
Permissions
tab.
Click
Add permissions
in the
Permissions policies
section.
Select
Add permissions
.
Select
Attach policies directly
.
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
How to configure CloudTrail for AWS VPN Logging
Sign in to the
AWS Management Console
.
In the search bar, type and select
CloudTrail
from the services list.
Click
Create trail
.
Provide a
Trail name
; for example,
VPN-Activity-Trail
.
Select the
Enable for all accounts in my organization
checkbox.
Type the S3 bucket URI created earlier (the format should be:
s3://your-log-bucket-name/
), or create a new S3 bucket.
If SSE-KMS is enabled, provide a name for
AWS KMS alias
, or choose an
existing AWS KMS Key
.
You can leave the other settings as default.
Click
Next
.
Select
Management events
to
All
and
Data events
to
Networking and VPN services
under
Event Types
.
Click
Next
.
Review the settings in
Review and create
.
Click
Create trail
.
Optional: If you created a new bucket during the CloudTrail configuration, continue with the following process:
Go to
S3
.
Identify and select the newly created log bucket.
Select the
AWSLogs
folder.
Click
Copy S3 URI
and save it.
How to configure AWS Client VPN logging
Go to the
AWS Client VPN
console.
Under
Client VPN Endpoints
, select the required endpoint.
In the
Logging
section, click
enable logging
and specify an
Amazon CloudWatch Log group
to which VPN connection logs will be sent.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the AWS VPN feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS VPN
log type.
Specify the values in the following fields.
Source Type
: Amazon SQS V2
Queue Name
: The SQS queue name to read from
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
SQS Queue Access Key ID
: An account access key that is a 20-character alphanumeric string.
SQS Queue Secret Access Key
: An account access key that is a 40-character alphanumeric string.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
UDM Mapping Table
Need more help?
Get answers from Community members and Google SecOps professionals.
