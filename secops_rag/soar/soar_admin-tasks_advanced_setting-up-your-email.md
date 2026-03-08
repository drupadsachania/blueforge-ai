# Set up your email

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/setting-up-your-email/  
**Scraped:** 2026-03-05T09:46:52.078926Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set up your email
Supported in:
Google secops
SOAR
You can set up an email box in Google Security Operations to send emails to users.
When you select the default Google SecOps Simple Mail Transfer Protocol (SMTP) configuration, the
platform's email service sends your emails. You can also select the
Customer Configuration
option to use your own email service to send your emails.
This document explains how to set up your email box using Microsoft Azure.
Before you begin
Sign in to the Microsoft Azure portal.
Go to
Users
>
Active Users
.
Select the Google SecOps user and click
Mail
.
In the
Email apps
section, click
Manage email apps
.
Verify that the
Authenticated SMTP
setting is enabled.
Click
Save changes
.
Set up Microsoft email settings
Go to
Settings
>
Advanced
>
Email Settings
.
Select
Customer Configuration
.
Enter the required information for your organization.
In the
Display name
field, enter the sender's email address.
Select the
Use Exchange OAuth
checkbox. The
Azure Client ID
and
Azure Tenant ID
fields display.
Get Azure IDs and enable permissions
To get the required IDs and enable this feature in Microsoft Azure, follow these steps:
Sign in to the Microsoft Azure portal.
Click
App Registrations
.
Locate the OAuth mail application app you previously created.
Store the
Application Client ID
and
Tenant ID
. You can use the IDs later in the Google SecOps platform.
Go to
Manage
>
Advanced Settings
and set
Allow public client flows
to
Yes
.
In the
API Permission
tab, grant the following permissions:
IMAP.AccessAsUser.All
SMTP.Send
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
