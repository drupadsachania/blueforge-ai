# Collect Fastly WAF logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fastly-waf/  
**Scraped:** 2026-03-05T09:55:39.494347Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fastly WAF logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Fastly WAF JSON logs, transforms and renames them, and maps them to the UDM. It handles various data types, converts severity levels, and categorizes events based on available IP and hostname information. It also handles potential parsing failures and drops malformed log entries.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Fastly account with access to configure WAF settings.
Set up feeds
To configure a feed, follow these steps:
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
Fastly WAF Logs
).
Select
Webhook
as the
Source type
.
Select
Fastly WAF
as the
Log type
.
Click
Next
.
Optional: Specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
On the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. You need to specify this endpoint URL in your client application.
Click
Done
.
Create an API key for the webhook feed
Go to
Google Cloud console
>
Credentials
.
Go to Credentials
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Google Security Operations API
.
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL.
If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Configure webhook in Fastly
Sign in to Fastly.
Optional: Select a site in the
Sites
menu (if you have more than one site).
Select
Manage
>
Site Integrations
.
Click
Add site integration
.
Select
Generic Webhook
.
Webhook URL
: enter Google SecOps
ENDPOINT_URL
, followed by
API_KEY
and
SECRET
.
Alert Placement
: select
All activity
or
Specific activity
.
Optional: If you selected
Specific activity
, go to the
Activity menu
and select the activity types that you want the webhook to send.
Click
Create site integration
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
anomaly_score
security_result.detection_fields[].key
: "anomaly"
security_result.detection_fields[].value
:
anomaly_score
If
waf.score.anomaly
is 0 or empty and
anomaly_score
is not empty or 0, the
anomaly_score
value is used to populate the
security_result.detection_fields
array with a key of "anomaly" and the value of the
anomaly_score
field.
cache_status
additional.fields[].key
: "cache_status"
additional.fields[].value.string_value
:
cache_status
The
cache_status
value is used to populate the
additional.fields
array with a key of "cache_status" and the value of the
cache_status
field.
client_ip
principal.ip
:
client_ip
The
client_ip
field is mapped to
principal.ip
.
connection.fastly_is_edge
additional.fields[].key
: "fastly_is_edge"
additional.fields[].value.bool_value
:
connection.fastly_is_edge
The
connection.fastly_is_edge
value is used to populate the
additional.fields
array with a key of "fastly_is_edge" and the value of the
connection.fastly_is_edge
field.
connection.fastly_is_shield
additional.fields[].key
: "fastly_is_shield"
additional.fields[].value.bool_value
:
connection.fastly_is_shield
The
connection.fastly_is_shield
value is used to populate the
additional.fields
array with a key of "fastly_is_shield" and the value of the
connection.fastly_is_shield
field.
connection.request_tls_version
network.tls.version
:
connection.request_tls_version
The
connection.request_tls_version
field is mapped to
network.tls.version
.
fastly.server
target.hostname
:
fastly.server
The
fastly.server
field is mapped to
target.hostname
.
fastly.service_id
additional.fields[].key
: "service_id"
additional.fields[].value.string_value
:
fastly.service_id
The
fastly.service_id
value is used to populate the
additional.fields
array with a key of "service_id" and the value of the
fastly.service_id
field.
geo.city
principal.location.city
:
geo.city
The
geo.city
field is mapped to
principal.location.city
.
geo.country
principal.location.country_or_region
:
geo.country
The
geo.country
field is mapped to
principal.location.country_or_region
.
geo.location
principal.location.region_latitude
: extracted from
geo.location
principal.location.region_longitude
: extracted from
geo.location
The latitude and longitude are extracted from the
geo.location
field using a regular expression and mapped to
principal.location.region_latitude
and
principal.location.region_longitude
respectively.
geo.region
principal.location.state
:
geo.region
The
geo.region
field is mapped to
principal.location.state
.
host
principal.hostname
:
host
The
host
field is mapped to
principal.hostname
.
request_headers.accept_charset
additional.fields[].key
: "accept_charset"
additional.fields[].value.string_value
:
request_headers.accept_charset
The
request_headers.accept_charset
value is used to populate the
additional.fields
array with a key of "accept_charset" and the value of the
request_headers.accept_charset
field.
request_headers.accept_language
additional.fields[].key
: "accept_language"
additional.fields[].value.string_value
:
request_headers.accept_language
The
request_headers.accept_language
value is used to populate the
additional.fields
array with a key of "accept_language" and the value of the
request_headers.accept_language
field.
request_headers.referer
network.http.referral_url
:
request_headers.referer
The
request_headers.referer
field is mapped to
network.http.referral_url
.
request_headers.user_agent
network.http.user_agent
:
request_headers.user_agent
The
request_headers.user_agent
field is mapped to
network.http.user_agent
.
request_id
metadata.product_log_id
:
request_id
The
request_id
field is mapped to
metadata.product_log_id
.
request_method
network.http.method
:
request_method
The
request_method
field is mapped to
network.http.method
.
response_headers.cache_control
additional.fields[].key
: "cache_control"
additional.fields[].value.string_value
:
response_headers.cache_control
The
response_headers.cache_control
value is used to populate the
additional.fields
array with a key of "cache_control" and the value of the
response_headers.cache_control
field.
response_headers.content_type
additional.fields[].key
: "content_type"
additional.fields[].value.string_value
:
response_headers.content_type
The
response_headers.content_type
value is used to populate the
additional.fields
array with a key of "content_type" and the value of the
response_headers.content_type
field.
response_state
additional.fields[].key
: "response_state"
additional.fields[].value.string_value
:
response_state
The
response_state
value is used to populate the
additional.fields
array with a key of "response_state" and the value of the
response_state
field.
response_status
network.http.response_code
:
response_status
The
response_status
field is mapped to
network.http.response_code
if the
status
field is empty.
rule_id
security_result.rule_id
:
rule_id
If
waf.rule_id
is empty, the
rule_id
value is used to populate
security_result.rule_id
.
severity
waf.severity
:
severity
The
severity
field value is copied to
waf.severity
.
size_bytes.request_header
network.sent_bytes
:
size_bytes.request_header
The
size_bytes.request_header
field is mapped to
network.sent_bytes
.
size_bytes.response_header
network.received_bytes
:
size_bytes.response_header
The
size_bytes.response_header
field is mapped to
network.received_bytes
.
status
network.http.response_code
:
status
The
status
field is mapped to
network.http.response_code
.
timestamp
metadata.event_timestamp
:
timestamp
The
timestamp
field is parsed and mapped to
metadata.event_timestamp
.
url
target.url
:
url
The
url
field is mapped to
target.url
.
waf.blocked
security_result.action
: derived
If
waf.blocked
is false,
security_result.action
is set to "ALLOW". If
waf.blocked
is true,
security_result.action
is set to "BLOCK".
waf.executed
security_result.detection_fields[].key
: "executed"
security_result.detection_fields[].value
:
waf.executed
The
waf.executed
value is used to populate the
security_result.detection_fields
array with a key of "executed" and the value of the
waf.executed
field.
waf.failures
security_result.detection_fields[].key
: "failures"
security_result.detection_fields[].value
:
waf.failures
The
waf.failures
value is used to populate the
security_result.detection_fields
array with a key of "failures" and the value of the
waf.failures
field.
waf.logged
security_result.detection_fields[].key
: "logged"
security_result.detection_fields[].value
:
waf.logged
The
waf.logged
value is used to populate the
security_result.detection_fields
array with a key of "logged" and the value of the
waf.logged
field.
waf.message
metadata.description
:
waf.message
If
waf.message
is not empty, it is mapped to
metadata.description
.
waf.rule_id
security_result.rule_id
:
waf.rule_id
If
waf.rule_id
is not empty, it is mapped to
security_result.rule_id
.
waf.score.anomaly
security_result.detection_fields[].key
: "anomaly"
security_result.detection_fields[].value
:
waf.score.anomaly
If
waf.score.anomaly
is not 0 and not empty, the value is used to populate the
security_result.detection_fields
array with a key of "anomaly" and the value of the
waf.score.anomaly
field.
waf.score.http_violation
security_result.detection_fields[].key
: "http_violation"
security_result.detection_fields[].value
:
waf.score.http_violation
If
waf.score.http_violation
is not 0 and not empty, the value is used to populate the
security_result.detection_fields
array.
waf.score.lfi
security_result.detection_fields[].key
: "lfi"
security_result.detection_fields[].value
:
waf.score.lfi
Similar logic as
waf.score.http_violation
.
waf.score.php_injection
security_result.detection_fields[].key
: "php_injection"
security_result.detection_fields[].value
:
waf.score.php_injection
Similar logic as
waf.score.http_violation
.
waf.score.rce
security_result.detection_fields[].key
: "rce"
security_result.detection_fields[].value
:
waf.score.rce
Similar logic as
waf.score.http_violation
.
waf.score.rfi
security_result.detection_fields[].key
: "rfi"
security_result.detection_fields[].value
:
waf.score.rfi
Similar logic as
waf.score.http_violation
.
waf.score.session_fixation
security_result.detection_fields[].key
: "session_fixation"
security_result.detection_fields[].value
:
waf.score.session_fixation
Similar logic as
waf.score.http_violation
.
waf.score.sql_injection
security_result.detection_fields[].key
: "sql_injection"
security_result.detection_fields[].value
:
waf.score.sql_injection
Similar logic as
waf.score.http_violation
.
waf.score.xss
security_result.detection_fields[].key
: "xss"
security_result.detection_fields[].value
:
waf.score.xss
Similar logic as
waf.score.http_violation
.
waf.severity
security_result.severity
: derived
security_result.severity_details
:
waf.severity
If
waf.severity
is not empty, it determines the value of
security_result.severity
based on ranges (<=3: HIGH, >3 and <=6: MEDIUM, >6 and <=8: LOW, else: UNKNOWN_SEVERITY). The original
waf.severity
value is also mapped to
security_result.severity_details
.
waf_message
metadata.description
:
waf_message
If
waf.message
is empty and
waf_message
is not empty, it is mapped to
metadata.description
. If
client_ip
or
host
and
fastly.server
are not empty,
metadata.event_type
is set to "NETWORK_HTTP". Else if
client_ip
or
host
are not empty,
metadata.event_type
is set to "STATUS_UPDATE". Otherwise, it's set to "GENERIC_EVENT". Hardcoded value. Hardcoded value. Hardcoded value.
Need more help?
Get answers from Community members and Google SecOps professionals.
