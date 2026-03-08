# Collect Palo Alto Networks IOC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/pan-ioc/  
**Scraped:** 2026-03-05T09:27:17.328877Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Palo Alto Networks IOC logs
Supported in:
Google secops
SIEM
Overview
This parser extracts IOC data from Palo Alto Networks Autofocus JSON logs, mapping fields to the UDM. It handles domain, IPv4, and IPv6 indicators, prioritizing
domain
and converting IP addresses to the appropriate format. It drops unsupported indicator types and defaults categorization to
MALWARE
unless
Trojan
is specifically identified in the message.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Palo Alto AutoFocus.
Configure Palo Alto AutoFocus license
Sign in to Palo Alto
Customer Support Portal
.
Go to
Assets
>
Site Licenses
.
Select
Add Site License
.
Enter the code.
Obtain Palo Alto AutoFocus API Key
Sign in to Palo Alto
Customer Support Portal
.
Go to
Assets
>
Site Licenses
.
Locate the Palo Alto AutoFocus license.
Click
Enable
in the Actions column.
Click
API Key
in the API Key column.
Copy
and
Save
the API Key from the top bar.
Create Palo Alto AutoFocus custom Feed
Sign in to Palo Alto AutoFocus.
Go to
Feeds
.
Select a feed already created. If no feed is present, proceed to create one.
Click
add
Create A Feed
.
Provide a descriptive name.
Create a
query
.
Select
Output
method as
URL
.
Click
Save
.
Access the feed details:
Copy
and
Save
the feed
<ID>
from the URL. (For example,
https://autofocus.paloaltonetworks.com/IOCFeed/<ID>/IPv4AddressC2
)
Copy
and
Save
the feed name.
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
Palo Alto Autofocus Logs
.
Select
Third party API
as the
Source type
.
Select
PAN Autofocus
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Authentication HTTP header
: API Key used to authenticate to autofocus.paloaltonetworks.com in
apiKey:<value>
format. Replace
<value>
with the AutoFocus API Key copied previously.
Feed ID
: Custom feed ID.
Feed Name
: Custom feed name.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
indicator.indicatorType
indicator.indicatorType
Directly mapped from the raw log. Converted to uppercase.
indicator.indicatorValue
event.ioc.domain_and_ports.domain
Mapped if
indicator.indicatorType
is
DOMAIN
.
indicator.indicatorValue
event.ioc.ip_and_ports.ip_address
Mapped if
indicator.indicatorType
matches "IP(V4|V6|)(_ADDRESS|)". Converted to IP address format.
indicator.wildfireRelatedSampleVerdictCounts.MALWARE
event.ioc.raw_severity
Mapped if present. Converted to string.
tags.0.description
event.ioc.description
Mapped if present for the first tag (index 0). Set to
PAN Autofocus IOC
by the parser. Set to
HIGH
by the parser. Set to
TROJAN
if the
message
field contains
Trojan
, otherwise set to
MALWARE
.
Need more help?
Get answers from Community members and Google SecOps professionals.
