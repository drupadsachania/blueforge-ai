# Collect Duo Activity logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/duo-activity/  
**Scraped:** 2026-03-05T09:47:47.239451Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Duo Activity logs
Supported in:
Google secops
SIEM
This document describes how to export Duo Activity logs and ingest them into Google Security Operations by deploying the ingestion script written in Python as a Cloud Run function and how log fields map to Google SecOps Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of Duo Activity and the ingestion script deployed as Cloud Run functions to send logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
Duo Activity
: The platform from which you collect logs.
Cloud Run functions
: The ingestion script deployed as Cloud Run functions to fetch logs from Duo Activity and ingest them into Google SecOps.
Google SecOps
: Retains and analyzes the logs.
Note:
An ingestion label identifies the parser which normalizes raw log data to structured UDM format. The information in this document applies to the parser with the
DUO_ACTIVITY
ingestion label.
Before you begin
Ensure that you have access to the Duo Admin panel.
Ensure that you're using Duo Admin API version 2 or later.
Configure Duo Activity
Sign in to the Duo Admin panel as an administrator. For more information, see
Duo Administration Admin Panel Overview
.
Click
Applications
>
Protect an Application
.
In the Applications list, click Admin API >
Protect
to get your integration key, secret key, and API hostname.
Select the required permissions you want to grant to the Admin API application. For more information regarding required permissions for the respective operations, see
Duo Admin API
.
Configure log ingestion for Google SecOps
Create a deployment directory to store the files for the Cloud Run functions. This directory will contain all files needed for the deployment.
Copy all files from the GitHub subdirectory of Duo Activity located in the Google SecOps
GitHub repository
to this deployment directory.
Copy the common folder and all its contents to the deployment directory.
Edit the
.env.yml
file to add all the required environment variables.
Configure the environment variables marked as
Secret
in Secret Manager. For more information on how to create secrets, see
Creating and accessing secrets
.
Use the secret's resource name as the value for the environment variables.
Enter the value
DUO_ACTIVITY
in the
CHRONICLE_NAMESPACE
environment variable.
In the
Source code
field, select
ZIP Upload
.
In the
Destination bucket
field, click
Browse
to select a Cloud Storage bucket to upload your source code to as part of your deployment.
In the
ZIP file
field, click
Browse
to select a zip file to upload from your local file system. Your function source files must be located at the root of the zip file.
Click
Deploy
.
For more information, see
Use ingestion scripts deployed as Cloud Run functions
.
Supported Duo Activity log formats
The Duo Activity parser supports logs in JSON formats.
Supported Duo Activity Sample Logs
JSON
{
    "access_device": {
      "browser": "Chrome",
      "browser_version": "127.0.0.0",
      "ip": {
        "address": "198.51.100.0"
      },
      "location": {
        "city": "Riverside",
        "country": "United States",
        "state": "California"
      },
      "os": "Windows",
      "os_version": "10"
    },
    "action": {
      "details": null,
      "name": "bypass_create"
    },
    "activity_id": "188c068b-1ef4-4c0a-80cc-700ee9a08612",
    "actor": {
      "details": "{\\"created\\": \\"2022-09-15T17: 27: 31.000000+00: 00\\", \\"last_login\\": \\"2024-08-26T22: 48: 50.000000+00: 00\\", \\"email\\": \\"test@gmail.com\\", \\"status\\": null, \\"groups\\": null}",
      "key": "dummyuserid",
      "name": "test",
      "type": "admin"
    },
    "akey": "DA06L58ASEO0DOKNXGXZ",
    "application": null,
    "old_target": null,
    "outcome": null,
    "target": {
      "details": "{\\"bkeys\\": [\\"DB8VPGAF6674GKS43FS9\\"], \\"count\\": 1, \\"valid_secs\\": 3600, \\"remaining_uses\\": 1, \\"auto_generated\\": true}",
      "key": "DU3H7GRU6UIENBKX5HRA",
      "name": "test",
      "type": "user_bypass"
    },
    "ts": "2024-08-26T22:49:21.975784+00:00"
  }
Field mapping reference
Field mapping reference: Event Identifier to Event Type
The following table lists the
DUO_ACTIVITY
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
admin_activate_duo_push
DEVICE_PROGRAM_DOWNLOAD
admin_factor_restrictions
RESOURCE_PERMISSIONS_CHANGE
admin_login
USER_UNCATEGORIZED
admin_rectivates_duo_push
DEVICE_PROGRAM_DOWNLOAD
admin_reset_password
USER_CHANGE_PASSWORD
admin_send_reset_password_email
EMAIL_TRANSACTION
bypass_create
RESOURCE_CREATION
bypass_delete
RESOURCE_DELETION
bypass_view
RESOURCE_READ
deregister_devices
USER_RESOURCE_DELETION
device_change_enrollment_summary_notification_answered
USER_COMMUNICATION
device_change_enrollment_summary_notification_answered_notify_admin
USER_COMMUNICATION
device_change_enrollment_summary_notification_send
USER_COMMUNICATION
device_change_notification_answered
USER_COMMUNICATION
device_change_notification_answered_notify_admin
USER_COMMUNICATION
device_change_notification_create
RESOURCE_CREATION
device_change_notification_send
USER_COMMUNICATION
group_create
GROUP_CREATION
group_delete
GROUP_DELETION
group_update
GROUP_MODIFICATION
hardtoken_create
RESOURCE_CREATION
hardtoken_delete
RESOURCE_DELETION
hardtoken_resync
RESOURCE_WRITTEN
hardtoken_update
RESOURCE_WRITTEN
integration_create
RESOURCE_CREATION
integration_delete
RESOURCE_DELETION
integration_group_policy_add
GROUP_UNCATEGORIZED
integration_group_policy_remove
GROUP_UNCATEGORIZED
integration_policy_assign
USER_UNCATEGORIZED
integration_policy_unassign
USER_UNCATEGORIZED
integration_skey_bulk_view
RESOURCE_READ
integration_skey_view
RESOURCE_READ
integration_update
RESOURCE_WRITTEN
log_export_start
USER_UNCATEGORIZED
log_export_complete
USER_UNCATEGORIZED
log_export_failure
USER_UNCATEGORIZED
management_system_activate_device_cache
DEVICE_CONFIG_UPDATE
management_system_active_device_cache_add_devices
RESOURCE_CREATION
management_system_active_device_cache_delete_devices
RESOURCE_DELETION
management_system_active_device_cache_edit_devices
RESOURCE_WRITTEN
management_system_add_devices
RESOURCE_CREATION
management_system_create
RESOURCE_CREATION
management_system_delete
RESOURCE_DELETION
management_system_delete_devices
RESOURCE_DELETION
management_system_device_cache_add_devices
RESOURCE_CREATION
management_system_device_cache_create
RESOURCE_CREATION
management_system_device_cache_delete
RESOURCE_DELETION
management_system_device_cache_delete_devices
RESOURCE_DELETION
management_system_download_device_api_script
DEVICE_PROGRAM_DOWNLOAD
management_system_pkcs12_enrollment
RESOURCE_CREATION
management_system_sync_failure
USER_UNCATEGORIZED
management_system_sync_success
USER_UNCATEGORIZED
management_system_update
USER_UNCATEGORIZED
management_system_view_password
RESOURCE_READ
management_system_view_token
RESOURCE_READ
phone_activation_code_regenerated
RESOURCE_CREATION
phone_associate
RESOURCE_CREATION
phone_create
RESOURCE_CREATION
phone_delete
RESOURCE_DELETION
phone_disassociate
RESOURCE_DELETION
phone_new_sms_passcode
RESOURCE_CREATION
phone_update
RESOURCE_WRITTEN
policy_create
RESOURCE_CREATION
policy_delete
RESOURCE_DELETION
policy_update
RESOURCE_WRITTEN
u2ftoken_create
RESOURCE_CREATION
u2ftoken_delete
RESOURCE_DELETION
user_not_enrolled_lockout
USER_CHANGE_PERMISSIONS
user_adminapi_lockout
USER_CHANGE_PERMISSIONS
user_lockout_cleared
USER_CHANGE_PERMISSIONS
webauthncredential_create
RESOURCE_CREATION
webauthncredential_delete
RESOURCE_DELETION
webauthncredential_rename
RESOURCE_WRITTEN
Field mapping reference: DUO_ACTIVITY
The following table lists the log fields of the
DUO_ACTIVITY
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
principal.platform
If the
access_device.os
log field value matches the regular expression pattern
(?i)Win
, then the
principal.platform
UDM field is set to
WINDOWS
.
Else, if the
access_device.os
log field value matches the regular expression pattern
(?i)Lin
, then the
principal.platform
UDM field is set to
LINUX
.
Else, if the
access_device.os
log field value matches the regular expression pattern
(?i)Mac
, then the
principal.platform
UDM field is set to
MAC
.
Else, if the
access_device.os
log field value matches the regular expression pattern
(?i)ios
, then the
principal.platform
UDM field is set to
IOS
.
Else, if the
access_device.os
log field value matches the regular expression pattern
(?i)Chrome
, then the
principal.platform
UDM field is set to
CHROME_OS
.
Else, if the
access_device.os
log field value matches the regular expression pattern
(?i)Android
, then the
principal.platform
UDM field is set to
ANDROID
.
Else, the
principal.platform
UDM field is set to
UNKNOWN_PLATFORM
.
access_device.os_version
principal.platform_version
access_device.ip.address
principal.ip
access_device.location.country
principal.location.country_or_region
access_device.location.state
principal.location.state
access_device.location.city
principal.location.city
access_device.browser
principal.asset.attribute.labels[access_device_browser]
access_device.browser_version
principal.asset.attribute.labels[access_device_browser_version]
ts
metadata.event_timestamp
activity_id
metadata.product_log_id
akey
principal.asset.product_object_id
outcome.result
security_result.action_details
application.key
principal.resource.product_object_id
application.name
principal.application
application.type
principal.resource.resource_subtype
action.details
principal.user.attribute.labels[action_details]
action.name
metadata.product_event_type
actor.key
principal.user.userid
actor.name
principal.user.user_display_name
actor.type
principal.user.attribute.labels[actor_type]
target.key
target.asset.attribute.labels[target_key]
target.name
target.asset.hostname
target.type
target.asset.category
target.details
target.user.attribute.labels[target_details]
old_target.key
about.asset.attribute.labels[old_target_key]
old_target.name
about.asset.hostname
old_target.type
about.asset.category
old_target.details
about.user.attribute.labels[old_target_details]
actor.details.created
principal.user.first_seen_time
actor.details.last_login
principal.user.last_login_time
actor.details.status
principal.user.attribute.labels[status]
actor.details.email
principal.user.email_addresses
actor.details.group.key
principal.user.attribute.labels[actor_details_group_key]
actor.details.group.name
principal.user.attribute.labels[actor_details_group_name]
What's next
Data ingestion to Google SecOps
Need more help?
Get answers from Community members and Google SecOps professionals.
