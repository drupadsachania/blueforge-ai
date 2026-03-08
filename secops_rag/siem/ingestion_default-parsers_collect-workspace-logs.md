# Collect Google Workspace logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-workspace-logs/  
**Scraped:** 2026-03-05T09:17:26.067014Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Google Workspace logs
Supported in:
Google secops
SIEM
This document describes how to ingest your Google Workspace logs into Google Security Operations. Sending these logs to Google SecOps lets you to use its security analytics capabilities for enhanced threat detection, investigation, and response across your Google Workspace environment.
You can ingest various log types from Google Workspace, including activity events, alerts, user information, and more. There are two primary methods available to bring this data into Google SecOps:
Native Ingestion
: This method provides a direct connection configured from the Google Workspace Admin console to Google SecOps. It is streamlined for specific log types but has particular Google Workspace license requirements.
Feed-based Ingestion
: This method uses the Feed Management feature within Google SecOps to regularly fetch logs from the Google Workspace APIs. This approach supports a wider range of Google Workspace log types.
The following sections detail each method, including their capabilities, prerequisites, limitations, and step-by-step configuration instructions, to help you make an informed decision.
This document also provides details on the supported Google Workspace log types and how the log fields from these sources map to the Google SecOps Unified Data Model (UDM), enabling you to understand how the data is normalized and can be utilized within Google SecOps.
Choosing Your Ingestion Method
The best method for your organization to ingest Google Workspace logs into Google SecOps depends on factors such as the specific log types you need, your current Google Workspace license, and your sensitivity to data latency. The following table summarizes the supported methods and key considerations for each Google Workspace log type:
Log Type (Ingestion Label)
Supported Ingestion Method(s)
Key Considerations
WORKSPACE_ACTIVITY
Native OR Feed
Native
: Near real-time ingestion. Requires a Google Workspace Enterprise license to access the Data Integrations feature within the Admin console Reporting section.
Feed
: Compatible with all Google Workspace log types. Subject to potential data latency.
WORKSPACE_ALERTS
Feed
Subject to potential data latency.
WORKSPACE_CHROMEOS
Feed
Subject to potential data latency.
WORKSPACE_GROUPS
Feed
Subject to potential data latency.
WORKSPACE_MOBILE
Feed
Subject to potential data latency.
WORKSPACE_PRIVILEGES
Feed
Subject to potential data latency.
WORKSPACE_USERS
Feed
Subject to potential data latency.
Key Differences
License Requirements
Native Ingestion for Google Workspace Activity logs (
WORKSPACE_ACTIVITY
) requires a Google Workspace Enterprise edition. This is because it leverages the Data Integrations functionality, which is part of the Enterprise offering.
Feed-based Ingestion is generally available across more Google Workspace editions as it uses the Google Workspace Reports API.
Data Latency
Native Ingestion offers a direct stream and is designed to deliver logs with lower latency, making it suitable for near real-time monitoring of activity events.
Feed-based Ingestion fetches data periodically. While configuration options exist, there's an inherent delay compared to the native method. The actual latency can vary based on the API and the log type. For more details on what to expect from the source, see
Google Workspace data retention and lag times
. Google SecOps feed configurations also influence the fetch schedule.
Supported Log Types
Only the WORKSPACE_ACTIVITY log type supports Native Ingestion.
Feed-based Ingestion supports all the listed Google Workspace log types, offering broader coverage across different data sources within Google Workspace.
Recommendation
If you have a Google Workspace Enterprise license and require Google Workspace Activity logs (
WORKSPACE_ACTIVITY
) in near real-time, Native Ingestion is the preferred method for that specific log type.
For all other log types (WORKSPACE_ALERTS, WORKSPACE_CHROMEOS, etc.), or if you don't have an Enterprise license for Google Workspace Activity logs (
WORKSPACE_ACTIVITY
), you must use the Feed-based Ingestion method.
If using the Feed method for Google Workspace Activity logs (
WORKSPACE_ACTIVITY
), be aware of the potential for data delays.
The following sections provide detailed instructions for configuring both Native Ingestion (for WORKSPACE_ACTIVITY) and Feed-based Ingestion.
Method 1: Configure Native Ingestion for WORKSPACE_ACTIVITY
This method streams Google Workspace Activity logs (
WORKSPACE_ACTIVITY
) directly from the Google Workspace Admin console to Google SecOps, offering nearly real time data. Multiple Workspace organizations can be mapped to a single SecOps instance through our native ingestion method. This method fully supports environments with multiple Google Workspace organizations; you can configure ingestion to collect activity logs from all associated Google Workspace organizations.
Native ingestion for WORKSPACE_ACTIVITY supports logs from the following Google application types:
Access Transparency
Accounts
Google Admin console
Google Calendar
Google Chat
Google Chrome
Classroom
Google Cloud
Access Context Manager
Looker Studio
Device
Google Drive
Gmail
Google Groups
Jamboard management
LDAP
Login
Google Meet
OAuth
Password Vault
Firewall Rules Logging
SAML
User accounts
Voice
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance
An enterprise version of Google Workspace
Obtain your Google SecOps instance ID and token
To obtain your Google SecOps instance ID and token, complete the following
steps from your Google SecOps account:
Open your Google SecOps instance.
From the navigation bar, select
Settings
.
Click
Google Workspace
.
Enter your Google Workspace Customer ID.
Click
Generate Token
.
Copy the token and your Google SecOps instance ID (located on the same
page).
Link Google Workspace to your Google SecOps instance
To send your Google Workspace data to your Google SecOps instance,
complete the following steps from the Google Workspace Admin console:
Open the Google Workspace Admin console.
Click
Reporting
.
Click
Data Integrations
.
Select
Google SecOps export
, and then click
Connect to
Google SecOps
. This opens the
Connect to Google SecOps
page.
Paste the token copied from your Google SecOps account into the
indicated field. Click
Connect
. Export audit data to Google SecOps
should now display
On
. Your Google Workspace account is now linked to
your Google SecOps instance and will begin sending your
Google Workspace data.
Click
Go to Google SecOps
to open your Google SecOps instance
and begin to monitor your Google Workspace data from Google SecOps. For more
information, see the
Data Ingestion and Health dashboard
.
Disconnect Google Workspace from Google SecOps
To disconnect your Google Workspace account from your Google SecOps
instance, complete the following steps:
Open the Google Workspace Admin console.
Click
Data Integrations
.
In the
Google SecOps export
panel, click
Disconnect from Google SecOps
.
Export audit data to Google SecOps
should now display
Off
.
What's next
The next step is to enable the
Cloud Threats category rules
sets
designed to help identify threats using Google Workspace data.
Method 2: Configure Feed-based Ingestion
This method uses Google SecOps Feed Management to periodically fetch logs from various Google Workspace APIs. As mentioned in the
Choosing Your Ingestion Method section
, this approach is necessary for all Google Workspace log types other than WORKSPACE_ACTIVITY, and it can also be used for WORKSPACE_ACTIVITY if you don't have an Enterprise license.
A typical deployment consists of Google Workspace and the Google Security Operations
feed configured to send logs to Google Security Operations. Each customer deployment
might differ and might be more complex.
The deployment contains the following components:
Google Workspace
. The Google Workspace platform from which you collect logs.
Google Security Operations feed
. The Google Security Operations feed that fetches logs
from Google Workspace and writes logs to Google Security Operations.
Google Security Operations
. Google Security Operations retains and analyzes the logs from
Google Workspace.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to Google Workspace parsers
with the following ingestion labels:
WORKSPACE_ACTIVITY
WORKSPACE_ALERTS
WORKSPACE_CHROMEOS
WORKSPACE_GROUPS
WORKSPACE_MOBILE
WORKSPACE_PRIVILEGES
WORKSPACE_USERS
Before you begin
Ensure that you have the following prerequisites:
Google Workspace Business Standard or Business Plus edition;
the Google Workspace parser supports both of these editions. For more information, see
Set up Google Workspace
.
Google Workspace Administrator account. For more information, see
Set up a Google Workspace administrator account
.
Enable the following APIs in your Google Cloud project:
Google Workspace Admin SDK
Alert Center API
To authenticate Google Workspace APIs, create a service account in your Google Cloud
project and take a note of the unique numeric ID and email address of the service account. For more information
about creating a service account, see
Creating and managing service accounts
.
Create a user that impersonates the service account, and then grant privileges to the user:
Sign in to Google Admin console.
Select
Directory
>
Users
and then click
Add new user
.
Enter the user details.
Click
Add new user
.
Click the newly created user link, and then
Admin roles and privileges
.
Click
expand_less
Expand less
.
Click
Create custom role
.
Click the
Create new role
and give this role a name.
Grant the following privileges to the role:
Privileges > Reports
Privileges > Services > Alert Center > Full Access > View access
Privileges > Services > Mobile Device Management > Manage Devices and Settings
Privileges > Services > Chrome Management > Settings
Admin API > Privileges > Users > Read
Admin API > Privileges > Groups > Read
Click
Continue
, and then
Create role
.
Click
Assign users
.
Select the user to assign the role.
Click
Assign role
.
The created user has the Super Admin role. For more information, see
How to assign a Super Admin role
.
Create access credentials. For more information about creating access credentials,
see
Create a service account key
.
Set up domain-wide delegation
for the service account to access data with the following scopes:
https://www.googleapis.com/auth/admin.reports.audit.readonly
https://www.googleapis.com/auth/apps.alerts
https://www.googleapis.com/auth/admin.directory.device.chromeos.readonly
https://www.googleapis.com/auth/admin.directory.group.readonly
https://www.googleapis.com/auth/admin.directory.device.mobile.readonly
https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly
https://www.googleapis.com/auth/admin.directory.user.readonly
To locate the Google Workspace customer ID, in the Google Admin console,
select
Account
>
Account Settings
>
Profile
.
All systems in the deployment architecture are configured
in the UTC time zone.
Verify the log types that the Google Security Operations parser supports. For information
about supported Google Workspace logs, see
Supported Google Workspace log types
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the Workspace Activity feed
To configure this log type, follow these steps:
Click the
Google Workspace
pack.
Locate the
Workspace Activities
log type.
Specify values for the following fields:
Source Type
: Third Party API
OAuth JWT endpoint
: contains the OAuth JSON Web Token.
Specify the
token_uri
value from the service account JSON key.
JWT claims issuer
: client ID. Specify the
client_email
value
from the service account JSON key. For example,
InsertServiceAccount@project.iam.gserviceaccount.com
JWT claims subject
: email address of the user that you created in the Google Workspace Admin console.
JWT claims audience
:
token_uri
value from the service account JSON key.
RSA private key
: key in PEM format. The PEM key is available
in the service account key file. When you enter the private key, include the
BEGIN PRIVATE KEY
header and the
END PRIVATE KEY
footer in the text box.
Customer ID
: for all log types, except the Alerts log type, the customer ID
field requires a leading 'C' character. If the customer ID field does not contain
a leading 'C' character, then prepend what the value with a 'C' character.
Applications
: required only when you create
a feed for Workspace Activities.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
Supported Google Workspace log types
The following sections list the log types that the Google Workspace parser supports:
WORKSPACE_ACTIVITY
The following table lists the supported application name and event types for the
WORKSPACE_ACTIVITY
log type.
Application name
Event type
Event name
Admin Console message
access_transparency
GSUITE_RESOURCE
ACCESS
Access to {RESOURCE_NAME} has been logged.
chrome
CHROME_OS_ADD_REMOVE_USER_TYPE
CHROME_OS_ADD_USER
{DEVICE_USER} has been added to ChromeOS device {DEVICE_NAME}
CHROME_OS_REMOVE_USER
{DEVICE_USER} has been removed from ChromeOS device {DEVICE_NAME} due to {REMOVE_USER_REASON}
DEVICE_BOOT_STATE_CHANGE_TYPE
DEVICE_BOOT_STATE_CHANGE
Device boot mode has changed from {PREVIOUS_BOOT_MODE} to {NEW_BOOT_MODE} mode for ChromeOS device {DEVICE_NAME}
CHROME_OS_LOGIN_LOGOUT_TYPE
CHROME_OS_LOGIN_FAILURE_EVENT
{DEVICE_USER} has attempted and failed to log into ChromeOS device {DEVICE_NAME} due to {LOGIN_FAILURE_REASON}
CHROME_OS_LOGIN_LOGOUT_EVENT
{DEVICE_USER} successfully logged in or out of device {DEVICE_NAME}
CHROME_OS_LOGIN_EVENT
{DEVICE_USER} has successfully logged into ChromeOS device {DEVICE_NAME}
CHROME_OS_LOGOUT_EVENT
{DEVICE_USER} has successfully logged out from ChromeOS device {DEVICE_NAME}
CHROME_OS_REPORTING_DATA_LOST_TYPE
CHROME_OS_REPORTING_DATA_LOST
An event was expected to be reported but failed to complete for device {DEVICE_NAME}
SAFE_BROWSING_PASSWORD_ALERT
PASSWORD_CHANGED
Password changed for {TRIGGER_USER}
PASSWORD_REUSE
Password reuse for {TRIGGER_USER}
DLP_EVENTS_TYPE
DLP_EVENT
Data access control rule triggered by ChromeOS
CONTENT_TRANSFER_TYPE
CONTENT_TRANSFER
Content was transfered
CONTENT_UNSCANNED_TYPE
CONTENT_UNSCANNED
The transfered content was not scanned because of {EVENT_REASON_ENUM_TYPE}
EXTENSION_REQUEST_TYPE
EXTENSION_REQUEST
Request for extension {APP_NAME} was received
LOGIN_EVENT_TYPE
LOGIN_EVENT
A login was performed
MALWARE_TRANSFER_TYPE
MALWARE_TRANSFER
Malware was detected in the transferred content for {TRIGGER_USER}
PASSWORD_BREACH_TYPE
PASSWORD_BREACH
A user's password was breached
SENSITIVE_DATA_TRANSFER_TYPE
SENSITIVE_DATA_TRANSFER
Sensitive data was detected in the transferred content for {TRIGGER_USER}
UNSAFE_SITE_VISIT_TYPE
UNSAFE_SITE_VISIT
Unsafe site visit warning shown for {TRIGGER_USER}
context_aware_access
CONTEXT_AWARE_ACCESS_USER_EVENT
ACCESS_DENY_EVENT
{USER_NAME} access denied
ACCESS_DENY_INTERNAL_ERROR_EVENT
{USER_NAME} access denied internal error
gplus
comment_change
create_comment
{actor} added a comment to a {post_visibility} post
delete_comment
{actor} removed a comment from a {post_visibility} post
edit_comment
{actor} edited a comment on a {post_visibility} post
plusone_change
add_plusone
{actor} added a like to a {post_visibility} {plusone_context}
remove_plusone
{actor} removed a like from a {post_visibility} {plusone_context}
poll_vote_change
add_poll_vote
{actor} added a vote to a {post_visibility} poll
remove_poll_vote
{actor} removed a vote from a {post_visibility} poll
post_change
create_post
{actor} created a {post_visibility} post
delete_post
{actor} deleted a post
content_manager_delete_post
{actor} deleted {post_author_name}'s post
edit_post
{actor} edited a {post_visibility} post
data_studio
ACCESS
ADD_REPORT_EMAIL_DELIVERY
{actor} added report email delivery
CREATE
{actor} created an asset
DATA_EXPORT
{actor} exported data as {DATA_EXPORT_TYPE}
DELETE
{actor} deleted an asset
DOWNLOAD_REPORT
{actor} downloaded a report as PDF
EDIT
{actor} edited an asset
RESTORE
{actor} restored an asset
STOP_REPORT_EMAIL_DELIVERY
{actor} stopped report email delivery
TRASH
{actor} trashed an asset
UPDATE_REPORT_EMAIL_DELIVERY
{actor} updated report email delivery
VIEW
{actor} viewed an asset
ACL_CHANGE
CHANGE_DATA_SOURCE_ACCESS_TYPE
{actor} changed access type from {OLD_VALUE} to {NEW_VALUE}
CHANGE_ASSET_LINK_SHARING_ACCESS_TYPE
{actor} changed link sharing access type from {OLD_VALUE} to {NEW_VALUE} for {TARGET_DOMAIN}
CHANGE_ASSET_LINK_SHARING_VISIBILITY
{actor} changed link sharing visibility from {OLD_VALUE} to {NEW_VALUE} for {TARGET_DOMAIN}
CHANGE_USER_ACCESS
{actor} changed sharing permissions for {TARGET_USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
mobile
device_applications
APPLICATION_EVENT
{APPLICATION_ID} version {NEW_VALUE} was {APPLICATION_STATE} {actor}'s {DEVICE_MODEL}
APPLICATION_REPORT_EVENT
{APPLICATION_ID} reported a status of severity:{APPLICATION_REPORT_SEVERITY} for application key:{APPLICATION_REPORT_KEY} with the message:'{APPLICATION_MESSAGE}'
device_updates
DEVICE_REGISTER_UNREGISTER_EVENT
{actor}'s account {ACCOUNT_STATE} {DEVICE_MODEL} {REGISTER_PRIVILEGE}
ADVANCED_POLICY_SYNC_EVENT
{POLICY_SYNC_TYPE} {POLICY_NAME} {NEW_VALUE}{VALUE} {DEVICE_TYPE} policy {POLICY_SYNC_RESULT} on {actor}'s {DEVICE_MODEL} with serial id {SERIAL_NUMBER}
DEVICE_ACTION_EVENT
{ACTION_TYPE} with id {ACTION_ID} on {actor}'s {DEVICE_MODEL} was {ACTION_EXECUTION_STATUS}
DEVICE_COMPLIANCE_CHANGED_EVENT
{actor}'s {DEVICE_MODEL} is {DEVICE_COMPLIANCE} {DEVICE_DEACTIVATION_REASON}
OS_UPDATED_EVENT
{OS_PROPERTY} updated on {actor}'s {DEVICE_MODEL} from {OLD_VALUE} to {NEW_VALUE}
DEVICE_OWNERSHIP_CHANGE_EVENT
Ownership of {actor}'s {DEVICE_MODEL} has changed to {DEVICE_OWNERSHIP}, with new device id {NEW_DEVICE_ID}
DEVICE_SETTINGS_UPDATED_EVENT
{DEVICE_SETTING} changed from {OLD_VALUE} to {NEW_VALUE} by {actor} on {DEVICE_MODEL}
APPLE_DEP_DEVICE_UPDATE_ON_APPLE_PORTAL_EVENT
Device with serial number {SERIAL_NUMBER} {DEVICE_STATUS_ON_APPLE_PORTAL} through Apple Device Enrollment
DEVICE_SYNC_EVENT
{actor}'s account synced on {DEVICE_MODEL}
RISK_SIGNAL_UPDATED_EVENT
{RISK_SIGNAL} updated on {actor}'s {DEVICE_MODEL} from {OLD_VALUE} to {NEW_VALUE}
ANDROID_WORK_PROFILE_SUPPORT_ENABLED_EVENT
Work profile is supported on {actor}'s {DEVICE_MODEL}
suspicious_activity
DEVICE_COMPROMISED_EVENT
{actor}'s {DEVICE_MODEL} {DEVICE_COMPROMISED_STATE}
FAILED_PASSWORD_ATTEMPTS_EVENT
{FAILED_PASSWD_ATTEMPTS} failed attempts to unlock {actor}'s {DEVICE_MODEL}
SUSPICIOUS_ACTIVITY_EVENT
{DEVICE_PROPERTY} changed on {actor}'s {DEVICE_MODEL} from {OLD_VALUE} to {NEW_VALUE}
calendar
calendar_change
change_calendar_acls
{actor} changed the access level on a calendar for {grantee_email} to {access_level}
change_calendar_country
{actor} changed the country of a calendar to {calendar_country}
create_calendar
{actor} created a new calendar
delete_calendar
{actor} deleted a calendar
change_calendar_description
{actor} changed the description of a calendar to {calendar_description}
change_calendar_location
{actor} changed the location of a calendar to {calendar_location}
change_calendar_timezone
{actor} changed the timezone of a calendar to {calendar_timezone}
change_calendar_title
{actor} changed the title of a calendar to {calendar_title}
notification
notification_triggered
{actor} triggered an {notification_method} notification of type {notification_type} to {recipient_email}
subscription_change
add_subscription
{actor} subscribed {subscriber_calendar_id} to {notification_type} notifications via {notification_method} for {calendar_id}
delete_subscription
{actor} unsubscribed {subscriber_calendar_id} from {notification_type} notifications via {notification_method} for {calendar_id}
event_change
create_event
{actor} created a new event {event_title}
delete_event
{actor} deleted the event {event_title}
add_event_guest
{actor} invited {event_guest} to {event_title}
change_event_guest_response_auto
{event_guest} auto-responded to the event {event_title} as {event_response_status}
remove_event_guest
{actor} uninvited {event_guest} from {event_title}
change_event_guest_response
{actor} changed the response of guest {event_guest} for the event {event_title} to {event_response_status}
change_event
{actor} modified {event_title}
remove_event_from_trash
{actor} removed the event {event_title} from trash
restore_event
{actor} restored the event {event_title}
change_event_start_time
{actor} changed the start time of {event_title}
change_event_title
{actor} changed the title of {old_event_title} to {event_title}
transfer_event_completed
{actor} accepted ownership of the event {event_title}
transfer_event_requested
{actor} requested transferring ownership of the event {event_title} to {grantee_email}
interop
interop_freebusy_lookup_outbound_successful
{actor} successfully fetched availability of Exchange calendar {calendar_id}
interop_freebusy_lookup_inbound_successful
Exchange Server at {IP_ADDRESS_IDENTIFIER} acting as {actor} successfully fetched availability for Google calendar {calendar_id}
interop_exchange_resource_availability_lookup_successful
{actor} successfully attempted to fetch availability of {calendar_id}
interop_exchange_resource_list_lookup_successful
{actor} successfully fetched Exchange resource list from {remote_ews_url}
interop_freebusy_lookup_outbound_unsuccessful
{actor} unsuccessfully attempted to fetch availability of Exchange calendar {calendar_id}
interop_freebusy_lookup_inbound_unsuccessful
Exchange Server at {IP_ADDRESS_IDENTIFIER} acting as {actor} unsuccessfully attempted to fetch availability for Google calendar {calendar_id}
interop_exchange_resource_availability_lookup_unsuccessful
{actor} unsuccessfully attempted to fetch availability of {calendar_id}
interop_exchange_resource_list_lookup_unsuccessful
{actor} unsuccessfully fetched Exchange resource list from {remote_ews_url}
drive
access
deny_access_request
{actor} denied an access request for {target_user}
expire_access_request
An access request for {target_user} expired
request_access
{actor} requested access to an item for {target_user}
add_to_folder
{actor} added an item to {destination_folder_title}
approval_canceled
{actor} canceled an approval on an item
approval_comment_added
{actor} added a comment on an approval on an item
approval_completed
An approval was completed
approval_decisions_reset
Approval decisions were reset
approval_due_time_change
{actor} requested a due time change on an approval
approval_requested
{actor} requested approval on an item
approval_reviewer_change
{actor} requested a reviewer change on an approval
approval_reviewer_responded
{actor} reviewed an approval on an item
create_comment
{actor} created a comment
delete_comment
{actor} deleted a comment
edit_comment
{actor} edited a comment
reassign_comment
{actor} reassigned a comment
reopen_comment
{actor} reopened a comment
resolve_comment
{actor} resolved a comment
connected_sheets_query
{execution_trigger} {query_type} query executed
copy
{actor} created a copy of original document {old_value}
create
{actor} created an item
delete
{actor} deleted an item
download
{actor} downloaded an item
email_as_attachment
{actor} shared this document as an email attachment to {target}
edit
{actor} edited an item
email_collaborators
{actor} emailed collaborators of an item
download_forms_response
{actor} downloaded forms responses
access_item_content
An application accessed an item's content on behalf of {actor}
sync_item_content
{actor} synced item content
label_added
{actor} applied Label {label_title}.
label_added_by_item_create
Label {label_title} was automatically applied on creation.
label_field_changed
{actor} changed the value of field {field} (Label: {label_title}) from '{old_value}' to '{new_value}'.
label_removed
{actor} removed Label {label_title}.
add_lock
{actor} locked an item
move
{actor} moved an item from {source_folder_title} to {destination_folder_title}
preview
{actor} previewed an item
print
{actor} printed an item
remove_from_folder
{actor} removed an item from {source_folder_title}
rename
{actor} renamed {old_value} to {new_value}
untrash
{actor} restored an item
sheets_import_url
A url was imported from this item
sheets_import_range
{sheets_import_range_recipient_doc} imported range from an item
source_copy
{actor} copied this item, creating a new item {copy_type} your organization {new_value}
accept_suggestion
{actor} accepted a suggestion
create_suggestion
{actor} created a suggestion
delete_suggestion
{actor} deleted a suggestion
reject_suggestion
{actor} rejected a suggestion
trash
{actor} trashed an item
remove_lock
{actor} unlocked an item
unmovable_item_reparented
When a parent folder was moved, an item that couldn't be moved was relocated from {source_folder_title} to {destination_folder_title}
upload
{actor} uploaded an item
access_url
A script accessed a url during execution
view
{actor} viewed an item
acl_change
apply_security_update
{actor} applied the security update to a file
shared_drive_apply_security_update
{actor} applied the security update to all files in a shared drive
shared_drive_remove_security_update
{actor} removed the security update from all files in a shared drive
change_owner_hierarchy_reconciled
Due to a change in a parent folder, the owner of an item was changed
change_owner
{actor} changed owner of an item
publish_change
{actor} changed publish status from {old_value} to {new_value} and changed visibility from {old_publish_visibility} to {new_publish_visibility}
change_acl_editors
{actor} changed editor settings from {old_value} to {new_value}
change_document_access_scope
{actor} changed link sharing access type from {old_value} to {new_value} for {target_domain}
change_document_access_scope_hierarchy_reconciled
{actor} changed link sharing access type from {old_value} to {new_value} for {target_domain}
change_document_visibility
{actor} changed link sharing visibility from {old_value} to {new_value} for {target_domain}
change_document_visibility_hierarchy_reconciled
Due to a change in a parent folder, the link sharing visibility for {target_domain} changed from {old_value} to {new_value}
publish_new_version
{actor} published a new version
remove_security_update
{actor} removed the security update from a file
shared_drive_membership_change
{actor} made a membership change of type {membership_change_type} for {target} by removing role(s) {removed_role} and adding role(s) {added_role}
shared_drive_settings_change
{actor} changed {shared_drive_settings_change_type} setting from {old_settings_state} to {new_settings_state}
sheets_import_range_access_change
{actor} enabled Sheets range import to {sheets_import_range_recipient_doc}
change_user_access
{actor} changed sharing permissions for {target_user} from {old_value} to {new_value}
change_user_access_hierarchy_reconciled
Due to a change in a parent folder, the sharing permissions for {target_user} changed from {old_value} to {new_value}
pooled_quota_metadata
storage_usage_update
Storage usage update for {actor}
groups
acl_change
change_acl_permission
{actor} changed {acl_permission} from {old_value_repeated} to {new_value_repeated} in group {group_email}
moderator_action
accept_invitation
{actor} accepted an invitation to group {group_email}
approve_join_request
{actor} approved join request from {user_email} to group {group_email}
join
{actor} added himself or herself to group {group_email}
request_to_join
{actor} requested to join group {group_email}
change_basic_setting
{actor} changed {basic_setting} from {old_value} to {new_value} in group {group_email}
create_group
{actor} created group {group_email}
delete_group
{actor} deleted group {group_email}
change_email_subscription_type
{actor} in group {group_email} changed the email subscription type for user {user_email} from {old_value} to {new_value}
change_identity_setting
{actor} changed {identity_setting} from {old_value} to {new_value} in group {group_email}
add_info_setting
{actor} added {info_setting} with value {value} in group {group_email}
change_info_setting
{actor} changed {info_setting} from {old_value} to {new_value} in group {group_email}
remove_info_setting
{actor} removed {info_setting} with value {value} in group {group_email}
change_new_members_restrictions_setting
{actor} changed {new_members_restrictions_setting} from {old_value} to {new_value} in group {group_email}
change_post_replies_setting
{actor} changed {post_replies_setting} from {old_value} to {new_value} in group {group_email}
change_spam_moderation_setting
{actor} changed {spam_moderation_setting} from {old_value} to {new_value} in group {group_email}
change_topic_setting
{actor} changed {topic_setting} from {old_value} to {new_value} in group {group_email}
moderate_message
{actor} moderated message in {group_email} with action: {message_moderation_action} and result: {status}. Message details: Message Id: {message_id}
always_post_from_user
{actor} made posts from {user_email} to always be posted in {group_email} with result: {status}
add_user
{actor} added {user_email} to group {group_email} with role {member_role}
ban_user_with_moderation
{actor} banned user {user_email} from group {group_email} with result: {status} during message moderation
revoke_invitation
{actor} revoked invitation to {user_email} from group {group_email}
invite_user
{actor} invited {user_email} to group {group_email}
reject_join_request
{actor} rejected join request from {user_email} to group {group_email}
reinvite_user
{actor} reinvited {user_email} to group {group_email}
remove_user
{actor} removed {user_email} from group {group_email}
unsubscribe_via_mail
{actor} unsubscribed group {group_email} via mail command
keep
user_action
deleted_attachment
{actor} deleted an attachment
uploaded_attachment
{actor} uploaded an attachment
edited_note_content
{actor} edited note content
created_note
{actor} created a note
deleted_note
{actor} deleted a note
modified_acl
{actor} edited permissions
meet
call
abuse_report_submitted
A participant submitted an abuse report in a meeting.
call_ended
The endpoint left a video meeting
livestream_watched
The viewer watched a livestream of a meeting on view page.
conference_action
dialed_out
The endpoint performed an action that requires to be reported
invitation_sent
The endpoint performed an action that requires to be reported
knocking_accepted
The endpoint performed an action that requires to be reported
knocking_denied
The endpoint performed an action that requires to be reported
presentation_started
The endpoint performed an action that requires to be reported
presentation_stopped
The endpoint performed an action that requires to be reported
recording_activity
The endpoint performed an action that requires to be reported
token
auth
activity
{app_name} called {method_name} on behalf of {actor}
authorize
{actor} authorized access to {app_name} for {scope} scopes
revoke
{actor} revoked access to {app_name} for {scope} scopes
rules
action_complete_type
action_complete
Action completed
label_applied_type
label_applied
DLP Rule applied Label {label_title}.
label_field_value_changed_type
label_field_value_changed
DLP Rule changed the value of field {label_field} (Label: {label_title}) from '{old_value}' to '{new_value}'.
label_removed_type
label_removed
DLP Rule removed Label {label_title}.
rule_match_type
rule_match
Rule matched
rule_trigger_type
rule_trigger
Rule triggered
sharing_blocked_type
sharing_blocked
content_matched_type
content_matched
content_unmatched_type
content_unmatched
saml
login
login_failure
{actor} failed to login because of the following error: {failure_type}
login_success
{actor} logged in
user_accounts
2sv_change
2sv_disable
{actor} has disabled 2-step verification
2sv_enroll
{actor} has enrolled for 2-step verification
password_change
password_edit
{actor} has changed Account password
recovery_info_change
recovery_email_edit
{actor} has changed Account recovery email
recovery_phone_edit
{actor} has changed Account recovery phone
recovery_secret_qa_edit
{actor} has changed Account recovery secret question/answer
titanium_change
titanium_enroll
{actor} has enrolled for Advanced Protection
titanium_unenroll
{actor} has disabled Advanced Protection
email_forwarding_change
email_forwarding_out_of_domain
{actor} has enabled out of domain email forwarding to {email_forwarding_destination_address}.
login
2sv_change
2sv_disable
{actor} has disabled 2-step verification
2sv_enroll
{actor} has enrolled for 2-step verification
password_change
password_edit
{actor} has changed Account password
recovery_info_change
recovery_email_edit
{actor} has changed Account recovery email
recovery_phone_edit
{actor} has changed Account recovery phone
recovery_secret_qa_edit
{actor} has changed Account recovery secret question/answer
account_warning
account_disabled_password_leak
Account {affected_email_address} disabled because Google has become aware that someone else knows its password
suspicious_login
Google has detected a suspicious login for {affected_email_address}
suspicious_login_less_secure_app
Google has detected a suspicious login for {affected_email_address} from a less secure app
suspicious_programmatic_login
Google has detected a suspicious programmatic login for {affected_email_address}
account_disabled_generic
Account {affected_email_address} disabled
account_disabled_spamming_through_relay
Account {affected_email_address} disabled because Google has become aware that it was used to engage in spamming through SMTP relay service
account_disabled_spamming
Account {affected_email_address} disabled because Google has become aware that it was used to engage in spamming
account_disabled_hijacked
Account {affected_email_address} disabled because Google has detected a suspicious activity indicating it might have been compromised
titanium_change
titanium_enroll
{actor} has enrolled for Advanced Protection
titanium_unenroll
{actor} has disabled Advanced Protection
attack_warning
gov_attack_warning
{actor} might have been targeted by government-backed attack
blocked_sender_change
blocked_sender
{actor} has blocked all future messages from {affected_email_address}.
email_forwarding_change
email_forwarding_out_of_domain
{actor} has enabled out of domain email forwarding to {email_forwarding_destination_address}.
login
login_failure
{actor} failed to login
login_challenge
{actor} was presented with a login challenge
login_verification
{actor} was presented with login verification
logout
{actor} logged out
risky_sensitive_action_allowed
{actor} was allowed to attempt sensitive action: {sensitive_action_name}. This action might be restricted based on privileges or other limitations.
risky_sensitive_action_blocked
{actor} wasn't allowed to attempt sensitive action: {sensitive_action_name}.
login_success
{actor} logged in
jamboard
administrative_action
DEVICE_LICENSE_ENROLLMENT_CHANGE
{CURRENT_JAMBOARD_NAME} was {LICENSE_ENROLLMENT_STATE}
DEVICE_PROVISIONING_CHANGE
{CURRENT_JAMBOARD_NAME} was {PROVISION_STATE}
DEVICE_REBOOT_REQUESTED
{CURRENT_JAMBOARD_NAME} reboot was requested by {actor}
EXPORT_JAMBOARD_FLEET
Export Jamboard fleet was requested by {actor}
DEVICE_OTA_UPDATE_REQUESTED
setting_change
DEVICE_ADDITIONAL_IMES_CHANGE
Additional keyboards were changed from {OLD_ADDITIONAL_IMES} to {NEW_ADDITIONAL_IMES} on {CURRENT_JAMBOARD_NAME}
DEVICE_LOGGING_CHANGE
Cloud logging was turned {ON_OFF} for {CURRENT_JAMBOARD_NAME}
DEMO_MODE_AVAILABILITY_CHANGE
Demo mode was changed from {OLD_DEMO_MODE_AVAILABILITY} to {NEW_DEMO_MODE_AVAILABILITY} on {CURRENT_JAMBOARD_NAME}
DEVICE_LANGUAGE_CHANGE
Language was changed from {OLD_LANGUAGE} to {NEW_LANGUAGE} on {CURRENT_JAMBOARD_NAME}
DEVICE_LOCATION_CHANGE
Stated location was changed from {OLD_LOCATION} to {NEW_LOCATION} on {CURRENT_JAMBOARD_NAME}
DEVICE_NAME_CHANGE
Name was changed from {OLD_JAMBOARD_NAME} to {CURRENT_JAMBOARD_NAME} on {OLD_JAMBOARD_NAME}
DEVICE_NOTE_CHANGE
Note on {CURRENT_JAMBOARD_NAME} was changed from {OLD_NOTE} to {NEW_NOTE}
DEVICE_PAIRING_CHANGE
{DEVICE_TYPE} changed from {OLD_DEVICE} to {NEW_DEVICE} on {CURRENT_JAMBOARD_NAME}
SCREENSAVER_TIMEOUT_CHANGE
Screensaver timeout was changed from {OLD_TIMEOUT_VALUE} minutes to {NEW_TIMEOUT_VALUE} minutes on {CURRENT_JAMBOARD_NAME}
VIDEOCONF_ENABLED_CHANGE
Videoconferencing was turned {ON_OFF} for {CURRENT_JAMBOARD_NAME}
ADB_ENABLED_STATE_CHANGE
FINGER_ERASING_CHANGE
DEVICE_SETTING_LOCKED
DEVICE_SETTING_UNLOCKED
status_change
DEVICE_UPDATE
{COMPONENT} was updated from {OLD_VERSION} to {NEW_VERSION} on {CURRENT_JAMBOARD_NAME}
admin
APPLICATION_SETTINGS
CREATE_APPLICATION_SETTING
For {APPLICATION_NAME}, {SETTING_NAME} created with value {NEW_VALUE}
CHANGE_APPLICATION_SETTING
For {APPLICATION_NAME}, {SETTING_NAME} changed from {OLD_VALUE} to {NEW_VALUE}
DOCS_SETTINGS
CHANGE_DOCS_SETTING
{SETTING_NAME} for Drive changed from {OLD_VALUE} to {NEW_VALUE}
ORG_SETTINGS
ASSIGN_CUSTOM_LOGO
New custom logo assigned for org unit {ORG_UNIT_NAME}
UNASSIGN_CUSTOM_LOGO
Custom logo unassigned for org unit {ORG_UNIT_NAME}
CREATE_ORG_UNIT
Org Unit {ORG_UNIT_NAME} created
REMOVE_ORG_UNIT
Org Unit {ORG_UNIT_NAME} deleted
EDIT_ORG_UNIT_DESCRIPTION
Description of {ORG_UNIT_NAME} changed
MOVE_ORG_UNIT
{ORG_UNIT_NAME} moved to parent {NEW_VALUE}
EDIT_ORG_UNIT_NAME
Name of {ORG_UNIT_NAME} changed to {NEW_VALUE}
TOGGLE_SERVICE_ENABLED
Service {SERVICE_NAME} changed to {NEW_VALUE} for {ORG_UNIT_NAME} organizational unit in your organization
CALENDAR_SETTINGS
CHANGE_CALENDAR_SETTING
{SETTING_NAME} for calendar service in your organization changed from {OLD_VALUE} to {NEW_VALUE}
DOMAIN_SETTINGS
ADD_APPLICATION
Application {APPLICATION_NAME} with id {APP_ID} has been added to the domain
CREATE_ALERT
Alert {ALERT_NAME} has been created
AUTHORIZE_API_CLIENT_ACCESS
API client access to your organization from client {API_CLIENT_NAME} authorized for scopes {API_SCOPES}
REMOVE_API_CLIENT_ACCESS
API client access to your organization from client {API_CLIENT_NAME} removed
CHANGE_DOMAIN_DEFAULT_LOCALE
Default locale for your organization changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_DOMAIN_DEFAULT_TIMEZONE
Default time zone for your organization changed from {OLD_VALUE} to {NEW_VALUE}
ADD_TRUSTED_DOMAINS
Domains {DOMAIN_NAME} added to Trusted Domains list
REMOVE_APPLICATION
Application {APPLICATION_NAME} with id {APP_ID} has been removed from the domain
CHANGE_SSO_SETTINGS
SSO settings changed for {DOMAIN_NAME}
SECURITY_SETTINGS
ALLOW_STRONG_AUTHENTICATION
Allow 2-Step Verification has been set from {OLD_VALUE} to {NEW_VALUE} for {DOMAIN_NAME}
DISALLOW_SERVICE_FOR_OAUTH2_ACCESS
{OAUTH2_SERVICE_NAME} API Access is blocked for {ORG_UNIT_NAME}
ADD_TO_BLOCKED_OAUTH2_APPS
{OAUTH2_APP_NAME} added to Blocked list for {ORG_UNIT_NAME}
ADD_TO_TRUSTED_OAUTH2_APPS
{OAUTH2_APP_NAME} trusted for {ORG_UNIT_NAME}
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
2-step verification enrollment period duration for {ORG_UNIT_NAME} changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
2-step verification frequency for {ORG_UNIT_NAME} changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
2-step verification grace period duration for {ORG_UNIT_NAME} changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_TWO_STEP_VERIFICATION_START_DATE
2-step verification start date has been changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_ALLOWED_TWO_STEP_VERIFICATION_METHODS
2-step verification allowed 2-step verification methods for {ORG_UNIT_NAME} changed to {ALLOWED_TWO_STEP_VERIFICATION_METHOD}
ENFORCE_STRONG_AUTHENTICATION
{SETTING_NAME} in security settings for your organization changed from {OLD_VALUE} to {NEW_VALUE}
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
Setting changed for {ORG_UNIT_NAME} organization unit from {OLD_VALUE} to {NEW_VALUE}
SESSION_CONTROL_SETTINGS_CHANGE
Session Control Settings updated for {REAUTH_APPLICATION} from {REAUTH_SETTING_OLD} to {REAUTH_SETTING_NEW}. (OrgUnit Name: {ORG_UNIT_NAME})
EMAIL_SETTINGS
EMAIL_LOG_SEARCH
An email log search is performed for logs from {EMAIL_LOG_SEARCH_START_DATE} to {EMAIL_LOG_SEARCH_END_DATE} with a sender of [{EMAIL_LOG_SEARCH_SENDER}], a recipient of [{EMAIL_LOG_SEARCH_RECIPIENT}], and an email message id of [{EMAIL_LOG_SEARCH_MSG_ID}]
CHANGE_EMAIL_SETTING
{SETTING_NAME} for email service in your organization changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_GMAIL_SETTING
Gmail setting {SETTING_NAME} was modified
CREATE_GMAIL_SETTING
New gmail setting {SETTING_NAME} was added
DELETE_GMAIL_SETTING
Gmail setting {SETTING_NAME} was deleted
RELEASE_FROM_QUARANTINE
A message with email message id of {EMAIL_LOG_SEARCH_MSG_ID} was released from the {QUARANTINE_NAME} quarantine.
CHROME_OS_SETTINGS
CHANGE_DEVICE_STATE
Changed the state of {DEVICE_TYPE} {DEVICE_SERIAL_NUMBER} from {DEVICE_PREVIOUS_STATE} to {DEVICE_NEW_STATE}
GROUP_SETTINGS
CREATE_GROUP
Group {GROUP_EMAIL} created
DELETE_GROUP
Group {GROUP_EMAIL} deleted
ADD_GROUP_MEMBER
User {USER_EMAIL} created under group {GROUP_EMAIL}
REMOVE_GROUP_MEMBER
User {USER_EMAIL} deleted from group {GROUP_EMAIL}
UPDATE_GROUP_MEMBER
Roles of the user {USER_EMAIL} in group {GROUP_EMAIL} updated from {OLD_VALUE} to {NEW_VALUE}
UPDATE_GROUP_MEMBER_DELIVERY_SETTINGS
DeliverySettings of the user {USER_EMAIL} in group {GROUP_EMAIL} updated from {OLD_VALUE} to {NEW_VALUE}
CHANGE_GROUP_SETTING
{SETTING_NAME} for group {GROUP_EMAIL} changed from {OLD_VALUE} to {NEW_VALUE}
USER_SETTINGS
DELETE_2SV_SCRATCH_CODES
2-step verification scratch codes of the user {USER_EMAIL} deleted
GENERATE_2SV_SCRATCH_CODES
New 2-step verification scratch codes generated for the user {USER_EMAIL}
REVOKE_3LO_DEVICE_TOKENS
3-legged OAuth tokens issued by user {USER_EMAIL} for the device type {DEVICE_TYPE} and id {DEVICE_ID} were revoked
REVOKE_3LO_TOKEN
3-legged OAuth tokens issued by user {USER_EMAIL} for application {APP_ID} were revoked
ADD_RECOVERY_EMAIL
Recovery email added for {USER_EMAIL}
ADD_RECOVERY_PHONE
Recovery phone added for {USER_EMAIL}
GRANT_ADMIN_PRIVILEGE
Admin privileges granted to {USER_EMAIL}
REVOKE_ADMIN_PRIVILEGE
Admin privileges revoked from {USER_EMAIL}
REVOKE_ASP
Application specific password with Id {ASP_ID} issued by user {USER_EMAIL} revoked
TOGGLE_AUTOMATIC_CONTACT_SHARING
Automatic contact sharing for {USER_EMAIL} changed to {NEW_VALUE}
BULK_UPLOAD
{BULK_UPLOAD_TOTAL_USERS_NUMBER} users selected for upload to your organization. {BULK_UPLOAD_FAIL_USERS_NUMBER} out of {BULK_UPLOAD_TOTAL_USERS_NUMBER} users were not uploaded.
BULK_UPLOAD_NOTIFICATION_SENT
Notification of bulk users upload sent to {USER_EMAIL}
CANCEL_USER_INVITE
Invite to {USER_EMAIL} cancelled
CHANGE_USER_CUSTOM_FIELD
{USER_CUSTOM_FIELD} changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_EXTERNAL_ID
External Ids changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_GENDER
Gender changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_IM
IMs changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
ENABLE_USER_IP_WHITELIST
IP whitelist changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_KEYWORD
Keywords changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_LANGUAGE
Languages changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_LOCATION
Locations changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_ORGANIZATION
Organizations changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_PHONE_NUMBER
Phone Numbers changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_RECOVERY_EMAIL
Recovery email changed for {USER_EMAIL}
CHANGE_RECOVERY_PHONE
Recovery phone changed for {USER_EMAIL}
CHANGE_USER_RELATION
Relations changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CHANGE_USER_ADDRESS
Addresses changed for {USER_EMAIL} from {OLD_VALUE} to {NEW_VALUE}
CREATE_EMAIL_MONITOR
Created an email monitor for {USER_EMAIL} to {EMAIL_MONITOR_DEST_EMAIL} that will expire on {END_DATE_TIME}
CREATE_DATA_TRANSFER_REQUEST
Data transfer request created from {USER_EMAIL} to {DESTINATION_USER_EMAIL} for apps {APPLICATION_NAME}
GRANT_DELEGATED_ADMIN_PRIVILEGES
{USER_EMAIL} assigned {NEW_VALUE} admin privileges
DELETE_ACCOUNT_INFO_DUMP
Deleted account and login information dump for {USER_EMAIL} and request ID {REQUEST_ID}
DELETE_EMAIL_MONITOR
Deleted an email monitor for {USER_EMAIL} to {EMAIL_MONITOR_DEST_EMAIL}
DELETE_MAILBOX_DUMP
Deleted mailbox dump for {USER_EMAIL} and request ID {REQUEST_ID}
DELETE_PROFILE_PHOTO
Profile photo of {USER_EMAIL} has been deleted
CHANGE_DISPLAY_NAME
Display name of {USER_EMAIL} changed from {OLD_VALUE} to {NEW_VALUE}
CHANGE_FIRST_NAME
First name of {USER_EMAIL} changed from {OLD_VALUE} to {NEW_VALUE}
GMAIL_RESET_USER
Gmail account of {USER_EMAIL} reset
CHANGE_LAST_NAME
Last name of {USER_EMAIL} changed from {OLD_VALUE} to {NEW_VALUE}
MAIL_ROUTING_DESTINATION_ADDED
User {USER_EMAIL} has received the following individual mail routing destination: {NEW_VALUE}
MAIL_ROUTING_DESTINATION_REMOVED
User {USER_EMAIL} has had the following individual mail routing destination removed: {OLD_VALUE}
ADD_NICKNAME
{USER_NICKNAME} created as a nickname of {USER_EMAIL}
REMOVE_NICKNAME
{USER_NICKNAME} deleted as a nickname of {USER_EMAIL}
CHANGE_PASSWORD
Password changed for {USER_EMAIL}
CHANGE_PASSWORD_ON_NEXT_LOGIN
Password change requirement for {USER_EMAIL} on next login changed from {OLD_VALUE} to {NEW_VALUE}
DOWNLOAD_PENDING_INVITES_LIST
Pending Invites List was downloaded as a CSV file
REMOVE_RECOVERY_EMAIL
Recovery email removed for {USER_EMAIL}
REMOVE_RECOVERY_PHONE
Recovery phone removed for {USER_EMAIL}
REQUEST_ACCOUNT_INFO
Requested account and login information for {USER_EMAIL}
REQUEST_MAILBOX_DUMP
Requested mailbox dump for {USER_EMAIL}
RESEND_USER_INVITE
Invite email to {USER_EMAIL} resent
RESET_SIGNIN_COOKIES
Cookies reset for {USER_EMAIL} and forced re-login
SECURITY_KEY_REGISTERED_FOR_USER
Security key registered for {USER_EMAIL}
REVOKE_SECURITY_KEY
A security key enrolled for user {USER_EMAIL} for 2-step verification was revoked
USER_INVITE
{USER_EMAIL} invited to join your organization
VIEW_TEMP_PASSWORD
Temporary password for user {USER_EMAIL} viewed by the admin
TURN_OFF_2_STEP_VERIFICATION
2-step verification has been turned off for the user {USER_EMAIL}
UNBLOCK_USER_SESSION
User {USER_EMAIL} unblocked by temporarily disabling login challenge
UNMANAGED_USERS_BULK_UPLOAD
A total of {BULK_UPLOAD_TOTAL_USERS_NUMBER} unmanaged users selected for upload. {BULK_UPLOAD_FAIL_USERS_NUMBER} out of {BULK_UPLOAD_TOTAL_USERS_NUMBER} users failed to be uploaded.
DOWNLOAD_UNMANAGED_USERS_LIST
Unmanaged Users list was downloaded as a CSV file
UPDATE_PROFILE_PHOTO
Profile photo of {USER_EMAIL} has been updated
UNENROLL_USER_FROM_TITANIUM
User {USER_EMAIL} unenrolled from Advanced Protection
ARCHIVE_USER
{USER_EMAIL} archived
UPDATE_BIRTHDATE
The birth date for {USER_EMAIL} changed to {BIRTHDATE}
CREATE_USER
{USER_EMAIL} created
DELETE_USER
{USER_EMAIL} deleted
DOWNGRADE_USER_FROM_GPLUS
{USER_EMAIL} was downgraded from Google+
USER_ENROLLED_IN_TWO_STEP_VERIFICATION
{USER_EMAIL} enrolled in 2-step verification
DOWNLOAD_USERLIST_CSV
User list was downloaded as a CSV file
MOVE_USER_TO_ORG_UNIT
{USER_EMAIL} moved from {ORG_UNIT_NAME} to {NEW_VALUE}
USER_PUT_IN_TWO_STEP_VERIFICATION_GRACE_PERIOD
2-step verification grace period has been enabled on {USER_EMAIL} till {NEW_VALUE}
RENAME_USER
{USER_EMAIL} renamed to {NEW_VALUE}
UNENROLL_USER_FROM_STRONG_AUTH
User {USER_EMAIL} unenrolled from Strong Auth
SUSPEND_USER
{USER_EMAIL} suspended
UNARCHIVE_USER
{USER_EMAIL} unarchived
UNDELETE_USER
{USER_EMAIL} undeleted
UNSUSPEND_USER
{USER_EMAIL} unsuspended
UPGRADE_USER_TO_GPLUS
{USER_EMAIL} was upgraded to Google+
USERS_BULK_UPLOAD
A total of {BULK_UPLOAD_TOTAL_USERS_NUMBER} users selected for upload. {BULK_UPLOAD_FAIL_USERS_NUMBER} out of {BULK_UPLOAD_TOTAL_USERS_NUMBER} users failed to be uploaded.
USERS_BULK_UPLOAD_NOTIFICATION_SENT
Notification of bulk users upload sent to {USER_EMAIL}
LICENSES_SETTINGS
USER_LICENSE_ASSIGNMENT
A license for {PRODUCT_NAME} product and {NEW_VALUE} sku was assigned to the user {USER_EMAIL}
USER_LICENSE_REVOKE
A license for {PRODUCT_NAME} product and {OLD_VALUE} sku was revoked from user {USER_EMAIL}
DELEGATED_ADMIN_SETTINGS
ASSIGN_ROLE
Role {ROLE_NAME} assigned to user {USER_EMAIL}
CREATE_ROLE
New role {ROLE_NAME} created
UNASSIGN_ROLE
Unassigned role {ROLE_NAME} from user {USER_EMAIL}
MOBILE_SETTINGS
ACTION_REQUESTED
{ACTION_TYPE} with id {ACTION_ID} on device type {DEVICE_TYPE} and id {DEVICE_ID} was requested by user {USER_EMAIL}
CUSTOMER_USER_DEVICE_DELETION_EVENT
Customer user device {COMPANY_DEVICE_ID} was deleted
REMOVE_MOBILE_APPLICATION_FROM_WHITELIST
{DEVICE_TYPE} application {MOBILE_APP_PACKAGE_ID} is no longer whitelisted for {DISTRIBUTION_ENTITY_NAME} {DISTRIBUTION_ENTITY_TYPE}
CHANGE_MOBILE_APPLICATION_SETTINGS
Changed {SETTING_NAME} app setting from {OLD_VALUE} to {NEW_VALUE} for {DEVICE_TYPE} application {MOBILE_APP_PACKAGE_ID} for {DISTRIBUTION_ENTITY_NAME} {DISTRIBUTION_ENTITY_TYPE}
ADD_MOBILE_APPLICATION_TO_WHITELIST
{DEVICE_TYPE} application {MOBILE_APP_PACKAGE_ID} is whitelisted for {DISTRIBUTION_ENTITY_NAME} {DISTRIBUTION_ENTITY_TYPE}
admin
APPLICATION_SETTINGS
CHANGE_APPLICATION_SETTING
For {APPLICATION_NAME}, {SETTING_NAME} changed from {OLD_VALUE} to {NEW_VALUE}
CREATE_APPLICATION_SETTING
For {APPLICATION_NAME}, {SETTING_NAME} created with value {NEW_VALUE}
DELETE_APPLICATION_SETTING
For {APPLICATION_NAME}, {SETTING_NAME} with value {OLD_VALUE} deleted
REORDER_GROUP_BASED_POLICIES_EVENT
For {APPLICATION_NAME}, group override priorities for {SETTING_NAME} changed to {GROUP_PRIORITIES}.
GPLUS_PREMIUM_FEATURES
Premium features for Google+ service for your organization changed to {NEW_VALUE}
CREATE_MANAGED_CONFIGURATION
Managed configuration with name {MANAGED_CONFIGURATION_NAME} is created for {DEVICE_TYPE} application {MOBILE_APP_PACKAGE_ID}.
DELETE_MANAGED_CONFIGURATION
Managed configuration with name {MANAGED_CONFIGURATION_NAME} is deleted for {DEVICE_TYPE} application {MOBILE_APP_PACKAGE_ID}.
UPDATE_MANAGED_CONFIGURATION
Managed configuration with name {MANAGED_CONFIGURATION_NAME} is updated for {DEVICE_TYPE} application {MOBILE_APP_PACKAGE_ID}.
FLASHLIGHT_EDU_NON_FEATURED_SERVICES_SELECTED
{FLASHLIGHT_EDU_NON_FEATURED_SERVICES_SELECTION} selection was made for Non-Featured Services.
UPDATE_SMART_FEATURES
Smart features and personalization setting has been updated to {NEW_VALUE}
For more information about the Google Workspace applications that Google Security Operations supports,
see
Google Workspace applications
.
WORKSPACE_ALERTS
The following is the list of supported alert types:
Customer takeout initiated
Malware reclassification
Misconfigured whitelist
Phishing reclassification
Suspicious message reported
User reported phishing
User reported spam spike
Leaked password
Suspicious login
Suspicious login (less secure app)
Suspicious programmatic login
User suspended
User suspended (spam)
User suspended (spam through relay)
User suspended (suspicious activity)
Google Operations
Configuration problem
Government attack warning
Device compromised
Suspicious activity
AppMaker Default Cloud SQL setup
Activity Rule
Data Loss Prevention
Apps outage
Primary admin changed
SSO profile added
SSO profile updated
SSO profile deleted
Super admin password reset
APNS certificate is expiring soon
APNS certificate has expired
WORKSPACE_CHROMEOS
For information about the supported ChromeOS log schema, see
ChromeOS devices
.
WORKSPACE_GROUPS
For information about the supported groups log schema, see
group
.
WORKSPACE_MOBILE
For information about the supported mobile log schema, see
mobile
.
WORKSPACE_PRIVILEGES
For information about the supported privileges log schema, see
privilege
.
WORKSPACE_USERS
For information about the supported users log schema, see
users
.
Supported Google Workspace log formats
The Google Workspace parser supports logs in JSON format.
Supported Google Workspace sample logs
Supported WORKSPACE_ACTIVITY sample logs
JSON
{
  "kind": "admin#reports#activity",
  "id": {
    "time": "2021-10-03T12:42:42.020Z",
    "uniqueQualifier": "1654049432447411495",
    "applicationName": "data_studio",
    "customerId": "dummycustomerid"
  },
  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/Zk_h3ikUIFND0y87A64RQpJm58s\\"",
  "actor": {
    "callerType": "USER",
    "email": "dummy.user@xyz.com",
    "profileId": "106217923299022556308"
  },
  "ipAddress": "198.51.100.0",
  "events": [
    {
      "type": "ACCESS",
      "name": "CREATE",
      "parameters": [
        {
          "name": "ASSET_ID",
          "value": "52605549-b378-4a08-8a34-a23c8412a952"
        },
        {
          "name": "ASSET_NAME",
          "value": "Flashpoint - Sheet1"
        },
        {
          "name": "ASSET_TYPE",
          "value": "DATA_SOURCE"
        },
        {
          "name": "OWNER_EMAIL",
          "value": "dummy.user@xyz.com"
        },
        {
          "name": "VISIBILITY",
          "value": "PRIVATE"
        },
        {
          "name": "CONNECTOR_TYPE",
          "value": "Google Sheets"
        },
        {
          "name": "EMBEDDED_IN_REPORT_ID",
          "value": "d4dec8a5-9d81-4c58-8a6d-5e53ee4d10b3"
        }
      ]
    }
  ]
}
Supported WORKSPACE_ALERTS sample logs
JSON
{
  "customerId": "dummycustomerid",
  "alertId": "8d647731-d2f8-4328-b48f-f753f42462bb",
  "createTime": "2021-10-03T07:45:09.500919Z",
  "startTime": "2021-10-03T05:47:59.592561Z",
  "endTime": "2022-10-03T07:29:26.205542Z",
  "type": "Phishing reclassification",
  "source": "Gmail phishing",
  "data": {
    "@type": "type.googleapis.com/google.apps.alertcenter.type.MailPhishing",
    "domainId": {
      "customerPrimaryDomain": "dummy.com"
    },
    "maliciousEntity": {
      "fromHeader": "dummy_noreply@xyz.com"
    },
    "messages": [
      {
        "messageId": "dummy_message_id",
        "md5HashMessageBody": "ecfb410a04167c7dc5e046f755446a88",
        "md5HashSubject": "1fbdd83c4f8d76482a1670b05c6ec5d9",
        "attachmentsSha256Hash": [
          "dba5166ad9db9ba648c1032ebbd34dcd0d085b50023b839ef5c68ca1db93a563",
          "c412fbec3dfff3b080b2ac918acc4d78b4c43bfa14a1aa5b8a8c684a2a0a7591"
        ],
        "recipient": "abc@xyz.com",
        "date": "2022-10-03T05:47:59.592561Z"
      }
    ],
    "systemActionType": "REMOVED_FROM_INBOX"
  },
  "metadata": {
    "customerId": "dummycustomerid",
    "alertId": "8d647731-d2f8-4328-b48f-f753f42462bb",
    "status": "NOT_STARTED",
    "updateTime": "2022-10-03T07:45:09.500919Z",
    "severity": "MEDIUM",
    "etag": "5o4FwC15S_k="
  },
  "updateTime": "2022-10-03T07:45:09.500919Z",
  "etag": "5o4FwC15S_k="
}
Supported WORKSPACE_CHROMEOS sample logs
JSON
{
  "kind": "admin#directory#chromeosdevice",
  "etag": "\\"occ7bTD-Q2yefKPIae3LMOtCT9xQVZYBzlAbHU5b86Q/1sxLKg0cwMsajkfUCDMjixGR8f4\\"",
  "deviceId": "deviceId",
  "serialNumber": "8B17G066JL",
  "status": "DEPROVISIONED",
  "lastSync": "2020-02-18T00:26:57.326Z",
  "annotatedUser": "",
  "model": "Google Pixelbook",
  "osVersion": "79.0.3945.123",
  "platformVersion": "12607.82.0 (Official Build) stable-channel eve",
  "firmwareVersion": "Google_Eve.9584.195.0",
  "macAddress": "b4692118c676",
  "bootMode": "Verified",
  "lastEnrollmentTime": "2020-02-17T05:28:08.264Z",
  "orgUnitPath": "/Kiosks",
  "recentUsers": [
    {
      "type": "USER_TYPE_MANAGED",
      "email": "user@dummy.com"
    }
  ],
  "ethernetMacAddress": "ethernetMacAddress",
  "activeTimeRanges": [
    {
      "date": "2020-02-03",
      "activeTime": 18760877
    },
    {
      "date": "2020-02-04",
      "activeTime": 21540238
    },
    {
      "date": "2020-02-05",
      "activeTime": 19920286
    },
    {
      "date": "2020-02-06",
      "activeTime": 16530212
    },
    {
      "date": "2020-02-07",
      "activeTime": 18012134
    },
    {
      "date": "2020-02-10",
      "activeTime": 9930058
    },
    {
      "date": "2020-02-11",
      "activeTime": 270002
    },
    {
      "date": "2020-02-12",
      "activeTime": 270003
    },
    {
      "date": "2020-02-14",
      "activeTime": 540005
    },
    {
      "date": "2020-02-17",
      "activeTime": 330006
    },
    {
      "date": "2020-02-18",
      "activeTime": 120002
    }
  ],
  "tpmVersionInfo": {
    "family": "322e3000",
    "specLevel": "74",
    "manufacturer": "43524f53",
    "tpmModel": "1",
    "firmwareVersion": "aa1dd980d1631ea",
    "vendorSpecific": "784347206654504D"
  },
  "systemRamTotal": "16695300096",
  "diskVolumeReports": [
    {
      "volumeInfo": [
        {
          "volumeId": "/home/chronos/u-1c8d83ca2fe7d986667dc2669affb8260fd4e605/MyFiles",
          "storageTotal": "494383112192",
          "storageFree": "466741694464"
        },
        {
          "volumeId": "/media/archive",
          "storageTotal": "8347648000",
          "storageFree": "8347648000"
        },
        {
          "volumeId": "/usr/share/oem",
          "storageTotal": "12042240",
          "storageFree": "11681792"
        },
        {
          "volumeId": "/media/removable",
          "storageTotal": "8347648000",
          "storageFree": "8347648000"
        }
      ]
    }
  ],
  "lastKnownNetwork": [
    {
      "ipAddress": "198.51.100.0",
      "wanIpAddress": "198.51.100.1"
    }
  ],
  "autoUpdateExpiration": "1719730800000"
}
Supported WORKSPACE_GROUPS sample logs
JSON
{
  "kind": "admin#directory#group",
  "id": "01mrcu093wh92ak",
  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/h8Qlm2adIy9p4D4KAM9kAGcpAWw\\"",
  "email": "test.user@domain.com",
  "name": "RH",
  "directMembersCount": "1",
  "description": "",
  "adminCreated": true,
  "nonEditableAliases": [
    "test@nimble.io.test-google-a.com"
  ]
}
Supported WORKSPACE_MOBILE sample logs
JSON
{
  "kind": "admin#reports#activity",
  "id": {
    "time": "2021-10-03T12:42:42.020Z",
    "uniqueQualifier": "1654049432447411495",
    "applicationName": "data_studio",
    "customerId": "C02umwv6u"
  },
  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/Zk_h3ikUIFND0y87A64RQpJm58s\\"",
  "actor": {
    "callerType": "USER",
    "email": "dummy.user@xyz.com",
    "profileId": "106217923299022556308"
  },
  "ipAddress": "198.51.100.0",
  "events": [
    {
      "type": "ACCESS",
      "name": "CREATE",
      "parameters": [
        {
          "name": "ASSET_ID",
          "value": "52605549-b378-4a08-8a34-a23c8412a952"
        },
        {
          "name": "ASSET_NAME",
          "value": "Flashpoint - Sheet1"
        },
        {
          "name": "ASSET_TYPE",
          "value": "DATA_SOURCE"
        },
        {
          "name": "OWNER_EMAIL",
          "value": "dummy.user@xyz.com"
        },
        {
          "name": "VISIBILITY",
          "value": "PRIVATE"
        },
        {
          "name": "CONNECTOR_TYPE",
          "value": "Google Sheets"
        },
        {
          "name": "EMBEDDED_IN_REPORT_ID",
          "value": "d4dec8a5-9d81-4c58-8a6d-5e53ee4d10b3"
        }
      ]
    }
  ]
}
Supported WORKSPACE_PRIVILEGES sample logs
JSON
{
  "userId": "115789998599383404219",
  "roleAssignments": [
    {
      "roleAssignmentId": "13801188331880513",
      "roleId": "13801188331880500",
      "assignedTo": "115789998599383404219",
      "scopeType": "CUSTOMER",
      "roleDetails": {
        "roleId": "13801188331880500",
        "roleName": "testadmin",
        "roleDescription": "",
        "rolePrivileges": [
          {
            "privilegeName": "USERS_DELETE_PRIVILEGE_GROUP",
            "serviceId": "serviceId",
            "details": null
          },
          {
            "privilegeName": "USERS_SUSPEND",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_UPDATE",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_ALL",
            "serviceId": "00haapch16h1ysv",
            "details": {
              "kind": "admin#directory#privilege",
              "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/wBCzWwKeC3waKUCE3yZ20yDyw-4\\"",
              "serviceId": "00haapch16h1ysv",
              "serviceName": "admin_apis",
              "privilegeName": "USERS_ALL",
              "isOuScopable": true,
              "childPrivileges": [
                {
                  "kind": "admin#directory#privilege",
                  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/_EwUpbUxOWRchDOLthCHXSIXfU8\\"",
                  "serviceId": "00haapch16h1ysv",
                  "serviceName": "admin_apis",
                  "privilegeName": "USERS_CREATE_PRIVILEGE_GROUP",
                  "isOuScopable": true
                },
                {
                  "kind": "admin#directory#privilege",
                  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/Gfb1BNFCQYMpoXP5kDFYaAxlRLA\\"",
                  "serviceId": "00haapch16h1ysv",
                  "serviceName": "admin_apis",
                  "privilegeName": "USERS_RETRIEVE_PRIVILEGE_GROUP",
                  "isOuScopable": true
                },
                {
                  "kind": "admin#directory#privilege",
                  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/OWKYOG2T8wp2XN5aN_rph-bSK6U\\"",
                  "serviceId": "00haapch16h1ysv",
                  "serviceName": "admin_apis",
                  "privilegeName": "USERS_UPDATE",
                  "isOuScopable": true,
                  "childPrivileges": [
                    {
                      "kind": "admin#directory#privilege",
                      "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/2ftvr43QDvhauQrbWTRZqCQTcCQ\\"",
                      "serviceId": "00haapch16h1ysv",
                      "serviceName": "admin_apis",
                      "privilegeName": "USERS_ALIAS",
                      "isOuScopable": true
                    },
                    {
                      "kind": "admin#directory#privilege",
                      "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/zPWWFJF3OJ4WitnItfmCG0D7lyA\\"",
                      "serviceId": "00haapch16h1ysv",
                      "serviceName": "admin_apis",
                      "privilegeName": "USERS_MOVE",
                      "isOuScopable": true
                    },
                    {
                      "kind": "admin#directory#privilege",
                      "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/GZlngzILW5ViYA8VleovaIvbkbE\\"",
                      "serviceId": "00haapch16h1ysv",
                      "serviceName": "admin_apis",
                      "privilegeName": "USERS_RESET_PASSWORD",
                      "isOuScopable": true
                    },
                    {
                      "kind": "admin#directory#privilege",
                      "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/LMEMNnXTsYvl3S-g6HYBXgU25-Q\\"",
                      "serviceId": "00haapch16h1ysv",
                      "serviceName": "admin_apis",
                      "privilegeName": "USERS_FORCE_PASSWORD_CHANGE",
                      "isOuScopable": true
                    },
                    {
                      "kind": "admin#directory#privilege",
                      "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/rL_F59Vg8sWQOcsHHWJ8Wwm0yhc\\"",
                      "serviceId": "00haapch16h1ysv",
                      "serviceName": "admin_apis",
                      "privilegeName": "USERS_ADD_NICKNAME",
                      "isOuScopable": true
                    },
                    {
                      "kind": "admin#directory#privilege",
                      "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/C1v3E2d3y7R8I52p_YoJbxD1328\\"",
                      "serviceId": "00haapch16h1ysv",
                      "serviceName": "admin_apis",
                      "privilegeName": "USERS_SUSPEND",
                      "isOuScopable": true
                    }
                  ]
                },
                {
                  "kind": "admin#directory#privilege",
                  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/MUKzUOa37XWIpUoKXfKRt55cYHQ\\"",
                  "serviceId": "00haapch16h1ysv",
                  "serviceName": "admin_apis",
                  "privilegeName": "USERS_UPDATE_CUSTOM_ATTRIBUTES_USER_PRIVILEGE_GROUP",
                  "isOuScopable": true
                },
                {
                  "kind": "admin#directory#privilege",
                  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/VrPNeHSLlnDFNuekbj7FihGGXds\\"",
                  "serviceId": "00haapch16h1ysv",
                  "serviceName": "admin_apis",
                  "privilegeName": "USERS_DELETE_PRIVILEGE_GROUP",
                  "isOuScopable": true
                }
              ]
            }
          },
          {
            "privilegeName": "USERS_ALIAS",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_MOVE",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_FORCE_PASSWORD_CHANGE",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_CREATE_PRIVILEGE_GROUP",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_RESET_PASSWORD",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_RETRIEVE_PRIVILEGE_GROUP",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_UPDATE_CUSTOM_ATTRIBUTES_USER_PRIVILEGE_GROUP",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "USERS_ADD_NICKNAME",
            "serviceId": "00haapch16h1ysv",
            "details": null
          },
          {
            "privilegeName": "ORGANIZATION_UNITS_RETRIEVE",
            "serviceId": "00haapch16h1ysv",
            "details": null
          }
        ],
        "isSystemRole": false
      }
    }
  ]
}
Supported WORKSPACE_USERS sample logs
JSON
{
  "kind": "admin#directory#user",
  "id": "102585217528814888330",
  "etag": "\\"JCPRxFaiNR1s5TJ6ecIH8OpGdY4efiOYXbIB65itOzY/Fvq8oDDWIwwaXS2j2yA3Stqn6mg\\"",
  "primaryEmail": "dummy@domain.io",
  "name": {
    "givenName": "dummyName",
    "familyName": "dummyFamilyName",
    "fullName": "dummy Shah"
  },
  "isAdmin": true,
  "isDelegatedAdmin": false,
  "lastLoginTime": "2022-08-13T02:04:12.000Z",
  "creationTime": "2017-05-19T01:44:55.000Z",
  "agreedToTerms": true,
  "suspended": false,
  "archived": false,
  "changePasswordAtNextLogin": false,
  "ipWhitelisted": false,
  "emails": [
    {
      "address": "dummy@domain.oi",
      "primary": true
    },
    {
      "address": "dummy@domain.oi.tast-goggle-a.com"
    }
  ],
  "languages": [
    {
      "languageCode": "en",
      "preference": "preferred"
    }
  ],
  "nonEditableAliases": [
    "dummy@domain.oi.tast-goggle-a.com"
  ],
  "customerId": "C03puekhd",
  "orgUnitPath": "/",
  "isMailboxSetup": true,
  "isEnrolledIn2Sv": false,
  "isEnforcedIn2Sv": false,
  "includeInGlobalAddressList": true,
  "recoveryEmail": "test@xyz.com",
  "recoveryPhone": "+919879995533"
}
Field mapping reference
The following sections explain how the Google Security Operations parser maps Google Workspace
log fields to Google Security Operations Unified Data Model (UDM) fields.
The field mappings of this parser remain the same for
feed-based ingestion
and
native ingestion
.
Field mapping reference: WORKSPACE_ACTIVITY log types to UDM event type
The following table lists the
WORKSPACE_ACTIVITY
log types and their corresponding UDM event types.
Workspace application
Event identifier
Event type
access_transparency
ACCESS
USER_RESOURCE_ACCESS
chrome
CHROME_OS_ADD_USER
USER_CREATION
chrome
CHROME_OS_REMOVE_USER
USER_DELETION
chrome
DEVICE_BOOT_STATE_CHANGE
SETTING_MODIFICATION
chrome
CHROME_OS_LOGIN_FAILURE_EVENT
USER_LOGIN
chrome
CHROME_OS_LOGIN_LOGOUT_EVENT
USER_LOGIN
chrome
CHROME_OS_LOGIN_EVENT
USER_LOGIN
chrome
CHROME_OS_LOGOUT_EVENT
USER_LOGOUT
chrome
CHROME_OS_REPORTING_DATA_LOST
STATUS_UPDATE
chrome
PASSWORD_CHANGED
USER_CHANGE_PASSWORD
chrome
PASSWORD_REUSE
USER_UNCATEGORIZED
chrome
DLP_EVENT
USER_UNCATEGORIZED
chrome
CONTENT_TRANSFER
STATUS_UNCATEGORIZED
chrome
CONTENT_UNSCANNED
SCAN_UNCATEGORIZED
chrome
EXTENSION_REQUEST
USER_UNCATEGORIZED
chrome
LOGIN_EVENT
USER_LOGIN
chrome
MALWARE_TRANSFER
SCAN_UNCATEGORIZED
.
The security category is
SOFTWARE_MALICIOUS
.
chrome
PASSWORD_BREACH
USER_RESOURCE_ACCESS
.
The security category is
PHISHING
.
chrome
SENSITIVE_DATA_TRANSFER
SCAN_UNCATEGORIZED
chrome
UNSAFE_SITE_VISIT
NETWORK_UNCATEGORIZED
.
The security category is
NETWORK_SUSPICIOUS
.
chrome
BROWSER_CRASH
STATUS_UNCATEGORIZED
chrome
BROWSER_EXTENSION_INSTALL
USER_RESOURCE_UPDATE_CONTENT
chrome
CHROMEOS_AFFILIATED_LOCK_SUCCESS
USER_LOGOUT
chrome
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
USER_LOGIN
chrome
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
USER_LOGIN
chrome
CHROMEOS_PERIPHERAL_ADDED
USER_RESOURCE_ACCESS
chrome
CHROMEOS_PERIPHERAL_REMOVED
USER_RESOURCE_DELETION
chrome
CHROMEOS_PERIPHERAL_STATUS_UPDATED
USER_RESOURCE_UPDATE_CONTENT
chrome
CHROMEOS_UPDATE_FAILURE
STATUS_UNCATEGORIZED
chrome
CHROMEOS_UPDATE_SUCCESS
STATUS_UNCATEGORIZED
chrome
CHROME_OS_CRD_CLIENT_CONNECTED
USER_LOGIN
chrome
CHROME_OS_CRD_HOST_ENDED
STATUS_STARTUP
chrome
CHROME_OS_CRD_HOST_STARTED
STATUS_STARTUP
chrome
URL_FILTERING_INTERSTITIAL
STATUS_UNCATEGORIZED
context_aware_access
ACCESS_DENY_EVENT
USER_RESOURCE_ACCESS
context_aware_access
ACCESS_DENY_INTERNAL_ERROR_EVENT
USER_RESOURCE_ACCESS
context_aware_access
MONITOR_MODE_ACCESS_DENY_EVENT
USER_RESOURCE_ACCESS
gplus
create_comment
USER_RESOURCE_CREATION
gplus
delete_comment
USER_RESOURCE_DELETION
gplus
edit_comment
USER_RESOURCE_UPDATE_CONTENT
gplus
add_plusone
STATUS_UPDATE
gplus
remove_plusone
STATUS_UPDATE
gplus
add_poll_vote
STATUS_UPDATE
gplus
remove_poll_vote
STATUS_UPDATE
gplus
create_post
USER_RESOURCE_CREATION
gplus
delete_post
USER_RESOURCE_DELETION
gplus
content_manager_delete_post
USER_RESOURCE_DELETION
gplus
edit_post
USER_RESOURCE_UPDATE_CONTENT
data_studio
ADD_REPORT_EMAIL_DELIVERY
USER_UNCATEGORIZED
data_studio
CREATE
USER_RESOURCE_CREATION
data_studio
DATA_EXPORT
USER_RESOURCE_ACCESS
data_studio
DELETE
USER_RESOURCE_DELETION
data_studio
DOWNLOAD_REPORT
USER_UNCATEGORIZED
data_studio
EDIT
USER_RESOURCE_UPDATE_CONTENT
data_studio
RESTORE
USER_RESOURCE_CREATION
data_studio
STOP_REPORT_EMAIL_DELIVERY
USER_UNCATEGORIZED
data_studio
TRASH
USER_RESOURCE_DELETION
data_studio
UPDATE_REPORT_EMAIL_DELIVERY
USER_UNCATEGORIZED
data_studio
VIEW
USER_RESOURCE_ACCESS
data_studio
CHANGE_DATA_SOURCE_ACCESS_TYPE
USER_RESOURCE_UPDATE_PERMISSIONS
data_studio
CHANGE_ASSET_LINK_SHARING_ACCESS_TYPE
USER_RESOURCE_UPDATE_PERMISSIONS
data_studio
CHANGE_ASSET_LINK_SHARING_VISIBILITY
USER_RESOURCE_UPDATE_PERMISSIONS
data_studio
CHANGE_USER_ACCESS
USER_CHANGE_PERMISSIONS
mobile
APPLICATION_EVENT
USER_RESOURCE_UPDATE_CONTENT
mobile
APPLICATION_REPORT_EVENT
STATUS_UPDATE
mobile
DEVICE_REGISTER_UNREGISTER_EVENT
USER_RESOURCE_UPDATE_PERMISSIONS
mobile
ADVANCED_POLICY_SYNC_EVENT
STATUS_UPDATE
mobile
DEVICE_ACTION_EVENT
USER_RESOURCE_UPDATE_CONTENT
mobile
DEVICE_COMPLIANCE_CHANGED_EVENT
STATUS_UPDATE
mobile
OS_UPDATED_EVENT
USER_RESOURCE_UPDATE_CONTENT
mobile
DEVICE_OWNERSHIP_CHANGE_EVENT
STATUS_UPDATE
mobile
DEVICE_SETTINGS_UPDATED_EVENT
SETTING_MODIFICATION
mobile
APPLE_DEP_DEVICE_UPDATE_ON_APPLE_PORTAL_EVENT
STATUS_UPDATE
mobile
DEVICE_SYNC_EVENT
USER_RESOURCE_UPDATE_CONTENT
mobile
RISK_SIGNAL_UPDATED_EVENT
STATUS_UPDATE
mobile
ANDROID_WORK_PROFILE_SUPPORT_ENABLED_EVENT
STATUS_UPDATE
mobile
DEVICE_COMPROMISED_EVENT
STATUS_UPDATE
mobile
FAILED_PASSWORD_ATTEMPTS_EVENT
STATUS_UPDATE
mobile
SUSPICIOUS_ACTIVITY_EVENT
STATUS_UPDATE
groups_enterprise
accept_invitation
USER_UNCATEGORIZED
groups_enterprise
add_info_setting
GROUP_MODIFICATION
groups_enterprise
add_member
GROUP_MODIFICATION
groups_enterprise
add_member_role
USER_CHANGE_PERMISSIONS
groups_enterprise
add_security_setting
GROUP_MODIFICATION
groups_enterprise
add_service_account_permission
USER_CHANGE_PERMISSIONS
groups_enterprise
approve_join_request
USER_UNCATEGORIZED
groups_enterprise
ban_member_with_moderation
GROUP_MODIFICATION
groups_enterprise
change_info_setting
GROUP_MODIFICATION
groups_enterprise
change_security_setting
GROUP_MODIFICATION
groups_enterprise
create_group
GROUP_CREATION
groups_enterprise
create_namespace
GROUP_UNCATEGORIZED
groups_enterprise
delete_group
GROUP_DELETION
groups_enterprise
delete_namespace
GROUP_UNCATEGORIZED
groups_enterprise
add_dynamic_group_query
GROUP_UNCATEGORIZED
groups_enterprise
change_dynamic_group_query
GROUP_MODIFICATION
groups_enterprise
invite_member
GROUP_UNCATEGORIZED
groups_enterprise
join
GROUP_MODIFICATION
groups_enterprise
add_membership_expiry
GROUP_MODIFICATION
groups_enterprise
remove_membership_expiry
GROUP_MODIFICATION
groups_enterprise
update_membership_expiry
GROUP_MODIFICATION
groups_enterprise
reject_invitation
USER_UNCATEGORIZED
groups_enterprise
reject_join_request
USER_UNCATEGORIZED
groups_enterprise
remove_info_setting
GROUP_MODIFICATION
groups_enterprise
remove_member
GROUP_MODIFICATION
groups_enterprise
remove_member_role
GROUP_MODIFICATION
groups_enterprise
remove_security_setting
GROUP_MODIFICATION
groups_enterprise
remove_service_account_permission
GROUP_MODIFICATION
groups_enterprise
request_to_join
USER_UNCATEGORIZED
groups_enterprise
revoke_invitation
USER_UNCATEGORIZED
groups_enterprise
unban_member
GROUP_MODIFICATION
calendar
change_calendar_acls
USER_CHANGE_PERMISSIONS
calendar
change_calendar_country
USER_RESOURCE_UPDATE_CONTENT
calendar
create_calendar
USER_RESOURCE_CREATION
calendar
delete_calendar
USER_RESOURCE_DELETION
calendar
change_calendar_description
USER_RESOURCE_UPDATE_CONTENT
calendar
change_calendar_location
USER_RESOURCE_UPDATE_CONTENT
calendar
change_calendar_timezone
USER_RESOURCE_UPDATE_CONTENT
calendar
change_calendar_title
USER_RESOURCE_UPDATE_CONTENT
calendar
notification_triggered
USER_UNCATEGORIZED
calendar
add_subscription
USER_UNCATEGORIZED
calendar
delete_subscription
STATUS_UPDATE
calendar
create_event
USER_RESOURCE_UPDATE_CONTENT
calendar
delete_event
USER_RESOURCE_UPDATE_CONTENT
calendar
add_event_guest
USER_RESOURCE_UPDATE_CONTENT
calendar
change_event_guest_response_auto
USER_UNCATEGORIZED
calendar
remove_event_guest
USER_RESOURCE_UPDATE_CONTENT
calendar
change_event_guest_response
USER_RESOURCE_UPDATE_CONTENT
calendar
change_event
USER_RESOURCE_UPDATE_CONTENT
calendar
remove_event_from_trash
USER_RESOURCE_UPDATE_CONTENT
calendar
restore_event
USER_RESOURCE_UPDATE_CONTENT
calendar
change_event_start_time
USER_RESOURCE_UPDATE_CONTENT
calendar
change_event_title
USER_RESOURCE_UPDATE_CONTENT
calendar
transfer_event_requested
USER_UNCATEGORIZED
calendar
transfer_event_completed
USER_UNCATEGORIZED
calendar
interop_freebusy_lookup_outbound_successful
USER_RESOURCE_ACCESS
calendar
interop_freebusy_lookup_inbound_successful
USER_RESOURCE_ACCESS
calendar
interop_exchange_resource_availability_lookup_successful
USER_RESOURCE_ACCESS
calendar
interop_exchange_resource_list_lookup_successful
USER_RESOURCE_ACCESS
calendar
interop_freebusy_lookup_outbound_unsuccessful
USER_RESOURCE_ACCESS
calendar
interop_freebusy_lookup_inbound_unsuccessful
USER_RESOURCE_ACCESS
calendar
interop_exchange_resource_availability_lookup_unsuccessful
USER_RESOURCE_ACCESS
calendar
interop_exchange_resource_list_lookup_unsuccessful
USER_RESOURCE_ACCESS
google_chat
add_room_member
GROUP_MODIFICATION
google_chat
attachment_download
FILE_UNCATEGORIZED
google_chat
attachment_upload
FILE_UNCATEGORIZED
google_chat
block_room
GROUP_UNCATEGORIZED
google_chat
block_user
USER_UNCATEGORIZED
google_chat
direct_message_started
USER_UNCATEGORIZED
google_chat
invite_accept
USER_UNCATEGORIZED
google_chat
invite_decline
USER_UNCATEGORIZED
google_chat
invite_send
USER_UNCATEGORIZED
google_chat
message_edited
USER_RESOURCE_UPDATE_CONTENT
google_chat
message_posted
USER_RESOURCE_CREATION
google_chat
message_reported
USER_UNCATEGORIZED
google_chat
message_deleted
USER_RESOURCE_DELETION
google_chat
remove_room_member
GROUP_MODIFICATION
google_chat
room_created
GROUP_CREATED
google_chat
reaction_added
USER_UNCATEGORIZED
google_chat
call_ended
USER_UNCATEGORIZED
google_chat
presentation_started
STATUS_UNCATEGORIZED
google_chat
invitation_sent
STATUS_UNCATEGORIZED
google_chat
presentation_stopped
STATUS_UNCATEGORIZED
gcp
IMPORT_SSH_PUBLIC_KEY
USER_UNCATEGORIZED
gcp
DELETE_POSIX_ACCOUNT
USER_UNCATEGORIZED
gcp
DELETE_SSH_PUBLIC_KEY
USER_UNCATEGORIZED
gcp
GET_SSH_PUBLIC_KEY
USER_UNCATEGORIZED
gcp
GET_LOGIN_PROFILE
USER_UNCATEGORIZED
gcp
UPDATE_SSH_PUBLIC_KEY
USER_UNCATEGORIZED
drive
add_to_folder
USER_RESOURCE_CREATION
drive
approval_canceled
USER_UNCATEGORIZED
drive
approval_comment_added
USER_UNCATEGORIZED
drive
approval_completed
USER_UNCATEGORIZED
drive
approval_decisions_reset
USER_UNCATEGORIZED
drive
approval_due_time_change
USER_UNCATEGORIZED
drive
approval_requested
USER_UNCATEGORIZED
drive
approval_reviewer_change
USER_UNCATEGORIZED
drive
approval_reviewer_responded
USER_UNCATEGORIZED
drive
copy
USER_RESOURCE_CREATION
drive
create
USER_RESOURCE_CREATION
drive
delete
USER_RESOURCE_DELETION
drive
download
USER_RESOURCE_ACCESS
drive
email_as_attachment
EMAIL_TRANSACTION
drive
edit
USER_RESOURCE_UPDATE_CONTENT
drive
label_added
USER_UNCATEGORIZED
drive
label_added_by_item_create
USER_UNCATEGORIZED
drive
label_field_changed
USER_UNCATEGORIZED
drive
label_removed
USER_UNCATEGORIZED
drive
add_lock
USER_UNCATEGORIZED
drive
move
USER_UNCATEGORIZED
drive
preview
USER_RESOURCE_ACCESS
drive
print
USER_UNCATEGORIZED
drive
remove_from_folder
USER_RESOURCE_DELETION
drive
rename
USER_RESOURCE_UPDATE_CONTENT
drive
untrash
USER_RESOURCE_CREATION
drive
sheets_import_range
USER_RESOURCE_ACCESS
drive
source_copy
USER_RESOURCE_UPDATE_CONTENT
drive
trash
USER_RESOURCE_DELETION
drive
remove_lock
USER_UNCATEGORIZED
drive
unmovable_item_reparented
USER_UNCATEGORIZED
drive
upload
USER_RESOURCE_CREATION
drive
view
USER_RESOURCE_ACCESS
drive
connected_sheets_query
USER_RESOURCE_ACCESS
drive
accept_suggestion
USER_RESOURCE_UPDATE_CONTENT
drive
create_comment
USER_RESOURCE_CREATION
drive
create_suggestion
USER_RESOURCE_CREATION
drive
delete_comment
USER_RESOURCE_DELETION
drive
delete_suggestion
USER_RESOURCE_DELETION
drive
edit_comment
USER_RESOURCE_UPDATE_CONTENT
drive
expire_access_request
USER_RESOURCE_UPDATE_PERMISSIONS
drive
reassign_comment
USER_RESOURCE_UPDATE_CONTENT
drive
reject_suggestion
USER_RESOURCE_UPDATE_CONTENT
drive
reopen_comment
USER_RESOURCE_UPDATE_CONTENT
drive
request_access
USER_RESOURCE_UPDATE_PERMISSIONS
drive
resolve_comment
USER_RESOURCE_UPDATE_CONTENT
drive
deny_access_request
USER_UNCATEGORIZED
drive
download_forms_response
USER_RESOURCE_ACCESS
drive
email_collaborators
EMAIL_UNCATEGORIZED
drive
access_url
USER_RESOURCE_ACCESS
drive
access_item_content
USER_RESOURCE_ACCESS
drive
sheets_import_url
USER_UNCATEGORIZED
drive
apply_security_update
USER_RESOURCE_UPDATE_PERMISSIONS
drive
shared_drive_apply_security_update
USER_RESOURCE_UPDATE_PERMISSIONS
drive
shared_drive_remove_security_update
USER_RESOURCE_UPDATE_PERMISSIONS
drive
publish_change
USER_RESOURCE_UPDATE_PERMISSIONS
drive
change_acl_editors
USER_RESOURCE_UPDATE_PERMISSIONS
drive
change_document_access_scope
USER_RESOURCE_UPDATE_PERMISSIONS
drive
change_document_access_scope_hierarchy_reconciled
USER_RESOURCE_UPDATE_PERMISSIONS
drive
change_document_visibility
USER_RESOURCE_UPDATE_PERMISSIONS
drive
change_document_visibility_hierarchy_reconciled
USER_RESOURCE_UPDATE_PERMISSIONS
drive
remove_security_update
USER_RESOURCE_UPDATE_PERMISSIONS
drive
shared_drive_membership_change
USER_RESOURCE_UPDATE_PERMISSIONS
drive
shared_drive_settings_change
USER_RESOURCE_UPDATE_PERMISSIONS
drive
sheets_import_range_access_change
USER_RESOURCE_UPDATE_PERMISSIONS
drive
change_user_access
USER_CHANGE_PERMISSIONS
drive
change_user_access_hierarchy_reconciled
USER_CHANGE_PERMISSIONS
drive
change_owner
USER_CHANGE_PERMISSIONS
drive
publish_new_version
USER_UNCATEGORIZED
drive
change_owner_hierarchy_reconciled
USER_CHANGE_PERMISSIONS
drive
team_drive_membership_change
USER_CHANGE_PERMISSIONS
drive
team_drive_settings_change
USER_CHANGE_PERMISSIONS
drive
storage_usage_update
USER_RESOURCE_ACCESS
groups
change_acl_permission
GROUP_MODIFICATION
groups
accept_invitation
USER_UNCATEGORIZED
groups
approve_join_request
USER_UNCATEGORIZED
groups
join
GROUP_MODIFICATION
groups
request_to_join
USER_UNCATEGORIZED
groups
change_basic_setting
GROUP_MODIFICATION
groups
create_group
GROUP_CREATION
groups
delete_group
GROUP_DELETION
groups
change_identity_setting
GROUP_MODIFICATION
groups
add_info_setting
GROUP_MODIFICATION
groups
change_info_setting
GROUP_MODIFICATION
groups
remove_info_setting
GROUP_MODIFICATION
groups
change_new_members_restrictions_setting
GROUP_UNCATEGORIZED
groups
change_post_replies_setting
GROUP_MODIFICATION
groups
change_spam_moderation_setting
GROUP_MODIFICATION
groups
change_topic_setting
GROUP_MODIFICATION
groups
moderate_message
GROUP_MODIFICATION
groups
always_post_from_user
USER_UNCATEGORIZED
groups
add_user
GROUP_MODIFICATION
groups
ban_user_with_moderation
GROUP_MODIFICATION
groups
revoke_invitation
USER_UNCATEGORIZED
groups
invite_user
USER_UNCATEGORIZED
groups
reject_join_request
USER_UNCATEGORIZED
groups
reinvite_user
USER_UNCATEGORIZED
groups
remove_user
GROUP_MODIFICATION
groups
change_email_subscription_type
GROUP_MODIFICATION
groups
unsubscribe_via_mail
USER_UNCATEGORIZED
keep
deleted_attachment
USER_UNCATEGORIZED
keep
uploaded_attachment
USER_UNCATEGORIZED
keep
edited_note_content
USER_RESOURCE_UPDATE_CONTENT
keep
created_note
USER_RESOURCE_CREATION
keep
deleted_note
USER_RESOURCE_DELETION
keep
modified_acl
USER_RESOURCE_UPDATE_PERMISSIONS
google_meet
abuse_report_submitted
USER_UNCATEGORIZED
google_meet
call_ended
USER_UNCATEGORIZED
google_meet
livestream_watched
USER_COMMUNICATION
google_meet
invitation_sent
STATUS_UNCATEGORIZED
google_meet
presentation_started
STATUS_UNCATEGORIZED
google_meet
presentation_stopped
STATUS_UNCATEGORIZED
google_meet
knocking_denied
STATUS_UNCATEGORIZED
google_meet
knocking_accepted
STATUS_UNCATEGORIZED
google_meet
recording_activity
STATUS_UNCATEGORIZED
google_meet
dialed_out
STATUS_UNCATEGORIZED
token
activity
USER_RESOURCE_ACCESS
token
authorize
USER_RESOURCE_ACCESS
token
revoke
USER_RESOURCE_UPDATE_PERMISSIONS
rules
action_complete
USER_RESOURCE_ACCESS
rules
rule_match
USER_RESOURCE_ACCESS
rules
rule_trigger
USER_RESOURCE_ACCESS
rules
label_field_value_changed
USER_RESOURCE_UPDATE_CONTENT
rules
label_applied
USER_RESOURCE_UPDATE_CONTENT
rules
sharing_blocked
USER_RESOURCE_UPDATE_CONTENT
rules
content_matched
USER_RESOURCE_ACCESS
rules
content_unmatched
USER_RESOURCE_ACCESS
saml
login_failure
USER_LOGIN
saml
login_success
USER_LOGIN
user_accounts
2sv_disable
USER_UNCATEGORIZED
user_accounts
2sv_enroll
USER_UNCATEGORIZED
user_accounts
password_edit
USER_UNCATEGORIZED
user_accounts
recovery_email_edit
USER_UNCATEGORIZED
user_accounts
recovery_phone_edit
USER_UNCATEGORIZED
user_accounts
recovery_secret_qa_edit
USER_UNCATEGORIZED
user_accounts
titanium_enroll
USER_UNCATEGORIZED
user_accounts
titanium_unenroll
USER_UNCATEGORIZED
user_accounts
email_forwarding_out_of_domain
USER_UNCATEGORIZED
jamboard
DEVICE_LICENSE_ENROLLMENT_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_OTA_UPDATE_REQUESTED
SETTING_MODIFICATION
jamboard
DEVICE_PROVISIONING_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_REBOOT_REQUESTED
USER_UNCATEGORIZED
jamboard
EXPORT_JAMBOARD_FLEET
USER_UNCATEGORIZED
jamboard
ADB_ENABLED_STATE_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_ADDITIONAL_IMES_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_LOGGING_CHANGE
SETTING_MODIFICATION
jamboard
DEMO_MODE_AVAILABILITY_CHANGE
SETTING_MODIFICATION
jamboard
DEMO_MODE_CHANGE
SETTING_MODIFICATION
jamboard
FINGER_ERASING_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_LANGUAGE_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_LOCATION_CHANGE
STATUS_UPDATE
jamboard
DEVICE_NAME_CHANGE
STATUS_UPDATE
jamboard
DEVICE_NOTE_CHANGE
STATUS_UPDATE
jamboard
DEVICE_PAIRING_CHANGE
SETTING_MODIFICATION
jamboard
SCREENSAVER_TIMEOUT_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_SETTING_LOCKED
SETTING_MODIFICATION
jamboard
DEVICE_SETTING_UNLOCKED
SETTING_MODIFICATION
jamboard
VIDEOCONF_ENABLED_CHANGE
SETTING_MODIFICATION
jamboard
DEVICE_UPDATE
STATUS_UPDATE
login
2sv_disable
SERVICE_STOP
login
2sv_enroll
SERVICE_START
login
password_edit
USER_CHANGE_PASSWORD
login
recovery_email_edit
USER_UNCATEGORIZED
login
recovery_phone_edit
USER_UNCATEGORIZED
login
recovery_secret_qa_edit
USER_UNCATEGORIZED
login
account_disabled_password_leak
USER_UNCATEGORIZED
login
suspicious_login
USER_LOGIN
login
suspicious_login_less_secure_app
USER_LOGIN
login
suspicious_programmatic_login
USER_LOGIN
login
account_disabled_generic
USER_UNCATEGORIZED
login
account_disabled_spamming_through_relay
USER_UNCATEGORIZED
login
account_disabled_spamming
USER_UNCATEGORIZED
login
account_disabled_hijacked
USER_UNCATEGORIZED
login
titanium_enroll
USER_UNCATEGORIZED
login
titanium_unenroll
USER_UNCATEGORIZED
login
gov_attack_warning
STATUS_UNCATEGORIZED
login
email_forwarding_out_of_domain
USER_UNCATEGORIZED
login
login_failure
USER_LOGIN
.
The security category is
AUTH_VIOLATION
.
login
login_challenge
USER_LOGIN
login
login_verification
USER_LOGIN
login
logout
USER_LOGOUT
login
login_success
USER_LOGIN
login
risky_sensitive_action_allowed
USER_LOGIN
login
risky_sensitive_action_blocked
USER_LOGIN
login
blocked_sender
STATUS_UNCATEGORIZED
admin
DELETE_2SV_SCRATCH_CODES
USER_RESOURCE_DELETION
admin
GENERATE_2SV_SCRATCH_CODES
USER_RESOURCE_CREATION
admin
REVOKE_3LO_DEVICE_TOKENS
USER_RESOURCE_ACCESS
admin
REVOKE_3LO_TOKEN
USER_RESOURCE_ACCESS
admin
ADD_RECOVERY_EMAIL
USER_RESOURCE_CREATION
admin
ADD_RECOVERY_PHONE
USER_RESOURCE_CREATION
admin
GRANT_ADMIN_PRIVILEGE
USER_CHANGE_PERMISSIONS
admin
REVOKE_ADMIN_PRIVILEGE
USER_CHANGE_PERMISSIONS
admin
REVOKE_ASP
USER_CHANGE_PERMISSIONS
admin
TOGGLE_AUTOMATIC_CONTACT_SHARING
SETTING_MODIFICATION
admin
BULK_UPLOAD
USER_RESOURCE_CREATION
admin
BULK_UPLOAD_NOTIFICATION_SENT
USER_UNCATEGORIZED
admin
CANCEL_USER_INVITE
USER_UNCATEGORIZED
admin
CHANGE_USER_CUSTOM_FIELD
USER_UNCATEGORIZED
admin
CHANGE_USER_EXTERNAL_ID
USER_UNCATEGORIZED
admin
CHANGE_USER_GENDER
USER_UNCATEGORIZED
admin
CHANGE_USER_IM
USER_UNCATEGORIZED
admin
ENABLE_USER_IP_WHITELIST
USER_UNCATEGORIZED
admin
CHANGE_USER_KEYWORD
USER_UNCATEGORIZED
admin
CHANGE_USER_LANGUAGE
USER_UNCATEGORIZED
admin
CHANGE_USER_LOCATION
USER_UNCATEGORIZED
admin
CHANGE_USER_ORGANIZATION
USER_UNCATEGORIZED
admin
CHANGE_USER_PHONE_NUMBER
USER_UNCATEGORIZED
admin
CHANGE_RECOVERY_EMAIL
USER_UNCATEGORIZED
admin
CHANGE_RECOVERY_PHONE
USER_UNCATEGORIZED
admin
CHANGE_USER_RELATION
USER_UNCATEGORIZED
admin
CHANGE_USER_ADDRESS
USER_UNCATEGORIZED
admin
CREATE_EMAIL_MONITOR
SERVICE_CREATION
admin
CREATE_DATA_TRANSFER_REQUEST
USER_UNCATEGORIZED
admin
GRANT_DELEGATED_ADMIN_PRIVILEGES
USER_CHANGE_PERMISSIONS
admin
DELETE_ACCOUNT_INFO_DUMP
USER_RESOURCE_DELETION
admin
DELETE_EMAIL_MONITOR
SERVICE_DELETION
admin
DELETE_MAILBOX_DUMP
USER_RESOURCE_DELETION
admin
DELETE_PROFILE_PHOTO
USER_RESOURCE_DELETION
admin
CHANGE_DISPLAY_NAME
USER_UNCATEGORIZED
admin
CHANGE_FIRST_NAME
USER_UNCATEGORIZED
admin
GMAIL_RESET_USER
USER_UNCATEGORIZED
admin
CHANGE_LAST_NAME
USER_UNCATEGORIZED
admin
MAIL_ROUTING_DESTINATION_ADDED
USER_RESOURCE_CREATION
admin
MAIL_ROUTING_DESTINATION_REMOVED
USER_RESOURCE_DELETION
admin
ADD_NICKNAME
USER_UNCATEGORIZED
admin
REMOVE_NICKNAME
USER_UNCATEGORIZED
admin
CHANGE_PASSWORD
USER_CHANGE_PASSWORD
admin
CHANGE_PASSWORD_ON_NEXT_LOGIN
USER_CHANGE_PASSWORD
admin
DOWNLOAD_PENDING_INVITES_LIST
STATUS_UNCATEGORIZED
admin
REMOVE_RECOVERY_EMAIL
USER_RESOURCE_DELETION
admin
REMOVE_RECOVERY_PHONE
USER_RESOURCE_DELETION
admin
REQUEST_ACCOUNT_INFO
USER_UNCATEGORIZED
admin
REQUEST_MAILBOX_DUMP
USER_UNCATEGORIZED
admin
RESEND_USER_INVITE
USER_UNCATEGORIZED
admin
RESET_SIGNIN_COOKIES
USER_RESOURCE_UPDATE_CONTENT
admin
SECURITY_KEY_REGISTERED_FOR_USER
USER_RESOURCE_CREATION
admin
REVOKE_SECURITY_KEY
USER_RESOURCE_UPDATE_PERMISSIONS
admin
USER_INVITE
USER_UNCATEGORIZED
admin
VIEW_TEMP_PASSWORD
USER_UNCATEGORIZED
admin
TURN_OFF_2_STEP_VERIFICATION
USER_RESOURCE_UPDATE_PERMISSIONS
admin
UNBLOCK_USER_SESSION
USER_UNCATEGORIZED
admin
UNMANAGED_USERS_BULK_UPLOAD
USER_RESOURCE_CREATION
admin
DOWNLOAD_UNMANAGED_USERS_LIST
USER_UNCATEGORIZED
admin
UPDATE_PROFILE_PHOTO
USER_RESOURCE_UPDATE_CONTENT
admin
UNENROLL_USER_FROM_TITANIUM
USER_UNCATEGORIZED
admin
ARCHIVE_USER
USER_UNCATEGORIZED
admin
UPDATE_BIRTHDATE
USER_UNCATEGORIZED
admin
CREATE_USER
USER_CREATION
admin
DELETE_USER
USER_DELETION
admin
DOWNGRADE_USER_FROM_GPLUS
USER_CHANGE_PERMISSIONS
admin
USER_ENROLLED_IN_TWO_STEP_VERIFICATION
USER_UNCATEGORIZED
admin
DOWNLOAD_USERLIST_CSV
STATUS_UNCATEGORIZED
admin
MOVE_USER_TO_ORG_UNIT
USER_UNCATEGORIZED
admin
USER_PUT_IN_TWO_STEP_VERIFICATION_GRACE_PERIOD
USER_UNCATEGORIZED
admin
RENAME_USER
USER_RESOURCE_UPDATE_CONTENT
admin
UNENROLL_USER_FROM_STRONG_AUTH
USER_UNCATEGORIZED
admin
SUSPEND_USER
USER_UNCATEGORIZED
admin
UNARCHIVE_USER
USER_UNCATEGORIZED
admin
UNDELETE_USER
USER_UNCATEGORIZED
admin
UNSUSPEND_USER
USER_UNCATEGORIZED
admin
UPGRADE_USER_TO_GPLUS
USER_CHANGE_PERMISSIONS
admin
USERS_BULK_UPLOAD
USER_RESOURCE_CREATION
admin
USERS_BULK_UPLOAD_NOTIFICATION_SENT
USER_UNCATEGORIZED
admin
ASSIGN_ROLE
USER_RESOURCE_UPDATE_PERMISSIONS
admin
CREATE_ROLE
USER_RESOURCE_CREATION
admin
UNASSIGN_ROLE
USER_RESOURCE_UPDATE_PERMISSIONS
admin
AUTHORIZE_API_CLIENT_ACCESS
USER_RESOURCE_ACCESS
admin
ADD_TRUSTED_DOMAINS
USER_RESOURCE_UPDATE_CONTENT
admin
CHANGE_DOMAIN_DEFAULT_TIMEZONE
USER_RESOURCE_UPDATE_CONTENT
admin
CHANGE_DOMAIN_DEFAULT_LOCALE
USER_RESOURCE_UPDATE_CONTENT
admin
CREATE_ALERT
USER_RESOURCE_CREATION
admin
REMOVE_APPLICATION
USER_RESOURCE_DELETION
admin
ADD_APPLICATION
USER_RESOURCE_CREATION
admin
REMOVE_API_CLIENT_ACCESS
USER_RESOURCE_DELETION
admin
CHANGE_SSO_SETTINGS
SETTING_MODIFICATION
admin
ALERT_CENTER_VIEW
STATUS_UNCATEGORIZED
admin
ALERT_CENTER_LIST_FEEDBACK
STATUS_UNCATEGORIZED
admin
ALERT_CENTER_GET_SIT_LINK
STATUS_UNCATEGORIZED
admin
ALERT_CENTER_LIST_CHANGE
STATUS_UNCATEGORIZED
admin
ALERT_CENTER_LIST_RELATED_ALERTS
STATUS_UNCATEGORIZED
admin
EMAIL_LOG_SEARCH
EMAIL_UNCATEGORIZED
admin
CHANGE_EMAIL_SETTING
SETTING_MODIFICATION
admin
CREATE_GMAIL_SETTING
SETTING_MODIFICATION
admin
CHANGE_GMAIL_SETTING
SETTING_MODIFICATION
admin
DELETE_GMAIL_SETTING
SETTING_MODIFICATION
admin
RELEASE_FROM_QUARANTINE
EMAIL_UNCATEGORIZED
admin
SECURITY_INVESTIGATION_QUERY
STATUS_UNCATEGORIZED
admin
SECURITY_INVESTIGATION_ACTION
STATUS_UNCATEGORIZED
admin
SECURITY_INVESTIGATION_OBJECT_CREATE_DRAFT_INVESTIGATION
STATUS_UNCATEGORIZED
admin
SECURITY_INVESTIGATION_ACTION_COMPLETION
STATUS_UNCATEGORIZED
admin
SECURITY_INVESTIGATION_EXPORT_QUERY
STATUS_UNCATEGORIZED
admin
SECURITY_INVESTIGATION_ACTION_CANCELLATION
STATUS_UNCATEGORIZED
admin
CHANGE_GROUP_SETTING
GROUP_MODIFICATION
admin
ADD_GROUP_MEMBER
GROUP_MODIFICATION
admin
CREATE_GROUP
GROUP_CREATION
admin
REMOVE_GROUP_MEMBER
GROUP_MODIFICATION
admin
UPDATE_GROUP_MEMBER_DELIVERY_SETTINGS
GROUP_MODIFICATION
admin
UPDATE_GROUP_MEMBER
GROUP_MODIFICATION
admin
DELETE_GROUP
GROUP_DELETION
admin
USER_LICENSE_ASSIGNMENT
USER_RESOURCE_UPDATE_PERMISSIONS
admin
USER_LICENSE_REVOKE
USER_RESOURCE_UPDATE_PERMISSIONS
admin
SECURITY_CHART_DRILLDOWN
STATUS_UNCATEGORIZED
admin
SYSTEM_DEFINED_RULE_UPDATED
SETTING_MODIFICATION
admin
CUSTOMER_USER_DEVICE_DELETION_EVENT
USER_RESOURCE_DELETION
admin
ADD_MOBILE_APPLICATION_TO_WHITELIST
USER_RESOURCE_UPDATE_CONTENT
admin
REMOVE_MOBILE_APPLICATION_FROM_WHITELIST
USER_RESOURCE_UPDATE_CONTENT
admin
CHANGE_MOBILE_APPLICATION_SETTINGS
SETTING_MODIFICATION
admin
ACTION_REQUESTED
USER_UNCATEGORIZED
admin
CREATE_APPLICATION_SETTING
SETTING_CREATION
admin
CHANGE_APPLICATION_SETTING
SETTING_MODIFICATION
admin
CREATE_SAML2_SERVICE_PROVIDER_CONFIG
SETTING_CREATION
admin
DELETE_SAML2_SERVICE_PROVIDER_CONFIG
SETTING_DELETION
admin
TOGGLE_SERVICE_ENABLED
SETTING_MODIFICATION
admin
CREATE_ORG_UNIT
USER_RESOURCE_CREATION
admin
MOVE_ORG_UNIT
USER_RESOURCE_UPDATE_CONTENT
admin
EDIT_ORG_UNIT_NAME
USER_RESOURCE_UPDATE_CONTENT
admin
REMOVE_ORG_UNIT
USER_RESOURCE_DELETION
admin
UNASSIGN_CUSTOM_LOGO
USER_RESOURCE_UPDATE_CONTENT
admin
ASSIGN_CUSTOM_LOGO
USER_RESOURCE_UPDATE_CONTENT
admin
EDIT_ORG_UNIT_DESCRIPTION
USER_RESOURCE_UPDATE_CONTENT
admin
CHANGE_DOCS_SETTING
SETTING_MODIFICATION
admin
CHANGE_CALENDAR_SETTING
SETTING_MODIFICATION
admin
SESSION_CONTROL_SETTINGS_CHANGE
SETTING_MODIFICATION
admin
DISALLOW_SERVICE_FOR_OAUTH2_ACCESS
SETTING_MODIFICATION
admin
ALLOW_STRONG_AUTHENTICATION
SETTING_MODIFICATION
admin
ENFORCE_STRONG_AUTHENTICATION
SETTING_MODIFICATION
admin
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
SETTING_MODIFICATION
admin
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
SETTING_MODIFICATION
admin
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
SETTING_MODIFICATION
admin
CHANGE_ALLOWED_TWO_STEP_VERIFICATION_METHODS
SETTING_MODIFICATION
admin
CHANGE_TWO_STEP_VERIFICATION_START_DATE
SETTING_MODIFICATION
admin
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
SETTING_MODIFICATION
admin
ADD_TO_BLOCKED_OAUTH2_APPS
STATUS_UPDATE
admin
ADD_TO_TRUSTED_OAUTH2_APPS
STATUS_UPDATE
admin
GENERATE_CERTIFICATE
USER_RESOURCE_CREATION
admin
ENABLE_DIRECTORY_SYNC
SETTING_MODIFICATION
admin
CHANGE_DEVICE_STATE
STATUS_UPDATE
admin
UPDATE_ACCESS_LEVEL_V2
USER_RESOURCE_UPDATE_PERMISSIONS
admin
UPDATE_AUTO_PROVISIONED_USER
STATUS_UPDATE
admin
SECURITY_CENTER_RULE_THRESHOLD_TRIGGER
STATUS_UPDATE
admin
LABEL_PERMISSION_UPDATED
USER_CHANGE_PERMISSIONS
admin
LABEL_CREATED
USER_RESOURCE_CREATION
admin
LABEL_UPDATED
USER_RESOURCE_UPDATE_CONTENT
admin
LABEL_PUBLISHED
USER_UNCATEGORIZED
gmail
EMAIL_TRANSACTION
Field mapping reference: WORKSPACE_ACTIVITY-Common Fields
The following table lists common fields of the
WORKSPACE_ACTIVITY
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
actor.callerType
target.user.attribute.labels[caller_type]
If the
event.name
log field value is equal to one of the following values, then the
actor.callerType
log field is mapped to the
target.user.attribute.labels
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.callerType
principal.user.attribute.labels[caller_type]
If the
event.name
log field value is not equal to one of the following values, then the
actor.callerType
log field is mapped to the
principal.user.attribute.labels
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
If the
id.applicationName
log field value is equal to
gmail
, then
principal.user.attribute.labels.key
UDM field is set to
actor_caller_type
and
actor.callerType
log field is mapped to
principal.user.attribute.labels.value
UDM field.
actor.email
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
actor.email
log field is mapped to the
target.user.email_addresses
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
If the
id.applicationName
log field value is equal to
gmail
, then
actor.email
log field is mapped to
principal.user.email_addresses
UDM field.
actor.email
principal.user.email_addresses
If the
event.name
log field value is not equal to one of the following values, then the
actor.email
log field is mapped to the
principal.user.email_addresses
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.email
security_result.about.email
actor.email
network.email.to
actor.key
target.user.attribute.labels[actor_key]
If the
event.name
log field value is equal to one of the following values, then the
actor.key
log field is mapped to the
target.user.attribute.labels[actor_key]
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.key
principal.user.attribute.labels[actor_key]
If the
event.name
log field value is not equal to one of the following values, then the
actor.key
log field is mapped to the
principal.user.attribute.labels[actor_key]
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.key
target.user.userid
The
actor.key
log field is mapped to the
target.user.userid
UDM field if the following conditions are met:
The
actor.callerType
log field value is equal to
KEY
.
The
event.name
log field value is equal to one of the following values:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.key
principal.user.userid
The
actor.key
log field is mapped to the
principal.user.userid
UDM field if the following conditions are met:
The
actor.callerType
log field value is equal to
KEY
.
If the
event.name
log field value is not equal to one of the following values:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.profileId
target.user.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
actor.profileId
log field is mapped to the
target.user.product_object_id
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.profileId
principal.user.product_object_id
If the
event.name
log field value is not equal to one of the following values, then the
actor.profileId
log field is mapped to the
principal.user.product_object_id
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.applicationInfo.applicationName
principal.application
actor.applicationInfo.oauthClientId
additional.fields[oauth_client_id]
actor.applicationInfo.impersonation
additional.fields[impersonation]
networkInfo.ipAsn
principal.ip_geo_artifact.network.asn
networkInfo.regionCode
principal.location.country_or_region
networkInfo.subdivisionCode
principal.location.state
etag
metadata.product_log_id
events.name
metadata.product_event_type
events.type
security_result.category_details
events.status.httpStatusCode
network.http.response_code
events.status.eventStatus
security_result.action_details
events.status.eventStatus
security_result.action
If the
events.status.eventStatus
log field value matches
SUCCEEDED
or
SUCCEEDED_WITH_WARNINGS
, then the
security_result.action
UDM field is set to
ALLOW
.
If the
events.status.eventStatus
log field value matches
FAILED
, then the
security_result.action
UDM field is set to
FAIL
.
Else, the
security_result.action
UDM field is set to
UNKNOWN_ACTION
.
events.status.errorCode
security_result.detection_fields[error_code]
events.status.errorMessage
security_result.description
userDeviceInfo.deviceType
principal.platform
If the
userDeviceInfo.deviceType
log field value matches
CHROME_OS_SYNC
or
DESKTOP_CHROME_OS
, then the
principal.platform
UDM field is set to
CHROME_OS
.
If the
userDeviceInfo.deviceType
log field value matches
DESKTOP_MAC
, then the
principal.platform
UDM field is set to
MAC
.
If the
userDeviceInfo.deviceType
log field value matches
ANDROID_SYNC
, then the
principal.platform
UDM field is set to
ANDROID
.
If the
userDeviceInfo.deviceType
log field value matches
IOS_SYNC
, then the
principal.platform
UDM field is set to
IOS
.
If the
userDeviceInfo.deviceType
log field value matches
DESKTOP_LINUX
, then the
principal.platform
UDM field is set to
LINUX
.
Else, the
principal.platform
UDM field is set to
UNKNOWN_PLATFORM
.
userDeviceInfo.deviceType
principal.asset.attribute.labels[device_type]
userDeviceInfo.deviceOsVersion
principal.platform_version
userDeviceInfo.deviceId
principal.asset.asset_id
The
principal.asset_id
is set to
AssetId:%{userDeviceInfo.deviceId}
.
id.applicationName
metadata.product_name
id.customerId
about.resource.product_object_id
id.time
metadata.event_timestamp
id.uniqueQualifier
metadata.product_log_id
ipAddress
principal.ip
kind
about.labels[kind]
(deprecated)
kind
additional.fields[kind]
ownerDomain
target.administrative_domain
If the
target.resource
log field value is
not
empty, then the
ownerDomain
log field is mapped to the
target.administrative_domain
UDM field.
If the
principal.resource
log field value is
not
empty, then the
ownerDomain
log field is mapped to the
principal.administrative_domain
If the
id.applicationName
log field value is equal to
gmail
, then
ownerDomain
log field is mapped to
principal.administrative_domain
UDM field.
about.resource.resource_type
The
about.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
actor.gaiaId
principal.user.product_object_id
If the
event.name
log field value is not equal to one of the following values, then the
actor.gaiaId
log field is mapped to the
principal.user.product_object_id
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.gaiaId
target.user.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
actor.gaiaId
log field is mapped to the
target.user.product_object_id
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.orgunitPath
principal.user.attribute.labels[org_unit_path]
If the
event.name
log field value is not equal to one of the following values, then the
actor.orgunitPath
log field is mapped to the
principal.user.attribute.labels[org_unit_path]
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.orgunitPath
target.user.attribute.labels[org_unit_path]
If the
event.name
log field value is equal to one of the following values, then the
actor.orgunitPath
log field is mapped to the
target.user.attribute.labels[org_unit_path]
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.groupId
principal.user.group_identifiers
If the
event.name
log field value is not equal to one of the following values, then the
actor.groupId
log field is mapped to the
principal.user.group_identifiers
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
actor.groupId
target.user.group_identifiers
If the
event.name
log field value is equal to one of the following values, then the
actor.groupId
log field is mapped to the
target.user.group_identifiers
UDM field:
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
LOGIN_EVENT
login_failure
login_success
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
login_failure
login_challenge
login_verification
login_success
risky_sensitive_action_allowed
logout
CHROME_OS_LOGOUT_EVENT
risky_sensitive_action_blocked
resourceDetails.id
about.resource.product_object_id
resourceDetails.title
about.resource.name
resourceDetails.type
about.resource.resource_subtype
events.resourceIds
about.resource.attribute.labels[resource_id]
resourceDetails.applicationId
about.resource.attribute.labels[application_id]
resourceDetails.relation
about.resource.attribute.labels[relation]
resourceDetails.ownerEmail
about.resource.attribute.labels[owner_email]
resourceDetails.appliedLabels.id
about.resource.attribute.labels[applied_labels_id]
resourceDetails.appliedLabels.title
about.resource.attribute.labels[applied_labels_title]
resourceDetails.appliedLabels.reason
about.resource.attribute.labels[applied_labels_reason]
resourceDetails.appliedLabels.fieldValues.reason
about.resource.attribute.labels[applied_labels_field_values_reason]
resourceDetails.appliedLabels.fieldValues.id
about.resource.attribute.labels[applied_labels_field_values_id]
resourceDetails.appliedLabels.fieldValues.displayName
about.resource.attribute.labels[applied_labels_field_values_display_name]
resourceDetails.appliedLabels.fieldValues.type
about.resource.attribute.labels[applied_labels_field_values_type]
resourceDetails.appliedLabels.fieldValues.dateValue.year
about.resource.attribute.labels[applied_labels_field_values_date_value_year]
resourceDetails.appliedLabels.fieldValues.dateValue.month
about.resource.attribute.labels[applied_labels_field_values_date_value_month]
resourceDetails.appliedLabels.fieldValues.dateValue.day
about.resource.attribute.labels[applied_labels_field_values_date_value_day]
resourceDetails.appliedLabels.fieldValues.selectionListValue.values.id
about.resource.attribute.labels[applied_labels_field_values_selection_list_value_id]
resourceDetails.appliedLabels.fieldValues.selectionListValue.values.displayName
about.resource.attribute.labels[applied_labels_field_values_selection_list_value_display_name]
resourceDetails.appliedLabels.fieldValues.selectionValue.displayName
about.resource.attribute.labels[applied_labels_field_values_selection_value_display_name]
resourceDetails.appliedLabels.fieldValues.selectionValue.id
about.resource.attribute.labels[applied_labels_field_values_selection_value_id]
resourceDetails.appliedLabels.fieldValues.userListValue.values.email
about.resource.attribute.labels[applied_labels_field_values_user_list_value_values_email]
resourceDetails.appliedLabels.fieldValues.textListValue.values
about.resource.attribute.labels[applied_labels_field_values_user_list_value_values]
Field mapping reference: WORKSPACE_ACTIVITY
The following table lists the log fields of the
WORKSPACE_ACTIVITY
log type and
their corresponding UDM fields.
Workspace application
Log field
UDM mapping
Logic
access_transparency
ACCESS_APPROVAL_REQUEST_IDS
about.labels [access_approval_request_ids]
(deprecated)
access_transparency
ACCESS_APPROVAL_REQUEST_IDS
additional.fields [access_approval_request_ids]
access_transparency
ACCESS_MANAGEMENT_POLICY
about.labels [access_management_policy]
(deprecated)
access_transparency
ACCESS_MANAGEMENT_POLICY
additional.fields [access_management_policy]
access_transparency
ACTOR_HOME_OFFICE
principal.user.office_address.country_or_region
If the
event.name
log field value is equal to
ACCESS
, then the
ACTOR_HOME_OFFICE
log field is mapped to the
principal.user.office_address.country_or_region
UDM field.
access_transparency
GSUITE_PRODUCT_NAME
target.application
If the
event.name
log field value is equal to
ACCESS
, then the
GSUITE_PRODUCT_NAME
log field is mapped to the
target.application
UDM field.
access_transparency
JUSTIFICATIONS
about.labels [justifications]
(deprecated)
If the
event.name
log field value is equal to
ACCESS
, then the
JUSTIFICATIONS
log field is mapped to the
about.labels
UDM field.
access_transparency
JUSTIFICATIONS
additional.fields [justifications]
If the
event.name
log field value is equal to
ACCESS
, then the
JUSTIFICATIONS
log field is mapped to the
additional.fields
UDM field.
access_transparency
LOG_ID
about.labels [logid]
(deprecated)
If the
event.name
log field value is equal to
ACCESS
, then the
LOG_ID
log field is mapped to the
about.labels
UDM field.
access_transparency
LOG_ID
additional.fields [logid]
If the
event.name
log field value is equal to
ACCESS
, then the
LOG_ID
log field is mapped to the
additional.fields
UDM field.
access_transparency
ON_BEHALF_OF
about.labels [on_behalf_of]
(deprecated)
If the
event.name
log field value is equal to
ACCESS
, then the
ON_BEHALF_OF
log field is mapped to the
about.labels
UDM field.
access_transparency
ON_BEHALF_OF
additional.fields [on_behalf_of]
If the
event.name
log field value is equal to
ACCESS
, then the
ON_BEHALF_OF
log field is mapped to the
additional.fields
UDM field.
access_transparency
OWNER_EMAIL
target.user.email_addresses
If the
event.name
log field value is equal to
ACCESS
, then the
OWNER_EMAIL
log field is mapped to the
target.user.email_addresses
UDM field.
access_transparency
RESOURCE_NAME
target.resource.name
If the
event.name
log field value is equal to
ACCESS
, then the
RESOURCE_NAME
log field is mapped to the
target.resource.name
UDM field.
access_transparency
TICKETS
about.labels [tickets]
(deprecated)
access_transparency
TICKETS
additional.fields [tickets]
chrome
DEVICE_NAME
target.asset.attribute.labels [device_name]
If the
event.name
log field value is equal to one of the following values, then the
DEVICE_NAME
log field is mapped to the
target.asset.attribute.labels
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
DEVICE_BOOT_STATE_CHANGE
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
CHROME_OS_REPORTING_DATA_LOST
PASSWORD_CHANGED
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
DEVICE_PLATFORM
target.asset.platform_software.platform
If the
DEVICE_PLATFORM
log field value matches
windows
, then the
target.asset.platform_software.platform
UDM field is set to
WINDOWS
.
If the
DEVICE_PLATFORM
log field value matches
mac
, then the
target.asset.platform_software.platform
UDM field is set to
MAC
.
If the
DEVICE_PLATFORM
log field value matches
linux
, then the
target.asset.platform_software.platform
UDM field is set to
LINUX
.
Else, the
target.asset.platform_software.platform
UDM field is set to
UNKNOWN_PLATFORM
.
chrome
DEVICE_USER
principal.user.user_display_name
If the
event.name
log field value is equal to
LOGIN_EVENT
, then the
DEVICE_USER
log field is mapped to the
principal.user.user_display_name
UDM field.
chrome
LOGIN_USER_NAME
target.user.user_display_name
If the
event.name
log field value is equal to
LOGIN_EVENT
, then the
LOGIN_USER_NAME
log field is mapped to the
target.user.user_display_name
UDM field.
chrome
DEVICE_USER
target.user.user_display_name
If the
event.name
log field value is equal to one of the following values, then the
DEVICE_USER
log field is mapped to the
target.user.user_display_name
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
PASSWORD_CHANGED
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
If the
event.name
log field value is equal to
LOGIN_EVENT
, then the
LOGIN_USER_NAME
log field is mapped to the
target.user.user_display_name
UDM field.
chrome
PROFILE_USER_NAME
target.user.attribute.labels [profile_user_name]
If the
event.name
log field value is equal to one of the following values, then the
PROFILE_USER_NAME
log field is mapped to the
target.user.attribute.labels
UDM field:
PASSWORD_CHANGED
PASSWORD_REUSE
CONTENT_TRANSFER
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
URL_FILTERING_INTERSTITIAL
chrome
DIRECTORY_DEVICE_ID
about.labels [directory_device_id]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
DIRECTORY_DEVICE_ID
log field is mapped to the
about.labels
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
DEVICE_BOOT_STATE_CHANGE
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
CHROME_OS_REPORTING_DATA_LOST
PASSWORD_CHANGED
PASSWORD_REUSE
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
DIRECTORY_DEVICE_ID
additional.fields [directory_device_id]
If the
event.name
log field value is equal to one of the following values, then the
DIRECTORY_DEVICE_ID
log field is mapped to the
additional.fields
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
DEVICE_BOOT_STATE_CHANGE
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
CHROME_OS_REPORTING_DATA_LOST
PASSWORD_CHANGED
PASSWORD_REUSE
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
DEVICE_ID
target.asset.asset_id
If the
event.name
log field value is equal to one of the following values, then the
DEVICE_ID
log field is mapped to the
target.asset.asset_id
UDM field:
CONTENT_TRANSFER
CONTENT_UNSCANNED
MALWARE_TRANSFER
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
chrome
VIRTUAL_DEVICE_ID
about.labels [virtual_device_id]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
VIRTUAL_DEVICE_ID
log field is mapped to the
about.labels
UDM field:
PASSWORD_CHANGED
PASSWORD_REUSE
CONTENT_TRANSFER
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
VIRTUAL_DEVICE_ID
additional.fields [virtual_device_id]
If the
event.name
log field value is equal to one of the following values, then the
VIRTUAL_DEVICE_ID
log field is mapped to the
additional.fields
UDM field:
PASSWORD_CHANGED
PASSWORD_REUSE
CONTENT_TRANSFER
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
EVENT_REASON
security_result.summary
If the
event.name
log field value is equal to one of the following values, then the
EVENT_REASON
log field is mapped to the
security_result.summary
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
DEVICE_BOOT_STATE_CHANGE
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
CHROME_OS_REPORTING_DATA_LOST
PASSWORD_REUSE
DLP_EVENT
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
BROWSER_CRASH
chrome
EVENT_RESULT
security_result.action_details
If the
event.name
log field value is equal to one of the following values, then the
EVENT_RESULT
log field is mapped to the
security_result.action_details
UDM field:
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
security_result.action
The
security_result.action
UDM field is set to
ALLOW
.
chrome
TIMESTAMP
about.labels [timestamp]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
TIMESTAMP
log field is mapped to the
about.labels
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
DEVICE_BOOT_STATE_CHANGE
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
CHROME_OS_REPORTING_DATA_LOST
PASSWORD_CHANGED
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
TIMESTAMP
additional.fields [timestamp]
If the
event.name
log field value is equal to one of the following values, then the
TIMESTAMP
log field is mapped to the
additional.fields
UDM field:
CHROME_OS_ADD_USER
CHROME_OS_REMOVE_USER
DEVICE_BOOT_STATE_CHANGE
CHROME_OS_LOGIN_FAILURE_EVENT
CHROME_OS_LOGIN_LOGOUT_EVENT
CHROME_OS_LOGIN_EVENT
CHROME_OS_LOGOUT_EVENT
CHROME_OS_REPORTING_DATA_LOST
PASSWORD_CHANGED
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
EXTENSION_REQUEST
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
CHROMEOS_AFFILIATED_LOCK_SUCCESS
CHROMEOS_AFFILIATED_UNLOCK_FAILURE
CHROMEOS_AFFILIATED_UNLOCK_SUCCESS
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
CHROMEOS_UPDATE_FAILURE
CHROMEOS_UPDATE_SUCCESS
CHROME_OS_CRD_CLIENT_CONNECTED
CHROME_OS_CRD_HOST_ENDED
CHROME_OS_CRD_HOST_STARTED
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
BROWSER_VERSION
target.resource.attribute.labels [browser_version]
If the
event.name
log field value is equal to one of the following values, then the
BROWSER_VERSION
log field is mapped to the
target.resource.attribute.labels
UDM field:
PASSWORD_CHANGED
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
LOGIN_FAILURE_REASON
security_result.description
chrome
USER_AGENT
network.http.user_agent
If the
event.name
log field value is equal to one of the following values, then the
USER_AGENT
log field is mapped to the
network.http.user_agent
UDM field:
PASSWORD_CHANGED
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
BROWSER_EXTENSION_INSTALL
URL_FILTERING_INTERSTITIAL
BROWSER_CRASH
chrome
URL
target.url
If the
event.name
log field value is equal to one of the following values, then the
URL
log field is mapped to the
about.url
UDM field:
PASSWORD_REUSE
DLP_EVENT
CONTENT_TRANSFER
CONTENT_UNSCANNED
LOGIN_EVENT
MALWARE_TRANSFER
PASSWORD_BREACH
SENSITIVE_DATA_TRANSFER
UNSAFE_SITE_VISIT
URL_FILTERING_INTERSTITIAL
chrome
SCAN_ID
about.labels [scan_id]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
SCAN_ID
log field is mapped to the
about.labels
UDM field:
CONTENT_TRANSFER
MALWARE_TRANSFER
SENSITIVE_DATA_TRANSFER
chrome
SCAN_ID
additional.fields [scan_id]
If the
event.name
log field value is equal to one of the following values, then the
SCAN_ID
log field is mapped to the
additional.fields
UDM field:
CONTENT_TRANSFER
MALWARE_TRANSFER
SENSITIVE_DATA_TRANSFER
chrome
REMOVE_USER_REASON
security_result.detection_fields [remove_user_reason]
If the
event.name
log field value is equal to
CHROME_OS_REMOVE_USER
, then the
REMOVE_USER_REASON
log field is mapped to the
security_result.detection_fields
UDM field.
chrome
NEW_BOOT_MODE
target.asset.attribute.labels [new_boot_mode]
chrome
PREVIOUS_BOOT_MODE
target.asset.attribute.labels [previous_boot_mode]
chrome
CLIENT_TYPE
target.resource.attribute.labels [client_type]
chrome
TRIGGER_USER
security_result.about.labels [trigger_user]
(deprecated)
chrome
TRIGGER_USER
additional.fields [trigger_user]
chrome
TRIGGER_DESTINATION
security_result.about.labels [trigger_destination]
(deprecated)
chrome
TRIGGER_DESTINATION
additional.fields [trigger_destination]
chrome
TRIGGER_SOURCE
security_result.about.labels [trigger_source]
(deprecated)
chrome
TRIGGER_SOURCE
additional.fields [trigger_source]
chrome
TRIGGER_TYPE
security_result.about.labels [trigger_type]
(deprecated)
chrome
TRIGGER_TYPE
additional.fields [trigger_type]
chrome
TRIGGERED_RULES_REASON
security_result.about.labels [triggered_rules_reason]
(deprecated)
chrome
TRIGGERED_RULES_REASON
additional.fields [triggered_rules_reason]
chrome
CONTENT_HASH
about.labels [content_hash]
(deprecated)
chrome
CONTENT_HASH
additional.fields [content_hash]
chrome
CONTENT_NAME
about.labels [content_name]
(deprecated)
chrome
CONTENT_NAME
additional.fields [content_name]
chrome
CONTENT_SIZE
about.labels [content_size]
(deprecated)
chrome
CONTENT_SIZE
additional.fields [content_size]
chrome
CONTENT_TYPE
about.labels [content_type]
(deprecated)
chrome
CONTENT_TYPE
additional.fields [content_type]
chrome
APP_NAME
target.application
If the
event.name
log field value is equal to one of the following values, then the
APP_NAME
log field is mapped to the
target.application
UDM field:
EXTENSION_REQUEST
BROWSER_EXTENSION_INSTALL
chrome
PRODUCT_NAME
target.application
If the
event.name
log field value is equal to one of the following values, then the
PRODUCT_NAME
log field is mapped to the
target.application
UDM field:
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
PRODUCT_NAME
log field is mapped to the
target.labels
UDM field.
chrome
PRODUCT_NAME
target.labels [product_name]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
PRODUCT_NAME
log field is mapped to the
target.application
UDM field:
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
PRODUCT_NAME
log field is mapped to the
target.labels
UDM field.
chrome
PRODUCT_NAME
additional.fields [product_name]
If the
event.name
log field value is equal to one of the following values, then the
PRODUCT_NAME
log field is mapped to the
target.application
UDM field:
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
PRODUCT_NAME
log field is mapped to the
additional.fields
UDM field.
chrome
ORG_UNIT_NAME
about.labels [org_unit_name]
(deprecated)
If the
event.name
log field value is equal to
EXTENSION_REQUEST
, then the
ORG_UNIT_NAME
log field is mapped to the
about.labels
UDM field.
chrome
ORG_UNIT_NAME
additional.fields [org_unit_name]
If the
event.name
log field value is equal to
EXTENSION_REQUEST
, then the
ORG_UNIT_NAME
log field is mapped to the
additional.fields
UDM field.
chrome
USER_JUSTIFICATION
principal.user.attribute.labels [user_justification]
chrome
FEDERATED_ORIGIN
security_result.about.labels [federated_origin]
(deprecated)
chrome
FEDERATED_ORIGIN
additional.fields [federated_origin]
chrome
IS_FEDERATED
security_result.about.labels [is_federated]
(deprecated)
chrome
IS_FEDERATED
additional.fields [is_federated]
chrome
EVIDENCE_LOCKER_FILEPATH
security_result.about.labels [evidence_locker_filepath]
(deprecated)
chrome
EVIDENCE_LOCKER_FILEPATH
additional.fields [evidence_locker_filepath]
Google Chrome
CONNECTION_TYPE
about.labels[connection_type]
(deprecated)
Google Chrome
CONNECTION_TYPE
additional.fields[connection_type]
Google Chrome
PREVIOUS_OS_VERSION
target.asset.attribute.labels[previous_os_version]
Google Chrome
VENDOR_ID
src.labels[vendor_id]
(deprecated)
Google Chrome
VENDOR_ID
additional.fields[vendor_id]
Google Chrome
LOCALIZED_URL_CATEGORY
about.labels[localized_url_category]
(deprecated)
Google Chrome
LOCALIZED_URL_CATEGORY
additional.fields[localized_url_category]
Google Chrome
VENDOR_NAME
src.labels[vendor_name]
(deprecated)
Google Chrome
VENDOR_NAME
additional.fields[vendor_name]
Google Chrome
SESSION_ID
network.session_id
Google Chrome
APP_ID
target.resource.product_object_id
If the
event.name
log field value is equal to
BROWSER_EXTENSION_INSTALL
, then the
APP_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
Google Chrome
CURRENT_OS_VERSION
target.asset.platform_software.platform_version
Google Chrome
PRODUCT_ID
target.resource.product_object_id
If the
events.name
log field value contains one of the following values, then the
PRODUCT_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
PRODUCT_ID
log field is mapped to the
target.labels
UDM field.
Google Chrome
PRODUCT_ID
target.labels[product_id]
(deprecated)
If the
events.name
log field value contains one of the following values, then the
PRODUCT_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
PRODUCT_ID
log field is mapped to the
target.labels
UDM field.
Google Chrome
PRODUCT_ID
additional.fields[product_id]
If the
events.name
log field value contains one of the following values, then the
PRODUCT_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
CHROMEOS_PERIPHERAL_ADDED
CHROMEOS_PERIPHERAL_REMOVED
CHROMEOS_PERIPHERAL_STATUS_UPDATED
Else, the
PRODUCT_ID
log field is mapped to the
additional.fields
UDM field.
Google Chrome
UNLOCK_TYPE
target.labels[unlock_type]
(deprecated)
Google Chrome
UNLOCK_TYPE
additional.fields[unlock_type]
Google Chrome
REPORT_ID
target.labels[report_id]
(deprecated)
Google Chrome
REPORT_ID
additional.fields[report_id]
Google Chrome
CHANNEL
target.labels[channel]
(deprecated)
Google Chrome
CHANNEL
additional.fields[channel]
Google Chrome
TAB_URL
additional.fields[tab_url]
context_aware_access
CAA_ACCESS_LEVEL_APPLIED
security_result.about.labels [caa_access_level_applied]
(deprecated)
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_ACCESS_LEVEL_APPLIED
log field is mapped to the
security_result.about.labels
UDM field.
context_aware_access
CAA_ACCESS_LEVEL_APPLIED
additional.fields [caa_access_level_applied]
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_ACCESS_LEVEL_APPLIED
log field is mapped to the
additional.fields
UDM field.
context_aware_access
CAA_ACCESS_LEVEL_SATISFIED
security_result.about.labels [caa_access_level_satisfied]
(deprecated)
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_ACCESS_LEVEL_SATISFIED
log field is mapped to the
security_result.about.labels
UDM field.
context_aware_access
CAA_ACCESS_LEVEL_SATISFIED
additional.fields [caa_access_level_satisfied]
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_ACCESS_LEVEL_SATISFIED
log field is mapped to the
additional.fields
UDM field.
context_aware_access
CAA_ACCESS_LEVEL_UNSATISFIED
security_result.about.labels [caa_access_level_unsatisfied]
(deprecated)
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_ACCESS_LEVEL_UNSATISFIED
log field is mapped to the
security_result.about.labels
UDM field.
context_aware_access
CAA_ACCESS_LEVEL_UNSATISFIED
additional.fields [caa_access_level_unsatisfied]
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_ACCESS_LEVEL_UNSATISFIED
log field is mapped to the
additional.fields
UDM field.
context_aware_access
CAA_APPLICATION
target.resource.name
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_APPLICATION
log field is mapped to the
target.resource.name
UDM field.
context_aware_access
target.resource.resource_type
If the
event.name
log field value is equal to
DEVICE_SETTINGS_UPDATED_EVENT
, then the
target.resource.resource_type
UDM field is set to
SETTING
.
Else, the
target.resource.resource_type
UDM field is set to
DEVICE
.
context_aware_access
CAA_DEVICE_ID
principal.asset.asset_id
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_DEVICE_ID
log field is mapped to the
principal.asset.asset_id
UDM field.
context_aware_access
CAA_DEVICE_STATE
principal.labels [caa_device_state]
(deprecated)
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_DEVICE_STATE
log field is mapped to the
principal.labels
UDM field.
context_aware_access
CAA_DEVICE_STATE
additional.fields [caa_device_state]
If the
event.name
log field value is equal to
ACCESS_DENY_EVENT
, then the
CAA_DEVICE_STATE
log field is mapped to the
additional.fields
UDM field.
context_aware_access
BLOCKED_API_ACCESS
additional.fields [blocked_api_access]
gplus
attachment_type
target.resource.attribute.labels [attachment_type]
If the
event.name
log field value is equal to one of the following values, then the
attachment_type
log field is mapped to the
target.resource.attribute.labels
UDM field:
create_comment
edit_comment
create_post
edit_post
gplus
comment_resource_name
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
comment_resource_name
log field is mapped to the
target.resource.product_object_id
UDM field:
create_comment
delete_comment
edit_comment
add_plusone
remove_plusone
gplus
post_resource_name
target.resource_ancestors.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
post_resource_name
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field:
create_comment
delete_comment
edit_comment
add_plusone
remove_plusone
add_poll_vote
remove_poll_vote
create_post
delete_post
content_manager_delete_post
edit_post
gplus
post_permalink
target.resource_ancestors.attribute.labels [post_permalink]
gplus
post_visibility
target.resource_ancestors.attribute.labels [post_visibility]
gplus
plusone_context
target.resource_ancestors.attribute.labels [plusone_context]
gplus
post_author_name
target.user.user_display_name
If the
event.name
log field value is equal to
content_manager_delete_post
, then the
post_resource_name
log field is mapped to the
target.user.user_display_name
UDM field.
data_studio
ASSET_ID
principal.resource.product_object_id
If the
ASSET_TYPE
log field value is equal to
DATA_SOURCE
, then the
ASSET_ID
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, the
ASSET_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
data_studio
ASSET_NAME
principal.resource.name
If the
ASSET_TYPE
log field value is equal to
DATA_SOURCE
, then the
ASSET_NAME
log field is mapped to the
principal.resource.name
UDM field.
Else, the
ASSET_NAME
log field is mapped to the
target.resource.name
UDM field.
data_studio
ASSET_TYPE
principal.resource.resource_subtype
If the
ASSET_TYPE
log field value is equal to
DATA_SOURCE
, then the
ASSET_TYPE
log field is mapped to the
principal.resource.resource_subtype
UDM field.
Else, the
ASSET_TYPE
log field is mapped to the
target.resource.resource_subtype
UDM field.
data_studio
ASSET_ID
target.resource.product_object_id
If the
ASSET_TYPE
log field value is equal to
DATA_SOURCE
, then the
ASSET_ID
log field is mapped to the
principal.resource.product_object_id
UDM field.
Else, the
ASSET_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
data_studio
ASSET_NAME
target.resource.name
If the
ASSET_TYPE
log field value is equal to
DATA_SOURCE
, then the
ASSET_NAME
log field is mapped to the
principal.resource.name
UDM field.
Else, the
ASSET_NAME
log field is mapped to the
target.resource.name
UDM field.
data_studio
ASSET_TYPE
target.resource.resource_subtype
If the
ASSET_TYPE
log field value is equal to
DATA_SOURCE
, then the
ASSET_TYPE
log field is mapped to the
principal.resource.resource_subtype
UDM field.
Else, the
ASSET_TYPE
log field is mapped to the
target.resource.resource_subtype
UDM field.
data_studio
CONNECTOR_TYPE
target.resource.attribute.labels[connector_type]
data_studio
EMBEDDED_IN_REPORT_ID
target.resource.attribute.labels[embedded_in_report_id]
data_studio
OWNER_EMAIL
principal.user.email_addresses
If the
actor.email
log field value is
not
equal to the
OWNER_EMAIL
, then the
OWNER_EMAIL
log field is mapped to the
principal.user.email_addresses
UDM field.
data_studio
TARGET_USER_EMAIL
target.user.email_addresses
data_studio
PRIOR_VISIBILITY
target.resource.attribute.labels [prior_visibility]
data_studio
VISIBILITY
target.resource.attribute.labels [visibility]
data_studio
NEW_VALUE
target.resource.attribute.labels [new_value]
data_studio
OLD_VALUE
target.resource.attribute.labels [old_value]
data_studio
TARGET_DOMAIN
target.domain.name [ target_domain]
data_studio
DATA_EXPORT_TYPE
target.resource.attribute.labels [data_export_type]
mobile
target.resource.resource_type
The
target.resource.resource_type
UDM field is set to
DEVICE
.
mobile
ACCOUNT_STATE
target.resource.attribute.labels [account_state]
mobile
ACTION_EXECUTION_STATUS
target.resource.attribute.labels [account_execution_status]
mobile
ACTION_ID
target.resource.attribute.labels [action_id]
mobile
ACTION_TYPE
target.resource.attribute.labels [action_type]
mobile
APK_SHA256_HASH
target.resource.attribute.labels [apk_sha256_hash]
mobile
APPLICATION_ID
target.resource.attribute.labels [application_id]
mobile
APPLICATION_MESSAGE
target.resource.attribute.labels [application_message]
mobile
APPLICATION_REPORT_KEY
target.resource.attribute.labels [application_report_key]
mobile
APPLICATION_REPORT_SEVERITY
target.resource.attribute.labels [application_report_severity]
mobile
APPLICATION_STATE
target.resource.attribute.labels [application_state]
mobile
APPLICATION_REPORT_TIMESTAMP
target.resource.attribute.labels [application_report_timestamp]
mobile
BASIC_INTEGRITY
target.resource.attribute.labels [basic_integrity]
mobile
CTS_PROFILE_MATCH
target.resource.attribute.labels [cts_profile_match]
mobile
DEVICE_COMPLIANCE
target.resource.attribute.labels [device_compliance]
mobile
DEVICE_COMPROMISED_STATE
about.target.resource.attribute.labels [device_compromised_state]
mobile
DEVICE_DEACTIVATION_REASON
target.resource.attribute.labels [device_deactivation_reason]
mobile
DEVICE_ID
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
DEVICE_ID
log field is mapped to the
target.resource.product_object_id
UDM field:
APPLICATION_EVENT
APPLICATION_REPORT_EVENT
DEVICE_REGISTER_UNREGISTER_EVENT
ADVANCED_POLICY_SYNC_EVENT
DEVICE_ACTION_EVENT
DEVICE_COMPLIANCE_CHANGED_EVENT
OS_UPDATED_EVENT
DEVICE_OWNERSHIP_CHANGE_EVENT
DEVICE_SETTINGS_UPDATED_EVENT
DEVICE_SYNC_EVENT
RISK_SIGNAL_UPDATED_EVENT
ANDROID_WORK_PROFILE_SUPPORT_ENABLED_EVENT
DEVICE_COMPROMISED_EVENT
FAILED_PASSWORD_ATTEMPTS_EVENT
SUSPICIOUS_ACTIVITY_EVENT
mobile
NEW_DEVICE_ID
target.resource.attribute.labels [new_device_id]
If the
NEW_DEVICE_ID
log field value is
not
empty, then the
NEW_DEVICE_ID
log field is mapped to the
target.resource.product_object_id
UDM field.
mobile
DEVICE_MODEL
target.resource.attribute.labels [device_model]
mobile
DEVICE_OWNERSHIP
target.resource.attribute.labels [device_ownership]
mobile
DEVICE_PROPERTY
target.resource.attribute.labels [device_property]
mobile
DEVICE_SETTING
target.resource.attribute.labels [device_setting]
mobile
DEVICE_STATUS_ON_APPLE_PORTAL
target.resource.attribute.labels [device_status_on_apple_portal]
mobile
DEVICE_TYPE
target.resource.resource_subtype
If the
event.name
log field value is equal to one of the following values, then the
DEVICE_TYPE
log field is mapped to the
target.resource.resource_subtype
UDM field:
APPLICATION_EVENT
APPLICATION_REPORT_EVENT
DEVICE_REGISTER_UNREGISTER_EVENT
ADVANCED_POLICY_SYNC_EVENT
DEVICE_ACTION_EVENT
DEVICE_COMPLIANCE_CHANGED_EVENT
OS_UPDATED_EVENT
DEVICE_OWNERSHIP_CHANGE_EVENT
DEVICE_SETTINGS_UPDATED_EVENT
DEVICE_SYNC_EVENT
RISK_SIGNAL_UPDATED_EVENT
ANDROID_WORK_PROFILE_SUPPORT_ENABLED_EVENT
DEVICE_COMPROMISED_EVENT
FAILED_PASSWORD_ATTEMPTS_EVENT
SUSPICIOUS_ACTIVITY_EVENT
mobile
FAILED_PASSWD_ATTEMPTS
target.resource.attribute.labels [failed_passwd_attempts]
mobile
IOS_VENDOR_ID
target.resource.attribute.labels [ios_vendor_id]
mobile
NEW_VALUE
target.resource.attribute.labels [new_value]
mobile
OLD_VALUE
target.resource.attribute.labels [old_value]
mobile
OS_EDITION
target.resource.attribute.labels [os_edition]
mobile
OS_PROPERTY
target.resource.attribute.labels [os_property]
mobile
OS_VERSION
target.resource.attribute.labels [os_version]
mobile
PHA_CATEGORY
security_results.detection_fields
mobile
POLICY_NAME
security_result.about.labels [policy_name]
(deprecated)
mobile
POLICY_NAME
additional.fields [policy_name]
mobile
POLICY_SYNC_RESULT
security_result.about.labels [policy_sync_result]
(deprecated)
mobile
POLICY_SYNC_RESULT
additional.fields [policy_sync_result]
mobile
POLICY_SYNC_TYPE
security_result.about.labels [policy_sync_type]
(deprecated)
mobile
POLICY_SYNC_TYPE
additional.fields [policy_sync_type]
mobile
RESOURCE_ID
target.resource.attribute.labels
If the
event.name
log field value is equal to one of the following values, then the
RESOURCE_ID
log field is mapped to the
target.resource.attribute.labels
UDM field:
APPLICATION_EVENT
APPLICATION_REPORT_EVENT
DEVICE_REGISTER_UNREGISTER_EVENT
ADVANCED_POLICY_SYNC_EVENT
DEVICE_ACTION_EVENT
DEVICE_COMPLIANCE_CHANGED_EVENT
OS_UPDATED_EVENT
DEVICE_OWNERSHIP_CHANGE_EVENT
DEVICE_SETTINGS_UPDATED_EVENT
DEVICE_SYNC_EVENT
RISK_SIGNAL_UPDATED_EVENT
ANDROID_WORK_PROFILE_SUPPORT_ENABLED_EVENT
DEVICE_COMPROMISED_EVENT
FAILED_PASSWORD_ATTEMPTS_EVENT
SUSPICIOUS_ACTIVITY_EVENT
mobile
REGISTER_PRIVILEGE
security_result.about.labels [register_privilege]
(deprecated)
mobile
REGISTER_PRIVILEGE
additional.fields
mobile
RISK_SIGNAL
security_result.about.labels [risk_signal]
(deprecated)
mobile
RISK_SIGNAL
additional.fields [risk_signal]
mobile
SECURITY_EVENT_ID
security_result.about.labels [security_event_id]
(deprecated)
If the
event.name
log field value is equal to
APPLICATION_EVENT
, then the
SECURITY_EVENT_ID
log field is mapped to the
security_result.about.labels
UDM field.
mobile
SECURITY_EVENT_ID
additional.fields
If the
event.name
log field value is equal to
APPLICATION_EVENT
, then the
SECURITY_EVENT_ID
log field is mapped to the
additional.fields
UDM field.
mobile
SECURITY_PATCH_LEVEL
security_result.about.labels [security_patch_level]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
SECURITY_PATCH_LEVEL
log field is mapped to the
security_result.about.labels
UDM field:
DEVICE_SYNC_EVENT
DEVICE_REGISTER_UNREGISTER_EVENT
mobile
SECURITY_PATCH_LEVEL
additional.fields [security_patch_level]
If the
event.name
log field value is equal to one of the following values, then the
SECURITY_PATCH_LEVEL
log field is mapped to the
additional.fields
UDM field:
DEVICE_SYNC_EVENT
DEVICE_REGISTER_UNREGISTER_EVENT
mobile
SERIAL_NUMBER
target.resource.attribute.labels [serial_number]
mobile
USER_EMAIL
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
USER_EMAIL
log field is mapped to the
target.user.email_addresses
UDM field:
APPLICATION_EVENT
APPLICATION_REPORT_EVENT
DEVICE_REGISTER_UNREGISTER_EVENT
ADVANCED_POLICY_SYNC_EVENT
DEVICE_ACTION_EVENT
DEVICE_COMPLIANCE_CHANGED_EVENT
OS_UPDATED_EVENT
DEVICE_OWNERSHIP_CHANGE_EVENT
DEVICE_SETTINGS_UPDATED_EVENT
DEVICE_SYNC_EVENT
RISK_SIGNAL_UPDATED_EVENT
ANDROID_WORK_PROFILE_SUPPORT_ENABLED_EVENT
DEVICE_COMPROMISED_EVENT
FAILED_PASSWORD_ATTEMPTS_EVENT
SUSPICIOUS_ACTIVITY_EVENT
mobile
VALUE
security_result.about.labels [value]
(deprecated)
mobile
VALUE
additional.fields [value]
mobile
WINDOWS_SYNCML_POLICY_STATUS_CODE
security_result.about.labels [windows_syncml_policy_status_code]
(deprecated)
mobile
WINDOWS_SYNCML_POLICY_STATUS_CODE
additional.fields [windows_syncml_policy_status_code]
mobile
LAST_SYNC_AUDIT_DATE
target.resource.attribute.labels[LAST_SYNC_AUDIT_DATE]
groups_enterprise
dynamic_group_query
target.group.attribute.labels [dynamic_group_query]
groups_enterprise
group_id
target.user.group_identifiers
If the
event.name
log field value is equal to one of the following values, then the
group_id
log field is mapped to the
target.user.group_identifiers
UDM field:
accept_invitation
add_info_setting
add_member
add_member_role
add_security_setting
approve_join_request
ban_member_with_moderation
change_info_setting
change_security_setting
create_group
delete_group
add_dynamic_group_query
change_dynamic_group_query
invite_member
join
add_membership_expiry
remove_membership_expiry
update_membership_expiry
reject_invitation
reject_join_request
remove_info_setting
remove_member
remove_member_role
remove_security_setting
request_to_join
revoke_invitation
unban_member
groups_enterprise
info_setting
target.group.attribute.labels [info_setting]
groups_enterprise
member_id
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
member_id
log field is mapped to the
target.user.email_addresses
UDM field:
add_member
add_member_role
add_service_account_permission
approve_join_request
ban_member_with_moderation
invite_member
add_membership_expiry
remove_membership_expiry
update_membership_expiry
reject_join_request
remove_member
remove_member_role
remove_service_account_permission
revoke_invitation
unban_member
groups_enterprise
member_role
target.user.attribute.roles.name
If the
event.name
log field value is equal to one of the following values, then the
member_role
log field is mapped to the
target.user.attribute.roles.name
UDM field:
add_member
add_member_role
add_service_account_permission
remove_member_role
remove_service_account_permission
groups_enterprise
member_type
target.user.attribute.labels[member_type]
groups_enterprise
membership_expiry
target.group.attribute.labels [membership_query]
groups_enterprise
namespace
target.group.group_display_name
groups_enterprise
new_value
target.group.attribute.labels [new_value]
groups_enterprise
old_value
target.group.attribute.labels [old_value]
groups_enterprise
value
target.group.attribute.labels [value]
groups_enterprise
security_setting
target.group.attribute.labels [security_setting]
calendar
access_level
security_result.about.labels [access_level]
(deprecated)
calendar
access_level
additional.fields [access_level]
calendar
api_kind
target.resource.attribute.labels [api_kind]
calendar
calendar_country
target.resource.attribute.labels [calendar_country]
If the
event.name
log field value is equal to
change_calendar_country
, then the
calendar_country
log field is mapped to the
target.resource.attribute.labels
UDM field.
calendar
calendar_description
target.resource.attribute.labels [calendar_description]
calendar
calendar_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
calendar_id
log field is mapped to the
target.resource.product_object_id
UDM field:
change_calendar_acls
change_calendar_country
create_calendar
delete_calendar
change_calendar_description
change_calendar_location
change_calendar_timezone
change_calendar_title
notification_triggered
add_subscription
delete_subscription
create_event
delete_event
add_event_guest
change_event_guest_response_auto
remove_event_guest
change_event_guest_response
change_event
remove_event_from_trash
restore_event
change_event_start_time
change_event_title
interop_freebusy_lookup_outbound_successful
interop_freebusy_lookup_inbound_successful
interop_exchange_resource_availability_lookup_successful
interop_freebusy_lookup_outbound_unsuccessful
interop_freebusy_lookup_inbound_unsuccessful
interop_exchange_resource_availability_lookup_unsuccessful
transfer_event_requested
transfer_event_completed
calendar
calendar_location
target.resource.attribute.labels [calendar_location]
calendar
calendar_timezone
target.resource.attribute.labels [calendar_timezone]
calendar
calendar_title
target.resource.name
If the
event.name
log field value is equal to
change_calendar_title
, then the
calendar_title
log field is mapped to the
target.resource.name
UDM field.
calendar
end_time
target.resource.attribute.labels [end_time]
calendar
start_time
target.resource.attribute.labels [start_time]
calendar
event_guest
target.labels [event_guest]
(deprecated)
calendar
event_guest
additional.fields [event_guest]
calendar
event_id
target.resource.attribute.labels [event_id]
If the
event.name
log field value is equal to one of the following values, then the
event_id
log field is mapped to the
target.resource.attribute.labels
UDM field:
notification_triggered
add_subscription
delete_subscription
create_event
delete_event
add_event_guest
change_event_guest_response_auto
remove_event_guest
change_event_guest_response
change_event
remove_event_from_trash
restore_event
change_event_start_time
change_event_title
transfer_event_requested
transfer_event_completed
calendar
event_response_status
target.resource.attribute.labels [event_response_status]
calendar
event_title
target.resource.attribute.labels [event_title]
If the
event.name
log field value is equal to one of the following values, then the
event_title
log field is mapped to the
target.resource.attribute.labels
UDM field:
create_event
delete_event
add_event_guest
change_event_guest_response_auto
remove_event_guest
change_event_guest_response
change_event
remove_event_from_trash
restore_event
change_event_start_time
change_event_title
transfer_event_requested
transfer_event_completed
calendar
old_event_title
target.resource.attribute.labels [old_event_title]
calendar
grantee_email
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
grantee_email
log field is mapped to the
target.user.email_addresses
UDM field:
change_calendar_acls
transfer_event_requested
calendar
interop_error_code
security_result.action_details
If the
event.name
log field value is equal to one of the following values, then the
interop_error_code
log field is mapped to the
security_result.action_details
UDM field:
interop_exchange_resource_list_lookup_successful
interop_freebusy_lookup_outbound_unsuccessful
interop_freebusy_lookup_inbound_unsuccessful
interop_exchange_resource_availability_lookup_unsuccessful
interop_exchange_resource_list_lookup_unsuccessful
calendar
notification_message_id
target.resource.attribute.labels [notification_message_id]
If the
event.name
log field value is equal to one of the following values, then the
notification_message_id
log field is mapped to the
target.resource.attribute.labels
UDM field:
notification_triggered
create_event
delete_event
add_event_guest
remove_event_guest
change_event_guest_response
change_event
restore_event
change_event_start_time
change_event_title
calendar
notification_method
target.resource.attribute.labels [notification_method]
If the
event.name
log field value is equal to one of the following values, then the
notification_method
log field is mapped to the
target.resource.attribute.labels
UDM field:
notification_triggered
add_subscription
delete_subscription
calendar
notification_type
target.resource.resource_subtype
If the
event.name
log field value is equal to one of the following values, then the
notification_type
log field is mapped to the
target.resource.resource_subtype
UDM field:
notification_triggered
add_subscription
delete_subscription
calendar
organizer_calendar_id
principal.user.attribute.labels[organizer_calendar_id]
If the
event.name
log field value is equal to one of the following values, then the
organizer_calendar_id
log field is mapped to the
principal.user.attribute.labels[organizer_calendar_id]
UDM field:
create_event
delete_event
add_event_guest
change_event_guest_response_auto
remove_event_guest
change_event_guest_response
change_event
remove_event_from_trash
restore_event
change_event_start_time
change_event_title
transfer_event_requested
transfer_event_completed
calendar
recipient_email
principal.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
recipient_email
log field is mapped to the
principal.user.email_addresses
UDM field:
notification_triggered
create_event
delete_event
add_event_guest
remove_event_guest
change_event_guest_response
change_event
restore_event
change_event_start_time
change_event_title
calendar
remote_ews_url
security_result.about.labels [remote_ews_url]
(deprecated)
calendar
remote_ews_url
additional.fields [remote_ews_url]
calendar
requested_period_end
security_result.about.labels [requested_period_end]
(deprecated)
calendar
requested_period_end
additional.fields [requested_period_end]
calendar
requested_period_start
security_result.about.labels [requested_period_start]
(deprecated)
calendar
requested_period_start
additional.fields [requested_period_start]
calendar
subscriber_calendar_id
principal.user.attribute.labels[subscriber_calendar_id]
calendar
user_agent
network.http.user_agent
calendar
target_calendar_id
target.resource.attribute.labels [target_calendar_id]
calendar
user_agent
network.http.user_agent
calendar
target_calendar_id
target.resource.attribute.labels [target_calendar_id]
calendar
client_side_encrypted
target.resource.attribute.labels [client_side_encrypted]
calendar
is_recurring
target.resource.attribute.labels [is_recurring]
calendar
recurring
target.resource.attribute.labels [recurring]
google_chat
actor
principal.user.email_addresses
The
event.name
log field is mapped to the
principal.user.email_addresses
UDM field if the following conditions are met:
The
actor
log field value is not equal to
actor.email
.
The
event.name
log field value is equal to one of the following values:
add_room_member
attachment_download
attachment_upload
block_room
block_user
direct_message_started
invite_accept
invite_decline
invite_send
message_edited
message_posted
message_reported
remove_room_member
room_created
reaction_added
message_deleted
google_chat
attachment_hash
target.file.sha256
If the
event.name
log field value is equal to one of the following values, then the
attachment_hash
log field is mapped to the
target.file.sha256
UDM field:
attachment_download
attachment_upload
message_edited
message_posted
google_chat
attachment_name
target.file.names
If the
event.name
log field value is equal to one of the following values, then the
attachment_name
log field is mapped to the
target.file.names
UDM field:
attachment_download
attachment_upload
message_edited
message_posted
google_chat
attachment_url
target.file.full_path
If the
event.name
log field value is equal to
attachment_download
, then the
attachment_url
log field is mapped to the
target.file.full_path
UDM field.
google_chat
dlp_scan_status
security_result.action_details
If the
event.name
log field value is equal to one of the following values, then the
dlp_scan_status
log field is mapped to the
security_result.action_details
UDM field:
attachment_upload
direct_message_started
message_edited
message_posted
google_chat
message_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
message_id
log field is mapped to the
target.resource.product_object_id
UDM field:
message_edited
message_posted
message_reported
reaction_added
message_deleted
google_chat
conference_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
message_id
log field is mapped to the
target.resource.product_object_id
UDM field:
call_ended
presentation_started
invitation_sent
google_chat
target.resource.resource_subtype
If the
event.name
log field value is equal to one of the following values, then the
target.resource.resource_subtype
UDM field is set to
Google Chat - Message
:
message_edited
message_posted
message_reported
google_chat
report_type
target.resource.attribute.labels [report_type]
google_chat
room_id
target.group.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
room_id
log field is mapped to the
target.group.product_object_id
UDM field:
add_room_member
attachment_download
attachment_upload
block_room
block_user
direct_message_started
invite_accept
invite_decline
invite_send
message_edited
message_posted
message_reported
remove_room_member
room_created
reaction_added
message_deleted
google_chat
dm_id
about.labels [dm_id]
(deprecated)
If the
event.name
log field value is equal to
direct_message_started
, then the
about.labels
UDM field is set to
dm_id
.
google_chat
dm_id
additional.fields [dm_id]
If the
event.name
log field value is equal to
direct_message_started
, then the
additional.fields
UDM field is set to
dm_id
.
google_chat
target_users
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
target_users
log field is mapped to the
target.user.email_addresses
UDM field:
add_room_member
block_user
invite_send
message_reported
remove_room_member
google_chat
retention_state
target.user.attribute.labels[retention_state]
google_chat
room_name
target.group.group_display_name
google_chat
timestamp_ms
target.resource.attribute.labels [timestamp_ms]
google_chat
external_room
about.labels[external_room]
(deprecated)
google_chat
external_room
additional.fields[external_room]
google_chat
device_type
principal.asset.attribute.labels [device_type]
google_chat
identifier_type
principal.user.attribute.labels [identifier_type]
google_chat
location_region
principal.user.attribute.labels [location_region]
google_chat
identifier
principal.user.userid
google_chat
display_name
principal.user.user_display_name
google_chat
location_country
principal.location.country_or_region
google_chat
product_type
principal.resource.resource_subtype
google_chat
ip_address
target.ip
google_chat
target_user_count
target.user.attribute.labels[target_user_count]
google_chat
duration_seconds
target.resource.attribute.labels [duration_seconds]
google_chat
meeting_code
target.resource.attribute.labels[meeting_code]
google_chat
organizer_email
about.user.email_addresses
google_chat
network_estimated_upload_kbps_mean
additional.fields [network_estimated_upload_kbps_mean]
google_chat
video_recv_fps_mean
additional.fields [video_recv_fps_mean]
google_chat
screencast_send_fps_mean
additional.fields [screencast_send_fps_mean]
google_chat
audio_recv_packet_loss_max
additional.fields [audio_recv_packet_loss_max]
google_chat
video_send_long_side_median_pixels
additional.fields [video_send_long_side_median_pixels]
google_chat
screencast_recv_packet_loss_mean
additional.fields [screencast_recv_packet_loss_mean]
google_chat
video_recv_packet_loss_mean
additional.fields [video_recv_packet_loss_mean]
google_chat
video_recv_long_side_median_pixels
additional.fields [video_recv_long_side_median_pixels]
google_chat
video_send_packet_loss_mean
additional.fields [video_send_packet_loss_mean]
google_chat
audio_send_packet_loss_max
additional.fields [audio_send_packet_loss_max]
google_chat
video_recv_short_side_median_pixels
additional.fields [video_recv_short_side_median_pixels]
google_chat
screencast_recv_bitrate_kbps_mean
additional.fields [screencast_recv_bitrate_kbps_mean]
google_chat
calendar_event_id
additional.fields [calendar_event_id]
video_send_fps_mean
additional.fields [video_send_fps_mean]
target
google_chat
audio_recv_packet_loss_mean
additional.fields [audio_recv_packet_loss_mean]
google_chat
video_recv_seconds
additional.fields [video_recv_seconds]
google_chat
video_send_packet_loss_max
additional.fields [video_send_packet_loss_max]
google_chat
network_recv_jitter_msec_max
additional.fields [network_recv_jitter_msec_max]
google_chat
network_recv_jitter_msec_mean
additional.fields [network_recv_jitter_msec_mean]
google_chat
audio_send_seconds
additional.fields [audio_send_seconds]
google_chat
screencast_send_long_side_median_pixels
additional.fields [screencast_send_long_side_median_pixels]
google_chat
screencast_recv_seconds
additional.fields [screencast_recv_seconds]
google_chat
screencast_recv_long_side_median_pixels
additional.fields [screencast_recv_long_side_median_pixels]
google_chat
screencast_send_bitrate_kbps_mean
additional.fields [screencast_send_bitrate_kbps_mean]
google_chat
screencast_send_packet_loss_max
additional.fields [screencast_send_packet_loss_max]
google_chat
video_send_bitrate_kbps_mean
additional.fields [video_send_bitrate_kbps_mean]
google_chat
screencast_send_seconds
additional.fields [screencast_send_seconds]
google_chat
audio_send_bitrate_kbps_mean
additional.fields [audio_send_bitrate_kbps_mean]
google_chat
screencast_recv_fps_mean
additional.fields [screencast_recv_fps_mean]
google_chat
audio_recv_seconds
additional.fields [audio_recv_seconds]
google_chat
video_recv_packet_loss_max
additional.fields [video_recv_packet_loss_max]
google_chat
screencast_send_packet_loss_mean
additional.fields [screencast_send_packet_loss_mean]
google_chat
network_transport_protocol
additional.fields [network_transport_protocol]
google_chat
screencast_recv_short_side_median_pixels
additional.fields [screencast_recv_short_side_median_pixels]
google_chat
screencast_send_short_side_median_pixels
additional.fields [screencast_send_short_side_median_pixels]
google_chat
screencast_recv_packet_loss_max
additional.fields [screencast_recv_packet_loss_max]
google_chat
is_external
additional.fields [is_external]
google_chat
video_send_short_side_median_pixels
additional.fields [video_send_short_side_median_pixels]
google_chat
endpoint_id
additional.fields [endpoint_id]
google_chat
network_estimated_download_kbps_mean
additional.fields [network_estimated_download_kbps_mean]
google_chat
network_send_jitter_msec_mean
additional.fields [network_send_jitter_msec_mean]
google_chat
video_send_seconds
additional.fields [video_send_seconds]
google_chat
network_rtt_msec_mean
additional.fields [network_rtt_msec_mean]
google_chat
network_congestion
additional.fields [network_congestion]
google_chat
audio_send_packet_loss_mean
additional.fields [audio_send_packet_loss_mean]
google_chat
action_time
additional.fields [action_time]
gcp
USER_EMAIL
principal.user.email_addresses
If the
actor.email
log field value is empty, then the
USER_EMAIL
log field is mapped to the
principal.user.email_addresses
UDM field.
drive
actor_is_collaborator_account
about.labels [actor_is_collaborator_account]
(deprecated)
drive
actor_is_collaborator_account
additional.fields [actor_is_collaborator_account]
drive
added_role
target.user.attribute.roles.name
If the
event.name
log field value is equal to
shared_drive_membership_change
, then the
added_role
log field is mapped to the
target.user.attribute.roles.name
UDM field.
drive
requested_role
target.user.attribute.roles.name
If the
event.name
log field value is equal to
request_access
, then the
requested_role
log field is mapped to the
target.user.attribute.roles.name
UDM field.
drive
billable
about.labels [billable]
(deprecated)
drive
billable
additional.fields [billable]
drive
copy_type
about.labels [copy_type]
(deprecated)
drive
copy_type
additional.fields [copy_type]
drive
destination_folder_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
destination_folder_id
log field is mapped to the
target.resource.product_object_id
UDM field:
add_to_folder
move
unmovable_item_reparented
drive
doc_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
doc_id
log field is mapped to the
target.resource.product_object_id
UDM field:
add_to_folder
approval_canceled
approval_comment_added
approval_completed
approval_decisions_reset
approval_due_time_change
approval_requested
approval_reviewer_change
approval_reviewer_responded
copy
create
delete
download
email_as_attachment
edit
label_added
label_added_by_item_create
label_field_changed
label_removed
add_lock
move
preview
print
remove_from_folder
rename
untrash
sheets_import_range
source_copy
trash
remove_lock
unmovable_item_reparented
upload
view
apply_security_update
shared_drive_apply_security_update
shared_drive_remove_security_update
publish_change
change_acl_editors
change_document_access_scope
change_document_access_scope_hierarchy_reconciled
change_document_visibility
change_document_visibility_hierarchy_reconciled
remove_security_update
shared_drive_membership_change
shared_drive_settings_change
sheets_import_range_access_change
change_user_access
change_user_access_hierarchy_reconciled
connected_sheets_query
create_comment
accept_suggestion
change_owner
create_suggestion
delete_comment
delete_suggestion
edit_comment
expire_access_request
reassign_comment
reject_suggestion
reopen_comment
request_access
resolve_comment
download_forms_response
email_collaborators
drive
destination_folder_title
target.resource.name
If the
event.name
log field value is equal to one of the following values, then the
destination_folder_title
log field is mapped to the
target.resource.name
UDM field:
add_to_folder
move
unmovable_item_reparented
drive
doc_title
target.resource.name
If the
event.name
log field value is equal to one of the following values, then the
doc_title
log field is mapped to the
target.resource.name
UDM field:
add_to_folder
approval_canceled
approval_comment_added
approval_completed
approval_decisions_reset
approval_due_time_change
approval_requested
approval_reviewer_change
approval_reviewer_responded
copy
create
delete
download
email_as_attachment
edit
label_added
label_added_by_item_create
label_field_changed
label_removed
add_lock
move
preview
print
remove_from_folder
rename
untrash
sheets_import_range
source_copy
trash
remove_lock
unmovable_item_reparented
upload
view
apply_security_update
shared_drive_apply_security_update
shared_drive_remove_security_update
publish_change
change_acl_editors
change_document_access_scope
change_document_access_scope_hierarchy_reconciled
change_document_visibility
change_document_visibility_hierarchy_reconciled
remove_security_update
shared_drive_membership_change
shared_drive_settings_change
sheets_import_range_access_change
change_user_access
change_user_access_hierarchy_reconciled
connected_sheets_query
create_comment
accept_suggestion
change_owner
create_suggestion
delete_comment
delete_suggestion
edit_comment
expire_access_request
reassign_comment
reject_suggestion
reopen_comment
request_access
resolve_comment
download_forms_response
email_collaborators
drive
doc_id
src.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
doc_id
log field is mapped to the
src.resource.product_object_id
UDM field:
add_to_folder
move
unmovable_item_reparented
drive
doc_title
src.resource.name
If the
event.name
log field value is equal to one of the following values, then the
doc_title
log field is mapped to the
src.resource.name
UDM field:
add_to_folder
move
unmovable_item_reparented
drive
doc_type
target.resource.attribute.labels[doc_type]
If the
event.name
log field value is equal to one of the following values, then the
doc_type
log field is mapped to the
target.resource.attribute.labels[doc_type]
UDM field:
add_to_folder
approval_canceled
approval_comment_added
approval_completed
approval_decisions_reset
approval_due_time_change
approval_requested
approval_reviewer_change
approval_reviewer_responded
copy
create
delete
download
email_as_attachment
edit
label_added
label_added_by_item_create
label_field_changed
label_removed
add_lock
move
preview
print
remove_from_folder
rename
untrash
sheets_import_range
source_copy
trash
remove_lock
unmovable_item_reparented
upload
view
apply_security_update
shared_drive_apply_security_update
shared_drive_remove_security_update
publish_change
change_acl_editors
change_document_access_scope
change_document_access_scope_hierarchy_reconciled
change_document_visibility
change_document_visibility_hierarchy_reconciled
remove_security_update
shared_drive_membership_change
shared_drive_settings_change
sheets_import_range_access_change
change_user_access
change_user_access_hierarchy_reconciled
connected_sheets_query
create_comment
accept_suggestion
change_owner
create_suggestion
delete_comment
delete_suggestion
edit_comment
expire_access_request
reassign_comment
reject_suggestion
reopen_comment
request_access
resolve_comment
download_forms_response
email_collaborators
drive
doc_type
src.resource.attribute.labels [doc_type]
If the
event.name
log field value is equal to one of the following values, then the
doc_type
log field is mapped to the
src.resource.attribute.labels [doc_type]
UDM field:
add_to_folder
move
unmovable_item_reparented
drive
field
target.resource.attribute.labels [field]
drive
field_id
target.resource.attribute.labels [field_id]
drive
is_encrypted
target.labels [is_encrypted]
(deprecated)
drive
is_encrypted
additional.fields [is_encrypted]
drive
label
target.resource.attribute.labels [label]
drive
label_title
target.resource.attribute.labels [label_title]
drive
membership_change_type
about.labels [membership_change_type]
(deprecated)
drive
membership_change_type
additional.fields [membership_change_type]
drive
new_publish_visibility
target.resource.attribute.labels [new_publish_visibility]
drive
new_value
target.resource.attribute.labels [new_value]
drive
new_value_id
target.resource.attribute.labels [new_value_id]
drive
new_settings_state
about.labels [new_settings_state]
(deprecated)
drive
new_settings_state
additional.fields [new_settings_state]
drive
old_settings_state
about.labels [old_settings_state]
(deprecated)
drive
old_settings_state
additional.fields [old_settings_state]
drive
old_publish_visibility
target.resource.attribute.labels [old_publish_visibility]
drive
old_value
target.resource.attribute.labels [old_value]
drive
old_value_id
target.resource.attribute.labels [old_value_id]
drive
old_visibility
target.resource.attribute.labels [old_visibility]
drive
originating_app_id
about.labels [originating_app_id]
(deprecated)
drive
originating_app_id
additional.fields [originating_app_id]
drive
owner
target.resource.attribute.labels[owner]
drive
owner_is_shared_drive
target.resource.attribute.labels [owner_is_shared_drive]
drive
primary_event
about.labels [primary_event]
(deprecated)
drive
primary_event
additional.fields [primary_event]
drive
reason
security_result.summary
If the
event.name
log field value is equal to one of the following values, then the
reason
log field is mapped to the
security_result.summary
UDM field:
label_added
label_added_by_item_create
label_field_changed
label_removed
drive
removed_role
target.user.attribute.labels [removed_role]
and
target.user.roles.description
If the
removed_role
log field value is equal to
commenter
,
then the
target.user.roles.description
UDM field is set to
Team Drive role Commenter
.
If the
removed_role
log field value is equal to
content_manager
,
then the
target.user.roles.description
UDM field is set to
Team Drive role Content manager
.
If the
removed_role
log field value is equal to
editor
,
then the
target.user.roles.description
UDM field is set to
Team Drive role Contributor
.
If the
removed_role
log field value is equal to
none
,
then the
target.user.roles.description
UDM field is set to
No role in Team Drive
.
If the
removed_role
log field value is equal to
organizer
,
then the
target.user.roles.description
UDM field is set to
Team Drive role Manager
.
If the
removed_role
log field value is equal to
viewer
,
then the
target.user.roles.description
UDM field is set to
Team Drive role Viewer
.
drive
target_domain
target.domain.name
If the
event.name
log field value is equal to one of the following values, then the
target_domain
log field is mapped to the
target.domain.name
UDM field:
change_document_access_scope
change_document_access_scope_hierarchy_reconciled
change_document_visibility
change_document_visibility_hierarchy_reconciled
drive
target_user
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
target_user
log field is mapped to the
target.user.email_addresses
UDM field:
change_user_access
change_user_access_hierarchy_reconciled
expire_access_request
request_access
drive
target_user
additional.fields[target_user]
drive
new_owner
target.user.email_addresses
The
new_owner
log field is mapped to the
target.user.email_addresses
UDM field if the following conditions are met:
The
event.name
log field value matches the regular expression pattern
^.+@.+$
.
The
event.name
log field value is equal to
change_owner
.
Else, the
new_owner
log field is mapped to the
target.user.attribute.labels
UDM field.
drive
target
target.user.email_addresses
If the
event.name
log field value matches the regular expression pattern
^.+@.+$
, then the
target
log field is mapped to the
target.user.email_addresses
UDM field.
drive
target
target.user.attribute.labels[target]
If the
event.name
log field value does not match the regular expression pattern
^.+@.+$
, then the
target
log field is mapped to the
target.user.attribute.labels[target]
UDM field.
drive
recipients
target.user.email_addresses
If the
event.name
log field value is equal to
email_collaborators
, then the
recipients
log field is mapped to the
target.user.email_addresses
UDM field.
drive
shared_drive_id
target.resource_ancestors.product_object_id
drive
shared_drive_settings_change_type
about.labels [shared_drive_settings_change_type]
(deprecated)
drive
shared_drive_settings_change_type
additional.fields [shared_drive_settings_change_type]
drive
sheets_import_range_recipient_doc
target.resource.attribute.labels [sheets_import_range_recipient_doc]
drive
source_folder_id
principal.resource.id
If the
event.name
log field value is equal to one of the following values, then the
source_folder_id
log field is mapped to the
principal.resource.id
UDM field:
unmovable_item_reparented
remove_from_folder
move
drive
source_folder_title
principal.resource.name
If the
event.name
log field value is equal to one of the following values, then the
source_folder_title
log field is mapped to the
principal.resource.name
UDM field:
move
remove_from_folder
unmovable_item_reparented
drive
storage_entity_id
about.labels [storage_entity_id]
(deprecated)
drive
storage_entity_id
additional.fields [storage_entity_id]
drive
storage_usage_in_bytes
about.labels [storage_usage_in_bytes]
(deprecated)
drive
storage_usage_in_bytes
additional.fields [storage_usage_in_bytes]
drive
visibility
target.resource.attribute.labels [visibility]
drive
visibility_change
target.resource.attribute.labels [visibility_change]
drive
team_drive_id
target.group.product_object_id
drive
owner_is_team_drive
target.resource.attribute.labels [owner_is_team_drive]
drive
data_connection_id
about.labels[data_connection_id]
(deprecated)
drive
data_connection_id
additional.fields[data_connection_id]
drive
delegating_principal
about.user.email_addresses
If the
actor.email
log field value is not equal to
delegating_principal
,
then the
delegating_principal
log field is mapped to
about.user.email_addresses
UDM field.
drive
execution_id
about.labels[execution_id]
(deprecated)
drive
execution_id
additional.fields[execution_id]
drive
execution_trigger
about.labels[execution_trigger]
(deprecated)
drive
execution_trigger
additional.fields[execution_trigger]
drive
query_type
about.labels[query_type]
(deprecated)
drive
query_type
additional.fields[query_type]
drive
owner_team_drive_id
target.resource.attribute.labels[owner_team_drive_id]
drive
new_owner_is_team_drive
target.resource.attribute.labels [new_owner_is_team_drive]
drive
new_owner_team_drive_id
target.resource.attribute.labels[new_owner_team_drive_id]
drive
owner_shared_drive_id
target.resource.attribute.labels[owner_shared_drive_id]
drive
dlp_info
target.resource.attribute.labels[dlp_info]
drive
team_drive_settings_change_type
target.resource.attribute.labels[team_drive_settings_change_type]
drive
accessed_url
target.url
drive
script_id
additional.fields[script_id]
drive
additional.fields[script_id]
additional.fields[api_method]
keep
attachment_name
target.resource.attribute.labels [attachment_name]
If the
event.name
log field value is equal to one of the following values, then the
attachment_name
log field is mapped to the
target.resource.attribute.labels
UDM field:
deleted_attachment
uploaded_attachment
keep
note_name
target.url
If the
event.name
log field value is equal to one of the following values, then the
note_name
log field is mapped to the
target.url
UDM field:
deleted_attachment
uploaded_attachment
edited_note_content
created_note
deleted_note
modified_acl
keep
owner_email
principal.user.email_addresses
If the
actor.email
log field value is empty, then the
owner_email
log field is mapped to the
principal.user.email_addresses
UDM field.
keep
target.resource_subtype
The
target.resource_subtype
UDM field is set to
keep
.
google_meet
action_description
security_result.action_details
If the
event.name
log field value is equal to
abuse_report_submitted
, then the
action_description
log field is mapped to the
security_result.action_details
UDM field.
google_meet
action_reason
security_result.summary
google_meet
conference_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
conference_id
log field is mapped to the
target.resource.product_object_id
UDM field:
abuse_report_submitted
call_ended
livestream_watched
knocking_accepted
knocking_denied
presentation_started
presentation_stopped
recording_activity
invitation_sent
google_meet
calendar_event_id
target.labels [calendar_event_id]
(deprecated)
google_meet
calendar_event_id
additional.fields [calendar_event_id]
google_meet
device_type
principal.asset.attribute.labels [device_type]
google_meet
display_name
principal.user.user_display_name
If the
event.name
log field value is equal to one of the following values, then the
display_name
log field is mapped to the
principal.user.user_display_name
UDM field:
abuse_report_submitted
call_ended
livestream_watched
google_meet
target_display_names
target.user.user_display_name
If the
event.name
log field value is equal to
abuse_report_submitted
, then the
target_display_name
log field is mapped to the
target.user.user_display_name
UDM field.
google_meet
duration_seconds
target.resource.attribute.labels [duration_seconds]
google_meet
end_of_call_rating
target.resource.attribute.labels  [end_of_call_rating]
google_meet
endpoint_id
security_result.about.labels [endpoint_id]
(deprecated)
google_meet
endpoint_id
additional.fields [endpoint_id]
google_meet
identifier
principal.user.userid
If the
event.name
log field value is equal to one of the following values, then the
identifier
log field is mapped to the
principal.user.userid
UDM field:
abuse_report_submitted
call_ended
knocking_accepted
knocking_denied
presentation_started
presentation_stopped
invitation_sent
google_meet
identifier_type
principal.user.attribute.labels [identifier_type]
google_meet
ip_address
target.ip
If the
ipAddress
log field value is empty, then the
ip_address
log field is mapped to the
target.ip
UDM field.
google_meet
is_external
principal.labels [is_external]
(deprecated)
google_meet
is_external
additional.fields [is_external]
google_meet
livestream_view_page_id
target.resource.attribute.labels [livestream_view_page_id]
google_meet
location_country
principal.location.country_or_region
If the
event.name
log field value is equal to
call_ended
, then the
location_country
log field is mapped to the
principal.location.country_or_region
UDM field.
google_meet
location_region
principal.user.attribute.labels [location_region]
If the
event.name
log field value is equal to
call_ended
, then the
location_region
log field is mapped to the
principal.location.country_or_region
UDM field.
google_meet
meeting_code
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
meeting_code
log field is mapped to the
target.resource.product_object_id
UDM field:
abuse_report_submitted
call_ended
livestream_watched
knocking_accepted
knocking_denied
presentation_started
presentation_stopped
invitation_sent
google_meet
organizer_email
about.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
organizer_email
log field is mapped to the
about.user.email_addresses
UDM field:
abuse_report_submitted
call_ended
livestream_watched
google_meet
product_type
principal.resource.resource_subtype
If the
event.name
log field value is equal to one of the following values, then the
product_type
log field is mapped to the
principal.resource.resource_subtype
UDM field:
abuse_report_submitted
call_ended
livestream_watched
google_meet
target_email
target.user.email_addresses
If the
event.name
log field value is equal to
abuse_report_submitted
, then the
target_email
log field is mapped to the
target.user.email_addresses
UDM field.
google_meet
target_phone_number
target.user.phone_numbers
If the
event.name
log field value is equal to
abuse_report_submitted
, then the
target_phone_number
log field is mapped to the
target.user.phone_numbers
UDM field.
google_meet
audio_recv_packet_loss_max
about.labels [audio_recv_packet_loss_max]
(deprecated)
google_meet
audio_recv_packet_loss_max
additional.fields [audio_recv_packet_loss_max]
google_meet
audio_recv_packet_loss_mean
about.labels [audio_recv_packet_loss_mean]
(deprecated)
google_meet
audio_recv_packet_loss_mean
additional.fields [audio_recv_packet_loss_mean]
google_meet
audio_recv_seconds
about.labels [audio_recv_seconds]
(deprecated)
google_meet
audio_recv_seconds
additional.fields [audio_recv_seconds]
google_meet
audio_send_bitrate_kbps_mean
about.labels [audio_send_bitrate_kbps_mean]
(deprecated)
google_meet
audio_send_bitrate_kbps_mean
additional.fields [audio_send_bitrate_kbps_mean]
google_meet
audio_send_packet_loss_max
about.labels [audio_send_packet_loss_max]
(deprecated)
google_meet
audio_send_packet_loss_max
additional.fields [audio_send_packet_loss_max]
google_meet
audio_send_packet_loss_mean
about.labels [audio_send_packet_loss_mean]
(deprecated)
google_meet
audio_send_packet_loss_mean
additional.fields [audio_send_packet_loss_mean]
google_meet
audio_send_seconds
about.labels [audio_send_seconds]
(deprecated)
google_meet
audio_send_seconds
additional.fields [audio_send_seconds]
google_meet
network_congestion
about.labels [network_congestion]
(deprecated)
google_meet
network_congestion
additional.fields [network_congestion]
google_meet
network_estimated_download_kbps_mean
about.labels [network_estimated_download_kbps_mean]
(deprecated)
google_meet
network_estimated_download_kbps_mean
additional.fields [network_estimated_download_kbps_mean]
google_meet
network_estimated_upload_kbps_mean
about.labels [network_estimated_upload_kbps_mean]
(deprecated)
google_meet
network_estimated_upload_kbps_mean
additional.fields [network_estimated_upload_kbps_mean]
google_meet
network_recv_jitter_msec_max
about.labels [network_recv_jitter_msec_max]
(deprecated)
google_meet
network_recv_jitter_msec_max
additional.fields [network_recv_jitter_msec_max]
google_meet
network_recv_jitter_msec_mean
about.labels [network_recv_jitter_msec_mean]
(deprecated)
google_meet
network_recv_jitter_msec_mean
additional.fields [network_recv_jitter_msec_mean]
google_meet
network_rtt_msec_mean
about.labels [network_rtt_msec_mean]
(deprecated)
google_meet
network_rtt_msec_mean
additional.fields [network_rtt_msec_mean]
google_meet
network_send_jitter_msec_mean
about.labels [network_send_jitter_msec_mean]
(deprecated)
google_meet
network_send_jitter_msec_mean
additional.fields [network_send_jitter_msec_mean]
google_meet
network_transport_protocol
about.labels [network_transport_protocol]
(deprecated)
google_meet
network_transport_protocol
additional.fields [network_transport_protocol]
google_meet
screencast_recv_bitrate_kbps_mean
about.labels [screencast_recv_bitrate_kbps_mean]
(deprecated)
google_meet
screencast_recv_bitrate_kbps_mean
additional.fields [screencast_recv_bitrate_kbps_mean]
google_meet
screencast_recv_fps_mean
about.labels [screencast_recv_fps_mean]
(deprecated)
google_meet
screencast_recv_fps_mean
additional.fields [screencast_recv_fps_mean]
google_meet
screencast_recv_long_side_median_pixels
about.labels [screencast_recv_long_side_median_pixels]
(deprecated)
google_meet
screencast_recv_long_side_median_pixels
additional.fields [screencast_recv_long_side_median_pixels]
google_meet
screencast_recv_packet_loss_max
about.labels [screencast_recv_packet_loss_max]
(deprecated)
google_meet
screencast_recv_packet_loss_max
additional.fields [screencast_recv_packet_loss_max]
google_meet
screencast_recv_packet_loss_mean
about.labels [screencast_recv_packet_loss_mean]
(deprecated)
google_meet
screencast_recv_packet_loss_mean
additional.fields [screencast_recv_packet_loss_mean]
google_meet
screencast_recv_seconds
about.labels [screencast_recv_seconds]
(deprecated)
google_meet
screencast_recv_seconds
additional.fields [screencast_recv_seconds]
google_meet
screencast_recv_short_side_median_pixels
about.labels [screencast_recv_short_side_median_pixels]
(deprecated)
google_meet
screencast_recv_short_side_median_pixels
additional.fields [screencast_recv_short_side_median_pixels]
google_meet
screencast_send_bitrate_kbps_mean
about.labels [screencast_send_bitrate_kbps_mean]
(deprecated)
google_meet
screencast_send_bitrate_kbps_mean
additional.fields [screencast_send_bitrate_kbps_mean]
google_meet
screencast_send_fps_mean
about.labels [screencast_send_fps_mean]
(deprecated)
google_meet
screencast_send_fps_mean
additional.fields [screencast_send_fps_mean]
google_meet
screencast_send_long_side_median_pixels
about.labels [screencast_send_long_side_median_pixels]
(deprecated)
google_meet
screencast_send_long_side_median_pixels
additional.fields [screencast_send_long_side_median_pixels]
google_meet
screencast_send_packet_loss_max
about.labels [screencast_send_packet_loss_max]
(deprecated)
google_meet
screencast_send_packet_loss_max
additional.fields [screencast_send_packet_loss_max]
google_meet
screencast_send_packet_loss_mean
about.labels [screencast_send_packet_loss_mean]
(deprecated)
google_meet
screencast_send_packet_loss_mean
additional.fields [screencast_send_packet_loss_mean]
google_meet
screencast_send_seconds
about.labels [screencast_send_seconds]
(deprecated)
google_meet
screencast_send_seconds
additional.fields [screencast_send_seconds]
google_meet
screencast_send_short_side_median_pixels
about.labels [screencast_send_short_side_median_pixels]
(deprecated)
google_meet
screencast_send_short_side_median_pixels
additional.fields [screencast_send_short_side_median_pixels]
google_meet
video_recv_fps_mean
about.labels [video_recv_fps_mean]
(deprecated)
google_meet
video_recv_fps_mean
additional.fields [video_recv_fps_mean]
google_meet
video_recv_long_side_median_pixels
about.labels [video_recv_long_side_median_pixels]
(deprecated)
google_meet
video_recv_long_side_median_pixels
additional.fields [video_recv_long_side_median_pixels]
google_meet
video_recv_packet_loss_max
about.labels [video_recv_packet_loss_max]
(deprecated)
google_meet
video_recv_packet_loss_max
additional.fields [video_recv_packet_loss_max]
google_meet
video_recv_packet_loss_mean
about.labels [video_recv_packet_loss_mean]
(deprecated)
google_meet
video_recv_packet_loss_mean
additional.fields [video_recv_packet_loss_mean]
google_meet
video_recv_seconds
about.labels [video_recv_seconds]
(deprecated)
google_meet
video_recv_seconds
additional.fields [video_recv_seconds]
google_meet
video_recv_short_side_median_pixels
about.labels [video_recv_short_side_median_pixels]
(deprecated)
google_meet
video_recv_short_side_median_pixels
additional.fields [video_recv_short_side_median_pixels]
google_meet
video_send_bitrate_kbps_mean
about.labels [video_send_bitrate_kbps_mean]
(deprecated)
google_meet
video_send_bitrate_kbps_mean
additional.fields [video_send_bitrate_kbps_mean]
google_meet
video_send_fps_mean
about.labels [video_send_fps_mean]
(deprecated)
google_meet
video_send_fps_mean
additional.fields [video_send_fps_mean]
google_meet
video_send_long_side_median_pixels
about.labels [video_send_long_side_median_pixels]
(deprecated)
google_meet
video_send_long_side_median_pixels
additional.fields [video_send_long_side_median_pixels]
google_meet
video_send_packet_loss_max
about.labels [video_send_packet_loss_max]
(deprecated)
google_meet
video_send_packet_loss_max
additional.fields [video_send_packet_loss_max]
google_meet
video_send_packet_loss_mean
about.labels [video_send_packet_loss_mean]
(deprecated)
google_meet
video_send_packet_loss_mean
additional.fields [video_send_packet_loss_mean]
google_meet
video_send_seconds
about.labels [video_send_seconds]
(deprecated)
google_meet
video_send_seconds
additional.fields [video_send_seconds]
google_meet
video_send_short_side_median_pixels
about.labels [video_send_short_side_median_pixels]
(deprecated)
google_meet
video_send_short_side_median_pixels
additional.fields [video_send_short_side_median_pixels]
google_meet
action_time
about.labels[action_time]
(deprecated)
google_meet
action_time
additional.fields[action_time]
google_meet
target_user_count
target.user.attribute.labels[target_user_count]
google_meet
streaming_session_state
about.labels[streaming_session_state]
(deprecated)
google_meet
streaming_session_state
additional.fields[streaming_session_state]
login
affected_email_address
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
affected_email_address
log field is mapped to the
target.user.email_addresses
UDM field:
account_disabled_password_leak
suspicious_login
suspicious_login_less_secure_app
suspicious_programmatic_login
account_disabled_generic
account_disabled_spamming_through_relay
account_disabled_spamming
account_disabled_hijacked
blocked_sender
login
login_timestamp
security_result.detection_fields [login_timestamp]
login
is_second_factor
about.labels[is_2sv]
(deprecated)
login
is_second_factor
additional.fields[is_2sv]
login
is_suspicious
about.labels[is_suspicious]
(deprecated)
login
is_suspicious
additional.fields[is_suspicious]
login
login_failure_type
scurity_result.summary
login
login_challenge_status
about.labels[login_challenge_status]
(deprecated)
login
login_challenge_status
additional.fields[login_challenge_status]
login
login_challenge_method
security_result.detection_fields [login_challenge_method]
login
login_challenge_method
security_result.detection_fields [login_challenge_method_attempts_count]
login
login_type
security_result.detection_fields [login_type]
login
sensitive_action_name
security_result.action_details [sensitive_action_name]
login
extensions.auth.mechanism
If the
param.value
log field value is equal to
google_password
, then the
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
Else, the
extensions.auth.mechanism
UDM field is set to
MECHANISM_UNSPECIFIED
.
login
extensions.auth.type
If the
param.value
log field value is equal to
google_password
, then the
extensions.auth.type
UDM field is set to
SSO
.
login
security_result.action
If the
event.name
log field value is equal to one of the following values, then the
security_result.action
UDM field is set to
BLOCK
:
login_failure
risky_sensitive_action_blocked
token
api_name
about.resource.attribute.labels [api_name]
token
app_name
target.resource.name
If the
event.name
log field value is equal to one of the following values, then the
app_name
log field is mapped to the
target.resource.name
UDM field:
activity
authorize
revoke
token
client_id
principal.asset.attribute.labels [client_id]
If the
event.name
log field value is equal to one of the following values, then the
client_id
log field is mapped to the
principal.asset.attribute.labels
UDM field:
activity
authorize
revoke
token
client_type
principal.asset.attribute.labels [client_type]
token
method_name
target.resource.attribute.labels [method_name]
token
num_response_bytes
target.resource.attribute.labels [num_response_bytes]
token
product_bucket
target.resource.attribute.labels product_bucket]
token
scope
target.resource.attribute.labels [scope]
token
scope_data
target.resource.attribute.labels [scope_data]
token
rejection_type
target.resource.attribute.labels [rejection_type]
rules
actions
security_result.action_details [actions]
rules
triggered_actions
security_result.action_details [actions]
rules
actor_ip_address
principal.ip
If the
ipAddress
log field value is equal to empty, then the
actor_ip_address
log field is mapped to the
principal.ip
UDM field.
rules
application
target.resource.attribute.labels[application]
rules
conference_id
target.resource.attribute.labels [conference_id]
rules
data_source
security_result.detection_fields [data_source]
rules
device_id
target.asset.asset_id
If the
event.name
log field value is equal to one of the following values, then the
device_id
log field is mapped to the
target.asset.asset_id
UDM field:
action_complete
label_field_value_changed
label_applied
rules
device_type
target.asset.attribute.labels[device_type]
rules
drive_shared_drive_id
target.resource.attribute.labels[drive_shared_drive_id]
rules
evaluation_context
about.labels [evaluation_context]
(deprecated)
rules
evaluation_context
additional.fields [evaluation_context]
rules
has_alert
security_result.about.labels [has_alert]
(deprecated)
rules
has_alert
additional.fields [has_alert]
rules
has_content_match
security_result.about.labels [has_content_match]
(deprecated)
rules
has_content_match
additional.fields [has_content_match]
rules
matched_detectors
security_result.detection_fields [matched_detectors]
rules
matched_templates
security_result.detection_fields [matched_templates]
rules
matched_threshold
security_result.detection_fields [matched_threshold]
rules
matched_trigger
security_result.detection_fields [matched_trigger]
rules
mobile_device_type
target.asset.category
If the
event.name
log field value is equal to
rule_match
, then the
mobile_device_type
log field is mapped to the
target.asset.category
UDM field.
rules
mobile_ios_vendor_id
target.asset.attribute.labels [mobile_ios_vendor_id]
rules
resource_id
target.resource.product_object_id
If the
event.name
log field value is equal to one of the following values, then the
resource_id
log field is mapped to the
target.resource.product_object_id
UDM field:
action_complete
rule_match
label_field_value_changed
label_applied
rules
resource_name
target.resource.name
If the
event.name
log field value is equal to
rule_match
, then the
resource_name
log field is mapped to the
target.resource.name
UDM field.
rules
resource_title
target.labels [resource_title]
(deprecated)
rules
resource_title
additional.fields [resource_title]
rules
resource_owner_email
principal.user.email_addresses
If the
actor.email
log field value is
not
equal to
resource_owner_email
, then the
principal.user.email_addresses
UDM field is set to
resource_owner_email
.
rules
resource_recipients
principal.user.email_addresses
If the
actor.email
log field value is
not
equal to
resource_recipients
, then the
principal.user.email_addresses
UDM field is set to
resource_recipients
.
rules
resource_recipients_omitted_count
target.labels [resource_recipients_omitted_count]
(deprecated)
rules
resource_recipients_omitted_count
additional.fields [resource_recipients_omitted_count]
rules
resource_type
target.resource.resource_subtype
If the
event.name
log field value is equal to one of the following values, then the
resource_type
log field is mapped to the
target.resource.resource_subtype
UDM field:
action_complete
label_field_value_changed
label_applied
sharing_blocked
rules
rule_name
security_result.rule_name
If the
event.name
log field value is equal to one of the following values, then the
rule_name
log field is mapped to the
security_result.rule_name
UDM field:
action_complete
rule_match
rule_trigger
label_field_value_changed
label_applied
rules
rule_id
security_result.rule_id
If the
event.name
log field value is equal to
rule_match
, then the
rule_id
log field is mapped to the
security_result.rule_id
UDM field.
rules
rule_resource_name
security_result.rule_labels [rule_resource_name]
rules
rule_type
security_result.rule_type
If the
event.name
log field value is equal to one of the following values, then the
rule_type
log field is mapped to the
security_result.rule_type
UDM field:
action_complete
rule_trigger
label_field_value_changed
sharing_blocked
rules
rule_update_time_usec
security_result.rule_labels [rule_update_time_usec]
rules
scan_type
security_result.about.labels [scan_type]
(deprecated)
rules
scan_type
additional.fields [scan_type]
rules
severity
security_result.severity
If the
event.name
log field value is equal to one of the following values, then the
severity
log field is mapped to the
security_result.severity
UDM field:
action_complete
rule_trigger
rules
space_id
target.resource.attribute.labels [space_id]
rules
space_type
target.resource.attribute.labels [space_type]
rules
suppressed_actions
security_result.about.labels [suppressed_actions]
(deprecated)
rules
suppressed_actions
additional.fields [suppressed_actions]
rules
label_field
target.resource.attribute.labels [label_field]
rules
label_title
target.resource.attribute.labels [label_title]
rules
new_value
target.resource.attribute.labels [new_value]
rules
old_value
target.resource.attribute.labels [old_value]
rules
blocked_recipients
target.user.email_addresses
rules
snippets
target.resource.attribute.labels [snippets]
saml
application_name
target.application
If the
event.name
log field value is equal to one of the following values, then the
application_name
log field is mapped to the
target.application
UDM field:
login_failure
login_success
saml
device_id
principal.asset.asset_id
If the
event.name
log field value is equal to one of the following values, then the
device_id
log field is mapped to the
principal.asset.assetid
UDM field:
login_failure
login_success
saml
failure_type
security_result.summary
If the
event.name
log field value is equal to
login_failure
, then the
failure_type
log field is mapped to the
security_result.summary
UDM field.
saml
initiated_by
security_result.detection_fields[initiated_by]
If the
event.name
log field value is equal to one of the following values, then the
initiated_by
log field is mapped to the
security_result.detection_fields
UDM field:
login_failure
login_success
saml
orgunit_path
target.user.attribute.labels [orgunit_path]
If the
event.name
log field value is equal to one of the following values, then the
orgunit_path
log field is mapped to the
target.user.attribute.labels
UDM field:
login_failure
login_success
saml
saml_second_level_status_code
security_result.about.labels [saml_second_level_status_code]
(deprecated)
saml
saml_second_level_status_code
additional.fields [saml_second_level_status_code]
saml
saml_status_code
security_result.about.labels [saml_status_code]
(deprecated)
saml
saml_status_code
additional.fields [saml_status_code]
saml
security_result.action
If the
event.name
log field value is equal to
login_failure
, then the
security_result.action
UDM field is set to
BLOCK
.
user_accounts
email_forwarding_destination_address
target.user.email_addresses
groups
acl_permission
target.group.attribute.roles.name
If the
event.name
log field value is equal to
change_acl_permission
, then the
acl_permission
log field is mapped to the
target.group.attribute.roles.name
UDM field.
groups
basic_setting
target.group.attribute.labels [basic_setting]
groups
group_email
target.group.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
group_email
log field is mapped to the
target.group.email_addresses
UDM field:
change_acl_permission
accept_invitation
approve_join_request
join
request_to_join
change_basic_setting
create_group
delete_group
change_identity_setting
add_info_setting
change_info_setting
remove_info_setting
change_new_members_restrictions_setting
change_post_replies_setting
change_spam_moderation_setting
change_topic_setting
moderate_message
always_post_from_user
add_user
ban_user_with_moderation
revoke_invitation
invite_user
reject_join_request
reinvite_user
remove_user
change_email_subscription_type
unsubscribe_via_mail
groups
identity_setting
target.group.attribute.labels [identity_setting]
groups
info_setting
target.group.attribute.labels [info_setting]
groups
message_id
network.email.mail_id
If the
event.name
log field value is equal to
moderate_message
, then the
message_id
log field is mapped to the
network.email.mail_id
UDM field.
groups
message_moderation_action
target.group.attribute.labels [message_moderation_action]
groups
member_role
target.user.attribute.roles.name
If the
event.name
log field value is equal to
add_user
, then the
member_role
log field is mapped to the
target.user.attribute.roles.name
UDM field.
groups
new_members_restrictions_setting
target.group.attribute.labels [new_members_restrictions_setting]
groups
new_value
target.group.attribute.labels [new_value]
groups
new_value_repeated
target.group.attribute.labels [new_value_repeated]
groups
old_value
target.group.attribute.labels [old_value]
groups
old_value_repeated
target.group.attribute.labels [old_value_repeated]
groups
post_replies_setting
target.group.attribute.labels [post_replies_setting]
groups
spam_moderation_setting
target.group.attribute.labels [spam_moderation_setting]
groups
status
target.group.attribute.labels[status]
groups
topic_setting
target.group.attribute.labels [topic_setting]
groups
user_email
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
user_email
log field is mapped to the
target.user.email_addresses
UDM field:
approve_join_request
always_post_from_user
add_user
ban_user_with_moderation
revoke_invitation
invite_user
reject_join_request
reinvite_user
remove_user
change_email_subscription_type
groups
user_email
principal.user.email_addresses
If the
event.name
log field value is equal to
unsubscribe_via_mail
and the
actor.email
log field value is
not
equal to the
user_email
, then the
user_email
log field is mapped to the
principal.user.email_addresses
UDM field.
groups
value
target.group.attribute.labels [value_of_info_setting]
admin
USER_EMAIL
src.user.email_addresses
If the
event.name
log field value is equal to
CREATE_DATA_TRANSFER_REQUEST
, then the
USER_EMAIL
log field is mapped to the
src.user.email_addresses
UDM field.
admin
USER_EMAIL
target.user.email_addresses
If the
event.name
log field value is equal to one of the following values, then the
USER_EMAIL
log field is mapped to the
target.user.email_addresses
UDM field:
DELETE_2SV_SCRATCH_CODES
GENERATE_2SV_SCRATCH_CODES
REVOKE_3LO_TOKEN
REVOKE_3LO_DEVICE_TOKENS
ADD_RECOVERY_EMAIL
ADD_RECOVERY_PHONE
GRANT_ADMIN_PRIVILEGE
REVOKE_ADMIN_PRIVILEGE
REVOKE_ASP
TOGGLE_AUTOMATIC_CONTACT_SHARING
BULK_UPLOAD_NOTIFICATION_SENT
CANCEL_USER_INVITE
CHANGE_USER_CUSTOM_FIELD
CHANGE_USER_EXTERNAL_ID
CHANGE_USER_GENDER
CHANGE_USER_IM
ENABLE_USER_IP_WHITELIST
CHANGE_USER_KEYWORD
CHANGE_USER_LANGUAGE
CHANGE_USER_LOCATION
CHANGE_USER_ORGANIZATION
CHANGE_USER_PHONE_NUMBER
CHANGE_RECOVERY_EMAIL
CHANGE_RECOVERY_PHONE
CHANGE_USER_RELATION
CHANGE_USER_ADDRESS
CREATE_EMAIL_MONITOR
CREATE_DATA_TRANSFER_REQUEST
CREATE_DATA_TRANSFER_REQUEST
CHANGE_PASSWORD
DELETE_ACCOUNT_INFO_DUMP
DELETE_EMAIL_MONITOR
DELETE_MAILBOX_DUMP
DELETE_PROFILE_PHOTO
CHANGE_FIRST_NAME
xyz_RESET_USER
CHANGE_LAST_NAME
MAIL_ROUTING_DESTINATION_ADDED
MAIL_ROUTING_DESTINATION_REMOVED
ADD_NICKNAME
REMOVE_NICKNAME
CHANGE_PASSWORD_ON_NEXT_LOGIN
REMOVE_RECOVERY_EMAIL
REMOVE_RECOVERY_PHONE
REQUEST_ACCOUNT_INFO
REQUEST_MAILBOX_DUMP
RESEND_USER_INVITE
RESEND_USER_INVITE
RESET_SIGNIN_COOKIES
SECURITY_KEY_REGISTERED_FOR_USER
REVOKE_SECURITY_KEY
USER_INVITE
VIEW_TEMP_PASSWORD
TURN_OFF_2_STEP_VERIFICATION
UNBLOCK_USER_SESSION
UPDATE_PROFILE_PHOTO
UNENROLL_USER_FROM_TITANIUM
ARCHIVE_USER
UPDATE_BIRTHDATE
CREATE_USER
DELETE_USER
DOWNGRADE_USER_FROM_GPLUS
USER_ENROLLED_IN_TWO_STEP_VERIFICATION
MOVE_USER_TO_ORG_UNIT
USER_PUT_IN_TWO_STEP_VERIFICATION_GRACE_PERIOD
RENAME_USER
UNENROLL_USER_FROM_STRONG_AUTH
SUSPEND_USER
UNARCHIVE_USER
UNDELETE_USER
UNSUSPEND_USER
UPGRADE_USER_TO_GPLUS
USERS_BULK_UPLOAD_NOTIFICATION_SENT
ASSIGN_ROLE
USER_LICENSE_ASSIGNMENT
USER_LICENSE_REVOKE
ADD_GROUP_MEMBER
REMOVE_GROUP_MEMBER
UNASSIGN_ROLE
ACTION_REQUESTED
admin
DESTINATION_USER_EMAIL
target.user.email_addresses
admin
DEVICE_ID
target.asset.asset_id
If the
event.name
log field value is equal to one of the following values, then the
DEVICE_ID
log field is mapped to the
target.asset.asset_id
UDM field:
REVOKE_3LO_DEVICE_TOKENS
ACTION_REQUESTED
admin
DEVICE_TYPE
target.platform
If the
DEVICE_TYPE
log field value matches the regular expression pattern
(?i)windows
, then the
target.platform
UDM field is set to
WINDOWS
.
Else, if the
DEVICE_TYPE
log field value matches the regular expression pattern
(?i)mac
, then the
target.platform
UDM field is set to
MAC
.
Else, if the
DEVICE_TYPE
log field value matches the regular expression pattern
(?i)linux
, then the
target.platform
UDM field is set to
LINUX
.
Else, if the
DEVICE_TYPE
log field value matches the regular expression pattern
(?i)ios
, then the
target.platform
UDM field is set to
IOS
.
Else, if the
DEVICE_TYPE
log field value matches the regular expression pattern
(?i)android
, then the
target.platform
UDM field is set to
ANDROID
.
Else, if the
DEVICE_TYPE
log field value matches the regular expression pattern
(?i)chrome
, then the
target.platform
UDM field is set to
CHROME_OS
.
admin
APP_ID
target.resource.name
If the
event.name
log field value is equal to one of the following values, then the
APP_ID
log field is mapped to the
target.resource.name
UDM field:
REVOKE_3LO_TOKEN
REMOVE_APPLICATION
ADD_APPLICATION
admin
NEW_VALUE
target.resource.name
If the
event.name
log field value is equal to
MAIL_ROUTING_DESTINATION_ADDED
, then the
NEW_VALUE
log field is mapped to the
target.resource.name
UDM field.
admin
SETTING_NAME
target.resource.name
If the
event.name
log field value is equal to one of the following values, then the
SETTING_NAME
log field is mapped to the
target.resource.name
UDM field:
CHANGE_GROUP_SETTING
CHANGE_EMAIL_SETTING
CREATE_APPLICATION_SETTING
CHANGE_APPLICATION_SETTING
CHANGE_DOCS_SETTING
ENFORCE_STRONG_AUTHENTICATION
CHANGE_GMAIL_SETTING
DELETE_GMAIL_SETTING
CREATE_GMAIL_SETTING
admin
CERTIFICATE_NAME
target.resource.name
If the
event.name
log field value is equal to
GENERATE_CERTIFICATE
, then the
CERTIFICATE_NAME
log field is mapped to the
target.resource.name
UDM field.
admin
ACCESS_LEVEL_NAME
target.resource.name
If the
event.name
log field value is equal to
UPDATE_ACCESS_LEVEL_V2
, then the
ACCESS_LEVEL_NAME
log field is mapped to the
target.resource.name
UDM field.
admin
ASP_ID
target.labels [asp_id]
(deprecated)
admin
ASP_ID
additional.fields [asp_id]
admin
NEW_VALUE
target.resource.attribute.labels [new_value]
If the
event.name
log field value is equal to one of the following values, then the
NEW_VALUE
log field is mapped to the
target.resource.attribute.labels
UDM field:
CHANGE_MOBILE_APPLICATION_SETTINGS
CREATE_APPLICATION_SETTING
CHANGE_APPLICATION_SETTING
CHANGE_DOCS_SETTING
CHANGE_CALENDAR_SETTING
admin
NEW_VALUE
target.labels [new_value]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
NEW_VALUE
log field is mapped to the
target.labels
UDM field:
CHANGE_DOMAIN_DEFAULT_TIMEZONE
CHANGE_DOMAIN_DEFAULT_LOCALE
TOGGLE_SERVICE_ENABLED
MOVE_ORG_UNIT
EDIT_ORG_UNIT_NAME
ALLOW_STRONG_AUTHENTICATION
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_START_DATE
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
ENFORCE_STRONG_AUTHENTICATION
admin
NEW_VALUE
additional.fields [new_value]
If the
event.name
log field value is equal to one of the following values, then the
NEW_VALUE
log field is mapped to the
additional.fields
UDM field:
CHANGE_DOMAIN_DEFAULT_TIMEZONE
CHANGE_DOMAIN_DEFAULT_LOCALE
TOGGLE_SERVICE_ENABLED
MOVE_ORG_UNIT
EDIT_ORG_UNIT_NAME
ALLOW_STRONG_AUTHENTICATION
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_START_DATE
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
ENFORCE_STRONG_AUTHENTICATION
admin
NEW_VALUE
target.user.attribute.labels [new_value]
admin
NEW_VALUE
target.user.user_display_name
If the
event.name
log field value is equal to one of the following values, then the
NEW_VALUE
log field is mapped to the
target.user.user_display_name
UDM field:
CHANGE_DISPLAY_NAME
RENAME_USER
admin
NEW_VALUE
target.user.first_name
If the
event.name
log field value is equal to
CHANGE_FIRST_NAME
, then the
NEW_VALUE
log field is mapped to the
target.user.first_name
UDM field.
admin
NEW_VALUE
target.user.last_name
If the
event.name
log field value is equal to
CHANGE_LAST_NAME
, then the
NEW_VALUE
log field is mapped to the
target.user.last_name
UDM field.
admin
OLD_VALUE
target.resource.attribute.labels [old_value]
If the
event.name
log field value is equal to one of the following values, then the
OLD_VALUE
log field is mapped to the
target.resource.attribute.labels
UDM field:
CHANGE_MOBILE_APPLICATION_SETTINGS
CREATE_APPLICATION_SETTING
CHANGE_APPLICATION_SETTING
CHANGE_DOCS_SETTING
CHANGE_CALENDAR_SETTING
admin
OLD_VALUE
target.labels [old_value]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
OLD_VALUE
log field is mapped to the
target.labels
UDM field:
CHANGE_DOMAIN_DEFAULT_TIMEZONE
CHANGE_DOMAIN_DEFAULT_LOCALE
TOGGLE_SERVICE_ENABLED
MOVE_ORG_UNIT
EDIT_ORG_UNIT_NAME
ALLOW_STRONG_AUTHENTICATION
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_START_DATE
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
ENFORCE_STRONG_AUTHENTICATION
admin
OLD_VALUE
additional.fields [old_value]
If the
event.name
log field value is equal to one of the following values, then the
OLD_VALUE
log field is mapped to the
additional.fields
UDM field:
CHANGE_DOMAIN_DEFAULT_TIMEZONE
CHANGE_DOMAIN_DEFAULT_LOCALE
TOGGLE_SERVICE_ENABLED
MOVE_ORG_UNIT
EDIT_ORG_UNIT_NAME
ALLOW_STRONG_AUTHENTICATION
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_START_DATE
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
ENFORCE_STRONG_AUTHENTICATION
admin
OLD_VALUE
target.user.attribute.labels [old_value]
admin
BULK_UPLOAD_FAIL_USERS_NUMBER
target.user.attribute.labels [bulk_upload_fail_users_number]
admin
BULK_UPLOAD_TOTAL_USERS_NUMBER
target.user.attribute.labels [bulk_upload_total_users_number]
admin
SYSTEM_DEFINED_RULE_NAME
security_result.rule_name
If the
event.name
log field value is equal to
SYSTEM_DEFINED_RULE_UPDATED
, then the
SYSTEM_DEFINED_RULE_NAME
log field is mapped to the
security_result.rule_name
UDM field.
admin
ALERT_NAME
security_result.rule_name
admin
SECURITY_CENTER_RULE_NAME
security_result.rule_name
admin
DOMAIN_NAME
target.domain.name
admin
USER_CUSTOM_FIELD
target.user.attribute.labels [user_custom_field]
admin
BEGIN_DATE_TIME
target.resource.attribute.labels [begin_date_time]
admin
EMAIL_MONITOR_DEST_EMAIL
target.resource.attribute.labels [email_monitor_dest_email]
admin
EMAIL_MONITOR_LEVEL_CHAT
target.resource.attribute.labels [email_monitor_level_chat]
admin
EMAIL_MONITOR_LEVEL_DRAFT_EMAIL
target.resource.attribute.labels [email_monitor_level_draft_email]
admin
EMAIL_MONITOR_LEVEL_INCOMING_EMAIL
target.resource.attribute.labels [email_monitor_level_incoming_email]
admin
EMAIL_MONITOR_LEVEL_OUTGOING_EMAIL
target.resource.attribute.labels [email_monitor_level_outgoing_email]
admin
END_DATE_TIME
target.resource.attribute.labels [end_date_time]
admin
APPLICATION_NAME
target.application
If the
event.name
log field value is equal to one of the following values, then the
APPLICATION_NAME
log field is mapped to the
target.application
UDM field:
CREATE_EMAIL_MONITOR
DELETE_EMAIL_MONITOR
REMOVE_APPLICATION
ADD_APPLICATION
CREATE_APPLICATION_SETTING
admin
SERVICE_NAME
target.application
If the
event.name
log field value is equal to
TOGGLE_SERVICE_ENABLED
, then the
SERVICE_NAME
log field is mapped to the
target.application
UDM field.
admin
REAUTH_APPLICATION
target.application
If the
event.name
log field value is equal to
SESSION_CONTROL_SETTINGS_CHANGE
, then the
REAUTH_APPLICATION
log field is mapped to the
target.application
UDM field.
admin
OAUTH2_SERVICE_NAME
target.application
If the
event.name
log field value is equal to
DISALLOW_SERVICE_FOR_OAUTH2_ACCESS
, then the
OAUTH2_SERVICE_NAME
log field is mapped to the
target.application
UDM field.
admin
OAUTH2_APP_NAME
target.application
If the
event.name
log field value is equal to one of the following values, then the
OAUTH2_APP_NAME
log field is mapped to the
target.application
UDM field:
ADD_TO_TRUSTED_OAUTH2_APPS
ADD_TO_BLOCKED_OAUTH2_APPS
admin
REQUEST_ID
target.labels [request_id]
(deprecated)
admin
REQUEST_ID
additional.fields [request_id]
admin
GMAIL_RESET_REASON
security_result.summary
admin
USER_NICKNAME
target.user.attribute.labels[nickname]
admin
EMAIL_EXPORT_INCLUDE_DELETED
target.resource.attribute.labels [email_export_include_deleted]
admin
EMAIL_EXPORT_PACKAGE_CONTENT
target.resource.attribute.labels [email_export_package_content]
admin
SEARCH_QUERY_FOR_DUMP
target.resource.attribute.labels [search_query_for_dump]
admin
BIRTHDATE
target.user.attribute.labels [birthdate]
admin
ORG_UNIT_NAME
target.labels[org_unit_name]
(deprecated)
If the
event.name
log field value is equal to one of the following values, then the
ORG_UNIT_NAME
log field is mapped to the
target.labels
UDM field:
TOGGLE_SERVICE_ENABLED
CREATE_ORG_UNIT
MOVE_ORG_UNIT
EDIT_ORG_UNIT_NAME
REMOVE_ORG_UNIT
UNASSIGN_CUSTOM_LOGO
ASSIGN_CUSTOM_LOGO
EDIT_ORG_UNIT_DESCRIPTION
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
CHANGE_ALLOWED_TWO_STEP_VERIFICATION_METHODS
CHANGE_TWO_STEP_VERIFICATION_START_DATE
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
admin
ORG_UNIT_NAME
additional.fields[org_unit_name]
If the
event.name
log field value is equal to one of the following values, then the
ORG_UNIT_NAME
log field is mapped to the
additional.fields
UDM field:
TOGGLE_SERVICE_ENABLED
CREATE_ORG_UNIT
MOVE_ORG_UNIT
EDIT_ORG_UNIT_NAME
REMOVE_ORG_UNIT
UNASSIGN_CUSTOM_LOGO
ASSIGN_CUSTOM_LOGO
EDIT_ORG_UNIT_DESCRIPTION
CHANGE_TWO_STEP_VERIFICATION_FREQUENCY
CHANGE_TWO_STEP_VERIFICATION_ENROLLMENT_PERIOD_DURATION
CHANGE_TWO_STEP_VERIFICATION_GRACE_PERIOD_DURATION
CHANGE_ALLOWED_TWO_STEP_VERIFICATION_METHODS
CHANGE_TWO_STEP_VERIFICATION_START_DATE
WEAK_PROGRAMMATIC_LOGIN_SETTINGS_CHANGED
admin
ORG_UNIT_NAME
about.labels[org_unit_name]
(deprecated)
admin
ORG_UNIT_NAME
additional.fields[org_unit_name]
admin
ROLE_ID
target.resource.attribute.labels[role_id]
admin
ROLE_NAME
target.resource.attribute.roles.name
admin
API_SCOPES
target.user.attribute.labels[api_scopes]
admin
API_CLIENT_NAME
target.user.userid
If the
API_CLIENT_NAME
log field value matches the regular expression
^(.){1,256}$
, then the
API_CLIENT_NAME
log field is mapped to the
target.user.userid
UDM field.
admin
API_CLIENT_NAME
target.user.attribute.labels[api_client_name]
If the
API_CLIENT_NAME
log field value doesn't match the regular expression
^(.){1,256}$
, then the
API_CLIENT_NAME
log field is mapped to the
target.user.attribute.labels[api_client_name]
UDM field.
admin
EMAIL_LOG_SEARCH_END_DATE
about.labels[email_log_search_end_date]
(deprecated)
admin
EMAIL_LOG_SEARCH_END_DATE
additional.fields[email_log_search_end_date]
admin
EMAIL_LOG_SEARCH_MSG_ID
network.email.mail_id
admin
EMAIL_LOG_SEARCH_RECIPIENT
network.email.to
admin
EMAIL_LOG_SEARCH_SENDER
network.email.from
admin
EMAIL_LOG_SEARCH_SMTP_RECIPIENT_IP
about.labels[email_log_search_smtp_recipient_ip]
(deprecated)
admin
EMAIL_LOG_SEARCH_SMTP_RECIPIENT_IP
additional.fields[email_log_search_smtp_recipient_ip]
admin
EMAIL_LOG_SEARCH_SMTP_SENDER_IP
about.labels[email_log_search_smtp_sender_ip]
(deprecated)
admin
EMAIL_LOG_SEARCH_SMTP_SENDER_IP
additional.fields[email_log_search_smtp_sender_ip]
admin
EMAIL_LOG_SEARCH_START_DATE
about.labels[email_log_search_start_date]
(deprecated)
admin
EMAIL_LOG_SEARCH_START_DATE
additional.fields[email_log_search_start_date]
admin
ALERT_ID
security_result.detection_fields[alert_id]
admin
INVESTIGATION_DATA_SOURCE
security_result.detection_fields[investigation_data_source]
admin
INVESTIGATION_QUERY
security_result.detection_fields[investigation_query]
admin
GROUP_EMAIL
target.group.email_addresses
admin
PRODUCT_NAME
target.resource.attribute.labels[product_name]
admin
INVESTIGATION_ACTION
security_result.detection_fields[investigation_action]
admin
INVESTIGATION_ENTITY_IDS
security_result.detection_fields[investigation_entity_ids]
admin
INVESTIGATION_OBJECT_IDENTIFIER
security_result.detection_fields[investigation_object_identifier]
admin
INVESTIGATION_URL_DISPLAY_TEXT
security_result.detection_fields[investigation_display_text]
admin
CHART_NAME
about.labels [chart_name]
(deprecated)
admin
CHART_NAME
additional.fields [chart_name]
admin
CHART_FILTERS
about.labels [chart_filters]
(deprecated)
admin
CHART_FILTERS
additional.fields [chart_filters]
admin
START_DATE
about.labels [start_date]
(deprecated)
admin
START_DATE
additional.fields [start_date]
admin
END_DATE
about.labels [end_date]
(deprecated)
admin
END_DATE
additional.fields [end_date]
admin
target.resource.resource_type
If the
event.name
log field value is not equal to one of the following values, then the
target.resource.resource_type
UDM field is set to
SETTING
:
EMAIL_LOG_SEARCH
ALERT_CENTER_LIST_FEEDBACK
ALERT_CENTER_GET_SIT_LINK
ALERT_CENTER_LIST_RELATED_ALERTS
ALERT_CENTER_LIST_CHANGE
SECURITY_INVESTIGATION_QUERY
SECURITY_INVESTIGATION_ACTION
SECURITY_INVESTIGATION_OBJECT_CREATE_DRAFT_INVESTIGATION
SECURITY_CHART_DRILLDOWN
CHANGE_DEVICE_STATE
SECURITY_INVESTIGATION_ACTION_COMPLETION
If the
event.name
log field value is equal to
GENERATE_CERTIFICATE
, then the
target.resource.resource_type
UDM field is set to
CREDENTIAL
.
admin
SYSTEM_DEFINED_RULE_ACTION_STATUS_CHANGE
security_result.rule_labels[system_defined_rule_action_status_change]
admin
SYSTEM_DEFINED_RULE_ACTION_SEVERITY_CHANGE
security_result.rule_labels[system_defined_rule_action_severity_change]
admin
SYSTEM_DEFINED_RULE_ACTION_RECEIVERS_CHANGE
security_result.rule_labels[system_defined_rule_action_receivers_change]
admin
COMPANY_DEVICE_ID
target.asset_id
admin
APPLICATION_ENABLED
target.labels[application_enabled]
(deprecated)
admin
APPLICATION_ENABLED
additional.fields[application_enabled]
admin
DISTRIBUTION_ENTITY_NAME
target.labels[distribution_entity_name]
(deprecated)
admin
DISTRIBUTION_ENTITY_NAME
additional.fields[distribution_entity_name]
admin
DISTRIBUTION_ENTITY_TYPE
target.labels[distribution_entity_type]
(deprecated)
admin
DISTRIBUTION_ENTITY_TYPE
additional.fields[distribution_entity_type]
admin
MOBILE_APP_PACKAGE_ID
target.labels[mobile_app_package_id]
(deprecated)
admin
MOBILE_APP_PACKAGE_ID
additional.fields[mobile_app_package_id]
admin
APPLICATION_EDITION
target.labels[application_edition]
(deprecated)
admin
APPLICATION_EDITION
additional.fields[application_edition]
admin
REAUTH_SETTING_NEW
target.labels[reauth_setting_new]
(deprecated)
admin
REAUTH_SETTING_NEW
additional.fields[reauth_setting_new]
admin
REAUTH_SETTING_OLD
target.labels[reauth_setting_old]
(deprecated)
admin
REAUTH_SETTING_OLD
additional.fields[reauth_setting_old]
admin
ALLOWED_TWO_STEP_VERIFICATION_METHOD
target.labels[allowed_2sv_method]
(deprecated)
admin
ALLOWED_TWO_STEP_VERIFICATION_METHOD
additional.fields[allowed_2sv_method]
admin
CERTIFICATE_TYPE
target.resource.resource_subtype
admin
SAML2_SERVICE_PROVIDER_ENTITY_ID
about.labels[saml2_service_provider_entity_id]
(deprecated)
admin
SAML2_SERVICE_PROVIDER_ENTITY_ID
additional.fields[saml2_service_provider_entity_id]
admin
SAML2_SERVICE_PROVIDER_NAME
about.labels[saml2_service_provider_name]
(deprecated)
admin
SAML2_SERVICE_PROVIDER_NAME
additional.fields[saml2_service_provider_name]
admin
SERVICE_ACCOUNT_EMAIL
about.user.email_addresses
admin
about.user.account_type
If the
event.name
log field value is equal to
ENABLE_DIRECTORY_SYNC
and the
SERVICE_ACCOUNT_EMAIL
log field value is
not
empty, then the
about.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
admin
DEVICE_NEW_STATE
target.asset.attribute.labels[device_new_state]
admin
DEVICE_PREVIOUS_STATE
target.asset.attribute.labels[device_previous_state]
admin
DEVICE_SERIAL_NUMBER
target.asset.hardware.serial_number
admin
INVESTIGATION_ACTION_NUM_ATTEMPTED
security_result.detection_fields[investigation_action_num_attempt]
admin
INVESTIGATION_ACTION_NUM_SUCCESS
security_result.detection_fields[investigation_action_num_success]
admin
INVESTIGATION_ACTION_NUM_FAILED
security_result.detection_fields[investigation_action_num_failed]
admin
INVESTIGATION_ACTION_IDENTIFIER
security_result.detection_fields[investigation_action_identifier]
admin
INVESTIGATION_ACTION_ID
security_result.detection_fields[investigation_action_id]
admin
SETTING_DESCRIPTION
target.resource.attribute.labels[setting_description]
admin
USER_DEFINED_SETTING_NAME
target.resource.attribute.labels[user_defined_setting_name]
admin
ACTION_TYPE
security_result.action_details
admin
security_result.action
If the
ACTION_TYPE
log field value is equal to
BLOCK
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, the
security_result.action
UDM field is set to
ALLOW
.
admin
ACTION_ID
security_result.detection_fields[action_id]
admin
OAUTH2_APP_ID
additional.fields [oauth2_app_id]
admin
OAUTH2_APP_TYPE
additional.fields [oauth2_app_type]
admin
ACCESS_LEVEL_TITLE
target.resource.attribute.labels [access_level_title]
admin
ACCESS_LEVEL_CURR_STATE
target.resource.attribute.labels [access_level_curr_state]
admin
ACCESS_LEVEL_PREV_STATE
target.resource.attribute.labels [access_level_prev_state]
admin
AUTH_PRINCIPLE_EMAIL
principal.user.email_addresses
If the
actor.email
log field value is
not
equal to the
AUTH_PRINCIPLE_EMAIL
, then the
AUTH_PRINCIPLE_EMAIL
log field is mapped to the
principal.user.email_addresses
UDM field.
admin
INVESTIGATION_ADMIN_EMAIL
principal.user.email_addresses
If the
actor.email
log field value is
not
equal to the
INVESTIGATION_ADMIN_EMAIL
, then the
INVESTIGATION_ADMIN_EMAIL
log field is mapped to the
principal.user.email_addresses
UDM field.
admin
target.resource.resource_type
If the
event.name
log field value is equal to
UPDATE_ACCESS_LEVEL_V2
, then the
target.resource.resource_type
UDM field is set to
ACCESS_POLICY
.
admin
APP_RESOURCE_ID
additional.fields [app_resource_id]
admin
SECURITY_CENTER_RULE_TRIGGER_WINDOW
security_result.rule_labels[security_center_rule_trigger_window]
admin
SECURITY_CENTER_RULE_CONDITION
security_result.rule_labels[security_center_rule_condition]
admin
SECURITY_CENTER_RULE_THRESHOLD
security_result.rule_labels[security_center_rule_threshold]
admin
SECURITY_CENTER_RULE_TIME_FRAME
security_result.rule_labels[security_center_rule_time_frame]
admin
SECURITY_CENTER_RULE_ACTION
security_result.rule_labels[security_center_rule_action]
admin
QUARANTINE_NAME
additional.fields[quarantine_name]
admin
LABEL_NAME
target.resource.name
If the
event.name
log field value is equal to one of the following values, then the
LABEL_NAME
log field is mapped to the
target.resource.name
UDM field:
LABEL_CREATED
LABEL_UPDATED
LABEL_PERMISSION_UPDATED
LABEL_PUBLISHED
admin
LABEL_ID
target.resource.product_object_id
admin
LABEL_PRINCIPAL_ROLE
target.resource.attribute.labels[label_principal_role]
admin
LABEL_PREVIOUS_PRINCIPAL_ROLE
target.resource.attribute.labels[label_previous_principal_role]
admin
LABEL_PRINCIPAL
target.resource.attribute.labels[label_principal]
admin
LABEL_REVISION_ID
target.resource.attribute.labels[label_revision_id]
jamboard
CURRENT_JAMBOARD_NAME
target.asset.attribute.labels [current_jamboard_name]
If the
event.name
log field value is equal to one of the following values, then the
CURRENT_JAMBOARD_NAME
log field is mapped to the
target.asset.attribute.labels
UDM field:
DEVICE_LICENSE_ENROLLMENT_CHANGE
DEVICE_OTA_UPDATE_REQUESTED
DEVICE_PROVISIONING_CHANGE
DEVICE_REBOOT_REQUESTED
ADB_ENABLED_STATE_CHANGE
DEVICE_ADDITIONAL_IMES_CHANGE
DEVICE_LOGGING_CHANGE
DEMO_MODE_AVAILABILITY_CHANGE
DEMO_MODE_CHANGE
FINGER_ERASING_CHANGE
DEVICE_LANGUAGE_CHANGE
DEVICE_LOCATION_CHANGE
DEVICE_NAME_CHANGE
DEVICE_NOTE_CHANGE
DEVICE_PAIRING_CHANGE
SCREENSAVER_TIMEOUT_CHANGE
DEVICE_SETTING_LOCKED
DEVICE_SETTING_UNLOCKED
VIDEOCONF_ENABLED_CHANGE
DEVICE_UPDATE
jamboard
JAMBOARD_ID
target.asset.asset_id
jamboard
LICENSE_ENROLLMENT_STATE
target.asset.attribute.labels [license_enrollment_state]
jamboard
PROVISION_STATE
target.asset.attribute.labels [provision_state]
jamboard
ON_OFF
target.asset.attribute.labels [on_off]
jamboard
NEW_ADDITIONAL_IMES
target.asset.attribute.labels [new_additional_imes]
jamboard
OLD_ADDITIONAL_IMES
target.asset.attribute.labels [old_additional_imes]
jamboard
NEW_DEMO_MODE_AVAILABILITY
target.asset.attribute.labels [new_demo_mode_availability]
jamboard
OLD_DEMO_MODE_AVAILABILITY
target.asset.attribute.labels [old_demo_mode_availability]
jamboard
NEW_LANGUAGE
target.asset.attribute.labels [new_language]
jamboard
OLD_LANGUAGE
target.asset.attribute.labels [old_language]
jamboard
NEW_LOCATION
target.asset.location.name
If the
event.name
log field value is equal to
DEVICE_LOCATION_CHANGE
, then the
NEW_LOCATION
log field is mapped to the
target.asset.location.name
UDM field.
jamboard
OLD_LOCATION
target.asset.attribute.labels [old_location]
jamboard
OLD_JAMBOARD_NAME
target.asset.attribute.labels [old_jamboard_name]
jamboard
NEW_NOTE
target.resource.attribute.labels [new_note]
jamboard
OLD_NOTE
target.resource.attribute.labels [old_note]
jamboard
DEVICE_TYPE
target.asset.attribute.labels [device_type]
jamboard
NEW_DEVICE
target.asset.attribute.labels [new_device]
jamboard
OLD_DEVICE
target.asset.attribute.labels [old_device]
jamboard
NEW_TIMEOUT_VALUE
target.asset.attribute.labels [new_timeout_value]
jamboard
OLD_TIMEOUT_VALUE
target.asset.attribute.labels [old_timeout_value]
jamboard
JAMBOARD_SETTING
target.asset.attribute.labels [jamboard_setting]
jamboard
COMPONENT
target.asset.attribute.labels [component]
jamboard
NEW_VERSION
target.asset.software.version
If the
event.name
log field value is equal to
DEVICE_UPDATE
, then the
NEW_VERSION
log field is mapped to the
target.asset.software.version
UDM field.
jamboard
OLD_VERSION
target.asset.attribute.labels [old_version]
gmail
events.parameters[delivery].msgValue[message_info].parameter.value[description]
metadata.description
gmail
events.parameters[delivery].msgValue[event_info].parameter.intValue[timestamp_usec]
metadata.event_timestamp
gmail
events.parameters[delivery].msgValue[event_info].parameter.intValue[mail_event_type]
metadata.product_event_type
gmail
id.applicationName
metadata.product_name
gmail
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google Workspace
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.value[rfc2822_message_id]
network.email.mail_id
gmail
events.parameters[delivery].msgValue[message_info].parameter.value[subject]
network.email.subject
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[payload_size]
network.sent_bytes
gmail
events.parameters[delivery].msgValue[event_info].parameter.intValue[elapsed_time_usec]
network.session_duration
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_tls_state]
network.smtp.is_tls
If this log field value is equal to
0
, then the
network.smtp.is_tls
UDM field is set to
false
.
Else, if this log field value is equal to
1
, then the
network.smtp.is_tls
UDM field is set to
true
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.value[address]
network.smtp.rcpt_to
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_response_reason]
network.smtp.server_response
If this log field value is equal to
1
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Default reason messages are rejected or accepted
.
Else, if this log field value is equal to
3
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Malware
.
Else, if this log field value is equal to
4
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
DMARC policy
.
Else, if this log field value is equal to
5
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Unsupported attachment (by Gmail)
.
Else, if this log field value is equal to
6
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Receive limit exceeded
.
Else, if this log field value is equal to
7
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Account over quota
.
Else, if this log field value is equal to
8
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Bad PTR record
.
Else, if this log field value is equal to
9
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Recipient doesn't exist
.
Else, if this log field value is equal to
10
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Customer policy
.
Else, if this log field value is equal to
12
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
RFC violation
.
Else, if this log field value is equal to
13
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Blatant spam
.
Else, if this log field value is equal to
14
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Denial of service
.
Else, if this log field value is equal to
15
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Malicious or spammy links
.
Else, if this log field value is equal to
16
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Low IP reputation
.
Else, if this log field value is equal to
17
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Low domain reputation
.
Else, if this log field value is equal to
18
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
IP listed in public Real-time Blackhole List (RBL)
.
Else, if this log field value is equal to
19
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Temporarily rejected due to DoS limits
.
Else, if this log field value is equal to
20
, then the
network.smtp.server_response
UDM field is set to
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.intValue[smtp_reply_code]
-
Permanently rejected due to DoS limits
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[smtp_tls_cipher]
network.tls.cipher
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[smtp_tls_version]
network.tls.version
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[client_host_zone]
principal.administrative_domain
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[service]
principal.application
gmail
events.parameters[delivery].msgValue[message_owner].parameter.value[customer_domain]
principal.domain.name
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[client_ip]
principal.ip
gmail
actor.gaiaId
principal.labels[actor_gaiaid]
(deprecated)
gmail
actor.gaiaId
additional.fields[actor_gaiaid]
gmail
actor.orgunitPath
principal.labels[actor_orgunitpath]
(deprecated)
gmail
actor.orgunitPath
additional.fields[actor_orgunitpath]
gmail
events.parameters[delivery].msgValue[message_owner].parameter.multiIntValue[gaia_ids]
principal.labels[message_owner_gaia_id]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_owner].parameter.multiIntValue[gaia_ids]
additional.fields[message_owner_gaia_id]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[selector]
principal.labels[source_selector]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[selector]
additional.fields[source_selector]
gmail
events.parameters[delivery].msgValue[message_owner].parameter.multiStrValue[addresses]
principal.user.email_addresses
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[from_header_address]
principal.network.email.from
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[from_header_address]
network.email.from
gmail
actor.email
principal.network.email.to
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[address]
principal.user.email_addresses
gmail
events.parameters[delivery].msgValue[message_owner].parameter.multiStrValue[addresses]
principal.user.email_addresses
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.value[from_header_displayname]
principal.user.user_display_name
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[source].parameter.intValue[user_id]
principal.user.userid
gmail
events.parameters[delivery].msgValue[message_info].parameter.value[flattened_destinations]
target.labels[flattened_destinations]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.value[flattened_destinations]
additional.fields[flattened_destinations]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.value[service]
target.application
This log field is mapped to
target.application
UDM field when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to the
about.application
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.intValue[rcpt_response]
target.labels[destination_rcpt_response]
(deprecated)
This log field is mapped to
target.labels.value
UDM field and
target.labels.key
is set to
destination_rcpt_response
, when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to
about.labels.value
UDM field and
about.labels.key
is set to
destination_rcpt_response
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.intValue[rcpt_response]
additional.fields[destination_rcpt_response]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.value[selector]
target.labels[destination_selector]
(deprecated)
This log field is mapped to
target.labels.value
UDM field and
target.labels.key
is set to
destination_selector
, when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to
about.labels.value
UDM field and
about.labels.key
is set to
destination_selector
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.value[selector]
additional.fields[destination_selector]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_decryption_success]
target.labels[destination_smime_decryption_success]
(deprecated)
This log field is mapped to
target.labels.value
UDM field and
target.labels.key
is set to
destination_smime_decryption_success
, when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to
about.labels.value
UDM field and
about.labels.key
is set to
destination_smime_decryption_success
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_decryption_success]
additional.fields[destination_smime_decryption_success]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_extraction_success]
target.labels[destination_smime_extraction_success]
(deprecated)
This log field is mapped to
target.labels.value
UDM field and
target.labels.key
is set to
destination_smime_extraction_success
, when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to
about.labels.value
UDM field and
about.labels.key
is set to
destination_smime_extraction_success
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_extraction_success]
additional.fields[destination_smime_extraction_success]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_parsing_success]
target.labels[destination_smime_parsing_success]
(deprecated)
This log field is mapped to
target.labels.value
UDM field and
target.labels.key
is set to
destination_smime_parsing_success
, when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to
about.labels.value
UDM field and
about.labels.key
is set to
destination_smime_parsing_success
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_parsing_success]
additional.fields[destination_smime_parsing_success]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_signature_verification_success]
target.labels[destination_smime_signature_verification_success]
(deprecated)
This log field is mapped to
target.labels.value
UDM field and
target.labels.key
is set to
destination_smime_signature_verification_success
, when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to
about.labels.value
UDM field and
about.labels.key
is set to
destination_smime_signature_verification_success
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.boolValue[smime_signature_verification_success]
additional.fields[destination_smime_signature_verification_success]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.value[address]
target.user.email_addresses
This log field is mapped to
target.user.email_addresses
UDM field when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to the
about.user.email_addresses
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination].parameter.intValue[user_id]
target.user.userid
This log field is mapped to
target.user.userid
UDM field when index value in
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[destination]
is equal to
0
.
For every other index value, this log field is mapped to the
about.user.userid
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[smtp_out_remote_host]
intermediary.hostname
gmail
events.parameters[delivery].msgValue[server_info].parameter.value[host_name]
intermediary.hostname
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[failed_smtp_out_connect_ip]
intermediary.ip
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[smtp_in_connect_ip]
intermediary.ip
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[smtp_out_connect_ip]
intermediary.ip
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[smtp_user_agent_ip]
intermediary.ip
gmail
events.parameters[delivery].msgValue[server_info].parameter.value[job_name]
intermediary.labels[job_name]
(deprecated)
gmail
events.parameters[delivery].msgValue[server_info].parameter.value[job_name]
additional.fields[job_name]
gmail
events.parameters[delivery].msgValue[server_info].parameter.intValue[server_type]
intermediary.labels[server_type]
(deprecated)
gmail
events.parameters[delivery].msgValue[server_info].parameter.intValue[server_type]
additional.fields[server_type]
gmail
events.parameters[delivery].msgValue[server_info].parameter.value[service_pool]
intermediary.labels[service_pool]
(deprecated)
gmail
events.parameters[delivery].msgValue[server_info].parameter.value[service_pool]
additional.fields[service_pool]
gmail
events.parameters[delivery].msgValue[server_info].parameter.intValue[task_number]
intermediary.labels[task_number]
(deprecated)
gmail
events.parameters[delivery].msgValue[server_info].parameter.intValue[task_number]
additional.fields[task_number]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.value[policy_holder_address]
security_result.about.user.email_addresses
If this log field value doesn't match the regular expression
^.+@.+$
, then it is mapped to the
security_result.about.administrative_domain
UDM field.
Else, it is mapped to the
security_result.about.administrative_domain
UDM field.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[consequence].parameter.value[policy_holder_email]
security_result.about.user.email_addresses
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[consequence].parameter.intValue[policy_holder_user_id]
security_result.about.user.userid
gmail
security_result.action
If the
events.parameters[delivery].msgValue[event_info].parameter.boolValue[success]
log field value is equal to
true
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, the
security_result.action
UDM field is set to
BLOCK
.
gmail
events.parameters[delivery].msgValue[event_info].parameter.boolValue[success]
security_result.action_details
gmail
security_result.category
If the
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[attachment].parameter.intValue[malware_family]
log field value is
not
empty, then the
security_result.category
UDM field is set to
SOFTWARE_MALICIOUS
.
If the
events.parameters[delivery].msgValue[message_info].parameter.boolValue[is_spam]
log field value is equal to
true
, then the
security_result.category
UDM field is set to
MAIL_SPAM
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[attachment].parameter.intValue[malware_family]
security_result.category_details
If this log field value is equal to
1
, then the
security_result.category_details
UDM field is set to
1 - A known malicious program type of malware
.
Else, if this log field value is equal to
2
, then the
security_result.category_details
UDM field is set to
2 - A virus or worm type of malware
.
Else, if this log field value is equal to
3
, then the
security_result.category_details
UDM field is set to
3 - Possible harmful email content
.
Else, if this log field value is equal to
4
, then the
security_result.category_details
UDM field is set to
4 - Possible unwanted email content
.
Else, if this log field value is equal to
5
, then the
security_result.category_details
UDM field is set to
5 - Other type of malware
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.value[flattened_triggered_rule_info]
security_result.detection_fields[flattened_triggered_rule_info]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[is_internal]
security_result.detection_fields[is_internal]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[is_intra_domain]
security_result.detection_fields[is_intra_domain]
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[is_policy_check_for_sender]
security_result.detection_fields[is_policy_check_for_sender]
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[is_spam]
security_result.detection_fields[is_spam]
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[smtp_replay_error]
security_result.detection_fields[smtp_replay_error]
If this log field value is equal to
1
, then the
security_result.detection_fields.key
UDM field is set to
smtp_replay_error
and the
security_result.detection_fields.value
UDM field is set to
1 - Authentication error
.
Else, if this log field value is equal to
2
, then the
security_result.detection_fields.key
UDM field is set to
smtp_replay_error
and the
2 - Daily rate limit was exceeded.
log field is mapped to the
security_result.detection_fields.value
UDM field.
Else, if this log field value is equal to
3
, then the
security_result.detection_fields.key
UDM field is set to
smtp_replay_error
and the
3 - Peak rate limit was exceeded.
log field is mapped to the
security_result.detection_fields.value
UDM field.
Else, if this log field value is equal to
4
, then the
security_result.detection_fields.key
UDM field is set to
smtp_replay_error
and the
4 - SMTP relay was abused.
log field is mapped to the
security_result.detection_fields.value
UDM field.
Else, if this log field value is equal to
5
, then the
security_result.detection_fields.key
UDM field is set to
smtp_replay_error
and the
5 - Per-user rate limit was exceeded.
log field is mapped to the
security_result.detection_fields.value
UDM field.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.intValue[classification_reason]
security_result.detection_fields[spam_info_classification_reason]
If this log field value is equal to
1
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
1 - Default spam classification reason
.
Else, if this log field value is equal to
2
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
2 - Message classified because of sender's past actions
.
Else, if this log field value is equal to
3
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
3 - Suspicious content
.
Else, if this log field value is equal to
4
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
4 - Suspicious link
.
Else, if this log field value is equal to
5
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
5 - Suspicious attachment
.
Else, if this log field value is equal to
6
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
6 - Custom policy defined in Google Workspace Admin Console > Gmail settings
.
Else, if this log field value is equal to
7
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
7 - DMARC
.
Else, if this log field value is equal to
8
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
8 - Domain in public RBLs
.
Else, if this log field value is equal to
9
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
9 - RFC standards violation
.
Else, if this log field value is equal to
10
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
10 - Gmail policy violation
.
Else, if this log field value is equal to
11
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
11 - Machine learning verdict
.
Else, if this log field value is equal to
12
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
12 - Sender reputation
.
Else, if this log field value is equal to
13
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
13 - Blatant spam
.
Else, if this log field value is equal to
14
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_classification_reason
and the
security_result.detection_fields.value
UDM field is set to
14 - Advanced phishing and malware protection
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.intValue[classification_timestamp_usec]
security_result.detection_fields[spam_info_classification_timestamp_usec]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.boolValue[delayed_for_deepscan]
security_result.detection_fields[spam_info_delayed_for_deepscan]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.intValue[disposition]
security_result.detection_fields[spam_info_disposition]
If this log field value is equal to
1
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_disposition
and the
security_result.detection_fields.value
UDM field is set to
1 - Message considered clean (not spam or malware)
.
Else, if this log field value is equal to
2
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_disposition
and the
security_result.detection_fields.value
UDM field is set to
2 - Spam
.
Else, if this log field value is equal to
3
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_disposition
and the
security_result.detection_fields.value
UDM field is set to
3 - Phishing
.
Else, if this log field value is equal to
4
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_disposition
and the
security_result.detection_fields.value
UDM field is set to
4 - Suspicious
.
Else, if this log field value is equal to
5
, then the
security_result.detection_fields.key
UDM field is set to
spam_info_disposition
and the
security_result.detection_fields.value
UDM field is set to
5 - Malware
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.value[ip_whitelist_entry]
security_result.detection_fields[spam_info_ip_whitelist_entry]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.multiMsgValue[safety_settings_info].parameter.intValue[safety_settings_action]
security_result.detection_fields[spam_info_safety_setting_action]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[spam_info].parameter.multiMsgValue[safety_settings_info].parameter.intValue[safety_settings_condition]
security_result.detection_fields[spam_info_safety_settings_condition]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[string_match].parameter.value[attachment_name]
security_result.detection_fields[triggered_rule_info_string_match_attachment_name]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[string_match].parameter.value[matched_string]
security_result.detection_fields[triggered_rule_info_string_match_matched_string]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[string_match].parameter.intValue[source]
security_result.detection_fields[triggered_rule_info_string_match_source]
If this log field value is equal to
0
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
0 - Unknown
.
Else, if this log field value is equal to
1
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
1 - Message body
or
including text format attachments
.
Else, if this log field value is equal to
2
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
2 - Binary format attachments
.
Else, if this log field value is equal to
3
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
3 - Message headers
.
Else, if this log field value is equal to
4
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
4 - Subject
.
Else, if this log field value is equal to
5
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
5 - Sender header
.
Else, if this log field value is equal to
6
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
6 - Recipient header
.
Else, if this log field value is equal to
7
, then the
security_result.detection_fields.key
UDM field is set to
triggered_rule_info_string_match_source
and the
security_result.detection_fields.value
UDM field is set to
7 - Raw message
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[upload_error_category]
security_result.detection_fields[upload_error_category]
If this log field value is equal to
0
, then the
security_result.detection_fields.key
UDM field is set to
upload_error_category
and the
security_result.detection_fields.value
UDM field is set to
0 - Uncategorized transient error
.
Else, if this log field value is equal to
1
, then the
security_result.detection_fields.key
UDM field is set to
upload_error_category
and the
security_result.detection_fields.value
UDM field is set to
1 - Recipient account is too busy
.
Else, if this log field value is equal to
2
, then the
security_result.detection_fields.key
UDM field is set to
upload_error_category
and the
security_result.detection_fields.value
UDM field is set to
2 - DNS error resolving recipient domain
.
Else, if this log field value is equal to
3
, then the
security_result.detection_fields.key
UDM field is set to
upload_error_category
and the
security_result.detection_fields.value
UDM field is set to
3 - Recipient's server refused connection
.
Else, if this log field value is equal to
4
, then the
security_result.detection_fields.key
UDM field is set to
upload_error_category
and the
security_result.detection_fields.value
UDM field is set to
4 - Recipient is out of storage
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.intValue[rule_id]
security_result.rule_id
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[consequence].parameter.intValue[action]
security_result.rule_labels[triggered_rule_info_consequence_action]
If this log field value is equal to
0
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
0 - Consequence is a no-op
.
Else, if this log field value is equal to
3
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
3 - Put message in Admin Quarantine
.
Else, if this log field value is equal to
4
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
4 - Modify the primary delivery target
.
Else, if this log field value is equal to
5
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
5 - Add a delivery target
.
Else, if this log field value is equal to
6
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
6 - Added a message header
.
Else, if this log field value is equal to
7
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
7 - Overwrite the envelope recipient
.
Else, if this log field value is equal to
9
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
9 - Add message to specified message set
.
Else, if this log field value is equal to
10
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
10 - Modify the message labels
.
Else, if this log field value is equal to
11
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
11 - Prefix text to message subject
.
Else, if this log field value is equal to
12
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
12 - Add a footer to the message
.
Else, if this log field value is equal to
13
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
13 - Strip the message body
.
Else, if this log field value is equal to
14
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
14 - Store a copy of the message in the user's mailbox
or
according to comprehensive mail storage setting.
log field is mapped to the
security_result.rule_labels.value
UDM field.
Else, if this log field value is equal to
15
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
15 - Replace attachment with canned text
.
Else, if this log field value is equal to
16
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
16 - Require secure message delivery
.
Else, if this log field value is equal to
17
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
17 - Message can't be delivered and bounced
.
Else, if this log field value is equal to
18
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
18 - Archive to Google Vault for recipients
.
Else, if this log field value is equal to
20
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
security_result.rule_labels.value
UDM field is set to
20 - Encrypt outbound message using S/MIME
.
Else, if this log field value is equal to
21
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_action
and the
21 - Change the recipient user when message is received at SMTP.
log field is mapped to the
security_result.rule_labels.value
UDM field.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[consequence].parameter.value[reason]
security_result.rule_labels[triggered_rule_info_consequence_reason]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[consequence].parameter.multiMsgValue[subconsequence].parameter.value[action]
security_result.rule_labels[triggered_rule_info_consequence_subconsequence_action]
If this log field value is equal to
0
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
0 - Consequence is a no-op
.
Else, if this log field value is equal to
3
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
3 - Put message in Admin Quarantine
.
Else, if this log field value is equal to
4
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
4 - Modify the primary delivery target
.
Else, if this log field value is equal to
5
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
5 - Add a delivery target
.
Else, if this log field value is equal to
6
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
6 - Added a message header
.
Else, if this log field value is equal to
7
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
7 - Overwrite the envelope recipient
.
Else, if this log field value is equal to
9
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
9 - Add message to specified message set
.
Else, if this log field value is equal to
10
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
10 - Modify the message labels
.
Else, if this log field value is equal to
11
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
11 - Prefix text to message subject
.
Else, if this log field value is equal to
12
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
12 - Add a footer to the message
.
Else, if this log field value is equal to
13
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
13 - Strip the message body
.
Else, if this log field value is equal to
14
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
14 - Store a copy of the message in the user's mailbox
or
according to comprehensive mail storage setting.
log field is mapped to the
security_result.rule_labels.value
UDM field.
Else, if this log field value is equal to
15
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
15 - Replace attachment with canned text
.
Else, if this log field value is equal to
16
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
16 - Require secure message delivery
.
Else, if this log field value is equal to
17
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
17 - Message can't be delivered and bounced
.
Else, if this log field value is equal to
18
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
18 - Archive to Google Vault for recipients
.
Else, if this log field value is equal to
20
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
security_result.rule_labels.value
UDM field is set to
20 - Encrypt outbound message using S/MIME
.
Else, if this log field value is equal to
21
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_consequence_subconsequence_action
and the
21 - Change the recipient user when message is received at SMTP.
log field is mapped to the
security_result.rule_labels.value
UDM field.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[consequence].parameter.multiMsgValue[subconsequence].parameter.value[reason]
security_result.rule_labels[triggered_rule_info_consequence_subconsequence_reason]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.intValue[policy_id]
security_result.rule_labels[triggered_rule_info_policy_id]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.value[spam_label_modifier]
security_result.rule_labels[triggered_rule_info_spam_label_modifier]
If this log field value is equal to
0
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_spam_label_modifier
and the
0 - No action—the rule honored the Gmail spam classification verdict.
log field is mapped to the
security_result.rule_labels.value
UDM field.
Else, if this log field value is equal to
1
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_spam_label_modifier
and the
1 - Spam—the rule classified the message as spam.
log field is mapped to the
security_result.rule_labels.value
UDM field.
Else, if this log field value is equal to
2
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_spam_label_modifier
and the
2 - Not spam—the rule classified the message as not spam.
log field is mapped to the
security_result.rule_labels.value
UDM field.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[string_match].parameter.value[match_expression]
security_result.rule_labels[triggered_rule_info_string_match_match_expression]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[string_match].parameter.value[predefined_detector_name]
security_result.rule_labels[triggered_rule_info_string_match_predefined_detector_name]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.multiMsgValue[string_match].parameter.intValue[type]
security_result.rule_labels[triggered_rule_info_string_match_type]
If this log field value is equal to
0
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_string_match_type
and the
security_result.rule_labels.value
UDM field is set to
0 - Undefined
.
Else, if this log field value is equal to
1
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_string_match_type
and the
security_result.rule_labels.value
UDM field is set to
1 - Regular expression match
.
Else, if this log field value is equal to
2
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_string_match_type
and the
security_result.rule_labels.value
UDM field is set to
2 - Predefined detector match
.
Else, if this log field value is equal to
3
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_string_match_type
and the
security_result.rule_labels.value
UDM field is set to
3 - Simple content match
.
Else, if this log field value is equal to
4
, then the
security_result.rule_labels.key
UDM field is set to
triggered_rule_info_string_match_type
and the
security_result.rule_labels.value
UDM field is set to
4 - Non-ASCII match
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.value[rule_name]
security_result.rule_name
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[triggered_rule_info].parameter.intValue[rule_type]
security_result.rule_type
If this log field value is equal to
0
, then the
security_result.rule_type
UDM field is set to
0 - Walled garden
.
Else, if this log field value is equal to
7
, then the
security_result.rule_type
UDM field is set to
7 - Objectionable content
.
Else, if this log field value is equal to
8
, then the
security_result.rule_type
UDM field is set to
8 - Content compliance
.
Else, if this log field value is equal to
10
, then the
security_result.rule_type
UDM field is set to
10 - Received mail routing
.
Else, if this log field value is equal to
11
, then the
security_result.rule_type
UDM field is set to
11 - Sent mail routing
.
Else, if this log field value is equal to
12
, then the
security_result.rule_type
UDM field is set to
12 - Spam override
.
Else, if this log field value is equal to
14
, then the
security_result.rule_type
UDM field is set to
14 - Blocked senders
.
Else, if this log field value is equal to
15
, then the
security_result.rule_type
UDM field is set to
15 - Append footer
.
Else, if this log field value is equal to
16
, then the
security_result.rule_type
UDM field is set to
16 - Attachment compliance
.
Else, if this log field value is equal to
17
, then the
security_result.rule_type
UDM field is set to
17 - TLS compliance
.
Else, if this log field value is equal to
18
, then the
security_result.rule_type
UDM field is set to
18 - Domain default routing
.
Else, if this log field value is equal to
19
, then the
security_result.rule_type
UDM field is set to
19 - Inbound email journal acceptance in Vault
.
Else, if this log field value is equal to
20
, then the
security_result.rule_type
UDM field is set to
20 - Outbound relay
.
Else, if this log field value is equal to
21
, then the
security_result.rule_type
UDM field is set to
21 - Quarantine summary
.
Else, if this log field value is equal to
22
, then the
security_result.rule_type
UDM field is set to
22 - Alternate secure route
.
Else, if this log field value is equal to
23
, then the
security_result.rule_type
UDM field is set to
23 - Alias table
.
Else, if this log field value is equal to
24
, then the
security_result.rule_type
UDM field is set to
24 - Comprehensive mail storage
.
Else, if this log field value is equal to
25
, then the
security_result.rule_type
UDM field is set to
25 - Routing rule
.
Else, if this log field value is equal to
26
, then the
security_result.rule_type
UDM field is set to
26 - Inbound gateway
.
Else, if this log field value is equal to
27
, then the
security_result.rule_type
UDM field is set to
27 - S/MIME
.
Else, if this log field value is equal to
28
, then the
security_result.rule_type
UDM field is set to
28 - Third-party email archiving
.
Else, if this log field value is equal to
31
, then the
security_result.rule_type
UDM field is set to
31 - S/MIME restrict delivery
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.multiMsgValue[authenticated_domain].parameter.value[name]
about.domain.name
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[attachment].parameter.value[file_extension_type]
about.file.file_type
FILE_TYPE_
string added before this log field value and converted it to uppercase, then If this log field value present in
File.FileType
then, this log field is mapped to
about.file.file_type
UDM field.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[attachment].parameter.value[file_extension_type]
about.file.mime_type
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.multiMsgValue[detected_file_types].parameter.value[mime_type]
about.file.mime_type
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[attachment].parameter.value[sha256]
about.file.sha256
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[ip_geo_city]
about.ip_geo_artifact.location.city
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[ip_geo_country]
about.ip_geo_artifact.location.country_or_region
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[action_type]
about.labels[action_type]
(deprecated)
If this log field value is equal to
1
, then the
about.labels
UDM field is set to
1 - Message received by inbound SMTP server.
Else, if this log field value is equal to
2
, then the
about.labels
UDM field is set to
2 - Message accepted by Gmail and prepared for delivery.
Else, if this log field value is equal to
3
, then the
about.labels
UDM field is set to
3 - Message was handled by Gmail.
Else, if this log field value is equal to
10
, then the
about.labels
UDM field is set to
10 - Message sent out by outbound SMTP server.
Else, if this log field value is equal to
14
, then the
about.labels
UDM field is set to
14 - A temporary error occurred when Gmail tried to deliver the message
or
and the message has been scheduled for retry.
Else, if this log field value is equal to
18
, then the
about.labels
UDM field is set to
18 - Message could not be delivered and bounced.
Else, if this log field value is equal to
19
, then the
about.labels
UDM field is set to
19 - Message was dropped by Gmail.
Else, if this log field value is equal to
45
, then the
about.labels
UDM field is set to
45 - Message was accepted for delivery by the Google Groups subsystem.
Else, if this log field value is equal to
46
, then the
about.labels
UDM field is set to
46 - Message's recipient address was a Google Group
or
and the recipient was expanded to each member of the Google Group that has message delivery enabled.
Else, if this log field value is equal to
48
, then the
about.labels
UDM field is set to
48 - Message received by inbound SMTP server for relay.
Else, if this log field value is equal to
49
, then the
about.labels
UDM field is set to
49 - Message sent through relay by outbound SMTP server.
Else, if this log field value is equal to
51
, then the
about.labels
UDM field is set to
51 - Message was written to Google Groups storage.
Else, if this log field value is equal to
54
, then the
about.labels
UDM field is set to
54 - Message was rejected by the Google Groups storage system.
Else, if this log field value is equal to
55
, then the
about.labels
UDM field is set to
55 - Message was re-inserted into Gmail by policies that modify the primary delivery route or envelope recipient.
Else, if this log field value is equal to
68
, then the
about.labels
UDM field is set to
68 - Message accepted by Gmail and prepared for delivery.
Else, if this log field value is equal to
69
, then the
about.labels
UDM field is set to
69 - A user changed the message's spam classification in Gmail.
Else, if this log field value is equal to
70
, then the
about.labels
UDM field is set to
70 - The message was reclassified as spam or phishing after it was delivered to Gmail.
Else, if this log field value is equal to
71
, then the
about.labels
UDM field is set to
71 - A user took an action in the inbox after receiving the message. Post-delivery actions include opening a message
or
clicking a link in a message
or
and downloading an attachment. BigQuery export doesn't provide details about the action.
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[action_type]
additional.fields[action_type]
If this log field value is equal to
1
, then the
additional.fields
UDM field is set to
1 - Message received by inbound SMTP server.
Else, if this log field value is equal to
2
, then the
additional.fields
UDM field is set to
2 - Message accepted by Gmail and prepared for delivery.
Else, if this log field value is equal to
3
, then the
additional.fields
UDM field is set to
3 - Message was handled by Gmail.
Else, if this log field value is equal to
10
, then the
additional.fields
UDM field is set to
10 - Message sent out by outbound SMTP server.
Else, if this log field value is equal to
14
, then the
additional.fields
UDM field is set to
14 - A temporary error occurred when Gmail tried to deliver the message
or
and the message has been scheduled for retry.
Else, if this log field value is equal to
18
, then the
additional.fields
UDM field is set to
18 - Message could not be delivered and bounced.
Else, if this log field value is equal to
19
, then the
additional.fields
UDM field is set to
19 - Message was dropped by Gmail.
Else, if this log field value is equal to
45
, then the
additional.fields
UDM field is set to
45 - Message was accepted for delivery by the Google Groups subsystem.
Else, if this log field value is equal to
46
, then the
additional.fields
UDM field is set to
46 - Message's recipient address was a Google Group
or
and the recipient was expanded to each member of the Google Group that has message delivery enabled.
Else, if this log field value is equal to
48
, then the
additional.fields
UDM field is set to
48 - Message received by inbound SMTP server for relay.
Else, if this log field value is equal to
49
, then the
additional.fields
UDM field is set to
49 - Message sent through relay by outbound SMTP server.
Else, if this log field value is equal to
51
, then the
additional.fields
UDM field is set to
51 - Message was written to Google Groups storage.
Else, if this log field value is equal to
54
, then the
additional.fields
UDM field is set to
54 - Message was rejected by the Google Groups storage system.
Else, if this log field value is equal to
55
, then the
additional.fields
UDM field is set to
55 - Message was re-inserted into Gmail by policies that modify the primary delivery route or envelope recipient.
Else, if this log field value is equal to
68
, then the
additional.fields
UDM field is set to
68 - Message accepted by Gmail and prepared for delivery.
Else, if this log field value is equal to
69
, then the
additional.fields
UDM field is set to
69 - A user changed the message's spam classification in Gmail.
Else, if this log field value is equal to
70
, then the
additional.fields
UDM field is set to
70 - The message was reclassified as spam or phishing after it was delivered to Gmail.
Else, if this log field value is equal to
71
, then the
additional.fields
UDM field is set to
71 - A user took an action in the inbox after receiving the message. Post-delivery actions include opening a message
or
clicking a link in a message
or
and downloading an attachment. BigQuery export doesn't provide details about the action.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.multiMsgValue[authenticated_domain].parameter.intValue[type]
about.labels[authenticated_domain_type]
(deprecated)
If this log field value is equal to
1
, then the
about.labels
UDM field is set to
1 - SPF
.
Else, if this log field value is equal to
2
, then the
about.labels
UDM field is set to
2 - DKIM
.
Else, if this log field value is equal to
3
, then the
about.labels
UDM field is set to
3 - DKIM_PROXY
.
Else, if this log field value is equal to
4
, then the
about.labels
UDM field is set to
4 - XOAR_SPF
.
Else, if this log field value is equal to
5
, then the
about.labels
UDM field is set to
5 - XOAR_DKIM
.
Else, if this log field value is equal to
6
, then the
about.labels
UDM field is set to
6 - ARC_SPF
.
Else, if this log field value is equal to
7
, then the
about.labels
UDM field is set to
7 - ARC_DKIM
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.multiMsgValue[authenticated_domain].parameter.intValue[type]
additional.fields[authenticated_domain_type]
If this log field value is equal to
1
, then the
additional.fields
UDM field is set to
1 - SPF
.
Else, if this log field value is equal to
2
, then the
additional.fields
UDM field is set to
2 - DKIM
.
Else, if this log field value is equal to
3
, then the
additional.fields
UDM field is set to
3 - DKIM_PROXY
.
Else, if this log field value is equal to
4
, then the
additional.fields
UDM field is set to
4 - XOAR_SPF
.
Else, if this log field value is equal to
5
, then the
additional.fields
UDM field is set to
5 - XOAR_DKIM
.
Else, if this log field value is equal to
6
, then the
additional.fields
UDM field is set to
6 - ARC_SPF
.
Else, if this log field value is equal to
7
, then the
additional.fields
UDM field is set to
7 - ARC_DKIM
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[delivery_timestamp_usec]
about.labels[delivery_timestamp_usec]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[delivery_timestamp_usec]
additional.fields[delivery_timestamp_usec]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.multiMsgValue[detected_file_types].parameter.intValue[category]
about.labels[detected_file_types_category]
(deprecated)
If this log field value is equal to
1
, then the
about.labels
UDM field is set to
1 - Unrecognized file type
.
Else, if this log field value is equal to
2
, then the
about.labels
UDM field is set to
2 - Microsoft Office documents, including word processing, spreadsheet, presentation, and database documents. Includes PDF files. The file might or might not be encrypted
.
Else, if this log field value is equal to
3
, then the
about.labels
UDM field is set to
3 - Video and multimedia, for example, MPEG, Quicktime, WMV
.
Else, if this log field value is equal to
4
, then the
about.labels
UDM field is set to
4 - Music and audio, for example, MP3, AAC, WAV
.
Else, if this log field value is equal to
5
, then the
about.labels
UDM field is set to
5 - Images, for example, JPEG, BMP, GIF
.
Else, if this log field value is equal to
6
, then the
about.labels
UDM field is set to
6 - Archives, for example, ZIP, TAR, TGZ
.
Else, if this log field value is equal to
7
, then the
about.labels
UDM field is set to
7 - Executables, for example EXE, COM, JS
.
Else, if this log field value is equal to
8
, then the
about.labels
UDM field is set to
8 - Office documents that are encrypted
.
Else, if this log field value is equal to
9
, then the
about.labels
UDM field is set to
9 - Office documents that are not encrypted
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.multiMsgValue[detected_file_types].parameter.intValue[category]
additional.fields[detected_file_types_category]
If this log field value is equal to
1
, then the
additional.fields
UDM field is set to
1 - Unrecognized file type
.
Else, if this log field value is equal to
2
, then the
additional.fields
UDM field is set to
2 - Microsoft Office documents, including word processing, spreadsheet, presentation, and database documents. Includes PDF files. The file might or might not be encrypted
.
Else, if this log field value is equal to
3
, then the
additional.fields
UDM field is set to
3 - Video and multimedia, for example, MPEG, Quicktime, WMV
.
Else, if this log field value is equal to
4
, then the
additional.fields
UDM field is set to
4 - Music and audio, for example, MP3, AAC, WAV
.
Else, if this log field value is equal to
5
, then the
additional.fields
UDM field is set to
5 - Images, for example, JPEG, BMP, GIF
.
Else, if this log field value is equal to
6
, then the
additional.fields
UDM field is set to
6 - Archives, for example, ZIP, TAR, TGZ
.
Else, if this log field value is equal to
7
, then the
additional.fields
UDM field is set to
7 - Executables, for example EXE, COM, JS
.
Else, if this log field value is equal to
8
, then the
additional.fields
UDM field is set to
8 - Office documents that are encrypted
.
Else, if this log field value is equal to
9
, then the
additional.fields
UDM field is set to
9 - Office documents that are not encrypted
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[dkim_pass]
about.labels[dkim_pass]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[dkim_pass]
additional.fields[dkim_pass]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[dmarc_pass]
about.labels[dmarc_pass]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[dmarc_pass]
additional.fields[dmarc_pass]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[dmarc_published_domain]
about.labels[dmarc_published_domain]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.value[dmarc_published_domain]
additional.fields[dmarc_published_domain]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.multiStrValue[recipients]
about.labels[exchange_journal_info_recipients]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.multiStrValue[recipients]
additional.fields[exchange_journal_info_recipients]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.value[rfc822_message_id]
about.labels[exchange_journal_info_rfc822_message_id]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.value[rfc822_message_id]
additional.fields[exchange_journal_info_rfc822_message_id]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.intValue[timestamp]
about.labels[exchange_journal_info_timestamp]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.intValue[timestamp]
additional.fields[exchange_journal_info_timestamp]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.multiStrValue[unknown_recipients]
about.labels[exchange_journal_info_unknown_recipients]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[structured_policy_log_info].parameter.msgValue[exchange_journal_info].parameter.multiStrValue[unknown_recipients]
additional.fields[exchange_journal_info_unknown_recipients]
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[internal_message_id]
about.labels[internal_message_id]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[internal_message_id]
additional.fields[internal_message_id]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiStrValue[link_domain]
about.labels[link_domain]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiStrValue[link_domain]
additional.fields[link_domain]
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[message_set].parameter.intValue[type]
about.labels[message_set_type]
(deprecated)
If this log field value is equal to
1
, then the
about.labels
UDM field is set to
1 - Message is inbound (received from outside your domains). This message set doesn't appear with message set 10.
Else, if this log field value is equal to
2
, then the
about.labels
UDM field is set to
2 - Message is outbound (sent to a recipient outside your domains). This message set doesn't appear with message set 10.
Else, if this log field value is equal to
4
, then the
about.labels
UDM field is set to
4 - Message contains objectionable content, as defined by one of your policies.
Else, if this log field value is equal to
6
, then the
about.labels
UDM field is set to
6 - Message triggered the walled garden rule you configured that restricts messages to authorized addresses or domains.
Else, if this log field value is equal to
7
, then the
about.labels
UDM field is set to
7 - Gmail classified the message as spam.
Else, if this log field value is equal to
8
, then the
about.labels
UDM field is set to
8 - Message being sent (outgoing message)
.
Else, if this log field value is equal to
9
, then the
about.labels
UDM field is set to
9 - Message being received (incoming message)
.
Else, if this log field value is equal to
10
, then the
about.labels
UDM field is set to
10 - Message that is internal to your domains
.
Else, if this log field value is equal to
11
, then the
about.labels
UDM field is set to
11 - Message has a sender or recipients outside your domains.
Else, if this log field value is equal to
12
, then the
about.labels
UDM field is set to
12 - Message has some recipients inside your domain and some recipients outside your domain. This message set might appear when:
Else, if this log field value is equal to
13
, then the
about.labels
UDM field is set to
13 - The type of the message set is unknown.
Else, if this log field value is equal to
15
, then the
about.labels
UDM field is set to
15 - The policy being checked against is tied to a Gmail user.
Else, if this log field value is equal to
18
, then the
about.labels
UDM field is set to
18 - Message doesn't have a default route.
Else, if this log field value is equal to
19
, then the
about.labels
UDM field is set to
19 - The address list you configured for domain default routing matches the correspondent of the message.
Else, if this log field value is equal to
20
, then the
about.labels
UDM field is set to
20 - Message is from an address in your blocked senders list.
Else, if this log field value is equal to
21
, then the
about.labels
UDM field is set to
21 - Message was sent over TLS and the SSL certificate is valid.
Else, if this log field value is equal to
22
, then the
about.labels
UDM field is set to
22 - Message was sent over TLS.
Else, if this log field value is equal to
24
, then the
about.labels
UDM field is set to
24 - The recipient of this message is unknown.
Else, if this log field value is equal to
25
, then the
about.labels
UDM field is set to
25 - Message is a non-delivery report responding to a message that was not delivered.
Else, if this log field value is equal to
26
, then the
about.labels
UDM field is set to
26 - Message triggered a rerouting rule, which you configured in domain default routing.
Else, if this log field value is equal to
27
, then the
about.labels
UDM field is set to
27 - Sender successfully passed SPF/DKIM/DMARC authentication. If the sender isn't authenticated, the sender domain is untrusted and the message is not considered internal.
Else, if this log field value is equal to
28
, then the
about.labels
UDM field is set to
28 - Exchange journal is archiving the message to Google Vault.
Else, if this log field value is equal to
29
, then the
about.labels
UDM field is set to
29 - Message was routed through SMTP relay.
Else, if this log field value is equal to
30
, then the
about.labels
UDM field is set to
30 - A recipient of the message matched one of the enumerated recipients (instead of a regular expression pattern) you configured for domain routing, or domain default routing.
Else, if this log field value is equal to
31
, then the
about.labels
UDM field is set to
31 - Message matched a domain default routing condition you configured.
Else, if this log field value is equal to
32
, then the
about.labels
UDM field is set to
32 - Message was created from an Exchange journal message for archiving to Google Vault.
Else, if this log field value is equal to
33
, then the
about.labels
UDM field is set to
33 - Message has to be transmitted through a secure connection, such as TLS.
Else, if this log field value is equal to
34
, then the
about.labels
UDM field is set to
34 - The policy being checked against is tied to a group instead of an individual Gmail user.
Else, if this log field value is equal to
35
, then the
about.labels
UDM field is set to
35 - Message could not be authenticated in SMTP relay because it has an empty SMTP envelope-from address or is possibly an Exchange Journal message. It will be checked later at SMTP RCPT command time.
Else, if this log field value is equal to
36
, then the
about.labels
UDM field is set to
36 - Message has aggressive spam filtering enabled.
Else, if this log field value is equal to
37
, then the
about.labels
UDM field is set to
37 - Message is authenticated for SMTP relay.
Else, if this log field value is equal to
39
, then the
about.labels
UDM field is set to
39 - Sender is from an authenticated domain for relay.
Else, if this log field value is equal to
40
, then the
about.labels
UDM field is set to
40 - Message is from a Google Workspace user in the domain being authenticated for relay.
Else, if this log field value is equal to
41
, then the
about.labels
UDM field is set to
41 - Sender has successfully authenticated with SMTP AUTH, and Gmail is trying to authenticate SMTP relay for the sender's domain.
Else, if this log field value is equal to
42
, then the
about.labels
UDM field is set to
42 - Message was sent from an address that isn't authenticated.
Else, if this log field value is equal to
43
, then the
about.labels
UDM field is set to
43 - Message was rerouted through an alias table.
Else, if this log field value is equal to
44
, then the
about.labels
UDM field is set to
44 - Message triggered a rule that changes the route of the mail flow.
Else, if this log field value is equal to
45
, then the
about.labels
UDM field is set to
45 - Message is to a catch-all account and is being relayed to an on-premise server. System-of-record policies won't be applied to it.
Else, if this log field value is equal to
46
, then the
about.labels
UDM field is set to
46 - Message bypassed the spam filter.
Else, if this log field value is equal to
47
, then the
about.labels
UDM field is set to
47 - Message was detected to be spam by tag-and-deliver information in the inbound gateway settings.
Else, if this log field value is equal to
48
, then the
about.labels
UDM field is set to
48 - Message was not checked for spam (by SMTP) due to a spam-override policy.
Else, if this log field value is equal to
49
, then the
about.labels
UDM field is set to
49 - Always override spam rejection for the message.
Else, if this log field value is equal to
50
, then the
about.labels
UDM field is set to
50 - Message matches a domain routing condition you configured.
Else, if this log field value is equal to
51
, then the
about.labels
UDM field is set to
51 - Message triggered a rerouting rule that you configured for domain routing.
Else, if this log field value is equal to
55
, then the
about.labels
UDM field is set to
55 - Message was created by the Exchange Journal generation setting.
Else, if this log field value is equal to
57
, then the
about.labels
UDM field is set to
57 - Message was received from an inbound gateway rule that you configured.
Else, if this log field value is equal to
60
, then the
about.labels
UDM field is set to
60 - Message is protected with Gmail confidential mode.
Else, if this log field value is equal to
61
, then the
about.labels
UDM field is set to
61 - Message was caught by Security sandbox.
Else, if this log field value is equal to
62
, then the
about.labels
UDM field is set to
62 - The address list you configured for domain default routing matches the SMTP envelope recipient instead of the correspondent of the message.
Else, if this log field value is equal to
63
, then the
about.labels
UDM field is set to
63 - Message triggered a domain-level rerouting rule, which you configured for domain routing, or domain default routing
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.multiMsgValue[message_set].parameter.intValue[type]
additional.fields[message_set_type]
If this log field value is equal to
1
, then the
additional.fields
UDM field is set to
1 - Message is inbound (received from outside your domains). This message set doesn't appear with message set 10.
Else, if this log field value is equal to
2
, then the
additional.fields
UDM field is set to
2 - Message is outbound (sent to a recipient outside your domains). This message set doesn't appear with message set 10.
Else, if this log field value is equal to
4
, then the
additional.fields
UDM field is set to
4 - Message contains objectionable content, as defined by one of your policies.
Else, if this log field value is equal to
6
, then the
additional.fields
UDM field is set to
6 - Message triggered the walled garden rule you configured that restricts messages to authorized addresses or domains.
Else, if this log field value is equal to
7
, then the
additional.fields
UDM field is set to
7 - Gmail classified the message as spam.
Else, if this log field value is equal to
8
, then the
additional.fields
UDM field is set to
8 - Message being sent (outgoing message)
.
Else, if this log field value is equal to
9
, then the
additional.fields
UDM field is set to
9 - Message being received (incoming message)
.
Else, if this log field value is equal to
10
, then the
additional.fields
UDM field is set to
10 - Message that is internal to your domains
.
Else, if this log field value is equal to
11
, then the
additional.fields
UDM field is set to
11 - Message has a sender or recipients outside your domains.
Else, if this log field value is equal to
12
, then the
additional.fields
UDM field is set to
12 - Message has some recipients inside your domain and some recipients outside your domain. This message set might appear when:
Else, if this log field value is equal to
13
, then the
additional.fields
UDM field is set to
13 - The type of the message set is unknown.
Else, if this log field value is equal to
15
, then the
additional.fields
UDM field is set to
15 - The policy being checked against is tied to a Gmail user.
Else, if this log field value is equal to
18
, then the
additional.fields
UDM field is set to
18 - Message doesn't have a default route.
Else, if this log field value is equal to
19
, then the
additional.fields
UDM field is set to
19 - The address list you configured for domain default routing matches the correspondent of the message.
Else, if this log field value is equal to
20
, then the
additional.fields
UDM field is set to
20 - Message is from an address in your blocked senders list.
Else, if this log field value is equal to
21
, then the
additional.fields
UDM field is set to
21 - Message was sent over TLS and the SSL certificate is valid.
Else, if this log field value is equal to
22
, then the
additional.fields
UDM field is set to
22 - Message was sent over TLS.
Else, if this log field value is equal to
24
, then the
additional.fields
UDM field is set to
24 - The recipient of this message is unknown.
Else, if this log field value is equal to
25
, then the
additional.fields
UDM field is set to
25 - Message is a non-delivery report responding to a message that was not delivered.
Else, if this log field value is equal to
26
, then the
additional.fields
UDM field is set to
26 - Message triggered a rerouting rule, which you configured in domain default routing.
Else, if this log field value is equal to
27
, then the
additional.fields
UDM field is set to
27 - Sender successfully passed SPF/DKIM/DMARC authentication. If the sender isn't authenticated, the sender domain is untrusted and the message is not considered internal.
Else, if this log field value is equal to
28
, then the
additional.fields
UDM field is set to
28 - Exchange journal is archiving the message to Google Vault.
Else, if this log field value is equal to
29
, then the
additional.fields
UDM field is set to
29 - Message was routed through SMTP relay.
Else, if this log field value is equal to
30
, then the
additional.fields
UDM field is set to
30 - A recipient of the message matched one of the enumerated recipients (instead of a regular expression pattern) you configured for domain routing, or domain default routing.
Else, if this log field value is equal to
31
, then the
additional.fields
UDM field is set to
31 - Message matched a domain default routing condition you configured.
Else, if this log field value is equal to
32
, then the
additional.fields
UDM field is set to
32 - Message was created from an Exchange journal message for archiving to Google Vault.
Else, if this log field value is equal to
33
, then the
additional.fields
UDM field is set to
33 - Message has to be transmitted through a secure connection, such as TLS.
Else, if this log field value is equal to
34
, then the
additional.fields
UDM field is set to
34 - The policy being checked against is tied to a group instead of an individual Gmail user.
Else, if this log field value is equal to
35
, then the
additional.fields
UDM field is set to
35 - Message could not be authenticated in SMTP relay because it has an empty SMTP envelope-from address or is possibly an Exchange Journal message. It will be checked later at SMTP RCPT command time.
Else, if this log field value is equal to
36
, then the
additional.fields
UDM field is set to
36 - Message has aggressive spam filtering enabled.
Else, if this log field value is equal to
37
, then the
additional.fields
UDM field is set to
37 - Message is authenticated for SMTP relay.
Else, if this log field value is equal to
39
, then the
additional.fields
UDM field is set to
39 - Sender is from an authenticated domain for relay.
Else, if this log field value is equal to
40
, then the
additional.fields
UDM field is set to
40 - Message is from a Google Workspace user in the domain being authenticated for relay.
Else, if this log field value is equal to
41
, then the
additional.fields
UDM field is set to
41 - Sender has successfully authenticated with SMTP AUTH, and Gmail is trying to authenticate SMTP relay for the sender's domain.
Else, if this log field value is equal to
42
, then the
additional.fields
UDM field is set to
42 - Message was sent from an address that isn't authenticated.
Else, if this log field value is equal to
43
, then the
additional.fields
UDM field is set to
43 - Message was rerouted through an alias table.
Else, if this log field value is equal to
44
, then the
additional.fields
UDM field is set to
44 - Message triggered a rule that changes the route of the mail flow.
Else, if this log field value is equal to
45
, then the
additional.fields
UDM field is set to
45 - Message is to a catch-all account and is being relayed to an on-premise server. System-of-record policies won't be applied to it.
Else, if this log field value is equal to
46
, then the
additional.fields
UDM field is set to
46 - Message bypassed the spam filter.
Else, if this log field value is equal to
47
, then the
additional.fields
UDM field is set to
47 - Message was detected to be spam by tag-and-deliver information in the inbound gateway settings.
Else, if this log field value is equal to
48
, then the
additional.fields
UDM field is set to
48 - Message was not checked for spam (by SMTP) due to a spam-override policy.
Else, if this log field value is equal to
49
, then the
additional.fields
UDM field is set to
49 - Always override spam rejection for the message.
Else, if this log field value is equal to
50
, then the
additional.fields
UDM field is set to
50 - Message matches a domain routing condition you configured.
Else, if this log field value is equal to
51
, then the
additional.fields
UDM field is set to
51 - Message triggered a rerouting rule that you configured for domain routing.
Else, if this log field value is equal to
55
, then the
additional.fields
UDM field is set to
55 - Message was created by the Exchange Journal generation setting.
Else, if this log field value is equal to
57
, then the
additional.fields
UDM field is set to
57 - Message was received from an inbound gateway rule that you configured.
Else, if this log field value is equal to
60
, then the
additional.fields
UDM field is set to
60 - Message is protected with Gmail confidential mode.
Else, if this log field value is equal to
61
, then the
additional.fields
UDM field is set to
61 - Message was caught by Security sandbox.
Else, if this log field value is equal to
62
, then the
additional.fields
UDM field is set to
62 - The address list you configured for domain default routing matches the SMTP envelope recipient instead of the correspondent of the message.
Else, if this log field value is equal to
63
, then the
additional.fields
UDM field is set to
63 - Message triggered a domain-level rerouting rule, which you configured for domain routing, or domain default routing
.
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[moderation_reason]
about.labels[moderation_reason]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[moderation_reason]
additional.fields[moderation_reason]
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[moderation_status]
about.labels[moderation_status]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[moderation_status]
additional.fields[moderation_status]
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[num_message_attachments]
about.labels[num_message_attachments]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[num_message_attachments]
additional.fields[num_message_attachments]
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[sequence_number]
about.labels[sequence_number]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[sequence_number]
additional.fields[sequence_number]
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[smime_content_type]
about.labels[smime_content_type]
(deprecated)
If this log field value is equal to
0
, then the
about.labels
UDM field is set to
0 - Message does not have a recognized S/MIME Content-Type.
Else, if this log field value is equal to
1
, then the
about.labels
UDM field is set to
1 - An S/MIME message with a detached signature Indicated by content type multipart/signed with parameter protocol=application/pkcs7-signature.
Else, if this log field value is equal to
2
, then the
about.labels
UDM field is set to
2 - An S/MIME message with an opaque signature Indicated by content type application/pkcs7-mime or application/x-pkcs7-mime with parameter smime-type=signed-data.
Else, if this log field value is equal to
3
, then the
about.labels
UDM field is set to
3 - An S/MIME message that is encrypted Indicated by content type application/pkcs7-mime or application/x-pkcs7-mime with parameter smime-type=enveloped-data.
Else, if this log field value is equal to
4
, then the
about.labels
UDM field is set to
4 - An S/MIME message that is compressed Indicated by content type application/pkcs7-mime or application/x-pkcs7-mime with parameter smime-type=compressed-data.
gmail
events.parameters[delivery].msgValue[message_info].parameter.intValue[smime_content_type]
additional.fields[smime_content_type]
If this log field value is equal to
0
, then the
additional.fields
UDM field is set to
0 - Message does not have a recognized S/MIME Content-Type.
Else, if this log field value is equal to
1
, then the
additional.fields
UDM field is set to
1 - An S/MIME message with a detached signature Indicated by content type multipart/signed with parameter protocol=application/pkcs7-signature.
Else, if this log field value is equal to
2
, then the
additional.fields
UDM field is set to
2 - An S/MIME message with an opaque signature Indicated by content type application/pkcs7-mime or application/x-pkcs7-mime with parameter smime-type=signed-data.
Else, if this log field value is equal to
3
, then the
additional.fields
UDM field is set to
3 - An S/MIME message that is encrypted Indicated by content type application/pkcs7-mime or application/x-pkcs7-mime with parameter smime-type=enveloped-data.
Else, if this log field value is equal to
4
, then the
additional.fields
UDM field is set to
4 - An S/MIME message that is compressed Indicated by content type application/pkcs7-mime or application/x-pkcs7-mime with parameter smime-type=compressed-data.
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_encrypt_message]
about.labels[smime_encrypt_message]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_encrypt_message]
additional.fields[smime_encrypt_message]
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_extraction_success]
about.labels[smime_extraction_success]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_extraction_success]
additional.fields[smime_extraction_success]
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_packaging_success]
about.labels[smime_packaging_success]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_packaging_success]
additional.fields[smime_packaging_success]
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_sign_message]
about.labels[smime_sign_message]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.boolValue[smime_sign_message]
additional.fields[smime_sign_message]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[spf_pass]
about.labels[spf_pass]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[spf_pass]
additional.fields[spf_pass]
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[tls_required_but_unavailable]
about.labels[tls_required_but_unavailable]
(deprecated)
gmail
events.parameters[delivery].msgValue[message_info].parameter.msgValue[connection_info].parameter.boolValue[tls_required_but_unavailable]
additional.fields[tls_required_but_unavailable]
Field mapping reference: WORKSPACE_ALERTS log types to UDM event type
The following table lists the
WORKSPACE_ALERTS
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
Customer takeout initiated
STATUS_UPDATE
Malware reclassification
EMAIL_TRANSACTION
MAIL_PHISHING
Misconfigured whitelist
EMAIL_TRANSACTION
MAIL_PHISHING
Phishing reclassification
EMAIL_TRANSACTION
MAIL_PHISHING
Suspicious message reported
EMAIL_TRANSACTION
MAIL_PHISHING
User reported phishing
EMAIL_TRANSACTION
MAIL_PHISHING
User reported spam spike
EMAIL_TRANSACTION
MAIL_PHISHING
Leaked password
USER_LOGIN
ACL_VIOLATION
Suspicious login
USER_LOGIN
ACL_VIOLATION
Suspicious login (less secure app)
USER_LOGIN
ACL_VIOLATION
Suspicious programmatic login
USER_LOGIN
ACL_VIOLATION
User suspended
USER_UNCATEGORIZED
ACL_VIOLATION
User suspended (spam)
USER_UNCATEGORIZED
ACL_VIOLATION
User suspended (spam through relay)
USER_UNCATEGORIZED
ACL_VIOLATION
User suspended (suspicious activity)
USER_UNCATEGORIZED
ACL_VIOLATION
Google Operations
STATUS_UPDATE
Configuration problem
STATUS_UNCATEGORIZED
Government attack warning
STATUS_UNCATEGORIZED
Device compromised
GENERIC_EVENT
Suspicious activity
USER_UNCATEGORIZED
AppMaker Default Cloud SQL setup
USER_RESOURCE_ACCESS
Activity Rule
STATUS_UNCATEGORIZED / USER_UNCATEGORIZED / EMAIL_UNCATEGORIZED
POLICY_VIOLATION
Data Loss Prevention
USER_UNCATEGORIZED
POLICY_VIOLATION
Apps outage
STATUS_UPDATE
Primary admin changed
USER_UNCATEGORIZED
SSO profile added
USER_RESOURCE_CREATION
SSO profile updated
USER_RESOURCE_UPDATE_CONTENT
SSO profile deleted
USER_RESOURCE_DELETION
Super admin password reset
USER_CHANGE_PASSWORD
User deleted
USER_DELETION
New user added
USER_CREATION
User password changed
USER_CHANGE_PASSWORD
Users Admin privilege revoked
USER_CHANGE_PERMISSIONS
Suspended user made active
USER_UNCATEGORIZED
User granted Admin privilege
USER_CHANGE_PERMISSIONS
User suspended (Administrator email alert)
USER_UNCATEGORIZED
Drive settings changed
USER_RESOURCE_ACCESS
Calendar settings changed
USER_RESOURCE_ACCESS
Reporting Rule
STATUS_UPDATE
APNS certificate is expiring soon
STATUS_UPDATE / GENERIC_EVENT
APNS certificate has expired
STATUS_UPDATE / GENERIC_EVENT
Field mapping reference: WORKSPACE_ALERTS
The following table lists the log fields of the
WORKSPACE_ALERTS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
data.domainId.customerPrimaryDomain
about.administrative_domain
data.messages.attachmentsSha256Hash
about.file.sha256
data.messages.attachmentsSha256Hash
security_result.detection_fields[attachments_sha256_hash]
data.mergeInfo.newAlertId
about.labels[new_alert_id]
(deprecated)
data.mergeInfo.newAlertId
additional.fields[new_alert_id]
data.mergeInfo.newIncidentTrackingId
about.labels[new_incident_tracking_id]
(deprecated)
data.mergeInfo.newIncidentTrackingId
additional.fields[new_incident_tracking_id]
data.nextUpdateTime
about.labels[next_update_time]
(deprecated)
data.nextUpdateTime
additional.fields[next_update_time]
data.resolutionTime
about.labels[resolution_time]
(deprecated)
data.resolutionTime
additional.fields[resolution_time]
data.status
about.labels[status]
(deprecated)
data.status
additional.fields[status]
data.incidentTrackingId
about.labels[tracking_id]
(deprecated)
data.incidentTrackingId
additional.fields[tracking_id]
customerId
about.resource.product_object_id
If the
customerId
log field value is
not
empty, then the
customerId
log field is mapped to the
about.resource.product_object_id
UDM field.
Else, the
metadata.customerId
log field is mapped to the
about.resource.product_object_id
UDM field.
metadata.customerId
about.resource.product_object_id
If the
customerId
log field value is
not
empty, then the
customerId
log field is mapped to the
about.resource.product_object_id
UDM field.
Else, the
metadata.customerId
log field is mapped to the
about.resource.product_object_id
UDM field.
about.resource.resource_type
The
about.resource.resource_type
UDM field is set to
CLOUD_ORGANIZATION
.
data.dashboardUri
about.url
data.attachmentData.csv.dataRows.entries
additional.fields.entries
data.attachmentData.csv.headers
additional.fields.header
extensions.auth.mechanism
If the
data.@type
log field value is equal to
AccountWarning
, then the
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
extensions.auth.type
If the
data.@type
log field value is equal to
AccountWarning
, then the
extensions.auth.type
UDM field is set to
SSO
.
data.description
metadata.description
createTime
metadata.event_timestamp
data.@type
metadata.product_event_type
etag
metadata.product_log_id
If the
etag
log field value is
not
empty, then the
etag
log field is mapped to the
metadata.product_log_id
UDM field.
Else, the
alertId
log field is mapped to the
metadata.product_log_id
UDM field.
metadata.etag
metadata.product_log_id
If the
metadata.etag
log field value is
not
empty, then the
metadata.etag
log field is mapped to the
metadata.product_log_id
UDM field.
Else, the
alertId
log field is mapped to the
metadata.product_log_id
UDM field.
metadata.product_name
The
metadata.product_name
UDM field is set to
WORKSPACE_ALERTS
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
data.maliciousEntity.fromHeader
network.email.from
data.messages.messageId
network.email.mail_id
data.messages.messageId
security_result.detection_fields[message_id]
data.messages.subjectText
network.email.subject
data.messages.recipient
network.email.to
data.messages.recipient
security_result.detection_fields[mail_recipient]
data.ruleViolationInfo.recipients
network.email.to
If the
data.ruleViolationInfo.recipients
log field value matches the regular expression pattern
^.+@.+$
, then the
data.ruleViolationInfo.recipients
log field is mapped to the
network.email.to
UDM field.
data.ruleViolationInfo.recipients
additional.fields[recipients]
If the
data.ruleViolationInfo.recipients
log field value is equal to
anyone
, then the
data.ruleViolationInfo.recipients
log field is mapped to the
additional.fields
UDM field.
data.ruleViolationInfo.recipients
target.domain.name
If the
data.ruleViolationInfo.recipients
log field value matches the regular expression pattern
^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$
, then the first occurrence of the matching value in the
data.ruleViolationInfo.recipients
log field is mapped to the
target.domain.name
UDM field and the other occurrences are mapped to the
additional.fields[domain_recipients]
UDM field.
data.sourceIp
principal.ip
data.loginDetails.ipAddress
principal.ip
data.maliciousEntity.displayName
principal.labels[malicious_entity_display_name]
(deprecated)
data.maliciousEntity.displayName
additional.fields[malicious_entity_display_name]
data.requestInfo.appDeveloperEmail
principal.user.email_addresses
data.actorEmail
principal.user.email_addresses
data.ruleViolationInfo.triggeringUserEmail
principal.user.email_addresses
data.email
principal.user.email_addresses
data.domain
security_result.about.administrative_domain
metadata.assignee
security_result.about.labels[assignee]
(deprecated)
metadata.assignee
additional.fields[assignee]
data.header
security_result.about.labels[header]
(deprecated)
data.header
additional.fields[header]
data.ruleViolationInfo.suppressedActionTypes
security_result.about.labels[suppressed_action_types]
(deprecated)
data.ruleViolationInfo.suppressedActionTypes
additional.fields[suppressed_action_types]
data.title
security_result.about.labels[title]
(deprecated)
data.title
additional.fields[title]
alertId
security_result.about.object_reference
data.affectedUserEmails
security_result.about.user.email_addresses
data.ruleViolationInfo.triggeredActionTypes
security_result.action_details
security_result.action
If the
data.ruleViolationInfo.triggeredActionTypes
log field value is equal to
DRIVE_WARN_ON_EXTERNAL_SHARING
or
ALERT
or
RULE_ACTIVATE
or
RULE_DEACTIVATE
, then the
security_result.action
UDM field is set to
ALLOW
.
If the
data.ruleViolationInfo.triggeredActionTypes
log field value is equal to
CHROME_WARN_FILE_DOWNLOAD
or
CHROME_WARN_FILE_UPLOAD
or
CHROME_WARN_WEB_CONTENT_UPLOAD
or
CHROME_WARN_PAGE_PRINT
or
CHROME_WARN_URL_VISITED
or
CHAT_WARN_USER
, then the
security_result.action
UDM field is set to
ALLOW_WITH_MODIFICATION
.
If the
data.ruleViolationInfo.triggeredActionTypes
log field value is equal to
DRIVE_BLOCK_EXTERNAL_SHARING
or
DRIVE_RESTRICT_DOWNLOAD_PRINT_COPY
or
CHROME_BLOCK_FILE_DOWNLOAD
or
CHROME_BLOCK_FILE_UPLOAD
or
CHROME_BLOCK_WEB_CONTENT_UPLOAD
or
CHROME_BLOCK_PAGE_PRINT
or
CHROME_BLOCK_URL_VISITED
or
CHAT_BLOCK_CONTENT
or
GMAIL_BLOCK_MESSAGE
, then the
security_result.action
UDM field is set to
BLOCK
.
If the
data.ruleViolationInfo.triggeredActionTypes
log field value is equal to
ACTION_TYPE_UNSPECIFIED
or
DRIVE_APPLY_DRIVE_LABELS
or
CHROME_STORE_CONTENT
or
DELETE_WEBPROTECT_EVIDENCE
, then the
security_result.action
UDM field is set to
UNKNOWN_ACTION
.
security_result.category
If the
source
log field value is equal to
Gmail Phishing
, then the
security_result.category
UDM field is set to
MAIL_PHISHING
.
If the
source
log field value is equal to
Google Identity
, then the
security_result.category
UDM field is set to
ACL_VIOLATION
.
If the
source
log field value is equal to
Security Center rules
or
Data Loss Prevention
, then the
security_result.category
UDM field is set to
POLICY_VIOLATION
.
source
security_result.category_details
data.actionNames
security_result.detection_fields[action_names]
data.alertDetails
security_result.detection_fields[alert_details]
data.createTime
security_result.detection_fields[create_time]
data.messages.date
security_result.detection_fields[date]
If the
source
log field value is equal to
Gmail phishing
, then the
data.messages.date
log field is mapped to the
security_result.detection_fields
UDM field.
data.messages.sentTime
security_result.detection_fields[sent_time]
data.events.deviceCompromisedState
security_result.detection_fields[device_compromised_state]
data.displayName
security_result.detection_fields[display_name]
data.eventTime
security_result.detection_fields[event_time]
data.isInternal
security_result.detection_fields[is_internal]
data.loginDetails.loginTime
security_result.detection_fields[login_time]
data.messages.md5HashMessageBody
security_result.detection_fields[md5_hash_message_body]
If the
source
log field value is equal to
Gmail phishing
, then the
data.messages.md5HashMessageBody
log field is mapped to the
security_result.detection_fields
UDM field.
data.messages.md5hashsubject
security_result.detection_fields[md5_hash_subject]
If the
source
log field value is equal to
Gmail phishing
, then the
data.messages.md5hashsubject
log field is mapped to the
security_result.detection_fields
UDM field.
data.messages.messageBodySnippet
security_result.detection_fields[message_body_snippet]
metadata.status
security_result.detection_fields[metadata_status]
data.query
security_result.detection_fields[query]
securityInvestigationToolLink
security_result.detection_fields[security_investigation_tool_link]
startTime
security_result.detection_fields[start_time]
data.supersededAlerts
security_result.detection_fields[superseded_alerts]
data.supersedingAlert
security_result.detection_fields[superseding_alert]
data.systemActionType
security_result.detection_fields[system_action_type]
data.threshold
security_result.detection_fields[threshold]
data.triggerSource
security_result.detection_fields[trigger_source]
data.ruleViolationInfo.trigger
security_result.detection_fields[trigger]
data.updateTime
security_result.detection_fields[update_time]
data.windowSize
security_result.detection_fields[windows_size]
data.ruleViolationInfo.ruleInfo.resourceName
security_result.rule_id
data.ruleViolationInfo.matchInfo.userDefinedDetector.displayName
security_result.rule_labels[detector_display_name]
data.ruleViolationInfo.matchInfo.predefinedDetector.detectorName
security_result.rule_labels[detector_name]
data.ruleViolationInfo.matchInfo.userDefinedDetector.resourceName
security_result.rule_labels[detector_resource_name]
data.name
security_result.rule_name
data.ruleViolationInfo.ruleInfo.displayName
security_result.rule_name
metadata.severity
security_result.severity
type
security_result.summary
data.type
security_result.summary
If the
type
log field value is empty, then the
data.type
log field is mapped to the
security_result.summary
UDM field.
security_result.alert_state
The
security_result.alert_state
UDM field is set to
ALERTING
.
data.requestInfo.appKey
target.application
data.events.deviceId
target.asset.asset_id
data.events.deviceProperty
target.asset.attribute.labels[device_property]
data.events.iosVendorId
target.asset.attribute.labels[ios_vendor_id]
data.events.newValue
target.asset.attribute.labels[new_value]
data.events.oldValue
target.asset.attribute.labels[old_value]
data.events.resourceId
target.asset.attribute.labels[resource_id]
data.events.deviceModel
target.asset.hardware.model
data.events.serialNumber
target.asset.hardware.serial_number
data.events.deviceType
target.asset.type
data.primaryAdminChangedEvent.domain
target.domain.name
data.ssoProfileUpdatedEvent.inboundSsoProfileChanges
target.labels[inbound_sso_profile_changes]
(deprecated)
data.ssoProfileUpdatedEvent.inboundSsoProfileChanges
additional.fields[inbound_sso_profile_changes]
data.requestInfo.numberOfRequests
target.labels[number_of_requests]
(deprecated)
data.requestInfo.numberOfRequests
additional.fields[number_of_requests]
data.primaryAdminChangedEvent.previousAdminEmail
target.labels[previous_admin_email]
(deprecated)
data.primaryAdminChangedEvent.previousAdminEmail
additional.fields[previous_admin_email]
data.products
target.labels[product]
(deprecated)
data.products
additional.fields[product]
data.ruleViolationInfo.resourceInfo.resourceTitle
target.labels[resource_title]
(deprecated)
data.ruleViolationInfo.resourceInfo.resourceTitle
additional.fields[resource_title]
data.takeoutRequestId
target.labels[takeout_request_id]
(deprecated)
data.takeoutRequestId
additional.fields[takeout_request_id]
data.ruleViolationInfo.dataSource
target.resource.name
data.ssoProfileCreatedEvent.inboundSsoProfileName
target.resource.name
data.ssoProfileUpdatedEvent.inboundSsoProfileName
target.resource.name
data.ssoProfileDeletedEvent.inboundSsoProfileName
target.resource.name
data.ruleViolationInfo.resourceInfo.documentId
target.resource.product_object_id
target.resource.resource_type
If the
data.@type
log field value is equal to
DlpRuleViolation
, then the
target.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
If the
data.@type
log field value is equal to
AppMakerSqlSetupNotification
, then the
target.resource.resource_type
UDM field is set to
DATABASE
.
If the
data.type
log field value is equal to
SSO profile added
or
SSO profile updated
or
SSO profile deleted
, then the
target.resource.resource_type
UDM field is set to
SETTING
.
data.maliciousEntity.entity.emailAddress
target.user.email_addresses
data.email
target.user.email_addresses
If the
data.@type
log field value is equal to
StateSponsoredAttack
,
DeviceCompromised
, or
AccountWarning
, then the
data.email
log field is mapped to the
target.user.email_addresses
UDM field.
Else, the
data.email
log field is mapped to the
principal.user.email_addresses
UDM field.
data.primaryAdminChangedEvent.updatedAdminEmail
target.user.email_addresses
data.superAdminPasswordResetEvent.userEmail
target.user.email_addresses
data.maliciousEntity.entity.displayName
target.user.user_display_name
data.ruleViolationInfo.triggeredActionInfo
data.expirationTime
target.resource.attribute.labels[expiration_time]
If the
data.@type
log field value is equal to
ApnsCertificateExpirationInfo
, then the
data.expirationTime
log field is mapped to the
target.resource.attribute.labels[expiration_time]
UDM field.
data.appleId
about.user.userid
If the
data.@type
log field value is equal to
ApnsCertificateExpirationInfo
, then the
data.appleId
log field is mapped to the
about.user.userid
UDM field.
data.uid
target.resource.product_object_id
If the
data.@type
log field value is equal to
ApnsCertificateExpirationInfo
, then the
data.uid
log field is mapped to the
target.resource.product_object_id
UDM field.
Field mapping reference: WORKSPACE_GROUPS
The following table lists the log fields of the
WORKSPACE_GROUPS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
adminCreated
entity.group.attribute.labels[admin_created]
If the
adminCreated
log field value is equal to
true
, then the
admin_created.value
UDM field is set to
true
.
Else, the
admin_created.value
UDM field is set to
false
.
description
metadata.description
directMembersCount
entity.group.attribute.labels[direct_members_count]
email
entity.group.email_addresses
nonEditableAliases
entity.group.email_addresses
aliases
entity.group.email_addresses
etag
entity.labels[etag]
(deprecated)
etag
additional.fields[etag]
id
entity.group.product_object_id
kind
entity.labels[kind]
(deprecated)
kind
additional.fields[kind]
name
entity.group.group_display_name
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
metadata.product_name
The
metadata.product_name
UDM field is set to
WORKSPACE GROUPS
.
metadata.entity_type
The
metadata.entity_type
UDM field is set to
GROUP
.
Field mapping reference: WORKSPACE_USERS
The following table lists the log fields of the
WORKSPACE_USERS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
addresses.country
entity.user.personal_address.country_or_region
addresses.countryCode
entity.user.attribute.labels[addresses_country_code]
addresses.customType
entity.user.attribute.labels[addresses_custom_type]
addresses.extendedAddress
entity.user.attribute.labels[addresses_extended_address]
addresses.formatted
entity.user.office_address.name
The
addresses.formatted
log field is mapped to the
user.office_address.name
UDM field if the following conditions are met:
The
message
log field value matches the regular expression pattern
addresses.*?formatted
.
The
addresses.type
log field value is equal to
work
.
The
addresses.formatted
log field value is
not
empty.
addresses.locality
entity.user.attribute.labels[addresses_locality]
addresses.poBox
entity.user.attribute.labels[addresses_pobox]
addresses.postalCode
entity.user.attribute.labels[addresses_postal_code]
addresses.primary
entity.user.attribute.labels[addresses_primary]
addresses.region
entity.user.attribute.labels[addresses_region]
addresses.sourceIsStructured
entity.user.attribute.labels[addresses_source_is_structured]
addresses.streetAddress
entity.user.attribute.labels[addresses_street_address]
addresses.type
entity.user.attribute.labels[addresses_type]
agreedToTerms
entity.user.attribute.labels[agreed_to_terms]
aliases
entity.user.attribute.labels[aliases_email]
changePasswordAtNextLogin
entity.user.attribute.labels[change_password_at_next_login]
If the
changePasswordAtNextLogin
log field value is equal to
true
, then the
change_password_at_next_login.value
UDM field is set to
true
.
Else, the
change_password_at_next_login.value
UDM field is set to
false
.
creationTime
entity.user.attribute.creation_time
customerId
entity.user.attribute.labels[customer_id]
deletionTime
entity.user.attribute.labels[deletion_time]
emails.customType
entity.user.attribute.labels[email_acustom_type]
emails.primary
entity.user.attribute.labels[email_primary]
emails.type
entity.user.attribute.labels[email_type]
etag
entity.labels[etag]
(deprecated)
etag
additional.fields[etag]
externalIds.customType
entity.user.attribute.labels[external_id_custom_type]
externalIds.type
entity.user.attribute.labels[external_id_type]
externalIds.value
entity.user.employee_id
If the
externalIds.type
log field value is equal to
organization
, then the
externalIds.value
log field is mapped to the
user.employee_id
UDM field.
gender.addressMeAs
entity.user.attribute.labels[gender_address_me_as]
gender.customGender
entity.user.attribute.labels[custom_gender]
gender.type
entity.user.attribute.labels[gender]
hashFunction
entity.user.attribute.labels[hash_function]
id
entity.user.product_object_id
ims.customProtocol
entity.user.attribute.labels[ims_custom_protocol]
ims.customType
entity.user.attribute.labels[ims_custom_type]
ims.im
entity.user.attribute.labels[ims_im]
ims.primary
entity.user.attribute.labels[ims_primary]
ims.protocol
entity.user.attribute.labels[ims_protocol]
ims.type
entity.user.attribute.labels[ims_type]
includeInGlobalAddressList
entity.user.attribute.labels[included_in_global_address_list]
If the
includeInGlobalAddressList
log field value is equal to
true
, then the
included_in_global_address_list.value
UDM field is set to
true
, else, then the
included_in_global_address_list.value
UDM field is set to
false
.
ipWhitelisted
entity.user.attribute.labels[ip_whitelisted]
isAdmin
entity.user.attribute.labels[is_admin]
isDelegatedAdmin
entity.user.attribute.labels[is_delegated_admin]
user.attribute.roles.type
If the
isAdmin
log field value or the
isDelegatedAdmin
log field value is equal to
true
, then the
user.attribute.roles.type
UDM field is set to
ADMINISTRATOR
.
isEnforcedIn2Sv
entity.user.attribute.labels[is_enforced_in_2sv]
If the
isEnforcedIn2Sv
log field value is equal to
true
, then the
is_enforced_in_2sv.value
UDM field is set to
true
, else, then the
is_enforced_in_2sv.value
UDM field is set to
false
.
isEnrolledIn2Sv
entity.user.attribute.labels[is_enrolled_in_2sv]
If the
isEnrolledIn2Sv
log field value is equal to
true
, then the
is_enrolled_in_2sv.value
UDM field is set to
true
, else, then the
is_enrolled_in_2sv.value
UDM field is set to
false
.
isMailboxSetup
entity.user.attribute.labels[is_mailbox_setup]
If the
isMailboxSetup
log field value is equal to
true
, then the
is_mail_box_setup.value
UDM field is set to
true
, else, then the
is_mail_box_setup.value
UDM field is set to
false
.
keywords.customType
entity.user.attribute.labels[keywords_custom_type]
keywords.type
entity.user.attribute.labels[keywords_type]
keywords.value
entity.user.attribute.labels[keywords_value]
kind
entity.labels[kind]
(deprecated)
kind
additional.fields[kind]
languages.customLanguage
entity.user.attribute.labels[language_custom_language]
languages.languageCode
entity.user.attribute.labels[language_code]
languages.preference
entity.user.attribute.labels[preferred_language]
lastLoginTime
entity.user.last_login_time
locations.area
entity.user.office_address.country_or_region
locations.buildingId
entity.user.attribute.labels[locations_buildingId]
locations.customType
entity.user.attribute.labels[locations_customType]
locations.deskCode
entity.user.officel_address.desk_name
locations.floorName
entity.user.office_address.floor_name
locations.floorSection
entity.user.attribute.labels[locations_floorSection]
locations.type
entity.user.attribute.labels[locations_type]
name.familyName
entity.user.last_name
name.fullName
entity.user.user_display_name
name.givenName
entity.user.first_name
notes.contentType
entity.user.attribute.labels[notes_content_type]
notes.value
entity.user.attribute.labels[notes_value]
organizations.costCenter
entity.user.attribute.labels[organization_cost_center]
organizations.customType
entity.user.attribute.labels[organization_custom_type]
organizations.department
entity.user.department
The
organizations.department
log field is mapped to the
user.department
UDM field if the following conditions are met:
The
message
log field value matches the regular expression pattern
organizations.*?department
.
The
org.department
log field value is
not
empty.
organizations.description
entity.user.attribute.labels [organizations_description]
organizations.domain
entity.user.attribute.labels[organization_domain]
organizations.fullTimeEquivalent
entity.user.attribute.labels[organization_full_time_equivalent]
organizations.location
entity.user.attribute.labels[organization_location]
organizations.name
entity.user.attribute.labels[organization_name]
organizations.primary
entity.user.attribute.labels[organization_primary]
organizations.symbol
entity.user.attribute.labels[organization_symbol]
organizations.title
entity.user.title
organizations.type
entity.user.attribute.labels[organization_type]
orgUnitPath
entity.user.attribute.labels[org_unit_path]
password
entity.user.attribute.labels[password]
phones.customType
entity.user.attribute.labels[phone_custom_type]
phones.primary
entity.user.attribute.labels[phone_primary]
phones.type
entity.user.attribute.labels[phone_type]
phones.value
entity.user.phone_numbers
If the
phones.value
log field value matches the regular expression pattern
(^the
+.0-9
log field value*)
, then the
phones.value
log field is mapped to the
user.phone_numbers
UDM field.
recoveryPhone
entity.user.phone_numbers
posixAccounts.accountId
entity.user.attribute.labels[posix_account_id]
posixAccounts.gecos
entity.user.attribute.labels[posix_account_gecos]
posixAccounts.gid
entity.user.group_identifiers
posixAccounts.homeDirectory
entity.user.attribute.labels[posix_account_home_directory]
posixAccounts.operatingSystemType
entity.platform
If the
posixAccounts.operatingSystemType
log field value is equal to
linux
, then the
entity.platform
UDM field is set to
LINUX
.
If the
posixAccounts.operatingSystemType
log field value is equal to
windows
, then the
entity.platform
UDM field is set to
WINDOWS
.
Else, the
entity.platform
UDM field is set to
UNKNOWN_PLATFORM
.
posixAccounts.primary
entity.user.attribute.labels[posix_account_primary]
posixAccounts.shell
entity.user.attribute.labels[posix_account_shell]
posixAccounts.systemId
entity.asset.asset_id
posixAccounts.uid
entity.user.attribute.labels[posix_account_uid]
posixAccounts.username
entity.user.userid
If the
posixAccounts.username
log field value is
not
empty, then the
posixAccounts.username
log field is mapped to the
entity.user.userid
UDM field.
primaryEmail
entity.user.email_addresses
recoveryEmail
entity.user.email_addresses
nonEditableAliases
entity.user.email_addresses
emails.address
entity.user.email_addresses
If the
emails.address
log field value is
not
equal to
primaryEmail
, then the
emails.address
log field is mapped to the
entity.user.email_addresses
UDM field.
relations.customType
entity.user.attribute.labels[relations_custom_type]
relations.type
entity.user.attribute.labels[relation_type]
relations.value
entity.user.managers.email_addresses
If the
relation.type
log field value is equal to
manager
, then the
relations.value
log field is mapped to the
user.managers.email_addresses
UDM field.
Else, the
relations.value
log field is mapped to the
user.attribute.labels
UDM field.
relations.value
entity.user.attribute.labels[relations_type]
If the
relation.type
log field value is equal to
manager
, then the
relations.value
log field is mapped to the
user.managers.email_addresses
UDM field.
Else, the
relations.value
log field is mapped to the
user.attribute.labels
UDM field.
sshPublicKeys.expirationTimeUsec
entity.user.attribute.labels[ssh_key_expiration_timec]
sshPublicKeys.fingerprint
entity.user.attribute.labels[ssh_key_fingerprint]
sshPublicKeys.key
entity.user.attribute.labels[ssh_key]
suspended
entity.user.user_authentication_status
If the
suspended
log field value is equal to
true
and the
archived
log field value is
not
equal to
true
, then the
entity.user.user_authentication_status
UDM field is set to
SUSPENDED
.
If the
archived
log field value is equal to
true
, then the
entity.user.user_authentication_status
UDM field is set to
DELETED
.
Else, the
entity.user.user_authentication_status
UDM field is set to
ACTIVE
.
archived
entity.user.user_authentication_status
If the
suspended
log field value is equal to
true
and the
archived
log field value is
not
equal to
true
, then the
entity.user.user_authentication_status
UDM field is set to
SUSPENDED
.
If the
archived
log field value is equal to
true
, then the
entity.user.user_authentication_status
UDM field is set to
DELETED
.
Else, the
entity.user.user_authentication_status
UDM field is set to
ACTIVE
.
suspensionReason
entity.user.attribute.labels[suspension_reason]
thumbnailPhotoEtag
entity.user.attribute.labels[thumbnail_photo_etag]
thumbnailPhotoUrl
entity.url
websites.customType
entity.user.attribute.labels[websites_custom_type]
websites.primary
entity.user.attribute.labels[websites_primary]
websites.type
entity.user.attribute.labels[websites_type]
websites.value
entity.user.attribute.labels[websites_value]
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Cloud Identity
.
metadata.entity_type
The
metadata.entity_type
UDM field is set to
USER
.
customSchemas
additional.fields[custom_schemas]
Iterate for each key-value pair of
customSchemas
, then
key
log field is mapped to the
additional.fields.key
UDM field.
Iterate for each key-value pair of log field
value
, then
%{key}_%{key1}
log field is mapped to the
additional.fields.key
UDM field.
Iterate for each key-value pair of log field
value1
, then
%{key}_%{key1}_%{key2}
log field is mapped to the
additional.fields.key
UDM field.
Iterate for each key-value pair of log field
value2
, then
%{key}_%{key1}_%{key2}_%{key3}
log field is mapped to the
additional.fields.key
UDM field.
Field mapping reference: WORKSPACE_MOBILE_DEVICES
The following table lists the log fields of the
WORKSPACE_MOBILE_DEVICES
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
adbStatus
entity.asset.attribute.labels[abd status]
applications.displayName
entity.asset.software.name
applications.packageName
entity.asset.attribute.labels[application_package_name]
applications.permission
entity.asset.software.permissions.name
applications.versionCode
entity.asset.attribute.labels[application_version_code]
applications.versionName
entity.asset.software.version
basebandVersion
entity.asset.attribute.labels[baseband_version]
bootloaderVersion
entity.asset.attribute.labels[bootloader_version]
brand
entity.asset.attribute.labels[brand]
buildNumber
entity.asset.attribute.labels[build_number]
defaultLanguage
entity.asset.attribute.labels[default_language]
developerOptionsStatus
entity.asset.attribute.labels[developer_options_status]
deviceCompromisedStatus
entity.asset.attribute.labels[device_compromised_status]
deviceId
entity.asset.asset_id
devicePasswordStatus
entity.asset.attribute.labels[device_password_status]
email
entity.user.email_addresses
encryptionStatus
entity.asset.attribute.labels[encryption_status]
etag
entity.labels[etag]
(deprecated)
etag
additional.fields[etag]
firstSync
entity.asset.attribute.labels[first_sync]
hardware
entity.asset.attribute.labels[hardware]
hardwareId
entity.asset.attribute.labels[hardware_id]
imei
entity.asset.asset_id
deviceId
entity.asset.asset_id
If the
imei
log field value is empty, then the
deviceId
log field is mapped to the
entity.asset.asset_id
UDM field.
kernelVersion
entity.asset.attribute.labels[kernel_version]
kind
entity.labels[kind]
(deprecated)
kind
additional.fields[kind]
lastSync
entity.asset.attribute.labels[last_sync]
managedAccountIsOnOwnerProfile
entity.asset.attribute.labels[managed_account_is_on_owner_profile]
manufacturer
entity.asset.hardware.manufacturer
meid
entity.asset.attribute.labels[meid]
model
entity.asset.hardware.model
name
entity.user.user_display_name
networkOperator
entity.asset.attribute.labels[network_operator]
os
entity.asset.platform_software.platform
If the
os
log field value matches
iOS
, then the
entity.asset.platform_software.platform
UDM field is set to
IOS
.
If the
os
log field value matches
Android
, then the
entity.asset.platform_software.platform
UDM field is set to
ANDROID
.
Else, the
entity.asset.platform_software.platform
UDM field is set to
UNKNOWN_PLATFORM
.
otherAccountsInfo[]
entity.asset.attribute.labels[other_accounts_info]
privilege
entity.asset.attribute.labels[privilege]
releaseVersion
entity.asset.attribute.labels[release_version]
resourceId
entity.asset.product_object_id
securityPatchLevel
entity.asset.platform_software.platform_patch_level
serialNumber
entity.asset.hardware.serial_number
status
entity.user.user_authentication_status
If the
status
log field value is equal to
approved
, then the
entity.user.user_authentication_status
UDM field is set to
ACTIVE
.
If the
status
log field value is equal to
unprovisined
, then the
entity.user.user_authentication_status
UDM field is set to
SUSPENDED
.
supportsWorkProfile
entity.asset.attribute.labels[supports_work_profile]
type
entity.asset.attribute.labels[type]
unknownSourcesStatus
entity.asset.attribute.labels[unknown_sources_status]
userAgent
entity.asset.attribute.labels[user_agent]
wifiMacAddress
entity.asset.mac
metadata.entity_type
The
metadata.entity_type
UDM field is set to
ASSET
.
metadata.product_name
The
metadata.product_name
UDM field is set to
WORKSPACE_MOBILE
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
relations.entity_type
The
relations.entity_type
UDM field is set to
USER
.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
.
Field mapping reference: WORKSPACE_CHROMEOS
The following table lists the log fields of the
WORKSPACE_CHROMEOS
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
activeTimeRanges.activeTime
entity.asset.attribute.labels[active_time]
activeTimeRanges.date
entity.asset.attribute.labels[active_time_range_date]
annotatedAssetId
entity.asset.asset_id
If the
annotatedAssetId
log field value is
not
empty, then the
ASSET ID: annotatedAssetId
log field is mapped to the
entity.asset.asset_id
UDM field.
deviceId
entity.asset.asset_id
If the
annotatedAssetId
log field value is empty, then the
CHROMEOS:deviceId
log field is mapped to the
entity.asset.asset_id
UDM field.
annotatedLocation
entity.asset.location.name
annotatedUser
relations.entity.user.user_display_name
If the
annotatedUser
log field value is
not
empty and the
annotatedUser
log field value does not match the regular expression
@
, then the
annotatedUser
log field is mapped to the
relations.entity.user.user_display_name
UDM field.
autoUpdateExpiration
entity.asset.attribute.labels[auto_update_expiration]
bootMode
entity.asset.attribute.labels[boot_mode]
cpuInfo.architecture
entity.asset.attribute.labels[cpu_architecture]
cpuInfo.logicalCpus.cStates.displayName
entity.asset.attribute.labels[cpu_logical_cups_cstates_display_name]
cpuInfo.logicalCpus.cStates.sessionDuration
entity.asset.attribute.labels[cpu_logical_cups_cstates_session_duration]
cpuInfo.logicalCpus.currentScalingFrequencyKhz
entity.asset.attribute.labels[cpu_current_scaling_frequency]
cpuInfo.logicalCpus.idleDuration
entity.asset.attribute.labels[cpu_ideal_duration]
cpuInfo.logicalCpus.maxScalingFrequencyKhz
entity.asset.attribute.labels[cpu_max_scaling_frequency]
cpuInfo.maxClockSpeedKhz
entity.asset.attribute.labels[cpu_max_clock_speed]
cpuInfo.model
entity.asset.hardware.cpu_model
cpuStatusReports.cpuTemperatureInfo.label
entity.asset.attribute.labels[cpu_temperature_label]
cpuStatusReports.cpuTemperatureInfo.temperature
entity.asset.attribute.labels[cpu_temperature]
cpuStatusReports.cpuUtilizationPercentageInfo
entity.asset.attribute.labels[cpu_utilization_percentage_info]
cpuStatusReports.reportTime
entity.asset.attribute.labels[cpu_report_time]
deviceFiles.createTime
relations.entity.file.first_seen_time
deviceFiles.downloadUrl
relations.entity.file.full_path
deviceFiles.name
relations.entity.file.names
deviceFiles.type
relations.entity.file.mime_type
relations.entity_type
The
relations.entity_type
UDM field is set to
FILE
.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
.
deviceId
entity.asset.product_object_id
diskVolumeReports.volumeInfo.storageFree
entity.asset.attribute.labels[volume_info_storage_free]
diskVolumeReports.volumeInfo.storageTotal
entity.asset.attribute.labels[volume_info_storage_total]
diskVolumeReports.volumeInfo.volumeId
entity.asset.attribute.labels[volume_id]
dockMacAddress
entity.asset.attribute.labels[dock_mac_address]
etag
entity.labels[etag]
(deprecated)
etag
additional.fields[etag]
ethernetMacAddress0
entity.asset.attribute.labels[ethernet_mac_address]
firmwareVersion
entity.asset.attribute.labels[firmware_version]
kind
entity.labels[kind]
(deprecated)
kind
additional.fields[kind]
lastEnrollmentTime
entity.asset.last_discover_time
lastKnownNetwork.ipAddress
entity.asset.ip
lastKnownNetwork.wanIpAddress
entity.asset.nat_ip
lastSync
entity.asset.system_last_update_time
macAddress
entity.asset.mac
ethernetMacAddress
entity.asset.mac
manufactureDate
entity.asset.attribute.labels[manufacture_date]
meid
entity.asset.attribute.labels[meid]
model
entity.asset.hardware.model
notes
entity.asset.attribute.labels[notes]
orderNumber
entity.asset.attribute.labels[order_number]
orgUnitId
entity.asset.attribute.labels[org_unit_id]
orgUnitPath
entity.user.attribute.labels[org_unit_path]
osVersion
entity.asset.attribute.labels[os_version]
platformVersion
entity.asset.platform_software.platform_version
annotatedUser
entity.user.email_addresses
If the
annotatedUser
log field value is
not
empty
and the
annotatedUser
log field value matches the regular expression
@
, then the
annotatedUser
log field is mapped to the
entity.user.email_addresses
UDM field.
recentUsers.email
entity.user.email_addresses
recentUsers.type
relations.entity.user.attribute.roles.name
relations.entity.user.attribute.roles.description
If the
recentUsers.type
log field value is equal to
USER_TYPE_MANAGED
, then the
relations.entity.user.attribute.roles.description
UDM field is set to
The user is managed by the domain
.
Else, if the
recentUsers.type
log field value is equal to
USER_TYPE_UNMANAGED
, then the
relations.entity.user.attribute.roles.description
UDM field is set to
The user is not managed by the domain
.
screenshotFiles.createTime
relations.entity.file.first_seen_time
screenshotFiles.downloadUrl
relations.entity.file.full_path
screenshotFiles.name
relations.entity.file.names
screenshotFiles.type
relations.entity.file.mime_type
serialNumber
entity.asset.hardware.serial_number
status
entity.asset.deployment_status
If the
status
log field value is equal to
DEPROVISIONED
, then the
entity.asset.deployment_status
UDM field is set to
DECOMMISSIONED
.
Else, the
entity.asset.deployment_status
UDM field is set to
ACTIVE
.
supportEndDate
entity.asset.attribute.labels[support_end_date]
systemRamFreeReports.reportTime
entity.asset.attribute.labels[system_ram_report_time]
systemRamFreeReports.systemRamFreeInfo
entity.asset.attribute.labels[system_ram_free_info]
systemRamTotal
entity.asset.hardware.ram
tpmVersionInfo.family
entity.asset.attribute.labels[tpm_ver_info_family]
tpmVersionInfo.firmwareVersion
entity.asset.attribute.labels[tpm_ver_info_firmware_version]
tpmVersionInfo.manufacturer
entity.asset.attribute.labels[tpm_ver_info_manufacturer]
tpmVersionInfo.specLevel
entity.asset.attribute.labels[tpm_ver_info_spec_level]
tpmVersionInfo.tpmModel
entity.asset.attribute.labels[tpm_ver_info_tpm_model]
tpmVersionInfo.vendorSpecific
entity.asset.attribute.labels[tpm_ver_info_vendor_specific]
willAutoRenew
entity.asset.attribute.labels[will_auto_renew]
entity.asset.type
The
entity.asset.type
UDM field is set to
WORKSTATION
.
metadata.entity_type
The
metadata.entity_type
UDM field is set to
ASSET
.
metadata.product_name
The
metadata.product_name
UDM field is set to
ChromeOS
.
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
GOOGLE
.
relations.entity_type
The
relations.entity_type
UDM field is set to
USER
.
relations.relationship
The
relations.relationship
UDM field is set to
MEMBER
.
Field mapping reference: WORKSPACE_PRIVILEGES
The following table lists the log fields of the
WORKSPACE_PRIVILEGES
log type and their corresponding UDM fields.
Log field
UDM mapping
roleAssignments.assignedTo
metadata.product_entity_id
roleAssignments.roleAssignmentId
entity.user.attribute.labels[role_assignment_id]
roleAssignments.roleDetails.roleDescription
entity.user.attribute.roles.description
roleAssignments.roleDetails.roleId
entity.user.attribute.labels[role_details_role_id]
roleAssignments.roleDetails.roleName
entity.user.attribute.roles.name
roleAssignments.roleDetails.rolePrivileges.details.childPrivileges.etag
roleAssignments.roleDetails.rolePrivileges.details.childPrivileges.isOuScopable
roleAssignments.roleDetails.rolePrivileges.details.childPrivileges.kind
roleAssignments.roleDetails.rolePrivileges.details.childPrivileges.privilegeName
entity.user.attribute.labels[%{rolePrivilege.privilegeName}_CHILD_PRIVILEGES]
roleAssignments.roleDetails.rolePrivileges.details.childPrivileges.serviceId
roleAssignments.roleDetails.rolePrivileges.details.childPrivileges.serviceName
roleAssignments.roleDetails.rolePrivileges.details.etag
entity.labels[etag]
(deprecated)
roleAssignments.roleDetails.rolePrivileges.details.etag
additional.fields[etag]
roleAssignments.roleDetails.rolePrivileges.details.isOuScopable
entity.user.attribute.labels[is_ou_scopable]
roleAssignments.roleDetails.rolePrivileges.details.kind
entity.labels[kind]
(deprecated)
roleAssignments.roleDetails.rolePrivileges.details.kind
additional.fields[kind]
roleAssignments.roleDetails.rolePrivileges.details.privilegeName
roleAssignments.roleDetails.rolePrivileges.details.serviceId
roleAssignments.roleDetails.rolePrivileges.details.serviceName
entity.user.attribute.labels[service_name]
roleAssignments.roleDetails.rolePrivileges.privilegeName
entity.user.attribute.permissions.name
roleAssignments.roleDetails.rolePrivileges.serviceId
entity.user.attribute.permissions.description
roleAssignments.roleId
entity.user.attribute.labels[role_id]
roleAssignments.scopeType
entity.user.attribute.labels[scope_type]
userId
entity.user.userid
metadata.vendor_name
metadata.product_name
metadata.entity_type
Need more help?
Get answers from Community members and Google SecOps professionals.
