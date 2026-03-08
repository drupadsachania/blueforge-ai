# Collect Crowdstrike IOC logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/crowdstrike-ioc/  
**Scraped:** 2026-03-05T09:22:43.365935Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Crowdstrike IOC logs
Supported in:
Google secops
SIEM
This document explains how to collect CrowdStrike IOC logs using the CrowdStrike Chronicle Intel Bridge, a Docker container that forwards threat intelligence indicators from CrowdStrike Falcon Intelligence to Google Security Operations.
CrowdStrike Falcon Intelligence provides threat intelligence indicators, including domains, IP addresses, file hashes, URLs, email addresses, file paths, file names, and mutex names. The Chronicle Intel Bridge polls the CrowdStrike Intel API and forwards these indicators to Google Security Operations for threat detection and analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
Privileged access to the CrowdStrike Falcon Console with permissions to create API clients
CrowdStrike Falcon Intelligence subscription
Docker installed on a system that can run continuously to poll CrowdStrike and forward indicators
All systems in the deployment architecture are configured in the UTC time zone
Get Google SecOps credentials
Get Google SecOps customer ID
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy and save the
Customer ID
from the
Organization Details
section.
Download Google SecOps service account file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Click
Download Ingestion Authentication File
.
Save the JSON file to a secure location on the system where you will run the Docker container (for example,
/path/to/service-account.json
).
Configure CrowdStrike Falcon API access
To enable the Chronicle Intel Bridge to retrieve indicators, you need to create an API client with read permissions for Falcon Intelligence Indicators.
Create API client
Sign in to the
CrowdStrike Falcon Console
.
Go to
Support and resources
>
Resources and tools
>
API Clients and Keys
.
Click
Add new API client
.
Provide the following configuration details:
Client name
: Enter a descriptive name (for example,
Chronicle Intel Bridge
).
Description
: Optional: Enter
Integration with Google Chronicle for threat intelligence indicators
.
In the
API scopes
section, select the
Read
checkbox next to
Indicators (Falcon Intelligence)
.
Click
Create
.
Record API credentials
After creating the API client, a dialog displays your credentials:
Client ID
: Your unique client identifier (for example,
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
)
Client Secret
: Your API secret key
Base URL
: The fully qualified domain name for your region (for example,
api.us-2.crowdstrike.com
)
Regional endpoints
CrowdStrike Falcon uses different API endpoints based on your cloud region:
Region
Base URL
Console URL
US-1
api.crowdstrike.com
https://falcon.crowdstrike.com
US-2
api.us-2.crowdstrike.com
https://falcon.us-2.crowdstrike.com
EU-1
api.eu-1.crowdstrike.com
https://falcon.eu-1.crowdstrike.com
US-GOV-1
api.laggar.gcw.crowdstrike.com
https://falcon.laggar.gcw.crowdstrike.com
US-GOV-2
api.us-gov-2.crowdstrike.com
https://falcon.us-gov-2.crowdstrike.com
Use the base URL that corresponds to your CrowdStrike Falcon instance region. The region code (for example,
us-1
,
us-2
,
eu-1
) is used in the Docker configuration.
Deploy the CrowdStrike Chronicle Intel Bridge
The Chronicle Intel Bridge is a Docker container that runs continuously to poll CrowdStrike Falcon Intelligence for indicators and forward them to Google Security Operations.
Set environment variables
Before running the Docker container, set the following environment variables with the credentials you collected:
export
FALCON_CLIENT_ID
=
"your-client-id"
export
FALCON_CLIENT_SECRET
=
"your-client-secret"
export
FALCON_CLOUD_REGION
=
"your-cloud-region"
export
CHRONICLE_CUSTOMER_ID
=
"your-customer-id"
export
CHRONICLE_REGION
=
"your-chronicle-region"
Replace the placeholder values:
your-client-id
: The Client ID from the CrowdStrike API client
your-client-secret
: The Client Secret from the CrowdStrike API client
your-cloud-region
: Your CrowdStrike cloud region (for example,
us-1
,
us-2
,
eu-1
,
us-gov-1
,
us-gov-2
)
your-customer-id
: Your Google SecOps Customer ID
your-chronicle-region
: Your Google SecOps region (see Chronicle region configuration below)
Chronicle region configuration
The
CHRONICLE_REGION
environment variable specifies which Google SecOps regional endpoint to use. The following values are supported:
Legacy region codes:
US
(default if not specified)
EU
UK
IL
AU
SG
Google Cloud region codes:
EUROPE
EUROPE-WEST2
EUROPE-WEST3
EUROPE-WEST6
EUROPE-WEST9
EUROPE-WEST12
ME-WEST1
ME-CENTRAL1
ME-CENTRAL2
ASIA-SOUTH1
ASIA-SOUTHEAST1
ASIA-NORTHEAST1
AUSTRALIA-SOUTHEAST1
SOUTHAMERICA-EAST1
NORTHAMERICA-NORTHEAST2
Run the Docker container
Choose one of the following deployment methods:
Interactive mode (foreground):
Use this mode for testing and troubleshooting:
docker
run
-it
--rm
\
--name
chronicle-intel-bridge
\
-e
FALCON_CLIENT_ID
=
"
$FALCON_CLIENT_ID
"
\
-e
FALCON_CLIENT_SECRET
=
"
$FALCON_CLIENT_SECRET
"
\
-e
FALCON_CLOUD_REGION
=
"
$FALCON_CLOUD_REGION
"
\
-e
CHRONICLE_CUSTOMER_ID
=
"
$CHRONICLE_CUSTOMER_ID
"
\
-e
CHRONICLE_REGION
=
"
$CHRONICLE_REGION
"
\
-e
GOOGLE_SERVICE_ACCOUNT_FILE
=
/gcloud/sa.json
\
-v
/path/to/your/service-account.json:/gcloud/sa.json:ro
\
quay.io/crowdstrike/chronicle-intel-bridge:latest
Detached mode (background with restart policy):
Use this mode for production deployment:
docker
run
-d
--restart
unless-stopped
\
--name
chronicle-intel-bridge
\
-e
FALCON_CLIENT_ID
=
"
$FALCON_CLIENT_ID
"
\
-e
FALCON_CLIENT_SECRET
=
"
$FALCON_CLIENT_SECRET
"
\
-e
FALCON_CLOUD_REGION
=
"
$FALCON_CLOUD_REGION
"
\
-e
CHRONICLE_CUSTOMER_ID
=
"
$CHRONICLE_CUSTOMER_ID
"
\
-e
CHRONICLE_REGION
=
"
$CHRONICLE_REGION
"
\
-e
GOOGLE_SERVICE_ACCOUNT_FILE
=
/gcloud/sa.json
\
-v
/path/to/your/service-account.json:/gcloud/sa.json:ro
\
quay.io/crowdstrike/chronicle-intel-bridge:latest
Replace
/path/to/your/service-account.json
with the actual path to the Google SecOps service account JSON file you downloaded earlier.
Verify the deployment
After starting the container, verify that indicators are being forwarded to Google Security Operations:
Check the container logs:
docker
logs
chronicle-intel-bridge
In the Google SecOps console, search for events with the log type
CROWDSTRIKE_IOC
.
Verify that indicator data is appearing in your Google SecOps instance.
Advanced configuration
For advanced configuration options, you can customize the Intel Bridge behavior using a configuration file.
Download the
config.ini
file from the
CrowdStrike Chronicle Intel Bridge repository
.
Modify the configuration file according to your requirements.
Mount the configuration file to the container using the volume flag:
docker
run
-d
--restart
unless-stopped
\
--name
chronicle-intel-bridge
\
-e
FALCON_CLIENT_ID
=
"
$FALCON_CLIENT_ID
"
\
-e
FALCON_CLIENT_SECRET
=
"
$FALCON_CLIENT_SECRET
"
\
-e
FALCON_CLOUD_REGION
=
"
$FALCON_CLOUD_REGION
"
\
-e
CHRONICLE_CUSTOMER_ID
=
"
$CHRONICLE_CUSTOMER_ID
"
\
-e
CHRONICLE_REGION
=
"
$CHRONICLE_REGION
"
\
-e
GOOGLE_SERVICE_ACCOUNT_FILE
=
/gcloud/sa.json
\
-v
/path/to/your/service-account.json:/gcloud/sa.json:ro
\
-v
/path/to/your/config.ini:/ccib/config.ini:ro
\
quay.io/crowdstrike/chronicle-intel-bridge:latest
Supported indicator types
The CrowdStrike Indicator of Compromise (IoC) parser supports the following indicator types:
Indicator Type
Description
domain
Domain names associated with malicious activity
email_address
Email addresses used in attacks
file_name
Malicious file names
file_path
File system paths associated with threats
hash_md5
MD5 file hashes
hash_sha1
SHA-1 file hashes
hash_sha256
SHA-256 file hashes
ip_address
IP addresses associated with malicious activity
mutex_name
Mutex names used by malware
url
URLs associated with threats
Manage the Docker container
Use the following Docker commands to manage the Chronicle Intel Bridge:
View container status:
docker
ps
-a
|
grep
chronicle-intel-bridge
View container logs:
docker
logs
chronicle-intel-bridge
Follow container logs in real-time:
docker
logs
-f
chronicle-intel-bridge
Stop the container:
docker
stop
chronicle-intel-bridge
Start the container:
docker
start
chronicle-intel-bridge
Restart the container:
docker
restart
chronicle-intel-bridge
Remove the container:
docker
stop
chronicle-intel-bridge
docker
rm
chronicle-intel-bridge
Troubleshooting
If you encounter issues with the Chronicle Intel Bridge:
Verify that the CrowdStrike API credentials are correct and have the
Indicators (Falcon Intelligence): READ
scope.
Verify that the Google SecOps Customer ID is correct.
Verify that the Google SecOps service account JSON file is valid and accessible to the Docker container.
Verify that the CrowdStrike cloud region is correct (for example,
us-1
,
us-2
,
eu-1
).
Verify that the Google SecOps region is correct.
Check the container logs for error messages:
docker
logs
chronicle-intel-bridge
Verify network connectivity from the Docker host to both CrowdStrike API endpoints and Google SecOps ingestion endpoints.
UDM mapping table
Log Field
UDM Mapping
Logic
when
metadata.event_timestamp
Value copied directly
messageid
metadata.id
Value copied directly
protocol
network.ip_protocol
Value copied directly
deviceName
principal.hostname
Value copied directly
srcAddr
principal.ip
Value copied directly
srcPort
principal.port
Value copied directly
action
security_result.action
Value copied directly
dstAddr
target.ip
Value copied directly
dstPort
target.port
Value copied directly
Need more help?
Get answers from Community members and Google SecOps professionals.
