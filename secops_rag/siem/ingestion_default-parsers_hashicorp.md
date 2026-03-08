# Collect HashiCorp audit logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/hashicorp/  
**Scraped:** 2026-03-05T09:25:16.212340Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect HashiCorp audit logs
Supported in:
Google secops
SIEM
This parser processes HashiCorp audit logs in JSON, Syslog, or combined formats. It extracts fields, performs Grok and KV parsing for both standard and "runner" type messages, handles JSON payloads, and maps the extracted data to the UDM. The parser also includes error handling and dropping malformed logs.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have a Windows 2016 or later or a Linux host with systemd.
If running behind a proxy, ensure firewall
ports
are open.
Ensure that you have privileged access to HCP.
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
Access the machine where Bindplane Agent is installed.
Edit the
config.yaml
file as follows:
receivers:
    udplog:
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
        namespace: auditd
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - udplog
            exporters:
                - chronicle/chronicle_w_labels
Restart the Bindplane Agent to apply the changes:
sudo
systemctl
restart
bindplane
Enable Syslog for HCP Vault
Sign in to the
HCP Portal
.
Go to
Vault Clusters
.
Select your
Vault
cluster from the list of
deployed clusters
.
In the
Cluster Overview
, locate and copy the
Vault Address
(for example, https://vault-cluster-name.hashicorpcloud.com:8200).
Go to the
Access Details
section, and copy the
Root Token
.
Install the Vault CLI
For Linux:
curl
-fsSL
https://apt.releases.hashicorp.com/gpg
|
sudo
gpg
--dearmor
-o
/usr/share/keyrings/hashicorp-archive-keyring.gpg
echo
"deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com
$(
lsb_release
-cs
)
main"
|
sudo
tee
/etc/apt/sources.list.d/hashicorp.list
sudo
apt
update
&&
sudo
apt
install
vault
For macOS (using Homebrew):
brew
tap
hashicorp/tap
brew
install
hashicorp/tap/vault
For Windows:
Download the executable file.
Extract it and add the Vault binary to your system's PATH.
Verify the Vault CLI installation by running:
vault
--version
Configure HCP Vault using CLI to send audit logs to Bindplane
Open the terminal or the command prompt.
Set the Vault server address using the environment variable:
export
VAULT_ADDR
=
"https://vault-cluster-name.hashicorpcloud.com:8200"
Log in to Vault using the root token:
vault
login
<root-token>
Configure the Syslog Path to an External Syslog Socket
Run the following command to enable syslog and send to Bindplane Agent:
vault
audit
enable
socket
address
=
"udp://<bindplane-ip>:<bindplane-port>"
socket_type
=
"udp"
tag
=
"vault"
Confirm the new configuration:
vault
audit
list
The output should display the new socket configuration.
Optional: Automate the setup using Terraform:
Create a Terraform configuration file (audit.tf):
resource
"vault_audit"
"syslog"
{
type
=
"syslog"
description
=
"Syslog audit logs"
options
=
{
tag
=
"vault"
facility
=
"LOCAL0"
}
}
resource
"vault_audit"
"socket"
{
type
=
"socket"
description
=
"Remote syslog socket"
options
=
{
address
=
"udp://<syslog-server-ip>:514"
socket_type
=
"udp"
tag
=
"vault"
}
}
Apply the configuration:
terraform
init
terraform
apply
Troubleshooting logs not received
Verify the syslog server is reachable:
ping
<syslog-server-ip>
UDM Mapping Table
Log Field
UDM Mapping
Logic
auth.accessor
security_result.about.resource.attribute.labels.value
The value of
auth.accessor
from the raw log is mapped to a label with key "auth_accessor" under
security_result.about.resource.attribute.labels
in the UDM.
auth.client_token
security_result.about.resource.attribute.labels.value
The value of
auth.client_token
from the raw log is mapped to a label with key "auth_client_token" under
security_result.about.resource.attribute.labels
in the UDM.
auth.display_name
target.user.user_display_name
The value of
auth.display_name
from the raw log is mapped to
target.user.user_display_name
in the UDM.
auth.entity_id
target.resource.product_object_id
The value of
auth.entity_id
from the raw log is mapped to
target.resource.product_object_id
in the UDM.
auth.metadata.account_id
target.user.userid
The value of
auth.metadata.account_id
from the raw log is mapped to
target.user.userid
in the UDM.
auth.metadata.auth_type
security_result.about.resource.attribute.labels.value
The value of
auth.metadata.auth_type
from the raw log is mapped to a label with key "auth_type" under
security_result.about.resource.attribute.labels
in the UDM.
auth.metadata.role_id
security_result.about.resource.attribute.labels.value
The value of
auth.metadata.role_id
from the raw log is mapped to a label with key "role_id" under
security_result.about.resource.attribute.labels
in the UDM.
auth.metadata.role_name
target.resource.attribute.roles.name
The value of
auth.metadata.role_name
from the raw log is mapped to
target.resource.attribute.roles.name
in the UDM.
auth.token_ttl
security_result.about.resource.attribute.labels.value
The value of
auth.token_ttl
from the raw log is mapped to a label with key "auth_token_ttl" under
security_result.about.resource.attribute.labels
in the UDM.
auth.token_type
security_result.about.resource.attribute.labels.value
The value of
auth.token_type
from the raw log is mapped to a label with key "auth_token_type" under
security_result.about.resource.attribute.labels
in the UDM.
cluster
observer.resource.name
The value of
cluster
from the raw log is mapped to
observer.resource.name
in the UDM.
error
security_result.description
The value of
error
from the raw log is mapped to
security_result.description
in the UDM.
headers.accept
security_result.about.resource.attribute.labels.value
The value of
headers.accept
from the raw log is mapped to a label with key "httpHeaders accept" under
security_result.about.resource.attribute.labels
in the UDM.
headers.httpHeaders.cache-control
additional.fields.value.string_value
The value of
headers.httpHeaders.cache-control
from the raw log is mapped to a field with key "httpHeaders cache control" under
additional.fields
in the UDM.
headers.snyk-acting-org-public-id
principal.resource.attribute.labels.value
The value of
headers.snyk-acting-org-public-id
from the raw log is mapped to a label with key "snyk-acting-org-public-id" under
principal.resource.attribute.labels
in the UDM.
headers.snyk-flow-name
principal.resource.attribute.labels.value
The value of
headers.snyk-flow-name
from the raw log is mapped to a label with key "snyk-flow-name" under
principal.resource.attribute.labels
in the UDM.
headers.snyk-request-id
principal.resource.attribute.labels.value
The value of
headers.snyk-request-id
from the raw log is mapped to a label with key "snyk-request-id" under
principal.resource.attribute.labels
in the UDM.
headers.user-agent
network.http.parsed_user_agent
The value of
headers.user-agent
from the raw log is parsed as a user agent and mapped to
network.http.parsed_user_agent
in the UDM.
headers.x-forwarded-host
principal.hostname
The value of
headers.x-forwarded-host
from the raw log is mapped to
principal.hostname
in the UDM.
headers.x-forwarded-port
principal.port
The value of
headers.x-forwarded-port
from the raw log is mapped to
principal.port
in the UDM.
headers.x-real-ip
principal.ip
The value of
headers.x-real-ip
from the raw log is mapped to
principal.ip
in the UDM.
hostname
observer.hostname
The value of
hostname
from the raw log is mapped to
observer.hostname
in the UDM.
httpHeaders.cf-cache-status
target.resource.attribute.labels.value
The value of
httpHeaders.cf-cache-status
from the raw log is mapped to a label with key "cf-cache-status" under
target.resource.attribute.labels
in the UDM.
httpHeaders.cf-ray
target.resource.attribute.labels.value
The value of
httpHeaders.cf-ray
from the raw log is mapped to a label with key "cf-ray" under
target.resource.attribute.labels
in the UDM.
httpHeaders.content-length
security_result.about.resource.attribute.labels.value
The value of
httpHeaders.content-length
from the raw log is mapped to a label with key "httpHeaders Content-Length" under
security_result.about.resource.attribute.labels
in the UDM.
httpHeaders.content-type
security_result.about.resource.attribute.labels.value
The value of
httpHeaders.content-type
from the raw log is mapped to a label with key "httpHeaders Content-Type" under
security_result.about.resource.attribute.labels
in the UDM.
httpHeaders.gitlab-lb
target.resource.attribute.labels.value
The value of
httpHeaders.gitlab-lb
from the raw log is mapped to a label with key "gitlab-lb" under
target.resource.attribute.labels
in the UDM.
httpHeaders.gitlab-sv
target.resource.attribute.labels.value
The value of
httpHeaders.gitlab-sv
from the raw log is mapped to a label with key "gitlab-sv" under
target.resource.attribute.labels
in the UDM.
httpHeaders.ratelimit-limit
target.resource.attribute.labels.value
The value of
httpHeaders.ratelimit-limit
from the raw log is mapped to a label with key "ratelimit-limit" under
target.resource.attribute.labels
in the UDM.
httpHeaders.ratelimit-observed
target.resource.attribute.labels.value
The value of
httpHeaders.ratelimit-observed
from the raw log is mapped to a label with key "ratelimit-observed" under
target.resource.attribute.labels
in the UDM.
httpHeaders.ratelimit-remaining
target.resource.attribute.labels.value
The value of
httpHeaders.ratelimit-remaining
from the raw log is mapped to a label with key "ratelimit-remaining" under
target.resource.attribute.labels
in the UDM.
httpHeaders.ratelimit-reset
target.resource.attribute.labels.value
The value of
httpHeaders.ratelimit-reset
from the raw log is mapped to a label with key "ratelimit-reset" under
target.resource.attribute.labels
in the UDM.
httpHeaders.ratelimit-resettime
target.resource.attribute.labels.value
The value of
httpHeaders.ratelimit-resettime
from the raw log is mapped to a label with key "ratelimit-resettime" under
target.resource.attribute.labels
in the UDM.
httpHeaders.referrer-policy
target.resource.attribute.labels.value
The value of
httpHeaders.referrer-policy
from the raw log is mapped to a label with key "referrer-policy" under
target.resource.attribute.labels
in the UDM.
httpHeaders.server
target.resource.attribute.labels.value
The value of
httpHeaders.server
from the raw log is mapped to a label with key "server" under
target.resource.attribute.labels
in the UDM.
httpHeaders.x-content-type-options
target.resource.attribute.labels.value
The value of
httpHeaders.x-content-type-options
from the raw log is mapped to a label with key "x-content-type-options" under
target.resource.attribute.labels
in the UDM.
httpHeaders.x-frame-options
target.resource.attribute.labels.value
The value of
httpHeaders.x-frame-options
from the raw log is mapped to a label with key "x-frame-options" under
target.resource.attribute.labels
in the UDM.
httpHeaders.x-request-id
target.resource.attribute.labels.value
The value of
httpHeaders.x-request-id
from the raw log is mapped to a label with key "x-request-id" under
target.resource.attribute.labels
in the UDM.
httpStatus
network.http.response_code
The value of
httpStatus
from the raw log is mapped to
network.http.response_code
in the UDM.
httpUrl
target.url
The value of
httpUrl
from the raw log is mapped to
target.url
in the UDM.
insertId
metadata.product_log_id
The value of
insertId
from the raw log is mapped to
metadata.product_log_id
in the UDM.
job
additional.fields.value.string_value
The value of
job
from the raw log is mapped to a field with key "job id" under
additional.fields
in the UDM.
job_status
additional.fields.value.string_value
The value of
job_status
from the raw log is mapped to a field with key "job_status" under
additional.fields
in the UDM.
labels.compute.googleapis.com/resource_name
target.resource.name
The value of
labels.compute.googleapis.com/resource_name
from the raw log is mapped to
target.resource.name
in the UDM.
labels.k8s-pod/app_kubernetes_io/instance
target.resource.attribute.labels.value
The value of
labels.k8s-pod/app_kubernetes_io/instance
from the raw log is mapped to a label with key "Kubernetes IO Instance" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/app_kubernetes_io/name
target.resource.attribute.labels.value
The value of
labels.k8s-pod/app_kubernetes_io/name
from the raw log is mapped to a label with key "Kubernetes IO Instance Name" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/component
target.resource.attribute.labels.value
The value of
labels.k8s-pod/component
from the raw log is mapped to a label with key "component" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/controller-revision-hash
target.resource.attribute.labels.value
The value of
labels.k8s-pod/controller-revision-hash
from the raw log is mapped to a label with key "Controller Revision Hash" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/helm_sh/chart
target.resource.attribute.labels.value
The value of
labels.k8s-pod/helm_sh/chart
from the raw log is mapped to a label with key "Kubernetes IO Instance Manager SH" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/vault-active
target.resource.attribute.labels.value
The value of
labels.k8s-pod/vault-active
from the raw log is mapped to a label with key "Vault active" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/vault-initialized
target.resource.attribute.labels.value
The value of
labels.k8s-pod/vault-initialized
from the raw log is mapped to a label with key "Vault initialized" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/vault-perf-standby
target.resource.attribute.labels.value
The value of
labels.k8s-pod/vault-perf-standby
from the raw log is mapped to a label with key "vault perf standby" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/vault-sealed
target.resource.attribute.labels.value
The value of
labels.k8s-pod/vault-sealed
from the raw log is mapped to a label with key "Vault sealed" under
target.resource.attribute.labels
in the UDM.
labels.k8s-pod/vault-version
target.resource.attribute.labels.value
The value of
labels.k8s-pod/vault-version
from the raw log is mapped to a label with key "Vault version" under
target.resource.attribute.labels
in the UDM.
maskedToken
security_result.about.resource.attribute.labels.value
The value of
maskedToken
from the raw log is mapped to a label with key "maskedToken" under
security_result.about.resource.attribute.labels
in the UDM.
method
network.http.method
,
operation
The value of
method
from the raw log is mapped to
operation
. If
operation
is not empty, then
network.application_protocol
is set to "HTTP". Based on the value of
operation
,
network.http.method
is derived.
msg
metadata.description
The value of
msg
from the raw log is mapped to
metadata.description
in the UDM.
pid
target.process.pid
The value of
pid
from the raw log is mapped to
target.process.pid
in the UDM.
request.client_token
target.resource.attribute.labels.value
The value of
request.client_token
from the raw log is mapped to a label with key "request_client_token" under
target.resource.attribute.labels
in the UDM.
request.client_token_accessor
target.resource.attribute.labels.value
The value of
request.client_token_accessor
from the raw log is mapped to a label with key "request_client_token_accessor" under
target.resource.attribute.labels
in the UDM.
request.data.role_id
target.resource.attribute.labels.value
The value of
request.data.role_id
from the raw log is mapped to a label with key "request_data_role_id" under
target.resource.attribute.labels
in the UDM.
request.data.secret_id
target.resource.attribute.labels.value
The value of
request.data.secret_id
from the raw log is mapped to a label with key "request_data_secret_id" under
target.resource.attribute.labels
in the UDM.
request.id
network.session_id
The value of
request.id
from the raw log is mapped to
network.session_id
in the UDM.
request.mount_accessor
target.resource.attribute.labels.value
The value of
request.mount_accessor
from the raw log is mapped to a label with key "request_mount_accessor" under
target.resource.attribute.labels
in the UDM.
request.mount_type
target.resource.attribute.labels.value
The value of
request.mount_type
from the raw log is mapped to a label with key "request_mount_type" under
target.resource.attribute.labels
in the UDM.
request.namespace.id
target.namespace
The value of
request.namespace.id
from the raw log is mapped to
target.namespace
in the UDM.
request.operation
target.resource.attribute.labels.value
,
network.http.method
,
operation
The value of
request.operation
from the raw log is mapped to
operation
. If
operation
is not empty, then
network.application_protocol
is set to "HTTP". Based on the value of
operation
,
network.http.method
is derived.  The value of
request.operation
is also mapped to a label with key "capabilities" under
target.resource.attribute.labels
in the UDM.
request.path
target.url
The value of
request.path
from the raw log is mapped to
target.url
in the UDM.
request.remote_address
principal.ip
The value of
request.remote_address
from the raw log is mapped to
principal.ip
in the UDM.
request.remote_port
principal.port
The value of
request.remote_port
from the raw log is mapped to
principal.port
in the UDM.
request.wrap_ttl
target.resource.attribute.labels.value
The value of
request.wrap_ttl
from the raw log is mapped to a label with key "request_wrap_ttl" under
target.resource.attribute.labels
in the UDM.
resource.labels.container_name
additional.fields.value.string_value
The value of
resource.labels.container_name
from the raw log is mapped to a field with key "container name" under
additional.fields
in the UDM.
resource.labels.location
target.location.name
The value of
resource.labels.location
from the raw log is mapped to
target.location.name
in the UDM.
resource.labels.namespace_name
target.namespace
The value of
resource.labels.namespace_name
from the raw log is mapped to
target.namespace
in the UDM.
resource.labels.pod_name
additional.fields.value.string_value
The value of
resource.labels.pod_name
from the raw log is mapped to a field with key "pod_name" under
additional.fields
in the UDM.
resource.labels.project_id
target.cloud.project.name
The value of
resource.labels.project_id
from the raw log is mapped to
target.cloud.project.name
in the UDM.
response.data.num_uses
target.resource.attribute.labels.value
The value of
response.data.num_uses
from the raw log is mapped to a label with key "response_data_num_uses" under
target.resource.attribute.labels
in the UDM.
response.data.orphan
target.resource.attribute.labels.value
The value of
response.data.orphan
from the raw log is mapped to a label with key "response_data_orphan" under
target.resource.attribute.labels
in the UDM.
response.data.renewable
target.resource.attribute.labels.value
The value of
response.data.renewable
from the raw log is mapped to a label with key "response_data_renewable" under
target.resource.attribute.labels
in the UDM.
response.data.ttl
target.resource.attribute.labels.value
The value of
response.data.ttl
from the raw log is mapped to a label with key "response_data_ttl" under
target.resource.attribute.labels
in the UDM.
response.wrap_info.accessor
target.resource.attribute.labels.value
The value of
response.wrap_info.accessor
from the raw log is mapped to a label with key "response_wrap_info_accessor" under
target.resource.attribute.labels
in the UDM.
response.wrap_info.token
target.resource.attribute.labels.value
The value of
response.wrap_info.token
from the raw log is mapped to a label with key "response_wrap_info_token" under
target.resource.attribute.labels
in the UDM.
response.wrap_info.ttl
target.resource.attribute.labels.value
The value of
response.wrap_info.ttl
from the raw log is mapped to a label with key "response_wrap_info_ttl" under
target.resource.attribute.labels
in the UDM.
response.wrap_info.wrapped_accessor
target.resource.attribute.labels.value
The value of
response.wrap_info.wrapped_accessor
from the raw log is mapped to a label with key "response_wrap_info_wrapped_accessor" under
target.resource.attribute.labels
in the UDM.
runner
principal.user.userid
The value of
runner
from the raw log is mapped to
principal.user.userid
in the UDM.
status
network.http.response_code
The value of
status
from the raw log is mapped to
network.http.response_code
in the UDM.
streamingID
target.resource.attribute.labels.value
The value of
streamingID
from the raw log is mapped to a label with key "streamingID" under
target.resource.attribute.labels
in the UDM.
time
metadata.event_timestamp.seconds
,
metadata.event_timestamp.nanos
The value of
time
from the raw log is parsed and used to populate the
metadata.event_timestamp
field in the UDM.
type
metadata.product_event_type
The value of
type
from the raw log is mapped to
metadata.product_event_type
in the UDM.
url
principal.url
The value of
url
from the raw log is mapped to
principal.url
in the UDM.  The value "MACHINE" is assigned to
extensions.auth.type
in the UDM. The value "USER_LOGIN" is assigned to
metadata.event_type
in the UDM. The value "HASHICORP" is assigned to
metadata.log_type
in the UDM. The value "HASHICORP" is assigned to
metadata.product_name
in the UDM. The value "HASHICORP" is assigned to
metadata.vendor_name
in the UDM. The value "SERVICE_ACCOUNT" is assigned to
target.resource.attribute.roles.type
in the UDM.
Need more help?
Get answers from Community members and Google SecOps professionals.
