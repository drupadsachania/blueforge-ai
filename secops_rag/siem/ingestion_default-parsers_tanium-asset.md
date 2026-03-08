# Collect Tanium Asset logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/tanium-asset/  
**Scraped:** 2026-03-05T09:28:55.525464Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Tanium Asset logs
Supported in:
Google secops
SIEM
This document explains how to ingest Tanium Asset logs to Google Security Operations using two different methods. You can choose between Tanium Connect's native Amazon S3 export or real-time syslog forwarding via Bindplane. Both methods use Tanium Connect module to extract asset data from Tanium and forward it to Chronicle for analysis and monitoring. The parser transforms raw logs into a structured format conforming to the Chronicle UDM. It achieves this by first normalizing key-value pairs from various input formats (JSON, Syslog) and then mapping the extracted fields to corresponding UDM attributes within nested JSON objects representing asset, user, and relationship entities.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to the Tanium Console (Connect module) to configure export destinations
Choose your preferred integration method:
Option 1 (Recommended)
: Privileged access to
AWS
(S3, IAM) for native S3 export
Option 2
: Windows 2016 or later, or a Linux host with
systemd
for the Bindplane agent installation
Option 1: Configure Tanium Asset logs export using AWS S3
Create an Amazon S3 bucket
Create
Amazon S3 bucket
following this user guide:
Creating a bucket
Save bucket
Name
and
Region
for future reference (for example,
tanium-asset-logs
).
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
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
Configure Tanium Connect for S3 export
Sign in to the
Tanium Console
with administrator privileges.
Go to
Modules
>
Connect
>
Overview
and click
Create Connection
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Asset S3 Export
).
Description
: Optional description for this connection.
Enable
: Select
Enable
to run on a schedule.
Click
Next
.
In
Source
configuration:
Source
: Select
Saved Question
.
Question
: Choose an existing saved question that returns Asset data or create a new one with Asset-related sensors (for example, Computer Name, IP Address, OS Platform, Domain).
Computer Group
: Select the computer group to target for asset data collection.
Click
Next
.
In
Destination
configuration:
Destination
: Choose
AWS S3
.
Name
: Enter a destination name (for example,
Chronicle Asset S3
).
AWS Access Key ID
: Enter the Access Key ID from the IAM user.
AWS Secret Access Key
: Enter the Secret Access Key from the IAM user.
S3 Bucket Name
:
tanium-asset-logs
.
S3 Key Prefix
:
tanium/assets/
(optional prefix for organization).
Region
: Select the AWS region where your S3 bucket is located.
Click
Next
.
In
Formatting
configuration:
Format
: Select
JSON
for structured data export.
Columns
: Select the Asset fields you want to export and format them appropriately.
Click
Next
.
In
Schedule
configuration:
Schedule
: Configure delivery schedule (for example, every hour or daily).
Start Date/Time
: Set when the connection should start running.
Click
Save
to create the connection and start automated S3 export.
Optional: Create read-only IAM user & keys for Google SecOps
Go to
AWS Console
>
IAM
>
Users
>
Add users
.
Click
Add users
.
Provide the following configuration details:
User
: Enter
secops-reader
.
Access type
: Select
Access key – Programmatic access
.
Click
Create user
.
Attach minimal read policy (custom):
Users
>
secops-reader
>
Permissions
>
Add permissions
>
Attach policies directly
>
Create policy
.
In the JSON editor, enter the following policy:
{
"Version"
:
"2012-10-17"
,
"Statement"
:
[
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:GetObject"
],
"Resource"
:
"arn:aws:s3:::tanium-asset-logs/*"
},
{
"Effect"
:
"Allow"
,
"Action"
:
[
"s3:ListBucket"
],
"Resource"
:
"arn:aws:s3:::tanium-asset-logs"
}
]
}
Set the name to
secops-reader-policy
.
Go to
Create policy
>
search/select
>
Next
>
Add permissions
.
Go to
Security credentials
>
Access keys
>
Create access key
.
Download the
CSV
(these values are entered into the feed).
Configure a feed in Google SecOps to ingest Tanium Asset logs
Go to
SIEM Settings
>
Feeds
.
Click
+ Add New Feed
.
In the
Feed name
field, enter a name for the feed (for example,
Tanium Asset logs
).
Select
Amazon S3 V2
as the
Source type
.
Select
Tanium Asset
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
:
s3://tanium-asset-logs/tanium/assets/
Source deletion options
: Select deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: User access key with access to the S3 bucket.
Secret Access Key
: User secret key with access to the S3 bucket.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Option 2: Configure Tanium Asset logs export using syslog and Bindplane
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the 
system where Bindplane will be installed.
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according to the following instructions.
Windows installation
Open the
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Additional installation resources
For additional installation options, consult this
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
PLACEHOLDER_CUSTOMER_ID
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'TANIUM_ASSET'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<PLACEHOLDER_CUSTOMER_ID>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in Linux, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in Windows, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog forwarding on Tanium Asset
Sign in to the
Tanium Console
with administrator privileges.
Go to
Modules
>
Connect
>
Overview
and click
Create Connection
.
Click
Create
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Asset Integration
).
Description
: Optional description for this connection.
Enable
: Select
Enable
to run on a schedule.
Click
Next
.
In
Source
configuration:
Source
: Select
Saved Question
.
Question
: Choose an existing saved question that returns Asset data or create a new one with Asset-related sensors.
Computer Group
: Select the computer group to target for asset data collection.
Click
Next
.
In
Destination
configuration:
Destination
: Choose
SIEM/Syslog
.
Name
: Enter a destination name (for example,
Chronicle Asset Syslog
).
Host
: Enter the BindPlane Agent IP address.
Port
: Enter the BindPlane Agent port number (for example,
514
).
Protocol
: Select
UDP
.
Format
: Select
SYSLOG RFC 5424
.
Timezone
: Select
UTC
timezone for universal consistency across systems.
Click
Next
.
In
Formatting
configuration:
Format
: Select
JSON
.
Columns
: Select the Asset fields you want to forward (for example, Computer Name, IP Address, OS Platform, Domain).
Click
Next
.
In
Schedule
configuration:
Schedule
: Configure delivery schedule (for example, every hour).
Start Date/Time
: Set when the connection should start running.
Click
Save
to create the connection and start forwarding.
UDM Mapping Table
Log Field
UDM Mapping
Logic
application_name
entity.metadata.source_labels.value
Value is taken from the "application_name" field if it exists in the raw log.
application_vendor
entity.metadata.source_labels.value
Value is taken from the "application_vendor" field if it exists in the raw log.
application_version
entity.metadata.product_version
Value is taken from the "application_version" field if it exists in the raw log.
BIOS_Current_Language
entity.metadata.source_labels.value
Value is taken from the "BIOS_Current_Language" field if it exists in the raw log.
BIOS_Release_Date
entity.metadata.source_labels.value
Value is taken from the "BIOS_Release_Date" field if it exists in the raw log.
BIOS_Vendor
entity.metadata.source_labels.value
Value is taken from the "BIOS_Vendor" field if it exists in the raw log.
BIOS_Version
entity.metadata.product_version
Value is taken from the "BIOS_Version" field if it exists in the raw log.
Chassis Type
entity.entity.asset.category
Value is taken from the "Chassis Type" field if it exists in the raw log.
Computer ID
entity.entity.asset.product_object_id
Value is taken from the "Computer ID" field if it exists in the raw log. Also used to populate entity.relations.entity.asset.asset_id with the prefix "id: ".
Computer Name
entity.entity.asset.hostname
Value is taken from the "Computer Name" field if it exists in the raw log.
Count
entity.metadata.source_labels.value
Value is taken from the "Count" field if it exists in the raw log.
Endpoint Fingerprint
entity.entity.asset.hardware.serial_number
Value is taken from the "Endpoint Fingerprint" field if it exists in the raw log.
IP Address
entity.entity.asset.ip
Values are taken from the "IP Address" field and added as separate IP addresses to the array.
Last Logged In User
entity.relations.entity.user.userid
Value is taken from the "Last Logged In User" field, with any domain prefix removed, if it exists in the raw log.
Last Reboot
entity.entity.asset.last_boot_time
Value is parsed from the "Last Reboot" field and formatted as a timestamp if it exists in the raw log.
MAC Address
entity.entity.asset.mac
Values are taken from the "MAC Address" field and added as separate MAC addresses to the array.
Manufacturer
entity.entity.asset.hardware.manufacturer
Value is taken from the "Manufacturer" field if it exists in the raw log.
Operating System
entity.entity.asset.platform_software.platform_version
Value is taken from the "Operating System" field if it exists in the raw log. Used to determine the value of entity.entity.asset.platform_software.platform (WINDOWS, LINUX, or MAC).
platform
entity.entity.asset.platform_software.platform_version
Value is taken from the "platform" field if it exists in the raw log. Used to determine the value of entity.entity.asset.platform_software.platform (WINDOWS, LINUX, or MAC).
serial_number
entity.entity.asset.hardware.serial_number
Value is taken from the "serial_number" field if it exists in the raw log.
version
entity.entity.asset.platform_software.platform_version
Value is taken from the "version" field if it exists in the raw log. Used to determine the value of entity.entity.asset.platform_software.platform (WINDOWS, LINUX, or MAC).
N/A
entity.metadata.collected_timestamp
Set to the create_time of the batch.
N/A
entity.metadata.vendor_name
Always set to "TANIUM_ASSET".
N/A
entity.metadata.product_name
Always set to "TANIUM_ASSET".
N/A
entity.metadata.entity_type
Always set to "ASSET".
N/A
entity.relations.entity_type
Always set to "USER".
N/A
entity.relations.relationship
Always set to "OWNS".
Need more help?
Get answers from Community members and Google SecOps professionals.
