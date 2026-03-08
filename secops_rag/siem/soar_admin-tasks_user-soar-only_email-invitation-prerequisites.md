# Email invitation prerequisites

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/email-invitation-prerequisites/  
**Scraped:** 2026-03-05T09:37:20.846038Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Email invitation prerequisites
Supported in:
SOAR
This document details how the email invitation system for new internal users is configured in the Google Security Operations SOAR platform. After an administrator creates a new internal user, an email invitation is automatically sent to them. You must choose to configure this system using either the Siemplify SMTP service (default) or a customer-specific SMTP configuration.
Configure a Gmail account
To configure a Gmail account, follow these steps:
Go to
Google Admin Panel
>
Security
>
Settings
.
Select
Allow users to manage their access to less secure apps
.
Click
Save
.
Go to
Gmail Account
>
Security
.
Click the
Less secure app access
toggle to the on position.
Once these settings are applied, an email invitation to the Google SecOps SOAR platform is automatically sent to the user. The user then receives the invitation to join.
Need more help?
Get answers from Community members and Google SecOps professionals.
