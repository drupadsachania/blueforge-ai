# Collect Microsoft Defender for Cloud alert logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/microsoft-defender-cloud-alerts/  
**Scraped:** 2026-03-05T09:58:02.294408Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Defender for Cloud alert logs
Supported in:
Google secops
SIEM
Overview
This parser extracts security alert data from Microsoft Defender for Cloud's JSON formatted logs. It transforms and maps the raw log fields into the Google SecOps UDM, handling various data types and nested structures, while also enriching the data with additional context and labels for improved analysis.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to Microsoft Defender for Cloud.
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
field, enter a name for the feed; for example,
Microsoft Defender for Cloud alert logs
.
Select
Webhook
as the
Source type
.
Select
Microsoft Defender for Cloud
as the
Log type
.
Click
Next
.
Optional: specify values for the following input parameters:
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
: Specify the API key as a header instead of specifying it in the URL. If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
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
Create Azure Logic App
Sign in to Azure Portal (https://portal.azure.com).
Click
Create a resource
and search for
Logic App
.
Click
Create
to start the deployment process.
Configure Logic App:
Name
: Provide a descriptive name for the Logic App (for example,
GoogleSecOpsWebhook
).
Subscription
: Select the appropriate subscription.
Resource Group
: Choose an existing resource group or create a new one.
Location
: Choose the location closest to your environment.
Log Analytics
: Enable this option if you want to log diagnostic data for the Logic App.
Click
Review + Create
to create the Logic App.
Click
Create
to deploy the Logic App.
Configure Azure Logic App Webhook connection
Go to the Logic App created in the previous step.
Click
Development Tools
>
Logic App Designer
.
Click
Add a trigger
.
Search
Microsoft Defender for Cloud
>
When a Microsoft Defender for Cloud alert is created or triggered
as the trigger.
Click
Create new
and follow the prompts to authenticate.
Click
Insert a new step
to add a new step to the workflow.
Click
Add an action
.
Search for
HTT
.
Select
HTTP
as the action.
Configure the HTTP action:
URI
: This is where you'll enter the Google SecOps API endpoint URL.
Method
:
POST
Add Content-Type header
: Set the
Content-Type
as header key and
application/json
as header value. This tells Google SecOps the format of the data being sent.
Add API Key to queries
: Set the
key
as the first query key and
<API_KEY>
as the query value.
API_KEY
is the generated API Key value during Google SecOps Feed configuration.
Add Secret Key to queries
: Set the
secret
as the second query key and
<SECRET_KEY>
as the query value.
SECRET_KEY
is the generated Secret Key during Google SecOps Feed configuration.
Set Body from previous step
: Click
Enter request content
>
click
Enter the data from previous steps
(button with lightning icon to the left of the input field).
Click
Save
.
Configure Microsoft Defender Cloud Alerts Webhook
Go to
Microsoft Defender for Cloud
.
Click
Management
>
Workflow automation
.
Click
Add workflow automation
.
Name
: Provide a descriptive name for the automation rule (for example,
ForwardAlertsToGoogleSecOps
).
Resource Group
: Choose an existing resource group.
Defender for Cloud data type
: Choose
Security alert
.
Alert severity
: Choose
Select all
.
Show Logic App instances from the following subscriptions
: Choose the subscription where the Logic App was created.
Select Logic App
: Choose the Logic App created in the previous steps.
Click
Create
to save the workflow automation.
Supported Microsoft Defender For Cloud sample logs
Standard Security Alert
{
"AlertLink"
:
"https://portal.azure.com/#blade/AlertDetails/alertId/2517_9b56-1701fd72392b/"
"subscriptionId/00000000-0000-0000-0000-000000000000/"
,
"AlertName"
:
"[SAMPLE] Unusual data extraction"
,
"AlertSeverity"
:
"Low"
,
"CompromisedEntity"
:
"prod-storage-account"
,
"Description"
:
"Realistic simulation of data exfiltration."
,
"Entities"
:
[
{
"$id"
:
"1"
,
"Address"
:
"192.168.1.50"
,
"Location"
:
{
"CountryCode"
:
"US"
,
"City"
:
"New York"
},
"Type"
:
"ip"
},
{
"$id"
:
"2"
,
"ResourceName"
:
"prod-storage-account"
,
"Type"
:
"azure-resource"
}
],
"ExtendedProperties"
:
{
"Client location"
:
"New York, US"
,
"User agent"
:
"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
,
"Operations types"
:
"GetBlob"
},
"ProductName"
:
"Microsoft Defender for Cloud"
,
"ResourceId"
:
"/subscriptions/00000000-0000-0000-0000-000000000000/resourcegroups/Security-RG/"
"providers/microsoft.storage/storageaccounts/prod-storage-account"
,
"SystemAlertId"
:
"25171206_5e67b569-b870-4429-91e6-1701fd72392b"
,
"TenantId"
:
"11111111-1111-1111-1111-111111111111"
,
"TimeGenerated"
:
"2026-02-24T12:00:00Z"
}
Advanced Hunting Record
{
"records"
:
[
{
"time"
:
"2026-02-24T10:30:00Z"
,
"tenantId"
:
"11111111-1111-1111-1111-111111111111"
,
"operationName"
:
"Publish"
,
"category"
:
"AdvancedHunting-CloudAppEvents"
,
"properties"
:
{
"ActionType"
:
"SendAs"
,
"AccountDisplayName"
:
"John Doe"
,
"AccountObjectId"
:
"abc-123-def-456"
,
"IPAddress"
:
"10.0.0.25"
,
"UserAgent"
:
"Client=MSExchangeRPC"
,
"ActivityObjects"
:
[
{
"Type"
:
"User"
,
"Role"
:
"Actor"
,
"Name"
:
"John Doe"
,
"Id"
:
"user-object-id-001"
}
],
"RawEventData"
:
{
"ClientIP"
:
"10.0.0.25"
,
"MailboxOwnerUPN"
:
"john.doe@company.com"
,
"Operation"
:
"SendAs"
,
"OrganizationName"
:
"company.onmicrosoft.com"
},
"Application"
:
"Microsoft Exchange Online"
}
}
]
}
Agentless Malware Alert
{
"VendorName"
:
"Microsoft"
,
"AlertType"
:
"VM.Agentless_MalwareWasDetected"
,
"ProductName"
:
"MDC Agentless Antimalware"
,
"Severity"
:
"High"
,
"CompromisedEntity"
:
"web-srv-01"
,
"Entities"
:
[
{
"$id"
:
"4"
,
"HostName"
:
"web-srv-01"
,
"Type"
:
"host"
},
{
"$id"
:
"5"
,
"Directory"
:
"/var/www/html/uploads"
,
"Name"
:
"malicious_script.sh"
,
"FileHashes"
:
[
{
"Algorithm"
:
"SHA256"
,
"Value"
:
"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
],
"Type"
:
"file"
}
],
"ExtendedProperties"
:
{
"Machine Name"
:
"web-srv-01"
,
"Threat Category"
:
"Trojan"
,
"EffectiveSubscriptionId"
:
"00000000-0000-0000-0000-000000000000"
}
}
IoT Security Alert
{
"DisplayName"
:
"Unauthorized BACNet Object Access"
,
"AlertSeverity"
:
"Medium"
,
"ProviderName"
:
"IoTSecurity"
,
"AlertType"
:
"IoT_ObjectServiceWhiteList"
,
"ExtendedProperties"
:
{
"SourceDevice"
:
"PLC_10.10.10.5"
,
"DestinationDevice"
:
"HMI_Console_01"
,
"Protocol"
:
"BACNet"
,
"SourceDeviceAddress"
:
"10.10.10.5"
,
"DestinationDeviceAddress"
:
"10.10.10.100"
},
"Entities"
:
[
{
"DeviceId"
:
"iot-uid-789"
,
"DeviceName"
:
"PLC_10.10.10.5"
,
"Owners"
:
[
"ot-admin@factory.com"
],
"MacAddress"
:
"00-11-22-33-44-55"
,
"Type"
:
"iotdevice"
}
]
}
UDM Mapping Table
Log Field
UDM Mapping
Logic
AlertLink
principal.resource.attribute.labels.AlertLink.value
Directly mapped.
AlertName
security_result.rule_name
Directly mapped.
AlertSeverity
security_result.severity
Directly mapped if value is one of HIGH, MEDIUM, LOW, CRITICAL, UNKNOWN_SEVERITY. Otherwise mapped to
security_result.severity_details
. Value is converted to uppercase before comparison.
AlertType
security_result.threat_name
Directly mapped.
CompromisedEntity
principal.resource.attribute.labels.CompromisedEntity.value
Directly mapped.
Description
security_result.description
Directly mapped.
DisplayName
security_result.summary
Directly mapped.
EndTime
about.resource.attribute.labels.EndTime.value
Directly mapped.
Entities[].Location.City
principal.location.city
Directly mapped.
Entities[].Location.CountryName
principal.location.country_or_region
Directly mapped.
ExtendedLinks[].Category
about.resource.attribute.labels.extendedLink_Category.value
Directly mapped.
ExtendedLinks[].Href
about.resource.attribute.labels.extendedLink_Href.value
Directly mapped.
ExtendedLinks[].Label
about.resource.attribute.labels.extendedLink_Label.value
Directly mapped.
ExtendedLinks[].Type
about.resource.attribute.labels.extendedLink_Type.value
Directly mapped.
ExtendedProperties.Account Session Id
network.session_id
Directly mapped after renaming to
accountSessionId
.
ExtendedProperties.Alert Id
metadata.product_log_id
Directly mapped after renaming to
alertId
.
ExtendedProperties.Authentication type
extensions.auth.auth_details
Directly mapped after renaming to
authenticationType
.
ExtendedProperties.Client Application
principal.application
Directly mapped after renaming to
clientApplication
.
ExtendedProperties.Client Hostname
principal.asset.hostname
,
principal.hostname
Directly mapped after renaming to
clientHostName
.
ExtendedProperties.Client IP address
principal.asset.ip
,
principal.ip
Directly mapped after renaming to
clientIpAddress
.
ExtendedProperties.Client IP location
principal.location.country_or_region
Directly mapped after renaming to
clientIpLocation
.
ExtendedProperties.Client Location
principal.location.country_or_region
Directly mapped after renaming to
clientLocation
.
ExtendedProperties.Client Principal Name
principal.user.userid
Directly mapped after renaming to
clientPrincipalName
.
ExtendedProperties.Compromised Host
principal.asset.hostname
,
principal.hostname
Directly mapped after renaming to
compromisedHost
.
ExtendedProperties.Suspicious Command Line
target.process.command_line
Directly mapped after renaming to
suspiciousCommandLine
.
ExtendedProperties.Suspicious Process
target.process.file.full_path
Directly mapped after renaming to
suspiciousProcess
.
ExtendedProperties.Suspicious Process Id
target.process.pid
Directly mapped after renaming to
suspiciousProcessId
.
ExtendedProperties.User agent
network.http.user_agent
Directly mapped after renaming to
userAgent
.
ExtendedProperties.User Name
principal.user.user_display_name
Directly mapped after renaming to
userName
.
ExtendedProperties.resourceType
principal.resource.name
Directly mapped.
IsIncident
security_result.detection_fields.IsIncident.value
Directly mapped. Converted to string.
ProcessingEndTime
about.resource.attribute.labels.ProcessingEndTime.value
Directly mapped.
ProductName
metadata.product_name
Directly mapped.
ResourceId
principal.resource.product_object_id
Directly mapped.
SourceSystem
security_result.detection_fields.SourceSystem.value
Directly mapped.
StartTime
about.resource.attribute.labels.StartTime.value
Directly mapped.
Status
security_result.detection_fields.Status.value
Directly mapped.
SystemAlertId
metadata.product_log_id
Directly mapped.
Tactics
security_result.attack_details.tactics.name
Directly mapped.
TenantId
additional.fields.TenantId.string_value
Directly mapped.
TimeGenerated
about.resource.attribute.labels.TimeGenerated.value
Directly mapped.
VendorName
metadata.vendor_name
Directly mapped.
WorkspaceResourceGroup
target.resource.attribute.labels.WorkspaceResourceGroup.value
Directly mapped.
WorkspaceSubscriptionId
target.resource.attribute.labels.WorkspaceSubscriptionId.value
Directly mapped.
_Internal_WorkspaceResourceId
target.resource.product_object_id
Directly mapped.
properties.alertDisplayName
security_result.rule_name
Directly mapped.
properties.alertType
security_result.threat_name
Directly mapped.
properties.alertUri
principal.resource.attribute.labels.AlertUri.value
Directly mapped.
properties.correlationKey
principal.resource.attribute.labels.correlationKey.value
Directly mapped.
properties.description
security_result.description
Directly mapped.
properties.endTimeUtc
additional.fields.EndTime.string_value
Directly mapped.
properties.entities[].location.city
principal.location.city
Directly mapped.
properties.entities[].location.countryName
principal.location.country_or_region
Directly mapped.
properties.entities[].location.latitude
principal.location.region_coordinates.latitude
Directly mapped. Converted to float.
properties.entities[].location.longitude
principal.location.region_coordinates.longitude
Directly mapped. Converted to float.
properties.extendedProperties.alert_Id
metadata.product_log_id
Directly mapped.
properties.extendedProperties.clientApplication
principal.application
Directly mapped.
properties.extendedProperties.clientIpAddress
principal.asset.ip
,
principal.ip
Directly mapped. Parsed as IP address.
properties.extendedProperties.clientLocation
principal.location.country_or_region
Directly mapped.
properties.extendedProperties.clientPrincipalName
principal.user.userid
Directly mapped.
properties.extendedProperties.compromisedEntity
principal.resource.attribute.labels.CompromisedEntity.value
Directly mapped.
properties.extendedProperties.resourceType
principal.resource.name
Directly mapped.
properties.IsIncident
security_result.detection_fields.isIncident.value
Directly mapped. Converted to string.
properties.productName
metadata.product_name
Directly mapped.
properties.resourceIdentifiers[].<key>
additional.fields.<key>_<index>.string_value
Directly mapped. Keys
$id
and
type
are appended with the index of the element in the array.
properties.severity
security_result.severity
Directly mapped if value is one of HIGH, MEDIUM, LOW, CRITICAL, UNKNOWN_SEVERITY. Otherwise mapped to
security_result.severity_details
. Value is converted to uppercase before comparison.
properties.startTimeUtc
additional.fields.StartTime.string_value
Directly mapped.
properties.status
security_result.detection_fields.Status.value
Directly mapped.
properties.timeGeneratedUtc
additional.fields.TimeGenerated.string_value
Directly mapped. Set to "MICROSOFT_DEFENDER_CLOUD_ALERTS" if not provided in the log. Set to "MICROSOFT_DEFENDER_CLOUD_ALERTS". Set to "USER_RESOURCE_ACCESS" if principal or target are present, otherwise set to "GENERIC_EVENT".
Need more help?
Get answers from Community members and Google SecOps professionals.
