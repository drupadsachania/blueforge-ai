# Manage forwarder configuration file manually

**Source:** https://docs.cloud.google.com/chronicle/docs/install/forwarder-configuration-manual/  
**Scraped:** 2026-03-05T09:16:23.625461Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage forwarder configuration file manually
Supported in:
Google secops
SIEM
This page describes how to create and modify a Google Security Operations forwarder
configuration file
manually. To configure the forwarder through the UI (recommended), see
Manage forwarder configurations through the Google SecOps UI
.
Each deployed Google SecOps forwarder requires a forwarder
configuration file.
A forwarder configuration file specifies the settings to transfer the data to
your Google SecOps instance.
For information about how to install and configure the Google SecOps
forwarder, system requirements, and details about configuration settings, see
Install and configure the forwarder
.
Before you begin
Before creating the configuration file,
plan your implementation
by understanding the types of data that can be ingested and the key attributes that
you need to define within the configuration file.
Create the configuration file
To create the configuration file manually, follow these steps:
Download the configuration files
through the UI.
Save the two files in the same directory using the following naming convention:
FORWARDER_NAME
.conf—Use this file to define the
configuration settings related to log ingestion.
FORWARDER_NAME
_auth.conf—Use this file to define the
authorization credentials.
Modify the files to include the configuration for your forwarder instance.
For details about the settings for each type of ingestion
mechanism, such as Splunk or Syslog, see
Define data types in your configuration file
.
For details about customizing each attribute, such as data compression or
disk buffering, see
Configure key attributes in the configuration file
.
Ensure that an entry exists for each input in the
FORWARDER_NAME
_auth.conf file even if the input doesn't have
corresponding authentication details. This is required to map the data correctly.
Any changes made to the configuration file will be automatically applied by the
forwarder within five minutes.
Sample configurations
You can reference the following configuration files as templates to create
your own.
Two file sample configuration
This two file system stores authentication credentials in a separate
file for enhanced security. You can store the
FORWARDER_NAME
.conf
file in a version control repository or any open configuration management system.
You can store the
FORWARDER_NAME
_auth.conf file directly in the physical or
virtual machine running the forwarder.
The following code sample shows the format of the configuration files for a
forwarder.
The
FORWARDER_NAME
.conf file
output:
  url: {region}-chronicle.googleapis.com (for example: us-chronicle.googleapis.com)
  use_dataplane : true
  project_id:
PROJECT_ID
region: {region} (for example: {us})
  identity:
    identity:
    collector_id:
COLLECTOR_ID
\
    customer_id:
CUSTOMER_ID
\

collectors:
  - syslog:
      common:
        enabled: true
        data_type: "WINDOWS_DHCP"
        data_hint:
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 0.0.0.0:10514
      udp_address: 0.0.0.0:10514
      connection_timeout_sec: 60
      tcp_buffer_size: 524288
  - syslog:
      common:
        enabled: true
        data_type: "WINDOWS_DNS"
        data_hint:
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 0.0.0.0:10515
      connection_timeout_sec: 60
      tcp_buffer_size: 524288
The
FORWARDER_NAME
_auth.conf file
output:
  identity:
    secret_key: |
      {
        "type": "service_account",
        "project_id": "
PROJECT_ID
" \,
        "private_key_id": "
PRIVATE_KEY_ID
" \,
        "private_key": "-----BEGIN PRIVATE KEY-----\\"
PRIVATE_KEY
" \n-----END PRIVATE KEY-----\n",
        "client_email": "
CLIENT_EMAIL
" \,
        "client_id": "
CLIENT_ID
" \,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/example-account-1%40example-account.iam.gserviceaccount.com"
      }

collectors:
  - syslog:
  - syslog:
      certificate: "../forwarder/inputs/testdata/localhost.pem"
      certificate_key: "../forwarder/inputs/testdata/localhost.key"
Single file sample configuration
output:
  url: us-chronicle.googleapis.com
  use_dataplane: true
  project_id:
PROJECT_ID
region: us
    identity:
    collector_id: COLLECTOR_ID \
    customer_id: CUSTOMER_ID \
    secret_key: |
      {
        "type": "service_account",
        "project_id": "
PROJECT_ID
" \,
        "private_key_id": "
PRIVATE_KEY_ID
" \,
        "private_key": "-----BEGIN PRIVATE KEY-----\ "
PRIVATE_KEY
" \n-----END PRIVATE KEY-----\n",
        "client_email": "
CLIENT_EMAIL
" \,
        "client_id": "
CLIENT_ID
" \,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/malachite-test-1%40malachite-test.iam.gserviceaccount.com"
      }

collectors:
  - syslog:
      common:
        enabled: true
        data_type: "WINDOWS_DHCP"
        data_hint:
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 0.0.0.0:10514
      udp_address: 0.0.0.0:10514
      connection_timeout_sec: 60
      tcp_buffer_size: 524288
  - syslog:
      common:
        enabled: true
        data_type: "WINDOWS_DNS"
        data_hint:
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 0.0.0.0:10515
      connection_timeout_sec: 60
      certificate: "../forwarder/inputs/testdata/localhost.pem"
      certificate_key: "../forwarder/inputs/testdata/localhost.key"
      tcp_buffer_size: 524288
Convert from single file to two files system
If you are using a single configuration file and want to move to the two file
system, do the following:
Create a copy of your existing configuration file.
Save one file as the
FORWARDER_NAME
.conf file and delete
the authorization credentials from the file.
Save the other file as
FORWARDER_NAME
_auth.conf file and
delete all the non-authorization data from the file. You can use the
sample configuration
for reference. Make sure that you follow
the naming convention and other guidelines mentioned in the section
Customize the configurations
.
Define data types in your configuration file
The following sections help you configure the Google SecOps
forwarder to ingest different types of data, which is
forwarded to the Google SecOps instance.
Splunk data
You can configure the Google SecOps forwarder to forward your Splunk
data to Google SecOps.
Google Cloud configures Google SecOps forwarder with the
following information to forward your data from Splunk:
URL for the Splunk REST API (for example, https://10.0.113.15:8089).
Splunk queries to generate data for each of the required data types (for example, index=dns).
FORWARDER_NAME
.conf
output:
collectors:
  - splunk:
      common:
        enabled: true
        data_type: WINDOWS_DNS
        data_hint: "#fields ts      uid     id.orig_h       id.orig_p       id.resp_h         id.resp_p       proto   trans_id        query   qclass  qclass_name"
        batch_n_seconds: 10
        batch_n_bytes: 819200
      url: https://127.0.0.1:8089
      is_ignore_cert: true
      minimum_window_size: 10s
      maximum_window_size: 30s
      query_string: search index=* sourcetype=dns
      query_mode: realtime
Make your Splunk account credentials available to the Google SecOps
forwarder. You can do this by creating a
creds.txt
file.
To use a
creds.txt
file:
Create a local file for your Splunk credentials and name it
creds.txt
.
Place your username on the first line and the password on the second line:
cat creds.txt

myusername
mypassword
To use the Google SecOps forwarder to access a Splunk
instance, copy the
creds.txt
file to the config directory (the same
directory where the configuration files reside).
Linux
cp creds.txt /opt/chronicle/config/creds.txt
Windows
cp creds.txt c:/opt/chronicle/config/creds.txt
Verify that the
creds.txt
file is in the intended directory:
Linux
ls /opt/chronicle/config
Windows
ls c:/opt/chronicle/config
Syslog data
A forwarder can work as a Syslog server. You can configure any
server that supports sending Syslog data over a TCP or UDP
connection to forward their data to Google SecOps forwarder. You can
control the data that the server sends to the
forwarder and the forwarder can then forward
the data to Google SecOps.
The
FORWARDER_NAME
.conf
configuration file (provided by
Google Cloud) specifies which ports to monitor for each type of
forwarded data (for example, port 10514). By default, the Google SecOps
forwarder accepts both TCP and UDP connections.
You can customize the TCP buffer size. The default TCP buffer size is 64 KB. The
default and recommended value for
connection_timeout
is 60 seconds.
The TCP connection gets terminated if the connection is inactive for more than
60 seconds.
Configure rsyslog
To configure rsyslog, you need to specify a target for each port (for example,
each data type). The
following examples illustrate the rsyslog target configuration:
TCP log traffic:
dns.* @@192.168.0.12:10514
UDP log traffic:
dns.* @192.168.0.12:10514
You can refer to your system documentation for details.
Enable TLS for Syslog configurations
You can enable TLS for the Syslog connection to the Google SecOps
forwarder. In the forwarder configuration file
(
FORWARDER_NAME
.conf), specify the location of your own
generated certificate and certificate key as shown in the following example.
You can create a
certs
directory under the
configuration
directory and store the
certificate files in it.
Linux:
certificate
/opt/chronicle/external/certs/client_generated_cert.pem
certificate_key
/opt/chronicle/external/certs/client_generated_cert.key
Windows:
certificate
c:/opt/chronicle/external/certs/client_generated_cert.pem
certificate_key
c:/opt/chronicle/external/certs/client_generated_cert.key
Based on the example shown, modify the forwarder
configuration file (
FORWARDER_NAME
.conf) as follows:
Linux:
collectors:
- syslog:
   common:
     enabled: true
     data_type: WINDOWS_DNS
     data_hint:
     batch_n_seconds: 10
     batch_n_bytes: 1048576
   tcp_address: 0.0.0.0:10515
   tcp_buffer_size: 65536
   connection_timeout_sec: 60
   certificate: "/opt/chronicle/external/certs/client_generated_cert.pem"
   certificate_key: "/opt/chronicle/external/certs/client_generated_cert.key"
   minimum_tls_version: "TLSv1_3"
Windows:
collectors:
- syslog:
    common:
      enabled: true
      data_type: WINDOWS_DNS
      data_hint:
      batch_n_seconds: 10
      batch_n_bytes: 1048576
    tcp_address: 0.0.0.0:10515
    tcp_buffer_size: 65536
    connection_timeout_sec: 60
    certificate: "c:/opt/chronicle/external/certs/client_generated_cert.pem"
    certificate_key: "c:/opt/chronicle/external/certs/client_generated_cert.key"
    minimum_tls_version: "TLSv1_3"
The TLS version of the input request should be greater than
   the minimum TLS version. The minimum TLS version should be one of the
   following values: TLSv1_0, TLSv1_1, TLSv1_2, TLSv1_3.
File data
A file collector is designed to fetch logs from a file that is
bound to the Docker container. You can use this if you want to manually upload
logs from a single log file.
Start the Google SecOps forwarder from the Docker container to map
the load volume to the container:
Linux
docker run
--detach
--name cfps
--log-opt max-size=100m
--log-opt max-file=10
--net=host
-v /opt/chronicle/config:/opt/chronicle/external
-v /var/log/crowdstrike/falconhostclient:/opt/chronicle/edr
gcr.io/chronicle-container/cf_production_stable
Windows
docker run `
    --name cfps `
    --log-opt max-size=100m `
    --log-opt max-file=10 `
    -p 10514:10514 `
    -v c:/opt/chronicle/config:c:/opt/chronicle/external `
    -v c:/var/log/crowdstrike/falconhostclient:c:/opt/chronicle/edr `
     gcr.io/chronicle-container/cf_production_stable_windows
You can add multiple ports using multiple options or multiple ranges. For
example:
-p 3001:3000 -p 2023:2022
or
-p 7000-8000:7000-8000
.
The port numbers provided in the sample code are examples. Replace the port
numbers as per your requirement.
Based on the example, you can modify the Google SecOps forwarder
configuration (
FORWARDER_NAME
.conf
file) as follows:
Linux
collectors:
 - file:
      common:
        enabled: true
        data_type: CS_EDR
        data_hint:
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      file_path: /opt/chronicle/edr/sample.txt
      filter:
Windows
collectors:
  - file:
       common:
         enabled: true
         data_type: CS_EDR
         data_hint:
         batch_n_seconds: 10
         batch_n_bytes: 1048576
       file_path: c:/opt/chronicle/edr/sample.txt
       filter:
The
sample.txt
file should be present in the
/var/log/crowdstrike/falconhostclient
folder.
Flag configurations
skip_seek_to_end
(bool): This flag is set to
false
by default and the file
input only sends new log lines as input. Setting this to
true
causes all the
previous log lines to be sent again during forwarder restarts. This causes log
duplication. Setting this flag to
true
is helpful in certain
situations (for example, during outages), because restarting the forwarder sends the
missing log lines again.
poll
(bool): File collector uses the Tail library to check for any changes in
the file system. By setting this flag to
true
, the Tail library uses the polling
method instead of the default notify method.
Packet data
The Google SecOps forwarder can capture packets instead of log
entries, directly from a network interface.
Linux systems
Google SecOps forwarder can capture packets using libcap on Linux.
For more information on libcap, see
libcap - Linux manual page
.
Instead of log entries, raw network packets are captured and sent to
Google SecOps. This capture is limited to a local interface. To enable
packet capture for your system, contact
Google SecOps
Support
.
Google SecOps configures Google SecOps forwarder with the Berkeley
Packet Filter (BPF) expression that is used when capturing packets (for example, port 53
and not localhost). For more information, see
Berkeley packet filters
.
Windows systems
The Google SecOps forwarder can capture packets using Npcap on
Windows systems.
Instead of log entries, raw network packets are captured and sent to
Google SecOps. This capture is limited to a local interface. To configure
your Google SecOps forwarder for packet capture, contact
Google SecOps
Support
.
Requirements for a packet capture PCAP forwarder:
Install Npcap on the Microsoft Windows host.
Grant the Google SecOps forwarder root or administrator
privileges to monitor the network interface.
On the Npcap installation, enable WinPcap compatibility mode.
To configure a PCAP forwarder, Google Cloud needs the GUID for the
interface used to capture packets.
Run
getmac.exe
on the machine where you plan to install the
Google SecOps forwarder
(either the server or the machine listening on the span port) and send the
output to Google SecOps.
Alternatively, you could modify the configuration file. Locate the PCAP section and
replace the existing GUID value with GUID obtained from running
getmac.exe
.
For example, here is an original PCAP section:
- pcap:
      common:
        enabled: true
        data_type: PCAP_DNS
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      interface: \Device\NPF_{1A7E7C8B-DD7B-4E13-9637-0437AB1A12FE}
      bpf: udp port 53
Output from running
getmac.exe
:
C:\>getmac.exe
  Physical Address    Transport Name
  ===========================================================================
  A4-73-9F-ED-E1-82   \Device\Tcpip_{2E0E9440-ABFF-4E5B-B43C-E188FCAD1234}
Revised PCAP section with the new GUID:
- pcap:
      common:
        enabled: true
        data_type: PCAP_DNS
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      interface: \Device\NPF_{2E0E9440-ABFF-4E5B-B43C-E188FCAD9734}
      bpf: udp port 53
The
getmac.exe
output for Transport Name starts with
\Device\Tcpip
whereas
the comparable pcap section starts with
\Device\NPF
.
Data from Kafka topic
The Google SecOps forwarder supports ingesting data directly from Kafka
topics. You can deploy up to three forwarders and
pull data from the same Kafka topic by leveraging the concept of consumer groups
for efficient and parallel processing. For more information, see
Kafka
. For more information on Kafka consumer
groups, see
Kafka consumer
.
The following forwarder configuration shows how to set up the forwarder to ingest
data from the Kafka topics.
Linux
The
FORWARDER_NAME
.conf file
collectors:
   - kafka:
         common:
           batch_n_bytes: 1048576
           batch_n_seconds: 10
           data_hint: null
           data_type:
NIX_SYSTEM
enabled: true
         topic: example-topic
         group_id: chronicle-forwarder
         timeout: 60s
         brokers: ["broker-1:9092", "broker-2:9093"]
         tls:
           insecureSkipVerify: true
           certificate: "/path/to/cert.pem"
           certificate_key: "/path/to/cert.key"
   - syslog:
         common:
           batch_n_bytes: 1048576
           batch_n_seconds: 10
           data_hint: null
           data_type:
WINEVTLOG
enabled: true
         tcp_address: 0.0.0.0:30001
         connection_timeout_sec: 60
The
FORWARDER_NAME
_auth.conf file
collectors:
   - kafka:
         username: user
         password: password
   - syslog:
Windows
FORWARDER_NAME
.conf file
collectors:
- kafka:
      common:
        batch_n_bytes: 1048576
        batch_n_seconds: 10
        data_hint: null
        data_type:
NIX_SYSTEM
enabled: true
      topic: example-topic
      group_id: chronicle-forwarder
      timeout: 60s
      brokers: ["broker-1:9092", "broker-2:9093"]
      tls:
        insecureSkipVerify: true
        certificate: "c:/path/to/cert.pem"
        certificate_key: "c:/path/to/cert.key"
- syslog:
      common:
        batch_n_bytes: 1048576
        batch_n_seconds: 10
        data_hint: null
        data_type:
WINEVTLOG
enabled: true
      tcp_address: 0.0.0.0:30001
      connection_timeout_sec: 60
FORWARDER_NAME
_auth.conf file
collectors:
- kafka:
      username: user
      password: password
- syslog:
WebProxy data
The Google SecOps forwarder can capture WebProxy data directly from a
network interface.
Linux
The Google SecOps forwarder can capture WebProxy data using libcap
on Linux. For more information on libcap, see
libcap - Linux manual page
.
To enable WebProxy data capture for your system, contact
Google SecOps
Support
.
Modify the Google SecOps forwarder configuration (
FORWARDER_NAME
.conf
file)
as follows:
- webproxy:
         common:
           enabled : true
           data_type: <Your LogType>
           batch_n_seconds: 10
           batch_n_bytes: 1048576
         interface: any
         bpf: tcp and dst port 80
Windows
The forwarder can capture WebProxy data using Npcap and send it to Google Cloud.
To enable WebProxy data capture for your system, contact Google SecOps
Support
.
Before you run a WebProxy forwarder, follow these steps:
Install Npcap on the Microsoft Windows host. Enable WinPcap compatibility
mode during the installation.
Grant root or administrator privileges to the forwarder
to monitor the network interface.
Obtain the GUID for the
interface used to capture the WebProxy packets.
Run
getmac.exe
on the machine where you want to install the Google SecOps
forwarder and send the output to Google SecOps. Alternatively, you can
modify the configuration file. Locate the WebProxy section and replace the GUID
shown next to the interface with the GUID displayed after running
getmac.exe
.
Modify the Google SecOps forwarder configuration
(
FORWARDER_NAME
.conf
) file as follows:
- webproxy:
    common:
        enabled : true
        data_type: <Your LogType>
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      interface: \Device\NPF_{2E0E9440-ABFF-4E5B-B43C-E188FCAD9734}
      bpf: tcp and dst port 80
Configure key attributes in the configuration file
The following table lists important parameters used in the forwarder
configuration file.
Parameter
Description
data_type
The type of log data that the collector can collect and process.
metadata
Metadata, which overrides global metadata.
max_file_buffer_bytes
Maximum number of bytes that can be accumulated in the disk or file buffer.
The default value is
1073741824
,  which is 1 GB.
max_memory_buffer_bytes
Maximum number of bytes that can be accumulated in the memory buffer. The
 default value is
1073741824
, which is 1 GB.
write_to_disk_dir_path
The path to be used for file or disk buffer.
write_to_disk_buffer_enabled
If
true
, disk buffer is used instead of memory buffer. The
default value is
false
.
batch_n_bytes
Maximum number of bytes that can be accumulated by the collector after
 which the data is batched. The default value is
1048576
, which is
 1 MB.
batch_n_seconds
The number of seconds after which the data gathered by the collector is
batched. The default value is 11 seconds.
data_hint
Data format that the collector can receive (usually the log file header that
describes the format).
For an extensive list of parameters used in the configuration file, see
Forwarder configuration fields
and
Collector configuration fields
.
Data compression
By default, log compression is disabled. Enabling log compression might
reduce bandwidth consumption. However, enabling log compression might also
increase CPU usage. Evaluate the tradeoff based on your environment and log data.
To enable log compression, set the
compression
field to
true
in the Google SecOps forwarder configuration file as
shown in the following example:
The
FORWARDER_NAME
.conf file
output:
  compression: true
    url: malachiteingestion-pa.googleapis.com:443
    identity:
      identity:
      collector_id: 10479925-878c-11e7-9421-10604b7cb5c1
      customer_id: ebdc4bb9-878b-11e7-8455-10604b7cb5c1
...
The
FORWARDER_NAME
_auth.conf file
output:
  identity:
    secret_key: |
    {
     "type": "service_account",
...
    }
Disk buffering
Disk buffering lets you buffer backlogged messages to disk as opposed to
memory.
You can configure automatic memory buffering to use a dynamically shared buffer across
collectors, which deals better with spikes in traffic. To enable the dynamically
shared buffer, add the following in your forwarder config:
auto_buffer:
  enabled: true
  target_memory_utilization: 80
If automatic disk buffering is enabled but
target_memory_utilization
is not defined, it uses a default value
of
70
.
If you are running the forwarder using Docker, we recommend mounting a
separate volume from your configuration volume for isolation purposes. Additionally,
each input should be isolated with its own directory or volume to avoid
conflicts.
Sample configuration
The following configuration includes syntax to enable disk buffering:
collectors:
- syslog:
    common:
      write_to_disk_buffer_enabled: true
      # /buffers/
NIX_SYSTEM
is part of the external mounted volume for the
forwarder
      write_to_disk_dir_path: /buffers/
NIX_SYSTEM
max_file_buffer_bytes: 1073741824
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
NIX_SYSTEM
enabled: true
    tcp_address: 0.0.0.0:30000
    connection_timeout_sec: 60
- syslog:
    common:
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
WINEVTLOG
enabled: true
    tcp_address: 0.0.0.0:30001
    connection_timeout_sec: 60
Regular expression filters
Regular expression filters enable you to filter logs by matching patterns
against the raw log data. The filters employ the
RE2 syntax
.
The filters must include a regular expression and, optionally, define a behavior
when there is a match.
The default behaviour on a match is
block
. You can specify filters with
allow
behaviour. If you specify
an
allow
filter, the forwarder blocks any logs that don't match at least one
allow
filter.
It is possible to define an arbitrary number of filters.
Block
filters take
precedence over
allow
filters.
When filters are defined, they must be assigned a name. The names of active
filters will be reported to Google SecOps through forwarder health
metrics. Filters
defined at the root of the configuration are merged with filters defined at the
collector level. The collector level filters take precedence in cases of
conflicting names. If no filters are defined either at the root or collector
level, the behavior is to allow all logs.
Sample configuration
In the following forwarder configuration, the
WINEVTLOG
logs that
don't match the root filter (
allow_filter
) are blocked. Given the regular
expression, the filter only allows logs with priorities between 0 and 99.
However, any
NIX_SYSTEM
logs containing 'foo' or 'bar' are blocked,
despite the
allow_filter
. This is because the filters use a logical OR. All
logs are processed until a filter is triggered.
regex_filters:
  allow_filter:
    regexp: ^<[1-9][0-9]?$>.*$
    behavior_on_match: allow
collectors:
- syslog:
    common:
      regex_filters:
        block_filter_1:
          regexp: ^.*foo.*$
          behavior_on_match: block
        block_filter_2:
          regexp: ^.*bar.*$
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
NIX_SYSTEM
enabled: true
    tcp_address: 0.0.0.0:30000
    connection_timeout_sec: 60
- syslog:
    common:
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
WINEVTLOG
enabled: true
    tcp_address: 0.0.0.0:30001
    connection_timeout_sec: 60
Arbitrary labels
Labels are used to attach custom metadata to logs using key-value pairs.
You can configure labels for an entire forwarder or within a specific collector
of the forwarder. If both are present, collector level labels override forwarder
level labels if keys overlap.
Sample configuration
In the following forwarder configuration, the 'foo=bar' and 'meow=mix' key and
value pairs are both attached to
WINEVTLOG
logs, and the 'foo=baz' and
'meow=mix' key and value pairs are attached to the
NIX_SYSTEM
logs.
metadata:
  labels:
    foo: bar
    meow: mix
collectors:
syslog:
    common:
      metadata:
        labels:
          foo: baz
          meow: mix
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
NIX_SYSTEM
enabled: true
    tcp_address: 0.0.0.0:30000
    connection_timeout_sec: 60
syslog:
    common:
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
WINEVTLOG
enabled: true
    tcp_address: 0.0.0.0:30001
    connection_timeout_sec: 60
Namespaces
You can use namespace labels to identify logs from distinct network segments and
deconflict overlapping IP addresses.
Any namespace configured for the forwarder appears with the associated assets in
the Google SecOps user interface. You can also search for namespaces
using the Google SecOps Search feature.
For information about how to view namespaces in the Google SecOps
user interface, see
Asset namespaces
.
Sample configuration
In the following forwarder configuration, the
WINEVTLOG
logs are
attached to the FORWARDER namespace and
NIX_SYSTEM
logs are
attached to the CORPORATE namespace.
metadata:
  namespace: FORWARDER
collectors:
- syslog:
      common:
        metadata:
          namespace: CORPORATE
        batch_n_bytes: 1048576
        batch_n_seconds: 10
        data_hint: null
        data_type:
NIX_SYSTEM
enabled: true
      tcp_address: 0.0.0.0:30000
      connection_timeout_sec: 60
- syslog:
      common:
        batch_n_bytes: 1048576
        batch_n_seconds: 10
        data_hint: null
        data_type:
WINEVTLOG
enabled: true
      tcp_address: 0.0.0.0:30001
      connection_timeout_sec: 60
Load balancing and high availability options
You can configure the HTTP server, load balancing, and high availability options
under the server section of the forwarder configuration file. These options
support setting timeout durations and status codes returned in response to
health checks received in container scheduler and orchestration-based
deployments, as well as from load balancers.
Use the following URL paths for health, readiness, and liveness checks.
The
<host:port>
values are defined in the forwarder configuration.
http://<host:port>/meta/available
: Liveness checks for container
schedulers or orchestrators
http://<host:port>/meta/ready
: Readiness checks and load
balancer health checks
The following forwarder configuration is an example for load balancing and high
availability:
collectors:
- syslog:
    common:
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
NIX_SYSTEM
enabled: true
    tcp_address: 0.0.0.0:30000
    connection_timeout_sec: 60
- syslog:
    common:
      batch_n_bytes: 1048576
      batch_n_seconds: 10
      data_hint: null
      data_type:
WINEVTLOG
enabled: true
    tcp_address: 0.0.0.0:30001
    connection_timeout_sec: 60
server:
  graceful_timeout: 15s
  drain_timeout: 10s
  http:
    port: 8080
    host: 0.0.0.0
    read_timeout: 3s
    read_header_timeout: 3s
    write_timeout: 3s
    idle_timeout: 3s
    routes:
    - meta:
        available_status: 204
        ready_status: 204
        unready_status: 503
Configuration path
Description
server : graceful_timeout
The amount of time the forwarder returns a bad readiness/health check and
still accepts new connections. This is also the time to wait between
receiving a signal to stop and actually beginning the shutdown of the
server itself. This allows the load balancer time to remove the forwarder
from the pool.
server : drain_timeout
The amount of time the forwarder waits for active connections to
successfully close on their own before being closed by the server.
server : http : port
The port number that the HTTP server listens on for health checks from the
load balancer. Must be between 1024-65535.
server : http : host
The IP address, or hostname that can be resolved to IP addresses, that the
server should listen to. If empty, the default value is local system
(0.0.0.0).
server : http : read_timeout
Used to tune the HTTP server. Typically, does not need to be changed from
the default setting. The maximum amount of time allowed to read the entire
request, both the header and the body. You can set both read_timeout and
read_header_timeout.
server : http : read_header_timeout
Used to tune the HTTP server. Typically, does not need to be changed from
the default setting. The maximum amount of time allowed to read request
headers. The connection's read the deadline is reset after reading the
header.
server : http : write_timeout
Used to tune the HTTP server. Typically, does not need to be changed from
the default setting. The maximum amount of time allowed to send a response.
It is reset when a new request header is read.
server : http : idle_timeout
Used to tune the HTTP server. Typically, does not need to be changed from
the default setting. The maximum amount of time to wait for the next
request when idle connections are enabled. If idle_timeout is zero, the
value of read_timeout is used. If both are zero, the read_header_timeout is
used.
routes : meta : ready_status
The status code the forwarder returns when it is ready to accept the traffic
in either of the following situations:
Readiness check is received from a container scheduler or
orchestrator.
Health check is received from a traditional load balancer.
routes : meta : unready_status
The status code the forwarder returns when it is not ready to accept
traffic.
routes : meta : available_status
The status code the forwarder returns when a liveness check is received
and the forwarder is available. Container schedulers or orchestrators often send
liveness checks.
Need more help?
Get answers from Community members and Google SecOps professionals.
