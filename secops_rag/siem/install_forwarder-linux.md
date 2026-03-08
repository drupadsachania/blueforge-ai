# Install and configure the forwarder

**Source:** https://docs.cloud.google.com/chronicle/docs/install/forwarder-linux/  
**Scraped:** 2026-03-05T09:37:36.095031Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Install and configure the forwarder
Supported in:
Google secops
SIEM
This document describes how to install and configure the Google Security Operations
forwarder on Linux and Windows systems using Docker.
The forwarder is a software component that you can
install on a machine or device, like a server, within your network. It
collects
log data and
forwards
that data to
your Google SecOps instance.
You can use the forwarder to send logs directly from your environment to
Google SecOps, without the need for cloud buckets or third-party APIs
for unsupported log types. The forwarder serves as a ready-to-deploy solution,
eliminating the need for manual integration with the ingestion API.
Google SecOps provides a Docker container for secure forwarder
deployment. You can run
and manage the Docker container on either physical or virtual machines.
System requirements
The following are general recommendations. For recommendations specific to your
system, contact Google SecOps
Support
.
Linux system
The forwarder is supported on various Linux distributions such as Debian, Ubuntu,
Red Hat, and Suse. For optimal performance, it is required to use Docker
version
20.10.21
or later.
RAM
: 1 GB RAM is required for each collected data type that
Google SecOps accepts
for ingestion. For example, if you specify four different collectors, you
need 4 GB RAM to collect data for all four.
CPU
: Two CPUs are sufficient to handle up to 10,000 events per second
(EPS) across all data types. If you anticipate your forwarder handling more than
10,000 EPS, allocate four to six CPUs.
Disk
: 20 GB of disk space is recommended, regardless of how much data the
forwarder handles.
Windows system
Forwarder is supported on Microsoft Windows Server 2022. For optimal performance,
it is required to use Docker version
20.10.21
or later.
RAM
: 1.5 GB RAM is required for each collected data type that
Google SecOps accepts
for ingestion. For example, if you specify four different collectors, you
need 6 GB RAM to collect data for all four.
CPU
: Two CPUs are sufficient to handle up to 10,000 events per second
(EPS) across all data types. If you anticipate your forwarder handling more
than 10,000 EPS, allocate four to six CPUs.
Disk
: 20 GB of disk space is recommended, regardless of how much data
the forwarder handles.
Before you begin
Before starting your forwarder implementation, take the following into consideration.
Google IP address ranges
When configuring the forwarder, you may need to adjust firewall settings that
involve specifying IP address ranges. The default domain IP ranges used by
Google APIs and services are allocated dynamically and change often. See
Obtain Google IP address ranges
for more information.
Verify the firewall configuration
If the forwarder container runs behind a firewall or authenticated proxy, grant 
outbound access to the following hosts:
Connection Type
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
eu-chronicle.googleapis.com
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
europe-west9-malachiteingestion-pa.googleapis.com
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
southamerica-east1-malachiteingestion-pa.googleapis.com
443
TCP
accounts.google.com
443
TCP
gcr.io
443
TCP
cloud.google.com/artifact-registry
443
TCP
oauth2.googleapis.com
443
TCP
storage.googleapis.com
443
Plan your implementation
Before you begin configuring the forwarder, plan your implementation. This will
help you align your data sources and configuration attributes with your security
objectives, infrastructure capabilities, and scalability requirements.
Determine the data to be ingested
Identify the most relevant data sources for your forwarder from the following
options:
Splunk
: Ideal if you already use Splunk for log management.
Syslog
: Versatile for system and application logs from various devices.
File
: Flexible for ingesting any log file.
Packet
: Offers deep network visibility by capturing raw traffic.
Kafka
: Ideal for high-volume and real-time log aggregation from distributed
systems.
WebProxy
: Ideal for insights into web traffic and user behaviour.
Limitation
Data feeds have a maximum log line size of 4 MB.
Determine the configuration
Before installing the forwarder, determine the following key attributes to ensure
a successful implementation.
Data compression
Data or log compression reduces network bandwidth consumption when transferring
logs to Google SecOps. However, it might cause an increase in CPU usage.
The optimal balance between bandwidth savings and CPU usage depends on multiple
factors like log type, compressibility of the data, available CPU resources,
and your network bandwidth constraints.
For example, text-based logs typically compress well and can provide substantial
bandwidth savings with low CPU usage, while encrypted or binary data
might not compress efficiently and might incur higher CPU usage.
By default, log compression is disabled. Evaluate the trade-off based on your
specific environment and the nature of your log data.
Disk buffering
It is recommended to enable disk buffering. 
Disk buffering lets you buffer backlogged messages to disk instead of
memory, safeguarding against data loss in case of forwarder or host crashes.
However, enabling disk buffering can impact performance.
If disk buffering is disabled, the forwarder allocates 1 GB of memory (RAM) for each
log type (for example, per connector). The maximum allowed memory for disk
buffering is 4 GB.
Regular expression filters
Regular expression filters enable you to filter logs by matching patterns
against the raw log data. The filters use the
RE2 syntax
.
The filters must include a regular expression and, optionally, define a behavior
when there is a match.
Arbitrary labels
Labels are used to attach custom metadata to logs using key-value pairs.
You can configure labels for an entire forwarder or within a specific collector
of the forwarder. If both are present, collector level labels override forwarder
level labels if keys overlap.
Namespaces
You can use namespace labels to identify logs from distinct network segments and
to deconflict overlapping IP addresses. You can configure a namespace label for an
entire forwarder or within a specific collector of the forwarder. If both are
present, collector-level namespace overrides forwarder-level namespace.
Log type
Google SecOps supports a variety of log types. For a comprehensive list,
see
Supported data sets
.
Load balancing and high availability options
Load balancing is supported only for the syslog collection type.
The forwarder can be deployed in environments where a layer 4 load balancer is
installed between the data source and forwarder instances. This lets you
distribute log collection across multiple forwarders, enhancing reliability by
redirecting logs to a different forwarder in case of a failure.
The forwarder has a built-in HTTP server that responds to health checks from
load balancers and prevents log loss during startup and shutdown. You can configure
the HTTP server, load balancing, and high availability options to specify timeout
durations and status codes for health checks. This configuration is compatible
with both container-based deployments and load balancers.
Setting
Description
Graceful timeout
The amount of time for which new connections are accepted after the
forwarder returns an
unready
status in response to a health check.
This is also the time to wait between receiving a signal to stop and
actually beginning the shutdown of the server itself. This gives the
load balancer time to remove the forwarder from the pool.
Valid values are in seconds. For example, to specify 10 seconds, type
10.
Decimal values are not allowed.
Default:
15 seconds
Drain timeout
The amount of time the forwarder waits for active connections to
close on their own before they are closed by the
server. For example, to specify 5 seconds, type
5.
Decimal values are not allowed.
Default:
10 seconds
Port
The port number that the HTTP server listens on for health checks
from the load balancer. The value must be between 1,024 to 65,535.
Default:
8080
IP address or hostname
The IP address or a hostname that can be resolved to an IP address,
that the server should listen to.
Default:
0.0.0.0 (the local system)
Read timeout
Used to tune the HTTP server. Typically, does not need to be changed
from the default setting. The maximum time allowed to read
the entire request, both the header and the body. You can set both
the
read timeout
field and the
read header
timeout
field.
Default:
3 seconds
Read header timeout
Used to tune the HTTP server. Typically, does not need to be changed
from the default setting. The maximum time allowed to read
request headers. The connection's read deadline is reset after
reading the header.
Default:
3 seconds
Write timeout
Used to tune the HTTP server. Typically, does not need to be changed
from the default setting. The maximum time allowed to send
a response. It is reset when a new request header is read.
Default:
3 seconds
Idle timeout
Used to tune the HTTP server. Typically, does not need to be changed
from the default setting. The maximum time to wait for the
next request when idle connections are enabled. If the
idle
timeout
field is set to zero, the value of the
read
timeout
field is used. If both are zero, the
read
header timeout
field is used.
Default:
3 seconds
Available status code
The status code the forwarder returns when a liveness check is
received and the forwarder is available. Container schedulers and
orchestrators often send liveness checks.
Default:
204
Ready status code
The status code that the forwarder returns when it is ready to accept
traffic in either of the following situations:
A readiness check is received from a container scheduler or
orchestrator.
A health check is received from a load balancer.
Default:
204
Unready status code
The status code the forwarder returns when it is not ready to accept
traffic.
Default:
503
Step 1: Define the forwarder configuration
Each deployed forwarder requires a forwarder configuration file. A
forwarder configuration file specifies the settings to transfer the data to
your Google SecOps instance. We recommend that you generate a new
configuration file for every host to
maintain clear distinctions between the collectors associated with each one.
Google Cloud customizes these configuration files with specific metadata for
each forwarder instance. You can modify these files to match your
specific requirements and incorporate details about the types of logs you want
to ingest.
You can generate a forwarder configuration file either through the UI, through
the API, or manually.
The UI provides a graphical interface for configuring
forwarders and is the recommended method for creating a forwarder configuration.
This is the easiest way to get started and does not require any
programming. To download the configuration file using the Google SecOps user
interface, see
Manage forwarder configurations through the
Google SecOps UI
.
The API provides a programmatic way to configure forwarders. To download
forwarder configuration programmatically, see
Forwarder Management API
.
You can create the configuration file manually and add the configuration
options to it. We recommend using the UI method for generating the
configuration file to ensure accuracy and minimize potential errors. To
generate the file manually, see
Manage forwarder configuration file manually
.
Step 2: Install Docker
This section describes how to install Docker on your system.
Docker authentication with artifact registry
As part of the docker installation, you need to authenticate the docker. You can 
authenticate the docker using Google Cloud CLI Command Line Interface (CLI) or, 
if you're unable to install the Google Cloud CLI (Command Line Interface),
by creating a new service account JSON in the VM.
Method one: Use Google Cloud CLI Command Line Interface (CLI)
Run the following command to authenticate Docker:
gcloud auth configure-docker gcr.io
Method two: Create and download a new service account JSON in the Virtual machine (VM).
Use this method if you're unable to install the Google Cloud CLI (Command Line Interface).
Run the following command to authenticate Docker:
cat key.json | docker login -u _json_key --password-stdin https://gcr.io
To learn more about additional methods for Docker authentication, see
:
Configure authentication to Artifact Registry for Docker
Linux system
Docker is open source and all the necessary documentation is available from the
open source Docker community. For instructions on Docker installation, see
Install Docker Engine
.
To check if Docker is installed properly on your system, execute the following
command (requires elevated privileges):
docker ps
The following response indicates that Docker has been installed properly:
CONTAINER ID  IMAGE  COMMAND  CREATED  STATUS   PORTS   NAMES
Windows system
Start Windows PowerShell with administrator privileges and check network
connectivity to Google Cloud by following these
steps:
Click
Start
.
Type
PowerShell
and right-click
Windows PowerShell
.
Click
Run as administrator
.
Run the following command:
C:\> test-netconnection <host> -port <port>
The command output indicates that the
TcpTestSucceeded
status is
true
.
Example:
C:\> test-netconnection malachiteingestion-pa.googleapis.com -port 443
ComputerName     :  malachiteingestion-pa.googleapis.com
RemoteAddress    : 198.51.100.1
RemotePort       : 443
InterfaceAlias   : Ethernet
SourceAddress    : 203.0.113.1
TcpTestSucceeded : True
To install Docker, do the following on your Windows server.
Enable the Microsoft Windows container feature:
Install-WindowsFeature containers -Restart
Execute the following command in PowerShell Administrator mode to install
Docker CE:
Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/microsoft/Windows-Containers/Main/helpful_tools/Install-DockerCE/install-docker-ce.ps1" -o install-docker-ce.ps1

.\install-docker-ce.ps1
Test the Docker command line interface by running the command
docker
ps
, which returns a list of running containers. If Docker is not installed
properly, an error is displayed.
For more information, see
Get started: Prep Windows for containers
.
For enterprise deployments,
install Mirantis Container Runtime
,
also known as Docker EE.
Step 3: Install the forwarder
This section describes how to install the forwarder using a Docker container.
Step 3a: Move configuration files to forwarder directory
The first step in the forwarder installation process involves placing the
necessary configuration files within the designated forwarder directory.
Linux system
Place the configuration files in the forwarder directory by following these steps:
Connect to the Linux forwarder host using terminal.
Change directory to the home directory that runs the Docker
container.
Create a directory to store the forwarder configuration files.
mkdir /opt/chronicle/'
CONFIG
'
You can replace the directory name,
CONFIG
with any name of your choice. Ensure
that you use the same directory name while running the
docker run
command.
Change the directory.
cd /opt/chronicle/config
After the files are transferred, ensure that the configuration files are
located in the
/opt/chronicle/config
directory.
ls -l
Windows system
Create a
C:\config
folder and place the configuration files in it. You can
replace the folder name,
config
, with any name of your choice. Ensure
that you use the same folder name while running the
docker run
command.
Step 3b: Run the forwarder
After the configuration files are placed within the designated forwarder
directory, you can start the forwarder
or upgrade to the latest version of the
Google SecOps container.
If you are upgrading the container, clean up any previous Docker runs by
executing the following commands.
docker stop '
cfps
'
docker rm '
cfps
'
In the example, the Docker container name is
cfps
.
To start the forwarder
for the first time or to upgrade to the latest version of the
Google SecOps container, do the following:
Obtain the latest Docker image from Google Cloud:
Linux system:
docker pull gcr.io/chronicle-container/cf_production_stable
Windows system:
docker pull gcr.io/chronicle-container/cf_production_stable_windows
Start the forwarder from the Docker container:
Linux system:
docker run \
  --detach \
  --name cfps \
  --restart=always \
  --log-opt max-size=100m \
  --log-opt max-file=10 \
  --net=host \
  -v /opt/chronicle/config:/opt/chronicle/external \
  gcr.io/chronicle-container/cf_production_stable
(Optional for the Linux system) When starting the forwarder from the Docker container, you have the option to mount a specific subdirectory from
/var/log/
.
To mount a specific subdirectory, add the following line to the command, and replace the
<parser-name>
placeholder with the name of the directory on the host system from which logs should be collected:
-v /var/log/<parser-name>:/opt/chronicle/edr \
Linux system (
including
the option to mount a specific subdirectory):
`
docker
run
\
--
detach
\
--
name
cfps
\
--
restart
=
always
\
--
log
-
opt
max
-
size
=
100
m
\
--
log
-
opt
max
-
file
=
10
\
--
net
=
host
\
-
v
/
opt
/
chronicle
/
config
:
/
opt
/
chronicle
/
external
\
-
v
/
var
/
log
/
<
parser
-
name
>
:
/
opt
/
chronicle
/
edr
\
gcr
.
io
/
chronicle
-
container
/
cf_production_stable
`
Windows system:
docker run `
    --detach `
    --name cfps `
    --restart=always `
    --log-opt max-size=100m `
    --log-opt max-file=10 `
    -p 0.0.0.0:10515-10520:10515-10520/udp `
    -v C:\config\:C:/opt/chronicle/external `
    gcr.io/chronicle-container/cf_production_stable_windows
The
--log-opt
options are available since
Docker
1.13
. These options limit the size of the container log files and
must be used as long as the Docker version that you use supports them.
Manage the forwarder
The following sections provide guidance on managing your forwarder.
View forwarder logs
To view the forwarder logs, execute the following command:
docker logs cfps
To view the path of the file in which the logs are stored, execute the
following command:
docker inspect --format='{{.LogPath}}'
CONTAINER_NAME
To view the live running logs, execute the following command:
docker logs cfps -f
To store the logs in a file, execute the following command:
docker logs cfps &> logs.txt
Uninstall the forwarder
The following Docker commands help you to stop, uninstall, or remove the forwarder.
To stop or uninstall the forwarder container, execute the following command:
docker stop cfps
To remove the forwarder container, execute the following command:
docker rm cfps
Update the forwarder
The forwarder consists of two components, each with an update process as follows:
Forwarder Bundle
: This component is updated automatically, eliminating
the need for a restart.
Forwarder Docker image
: Updates to this component are performed manually.
You'll need to stop the current forwarder instance and start a new one, as
described in
Step 3b
.
Forwarder ingestion guides for specific datasets
To learn how a particular dataset is ingested using forwarders, see the
following:
Install Carbon Black Event Forwarder
Collect Cisco ASA firewall logs
Collect Corelight Sensor logs
Collect Fluentd logs
Collect Linux auditd and Unix system logs
Collect Microsoft Windows AD data
Collect Microsoft Windows DHCP data
Collect Microsoft Windows DNS data
Collect Microsoft Windows Event data
Collect Microsoft Windows Sysmon data
Collect osquery logs
Collect OSSEC logs
Collect Palo Alto Networks firewall logs
Collect Splunk CIM logs
Collect Zeek logs
Need more help?
Get answers from Community members and Google SecOps professionals.
