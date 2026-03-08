# Collect Linux auditd and AIX systems logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/auditd/  
**Scraped:** 2026-03-05T09:57:41.700504Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Linux auditd and AIX systems logs
Supported in:
Google secops
SIEM
This parser handles Linux audit logs in SYSLOG format, transforming them into UDM. It processes both JSON-formatted and plain text log messages, extracting fields using grok, XML parsing, and JSON parsing techniques, and mapping them to appropriate UDM fields based on the event type. The parser also handles specific audit log formats from AIX systems and enriches the UDM with additional fields like
security_result
and intermediary details.
Before you begin
Ensure that you have a Google Security Operations instance.
Ensure that you have root access to the Auditd host.
Ensure that you installed rsyslog on the Auditd host.
Ensure that you have a Windows 2012 SP2 or later or Linux host with systemd.
If running behind a proxy, ensure that the firewall
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
        namespace: auditd
        raw_log_field: body
service:
    pipelines:
        logs/source0__chronicle_w_labels-0:
            receivers:
                - tcplog
            exporters:
                - chronicle/chronicle_w_labels
Restart Bindplane Agent to apply the changes using the following command:
sudo systemctl bindplane restart
Exporting Syslog from Auditd
Access the machine from which you want to export audit logs.
Open the Auditd configuration file (typically located at
/etc/audit/auditd.conf
).
sudo
vi
/etc/audit/auditd.conf
Find or add the following line(s) to configure auditd:
active = yes
output = syslog
log_format = ENRICHED
dispatcher = /sbin/audispd
Optional: Specify Syslog Facility: Add or modify the following line in
auditd.conf
:
```none
syslog_facility = LOG_AUTHPRIV
```
Open audispd configuration file (typically located at
/etc/audisp/plugins.d/syslog.conf
):
sudo
vi
/etc/audisp/plugins.d/syslog.conf
Find or add the following line(s) to configure audispd:
active = yes
direction = out
path = builtin_syslog
type = builtin
args = LOG_INFO
format = string
Restart Auditd service to apply the changes:
sudo
systemctl
restart
auditd
Use a tool like
tail
to monitor the syslog and verify that Auditd logs are being sent:
tail
-f
/var/log/syslog
|
grep
auditd
# Follow syslog and filter for auditd messages (path may vary depending on your system)
Edit the
rsyslog.conf
or create a custom configuration:
sudo
vi
/etc/rsyslog.d/50-audit-forwarding.conf
Add a rule to forward logs:
if $programname == 'auditd' then @@<Bindplane_Agent>:<Bindplane_Port>
Use
@
for UDP or
@@
for TCP
Replace
<BindPlane_Agent>
with your server's IP/hostname.
Replace
<BindPlane_Port>
with your server's Port.
Restart rsyslog service to apply the changes:
sudo
systemctl
restart
rsyslog
Supported Linux Auditing System (AuditD) Sample Logs
SYSLOG + KV (Linux AuditD)
events_for_log_entry
:
{
events
:
{
timestamp
:
{
seconds
:
1718778607
nanos
:
898000000
}
idm
:
{
read_only_udm
:
{
metadata
:
{
product_log_id
:
"5512409"
event_timestamp
:
{
seconds
:
1718778607
nanos
:
898000000
}
event_type
:
USER_LOGIN
vendor_name
:
"Linux"
product_name
:
"AuditD"
product_event_type
:
"USER_AUTH"
}
principal
:
{
hostname
:
"sec-dev-01.internal"
user
:
{
userid
:
"0"
user_display_name
:
"secuser"
}
process
:
{
pid
:
"3306219"
}
asset
:
{
hostname
:
"sec-dev-01.internal"
ip
:
"192.168.1.5"
}
ip
:
"192.168.1.5"
application
:
"ssh"
platform
:
LINUX
}
target
:
{
user
:
{
userid
:
"0"
user_display_name
:
"secuser"
}
process
:
{
file
:
{
full_path
:
"/usr/sbin/secure_shell"
}
}
}
intermediary
:
{
hostname
:
"sec-dev-01.internal"
}
about
:
{
user
:
{
userid
:
"sysadmin"
user_display_name
:
"unset"
}
}
security_result
:
{
detection_fields
:
{
key
:
"AUID0"
value
:
"unset"
}
detection_fields
:
{
key
:
"UID0"
value
:
"sysadmin"
}
detection_fields
:
{
key
:
"acct0"
value
:
"secuser"
}
detection_fields
:
{
key
:
"addr0"
value
:
"192.168.1.5"
}
detection_fields
:
{
key
:
"auid0"
value
:
"sysadmin"
}
detection_fields
:
{
key
:
"exe0"
value
:
"/usr/sbin/secure_shell"
}
detection_fields
:
{
key
:
"grantors0"
value
:
"pam_unix"
}
detection_fields
:
{
key
:
"hostname0"
value
:
"192.168.1.5"
}
detection_fields
:
{
key
:
"msg0"
value
:
"op=PAM:authentication"
}
detection_fields
:
{
key
:
"pid0"
value
:
"3306219"
}
detection_fields
:
{
key
:
"res0"
value
:
"success"
}
detection_fields
:
{
key
:
"ses0"
value
:
"4294967295"
}
detection_fields
:
{
key
:
"terminal0"
value
:
"ssh"
}
detection_fields
:
{
key
:
"uid0"
value
:
"0"
}
detection_fields
:
{
key
:
"AUID_kv0"
value
:
"AUID0:unset"
}
detection_fields
:
{
key
:
"UID_kv0"
value
:
"UID0:sysadmin"
}
detection_fields
:
{
key
:
"acct_kv0"
value
:
"acct0:secuser"
}
detection_fields
:
{
key
:
"addr_kv0"
value
:
"addr0:192.168.1.5"
}
detection_fields
:
{
key
:
"auid_kv0"
value
:
"auid0:sysadmin"
}
detection_fields
:
{
key
:
"exe_kv0"
value
:
"exe0:/usr/sbin/secure_shell"
}
detection_fields
:
{
key
:
"grantors_kv0"
value
:
"grantors0:pam_unix"
}
detection_fields
:
{
key
:
"hostname_kv0"
value
:
"hostname0:192.168.1.5"
}
detection_fields
:
{
key
:
"msg_kv0"
value
:
"msg0:op=PAM:authentication"
}
detection_fields
:
{
key
:
"pid_kv0"
value
:
"pid0:3306219"
}
detection_fields
:
{
key
:
"res_kv0"
value
:
"res0:success"
}
detection_fields
:
{
key
:
"ses_kv0"
value
:
"ses0:4294967295"
}
detection_fields
:
{
key
:
"terminal_kv0"
value
:
"terminal0:ssh"
}
detection_fields
:
{
key
:
"uid_kv0"
value
:
"uid0:0"
}
summary
:
"authentication secuser"
action
:
ALLOW
action_details
:
"success"
}
network
:
{
session_id
:
"4294967295"
application_protocol
:
SSH
}
extensions
:
{
auth
:
{}
}
}
}
}
}
SYSLOG (Generic)
events_for_log_entry
:
{
events
:
{
timestamp
:
{
seconds
:
1754848621
}
idm
:
{
read_only_udm
:
{
metadata
:
{
event_timestamp
:
{
seconds
:
1754848621
}
event_type
:
PROCESS_LAUNCH
vendor_name
:
"Linux"
product_name
:
"AuditD"
product_event_type
:
"CROND"
description
:
"(monitorsvc) CMD (/opt/monitor/bin/scheduler -j /opt/monitor/cache/jobs/check.jx)"
}
principal
:
{
hostname
:
"log-host-05"
user
:
{
userid
:
"monitorsvc"
}
process
:
{
pid
:
"124662"
}
asset
:
{
hostname
:
"log-host-05"
}
platform
:
LINUX
}
target
:
{
process
:
{
command_line
:
"/opt/monitor/bin/scheduler -j /opt/monitor/cache/jobs/check.jx"
}
}
intermediary
:
{
hostname
:
"log-host-05"
}
}
}
}
}
JSON (Cloud Storage Logging or Auditbeat)
eve
nts
_
f
or_log_e
ntr
y
:
{
eve
nts
:
{
t
imes
ta
mp
:
{
seco
n
ds
:
1611615589
nan
os
:
212000000
}
idm
:
{
read_o
nl
y_udm
:
{
me
ta
da
ta
:
{
produc
t
_log_id
:
"32946"
eve
nt
_
t
imes
ta
mp
:
{
seco
n
ds
:
1611615589
nan
os
:
212000000
}
collec
te
d_
t
imes
ta
mp
:
{
seco
n
ds
:
1609752843
nan
os
:
349722230
}
eve
nt
_
t
ype
:
SERVICE_START
ve
n
dor_
na
me
:
"Linux"
produc
t
_
na
me
:
"AuditD"
produc
t
_eve
nt
_
t
ype
:
"SERVICE_START"
}
addi
t
io
nal
:
{
f
ields
:
{
key
:
"insertId"
value
:
{
s
tr
i
n
g_value
:
"tf9cuofcnbn6i"
}
}
f
ields
:
{
key
:
"logName"
value
:
{
s
tr
i
n
g_value
:
"projects/prj-secops-dev/logs/auditd"
}
}
}
pri
n
cipal
:
{
hos
tna
me
:
"gce-test-web"
user
:
{
userid
:
"0"
}
process
:
{
pid
:
"1"
}
asse
t
:
{
hos
tna
me
:
"gce-test-web"
}
applica
t
io
n
:
"sysmgr"
pla
tf
orm
:
LINUX
}
tar
ge
t
:
{
process
:
{
f
ile
:
{
full
_pa
t
h
:
"/usr/bin/sysmgr"
}
}
cloud
:
{
projec
t
:
{
na
me
:
"prj-secops-dev"
}
}
resource
:
{
resource_sub
t
ype
:
"gce_instance"
produc
t
_objec
t
_id
:
"1000000000000000001"
a
ttr
ibu
te
:
{
cloud
:
{
availabili
t
y_zo
ne
:
"us-east4-a"
}
}
}
}
abou
t
:
{
user
:
{
userid
:
"9001"
user_display_
na
me
:
"unset"
}
}
securi
t
y_resul
t
:
{
de
te
c
t
io
n
_
f
ields
:
{
key
:
"AUID0"
value
:
"unset"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"UID0"
value
:
"secsvc"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"auid0"
value
:
"9001"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"comm0"
value
:
"sysmgr"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"exe0"
value
:
"/usr/bin/sysmgr"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"msg0"
value
:
"unit=gce-cert-renew"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"pid0"
value
:
"1"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"res0"
value
:
"success"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"ses0"
value
:
"4294967295"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"subj0"
value
:
"system_u:system_r:init_t:s0"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"uid0"
value
:
"0"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"AUID_kv0"
value
:
"AUID0:unset"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"UID_kv0"
value
:
"UID0:secsvc"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"auid_kv0"
value
:
"auid0:9001"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"comm_kv0"
value
:
"comm0:sysmgr"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"exe_kv0"
value
:
"exe0:/usr/bin/sysmgr"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"msg_kv0"
value
:
"msg0:unit=gce-cert-renew"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"pid_kv0"
value
:
"pid0:1"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"res_kv0"
value
:
"res0:success"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"ses_kv0"
value
:
"ses0:4294967295"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"subj_kv0"
value
:
"subj0:system_u:system_r:init_t:s0"
}
de
te
c
t
io
n
_
f
ields
:
{
key
:
"uid_kv0"
value
:
"uid0:0"
}
summary
:
"unit=gce-cert-renew success"
ac
t
io
n
:
ALLOW
ac
t
io
n
_de
ta
ils
:
"success"
}
net
work
:
{
sessio
n
_id
:
"4294967295"
}
}
}
}
}
JSON (Windows Event)
JSON
(Wi
n
dows
Eve
nt
)
eve
nts
_
f
or_log_e
ntr
y
:
{
eve
nts
:
{
t
imes
ta
mp
:
{
seco
n
ds
:
1711012395
nan
os
:
723000000
}
idm
:
{
read_o
nl
y_udm
:
{
me
ta
da
ta
:
{
eve
nt
_
t
imes
ta
mp
:
{
seco
n
ds
:
1711012395
nan
os
:
723000000
}
eve
nt
_
t
ype
:
USER_LOGIN
ve
n
dor_
na
me
:
"Microsoft"
produc
t
_
na
me
:
"Microsoft-Windows-Security-Auditing"
produc
t
_eve
nt
_
t
ype
:
"4624"
descrip
t
io
n
:
"An account was successfully logged on"
}
addi
t
io
nal
:
{
f
ields
:
{
key
:
"Message"
value
:
{
s
tr
i
n
g_value
:
"An account was successfully logged on."
"Subject:Security ID:S-1-0-0"
"Account Name:-... (omitted for brevity) ..."
"New Logon:Security ID:S-1-5-21-1234567890-123456789-1234567890-2001"
"Account Name:svc_log_collector"
"Account Domain:SEC_LAB... (omitted for brevity) ..."
"Network Information:"
"Workstation Name:DEV-WS-42"
"Source Network Address:172.16.1.100"
"Source Port:53856..."
}
}
f
ields
:
{
key
:
"Workstation Name"
value
:
{
s
tr
i
n
g_value
:
"DEV-WS-42"
}
}
}
pri
n
cipal
:
{
hos
tna
me
:
"DEV-WS-42"
process
:
{}
asse
t
:
{
hos
tna
me
:
"DEV-WS-42"
ip
:
"172.16.1.100"
}
ip
:
"172.16.1.100"
por
t
:
53856
labels
:
{
key
:
"Workstation Name"
value
:
"DEV-WS-42"
}
}
tar
ge
t
:
{
user
:
{
userid
:
"svc_log_collector"
wi
n
dows_sid
:
"S-1-5-21-1234567890-123456789-1234567890-2001"
}
admi
n
is
trat
ive_domai
n
:
"SEC_LAB"
}
i
nter
mediary
:
{
hos
tna
me
:
"win-server-01"
}
securi
t
y_resul
t
:
{
rule_
na
me
:
"EventID: 4624"
ac
t
io
n
:
ALLOW
}
ex
tens
io
ns
:
{
au
t
h
:
{
mecha
n
ism
:
MECHANISM_UNSPECIFIED
}
}
}
}
}
}
SYSLOG + XML (Solaris AuditD)
{
"events_for_log_entry"
:
{
"events"
:
{
"timestamp"
:
{
"seconds"
:
1735824379
},
"idm"
:
{
"read_only_udm"
:
{
"metadata"
:
{
"product_log_id"
:
"1638473100678580410"
,
"event_timestamp"
:
{
"seconds"
:
1735824379
},
"event_type"
:
"PROCESS_LAUNCH"
,
"vendor_name"
:
"Linux"
,
"product_name"
:
"AuditD"
,
"product_version"
:
"2"
,
"product_event_type"
:
"AUE_EXECVE"
,
"description"
:
"<record version=
\"
2
\"
event=
\"
23
\"
host=
\"
192.0.2.1
\"
iso8601=
\"
1638473100678580410
\">\n
"
"  <ntrs hostname=
\"
sanitized-host-01
\"
eventstring=
\"
AUE_EXECVE
\"
timestamp=
\"
1638473100.678580410
\"
ppid=
\"
2853
\"
><
/ntrs
>
\n
"
"  <path>/usr/bin/find</path>
\n
"
"  <attribute mode=
\"
100555
\"
uid=
\"
0
\"
gid=
\"
2
\"
fsid=
\"
256
\"
nodeid=
\"
722
\"
device=
\"
18446744073709551615
\"
/
>
\n
"
"  <exec_args>
\n
"
"    <arg>find</arg>
\n
"
"    <arg>/var/log/secure</arg>
\n
"
"    <arg>-type</arg>
\n
"
"    <arg>f</arg>
\n
"
"    <arg>-xdev</arg>
\n
"
"    <arg>-prune</arg>
\n
"
"    <arg>-name</arg>
\n
"
"    <arg>secure_data_file.txt</arg>
\n
"
"    <arg>-mtime</arg>
\n
"
"    <arg>+3</arg>
\n
"
"    <arg>-exec</arg>
\n
"
"    <arg>rm</arg>
\n
"
"    <arg>-f</arg>
\n
"
"    <arg>{}</arg>
\n
"
"    <arg>;</arg>
\n
"
"  </exec_args>
\n
"
"  <path>/lib/ld.so.1</path>
\n
"
"  <attribute mode=
\"
100755
\"
uid=
\"
0
\"
gid=
\"
2
\"
fsid=
\"
256
\"
nodeid=
\"
449952
\"
device=
\"
18446744073709551615
\"
/
>
\n
"
"  <subject audit-uid=
\"
99999
\"
uid=
\"
0
\"
gid=
\"
0
\"
ruid=
\"
0
\"
rgid=
\"
0
\"
pid=
\"
2871
\"
sid=
\"
1898719819
\"
tid=
\"
9307 196630 192.0.2.10
\"
/
>
\n
"
"  <return errval=
\"
0
\"
retval=
\"
0
\"
/
>
\n
"
"  <sequence seq-num=
\"
6849431
\"
/
>
\n
"
"</record>"
},
"principal"
:
{
"hostname"
:
"sanitized-host-01"
,
"user"
:
{
"userid"
:
"99999"
},
"asset"
:
{
"hostname"
:
"sanitized-host-01"
,
"ip"
:
"192.0.2.1"
},
"ip"
:
"192.0.2.1"
,
"platform"
:
"LINUX"
},
"target"
:
{
"process"
:
{
"parent_process"
:
{
"pid"
:
"2853"
},
"command_line"
:
"find /var/log/secure -type f -xdev -prune -name secure_data_file.txt -mtime +3 -exec rm -f {} ;"
}
},
"intermediary"
:
{
"hostname"
:
"internal-proxy.local"
},
"security_result"
:
{
"detection_fields"
:
[
{
"key"
:
"event"
,
"value"
:
"event: 23"
},
{
"key"
:
"uid"
,
"value"
:
"uid: 0"
},
{
"key"
:
"gid"
,
"value"
:
"gid: 0"
},
{
"key"
:
"ruid"
,
"value"
:
"ruid: 0"
},
{
"key"
:
"rgid"
,
"value"
:
"rgid: 0"
},
{
"key"
:
"pid"
,
"value"
:
"pid: 2871"
},
{
"key"
:
"sid"
,
"value"
:
"sid: 1898719819"
},
{
"key"
:
"tid"
,
"value"
:
"tid: 9307 196630 192.0.2.10"
},
{
"key"
:
"seq_num"
,
"value"
:
"seq_num: 6849431"
},
{
"key"
:
"errval"
,
"value"
:
"errval: 0"
},
{
"key"
:
"retval"
,
"value"
:
"retval: 0"
},
{
"key"
:
"path"
,
"value"
:
"path: /usr/bin/find"
},
{
"key"
:
"device"
,
"value"
:
"device: 18446744073709551615"
},
{
"key"
:
"mode"
,
"value"
:
"mode: 100555"
},
{
"key"
:
"fsid"
,
"value"
:
"fsid: 256"
},
{
"key"
:
"nodeid"
,
"value"
:
"nodeid: 722"
}
]
}
}
}
}
}
}
UDM mapping table
Log field
UDM mapping
Remark
acct
target.user.user_display_name
The value of
acct
from the raw log is mapped to the
target.user.user_display_name
field in the UDM.  This represents the account associated with the event.
addr
principal.ip
The value of
addr
from the raw log is mapped to the
principal.ip
field in the UDM. This represents the IP address of the principal involved in the event.
additional.fields
additional.fields
Additional fields from parsed key-value pairs or labels are added to the
additional.fields
array in the UDM.
agent.googleapis.com/log_file_path
(Not Mapped)
This label is present in some raw logs but is not mapped to the IDM object in the UDM.
algo
(Not used in this example)
Although present in the parser and some raw logs, this field isn't used in the provided example and doesn't appear in the final UDM.
application
principal.application
Derived from the
terminal
field in the raw log or other fields like
exe
depending on the log type. Represents the application involved.
arch
security_result.about.platform_version
The architecture from the raw log's
arch
field is mapped to
security_result.about.platform_version
.
auid
about.user.userid
,
security_result.detection_fields.auid
The audit user ID (
auid
) is mapped to
about.user.userid
and added as a detection field in
security_result
.
cmd
target.process.command_line
The command from the raw log's
cmd
field is mapped to
target.process.command_line
.
collection_time
(Not Mapped)
This field is the log collection time and is not mapped to the IDM object in the UDM.
comm
principal.application
The command name (
comm
) is mapped to
principal.application
.
COMMAND
target.process.command_line
compute.googleapis.com/resource_name
principal.hostname
The resource name from this label is mapped to
principal.hostname
.
create_time
(Not Mapped)
This field is not mapped to the IDM object in the UDM.
cwd
security_result.detection_fields.cwd
The current working directory (
cwd
) is added as a detection field in
security_result
.
data
(Processed)
The
data
field contains the main log message and is processed by the parser to extract various fields. It is not directly mapped to a single UDM field.
exe
target.process.file.full_path
The executable path (
exe
) is mapped to
target.process.file.full_path
.
extensions.auth.type
extensions.auth.type
The authentication type is set by the parser logic based on the event type.  Often set to
MACHINE
or
AUTHTYPE_UNSPECIFIED
.
fp
network.tls.client.certificate.sha256
The fingerprint (
fp
) is parsed to extract the SHA256 hash and mapped to
network.tls.client.certificate.sha256
.
_Item_Id
metadata.product_log_id
insertId
(Not Mapped)
This field is not mapped to the IDM object in the UDM.
jsonPayload.message
(Processed)
This field contains the main log message in JSON format and is processed by the parser.
key
security_result.about.registry.registry_key
The key field is mapped to
security_result.about.registry.registry_key
.
labels
(Processed)
Labels from the raw log are processed and mapped to various UDM fields or added to
additional.fields
.
logName
(Not Mapped)
This field is not mapped to the IDM object in the UDM.
metadata.product_event_type
SECCOMP
The key exchange curve is extracted from the raw log and mapped to this field.
msg
security_result.summary
The message (
msg
) is often used to populate the
security_result.summary
field.
network.application_protocol
network.application_protocol
Set by the parser logic based on the event type (e.g., SSH, HTTP).
network.direction
network.direction
Set by the parser logic based on the event type (e.g., INBOUND, OUTBOUND).
network.ip_protocol
network.ip_protocol
Set by the parser logic, usually to TCP for SSH events.
network.session_id
network.session_id
Mapped from the
ses
field or derived from other fields.
network.tls.cipher
network.tls.cipher
The cipher information is extracted from the raw log and mapped to this field.
network.tls.curve
network.tls.curve
The key exchange curve is extracted from the raw log and mapped to this field.
pid
principal.process.pid
,
target.process.pid
The process ID (
pid
) is mapped to either
principal.process.pid
or
target.process.pid
depending on the context.
ppid
principal.process.parent_process.pid
,
target.process.parent_process.pid
The parent process ID (
ppid
) is mapped to either
principal.process.parent_process.pid
or
target.process.parent_process.pid
depending on the context.
principal.asset.hostname
principal.asset.hostname
Copied from
principal.hostname
.
principal.asset.ip
principal.asset.ip
Copied from
principal.ip
.
principal.platform
principal.platform
Set by the parser logic based on the operating system (e.g., LINUX).
principal.port
principal.port
The port number associated with the principal.
principal.user.group_identifiers
principal.user.group_identifiers
Group IDs associated with the principal user.
process.name
target.process.file.full_path
receiveTimestamp
(Not Mapped)
This field is the log receive timestamp and is not mapped to the IDM object in the UDM.
res
security_result.action_details
The result (
res
) is mapped to
security_result.action_details
.
_Resource_Id
target.resource.product_object_id
resource.labels
(Not Mapped)
These labels are present in some raw logs but are not mapped to the IDM object in the UDM.
resource.type
(Not Mapped)
This field is present in some raw logs but is not mapped to the IDM object in the UDM.
security_result.action
security_result.action
Set by the parser logic based on the
res
field (e.g., ALLOW, BLOCK).
security_result.detection_fields
security_result.detection_fields
Various fields from the raw log are added as key-value pairs to this array for context.
security_result.rule_id
security_result.rule_id
Set by the parser logic, often to the
type_name
for syscall events.
security_result.severity
security_result.severity
Set by the parser logic based on the severity level in the raw log.
security_result.summary
security_result.summary
A summary of the event, often derived from the
msg
field or other relevant fields.
ses
network.session_id
The session ID (
ses
) is mapped to
network.session_id
.
source
(Not Mapped)
This field contains metadata about the log source and is not mapped to the IDM object in the UDM.
subj
(Processed)
The subject field (
subj
) is processed to extract user and security context information.
syscall
security_result.about.labels.Syscall
The syscall number is added as a label within
security_result.about
.
target.administrative_domain
target.administrative_domain
The domain of the target user.
target.group.group_display_name
target.group.group_display_name
The name of the target group.
target.ip
target.ip
The IP address of the target.
target.port
target.port
The port number associated with the target.
target.process.command_line
target.process.command_line
The command line of the target process.
target.resource.type
target.resource.type
The type of the target resource, set by the parser logic (e.g., CREDENTIAL, SETTING).
target.user.attribute.permissions
target.user.attribute.permissions
Permissions related to the target user.
target.user.group_identifiers
target.user.group_identifiers
Group IDs associated with the target user.
target.user.userid
target.user.userid
The user ID of the target.
TenantId
metadata.product_deployment_id
textPayload
(Processed)
The text payload of the log, processed by the parser to extract various fields.
timestamp
metadata.event_timestamp
The timestamp of the event.
tty
security_result.about.labels.tty
The tty is added as a label within
security_result.about
.
type
metadata.product_event_type
The event type (
type
) is mapped to
metadata.product_event_type
.
uid
target.user.userid
The user ID (
uid
) is mapped to
target.user.userid
.
UDM mapping delta reference
On September 23, 2025, Google SecOps released a new version of the Okta parser, which includes significant changes to the mapping of Okta log fields to UDM fields and changes to the mapping of event types.
Log-field mapping delta
The following table lists the mapping delta for Okta log-to-UDM fields exposed prior to September 23, 2025 and subsequently (listed in the
Old mapping
and
Current mapping
columns, respectively).
Log field
Old mapping
Current mapping
Reference log sample
1.1.1.1
(ip address)
src.ip
principal.ip
"<163>Apr 10 09:00:05 hostname.com sshd[3318513]: Accepted password for abc from 1.1.1.1 port 33988 ssh2"
1.1.1.1
(ip address)
principal.ip
target.ip
"<29>Oct 5 08:37:16 abc ProxySG: E0000 Access Log HTTP (main): Connecting to server 1.1.1.1 on port 4433.(0) NORMAL_EVENT alog_stream_http.cpp 261"
abc
(user)
principal.user.userid
target.user.userid
"<85>Feb 27 08:26:55 offozcav login: FAILED LOGIN 1 FROM ::ffff:1.1.1.1 FOR abc, Authentication failure\r\n\r\n"
abc.abc
(user)
principal.user.userid
target.user.userid
"<86>Feb 27 08:29:19 offozcav login: LOGIN ON pts/43 BY
abc.abc FROM\r\n\r\n::ffff:1.1.1.1
"
COMMAND
principal.process.command_line
target.process.command_line
"<85>Sep 24 14:33:59 abc sudo: abc : \r\nTTY=unknown ; PWD=/abc ; USER=abc ; COMMAND=/sbin/iptables -t nat -nL \r\n--line-number"
exe
target.process.file.full_path
principal.process.file.full_path
_ItemId
additional.fields
metadata.product_log_id
metadata.product_event_type
PATH
SECCOMP
process.name
principal.process.file.full_path
target.process.file.full_path
_ResourceId
additional.fields
target.resource.product_object_id
TenantId
additional.fields
metadata.product_deployment_id
uid
principal.user.userid
target.user.userid
USER
principal.user.user_display_name
target.user.userid
"<85>Sep 24 14:33:59 abc sudo: abc : \r\nTTY=unknown ; PWD=/abc ; USER=abc ; COMMAND=/sbin/iptables -t nat -nL \r\n--line-number"
user
principal.user.userid
target.user.userid
"29>Jan 16 11:28:00 san-auth-1-irl2 tac_plus[17329]: login failure: user 1.1.1.1 (1.1.1.1) vty0"
user
principal.user.userid
target.user.userid
"<87>Jul 15 10:27:01 xpgjrconfdb01 crond[1045]: pam_unix(crond:account): expired password for user root (password aged)"
Event-type mapping delta
Multiple events that were classified before as generic event are now properly classified with meaningful event types.
The following table lists the delta for the handling of Okta event types prior to September 23, 2025 and subsequently (listed in the
Old event_type
and
Current event-type
columns respectively).
eventType from log
Old event_type
Current event_type
aix_event_type=CRON_Start
USER_LOGIN
PROCESS_LAUNCH
CRYPTO_KEY_USER
NETWORK_CONNECTION
USER_LOGIN
FILE_Mknod
USER_LOGIN
FILE_CREATION
FILE_Rename
USER_LOGIN
FILE_MODIFICATION
FILE_Stat
USER_LOGIN
FILE_OPEN
FILE_Unlink
USER_LOGIN
FILE_DELETION
FS_Chabc
USER_LOGIN
PROCESS_UNCATEGORIZED
FS_Mkdir
USER_LOGIN
FILE_CREATION
FS_Rmdir
USER_LOGIN
FILE_DELETION
PROC_Execute
USER_LOGIN
PROCESS_LAUNCH
type=ANOM_ABEND
STATUS_UPDATE
PROCESS_TERMINATION
type=ANOM_PROMISCUOUS
SETTING_MODIFICATION
type=CRED_REFR
USER_LOGIN
USER_CHANGE_PERMISSIONS
type=PROCTILE
PROCESS_UNCATEGORIZED
PROCESS_LAUNCH
type=SERVICE_START
USER_RESOURCE_ACCESS
SERVICE_START
type=SERVICE_STOP
USER_RESOURCE_ACCESS
SERVICE_STOP
type=USER_ACCT
USER_LOGIN/SETTING_MODIFICTION
USER_LOGIN
type=USER_MGMT
SETTING_MODIFICATION/GROUP_MODIFICATION
GROUP_MODIFICATION
USER_ERR
USER_LOGOUT
USER_LOGIN
Additional changes
Removed duplicate mapping of
res
from
security_result.description
. It's captured in
security_result.action_details
.
Removed unnecessary
auditd_msg_data
from additional fields.
Removed unnecessary
auditd_msg_data
from
security_result.summary
.
When
type=ADD_USER
, removed duplicate mapping of
acct
to
target.user.display_name
. It's already mapped under
target.user.userid
.
Removed duplicate mapping of
comm
from
principal.process.command_line
and
principal.process.file.names
. It's captured in
principal.application
.
Removed duplicate mapping of
target.hostname
when the value is there in
principal
.
Removed unnecessary hard-coded mapping of
target.resource.type
to
SETTING
.
Removed about labels mappings since it is deprecated.
Corrected mapping: IP's now route to
principal.ip
, not
principal.hostname
.
Fixed the repetition of events being generated.
Need more help?
Get answers from Community members and Google SecOps professionals.
