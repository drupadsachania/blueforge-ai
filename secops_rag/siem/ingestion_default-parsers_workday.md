# Collect Workday HCM logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/workday/  
**Scraped:** 2026-03-05T09:30:23.351185Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Workday HCM logs
Supported in:
Google secops
SIEM
This document explains how to ingest Workday logs to Google Security Operations using the API. The parser extracts Workday HCM user data from JSON-formatted logs. It handles various data transformations, including renaming fields, merging nested objects, parsing dates, and populating UDM fields for user attributes, employment details, and organizational structure. Additionally, it includes error handling for malformed JSON and missing critical fields.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Workday.
Configure Workday API Authentication
Create an Integration System User (ISU) in Workday
Sign in to Workday with administrative privileges.
Type
Create Integration System User
in the search bar and select the task from the results.
Enter a
Username
.
Set a
Password
.
Set
Session Timeout Minutes
to
0
to prevent the ISU from timing out.
Enable
Do Not Allow UI Sessions
to enhance security by restricting UI logins.
Go to the
Maintain Password Rules
task.
Add the integration system user to the
System Users exempt from password expiration
field.
Create an integration security group in Workday
Type
Create Security Group
in the search bar and select the task from the results.
Locate the
Type of Tenanted Security Group
field, and select
Integration System Security Group (Unconstrained)
.
Provide a
Name
for the security group.
Click
OK
.
Click
Edit
for the newly created security group.
Assign
the
Integration System User
from the previous step to the security group.
Click
Done
.
Grant domain access to security group in Workday
Type
Maintain Permissions for Security Group
in the search bar and select the task from the results.
Choose the security group you created from the
Source Security Group
list to modify its permissions.
Click
OK
.
Go to
Maintain Permissions for Security Group
>
Domain Security Policy Permissions
.
Assign the necessary permissions for each domain, such as GET operations.
Click
OK
.
Click
Done
to save changes.
Activate security policy changes in Workday
Type
Activate Pending Security Policy Changes
in the search bar and select the task from the results.
Start the
Activate Pending Security Policy Changes
task by entering a reason for your audit in the comment field, then click
OK
.
Complete the task on the next screen by selecting
Confirm
, then click
OK
.
Configure API Client for Integrations
In the search bar, type
Register API Client for Integrations
and select it.
Click
Create
.
Provide the following configurations details:
Client Name
: Enter a name for the API client (for example,
Google SecOps Client
).
System User
: Select the
Integration System User
you created in the previous step.
Scope
: Select HCM API or the relevant scope that includes the worker data and other areas you're accessing.
Select
Save
.
Click
OK
to create the API client.
After creating the API client,
Save
the
Client Secret
. It will not be displayed again after you exit the page.
Generate OAuth 2.0 Refresh Token
In the Workday search bar, type
Manage Refresh Tokens for Integrations
and select it.
Click
Generate New Refresh Token
.
In the
Workday Account
field, search for and select the
Integration System User
you created.
Select the user and click
OK
.
Copy and save the refresh token displayed.
Get API Endpoint URLs
In the Workday search bar, type
View API Clients
and select it.
Under
API Clients for Integrations
, locate the
Google SecOps Client
you created.
Copy and save the following details:
Token Endpoint
: The
URL
you will send a request to obtain an access token.
Workday REST API Endpoint
: The
URL
you'll use to configure the integration with Google SecOps.
Generate OAuth Access Token
Use curl or a similar HTTP client to send a POST request to the Token Endpoint:
curl
-X
POST
"https://{hostname}/ccx/oauth2/token"
\
-d
"grant_type=refresh_token"
\
-d
"client_id={your_client_id}"
\
-d
"client_secret={your_client_secret}"
\
-d
"refresh_token={your_refresh_token}"
This will return an
access token
(for example,
"access_token": "abcd1234"
)
Copy and save the access token.
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
Workday Logs
).
Select
Third Party API
as the
Source type
.
Select the
Workday
log type.
Click
Next
.
Specify values for the following input parameters:
API Hostname
: the URL of your Workday REST API Endpoint.
Tenant
: the last path element of your Workday API endpoint that identifies your instance.
Access Token
: OAuth access token.
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
@timestamp
read_only_udm.metadata.event_timestamp.seconds
The raw log's
@timestamp
field is renamed to
timestamp
and parsed as a timestamp in seconds since epoch.
businessTitle
read_only_udm.entity.entity.user.title
Directly mapped from the
businessTitle
field in the raw log.
descriptor
read_only_udm.entity.entity.user.user_display_name
Directly mapped from the
descriptor
field in the raw log.
Employee_ID
read_only_udm.entity.entity.user.employee_id
Directly mapped from the
Employee_ID
field in the raw log.
Employee_ID
read_only_udm.entity.metadata.product_entity_id
Directly mapped from the
Employee_ID
field in the raw log when
id
is not present.
gopher-supervisor.descriptor
read_only_udm.entity.entity.user.managers.user_display_name
Directly mapped from the
gopher-supervisor.descriptor
field in the raw log, renamed to
empmanager.user_display_name
and then merged into
managers
.
gopher-supervisor.id
read_only_udm.entity.entity.user.managers.product_object_id
Directly mapped from the
gopher-supervisor.id
field in the raw log, renamed to
empmanager.product_object_id
and then merged into
managers
.
gopher-supervisor.primaryWorkEmail
read_only_udm.entity.entity.user.managers.email_addresses
Directly mapped from the
gopher-supervisor.primaryWorkEmail
field in the raw log and then merged into
managers
.
gopher-time-off.date
read_only_udm.entity.entity.user.time_off.interval.start_time
Parsed as a date from the
gopher-time-off.date
field within the
gopher-time-off
array in the raw log.
gopher-time-off.descriptor
read_only_udm.entity.entity.user.time_off.description
Directly mapped from the
gopher-time-off.descriptor
field within the
gopher-time-off
array in the raw log.
Hire_Date
read_only_udm.entity.entity.user.hire_date
Parsed as a date from the
Hire_Date
field in the raw log.
id
read_only_udm.entity.metadata.product_entity_id
Directly mapped from the
id
field in the raw log when present.
Job_Profile
read_only_udm.entity.entity.user.title
Directly mapped from the
Job_Profile
field in the raw log when
businessTitle
is not present.
Legal_Name_First_Name
read_only_udm.entity.entity.user.first_name
Directly mapped from the
Legal_Name_First_Name
field in the raw log.
Legal_Name_Last_Name
read_only_udm.entity.entity.user.last_name
Directly mapped from the
Legal_Name_Last_Name
field in the raw log.
location.descriptor
read_only_udm.entity.entity.location.city
Directly mapped from the
location.descriptor
field in the raw log, renamed to
_location.city
and then to
entity.entity.location.city
.
primarySupervisoryOrganization.descriptor
read_only_udm.entity.entity.user.department
Directly mapped from the
primarySupervisoryOrganization.descriptor
field in the raw log.
primaryWorkEmail
read_only_udm.entity.entity.user.email_addresses
Directly mapped from the
primaryWorkEmail
field in the raw log.
primaryWorkPhone
read_only_udm.entity.entity.user.phone_numbers
Directly mapped from the
primaryWorkPhone
field in the raw log.
Termination_Date
read_only_udm.entity.entity.user.termination_date
Parsed as a date from the
Termination_Date
field in the raw log.
Work_Email
read_only_udm.entity.entity.user.email_addresses
Directly mapped from the
Work_Email
field in the raw log when
primaryWorkEmail
is not present.
collection_time
read_only_udm.metadata.event_timestamp.collected_timestamp
The log's
collection_time
is mapped to
collected_timestamp
.
Need more help?
Get answers from Community members and Google SecOps professionals.
