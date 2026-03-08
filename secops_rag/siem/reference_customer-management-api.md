# Customer Management

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/customer-management-api/  
**Scraped:** 2026-03-05T09:37:40.677760Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Customer Management
Supported in:
Google secops
SIEM
Get API authentication credentials
Your Google Security Operations representative will provide you with a
Google Developer
Service Account
Credential to enable the API client to communicate with the API.
You also must provide the Auth Scope when initializing your API client. OAuth 2.0 uses
a scope to limit an application's access to an account. When an application requests a scope,
the access token issued to the application is limited to the scope granted.
Use the following scope to initialize your Backstory API client:
https://www.googleapis.com/auth/chronicle-backstory
Python example
The following Python example demonstrates how to use the OAuth2 credentials
and HTTP client using
google.oauth2
and
googleapiclient
.
# Imports required for the sample - Google Auth and API Client Library Imports.
# Get these packages from https://pypi.org/project/google-api-python-client/ or run $ pip
# install google-api-python-client from your terminal
from google.auth.transport import requests
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/chronicle-backstory']

# The apikeys-demo.json file contains the customer's OAuth 2 credentials.
# SERVICE_ACCOUNT_FILE is the full path to the apikeys-demo.json file
# ToDo: Replace this with the full path to your OAuth2 credentials
SERVICE_ACCOUNT_FILE = '/customer-keys/apikeys-demo.json'

# Create a credential using the Google Developer Service Account Credential and Backstory API
# Scope.
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Build a requests Session Object to make authorized OAuth requests.
http_session = requests.AuthorizedSession(credentials)

# Your endpoint GET|POST|PATCH|etc. code will vary below

# Reference List example (for US region)
url = 'https://backstory.googleapis.com/v2/lists/COLDRIVER_SHA256'

# You might need another regional endpoint for your API call; see
# https://cloud.google.com/chronicle/docs/reference/ingestion-api#regional_endpoints

# requests GET example
response = http_session.request("GET", url)

# POST example uses json
body = {
  "foo": "bar"
}
response = http_session.request("POST", url, json=body)

# PATCH example uses params and json
params = {
  "foo": "bar"
}
response = http_session.request("PATCH", url, params=params, json=body)

# For more complete examples, see:
# https://github.com/chronicle/api-samples-python/
Backstory API Query Limits
The Backstory API enforces limits on the volume of requests that can be made by any one customer against the Google Security Operations platform. If you reach or exceed the query limit, the Backstory API server returns HTTP 429 (RESOURCE_EXHAUSTED) to the caller. When developing applications for the Backstory API, Google SecOps recommends that you enforce rate limits within your system to avoid resource exhaustion. These limits apply to all of the Backstory APIs, including the Search, Customer Management, and Tooling APIs.
The following limit for the Backstory API is being enforced and is measured in queries per day (QPD):
Backstory API
API Method
Limit
Customer Management
CreateCustomer
30 QPD
Regional Endpoints
Your API endpoint varies depending on where your customer account is provisioned:
São Paulo
—
https://southamerica-east1-backstory.googleapis.com
Canada
—
https://northamerica-northeast2-backstory.googleapis.com
Dammam
—
https://me-central2-backstory.googleapis.com
Doha
—
https://me-central1-backstory.googleapis.com
Europe Multi-Region
—
https://europe-backstory.googleapis.com
Frankfurt
—
https://europe-west3-backstory.googleapis.com
Jakarta
—
https://asia-southeast2-backstory.googleapis.com
Johannesburg
—
https://africa-south1-backstory.googleapis.com
London
—
https://europe-west2-backstory.googleapis.com
Mumbai
—
https://asia-south1-backstory.googleapis.com
Paris
—
https://europe-west9-backstory.googleapis.com
Warsaw
—
https://europe-central2-backstory.googleapis.com
Singapore
—
https://asia-southeast1-backstory.googleapis.com
Sydney
—
https://australia-southeast1-backstory.googleapis.com
Tel Aviv
—
https://me-west1-backstory.googleapis.com
Tokyo
—
https://asia-northeast1-backstory.googleapis.com
Turin
—
https://europe-west12-backstory.googleapis.com
United States Multi-Region
—
https://backstory.googleapis.com
Zurich
—
https://europe-west6-backstory.googleapis.com
Onboarding Backstory APIs
You can onboard new Google SecOps customers using the following API calls:
CreateCustomer
GetCustomer
GetCustomerForwarderConfigs
ListCustomers
SetUIState
UpdateSSOConfig
SetGCPProjectLink
EnableIAM
GenerateIamMigrationCommands
CreateCustomer
Creates a customer and associates this customer with the partner. This API fully provisions a customer in Google SecOps. The response includes the customer ID.
Note:
CreateCustomer uses the POST method. If the POST call returns the error message "customer creation failed, creation may be retried by rerunning with the same parameters", CreateCustomer may be retried by rerunning the same request.
Note:
Valid data retention durations are limited to: SIX_MONTHS or ONE_YEAR. If the duration is unspecified, the default of ONE_YEAR is used. 
For additional retention settings, please contact Google SecOps Support or Partner Engineering.
Request
POST https://backstory.googleapis.com/v1/partner/customer/createcustomer
Request Body
{
    "customer_name": "
CUSTOMER_NAME
",
    "customer_code": "
CUSTOMER_CODE
",
    "customer_subdomains": "
CUSTOMER_SUBDOMAIN
",
    "retention_duration": "
RETENTION_DURATION
",
    "sso_config": "
SSO_CONFIGURATION
",
    "gcp_project" : "projects/
PROJECT_ID
",
    "provider_id": "locations/global/workforcePools/
WORKFORCE_POOL_ID
/providers/
PROVIDER_ID
"
    "auth_version":
"AUTH_VERSION"
}
Replace the following:
CUSTOMER_NAME
: the customer name
CUSTOMER_CODE
: the customer code
CUSTOMER_SUBDOMAIN
: the customer subdomain is how the customer accesses Google SecOps. For example,
<subdomain>.backstory.chronicle.security
.
RETENTION_DURATION
: the period of time for which data is retained
SSO_CONFIGURATION
: SAML SSO configuration for the customer's IdP.
If provided, it is validated and SSO is provisioned for the customer.
PROJECT_ID
: a globally unique identifier for your Google Cloud
project
WORKFORCE_POOL_ID
: the identifier you defined for the workforce identity pool
PROVIDER_ID
: the identifier you defined for the workforce provider
AUTH_VERSION
: the authentication mechanism for
Google SecOps. If your Google SecOps instance is
authenticated using
Cloud Identity
, then you need to specify
AUTH_VERSION_4
. However, if your Google SecOps instance is
authenticated using
Workforce Identity Federation
(
AUTH_VERSION_3
), then the
auth_version
field is
optional.
Sample Request
Save the request body in a file named
request.json
and execute the following
HTTP POST request:
curl -X POST \
    -d @request.json \
    https://backstory.googleapis.com/v1/partner/customer/createcustomer
Sample Response
{
    "id":"a216c252-adf8-4c65-b034-bb01b0619c8d",
    "customer_id":"1GVjfYUMQ/Gjzkv2/jvz3w==",
    "customer_code":"CODE",
    "customer_name":"NAME",
    "retention_duration": "ONE_YEAR",
    "sso_config":{
    "create_time":"2018-09-14T20:10:27.157476Z",
    "deploy_time":"2018-09-14T22:10:27.157476Z",
    "state":"DEPLOYED",
    "config":"SSO_CONFIG_DEPLOYED"
    },
    "credentials":[
    {
        "id":"7a34158e-75ba-4da8-917d-a1db53527059",
        "credential_type":"BACKSTORY_API",
        "credential":"12GVjfYUMQ+="
    },
    {
        "id":"c180fd3d-442f-4fc1-a84a-a9b394643625",
        "credential_type":"INGESTION_API",
        "credential":"13GVjfYUMQ+="
    },
    {
    "id": "f7a79c4c-3125-4110-a397-a8bdbb10887d",
    "credential_type": "BIGQUERY_API",
    "credential": "14GVjfYUMQ+=",
    "gcp_project" : "projects/
PROJECT_ID
",
    "provider_id": "locations/global/workforcePools/
WORKFORCE_POOL_ID
/providers/
PROVIDER_ID
"
    }
]
}
Limitations
The customer_code has the following limitations:
The code must start with a lowercase letter.
The code can only contain lowercase letters, digits, and hyphens.
The code cannot end with a hyphen.
The total length of the customer_code must be between 1 and 18 characters.
GenerateIdPMetadata
Generates new IdP metadata for a given subdomain. Customers can access Google Security Operations using
<subdomain>.backstory.chronicle.security
.
Request
POST https://backstory.googleapis.com/v1/partner/customer/generateidpmetadata
Sample Request
https://backstory.googleapis.com/v1/partner/customer/generateidpmetadata
{
    "customer_subdomain": "customer-subdomain"
}
Sample Response
{
    "metadata": "<md:EntityDescriptor xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata" entityID="https://customer-subdomain.backstory.chronicle.security/">
        <md:Extensions xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport">
            <alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512"/>
            <alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#sha384"/>
            <alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
            <alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#sha224"/>
            <alg:DigestMethod Algorithm="http://www.w3.org/2000/09/xmldsig#sha1"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha512"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha384"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha224"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha512"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha384"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2009/xmldsig11#dsa-sha256"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha1"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2000/09/xmldsig#rsa-sha1"/>
            <alg:SigningMethod Algorithm="http://www.w3.org/2000/09/xmldsig#dsa-sha1"/>
        </md:Extensions>

        <md:SPSSODescriptor WantAssertionsSigned="true" protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
            <md:Extensions>
            <init:RequestInitiator xmlns:init="urn:oasis:names:tc:SAML:profiles:SSO:request-init" Binding="urn:oasis:names:tc:SAML:profiles:SSO:request-init" Location="https://customer-subdomain.backstory.chronicle.security/"/>
            </md:Extensions>

            <md:AssertionConsumerService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="https://customer-subdomain.backstory.chronicle.security/acs"/>
        </md:SPSSODescriptor>

    </md:EntityDescriptor>"
}
GetCustomer
Retrieves the customer details, including the customer name, forwarder IDs, stored credentials, and subdomains for a given customer being managed by the calling partner.
Request
GET https://backstory.googleapis.com/v1/partner/customer/getcustomer?customer_code=code
Sample Request
https://backstory.googleapis.com/v1/partner/customer/getcustomer?customer_code=mycustomercode
Sample Response
{
    'customerCode': 'CODE',
    'customerId': '1GVjfYUMQ/Gjzkv2/jvz3w==',
    'customerName': 'NAME',
    'customerSubdomains': ['domain1', 'domain2'],
    'forwarders': ['7f675b71-e7c5-4f2a-b621-d1f0f78a0029'],
    'id': 'a216c252-adf8-4c65-b034-bb01b0619c8d',
    'retentionDuration': 'ONE_YEAR'
}
SSO Config: <xml>
INGESTION_API : {
    "type": "service_account",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
}
FORWARDER_API : {
    "type": "service_account",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
}
BACKSTORY_API : {
    "type": "service_account",
    "project_id": "",
    "private_key_id": "",
    "private_key": "",
    "client_email": "",
    "client_id": "",
    "auth_uri": "",
    "token_uri": "",
    "auth_provider_x509_cert_url": "",
    "client_x509_cert_url": ""
}
BIGQUERY_API : {
  "type": "service_account",
  "project_id": "",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "",
  "token_uri": "",
  "auth_provider_x509_cert_url": "",
  "client_x509_cert_url": ""
}
GetCustomerForwarderConfigs
Retrieves the configuration for the Linux or Windows forwarder associated with 
a customer.
This method returns the configuration for the first active forwarder
created when the Google SecOps instance was initialized. To
manage or retrieve configurations for other forwarders, use the
Forwarder Management API
or the Google SecOps
web interface.
This method ensures that the partner identified by the service account is authorized
to access the forwarder configuration for the specified customer.
Request
GET https://backstory.googleapis.com/v1/partner/customer/forwarder/getconfigs?
customer_code=code
Sample Request
https://backstory.googleapis.com/v1/partner/customer/forwarder/getconfigs?
customer_code=mycustomercode
Sample Response
{
    "id": "ID",
    "forwarder_configs": [
        {
            "platform": "UNIX",
            "config": "BASE64_REPRESENTATION_OF_CONFIG"
        },
        {
            "platform": "WINDOWS",
            "config": "BASE64_REPRESENTATION_OF_CONFIG"
        }
    ]
}
ListCustomers
Retrieves a list of the customers associated with the partner. The partner is 
identified when they authenticate using their service account credentials.
Request
GET https://backstory.googleapis.com/v1/partner/customer/listcustomers
Sample Request
https://backstory.googleapis.com/v1/partner/customer/listcustomers
Sample Response
{
   "customers":[
      {
         "id":"a216c252-adf8-4c65-b034-bb01b0619c8d",
         "customer_id":"1GVjfYUMQ/Gjzkv2/jvz3w==",
         "customer_code":"CODE",
         "customer_name":"NAME",
         "forwarders":[
            "7f675b71-e7c5-4f2a-b621-d1f0f78a0029"
         ],
         "customer_subdomains":[
            "domain1"
         ],
         "sso_config":{
            "create_time":"2018-09-14T20:10:27.157476Z",
            "deploy_time":"2018-09-14T22:10:27.157476Z",
            "state":"DEPLOYED",
            "config":"SSO_CONFIG_DEPLOYED"
         },
         "credentials":[
            {
               "id":"7a34158e-75ba-4da8-917d-a1db53527059",
               "credential_type":"BACKSTORY_API",
               "credential":"12GVjfYUMQ+="
            },
            {
               "id":"c180fd3d-442f-4fc1-a84a-a9b394643625",
               "credential_type":"INGESTION_API",
               "credential":"13GVjfYUMQ+="
            },
            {
            "id": "f7a79c4c-3125-4110-a397-a8bdbb10887d",
            "credential_type": "BIGQUERY_API",
            "credential": "14GVjfYUMQ+="
            }
        ]
      }
   ]
}
SetAuthVersion
Update the authentication version for the specified customer. After you've
integrated Google Security Operations with a third-party
identity provider
and updated
the workforce provider ID using the
SetWorkforcePoolProvider
API, you can use
the
SetAuthVersion
API to update the customer to
AUTH_VERSION_3
.
Note
:
SetAuthVersion
uses the POST method and the
auth_version
field can
only be set to
AUTH_VERSION_3
or
AUTH_VERSION_4
.
The values in the
auth_version
field are tied in to the following single
sign-on (SSO) authentication mechanisms:
AUTH_VERSION_3
corresponds to an authentication mechanism through a
third-party identity provider using
Workforce Identity Federation
.
AUTH_VERSION_4
corresponds to an authentication mechanism using
Cloud Identity
.
To use
AUTH_VERSION_3
or
AUTH_VERSION_4
, the Google SecOps
instance must be bound to a customer-owned Google Cloud project.
If you migrate an existing Google SecOps instance from a third-party
identity provider (
AUTH_VERSION_3
) to Cloud Identity (
AUTH_VERSION_4
), you
need to
change the principal in the IAM policy binding to the
user's email
.
Request
POST https://backstory.googleapis.com/v1/partner/customer/setauthversion
Sample Request
https://backstory.googleapis.com/v1/partner/customer/setauthversion
{
    "customer_code" : "CODE",
    "auth_version"  : "AUTH_VERSION_2"
}
Sample Response
{
    "authVersion":"AUTH_VERSION_2"
}
SetComplianceRequirements
Given a customer code and a list of compliance certifications, SetComplianceRequirements sets compliance requirements for the customer.
Request
POST https://backstory.googleapis.com/v1/partner/customer/setcompliancerequirements
Sample Request
https://backstory.googleapis.com/v1/partner/customer/setcompliancerequirements
{
    "customer_code" : "CODE",
    "compliance_certifications": ["COMPLIANCE_CERTIFICATION_FEDRAMP_MODERATE", "COMPLIANCE_CERTIFICATION_PCI_DSS"]
}
Sample Response
{
    "complianceCertifications": "COMPLIANCE_CERTIFICATION_FEDRAMP_MODERATE"
}
SetUIState
Enables or disables the web application of a tenant managed by a partner by updating the customer's feature flag.
Request
POST https://backstory.googleapis.com/v1/partner/customer/setuistate:state
Sample Request
https://backstory.googleapis.com/v1/partner/customer/setuistate:state
{
    "customer_code" : "CODE",
    "state": true
}
Sample Response
{
    "state": true
}
SetWorkforcePoolProvider
Given a customer code and its subdomain,
SetWorkforcePoolProvider
sets the workforce pool provider ID for the customer and its specified subdomain. Refer to the guide on
how to create a workforce pool provider ID
.
Note:
SetWorkforcePoolProvider
is an HTTP
POST
request.
Request
https://backstory.googleapis.com/v1/partner/customer/setworkforcepoolprovider
Sample Request
https://backstory.googleapis.com/v1/partner/customer/setworkforcepoolprovider
{
    "customer_code" : "CODE",
    "customer_subdomain": "customer-subdomain",
    "provider_id": "locations/global/workforcePools/workforce-pool-id-foo/providers/workforce-provider-id-bar"
}
Sample Response
{
    "providerId":"locations/global/workforcePools/workforce-pool-id-foo/providers/workforce-provider-id-bar"
}
UpdateSSOConfig
Lets you update the SSO Configuration for a specified Google SecOps instance that uses federated authentication,
not
Bring Your Own Identity (BYOID). You can optionally add a subdomain if there are multiple subdomains for a given customer. If you call this API as part of the migration from AUTH_VERSION_1 to AUTH_VERSION_2, Google recommends setting the
update_v2_only
field to true.
Note:
To update BYOID, a customer must use the
SetWorkforcePoolProvider
endpoint.
Note:
UpdateSSOConfig uses HTTP
PATCH
request.
Note:
A Google SecOps instance can use only one authorization method. For example, if a Google SecOps instance has 2 frontend paths (URLs), both of them must use federated authentication or BYOID.
Request
PATCH https://backstory.googleapis.com/v1/partner/customer/updatessoconfig
Sample Request
https://backstory.googleapis.com/v1/partner/customer/updatessoconfig
{
    "customer_code" : "CODE",
    "sso_config": "NEW_CONFIG"
    "customer_subdomain": "customer-subdomain"
    "update_v2_only": "true"

}
Sample Response
{
    "create_time":"2018-09-14T20:10:27.157476Z",
    "deploy_time":"2018-09-14T22:10:27.157476Z",
    "state":"DEPLOYED",
    "config":"SSO_CONFIG_DEPLOYED"
}
SetGCPProjectLink
Binds a Google Cloud
project
to the Google SecOps instance of the customer organization specified in the request body. For more information, see
Bind Google SecOps to a Google Cloud project
.
Before making a SetGCPProjectLink request, confirm the following:
The Google Cloud project must be owned by the Google SecOps customer within a Google Cloud organization that is also owned by the customer.
The Backstory API must be enabled on the Google Cloud project.
The Google SecOps customer must be a customer that you, the partner, created.
Request
POST https://backstory.googleapis.com/v1/partner/customer/setgcpprojectlink
Sample Request
POST https://backstory.googleapis.com/v1/partner/customer/setgcpprojectlink
{
    "customer_code" : "mycustomercode",
    "gcp_project" : "projects/012345678901",
}
Body parameters
Field
Type
Required
Description
customer_code
string
Required
The value for the
customer_code
field specified in a CreateCustomer request.
gcp_project
string
Required
Either of the following:
The
projectId
of the Google Cloud project in the format
projects/
PROJECT_ID
The
projectNumber
of the Google Cloud project in the format
projects/
PROJECT_NUMBER
For example:
projects/012345678901
or
projects/my-project
For more information, see
Creating and managing projects
.
Sample Response
A successful call returns an empty response object.
{
}
GenerateIamMigrationCommands
Provides auto-generated commands that create new
IAM policies equivalent to your existing
Google SecOps RBAC
access control, which is configured in Google SecOps, under the
SIEM Settings
>
Users and Groups
page.
Request
POST https://backstory.googleapis.com/v1/partner/customer/iammigration:generateIamMigrationCommands
Sample Request
POST https://backstory.googleapis.com/v1/partner/customer/iammigration:generateIamMigrationCommands
{
    "customer_code" : "mycustomercode",
}
Body parameters
Field
Type
Required
Description
customer_code
string
Required
The value for the
customer_code
field specified in a CreateCustomer request.
Sample Response
{
    "migrations" : [
        {
            "frontend_path": "customer-subdomain",
            "commands": "gcloud projects add-iam-policy-binding my-project --member='principal://iam.googleapis.com/locations/global/workforcePools/workforce-pool-id-foo/subject/user1@somedomain.com' --role=roles/chronicle.editor; gcloud projects add-iam-policy-binding my-project --member='principal://iam.googleapis.com/locations/global/workforcePools/workforce-pool-id-foo/subject/user2@somedomain.com' --role=roles/chronicle.viewer;"
        }
    ]
}
EnableIAM
Enables Feature RBAC controlled using IAM on the Google SecOps instance of the customer organization specified in the request body.
Before making a EnableIAM request, confirm the following:
You have completed all the prerequisites mentioned in
Configure feature access control using IAM
GenerateIamMigrationCommands API
provides auto-generated commands that create new
IAM policies equivalent to your existing
Google SecOps RBAC
access control, which is configured in Google SecOps, under the
SIEM Settings
>
Users and Groups
page. Make sure you have executed all these commands in gcloud CLI.
After you execute this API request, you can't revert back to the
Google SecOps RBAC
access control feature. If you encounter an issue, contact
Technical Support
.
Request
POST https://backstory.googleapis.com/v1/partner/customer/iammigration:enableIam
Sample Request
POST https://backstory.googleapis.com/v1/partner/customer/iammigration:enableIam
{
    "customer_code" : "mycustomercode",
}
Body parameters
Field
Type
Required
Description
customer_code
string
Required
The value for the
customer_code
field specified in a CreateCustomer request.
Sample Response
A successful call returns an empty response object.
{
}
