# Onboard a Google SecOps instance

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/  
**Scraped:** 2026-03-05T09:45:25.113668Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Onboard a Google SecOps instance
Supported in:
Google secops
This document describes how to onboard (deploy) a Google SecOps
(SIEM and SOAR) instance, and enable Google SecOps features based on your
Google SecOps package tier and entitlements. These onboarding steps apply to the
following
Google SecOps packages
:
Standard
,
Enterprise
, and
Enterprise Plus
.
Your designated
onboarding SME
, also referred to as the
Google SecOps SME
or the
billing administrator
, performs the
onboarding process. This person serves as your organization's main point of
contact for Google SecOps.
Prerequisites
Before you can onboard a new Google SecOps instance, make sure
your organization has met these prerequisites:
An active registration for one of the following
Google SecOps packages
:
Standard
,
Enterprise
, or
Enterprise Plus
.
A signed Google SecOps contract from your organization. This contract gives
you permission to provision each new Google SecOps instance.
Deploy a new Google SecOps instance
Perform these steps to deploy a new Google SecOps instance:
Sign the Google SecOps contract.
Provisioning a new Google SecOps instance starts when your
organization signs a Google SecOps contract. This action
triggers Google's internal onboarding workflow and registers the contract
details in Google's system, including your billing account and your
onboarding SME's email address.
Prepare your environment for onboarding
.
Your onboarding SME should prepare your environment before you onboard a new
Google SecOps instance.
Onboard a new Google SecOps instance
.
Contact your account team or partner team to deploy additional instances.
Prepare your environment for onboarding
The onboarding SME should prepare your environment before onboarding a
Google SecOps instance, as described in these sections:
Grant permissions to perform onboarding
.
Set up an Assured Workloads folder (optional)
.
Configure a Google Cloud project
.
Configure an identity provider
.
Grant permissions to perform onboarding
For each new Google SecOps instance, grant the required
   onboarding roles and permissions to the onboarding SME, as described in
Required roles and permissions
.
Set up an Assured Workloads folder (optional)
To create an Assured Workloads folder:
Go to the
Create a new Assured Workloads folder
page.
In the list, select the
control package
* type you want to apply to the
Assured Workloads folder.
Make sure you have the required permissions listed in the
Required IAM
roles
section.
Follow the steps in the
Create an Assured Workloads folder for...
section.
As you set up your folder, consider these guidelines:
A
compliance controlled
tenant (instance) is one that must conform to one or
more of the following compliance control standards:
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
All files associated with a compliance-controlled tenant must reside in an
Assured Workloads folder that is configured for the appropriate
compliance control standard.
An Assured Workloads folder is created at the organization level.
An organization can create multiple Assured Workloads folders, each
dedicated to a specific compliance control package based on its requirements.
For example, one folder may support
FedRAMP_MODERATE
instances, while
another
FedRAMP_HIGH
instances.
Consider these guidelines when you deploy a compliance controlled tenant (instance):
You must link the compliance controlled tenant (instance) to a Google Cloud
project that is located within an Assured Workloads folder.
If you plan to create a new Google Cloud project for your
Google SecOps instance, you must create the project within an
Assured Workloads folder that is configured for the required
compliance control package.
If your organization doesn't have an Assured Workloads folder, you must create one.
Each new Google SecOps instance must be linked to a
Google Cloud project. You can use an existing Google Cloud project or
create a new one.
To create a new Google Cloud project:
For a FedRAMP-compliant tenant (instance), create the project within your
organization's Assured Workloads folder. If your organization
doesn't have an Assured Workloads folder for the required control
package,
create one
.
Follow the steps in
Create a project
.
Configure a Google Cloud project
A Google Cloud project acts as the control layer for the linked
   Google SecOps instance.
To set it up properly, follow the steps in
Configure a Google Cloud project for Google SecOps
.
Configure an identity provider
Configure an identity provider to manage users, groups, and authentication for your Google SecOps instance.
There are two supported options:
Option 1:
Google Cloud Identity
:
Use this option if you have a Google Workspace account, or you sync
 identities from your IdP to Google Cloud.
Create managed user accounts to control access to Google Cloud resources and
your Google SecOps instance.
Define IAM policies using predefined or custom roles to grant
feature access to users and groups.
For detailed instructions, see
Configure a Google Cloud identity provider
.
Option 2:
Workforce Identity Federation
:
Use this option if you use a third-party IdP (such as Okta or Azure AD).
Configure Google's
Workforce Identity Federation
and create a workforce identity pool. Google's
  Workforce Identity Federation lets you grant on-premises or multi-cloud
  workloads access to Google Cloud resources, without using
  service account keys.
For detailed instructions, see
Configure a third-party identity provider
.
Onboard a new Google SecOps instance
The Google system sends a Google SecOps onboarding invitation
email to your onboarding SME. This email includes an activation link to
initiate the setup process.
After preparing your environment for onboarding, the onboarding SME should do
the following:
Click the activation link in the invitation email.
Perform the steps in the following sections to deploy the
Google SecOps instance:
Configure a new Google SecOps instance
and link it to a Google Cloud project.
Configure feature access control using IAM
.
Configure data RBAC for users
.
Map IdP groups to access control parameters
to complete the deployment.
Required roles and permissions
This section lists the roles and permissions required to deploy a Google SecOps instance.
Grant these permissions to the onboarding SME performing the deployment tasks:
All roles and permissions must be granted at the project level
. These
permissions apply only to the specified Google Cloud project and the
associated Google SecOps instance. To deploy additional
instances, contact your account team or partner team.
If you deploy another Google SecOps instance under a different
contract, you must grant a new set of roles and permissions for that
deployment.
Grant the onboarding SME the roles and permissions listed in these following
sections:
Permissions in the Google billing account
Predefined IAM roles
Permissions to create an Assured Workloads folder
Permissions to add a Google Cloud project
Permissions to configure an identity provider
Permissions to configure Cloud Identity or Google Workspace
Permissions to configure a third-party identity provider
Permissions to link a Google SecOps instance to Google Cloud services
Permissions to configure feature access control using IAM
Permissions to configure data access control
Google SecOps advanced capabilities requirements
Permissions in the Google billing account
Grant the onboarding SME the
billing.resourceAssociations.list
permission for
the Google billing account specified in the contract. For detailed steps, see
Update user permissions for a Cloud Billing account
.
Predefined IAM roles
Grant the onboarding SME the following predefined IAM roles:
Chronicle API Admin
Chronicle Service Admin
Chronicle SOAR Admin
Permissions to create an Assured Workloads folder
Grant the onboarding SME the
Assured Workloads Administrator (
roles/assuredworkloads.admin
)
role, which contains the minimum IAM permissions
to create and manage Assured Workloads folders.
Permissions to add a Google Cloud project
Grant the onboarding SME the project creator permissions required to
create a Google Cloud project and enable the Chronicle API:
If the onboarding SME has
project creator
(
resourcemanager.projects.create
)
permissions at the organization level, no additional permissions are required.
If the onboarding SME doesn't have project creator permissions at the
organization level, grant the following project-level IAM roles:
Chronicle Service Admin (
roles/chroniclesm.admin
)
(if this role was not granted earlier)
Editor (
roles/editor
)
Project IAM Admin (
roles/resourcemanager.projectIamAdmin
)
Service Usage Admin (
roles/serviceusage.serviceUsageAdmin
)
Permissions to configure an identity provider
You can use an IdP to manage users, groups, and authentication.
Grant the following permissions to the onboarding SME for configuring an IdP:
Permissions to configure Cloud Identity or Google Workspace
For Cloud Identity:
If you're using Cloud Identity, grant the onboarding SME the roles and
permissions described in
Manage access to projects, folders, and organizations
.
For Google Workspace:
If you're using Google Workspace, the onboarding SME must have a
Cloud Identity administrator account
and be able
to sign in to the
Admin console
.
For more information about using Cloud Identity or Google Workspace as the
  identity provider, see
Configure Google Cloud identity provider
.
Permissions to configure a third-party IdP
If you use a third-party IdP (such as Okta or Azure AD), configure
Workforce Identity Federation
along with a workforce identity pool to enable secure authentication.
Grant the onboarding SME the following IAM roles and permissions:
Editor (
roles/editor
)
:
Project Editor
permissions to the Google SecOps-bound
  project.
IAM Workforce Pool Admin (
roles/iam.workforcePoolAdmin
)
permission at the organization level.
Use the following example to set the
roles/iam.workforcePoolAdmin
role:
gcloud
organizations
add-iam-policy-binding
ORGANIZATION_ID
\
--member
"user:
USER_EMAIL
"
\
--role
roles/iam.workforcePoolAdmin
Replace the following:
ORGANIZATION_ID
: numeric organization ID.
USER_EMAIL
: administrator's email address.
Organization Viewer (
resourcemanager.organizations.get
)
permission at the organization level.
Permissions to link a Google SecOps instance to Google Cloud services
Grant the onboarding SME the same permissions as the
Permissions to add a Google Cloud project
.
If you plan to
migrate an existing Google SecOps instance
, you need permissions to access Google SecOps. For a list of
predefined roles, see
Google SecOps predefined roles in IAM
.
Permissions to configure feature access control using IAM
Grant the
Project IAM Admin (
roles/resourcemanager.projectIamAdmin
)
role at the project level to the onboarding SME. This permission is required
to assign and modify IAM role bindings for the project.
Assign IAM roles to users based on their responsibilities. For examples, see
Assign roles to users and groups
.
If you plan to migrate an existing Google SecOps instance to
IAM, grant the onboarding SME the same permissions as the
Permissions to configure an identity provider
.
Permissions to configure data access control
Grant the onboarding SME the following IAM roles:
Chronicle API Admin (
roles/chronicle.admin
) and Role Viewer (
roles/iam.roleViewer
) roles, for configuring data RBAC for users.
Project IAM Admin (
roles/resourcemanager.projectIamAdmin
) or Security Admin (
roles/iam.securityAdmin
) role, for assigning the scopes to users.
If you don't have the required roles,
assign the roles in IAM
.
Google SecOps advanced capabilities requirements
The following table lists Google SecOps advanced capabilities and their
dependencies on a customer-provided Google Cloud project and Google workforce
identity federation.
Capability
Google Cloud foundation
Requires Google Cloud project?
Requires IAM integration?
Cloud Audit Logs: administrative activities
Cloud Audit Logs
Yes
Yes
Cloud Audit Logs: data access
Cloud Audit Logs
Yes
Yes
Cloud Billing: online subscription or pay-as-you-go
Cloud Billing
Yes
No
Chronicle APIs: general access, mint and manage credentials using third-party IdP
Google Cloud APIs
Yes
Yes
Chronicle APIs: general access, mint and manage credentials using Cloud Identity
Google Cloud APIs, Cloud Identity
Yes
Yes
Compliant controls: CMEK
Cloud Key Management Service or Cloud External Key Manager
Yes
No
Compliant controls: FedRAMP High or above
Assured Workloads
Yes
Yes
Compliant controls: Organization Policy Service
Organization Policy Service
Yes
No
Contact management: legal disclosures
Essential Contacts
Yes
No
Health monitoring: ingestion pipeline outages
Cloud Monitoring
Yes
No
Ingestion: webhook, Pub/Sub, Azure Event Hub, Amazon Kinesis Data Firehose
Identity and Access Management
Yes
No
Role-based access controls: data
Identity and Access Management
Yes
Yes
Role-based access controls: features or resources
Identity and Access Management
Yes
Yes
Support access: case submission, tracking
Cloud Customer Care
Yes
No
Unified SecOps authentication
Google workforce identity federation
No
Yes
Need more help?
Get answers from Community members and Google SecOps professionals.
