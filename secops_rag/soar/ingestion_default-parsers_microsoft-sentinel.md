# Collect Microsoft Sentinel logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-sentinel/  
**Scraped:** 2026-03-05T09:58:13.829170Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Sentinel logs
Supported in:
Google secops
SIEM
This document explains how to configure Microsoft Sentinel to send incidents and alerts to Google Security Operations using Logic Apps and webhooks.
Microsoft Sentinel is a cloud-native security information and event management (SIEM) and security orchestration, automation, and response (SOAR) solution. It delivers intelligent security analytics and threat intelligence across the enterprise.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to
Microsoft Azure
portal with permissions to:
Create Logic Apps
Configure Microsoft Sentinel automation rules
Manage resource group permissions
Create and manage service principals
Access to Google Cloud console (for API key creation)
Create webhook feed in Google SecOps
Create the feed
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
Microsoft Sentinel Incidents
).
Select
Webhook
as the
Source type
.
Select
Microsoft Sentinel
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
(optional): Leave empty (each incident or alert is a single event).
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
Generate and save secret key
After creating the feed, you must generate a secret key for authentication:
On the feed details page, click
Generate Secret Key
.
A dialog displays the secret key.
Copy and save the secret key securely.
Get the feed endpoint URL
Go to the
Details
tab of the feed.
In the
Endpoint Information
section, copy the
Feed endpoint URL
.
The URL format is:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
or
https://<REGION>-malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
Save this URL for the next steps.
Click
Done
.
Create Google Cloud API key
Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud console.
Create the API key
Go to the
Google Cloud console Credentials page
.
Select your project (the project associated with your Google SecOps instance).
Click
Create credentials
>
API key
.
An API key is created and displayed in a dialog.
Click
Edit API key
to restrict the key.
Restrict the API key
In the
API key
settings page:
Name
: Enter a descriptive name (for example,
Google SecOps Webhook API Key
).
Under
API restrictions
:
Select
Restrict key
.
In the
Select APIs
list, search for and select
Google SecOps API
(or
Chronicle API
).
Click
Save
.
Copy
the API key value from the
API key
field at the top of the page.
Save the API key securely.
Configure Logic App for Microsoft Sentinel incidents
This section configures a Logic App to send Microsoft Sentinel incidents to Google SecOps.
Create Logic App
Sign in to
Azure Portal
.
Click
Create a resource
.
Search for
Logic App
.
Click
Create
to start the creation process.
Specify values for the following input parameters:
Subscription
: Select the subscription.
Resource group
: Select the resource group.
Name
: Enter a name for the Logic App (for example,
Sentinel-Incidents-to-SecOps
).
Region
: Select the region.
Log Analytics workspace
: Select the Log Analytics workspace.
Click
Review + create
.
Click
Create
.
After the Logic App is created, click
Go to resource
.
Configure Logic App designer
Click
Development Tools
>
Logic App Designer
.
Click
Add a trigger
.
Search for
Microsoft Sentinel
.
Select
Microsoft Sentinel incident
as the trigger.
If you haven't already created a connection to Microsoft Sentinel, you'll need to do so now.
Click
Create new
and follow the prompts to authenticate:
Select
Sign in with managed identity
(recommended) or
Sign in
to use your credentials.
Click
Insert a new step
.
Click
Add an action
.
Search for and select
HTTP
as the action.
Specify values for the following input parameters:
URI
: Paste the feed endpoint URL from the Google SecOps feed.
Method
: Select
POST
.
Headers
: Add the following headers:
Header name
:
X-goog-api-key
Value
: Paste the API key created earlier.
Header name
:
X-Webhook-Access-Key
Value
: Paste the secret key from the feed creation.
Click in the
Body
field.
Click the
Expression
tab in the dynamic content panel.
Enter
@{triggerBody()}
in the expression field and click
OK
.
Click
Save
to save the Logic App.
Grant Microsoft Sentinel permissions to run Logic App
Two separate permission assignments are required for automation rules to successfully trigger the Logic App.
Permission 1: Grant Logic App managed identity access to Sentinel workspace
The Logic App's managed identity needs permission to read incidents from the Microsoft Sentinel workspace.
Enable managed identity for Logic App
In the
Azure Portal
, go to your Logic App resource (
Sentinel-Incidents-to-SecOps
).
In the left navigation, select
Identity
under
Settings
.
On the
System assigned
tab, set
Status
to
On
.
Click
Save
.
Click
Yes
to confirm.
After enabling, note the
Object (principal) ID
displayed.
Grant Microsoft Sentinel Responder role to Logic App
In the
Azure Portal
, navigate to your
Microsoft Sentinel workspace
.
In the left navigation, select
Access control (IAM)
under
Settings
.
Click
+ Add
>
Add role assignment
.
In the
Role
tab, search for and select
Microsoft Sentinel Responder
:
Alternative
: If the playbook only reads incidents, use
Microsoft Sentinel Reader
role.
Click
Next
.
In the
Members
tab, configure the following:
Assign access to
: Select
Managed identity
.
Click
+ Select members
.
In the
Managed identity
list, select
Logic App
.
Select your Logic App (
Sentinel-Incidents-to-SecOps
) from the list.
Click
Select
.
Click
Review + assign
.
Click
Review + assign
again to confirm.
Permission 2: Grant Microsoft Sentinel automation permissions on resource group
Microsoft Sentinel requires
Microsoft Sentinel Automation Contributor
role on the resource group containing the Logic App. Without this permission, automation rules cannot trigger playbooks.
Grant automation permissions via Sentinel UI
In the
Azure Portal
, navigate to your
Microsoft Sentinel workspace
.
Go to
Settings
>
Automation
.
Click
Manage playbook permissions
at the top of the page.
In the
Manage permissions
pane, configure the following:
Select the
resource group
containing your Logic App (
Sentinel-Incidents-to-SecOps
).
Click
Apply
.
Verify automation permissions (Optional)
In the
Azure Portal
, navigate to the
resource group
containing your Logic App.
In the left navigation, select
Access control (IAM)
.
Click
Role assignments
.
Search for
Azure Security Insights
.
Verify that
Azure Security Insights
has the
Microsoft Sentinel Automation Contributor
role.
Go to the
resource group
containing your Logic App.
Select
Access control (IAM)
>
Add role assignment
.
Select
Microsoft Sentinel Automation Contributor
role.
In
Members
, select
User, group, or service principal
.
Click
+ Select members
and search for
Azure Security Insights
.
Select
Azure Security Insights
and click
Select
.
Click
Review + assign
twice to confirm.
Configure Logic App for Microsoft Sentinel alerts
This section configures a separate Logic App to send Microsoft Sentinel alerts to Google SecOps.
Create Logic App for alerts
Go to
Azure Portal Home Page
.
Click
Create a resource
.
Search for
Logic App
.
Click
Create
to start the creation process.
Specify values for the following input parameters:
Subscription
: Select the subscription.
Resource group
: Select the resource group.
Name
: Enter a name for the Logic App (for example,
Sentinel-Alerts-to-SecOps
).
Region
: Select the region.
Log Analytics workspace
: Select the Log Analytics workspace.
Click
Review + create
.
Click
Create
.
After the Logic App is created, click
Go to resource
.
Configure Logic App designer for alerts
Click
Development Tools
>
Logic App Designer
.
Click
Add a trigger
.
Search for
Microsoft Sentinel
.
Select
Microsoft Sentinel alert
as the trigger.
If you haven't already created a connection to Microsoft Sentinel, you'll need to do so now.
Click
Create new
and follow the prompts to authenticate:
Select
Sign in with managed identity
(recommended) or
Sign in
to use your credentials.
Click
Insert a new step
.
Click
Add an action
.
Search for and select
HTTP
as the action.
Specify values for the following input parameters:
URI
: Paste the feed endpoint URL from the Google SecOps feed.
Method
: Select
POST
.
Headers
: Add the following headers:
Header name
:
X-goog-api-key
Value
: Paste the API key created earlier.
Header name
:
X-Webhook-Access-Key
Value
: Paste the secret key from the feed creation.
Click in the
Body
field.
Click the
Expression
tab in the dynamic content panel.
Enter
@{triggerBody()}
in the expression field and click
OK
.
Click
Save
to save the Logic App.
Grant Microsoft Sentinel permissions to run alerts Logic App
Two separate permission assignments are required for the alerts Logic App, identical to the incidents Logic App configuration.
Permission 1: Grant alerts Logic App managed identity access to Sentinel workspace
The alerts Logic App's managed identity needs permission to read alerts from the Microsoft Sentinel workspace.
Enable managed identity for alerts Logic App
In the
Azure Portal
, go to your alerts Logic App resource (
Sentinel-Alerts-to-SecOps
).
In the left navigation, select
Identity
under
Settings
.
On the
System assigned
tab, set
Status
to
On
.
Click
Save
.
Click
Yes
to confirm.
After enabling, note the
Object (principal) ID
displayed.
Grant Microsoft Sentinel Responder role to alerts Logic App
In the
Azure Portal
, navigate to your
Microsoft Sentinel workspace
.
In the left navigation, select
Access control (IAM)
under
Settings
.
Click
+ Add
>
Add role assignment
.
In the
Role
tab, search for and select
Microsoft Sentinel Responder
:
Alternative
: If the playbook only reads alerts, use
Microsoft Sentinel Reader
role.
Click
Next
.
In the
Members
tab, configure the following:
Assign access to
: Select
Managed identity
.
Click
+ Select members
.
In the
Managed identity
list, select
Logic App
.
Select your alerts Logic App (
Sentinel-Alerts-to-SecOps
) from the list.
Click
Select
.
Click
Review + assign
.
Click
Review + assign
again to confirm.
Permission 2: Grant Microsoft Sentinel automation permissions on resource group for alerts
Microsoft Sentinel requires
Microsoft Sentinel Automation Contributor
role on the resource group containing the alerts Logic App.
Grant automation permissions via Sentinel UI
In the
Azure Portal
, navigate to your
Microsoft Sentinel workspace
.
Go to
Settings
>
Automation
.
Click
Manage playbook permissions
at the top of the page.
In the
Manage permissions
pane, configure the following:
Select the
resource group
containing your alerts Logic App (
Sentinel-Alerts-to-SecOps
).
If this is the same resource group as the incidents Logic App, it may already be selected.
Click
Apply
.
Verify automation permissions for alerts Logic App (Optional)
In the
Azure Portal
, navigate to the
resource group
containing your alerts Logic App.
In the left navigation, select
Access control (IAM)
.
Click
Role assignments
.
Search for
Azure Security Insights
.
Verify that
Azure Security Insights
has the
Microsoft Sentinel Automation Contributor
role.
Configure automation rules for Microsoft Sentinel
Automation rules trigger Logic Apps when incidents are created or updated in Microsoft Sentinel.
Create automation rule for incident creation
Go to your
Microsoft Sentinel Workspace
.
Click
Configuration
>
Automation
.
Click
Create
.
Select
Automation rule
.
Specify values for the following input parameters:
Name
: Enter a name for the automation rule (for example,
Send New Incidents to SecOps
).
Trigger
: Select
When incident is created
.
Actions
: Select
Run playbook
from the list.
Select the Logic App created for incidents (
Sentinel-Incidents-to-SecOps
).
Click
Apply
.
Create automation rule for incident updates
Go to your
Microsoft Sentinel Workspace
.
Click
Configuration
>
Automation
.
Click
Create
.
Select
Automation rule
.
Specify values for the following input parameters:
Name
: Enter a name for the automation rule (for example,
Send Updated Incidents to SecOps
).
Trigger
: Select
When incident is updated
.
Condition
: Click
Add
>
Condition (And)
>
Status
>
Changed
.
In the
Actions
section, configure the following:
Select
Run playbook
from the list.
Select the Logic App created for incidents (
Sentinel-Incidents-to-SecOps
).
Click
Apply
.
Create automation rule for alerts
Go to your
Microsoft Sentinel Workspace
.
Click
Configuration
>
Automation
.
Click
Create
.
Select
Automation rule
.
Specify values for the following input parameters:
Name
: Enter a name for the automation rule (for example,
Send Alerts to SecOps
).
Trigger
: Select
When alert is created
.
Actions
: Select
Run playbook
from the list.
Select the Logic App created for alerts (
Sentinel-Alerts-to-SecOps
).
Click
Apply
.
Need more help?
Get answers from Community members and Google SecOps professionals.
