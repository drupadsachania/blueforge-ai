# Configure Okta in Google SecOps SOAR

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-okta/  
**Scraped:** 2026-03-05T09:37:15.302026Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure Okta in Google SecOps SOAR
Supported in:
SOAR
This document explains how to configure Okta for authentication and how to configure the Google Security Operations SOAR platform to support this.
Before you begin
To configure Okta in the Google SecOps SOAR platform, you must set up the SAML account in Okta. For details, see
Create an app for SAML in Okta
.
Once you set up the SAML account in Okta, you can configure the Okta settings in the Google SecOps SOAR platform:
In the Google SecOps SOAR platform, go to
Settings
>
Advanced
>
External
    Authentication
.
Click
Create a new SAML provider
.
In the
Provider Type
menu, select
Okta
.
Enter a provider name, such as
mycompany_Okta
, and click
Create
.
Open the Okta portal and go to
Applications
>
Applications
.
Select the SAML app you created.
Click the
General
tab and go to
SAML Settings
.
Copy the string in the
Audience Restriction
field.
Return to the Google SecOps SOAR platform, and paste the string 
    into the
ACS URL
field.
Return to the Okta portal and in the SAML app, click the
Sign On
tab and locate and click
View SAML setup instructions
.
Copy the string into the
Identity Provider Issuer
field.
Return to the Google SecOps platform, and paste this string into the
Identifier
field.
Return to the Okta portal. In
View SAML setup instructions
, go to the
Optional
heading and copy the 
    Identity Provider (IdP) metadata into a text file. Save this file as
metadata.xml
.
Return to the Google SecOps SOAR platform. Next to the
IdP Metadata
field, click
upload
Upload
.
Click
Save
>
Test
to make sure the configuration is correct.
For more information, see
Authenticate users using SSO.
Need more help?
Get answers from Community members and Google SecOps professionals.
