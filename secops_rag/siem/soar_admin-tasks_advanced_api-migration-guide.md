# Migrate SOAR endpoints to Chronicle API

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/api-migration-guide/  
**Scraped:** 2026-03-05T09:16:12.656169Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Migrate SOAR endpoints to Chronicle API
Supported in:
Google secops
SOAR
This document outlines the steps and considerations for migrating from the 
deprecated SOAR API surface to the unified Chronicle API. This guide is 
intended to help you transition smoothly and efficiently, minimizing 
disruption and leveraging the new functionalities.
The Chronicle API surface introduces several improvements designed to 
streamline your development process. It also addresses limitations and 
complexities present in the older API.
Prerequisites
Before performing the SOAR API migration, you need to do the following:
Complete Stage 1 of the migration
.
Stage 2 - Migrate SOAR permissions groups to IAM
Key changes and enhancements
The following table highlights the major differences between the old and new API 
surfaces:
Feature area
Old API
New API
Details
Authentication
API token
OAuth 2.0
The new authentication method provides enhanced security and standardizes the process.
Data models
Flat structures
Resource oriented design
This new design improves data consistency and simplifies object manipulation.
Endpoint naming
Inconsistent
RESTful and standardized
Consistent naming makes the API more intuitive and easier to integrate.
Deprecation schedule
The old API surface for SOAR is scheduled to be fully deprecated on 
June 30, 2026. We recommend completing your migration before this date to avoid 
any service interruptions.
Migration steps
This section outlines the steps to successfully migrate your applications to Chronicle API:
Review the documentation
Familiarize yourself with the comprehensive documentation for the new API, 
including the
Chronicle API
reference guide.
Map endpoints to the new API surface
Identify the corresponding new endpoints for each of the old API calls your 
application makes. Similarly, map the old data models to the new ones, 
accounting for any structural changes or new fields. For details, see
API endpoint mapping table
.
Optional: Create a staging integration
If you're editing a custom integration or a component of a commercial 
integration, we recommend to push the changes to a staging integration first. 
This process lets you test without impacting your production automation flows. 
If you're migrating a custom-built application that uses the SOAR API, 
you can skip to the next step. For details about integration staging, see
Test integrations in staging mode
.
Update the service endpoint and URLs
A service endpoint is the base URL that specifies the network address of an API 
service. A single service can have multiple service endpoints. Chronicle is a 
regional service and only supports regional endpoints.
All new endpoints use a consistent prefix, making the final endpoint address 
predictable. The following example shows the new endpoint URL structure:
[api_version]/projects/[project_id]/locations/[location]/instances[instance_id]/...
This structure makes the final address to the endpoint as follows:
https://[service_endpoint]/[api_version]/projects/[project_id]/locations/[location]/instances/[instance_id]/...
Where:
service_endpoint
: A regional service address
api_version
: The API version to query. Can be
v1alpha
,
v1beta
, or
v1
.
project_id
: Your project ID (same project as you defined for your IAM permissions)
location
: The location of your project (region); same as the regional 
endpoints
instance_id
: Your Google Security Operations SIEM customer ID.
Regional addresses:
africa-south1:
https://chronicle.africa-south1.rep.googleapis.com
asia-northeast1:
https://chronicle.asia-northeast1.rep.googleapis.com
asia-south1:
https://chronicle.asia-south1.rep.googleapis.com
asia-southeast1:
https://chronicle.asia-southeast1.rep.googleapis.com
asia-southeast2:
https://chronicle.asia-southeast2.rep.googleapis.com
australia-southeast1:
https://chronicle.australia-southeast1.rep.googleapis.com
europe-west12:
https://chronicle.europe-west12.rep.googleapis.com
europe-west2:
https://chronicle.europe-west2.rep.googleapis.com
europe-west3:
https://chronicle.europe-west3.rep.googleapis.com
europe-west6:
https://chronicle.europe-west6.rep.googleapis.com
europe-west9:
https://chronicle.europe-west9.rep.googleapis.com
me-central1:
https://chronicle.me-central1.rep.googleapis.com
me-central2:
https://chronicle.me-central2.rep.googleapis.com
me-west1:
https://chronicle.me-west1.rep.googleapis.com
northamerica-northeast2:
https://chronicle.northamerica-northeast2.rep.googleapis.com
southamerica-east1:
https://chronicle.southamerica-east1.rep.googleapis.com
us:
https://chronicle.us.rep.googleapis.com
eu:
https://chronicle.eu.rep.googleapis.com
For example, to get a list of all cases on a project in the US:
GET 
  https://chronicle.us.rep.googleapis.com/v1alpha/projects/my-project-name-or-id/locations/us/instances/408bfb7b-5746-4a50-885a-50a323023529/cases
Update the authentication method
The new API uses Google Cloud IAM for authentication. You'll need 
to update your application or response integration to implement this new 
authentication flow. Make sure the user who runs the script has the correct 
permissions for the endpoints they're trying to access.
To implement this new flow, you must update your response integrations or applications. Ensure that the user executing the script possesses the necessary permissions for the targeted endpoints. For detailed instructions, see the
Authenticate to Chronicle API page
.
Update API logic
Analyze the new data models and endpoint structures provided in the API 
reference. Not all methods have changed significantly, and some existing 
code can be reused. The primary objective is to review the new reference 
documentation and, for each specific use case, identify and implement necessary 
changes to field names and data structures within your application's logic.
Test your integration
Test your updated application in a staging integration before deploying to 
production:
Create a test plan: Define test cases that cover all migrated 
functionalities.
Execute tests: Run automated and manual tests to confirm accuracy and 
validity.
Monitor performance: Assess the performance of your application with the 
new API.
Need more help?
Get answers from Community members and Google SecOps professionals.
