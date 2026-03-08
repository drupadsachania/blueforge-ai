# Google SecOps forwarder executable for Windows

**Source:** https://docs.cloud.google.com/chronicle/docs/install/forwarder-windows/  
**Scraped:** 2026-03-05T09:47:13.657479Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Google SecOps forwarder executable for Windows
Supported in:
Google secops
SIEM
This document describes how to install and configure the Google SecOps forwarder on Microsoft
Windows.
Customize the configuration files
Based on the information you submitted prior to deployment, Google Cloud
provides you with an executable file and an optional configuration file for the
Google SecOps forwarder. The executable file should only be run on the host it
was configured for. Each executable file includes configuration specific to the
Google SecOps forwarder instance on your network. If you need to alter the configuration, contact Google SecOps
Support
.
System requirements
The following are general recommendations. For recommendations specific to your
system, contact Google SecOps
Support
.
Windows Server version: The Google SecOps forwarder is supported
on the following versions of Microsoft Windows Server:
2008 R2
2012 R2
2016
RAM: 1.5 GB for each collected data type. For example, endpoint detection and response
(EDR), DNS, and DHCP are all separate data types. You need 4.5 GB of RAM to collect data for
all three.
CPU: 2 CPUs are sufficient to handle less than 10,000 events per second (EPS) (total for
all data types). If you expect to forward more than 10,000 EPS, 4 to 6 CPUs are necessary.
Disk: 20 GB of disk space is required, regardless of how much data the Google SecOps forwarder
handles. The Google SecOps forwarder does not buffer to disk by default, but it is recommended to enable disk buffering.
You can buffer the disk by adding
write_to_disk_buffer_enabled
and
write_to_disk_dir_path
parameters in the config file.
For example:
-
<
collector
>
:
common
:
...
write_to_disk_buffer_enabled
:
true
write_to_disk_dir_path
:
<
var>your_path
<
/
var
>
...
Google IP address ranges
You might need the IP address range to open when setting up a Google SecOps forwarder configuration, 
such as when setting up the configuration for your firewall. 
It's not possible for Google to provide a specific list of IP addresses. 
However, you can
obtain Google IP address ranges
.
Verify the firewall configuration
If you have firewalls or authenticated proxies in between the Google SecOps forwarder container and
the internet, they require rules to allow access to the following Google Cloud hosts:
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
You can check network connectivity to Google Cloud using the following steps:
Start Windows PowerShell with Administrator privileges (Click
Start
, type
PowerShell
, right-click
Windows PowerShell
, and click
Run as administrator
).
Run the following command.
TcpTestSucceeded
should return true.
C:\> test-netconnection <host> -port <port>
For example:
C:\> test-netconnection malachiteingestion-pa.googleapis.com -port 443
ComputerName     : malchiteingestion-pa.googleapis.com
RemoteAddress    : 198.51.100.202
RemotePort       : 443
InterfaceAlias   : Ethernet
SourceAddress    : 10.168.0.2
TcpTestSucceeded : True
You can also use the Google SecOps forwarder to check network connectivity:
Start Command Prompt with administrator privileges (Click
Start
, type
Command Prompt
, right-click
Command Prompt
, and click
Run as Administrator
).
To verify network connectivity, run the Google SecOps forwarder with the
-test
option.
C:\> .\chronicle_forwarder.exe -test
Verify network connection succeeded!
Install the Google SecOps forwarder on Windows
On Windows, the Google SecOps forwarder executable needs to be installed as a service.
Copy the
chronicle_forwarder.exe
file and the configuration file to a working directory.
Start Command Prompt with administrator privileges (Click
Start
, type
Command Prompt
, right-click
Command Prompt
, and click
Run as Administrator
).
To install the service, navigate to the working directory you created in step 1 and run the following command:
C:\> .\chronicle_forwarder.exe -install -config
FILE_NAME
Replace
FILE_NAME
with the name of the configuration file
provided to you.
The service is installed to
C:\Windows\system32\ChronicleForwarder
.
To start the service, run the following command:
C:\> sc.exe start chronicle_forwarder
Verify the Google SecOps forwarder is running
The Google SecOps forwarder should have a network connection open on port 443 and your data should be displayed in the Google SecOps web interface within minutes.
You can verify that the Google SecOps forwarder is running using any of the following methods:
Task Manager: Navigate to the
Processes
tab >
Background processes
>
chronicle_forwarder
.
Resources Monitor: On the
Network
tab, the
chronicle_forwarder.exe
application should be listed under
Network Activity
(whenever the
chronicle_forwarder.exe
application connects to  Google Cloud), under TCP Connections, and under Listening Ports.
View forwarder logs
Google SecOps forwarder log files are stored in the
C:\Windows\Temp
folder. The log files begin with
chronicle_forwarder.exe.win-forwarder
.
The log files provide a variety of information, including when the forwarder was
started and when it began sending data to Google Cloud.
Uninstall the Google SecOps forwarder
To uninstall the Google SecOps forwarder service, complete the following steps:
Open Command Prompt in administrator mode.
Stop the Google SecOps forwarder service:
SERVICE_NAME
:
chronicle_forwarder
TYPE
:
10
WIN32_OWN_PROCESS
STATE
:
4
RUNNING
(
STOPPABLE
,
PAUSABLE
,
ACCEPTS_SHUTDOWN
)
WIN32_EXIT_CODE
:
0
(
0x0
)
SERVICE_EXIT_CODE
:
0
(
0x0
)
CHECKPOINT
:
0x0
WAIT_HINT
:
0x0
Navigate to the
C:\Windows\system32\ChronicleForwarder
directory and uninstall the Google SecOps forwarder service:
C:\> .\chronicle_forwarder.exe -uninstall
Upgrade the Google SecOps forwarder
To upgrade the Google SecOps forwarder while continuing to use your current configuration file, complete the following steps:
Open Command Prompt in administrator mode.
Copy your configuration file from the
C:\Windows\system32\ChronicleForwarder
directory to another directory.
Stop the Google SecOps forwarder:
C:\> sc.exe stop chronicle_forwarder
Uninstall the Google SecOps forwarder service and application:
C:\> .\chronicle_forwarder.exe --uninstall
Delete all files in the
C:\windows\system32\ChronicleForwarder
directory.
Copy the new
chronicle_forwarder.exe
application and the original configuration file to a working directory.
From the working directory, run the following command:
C:\> .\chronicle_forwarder.exe -install -config configFileProvidedToYou
Start the service:
C:\ sc.exe start chronicle_forwarder
Collect Splunk data
Contact Google SecOps
Support
to update your Google SecOps forwarder 
configuration file to forward your Splunk data to Google Cloud.
Collect syslog data
The Google SecOps forwarder can operate as a syslog server, meaning you can 
configure any appliance or server that supports sending syslog data over a TCP or UDP connection 
to forward their data to the Google SecOps forwarder. You can control exactly what 
data the appliance or server sends to the Google SecOps forwarder which can then forward the data to Google Cloud.
The Google SecOps forwarder configuration file specifies which ports to monitor for 
each type of forwarded data (for example, port 10514). By default, the Google SecOps forwarder 
accepts both TCP and UDP connections. 
Contact Google SecOps
Support
to update your Google SecOps forwarder configuration file to support syslog.
Toggle data compression
Log compression reduces network bandwidth consumption when transferring logs to Google SecOps.
However, compression might cause an increase in CPU usage. The tradeoff between CPU usage and
bandwidth depends on many factors, including the type of log data, the compressibility of that
data, the availability of CPU cycles on the host running the forwarder, and the need for reducing
network bandwidth consumption.
For example, text based logs compress well and can provide substantial bandwidth savings
with low CPU usage. However, encrypted payloads of raw packets do not compress well and incur
higher CPU usage.
Since most of the log types ingested by the forwarder are efficiently compressible, log
compression is enabled by default to reduce bandwidth consumption. However, if the increased CPU
usage outweighs the benefit of the bandwidth savings, you can disable compression 
by setting the
compression
field to
false
in the Google SecOps forwarder configuration file as shown in the following example:
compression
:
false
url
:
malachiteingestion
-
pa
.
googleapis
.
com
:
443
identity
:
identity
:
collector_id
:
10479925
-
878
c
-
11
e7
-
9421
-
10604
b7abba1
customer_id
:
abcd4bb9
-
878
b
-
11
e7
-
8455
-
12345
b7cb5c1
secret_key
:
|
{
"type"
:
"service_account"
,
...
Enable TLS for syslog configurations
You can enable Transport Layer Security (TLS) for the syslog connection to the Google SecOps
forwarder. In the Google SecOps forwarder configuration file, specify the
location of your certificate and certificate key as shown in the following
example:
certificate
C:/opt/chronicle/external/certs/edb3ae966a7bbe1f.pem
certificate_key
C:/opt/chronicle/external/certs/forwarder.key
Based on the example shown, the Google SecOps forwarder configuration would
be modified as follows:
collectors:
- syslog:
    common:
      enabled: true
      data_type: WINDOWS_DNS
      data_hint:
      batch_n_seconds: 10
      batch_n_bytes: 1048576
  tcp_address: 0.0.0.0:10515
  connection_timeout_sec: 60
  certificate: "C:/opt/chronicle/external/certs/edb3ae966a7bbe1f.pem"
  certificate_key: "C:/opt/chronicle/external/certs/forwarder.key"
You can create a certs directory under the configuration directory and store the
certificate files there.
Collect packet data
The Google SecOps forwarder can capture packets directly from a network interface using Npcap on Windows systems.
Packets are captured and sent to Google Cloud instead of log entries. Capture is done from a local interface only.
Contact Google SecOps
Support
to update your Google SecOps forwarder configuration file to support packet capture.
To run a Packet Capture (PCAP) forwarder, you need the following:
Install Npcap on the Microsoft Windows host.
Grant the Google SecOps forwarder root or administrator privileges to monitor the network interface.
No command-line options are needed.
On the Npcap installation, enable WinPcap compatibility mode.
To configure a PCAP forwarder, Google Cloud needs the GUID for the interface used to capture packets. 
Run
getmac.exe
on the machine where you plan to install the Google SecOps forwarder 
(either the server or the machine listening on the span port) and send the output to Google SecOps.
Alternatively, you could modify the configuration file. Locate the PCAP section and 
replace the GUID value shown next to interface with GUID displayed from running getmac.exe.
For example, here is an original PCAP section:
common
:
enabled
:
true
data_type
:
PCAP_DNS
batch_n_seconds
:
10
batch_n_bytes
:
1048576
interface
:
\
Device
\
NPF_
{
1
A7E7C8B
-
DD7B
-
4
E13
-
9637
-
0437
AB1A12FE
}
bpf
:
udp
port
53
Here is the output from running
getmac.exe
:
C:\>getmac.exe
  Physical Address    Transport Name
  ===========================================================================
  A4-73-9F-ED-E1-82   \Device\Tcpip_{2E0E9440-ABFF-4E5B-B43C-E188FCAD1234}
And finally, here is the revised PCAP section with the new GUID:
- pcap:
       common:
     enabled: true
         data_type: PCAP_DNS
     batch_n_seconds: 10
         batch_n_bytes: 1048576
       interface: \Device\NPF_{2E0E9440-ABFF-4E5B-B43C-E188FCAD9734}
     bpf: udp port 53
Collect WebProxy data
The Google SecOps forwarder can capture WebProxy data directly from a network
interface using Npcap and send it to Google Cloud.
To enable WebProxy data capture for your system, contact Google SecOps
Support
.
Before you run a WebProxy forwarder, do the following:
Install Npcap on the Microsoft Windows host. Enable WinPcap compatibility
mode during the installation.
Grant root or administrator privileges to the Google SecOps forwarder
to monitor the network interface.
To configure a WebProxy forwarder, Google Cloud needs the GUID for the
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
-
webproxy
:
common
:
enabled
:
true
data_type
:
<
Your
LogType
>
batch_n_seconds
:
10
batch_n_bytes
:
1048576
interface
:
\
Device
\
NPF_
{
2
E0E9440
-
ABFF
-
4
E5B
-
B43C
-
E188FCAD9734
}
bpf
:
tcp
and
dst
port
80
Need more help?
Get answers from Community members and Google SecOps professionals.
