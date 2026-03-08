# Authenticate users using SSO

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/external-authentication/  
**Scraped:** 2026-03-05T10:10:19.476963Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Authenticate users using SSO
Supported in:
SOAR
This document describes how to configure a SAML provider with one of these use cases:
For Okta,  see
Configure Okta in Google SecOps SOAR
.
For Google Workspace, see
Configure SAML for Google Workspace
.
For Azure, see
Configure SAML for Microsoft Azure
.
After you configure the SAML provider, you can authenticate users in the Google SecOps SOAR platform, as follows:
Go to
SOAR Settings
>
Advanced
>
External Authentication
.
On the
Provider
page, click
add
Add
.
In the
Provider Type
field, select the required SAML provider. For example,
Okta
or
Google Workspace
.
In the
Provider Name
field, enter the name of the instance. For example,
Okta Customer name
.
Set the
Configuration
settings using the following details:
Field
Description
Provider name
Name of the SAML provider.
IdP Metadata
SAML metadata that shares configuration
            information between the Identity Provider (IdP) and the Service
            Provider (SP). If you use a certificate, set
WantAuthnRequestsSigned="true"
in the XML;
            otherwise, set it to
false
.
Identifier
The SP ID in the SAML provider. 
            This term is referred to as
Entity ID
in Google Workspace,
            though service providers can use different names.
ACS URL
Google SecOps SOAR 
            server name. Can be an IP URL, Hostname URL, or Local Host
            URL.
To sign in with SAML, you must do the following:
Connect to the platform with the same
            URL pattern as configured in this field.
Make sure that the URL contains the IP address of the Google SecOps SOAR server,
            followed by
/saml2
.
Unsolicited Response
This setting is also known as an
IdP-Initiated response
. It lets SAML users access the Google SecOps SOAR platform directly from their IdP application. For example, if your company uses Okta, users can enter Google SecOps SOAR  directly through the Okta application.
Auto-redirect
Auto-redirect automatically sends users who aren't signed in to the IdP login page. To force a user to sign in to the platform directly, append
?autoExternalLogin=false
to the URL.

Example:
https://example.com/#/login?autoExternalLogin=false
.
Click
Test
to verify that the configuration works.
Click
Save
.
Select one of the user creation types as needed:
Manual
: Add users, individually, 
in the
User Management
window. For 
details on how to add users, see
Manage users
.
Just in Time
: Automatically create the user (at login) in Google SecOps. When you select this option, an advanced tab opens 
with more parameters. For details, see
Configure just-in-time provisioning
.
IdP Group Mapping
: Create the user automatically in Google SecOps based on the IdP group assignment. When you select this 
option, an advanced tab opens with more parameters. For more information on IdP group mapping, see
Map IdP groups to SOAR roles
.
Need more help?
Get answers from Community members and Google SecOps professionals.
