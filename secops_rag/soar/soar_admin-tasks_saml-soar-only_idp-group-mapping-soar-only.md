# Map IdP groups to SOAR roles

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/idp-group-mapping-soar-only/  
**Scraped:** 2026-03-05T10:10:32.493417Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Map IdP groups to SOAR roles
Supported in:
SOAR
This document explains how to automatically create users in the Google Security Operations SOAR platform based on their Identity Provider (IdP) group assignments.
Before you begin
Read through and complete the instructions in
Authenticate users using SSO
.
Set up the IdP group mapping
The following procedure assumes you're setting up the
IdP group mapping
in the Google SecOps SOAR-only platform:
Select the
IdP group mapping
option. This opens an advanced tab where you can configure parameters based on the fields in your SAML provider.
First Name Attribute
: Name of the attribute that contains the 
given name (for example,
first name
in Google Workspace).
Last Name Attribute
: Name of the attribute that contains the 
user's family name (for example,
last name
in Google Workspace).
Login ID Attribute
: Name of the attribute that contains the 
user's unique ID (for example,
subject
in Google Workspace).
Email Attribute
: Name of the attribute that contains the user's 
primary address (for example,
primary email
in Google Workspace).
Group Name Attribute
: Name of the attribute that contains the 
groups to which the user belongs within the organization (for example,
groups
in Google Workspace).
After you've defined the attributes, click
add
Add IDP Group
.
Complete the IdP group mapping table. For each IdP group from your SAML provider, you must assign the following:
A SOAR SOC role
A permission group
An environment or environment group (you can assign both at the same time.
For more information about these fields, see
Control access to platform
.
When you're finished mapping the IdP groups, click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
