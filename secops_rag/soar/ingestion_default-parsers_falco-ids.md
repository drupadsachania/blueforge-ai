# Collect Falco IDS logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/falco-ids/  
**Scraped:** 2026-03-05T09:55:36.847299Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Falco IDS logs
Supported in:
Google secops
SIEM
This document explains how to configure Falco to push runtime security alerts to Google Security Operations using webhooks via Falcosidekick.
Falco is an open-source runtime security tool that detects unexpected application behavior and alerts on threats at runtime. It uses system call monitoring to detect anomalous activity in containers, Kubernetes, and Linux hosts based on customizable security rules.
Before you begin
Make sure that you have the following prerequisites:
A Google SecOps instance
Falco installed on Kubernetes (via Helm) or Linux hosts
Access to modify Falco configuration files or Helm values
Privileged access to deploy Falcosidekick (if not already deployed)
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
Falco Runtime Security
).
Select
Webhook
as the
Source type
.
Select
Falco IDS
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Split delimiter
(optional): Leave empty (Falcosidekick sends one event per request)
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
. An API key is created and displayed in a dialog.
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
list, search for and select
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
Deploy Falcosidekick
Falcosidekick is the official proxy forwarder for Falco that routes alerts to multiple destinations including webhooks, cloud storage, and SIEM platforms.
Option A: Deploy with Falco using Helm (Recommended)
If you are installing Falco for the first time or can redeploy it, use this method to deploy both Falco and Falcosidekick together:
Add the Falco Helm repository:
helm
repo
add
falcosecurity
https://falcosecurity.github.io/charts
helm
repo
update
Create a namespace for Falco:
kubectl
create
namespace
falco
Construct the Google SecOps webhook URL with authentication:
<ENDPOINT_URL>?key=<API_KEY>
Example:
https://malachiteingestion-pa.googleapis.com/v2/unstructuredlogentries:batchCreate?key=AIzaSyD...
Install Falco with Falcosidekick enabled:
helm
install
falco
falcosecurity/falco
\
--namespace
falco
\
--set
falcosidekick.enabled
=
true
\
--set
falcosidekick.config.webhook.address
=
"<ENDPOINT_URL>?key=<API_KEY>"
\
--set
falcosidekick.config.webhook.customHeaders
=
"x-chronicle-auth:<SECRET_KEY>"
\
--set
falcosidekick.config.webhook.minimumpriority
=
"warning"
\
--set
tty
=
true
Replace:
<ENDPOINT_URL>
: Google SecOps feed endpoint URL
<API_KEY>
: Google Cloud API key
<SECRET_KEY>
: Google SecOps secret key from feed creation
Verify the deployment:
kubectl
get
pods
-n
falco
Expected output shows both Falco and Falcosidekick pods running:
NAME                            READY   STATUS    RESTARTS   AGE
falco-xxxxx                     2/2     Running   0          2m
falco-falcosidekick-xxxxx       1/1     Running   0          2m
Option B: Deploy Falcosidekick standalone
If Falco is already deployed, you can deploy Falcosidekick separately and configure Falco to send alerts to it.
Deploy Falcosidekick
Add the Falco Helm repository (if not already added):
helm
repo
add
falcosecurity
https://falcosecurity.github.io/charts
helm
repo
update
Construct the Google SecOps webhook URL with authentication:
<ENDPOINT_URL>?key=<API_KEY>
Install Falcosidekick:
helm
install
falcosidekick
falcosecurity/falcosidekick
\
--namespace
falco
\
--set
config.webhook.address
=
"<ENDPOINT_URL>?key=<API_KEY>"
\
--set
config.webhook.customHeaders
=
"x-chronicle-auth:<SECRET_KEY>"
\
--set
config.webhook.minimumpriority
=
"warning"
Replace:
<ENDPOINT_URL>
: Google SecOps feed endpoint URL
<API_KEY>
: Google Cloud API key
<SECRET_KEY>
: Google SecOps secret key from feed creation
Verify Falcosidekick is running:
kubectl
get
pods
-n
falco
-l
app.kubernetes.io/name
=
falcosidekick
Configure Falco to send alerts to Falcosidekick
Get the Falcosidekick service name:
kubectl
get
svc
-n
falco
-l
app.kubernetes.io/name
=
falcosidekick
The service name is typically
falcosidekick
.
Update Falco configuration to enable HTTP output:
If using Helm, upgrade the Falco release:
helm
upgrade
falco
falcosecurity/falco
\
--namespace
falco
\
--reuse-values
\
--set
falco.json_output
=
true
\
--set
falco.json_include_output_property
=
true
\
--set
falco.http_output.enabled
=
true
\
--set
falco.http_output.url
=
"http://falcosidekick:2801/"
If managing Falco configuration manually, edit
/etc/falco/falco.yaml
:
json_output
:
true
json_include_output_property
:
true
http_output
:
enabled
:
true
url
:
"http://falcosidekick:2801/"
Restart Falco pods to apply the configuration:
kubectl
rollout
restart
daemonset/falco
-n
falco
Configure Falcosidekick on Linux hosts
If running Falco on Linux hosts (not Kubernetes), deploy Falcosidekick as a systemd service.
Install Falcosidekick binary
Download the latest Falcosidekick release:
FALCOSIDEKICK_VERSION
=
"2.29.0"
wget
https://github.com/falcosecurity/falcosidekick/releases/download/
${
FALCOSIDEKICK_VERSION
}
/falcosidekick_
${
FALCOSIDEKICK_VERSION
}
_linux_amd64.tar.gz
Extract and install the binary:
sudo
tar
-C
/usr/local/bin/
-xzf
falcosidekick_
${
FALCOSIDEKICK_VERSION
}
_linux_amd64.tar.gz
sudo
chmod
+x
/usr/local/bin/falcosidekick
Create configuration directory:
sudo
mkdir
-p
/etc/falcosidekick
Configure Falcosidekick
Create the configuration file
/etc/falcosidekick/config.yaml
:
listenaddress
:
"0.0.0.0"
listenport
:
2801
debug
:
false
webhook
:
address
:
"<ENDPOINT_URL>?key=<API_KEY>"
method
:
"POST"
customHeaders
:
"x-chronicle-auth:<SECRET_KEY>"
minimumpriority
:
"warning"
checkcert
:
true
Replace:
<ENDPOINT_URL>
: Google SecOps feed endpoint URL
<API_KEY>
: Google Cloud API key
<SECRET_KEY>
: Google SecOps secret key from feed creation
Create a systemd service file
/etc/systemd/system/falcosidekick.service
:
[Unit]
Description
=
Falcosidekick
After
=
network.target
[Service]
Type
=
simple
User
=
root
ExecStart
=
/usr/local/bin/falcosidekick --config-file=/etc/falcosidekick/config.yaml
Restart
=
on-failure
RestartSec
=
5s
[Install]
WantedBy
=
multi-user.target
Enable and start Falcosidekick:
sudo
systemctl
daemon-reload
sudo
systemctl
enable
falcosidekick
sudo
systemctl
start
falcosidekick
Verify Falcosidekick is running:
sudo
systemctl
status
falcosidekick
Configure Falco to send alerts to Falcosidekick
Edit the Falco configuration file
/etc/falco/falco.yaml
:
json_output
:
true
json_include_output_property
:
true
http_output
:
enabled
:
true
url
:
"http://localhost:2801/"
Restart Falco:
sudo
systemctl
restart
falco
Verify integration
Trigger a test alert
Trigger a Falco rule by executing a shell in a container (if using Kubernetes):
kubectl
run
test-pod
--image
=
nginx
--restart
=
Never
kubectl
exec
-it
test-pod
--
/bin/bash
This triggers the Falco rule "Terminal shell in container".
For Linux hosts, trigger a rule by reading sensitive files:
cat
/etc/shadow
This triggers the Falco rule "Read sensitive file untrusted".
Check Falcosidekick logs
For Kubernetes deployments:
kubectl
logs
-n
falco
-l
app.kubernetes.io/name
=
falcosidekick
--tail
=
50
Look for log entries indicating successful webhook delivery:
2025-01-15T10:30:00Z [INFO] : Webhook - Post OK
For Linux hosts:
sudo
journalctl
-u
falcosidekick
-n
50
Verify events in Google SecOps
Go to
Google SecOps
>
Search
.
Run a search query:
metadata.log_type = "FALCO_IDS"
Verify that Falco events appear in the search results.
Check that events contain expected fields such as:
rule
- Falco rule name
priority
- Alert priority (Emergency, Alert, Critical, Error, Warning, Notice, Informational, Debug)
output
- Human-readable alert message
source
- Event source (syscall, k8s_audit)
hostname
- Host where event occurred
container_id
- Container ID (if applicable)
Priority filtering
Falcosidekick supports filtering events by priority to reduce noise and focus on critical alerts.
לֹ
Priority levels
Falco uses the following priority levels (from highest to lowest):
Priority
Description
Use case
Emergency
System is unusable
Critical security incidents
Alert
Action must be taken immediately
Active attacks, privilege escalation
Critical
Critical conditions
Unauthorized access, malware execution
Error
Error conditions
Policy violations, suspicious activity
Warning
Warning conditions
Anomalous behavior, potential threats
Notice
Normal but significant
Configuration changes, audit events
Informational
Informational messages
General activity logging
Debug
Debug-level messages
Troubleshooting, development
Configure minimum priority
To send only high-priority alerts to Google SecOps, set the
minimumpriority
parameter:
For Helm deployments:
helm
upgrade
falco
falcosecurity/falco
\
--namespace
falco
\
--reuse-values
\
--set
falcosidekick.config.webhook.minimumpriority
=
"error"
For Linux hosts
, edit
/etc/falcosidekick/config.yaml
:
webhook
:
minimumpriority
:
"error"
This configuration sends only events with priority
error
or higher (Error, Critical, Alert, Emergency) to Google SecOps.
Custom fields
Falcosidekick allows adding custom fields to all events for better context and filtering in Google SecOps.
Add custom fields
For Helm deployments:
helm
upgrade
falco
falcosecurity/falco
\
--namespace
falco
\
--reuse-values
\
--set
falcosidekick.config.customfields.environment
=
"production"
\
--set
falcosidekick.config.customfields.region
=
"us-east-1"
\
--set
falcosidekick.config.customfields.cluster
=
"prod-cluster-01"
For Linux hosts
, edit
/etc/falcosidekick/config.yaml
:
customfields
:
environment
:
"production"
region
:
"us-east-1"
datacenter
:
"dc1"
These custom fields are added to every Falco event sent to Google SecOps, enabling filtering and correlation across multiple environments.
Alternative ingestion paths
While webhook is the recommended method, Falcosidekick supports alternative ingestion paths for specific use cases.
AWS S3 ingestion
For high-volume environments or compliance requirements, you can configure Falcosidekick to write events to AWS S3, then ingest from S3 to Google SecOps.
Configure Falcosidekick for S3:
helm
upgrade
falco
falcosecurity/falco
\
--namespace
falco
\
--reuse-values
\
--set
falcosidekick.config.aws.accesskeyid
=
"<AWS_ACCESS_KEY>"
\
--set
falcosidekick.config.aws.secretaccesskey
=
"<AWS_SECRET_KEY>"
\
--set
falcosidekick.config.aws.region
=
"us-east-1"
\
--set
falcosidekick.config.aws.s3.bucket
=
"falco-events"
\
--set
falcosidekick.config.aws.s3.prefix
=
"runtime-security/"
Falcosidekick writes events to S3 in JSON format with the path structure:
s3://falco-events/runtime-security/YYYY-MM-DD/YYYY-MM-DDTHH:mm:ss.s+01:00.json
Then configure a Google SecOps feed with
Amazon S3 V2
as the source type.
GCP Cloud Storage ingestion
For GCP environments, configure Falcosidekick to write events to Google Cloud Storage.
Configure Falcosidekick for GCS:
Create a GCP service account with
Storage Object Admin
role on the target bucket.
Download the service account JSON key file.
Base64-encode the JSON key:
cat
service-account-key.json
|
base64
-w
0
Configure Falcosidekick:
helm
upgrade
falco
falcosecurity/falco
\
--namespace
falco
\
--reuse-values
\
--set
falcosidekick.config.gcp.credentials
=
"<BASE64_ENCODED_KEY>"
\
--set
falcosidekick.config.gcp.storage.bucket
=
"falco-events"
\
--set
falcosidekick.config.gcp.storage.prefix
=
"runtime-security/"
Falcosidekick writes events to GCS with the path structure:
gs://falco-events/runtime-security/YYYY-MM-DD/YYYY-MM-DDTHH:mm:ss.s+01:00.json
Then configure a Google SecOps feed with
Google Cloud Storage V2
as the source type.
AWS Kinesis Firehose ingestion
For real-time streaming ingestion, configure Falcosidekick to send events to AWS Kinesis Firehose.
Configure Falcosidekick for Kinesis:
helm
upgrade
falco
falcosecurity/falco
\
--namespace
falco
\
--reuse-values
\
--set
falcosidekick.config.aws.accesskeyid
=
"<AWS_ACCESS_KEY>"
\
--set
falcosidekick.config.aws.secretaccesskey
=
"<AWS_SECRET_KEY>"
\
--set
falcosidekick.config.aws.region
=
"us-east-1"
\
--set
falcosidekick.config.aws.kinesis.streamname
=
"falco-events-stream"
Then configure a Google SecOps feed with
Amazon Kinesis Firehose
as the source type.
Troubleshooting
Falcosidekick not receiving events
Check Falco is sending events to Falcosidekick:
kubectl
logs
-n
falco
-l
app.kubernetes.io/name
=
falco
--tail
=
50
|
grep
http_output
Verify Falco configuration includes HTTP output:
kubectl
get
configmap
-n
falco
falco
-o
yaml
|
grep
-A
5
http_output
Check Falcosidekick is listening on port 2801:
kubectl
get
svc
-n
falco
falcosidekick
Webhook delivery failures
Check Falcosidekick logs for HTTP errors:
kubectl
logs
-n
falco
-l
app.kubernetes.io/name
=
falcosidekick
--tail
=
100
|
grep
-i
error
Common errors:
401 Unauthorized
: Incorrect API key or secret key
403 Forbidden
: API key not authorized for Google SecOps API
SSL certificate errors
: Set
checkcert: false
for testing (not recommended for production)
Test webhook manually:
curl
-X
POST
\
-H
"Content-Type: application/json"
\
-H
"x-chronicle-auth: <SECRET_KEY>"
\
-d
'{"test": "event"}'
\
"<ENDPOINT_URL>?key=<API_KEY>"
Events not appearing in Google SecOps
Verify the feed is active:
Go to
SIEM Settings
>
Feeds
.
Check feed status is
Active
.
Check
Last Ingestion Time
is recent.
Check for ingestion errors:
Go to the feed details page.
Click the
Errors
tab.
Review any parsing or validation errors.
Verify log type mapping:
Search for raw logs:
metadata.log_type = "FALCO_IDS"
.
If events appear but fields are not parsed, check UDM mapping.
UDM mapping table
Log field
UDM mapping
Logic
output_fields.k8s.ns.name, output_fields.k8s.pod.name
additional.fields
Merged from k8_ns_name and k8s_pod_name objects
stageTimestamp
metadata.collected_timestamp
Converted using ISO8601 format
stage, description, output
metadata.description
Value from stage if not empty, else description, else output
verb, user.uid, uid, output
metadata.event_type
Set to USER_RESOURCE_ACCESS if verb in GET LIST WATCH; USER_RESOURCE_CREATION if CREATE and (user.uid or uid not empty); USER_RESOURCE_UPDATE_CONTENT if (PATCH or UPDATE) and user.uid not empty; USER_RESOURCE_DELETION if DELETE; or USER_RESOURCE_ACCESS if output contains Error, else USER_UNCATEGORIZED; else GENERIC_EVENT
kind
metadata.product_event_type
Value copied directly
auditID
metadata.product_log_id
Value copied directly
apiVersion, product_version
metadata.product_version
Value from apiVersion if not empty, else product_version (after removing quotes)
portdetails.name
network.application_protocol
Uppercased, set to value if in HTTP HTTPS DNS, else UNKNOWN_APPLICATION_PROTOCOL
verb
network.http.method
Value uppercased and copied directly
responseStatus.code
network.http.response_code
Converted to integer and copied directly
userAgent
network.http.user_agent
Value copied directly
portdetails.protocol
network.ip_protocol
Value copied directly
output_fields.cloud-project-id
observer.cloud.project.id
Value copied directly
output_fields.pod-name, output_fields.falco.pod.name
observer.hostname
Value from output_fields.pod-name if not empty, else output_fields.falco.pod.name
output_fields.pod-ip, output_fields.falco.pod.ip
observer.ip
Value from output_fields.pod-ip if not empty, else output_fields.falco.pod.ip
output_fields.falco.host.name
principal.asset.hostname
Value copied directly
sourceIPs, output_fields.falco.host.ip
principal.asset.ip
Merged from each ip in sourceIPs if not empty, else from output_fields.falco.host.ip
output_fields.falco.host.name
principal.hostname
Value copied directly
sourceIPs, output_fields.falco.host.ip
principal.ip
Merged from each ip in sourceIPs if not empty, else from output_fields.falco.host.ip
output_fields.falco.contact
principal.user.email_addresses
Value copied directly
user.groups
principal.user.group_identifiers
Merged from array user.groups
user.username, output_fields.user.name
principal.user.user_display_name
Value from user.username if not empty, else output_fields.user.name
user.uid, uid
principal.user.userid
Value from user.uid if not empty, else uid (after removing quotes)
annotations.authorization.k8s.io/decision
security_result.action
Set to ALLOW if allow
annotations.authorization.k8s.io/reason
security_result.description
Value copied directly, quotes removed
rule
security_result.rule_name
Value copied directly
priority
security_result.severity_details
Value copied directly
containerid.containerID, output_fields.container.id
target.asset.asset_id
Value from containerid.containerID if not empty, else "container_id:" + output_fields.container.id
target.asset.deployment_status
Set to ACTIVE if running or waiting, DECOMISSIONED if terminated, else DEPLOYMENT_STATUS_UNSPECIFIED
address.nodeName, output_fields.host-name, tar_host
target.asset.hostname
Value from address.nodeName if not empty, else output_fields.host-name, else tar_host from grok on output
address.ip, podip.ip, requestObject.status.podIP, requestObject.status.hostIP, output_fields.host-ip, tar_ip
target.asset.ip
Merged from address.ip in responseObject.subsets.addresses, or podip.ip in requestObject.status.podIPs, or requestObject.status.podIP, or requestObject.status.hostIP, or output_fields.host-ip, or tar_ip from grok on output
output_fields.email
target.email
Value copied directly if matches email regex
containerStatuse.imageID, containerStatuse.image, output_fields.container.image.repository
target.file.full_path
Value from containerStatuse.imageID if not empty and file.full_path empty, else containerStatuse.image if not empty and file.full_path empty, else output_fields.container.image.repository
address.nodeName, output_fields.host-name, tar_host
target.hostname
Value from address.nodeName if not empty, else output_fields.host-name, else tar_host from grok on output
address.ip, podip.ip, requestObject.status.podIP, requestObject.status.hostIP, output_fields.host-ip, tar_ip
target.ip
Merged from address.ip in responseObject.subsets.addresses, or podip.ip in requestObject.status.podIPs, or requestObject.status.podIP, or requestObject.status.hostIP, or output_fields.host-ip, or tar_ip from grok on output
targetnamespace
target.namespace
Value copied directly
portdetails.port
target.port
Converted to integer and copied directly for first port
output_fields.cloud-provider
target.resource.attribute.cloud.environment
Set to GOOGLE_CLOUD_PLATFORM if GCP, MICROSOFT_AZURE if Azure
requestObject.status.containerStatuses.0.state.waiting.reason, output_fields.evt.arg.fd, output_fields.evt.arg.filename, output_fields.evt.arg.mode, output_fields.fd.name, output_fields.ol-env, output_fields.tags, output_fields.proc.cmdline, output_fields.ebpf_enabled
target.resource.attribute.labels
Merged from various label objects
address.targetRef.uid
target.resource.id
Value from address.targetRef.uid if not empty and resource_id empty
address.targetRef.name, objectRef.name, output_fields.bl-ssr
target.resource.name
Value from address.targetRef.name if not empty and resource_name empty, else objectRef.name if not empty and resource_name empty, else output_fields.bl-ssr if not empty and resource_name empty
output_fields.falco.ssrid
target.resource.product_object_id
Value copied directly
address.targetRef.kind, objectRef.resource
target.resource.resource_subtype
Value from address.targetRef.kind if not empty and target_resource_subtype empty, else objectRef.resource if not empty and target_resource_subtype empty
resource_type
target.resource.resource_type
Set to CLUSTER if empty, else copied directly
requestURI
target.url
Value copied directly
responseObject.spec.group
target.user.group_identifiers
Merged from array responseObject.spec.group
responseObject.spec.user
target.user.user_display_name
Value copied directly
responseObject.metadata.uid, responseObject.spec.uid, objectRef.uid, requestObject.metadata.uid, output_fields.user.loginuid
target.user.userid
Value from responseObject.metadata.uid if not empty, else responseObject.spec.uid, else objectRef.uid, else requestObject.metadata.uid, else output_fields.user.loginuid (converted to string)
metadata.product_name
Set to "FALCO_IDS"
metadata.vendor_name
Set to "FALCO_IDS"
Need more help?
Get answers from Community members and Google SecOps professionals.
