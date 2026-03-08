# Collect DomainTools Iris Investigate results

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/domaintools-threatintel/  
**Scraped:** 2026-03-05T09:54:42.477682Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect DomainTools Iris Investigate results
Supported in:
Google secops
SIEM
This document explains how to ingest DomainTools Iris Investigate results to Google Security Operations using Google Cloud Storage. The parser transforms raw JSON data from DomainTools' Iris API into a structured format conforming to Google SecOps's Unified Data Model (UDM). It extracts information related to domain details, contact information, security risks, SSL certificates, and other relevant attributes, mapping them to corresponding UDM fields for consistent analysis and threat intelligence.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to DomainTools enterprise account (API access to Iris Investigate)
A GCP project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to manage IAM policies on GCS buckets
Permissions to create Cloud Run services, Pub/Sub topics, and Cloud Scheduler jobs
Get DomainTools API Key and Endpoint
Sign in to the
DomainTools API Dashboard
(only the API owner account can reset the API key).
In the
My Account
section, select the
View API Dashboard
link located in the
Account Summary
tab.
Go to the
API Username
section to obtain your username.
In the same tab, locate your
API Key
.
Copy and save the key in a secure location. If you need a new key, select
Reset API Key
.
Note the Iris Investigate endpoint:
https://api.domaintools.com/v1/iris-investigate/
.
Create Google Cloud Storage bucket
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
domaintools-iris
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location (for example,
us-central1
)
Storage class
Standard (recommended for frequently accessed logs)
Access control
Uniform (recommended)
Protection tools
Optional: Enable object versioning or retention policy
Click
Create
.
Create service account for Cloud Run function
The Cloud Run function needs a service account with permissions to write to GCS bucket and be invoked by Pub/Sub.
Create service account
In the
GCP Console
, go to
IAM & Admin
>
Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter
domaintools-iris-collector-sa
.
Service account description
: Enter
Service account for Cloud Run function to collect DomainTools Iris Investigate logs
.
Click
Create and Continue
.
In the
Grant this service account access to project
section, add the following roles:
Click
Select a role
.
Search for and select
Storage Object Admin
.
Click
+ Add another role
.
Search for and select
Cloud Run Invoker
.
Click
+ Add another role
.
Search for and select
Cloud Functions Invoker
.
Click
Continue
.
Click
Done
.
These roles are required for:
Storage Object Admin
: Write logs to GCS bucket and manage state files
Cloud Run Invoker
: Allow Pub/Sub to invoke the function
Cloud Functions Invoker
: Allow function invocation
Grant IAM permissions on GCS bucket
Grant the service account write permissions on the GCS bucket:
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
domaintools-iris-collector-sa@PROJECT_ID.iam.gserviceaccount.com
).
Assign roles
: Select
Storage Object Admin
.
Click
Save
.
Create Pub/Sub topic
Create a Pub/Sub topic that Cloud Scheduler will publish to and the Cloud Run function will subscribe to.
In the
GCP Console
, go to
Pub/Sub
>
Topics
.
Click
Create topic
.
Provide the following configuration details:
Topic ID
: Enter
domaintools-iris-trigger
.
Leave other settings as default.
Click
Create
.
Create Cloud Run function to collect logs
The Cloud Run function is triggered by Pub/Sub messages from Cloud Scheduler to fetch logs from DomainTools Iris Investigate API and writes them to GCS.
In the
GCP Console
, go to
Cloud Run
.
Click
Create service
.
Select
Function
(use an inline editor to create a function).
In the
Configure
section, provide the following configuration details:
Setting
Value
Service name
domaintools-iris-collector
Region
Select region matching your GCS bucket (for example,
us-central1
)
Runtime
Select
Python 3.12
or later
In the
Trigger (optional)
section:
Click
+ Add trigger
.
Select
Cloud Pub/Sub
.
In
Select a Cloud Pub/Sub topic
, choose the Pub/Sub topic (
domaintools-iris-trigger
).
Click
Save
.
In the
Authentication
section:
Select
Require authentication
.
Check
Identity and Access Management (IAM)
.
Scroll down and expand
Containers, Networking, Security
.
Go to the
Security
tab:
Service account
: Select the service account (
domaintools-iris-collector-sa
).
Go to the
Containers
tab:
Click
Variables & Secrets
.
Click
+ Add variable
for each environment variable:
Variable Name
Example Value
Description
GCS_BUCKET
domaintools-iris
GCS bucket name where data will be stored.
GCS_PREFIX
domaintools/iris/
Optional GCS prefix (subfolder) for objects.
STATE_KEY
domaintools/iris/state.json
Optional state/checkpoint file key.
DT_API_KEY
DT-XXXXXXXXXXXXXXXXXXXX
DomainTools API key.
USE_MODE
HASH
Select which mode to use:
HASH
,
DOMAINS
, or
QUERY
(only one is active at a time).
SEARCH_HASHES
hash1;hash2;hash3
Required if
USE_MODE=HASH
. Semicolon-separated list of saved search hashes from the Iris UI.
DOMAINS
example.com;domaintools.com
Required if
USE_MODE=DOMAINS
. Semicolon-separated list of domains.
QUERY_LIST
ip=1.1.1.1;ip=8.8.8.8;domain=example.org
Required if
USE_MODE=QUERY
. Semicolon-separated list of query strings (
k=v&k2=v2
).
PAGE_SIZE
500
Rows per page (default 500).
MAX_PAGES
20
Max pages per request.
In the
Variables & Secrets
section, scroll down to
Requests
:
Request timeout
: Enter
900
seconds (15 minutes).
Go to the
Settings
tab:
In the
Resources
section:
Memory
: Select
512 MiB
or higher.
CPU
: Select
1
.
In the
Revision scaling
section:
Minimum number of instances
: Enter
0
.
Maximum number of instances
: Enter
100
(or adjust based on expected load).
Click
Create
.
Wait for the service to be created (1-2 minutes).
After the service is created, the
inline code editor
opens automatically.
Add function code
Enter
main
in
Function entry point
In the inline code editor, create two files:
First file:
main.py:
import
functions_framework
from
google.cloud
import
storage
import
json
import
os
import
urllib.parse
from
urllib.request
import
Request
,
urlopen
from
urllib.error
import
HTTPError
import
time
from
datetime
import
datetime
,
timezone
# Initialize Storage client
storage_client
=
storage
.
Client
()
# Environment variables
GCS_BUCKET
=
os
.
environ
.
get
(
"GCS_BUCKET"
,
""
)
.
strip
()
GCS_PREFIX
=
os
.
environ
.
get
(
"GCS_PREFIX"
,
"domaintools/iris/"
)
.
strip
()
STATE_KEY
=
os
.
environ
.
get
(
"STATE_KEY"
,
"domaintools/iris/state.json"
)
.
strip
()
DT_API_KEY
=
os
.
environ
.
get
(
"DT_API_KEY"
,
""
)
.
strip
()
USE_MODE
=
os
.
environ
.
get
(
"USE_MODE"
,
"HASH"
)
.
strip
()
.
upper
()
SEARCH_HASHES
=
[
h
.
strip
()
for
h
in
os
.
environ
.
get
(
"SEARCH_HASHES"
,
""
)
.
split
(
";"
)
if
h
.
strip
()]
DOMAINS
=
[
d
.
strip
()
for
d
in
os
.
environ
.
get
(
"DOMAINS"
,
""
)
.
split
(
";"
)
if
d
.
strip
()]
QUERY_LIST
=
[
q
.
strip
()
for
q
in
os
.
environ
.
get
(
"QUERY_LIST"
,
""
)
.
split
(
";"
)
if
q
.
strip
()]
PAGE_SIZE
=
int
(
os
.
environ
.
get
(
"PAGE_SIZE"
,
"500"
))
MAX_PAGES
=
int
(
os
.
environ
.
get
(
"MAX_PAGES"
,
"20"
))
USE_NEXT
=
os
.
environ
.
get
(
"USE_NEXT"
,
"true"
)
.
lower
()
==
"true"
HTTP_TIMEOUT
=
int
(
os
.
environ
.
get
(
"HTTP_TIMEOUT"
,
"60"
))
RETRIES
=
int
(
os
.
environ
.
get
(
"HTTP_RETRIES"
,
"2"
))
BASE_URL
=
"https://api.domaintools.com/v1/iris-investigate/"
HDRS
=
{
"X-Api-Key"
:
DT_API_KEY
,
"Accept"
:
"application/json"
,
}
def
_http_post
(
url
:
str
,
body
:
dict
)
-
>
dict
:
"""Make HTTP POST request with form-encoded body."""
req
=
Request
(
url
,
method
=
"POST"
)
for
k
,
v
in
HDRS
.
items
():
req
.
add_header
(
k
,
v
)
req
.
add_header
(
"Content-Type"
,
"application/x-www-form-urlencoded"
)
encoded_body
=
urllib
.
parse
.
urlencode
(
body
,
doseq
=
True
)
.
encode
(
'utf-8'
)
attempt
=
0
while
True
:
try
:
with
urlopen
(
req
,
data
=
encoded_body
,
timeout
=
HTTP_TIMEOUT
)
as
r
:
return
json
.
loads
(
r
.
read
()
.
decode
(
"utf-8"
))
except
HTTPError
as
e
:
if
e
.
code
in
(
429
,
500
,
502
,
503
,
504
)
and
attempt
<
RETRIES
:
delay
=
int
(
e
.
headers
.
get
(
"Retry-After"
,
"2"
))
time
.
sleep
(
max
(
1
,
delay
))
attempt
+=
1
continue
raise
def
_write_page
(
bucket
,
obj
:
dict
,
label
:
str
,
page
:
int
)
-
>
str
:
ts
=
time
.
strftime
(
"%Y/%m/
%d
/%H%M%S"
,
time
.
gmtime
())
key
=
f
"
{
GCS_PREFIX
.
rstrip
(
'/'
)
}
/
{
ts
}
-
{
label
}
-p
{
page
:
05d
}
.json"
blob
=
bucket
.
blob
(
key
)
blob
.
upload_from_string
(
json
.
dumps
(
obj
,
separators
=
(
","
,
":"
)),
content_type
=
"application/json"
)
return
key
def
_first_page_params
()
-
>
dict
:
params
=
{
"page_size"
:
str
(
PAGE_SIZE
)}
if
USE_NEXT
:
params
[
"next"
]
=
"true"
return
params
def
_paginate
(
bucket
,
label
:
str
,
params
:
dict
)
-
>
tuple
:
pages
=
0
total
=
0
while
pages
<
MAX_PAGES
:
data
=
_http_post
(
BASE_URL
,
params
)
_write_page
(
bucket
,
data
,
label
,
pages
)
resp
=
data
.
get
(
"response"
)
or
{}
results
=
resp
.
get
(
"results"
)
or
[]
total
+=
len
(
results
)
pages
+=
1
next_url
=
resp
.
get
(
"next"
)
if
isinstance
(
resp
,
dict
)
else
None
if
next_url
:
parsed
=
urllib
.
parse
.
urlparse
(
next_url
)
params
=
dict
(
urllib
.
parse
.
parse_qsl
(
parsed
.
query
))
continue
if
resp
.
get
(
"has_more_results"
)
and
resp
.
get
(
"position"
):
base
=
_first_page_params
()
base
.
pop
(
"next"
,
None
)
base
[
"position"
]
=
resp
[
"position"
]
params
=
base
continue
break
return
pages
,
total
def
run_hashes
(
bucket
,
hashes
:
list
)
-
>
dict
:
agg_pages
=
agg_results
=
0
for
h
in
hashes
:
params
=
_first_page_params
()
params
[
"search_hash"
]
=
h
p
,
r
=
_paginate
(
bucket
,
f
"hash-
{
h
}
"
,
params
)
agg_pages
+=
p
agg_results
+=
r
return
{
"pages"
:
agg_pages
,
"results"
:
agg_results
}
def
run_domains
(
bucket
,
domains
:
list
)
-
>
dict
:
agg_pages
=
agg_results
=
0
for
d
in
domains
:
params
=
_first_page_params
()
params
[
"domain"
]
=
d
p
,
r
=
_paginate
(
bucket
,
f
"domain-
{
d
}
"
,
params
)
agg_pages
+=
p
agg_results
+=
r
return
{
"pages"
:
agg_pages
,
"results"
:
agg_results
}
def
run_queries
(
bucket
,
queries
:
list
)
-
>
dict
:
agg_pages
=
agg_results
=
0
for
q
in
queries
:
base
=
_first_page_params
()
for
k
,
v
in
urllib
.
parse
.
parse_qsl
(
q
,
keep_blank_values
=
True
):
base
.
setdefault
(
k
,
v
)
p
,
r
=
_paginate
(
bucket
,
f
"query-
{
q
.
replace
(
'='
,
'-'
)
}
"
,
base
)
agg_pages
+=
p
agg_results
+=
r
return
{
"pages"
:
agg_pages
,
"results"
:
agg_results
}
@functions_framework
.
cloud_event
def
main
(
cloud_event
):
"""
Cloud Run function triggered by Pub/Sub to fetch DomainTools Iris Investigate results and write to GCS.
Args:
cloud_event: CloudEvent object containing Pub/Sub message
"""
if
not
GCS_BUCKET
:
print
(
"Error: GCS_BUCKET environment variable not set"
)
return
try
:
bucket
=
storage_client
.
bucket
(
GCS_BUCKET
)
if
USE_MODE
==
"HASH"
and
SEARCH_HASHES
:
res
=
run_hashes
(
bucket
,
SEARCH_HASHES
)
elif
USE_MODE
==
"DOMAINS"
and
DOMAINS
:
res
=
run_domains
(
bucket
,
DOMAINS
)
elif
USE_MODE
==
"QUERY"
and
QUERY_LIST
:
res
=
run_queries
(
bucket
,
QUERY_LIST
)
else
:
raise
ValueError
(
"Invalid USE_MODE or missing parameters. Set USE_MODE to HASH | DOMAINS | QUERY "
"and provide SEARCH_HASHES | DOMAINS | QUERY_LIST accordingly."
)
print
(
f
"Successfully processed:
{
json
.
dumps
({
'ok'
:
True
,
'mode'
:
USE_MODE
,
**
res
})
}
"
)
except
Exception
as
e
:
print
(
f
"Error processing DomainTools Iris data:
{
str
(
e
)
}
"
)
raise
Second file:
requirements.txt:
functions
-
framework
==
3
.*
google
-
cloud
-
storage
==
2
.*
Click
Deploy
to save and deploy the function.
Wait for deployment to complete (2-3 minutes).
Create Cloud Scheduler job
Cloud Scheduler will publish messages to the Pub/Sub topic at regular intervals, triggering the Cloud Run function.
In the
GCP Console
, go to
Cloud Scheduler
.
Click
Create Job
.
Provide the following configuration details:
Setting
Value
Name
domaintools-iris-1h
Region
Select same region as Cloud Run function
Frequency
0 * * * *
(every hour, on the hour)
Timezone
Select timezone (UTC recommended)
Target type
Pub/Sub
Topic
Select the Pub/Sub topic (
domaintools-iris-trigger
)
Message body
{}
(empty JSON object)
Click
Create
.
Schedule frequency options
Choose frequency based on log volume and latency requirements:
Frequency
Cron Expression
Use Case
Every 5 minutes
*/5 * * * *
High-volume, low-latency
Every 15 minutes
*/15 * * * *
Medium volume
Every hour
0 * * * *
Standard (recommended)
Every 6 hours
0 */6 * * *
Low volume, batch processing
Daily
0 0 * * *
Historical data collection
Test the integration
In the
Cloud Scheduler
console, find your job.
Click
Force run
to trigger the job manually.
Wait a few seconds.
Go to
Cloud Run
>
Services
.
Click on your function name (
domaintools-iris-collector
).
Click the
Logs
tab.
Verify the function executed successfully. Look for the following:
Successfully processed: {"ok": true, "mode": "HASH", "pages": X, "results": Y}
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Navigate to the prefix folder (
domaintools/iris/
).
Verify that new
.json
files were created with the current timestamp.
If you see errors in the logs:
HTTP 401
: Check DomainTools API credentials in environment variables
HTTP 403
: Verify account has required permissions for Iris Investigate API
HTTP 429
: Rate limiting - function will automatically retry with backoff
Missing environment variables
: Check all required variables are set
Invalid USE_MODE
: Verify USE_MODE is set to HASH, DOMAINS, or QUERY and corresponding parameters are provided
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Get the service account email
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
DomainTools Iris Investigate
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
DomainTools Threat Intelligence
as the
Log type
.
Click
Get Service Account
. A unique service account email is displayed, for example:
chronicle
-
12345678
@chronicle
-
gcp
-
prod
.
iam
.
gserviceaccount
.
com
Copy this email address for use it in the next step.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click your bucket name.
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email.
Assign roles
: Select
Storage Object Viewer
.
Click
Save
.
Configure a feed in Google SecOps to ingest DomainTools Iris Investigate results
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
DomainTools Iris Investigate
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
DomainTools Threat Intelligence
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI with the prefix path:
gs
:
//
domaintools
-
iris
/
domaintools
/
iris
/
Replace:
domaintools-iris
: Your GCS bucket name.
domaintools/iris/
: Optional prefix/folder path where logs are stored (leave empty for root).
Examples:
Root bucket:
gs://domaintools-iris/
With prefix:
gs://domaintools-iris/domaintools/iris/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Asset namespace
:
domaintools.threat_intel
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Supported DomainTools Iris Investigate sample logs
Standard domain enrichment (basic)
{
"domain"
:
"example-sanitized-01.com"
,
"whois_url"
:
"https://whois.domaintools.com/example-sanitized-01.com"
,
"active"
:
false
,
"admin_contact"
:
{
"name"
:
{
"value"
:
"REDACTED_NAME"
},
"org"
:
{
"value"
:
"Sanitized Corp"
},
"email"
:
[
{
"value"
:
"admin@example-sanitized.com"
}
]
},
"ip"
:
[
{
"address"
:
{
"value"
:
"192.168.1.100"
},
"asn"
:
[
{
"value"
:
12345
}
],
"isp"
:
{
"value"
:
"Generic ISP"
}
}
],
"domain_risk"
:
{
"risk_score"
:
46
,
"components"
:
[
{
"name"
:
"proximity"
,
"risk_score"
:
5
},
{
"name"
:
"threat_profile_phishing"
,
"risk_score"
:
46
}
]
},
"timestamp"
:
"2023-11-21T12:15:50.130728Z"
}
Advanced marketing/tracking schema
{
"domain"
:
"analytics-tracker-sample.com"
,
"google_analytics"
:
{
"value"
:
"UA-000000-0"
},
"ga4"
:
[
{
"value"
:
"G-YYYYYYYYYX"
}
],
"gtm_codes"
:
[
{
"value"
:
"GTM-YYYX"
}
],
"fb_codes"
:
[
{
"value"
:
"1234567890"
}
],
"baidu_codes"
:
[
{
"value"
:
"hash_masked_value"
}
],
"yandex_codes"
:
[
{
"value"
:
"98765432"
}
],
"matomo_codes"
:
[
{
"value"
:
"https://analytics.internal-sanitized.net/"
}
]
}
Tagged and monitored schema
{
"domain"
:
"monitored-threat.net"
,
"monitor_domain"
:
true
,
"monitoring_domain_list_name"
:
"Watchlist_Alpha"
,
"tags"
:
[
{
"label"
:
"Sanitized_Tag"
,
"scope"
:
"group"
,
"tagged_at"
:
"2020-12-02T13:33:40Z"
}
],
"registrar"
:
{
"value"
:
"Safe-Registrar LLC"
}
}
High-risk SSL and web response schema
{
"domain"
:
"high-risk-malware.org"
,
"domain_risk"
:
{
"risk_score"
:
100
,
"components"
:
[
{
"name"
:
"threat_profile_malware"
,
"risk_score"
:
95
}
]
},
"ssl_info"
:
[
{
"hash"
:
{
"value"
:
"sha1_masked_hash_sequence"
},
"common_name"
:
{
"value"
:
"www.sanitized-cert.com"
},
"issuer_common_name"
:
{
"value"
:
"Sanitized CA"
},
"not_after"
:
{
"value"
:
20251231
}
}
],
"website_response"
:
200
,
"server_type"
:
"Sanitized-Server-v1.0"
,
"website_title"
:
"Sanitized Landing Page"
}
UDM mapping table
Log field
UDM mapping
Logic
active
principal.domain.status
Directly mapped from the active field in the raw log.
additional_whois_email.[].value
about.labels.additional_whois_email
Extracted from additional_whois_email array and added as a label in the about object.
adsense.value
about.labels.adsense
Extracted from adsense.value and added as a label in the about object.
admin_contact.city.value
principal.domain.admin.office_address.city
Directly mapped from the admin_contact.city.value field in the raw log.
admin_contact.country.value
principal.domain.admin.office_address.country_or_region
Directly mapped from the admin_contact.country.value field in the raw log.
admin_contact.email.[].value
principal.domain.admin.email_addresses
Extracted from admin_contact.email array and added to the email_addresses field.
admin_contact.fax.value
principal.domain.admin.attribute.labels.fax
Extracted from admin_contact.fax.value and added as a label with key "fax" in the admin attribute.
admin_contact.name.value
principal.domain.admin.user_display_name
Directly mapped from the admin_contact.name.value field in the raw log.
admin_contact.org.value
principal.domain.admin.company_name
Directly mapped from the admin_contact.org.value field in the raw log.
admin_contact.phone.value
principal.domain.admin.phone_numbers
Directly mapped from the admin_contact.phone.value field in the raw log.
admin_contact.postal.value
principal.domain.admin.attribute.labels.postal
Extracted from admin_contact.postal.value and added as a label with key "postal" in the admin attribute.
admin_contact.state.value
principal.domain.admin.office_address.state
Directly mapped from the admin_contact.state.value field in the raw log.
admin_contact.street.value
principal.domain.admin.office_address.name
Directly mapped from the admin_contact.street.value field in the raw log.
alexa
about.labels.alexa
Directly mapped from the alexa field in the raw log and added as a label in the about object.
baidu_codes.[].value
about.labels.baidu_codes
Extracted from baidu_codes array and added as a label in the about object.
billing_contact.city.value
principal.domain.billing.office_address.city
Directly mapped from the billing_contact.city.value field in the raw log.
billing_contact.country.value
principal.domain.billing.office_address.country_or_region
Directly mapped from the billing_contact.country.value field in the raw log.
billing_contact.email.[].value
principal.domain.billing.email_addresses
Extracted from billing_contact.email array and added to the email_addresses field.
billing_contact.fax.value
principal.domain.billing.attribute.labels.fax
Extracted from billing_contact.fax.value and added as a label with key "fax" in the billing attribute.
billing_contact.name.value
principal.domain.billing.user_display_name
Directly mapped from the billing_contact.name.value field in the raw log.
billing_contact.org.value
principal.domain.billing.company_name
Directly mapped from the billing_contact.org.value field in the raw log.
billing_contact.phone.value
principal.domain.billing.phone_numbers
Directly mapped from the billing_contact.phone.value field in the raw log.
billing_contact.postal.value
principal.domain.billing.attribute.labels.postal
Extracted from billing_contact.postal.value and added as a label with key "postal" in the billing attribute.
billing_contact.state.value
principal.domain.billing.office_address.state
Directly mapped from the billing_contact.state.value field in the raw log.
billing_contact.street.value
principal.domain.billing.office_address.name
Directly mapped from the billing_contact.street.value field in the raw log.
create_date.value
principal.domain.creation_time
Converted to timestamp format from the create_date.value field in the raw log.
data_updated_timestamp
principal.domain.audit_update_time
Converted to timestamp format from the data_updated_timestamp field in the raw log.
domain
principal.hostname
Directly mapped from the domain field in the raw log.
domain_risk.components.[].evidence
security_result.detection_fields.evidence
Extracted from domain_risk.components.[].evidence array and added as a detection field with key "evidence" in the security_result object.
domain_risk.components.[].name
security_result.category_details
Directly mapped from the domain_risk.components.[].name field in the raw log.
domain_risk.components.[].risk_score
security_result.risk_score
Directly mapped from the domain_risk.components.[].risk_score field in the raw log.
domain_risk.components.[].threats
security_result.threat_name
The first element of the domain_risk.components.[].threats array is mapped to security_result.threat_name.
domain_risk.components.[].threats
security_result.detection_fields.threats
The remaining elements of the domain_risk.components.[].threats array are added as detection fields with key "threats" in the security_result object.
domain_risk.risk_score
security_result.risk_score
Directly mapped from the domain_risk.risk_score field in the raw log.
email_domain.[].value
about.labels.email_domain
Extracted from email_domain array and added as a label in the about object.
expiration_date.value
principal.domain.expiration_time
Converted to timestamp format from the expiration_date.value field in the raw log.
fb_codes.[].value
about.labels.fb_codes
Extracted from fb_codes array and added as a label in the about object.
first_seen.value
principal.domain.first_seen_time
Converted to timestamp format from the first_seen.value field in the raw log.
ga4.[].value
about.labels.ga4
Extracted from ga4 array and added as a label in the about object.
google_analytics.value
about.labels.google_analytics
Extracted from google_analytics.value and added as a label in the about object.
gtm_codes.[].value
about.labels.gtm_codes
Extracted from gtm_codes array and added as a label in the about object.
hotjar_codes.[].value
about.labels.hotjar_codes
Extracted from hotjar_codes array and added as a label in the about object.
ip.[].address.value
principal.ip
The first element of the ip array is mapped to principal.ip.
ip.[].address.value
about.labels.ip_address
The remaining elements of the ip array are added as labels with key "ip_address" in the about object.
ip.[].asn.[].value
network.asn
The first element of the first ip.asn array is mapped to network.asn.
ip.[].asn.[].value
about.labels.asn
The remaining elements of the ip.asn arrays are added as labels with key "asn" in the about object.
ip.[].country_code.value
principal.location.country_or_region
The country_code.value of the first element in the ip array is mapped to principal.location.country_or_region.
ip.[].country_code.value
about.location.country_or_region
The country_code.value of the remaining elements in the ip array are mapped to about.location.country_or_region.
ip.[].isp.value
principal.labels.isp
The isp.value of the first element in the ip array is mapped to principal.labels.isp.
ip.[].isp.value
about.labels.isp
The isp.value of the remaining elements in the ip array are mapped to about.labels.isp.
matomo_codes.[].value
about.labels.matomo_codes
Extracted from matomo_codes array and added as a label in the about object.
monitor_domain
about.labels.monitor_domain
Directly mapped from the monitor_domain field in the raw log and added as a label in the about object.
monitoring_domain_list_name
about.labels.monitoring_domain_list_name
Directly mapped from the monitoring_domain_list_name field in the raw log and added as a label in the about object.
mx.[].domain.value
about.domain.name
Directly mapped from the mx.[].domain.value field in the raw log.
mx.[].host.value
about.hostname
Directly mapped from the mx.[].host.value field in the raw log.
mx.[].ip.[].value
about.ip
Extracted from mx.[].ip array and added to the ip field.
mx.[].priority
about.security_result.priority_details
Directly mapped from the mx.[].priority field in the raw log.
name_server.[].domain.value
about.labels.name_server_domain
Extracted from name_server.[].domain.value and added as a label with key "name_server_domain" in the about object.
name_server.[].host.value
principal.domain.name_server
Extracted from name_server.[].host.value and added to the name_server field.
name_server.[].host.value
about.domain.name_server
Extracted from name_server.[].host.value and added to the name_server field.
name_server.[].ip.[].value
about.labels.ip
Extracted from name_server.[].ip array and added as a label with key "ip" in the about object.
popularity_rank
about.labels.popularity_rank
Directly mapped from the popularity_rank field in the raw log and added as a label in the about object.
redirect.value
about.labels.redirect
Extracted from redirect.value and added as a label in the about object.
redirect_domain.value
about.labels.redirect_domain
Extracted from redirect_domain.value and added as a label in the about object.
registrant_contact.city.value
principal.domain.registrant.office_address.city
Directly mapped from the registrant_contact.city.value field in the raw log.
registrant_contact.country.value
principal.domain.registrant.office_address.country_or_region
Directly mapped from the registrant_contact.country.value field in the raw log.
registrant_contact.email.[].value
principal.domain.registrant.email_addresses
Extracted from registrant_contact.email array and added to the email_addresses field.
registrant_contact.fax.value
principal.domain.registrant.attribute.labels.fax
Extracted from registrant_contact.fax.value and added as a label with key "fax" in the registrant attribute.
registrant_contact.name.value
principal.domain.registrant.user_display_name
Directly mapped from the registrant_contact.name.value field in the raw log.
registrant_contact.org.value
principal.domain.registrant.company_name
Directly mapped from the registrant_contact.org.value field in the raw log.
registrant_contact.phone.value
principal.domain.registrant.phone_numbers
Directly mapped from the registrant_contact.phone.value field in the raw log.
registrant_contact.postal.value
principal.domain.registrant.attribute.labels.postal
Extracted from registrant_contact.postal.value and added as a label with key "postal" in the registrant attribute.
registrant_contact.state.value
principal.domain.registrant.office_address.state
Directly mapped from the registrant_contact.state.value field in the raw log.
registrant_contact.street.value
principal.domain.registrant.office_address.name
Directly mapped from the registrant_contact.street.value field in the raw log.
registrant_name.value
about.labels.registrant_name
Extracted from registrant_name.value and added as a label in the about object.
registrant_org.value
about.labels.registrant_org
Extracted from registrant_org.value and added as a label in the about object.
registrar.value
principal.domain.registrar
Directly mapped from the registrar.value field in the raw log.
registrar_status
about.labels.registrar_status
Extracted from registrar_status array and added as a label in the about object.
server_type
network.tls.client.server_name
Directly mapped from the server_type field in the raw log.
soa_email.[].value
principal.user.email_addresses
Extracted from soa_email array and added to the email_addresses field.
spf_info
about.labels.spf_info
Directly mapped from the spf_info field in the raw log and added as a label in the about object.
ssl_email.[].value
about.labels.ssl_email
Extracted from ssl_email array and added as a label in the about object.
ssl_info.[].alt_names.[].value
about.labels.alt_names
Extracted from ssl_info.[].alt_names array and added as a label in the about object.
ssl_info.[].common_name.value
about.labels.common_name
Extracted from ssl_info.[].common_name.value and added as a label in the about object.
ssl_info.[].duration.value
about.labels.duration
Extracted from ssl_info.[].duration.value and added as a label in the about object.
ssl_info.[].email.[].value
about.labels.ssl_info_email
Extracted from ssl_info.[].email array and added as a label with key "ssl_info_email" in the about object.
ssl_info.[].hash.value
network.tls.server.certificate.sha1
The hash.value of the first element in the ssl_info array is mapped to network.tls.server.certificate.sha1.
ssl_info.[].hash.value
about.labels.hash
The hash.value of the remaining elements in the ssl_info array are mapped to about.labels.hash.
ssl_info.[].issuer_common_name.value
network.tls.server.certificate.issuer
The issuer_common_name.value of the first element in the ssl_info array is mapped to network.tls.server.certificate.issuer.
ssl_info.[].issuer_common_name.value
about.labels.issuer_common_name
The issuer_common_name.value of the remaining elements in the ssl_info array are mapped to about.labels.issuer_common_name.
ssl_info.[].not_after.value
network.tls.server.certificate.not_after
The not_after.value of the first element in the ssl_info array is converted to timestamp format and mapped to network.tls.server.certificate.not_after.
ssl_info.[].not_after.value
about.labels.not_after
The not_after.value of the remaining elements in the ssl_info array are mapped to about.labels.not_after.
ssl_info.[].not_before.value
network.tls.server.certificate.not_before
The not_before.value of the first element in the ssl_info array is converted to timestamp format and mapped to network.tls.server.certificate.not_before.
ssl_info.[].not_before.value
about.labels.not_before
The not_before.value of the remaining elements in the ssl_info array are mapped to about.labels.not_before.
ssl_info.[].organization.value
network.organization_name
The organization.value of the first element in the ssl_info array is mapped to network.organization_name.
ssl_info.[].organization.value
about.labels.organization
The organization.value of the remaining elements in the ssl_info array are mapped to about.labels.organization.
ssl_info.[].subject.value
about.labels.subject
Extracted from ssl_info.[].subject.value and added as a label in the about object.
statcounter_project_codes.[].value
about.labels.statcounter_project_codes
Extracted from statcounter_project_codes array and added as a label in the about object.
statcounter_security_codes.[].value
about.labels.statcounter_security_codes
Extracted from statcounter_security_codes array and added as a label in the about object.
tags.[].label
about.file.tags
Extracted from tags.[].label and added to the tags field.
tags.[].scope
security_result.detection_fields.scope
Extracted from tags.[].scope and added as a detection field with key "scope" in the security_result object.
tags.[].tagged_at
security_result.detection_fields.tagged_at
Extracted from tags.[].tagged_at and added as a detection field with key "tagged_at" in the security_result object.
technical_contact.city.value
principal.domain.tech.office_address.city
Directly mapped from the technical_contact.city.value field in the raw log.
technical_contact.country.value
principal.domain.tech.office_address.country_or_region
Directly mapped from the technical_contact.country.value field in the raw log.
technical_contact.email.[].value
principal.domain.tech.email_addresses
Extracted from technical_contact.email array and added to the email_addresses field.
technical_contact.fax.value
principal.domain.tech.attribute.labels.fax
Extracted from technical_contact.fax.value and added as a label with key "fax" in the tech attribute.
technical_contact.name.value
principal.domain.tech.user_display_name
Directly mapped from the technical_contact.name.value field in the raw log.
technical_contact.org.value
principal.domain.tech.company_name
Directly mapped from the technical_contact.org.value field in the raw log.
technical_contact.phone.value
principal.domain.tech.phone_numbers
Directly mapped from the technical_contact.phone.value field in the raw log.
technical_contact.postal.value
principal.domain.tech.attribute.labels.postal
Extracted from technical_contact.postal.value and added as a label with key "postal" in the tech attribute.
technical_contact.state.value
principal.domain.tech.office_address.state
Directly mapped from the technical_contact.state.value field in the raw log.
technical_contact.street.value
principal.domain.tech.office_address.name
Directly mapped from the technical_contact.street.value field in the raw log.
tld
about.labels.tld
Directly mapped from the tld field in the raw log and added as a label in the about object.
timestamp
about.labels.timestamp
Directly mapped from the timestamp field in the raw log and added as a label in the about object.
website_response
principal.network.http.response_code
Directly mapped from the website_response field in the raw log.
website_title
about.labels.website_title
Directly mapped from the website_title field in the raw log and added as a label in the about object.
whois_url
principal.domain.whois_server
Directly mapped from the whois_url field in the raw log.
yandex_codes.[].value
about.labels.yandex_codes
Extracted from yandex_codes array and added as a label in the about object.
edr.client.hostname
Set to the value of the domain field.
edr.client.ip_addresses
Set to the value of the first element in the ip array, specifically ip.[0].address.value.
edr.raw_event_name
Set to "STATUS_UPDATE" if principal.hostname is present, otherwise set to "GENERIC_EVENT".
metadata.event_timestamp
Copied from the top-level create_time field in the raw log.
metadata.event_type
Set to "STATUS_UPDATE" if principal.hostname is present, otherwise set to "GENERIC_EVENT".
metadata.log_type
Set to "DOMAINTOOLS_THREATINTEL".
metadata.product_name
Set to "DOMAINTOOLS".
metadata.vendor_name
Set to "DOMAINTOOLS".
Need more help?
Get answers from Community members and Google SecOps professionals.
