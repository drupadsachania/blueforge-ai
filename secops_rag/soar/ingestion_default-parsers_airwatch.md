# Collect VMware Airwatch logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/airwatch/  
**Scraped:** 2026-03-05T10:02:10.117864Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect VMware Airwatch logs
Supported in:
Google secops
SIEM
This document explains how to ingest VMware Airwatch (VMware Workspace ONE UEM) logs to Google Security Operations using Bindplane. The parser extracts security event data from the logs in various formats (SYSLOG + KV, CEF). It first attempts to parse the log message using a series of Grok patterns specific to AirWatch log structures, then extracts key-value pairs from the event data and maps them to the Unified Data Model (UDM) fields, categorizing events and enriching them with contextual information for security analysis.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Windows 2016 or later or a Linux host with
systemd
If running behind a proxy, ensure firewall
ports
are open
Privileged access to VMware Airwatch
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
. Save the file securely on the
system where Bindplane will be installed.
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
Install the Bindplane agent
Install the Bindplane agent on your Windows or Linux operating system according
to the following instructions.
Windows installation
Open the
Command Prompt
or
PowerShell
as an administrator.
Run the following command:
msiexec
/
i
"https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi"
/
quiet
Linux installation
Open a terminal with root or sudo privileges.
Run the following command:
sudo
sh
-c
"
$(
curl
-fsSlL
https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh
)
"
install_unix.sh
Additional installation resources
For additional installation options, consult the
installation guide
.
Configure the Bindplane agent to ingest Syslog and send to Google SecOps
Access the configuration file:
Locate the
config.yaml
file. Typically, it's in the
/etc/bindplane-agent/
directory on Linux or in the installation directory on Windows.
Open the file using a text editor (for example,
nano
,
vi
, or Notepad).
Edit the
config.yaml
file as follows:
receivers
:
udplog
:
# Replace the port and IP address as required
listen_address
:
"0.0.0.0:514"
exporters
:
chronicle/chronicle_w_labels
:
compression
:
gzip
# Adjust the path to the credentials file you downloaded in Step 1
creds_file_path
:
'/path/to/ingestion-authentication-file.json'
# Replace with your actual customer ID from Step 2
customer_id
:
<
customer_id
>
endpoint
:
malachiteingestion-pa.googleapis.com
# Add optional ingestion labels for better organization
log_type
:
'AIRWATCH'
raw_log_field
:
body
ingestion_labels
:
service
:
pipelines
:
logs/source0__chronicle_w_labels-0
:
receivers
:
-
udplog
exporters
:
-
chronicle/chronicle_w_labels
Replace the port and IP address as required in your infrastructure.
Replace
<customer_id>
with the actual customer ID.
Update
/path/to/ingestion-authentication-file.json
to the path where the authentication file was saved in the
Get Google SecOps ingestion authentication file
section.
Restart the Bindplane agent to apply the changes
To restart the Bindplane agent in
Linux
, run the following command:
sudo
systemctl
restart
bindplane-agent
To restart the Bindplane agent in
Windows
, you can either use the
Services
console or enter the following command:
net stop BindPlaneAgent && net start BindPlaneAgent
Configure Syslog for VMware Airwatch (VMware Workspace ONE UEM)
Sign in to the
VMware AirWatch
web UI.
Go to
Monitor
>
Reports and Analytics
>
Events
>
Syslog
.
Provide the following configuration details:
Syslog Integration
: Select
Enabled
.
Hostname
: Enter the Bindplane agent IP address.
Protocol
: Select
UDP
.
Port
: Enter the Bindplane agent port number.
Message Tag
: Enter
Airwatch
.
Message Content
: Leave as default.
Go to the
Advanced
tab.
Provide the following configuration details:
Console Events
: Select
Enable
.
Select Console Events to Send to Syslog
: Click
Select All
.
Device Events
: Select
Enable
.
Select Device Events to Send to Syslog
: Click
Select All
.
Click
Save
.
Click
Test Connection
.
UDM Mapping Table
Log field
UDM mapping
Logic
AdminAccount
principal.user.userid
The value is taken from the AdminAccount field in the raw log.
Application
target.application
The value is taken from the Application field in the raw log.
ApplicationUUID
additional.fields[].value.string_value
The value is taken from the ApplicationUUID field in the raw log. The key is set to "ApplicationUUID".
BytesReceived
network.received_bytes
The value is taken from the BytesReceived field in the raw log.
Device
target.hostname
The value is taken from the Device field in the raw log.
DeviceEventLogDescription
metadata.description
The value is taken from the DeviceEventLogDescription field in the raw log.
Enrollment User
principal.user.userid
The value is taken from the Enrollment User field in the raw log when the event_name is one of: AppCatalogLaunch, InstallApplicationConfirmed, InstallProfileConfirmed, BreakMDMConfirmed, DeviceOperatingSystemChanged, RemoveProfileConfirmed, CertificateIssued, CompromisedStatusChanged, AppListSampleRefused, CertificateListSampleRefused, DeviceInformationRefused, ProfileListRefused, SecurityInformation, SecureChannelCheckIn, SecurityInformationConfirmed, StartACMConfirmed, DeviceAttributeDeviceMCCModified, DeviceAttributePhoneNumberModified, AvailableOSUpdatesList, AvailableOsUpdatesConfirmed.
Event Category
additional.fields[].value.string_value
The value is taken from the Event Category field in the raw log. The key is set to "Event Category".
Event Module
additional.fields[].value.string_value
The value is taken from the Event Module field in the raw log. The key is set to "Event Module".
Event Source
additional.fields[].value.string_value
The value is taken from the Event Source field in the raw log. The key is set to "Event Source".
Event Timestamp
metadata.event_timestamp.seconds
The value is taken from the Event Timestamp field in the raw log.
FriendlyName
target.hostname
The value is taken from the FriendlyName field in the raw log.
GroupManagementData
security_result.description
The value is taken from the GroupManagementData field in the raw log.
Hmac
additional.fields[].value.string_value
The value is taken from the Hmac field in the raw log. The key is set to "Hmac".
LoginSessionID
network.session_id
The value is taken from the LoginSessionID field in the raw log.
MessageText
metadata.description
The value is taken from the MessageText field in the raw log.
OriginatingOrganizationGroup
principal.user.group_identifiers
The value is taken from the OriginatingOrganizationGroup field in the raw log.
OwnershipType
additional.fields[].value.string_value
The value is taken from the OwnershipType field in the raw log. The key is set to "OwnershipType".
Profile
target.resource.name
The value is taken from the Profile field in the raw log.
ProfileName
target.resource.name
The value is taken from the ProfileName field in the raw log.
Request Url
target.url
The value is taken from the Request Url field in the raw log.
SmartGroupName
target.group.group_display_name
The value is taken from the SmartGroupName field in the raw log.
Tags
additional.fields[].value.string_value
The value is taken from the Tags field in the raw log. The key is set to "Tags".
User
target.user.userid
The value is taken from the User field in the raw log when the event_name is SSPUserLoginAttemptFailed.
event_name
metadata.product_event_type
The value is taken from the Event field in the raw log.
extensions.auth.type
The value is set to "SSO" when the event_name is one of: AdminUserLoggedIn, SSPUserLoginAttemptFailed, AdminUserLoggedOut, AuthTokenIssued, AuthTokenRevoked.
is_alert
The value is set to "true" when the event_name is one of: ComplianceStatusChanged, DeviceProfileTypeBlocked, ComplianceActionTaken.
is_significant
The value is set to "true" when the event_name is ComplianceStatusChanged.
is_significant
The value is set to "false" when the event_name is DeviceProfileTypeBlocked.
metadata.event_type
The value is set to "GENERIC_EVENT" when the event_name is SecureChannelCheckIn.
metadata.event_type
The value is set to "GROUP_CREATION" when the event_name is ApplicationGroupCreated.
metadata.event_type
The value is set to "GROUP_DELETION" when the event_name is SmartGroupsDeleted.
metadata.event_type
The value is set to "GROUP_MODIFICATION" when the event_name is one of: SmartGroupsModified, ApplicationGroupAssignmentModified.
metadata.event_type
The value is set to "NETWORK_CONNECTION" when the event_data field contains "session" and the hash_value field ends with "org".
metadata.event_type
The value is set to "NETWORK_CONNECTION" when the principal_hostname or src_ip fields are not empty and the target_hostname or target_ip fields are not empty.
metadata.event_type
The value is set to "SETTING_DELETION" when the event_name is Revoked and the event_data field does not contain "Certificate".
metadata.event_type
The value is set to "SETTING_MODIFICATION" when the event_name is one of: DeviceAttributeDeviceMCCModified, DeviceAttributePhoneNumberModified, ComplianceStatusChanged, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked.
metadata.event_type
The value is set to "STATUS_UNCATEGORIZED" when the event_name is one of: AppListSampleRefused, CertificateListSampleRefused, DeviceInformationRefused, ProfileListRefused, SecurityInformation, StartACMRequested, AvailableOSUpdatesList, AvailableOsUpdatesConfirmed, AvailableOsUpdatesRequested.
metadata.event_type
The value is set to "STATUS_UPDATE" when the event_name is one of: BreakMDMRequested, CertificateIssued, CompromisedStatusChanged, SecureChannelCheckIn, EditDevice.
metadata.event_type
The value is set to "USER_LOGOUT" when the event_name is one of: AdminUserLoggedOut, AuthTokenIssued, AuthTokenRevoked.
metadata.event_type
The value is set to "USER_LOGIN" when the event_name is one of: AdminUserLoggedIn, SSPUserLoginAttemptFailed.
metadata.event_type
The value is set to "USER_RESOURCE_ACCESS" when the request_url field is not empty.
metadata.event_type
The value is set to "USER_RESOURCE_ACCESS" when the event_name is AppCatalogLaunch.
metadata.event_type
The value is set to "USER_RESOURCE_CREATION" when the event_name is one of: ApplicationDownload, EnrollmentComplete, InstallApplicationConfirmed, InstallProfileConfirmed.
metadata.event_type
The value is set to "USER_RESOURCE_DELETION" when the event_name is one of: BreakMDMConfirmed, RemoveProfileConfirmed.
metadata.event_type
The value is set to "USER_RESOURCE_UPDATE_CONTENT" when the event_name is one of: ProfileModified, ProfilePublished, ProfileSetToInactive, ProfileVersionAdded, RestrictionPayloadModified, DeviceOperatingSystemChanged.
metadata.event_type
The value is set to "USER_RESOURCE_UPDATE_PERMISSIONS" when the event_name is EULAAccepted.
metadata.event_type
The value is set to "USER_UNCATEGORIZED" when the event_name is one of: Revoked, ComplianceNotificationSent, DeleteDeviceRequested, DeviceClearPasscodeRequested, DeviceWipeRequested, InstallApplicationRequested, ApplicationInstallOnDeviceRequested, RemoveApplicationRequested, SendMessageRequested, AddMissingUserCompletedEvent, AddMissingUserFailureEvent, ApplicationAdded, ApplicationDeleted, ApplicationRemoveFromDeviceRequested, ApplicationModified, ApplicationPublished, ApplicationPublishFailed, ApplicationPublishStarted, ApplicationVersionAdded, SyncGroupCompletedEvent, SyncGroupFailureEvent, SearchMissingUserCompleteEvent, SyncAdminFailure, SyncUserCompletedEvent, SyncUserFailureEvent, UserDeleted, HealthAttestationCertificateRequestConfirmed, WindowsDeviceCheckInMode, SampleResponseListReceived, HealthAttestationCertificateRequested, WindowsInformationConfirmed, RemoteManagement, HealthAttestationServerToServerSyncReqConfirmed, ScepThumbprintSampleConfirmed, HealthAttestationSampleRequestConfirmed, HealthAttestationServerToServerSyncRequested, HealthAttestationServerToServerSyncRequestFailed, WipeRequest, InstallApplicationFailed, OwnershipChanged, WipeConfirmed, FreshDeviceCreatedInDeviceState, UserSetToInactive, ExistingDeviceUpdatedInDeviceState, HealthAttestationCertificateRequestFailed, AppleOsXmdmDeviceTokenUpdate, DeviceUnenrolled, ScheduleOsUpdateResults, UserRoleAssignmentModified, UserModified, AppleTokenUpdateComplete, UserEnrollmentTokenCreated, ScheduleOsUpdatesConfirmed, OsUpdateStatusRequested, InstallProfileConfirmed, TagAssignmentChanged.
metadata.log_type
The value is set to "AIRWATCH".
metadata.product_name
The value is set to "AirWatch".
metadata.vendor_name
The value is set to "VMWare".
network.application_protocol
The value is set to "HTTP" when the application_protocol field contains "HTTP".
network.http.method
The value is taken from the method_url field in the raw log.
network.http.referral_url
The value is taken from the referral_url field in the raw log.
network.http.response_code
The value is taken from the http_status field in the raw log.
network.http.user_agent
The value is taken from the user_agent field in the raw log.
network.ip_protocol
The value is set to "TCP" when the protocol field is "TCP".
network.ip_protocol
The value is set to "UDP" when the protocol field is "UDP".
principal.administrative_domain
The value is taken from the domain field in the raw log when the event_name is one of: SmartGroupsDeleted, SmartGroupsModified, ProfileModified, ProfilePublished, ProfileSetToInactive, DeleteDeviceRequested, DeviceEnterpriseWipeRequested, InstallProfileRequested, RemoveProfileRequested, FindDeviceRequested, InstallApplicationRequested, ApplicationInstallOnDeviceRequested, RemoveApplicationRequested, SendMessageRequested, ApplicationAdded, ApplicationDeleted, ApplicationRemoveFromDeviceRequested, ApplicationModified, ApplicationPublished, ApplicationPublishFailed, ApplicationPublishStarted, ApplicationVersionAdded, UserDeleted.
principal.hostname
The value is taken from the hostname field in the raw log.
principal.ip
The value is taken from the sys_ip field in the raw log when the event_name is one of: AuthTokenIssued, AuthTokenRevoked, BreakMDMRequested, ComplianceNotificationSent, DeleteDeviceRequested, Revoked, ComplianceStatusChanged, CompliancePolicyModified, ProfileModified, ProfilePublished, ProfileSetToInactive, SmartGroupsDeleted, ApplicationDownload, EnrollmentComplete, EULAAccepted, StartACMRequested, DeviceEnterpriseWipeRequested, InstallApplicationRequested, InstallProfileRequested, RemoveProfileRequested, ApplicationInstallOnDeviceRequested, FindDeviceRequested, RemoveApplicationRequested, SendMessageRequested, AvailableOsUpdatesRequested, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked, AddMissingUserCompletedEvent, AddMissingUserFailureEvent, ApplicationAdded, ApplicationDeleted, ApplicationGroupAssignmentModified, ApplicationGroupCreated, ApplicationRemoveFromDeviceRequested, ApplicationModified, ApplicationPublished, ApplicationPublishFailed, ApplicationPublishStarted, ApplicationVersionAdded, DeviceWipeRequested, ProfileVersionAdded, RestrictionPayloadModified, SmartGroupsModified, SyncGroupCompletedEvent, SyncGroupFailureEvent, SearchMissingUserCompleteEvent, SyncAdminFailure, SyncUserCompletedEvent, SyncUserFailureEvent, UserDeleted, HealthAttestationCertificateRequestConfirmed, WindowsDeviceCheckInMode, SampleResponseListReceived, HealthAttestationCertificateRequested, WindowsInformationConfirmed, RemoteManagement, HealthAttestationServerToServerSyncReqConfirmed, ScepThumbprintSampleConfirmed, HealthAttestationSampleRequestConfirmed, HealthAttestationServerToServerSyncRequested, HealthAttestationServerToServerSyncRequestFailed, WipeRequest, InstallApplicationFailed, OwnershipChanged, WipeConfirmed, FreshDeviceCreatedInDeviceState, UserSetToInactive, ExistingDeviceUpdatedInDeviceState, HealthAttestationCertificateRequestFailed, AppleOsXmdmDeviceTokenUpdate, DeviceUnenrolled, ScheduleOsUpdateResults, UserRoleAssignmentModified, UserModified, ComplianceActionTaken, AppleTokenUpdateComplete, UserEnrollmentTokenCreated, ScheduleOsUpdatesConfirmed, OsUpdateStatusRequested.
principal.process.pid
The value is taken from the process_id field in the raw log.
principal.user.group_identifiers
The value is taken from the auth_group field in the raw log when the event_name is one of: AuthTokenIssued, AuthTokenRevoked.
principal.user.user_display_name
The value is taken from the user_info field in the raw log.
principal.user.userid
The value is taken from the user_name field in the raw log when the event_name is one of: AuthTokenIssued, AuthTokenRevoked, BreakMDMRequested, ComplianceNotificationSent, DeleteDeviceRequested, Revoked, ComplianceStatusChanged, CompliancePolicyModified, ProfileModified, ProfilePublished, ProfileSetToInactive, SmartGroupsDeleted, ApplicationDownload, EnrollmentComplete, EULAAccepted, StartACMRequested, DeviceEnterpriseWipeRequested, InstallApplicationRequested, InstallProfileRequested, RemoveProfileRequested, ApplicationInstallOnDeviceRequested, FindDeviceRequested, RemoveApplicationRequested, SendMessageRequested, AvailableOsUpdatesRequested, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked, AddMissingUserCompletedEvent, AddMissingUserFailureEvent, ApplicationAdded, ApplicationDeleted, ApplicationGroupAssignmentModified, ApplicationGroupCreated, ApplicationRemoveFromDeviceRequested, ApplicationModified, ApplicationPublished, ApplicationPublishFailed, ApplicationPublishStarted, ApplicationVersionAdded, DeviceWipeRequested, ProfileVersionAdded, RestrictionPayloadModified, SmartGroupsModified, SyncGroupCompletedEvent, SyncGroupFailureEvent, SearchMissingUserCompleteEvent, SyncAdminFailure, SyncUserCompletedEvent, SyncUserFailureEvent, UserDeleted, HealthAttestationCertificateRequestConfirmed, WindowsDeviceCheckInMode, SampleResponseListReceived, HealthAttestationCertificateRequested, WindowsInformationConfirmed, RemoteManagement, HealthAttestationServerToServerSyncReqConfirmed, ScepThumbprintSampleConfirmed, HealthAttestationSampleRequestConfirmed, HealthAttestationServerToServerSyncRequested, HealthAttestationServerToServerSyncRequestFailed, WipeRequest, InstallApplicationFailed, OwnershipChanged, WipeConfirmed, FreshDeviceCreatedInDeviceState, UserSetToInactive, ExistingDeviceUpdatedInDeviceState, HealthAttestationCertificateRequestFailed, AppleOsXmdmDeviceTokenUpdate, DeviceUnenrolled, ScheduleOsUpdateResults, UserRoleAssignmentModified, UserModified, ComplianceActionTaken, AppleTokenUpdateComplete, UserEnrollmentTokenCreated, ScheduleOsUpdatesConfirmed, OsUpdateStatusRequested, EditDevice.
security_result.action
The value is set to "ALLOW" when the event_name is DeviceProfileTypeUnblocked.
security_result.action
The value is set to "BLOCK" when the event_name is one of: DeviceProfileTypeBlocked, SyncAdminFailure, SyncGroupFailureEvent, SyncUserFailureEvent.
security_result.category
The value is set to "AUTH_VIOLATION" when the event_name is SSPUserLoginAttemptFailed.
security_result.category
The value is set to "POLICY_VIOLATION" when the event_name is one of: ComplianceStatusChanged, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked, ComplianceNotificationSent, CompromisedStatusChanged.
security_result.category_details
The value is taken from the Event Category field in the raw log.
security_result.description
The value is taken from the des field in the raw log when the description field contains an IP address.
security_result.description
The value is taken from the description field in the raw log when the description field does not contain an IP address.
security_result.description
The value is set to "unexpected error occurred, check logs for details" when the event_name is SyncAdminFailure.
security_result.description
The value is taken from the GroupManagementData field in the raw log when the event_name is MergeGroupCompletedEvent.
security_result.summary
The value is taken from the summary field in the raw log.
target.administrative_domain
The value is taken from the domain field in the raw log when the event_name is CompliancePolicyModified.
target.application
The value is taken from the app_name field in the raw log when the event_name is one of: InstallApplicationRequested, ApplicationInstallOnDeviceRequested, RemoveApplicationRequested, ApplicationAdded, ApplicationDeleted, ApplicationRemoveFromDeviceRequested, ApplicationModified, ApplicationPublished, ApplicationPublishFailed, ApplicationPublishStarted, ApplicationVersionAdded, ApplicationDownload, InstallApplicationConfirmed.
target.asset_id
The value is set to "device_serial_number:device_udid" when the event_name is DeleteDeviceRequested and the device_serial_number and device_udid fields are not empty.
target.group.group_display_name
The value is taken from the ApplicationGroup field in the raw log when the event_name is one of: ApplicationGroupAssignmentModified, ApplicationGroupCreated.
target.hostname
The value is taken from the Device field in the raw log when the event_name is DeviceLocationGroupChanged.
target.ip
The value is taken from the sys_ip field in the raw log when the event_name is SSPUserLoginAttemptFailed.
target.ip
The value is taken from the target_ip field in the raw log when the event_name is one of: CompliancePolicyModified, CertificateIssued, CompromisedStatusChanged, AppListSampleRefused, CertificateListSampleRefused, DeviceInformationRefused, ProfileListRefused, SecurityInformation, SecureChannelCheckIn, SecurityInformationConfirmed, StartACMConfirmed, AdminUserLoggedIn, AdminUserLoggedOut, AvailableOSUpdatesList, AvailableOsUpdatesConfirmed.
target.port
The value is taken from the target_port field in the raw log.
target.resource.name
The value is set to "SETTING" when the event_name is one of: Revoked, CompliancePolicyModified, ComplianceStatusChanged, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked.
target.resource.type
The value is set to "APP" when the event_name is ApplicationDownload.
target.resource.type
The value is set to "DEVICE" when the event_name is EnrollmentComplete.
target.resource.type
The value is set to "EULA" when the event_name is EULAAccepted.
target.resource.type
The value is set to "OS" when the event_name is DeviceOperatingSystemChanged.
target.resource.type
The value is set to "PROFILE" when the event_name is InstallProfileConfirmed.
target.resource.type
The value is set to "SETTING" when the event_name is one of: Revoked, CompliancePolicyModified, ComplianceStatusChanged, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked.
target.url
The value is taken from the target_url field in the raw log when the method_url field is not empty.
target.user.group_identifiers
The value is taken from the auth_group field in the raw log when the event_name is one of: AuthTokenIssued, AuthTokenRevoked.
target.user.userid
The value is taken from the group_user field in the raw log when the event_name is one of: AddMissingUserCompletedEvent, AddMissingUserFailureEvent.
target.user.userid
The value is taken from the enrollment_user field in the raw log when the event_name is one of: BreakMDMRequested, ComplianceNotificationSent, DeleteDeviceRequested, Revoked, ComplianceStatusChanged, ApplicationDownload, EnrollmentComplete, EULAAccepted, StartACMRequested, DeviceEnterpriseWipeRequested, InstallApplicationRequested, InstallProfileRequested, RemoveProfileRequested, ApplicationInstallOnDeviceRequested, FindDeviceRequested, RemoveApplicationRequested, SendMessageRequested, AuthTokenIssued, AuthTokenRevoked, InstallApplicationConfirmed, InstallProfileConfirmed, BreakMDMConfirmed, DeviceOperatingSystemChanged, RemoveProfileConfirmed, DeviceAttributeDeviceMCCModified, DeviceAttributePhoneNumberModified, AvailableOsUpdatesRequested, DeviceProfileTypeBlocked, DeviceProfileTypeUnblocked, ApplicationRemoveFromDeviceRequested, DeviceClearPasscodeRequested, DeviceWipeRequested.
target.user.userid
The value is taken from the User field in the raw log when the event_name is UserDeleted.
Need more help?
Get answers from Community members and Google SecOps professionals.
