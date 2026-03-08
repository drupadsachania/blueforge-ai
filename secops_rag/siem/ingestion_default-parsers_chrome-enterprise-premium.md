# Collect Chrome Enterprise Premium Context Access Aware Data

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-enterprise-premium/  
**Scraped:** 2026-03-05T09:22:34.087590Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Chrome Enterprise Premium Context Access Aware Data
Supported in:
Google secops
SIEM
This document explains how you can connect your organization to Google Security Operations, enable the
Identity-Aware Proxy (IAP) API, and set up feeds to ingest the following data to
Google Security Operations. The feeds include Chrome Enterprise Premium content specific to IAP and context access aware data.
Google Cloud Logs
Cloud Identity Devices
Cloud Identity Device Users
Before you begin
Before you set up feeds to ingest Chrome Enterprise Premium data, complete the following tasks:
Connect your Google Cloud organization to Google Security Operations by completing the following sections:
Enable telemetry ingestion to Google Security Operations
.
Enable the export of Google Cloud logs to Google Security Operations
.
Enable the Cloud Identity API and create a service account to authenticate the API.
Create a domain-wide delegation.
Create a user for impersonation.
Enable the Cloud Identity API and create a service account
In the Google Cloud console, select the Google Cloud project for
which you want to enable the API, and then go to the
APIs & Services
page:
Go to
APIs & Services
Click
Enable APIs and Services
.
Search for "Cloud Identity API".
In the search results, click
Cloud Identity API
.
Click
Enable
.
Create a service account:
In the Google Cloud console, select
IAM & Admin
>
Service Accounts
.
Click
Create service account
.
On the
Create service account page
, enter a name for the service account.
Click
Done
.
Select the service account that you created.
Copy and save the ID that appears in the
Unique ID
field. You use this ID
when you create a domain-wide delegation.
Select the
Keys
tab.
Click
Add key
>
Create new key
.
Select
JSON
as the
Key type
.
Click
Create
.
Copy and save the JSON key. You use this key when you set up feeds.
For more information, see
Enable the Cloud Identity API and create a service account to authenticate the
   API
.
Create a domain-wide delegation
To control API access for the service account using domain-wide delegation, do
the following:
From the Google Admin console Home page, select
Security
>
Access
and Data Controls
>
API Controls
.
Select
Domain-wide delegation
>
Manage Domain-Wide Delegation
.
Click
Add new
.
Enter the service account client ID. The service account client ID is the unique ID
that you obtained when you created a service account.
In
OAuth scopes
, enter
https://www.googleapis.com/auth/cloud-identity.devices.readonly
.
Click
Authorize
.
For more information, see
Control API access with domain-wide delegation
Create a user for impersonation
From the Google Admin console Home page, select
Directory
>
Users
.
To add a new user, do the following:
Click
Add new user
.
Enter a name for the user.
Enter the email address associated with the user.
Click
Create
, and then click
Done
.
To create a new role and assign a privilege, do the following:
Select the newly created username.
Click
Admin roles and privileges
.
Click
Create custom role
.
Click
Create new role
.
Enter a name for the role.
Select
Services
>
Mobile Devices Management
, and then select the
Manage Devices and Setting
privilege.
Click
Continue
.
To assign the role to the user, do the following:
Click
Assign Users
.
Navigate to the newly created user and click
Assign Role
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
Enter a unique name for the
Field name
(for example,
Chrome Enterprise Premium logs
).
Select
Third party API
as the
Source type
.
In the
Log type
list, select either
GCP Cloud Identity Devices
or
GCP Cloud Identity Device Users
.
Click
Next
.
On the
Input parameters
tab, specify the following details:
OAuth JWT endpoint
. Enter
https://oauth2.googleapis.com/token
.
JWT claims issuer
. Specify <insert_service_account@project.iam.gserviceaccount.com>.
This is the service account you created in the section
Enable the Cloud Identity API and create a service account
.
JWT claims subject
. Enter the email of the user that you created in the section
Create a user for impersonation
.
JWT claims audience
. Enter
https://oauth2.googleapis.com/token
.
RSA private key
. Enter the JSON key that was created when you created a
service account to authenticate the API.
API version
. Optional. You can leave this field blank.
Click
Next
.
On the
Finalize
tab, review the values that you entered and then click
Submit
.
Need more help?
Get answers from Community members and Google SecOps professionals.
