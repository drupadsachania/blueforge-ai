# Configure SAML for Google Workspace

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-configuration-for-g-suite/  
**Scraped:** 2026-03-05T10:10:20.457621Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure SAML for Google Workspace
Supported in:
SOAR
This document explains how to configure Google Workspace for authentication and how to connect it to the Google SecOps SOAR platform.
Configure Google Workspace for SSO
Go to the
Google Admin Portal
.
Select
Apps
>
Web and mobile apps
.
In the
Add App
menu, select
Add custom SAML app
.
Enter a name in
New Name of App
, upload an app icon, and then click
Continue
.
On the
Google IdP Information
page, click
Next
.
On the
Service Provider Details
page, enter the following information, and then click
Next
:
ACS URL
:
https://{your_siemplify_server_IP_address}/Saml2/Acs
Entity ID
:
https://{your_siemplify_server_IP_address}/Saml2
In the
Attribute Mapping
screen, click
Add New Mapping
.
Set the
Primary email
to
email
.
Make sure that the
Service Status
is on.
Configure Google Workspace in Google SecOps SOAR
Go to
Settings
>
Advanced
>
External Authentication
.
Create a new custom SAML provider.
In the
Provider Type
menu, select
G Suite
.
In the
Provider Name
field, enter a name (for example,
mycompany_workspace
).
Complete the following fields. When you're finished, click
Save
:
IdP Metadata
Return to the Google Workspace app that you created, select
Download Metadata
from the menu, and 
save the XML file.
In the Google SecOps SOAR platform, click the
IdP Metadata
field, and then
Upload
to upload the saved file.
Identifier
Return to the Google Workspace app, expand
Service provider details
, and 
click
Manage Certificates
.
Under
Google Identity Provider Details
, locate the
Entity ID
and copy and paste its contents into the Google SecOps SOAR
Identifier
field.
In the Google SecOps SOAR platform, paste the contents into the
Identifier
field.
ACS URL
Return to the Google Workspace app, expand
Service Provider details
,
and copy the contents of the
ACS URL
field.
In the Google SecOps SOAR platform, paste the contents into the
ACS URL
field, making sure to remove the trailing
"/Acs"
at the end.
For more information, see
Authenticate users using SSO
.
Need more help?
Get answers from Community members and Google SecOps professionals.
