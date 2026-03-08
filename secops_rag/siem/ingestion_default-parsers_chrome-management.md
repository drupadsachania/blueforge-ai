# Collect Chrome Enterprise data

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chrome-management/  
**Scraped:** 2026-03-05T09:16:53.408975Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Chrome Enterprise data
Supported in:
Google secops
SIEM
This document describes how to collect Google Chrome logs into
Google SecOps using the Enterprise reporting connector. It
details the data ingestion process for both Google Chrome Enterprise Core and
Chrome Enterprise Premium deployments, while noting that some advanced log data
requires a Chrome Enterprise Premium license.
Typical deployment
A typical deployment consists of a combination of the following components:
Chrome
: The Chrome browser and ChromeOS management events that you want to collect.
ChromeOS
: You can configure ChromeOS managed devices to send logs to Google SecOps. ChromeOS devices are optional.
Chrome Enterprise reporting connector
: The Chrome Enterprise reporting connector forwards Chrome logs to Google SecOps.
Google SecOps
: Retains and analyzes Chrome logs.
Before you begin
A Google Workspace Administrator account.
Google Chrome 137 or later. Earlier versions don't provide complete referrer URL data.
Chrome Enterprise Premium licenses for advanced features.
Optional: A Google SecOps ingestion token. If using this option, you also need your Google Workspace
Customer ID
from the Google Workspace Admin console.
Optional: A
Chronicle Ingestion API key
provided by your Google SecOps representative.
Set up Chrome browser cloud management
Enroll the target devices to enable cloud management of Chrome browsers. For details, see
Enroll cloud-managed Chrome browsers
.
Optional: Configure
Evidence Locker
for investigation of suspicious files. (Chrome Enterprise Premium only)
Optional: If you use Identity-Aware Proxy, perform the steps in
Collect Chrome Enterprise Premium Context Access Aware Data
to integrate this data into Google SecOps.
Connect Chrome data to your Google SecOps instance
Configure the Chrome Management parser and the Chrome Enterprise reporting connector.
Configure the Chrome Management parser
You may need to update to a new version of the Chrome Management parser to support recent Chrome logs.
In your Google SecOps instance, go to
Menu
>
Settings
>
Parsers
.
Find the Chrome Management prebuilt entry and verify that you are using a version date
2025-08-14
or newer by applying any pending updates.
Configure Chrome Enterprise Premium
This section describes how to set up logging for Chrome Enterprise Premium.
You can configure log forwarding for Chrome Enterprise Premium that includes context from Safe Browsing. The Chrome Enterprise reporting connector for Chrome Enterprise Premium can configure, and optionally forward the following log types:
Browser crashes
Content transfers
Data access controls
Extension installations
Extension telemetry
Google login activity
Malware transfer
Password breach
Password changed
Password reuse
Sensitive data transfer
Suspicious URL
Unsafe site visits
URL filtering interstitial
URL navigations
Set up the Chrome Enterprise Premium data for export
To configure the Chrome Enterprise reporting connector for Chrome Enterprise Premium logging using the recommended security settings:
In the Google Admin console, go to
Menu > Chrome browser > Connectors
.
In the
Introducing Google SecOps for Chrome Enterprise Data
banner, click
View Details & Enable
.
On the
Enable Google SecOps for Chrome Enterprise Premium
page, enter a
Configuration name
.
Select a forwarding option, as described in
Configure the Chrome Enterprise reporting connector
.
Configure the Chrome Enterprise reporting connector
The Chrome Enterprise reporting connector sends log data to Google SecOps for both Chrome Enterprise Premium and Chrome Enterprise Core.
Configure the Chrome Enterprise reporting connector to send Chrome data to Google SecOps using one of the following options:
If you've previously configured Google Cloud Audit Logs to forward to a Google SecOps, you may have an option to send Chrome Enterprise Premium logs. For details, see
Configure Chrome Forwarding to a Google SecOps instance in the same organization
.
You can use a temporary token code generated from Google SecOps to configure forwarding to a Chrome Enterprise Premium instance. For details, see
Configure Chrome Forwarding to Google SecOps using an integration token
.
Alternatively, you can use a Chronicle Ingestion API key. For details, see
Configure Chrome Forwarding to Google SecOps using the Chronicle Ingestion API
.
Configure Chrome Forwarding to a Google SecOps instance in the same organization
You may have an option to select an existing Google SecOps instance in the connector configuration if all of the following prerequisites are satisfied:
The Google SecOps instance is connected to a Google Cloud project.
The Google Cloud project is within the same organization as the Google Workspace managing your Chrome Enterprise Premium.
You previously configured a Cloud Audit Logs integration from that organization to Google SecOps.
If these prerequisites are satisfied, the Google SecOps instance should appear in the selection list under
Use instance in associated GCP account
.
To configure Chrome forwarding to a Google SecOps instance in the same organization, do the following:
Type a name for the configuration.
From the
Use instance in associated GCP account
option, select the Google SecOps instance.
Select the log types to forward from the
Log export settings
.
Click
Test connection
.
Click
Enable
after successfully testing the connection.
Click
Done
when the configuration has completed.
Configure Chrome Forwarding to Google SecOps using an integration token
If the destination Google SecOps instance doesn't appear in the selection list or you need to forward Chrome logs to a Google SecOps instance in a different Google Cloud, do the following:
Provide your Google Workspace Customer ID to the Google SecOps administrator of the destination instance and have them
obtain your Google SecOps instance ID and token
. This token is valid for 24 hours.
Type a name for the configuration.
Select
Use instance outside of your organization
.
Enter the token code provided by the Google SecOps administrator.
Select the log types to forward from the
Log export settings
.
Click
Test Connection
.
Click
Enable
after successfully testing the connection.
Click
Done
when the configuration has completed.
Configure Chrome Forwarding to Google SecOps using the Chronicle Ingestion API
You can configure the Google Chrome reporting connector using a Chronicle
Ingestion API key. You should only use this method if no other integration
method is available.
In the Admin console, go to
Menu
>
Devices
>
Chrome
>
Connectors
.
Click
+ New provider configuration
.
On the side panel, find the Google SecOps setup and click
Set up
.
Enter the
Configuration ID
,
API key
, and
Host Name
:
Configuration ID
: The ID is shown on the
User & browsers settings
page and the
Connectors
page.
API key
: The API key to specify when calling the Chronicle ingestion API to identify the customer.
Host Name
: The Ingestion API endpoint. For US customers, this must be
malachiteingestion-pa.googleapis.com
. For other regions, see
regional endpoints documentation
.
Click
Add Configuration
to add the new provider configuration.
Link Organizational Units (OUs) to the connector
After you have configured the Chrome Enterprise reporting
connector using one of the options described in the
Configure the Chrome Enterprise reporting connector
section, you must enable the connector for the specific Organizational Units
(OUs) from which you want to collect logs.
In the (Google Admin console), go to
Menu
>
Devices
>
Chrome
>
Settings
.
The
Users & browsers
tab is selected by default.
In the
Organizational Units
panel, select the OU you want to collect logs from.
In the main settings list, go to the
Chrome Enterprise reporting connector
setting.
Set the status to
Enabled
and select the configuration you created in the previous steps.
Click
Save
. Repeat these steps for any other OUs that require log ingestion.
Collect Chrome Enterprise Premium context access-aware data
Set up feeds to ingest Chrome Enterprise Premium content specific to Identity-Aware Proxy (IAP)
and context-aware access data.
Who should enable the Identity-Aware Proxy API?
Chrome Enterprise Premium customers who use Identity-Aware Proxy (IAP) data should enable it.
For Chrome Enterprise Premium customers who don't use Identity-Aware Proxy data, enabling the
Identity-Aware Proxy API is optional (but recommended). Doing so adds additional
context-aware access data fields to your log data.
To enable the Identity-Aware Proxy API, perform the steps in
Collect Chrome Enterprise Premium Context Access Aware Data
.
Verify the data flow
To verify the data flow:
Open your Google SecOps instance.
Go to
Menu
>
Search
.
Run the following search query to look for raw, unparsed events:
metadata.log_type = "CHROME_MANAGEMENT"
Supported log types
The following sections are applicable to the
CHROME_MANAGEMENT
parser.
Supported log events
Security category
Event type
Audit Activity
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
browserExtensionInstallEvent
browserCrashEvent
extensionTelemetryEvent
loginEvent
passwordChangedEvent
ChromeOS
ChromeOS login failure
(CHROME_OS_LOGIN_FAILURE_EVENT)
ChromeOS login success
(CHROME_OS_LOGIN_EVENT)
ChromeOS logout
(CHROME_OS_LOGOUT_EVENT)
ChromeOS user added
(CHROME_OS_ADD_USER)
ChromeOS user removed
(CHROME_OS_REMOVE_USER)
ChromeOS lock success
(CHROMEOS_AFFILIATED_LOCK_SUCCESS)
ChromeOS unlock success
(CHROMEOS_AFFILIATED_UNLOCK_SUCCESS)
ChromeOS unlock failure
(CHROMEOS_AFFILIATED_UNLOCK_FAILURE)
ChromeOS device boot state change
(CHROMEOS_DEVICE_BOOT_STATE_CHANGE)
ChromeOS USB device added
(CHROMEOS_PERIPHERAL_ADDED)
ChromeOS USB device removed
(CHROMEOS_PERIPHERAL_REMOVED)
ChromeOS USB status change
(CHROMEOS_PERIPHERAL_STATUS_UPDATED)
ChromeOS CRD host started
(CHROME_OS_CRD_HOST_STARTED)
ChromeOS CRD client connected
(CHROME_OS_CRD_CLIENT_CONNECTED)
ChromeOS CRD client disconnected
(CHROME_OS_CRD_CLIENT_DISCONNECTED)
ChromeOS CRD host stopped
(CHROME_OS_CRD_HOST_ENDED)
Credential Security
passwordReuseEvent
passwordBreachEvent
Data Protection
dataAccessControlEvent
sensitiveDataEvent
sensitiveDataTransferEvent
File Transfer
contentTransferEvent
dangerousDownloadEvent
unscannedFileEvent
Malicious Activity
badNavigationEvent
dangerousDownloadEvent
malwareTransferEvent
Navigation
interstitialEvent
urlFilteringInterstitialEvent
urlNavigationEvent
SafeBrowsingInterstitialEvent
suspiciousUrlEvent
Supported Chrome log formats
The
CHROME_MANAGEMENT
parser supports logs in JSON format.
Supported Chrome sample log
Sample of a raw log for ingestion by the
Chrome Management
parser, in JSON format:
JSON:
{
  "event": "badNavigationEvent",
  "time": "1622093983.104",
  "reason": "SOCIAL_ENGINEERING",
  "result": "EVENT_RESULT_WARNED",
  "device_name": "",
  "device_user": "",
  "profile_user": "sample@domain.io",
  "url": "https://test.domain.com/s/phishing.html",
  "device_id": "e9806c71-0f4e-4dfa-8c52-93c05420bb8f",
  "os_platform": "",
  "os_version": "",
  "browser_version": "109.0.5414.120",
  "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
  "client_type": "CHROME_BROWSER_PROFILE"
}
Field mapping reference
The following field mapping tables are relevant to the
CHROME_MANAGEMENT
parser (log type).
This section explains how the Google SecOps parser maps Chrome log fields to Google SecOps Unified Data Model (UDM) fields for the data sets.
Field mapping reference: Event Identifier to Event Type
The following table lists the
CHROME_MANAGEMENT
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
badNavigationEvent - SOCIAL_ENGINEERING
USER_RESOURCE_ACCESS
SOCIAL_ENGINEERING
badNavigationEvent - SSL_ERROR
USER_RESOURCE_ACCESS
NETWORK_SUSPICIOUS
badNavigationEvent - MALWARE
USER_RESOURCE_ACCESS
SOFTWARE_MALICIOUS
badNavigationEvent - UNWANTED_SOFTWARE
USER_RESOURCE_ACCESS
SOFTWARE_PUA
badNavigationEvent - THREAT_TYPE_UNSPECIFIED
USER_RESOURCE_ACCESS
SOFTWARE_MALICIOUS
browserCrashEvent
STATUS_UPDATE
browserExtensionInstallEvent
USER_RESOURCE_UPDATE_CONTENT
Extension install - BROWSER_EXTENSION_INSTALL
USER_RESOURCE_UPDATE_CONTENT
EXTENSION_REQUEST
USER_UNCATEGORIZED
CHROME_OS_ADD_USER - CHROMEOS_AFFILIATED_USER_ADDED
USER_CREATION
CHROME_OS_ADD_USER - CHROMEOS_UNAFFILIATED_USER_ADDED
USER_CREATION
ChromeOS user added - CHROMEOS_UNAFFILIATED_USER_ADDED
USER_CREATION
ChromeOS user removed - CHROMEOS_UNAFFILIATED_USER_REMOVED
USER_DELETION
CHROME_OS_REMOVE_USER - CHROMEOS_AFFILIATED_USER_REMOVED
USER_DELETION
CHROME_OS_REMOVE_USER - CHROMEOS_UNAFFILIATED_USER_REMOVED
USER_DELETION
Login events
USER_LOGIN
LOGIN_EVENT - CHROMEOS_UNAFFILIATED_LOGIN
USER_LOGIN
loginEvent
USER_LOGIN
ChromeOS login success
USER_LOGIN
CHROME_OS_LOGIN_EVENT - CHROMEOS_AFFILIATED_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_EVENT - CHROMEOS_UNAFFILIATED_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_EVENT - CHROMEOS_GUEST_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_EVENT - CHROMEOS_KIOSK_SESSION_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_EVENT - CHROMEOS_GUEST_SESSION_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_EVENT - CHROMEOS_MANAGED_GUEST_SESSION_LOGIN
USER_LOGIN
ChromeOS login failure - CHROMEOS_AFFILIATED_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_FAILURE_EVENT - CHROMEOS_AFFILIATED_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_FAILURE_EVENT - CHROMEOS_UNAFFILIATED_LOGIN
USER_LOGIN
CHROME_OS_LOGIN_LOGOUT_EVENT - CHROMEOS_AFFILIATED_LOGIN
USER_LOGIN
CHROME_OS_LOGOUT_EVENT - CHROMEOS_AFFILIATED_LOGOUT
USER_LOGOUT
CHROME_OS_LOGOUT_EVENT - CHROMEOS_GUEST_LOGOUT
USER_LOGOUT
CHROME_OS_LOGOUT_EVENT - CHROMEOS_MANAGED_GUEST_SESSION_LOGOUT
USER_LOGOUT
CHROME_OS_LOGOUT_EVENT - CHROMEOS_UNAFFILIATED_LOGOUT
USER_LOGOUT
CHROME_OS_LOGOUT_EVENT - CHROMEOS_KIOSK_SESSION_LOGOUT
USER_LOGOUT
CHROME_OS_LOGOUT_EVENT - CHROMEOS_GUEST_SESSION_LOGOUT
USER_LOGOUT
ChromeOS logout - CHROMEOS_AFFILIATED_LOGOUT
USER_LOGOUT
CHROME_OS_REPORTING_DATA_LOST
STATUS_UPDATE
ChromeOS CRD client connected - CHROMEOS_CRD_CLIENT_CONNECTED
USER_LOGIN
ChromeOS CRD client disconnected
USER_LOGOUT
CHROME_OS_CRD_HOST_STARTED - CHROMEOS_CRD_HOST_STARTED
STATUS_STARTUP
ChromeOS CRD host started - CHROMEOS_CRD_HOST_STARTED
STATUS_STARTUP
ChromeOS CRD host stopped - CHROMEOS_CRD_HOST_ENDED
STATUS_STARTUP
ChromeOS device boot state change - CHROME_OS_VERIFIED_MODE
SETTING_MODIFICATION
ChromeOS device boot state change - CHROME_OS_DEV_MODE
SETTING_MODIFICATION
DEVICE_BOOT_STATE_CHANGE - CHROME_OS_VERIFIED_MODE
SETTING_MODIFICATION
ChromeOS lock success - CHROMEOS_AFFILIATED_LOCK_SUCCESS
USER_LOGOUT
ChromeOS unlock success - CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
USER_LOGIN
ChromeOS unlock failure - CHROMEOS_AFFILIATED_LOGIN
USER_LOGIN
ChromeOS USB device added - CHROMEOS_PERIPHERAL_ADDED
USER_RESOURCE_ACCESS
ChromeOS USB device removed - CHROMEOS_PERIPHERAL_REMOVED
USER_RESOURCE_DELETION
ChromeOS USB status change - CHROMEOS_PERIPHERAL_STATUS_UPDATED
USER_RESOURCE_UPDATE_CONTENT
CHROMEOS_PERIPHERAL_STATUS_UPDATED - CHROMEOS_PERIPHERAL_STATUS_UPDATED
USER_RESOURCE_UPDATE_CONTENT
Client Side Detection
USER_UNCATEGORIZED
Content transfer
SCAN_FILE
CONTENT_TRANSFER
SCAN_FILE
contentTransferEvent
SCAN_FILE
Content unscanned
SCAN_UNCATEGORIZED
CONTENT_UNSCANNED
SCAN_UNCATEGORIZED
dataAccessControlEvent
USER_RESOURCE_ACCESS
dangerousDownloadEvent - Dangerous
SCAN_FILE
SOFTWARE_PUA
dangerousDownloadEvent - DANGEROUS_HOST
SCAN_HOST
dangerousDownloadEvent - UNCOMMON
SCAN_UNCATEGORIZED
dangerousDownloadEvent - POTENTIALLY_UNWANTED
SCAN_UNCATEGORIZED
SOFTWARE_PUA
dangerousDownloadEvent - UNKNOWN
SCAN_UNCATEGORIZED
dangerousDownloadEvent - DANGEROUS_URL
SCAN_UNCATEGORIZED
dangerousDownloadEvent - UNWANTED_SOFTWARE
SCAN_FILE
SOFTWARE_PUA
dangerousDownloadEvent - DANGEROUS_FILE_TYPE
SCAN_FILE
SOFTWARE_MALICIOUS
Desktop DLP Warnings
USER_UNCATEGORIZED
DLP_EVENT
USER_UNCATEGORIZED
interstitialEvent - Malware
NETWORK_HTTP
NETWORK_SUSPICIOUS
IOS/OSX Warnings
SCAN_UNCATEGORIZED
Malware transfer - MALWARE_TRANSFER_DANGEROUS
SCAN_FILE
SOFTWARE_MALICIOUS
MALWARE_TRANSFER - MALWARE_TRANSFER_UNCOMMON
SCAN_FILE
SOFTWARE_MALICIOUS
MALWARE_TRANSFER - MALWARE_TRANSFER_DANGEROUS
SCAN_FILE
SOFTWARE_MALICIOUS
MALWARE_TRANSFER - MALWARE_TRANSFER_UNWANTED_SOFTWARE
SCAN_FILE
SOFTWARE_MALICIOUS
MALWARE_TRANSFER - MALWARE_TRANSFER_UNKNOWN
SCAN_FILE
SOFTWARE_MALICIOUS
MALWARE_TRANSFER - MALWARE_TRANSFER_DANGEROUS_HOST
SCAN_FILE
SOFTWARE_MALICIOUS
malwareTransferEvent - DANGEROUS
SCAN_FILE
SOFTWARE_MALICIOUS
malwareTransferEvent - UNSPECIFIED
SCAN_FILE
SOFTWARE_MALICIOUS
Password breach
USER_RESOURCE_ACCESS
PASSWORD_BREACH
USER_RESOURCE_ACCESS
passwordBreachEvent - PASSWORD_ENTRY
USER_RESOURCE_ACCESS
Password changed
USER_CHANGE_PASSWORD
PASSWORD_CHANGED
USER_CHANGE_PASSWORD
passwordChangedEvent
USER_CHANGE_PASSWORD
Password reuse - PASSWORD_REUSED_UNAUTHORIZED_SITE
USER_RESOURCE_ACCESS
POLICY_VIOLATION, AUTH_VIOLATION
Password reuse - PASSWORD_REUSED_PHISHING_URL
USER_UNCATEGORIZED
PHISHING
PASSWORD_REUSE - PASSWORD_REUSED_UNAUTHORIZED_SITE
USER_RESOURCE_ACCESS
POLICY_VIOLATION, AUTH_VIOLATION
passwordReuseEvent - Unauthorized site
USER_RESOURCE_ACCESS
POLICY_VIOLATION, AUTH_VIOLATION
passwordReuseEvent - PASSWORD_REUSED_PHISHING_URL
USER_UNCATEGORIZED
PHISHING
passwordReuseEvent - PASSWORD_REUSED_UNAUTHORIZED_SITE
USER_RESOURCE_ACCESS
POLICY_VIOLATION, AUTH_VIOLATION
Permissions Blacklisting
RESOURCE_PERMISSIONS_CHANGE
Sensitive data transfer
SCAN_FILE
DATA_EXFILTRATION
SENSITIVE_DATA_TRANSFER
SCAN_FILE
DATA_EXFILTRATION
sensitiveDataEvent - [test_user_5] warn
SCAN_FILE
DATA_EXFILTRATION
sensitiveDataTransferEvent
SCAN_FILE
DATA_EXFILTRATION
Unsafe site visit - UNSAFE_SITE_VISIT_SSL_ERROR
USER_RESOURCE_ACCESS
NETWORK_SUSPICIOUS
UNSAFE_SITE_VISIT - UNSAFE_SITE_VISIT_MALWARE
USER_RESOURCE_ACCESS
SOFTWARE_MALICIOUS
UNSAFE_SITE_VISIT - UNSAFE_SITE_VISIT_UNWANTED_SOFTWARE
USER_RESOURCE_ACCESS
SOFTWARE_SUSPICIOUS
UNSAFE_SITE_VISIT - EVENT_REASON_UNSPECIFIED
USER_RESOURCE_ACCESS
UNSAFE_SITE_VISIT - UNSAFE_SITE_VISIT_SOCIAL_ENGINEERING
USER_RESOURCE_ACCESS
SOCIAL_ENGINEERING
UNSAFE_SITE_VISIT - UNSAFE_SITE_VISIT_SSL_ERROR
USER_RESOURCE_ACCESS
NETWORK_SUSPICIOUS
unscannedFileEvent - FILE_PASSWORD_PROTECTED
SCAN_FILE
unscannedFileEvent - FILE_TOO_LARGE
SCAN_FILE
urlFilteringInterstitialEvent
USER_RESOURCE_ACCESS
POLICY_VIOLATION
extensionTelemetryEvent
If the
telemetry_event_signals.signal_name
log field value is equal to the
COOKIES_GET_ALL_INFO, COOKIES_GET_INFO, TABS_API_INFO
, then the
event_type
set to
USER_RESOURCE_ACCESS
.
Else, if the
telemetry_event_signals.signal_name
log field value is equal to
REMOTE_HOST_CONTACTED_INFO
, then if the
telemetry_event_signals.connection_protocol
log field value is equal to
HTTP_HTTPS
, then the
event_type
is set to
NETWORK_HTTP
.
Else, the
event_type
UDM field is set to
NETWORK_UNCATEGORIZED
.
If the
telemetry_event_signals.signal_name
log field value is equal to
REMOTE_HOST_CONTACTED_INFO
, then the
security category
is set to
NETWORK_SUSPICIOUS
.
Else, if the
telemetry_event_signals.signal_name
log field value contain one of the following values, then the
security category
UDM field is set to
SOFTWARE_SUSPICIOUS
.
COOKIES_GET_INFO
COOKIES_GET_ALL_INFO
Field mapping reference: CHROME_MANAGEMENT
The following table lists the log fields of the
CHROME_MANAGEMENT
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
id.customerId
about.resource.product_object_id
event_detail
metadata.description
time
metadata.event_timestamp
events.parameters.name [TIMESTAMP]
metadata.event_timestamp
event
metadata.product_event_type
events.name
metadata.product_event_type
id.uniqueQualifier
metadata.product_log_id
metadata.product_name
The
metadata.product_name
UDM field is set to
Chrome Management
.
id.applicationName
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
user_agent
network.http.user_agent
userAgent
network.http.user_agent
events.parameters.name [USER_AGENT]
network.http.user_agent
events.parameters.name [SESSION_ID]
network.session_id
client_type
principal.application
clientType
principal.application
events.parameters.name [CLIENT_TYPE]
principal.application
device_id
principal.asset.product_object_id
deviceId
principal.asset.product_object_id
events.parameters.name [DEVICE_ID]
principal.asset.product_object_id
device_name
principal.hostname
deviceName
principal.hostname
events.parameters.name [DEVICE_NAME]
principal.hostname
os_platform
principal.platform
The
principal.platform
UDM field is set to one of the following values:
LINUX
if the
os_platform
log field value is matched with regular expression pattern
linux
.
MAC
if the
os_platform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
os_platform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
os_platform
log field value is matched with regular expression pattern
chromeos
.
Else, if the
os_platform
log field value is
not
empty and
osVersion
log field value is
not
empty, then the
os_platform osVersion
log field is mapped to the
principal.platform_version
UDM field.
os_platform
principal.asset.platform_software.platform
The
principal.asset.platform_software.platform
UDM field is set to one of the following values:
LINUX
if the
os_platform
log field value is matched with regular expression pattern
linux
.
MAC
if the
os_platform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
os_platform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
os_platform
log field value is matched with regular expression pattern
chromeos
.
os_platform
principal.asset.platform_software.platform
The
principal.asset.platform_software.platform
UDM field is set to one of the following values:
LINUX
if the
os_platform
log field value is matched with regular expression pattern
linux
.
MAC
if the
os_platform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
os_platform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
os_platform
log field value is matched with regular expression pattern
chromeos
.
osPlatform
principal.platform
The
principal.platform
UDM field is set to one of the following values:
LINUX
if the
osPlatform
log field value is matched with regular expression pattern
linux
.
MAC
if the
osPlatform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
osPlatform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
osPlatform
log field value is matched with regular expression pattern
chromeos
.
Else, if the
osPlatform
log field value is
not
empty and
osVersion
log field value is
not
empty, then the
osPlatform osVersion
log field is mapped to the
principal.platform_version
UDM field.
osPlatform
principal.asset.platform_software.platform
The
principal.asset.platform_software.platform
UDM field is set to one of the following values:
LINUX
if the
osPlatform
log field value is matched with regular expression pattern
linux
.
MAC
if the
osPlatform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
osPlatform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
osPlatform
log field value is matched with regular expression pattern
chromeos
.
events.parameters.name [DEVICE_PLATFORM]
principal.platform
The
os_platform
and
os_version
is extracted from the
events.parameters.name [DEVICE_PLATFORM]
log field using Grok pattern.
The
principal.platform
UDM field is set to one of the following values:
LINUX
if the
os_platform
log field value is matched with regular expression pattern
linux
.
MAC
if the
os_platform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
os_platform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
os_platform
log field value is matched with regular expression pattern
chromeos
.
Else, if the
os_platform
log field value is
not
empty and
osVersion
log field value is
not
empty, then the
os_platform osVersion
log field is mapped to the
principal.platform_version
UDM field.
events.parameters.name [DEVICE_PLATFORM]
principal.asset.platform_software.platform
The
os_platform
is extracted from the
events.parameters.name [DEVICE_PLATFORM]
log field using Grok pattern.
The
principal.asset.platform_software.platform
UDM field is set to one of the following values:
LINUX
if the
os_platform
log field value is matched with regular expression pattern
linux
.
MAC
if the
os_platform
log field value is matched with regular expression pattern
mac
.
WINDOWS
if the
os_platform
log field value is matched with regular expression pattern
windows
.
CHROME_OS
if the
os_platform
log field value is matched with regular expression pattern
chromeos
.
os_version
principal.platform_version
osVersion
principal.platform_version
events.parameters.name [DEVICE_PLATFORM]
principal.platform_version
The
Version
is extracted from the
events.parameters.name [DEVICE_PLATFORM]
log field using Grok pattern.
device_id
principal.resource.id
deviceId
principal.resource.id
events.parameters.name [DEVICE_ID]
principal.resource.id
directory_device_id
principal.resource.product_object_id
events.parameters.name [DIRECTORY_DEVICE_ID]
principal.resource.product_object_id
principal.resource.resource_subtype
If the
event
log field value is equal to
CHROMEOS_PERIPHERAL_STATUS_UPDATED
, then the
principal.resource.resource_subtype
UDM field is set to
USB
.
Else, if the
events.name
log field value is equal to
CHROMEOS_PERIPHERAL_STATUS_UPDATED
, then the
principal.resource.resource_subtype
UDM field is set to
USB
.
principal.resource.resource_type
If the
device_id
log field value is
not
empty, then the
principal.resource.resource_type
UDM field is set to
DEVICE
.
actor.email
principal.user.email_addresses
actor.profileId
principal.user.userid
result
security_result.action_details
events.parameters.name [EVENT_RESULT]
security_result.action_details
event_result
security_result.action_details
security_result.action
The
security_result.action
UDM field is set to one of the following values:
ALLOW
if the
result
or
events.parameters.name [EVENT_RESULT]
log field value is matched with regular expression pattern
ALLOWED
or
EVENT_RESULT_ALLOWED
.
BLOCK
if the
result
or
events.parameters.name [EVENT_RESULT]
log field value is matched with regular expression pattern
BLOCKED
or
EVENT_RESULT_BLOCKED
.
reason
security_result.category_details
events.parameters.name [EVENT_REASON]
security_result.category_details
events.parameters.name [EVENT_REASON]
security_result.summary
events.parameters.name [LOGIN_FAILURE_REASON]
security_result.description
events.parameters.name [REMOVE_USER_REASON]
security_result.description
If the
events.name
log field value is equal to
CHROME_OS_REMOVE_USER
, then the
events.parameters.name
REMOVE_USER_REASON
log field value is mapped to the
security_result.description
UDM field.
triggered_rules
security_result.rule_name
events.type
security_result.category_details
events.parameters.name [PRODUCT_NAME]
target.application
If the
events.name
log field value contains one of the following values, then the
events.parameters.name [PRODUCT_NAME]
log field is mapped to the
target.resource.name
UDM field:
ChromeOS USB device added
ChromeOS USB device removed
ChromeOS USB status change
CHROMEOS_PERIPHERAL_STATUS_UPDATED
content_name
target.file.full_path
contentName
target.file.full_path
events.parameters.name [CONTENT_NAME]
target.file.full_path
content_type
target.file.mime_type
contentType
target.file.mime_type
events.parameters.name [CONTENT_TYPE]
target.file.mime_type
content_hash
target.file.sha256
events.parameters.name [CONTENT_HASH]
target.file.sha256
content_size
target.file.size
contentSize
target.file.size
events.parameters.name [CONTENT_SIZE]
target.file.size
target.file.file_type
The
fileType
is extracted from the
content_name
log field using Grok pattern, Then
target.file.file_type
UDM field is set to one of the following values:
FILE_TYPE_ZIP
if the
fileType
value is equal to
zip
.
FILE_TYPE_DOS_EXE
if the
fileType
value is equal to
exe
.
FILE_TYPE_PDF
if the
fileType
value is equal to
pdf
.
FILE_TYPE_XLSX
if the
fileType
value is equal to
xlsx
.
extension_id
target.resource.product_object_id
events.parameters.name [APP_ID]
target.resource.product_object_id
extension_name
target.resource.name
If the
event
log field value is equal to
badNavigationEvent
or the
events.name
log field value is equal to
badNavigationEvent
, then the
extension_name
log field is mapped to the
target.resource.name
UDM field.
telemetry_event_signals.signal_name
target.resource.name
If the
event
log field value is equal to
extensionTelemetryEvent
, then the
telemetry_event_signals.signal_name
log field is mapped to the
target.resource.name
UDM field.
events.parameters.name [APP_NAME]
target.resource.name
url
target.url
events.parameters.name [URL]
target.url
telemetry_event_signals.url
target.url
If the
telemetry_event_signals.url
log field value matches the regular expression pattern the
[http:\/\/ or https:\/\/].*
, then the
telemetry_event_signals.url
log field is mapped to the
target.url
UDM field.
device_user
target.user.userid
deviceUser
principal.user.userid
If the
event
log field value is equal to
passwordChangedEvent
, then the
deviceUser
log field is mapped to the
principal.user.userid
UDM field.
Else, the
deviceUser
log field is mapped to the
principal.user.user_display_name
UDM field.
events.parameters.name [DEVICE_USER]
If the
event
log field value is equal to
passwordChangedEvent
, then the
events.parameters.name [DEVICE_USER]
log field is mapped to the
principal.user.userid
UDM field.
Else, the
events.parameters.name [DEVICE_USER]
log field is mapped to the
principal.user.user_display_name
UDM field.
scan_id
about.labels [scan_id]
events.parameters.name [CONNECTION_TYPE]
about.labels [connection_type]
etag
about.labels [etag]
kind
about.labels [kind]
actor.key
principal.user.attribute.labels [actor_key]
actor.callerType
principal.user.attribute.labels [actor_callerType]
events.parameters.name [EVIDENCE_LOCKER_FILEPATH]
security_result.about.labels [evidence_locker_filepath]
federated_origin
security_result.about.labels [federated_origin]
is_federated
security_result.about.labels [is_federated]
destination
security_result.about.labels [trigger_destination]
events.parameters.name [TRIGGER_DESTINATION]
security_result.about.labels [trigger_destination]
source
security_result.about.labels [trigger_source]
events.parameters.name [TRIGGER_SOURCE]
security_result.about.labels [trigger_source]
trigger_type
security_result.about.labels [trigger_type]
trigger_type
additional.fields [trigger_type]
triggerType
security_result.about.labels [trigger_type]
triggerType
additional.fields [trigger_type]
events.parameters.name  [TRIGGER_TYPE]
security_result.about.labels [trigger_type]
trigger_user
security_result.about.labels [trigger_user]
events.parameters.name [TRIGGER_USER]
security_result.about.labels [trigger_user]
events.parameters.name [MALWARE_CATEGORY]
security_result.threat_name
events.parameters.name [MALWARE_FAMILY]
security_result.detection_fields [malware_family]
events.parameters.name [VENDOR_ID]
src.labels [vendor_id]
events.parameters.name [VENDOR_NAME]
src.labels [vendor_name]
events.parameters.name [VIRTUAL_DEVICE_ID]
src.labels [virtual_device_id]
events.parameters.name [VIRTUAL_DEVICE_ID]
additional.fields [virtual_device_id]
events.parameters.name [NEW_BOOT_MODE]
target.asset.attribute.labels [new_boot_mode]
events.parameters.name [PREVIOUS_BOOT_MODE]
target.asset.attribute.labels [previous_boot_mode]
id.time
target.asset.attribute.labels [timestamp]
events.parameters.name [PRODUCT_ID]
target.labels [product_id]
If the
events.name
log field value contains one of the following values, then the
events.parameters.name [PRODUCT_ID]
log field is mapped to the
target.resource.product_object_id
UDM field:
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
events.parameters.name [PRODUCT_ID]
log field is mapped to the
target.labels
UDM field.
extensions.auth.mechanism
If the
events.name
log field value contains one of the following values, then the
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
:
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
events.parameters.name [UNLOCK_TYPE]
target.labels [unlock_type]
extension_description
target.resource.attribute.labels [extension_description]
extension_action
target.resource.attribute.labels [extension_action]
extension_version
target.resource.attribute.labels [extension_version]
If the
event
log field value is
not
equal to
extensionTelemetryEvent
, then the
extension_version
log field is mapped to the
target.resource.attribute.labels[extension_version]
UDM field.
extension_source
target.resource.attribute.labels[extension_source]
If the
event
log field value is
not
equal to
extensionTelemetryEvent
, then the
extension_source
log field is mapped to the
target.resource.attribute.labels[extension_source]
UDM field.
browser_version
target.resource.attributes.labels [browser_version]
browserVersion
target.resource.attributes.labels [browser_version]
events.parameters.name [BROWSER_VERSION]
target.resource.attributes.labels [browser_version]
profile_user
target.user.email_addresses
If the
event
log field value contain one of the following values and the
profile_user
log field value matches the regular expression pattern
^.+@.+$
, then the
profile_user
log field is mapped to the
target.user.email_addresses
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
profile_user
principal.user.email_addresses
If the
event
log field value does not contain one of the following values and the
profile_user
log field value matches the regular expression pattern
^.+@.+$
and the
actor.email
log field value is
not
equal to the
profile_user
, then the
profile_user
log field is mapped to the
principal.user.email_addresses
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
profile_user
target.user.attribute.labels[profile_user_name]
If the
event
log field value contain one of the following values and the
profile_user
log field value does not match the regular expression pattern
^.+@.+$
, then the
profile_user
log field is mapped to the
target.user.attribute.labels.profile_user_name
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
profile_user
principal.user.attribute.labels[profile_user_name]
If the
event
log field value does not contain one of the following values and the
profile_user
log field value does not match the regular expression pattern
^.+@.+$
or the
actor.email
log field value is equal to the
profile_user
, then the
profile_user
log field is mapped to the
principal.user.attribute.labels.profile_user_name
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
events.parameters.name [PROFILE_USER_NAME]
target.user.email_addresses
If the
event
log field value contain one of the following values and the
events.parameters.name [PROFILE_USER_NAME]
log field value matches the regular expression pattern
^.+@.+$
, then the
events.parameters.name [PROFILE_USER_NAME]
log field is mapped to the
target.user.email_addresses
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
events.parameters.name [PROFILE_USER_NAME]
principal.user.email_addresses
If the
event
log field value does not contain one of the following values and the
events.parameters.name [PROFILE_USER_NAME]
log field value matches the regular expression pattern
^.+@.+$
and the
actor.email
log field value is
not
equal to the
events.parameters.name [PROFILE_USER_NAME]
, then the
events.parameters.name [PROFILE_USER_NAME]
log field is mapped to the
principal.user.email_addresses
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
events.parameters.name [PROFILE_USER_NAME]
target.user.attribute.labels[profile_user_name]
If the
event
log field value contain one of the following values and the
events.parameters.name [PROFILE_USER_NAME]
log field value does not match the regular expression pattern
^.+@.+$
, then the
events.parameters.name [PROFILE_USER_NAME]
log field is mapped to the
target.user.attribute.labels.profile_user_name
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
events.parameters.name [PROFILE_USER_NAME]
principal.user.attribute.labels[profile_user_name]
If the
event
log field value does not contain one of the following values and the
events.parameters.name [PROFILE_USER_NAME]
log field value does not match the regular expression pattern
^.+@.+$
or the
actor.email
log field value is equal to the
events.parameters.name [PROFILE_USER_NAME]
, then the
events.parameters.name [PROFILE_USER_NAME]
log field is mapped to the
principal.user.attribute.labels.profile_user_name
UDM field.
CHROME_OS_LOGIN_EVENT
loginEvent
CHROME_OS_LOGIN_FAILURE_EVENT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_LOGOUT_EVENT
CHROMEOS_AFFILIATED_LOCK_SUCCESS
.
target.resource.resource_type
If the
events.name
log field value is equal to
DEVICE_BOOT_STATE_CHANGE
, then the
target.resource.resource_type
UDM field is set to
SETTING
.
url_category
target.labels [url_category]
browser_channel
target.resource.attribute.labels [browser_channel]
report_id
target.labels [report_id]
clickedThrough
target.labels [clickedThrough]
threat_type
security_result.detection_fields [threatType]
triggered_rule_info.action
security_result.action
If the
triggered_rule_info.action
log field value contains one of the following values, then the
triggered_rule_info.action
log field is mapped to the
security_result.action
UDM field:
ALLOW
ALLOW_WITH_MODIFICATION
BLOCK
CHALLENGE
FAIL
QUARANTINE
UNKNOWN_ACTION
Else, the
triggered_rule_info.action
log field is mapped to the
security_result.rule_labels [triggeredRuleInfo_action]
UDM field.
triggered_rule_info.rule_id
security_result.rule_id
triggered_rule_info.rule_name
security_result.rule_name
triggered_rule_info.url_category
security_result.category_details
transfer_method
additional.fields [transfer_method]
extension_name
target.resource_ancestors.name
If the
event
log field value is
equal
to
extensionTelemetryEvent
, then the
extension_name
log field is mapped to the
target.resource_ancestors.name
UDM field.
extension_id
target.resource_ancestors.product_object_id
If the
event
log field value is
equal
to
extensionTelemetryEvent
, then the
extension_id
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field.
extension_version
target.resource_ancestors.attribute.labels[extension_version]
If the
event
log field value is equal to
extensionTelemetryEvent
, then the
extension_version
log field is mapped to the
target.resource_ancestors.attribute.labels[extension_version]
UDM field.
extension_source
target.resource_ancestors.attribute.labels[extension_source]
If the
event
log field value is equal to
extensionTelemetryEvent
, then the
extension_source
log field is mapped to the
target.resource_ancestors.attribute.labels[extension_source]
UDM field.
profile_identifier
additional.fields[profile_identifier]
extension_files_info.file_name
target.resource_ancestors.file.names
extension_files_info.file_hash.hash
target.resource_ancestors.attribute.labels[file_hash]
telemetry_event_signals.count
target.resource.attribute.labels[count]
telemetry_event_signals.tabs_api_method
target.resource.attribute.labels[tabs_api_method]
target.hostname
If the
telemetry_event_signals.url
log field value does not match the regular expression pattern the
[http:\/\/ or https:\/\/].*
, then the
telemetry_event_signals.url
log field is mapped to the
target.hostname
UDM field.
telemetry_event_signals.destination
target.resource.attribute.labels[destination]
telemetry_event_signals.source
target.resource.attribute.labels[source]
telemetry_event_signals.domain
target.domain.name
telemetry_event_signals.cookie_name
target.resource.attribute.labels[cookie_name]
telemetry_event_signals.cookie_path
target.resource.attribute.labels[cookie_path]
telemetry_event_signals.cookie_is_secure
target.resource.attribute.labels[cookie_is_secure]
telemetry_event_signals.cookie_store_id
target.resource.attribute.labels[cookie_store_id]
telemetry_event_signals.cookie_is_session
target.resource.attribute.labels[cookie_is_session]
telemetry_event_signals.connection_protocol
network.application_protocol
If the
telemetry_event_signals.connection_protocol
log field value is equal to
HTTP_HTTPS
, then the
network.application_protocol
UDM field is set to
HTTP
Else, If the
telemetry_event_signals.connection_protocol
log field value is equal to
UNSPECIFIED
, then the
network.application_protocol
UDM field is set to
UNKNOWN_APPLICATION_PROTOCOL
Else, the
telemetry_event_signals.connection_protocol
log field is mapped to the
target.resource.attribute.labels
UDM field.
telemetry_event_signals.contacted_by
target.resource.attribute.labels[contacted_by]
local_ips
principal.ip
If the event log field value is equal to
extensionTelemetryEvent
, then the
local_ips
log field is mapped to the
principal.ip
UDM field.
remote_ip
target.ip
If the event log field value is equal to
extensionTelemetryEvent
, then the
remote_ip
log field is mapped to the
target.ip
UDM field.
device_fqdn
principal.asset.attribute.labels
If the event log field value is equal to
extensionTelemetryEvent
, then the
device_fqdn
log field is mapped to the
principal.asset.attribute.labels
UDM field.
network_name
principal.network.carrier_name
If the event log field value is equal to
extensionTelemetryEvent
, then the
network_name
log field is mapped to the
principal.network.carrier_name
UDM field.
web_app_signed_in_account
target.user.email_addresses
If the
event
log field value contains one of the following values, then the
web_app_signed_in_account
log field is mapped to the
target.user.email_addresses
UDM field:
contentTransferEvent
sensitiveDataEvent
urlFilteringInterstitialEvent
Field mapping reference (preview version)
All fields are applicable to Chrome Enterprise Core customers and Chrome Enterprise Premium customers. Fields that
are only applicable to Chrome Enterprise Premium customers are labeled "[CEP Only]".
Field mapping reference: CHROME_MANAGEMENT (preview version)
The following table lists the log fields of the
CHROME_MANAGEMENT
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
pehash_sha256
about.file.sha256
[CEP Only] The SHA256 file hash (
pehash_sha256
) reported from a
dangerousDownloadEvent
or
contentTransferEvent
.
device_fqdn
principal.asset.attribute.labels
[CEP Only] The device's fully qualified domain name reported in a
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
. Not reported for unmanaged devices
    with managed user profiles.
network_name
principal.network.carrier_name
[CEP Only] The network name (SSID) the device is connected to reported in a
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
.
content_risk.threat_type
security_result.threat_name
[CEP Only] The threat type of the content reported in a
dangerousDownloadEvent
or
contentTransferEvent
.
content_risk_level, content_risk.risk_level
security_result.severity
[CEP Only] The content risk level reported by Safe Browsing in a
dangerousDownloadEvent
or
contentTransferEvent
.
content_risk.risk_reasons
security_result.rule_label
[CEP Only] The content risk reason reported by Safe Browsing in a
dangerousDownloadEvent
or
contentTransferEvent
.
content_risk.risk_indicators
security_result.detection_fields[content_risk_indicators]
[CEP Only] The list of indicators from the Safe Browsing risk level in a
dangerousDownloadEvent
or
contentTransferEvent
.
content_risk.risk_source
security_result.detection_fields[content_risk_source]
[CEP Only] The risk source of the content reported by Safe Browsing in a
dangerousDownloadEvent
or
contentTransferEvent
.
is_encrypted
additional.fields[is_encrypted]
[CEP Only] Set to
true
if the content is encrypted in
dangerousDownloadEvent
or
contentTransferEvent
.
server_scan_status
additional.fields[server_scan_status]
[CEP Only] The status of whether the content in
dangerousDownloadEvent
or
contentTransferEvent
was successfully scanned by Safe Browsing.
url_info.url
principal.url
[CEP Only] The URL of
dangerousDownloadEvent
,
contentTransferEvent
,
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
.
url_info.ip
principal.ip
[CEP Only] The IP address of
dangerousDownloadEvent
,
contentTransferEvent
,
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
.
url_info.type
principal.security_result.detection_fields[url_info_type]
[CEP Only] The URL type (download, tab, or redirect) of
dangerousDownloadEvent
,
contentTransferEvent
,
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
.
url_info.risk_level
principal.security_result.severity
[CEP Only] The risk level of the URL reported by Safe Browsing.
url_info.risk_infos.risk_level
principal.security_result.severity
[CEP Only] Additional risk information reported by Safe Browsing.
url_info.navigation_initiator.initiator_type
principal.security_result.detection_fields[url_info_initiator_type]
[CEP Only] This maps the
url_info_initiator_type
in a
dangerousDownloadEvent
or
contentTransferEvent
. In a
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
this maps the
url_navigation_initiator
.
url_info.navigation_initiator.entity
principal.security_result.detection_fields[url_info_entity]
[CEP Only] This maps the
url_info_entity
in a
dangerousDownloadEvent
or
contentTransferEvent
. In a
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
this maps the
url_infos_navigation_entity
.
url_info.request_http_method
principal.security_result.detection_fields[url_info_request_http_method]
[CEP Only] The HTTP method used to contact the URL.
url_info.url_categories
principal.url_metadata.categories
[CEP Only] The URL category reported by Safe Browsing of
urlNavigationEvent
or
suspiciousUrlEvent
.
url_info.risk_infos.risk_indicators
principal.security_result.detection_fields[url_info_risk_infos_risk_indicators_key]
[CEP Only] The URL risk indicators reported by Safe Browsing of
urlNavigationEvent
or
suspiciousUrlEvent
.
url_info.risk_infos.risk_reasons
principal.security_result.rule_label[risk_reason]
[CEP Only] The Safe Browsing reason for the URL risk classification of
urlNavigationEvent
or
suspiciousUrlEvent
.
url_info.risk_infos.risk_source
principal.security_result.detection_fields[content_risk_source]
[CEP Only] The risk source determination reported by Safe Browsing. This includes URL and file reputation
    and content scanning results for
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
.
url_info.risk_infos.threat_type
security_result.threat_name
[CEP Only] The threat type reported by Safe Browsing of the URL for
urlNavigationEvent
,
suspiciousUrlEvent
, or
urlFilteringInterstitialEvent
.
tab_url_info.url, tab_url, referrers.url
about.url
[CEP Only] Maps the
tab_url_info.url
of
dangerousDownloadEvent
or
contentTransferEvent
. Maps the
referrers.url
of a
urlNavigationEvent
, or
suspiciousUrlEvent
.
tab_url_info.ip, referrers.ip
about.ip
[CEP Only] Maps the
tab_url_info_ip
IP address associated with
dangerousDownloadEvent
or
contentTransferEvent
. Maps the IP address of
referrers.ip
in
urlNavigationEvent
or
suspiciousUrlEvent
.
remote_ip
target.ip
[CEP Only] If the
event
log field value contains one of the following values, then the
remote_ip
log field is mapped to the
target.ip
UDM field:
dangerousDownloadEvent
contentTransferEvent
urlNavigationEvent
suspiciousUrlEvent
urlFilteringInterstitialEvent
tab_url_info.type
about.security_result.detection_fields[tab_url_info_type]
[CEP Only] The URL tab type for
dangerousDownloadEvent
or
contentTransferEvent
.
tab_url_info.risk_level
about.security_result.severity
[CEP Only] The Safe Browsing risk level associated with the URL from a tab event for
dangerousDownloadEvent
or
contentTransferEvent
.
tab_url_info.navigation_initiator.initiator_type
about.security_result.detection_fields[tab_url_info_initiator_type]
[CEP Only] The initiator type of the tab event for
dangerousDownloadEvent
or
contentTransferEvent
.
tab_url_info.navigation_initiator.entity
about.security_result.detection_fields[tab_url_info_entity]
[CEP Only] The
tab_url_info_entity
for
dangerousDownloadEvent
or
contentTransferEvent
.
tab_url_info.request_http_method
about.security_result.detection_fields[tab_url_info_request_http_method]
[CEP Only] The HTTP method a tab used to contact the URL of
dangerousDownloadEvent
or
contentTransferEvent
.
referrers.navigation_initiator.entity
about.security_result.detection_fields[referrers_navigation_initiator_entity]
[CEP Only] The referrer entity name that initiated the navigation event for
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.navigation_initiator.initiator_type
about.security_result.detection_fields[referrers_navigation_initiator_initiator_type]
[CEP Only] The referrer type that initiated
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.request_http_method
about.security_result.detection_fields[referrers_request_http_method]
[CEP Only] The HTTP method of
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.risk_infos.risk_categories
about.security_result.detection_fields[referrers_risk_infos_risk_categories]
[CEP Only] The URL category of the referrer, as provided by the Safe Browsing service, associated with
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.risk_infos.risk_level, referrers.risk_level
about.security_result.severity
[CEP Only] Maps the risk level provided by Safe Browsing
referrers.risk_level
for a
urlNavigationEvent
or
suspiciousUrlEvent
or
referrers.risk_infos.risk_level
for
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.type
about.security_result.detection_fields[referrers_type]
[CEP Only] The URL type provided by Safe Browsing of the referrer URL of
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.risk_infos.risk_source
about.security_result.detection_fields[referrers_risk_source]
[CEP Only] The risk source provided by Safe Browsing for the referrer URL of
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.risk_infos.threat_type
about.security_result.threat_name
[CEP Only] The threat type provided by Safe Browsing for the referrer URL of
urlNavigationEvent
or
suspiciousUrlEvent
.
referrers.url_categories
about.url_metadata.categories
[CEP Only] The URL category provided by Safe Browsing for the referrer URL of
urlNavigationEvent
or
suspiciousUrlEvent
.
Need more help?
Get answers from Community members and Google SecOps professionals.
