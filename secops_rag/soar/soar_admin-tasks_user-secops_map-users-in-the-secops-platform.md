# Map users in the Google SecOps platform

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-secops/map-users-in-the-secops-platform/  
**Scraped:** 2026-03-05T09:45:59.594400Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Map users in the Google SecOps platform
Supported in:
Google secops
This document explains how to provision, authenticate, and map users with secure 
identification to the Google Security Operations platform. It outlines the configuration 
process with Google Workspace as the external Identity Provider (IdP), though
the steps are similar for other IdPs.
When you use the Cloud Identity Provider, you should configure the
service with email groups instead of IdP groups. For details, see
Map users in Google SecOps 
platform using Cloud Identity
.
Set up SAML attributes for provisioning
To set up SAML attributes and groups in the external IdP, do the following:
In the Google Workspace, go to the
SAML Attributes
mapping section.
Add the following mandatory attributes:
first_name
last_name
user_email
groups
In
Google Groups
, enter the IdP group names. For example,
Google SecOps administrators
or
Gcp-security-admins
. Note
these group names; you need them later for mapping in the
Google SecOps platform. (In other external providers, such as Okta, 
this is referred to as
IdP Groups
).
Figure 1.
SAML attribute mapping
Set up IdP provisioning
To set up IdP provisioning, follow the steps in
Configure the IdP
and
Create a workforce identity pool provider
.
The following example is the
workforce pool
creation command for the app configuration 
described in
Configure Workforce Identity Federation
:
gcloud
iam
workforce-pools
providers
create-saml
WORKFORCE_PROVIDER_ID
\
--workforce-pool
=
WORKFORCE_POOL_ID
\
--location
=
"global"
\
--display-name
=
WORKFORCE_PROVIDER_DISPLAY_NAME
\
--description
=
WORKFORCE_PROVIDER_DESCRIPTION
\
--idp-metadata-path
=
PATH_TO_METADATA_XML
\
--attribute-mapping
=
"google.subject=assertion.subject,attribute.first_name=assertion.attributes.first_name[0],attribute.last_name=assertion.attributes.last_name[0],attribute.user_email=assertion.attributes.user_email[0],google.groups=assertion.attributes.groups"
Control user access
There are multiple ways to manage user access to different aspects of the platform:
Permissions groups
: Set user access levels by assigning them to 
specific permission groups. These groups determine which modules and submodules 
users can view or edit. For example, a user might have access to
Cases
and
Workdesk
pages, but be restricted from
Playbooks
and
Settings
. 
For more information, see
Work with permission groups
.
SOC roles
: Define the role of a group of users. You can assign users 
to SOC roles to streamline task management. Instead of assigning cases, actions,
 or playbooks to individuals, they can be assigned to a SOC role. Users can see 
 cases assigned to them, their role, or additional roles.
For more information, see
Work with roles
.
Environments or environment groups
: Configure environments or environment 
groups to segment data across different networks or business units, commonly used 
by businesses and Managed Security Service Providers (MSSPs). Users can only access 
data within the environments or groups assigned to them. For more information, see
Work with environments
.
Map and authenticate users
The combination of permission groups, SOC roles, and environments determines the 
Google SecOps user journey for each IdP group in the 
Google SecOps platform.
For customers who use a third-party provider, map each IdP group defined in the 
SAML settings on the
IdP Group Mapping
page.
For customers who use Cloud Identity Provider, map email groups on the
Group Mapping
page. 
For more information, see
Map users in the Google SecOps 
platform using Cloud Identity
.
You can map IdP groups with
multiple permission groups, SOC roles, and environments. This makes sure that different 
users mapped to different IdP groups in the SAML provider inherit all required permission levels. For more information, including how Google SecOps manages this, see
Multiple permissions in IdP group mapping
.
You can also choose to map IdP groups to individual control access parameters. This 
enables a more granular level of mapping and can be helpful for large customers. 
For more information, see
Map IdP groups to access control parameters
.
By default, the Google SecOps platform includes an IdP group of default administrators.
To map IdP groups, follow these steps:
In Google SecOps, go to
Settings
>
SOAR Settings
>
Advanced
>
IdP Group Mapping
.
Make sure you have the names of the IdP groups available.
Click
Add
Add
and start mapping the parameters for each IdP group.
Once you've finished, click
Add
. Each time a user signs in to the platform, 
they are automatically added to the
User Management
page, found under
Settings
>
Organization
.
When users attempt to sign in to the Google SecOps platform, but their IdP group 
hasn't been mapped, for users not to be rejected, we recommend enabling the
Default Access Settings
and setting administrator permissions on this
page. After the initial administrator setup is complete, we suggest adjusting
the administrator permissions to a more minimal level.
Map IdP groups to access control parameters
This section describes how to map different IdP groups to one or more access
control parameters within
the
IdP Group Mapping
page. This approach is beneficial for customers who 
want to onboard and provision user groups based on specific customizations, rather 
than adhering to the standardization of the Google SecOps SOAR platform. 
While mapping groups to parameters may require you to create more groups initially,
once the mapping is set, new users can join Google SecOps without 
the need to create additional groups.
For information about multiple permission in group mapping, 
see
Map users with multiple control access parameters
.
Delete users
If you delete groups from here, make sure to delete the individual users from the
User Management
screen. For more information, see
Delete Google SecOps users
.
Use Case: Assign unique permission fields to each IdP group
The following example illustrates how to use this feature to help onboard and provision 
users according to your company's needs.
Your company has three different personas:
Security analysts (containing group members Sasha and Tal)
SOC engineers (containing group members Quinn and Noam)
NOC engineers (containing group members Kim and Kai)
Security analysts and SOC Engineers have the same Google SecOps 
Permission Groups (Analyst) and SOC Roles (Tier 1), but while the Security Analysts have 
permissions for the London environment, the SOC Engineers have permissions 
for the Manchester environment. Meanwhile, NOC Engineers have permissions for the
London
environment, but are assigned the
Basic
Permission Group and
Tier 2
SOC Role.
This scenario is illustrated in the following table:
Persona
Permission Group
SOC Role
Environment
Security analysts
Analyst
Tier 1
London
SOC engineers
Analyst
Tier 1
Manchester
NOC engineers
Basic
Tier 2
London
For this example, assume that you already set up the necessary permission groups, 
SOC roles, and environments in Google SecOps.
Here is how you would set up the IdP groups in the SAML provider and in the Google SecOps
platform:
In your SAML provider, create the following user groups:
Security analysts (containing Sasha and Tal)
SOC engineers (containing Quinn and Noam)
NOC engineers (containing Kim and Kai)
London (containing Sasha, Tal, Kim and Kai)
Manchester (containing Quinn and Noam)
Go to
Settings
>
SOAR
Settings
>
Advanced
>
IdP Group Mapping
.
Click
Add IdP Group
.
Enter the following details in the dialog:
IdP Group:
Security analysts
Permission Group:
Analyst
SOC Role:
Tier 1
Environment:
leave blank
Enter the following details in the next dialog:
IdP Group:
SOC engineers
Permission Group:
Analyst
SOC Role:
Tier 1
Environment:
leave blank
Enter the following details in the next dialog:
IdP Group:
NOC engineers
Permission Group:
Basic
SOC Role:
Tier 2
Environment:
leave blank
Enter the following details in the next dialog:
IdP Group:
London
Permission Group:
leave blank
SOC Role:
leave blank
Environment:
London
Enter the following details in the next dialog:
IdP Group:
Manchester
Permission Group:
leave blank
SOC Role:
leave blank
Environment:
Manchester
For customers using the Case Federation feature, see
Set up federated case access for Google SecOps
.
Need more help?
Get answers from Community members and Google SecOps professionals.
