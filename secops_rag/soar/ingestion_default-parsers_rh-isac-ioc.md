# Collect RH-ISAC IOC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/rh-isac-ioc/  
**Scraped:** 2026-03-05T09:59:37.050929Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect RH-ISAC IOC logs
Supported in:
Google secops
SIEM
This document explains how to collect RH-ISAC IOC (Indicators of Compromise) logs by setting up a Google Security Operations feed using the Third party API.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
RH_ISAC_IOC
ingestion label.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Active RH-ISAC Core Membership with access to the MISP platform
Privileged access to the RH-ISAC MISP instance at https://misp.rhisac.org
Generate RH-ISAC MISP API authentication key
To enable Google SecOps to retrieve IOCs from RH-ISAC MISP, you need to generate an API authentication key.
Access your MISP profile
Sign in to the
RH-ISAC MISP instance
at
https://misp.rhisac.org
.
Go to
My Profile
by clicking your username in the top right corner.
Alternatively, navigate directly to:
https://misp.rhisac.org/users/view/me
.
Create authentication key
In your profile page, select the
Auth Keys
tab.
Click
Add authentication key
.
Provide the following configuration details:
Comment
: Enter a descriptive comment to identify the key (for example,
Google SecOps Integration
).
Read only
: Select this option (recommended).
Allowed IPs
: Optional. Enter Google SecOps IP ranges if you want to restrict key usage to specific IPs.
Click
Submit
.
Save authentication key
After creating the key, a new authentication key is displayed
only once
.
Copy and save*the authentication key immediately in a secure location.
The key format is a long hexadecimal string (for example,
abc123def456...
).
Required API permissions
The RH-ISAC MISP API authentication key provides the following access based on your RH-ISAC membership role:
Permission
Access Level
Purpose
Read IOCs
Read
Retrieve indicators of compromise
Read Events
Read
Retrieve MISP events with IOC data
Read Attributes
Read
Retrieve specific IOC attributes
Read Tags
Read
Retrieve taxonomy tags (e.g., rhisac:vetted)
Understanding RH-ISAC IOC data
RH-ISAC provides curated, high-confidence threat intelligence through their MISP platform:
Vetted Indicators
: IOCs tagged with
rhisac:vetted
are high-fidelity indicators validated by retail and hospitality sector members.
Enriched Data
: All IOCs are automatically enriched using RH-ISAC's PyOTI (Python Open Threat Intelligence) framework.
MITRE ATT&CK Mapping
: Events include MITRE ATT&CK framework mappings for tactics, techniques, and procedures.
Threat Actor Context
: Galaxy clusters provide threat actor attribution and tool relationships.
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
RH-ISAC IOC Feed
).
Select
Third party API
as the
Source type
.
Select
RH-ISAC
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
OAuth token endpoint
: Contact RH-ISAC support to obtain the OAuth token endpoint URL for your organization.
OAuth client ID
: Contact RH-ISAC support to obtain your organization's OAuth client ID.
OAuth client secret
: Contact RH-ISAC support to obtain your organization's OAuth client secret.
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
After setup, the feed begins to retrieve IOCs from the RH-ISAC MISP instance in chronological order.
UDM mapping table
Log Field
UDM Mapping
Logic
Event.uuid
metadata.event_id
MISP event unique identifier
Attribute.type
security_result.category
IOC type (e.g., ip-dst, domain, md5)
Attribute.value
security_result.detection_fields
IOC value (e.g., IP address, domain name, hash)
Attribute.comment
security_result.description
Analyst comment or context
Event.info
security_result.summary
Event description or title
Event.timestamp
metadata.event_timestamp
Event creation or modification time
Attribute.category
security_result.rule_name
MISP attribute category (e.g., Network activity, Payload)
Tag.name
security_result.detection_fields.tags
Taxonomy tags (e.g., rhisac:vetted, tlp:amber)
GalaxyCluster.value
security_result.threat_name
Threat actor or tool name
Need more help?
Get answers from Community members and Google SecOps professionals.
