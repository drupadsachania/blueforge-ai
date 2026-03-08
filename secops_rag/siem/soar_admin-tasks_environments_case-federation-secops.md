# Set up federated case access for SecOps

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/environments/case-federation-secops/  
**Scraped:** 2026-03-05T09:15:14.896391Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set up federated case access for SecOps
Supported in:
Google secops
The case management federation feature lets secondary customers
have their own separate Google Security Operations platform, rather than having their
Google SecOps instance operating as environments within a
shared instance. This setup is ideal for Managed Security Service Providers (MSSPs)
or enterprises that require independent platforms across geographic regions.
All case metadata is synchronized from the secondary (remote) platform to the primary provider's platform as follows:
Primary platform analysts can view, access, and act on federated cases if they've been granted access.
Secondary customers retain control over which environments and cases are accessible to the primary platform.
When a primary platform analyst opens a remote case link, the system redirects them to the remote platform, if they have the necessary permissions to access the case's environment. On the remote platform, the primary platform analyst can sign in with their email and password. Access requires valid credentials and is granted for the current session only.
Add secondary platform access for primary platform users
To assign access to one or more remote (secondary) platforms, follow these steps:
In the primary platform, go to
SOAR Settings
>
Advanced
>
Group Mapping
.
Add or edit users, as needed. For more information on how to add users, see
Map users in the SecOps platform
.
In the
Platform
field, select as many remote platforms as needed.
Click
Save
.
Register a new secondary platform on the primary platform
To register a secondary platform, you need an Admin API key for the primary platform and to carry out an API call to generate a sync API key. 

Create a new Admin API key if you don't already have one by following these steps, or you can read more about
managing API keys
:
Go to
SOAR Settings
>
Advanced
>
API keys
.
Create a new Admin API key.
Generate the sync API key by following these steps:
Execute the following API call, where the variable `$PRIMARY_INSTANCE_URL` is the root URL of your primary SOAR instance, for example `https://primaryinstance.siemplify-soar.com`, and the value for `"host"`. In the data payload, set the "host" value to your secondary SOAR instance, without the `https` prefix (for example `mysecondary.siemplify-soar.com`).
curl --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms" \
--header 'Content-Type: application/json' \
--header "AppKey: $ADMIN_API_KEY" \
--data '{
"displayName": "My Secondary Platform",
"host": "mysecondary.siemplify-soar.com"
}'
This returns a sync API key which is unique per secondary platform and used to authenticate to the primary platform.
Set up metadata sync on the secondary (remote) platform
To enable synchronization on the secondary platform, complete the following steps on the secondary SecOps instance.
Download the Case Federation integration
To download the Case Federation integration, follow these steps:
In the platform, go to the
Content Hub
.
Select the
Response Integrations
tab and search for
Case Federation
.
Click the
Case Federation integration configuration
and then
click
Save
. Don't select the
Is Primary
checkbox.
Go to
Response
>
Job Scheduler
, and then click
add
Add
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
The hostname is the platform URL without the `https://` prefix (for example, `primaryinstance.siemplify-soar.com`).
In the
API key
field, enter the sync API key you created previously.
Set the default sync time to one minute.
Click
Save
.
Grant access to primary users
This procedure lets you grant permissions to specific environments
for the relevant primary platform personas. This lets the primary analyst 
pivot to the relevant cases in the secondary platform.
To create or edit a user on the secondary platform, follow these steps:
In the secondary platform, go to
SOAR Settings
>
Advanced
>
IAM Role Mapping
.
Add or edit users, as needed. For more information on how to add or edit users, see
Map users in the Google SecOps platform
.
In the
Environment
field, select the environments that primary platform analysts can access.
Click
Save
.
Access remote cases from the primary platform
Primary platform users can view remote cases either in the list view or side-by-side view on the
Cases
page
To open cases on the remote platform, follow these steps:
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
Click a remote case to open it in the corresponding remote platform.
List view
Locate remote cases in the
Platform
column.
Click the
case ID
to open the case in the remote platform.
Sign in to the remote platform with your email and password.
If you can't sign in, it means that the secondary customer may not have granted you access to the case's source environment.
List secondary platforms
You can list secondary platforms from the primary platform by running the following command, which returns a list of platform names and IDs:
curl --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms/{platform_id}"
--header 'Content-Type: application/json'
--header "AppKey: $ADMIN_API_KEY"
Delete secondary platforms
You can delete secondary platforms from the primary platform by running the following command:
curl -X DELETE --location "$PRIMARY_INSTANCE_URL/api/external/v1/federation/platforms/{platform_id}"
--header "AppKey: $ADMIN_API_KEY"
Need more help?
Get answers from Community members and Google SecOps professionals.
