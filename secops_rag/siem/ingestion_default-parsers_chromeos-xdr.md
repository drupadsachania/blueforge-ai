# Collect ChromeOS XDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/chromeos-xdr/  
**Scraped:** 2026-03-05T09:21:04.951986Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ChromeOS XDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest ChromeOS XDR logs to Google Security Operations.
Chrome Enterprise provides comprehensive visibility into browser and ChromeOS device security events, including malware transfers, unsafe site visits, password reuse, extension installations, login activity, and ChromeOS device telemetry. The Chrome Enterprise Reporting Connector forwards these logs directly from Google Admin Console to Google Security Operations for analysis and threat detection.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Google Workspace Administrator account with Super Admin privileges
Google Chrome 137 or later (earlier versions don't provide complete referrer URL data)
Chrome Enterprise Premium licenses for advanced features (optional, but recommended for full event coverage)
Chrome browser cloud management enabled on target devices
Your Google Workspace Customer ID from the Google Workspace Admin console
Configure the Chrome Management parser
You may need to update to a new version of the Chrome Management parser to support recent Chrome logs.
In your Google SecOps instance, go to
Menu
>
Settings
>
Parsers
.
Find the
Chrome Management
prebuilt entry.
Verify that you are using a version date
2025-08-14
or newer by applying any pending updates.
Obtain Chronicle Ingestion API credentials
You can configure the Chrome Enterprise reporting connector using one of three methods. This document covers the Chronicle Ingestion API key method, which should only be used if no other integration method is available.
Create Google Cloud API key
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
In the
API key
settings page:
Name
: Enter a descriptive name (for example,
Chronicle Chrome Enterprise API Key
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
Determine the ingestion endpoint hostname
The hostname depends on your Google SecOps instance region:
US customers
:
malachiteingestion-pa.googleapis.com
Europe customers
:
europe-malachiteingestion-pa.googleapis.com
Asia Southeast customers
:
asia-southeast1-malachiteingestion-pa.googleapis.com
For other regions, see the
regional endpoints documentation
.
Configure Chrome Enterprise Reporting Connector
Add the Google SecOps provider configuration
Sign in with a
super administrator
account to the
Google Admin console
.
If you aren't using a super administrator account, you can't complete these steps.
Go to
Menu
>
Devices
>
Chrome
>
Connectors
.
Optional: If you're configuring Chrome Enterprise connectors settings for the first time, follow the prompts to turn on
Chrome Enterprise Connectors
.
At the top, click
+ New provider configuration
.
In the panel that appears on the right, find the
Google SecOps
setup.
Click
Set up
.
Enter the following configuration details:
Configuration ID
: Enter a descriptive name (for example,
Chronicle Chrome Enterprise Connector
). This ID is shown on the User & browsers settings page and the Connectors page.
API key
: Paste the API key you created in the previous section.
Host Name
: Enter the ingestion API endpoint hostname for your region (for example,
malachiteingestion-pa.googleapis.com
for US customers).
Click
Test connection
to validate the configuration details.
If the validation fails, review the configuration details and retest. Verify that:
The API key is correct and has not expired
The hostname matches your Google SecOps instance region
The API key has the Chronicle API restriction applied
If the validation is successful, click
Add Configuration
.
The configuration is now added for your entire organization and can be used in any organizational unit.
Enable event reporting
In the Google Admin console, go to
Menu
>
Devices
>
Chrome
>
Settings
.
The
User & browser settings
page opens by default.
To apply the setting to all users and enrolled browsers, leave the top organizational unit selected. Otherwise, select a child
organizational unit
.
Go to
Browser reporting
.
Click
Event reporting
.
Select
Enable event reporting
.
Optional: Configure additional settings. Choose the reported event types that you need, based on what type of content you want to send for analysis:
Default event types
: Chrome threat and data protection events include malware transfer, password reuse, and unsafe site visits
Browser crashes
: Browser crash events
Content transfers
: File upload and download events
Data access controls
: Data access control events
Extension installations
: Browser extension installation events
Extension telemetry
: Extension telemetry events
Google login activity
: Google account login events
Malware transfer
: Malware transfer events
Password breach
: Password breach events
Password changed
: Password change events
Password reuse
: Password reuse events
Sensitive data transfer
: Sensitive data transfer events
Suspicious URL
: Suspicious URL events
Unsafe site visits
: Unsafe site visit events
URL filtering interstitial
: URL filtering interstitial events
URL navigations
: URL navigation events
Click
Save
.
Or, you might click
Override
for an organizational unit. To later restore the inherited value, click
Inherit
.
Link organizational units to the connector
After you have configured the Chrome Enterprise reporting connector, you must enable the connector for the specific Organizational Units (OUs) from which you want to collect logs.
In the Google Admin console, go to
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
.
Repeat these steps for any other OUs that require log ingestion.
Configure ChromeOS device reporting
Optional: If you want to collect ChromeOS device events in addition to Chrome browser events, enable ChromeOS device reporting.
In the Google Admin console, go to
Menu
>
Devices
>
Chrome
>
Settings
>
Device settings
.
Optional: To apply the setting to a department or team, at the side, select an
organizational unit
.
Go to
User and Device reporting
.
Next to
Report extended detection and response (XDR) events
, select
Report information about extended detection and response (XDR) events
.
Click
Save
.
Verify the data flow
To verify that Chrome Enterprise logs are being ingested into Google SecOps:
Open your Google SecOps instance.
Go to
Menu
>
Search
.
Run the following search query to look for Chrome Management events:
metadata.log_type = "CHROME_MANAGEMENT"
You should see events appearing within a few minutes of configuration. If no events appear:
Verify that event reporting is enabled in Google Admin Console
Verify that the connector is linked to the correct organizational units
Verify that Chrome browsers are enrolled in cloud management
Check that the API key is valid and has not expired
Verify that the hostname matches your Google SecOps instance region
Supported log types
The Chrome Enterprise Reporting Connector forwards the following event types to Google SecOps:
Chrome browser events
Event Type
Description
Security Category
badNavigationEvent
User navigated to a malicious or suspicious URL
SOFTWARE_MALICIOUS, SOCIAL_ENGINEERING, NETWORK_SUSPICIOUS
browserCrashEvent
Chrome browser crashed
STATUS_UPDATE
browserExtensionInstallEvent
Browser extension was installed
USER_RESOURCE_UPDATE_CONTENT
contentTransferEvent
File was uploaded or downloaded
SCAN_FILE
dangerousDownloadEvent
Dangerous file was downloaded
SOFTWARE_PUA, SOFTWARE_MALICIOUS
extensionTelemetryEvent
Extension telemetry data
USER_RESOURCE_ACCESS, NETWORK_HTTP
loginEvent
User logged in to Google account
USER_LOGIN
malwareTransferEvent
Malware was transferred
SOFTWARE_MALICIOUS
passwordBreachEvent
Password was found in a breach
USER_RESOURCE_ACCESS
passwordChangedEvent
User changed their password
USER_CHANGE_PASSWORD
passwordReuseEvent
Password was reused on unauthorized site
POLICY_VIOLATION, AUTH_VIOLATION, PHISHING
sensitiveDataEvent
Sensitive data was detected
DATA_EXFILTRATION
sensitiveDataTransferEvent
Sensitive data was transferred
DATA_EXFILTRATION
suspiciousUrlEvent
Suspicious URL was accessed
SOFTWARE_SUSPICIOUS
unsafeSiteVisitEvent
User visited an unsafe site
SOFTWARE_MALICIOUS, NETWORK_SUSPICIOUS
urlFilteringInterstitialEvent
URL filtering interstitial was displayed
POLICY_VIOLATION
urlNavigationEvent
User navigated to a URL
NETWORK_HTTP
ChromeOS device events
Event Type
Description
Security Category
CHROME_OS_LOGIN_EVENT
User logged in to ChromeOS device
USER_LOGIN
CHROME_OS_LOGIN_FAILURE_EVENT
ChromeOS login failed
USER_LOGIN
CHROME_OS_LOGOUT_EVENT
User logged out of ChromeOS device
USER_LOGOUT
CHROME_OS_ADD_USER
User was added to ChromeOS device
USER_CREATION
CHROME_OS_REMOVE_USER
User was removed from ChromeOS device
USER_DELETION
CHROMEOS_AFFILIATED_LOCK_SUCCESS
ChromeOS device was locked
USER_LOGOUT
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
ChromeOS device was unlocked
USER_LOGIN
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
ChromeOS unlock failed
USER_LOGIN
CHROMEOS_DEVICE_BOOT_STATE_CHANGE
Device boot state changed
SETTING_MODIFICATION
CHROMEOS_PERIPHERAL_ADDED
USB device was added
USER_RESOURCE_ACCESS
CHROMEOS_PERIPHERAL_REMOVED
USB device was removed
USER_RESOURCE_DELETION
CHROMEOS_PERIPHERAL_STATUS_UPDATED
USB device status changed
USER_RESOURCE_UPDATE_CONTENT
CHROME_OS_CRD_HOST_STARTED
Chrome Remote Desktop host started
STATUS_STARTUP
CHROME_OS_CRD_CLIENT_CONNECTED
Chrome Remote Desktop client connected
USER_LOGIN
CHROME_OS_CRD_CLIENT_DISCONNECTED
Chrome Remote Desktop client disconnected
USER_LOGOUT
CHROME_OS_CRD_HOST_ENDED
Chrome Remote Desktop host stopped
STATUS_STARTUP
UDM mapping table
The following table shows how Chrome Management log fields are mapped to Google SecOps Unified Data Model (UDM) fields:
Chrome Log Field
UDM Field
Description
event
metadata.product_event_type
Event type identifier
time
metadata.event_timestamp
Event timestamp
device_id
principal.asset.product_object_id
Device identifier
device_name
principal.hostname
Device hostname
device_user
principal.user.user_display_name
Device user
profile_user
principal.user.email_addresses
Profile user email
os_platform
principal.platform
Operating system platform
os_version
principal.platform_version
Operating system version
browser_version
target.resource.attributes.labels[browser_version]
Browser version
user_agent
network.http.user_agent
HTTP user agent
url
target.url
Target URL
reason
security_result.category_details
Event reason
result
security_result.action_details
Event result
content_name
target.file.full_path
File name
content_type
target.file.mime_type
File MIME type
content_hash
target.file.sha256
File SHA256 hash
content_size
target.file.size
File size
extension_id
target.resource.product_object_id
Extension identifier
extension_name
target.resource.name
Extension name
extension_version
target.resource.attribute.labels[extension_version]
Extension version
For a complete field mapping reference, see the
Chrome Management parser documentation
.
Need more help?
Get answers from Community members and Google SecOps professionals.
