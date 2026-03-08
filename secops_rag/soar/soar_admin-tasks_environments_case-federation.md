# Set up case federation access for SOAR

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation/  
**Scraped:** 2026-03-05T10:10:35.561793Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set up case federation access for SOAR
Supported in:
SOAR
The case management federation feature lets secondary customers
 have their own standalone SOAR platform, rather than hosting their SOAR instance
    as an environment with a shared platform. This setup is ideal for Managed Security Service Providers (MSSPs)
    or enterprises that require independent platforms across geographic regions.
All case metadata is synchronized from the secondary (remote) platform to the primary provider's platform as follows:
Primary platform analysts can view, access, and act on federated cases if they've been granted access.
Secondary customers retain control over which environments and cases are accessible to the primary platform.
When a primary platform analyst opens a remote case link, the system redirects them to the remote platform, if they have the necessary permissions to access the case's environment. On the remote platform, the primary platform analyst can sign in with their email and password. Access requires valid credentials and is granted for the current session only.
Create or edit a user on the primary platform
To assign access to one or more remote platforms, follow these steps:
In the primary platform, go to
Settings
>
Organization
>
User Management
.
Click
add
Add.
Enter the required information.
In the
Platform
field, select as many remote platforms as needed.
Click
Save
.
Register a new secondary platform on the primary platform
To register a secondary platform, you need an Admin API key for the primary platform and to carry out an API call to generate a sync API key.

Create a new Admin API key if you don't already have one by following these steps:
Go to
SOAR Settings
>
Advanced
>
API keys
.
Create a new Admin API key.
Generate the sync API key by following these steps:
Execute the following API call.
curl --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms" \
--header 'Content-Type: application/json' \
--header "AppKey: $ADMIN_API_KEY" \
--data '{
"displayName": "My Secondary Platform",
"host": "mysecondary.siemplify-soar.com"
}'
This returns a sync API key which is unique per secondary platform and used to authenticate to the primary platform.
Set up metadata sync on the secondary (remote) platform
To enable synchronization on the secondary platform, complete the following steps.
Download the Case Federation integration
To download the Case Federation integration, follow these steps:
In the platform, go to the
Content Hub
.
Click the
Case Federation integration configuration
>
click
Save
. Don't select the
Is Primary
checkbox.
Go to
Response
>
IDE
, and then click
add
Add
.
Select
Job
.
In the
Job Name
field, select
Case Federation Sync Job
.
In the
Integration
field, select
Case Federation
.
Click
Create
.
In the
Target Platform
field, enter the hostname of the primary provider.
    The hostname is taken from the beginning of the primary provider's platform URL.
In the
API key
field, enter the API key provided by your primary provider.
Set the default sync time to one minute.
Create or edit a user on the secondary platform
To give primary analysts access to selected environments, follow these steps:
In the secondary platform, go to
Settings
>
Organization
>
User Management
Click
add
Add.
Enter the required information.
In the
Environment
field, select the environments that the primary platform analysts can access.
Click
Save
.
Access remote cases from the primary platform
The primary platform analyst can move from their local platform to view and manage cases on the remote (secondary) platform. You can do this either in case list view
    or the case side-by-side view on the
Cases
page.
To open a case from the remote platform, follow these steps:
On the
Cases
page, select either
list view
or the
side-by-side view
.
Do any one of the following:
Side-by-side view
In the case queue, look for cases marked with an "R" (for remote).
Click the case to open it in the remote platform.
List view
Scan the
Platform
column to find cases originating from the remote platform.
Click the
case ID
to open it in the remote platform.
Sign in to the remote platform with your email and password.
If you can't sign in, it means that the secondary customer may not have granted you access to the case's source environment.
Need more help?
Get answers from Community members and Google SecOps professionals.
