# Configure multiple SAML providers

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/configure-multiple-saml-providers/  
**Scraped:** 2026-03-05T10:10:24.700901Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure multiple SAML providers
Supported in:
SOAR
When managing security for diverse clients, a key challenge for Managed Security Service Providers (MSSPs) is accommodating their various authentication methods and Identity Providers (IdPs). By configuring multiple instances for each SAML provider, MSSPs can efficiently handle these unique requirements.
This document explains how this approach can simplify customer onboarding, improve management, and enhance security by ensuring each customer's configurations are isolated.
To configure a few different providers for Okta, follow these steps:
Go to
Settings
>
Advanced
>
External Authentication
.
Click
add
Add
, select the
Provider Type
, and then enter the
Provider name
.
Configure the SAML parameters as required.
Repeat this procedure as many times as needed.
Sign in as a SAML user
Click
Sign in with SAML
.
In the next screen, you're prompted to add your
Login Identifier
(this can be either an email or a username).
Click
Login with External Provider
.
For more information, see
Authenticate users using SSO.
Need more help?
Get answers from Community members and Google SecOps professionals.
