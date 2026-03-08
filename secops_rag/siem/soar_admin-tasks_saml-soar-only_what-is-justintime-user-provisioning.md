# Configure just-in-time provisioning

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/what-is-justintime-user-provisioning/  
**Scraped:** 2026-03-05T09:37:22.849363Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure just-in-time provisioning
Supported in:
SOAR
This document explains how to configure just-in-time (JIT) provisioning for Okta users and Azure users.
With JIT enabled, Google Security Operations SOAR automatically creates the user after a successful SAML sign-in from the configured Identity Provider (IdP), such as Okta or Google Workspace.
Define JIT provisioning for Okta users
In Google SecOps SOAR, go to
Settings
>
Advanced
>
External Authentication
.
Select
Okta
and enter the required parameters.
Select the
JIT provisioning
checkbox to display the mapping fields.
In Okta, click
Directory
>
Profile Editor
. Copy the exact field names and enter them into the corresponding fields in Google SecOps SOAR.
Confirm the fields are identical in the Google SecOps SOAR platform and in Okta, and then save.
Define JIT provisioning for Azure users
In Google SecOps SOAR, go to
Settings
>
Advanced
>
External Authentication
.
Select
Azure
and enter the required parameters.
Select the
JIT provisioning
checkbox to display the mapping fields, then use the following standard claim URIs:
First Name Attribute
:
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname
.
Last Name Attribute
:
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname
.
User Name Attribute
:
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name
.
Email Attribute
:
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name
. The Email Attribute can also sometimes be seen as
http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress
.
Need more help?
Get answers from Community members and Google SecOps professionals.
