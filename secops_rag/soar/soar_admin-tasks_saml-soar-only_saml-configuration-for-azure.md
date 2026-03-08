# Configure SAML for Microsoft Azure

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-azure/  
**Scraped:** 2026-03-05T10:10:22.029389Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure SAML for Microsoft Azure
Supported in:
SOAR
This document explains how to configure SAML for Microsoft Azure to use with the standalone Google Security Operations SOAR platform.
Before you begin
Confirm that you've set up a SAML account in Microsoft Azure by completing the instructions in the following Quickstart guides:
Create and assign a user account
Add an enterprise application
View enterprise applications
Configure SAML in Microsoft Azure
To configure SAML in Microsoft Azure, follow these steps:
Sign in to the Azure portal.
Go to
Enterprise Applications
.
Locate your company's SAML sign-on app.
In the sidebar, select
Single Sign-on
.
Basic SAML Configuration
, configure the
    following fields and save your changes:
Identifier (Entity ID)
:
https://platform_Address/Saml2/
Reply URL (Assertion Consumer Service URL)
:
https://platform_Address/Saml2/ACS
Sign on URL
:
https://platform_Address/Saml2/
Configure Azure in Google SecOps SOAR
Go to
Settings
>
Advanced
>
External
    Authentication
.
Create a new SAML provider.
In the
Provider Type
menu, select
Custom SAML Provider
.
Enter a provider name. For example,
mycompany_Azure
.
Complete the following fields using information from the Azure portal:
IdP Metadata
Return to the Azure portal.
In
SAML Certificates
, go to the
Federation Metadata XML
field.
Click
Download
and save the Federation Metadata XML file.
Return to the Google SecOps SOAR platform.
In the
IdP Metadata
field, upload the Federation Metadata XML file to the
IdP Metadata
field.
Identifier
Return to the Azure portal.
Go to
Set up \
and click the
Microsoft Entra Identifier
field.
Copy the data from the
Microsoft Entra Identifier
field.
Return to the Google SecOps SOAR platform.
Paste the value into the
Identifier
field.
ACS URL
Return to the Azure portal.
Go to
Basic SAML Configuration
>
the
Sign On URL
field.
Copy the data from the Azure
Sign On URL
field.
Return to the Google SecOps SOAR platform.
Paste the value into the
ACS URL
field.
Field mapping
Google SecOps SOAR field
Microsoft Azure field
IdP Metadata
Federation Metadata XML
Identifier
Microsoft Entra Identifier
ACS URL
Sign on URL
For more information, see
Authenticate users using SSO.
Need more help?
Get answers from Community members and Google SecOps professionals.
