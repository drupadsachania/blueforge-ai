# Use Bindplane with Google SecOps

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/use-bindplane-agent/  
**Scraped:** 2026-03-05T09:16:28.820121Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use Bindplane with Google SecOps
Supported in:
Google secops
SIEM
This document describes Bindplane for Google Security Operations.
Bindplane is a telemetry pipeline, which can collect, refine, and export logs from any source into Google SecOps.
Bindplane offers
two editions especially for Google
.
Bindplane includes the following main components:
Bindplane collector
. An open-source agent, based on the
OpenTelemetry
(
OTel
)
Collector
. It collects logs from various sources, including Microsoft Windows event logs, and sends them to Google SecOps. You can install the collectors on-premises or in the cloud.
This component can also be referred to as
Bindplane Distribution for OpenTelemetry (BDOT) Collector
,
bindplane agent
,
collection agent
,
collector
, or
agent
.
Bindplane Server
. A comprehensive and unified platform for managing your OTel collector deployments. These deployments can reside in Google SecOps and Google Cloud. Many Google SecOps customers use Bindplane Server, but its use is optional. Bindplane Server can run on-premises or in the Bindplane cloud. For more information about the server, see
Bindplane server
.
This component may also be referred to as the
Bindplane Observability Pipeline (OP) Management console
or
Bindplane Management console
.
Bindplane's Google editions
Bindplane offers two editions especially for Google:
Bindplane (Google Edition)
and
Bindplane Enterprise (Google Edition)
.
Bindplane (Google Edition)
Bindplane (Google Edition)
is provided to all Google SecOps customers.
You can self-service Bindplane (Google Edition) on the Bindplane cloud.
To get started installing and self-hosting Bindplane (Google Edition) or generate your key for an on-premises Bindplane server, see
Bindplane (Google Edition)
.
Bindplane Enterprise (Google Edition)—for Google SecOps Enterprise Plus customers
Bindplane Enterprise (Google Edition)
is included for Google SecOps Enterprise Plus customers.
Bindplane Enterprise (Google Edition) is recommended for large-scale deployments.
Contact your Google Account team to get your license key for Bindplane Enterprise (Google Edition).
Bindplane Google editions—differences
The following table lists the differences in the Bindplane Google editions:
Topic/feature
Bindplane (Google Edition)
Bindplane Enterprise (Google Edition)
Cost
Included at no extra charge for all Google SecOps customers
Included at no charge for Google SecOps Enterprise Plus customers
Routing/Destinations
Google only, including Google SecOps, Cloud Logging,
  BigQuery, and Cloud Storage through Google SecOps
Google, including 12 months of routing to a non-Google destination
  for SIEM migrations
Filtering
Basic filter with regular expression
Advanced filtering processors (for example, filter by condition, field, severity, and so on),
  data reduction, log sampling, deduplication
Redaction
N/A
PII masking
Transformation
Add field, move field, parse data (KV, JSON, CSV, XML, timestamp,
  parse by regular expression), rename field, event breaker
Includes all capabilities supported in Bindplane (Google Edition)
plus
delete field, delete empty values, coalesce
General platform-level features
Gateway (aggregate data from collectors), Bindplane collectors,
Bindplane server (Bindplane management layer) on-premises or cloud-hosted, all sources,
silent-host monitoring through Google SecOps processor, persistent queue, enrich
telemetry, high availability, RBAC, both Google SecOps ingestion APIs supported, credential obfuscation,
advanced fleet management including grouping of collectors, dynamic log-type assignment
All capabilities supported in Bindplane (Google Edition)
Bindplane collector architecture
Bindplane uses the BDOT Collector—generically referred to as a
collector
—to standardize telemetry management with
Open Agent Management Protocol
(
OpAMP
). You can also create and manage
custom
OpenTelemetry Collector distributions with Bindplane.
The collector can run in Linux or Docker as a lightweight web server with no external dependencies.
To learn more about the deployment architecture of Bindplane OpenTelemetry collectors, see
Deployment
.
The following sections describe available architecture options.
Collectors send logs to a collector acting as a gateway
For large-scale deployments, we recommend that you use collectors that act as gateways. These gateways receive telemetry from other collectors over the network, optionally perform additional processing, and route the data to Google SecOps.
A collector acting as a gateway uses the same binary as all the other collectors.
The following diagram shows collectors sending logs to a collector acting as a gateway:
Collectors send logs directly to Google SecOps ingestion API
The following diagram shows collectors sending logs directly to Google SecOps ingestion API:
Collectors send logs directly to Cloud Logging
The following diagram shows collectors sending logs directly to Cloud Logging:
Collectors send logs to multiple destinations
The following diagram shows collectors sending logs to multiple destinations:
Bindplane server
Bindplane server offers the following key features:
Centralized management
. The server lets you manage all of your OTel collector deployments across Google Cloud. You can view the status of each deployment and perform common management tasks such as starting, stopping, and restarting collectors.
Real-time monitoring
. The server provides real-time monitoring of your OTel collector deployments. You can track metrics such as CPU usage, memory usage, and throughput. You can also view logs and traces to troubleshoot issues.
Alerting and notifications
. The server lets you set up alerts and notifications for important events, such as when a collector goes down or when a metric threshold is exceeded.
Configuration management
. The server lets you centrally manage the configuration of your OTel collectors. You can edit configuration files, set environment variables, and apply security policies to all your deployments.
Integration with Google Cloud
. You can create and manage OTel collector deployments in Google Cloud and use the server to access your Google Cloud resources.
Bindplane offers cloud and on-premises deployment options. For more information, see
Use the Bindplane server
.
Technical requirements and recommendations
This section describes the technical requirements and recommendations for installing and running Bindplane with Google SecOps.
Bandwidth requirements
Bindplane maintains network connections for the following:
Collector management
Collector throughput measurements
Command line and web user interfaces
Connectivity requirements
Bindplane listens on port 3001 by default. This port is configurable.
The Bindplane port is used for:
Collector command and control using OpAMP (WebSocket)
Collector throughput measurement requests (HTTP
POST
request)
Browser and CLI users (HTTP and WebSocket)
Collectors must be able to initiate connections to Bindplane for OpAMP (WebSocket) and throughput measurements (HTTP).
Bindplane never initiates connections to the collectors. You can configure a firewall to prevent Bindplane from reaching the collector networks; however, collector networks must be able to reach Bindplane on the configured port.
Bindplane collector general technical requirements
To learn about the general technical requirements for the Bindplane collector, see the following:
Bindplane OTel collector on GitHub
Install and Uninstall Bindplane Collectors
Prerequisites for installation
Collector sizing and scaling guidelines
Collector resource requirements
Bindplane's resource requirements differ based on the number of managed collectors. As the number of managed collectors increases, CPU, memory, disk throughput/IOPS, and network consumption also increase.
Use the following table for CPU, memory, and storage-capacity sizing:
Collector count
Bindplane nodes
Fault tolerance
CPU cores
Memory
Database
1-100
1
N/A
2
4 GB
bbolt
100-25,000
1
N/A
4
16 GB
postgres
1-60,000
3
1
2
8 GB
postgres
60,001-125,000
5
1
2
8 GB
postgres
125,001-250,000
10
2
2
8 GB
postgres
Plan your installation and deployment
The following sections include recommendations and best practices, which you should consider when you plan your Bindplane deployment.
Consider scaling and fault tolerance
Horizontal scaling is preferable because it provides fault tolerance and can eliminate exporter bottlenecks.
When you run Bindplane collectors in
gateway mode
, we recommend that you pair them with a load balancer to provide fault tolerance and horizontal scaling.
Calculate how many collectors you need
When calculating the number of collectors required for your workload, consider the anticipated throughput or log rate, and use the following table. This table presumes that each collector has four CPU cores and 16 GB of memory. The table doesn't include calculations with processors; when processors are added, the compute requirements increase.
Telemetry throughput
Logs/second
Collectors
5 GB/m
250,000
2
10 GB/m
500,000
3
20 GB/m
1,000,000
5
100 GB/m
5,000,000
25
Overprovision the collector fleet for fault tolerance
Overprovision the collector fleet to ensure fault tolerance. In the event that one or more collector systems fail or are taken offline for maintenance, the remaining collectors must have sufficient capacity to manage the telemetry throughput.
If you're working with a fixed number of collectors, you can implement vertical scaling of their CPU and memory to increase throughput.
Offload processing overhead
Generally, you want your collectors to perform as little work as possible. If you have heavy processing requirements, it can be useful to offload that processing to a fleet of gateway collectors. For example, instead of filtering telemetry with an expensive regular-expression operation, you can have the gateway collectors perform that task. Generally, gateway collectors run on a dedicated system. This justifies the processing overhead because it does not consume the compute power of other services running on the same system, unlike a non-gateway collector that may be running on a database server.
Best practices for gateway mode
When you run Bindplane collectors in
gateway mode
, we recommend that you plan your deployment with the following best practices:
Place at least two collectors behind a
load balancer
.
Each collector should have a minimum of two cores.
Each collector should have a minimum of 8 GB of memory.
Each collector should have 60 GB of usable space for a persistent queue.
Use a load balancer when needed
A load balancer is required when you operate Bindplane in
high-availability mode
.
When you run Bindplane collectors in
gateway mode
, use a load balancer for increased performance and redundancy. Load balancing also enables the horizontal scaling of your gateway fleet and the ability to withstand failures without causing outages.
The Bindplane collector can work with a wide range of load balancers.
To learn more, see
Load Balancer Configuration
.
Load-balancing port and protocols
Bindplane listens on port 3001 by default.
To support the wide range of network-based receivers in OpenTelemetry, the load balancer must support:
TCP/UDP transport protocols
HTTP and gRPC application protocols
Load-balancing sizing
Bindplane nodes should manage no more than 30,000 collectors for maximum fault tolerance. Each collector opens two connections to Bindplane (one for OpAMP remote management and one for publishing throughput metrics). This limit helps ensure that you don't exceed the connection limit of approximately 65,535 per backend instance imposed by most load balancers.
If an organization has 100,000 collectors, a cluster size of three would be insufficient. Each node would be responsible for approximately 33,000 collectors, which translates to 66,000 TCP connections per Bindplane instance. This situation worsens if one node is taken down for maintenance, as each remaining Bindplane instance would then manage 50,000 collectors, or 100,000 TCP connections.
Load-balancing sizing best practices
Implement health checks
. Configure the load balancer to make sure the collector is ready to receive traffic.
Distribute connections evenly
. Connections should be distributed evenly among collectors.
Support required protocols
. To support the wide range of network-based receivers in OpenTelemetry, the load balancer must support:
TCP/UDP transport protocols
HTTP and gRPC application protocols
To learn more, see
Collector Resilience
.
Source-type load balancing
Any source type that receives telemetry from remote systems over the network is a suitable candidate for load balancing, including the following:
OTLP
Syslog
TCP/UDP
Splunk HEC
Fluent Forward
Use high-availability mode in production environments
You can deploy a Bindplane instance in either a
single-instance
or
multi-instance
configuration. For production deployments that require high availability (HA) and resilience, we recommend that you use a multi-instance (HA) deployment model.
When Bindplane manages more than 25,000 collectors, we recommend that you operate Bindplane in high-availability (HA) mode.
To learn about HA in Bindplane, see
High Availability
.
Calculate the number of collectors and Bindplane servers for HA
When you operate Bindplane in HA mode, you must consider how many collectors you expect each Bindplane server to handle.
Take the total number of Bindplane instances, and subtract the maximum number of nodes you expect to become unavailable due to maintenance. Make sure that each node manages no more than 30,000 collectors during a node outage.
Postgres for HA
Postgres is a prerequisite when you operate Bindplane in HA mode.
Prometheus for HA
Prometheus is required when you operate Bindplane in HA mode.
To learn more, see
Prometheus
.
Event bus for HA
Bindplane uses an event bus to communicate between components within Bindplane. When you operate Bindplane in HA mode, you can use the event bus to send events between Bindplane servers.
To learn more, see
Event Bus
.
Use a single-instance deployment for a test environment or a proof-of-concept
For a test environment or a proof-of-concept, we recommend that you use a single-instance deployment.
To learn more, see
Single Instance
.
Isolate backend credentials
Instead of deploying credentials to all of your collector systems, you can keep credentials exclusively on the gateway collectors. This simplifies credential rotation and reduces the security attack surface by limiting credential deployment to a subset of your systems.
Firewall your gateway collectors
You can place gateway collectors within a perimeter network, firewalled from the internal network. You can configure your network to allow your other collectors to forward data to the gateway collectors while blocking gateway collectors from accessing your application network. This lets you send telemetry to a cloud-based backend without granting your endpoints direct access to the internet.
The firewall must allow HTTP traffic to reach the Bindplane on the configured port.
Verify the firewall configuration
Any firewalls or authenticated proxies between the collector and the internet
require rules to open access to the following hosts:
Connection type
Destination
Port
TCP
malachiteingestion-pa.googleapis.com
443
TCP
asia-northeast1-malachiteingestion-pa.googleapis.com
443
TCP
asia-south1-malachiteingestion-pa.googleapis.com
443
TCP
asia-southeast1-malachiteingestion-pa.googleapis.com
443
TCP
australia-southeast1-malachiteingestion-pa.googleapis.com
443
TCP
europe-malachiteingestion-pa.googleapis.com
443
TCP
europe-west2-malachiteingestion-pa.googleapis.com
443
TCP
europe-west3-malachiteingestion-pa.googleapis.com
443
TCP
europe-west6-malachiteingestion-pa.googleapis.com
443
TCP
europe-west12-malachiteingestion-pa.googleapis.com
443
TCP
me-central1-malachiteingestion-pa.googleapis.com
443
TCP
me-central2-malachiteingestion-pa.googleapis.com
443
TCP
me-west1-malachiteingestion-pa.googleapis.com
443
TCP
northamerica-northeast2-malachiteingestion-pa.googleapis.com
443
TCP
accounts.google.com
443
TCP
oauth2.googleapis.com
443
Use PostgreSQL for production deployments
Postgres
is required for production deployments of Bindplane.
Postgres is a prerequisite for you operate Bindplane in HA mode.
The number of CPU cores and available memory generally limit the performance of PostgreSQL storage backends. We recommend backing PostgreSQL storage with low-latency, high-throughput storage, such as solid-state drives (SSDs).
Collector count
CPU cores
Memory
1-60,000
4
16 GB
60,001-125,000
8
32 GB
125,001-250,000
16
64 GB
To learn more, see the following:
PostgreSQL documentation
Postgres setup guide
Postgres Store configuration
Postgres TLS setup
Implement proper authentication
Bindplane supports authentication with the following protocols and services; make sure that they are properly implemented:
Azure Entra LDAP
. To learn more, see
Azure LDAP
and
Changing Bindplane Authentication Type
.
LDAP
.
OpenID Connect (OIDC)
.
Local
.
SAML
.
Postgres TLS
. To learn more, see
Postgres TLS
.
Kubernetes
. To learn more, see
GKE Workload Identity
.
Use the Bindplane server
Most Google SecOps customers use the Bindplane server, but its use is optional. If you're installing the Bindplane server, you need access to
storage.googleapis.com
. If you're installing only a collector, this access isn't required.
For a demo that shows how to configure Bindplane server to standardize logs and export them to Google SecOps, 
go to
Bindplane Use Case Demos
, and then select
Google SecOps Configuration
.
Use the Bindplane Cloud server
Bindplane Cloud is available for Google customers.
Sign in to the Google Edition
.
For any issues related to Bindplane Cloud Server, contact
Bindplane support
. For any issues related to on-premises Bindplane Server, contact Google SecOps support.
Use the Bindplane server on your Google Cloud
For information on how to run the Bindplane server on your Google Cloud, see
Bindplane Enterprise Edition
.
Use the Bindplane on-premises server
The use of the on-premises Bindplane server is governed by the existing
Google Cloud Terms of Service
.
Install the on-premises server on Linux
You can install the on-premises Bindplane server on Linux either by running a script (
recommended
) or downloading a binary file and installing manually. To learn more, see
Install Bindplane Server
.
To install the on-premises Bindplane server on Linux with a script, do the following:
Run this script:
curl -fsSlL https://storage.googleapis.com/bindplane-op-releases/bindplane/latest/install-linux.sh -o install-linux.sh && bash install-linux.sh --init && rm install-linux.sh
Follow the instructions, which guide you through to the server initialization.
To install the on-premises Bindplane server on Linux with a binary file, do the following:
Download one of the following files:
Bindplane-ee-linux-amd64.zip
Bindplane-ee-linux-arm64.zip
Bindplane-ee_linux_amd64.deb
Bindplane-ee_linux_amd64.rpm
Bindplane-ee_linux_arm64.deb
Bindplane-ee_linux_arm64.rpm
Update the configuration file using the instructions in
Configure Bindplane Server
.
Supported Linux distributions:
Red Hat, Centos, Oracle Linux 7, 8, 9
Debian 11 and 12
Ubuntu LTS 20.04 and 22.04
SUSE Linux 12 and 15
Alma and Rocky Linux
To learn more, see the following:
Install Bindplane Server
Package Downloads
Docker on-premises deployments
To learn more, see
Install Bindplane Server
.
You can find Bindplane Docker container images at the following locations:
GitHub packages
:
ghcr.io/observiq/Bindplane-ee
Google artifact repository
:
us-central1-docker.pkg.dev/observiq-containers/bindplane/bindplane-ee
Docker hub
:
observiq/bindplane-ee
Container images are tagged with the release version: for example, Release
v1.35.0
will have the tag
observiq/bindplane-ee:1.35.0
.
Install the Bindplane collector
This section describes how to install the Bindplane collector for Google SecOps on various systems.
Collectors typically use minimal resources. However, when handling large volumes of logs, be mindful of resource consumption to avoid impacting other services. For more information, see
Technical requirements and recommendations
,
Plan your installation and deployment
, and
Agent Sizing and Scaling
.
To learn about how to install the collector (that is, the OTel agent), see
Bindplane OTel Collector
.
You can also refer to the GitHub documentation
bindplane-otel-collector
.
To install the collector, you need the following:
Google SecOps ingestion authentication file
To download the authentication file, follow these steps:
Open the Google SecOps console.
Go to
SIEM Settings
>
Collection Agent
.
Download the Google SecOps ingestion authentication file.
Google SecOps customer ID
To find the customer ID, follow these steps:
Open the Google SecOps console.
Go to
SIEM Settings
>
Profile
.
Copy the customer ID from the
Organization Details
section.
Windows 2012 SP2 or later
or
Linux host with systemd
Internet connectivity
GitHub access
Deployment tools
This section describes the deployment tools for Bindplane.
GitOps
Deploy Bindplane resources using a GitOps model, which includes the following:
Bindplane authentication
Bindplane CLI
Network access
Integration with a GitHub repository and GitHub Actions
Exporting existing resources
Managing sensitive values
Establishing a GitHub Action workflow
Step-by-step instructions for committing and testing the configuration, enabling automatic rollouts, and updating resources utilizing either direct edits or the UI export method
Updating sensitive values and employing RBAC
To learn more, see
GitOps
.
Ansible
To learn about deploying Bindplane with Ansible, see
bindplane-agent-ansible
.
Bindplane CLI
To learn about the Bindplane CLI, see
GitOps
.
Terraform
To learn about using Terraform to configure your Bindplane resources, see
Bindplane Provider
.
Kubernetes
To learn about Kubernetes with Bindplane, see the following:
Kubernetes Dynamic Cluster Name
Kubernetes Postgres Migration
Install the Bindplane collector on Windows
To install the Bindplane collector on Windows, run the following PowerShell command:
msiexec /i "https://github.com/observIQ/bindplane-agent/releases/latest/download/observiq-otel-collector.msi" /quiet
Alternatively, to install using an installation wizard,
download the latest installer for Windows
. After you download the installer, open the installation wizard and follow
the instructions to configure and install the Bindplane collector.
To learn more about installing the Bindplane collector on Windows, see
Windows Installation
.
Install the Bindplane collector on Linux
You can install the collector on Linux using a script that automatically determines
which package to install. You can also use the same script to update an existing installation.
To install using the installation script, run the following script:
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh
Installation from a local package
To install the collector from a local package, use
-f
with the path to the package.
sudo sh -c "$(curl -fsSlL https://github.com/observiq/bindplane-agent/releases/latest/download/install_unix.sh)" install_unix.sh -f
path_to_package
RPM installation
Download the RPM package for your architecture from the
releases page
and install the package using
rpm
. Refer to the following example for installing
the
amd64
package:
sudo rpm -U ./observiq-otel-collector_v${
VERSION
}_linux_amd64.rpm
sudo systemctl enable --now observiq-otel-collector
Replace
VERSION
with the version of the package you downloaded.
DEB installation
Download the DEB package for your architecture from the
releases page
and install the package using
dpkg
. Refer to the following example for installing the
amd64
package:
sudo dpkg -i --force-overwrite ./observiq-otel-collector_v${
VERSION
}_linux_amd64.deb
sudo systemctl enable --now observiq-otel-collector
Replace
VERSION
with the version of the package that you downloaded.
Configure the Bindplane collector
After installing the collector, the
observiq-otel-collector
service runs and is ready for configuration.
You can configure the collector either manually or using the Bindplane server.
If you're configuring the collector manually, you need to update the exporter
parameters to ensure that the collector authenticates with Google SecOps.
OTel collector config file
In Linux, the collector's config file can be found at
/opt/observiq-otel-collector/config.yaml
.
OTel collector service and logs
The collector logs to
C:\Program Files\observIQ OpenTelemetry Collector\log\collector.log
by default.
The standard error log for the collector process can be found at
C:\Program Files\observIQ OpenTelemetry Collector\log\observiq_collector.err
.
In Linux, to view logs from the collector, run
sudo tail -F /opt/observiq-otel-collector/log/collector.log
.
Common Linux OTel collector service commands:
To stop the OTel collector service, run
sudo systemctl stop observiq-otel-collector
.
To start the OTel collector service, run
sudo systemctl start observiq-otel-collector
.
To restart the OTel collector service, run
sudo systemctl restart observiq-otel-collector
.
To enable the OTel collector service on startup, run
sudo systemctl enable observiq-otel-collector
.
Restart the collector service for the configuration changes
When changing the configuration, you must restart the collector service for the configuration changes to take effect (
sudo systemctl restart observiq-otel-collector
).
Use a default sample configuration file
By default, a collector configuration file is located at
C:\Program Files\observIQ OpenTelemetry Collector\config.yaml
.
To download a sample configuration file and authentication token used by the
collector:
Open the Google SecOps console and go to
SIEM Settings
>
Collection Agent
.
Customize the following two sections in the configuration file:
Receiver
: specifies which logs the collector should collect and send to Google SecOps.
Exporter
: specifies the destination where the collector sends the logs.
The following exporters are supported:
Google SecOps exporter
: sends logs directly to Google SecOps ingestion API.
Google SecOps forwarder exporter
: sends logs to Google SecOps forwarder.
Cloud Logging exporter
: sends logs to (Cloud Logging).
In the exporter, customize the following:
customer_id
: Your Google SecOps customer ID.
endpoint
: Your Google SecOps regional endpoint.
creds
: Your authentication token.
Alternatively, you can use
creds_file_path
to reference the credentials file
directly. For the Windows configuration, escape the path with backslashes.
log_type
: Log type. We recommend that you select
WINDOWS_DNS
as the
Log Type
.
ingestion_labels
: Ingestion labels. These labels identify the logs in Google SecOps.
namespace
: Optional namespace.
Each log type requires you to configure an exporter.
Log-collection configuration samples
The following sections contain configuration samples for log collection.
Send Windows events and sysmon directly to Google SecOps
Configure these parameters in the sample:
chronicleexporter
namespace
ingestion_labels
log_type
customer_id
creds
Sample configuration:
receivers:
  windowseventlog/sysmon:
    channel: Microsoft-Windows-Sysmon/Operational
    raw: true
  windowseventlog/security:
    channel: security
    raw: true
  windowseventlog/application:
    channel: application
    raw: true
  windowseventlog/system:
    channel: system
    raw: true

processors:
  batch:

exporters:
  chronicle/sysmon:
    endpoint: malachiteingestion-pa.googleapis.com
    creds: '{
  "type": "service_account",
  "project_id": "malachite-projectname",
  "private_key_id": "abcdefghijklmnopqrstuvwxyz123456789",
  "private_key": "-----BEGIN PRIVATE KEY-----abcdefg-----END PRIVATE KEY-----\n",
  "client_email": "account@malachite-projectname.iam.gserviceaccount.com",
  "client_id": "123456789123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/account%40malachite-projectname.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}' 
    log_type: 'WINDOWS_SYSMON'
    override_log_type: false
    raw_log_field: body
    customer_id: 'dddddddd-dddd-dddd-dddd-dddddddddddd'
  chronicle/winevtlog:
    endpoint: malachiteingestion-pa.googleapis.com
    creds: '{
  "type": "service_account",
  "project_id": "malachite-projectname",
  "private_key_id": "abcdefghijklmnopqrstuvwxyz123456789",
  "private_key": "-----BEGIN PRIVATE KEY-----abcdefg-----END PRIVATE KEY-----\n",
  "client_email": "account@malachite-projectname.iam.gserviceaccount.com",
  "client_id": "123456789123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/account%40malachite-projectname.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}'
    log_type: 'WINEVTLOG'
    override_log_type: false
    raw_log_field: body
    customer_id: 'dddddddd-dddd-dddd-dddd-dddddddddddd'

service:
  pipelines:
    logs/sysmon:
      receivers: [windowseventlog/sysmon]
      processors: [batch]
      exporters: [chronicle/sysmon]
    logs/winevtlog:
      receivers: 
        - windowseventlog/security
        - windowseventlog/application
        - windowseventlog/system
      processors: [batch]
      exporters: [chronicle/winevtlog]
Send Windows events and syslog directly to Google SecOps
Configure these parameters in the sample:
windowseventlogreceiver
tcplogreceiver
listen_address
chronicleexporter
namespace
ingestion_labels
log_type
customer_id
creds
Sample configuration:
receivers:
    tcplog:
      listen_address: "0.0.0.0:54525"
    windowseventlog/source0__application:
        attributes:
            log_type: windows_event.application
        channel: application
        max_reads: 100
        poll_interval: 1s
        raw: true
        start_at: end
    windowseventlog/source0__security:
        attributes:
            log_type: windows_event.security
        channel: security
        max_reads: 100
        poll_interval: 1s
        raw: true
        start_at: end
    windowseventlog/source0__system:
        attributes:
            log_type: windows_event.system
        channel: system
        max_reads: 100
        poll_interval: 1s
        raw: true
        start_at: end
exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        creds: '{ json blob for creds }'
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        ingestion_labels:
            env: dev
        log_type: <applicable_log_type>
        namespace: testNamespace
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - windowseventlog/source0__system
                - windowseventlog/source0__application
                - windowseventlog/source0__security
            exporters:
                - chronicle/chronicle_w_labels
        logs/source1__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Send Windows events and syslog to Google SecOps forwarder
Configure these parameters in the sample:
windowseventlogreceiver
tcplogreceiver
listen_address
chronicleforwarder
endpoint
Sample configuration:
receivers:
tcplog:
    listen_address: "0.0.0.0:54525"
    windowseventlog/source0__application:
        attributes:
            log_type: windows_event.application
        channel: application
        max_reads: 100
        poll_interval: 1s
        raw: true
        start_at: end
    windowseventlog/source0__security:
        attributes:
            log_type: windows_event.security
        channel: security
        max_reads: 100
        poll_interval: 1s
        raw: true
        start_at: end
    windowseventlog/source0__system:
        attributes:
            log_type: windows_event.system
        channel: system
        max_reads: 100
        poll_interval: 1s
        raw: true
        start_at: end
exporters:
    chronicleforwarder/forwarder:
        export_type: syslog
        raw_log_field: body
        syslog:
            endpoint: 127.0.0.1:10514
            transport: udp
service:
    pipelines:
        logs/source0__forwarder-0:
            receivers:
                - windowseventlog/source0__system
                - windowseventlog/source0__application
                - windowseventlog/source0__security
            exporters:
                - chronicleforwarder/forwarder
        logs/source1__forwarder-0:
            receivers:
                - tcplog
            exporters:
                - chronicleforwarder/forwarder
Send syslog directly to Google SecOps
Configure these parameters in the sample:
tcplogreceiver
listen_address
chronicleexporter
namespace
ingestion_labels
log_type
customer_id
Creds
Sample configuration:
receivers:
  tcplog:
    listen_address: "0.0.0.0:54525"

exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        creds: '{ json blob for creds }'
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        ingestion_labels:
            env: dev
        log_type: <applicable_log_type>
        namespace: testNamespace
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Collect Windows events remotely and send them directly to Google SecOps
Configure these parameters in the sample:
windowseventlogreceiver
username
password
server
chronicleexporter
namespace
ingestion_labels
log_type
customer_id
creds
Sample configuration:
receivers:
    windowseventlog/system:
        channel: system
        max_reads: 100
        start_at: end
        poll_interval: 10s
        raw: true
        remote:
            username: "username"
            password: "password"
            server: "remote-server"
    windowseventlog/application:
        channel: application
        max_reads: 100
        start_at: end
        poll_interval: 10s
        raw: true
        remote:
            username: "username"
            password: "password"
            server: "server-ip"
    windowseventlog/security:
        channel: security
        max_reads: 100
        start_at: end
        poll_interval: 10s
        raw: true
        remote:
            username: "username"
            password: "password"
            server: "server-ip"
exporters:
    chronicle/chronicle_w_labels:
        compression: gzip
        creds: '{ json blob for creds }'
        customer_id: <customer_id>
        endpoint: malachiteingestion-pa.googleapis.com
        ingestion_labels:
            env: dev
        log_type: WINEVTLOG
        namespace: testNamespace
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - windowseventlog/system
                - windowseventlog/application
                - windowseventlog/security
            exporters:
                - chronicle/chronicle_w_labels
Send data to Cloud Logging
Configure the
credentials_file
parameter in the sample.
Sample configuration:
exporters:
  googlecloud:
    credentials_file: /opt/observiq-otel-collector/credentials.json
Query a SQL database and send the results to Google SecOps
Configure these parameters in the sample:
sqlqueryreceiver
chronicleexporter
namespace
ingestion_labels
log_type
customer_id
creds
Sample configuration:
receivers:
  sqlquery/source0:
    datasource: host=localhost port=5432 user=postgres password=s3cr3t sslmode=disable
    driver: postgres
    queries:
      - logs:
          - body_column: log_body
        sql: select * from my_logs where log_id > $$1
        tracking_column: log_id
        tracking_start_value: "10000"
processors:
  transform/source0_processor0__logs:
    error_mode: ignore
    log_statements:
      - context: log
        statements:
          - set(attributes["chronicle_log_type"], "POSTGRESQL") where true
exporters:
  chronicle/chronicle_sql:
    compression: gzip
    creds: '{
  "type": "service_account",
  "project_id": "malachite-projectname",
  "private_key_id": "abcdefghijklmnopqrstuvwxyz123456789",
  "private_key": "-----BEGIN PRIVATE KEY-----abcdefg-----END PRIVATE KEY-----\n",
  "client_email": "account@malachite-projectname.iam.gserviceaccount.com",
  "client_id": "123456789123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/account%40malachite-projectname.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}' 
    customer_id: customer_id
    endpoint: malachiteingestion-pa.googleapis.com
    log_type: POSTGRESQL
    namespace: null
    raw_log_field: body
    retry_on_failure:
      enabled: false
    sending_queue:
      enabled: false
service:
  pipelines:
    logs/source0_chronicle_sql-0:
      receivers:
        - sqlquery/source0
      processors:
        - transform/source0_processor0__logs
      exporters:
        - chronicle/chronicle_sql
Drop logs that match a regular expression
You can configure the collector to drop logs that match a regular expression. This is useful for filtering out unwanted logs, such as known errors or debugging messages.
To drop logs that match a regular expression, add a processor of type
filter/drop-matching-logs-to-Chronicle
to your configuration. This processor uses the
IsMatch
function to evaluate the log body against the regular expression. If the function returns
true
, the log is dropped.
The following example configuration drops logs that contain the strings
<EventID>10</EventID>
or
<EventID>4799</EventID>
in the log body.
You can customize the regular expression to match any pattern you need. The
IsMatch
function uses the
RE2 regular expression syntax
.
Sample configuration:
processors
:
filter/drop-matching-logs-to-Chronicle
:
error_mode
:
ignore
logs
:
log_record
:
-
(IsMatch(body, "<EventID>10</EventID>")) or (IsMatch(body, "<EventID>4799</EventID>"))
The following example adds the processor to the pipeline in the same configuration:
service
:
pipelines
:
logs/winevtlog
:
receivers
:
-
windowseventlog/security
-
windowseventlog/application
-
windowseventlog/system
processors
:
-
filter/drop-matching-logs-to-Chronicle
# Add this line
-
batch
exporters
:
[
chronicle/winevtlog
]
Bindplane operation and maintenance
This section describes routine operation and maintenance actions.
Verify an OTel configuration
To learn about how to verify the Bindplane OTel configuration, see
OTelBin
.
Collector release updates
Bindplane can poll
bindplane-otel-collector/releases
to detect new collector releases. This feature is optional.
You can disable GitHub polling by setting
agentVersions.syncInterval
to
0
in your Bindplane configuration:
agentVersions:
syncInterval: 0
Backup and disaster recovery
To learn about backup and disaster recovery with Bindplane, see
Bindplane resources
.
PostgreSQL backup and disaster recovery
To learn about PostgreSQL backup and disaster recovery with Bindplane, see
PostgreSQL documentation
.
BBolt backup and disaster recovery
To learn about BBolt (deprecated) backup and disaster recovery with Bindplane, see
BBolt Store documentation
.
Resilience and retry
Retry is enabled by default on all destinations that support it. By default, failed requests retry after five seconds and progressively back off for up to 30 seconds. After five minutes, requests are permanently dropped.
To learn more, see
Collector Resilience
.
Reduce log volume with the severity filter
To learn how to reduce log volume, see
Reduce Log Volume with the Severity Filter
.
Bindplane integrations with third-party collectors
Although Bindplane is more powerful when you use the
Bindplane
collector for collection at the edge, in most cases, Bindplane can remain within your existing infrastructure. For example, if you are already using Fluent Bit or Splunk Universal Forwarders, you can continue doing so.
Bindplane integration with Splunk
To learn about Splunk with Bindplane, see the following:
Using Splunk OTEL Collector with Bindplane
Using Splunk UF with Bindplane
Bindplane integrations with other third-party collectors
To learn about Bindplane integrations with third-party collectors, see
Connecting Other OpenTelemetry Collectors Using the OpAMP Extension
.
Silent Host Monitoring
Google Security Operations Silent Host Monitoring lets you create alerts for ingestion rate changes using Google Cloud Monitoring. It generates alerts per collector and notifies you when the ingestion rate falls below your defined threshold, signaling potential collector stoppages.
For information about using Bindplane for silent-host monitoring, see the following:
Google SecOps Silent Host Monitoring
Configure Bindplane for silent-host monitoring with Google Cloud Monitoring
Upgrade Bindplane on Linux
Running the install command without the
--init
flag at the end is sufficient to upgrade Bindplane. Run this script on your Bindplane server to upgrade Bindplane. To learn more, see
Upgrade, Downgrade or Uninstall Bindplane Server
.
Monitor Bindplane
To learn about how to monitor Bindplane, see
Monitoring Bindplane
.
Monitor Kubernetes in Bindplane
To learn about how to monitor Kubernetes in Bindplane, see
Kubernetes Monitoring
.
Additional documentation
To learn more about Bindplane (formerly known as observIQ), see the following:
Industry-Leading Observability and Security Powered by OpenTelemetry
Using Google SecOps with Bindplane Best Practices
Bindplane Solutions
Getting Started with Bindplane
Supported log types for Google Cloud
Filter by Condition Processor
Sources Available for Bindplane
Need more help?
Get answers from Community members and Google SecOps professionals.
