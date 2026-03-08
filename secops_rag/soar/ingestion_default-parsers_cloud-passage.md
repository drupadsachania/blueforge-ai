# Collect CloudPassage Halo logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cloud-passage/  
**Scraped:** 2026-03-05T09:53:22.977832Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect CloudPassage Halo logs
Supported in:
Google secops
SIEM
This document explains how to collect CloudPassage Halo (formerly CloudPassage) logs by setting up a Google Security Operations feed using the Third party API.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
CLOUD_PASSAGE
ingestion label.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to CloudPassage Halo portal with administrator permissions
Active CloudPassage Halo account with API access enabled
Configure CloudPassage Halo API access
To enable Google SecOps to pull event logs, you need to create an API key pair with read-only permissions.
Create API key pair
Sign in to the
CloudPassage Halo Portal
.
Go to
Settings
>
Site Administration
>
API Keys
.
Click
Create Key
or
New API Key
.
Provide the following configuration details:
Key Name
: Enter a descriptive name (for example,
Google SecOps Integration
).
Read Only
: Select
Yes
(read-only access is recommended for security).
Click
Create
.
Record API credentials
After creating the API key, you'll receive the following credentials:
Key ID
: Your unique API key identifier (for example,
abc123def456
)
Secret Key
: Your API secret key (for example,
xyz789uvw012
)
Required API permissions
CloudPassage Halo API keys support the following permission levels:
Permission Level
Access
Purpose
Read Only
Read
Retrieve event data and configuration (recommended)
Full Access
Read + Write
Retrieve events and modify configuration (not required)
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
CloudPassage Halo Events
).
Select
Third party API
as the
Source type
.
Select
Cloud Passage
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Username
: Enter the
Key ID
from the CloudPassage Halo API key pair created earlier.
Secret
: Enter the
Secret Key
from the CloudPassage Halo API key pair created earlier.
Event types
(optional): Specify which event types to ingest. Enter one event type per line.
If you leave this field empty, the feed will automatically retrieve the following default event types:
fim_target_integrity_changed
(File Integrity Monitoring events)
lids_rule_failed
(Log-based Intrusion Detection System events)
sca_rule_failed
(Security Configuration Assessment events)
To retrieve additional event types, enter them one per line. For example:
fim_target_integrity_changed
lids_rule_failed
sca_rule_failed
lids_rule_passed
sca_rule_passed
agent_connection_lost
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
After setup, the feed begins to retrieve event logs from the CloudPassage Halo API in chronological order.
UDM mapping table
Log Field
UDM Mapping
Logic
id
metadata.product_log_id
Unique event identifier
created_at
metadata.event_timestamp
Event creation timestamp
type
metadata.product_event_type
Event type (e.g., fim_target_integrity_changed)
server_hostname
target.hostname
Hostname of the affected server
server_platform
target.platform
Operating system platform
server_primary_ip_address
target.ip
Primary IP address of the server
rule_name
security_result.rule_name
Name of the security rule that triggered the event
critical
security_result.severity
Criticality level of the event
policy_name
security_result.category
Security policy name
user
principal.user.userid
User associated with the event
message
security_result.description
Event description or message
Need more help?
Get answers from Community members and Google SecOps professionals.
