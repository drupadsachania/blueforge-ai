# Collect DNSFilter logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/dnsfilter/  
**Scraped:** 2026-03-05T09:23:27.091925Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect DNSFilter logs
Supported in:
Google secops
SIEM
This document explains how to configure DNSFilter to push logs into Google Security Operations using webhooks via the HTTP Event Collector (HEC) protocol.
DNSFilter is an AI-powered DNS security solution that provides threat protection, content filtering, and network visibility. The Data Export feature enables automated export of DNS query log data to SIEM platforms via HTTP Event Collector (HEC) API, supporting real-time security monitoring and compliance reporting.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Access to
DNSFilter dashboard
with administrator permissions or higher
DNSFilter Data Export
add-on feature enabled (available for Basic, Pro, and Enterprise plans as a paid add-on)
Access to Google Cloud Console (for API key creation)
Create webhook feed in Google SecOps
Create the feed
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
DNSFilter HEC Feed
).
Select
Webhook
as the
Source type
.
Select
DNSFILTER
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
(optional): Leave empty as each HEC request contains properly formatted events
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Generate and save secret key
After creating the feed, you must generate a secret key for authentication:
On the feed details page, click
Generate Secret Key
.
A dialog displays the secret key.
Copy and save
the secret key securely.
Get the feed endpoint URL
Go to the
Details
tab of the feed.
In the
Endpoint Information
section, copy the
Feed endpoint URL
.
The URL format is:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
or
https://<REGION>-malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate
Save this URL for the next steps.
Click
Done
.
Create Google Cloud API key
Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.
Create the API key
Go to the
Google Cloud Console Credentials page
.
Select your project (the project associated with your Google SecOps instance).
Click
Create credentials
>
API key
.
An API key is created and displayed in a dialog.
Click
Edit API key
to restrict the key.
Restrict the API key
In the
API key
settings page:
Name
: Enter a descriptive name (for example,
Google SecOps DNSFilter Webhook API Key
)
Under
API restrictions
:
Select
Restrict key
.
In the
Select APIs
dropdown, search for and select
Google SecOps API
(or
Chronicle API
).
Click
Save
.
Copy
the API key value from the
API key
field at the top of the page.
Save the API key securely.
Configure DNSFilter Data Export
Construct the HEC endpoint URL
Combine the Google SecOps endpoint URL and API key to create the HEC URL:
<ENDPOINT_URL>?key=<API_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
Configure Data Export in DNSFilter
Sign in to the
DNSFilter dashboard
.
Go to
Tools
>
Data Export
.
In the
Export Destination
section, select
HTTP Event Collector (HEC)
.
In the
HEC Configuration
section, enter the following:
HTTP Event Collector URL
: Paste the complete endpoint URL with API key from the previous step.
Active Event Collector Token
: Paste the secret key generated during Google SecOps feed creation.
Click
Save Configuration
.
DNSFilter will test the connection and display a success message if the configuration is correct.
Verify data ingestion
In the
DNSFilter dashboard
, go to
Tools
>
Data Export
.
Verify the
Status
shows as
Active
or
Connected
.
In the Google SecOps console, go to
SIEM Settings
>
Feeds
.
Locate your DNSFilter feed and verify the
Status
shows as
Active
.
Click the feed name to view details.
Check the
Logs Ingested
metric to confirm data is flowing.
To search for DNSFilter events, go to
Search
, and run the following query:
metadata.log_type = "DNSFILTER"
Authentication methods reference
Google SecOps webhook feeds support multiple authentication methods. DNSFilter HEC integration uses the hybrid method.
Method used: Hybrid (URL + Header)
DNSFilter sends the API key in the URL and the secret key (HEC token) in the request header.
Request format:
POST <ENDPOINT_URL>?key=<API_KEY> HTTP/1.1
Content-Type: application/json
Authorization: Splunk <SECRET_KEY>
{
"event": "data",
"timestamp": "2025-01-15T10:30:00Z"
}
Alternative method: Custom headers
If configuring a custom application to send logs to Google SecOps, use this method for better security.
Request format:
POST <ENDPOINT_URL> HTTP/1.1
Content-Type: application/json
x-goog-chronicle-auth: <API_KEY>
x-chronicle-auth: <SECRET_KEY>
{
"event": "data",
"timestamp": "2025-01-15T10:30:00Z"
}
Advantages:
API key and secret not visible in URL
More secure (headers not logged in web server access logs)
Preferred method when vendor supports it
Authentication header names
Google SecOps accepts the following header names for authentication:
For API key:
x-goog-chronicle-auth
(recommended)
X-Goog-Chronicle-Auth
(case-insensitive)
For secret key:
x-chronicle-auth
(recommended)
X-Chronicle-Auth
(case-insensitive)
Authorization: Splunk <TOKEN>
(HEC compatibility)
Webhook limits and best practices
Request limits
Limit
Value
Max request size
4 MB
Max QPS (queries per second)
15,000
Request timeout
30 seconds
Retry behavior
Automatic with exponential backoff
Best practices
Monitor export status
: Regularly check the Data Export status in DNSFilter dashboard to ensure continuous data flow.
API key rotation
: Periodically rotate your Google Cloud API key for security.
Secret key management
: Store the Google SecOps secret key securely and regenerate if compromised.
Data retention
: Configure appropriate data retention policies in both DNSFilter and Google SecOps.
Alert configuration
: Set up alerts in Google SecOps for critical DNS security events.
Troubleshooting
Connection test fails
If the DNSFilter Data Export configuration test fails:
Verify the HEC URL is correct and includes the API key parameter.
Verify the secret key (HEC token) is copied correctly without extra spaces.
Check that the Google Cloud API key has Chronicle API access enabled.
Verify the Google SecOps feed is in
Active
status.
Check network connectivity from DNSFilter to Google Cloud endpoints.
No data appearing in Google SecOps
If the connection succeeds but no data appears:
Verify DNS queries are being generated in your DNSFilter deployment.
Check the DNSFilter Query Log to confirm traffic is being processed.
In Google SecOps, search for
metadata.log_type = "DNSFILTER"
to verify ingestion.
Check the feed
Logs Ingested
metric in Google SecOps.
Review the feed
Error Logs
for any ingestion errors.
Data Export returns error message
Common error causes:
Invalid credentials
: The API key or secret key is incorrect or expired.
Region mismatch
: The Google SecOps endpoint URL region doesn't match your instance.
Permissions
: The API key doesn't have Chronicle API access enabled.
Network issues
: Firewall or proxy blocking outbound HTTPS connections.
UDM mapping table
Log Field
UDM Mapping
Logic
time
metadata.collected_timestamp
Converted using date format: yyyy-MM-dd HH:mm:ss Z UTC
metadata.event_type
Set to "STATUS_UPDATE" if principal_ip_present, principal_hostname_present, or principal_mac_present is true, else "GENERIC_EVENT"
question_type
network.dns.questions
Converted question_type to question.type using DNS record type mapping, then merged into array
code
network.dns.response_code
Converted using DNS response code mapping
protocol
network.ip_protocol
Converted using IP protocol mapping
client
principal.hostname
Value copied directly
request_address, ip4, ip6, source_addresses
principal.ip
Merged from request_address (extracted IP), ip4 (extracted IP), ip6 (extracted IP), and IPs extracted from source_addresses array
region
principal.location.country_or_region
Value copied directly
clientMac
principal.mac
Value copied directly if matches MAC regex
clientID
principal.resource.product_object_id
Value copied directly
username
principal.user.user_display_name
Value copied directly
user_id
principal.user.userid
Value copied directly
code, original_code, clientType, collection, network_name, networkID, collectionID, policy, policyID, scheduled_policy, scheduled_policyID, sec_cats, sec_allow_cats, block_cats, block_allow_cats, threat, allowed, method, organization, organizationID, applicationID, application_name, application_categoryID, application_category_name
security_result.detection_fields
Merged labels from various source fields as key-value pairs
domain
target.administrative_domain
Value copied directly
fqdn
target.domain.name
Value copied directly
metadata.product_name
Set to "DNSFILTER"
metadata.vendor_name
Set to "DNSFILTER"
Need more help?
Get answers from Community members and Google SecOps professionals.
