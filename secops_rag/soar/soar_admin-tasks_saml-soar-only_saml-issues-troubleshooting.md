# Troubleshoot SAML issues in Google SecOps SOAR

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-issues-troubleshooting/  
**Scraped:** 2026-03-05T10:10:26.238176Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Troubleshoot SAML issues in Google SecOps SOAR
Supported in:
SOAR
This document explains how to troubleshoot common issues you may encounter with SAML authentication in your Google Security Operations SOAR platform.
Application not found in directory
Message
:
AADSTS700016: Application with identifier 'https://yyy.yyyyyy.com/api/auth/saml/metadata' was not found in the directory 'yyy'.
Explanation
: There's a mismatch between the configuration in Azure AD (Basic SAML) and the system.
Fix
: In Azure AD, set
Identifier (Entity ID)
to the SP's Entity ID and ensure the
Reply URL (ACS)
matches your SP; confirm you're in the correct tenant and that users are assigned to the app.
Invalid value for saml:AuthnContextDeclRef
Message
:
Microsoft.IdentityModel.Tokens.Saml2.Saml2SecurityTokenReadException: IDX13102: Exception thrown while reading 'System.String' for Saml2SecurityToken. Inner exception: System.ArgumentException.
Explanation
: This error indicates an invalid value for
saml:AuthnContextDeclRef
in the SAML response.
Fix
: Decode and inspect the SAML Response. If the IdP sends an invalid
AuthnContextDeclRef
, remove it or switch to a supported
saml:AuthnContextClassRef
(for example,
urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport
).
System.ArgumentException: 'System.String' must be an absolute URI
Message
:
/ds:Signature>saml:Subject<saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified" System.ArgumentException: IDX13300: 'System.String' must be an absolute URI, was: 'System.Uri"></saml:NameID>
Explanation
: The
NameID
Format
must be a valid absolute URI (URN) supported by the SP, and the
<saml:NameID>
value must be present.
Fix
: Set the
DefaultNameIDFormat
parameter in your SAML configuration to one of the following options:
urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
(
most common
)
urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
urn:oasis:names:tc:SAML:2.0:nameid-format:transient
User attributes not found and
LoginIdentifier
field is required
Message
:
logs Server error Login error for user _yyyyyyyyyyyyyyyyyyyyyyy. User attributes were not found for creating new followed by Error: register : The LoginIdentifier field is required.
Explanation
: With Just-In-Time (JIT) provisioning enabled, the SP looks up the user using the
NameID
(or a mapped attribute). The incoming value doesn't match any existing login IDs.
Fix
: The IdP must be configured to send a value that matches the
Login ID
field in user management (Settings
>
User Management). This value might be the user's email address or another unique ID.
User type mismatch
Message
:
Login error for user user@user.com. User type (Internal) does not match to this type of authentication (External).
Explanation
: An account with the same Login ID exists as
Internal
, but SAML authentication requires an
External
user.
Fix
: Change the user type of the existing user with the conflicting username to
External
to match the SAML authentication method.
Redirect loop
If your instance is configured for automatic redirection to the IdP login page, and you encounter a continuous redirect loop, you can temporarily disable auto-redirection by appending the following text to your instance hostname:
/#/login?autoExternalLogin=false
Need more help?
Get answers from Community members and Google SecOps professionals.
