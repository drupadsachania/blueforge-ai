# Collect Jamf Threat Events logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/jamf-threat-events/  
**Scraped:** 2026-03-05T09:48:21.091677Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Jamf Threat Events logs
Supported in:
Google secops
SIEM
This document describes how you can collect Jamf Threat Events logs by setting up a Google Security Operations
feed and how log fields map to Google SecOps Unified Data Model (UDM) fields.
This document also lists the supported Jamf Threat Events version.
For more information, see
Data ingestion to Google SecOps
.
A typical deployment consists of Jamf Threat Events and the Google SecOps feed configured to send logs to Google SecOps. Each customer deployment can differ and might be more
complex.
The deployment contains the following components:
Jamf Protect
: The Jamf Protect platform, configured with Jamf Security Cloud, where you collect network threat logs.
Google SecOps feed
: The Google SecOps feed that fetches logs from Jamf Protect and writes logs to Google SecOps.
Google SecOps
: Google SecOps retains and analyzes the logs from Jamf Protect.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
JAMF_THREAT_EVENTS
ingestion label.
Before you begin
Ensure you have the following prerequisites:
A
Jamf Protect Telemetry
set up
Jamf Protect version 4.0.0 or later
All systems in the deployment architecture are configured with the UTC time zone.
Set up feeds from SIEM Settings
>
Feeds
You can use either Amazon S3 V2 or a webhook to set up an ingestion feed in Google SecOps.
Set up an ingestion feed using Amazon S3 V2
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
JAMF
feed pack.
Locate the
Jamf Protect Threat Events
feed.
Select
Amazon S3 V2
as the
Source Type
.
Specify the values for the following fields.
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Includes files modified in the last number of days. Default is 180 days.
Access Key ID
: The user's access key with permissions to read from the S3 bucket.
Secret Access Key
: The user's secret key with permissions to read from the S3 bucket.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
:
Namespace associated with the feed
.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create Feed
.
Set up an ingestion feed using a webhook
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click the
JAMF
feed pack.
Locate the
Jamf Protect Threat Events
feed.
In the
Source Type
list, select
Webhook
..
Specify values for the following fields
Split delimiter
: The delimiter that is used to separate log lines, such as
\n
.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Create Feed
.
To configure multiple feeds for different log types within this product family, see
Configure feeds by product
.
Create an API key for a webhook feed
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
Set up Jamf Security Cloud for a webhook feed
In the Jamf Security Cloud application, go to
Integrations
>
Data Streams
.
Click
New Configuration
.
Select
Threat Events
>
Generic HTTP
>
Continue
.
In the
HTTP Connection Configuration
section, select
https
as the default protocol.
Enter your server hostname in the
Server Hostname/IP
field, such as
us-chronicle.googleapis.com
.
Enter your server port in the
Port
field, such as
443
.
Enter your web endpoint in the
Endpoint
field. (This is the
Endpoint Information
field that you copied from the webhook feed setup. It's already in the required format.)
In the
Additional headers
section, enter the following settings, where each header is a custom, case-sensitive header that you manually enter:
Header name:
X-goog-api-key
and click
Create option X-goog-api-key
Header value insert:
API_KEY
(The API key to authenticate to Google SecOps.)
Header name:
X-Webhook-Access-Key
and click
Create option X-Webhook-Access-Key
Header value insert:
SECRET
(The secret key that you generated to authenticate the feed.)
Click
Test Configuration
.
If successful, click
Create Configuration
.
For more information about Google SecOps feeds, see
Create and manage feeds using the feed management UI
. For information about requirements for each
feed type, see
Feed configuration API
.
Supported Jamf Threat Events log formats
The Jamf Threat Events parser supports logs in JSON format.
Supported Jamf Threat Events sample logs
JSON
{
  "event": {
    "metadata": {
      "schemaVersion": "1.0",
      "vendor": "Jamf",
      "product": "Threat Events Stream"
    },
    "timestamp": "2023-01-11T13:10:40.410Z",
    "alertId": "debd2e4b-9da1-454e-952d-18a00b42ffce",
    "account": {
      "customerId": "dummycustomerid",
      "parentId": "dummyparentid",
      "name": "Jamf Internal Test Accounts (root) - Jamf - CE Security Team"
    },
    "device": {
      "deviceId": "e9671102-5ccf-4e66-a6b3-b117ba257d5f",
      "os": "UNKNOWN 13.2.1",
      "deviceName": "Mac (13.2.1)",
      "userDeviceName": "darrow",
      "externalId": "0c221ae4-50af-5e39-8275-4424cc87ab8e"
    },
    "eventType": {
      "id": "303",
      "description": "Risky Host/Domain - Malware",
      "name": "ACCESS_BAD_HOST"
    },
    "app": {
      "id": "ru.freeapps.calc",
      "name": "MyFreeCalculator",
      "version": "10.4",
      "sha1": "c3499c2729730a7f807efb8676a92dcb6f8a3f8f",
      "sha256": "50d858e0985ecc7f60418aaf0cc5ab587f42c2570a884095a9e8ccacd0f6545"
    },
    "destination": {
      "name": "dummy.domain.org",
      "ip": "0000:1111:2222:3333:4444:5",
      "port": "80"
    },
    "source": {
      "ip": "198.51.100.1",
      "port": "243"
    },
    "location": "GB",
    "accessPoint": null,
    "accessPointBssid": "23:8f:cf:00:9d:23",
    "severity": 8,
    "user": {
      "email": "test.user@domain.io",
      "name": "Test User"
    },
    "eventUrl": "dummy.domain.com",
    "action": "Blocked"
  }
}
Field mapping reference
The following table explains how the Google SecOps parser maps Jamf Threat Events logs fields to Google SecOps Unified Data Model (UDM) fields.
Field mapping reference: Event Identifier to Event Type
The following table lists the
JAMF_THREAT_EVENTS
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
MALICIOUS_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
ADWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
BANKER_MALWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
POTENTIALLY_UNWANTED_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
RANSOMWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
ROOTING_MALWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
SMS_MALWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
SPYWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
TROJAN_MALWARE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
THIRD_PARTY_APP_STORES_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
ADMIN_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
SIDE_LOADED_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
VULNERABLE_APP_IN_INVENTORY
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS, SOFTWARE_PUA
SSL_TRUST_COMPROMISE
SCAN_NETWORK
NETWORK_SUSPICIOUS
JAILBREAK
SCAN_UNCATEGORIZED
EXPLOIT
IOS_PROFILE
SCAN_UNCATEGORIZED
OUTDATED_OS
SCAN_VULN_HOST
SOFTWARE_MALICIOUS
OUTDATED_OS_LOW
SCAN_VULN_HOST
SOFTWARE_MALICIOUS
OUT_OF_DATE_OS
SCAN_UNCATEGORIZED
LOCK_SCREEN_DISABLED
SCAN_UNCATEGORIZED
STORAGE_ENCRYPTION_DISABLED
SCAN_UNCATEGORIZED
UNKNOWN_SOURCES_ENABLED
SCAN_UNCATEGORIZED
DEVELOPER_MODE_ENABLED
SCAN_UNCATEGORIZED
USB_DEBUGGING_ENABLED
SCAN_UNCATEGORIZED
USB_APP_VERIFICATION_DISABLED
SCAN_UNCATEGORIZED
FIREWALL_DISABLED
SCAN_UNCATEGORIZED
POLICY_VIOLATION
USER_PASSWORD_DISABLED
SCAN_UNCATEGORIZED
ANTIVIRUS_DISABLED
SCAN_UNCATEGORIZED
APP_INACTIVITY
SCAN_UNCATEGORIZED
MISSING_ANDROID_SECURITY_PATCHES
SCAN_UNCATEGORIZED
ACCESS_SPAM_HOST
SCAN_HOST
NETWORK_SUSPICIOUS
ACCESS_PHISHING_HOST
SCAN_HOST
PHISHING
ACCESS_BAD_HOST
SCAN_HOST
NETWORK_MALICIOUS
RISKY_APP_DOWNLOAD
SCAN_UNCATEGORIZED
SOFTWARE_SUSPICIOUS
ACCESS_CRYPTOJACKING_HOST
SCAN_HOST
NETWORK_SUSPICIOUS
SSL_MITM_TRUSTED_VALID_CERT
SCAN_NETWORK
NETWORK_SUSPICIOUS
SSL_MITM_UNTRUSTED_VALID_CERT
SCAN_NETWORK
NETWORK_SUSPICIOUS
SSL_STRIP_MITM
SCAN_NETWORK
NETWORK_MALICIOUS
SSL_MITM_UNTRUSTED_INVALID_CERT
SCAN_NETWORK
NETWORK_MALICIOUS
SSL_MITM_TRUSTED_INVALID_CERT
SCAN_NETWORK
NETWORK_MALICIOUS
LEAK_CREDIT_CARD
SCAN_UNCATEGORIZED
ACL_VIOLATION
LEAK_PASSWORD
SCAN_UNCATEGORIZED
ACL_VIOLATION
LEAK_EMAIL
SCAN_UNCATEGORIZED
ACL_VIOLATION
LEAK_USERID
SCAN_UNCATEGORIZED
ACL_VIOLATION
LEAK_LOCATION
SCAN_UNCATEGORIZED
ACL_VIOLATION
Field mapping reference: JAMF_THREAT_EVENTS
The following table lists the log fields of the
JAMF_THREAT_EVENTS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
event.account.parentId
about.resource_ancestors.product_object_id
event.account.name
about.resource.name
event.account.customerId
about.resource.product_object_id
event.timestamp
metadata.event_timestamp
event.eventType.name
metadata.product_event_type
event.alertId
metadata.product_log_id
event.metadata.product
metadata.product_name
event.metadata.vendor
metadata.vendor_name
event.source.port
princiap.port
event.device.deviceName
principal.asset.assetid
event.location
principal.asset.location.country_or_region
principal.asset.platform_software.platform
The platform_name
is extracted from the
event.device.deviceName
log field using a Grok pattern.
If the
platform_name
value is equal to
Mac
, then the
principal.asset.platform_software.platform
UDM field is set to
MAC
.
event.device.os
principal.asset.platform_software.platform_version
event.device.deviceId
principal.asset.product_object_id
event.source.ip
principal.ip
event.accessPointBssid
principal.mac
event.user.email
principal.user.email_addresses
event.user.name
principal.user.user_display_name
sourceUserName
principal.user.user_display_name
event.device.externalId
principal.asset.attribute.labels [event_device_externalId]
event.device.userDeviceName
principal.asset.attribute.labels [event_device_userDeviceName]
event.accessPoint
principal.labels [event_accessPoint]
event.action
security_result.action
The
security_result.action
UDM field is set to one of the following values:
ALLOW
if the
event.action
log field value is equal to
Resolved
or
Detected
.
BLOCK
if the
event.action
log field value is equal to
Blocked
.
event.action
security_result.action_details
event.eventType.name
security_result.category_details
event.eventType.description
security_result.description
event.severity
security_result.severity_details
event.eventType.id
security_result.threat_id
event.eventType.name
security_result.threat_name
event.eventUrl
security_result.url_back_to_product
event.destination.port
target.port
event.app.name
target.application
event.app.name
target.file.full_path
event.app.sha1
target.file.sha1
event.app.sha256
target.file.sha256
event.destination.ip
target.ip
event.destination.name
target.url
event.app.version
target.labels [event_app_version]
event.app.id
target.labels [event_app_id]
event.metadata.schemaVersion
about.labels [event_metadata_schemaVersion]
What's next
Data ingestion to Google SecOps
Need more help?
Get answers from Community members and Google SecOps professionals.
