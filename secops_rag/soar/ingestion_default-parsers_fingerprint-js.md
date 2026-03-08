# Collect FingerprintJS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fingerprint-js/  
**Scraped:** 2026-03-05T09:55:44.730820Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect FingerprintJS logs
Supported in:
Google secops
SIEM
This document explains how to configure FingerprintJS to push logs to Google Security Operations using webhooks.
FingerprintJS is a device intelligence platform that provides visitor identification and fraud detection capabilities. It generates unique visitor identifiers and provides smart signals including bot detection, VPN detection, incognito mode detection, and other device intelligence insights. When a visitor is identified through the FingerprintJS JavaScript agent, webhooks can send the identification event data to Google Security Operations in real time.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
FingerprintJS account with webhook support
Access to Google Cloud console (for API key creation)
FingerprintJS JavaScript agent installed on your website or application
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
FingerprintJS Identification Events
).
Select
Webhook
as the
Source type
.
Select
FingerprintJS
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
(optional): Leave empty. Each webhook request contains a single identification event.
Asset namespace
: The
asset namespace
.
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
Chronicle requires an API key for authentication. Create a restricted API key in the Google Cloud console.
Create the API key
Go to the
Google Cloud console Credentials page
Select your project (the project associated with your Chronicle instance).
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
Chronicle FingerprintJS Webhook API Key
).
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
Configure FingerprintJS webhook
Construct the webhook URL
Combine the Chronicle endpoint URL and API key:
<ENDPOINT_URL>?key=<API_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
Create webhook in FingerprintJS Dashboard
Sign in to the
FingerprintJS Dashboard
.
Go to
Dashboard
>
Webhooks
.
Click
Add webhook
.
Provide the following configuration details:
URL
: Paste the complete endpoint URL with API key from above.
Environment
(optional): If you select an environment, your webhook will only report on events from a matching environment. Leave empty to receive events from all environments.
Basic authentication
(optional): Expand
Basic authentication
if you want to add additional authentication. For Chronicle integration, you can leave this empty as authentication is handled via the API key and secret key.
Click
Create Webhook
.
A success modal displays
Webhooks created
.
Important
: If you are using webhook signatures (Enterprise plan only), copy and save the encryption key shown in the success modal. The key is displayed only once.
Add Chronicle secret key to webhook
FingerprintJS does not support custom HTTP headers during webhook creation. You must add the Chronicle secret key as a query parameter in the webhook URL.
Update the webhook URL to include the secret key:
<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
To update the webhook URL:
In the FingerprintJS Dashboard, go to
Dashboard
>
Webhooks
.
Find your webhook in the table and click the
Edit
icon.
Update the
URL
field with the complete URL including both API key and secret key.
Click
Edit webhook
.
Test the webhook
In the FingerprintJS Dashboard, go to
Dashboard
>
Webhooks
.
Find your webhook in the table.
Click
Send test event
.
Wait for confirmation that the test event was sent successfully.
Verify the webhook shows a successful delivery status.
Authentication methods reference
Chronicle webhook feeds support multiple authentication methods. FingerprintJS webhooks use query parameters for authentication.
Query parameters method
FingerprintJS does not support custom HTTP headers during webhook creation, so credentials must be appended to the URL.
URL format:
<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
Request format:
POST <ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY> HTTP/1.1
Content-Type: application/json
{
"visitorId": "3HNey93AkBW6CRbxV6xP",
"requestId": "1708102555327.NLOjmg",
"timestamp": 1582299576512
}
Note
: Credentials are visible in the URL and may be logged in web server access logs. This is the only authentication method supported by FingerprintJS webhooks.
UDM mapping table
Log Field
UDM Mapping
Logic
rawDeviceAttributes.architecture.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesArchitecture"
rawDeviceAttributes.audio.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesAudio"
rawDeviceAttributes.colorDepth.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesColorDepth"
rawDeviceAttributes.colorGamut.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesColorGamut"
rawDeviceAttributes.contrast.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesContrast"
rawDeviceAttributes.cookiesEnabled.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesCookiesEnabled"
rawDeviceAttributes.deviceMemory.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesDeviceMemory"
rawDeviceAttributes.fontPreferences.value.apple
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesApple"
rawDeviceAttributes.fontPreferences.value.default
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesDefault"
rawDeviceAttributes.fontPreferences.value.min
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesMin"
rawDeviceAttributes.fontPreferences.value.mono
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesMono"
rawDeviceAttributes.fontPreferences.value.sans
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesSansSerif"
rawDeviceAttributes.fontPreferences.value.serif
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesSerif"
rawDeviceAttributes.fontPreferences.value.system
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesFontPreferencesSystem"
rawDeviceAttributes.fonts.value
event.idm.read_only_udm.additional.fields
Merged as list_value under key "RawDeviceAttributesFonts"
rawDeviceAttributes.forcedColors.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesForcedColors"
rawDeviceAttributes.hardwareConcurrency.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesHardwareConcurrency"
rawDeviceAttributes.hdr.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesHdr"
rawDeviceAttributes.indexedDB.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesIndexedDB"
rawDeviceAttributes.languages.value
event.idm.read_only_udm.additional.fields
Merged as indexed list_value under keys like "0:RawDeviceAttributesLanguage"
rawDeviceAttributes.localStorage.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesLocalStorage"
rawDeviceAttributes.math.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesMath"
rawDeviceAttributes.monochrome.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesMonochrome"
rawDeviceAttributes.openDatabase.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesOpenDatabase"
rawDeviceAttributes.pdfViewerEnabled.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesPdfViewerEnabled"
rawDeviceAttributes.reducedMotion.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesReducedMotion"
rawDeviceAttributes.screenFrame.value
event.idm.read_only_udm.additional.fields
Merged as list_value under key "RawDeviceAttributesScreenFrame"
rawDeviceAttributes.screenResolution.value
event.idm.read_only_udm.additional.fields
Merged as list_value under key "RawDeviceAttributesScreenResolution"
rawDeviceAttributes.sessionStorage.value
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesSessionStorage"
rawDeviceAttributes.touchSupport.value.maxTouchPoints
event.idm.read_only_udm.additional.fields
Set as label with key "RawDeviceAttributesTouchSupportMaxTouchPoints"
rawDeviceAttributes.vendorFlavors.value
event.idm.read_only_udm.additional.fields
Merged as list_value under key "RawDeviceAttributesVendorFlavors"
firstSeenAt.subscription
event.idm.read_only_udm.metadata.event_timestamp
Parsed timestamp from firstSeenAt.subscription
time
event.idm.read_only_udm.metadata.event_timestamp
Parsed timestamp from time
event.idm.read_only_udm.metadata.event_type
Derived: if has_principal and has_target → "NETWORK_CONNECTION"; if has_target_resource → "USER_RESOURCE_ACCESS"; if has_principal → "STATUS_UPDATE"; else "GENERIC_EVENT"
source_type
event.idm.read_only_udm.metadata.product_event_type
Value taken from source_type
requestId
event.idm.read_only_udm.metadata.product_log_id
Value taken from requestId
event.idm.read_only_udm.metadata.product_name
Set to "FINGERPRINT_JS"
event.idm.read_only_udm.metadata.vendor_name
Set to "FINGERPRINT_JS"
browserDetails.userAgent
event.idm.read_only_udm.network.http.parsed_user_agent
Renamed from browserDetails.userAgent after conversion
browserDetails.browserName
event.idm.read_only_udm.network.http.parsed_user_agent.browser
Value taken from browserDetails.browserName
browserDetails.browserFullVersion
event.idm.read_only_udm.network.http.parsed_user_agent.browser_version
Value taken from browserDetails.browserFullVersion
browserDetails.device
event.idm.read_only_udm.network.http.parsed_user_agent.device
Value taken from browserDetails.device
event.idm.read_only_udm.network.http.parsed_user_agent.family
Set to "USER_DEFINED"
browserDetails.os
event.idm.read_only_udm.network.http.parsed_user_agent.os
Value taken from browserDetails.os
browserDetails.clientReferrer
event.idm.read_only_udm.network.http.referral_url
Value taken from browserDetails.clientReferrer
browserDetails.userAgent
event.idm.read_only_udm.network.http.user_agent
Value taken from browserDetails.userAgent
userAgent
event.idm.read_only_udm.network.http.user_agent
Value taken from userAgent
tag.session
event.idm.read_only_udm.network.session_id
Value taken from tag.session
rawDeviceAttributes.vendor.value
event.idm.read_only_udm.principal.administrative_domain
Value taken from rawDeviceAttributes.vendor.value
ip
event.idm.read_only_udm.principal.asset.ip
Value taken from ip
ip
event.idm.read_only_udm.principal.ip
Value taken from ip
ipInfo.v4.geolocation.city.name
event.idm.read_only_udm.principal.location.city
Value taken from ipInfo.v4.geolocation.city.name
ipInfo.v4.geolocation.country.name
event.idm.read_only_udm.principal.location.country_or_region
Value taken from ipInfo.v4.geolocation.country.name
ipInfo.v4.geolocation.latitude
event.idm.read_only_udm.principal.location.region_coordinates.latitude
Converted from ipInfo.v4.geolocation.latitude to float
ipInfo.v4.geolocation.longitude
event.idm.read_only_udm.principal.location.region_coordinates.longitude
Converted from ipInfo.v4.geolocation.longitude to float
browserDetails.osVersion
event.idm.read_only_udm.principal.platform_version
Value taken from browserDetails.osVersion
rawDeviceAttributes.platform.value
event.idm.read_only_udm.principal.platform_version
Value taken from rawDeviceAttributes.platform.value
ipInfo.v4.asn.asn
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "ASN"
ipInfo.v4.asn.name
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "ASNName"
ipInfo.v4.asn.network
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "ASNNetwork"
ipInfo.v4.geolocation.accuracyRadius
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "AccuracyRadius"
ipInfo.v4.geolocation.continent.name
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "Continent_Name"
ipInfo.v4.geolocation.subdivisions.isoCode
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "ISOCode"
ipInfo.v4.geolocation.subdivisions.name
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "Name"
ipInfo.v4.geolocation.timezone
event.idm.read_only_udm.principal.resource.attribute.labels
Set as label with key "Timezone"
bot.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "BotResult"
browserDetails.browserMajorVersion
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "BrowserMajorVersion"
rawDeviceAttributes.canvas.value.Geometry
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesCanvasGeometry"
rawDeviceAttributes.canvas.value.Text
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesCanvasText"
rawDeviceAttributes.canvas.value.Winding
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesCanvasWinding"
confidence.score
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "ConfidenceScore"
confidence.revision
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "ConfidenceRevision"
developerTools.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "DeveloperToolsResult"
rawDeviceAttributes.emoji.value.bottom
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiBottom"
rawDeviceAttributes.emoji.value.font
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiFont"
rawDeviceAttributes.emoji.value.height
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiHeight"
rawDeviceAttributes.emoji.value.left
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiLeft"
rawDeviceAttributes.emoji.value.right
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiRight"
rawDeviceAttributes.emoji.value.top
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiTop"
rawDeviceAttributes.emoji.value.width
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiWidth"
rawDeviceAttributes.emoji.value.x
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiX"
rawDeviceAttributes.emoji.value.y
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesEmojiY"
highActivity.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "HighActivityResult"
incognito
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "Incognito"
ipBlocklist.details.attackSource
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "AttackSource"
ipBlocklist.details.emailSpam
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "emailSpam"
ipBlocklist.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "IpBlocklistResult"
rawDeviceAttributes.mathML.value.bottom
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLBottom"
rawDeviceAttributes.mathML.value.font
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLFont"
rawDeviceAttributes.mathML.value.height
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLHeight"
rawDeviceAttributes.mathML.value.left
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLLeft"
rawDeviceAttributes.mathML.value.right
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLRight"
rawDeviceAttributes.mathML.value.top
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLTop"
rawDeviceAttributes.mathML.value.width
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLWidth"
rawDeviceAttributes.mathML.value.x
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLX"
rawDeviceAttributes.mathML.value.y
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesMathMLY"
privacySettings.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "PrivacySettingsResult"
proxy.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "ProxyResult"
rawDeviceAttributes.webGlBasics.value.renderer
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLBasicsRenderer"
rawDeviceAttributes.webGlBasics.value.rendererUnmasked
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLBasicsRendererUnmasked"
rawDeviceAttributes.webGlBasics.value.shadingLanguageVersion
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLBasicsShadingLanguageVersion"
rawDeviceAttributes.webGlBasics.value.vendorUnmasked
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLBasicsVendorUnmasked"
rawDeviceAttributes.webGlExtensions.value.contextAttributes
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLExtensionsContextAttributes"
rawDeviceAttributes.webGlExtensions.value.extensionParameters
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLExtensionsExtensionParameters"
rawDeviceAttributes.webGlExtensions.value.extensions
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLExtensionsExtensions"
rawDeviceAttributes.webGlExtensions.value.parameters
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLExtensionsParameters"
rawDeviceAttributes.webGlExtensions.value.shaderPrecisions
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "RawDeviceAttributesWebGLExtensionsShaderPrecisions"
suspectScore.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "SuspectScoreResult"
tag.request
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "TagRequest"
tampering.anomalyScore
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "TamperingAnomalyScore"
tampering.antiDetectBrowser
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "TamperingAntiDetectBrowser"
tampering.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "TamperingAntiDetectBrowserResult"
tor.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "TorResult"
velocity.distinctCountry.intervals.1h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityDistinctCountryIntervals1h"
velocity.distinctCountry.intervals.24h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityDistinctCountryIntervals24h"
velocity.distinctCountry.intervals.5m
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityDistinctCountryIntervals5m"
velocity.distinctIp.intervals.1h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityDistinctIpIntervals1h"
velocity.distinctIp.intervals.24h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityDistinctIpIntervals24h"
velocity.distinctIp.intervals.5m
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityDistinctIpIntervals5m"
velocity.events.intervals.1h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityEventsIntervals1h"
velocity.events.intervals.24h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityEventsIntervals24h"
velocity.events.intervals.5m
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityEventsIntervals5m"
velocity.ipEvents.intervals.1h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityIpEventsIntervals1h"
velocity.ipEvents.intervals.24h
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityIpEventsIntervals24h"
velocity.ipEvents.intervals.5m
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VelocityIpEventsIntervals5m"
visitorFound
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VisitorFound"
visitorId
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VisitorId"
vpn.confidence
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnConfidence"
vpn.methods.auxiliaryMobile
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnMethodsAuxiliaryMobile"
vpn.methods.osMismatch
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnMethodsOsMismatch"
vpn.methods.publicVPN
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnMethodsPublicVPN"
vpn.methods.timezoneMismatch
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnMethodsTimezoneMismatch"
vpn.originCountry
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnOriginCountry"
vpn.originTimezone
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnOriginTimezone"
vpn.result
event.idm.read_only_udm.security_result.detection_fields
Set as label with key "VpnResult"
rawDeviceAttributes.webGlBasics.value.vendor
event.idm.read_only_udm.target.administrative_domain
Value taken from rawDeviceAttributes.webGlBasics.value.vendor
ipInfo.v6.address
event.idm.read_only_udm.target.asset.ip
Value taken from ipInfo.v6.address
ipInfo.v6.address
event.idm.read_only_udm.target.ip
Value taken from ipInfo.v6.address
ipInfo.v6.geolocation.city.name
event.idm.read_only_udm.target.location.city
Value taken from ipInfo.v6.geolocation.city.name
ipInfo.v6.geolocation.country.name
event.idm.read_only_udm.target.location.country_or_region
Value taken from ipInfo.v6.geolocation.country.name
ipInfo.v6.geolocation.latitude
event.idm.read_only_udm.target.location.region_coordinates.latitude
Converted from ipInfo.v6.geolocation.latitude to float
ipInfo.v6.geolocation.longitude
event.idm.read_only_udm.target.location.region_coordinates.longitude
Converted from ipInfo.v6.geolocation.longitude to float
path
event.idm.read_only_udm.target.path
Value taken from path
rawDeviceAttributes.webGlBasics.value.version
event.idm.read_only_udm.target.platform_version
Value taken from rawDeviceAttributes.webGlBasics.value.version
ipInfo.v6.asn.asn
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "ASN"
ipInfo.v6.asn.name
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "ASNName"
ipInfo.v6.asn.network
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "ASNNetwork"
ipInfo.v6.geolocation.accuracyRadius
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "AccuracyRadius"
ipInfo.v6.geolocation.continent.name
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "Continent_Name"
ipInfo.v6.geolocation.subdivisions.isoCode
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "ISOCode"
ipInfo.v6.geolocation.subdivisions.name
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "Name"
ipInfo.v6.geolocation.timezone
event.idm.read_only_udm.target.resource.attribute.labels
Set as label with key "Timezone"
url
event.idm.read_only_udm.target.url
Value taken from url
Need more help?
Get answers from Community members and Google SecOps professionals.
