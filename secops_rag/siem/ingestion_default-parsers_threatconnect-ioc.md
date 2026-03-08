# Collect ThreatConnect IOC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/threatconnect-ioc/  
**Scraped:** 2026-03-05T09:29:14.579300Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ThreatConnect IOC logs
Supported in:
Google secops
SIEM
This parser extracts IOC data from ThreatConnect JSON logs and transforms it into the UDM format. It handles various IOC types such as Host, Address, File, and URL, mapping fields like confidence scores, descriptions, and entity details to their corresponding UDM equivalents, and categorizes threats based on keywords within the log data.
Before you begin
Ensure that you have the following prerequisites:
Google Security Operations instance.
Privileged access to ThreatConnect.
Configure API User on ThreatConnect
Sign in to ThreatConnect.
Go to
Settings
>
Org Settings
.
Go to the
Membership
tab in the
Organization Settings
.
Click
Create API User
.
Fill out the fields on the API User Administration window:
First Name
: enter the API user's first name.
Last Name
: enter the API user's last name
System Role
: select the
Api User
or
Exchange Admin
System role.
Organization Role
: select the API user's Organization role.
Include in Observations and False Positives
: select the checkbox to allow data provided by the API user to be included in observation and false-positive counts.
Disabled
: click the checkbox to disable an API user's account in the event that the Administrator wants to retain log integrity.
Copy and save the
Access ID
and
Secret Key
.
Click
Save
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
field, enter a name for the feed; for example,
ThreatConnect Logs
.
Select
Third Party API
as the
Source type
.
Select the
ThreatConnect
as the log type.
Click
Next
.
Specify values for the following input parameters:
Username
: enter the ThreatConnect Access ID to authenticate as.
Secret
: enter the ThreatConnect Secret Key for the specified user.
API Hostname
: Fully Qualified Domain Name (FQDN) of your ThreatConnect instance (for example,
<myinstance>.threatconnect.com
).
Owners
: all owner names, where the owner identifies a collection of IOCs.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Need more help?
Get answers from Community members and Google SecOps professionals.
