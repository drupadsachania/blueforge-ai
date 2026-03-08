# Configure a third-party identity provider

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/configure-authentication/  
**Scraped:** 2026-03-05T09:45:30.434726Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure a third-party identity provider
Supported in:
Google secops
SIEM
You can use Cloud Identity, Google Workspace, or a third-party identity
provider (such as Okta or Azure AD) to manage users, groups, and authentication.
This page describes how to use a third-party identity provider by configuring
Workforce Identity Federation.
Google's Workforce Identity Federation lets you
grant on-premises or multi cloud workloads access to Google Cloud
resources, without having to use a service account key.
You can use Workforce Identity Federation with any IdP that supports
SAML 2.0
, such as Microsoft Entra ID, Active Directory Federation Services (AD FS), Okta, and others.
Google Security Operations requires using Google's workforce identity federation as the
SSO broker for the following:
Customers with FedRAMP High (or higher) compliance requirements.
Customers accessing any enterprise-level controls in Google Security Operations that are enabled by Google Cloud,
including data and feature role-based access control (RBAC) using Identity and Access Management (IAM).
Customers using self-service credential management for programmatic access of the Chronicle API.
Google Security Operations supports Service Provider Initiated (SP-initiated) SAML SSO for
users. With this capability, users navigate directly to Google Security Operations.
Google Security Operations issues a request through Google Cloud Identity and Access Management (IAM)
workforce identity federation
to the third-party identity provider (IdP).
After the IdP authenticates the user identity, the user is returned to
Google Security Operations with an authentication assertion. Google Cloud workforce identity
federation acts as an intermediary in the authentication flow.
Communication between Google Security Operations, IAM workforce identity
    federation, and IdP
At a high level, the communication is as follows:
The user navigates to Google Security Operations.
Google Security Operations looks up IdP information in the Google Cloud workforce identity pool.
A request is sent to the IdP.
The SAML assertion is sent to the Google Cloud workforce identity pool.
If authentication is successful, Google Security Operations receives only the SAML
attributes defined when you configured the workforce provider in the workforce identity pool.
Google Security Operations administrators create groups in their identity provider, configure
the SAML application to pass group membership information in the assertion, and then
associate users and groups to Google Security Operations
predefined roles in IAM
or to custom roles that they created.
IdP initiated login (initiating a login from your IdP dashboard) is not supported.
Contact your Google Security Operations representative to request this feature if your organization needs the capability.
This document describes high-level steps to set up authentication through a
third-party identity provider (IdP) using Google Cloud workforce identity federation.
After performing the steps in this document, you will be able to access Google Security Operations using your third-party IdP
and manage access to the Google Security Operations using SAML SSO using workforce identity federation.
Before you begin
Make sure you are familiar with
Cloud Shell
,
the
gcloud
command
, and the Google Cloud console.
Perform the steps in
Configure a Google Cloud project for Google Security Operations
to set up a project that binds to Google Security Operations.
Familiarize yourself with Google Cloud
workforce identity federation
.
Make sure you have the permissions to perform the steps in this document.
For information about required permissions for each phase of the onboarding process,
see
Required roles
.
The following steps describe how to perform the configuration using
gcloud
commands. If a step can be performed in the Google Cloud console, a link to the related IAM documentation is provided.
Plan the implementation
The following section describes the decisions you must make and information you
define before performing the steps in this document.
Define the workforce identity pool and workforce provider
As part of this process, you will configure Google Cloud workforce identity
federation as an intermediary in the authentication flow. To accomplish this, you
create the following Google Cloud resources:
Workforce pool
:
A workforce identity pool lets you grant your workforce (e.g. employees) access to Google Security Operations.
Workforce provider
:
A workforce provider is a sub-resource of the workforce identity pool. It stores details about a single IdP.
The relationship between workforce identity pool, workforce providers, and a Google Security Operations
instance, identified by a single customer subdomain, is as follows:
A workforce identity pool is defined at the organization-level.
Each Google Security Operations instance has a workforce identity pool configured and associated with it.
A workforce identity pool can have multiple workforce providers.
Each workforce provider integrates a third-party IdP with the workforce identity pool.
The workforce identity pool you create using these steps must be dedicated to Google SecOps.
Although you may manage multiple workforce identity pools for other purposes,
the workforce identity pool created for Google SecOps cannot be shared.
We recommend that you create the workforce identity pool in the same Google Cloud
organization that contains the project bound to Google SecOps.
It helps save time if you predefine information about the
workforce identity pool and workforce provider. You use this information when configuring
both the IdP SAML application and workforce identity federation.
Choose the values for the following identifiers:
Workforce pool ID (
WORKFORCE_POOL_ID
): select a value that indicates
  the scope or purpose of the workforce identity pool. The value must meet
  the following requirements:
Must be globally unique.
Must use only lowercase characters [a-z], digit [0-9], and dashes [-].
Must begin with a lowercase character [a-z].
Must end with either a lowercase character [a-z] or digit [0-9].
Can be between 4 to 61 characters in length.
Workforce pool display name (
WORKFORCE_POOL_DISPLAY_NAME
): define a user-friendly name.
for the workforce identity pool.
Workforce pool description (
WORKFORCE_POOL_DESCRIPTION
): define a detailed
description of the workforce identity pool.
Workforce provider ID (
WORKFORCE_PROVIDER_ID
): choose a value that indicates
the IdP it represents. The value must meet the following requirements::
Must use only lowercase characters [a-z], digit [0-9], and dash [-].
Can be between 4 to 32 characters in length.
Workforce provider display name (
WORKFORCE_PROVIDER_DISPLAY_NAME
): define a
user-friendly name for the workforce provider. It must be less than 32 characters long.
Workforce provider description (
WORKFORCE_PROVIDER_DESCRIPTION
): define a detailed
description of the workforce provider.
Define user attributes and groups in the IdP
Before you create the SAML application in the IdP, identify which user attributes
and groups are needed to configure access to features in Google Security Operations.
For more information, see
Configure feature access control using IAM
and
Google Security Operations permissions in IAM
.
You need this information during the following phases of this process:
When configuring the SAML application, you create the groups defined during planning.
You configure the IdP SAML application to pass group memberships in the
assertion.
When you create the workforce provider, you map assertion attributes and groups to
Google Cloud attributes
.
This information is sent in the assertion claim as part of a user's identity.
When setting up role-based access control in Google Security Operations, you use the
user attributes and group information to configure access to Google Security Operations features.
Google Security Operations provides multiple predefined roles that each allow access to
specific features. You can map groups defined in the IdP SAML application to
these predefined roles.
Create an IdP group for administrators who configure SOAR-related feature
access. Specify this group name during the onboarding process to authorize
group members to
configure user and group access
to SOAR-related features in Google SecOps.
Configure the IdP
This section describes only the specific configuration needed in an IdP SAML application to
integrate with Google Cloud workforce identity federation and Google Security Operations.
Create a new SAML application in your IdP.
Configure the application with the following Assertion Consumer Service (ACS) URL, which is also referred to as a single sign-on URL depending on the service provider.
https://auth.backstory.chronicle.security/signin-callback/locations/global/workforcePools/
WORKFORCE_POOL_ID
/providers/
WORKFORCE_PROVIDER_ID
Replace the following:
WORKFORCE_POOL_ID
: the identifier you defined
for the workforce identity pool.
WORKFORCE_PROVIDER_ID
: the identifier you
defined for the workforce provider.
For value descriptions, see
Plan the implementation
.
Configure the application with the following Entity ID (also called, SP Entity ID).
https://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/providers/
WORKFORCE_PROVIDER_ID
Replace the following:
WORKFORCE_POOL_ID
: the identifier you defined for the workforce identity pool.
WORKFORCE_PROVIDER_ID
: the identifier you defined for the workforce provider.
Configure the name identifier in your IdP to ensure that the
NameID
field is
returned in the SAML response.
You can set this to a value that supports your organization policies, such as email address or username. Consult your IdP documentation for information about configuring this value. For more information about this requirement, see
Troubleshoot workforce identity federation
.
Optionally, create the group attributes in the SAML application.
You defined these when you
planned the IdP implementation
.
Download the application metadata XML file. In the next section, you will
upload this file from your local system to your Google Cloud home directory
using
Cloud Shell
.
Configure workforce identity federation
This section describes only the specific steps needed to configure workforce
identity federation with the IdP SAML application that you created in the previous section.
For more information about managing workforce identity pools,
see
Manage workforce identity pool providers
Open the Google Cloud console as the user with the required permissions on the
Google Security Operations-bound project. You identified or created this user earlier.
See the
Before you begin
section.
Launch a
Cloud Shell   session
.
Set the Google Cloud project that is billed and charged quota for
operations performed using the gcloud CLI. Use the following
gcloud
command as an example:
gcloud
config
set
billing/quota_project
PROJECT_ID
Replace
PROJECT_ID
with the project ID of the
Google Security Operations-bound project you created in
Configure a Google Cloud project for Google Security Operations
. For a
description of fields that identify a project, see
Creating and managing projects
.
For information about quotas, see the following documents:
The
Cloud Quotas overview
Set the quota project
If you encounter an error, see
Troubleshoot quota errors
.
Create and configure a workforce identity pool
You can configure a workforce identity pool to integrate with an external
identity provider (IdP) or with Google Workspace or Cloud Identity.
Create a workforce identity pool.
Create a workforce identity pool for a third-party IdP:
Use the following
gcloud
command as an example:
gcloud
iam
workforce-pools
create
WORKFORCE_POOL_ID
\
--location
=
"global"
\
--organization
=
"
ORGANIZATION_ID
"
\
--description
=
"
WORKFORCE_POOL_DESCRIPTION
"
\
--display-name
=
"
WORKFORCE_POOL_DISPLAY_NAME
"
Replace the following:
WORKFORCE_POOL_ID
: the identifier you defined
for the workforce identity pool.
ORGANIZATION_ID
: the numeric organization ID.
WORKFORCE_POOL_DESCRIPTION
: specify a description
of the workforce identity pool.
WORKFORCE_POOL_DISPLAY_NAME
: specify a
user-friendly name for the workforce identity pool.
To perform this configuration using the Google Cloud console,
see
Create a pool
.
If you want to use Google Workspace or Cloud Identity to sign in to
Google SecOps, add these flags:
--allowed-services domain=backstory.chronicle.security
and
--disable-programmatic-signin
to the command:
gcloud
iam
workforce-pools
create
WORKFORCE_POOL_ID
\
--location
=
"global"
\
--organization
=
"
ORGANIZATION_ID
"
\
--description
=
"
WORKFORCE_POOL_DESCRIPTION
"
\
--display-name
=
"
WORKFORCE_POOL_DISPLAY_NAME
"
\
--allowed-services
domain
=
backstory.chronicle.security
\
--disable-programmatic-signin
This command creates a workforce identity pool that does not support
signing in to Google Cloud. To enable sign-in functionality, you need to
use the appropriate flags for each scenario.
If you are prompted at the command line to enable the Chronicle API, type
Yes
.
Create a workforce identity pool provider
A workforce identity pool provider is an entity that describes a relationship
between your Google Cloud organization and your IdP.
Upload the SAML application metadata file to your Cloud Shell home directory by clicking
more_vert
More
>
. Files can only
be uploaded to your home directory. For more options to transfer files
between Cloud Shell and your local workstation, see
Upload and download files and folders from Cloud Shell
.
Make a note of the directory path where you uploaded the SAML application metadata XML file
in Cloud Shell. You will need this path in the next step.
Create a workforce identity pool provider and specify the IdP details.
Use the following
gcloud
command as an example:
gcloud
iam
workforce-pools
providers
create-saml
WORKFORCE_PROVIDER_ID
\
--workforce-pool
=
"
WORKFORCE_POOL_ID
"
\
--location
=
"global"
\
--display-name
=
"
WORKFORCE_PROVIDER_DISPLAY_NAME
"
\
--description
=
"
WORKFORCE_PROVIDER_DESCRIPTION
"
\
--idp-metadata-path
=
PATH_TO_METADATA_XML
\
--attribute-mapping
=
"
ATTRIBUTE_MAPPINGS
"
For value descriptions, see
Plan the implementation
.
Replace the following:
WORKFORCE_PROVIDER_ID
: the value you defined for the workforce provider ID.
WORKFORCE_POOL_ID
: the value you defined for the workforce identity pool ID.
WORKFORCE_PROVIDER_DISPLAY_NAME
: a user-friendly name
for the workforce provider. It must be less than 32 characters long.
WORKFORCE_PROVIDER_DESCRIPTION
: a description of the workforce provider.
PATH_TO_METADATA_XML
: the Cloud Shell directory location of the application metadata XML file
 that you uploaded using Cloud Shell, for example:
/path/to/sso_metadata.xml
.
ATTRIBUTE_MAPPINGS
: definition of how to map assertion attributes to
Google Cloud attributes
.
Common Expression Language
is used to interpret these mapping. For example:
google.subject=assertion.subject,google.display_name=assertion.attributes.name[0],google.groups=assertion.attributes.groups
The previous example maps the following attributes:
assertion.subject
to
google.subject
. This is a minimum requirement.
assertion.attributes.name[0]
to
google.display_name
.
assertion.attributes.groups
to the
google.groups
attribute.
If you are performing this configuration for Google Security Operations, which includes
Google Security Operations SIEM and Google SecOps SOAR, you must also map the following
attributes required by Google SecOps SOAR:
attribute.first_name
attribute.last_name
attribute.user_email
google.groups
For more information, see
Provisioning and mapping users for Google SecOps SOAR
.
By default, Google Security Operations reads group information from the following
case-insensitive assertion attribute names:
_assertion.attributes.groups_
,
_assertion.attributes.idpGroup_
, and
_assertion.attributes.memberOf_
.
When configuring the SAML application to pass group membership information
in the assertion, set the group attribute name to either
_group_
,
_idpGroup_
, or
_memberOf_
.
In the example command, you can replace
assertion.attributes.groups
with
either
assertion.attributes.idpGroup
or
assertion.attributes.memberOf
,
which represents the name of the group attribute you configured in the IdP
SAML application and that contains group membership information in the assertion.
The following example maps multiple groups to the
google.groups
attribute:
google.groups="(has(assertion.attributes.idpGroup) ? assertion.attributes.idpGroup : []) + (has(assertion.attributes.groups) ? assertion.attributes.groups : []) + (has(assertion.attributes.memberof) ? assertion.attributes.memberof : [])"
The following example maps the group
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/group
containing special characters to
google.groups
:
google.groups="assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/claims/group']"
For more information about mapping attributes, see
Attribute Mappings
.
To perform this configuration using Google Cloud console, see
Create a SAML provider
.
Grant a role to enable sign in to Google Security Operations
The following steps describe how to grant a specific role using IAM
so that users can sign in to Google Security Operations. Perform the configuration using
the Google Security Operations-bound Google Cloud project you created earlier.
Grant the
Chronicle API Viewer (
roles/chronicle.viewer
)
role to users or groups that should have access to the Google Security Operations application.
The following example grants the Chronicle API Viewer role to identities managed
using the workforce identity pool and workforce provider you created previously.
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--role
roles/chronicle.viewer
\
--member
"principalSet://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/*"
Replace the following:
PROJECT_ID
: with the project ID of the Google Security Operations-bound project
you configured in
Configure a Google Cloud project for Google Security Operations
.
For a description of fields that identify a project, see
Creating and managing projects
.
WORKFORCE_POOL_ID
: the value you defined for the workforce identity pool ID.
To grant the Chronicle API Viewer role to a specific group, run the following command:
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--role
roles/chronicle.viewer
\
--member
"principalSet://iam.googleapis.com/locations/global/workforcePools/
WORKFORCE_POOL_ID
/group/
GROUP_ID
"
Replace
GROUP_ID
: a group in the mapped
google.groups
claim.
Configure additional IAM policies to meet your organization's requirements.
Required: To complete authentication and enable user access to the
 Google SecOps platform, you need to configure user access
 from the SOAR side of the Google SecOps. For more information, see
Map users in the Google SecOps platform
.
Verify or configure Google Security Operations feature access control
If you configured workforce identity federation with attributes or groups mapped
to the
google.groups
attribute, this information is passed to Google Security Operations
so that you can configure role-based access control (RBAC) to Google Security Operations features.
If the Google Security Operations instance has an existing RBAC configuration, verify
that the original configuration works as expected.
If you have not previously configured access control, see
Configure feature access control using IAM
for information about controlling access to features.
Modify the workforce identity federation configuration
If you need to update the workforce identity pool or workforce provider,
see
Manage workforce identity pool providers
for information about updating the configuration.
The
Key management
section in
Create a SAML workforce pool provider
describes how to update IdP signing keys, and then update the workforce provider
configuration with the latest application metadata XML file.
The following is an example
gcloud
command that updates the workforce provider configuration:
gcloud
iam
workforce-pools
providers
update-saml
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
"
WORKFORCE_PROVIDER_DISPLAY_NAME
"
\
--description
=
"
WORKFORCE_PROVIDER_DESCRIPTION
"
\
--idp-metadata-path
=
PATH_TO_METADATA_XML
\
--attribute-mapping
=
"
ATTRIBUTE_MAPPINGS
"
Replace the following:
WORKFORCE_PROVIDER_ID
: the value you defined for the workforce provider ID.
WORKFORCE_POOL_ID
: the value you defined for the workforce identity pool ID.
WORKFORCE_PROVIDER_DISPLAY_NAME
: a user-friendly name
for the workforce provider. The value must be less than 32 characters.
WORKFORCE_PROVIDER_DESCRIPTION
: the description of the workforce provider.
PATH_TO_METADATA_XML
: the location of the updated application metadata XML file,
for example:
/path/to/sso_metadata_updated.xml
.
ATTRIBUTE_MAPPINGS
: the mapped assertion attributes to
Google Cloud attributes
. For example:
google.subject=assertion.subject,google.display_name=assertion.attributes.name[0],google.groups=assertion.attributes.memberOf
To ensure that Google SecOps RBAC continues to function as expected, also map the
google.groups
attribute to all groups used to define roles in Google SecOps.
Troubleshoot issues with configuration
If you encounter errors during this process, review
Troubleshoot workforce identity federation
to resolve common issues. The following section provides information about common
problems encountered when performing the steps in this document.
If you still encounter issues, contact your Google SecOps representative
and provide your
Chrome Network Logs File
.
Command not found
When
creating a workforce identity pool provider
and specifying the IdP details,
you get the following error:
Error: bash: --attribute-mapping=google.subject=assertion.subject,
google.display_name=assertion.attributes.name[0],
google.groups=assertion.attributes.groups: command not found
Check that the
PATH_TO_METADATA_XML
is the location where you uploaded the
SAML application metadata XML file to your Cloud Shell home directory.
The caller does not have permission
When running the command
gcloud projects add-iam-policy-binding
to grant roles to users or groups, you get the following error:
ERROR: (gcloud.organizations.add-iam-policy-binding) User [ ] does not have
permission to access organizations instance [538073083963:getIamPolicy]
(or it may not exist): The caller does not have permission
Check that you have the required permissions. For more information, see
Required roles
.
Verification failure: missing session ID in the request
When attempting to authenticate, you get the following error in the browser:
Verification failure: missing session ID in request
Check that the ACS and Entity ID base URLs are correct. For more information, see
Configure the IdP
.
What's next
After completing the steps in this document, perform the following:
Perform steps to
Link a Google Security Operations instance to Google Cloud services
.
If you have not yet set up audit logging, continue with
enabling Google Security Operations audit logging
.
If you are configuring for Google Security Operations, perform additional steps in
Provision, authenticate, and map users in Google Security Operations
.
To configure access to features, perform additional steps in
Configure feature access control using IAM
and
Google Security Operations permissions in IAM
.
Need more help?
Get answers from Community members and Google SecOps professionals.
