# Pre-migration validation guide

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation/  
**Scraped:** 2026-03-05T09:46:58.977920Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Pre-migration validation guide
Supported in:
Google secops
SOAR
This document outlines a systematic, step-by-step diagnostic approach for
validating the Google Security Operations instance and authentication setup before SOAR migration.
This guide focuses on the SAML standard that is used for user authentication and
authorization.
Chronicle API setup validation
To check if Chronicle API is correctly configured in your Google Cloud project,
follow these steps:
Sign in to the
Google Cloud console
and select the correct Google Cloud project from the
project
list in the 
top navigation bar.
Open the
navigation menu
(≡) and go to
APIs & Services
>
Enabled APIs & services
.
Go to the list of
Enabled APIs & Services
to find
Chronicle API
.
If it is listed:
The API is enabled.
If it is NOT listed:
Click
+ ENABLE APIS AND SERVICES
at the top, search for
Chronicle API
, and
click
Enable
.
To verify whether the Service Account is created, do the following:
Go to the
IAM Page
in the Google Cloud console.
Reveal hidden accounts
(crucial step): You must select the box on the
right side of the filter bar that says
Include Google-provided role grants
.
Search for the agent:
In the filter bar, type
chronicle
. You're
looking for an email address that matches this specific pattern:
service-[PROJECT_NUMBER]@gcp-sa-chronicle.iam.gserviceaccount.com
Verify permissions:
Ensure it has the role of
Chronicle Service Agent
.
If the role is missing, click
edit
Edit
and add it back.
Authentication workflow architecture
Understanding the request flow is critical for isolating any failure points. The following diagram illustrates the sequential path of a successful login.
Step-by-step troubleshooting procedure
To diagnose and trace the SAML authentication process effectively, you can use
the web-based utilities listed in the following sections.
Although Google does not endorse any
particular product, the following tools are known to aid in troubleshooting the process:
SAML validation:
https://www.samltool.io/
Purpose:
Used to decode and validate raw SAML requests and responses.
JWT inspection:
https://www.jwt.io/
Purpose:
Used to inspect the claims and contents of JSON Web Tokens
(JWTs).
Phase 1: Environment preparation
Before beginning, do the following to ensure that your browser environment is ready to capture network
traffic:
Open a new, blank browser tab.
Open
Developer Tools
(press
F12
or
Ctrl + Shift + I
(Windows /Linux) or
Cmd + Option + I
(macOS)) and navigate to the
Network
tab.
Select the
Preserve log
box to ensure no data is lost during
redirects.
Navigate to your Google SecOps environment URL to initiate the login flow. You will
receive this URL through email after you complete Google SecOps
setup in
Step 5 of Migration stage 1 for SOAR standalone customers
.
The Subject of the email is
YourGoogle SecOps instance is ready
.
Phase 2: Validate the SAML request to IDP
This step verifies the initial message sent by Google Cloud to your Identity Provider (IDP).
Locate the request:
In the
Network
tab filter bar, search for
saml
.
Extract data:
Select the request and click the
Payload
tab. Locate
the query string parameter labeled
SAMLRequest
.
Decode:
Copy the request value and paste it into the
SAML Validation
tool (
samltool.io
) to decode it.
Verification:
Check the
Request Destination
.
Confirm this URL matches the configuration settings within your IDP.
Phase 3: Validate the SAML response from IDP
This step verifies the attributes returned by the IDP to Google Cloud after authentication.
Locate the response:
In the
Network
tab filter bar, search for
signin-callback
.
Extract data:
Select the request and click the
Payload
tab. Locate
the
SAMLResponse
data.
Decode:
Copy the response value and paste it into the
SAML Validation
tool.
Verification:
Review the returned claims (attributes) such as
groups
,
first name
,
last name
, and
email
.
Critical:
Ensure these attributes match the configuration in the
Workforce pool
settings in Google Cloud.
Confirm the values are correct for the specific user attempting to log in.
The following image shows an attribute mapping:
The mapping in the image is as follows:
google.subject  = assertion.subject
attribute.last_name = assertion.attributes.last_name[0]
attribute.user_email = assertion.attributes.user_email[0]
attribute.first_name = assertion.attributes.first_name[0]
google.groups = assertion.attributes.groups
The left part is always the same; it's the Google syntax. The right side is according to the claim Attribute keys shown in the SAML response.
The
[0]
is critical for the specific attributes stated (
last_name
,
user_email
,
first_name
), and not relevant for
subject
and
groups
.
Phase 4: Validate the Google SecOps authentication
This step verifies whether Google Cloud is authenticating the user to log in to Google SecOps SOAR.
Locate the token in the user's browser:
In the
Network
tab filter 
bar, search for the endpoint
auth/siem
.
Extract data:
Select the request and view the
Payload
tab. Locate
the
jwt
string.
Decode:
Copy the JWT string and paste it into the
JWT Inspection
tool (
jwt.io
).
Verification:
Compare the decoded claims for
given_name
,
family_name
,
email
, and
idpgroups
.
Match confirmation:
These values must
exactly match
the
attributes validated in Phase 3 (SAML Response).
If the values match and you still don't have access, then check the
roles assignment in IAM. Make sure all of your users are
assigned
one of the Chronicle predefined roles by using the correct principal format
for your Identity setup (Workforce Identity Federation or Cloud Identity 
for Google Managed Accounts).
Need more help?
Get answers from Community members and Google SecOps professionals.
