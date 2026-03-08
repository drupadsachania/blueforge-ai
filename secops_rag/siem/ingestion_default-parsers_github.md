# Collect GitHub audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/github/  
**Scraped:** 2026-03-05T09:24:57.968344Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect GitHub audit logs
Supported in:
Google secops
SIEM
This document explains how to ingest GitHub audit logs to Google Security Operations. You can configure ingestion using one of the following methods:
Google Cloud Storage V2
(recommended): Stream audit logs from GitHub Enterprise Cloud directly to a GCS bucket, then ingest into Google SecOps.
Webhook
: Configure GitHub to push event payloads directly to a Google SecOps webhook endpoint in real time.
GitHub is a cloud-based platform for version control and collaboration that lets developers store and manage code, track changes, and collaborate on software projects. GitHub Enterprise Cloud provides enterprise-grade security features, including audit log streaming for compliance and security monitoring.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
A GitHub Enterprise Cloud account with enterprise owner permissions (for GCS streaming) or organization owner permissions (for webhooks)
For the GCS method, you also need:
A Google Cloud project with Cloud Storage API enabled
Permissions to create and manage GCS buckets
Permissions to create service accounts and manage IAM policies
For the Webhook method, you also need:
Access to Google Cloud Console (for API key creation)
Repository admin or organization owner permissions in GitHub
Option 1: Configure ingestion using Google Cloud Storage V2 (Recommended)
Create Google Cloud Storage bucket
Go to the
Google Cloud Console
.
Select your project or create a new one.
In the navigation menu, go to
Cloud Storage
>
Buckets
.
Click
Create bucket
.
Provide the following configuration details:
Setting
Value
Name your bucket
Enter a globally unique name (for example,
github-audit-logs
)
Location type
Choose based on your needs (Region, Dual-region, Multi-region)
Location
Select the location (for example,
us-central1
)
Storage class
Standard (recommended for frequently accessed logs)
Access control
Uniform (recommended)
Protection tools
Optional: Enable object versioning or retention policy
Click
Create
.
Create a service account for GitHub audit log streaming
GitHub requires a Google Cloud service account with a JSON key to authenticate and write audit logs to your GCS bucket.
In the
Google Cloud Console
, go to
IAM & Admin
>
Service Accounts
.
Click
Create Service Account
.
Provide the following configuration details:
Service account name
: Enter a descriptive name (for example,
github-audit-streaming
)
Service account description
: Enter
Service account for GitHub Enterprise Cloud audit log streaming to GCS
Click
Create and Continue
.
Click
Done
.
Grant the service account write access to the GCS bucket
Go to
Cloud Storage
>
Buckets
.
Click your bucket name (for example,
github-audit-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Enter the service account email (for example,
github-audit-streaming@PROJECT_ID.iam.gserviceaccount.com
)
Assign roles
: Select
Storage Object Creator
Click
Save
.
Create a JSON key for the service account
In the
Google Cloud Console
, go to
IAM & Admin
>
Service Accounts
.
Click the service account (for example,
github-audit-streaming
).
Go to the
Keys
tab.
Click
Add Key
>
Create new key
.
Select
JSON
as the key type.
Click
Create
.
A JSON key file is downloaded to your computer. Save this file securely.
Configure GitHub Enterprise Cloud audit log streaming to GCS
Sign in to
GitHub Enterprise Cloud
as an enterprise owner.
In the top-right corner, click your profile photo, then click
Enterprise settings
(or click
Enterprises
then click the enterprise you want to view).
At the top of the page, click
Settings
.
Under
Settings
, click
Audit log
.
Under
Audit log
, click
Log streaming
.
Select the
Configure stream
drop-down menu and click
Google Cloud Storage
.
Provide the following configuration details:
Bucket
: Enter the name of the GCS bucket (for example,
github-audit-logs
)
JSON Credentials
: Paste the entire contents of the service account JSON key file
Click
Check endpoint
to verify that GitHub can connect and write to the Google Cloud Storage bucket.
After you have successfully verified the endpoint, click
Save
.
Retrieve the Google SecOps service account
Google SecOps uses a unique service account to read data from your GCS bucket. You must grant this service account access to your bucket.
Get the service account email
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
Click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed (for example,
GitHub audit logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
GitHub
as the
Log type
.
Click
Get Service Account
.
A unique service account email will be displayed, for example:
chronicle-12345678@chronicle-gcp-prod.iam.gserviceaccount.com
Copy this email address for use in the next step.
Click
Next
.
Specify values for the following input parameters:
Storage bucket URL
: Enter the GCS bucket URI:
gs://github-audit-logs/
Source deletion option
: Select the deletion option according to your preference:
Never
: Never deletes any files after transfers (recommended for testing).
Delete transferred files
: Deletes files after successful transfer.
Delete transferred files and empty directories
: Deletes files and empty directories after successful transfer.
Maximum File Age
: Include files modified in the last number of days (default is 180 days)
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Grant IAM permissions to the Google SecOps service account
The Google SecOps service account needs
Storage Object Viewer
role on your GCS bucket.
Go to
Cloud Storage
>
Buckets
.
Click the bucket name (
github-audit-logs
).
Go to the
Permissions
tab.
Click
Grant access
.
Provide the following configuration details:
Add principals
: Paste the Google SecOps service account email
Assign roles
: Select
Storage Object Viewer
Click
Save
.
Option 2: Configure ingestion using Webhook
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
GitHub webhook events
).
Select
Webhook
as the
Source type
.
Select
GitHub
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
(optional): Enter
\n
if GitHub sends multiple events per request, or leave empty for single-event payloads
Asset namespace
: The
asset namespace
Ingestion labels
: The label to be applied to the events from this feed
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
Copy and save the secret key securely.
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
Save this URL for the next steps.
Click
Done
.
Create Google Cloud API key
Google SecOps requires an API key for authentication. Create a restricted API key in the Google Cloud Console.
Create the API key
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
Restrict the API key
In the
API key
settings page:
Name
: Enter a descriptive name (for example,
Chronicle Webhook API Key
)
Under
API restrictions
:
Select
Restrict key
.
In the
Select APIs
drop-down, search for and select
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
Construct the webhook URL
Combine the Google SecOps endpoint URL and API key:
<ENDPOINT_URL>?key=<API_KEY>&secret=<SECRET_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...&secret=abcd1234...
Configure GitHub organization webhook
Sign in to
GitHub
and navigate to your organization.
Click
Settings
.
In the left sidebar, click
Webhooks
.
Click
Add webhook
.
Provide the following configuration details:
Payload URL
: Paste the complete webhook URL constructed in the previous step (endpoint URL with API key and secret key appended as query parameters)
Content type
: Select
application/json
Secret
: Leave empty (authentication is handled through the URL parameters)
Under
Which events would you like to trigger this webhook?
:
Select
Let me select individual events
.
Select the events you want to send to Google SecOps. Recommended events for security monitoring include:
Branch or tag creation
Branch or tag deletion
Collaborator add, remove, or changed
Deploy keys
Deployments
Forks
Member
Memberships
Organizations
Pull requests
Pull request reviews
Pushes
Releases
Repositories
Secret scanning alerts
Security advisories
Teams
Visibility changes
Select the
Active
checkbox to enable the webhook.
Click
Add webhook
.
GitHub sends a test
ping
event. Verify the webhook shows a green checkmark indicating successful delivery.
Event types
The following table lists the event types and the conditions for the event types:
event_type
Conditions
NETWORK_CONNECTION
[has_target] == "true" && [has_principal] == "true"
PROCESS_LAUNCH
[has_principal] == "true" && [has_target_process] == "true"
STATUS_UPDATE
[has_principal] == "true"
USER_LOGIN
[raw][message] =~ "Authentication success" or [message] =~ "Authentication success" && ([has_target]== "true"
||
[has_target_user] == "true")
USER_RESOURCE_CREATION
[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in ["personal_access_token.create" ,"repository_vulnerability_alert.create"]
USER_RESOURCE_DELETION
[has_target_resource] == "true" && [has_principal_user] == "true" && [action] in ["hook.destroy" ,"protected_branch.destroy" ,"public_key.delete"]
USER_RESOURCE_DELETION
[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in [ "hook.destroy" ,"protected_branch.destroy" ,"public_key.delete"]
USER_RESOURCE_UPDATE_CONTENT
[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in [ "pull_request.merge" , "hook.events_changed"]
USER_RESOURCE_UPDATE_PERMISSIONS
[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in ["repo.update_actions_secret","protected_branch.update_pull_request_reviews_enforcement_level", "org.update_member" ,"protected_branch.update_admin_enforced" ,"protected_branch.update_required_status_checks_enforcement_level","org.integration_manager_removed" ,"repo.update_member", "repo.add_member"]
USER_UNCATEGORIZED
[has_principal_userid] == "true"
UDM mapping table
Log field
UDM mapping
Remarks
above_lock_quota
additional.fields
above_warn_quota
additional.fields
ac_ms
additional.fields
accept
additional.fields
action
metadata.product_event_type
For JSON logs.
action
security_result.summary
For syslog logs.
active
target.resource.attribute.labels
active_job_id
additional.fields
actor
principal.user.userid
actor_id
principal.user.attribute.labels.value
actor_ip
principal.ip
actor_is_agent
additional.fields
actor_is_bot
principal.user.attribute.labels
actor_location.country_code
principal.location.country_or_region
actor_session
additional.fields
additional_list
additional.fields
additional_string
additional.fields
after
additional.fields
alert_id
security_result.detection_fields
alert_number
security_result.detection_fields
alert_numbers
additional.fields
allow_deletions_enforcement_level
additional.fields
allow_force_pushes_enforcement_level
additional.fields
allow_private_repository_forking
additional.fields
application_name
target.application
aqueduct_job_id
additional.fields
auth_tries
additional.fields
babeld
additional.fields
banner
additional.fields
before
additional.fields
best_cipher
additional.fields
best_kex
additional.fields
best_mac
additional.fields
best_sigtype
additional.fields
Body
security_result.description
branch
target.resource.attribute.labels
branches
target.resource.attribute.labels
business
additional.fields
business_id
additional.fields
cactive
additional.fields
calling_workflow_refs
target.resource.attribute.labels
calling_workflow_shas
target.resource.attribute.labels
changes.body.from
additional.fields
charset
additional.fields
check_run.app
additional.fields
check_run.app.events
additional.fields
check_run.app.owner
additional.fields
check_run.check_suite.app.client_id
additional.fields
check_run.check_suite.app.created_at
additional.fields
check_run.check_suite.app.description
additional.fields
check_run.check_suite.app.events
additional.fields
check_run.check_suite.app.external_url
additional.fields
check_run.check_suite.app.html_url
additional.fields
check_run.check_suite.app.id
additional.fields
check_run.check_suite.app.name
additional.fields
check_run.check_suite.app.node_id
additional.fields
check_run.check_suite.app.slug
additional.fields
check_run.check_suite.app.updated_at
additional.fields
check_run.check_suite.conclusion
additional.fields
check_run.check_suite.id
additional.fields
check_run.check_suite.url
additional.fields
check_run.completed_at
additional.fields
check_run.conclusion
additional.fields
check_run.output
additional.fields
check_run.started_at
additional.fields
check_suite
(all its subfields)
additional.fields
check_suite.app
(all its subfields)
additional.fields
check_suite.app.events
additional.fields
check_suite.app.owner
(all its subfields)
additional.fields
check_suite.head_commit
(all its subfields)
additional.fields
cid
additional.fields
cipher
network.tls.cipher
client_id
principal.user.attribute.labels
cloning
additional.fields
code
additional.fields
CodeNamespace
additional.fields
comment
(all its subfields)
additional.fields
comment.performed_via_github_app
(all its subfields)
additional.fields
comment.performed_via_github_app.events
additional.fields
comment.reactions
(all its subfields)
additional.fields
commit.author
principal.resource.attribute.labels
commit.commit.author.date
additional.fields
commit.commit.author.email
additional.fields
commit.commit.author.name
additional.fields
commit.commit.tree.url
additional.fields
commit.commit.verification
additional.fields
commit.committer
additional.fields
commit.parents
additional.fields
commit.sha
additional.fields
commit.url
additional.fields
commit_oid
additional.fields
committer_date
additional.fields
completed_at
vulns.vulnerabilities.scan_end_time
config.content_typt
target.resource.attribute.labels
config.insecure_ssl
target.resource.attribute.labels
config.secret
target.resource.attribute.labels
config.url
target.url
considers.site.admin
additional.fields
content_type
target.file.mime_type
cr
additional.fields
create_protected
additional.fields
created_at
metadata.event_timestamp
The value is converted from UNIX milliseconds to a timestamp.
credential
detection_fields
ctotal
additional.fields
data._document_id
metadata.product_log_id
data.active_job_id
additional.fields
data.aqueduct_job_id
additional.fields
data.business
target.administrative_domain
data.business_id
additional.fields
data.cancelled_at
extensions.vulns.vulnerabilities.scan_end_time
The value is converted from ISO8601 format to a timestamp.
data.category_type
security_result.category_details
data.dn
additional.fields
data.email
target.user.email_addresses
data.entry_found
additional.fields
data.event
target.resource.attribute.labels
data.events
security_result.about.labels.value
data.head_branch
target.resource.attribute.labels
data.head_sha
target.file.sha256
data.hook_id
target.resource.product_object_id
data.job
target.application
data.operation_type
additional.fields
data.started_at
extensions.vulns.vulnerabilities.scan_start_time
The value is converted from ISO8601 format to a timestamp.
data.team
target.group.group_display_name
data.trigger_id
target.resource.attribute.labels
data.uid
additional.fields
data.workflow_id
target.resource.attribute.labels
data.workflow_run_id
target.resource.attribute.labels
default_new_repo_branch
additional.fields
default_repo_visibility
additional.fields
default_repository_permission
additional.fields
degraded
additional.fields
dependency_scope
additional.fields
deployment.environment
additional.fields
disable_members_can_create_repositories
additional.fields
disable_members_can_delete_repositories
additional.fields
disable_user_org_creation
additional.fields
disk_info
additional.fields
disk_py_file
additional.fields
dismiss_stale_reviews_on_push
additional.fields
dotcom_contributions
additional.fields
dotcom_user_license_usage_upload
additional.fields
duration_ms
additional.fields
ecosystem
additional.fields
enforcement_level
additional.fields
enterprise
principal.resource.attribute.labels
enterprise.name
additional.fields.value.string_value
environment_name
target.resource.attribute.labels
error
additional.fields
external_id
additional.fields
external_identity_nameid
target.user.email_addresses
If the value is an email address, it is added to the
target.user.email_addresses
array.
external_identity_nameid
target.user.userid
external_identity_username
additional.fields
Mapped to
additional.fields
when it is not populated in
target.user.user_display_name
.
external_identity_username
target.user.user_display_name
Mapped when it is populated in
target.user.user_display_name
.
features
additional.fields
filtered
additional.fields
filtered_request_body.query
additional.fields
fluentbit_pod_name
additional.fields
fp_sha256
additional.fields
frontend
additional.fields
frontend_pid
intermediary.process.pid
frontend_ppid
intermediary.process.parent_process.pid
fs_host
target.hostname
fsc_ms
additional.fields
fully_qualified_domain_name
additional.fields
gh.sdk.name
additional.fields
gh.sdk.version
additional.fields
gh.timerd.timer.name
additional.fields
ghsa_id
additional.fields
git.maxobjectsize
additional.fields
git_dir_safe
target.resource.attribute.labels
github_event_after
target.resource.attribute.labels
github_event_before
target.resource.attribute.labels
github_event_compare
target.resource.attribute.labels
github_event_created
target.resource.attribute.labels
github_event_deleted
target.resource.attribute.labels
github_event_forced
target.resource.attribute.labels
github_event_head_commit_author_email
target.resource.attribute.labels
github_event_head_commit_author_name
target.resource.attribute.labels
github_event_head_commit_author_username
target.resource.attribute.labels
github_event_head_commit_committer_email
target.resource.attribute.labels
github_event_head_commit_committer_name
target.resource.attribute.labels
github_event_head_commit_committer_username
target.resource.attribute.labels
github_event_head_commit_distinct
target.resource.attribute.labels
github_event_head_commit_msg1
target.resource.attribute.labels
github_event_head_commit_timestamp
target.resource.attribute.labels
github_event_pusher_email
target.resource.attribute.labels
github_event_pusher_name
target.resource.attribute.labels
github_event_ref
target.resource.attribute.labels
github_event_repository_has_projects
target.resource.attributes.labels
github_event_repository_master_branch
target.resource.attribute.labels
github_event_repository_organization
target.resource.attribute.labels
github_event_repository_owner_name
target.resource.attribute.labels
github_event_repository_stargazers
target.resource.attribute.labels
github_event_workflow_job_completed_at
target.resource.attributes.labels
gpv
additional.fields
handler_code
additional.fields
hashed_token
network.session_id
head_branch
target.resource.attribute.labels
head_sha
target.file.sha256
healthy
additional.fields
hmac
additional.fields
hook_id
target.resource.attribute.labels
host.name
principal.user.attribute.labels
http_version
network.application_protocol_version
id
metadata.product_log_id
ignore_approvals_from_contributors
additional.fields
imode
additional.fields
imperfect
additional.fields
InstrumentationScope
additional.fields
integration_id
additional.fields
intel.flat
additional.fields
is_hosted_runner
target.resource.attribute.labels
issue
(all its subfields)
additional.fields
issue.pull_request
(all its subfields)
additional.fields
job_name
target.resource.attribute.labels.value
job_workflow_ref
target.resource.attribute.labels.value
job_workflow_sha
target.resource.attribute.labels.value
kafka_cluster
additional.fields
kex
additional.fields
keytype
additional.fields
kubernetes.container_image
principal.resource.attribute.labels
kubernetes.container_name
principal.resource.attribute.labels
kubernetes.host
principal.resource.attribute.labels
kubernetes.labels.app
principal.resource.attribute.labels
kubernetes.labels.chart
principal.resource.attribute.labels
kubernetes.labels.component
principal.resource.attribute.labels
kubernetes.labels.heritage
principal.resource.attribute.labels
kubernetes.labels.pod-template-hash
principal.resource.attribute.labels
kubernetes.labels.release
principal.resource.attribute.labels
kubernetes.labels.system
principal.resource.attribute.labels
kubernetes.namespace_name
principal.resource.attribute.labels
kubernetes.pod_ip
principal.ip
,
principal.asset.ip
kubernetes.pod_name
principal.resource.attribute.labels
last_state_change_at
additional.fields
last_state_change_reason
additional.fields
lat
principal.location.region_coordinates.latitude
ldap.debug_logging_enabled
additional.fields
level
security_result.severity
lfs_auth_scope
additional.fields
lfs_deploy_key_header
additional.fields
lfs_verify_reason
additional.fields
linear_history_requirement_enforcement_level
additional.fields
lock_allows_fetch_and_merge
additional.fields
lock_branch_enforcement_level
additional.fields
log_level
security_result.severity
log_source
additional.fields
log_source_file
target.file.full_path
logData.Count
additional.fields
logData.Metrics.*
additional.fields
The star (*) denotes that this includes all subfields.
logType
additional.fields
lon
principal.location.region_coordinates.longitude
loop
additional.fields
matched_policies
security_result.detection_fields
member
target.user.attribute.labels
merge_queue_enforcement_level
additional.fields
method
additional.fields
multi_repo
security_result.detection_fields
mysql_component
additional.fields
mysql_warning_code
additional.fields
name
target.resource.attribute.labels
non_integer_id
additional.fields
ns
additional.fields
number
additional.fields
oauth_application
principal.application
oauth_application_id
principal.resource.attribute.labels
oauth_party
additional.fields
offset
additional.fields
old_permissions
additional.fields
old_repo_permissions
additional.fields
org
target.administrative_domain
org_id
additional.fields.value.string_value
organization.url
additional.fields
original_user_agent
additional.fields
overridden_codes
additional.fields
owner
principal.user.user_display_name
owner_id
principal.user.userid
package
additional.fields
package_name
target.application
parent
additional.fields
parent_installation_id
additional.fields
partition
additional.fields
path_info
additional.fields
This is the mapping when the path is already getting mapped to
target.file.full_path
.
path_info
target.file.full_path
This is the mapping when the path isn't already getting mapped to
target.file.full_path
.
pgroup
additional.fields
pk_ms
additional.fields
prin_ip
principal.ip
,
principal.asset.ip
prin_port
principal.port
prin_usr
principal.user.userid
pro_pid
target.process.pid
probe_fail
additional.fields
probe_ok
additional.fields
programmatic_access_type
additional.fields.value.string_value
pubkey_creator_id
additional.fields
pubkey_creator_login
additional.fields
pubkey_fingerprint
additional.fields
pubkey_id
additional.fields
pubkey_verifier_id
additional.fields
pubkey_verifier_login
additional.fields
public_repo
additional.fields.value.string_value
public_repo
target.location.name
publicly_leaked
security_result.detection_fields
pull_request.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request._links.comments.href
additional.fields
pull_request._links.commits.href
additional.fields
pull_request._links.html.href
additional.fields
pull_request._links.issue.href
additional.fields
pull_request._links.review_comment.href
additional.fields
pull_request._links.review_comments.href
additional.fields
pull_request._links.self.href
additional.fields
pull_request._links.statuses.href
additional.fields
pull_request.base.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.base.repo.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.base.repo.owner.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.head.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.head.owner.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.head.repo.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.head.user.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.requested_reviewers.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.requested_teams.*
additional.fields
The star (*) denotes that this includes all subfields.
pull_request.user.
(and all its subfields except
login
)
principal.user.attribute.labels
pull_request.user.login
principal.user.user_display_name
pull_request_id
target.resource.attribute.labels
pull_request_title
target.resource.attribute.labels
query_string
additional.fields.value.string_value
queue_duration
additional.fields
quotas_enabled
additional.fields
rate_limit
additional.fields
rate_limit_family
additional.fields
rate_limit_key
additional.fields
rate_limit_remaining
additional.fields.value.string_value
rate_limit_reset
additional.fields
rate_limit_used
additional.fields
raw.at
additional.fields
raw.hashed_token
network.session_id
raw.token_type
additional.fields
raw.url
target.url
raw.user_agent
network.http.user_agent
,
network.http.parsed_user_agent
raw_login
additional.fields
read_only
additional.fields
readonly
additional.fields
reasons
additional.fields
ref
target.resource.attribute.labels
replicas
additional.fields
repo
target.resource.name
repo_id
additional.fields.value.string_value
repo_owner_login
target.resource.attribute.labels
repo_owner_type
target.resource.attribute.labels
repo_public
additional.fields
repository
target.resource.attribute.labels
repository.archive_url
target.resource.attribute.labels
repository.assignees_url
target.resource.attribute.labels
repository.blobs_url
target.resource.attribute.labels
repository.branches_url
target.resource.attribute.labels
repository.clone_url
target.resource.attribute.labels
repository.collaborators_url
target.resource.attribute.labels
repository.comments_url
target.resource.attribute.labels
repository.commits_url
target.resource.attribute.labels
repository.compare_url
target.resource.attribute.labels
repository.contents_url
target.resource.attribute.labels
repository.contributors_url
target.resource.attribute.labels
repository.created_at
target.resource.attribute.labels
repository.custom_properties.
(and all its subfields)
target.resource.attribute.labels
repository.deployments_url
target.resource.attribute.labels
repository.downloads_url
target.resource.attribute.labels
repository.events_url
target.resource.attribute.labels
repository.fork
target.resource.attribute.labels
repository.forks_url
target.resource.attribute.labels
repository.full_name
target.resource.attribute.labels
repository.git_commits_url
target.resource.attribute.labels
repository.git_refs_url
target.resource.attribute.labels
repository.git_tags_url
target.resource.attribute.labels
repository.git_url
target.resource.attribute.labels
repository.homepage
target.resource.attributes.labels
repository.hooks_url
target.resource.attribute.labels
repository.html_url
target.resource.attribute.labels
repository.id
target.resource.attribute.labels
repository.issue_comment_url
target.resource.attribute.labels
repository.issue_events_url
target.resource.attribute.labels
repository.issues_url
target.resource.attribute.labels
repository.keys_url
target.resource.attribute.labels
repository.labels_url
target.resource.attribute.labels
repository.languages_url
target.resource.attribute.labels
repository.license
target.resource.attributes.labels
repository.merges_url
target.resource.attribute.labels
repository.milestones_url
target.resource.attribute.labels
repository.mirror_url
target.resource.attributes.labels
repository.name
target.resource.attribute.labels
repository.node_id
target.resource.attribute.labels
repository.notifications_url
target.resource.attribute.labels
repository.open_issues_count
target.resource.attribute.labels
repository.owner.avatar_url
target.resource.attribute.labels
repository.owner.events_url
target.resource.attribute.labels
repository.owner.followers_url
target.resource.attribute.labels
repository.owner.following_url
target.resource.attribute.labels
repository.owner.gists_url
target.resource.attribute.labels
repository.owner.gravatar_id
target.resource.attribute.labels
repository.owner.html_url
target.resource.attribute.labels
repository.owner.id
target.resource.attribute.labels
repository.owner.node_id
target.resource.attribute.labels
repository.owner.organizations_url
target.resource.attribute.labels
repository.owner.received_events_url
target.resource.attribute.labels
repository.owner.repos_url
target.resource.attribute.labels
repository.owner.site_admin
target.resource.attribute.labels
repository.owner.starred_url
target.resource.attribute.labels
repository.owner.subscriptions_url
target.resource.attribute.labels
repository.owner.type
target.resource.attribute.labels
repository.owner.url
target.resource.attribute.labels
repository.owner.user_view_type
target.resource.attribute.labels
repository.private
target.resource.attribute.labels
repository.pulls_url
target.resource.attribute.labels
repository.pushed_at
target.resource.attribute.labels
repository.releases_url
target.resource.attribute.labels
repository.size
target.resource.attribute.labels
repository.ssh_url
target.resource.attribute.labels
repository.stargazers_url
target.resource.attribute.labels
repository.statuses_url
target.resource.attribute.labels
repository.subscribers_url
target.resource.attribute.labels
repository.subscription_url
target.resource.attribute.labels
repository.svn_url
target.resource.attribute.labels
repository.tags_url
target.resource.attribute.labels
repository.teams_url
target.resource.attribute.labels
repository.topics
target.resource.attributes.labels
repository.trees_url
target.resource.attribute.labels
repository.updated_at
target.resource.attribute.labels
repository.url
target.resource.attribute.labels
repository.visibility
target.resource.attribute.labels
repository_public
target.resource.attribute.labels
req_content_type
target.file.mime_type
request_access_security_header
security_result.detection_fields
request_auth
additional.fields
request_body
additional.fields.value.string_value
request_duration
additional.fields
request_host
principal.ip
,
principal.asset.ip
When an IP address is present, the mapping is to
principal.ip
(keeping the existing mapping of
principal.hostname
).
request_method
network.http.method
The value is converted to uppercase.
requested_reviewers.*
additional.fields
The star (*) denotes that this includes all subfields.
require_code_owner_review
additional.fields
require_last_push_approval
additional.fields
required_approving_review_count
additional.fields
required_deployments_enforcement_level
additional.fields
required_review_thread_resolution_enforcement_level
additional.fields
rerun_type
additional.fields
res_type
target.resource.resource_subtype
response_time
additional.fields
review_id
target.resource.attributes.labels
route
additional.fields.value.string_value
rpc.jsonrpc.error_code
network.http.response_code
rpc.jsonrpc.error_message
security_result.summary
rule_suite_id
security_result.rule_id
run_attempt
additional.fields
run_number
additional.fields
runner_labels
target.resource.attribute.labels
runner_owner_type
target.resource.attribute.labels
runner_tenant_id
target.resource.attribute.labels
s3_tag
additional.fields
secret_type
security_result.detection_fields
secret_types
security_result.detection_fields
secrets_passed
security_result.detection_fields
sender.id
src.user.product_object_id
sender.login
src.user.user_display_name
sender.node_id
src.asset_id
sender.type
src.user.title
sender.url
src.url
service
target.resource.name
service.version
additional.fields
serviceName
target.resource.name
severity
(if high)
security_result.severity
SeverityText
security_result.severity
shallow
additional.fields
sign_in_verification_method
security_result.detection_fields
signature_requirement_enforcement_level
additional.fields
sigtype
additional.fields
source
src.resource.name
spec
additional.fields
sr
additional.fields
ss
additional.fields
started_at
vulns.vulnerabilities.scan_start_time
stateless
additional.fields
status_code
network.http.response_code
strict_required_status_checks_policy
additional.fields
subject.business.id
target.resource.attribute.labels
subject.owner.id
additional.fields
subject.owning_organization.id
principal.group.product_object_id
subject.repository.id
target.resource.product_object_id
subject.repository.internal
target.resource.attribute.labels
subject.repository.owner.id
additional.fields
subject.repository.public
target.resource.attribute.labels
subject.repository.writable
target.resource.attribute.labels
subject.type
target.resource.attribute.labels
synthetic_status
additional.fields
tar_application
target.application
telemetry.sdk.name
additional.fields
tenant_id
target.resource.attribute.labels
tid
additional.fields
time
metadata.event_timestamp
time_duration_ms
additional.fields
time_zone
additional.fields
timestamp
metadata.event_timestamp
tls_version
network.tls.version
token_id
additional.fields.value.string_value
token_scopes
additional.fields.value.string_value
topic
additional.fields
total
additional.fields
transport_protocol
additional.fields
transport_protocol_name
network.application_protocol
The value is converted to uppercase.
ts
metadata.event_timestamp
When
process_type
is
github_production
.
TTY
additional.fields
twirp_method
additional.fields
twirp_package
additional.fields
twirp_service
additional.fields
twirp_status
network.http.response_code
two_factor_type
security_result.detection_fields
type
additional.fields
unavailable
additional.fields
updated_at
metadata.collected_timestamp
url_path
target.url
usage_metrics
additional.fields
user
target.user.userid
user.id
target.user.attr.labels
When
actor.id
is present.
user.id
target.user.userid
When
actor.id
isn't present.
user_agent
network.http.parsed_user_agent
The value is parsed.
user_agent
network.http.user_agent
user_id
target.user.userid
user_operator_mode
additional.fields
user_programmatic_access_id
additional.fields
user_renaming_enabled
additional.fields
user_spammy
additional.fields
version
metadata.product_version
This mapping includes JSON logs.
visibility
additional.fields
vk_ms
additional.fields
vulnerability_id
additional.fields
vulnerable_version_range_id
additional.fields
workflow
target.resource.attributes.labels
workflow.name
target.resource.attribute.labels
workflow_id
target.resource.attribute.labels
workflow_job.head_branch
security_result.detection_fields
workflow_job.name
target.resource.attributes.labels
workflow_job.workflow_name
security_result.detection_fields
workflow_run.actor.
(and all its subfields except for the
login
field, included in every subfield)
principal.user.attribute.labels
workflow_run.actor.login
principal.user.userid
workflow_run.artifacts_url
target.resource.attributes.labels
workflow_run.cancel_url
target.resource.attributes.labels
workflow_run.check_suite_id
additional.fields
workflow_run.check_suite_node_id
additional.fields
workflow_run.check_suite_url
target.resource.attributes.labels
workflow_run.conclusion
target.resource.attribute.labels
workflow_run.created_at
metadata.event_timestamp
workflow_run.display_title
target.resource.attribute.labels
workflow_run.event
additional.fields.value.string_value
workflow_run.event
target.resource.attribute.labels
workflow_run.head_branch
target.resource.attribute.labels
workflow_run.head_commit
target.resource.attributes.labels
workflow_run.head_repository
additional.fields
workflow_run.head_sha
target.file.sha256
workflow_run.html_url
target.resource.attribute.labels
workflow_run.id
target.resource.attribute.labels.value
workflow_run.jobs_url
target.resource.attributes.labels
workflow_run.logs_url
target.resource.attributes.labels
workflow_run.name
target.resource.name
workflow_run.node_id
target.resource.product_object_id
workflow_run.path
target.resource.attribute.labels
workflow_run.previous_attempt_url
target.resource.attributes.labels
workflow_run.pull_requests
about.resource.attribute.labels
workflow_run.repository
additional.fields
workflow_run.rerun_url
target.resource.attributes.labels
workflow_run.run_attempt
target.resource.attribute.labels
workflow_run.run_number
target.resource.attribute.labels
workflow_run.run_started_at
target.resource.attribute.labels
workflow_run.status
security_result.description
workflow_run.triggering_actor
additional.fields
workflow_run.updated_at
metadata.collected_timestamp
workflow_run.url
target.url
workflow_run.workflow_id
security_result.about.labels.value
workflow_run.workflow_id
target.resource.attribute.labels
workflow_run.workflow_url
target.resource.attributes.labels
Release deltas reference
On January 8, 2026, Google SecOps released a new version of the GitHub parser, which includes significant changes.
Log-field mapping delta
The following table lists the mapping delta for GitHub log-to-UDM fields exposed prior to January 8, 2026 and subsequently (listed in the
Old mapping
and
Current mapping
columns respectively):
Log field
Old mapping
Current mapping
action
(for JSON logs)
metadata.product_event_type, security_result.summary,security_result.detection_fields
metadata.product_event_type
action
(for syslog logs)
additional.fields, security_result.summary
security_result.summary
business
additional.fields, target.user.company_name
additional.fields
business_id
target.resource.attribute.labels
additional.fields
data.email
target.email
target.user.email_addresses
data.event
security_result.about.labels
target.resource.attribute.labels
data.head_branch
security_result.about.labels
target.resource.attribute.labels
data.hook_id
target.resource.attribute.labels
target.resource.product_object_id
data.team
target.user.group_identifiers
target.group.group_display_name
data.trigger_id
security_result.about.labels
target.resource.attribute.labels
data.workflow_id
security_result.about.labels
target.resource.attribute.labels
data.workflow_run_id
security_result.about.labels
target.resource.attribute.labels
hashed_token
additional.fields
network.session_id
hook_id
(for JSON logs)
additional.fields
target.resource.attribute.labels
name
additional.fields
target.resource.attribute.labels
oauth_application_id
additional.fields
principal.resource.attribute.labels
pull_request_id
additional.fields
target.resource.attribute.labels
pull_request_title
additional.fields
target.resource.attribute.labels
repository.archive_url
additional.fields
target.resource.attribute.labels
repository.assignees_url
additional.fields
target.resource.attribute.labels
repository.blobs_url
additional.fields
target.resource.attribute.labels
repository.branches_url
additional.fields
target.resource.attribute.labels
repository.clone_url
additional.fields
target.resource.attribute.labels
repository.collaborators_url
additional.fields
target.resource.attribute.labels
repository.comments_url
additional.fields
target.resource.attribute.labels
repository.commits_url
additional.fields
target.resource.attribute.labels
repository.compare_url
additional.fields
target.resource.attribute.labels
repository.contents_url
additional.fields
target.resource.attribute.labels
repository.contributors_url
additional.fields
target.resource.attribute.labels
repository.created_at
additional.fields
target.resource.attribute.labels
repository.deployments_url
additional.fields
target.resource.attribute.labels
repository.downloads_url
additional.fields
target.resource.attribute.labels
repository.events_url
additional.fields
target.resource.attribute.labels
repository.fork
additional.fields
target.resource.attribute.labels
repository.forks_url
additional.fields
target.resource.attribute.labels
repository.full_name
additional.fields
target.resource.attribute.labels
repository.git_commits_url
additional.fields
target.resource.attribute.labels
repository.git_refs_url
additional.fields
target.resource.attribute.labels
repository.git_tags_url
additional.fields
target.resource.attribute.labels
repository.git_url
additional.fields
target.resource.attribute.labels
repository.hooks_url
additional.fields
target.resource.attribute.labels
repository.html_url
additional.fields
target.resource.attribute.labels
repository.id
additional
target.resource.attribute.labels
repository.issue_comment_url
additional.fields
target.resource.attribute.labels
repository.issue_events_url
additional.fields
target.resource.attribute.labels
repository.issues_url
additional.fields
target.resource.attribute.labels
repository.keys_url
additional.fields
target.resource.attribute.labels
repository.labels_url
additional.fields
target.resource.attribute.labels
repository.languages_url
additional.fields
target.resource.attribute.labels
repository.merges_url
additional.fields
target.resource.attribute.labels
repository.milestones_url
additional.fields
target.resource.attribute.labels
repository.name
additional.fields
target.resource.attribute.labels
repository.node_id
additional.fields
target.resource.attribute.labels
repository.notifications_url
additional.fields
target.resource.attribute.labels
repository.owner.avatar_url
additional.fields
target.resource.attribute.labels
repository.owner.events_url
additional.fields
target.resource.attribute.labels
repository.owner.followers_url
additional.fields
target.resource.attribute.labels
repository.owner.following_url
additional.fields
target.resource.attribute.labels
repository.owner.gists_url
additional.fields
target.resource.attribute.labels
repository.owner.gravatar_id
additional.fields
target.resource.attribute.labels
repository.owner.html_url
additional.fields
target.resource.attribute.labels
repository.owner.id
additional.fields
target.resource.attribute.labels
repository.owner.node_id
additional.fields
target.resource.attribute.labels
repository.owner.organizations_url
additional.fields
target.resource.attribute.labels
repository.owner.received_events_url
additional.fields
target.resource.attribute.labels
repository.owner.repos_url
additional.fields
target.resource.attribute.labels
repository.owner.site_admin
additional.fields
target.resource.attribute.labels
repository.owner.starred_url
additional.fields
target.resource.attribute.labels
repository.owner.subscriptions_url
additional.fields
target.resource.attribute.labels
repository.owner.type
additional.fields
target.resource.attribute.labels
repository.owner.url
additional.fields
target.resource.attribute.labels
repository.owner.user_view_type
additional.fields
target.resource.attribute.labels
repository.private
additional.fields
target.resource.attribute.labels
repository.pulls_url
additional.fields
target.resource.attribute.labels
repository.pushed_at
additional.fields
target.resource.attribute.labels
repository.releases_url
additional.fields
target.resource.attribute.labels
repository.size
additional.fields
target.resource.attribute.labels
repository.ssh_url
additional.fields
target.resource.attribute.labels
repository.stargazers_url
additional.fields
target.resource.attribute.labels
repository.statuses_url
additional.fields
target.resource.attribute.labels
repository.subscribers_url
additional.fields
target.resource.attribute.labels
repository.subscription_url
additional.fields
target.resource.attribute.labels
repository.svn_url
additional.fields
target.resource.attribute.labels
repository.tags_url
additional.fields
target.resource.attribute.labels
repository.teams_url
additional.fields
target.resource.attribute.labels
repository.trees_url
additional.fields
target.resource.attribute.labels
repository.updated_at
additional.fields
target.resource.attribute.labels
repository.url
additional.fields
target.resource.attribute.labels
repository.visibility
additional.fields
target.resource.attribute.labels
repository_public
additional.fields
target.resource.attribute.labels
res_type
target.resource.type
target.resource.resource_subtype
sender.id
src.user.product_object_id, additional.fields
src.user.product_object_id
sender.login
additional.fields, src.user.user_display_name
src.user.user_display_name
sender.node_id
src.asset_id, additional.fields
src.asset_id
sender.type
src.user.title, additional.fields
src.user.title
sender.url
src.url, additional.fields
src.url
workflow.name
security_result.about.labels
target.resource.attribute.labels
workflow_job.head_branch
security_result.about.labels
security_result.detection_fields
workflow_job.workflow_name
security_result.about.labels
security_result.detection_fields
workflow_run.event
additional.fields
target.resource.attribute.labels
workflow_run.head_branch
security_result.about.labels
target.resource.attribute.labels
workflow_run.workflow_id
security_result.about.labels
target.resource.attribute.labels
Event-type conditions delta
The conditions that determine Google SecOps event types were changed in the January 8, 2026 release.
The following table lists the event types and the current conditions (that is, the conditions were different prior to the January 8, 2026 release):
event_type
Conditions
NETWORK_CONNECTION
[has_target] == "true" && [has_principal] == "true"
STATUS_UPDATE
[has_principal] == "true"
USER_RESOURCE_DELETION
[has_target_resource] == "true" && [has_principal_user] == "true" && [action] in ["hook.destroy" ,"protected_branch.destroy" ,"public_key.delete"]
USER_RESOURCE_UPDATE_CONTENT
[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in [ "pull_request.merge" , "hook.events_changed"]
USER_RESOURCE_UPDATE_PERMISSIONS
[has_target_resource] == "true" && [has_principal_userid] == "true" && [action] in ["repo.update_actions_secret","protected_branch.update_pull_request_reviews_enforcement_level", "org.update_member" ,"protected_branch.update_admin_enforced" ,"protected_branch.update_required_status_checks_enforcement_level","org.integration_manager_removed" ,"repo.update_member", "repo.add_member"]
Key mapping delta
The following table lists the mapping delta for keys in raw-log fields to keys in UDM fields exposed prior to January 8, 2026 and subsequently (listed in the
Old key
and
Current key
columns respectively):
Key in raw log
Old key
Current key
alert.secret_type_display_name
secret_type_display_name
alert_secret_type_display_name
enterprise.name
Enterprise Name
enterprise_name
hook_id
Hook Id
Hook_Id
invitation.failed_at
failed_at
invitation_failed_at
invitation.failed_reason
failed_reason
invitation_failed_reason
invitation.invitation_source
invitation_source
invitation_invitation_source
raw.failure_reason
failure_reason
raw_failure_reason
raw.failure_type
failure_type
raw_failure_type
raw.from
from
raw_from
workflow_run.event
event
workflow_run_event
workflow_run.head_branch
Head Branch
Head_Branch
workflow_run.id
workflow_run_id
workflow_Run_id
workflow_run.workflow_id
Workflow Id
Workflow_Id
Need more help?
Get answers from Community members and Google SecOps professionals.
