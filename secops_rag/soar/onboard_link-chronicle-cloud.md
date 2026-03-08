# Link a Google SecOps instance to Google Cloud services

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/link-chronicle-cloud/  
**Scraped:** 2026-03-05T09:45:31.630921Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Link a Google SecOps instance to Google Cloud services
Supported in:
Google secops
SIEM
A Google Security Operations instance depends on Google Cloud services for certain key capabilities,
such as authentication.
This document explains how to configure your instance to link to these services, whether you're setting up a new deployment or migrating an existing Google SecOps instance.
Before you begin
Before you configure a Google SecOps instance with Google Cloud
services, you must do the following:
Verify permissions
. Ensure you have the necessary permissions to complete
the steps in this document. For information about required permissions for
each phase of the onboarding process, see
Required roles and permissions
.
Choose your project setup
: You can either create a new Google Cloud
project for your Google SecOps instance or link it to an
existing Google Cloud project.
To create a new Google Cloud project and enable the Chronicle API, follow the
steps in
Create a Google Cloud project
.
Configure an SSO provider for the Google SecOps instance
:
You can use Cloud Identity, Google Workspace, or a third-party identity
provider (IdP), as follows:
If you use a third-party IdP, perform the steps in
Configure a third-party identity provider for Google SecOps
.
If you use Cloud Identity or Google Workspace, perform the steps in
Configure a Google Cloud identity provider for Google SecOps
.
To link a Google SecOps instance created for a Manage Security
Services Provider (MSSP), contact your Google SecOps
representative. Setup requires assistance from a Google SecOps
representative.
After linking a Google SecOps instance to a Google Cloud project,
the Google SecOps instance is now ready for further
configuration. You can now examine ingested data and monitor the project for
potential security threats.
Configure a new Google SecOps instance
Linking your new instance to a project enables authentication and monitoring
features, including:
Cloud Identity integration for accessing a range of Google Cloud services,
such as authentication, Identity and Access Management, Cloud Monitoring, and Cloud Audit Logs.
IAM and Workforce Identity Federation support for
authenticating with your existing third-party IdP.
To link a Google SecOps instance to a Google Cloud project, perform these steps:
After your organization signs the Google SecOps customer
contract, the onboarding SME receives an onboarding invitation email with an
activation link. The activation link is valid for one-time use only.
In the onboarding invitation email, click the
Go to Google Cloud
activation link 
to open the
Link SecOps to a project
page.
Click
Select a project
to open the
Select a resource
page.
On the
Select a resource
page, select a Google Cloud project to link your
new Google SecOps instance. There are two options:
Option 1:
Create a new Google Cloud project
:
Click
New Project
, and follow the steps described in
Create a Google Cloud project
.
Option 2:
Select an existing project
from the list:
Follow the steps described in
Select an existing project
.
After you select a project, the system enables the
Add contacts
button, and the
Add essential contacts
section displays the
Essential contacts
table.
This table shows notification
Categories
and the
Email
address of the
contact assigned to each.
Assign a contact person to at least the following four mandatory notification
categories:
technical
,
security
,
legal
, and
billing
.
Assign a contact to one or more notification categories as follows:
To open the
Edit contact
window, click
Add contact
or click
edit
Edit
in a notification
category with an existing contact.
Enter the contact person's
Email
address, and select one or more
notification
Categories
.
Click
Save
.
Click
Next
.
The system checks whether the Chronicle API is enabled. If enabled, the
Onboarding
page displays the pre-filled onboarding information and runs
the deployment process. This process can take up to 15 minutes to complete.
When the deployment completes successfully, you receive a notification.
If the deployment fails, contact
Google SecOps Support
.
Verify that the deployment is correct as follows:
To view instance information, go to
https://console.cloud.google.com/security/chronicle/settings.
To update any information, contact
Google SecOps Support
.
Select an existing project
On the
Select a resource
page, select your
Organization
from the list.
The page displays a list of the Google Cloud projects and folders.
These belong to the same organization as the Google SecOps
instance, and they have the same billing account.
If a project or folder has a
warning
Warning
icon next to it, you cannot select it. Hold the
pointer over the icon to view the reason, for
example: missing permissions or billing mismatch.
Select a project based on the following criteria:
Criteria for linking an instance to a Google Cloud project
:
The Google Cloud project must not already be linked to another
Google SecOps instance.
You have the required IAM permissions to access and work with the
project, see
Permissions to add a Google Cloud project
.
For a
compliance controlled
tenant (instance), the project must be in an
Assured Workloads folder. See
Workforce Identity Federation
for details.
A
compliance controlled
tenant (instance) conforms to one of the
following compliance control standards:
FedRAMP
,
FedRAMP_MODERATE
,
HIPAA
,
PCI_DSS
,
FedRAMP_HIGH
,
IL4
,
IL5
,
CMEK_V1
, or
DRZ_ADVANCED
.
To select a Google Cloud project for a
compliance controlled
tenant (instance):
Select an Assured Workloads folder to open it.
Inside the Assured Workloads folder, click the name of a
Google Cloud project to open the
Link SecOps to a project
page.
Complete the configuration described in
Configure the IdP
.
To select a Google Cloud project for a
non-compliance controlled
tenant (instance):
Click the name of a valid Google Cloud project to open the
Link SecOps to a project
page.
On the
Link SecOps to a project
page, select a different project,
if needed. To do so, you click the project to display the
Select a resource
page again.
Click
Next
to link your Google SecOps instance to
  the selected project, and open the
Deployment
page.
The
Deployment
page displays the final details of your instance and
service and requires your consent before performing the final ddx. The page
consists of sections displaying pre-filled, non-editable fields. Only a
Google representative can change these details.
Review the details in each of the following sections. Click
Next
to move to the next section:
Instance details
The page displays instance details set in your contract, for example
company, region, package tier, and data retention duration.
Click
Next
to display the next section.
Review service account
The page displays details of the service account to be created.
Click
Next
to display the next section.
Configure single sign-on (SSO)
Choose a configured SSO provider. Select one of the following
options based on the identity provider you use to manage user and
group access to Google SecOps:
Google Cloud Identity
:
Select this if you are using Cloud Identity or Google Workspace.
Workforce Identity Federation
:
If you are using a third-party identity provider, select your
workforce provider
from the list.
If you don't see your identity provider listed, configure your
provider, and then select your provider from the list. For details, see
Configure a third-party identity provider
.
Click
Next
to display the next section.
Terms of service
Select the
I agree to...
checkbox to agree to the terms.
Click
Start setup
to deploy your
Google SecOps instance, according to the displayed
details.
Click here to continue to the
Next
step.
Migrate an existing Google SecOps instance
The following sections explain how to migrate an existing
Google SecOps instance to link it to a Google Cloud project and
use IAM for feature access control.
Link to a project and workforce provider
The following procedure describes how to connect an existing Google SecOps
instance with a Google Cloud project and configure SSO using IAM
Workforce Identity Federation services.
Sign in to Google SecOps.
Select
Settings > SIEM Settings
.
Click
Google Cloud Platform
.
Enter the Google Cloud project ID to link the project to the Google SecOps instance.
Click
Generate Link
.
Click
Connect to Google Cloud Platform
. The Google Cloud console opens.
If you enter an incorrect Google Cloud project ID in the Google SecOps
application, return to the
Google Cloud Platform
page in Google SecOps and enter the correct project ID.
On the Google Cloud console, go to
Security > Google SecOps
.
Verify the service account that the system created for the Google Cloud project.
Under
Configure single sign-on
, select one of the following options
based on which identity provider you use to manage user and group access to Google SecOps:
If you are using Cloud Identity or Google Workspace, select
Google Cloud Identity
.
If you are using a third-party identity provider, select
Workforce Identity Federation
,
and then select the workforce provider you want to use. You set this up when
configuring workforce identity federation
.
If you select
Workforce Identity Federation
, right-click the
Test SSO setup
link, and then open it in a private or incognito window.
If you see a login screen, then SSO setup is successful.
If you don't see a login screen, check the configuration of the third-party identity
provider.
See
Configure a third-party identity provider for Google SecOps
.
Continue with the next section:
Migrate existing permissions to IAM
.
Migrate existing permissions to IAM
After you migrate an
existing Google SecOps instance
,
you can use auto-generated commands to migrate existing permissions and
roles to IAM. Google SecOps creates these commands
using your pre-migration
Feature RBAC
access control configuration.
When run, they create new IAM policies equivalent to your existing
configuration, as defined in Google SecOps under the
SIEM Settings
>
Users and Groups
page.
After you run these commands, you can't revert back to the previous
Feature RBAC
access control feature. If you encounter an issue, contact
Google SecOps Technical Support
.
On the Google Cloud console, go to
Security
>
Google SecOps
>
Access
management
tab.
Under
Migrate role bindings
, you will see a set of auto-generated
Google Cloud CLI commands.
Review and verify that the commands create the expected permissions.
For information about Google SecOps roles and permissions,
see
How IAM permissions map to each Feature RBAC role
.
Launch a Cloud Shell session.
Copy the auto-generated commands, then paste and run them in the
gcloud CLI.
After you execute all commands, click
Verify Access
.
If successful, you see the message
Access verified
on the Google SecOps
Access Management
. Otherwise, you see
the message
Access denied
. This may take 1-2 minutes to appear.
To complete the migration, return to the
Security
>
Google SecOps
>
Access
management
tab, and then click
Enable IAM
.
Verify that you can access Google SecOps as a user with the
Chronicle API Admin role.
Sign in to Google SecOps as a user with the Chronicle API Admin
predefined role. For more details, see
Sign in to Google SecOps
.
Open the
SIEM Settings > Users & Groups
page.
You should see the message:
To manage users and groups, go to
Identity Access Management (IAM)
in the Google Cloud console. Learn more about managing users and groups.
Sign in to Google SecOps as a user with a different role. 
For more details, see
Sign in to Google SecOps
.
Verify that available features in the application match the permissions
defined in IAM.
Change SSO configuration
The following sections describe how to change identity providers:
Change the third-party identity provider
Migrate from a third-party identity provider to Cloud Identity
Change the third-party identity provider
Set up the new
third-party identity provider and workforce identity pool
.
In Google SecOps, under
Settings
>
SOAR settings
>
Advanced
>
IDP group mapping
,
change the
IdP group mapping
to reference groups in the new identity provider.
Update SSO settings
Complete the following steps to change the SSO configuration for Google SecOps:
Open the Google Cloud console, and then select the Google Cloud project that is
bound to Google SecOps.
Go to
Security > Google SecOps
.
On the
Overview
page, click the
Single Sign-On
tab. This page displays
the IdPs you configured when
Configuring a third-party identity provider for Google SecOps
.
Use the
Single Sign-On
menu to change SSO providers.
Right-click the
Test SSO setup
link, and then open a private or incognito window.
If you see a login screen, then SSO setup is successful. Continue with the next step.
If you don't see a login screen, check the configuration of the third-party identity provider.
See
Configure a third-party identity provider for Google SecOps
.
Return to Google Cloud console, click the
Security > Google SecOps > Overview
page, and then click the
Single Sign-On
tab.
Click
Save
at the bottom of the page to update the new provider.
Verify that you can sign in to Google SecOps.
Migrate from third-party identity provider to Cloud Identity
Complete the following steps to change the SSO configuration from using a third-party identity provider to
Google Cloud Identity
:
Make sure you configure either Cloud Identity or Google Workspace as the identity provider.
Grant the predefined Chronicle IAM roles and custom roles to users and groups in the Google SecOps-bound project.
Grant the
Chronicle SOAR Admin
role to the relevant users or groups.
In Google SecOps, under
Settings
>
SOAR settings
>
Advanced
>
IDP group mapping
,
add the
Chronicle SOAR Admin
. For more information, see
IdP group mapping
.
Open the Google Cloud console, and then select the Google Cloud project that is
bound to Google SecOps.
Go to
Security > Chronicle SecOps
.
On the
Overview
page, click the
Single Sign-On
tab. This page displays
the IdPs you configured when
Configuring a third-party identity provider for Google SecOps
.
Select the
Google Cloud Identity
checkbox.
Right-click the
Test SSO setup
link, and then open a private or incognito window.
If you see a login screen, then SSO setup is successful. Continue with the next step.
If you don't see a login screen, check the configuration of the identity provider.
Return to Google Cloud console, and then click
Security > Chronicle SecOps
>
Overview
page >
Single Sign-On
tab.
Click
Save
at the bottom of the page to update the new provider.
Verify that you can sign in to Google SecOps.
Need more help?
Get answers from Community members and Google SecOps professionals.
