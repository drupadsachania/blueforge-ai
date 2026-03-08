# Collect BeyondTrust Remote Support logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/bomgar/  
**Scraped:** 2026-03-05T09:51:18.582857Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect BeyondTrust Remote Support logs
Supported in:
Google secops
SIEM
This parser handles syslog messages from BeyondTrust Remote Support, transforming them into UDM format. It processes both CEF and non-CEF formatted logs, extracting fields, performing data transformations, and mapping them to the appropriate UDM fields, including principal, target, and security result details.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you are using Windows 2016 or later, or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
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
Install Bindplane Agent
For
Windows installation
, run the following script:
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
For
Linux installation
, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
Additional installation options can be found in this
installation guide
.
Configure Bindplane Agent to ingest Syslog and send to Google SecOps
Access the machine where Bindplane is installed.
Edit the
config.yaml
file as follows:
receivers:
    tcplog:
        # Replace the below port <54525> and IP <0.0.0.0> with your specific values
        listen_address: "0.0.0.0:54525" 

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        # Adjust the creds location below according the placement of the credentials file you downloaded
        creds: '{ json file for creds }'
        # Replace <customer_id> below with your actual ID that you copied
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        # You can apply ingestion labels below as preferred
        ingestion_labels:
        log_type: SYSLOG
        namespace: BeyondTrust_Remote_Support
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes:
sudo
systemctl
restart
bindplane
Configure Syslog export from BeyondTrust Remote Support
Sign in to your BeyondTrust Remote Support.
Go to
Security
>
Appliance Administration
.
Go to the
Syslog
section and set the following values:
Remote Syslog Server
: enter the hostname or IP address of the syslog host server (Bindplane). In this field, you can add up to three syslog servers.
Message format
: select
RFC 5424
.
Port
: enter the port of the syslog host server (Bindplane).
Click
Submit
.
UDM Mapping
Log field
UDM mapping
Logic
account:expiration
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "account:expiration" field in the raw log.
account:email:locale
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "account:email:locale" field in the raw log.
command_shell_is_whitelist
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "ssions:command_shell_is_whitelist" field in the raw log.
datetime
read_only_udm.metadata.event_timestamp.seconds
The value is parsed from the "datetime" field in the raw log and converted to a Unix timestamp.
dtPostTime
read_only_udm.metadata.event_timestamp.seconds
The value is parsed from the "dtPostTime" field in the raw log and converted to a Unix timestamp.
event
read_only_udm.metadata.product_event_type
The value is taken from the "event" field in the raw log.
host
read_only_udm.principal.hostname
The value is taken from the "host" field in the raw log.
id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "id" field in the raw log.
license_pool:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "license_pool:id" field in the raw log.
login_schedule:timezone
read_only_udm.target.location.country_or_region
The value is taken from the "login_schedule:timezone" field in the raw log.
old_account:email:address
read_only_udm.target.user.email_addresses
The value is taken from the "old_account:email:address" field in the raw log.
old_account:failed_logins
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_account:failed_logins" field in the raw log.
old_display_number
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_display_number" field in the raw log.
old_login_schedule:timezone
read_only_udm.target.location.country_or_region
The value is taken from the "old_login_schedule:timezone" field in the raw log.
old_permissions:api:reporting
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:api:reporting" field in the raw log.
old_permissions:jump_item_role:default:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:jump_item_role:default:id" field in the raw log.
old_permissions:jump_item_role:default:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:jump_item_role:default:name" field in the raw log.
old_permissions:jump_item_role:teams:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:jump_item_role:teams:id" field in the raw log.
old_permissions:jump_item_role:teams:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:jump_item_role:teams:name" field in the raw log.
old_permissions:presentations:control:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:presentations:control:status" field in the raw log.
old_permissions:public_sites:templates:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:public_sites:templates:status" field in the raw log.
old_permissions:reporting:presentation_reports
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:reporting:presentation_reports" field in the raw log.
old_permissions:reporting:support_reports
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:reporting:support_reports" field in the raw log.
old_permissions:reporting:vault_reports
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:reporting:vault_reports" field in the raw log.
old_permissions:support
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support" field in the raw log.
old_permissions:support:accept_team_sessions:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:accept_team_sessions:status" field in the raw log.
old_permissions:support:bomgar_button:change_public_sites:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:bomgar_button:change_public_sites:status" field in the raw log.
old_permissions:support:bomgar_button:personal:deploy:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:bomgar_button:personal:deploy:status" field in the raw log.
old_permissions:support:bomgar_button:team:manage
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:bomgar_button:team:manage" field in the raw log.
old_permissions:support:bomgar_button:team:manage:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:bomgar_button:team:manage:status" field in the raw log.
old_permissions:support:ios_content
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:ios_content" field in the raw log.
old_permissions:support:jump:local
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:jump:local" field in the raw log.
old_permissions:support:jump:local:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:jump:local:status" field in the raw log.
old_permissions:support:jump:remote
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:jump:remote" field in the raw log.
old_permissions:support:jump:remote:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:jump:remote:status" field in the raw log.
old_permissions:support:rdp:local
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:rdp:local" field in the raw log.
old_permissions:support:rdp:local:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:rdp:local:status" field in the raw log.
old_permissions:support:rdp:remote
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:rdp:remote" field in the raw log.
old_permissions:support:rdp:remote:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:rdp:remote:status" field in the raw log.
old_permissions:support:session_assignment:idle_timeout
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:session_assignment:idle_timeout" field in the raw log.
old_permissions:support:session_assignment:idle_timeout:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:session_assignment:idle_timeout:status" field in the raw log.
old_permissions:support:session_assignment:session_limit
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:session_assignment:session_limit" field in the raw log.
old_permissions:support:session_assignment:session_limit:status=forbid_override
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:session_assignment:session_limit:status=forbid_override" field in the raw log.
old_permissions:support:session_keys
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:session_keys" field in the raw log.
old_permissions:support:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:status" field in the raw log.
old_permissions:support:team_share
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:team_share" field in the raw log.
old_permissions:support:team_transfer
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:team_transfer" field in the raw log.
old_permissions:support:vnc:local
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:vnc:local" field in the raw log.
old_permissions:support:vnc:local:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:vnc:local:status" field in the raw log.
old_permissions:support:vnc:remote
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:vnc:remote" field in the raw log.
old_permissions:support:vnc:remote:status
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_permissions:support:vnc:remote:status" field in the raw log.
old_private_display_name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_private_display_name" field in the raw log.
old_provider:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_provider:id" field in the raw log.
old_provider:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "old_provider:name" field in the raw log.
permissions:jump_item_role:default:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "permissions:jump_item_role:default:id" field in the raw log.
permissions:jump_item_role:default:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "permissions:jump_item_role:default:name" field in the raw log.
permissions:jump_item_role:teams:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "permissions:jump_item_role:teams:id" field in the raw log.
permissions:jump_item_role:teams:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "permissions:jump_item_role:teams:name" field in the raw log.
provider:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "provider:id" field in the raw log.
provider:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "provider:name" field in the raw log.
reason
read_only_udm.security_result.description
The value is taken from the "reason" field in the raw log and appended to the description field with the prefix " - Reason:".
sEventID
read_only_udm.metadata.product_event_type
The value is taken from the "sEventID" field in the raw log.
sIpAddress
read_only_udm.principal.ip
The value is taken from the "sIpAddress" field in the raw log.
sLoginName
read_only_udm.principal.user.userid
The value is parsed from the "sLoginName" field in the raw log. If the field contains a domain, the domain is extracted and mapped to read_only_udm.principal.namespace.
sMessage
read_only_udm.security_result.description
The value is taken from the "sMessage" field in the raw log. The parser extracts the text within the quotes and maps it to the description field.
sOriginatingAccount
read_only_udm.principal.user.userid
The value is parsed from the "sOriginatingAccount" field in the raw log. If the field contains a domain, the domain is extracted and mapped to read_only_udm.principal.namespace.
sOriginatingApplicationComponent
read_only_udm.principal.application
The value is taken from the "sOriginatingApplicationComponent" field in the raw log and appended to the application field within parentheses after the value from sOriginatingApplicationName.
sOriginatingApplicationName
read_only_udm.principal.application
The value is taken from the "sOriginatingApplicationName" field in the raw log.
sOriginatingSystem
read_only_udm.principal.hostname
The value is taken from the "sOriginatingSystem" field in the raw log.
session_policy:id
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "session_policy:id" field in the raw log.
session_policy:name
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "session_policy:name" field in the raw log.
session_policy:purpose
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "session_policy:purpose" field in the raw log.
site
read_only_udm.target.hostname
The value is taken from the "site" field in the raw log.
status
read_only_udm.security_result.summary
The value is taken from the "status" field in the raw log and appended to the summary field.
support:jump:local
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:jump:local" field in the raw log.
support:permissions:allow_pinned_clients
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:allow_pinned_clients" field in the raw log.
support:permissions:allow_users
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:allow_users" field in the raw log.
support:permissions:canned_scripts
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:canned_scripts" field in the raw log.
support:permissions:chat
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:chat" field in the raw log.
support:permissions:chat:push_url
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:chat:push_url" field in the raw log.
support:permissions:chat:send_file
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:chat:send_file" field in the raw log.
support:permissions:command_shell
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:command_shell" field in the raw log.
support:permissions:deploy_callback_button
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:deploy_callback_button" field in the raw log.
support:permissions:elevation
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:elevation" field in the raw log.
support:permissions:file_transfers:cust
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:file_transfers:cust" field in the raw log.
support:permissions:file_transfers:download
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:file_transfers:download" field in the raw log.
support:permissions:file_transfers:rep
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:file_transfers:rep" field in the raw log.
support:permissions:file_transfers:upload
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:file_transfers:upload" field in the raw log.
support:permissions:registry_access
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:registry_access" field in the raw log.
support:permissions:request_pin_unpin
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:request_pin_unpin" field in the raw log.
support:permissions:screen_sharing
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing" field in the raw log.
support:permissions:screen_sharing:allow_elevated_tools
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:allow_elevated_tools" field in the raw log.
support:permissions:screen_sharing:annotations
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:annotations" field in the raw log.
support:permissions:screen_sharing:application_restriction
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:application_restriction" field in the raw log.
support:permissions:screen_sharing:application_sharing
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:application_sharing" field in the raw log.
support:permissions:screen_sharing:clipboard_direction
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:clipboard_direction" field in the raw log.
support:permissions:screen_sharing:cobrowse
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:cobrowse" field in the raw log.
support:permissions:screen_sharing:privacy_mode
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:privacy_mode" field in the raw log.
support:permissions:screen_sharing:show_screen
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:screen_sharing:show_screen" field in the raw log.
support:permissions:system_info
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:system_info" field in the raw log.
support:permissions:system_info:actions
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:permissions:system_info:actions" field in the raw log.
support:prompting:command_shell
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:command_shell" field in the raw log.
support:prompting:default
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:default" field in the raw log.
support:prompting:deploy_callback_button
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:deploy_callback_button" field in the raw log.
support:prompting:elevate
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:elevate" field in the raw log.
support:prompting:file_transfer
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:file_transfer" field in the raw log.
support:prompting:registry
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:registry" field in the raw log.
support:prompting:screen_sharing:cobrowse
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:screen_sharing:cobrowse" field in the raw log.
support:prompting:screen_sharing:full_access
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "support:prompting:screen_sharing:full_access" field in the raw log.
target
read_only_udm.target.application
The value is taken from the "target" field in the raw log. The parser replaces "rep_client" with "Representative Console" and "web/login" with "Web/Login".
two_factor_auth:app
read_only_udm.principal.user.attribute.labels.value
The value is taken from the "two_factor_auth:app" field in the raw log.
when
read_only_udm.metadata.product_log_id
The value is taken from the "when" field in the raw log.
when
read_only_udm.metadata.event_timestamp.seconds
The value is parsed from the "when" field in the raw log and converted to a Unix timestamp.
who
read_only_udm.principal.user.userid
The value is parsed from the "who" field in the raw log. The parser extracts the text within the parentheses.
who
read_only_udm.principal.user.user_display_name
The value is parsed from the "who" field in the raw log. The parser extracts the text before the parentheses.
who_ip
read_only_udm.principal.ip
The value is taken from the "who_ip" field in the raw log.
read_only_udm.metadata.vendor_name
The value is set to "BeyondTrust" by the parser.
read_only_udm.metadata.product_name
The value is set to "BeyondTrust Remote Support" by the parser.
read_only_udm.metadata.log_type
The value is set to "BOMGAR" by the parser.
read_only_udm.extensions.auth.type
The value is set to "MACHINE" if the target is "rep_client", "SSO" if the target is "web/login", and "AUTHTYPE_UNSPECIFIED" otherwise by the parser.
read_only_udm.extensions.auth.mechanism
The value is set to "USERNAME_PASSWORD" if the method is "using password", "REMOTE" if the method is "using elevate", and left empty otherwise by the parser.
read_only_udm.security_result.action
The value is set to "ALLOW" if the status is not "failure", the reason is not "failed" or "user not found", and the sMessage does not contain "failed login to web app". Otherwise, the value is set to "BLOCK" by the parser.
read_only_udm.security_result.summary
The value is set to "User login " or "User logout " based on the eventName, followed by the status if it is not empty by the parser.
read_only_udm.security_result.description
The value is set to "User " followed by the userid, IP address, status, eventName, connector ("to" for login and "from" for logout), target, and method. If the reason is not empty and not "failed", it is appended to the description with the prefix " - Reason:" by the parser.
Need more help?
Get answers from Community members and Google SecOps professionals.
