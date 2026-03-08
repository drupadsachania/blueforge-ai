# Manage playbook permissions

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions/  
**Scraped:** 2026-03-05T10:08:25.249270Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage playbook permissions
Supported in:
Google secops
SOAR
The playbook creator can define, view, and edit permissions for users per
playbook. This means you can restrict access for specific users or SOC
roles to edit certain playbooks.
Examples of Managed Security Service Providers (MSSPs) use cases for playbook permissions include:
Grant end customers (Managed-plus users) permission to build playbooks in their own
environment while collaborating with MSSP engineers.
Grant MSSPs permission to create playbooks without giving edit permissions to their end customers (Managed-plus users).
Examples of Enterprise use cases for playbook permissions include:
Restrict edit access of certain engineers to sensitive playbooks.
Prevent engineers from overriding your work while building a playbook.
Grant permission to uers
To grant permission to users, follow these steps:
On the
Playbooks
page, click
passkey
Permissions
to show the
Playbook access permissions
dialog.
The
Playbook access permissions
dialog has two main sections:
Default Permissions
: This section focuses on all the users who have
access to all the environments that the playbook can run on. In this dialog can choose 
to let users view this playbook or grant them permission to make changes. You have
to have access to all the environments the playbook runs on in order to have
editing rights. However, you only need access to one environment in order to
have viewing rights.
Specific permissions
: This section facilitates more granular flexibility in
drilling down to specific users or SOC roles within specific groups to grant
them either edit and view access. Permissions selected here override the default
permissions that were previously set.
Grant specific permissions
You can configure specific permissions for individual users or for SOC roles. 
SOC roles can be assigned to both users and API keys.
For example, you could tag Tier 3 as
view only
and select Alex Smith (who is
in Tier 3) as having edit permissions.
Need more help?
Get answers from Community members and Google SecOps professionals.
