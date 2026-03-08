# Configure a Google Cloud identity provider

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-authentication/  
**Scraped:** 2026-03-05T09:14:40.213121Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure a Google Cloud identity provider
Supported in:
Google secops
SIEM
You can use Cloud Identity, Google Workspace, or a third-party identity
provider (such as Okta or Azure AD) to manage users, groups, and authentication.
This page describes how to use Cloud Identity or Google Workspace.
When using Cloud Identity or Google Workspace, you create managed user accounts
to control access to Google Cloud resources and to Google SecOps.
You create IAM policies that define which users and groups have access
to Google SecOps features. These IAM policies
are defined using predefined roles and permissions provided by Google SecOps
or custom roles that you create.
As part of linking a Google SecOps instance to Google Cloud
services, configure a connection to a Google Cloud IdP. The
Google SecOps instance integrates directly with Cloud Identity
or Google Workspace to authenticate users and enforce access control based on
your configured IAM policies.
See
Identities for users
for detailed information about creating Cloud Identity or Google Workspace accounts.
Grant a role to enable sign-in to Google SecOps
The following steps describe how to grant a specific role using IAM
so that a user can sign in to Google SecOps. Perform the configuration using
the Google SecOps-bound Google Cloud project you created earlier.
Grant the
Chronicle API Viewer (
roles/chronicle.viewer
)
role to users or groups that should have access to the Google Security Operations application.
The following example grants the Chronicle API Viewer role to to a specific group:
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--role
roles/chronicle.viewer
\
--member
"group:
GROUP_EMAIL
"
Replace the following:
PROJECT_ID
: with the project ID of the Google Security Operations-bound project
you configured in
Configure a Google Cloud project for Google Security Operations
.
See
Creating and managing projects
for a description of fields that identify a project.
GROUP_EMAIL
: the email alias for the group, such as
analyst-t1@example.com
.
To grant the Chronicle API Viewer role to a specific user, run the following command:
gcloud
projects
add-iam-policy-binding
PROJECT_ID
\
--role
roles/chronicle.viewer
\
--member
"user:
USER_EMAIL
"
Replace
USER_EMAIL
: the user's user email address, such as
alice@example.com
.
For examples of how to grant roles to other members, such as a group or
domain, see
gcloud projects add-iam-policy-binding
and
Principal identifiers
reference
documentation.
Configure additional IAM policies to meet your
 organization's access and security requirements.
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
