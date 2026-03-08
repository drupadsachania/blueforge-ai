# Collect Akamai DNS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/akamai-dns/  
**Scraped:** 2026-03-05T09:49:29.610280Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Akamai DNS logs
Supported in:
Google secops
SIEM
This parser processes Akamai DNS logs. It extracts fields like timestamps, source IP and port, query, DNS record type, and response details. It then maps these fields to the UDM, handling various DNS record types and potential SPF records. The parser classifies the event as either
NETWORK_DNS
or
GENERIC_EVENT
based on the presence of principal information.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to AWS IAM and S3.
Your Akamai account has access to the Log Delivery Service.
Configure an Amazon S3 bucket
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
Save the bucket
Name
and
Region
for future reference.
Create a
User
following this user guide:
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
Optional: Add a description tag.
Click
Create access key
.
Click
Download .csv file
and save the
Access Key
and
Secret Access Key
for future reference.
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
Configure Log Delivery Service in Akamai
Sign in to the Akamai Control Center.
Go to
Log Delivery Service
under
Data Services
.
Click
Add New Configuration
.
In the
Configuration Name
field, provide a name for your configuration (for example,
Edge DNS Logs to S3
).
Select
Edge DNS
as the
Log Source
.
Select
AWS S3
as the
Delivery Target
.
Provide the following details:
Bucket Name
: the name of your S3 bucket.
Region
: the AWS region where your bucket is hosted.
Access Key ID
: the IAM user Access Key ID.
Secret Access Key
: the IAM user Secret Access Key.
Optional: specify the
Directory Structure
. (for example:
logs/akamai-dns/YYYY/MM/DD/HH/
).
Optional: set the
File Naming Convention
. (for example:
edge-dns-logs-{timestamp}.log
).
Select the
Log Formats
you want to include:
DNS Queries
DNS Responses
Choose the
Delivery Frequency
:
Options include hourly, daily, or upon reaching a certain file size (for example, 100MB).
Optional: Click
Add Filters
to include or exclude specific logs based on specific criteria (for example, hostname or record type).
Review the configuration details and click
Save and Activate
.
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
Akamai DNS Logs
).
Select
Amazon S3
as the
Source type
.
Select
Akamai DNS
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Region
: the region where the Amazon S3 bucket is located.
S3 URI
: the bucket URI.
s3://BUCKET_NAME
Replace the following:
BUCKET_NAME
: the name of the bucket.
URI is a
: select the
URI_TYPE
according to log stream configuration (
Single file
|
Directory
|
Directory which includes subdirectories
).
Source deletion option
: select deletion option according to your preference.
Access Key ID
: the User access key with access to the s3 bucket.
Secret Access Key
: the User secret key with access to the s3 bucket.
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
Finalize screen
, and then click
Submit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
class
read_only_udm.network.dns.questions.class
If
class
is "IN", set to 1. Otherwise, attempt conversion to unsigned integer.
column11
read_only_udm.target.hostname
Mapped if it contains a hostname and doesn't contain specific patterns like "ip4", "=", ".net", or "10 mx0". Also used for extracting IP addresses, email addresses, and DNS authority data based on various patterns.
column11
read_only_udm.target.ip
Extracted from
column11
if it matches the pattern for IP addresses within SPF records.
column11
read_only_udm.target.user.email_addresses
Extracted from
column11
if it matches the pattern for email addresses within DMARC records.
column11
read_only_udm.network.dns.authority.data
Extracted from
column11
if it matches patterns for domain names within various record types.
column11
read_only_udm.network.dns.response_code
Set to 3 if
column11
contains "NXDOMAIN".
column2
read_only_udm.principal.ip
Mapped if it is a valid IP address.
column3
read_only_udm.principal.port
Mapped if it is a valid integer.
column4
read_only_udm.network.dns.questions.name
Directly mapped.
column6
read_only_udm.network.dns.questions.type
Mapped based on the value of
type
, using conditional logic to assign the corresponding numerical value.
column8
read_only_udm.network.sent_bytes
Converted to an unsigned integer and mapped.
read_only_udm.metadata.event_timestamp
Constructed from the
date
and
time
fields extracted from
column1
.
read_only_udm.event_type
Set to
NETWORK_DNS
if
principal.ip
is present, otherwise set to
GENERIC_EVENT
.
read_only_udm.product_name
Hardcoded to
AKAMAI_DNS
.
read_only_udm.vendor_name
Hardcoded to
AKAMAI_DNS
.
read_only_udm.dataset
Hardcoded to
AKAMAI_DNS
.
read_only_udm.event_subtype
Hardcoded to
DNS
.
Need more help?
Get answers from Community members and Google SecOps professionals.
