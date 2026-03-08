# Enable SOAR access

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/enable-soar-access/  
**Scraped:** 2026-03-05T09:14:55.317884Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Enable SOAR access
Supported in:
Google secops
This document is for Google Security Operations admins who want provide users with access to 
SOAR features in Google SecOps (such as managing cases).
Before you begin
These procedures are based on the assumption that you have already onboarded
to the Google SecOps platform, enabled the Chronicle API, and started
working with IAM permissions. The following procedures may vary slightly,
depending on whether you configured a
Cloud Identity provider
or a
third-party identity provider
.
Enable access
Define either a
predefined role
or a
custom role
.
The custom role must contain the following minimum permissions:
chronicle.instances.get
chronicle.preferenceSets.get
chronicle.preferenceSets.update
chronicle.dataAccessScopes.list
If you're using the Cloud Identity Provider, map
user email groups
into the
email group mapping page
.
If you're using a third-party identity provider, map
IdP groups
into the
IdP group mapping page
.
You can choose the control access parameters that meet your needs. 
For more information see,
control access parameters
.
Need more help?
Get answers from Community members and Google SecOps professionals.
