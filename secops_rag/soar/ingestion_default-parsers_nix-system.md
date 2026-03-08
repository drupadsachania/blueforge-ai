# Collect Nix System logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/nix-system/  
**Scraped:** 2026-03-05T09:48:42.276965Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Nix System logs
This document describes how you can collect Nix System logs by enabling Google Cloud telemetry ingestion to Google Security Operations and how log fields of Nix System logs map to Google Security Operations Unified Data Model (UDM) fields.
For more information, see
Data ingestion to Google Security Operations
.
A typical deployment consists of Nix System logs enabled for ingestion to Google Security Operations. Each customer deployment might differ from this representation and might be more complex.
The deployment contains the following components:
Google Cloud
: The Google Cloud services and products from which you collect logs.
Nix System logs
: The Nix System logs that are
enabled for ingestion into Google Security Operations.
Google Security Operations
: Google Security Operations retains and analyzes the logs from Nix System.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information into this document applies to the parser
with the
NIX_SYSTEM
ingestion label.
The following log source paths are supported by the Nix System parser:
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/nginx/access.log
/var/log/nginx/error.log
/var/log/rkhunter.log
/var/log/auth.log
/var/log/kern.log
/var/log/rundeck/service.log
/var/log/samba/log.winbindd
/var/log/mail.log
/var/log/audit/audit.log
/var/log/syslog
/var/log/openvpnas.log
Before you begin
Set up NixOS on Google Compute Engine. For more information, see
Install NixOS on GoogleCompute Engine
.
Ensure that all systems in the deployment architecture are configured in the UTC time zone.
Configure Google Cloud to ingest Nix System logs
Nix System is deployed on Google Cloud. You must configure Google Cloud to ingest Nix System logs to Google Security Operations, see
Ingest Google Cloud logs to Google Security Operations
.
If you encounter issues when you ingest Nix System logs, contact
Google Security Operations support
.
Supported Nix System log formats
The Nix System parser supports logs in JSON,SYSLOG+JSON and KV format.
Supported Nix System sample logs
JSON
{
  "_path": "ssl",
  "_system_name": "zeek-sensor",
  "_write_ts": "2021-12-21T00:58:02.468587Z",
  "ts": "2021-12-21T00:58:02.440196Z",
  "uid": "CzXKYpiKYBEHtfte1",
  "id.orig_h": "198.51.100.0",
  "id.orig_p": 17682,
  "id.resp_h": "198.51.100.1",
  "id.resp_p": 443,
  "version": "TLSv13",
  "cipher": "TLS_AES_256_GCM_SHA384",
  "curve": "x25519",
  "server_name": "dummy.domain.com",
  "resumed": true,
  "established": true,
  "ja3": "598872011444709307b861ae817a4b60",
  "ja3_version": "771",
  "ja3_ciphers": "4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53",
  "ja3_extensions": "0-23-65281-10-11-35-16-5-13-18-51-45-43-27-17513-41",
  "ja3_ec": "29-23-24",
  "ja3_ec_fmt": "0",
  "ja3s": "2253c82f03b621c5144709b393fde2c9",
  "ja3s_version": "771",
  "ja3s_cipher": "4866",
  "ja3s_extensions": "43-51-41"
}
SYSLOG+JSON
<13>1 2021-12-21T23: 51: 25-08: 00 dummyhostname bro_http - - - {
  "ts": 1640159484.694295,
  "uid": "dummyuid",
  "id.orig_h": "198.51.100.0",
  "id.orig_p": 58729,
  "id.resp_h": "198.51.100.1",
  "id.resp_p": 8088,
  "trans_depth": 2284,
  "method": "POST",
  "host": "198.51.100.2",
  "uri": "/system/gateway",
  "version": "1.1",
  "user_agent": "Java/11.0.11",
  "request_body_len": 304,
  "response_body_len": 203,
  "status_code": 200,
  "status_msg": "OK",
  "tags": [],
  "orig_fuids": [
    "FefIdu4i8dzFTUONb5"
  ],
  "orig_mime_types": [
    "application/xml"
  ],
  "resp_fuids": [
    "Flqz7L3yyQR1eSN4Kf"
  ],
  "resp_mime_types": [
    "application/xml"
  ]
}
KV
<85>Aug 1 19:55:40 dummyhostname sshd[86907]: pam_sss(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=10.17.42.6 user=dummyuser
Field mapping reference
Field mapping reference: Event Identifier to Event Type for Audit logs
The following table lists the
Audit logs
log types and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
ADD_GROUP
GROUP_CREATION
ADD_USER
USER_CREATION
ANOM_ABEND
PROCESS_TERMINATION
ANOM_ACCESS_FS
FILE_READ
ANOM_ADD_ACCT
USER_CREATION
ANOM_AMTU_FAIL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_CRYPTO_FAIL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_DEL_ACCT
USER_DELETION
ANOM_EXEC
FILE_UNCATEGORIZED
ANOM_LOGIN_ACCT
USER_LOGIN
ANOM_LOGIN_FAILURES
USER_LOGIN
AUTH_VIOLATION
ANOM_LOGIN_LOCATION
USER_LOGIN
ANOM_LOGIN_SESSIONS
USER_LOGIN
ANOM_LOGIN_TIME
USER_LOGIN
ANOM_MAX_DAC
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_MAX_MAC
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_MK_EXEC
FILE_UNCATEGORIZED
ANOM_MOD_ACCT
USER_UNCATEGORIZED
ANOM_PROMISCUOUS
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_RBAC_FAIL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_RBAC_INTEGRITY_FAIL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ANOM_ROOT_TRANS
USER_CHANGE_PERMISSIONS
AVC
GENERIC_EVENT
AVC_PATH
GENERIC_EVENT
BPRM_FCAPS
USER_UNCATEGORIZED
CAPSET
PROCESS_UNCATEGORIZED
CHGRP_ID
GROUP_MODIFICATION
CHUSER_ID
USER_UNCATEGORIZED
CONFIG_CHANGE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
CRED_ACQ
USER_LOGIN
CRED_DISP
USER_LOGOUT
CRED_REFR
USER_LOGIN
CRYPTO_FAILURE_USER
SYSTEM_AUDIT_LOG_UNCATEGORIZED
CRYPTO_KEY_USER
USER_RESOURCE_ACCESS
CRYPTO_LOGIN
USER_LOGIN
CRYPTO_LOGOUT
USER_LOGOUT
CRYPTO_PARAM_CHANGE_USER
USER_CHANGE_PERMISSIONS
CRYPTO_REPLAY_USER
SYSTEM_AUDIT_LOG_UNCATEGORIZED
CRYPTO_SESSION
NETWORK_CONNECTION
CRYPTO_TEST_USER
SYSTEM_AUDIT_LOG_UNCATEGORIZED
CWD
SYSTEM_AUDIT_LOG_UNCATEGORIZED
DAC_CHECK
SYSTEM_AUDIT_LOG_UNCATEGORIZED
DAEMON_ABORT
PROCESS_TERMINATION
DAEMON_ACCEPT
NETWORK_CONNECTION
DAEMON_CLOSE
NETWORK_CONNECTION
DAEMON_CONFIG
SYSTEM_AUDIT_LOG_UNCATEGORIZED
DAEMON_END
PROCESS_TERMINATION
DAEMON_RESUME
PROCESS_UNCATEGORIZED
DAEMON_ROTATE
PROCESS_UNCATEGORIZED
DAEMON_START
PROCESS_LAUNCH
DEL_GROUP
GROUP_DELETION
DEL_USER
USER_DELETION
DEV_ALLOC
USER_RESOURCE_CREATION
DEV_DEALLOC
USER_RESOURCE_DELETION
EOE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
EXECVE
PROCESS_LAUNCH
FD_PAIR
SYSTEM_AUDIT_LOG_UNCATEGORIZED
FS_RELABEL
FILE_UNCATEGORIZED
GRP_AUTH
SYSTEM_AUDIT_LOG_UNCATEGORIZED
INTEGRITY_DATA
PROCESS_LAUNCH
INTEGRITY_HASH
PROCESS_LAUNCH
INTEGRITY_METADATA
PROCESS_LAUNCH
INTEGRITY_PCR
SYSTEM_AUDIT_LOG_UNCATEGORIZED
INTEGRITY_RULE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
INTEGRITY_STATUS
SYSTEM_AUDIT_LOG_UNCATEGORIZED
IPC
SYSTEM_AUDIT_LOG_UNCATEGORIZED
IPC_SET_PERM
SYSTEM_AUDIT_LOG_UNCATEGORIZED
KERNEL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
KERNEL_OTHER
SYSTEM_AUDIT_LOG_UNCATEGORIZED
LABEL_LEVEL_CHANGE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
LABEL_OVERRIDE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
LOGIN
USER_LOGIN
MAC_CIPSOV4_ADD
USER_UNCATEGORIZED
MAC_CIPSOV4_DEL
USER_UNCATEGORIZED
MAC_CONFIG_CHANGE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_IPSEC_EVENT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_MAP_ADD
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_MAP_DEL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_POLICY_LOAD
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_STATUS
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_UNLBL_ALLOW
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_UNLBL_STCADD
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MAC_UNLBL_STCDEL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MMAP
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MQ_GETSETATTR
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MQ_NOTIFY
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MQ_OPEN
SYSTEM_AUDIT_LOG_UNCATEGORIZED
MQ_SENDRECV
SYSTEM_AUDIT_LOG_UNCATEGORIZED
NETFILTER_CFG
SYSTEM_AUDIT_LOG_UNCATEGORIZED
NETFILTER_PKT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
OBJ_PID
PROCESS_UNCATEGORIZED
PATH
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_ACCT_LOCK
USER_UNCATEGORIZED
RESP_ACCT_LOCK_TIMED
USER_UNCATEGORIZED
RESP_ACCT_REMOTE
USER_UNCATEGORIZED
RESP_ACCT_UNLOCK_TIMED
USER_UNCATEGORIZED
RESP_ALERT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_ANOMALY
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_EXEC
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_HALT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_KILL_PROC
PROCESS_TERMINATION
RESP_SEBOOL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_SINGLE
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_TERM_ACCESS
SYSTEM_AUDIT_LOG_UNCATEGORIZED
RESP_TERM_LOCK
SYSTEM_AUDIT_LOG_UNCATEGORIZED
ROLE_ASSIGN
USER_CHANGE_PERMISSIONS
ROLE_MODIFY
USER_CHANGE_PERMISSIONS
ROLE_REMOVE
USER_CHANGE_PERMISSIONS
SELINUX_ERR
SYSTEM_AUDIT_LOG_UNCATEGORIZED
SERVICE_START
SERVICE_START
SERVICE_STOP
SERVICE_STOP
SOCKADDR
SYSTEM_AUDIT_LOG_UNCATEGORIZED
SOCKETCALL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
SYSCALL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
SYSTEM_BOOT
STATUS_STARTUP
SYSTEM_RUNLEVEL
SYSTEM_AUDIT_LOG_UNCATEGORIZED
SYSTEM_SHUTDOWN
STATUS_SHUTDOWN
TEST
SYSTEM_AUDIT_LOG_UNCATEGORIZED
TRUSTED_APP
SYSTEM_AUDIT_LOG_UNCATEGORIZED
TTY
SYSTEM_AUDIT_LOG_UNCATEGORIZED
USER_ACCT
USER_UNCATEGORIZED
USER_AUTH
USER_LOGIN
USER_AVC
USER_UNCATEGORIZED
USER_CHAUTHTOK
USER_RESOURCE_UPDATE_CONTENT
USER_CMD
USER_UNCATEGORIZED
USER_END
USER_LOGOUT
USER_ERR
USER_UNCATEGORIZED
USER_LABELED_EXPORT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
USER_LOGIN
USER_LOGIN
USER_LOGOUT
USER_LOGOUT
USER_MAC_POLICY_LOAD
RESOURCE_READ
USER_MGMT
USER_UNCATEGORIZED
USER_ROLE_CHANGE
USER_CHANGE_PERMISSIONS
USER_SELINUX_ERR
USER_UNCATEGORIZED
USER_START
USER_LOGIN
USER_TTY
SYSTEM_AUDIT_LOG_UNCATEGORIZED
USER_UNLABELED_EXPORT
SYSTEM_AUDIT_LOG_UNCATEGORIZED
USYS_CONFIG
USER_RESOURCE_UPDATE_CONTENT
VIRT_CONTROL
STATUS_UPDATE
VIRT_MACHINE_ID
USER_RESOURCE_ACCESS
VIRT_RESOURCE
USER_RESOURCE_ACCESS
BPF
SYSTEM_AUDIT_LOG_UNCATEGORIZED
SECCOMP
SYSTEM_AUDIT_LOG_UNCATEGORIZED
PROCTITLE
PROCESS_UNCATEGORIZED
Field mapping reference:  Audit logs
The following table lists the log fields of the
Audit logs
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
target.platform
The
target.platform
UDM field is set to
LINUX
.
exit
additional.fields[exit]
a0
additional.fields[a0]
a1
additional.fields[a1]
a2
additional.fields[a2]
a3
additional.fields[a3]
arch
additional.fields[arch]
cap_fi
additional.fields[cap_fi]
cap_fp
additional.fields[cap_fp]
cap_pe
additional.fields[cap_pe]
cap_pi
additional.fields[cap_pi]
cap_pp
additional.fields[cap_pp]
capability
additional.fields[capability]
cwd
additional.fields[cwd]
If the
name
log field value doesn't contains one of the following values, then the
cwd
log field is mapped to the
additional.fields
UDM field.
empty
?
data
additional.fields[data]
dev
additional.fields[dev]
devmajor
additional.fields[devmajor]
devminor
additional.fields[devminor]
flags
additional.fields[flags]
item
additional.fields[item]
list
additional.fields[list]
The
additional.fields
UDM field is set to one of the following values:
0 - user
when the following conditions are met:
The value in the
list
field is
0
.
If the
list
field value does not contains one of the following values:
empty
?
1 - task
when the following conditions are met:
The value in the
list
field is
1
.
If the
list
field value does not contains one of the following values:
empty
?
4 - exit
when the following conditions are met:
The value in the
list
field is
4
.
If the
list
field value does not contains one of the following values:
empty
?
5 - exclude
when the following conditions are met:
The value in the
list
field is
5
.
If the
list
field value does not contains one of the following values:
empty
?
msgtype
additional.fields[msgtype]
obj_gid
additional.fields[obj_gid]
obj_role
additional.fields[obj_role]
If the
obj_role
log field value doesn't contains one of the following values, then the
obj_role
log field is mapped to the
additional.fields
UDM field.
empty
?
obj_uid
additional.fields[obj_uid]
ocomm
additional.fields[ocomm]
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
ocomm
log field is mapped to the
additional.fields
UDM field.
old_prom
additional.fields[old_prom]
old-disk
additional.fields[old-disk]
old-mem
additional.fields[old-mem]
old-net
additional.fields[old-net]
old-vcpu
additional.fields[old-vcpu]
opid
additional.fields[opid]
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
opid
log field is mapped to the
additional.fields
UDM field.
oses
additional.fields[oses]
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
oses
log field is mapped to the
additional.fields
UDM field.
pid
additional.fields[pid]
If the
eventType
log field value is equal to
OBJ_PID
, then the
pid
log field is mapped to the
additional.fields
UDM field.
prom
additional.fields[prom]
ses
additional.fields[ses]
If the
eventType
log field value is equal to
OBJ_PID
, then the
ses
log field is mapped to the
additional.fields
UDM field.
subj_clr
additional.fields[subj_clr]
subj_role
additional.fields[subj_role]
subj_sen
additional.fields[subj_sen]
subj
additional.fields[subj]
syscall
additional.fields[syscall]
tty
additional.fields[tty]
extensions.auth.type
If the
eventType
log field value contains one of the following values, then the
extensions.auth.type
UDM field is set to
MACHINE
.
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
type
metadata.product_event_type
network.application_protocol
If the
eventType
log field value contains one of the following values, then the
network.application_protocol
UDM field is set to
SSH
.
CRYPTO_SESSION
CRYPTO_KEY_USER
direction
network.direction
If the
direction
log field value is equal to
from-client
, then the
network.direction
UDM field is set to
OUTBOUND
.
Else, if the
direction
log field value is equal to
from-server
, then the
network.direction
UDM field is set to
INBOUND
.
family
network.ip_protocol
The
network.ip_protocol
UDM field is set to one of the following values:
IP6IN4
when the following conditions are met:
The value in the
family
field is
2
.
If the
family
field value does not contains one of the following values:
empty
?
UNKNOWN_IP_PROTOCOL
when the following conditions are met:
The value in the
family
field is not
2
.
If the
family
field value does not contains one of the following values:
empty
?
proto
network.ip_protocol
The
network.ip_protocol
UDM field is set to one of the following values:
IP6IN4
when the following conditions are met:
The value in the
proto
field is
2
.
If the
proto
field value does not contains one of the following values:
empty
?
UNKNOWN_IP_PROTOCOL
when the following conditions are met:
The value in the
proto
field is not
2
.
If the
proto
field value does not contains one of the following values:
empty
?
icmptype
network.ip_protocol
If the
icmptype
log field value doesn't contains one of the following values, then the
network.ip_protocol
UDM field is set to
ICMP
.
empty
?
network.ip_protocol
If the
eventType
log field value contains one of the following values, then the
network.ip_protocol
UDM field is set to
TCP
.
CRYPTO_SESSION
CRYPTO_KEY_USER
ksize
network.sent_bytes
oses
network.session_id
If the
eventType
log field value is equal to
OBJ_PID
, then the
oses
log field is mapped to the
network.session_id
UDM field.
ses
network.session_id
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
oses
log field is mapped to the
network.session_id
UDM field.
cipher
network.tls.cipher
pfs
network.tls.curve
hostname
principal.hostname
If the
eventType
log field value doesn't contains one of the following values, then the
hostname
log field is mapped to the
principal.hostname
UDM field.
CRYPTO_SESSION
CRYPTO_KEY_USER
addr
principal.ip
The
addr
log field is mapped to the
principal.ip
UDM field if all of the following conditions are met:
The
eventType
field value contains one of the following values:
CRYPTO_SESSION
CRYPTO_KEY_USER
The
addr
field value does not contains one of the following values:
empty
?
ip
principal.ip
If the
ip
log field value doesn't contains one of the following values, then
the
ip
log field is mapped to the
principal.ip
UDM field.
empty
?
laddr
principal.ip
To determine if the
laddr
field contains a valid IP address, the following conditions are evaluated:
The
laddr
field is not empty and doesn't contain the value
?
.
The
laddr
field matches the regular expression
%{IP:new_laddr}
.
If the
new_laddr
field is not empty, then the
principal.ip
field is set to the value of
new_laddr
field.
dvc
principal.ip
To filter events that have a device identifier but are not related to login activity, the following conditions are evaluated:
The
eventType
field does not contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
dvc
field is not empty and contains a device identifier.
If the device identifier is a valid IP address, the
principal.ip
and
intermediary.ip
fields are set with the value of the device identifier. If the device identifier is not a valid IP address, the
principal.hostname
and
intermediary.hostname
fields are set with the value of  the device identifier.
lport
principal.port
cgroup
principal.process.file.full_path
spid
principal.process.pid
uid
principal.user.userid
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to
root
if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
uid
field is
not
empty or doesn't contain the
?
value.
The
uid
field value is
0
.
If these conditions aren't met, the
principal.user.userid
field is set with the value of the
uid
field and
principal_userid
field is set to
true
.
auid
principal.user.attribute.labels[auid]
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to the value of the
auid
field if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
auid
field is
not
empty or doesn't contain the
?
value.
The
principal_userid
field value is
false
.
If these conditions aren't met, the
principal.user.attribute.labels
field is set with the value of the
auid
field.
euid
principal.user.attribute.labels[euid]
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to the value of the
euid
field if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
euid
field is
not
empty or doesn't contain the
?
value.
The
principal_userid
field value is
false
.
If these conditions aren't met, the
principal.user.attribute.labels
field is set with the value of the
euid
field.
fsuid
principal.user.attribute.labels[fsuid]
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to the value of the
fsuid
field if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
fsuid
field is
not
empty or doesn't contain the
?
value.
The
principal_userid
field value is
false
.
If these conditions aren't met, the
principal.user.attribute.labels
field is set with the value of the
fsuid
field.
oauid
principal.user.attribute.labels[oauid]
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to the value of the
oauid
field if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
oauid
field is
not
empty or doesn't contain the
?
value.
The
principal_userid
field value is
false
.
If these conditions aren't met, the
principal.user.attribute.labels
field is set with the value of the
oauid
field.
ouid
principal.user.attribute.labels[ouid]
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to the value of the
ouid
field if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
ouid
field is
not
empty or doesn't contain the
?
value.
The
principal_userid
field value is
false
.
If these conditions aren't met, the
principal.user.attribute.labels
field is set with the value of the
ouid
field.
suid
principal.user.attribute.labels[suid]
The
principal_userid
field is set to
true
and
principal.user.userid
field is set to the value of the
suid
field if the following conditions are met:
The eventType field doesn't contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
suid
field is
not
empty or doesn't contain the
?
value.
The
principal_userid
field value is
false
.
If these conditions aren't met, the
principal.user.attribute.labels
field is set with the value of the
suid
field.
inode_gid
principal.user.attribute.labels[inode_gid]
inode_uid
principal.user.attribute.labels[inode_uid]
security_result.action
If the
res
log field value matches the regular expression pattern
success
, then the
security_result.action
UDM field is set to
ALLOW
.
Else, if the
res
log field value matches the regular expression pattern
fail
, then the
security_result.action
UDM field is set to
BLOCK
.
key
security_result.detection_fields[key]
If the
key
log field value doesn't contains one of the following values, then the
key
log field is mapped to the
security_result.detection_fields.key
UDM field.
empty
?
saddr
security_result.detection_fields[saddr]
sig
security_result.detection_fields[sig]
res
security_result.summary
If the
res
log field value doesn't contains one of the following values, then the
res
log field is mapped to the
security_result.summary
UDM field.
empty
?
.
result
security_result.summary
If the
result
log field value doesn't contains one of the following values, then the
result
log field is mapped to the
security_result.summary
UDM field.
empty
?
reason
security_result.summary
If the
reason
log field value doesn't contains one of the following values, then the
reason
log field is mapped to the
security_result.summary
UDM field.
empty
?
success
security_result.summary
If the
eventType
log field value is equal to
SYSCALL
, then if the
success
log field value is equal to
yes
, then the
security_result.summary
UDM field is set to
systemcall was successful
.
If the
eventType
log field value is equal to
SYSCALL
, then if the
success
log field value is equal to
no
, then the
security_result.summary
UDM field is set to
systemcall was failed
.
name
src.file.full_path
If the
eventType
log field value is equal to
PATH
, then if the
item
log field value is
not
equal to
0
, then the
name
log field is mapped to the
src.file.full_path
UDM field.
src
src.ip
terminal
additional.fields[terminal]
If the
eventType
log field value doesn't contains one of the following values, then the
terminal
log field is mapped to the
additional.fields.terminal
UDM field.
SYSCALL
LOGIN
USER_LOGIN
USER_ACCT
USER_ROLE_CHANGE
USER_START
USER_AUTH
USER_END
USER_LOGOUT
CRED_ACQ
CRED_DISP
CRED_REFR
SERVICE_START
SERVICE_STOP
CRYPTO_SESSION
CRYPTO_KEY_USER
ADD_USER
terminal
target.application
The
terminal
log field is mapped to the
target.application
UDM field when all of the following conditions are met:
If the
eventType
log field value contains one of the following values:
CRYPTO_SESSION
CRYPTO_KEY_USER
ADD_USER
If the
terminal
log field value doesn't contains one of the following values:
empty
?
terminal
principal.application
The
terminal
log field is mapped to the
principal.application
UDM field when all of the following conditions are met:
If the
eventType
log field value contains one of the following values:
SYSCALL
LOGIN
USER_LOGIN
USER_ACCT
USER_ROLE_CHANGE
USER_START
USER_AUTH
USER_END
USER_LOGOUT
CRED_ACQ
CRED_DISP
CRED_REFR
SERVICE_START
SERVICE_STOP
If the
terminal
log field value doesn't contains one of the following values:
empty
?
ocomm
target.process.command_line
If the
eventType
log field value is equal to
OBJ_PID
, then the
ocomm
log field is mapped to the
target.process.command_line
UDM field.
cmd
target.process.command_line
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
target.process.command_line
UDM field is mapped based on the following conditions:
If the
cmd
field is
not
empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
cmd
field and the
target.application
UDM field is set with the value of the
comm
field.
Else, if the
comm
field is not empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
comm
field/
Else, if the
proctitle
field is not empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
proctitle
field.
comm
target.process.command_line
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
target.process.command_line
UDM field is mapped based on the following conditions:
If the
cmd
field is
not
empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
cmd
field and the
target.application
UDM field is set with the value of the
comm
field.
Else, if the
comm
field is not empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
comm
field/
Else, if the
proctitle
field is not empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
proctitle
field.
proctitle
target.process.command_line
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
target.process.command_line
UDM field is mapped based on the following conditions:
If the
cmd
field is
not
empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
cmd
field and the
target.application
UDM field is set with the value of the
comm
field.
Else, if the
comm
field is not empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
comm
field/
Else, if the
proctitle
field is not empty or equal to
?
, then the
target.process.command_line
UDM field is set with the value of the
proctitle
field.
unit
additional.fields[unit]
name
target.file.full_path
The
name
log field is mapped to the
target.file.full_path
UDM field when all of the following conditions are met:
If the
name
log field value doesn't contains one of the following values:
empty
?
If the
eventType
log field value is equal to
PATH
.
If the
item
log field value is equal to
0
.
cwd
target.file.full_path
If the
cwd
log field value doesn't contains one of the following values, then the
cwd
log field is mapped to the
target.file.full_path
UDM field.
empty
?
path
target.file.full_path
If the
path
log field value doesn't contains one of the following values, then the
path
log field is mapped to the
target.file.full_path
UDM field.
empty
?
filetype
target.file.mime_type
If the
filetype
log field value doesn't contains one of the following values, then the
filetype
log field is mapped to the
target.file.mime_type
UDM field.
empty
?
gid
target.group.product_object_id
The
target_groupid
field is set to
true
and
target.group.product_object_id
field is set to the value of the
gid
field if the
gid
field is
not
empty or doesn't contain the
?
value.
egid
target.group.attribute.labels[egid]
The
target_groupid
field is set to
true
and
target.group.product_object_id
field is set to the value of the
egid
field if the following conditions are met:
The
egid
field is
not
empty or doesn't contain the
?
value.
The
target_groupid
field value is
false
.
If these conditions aren't met, the
target.group.attribute.labels
field is set with the value of the
egid
field.
fsgid
target.group.attribute.labels[fsgid]
The
target_groupid
field is set to
true
and
target.group.product_object_id
field is set to the value of the
fsgid
field if the following conditions are met:
The
fsgid
field is
not
empty or doesn't contain the
?
value.
The
target_groupid
field value is
false
.
If these conditions aren't met, the
target.group.attribute.labels
field is set with the value of the
fsgid
field.
new_gid
target.group.attribute.labels[new_gid]
The
target_groupid
field is set to
true
and
target.group.product_object_id
field is set to the value of the
new_gid
field if the following conditions are met:
The
new_gid
field is
not
empty or doesn't contain the
?
value.
The
target_groupid
field value is
false
.
If these conditions aren't met, the
target.group.attribute.labels
field is set with the value of the
new_gid
field.
ogid
target.group.attribute.labels[ogid]
The
target_groupid
field is set to
true
and
target.group.product_object_id
field is set to the value of the
ogid
field if the following conditions are met:
The
ogid
field is
not
empty or doesn't contain the
?
value.
The
target_groupid
field value is
false
.
If these conditions aren't met, the
target.group.attribute.labels
field is set with the value of the
ogid
field.
sgid
target.group.attribute.labels[sgid]
The
target_groupid
field is set to
true
and
target.group.product_object_id
field is set to the value of the
sgid
field if the following conditions are met:
The
sgid
field is
not
empty or doesn't contain the
?
value.
The
target_groupid
field value is
false
.
If these conditions aren't met, the
target.group.attribute.labels
field is set with the value of the
sgid
field.
grp
target.group.group_display_name
id
target.group.product_object_id
If the
eventType
log field value is equal to
ADD_GROUP
, then the
id
log field is mapped to the
target.group.product_object_id
UDM field.
hostname
target.hostname
If the
eventType
log field value contains one of the following values, then the
hostname
log field is mapped to the
target.hostname
UDM field.
CRYPTO_SESSION
CRYPTO_KEY_USER
addr
target.ip
The
addr
field is mapped to
target.ip
UDM field when all of the following conditions are met:
The
eventType
log field value contains one of the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
addr
field is
not
empty or doesn't contain the
?
value.
dvc
target.ip
To filter events that have a device identifier but are related to login activity, the following conditions are evaluated:
The
eventType
field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
dvc
field is not empty and contains a device identifier.
If the device identifier is a valid IP address, the
target.ip
and
intermediary.
ip fields are set with the value of the device identifier. If the device identifier is not a valid IP address, the
target.hostname
and
intermediary.hostname
fields are set with the value of  the device identifier.
new-net
target.mac
ppid
target.process.parent_process.pid
rport
target.port
exe
target.process.file.full_path
If the
eventType
log field value doesn't contains one of the following values, then the
exe
log field is mapped to the
target.process.file.full_path
UDM field.
USER_CHAUTHTOK
USYS_CONFIG
opid
target.process.pid
If the
eventType
log field value is equal to
OBJ_PID
, then the
opid
log field is mapped to the
target.process.pid
UDM field.
pid
target.process.pid
If the
eventType
log field value is
not
equal to
OBJ_PID
, then the
opid
log field is mapped to the
target.process.pid
UDM field.
new-mem
target.resource.attribute.labels[new-mem]
new-vcpu
target.resource.attribute.labels[new-vcpu]
obj_lev_high
target.resource.attribute.labels[obj_lev_high]
obj_lev_low
target.resource.attribute.labels[obj_lev_low]
mode
target.resource.attribute.permissions.name
If the mode field value matches one of the following values: admin_perm, group_perm, or others_perm, the permissions are set.
If the
admin_perm
value is equal to
7
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Admin - Read
Admin - Write
Admin - Execute
Else, if the
admin_perm
value is equal to
6
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Admin - Read
Admin - Write
Else, if the
admin_perm
value is equal to
5
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Admin - Read
Admin - Execute
Else, if the
admin_perm
value is equal to
4
, then the
target.resource.attribute.permissions.name
UDM field is set to
Admin - Read
.
Else, if the
admin_perm
value is equal to
3
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Admin - Write
Admin - Execute
Else, if the
admin_perm
value is equal to
2
, then the
target.resource.attribute.permissions.name
UDM field is set to
Admin - Write
.
Else, if the
admin_perm
value is equal to
1
, then the
target.resource.attribute.permissions.name
UDM field is set to
Admin - Execute
.
Else, if the
admin_perm
value is equal to
0
, then the
target.resource.attribute.permissions.name
UDM field is set to
Admin - Nopermissions
.
If the
group_perm
value is equal to
7
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Group - Read
Group - Write
Group - Execute
Else, if the
group_perm
value is equal to
6
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Group - Read
Group - Write
Else, if the
group_perm
value is equal to
5
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Group - Read
Group - Execute
Else, if the
group_perm
value is equal to
4
, then the
target.resource.attribute.permissions.name
UDM field is set to
Group - Read
.
Else, if the
group_perm
value is equal to
3
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Group - Write
Group - Execute
Else, if the
group_perm
value is equal to
2
, then the
target.resource.attribute.permissions.name
UDM field is set to
Group - Write
.
Else, if the
group_perm
value is equal to
1
, then the
target.resource.attribute.permissions.name
UDM field is set to
Group - Execute
.
Else, if the
group_perm
value is equal to
0
, then the
target.resource.attribute.permissions.name
UDM field is set to
Group - Nopermissions
.
If the
others_perm
value is equal to
7
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Others - Read
Others - Write
Others - Execute
Else, if the
others_perm
value is equal to
6
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Others - Read
Others - Write
Else, if the
others_perm
value is equal to
5
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Others - Read
Others - Execute
Else, if the
others_perm
value is equal to
4
, then the
target.resource.attribute.permissions.name
UDM field is set to
Others - Read
.
Else, if the
others_perm
value is equal to
3
, then the
target.resource.attribute.permissions.name
UDM field is set to the following permissions:
Others - Write
Others - Execute
Else, if the
others_perm
value is equal to
2
, then the
target.resource.attribute.permissions.name
UDM field is set to
Others - Write
.
Else, if the
others_perm
value is equal to
1
, then the
target.resource.attribute.permissions.name
UDM field is set to
Others - Execute
.
Else, if the
others_perm
value is equal to
0
, then the
target.resource.attribute.permissions.name
UDM field is set to
Others - Nopermissions
.
perm
target.resource.attribute.permissions.name
mode
target.resource.attribute.permissions.type
If the mode field value matches one of the following values: admin_perm, group_perm, or others_perm, the permissions are set.
If the
admin_perm
value is equal to
7
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
ADMIN_READ
ADMIN_WRITE
UNKNOWN_PERMISSION_TYPE
Else, if the
admin_perm
value is equal to
6
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
ADMIN_READ
ADMIN_WRITE
Else, if the
admin_perm
value is equal to
5
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
ADMIN_READ
UNKNOWN_PERMISSION_TYPE
Else, if the
admin_perm
value is equal to
4
, then the
target.resource.attribute.permissions.type
UDM field is set to
ADMIN_READ
.
Else, if the
admin_perm
value is equal to
3
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
ADMIN_WRITE
UNKNOWN_PERMISSION_TYPE
Else, if the
admin_perm
value is equal to
2
, then the
target.resource.attribute.permissions.type
UDM field is set to
ADMIN_WRITE
.
Else, if the
admin_perm
value is equal to
1
, then the
target.resource.attribute.permissions.type
UDM field is set to
UNKNOWN_PERMISSION_TYPE
.
Else, if the
admin_perm
value is equal to
0
, then the
target.resource.attribute.permissions.type
UDM field is set to
Admin - Nopermissions
.
If the
group_perm
value is equal to
7
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_READ
DATA_WRITE
UNKNOWN_PERMISSION_TYPE
Else, if the
group_perm
value is equal to
6
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_READ
DATA_WRITE
Else, if the
group_perm
value is equal to
5
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_READ
UNKNOWN_PERMISSION_TYPE
Else, if the
group_perm
value is equal to
4
, then the
target.resource.attribute.permissions.type
UDM field is set to
DATA_READ
.
Else, if the
group_perm
value is equal to
3
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_WRITE
UNKNOWN_PERMISSION_TYPE
Else, if the
group_perm
value is equal to
2
, then the
target.resource.attribute.permissions.type
UDM field is set to
DATA_WRITE
.
Else, if the
group_perm
value is equal to
1
, then the
target.resource.attribute.permissions.type
UDM field is set to
UNKNOWN_PERMISSION_TYPE
.
Else, if the
group_perm
value is equal to
0
, then the
target.resource.attribute.permissions.type
UDM field is set to
Group - Nopermissions
.
If the
others_perm
value is equal to
7
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_READ
DATA_WRITE
UNKNOWN_PERMISSION_TYPE
Else, if the
others_perm
value is equal to
6
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_READ
DATA_WRITE
Else, if the
others_perm
value is equal to
5
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_READ
UNKNOWN_PERMISSION_TYPE
Else, if the
others_perm
value is equal to
4
, then the
target.resource.attribute.permissions.type
UDM field is set to
DATA_READ
.
Else, if the
others_perm
value is equal to
3
, then the
target.resource.attribute.permissions.type
UDM field is set to the following permissions:
DATA_WRITE
UNKNOWN_PERMISSION_TYPE
Else, if the
others_perm
value is equal to
2
, then the
target.resource.attribute.permissions.type
UDM field is set to
DATA_WRITE
.
Else, if the
others_perm
value is equal to
1
, then the
target.resource.attribute.permissions.type
UDM field is set to
UNKNOWN_PERMISSION_TYPE
.
Else, if the
others_perm
value is equal to
0
, then the
target.resource.attribute.permissions.type
UDM field is set to
Others - Nopermissions
.
exe
target.resource.name
If the
eventType
log field value contains one of the following values, then the
exe
log field is mapped to the
target.resource.name
UDM field.
USER_CHAUTHTOK
USYS_CONFIG
new-disk
target.resource.name
If the
new-disk
log field value doesn't contains one of the following values, then the
new-disk
log field is mapped to the
target.resource.name
UDM field.
empty
?
obj
target.resource.name
If the
obj
log field value doesn't contains one of the following values, then the
obj
log field is mapped to the
target.resource.name
UDM field.
empty
?
vm
target.resource.name
If the
vm
log field value doesn't contains one of the following values, then the
vm
log field is mapped to the
target.resource.name
UDM field.
empty
?
inode
target.resource.product_object_id
ino
target.resource.product_object_id
target.resource.resource_subtype
If the
perm
log field value is
not
empty, then the
target.resource.resource_subtype
UDM field is set to
File
.
target.resource.resource_type
If the
eventType
log field value contains one of the following values and the
exe
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
SETTING
.
USER_CHAUTHTOK
USYS_CONFIG
If the
inode
log field value is
not
empty or the
ino
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
If the
obj
log field value doesn't contains one of the following values, then the
target.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
empty
?
NULL
If the
vm
log field value doesn't contains one of the following values, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
empty
?
NULL
If the
new-disk
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
DISK
.
If the
perm
log field value is
not
empty, then the
target.resource.resource_type
UDM field is set to
STORAGE_OBJECT
.
If the
eventType
log field value contains one of the following values, then the
target.resource.resource_type
UDM field is set to
DEVICE
.
DEV_ALLOC
DEV_DEALLOC
uid
target.user.userid
The
target_userid
field is set to
true
and
target.user.userid
field is set to
root
if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
uid
field is
not
empty or doesn't contain the
?
value.
The uid field value is
0
.
If these conditions aren't met, the
target.user.userid
field is set with the value of the
uid
field and
target_userid
field is set to
true
.
auid
target.user.attribute.labels[auid]
The
target_userid
field is set to
true
and
target.user.userid
field is set to the value of the
auid
field if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
auid
field is
not
empty or doesn't contain the
?
value.
The
target_userid
field value is
false
.
If these conditions aren't met, the
target.user.attribute.labels
field is set with the value of the
auid
field.
euid
target.user.attribute.labels[euid]
The
target_userid
field is set to
true
and
target.user.userid
field is set to the value of the
euid
field if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
euid
field is
not
empty or doesn't contain the
?
value.
The
target_userid
field value is
false
.
If these conditions aren't met, the
target.user.attribute.labels
field is set with the value of the
euid
field.
fsuid
target.user.attribute.labels[fsuid]
The
target_userid
field is set to
true
and
target.user.userid
field is set to the value of the
fsuid
field if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
fsuid
field is
not
empty or doesn't contain the
?
value.
The
target_userid
field value is
false
.
If these conditions aren't met, the
target.user.attribute.labels
field is set with the value of the
fsuid
field.
oauid
target.user.attribute.labels[oauid]
The
target_userid
field is set to
true
and
target.user.userid
field is set to the value of the
oauid
field if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
oauid
field is
not
empty or doesn't contain the
?
value.
The
target_userid
field value is
false
.
If these conditions aren't met, the
target.user.attribute.labels
field is set with the value of the
oauid
field.
ouid
target.user.attribute.labels[ouid]
The
target_userid
field is set to
true
and
target.user.userid
field is set to the value of the
ouid
field if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
ouid
field is
not
empty or doesn't contain the
?
value.
The
target_userid
field value is
false
.
If these conditions aren't met, the
target.user.attribute.labels
field is set with the value of the
ouid
field.
suid
target.user.attribute.labels[suid]
The
target_userid
field is set to
true
and
target.user.userid
field is set to the value of the
suid
field if the following conditions are met:
The eventType field contain the following values:
ANOM_LOGIN_ACCT
ANOM_LOGIN_FAILURES
ANOM_LOGIN_LOCATION
ANOM_LOGIN_SESSIONS
ANOM_LOGIN_TIME
CRED_ACQ
CRED_DISP
CRED_REFR
CRYPTO_LOGIN
CRYPTO_LOGOUT
LOGIN
USER_AUTH
USER_END
USER_LOGIN
USER_LOGOUT
USER_START
USER_ACCT
USER_ROLE_CHANGE
DEL_GROUP
The
suid
field is
not
empty or doesn't contain the
?
value.
The
target_userid
field value is
false
.
If these conditions aren't met, the
target.user.attribute.labels
field is set with the value of the
suid
field.
id
target.user.attribute.labels[id]
If the
eventType
log field value is equal to
ADD_USER
, then the
id
log field is mapped to the
target.user.userid
UDM field.
Else, if the
eventType
log field value is equal to
ADD_GROUP
, then the
id
log field is mapped to the
target.group.product_object_id
UDM field.
Else, the
id
log field is mapped to the
target.user.attribute.labels
UDM field.
sauid
target.user.attribute.labels[sauid]
acct
target.user.user_display_name
If the
acct
log field value doesn't contains one of the following values, then the
acct
log field is mapped to the
target.user.user_display_name
UDM field.
empty
?
subj_user
target.user.user_display_name
If the
subj_user
log field value doesn't contains one of the following values, then the
subj_user
log field is mapped to the
target.user.user_display_name
UDM field.
empty
?
obj_user
target.user.user_display_name
If the
obj_user
log field value doesn't contains one of the following values, then the
obj_user
log field is mapped to the
target.user.user_display_name
UDM field.
empty
?
id
target.user.userid
If the
eventType
log field value contains one of the following values, then the
id
log field is mapped to the
target.user.userid
UDM field.
ADD_USER
DEL_USER
Field mapping reference: Event Identifier to Event Type for all Log source paths
The following table lists all the remaining log types and their corresponding UDM event types.
Event Identifier
Event Type
/var/log/apache2/error.log
NETWORK_UNCATEGORIZED
/var/log/apache2/error.log
NETWORK_UNCATEGORIZED
/var/log/apache2/error.log
NETWORK_UNCATEGORIZED
/var/log/apache2/error.log
NETWORK_HTTP
/var/log/apache2/error.log
NETWORK_UNCATEGORIZED
/var/log/apache2/error.log
NETWORK_UNCATEGORIZED
/var/log/apache2/error.log
NETWORK_UNCATEGORIZED
/var/log/apache2/access.log
NETWORK_HTTP
/var/log/apache2/access.log
NETWORK_HTTP
/var/log/apache2/access.log
NETWORK_HTTP
/var/log/apache2/access.log
NETWORK_HTTP
/var/log/apache2/access.log
NETWORK_HTTP
/var/log/apache2/access.log
GENERIC_EVENT
var/log/apache2/other_vhosts_access.log
NETWORK_HTTP
var/log/apache2/other_vhosts_access.log
NETWORK_HTTP
var/log/nginx/access.log
NETWORK_HTTP
var/log/nginx/error.log
NETWORK_HTTP
/var/log/kern.log
NETWORK_CONNECTION
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/kern.log
GENERIC_EVENT
/var/log/rundeck/service.log
GENERIC_EVENT
var/log/rundeck/rundeck.api.log
STATUS_UPDATE
var/log/openvpnas.log
NETWORK_CONNECTION
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
NETWORK_UNCATEGORIZED
var/log/openvpnas.log
GENERIC_EVENT
var/log/openvpnas.log
GENERIC_EVENT
/var/log/mail.log
GENERIC_EVENT
/var/log/mail.log
EMAIL_UNCATEGORIZED
/var/log/mail.log
GENERIC_EVENT
/var/log/mail.log
EMAIL_UNCATEGORIZED
/var/log/mail.log
GENERIC_EVENT
/var/log/mail.log
EMAIL_UNCATEGORIZED
/var/log/auth.log
USER_LOGOUT
/var/log/auth.log
USER_LOGIN
/var/log/auth.log
USER_LOGIN
/var/log/auth.log
USER_LOGIN
/var/log/auth.log
USER_UNCATEGORIZED
/var/log/auth.log
USER_UNCATEGORIZED
/var/log/auth.log
USER_LOGIN
/var/log/auth.log
USER_LOGOUT
/var/log/auth.log
STATUS_UPDATE
/var/log/auth.log
USER_LOGIN
var/log/samba/log.winbindd
GENERIC_EVENT
var/log/samba/log.winbindd
GENERIC_EVENT
var/log/samba/log.winbindd
GENERIC_EVENT
var/log/rkhunter.log
GENERIC_EVENT
var/log/rkhunter.log
GENERIC_EVENT
var/log/rkhunter.log
GENERIC_EVENT
/var/log/syslog.log
NETWORK_CONNECTION
/var/log/syslog.log
GENERIC_EVENT
/var/log/syslog.log
GENERIC_EVENT
/var/log/syslog.log
GENERIC_EVENT
/var/log/syslog.log
GENERIC_EVENT
/var/log/syslog.log
GENERIC_EVENT
/var/log/syslog.log
GENERIC_EVENT
/var/log/syslog.log
GENERIC_EVENT
Field mapping reference: /var/log/apache2/error.log
The following table lists the log fields of the
/var/log/apache2/error.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
log_module
principal.resource.name
severity
security_result.severity
If the
severity
log field value is equal to
info
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
severity
log field value is equal to
error
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
severity
log field value is equal to
crit
, then the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
severity
log field value is equal to
notice
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value is equal to
emerg
, then the
security_result.severity
UDM field is set to
HIGH
.
tid
target.process.pid
If the
tid
log field value is
not
empty and the
pid
log field value is
not
empty, then the
tid
log field is mapped to the
target.process.pid
UDM field.
pid
target.process.pid
If the
tid
log field value is empty and the
pid
log field value is
not
empty, then the
pid
log field is mapped to the
target.process.pid
UDM field.
pid
target.process.parent_process.pid
If the
tid
log field value is
not
empty, then the
pid
log field is mapped to the
target.process.parent_process.pid
UDM field.
principal_ip
principal.ip
principal_port
principal.port
error_message
security_result.description
referer_url
network.http.referral_url
If the
referer_url
log field value doesn't contains one of the following values, then the
referer_url
log field is mapped to the
network.http.referral_url
UDM field.
empty
-
target_ip
target.ip
connection_id
network.session_id
request_id
security_result.detection_fields[request]
file_path
target.file.full_path
network.application_protocol
The
network.application_protocol
UDM field is set to
HTTP
.
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.event_type
If the
principal_ip
log field value is
not
empty and the
target_ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
Else, if the
principal_ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
Field mapping reference: /var/log/apache2/access.log
The following table lists the log fields of the
/var/log/apache2/access.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
principal_ip
principal.ip
principal_user_userid
principal.user.userid
If the
principal_user_userid
log field value doesn't contains one of the following values, then the
principal_user_userid
log field is mapped to the
principal.user.userid
UDM field.
-
empty
timestamp
metadata.event_timestamp
http_method
network.http.method
resource_name
principal.resource.name
protocol
network.application_protocol
result_status
network.http.response_code
object_size
network.sent_bytes
referer_url
network.http.referral_url
If the
referer_url
log field value doesn't contains one of the following values, then the
referer_url
log field is mapped to the
network.http.referral_url
UDM field.
-
empty
user_agent
network.http.user_agent
If the
user_agent
log field value doesn't contains one of the following values, then the
user_agent
log field is mapped to the
network.http.user_agent
UDM field.
-
empty
target_host
target.hostname
target_host
target.asset.hostname
target_port
target.port
host
principal.hostname
network.ip_protocol
The
network.ip_protocol
UDM field is set to
TCP
when all of the following conditions are met:
The
message
log field value does not match the regular expression pattern
(?:%DATA:referer_url? or -)\s+->\s+(?:%GREEDYDATA:path? or -)
.
The
message
log field value does not match the regular expression pattern
(?:%GREEDYDATA:user_agent)
.
network.direction
The
network.direction
UDM field is set to
OUTBOUND
.
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.event_type
If the
principal.ip
log field value is
not
empty and the
target.hostname
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
Else, if the
principal.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
target.url
If the
referer_url
log field value doesn't contains one of the following values, then the
%{referer_url}%{resource_name}
log field is mapped to the
target.url
UDM field.
-
empty
None
Field mapping reference: /var/log/nginx/access.log
The following table lists the log fields of the
/var/log/nginx/access.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
principal_ip
principal.ip
principal_user_userid
principal.user.userid
timestamp
metadata.event_timestamp
http_method
network.http.method
resource_name
principal.resource.name
protocol
network.application_protocol
result_status
network.http.response_code
object_size
network.sent_bytes
referer_url
network.http.referral_url
user_agent
network.http.user_agent
target_host
target.hostname
target_host
target.asset.hostname
target_port
target.port
host
principal.hostname
network.ip_protocol
The
network.ip_protocol
UDM field is set to
TCP
when all of the following conditions are met:
The
message
log field value does not match the regular expression pattern
(?:%DATA:referer_url? or -)\s+->\s+(?:%GREEDYDATA:path? or -)
.
The
message
log field value does not match the regular expression pattern
(?:%GREEDYDATA:user_agent)
.
network.direction
The
network.direction
UDM field is set to
OUTBOUND
.
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.event_type
If the
principal.ip
log field value is
not
empty and the
target.hostname
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
Else, if the
principal.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
STATUS_UPDATE
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
target.url
If the
referer_url
log field value doesn't contains one of the following values, then the
%{referer_url}%{resource_name}
log field is mapped to the
target.url
UDM field.
-
empty
None
Field mapping reference: /var/log/nginx/error.log
The following table lists the log fields of the
/var/log/nginx/error.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
thread_id
principal.process.pid
severity
security_result.severity
If the
severity
log field value is equal to
debug
, then the
security_result.severity
UDM field is set to
UNKNOWN_SEVERITY
.
Else, if the
severity
log field value is equal to
info
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
severity
log field value is equal to
notice
, then the
security_result.severity
UDM field is set to
LOW
.
Else, if the
severity
log field value is equal to
warn
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value is equal to
error
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
severity
log field value is equal to
crit
, then the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
severity
log field value is equal to
alert
, then the
security_result.severity
UDM field is set to
HIGH
.
year
metadata.event_timestamp
If the
year
log field value is
not
empty and the
day
log field value is
not
empty and the
month
log field value is
not
empty and the
time
log field value is
not
empty, then the
%{year}/%{day}/%{month} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
day
metadata.event_timestamp
If the
year
log field value is
not
empty and the
day
log field value is
not
empty and the
month
log field value is
not
empty and the
time
log field value is
not
empty, then the
%{year}/%{day}/%{month} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
month
metadata.event_timestamp
If the
year
log field value is
not
empty and the
day
log field value is
not
empty and the
month
log field value is
not
empty and the
time
log field value is
not
empty, then the
%{year}/%{day}/%{month} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
time
metadata.event_timestamp
If the
year
log field value is
not
empty and the
day
log field value is
not
empty and the
month
log field value is
not
empty and the
time
log field value is
not
empty, then the
%{year}/%{day}/%{month} %{time}
log field is mapped to the
metadata.event_timestamp
UDM field.
target_file_full_path
target.file.full_path
principal_ip
principal.ip
target_hostname
target.hostname
http_method
network.http.method
resource_name
principal.resource.name
target_ip
target.ip
target_port
target.port
security_description
security_result.description
pid
principal.process.parent_process.pid
network.ip_protocol
The
network.ip_protocol
UDM field is set to
TCP
.
network.direction
The
network.direction
UDM field is set to
OUTBOUND
.
target.platform
The
target.platform
UDM field is set to
LINUX
.
network.application_protocol
The
network.application_protocol
UDM field is set to
HTTP
.
metadata.event_type
The
metadata.event_type
UDM field is set to
NETWORK_HTTP
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
Field mapping reference: /var/log/kern.log
The following table lists the log fields of the
/var/log/kern.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
principal_hostname
principal.hostname
principal_hostname
principal.asset.hostname
metadata_product_event_type
metadata.product_event_type
target_ip_addr
target.ip
principal_ip
principal.ip
target_user_userid
target.user.userid
metadata_description
metadata.description
file_path
principal.process.file.full_path
pid
principal.process.pid
principal_asset_hardware_cpu_model
principal.asset.hardware.cpu_model
principal.platform
The
principal.platform
UDM field is set to
LINUX
.
metadata.event_type
If the
target.ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
network.application_protocol
If the
target.ip
log field value is
not
empty, then the
network.application_protocol
UDM field is set to
HTTP
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
principal_port
principal.port
target_port
target.port
Field mapping reference: /var/log/rundeck/service.log
The following table lists the log fields of the
/var/log/rundeck/service.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
severity
security_result.severity
security_description
security_result.description
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
summary
security_result.summary
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
Field mapping reference: /var/log/openvpnas.log
The following table lists the log fields of the
/var/log/openvpnas.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
severity
security_result.severity
If the
severity
log field value matches the regular expression pattern
info
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
severity
log field value matches the regular expression pattern
err
, then the
security_result.severity
UDM field is set to
ERROR
.
Else, if the
severity
log field value matches the regular expression pattern
warn
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
severity
log field value is
not
empty, then the
security_result.severity
UDM field is set to
UNKNOWN_SEVERITY
.
target_ip_addr
target.ip
target_hostname1
target.hostname
target_hostname1
target.asset.hostname
target_port
target.port
common_name
target.user.user_display_name
ip
principal.ip
local_ip
principal.ip
summary
security_result.summary
command_line
target.process.command_line
status
principal.user.user_authentication_status
If the
status
log field value is equal to
0
, then the
principal.user.user_authentication_status
UDM field is set to
UNKNOWN_AUTHENTICATION_STATUS
.
Else, if the
status
log field value is equal to
1
, then the
principal.user.user_authentication_status
UDM field is set to
ACTIVE
.
Else, if the
status
log field value is equal to
2
, then the
principal.user.user_authentication_status
UDM field is set to
SUSPENDED
.
Else, if the
status
log field valueis equal to
3
, then the
principal.user.user_authentication_status
UDM field is set to
NO_ACTIVE_CREDENTIALS
.
Else, if the
status
log field valueis equal to
4
, then the
principal.user.user_authentication_status
UDM field is set to
DELETED
.
principal.platform
The
principal.platform
UDM field is set to
LINUX
.
metadata.event_type
The
metadata.event_type
UDM field is set to
NETWORK_UNCATEGORIZED
when the following conditions are met:
If the
target_ip_addr
log field value is
not
empty or the
target_hostname1
log field value is
not
empty and the
local_ip
log field value is
not
empty.
If the
message
log field value matches the regular expression pattern
Peer connection initiated
.
If the
target_ip_addr
log field value is
not
empty or the
target_hostname1
log field value is
not
empty and the
local_ip
log field value is
not
empty, then the
metadata.event_type
UDM field is set to
NETWORK_CONNECTION
.
Else, the
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
network.application_protocol
The
network.application_protocol
UDM field is set to
HTTP
.
network.ip_protocol
The
network.ip_protocol
UDM field is set to
TCP
.
network.direction
The
network.direction
UDM field is set to
OUTBOUND
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
msg
metadata.description
metadata_description
metadata.description
intermediary_ip
intermediary.ip
reason
security_result.description
Field mapping reference: /var/log/mail.log
The following table lists the log fields of the
/var/log/mail.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
relay
target.ip
target_ip_addr
target.ip
target_hostname1
target.hostname
If the
target_ip
log field value is empty, then the
target_hostname1
log field is mapped to the
target.hostname
UDM field.
application
target.application
pid
target.process.pid
resource_name
target.resource.name
size
network.received_bytes
metadata.event_type
The
metadata.event_type
UDM field is set to one of the following values:
EMAIL_TRANSACTION
when the following conditions are met:
If the
application
field value contains one of the following values:
postfix/qmgr
postfix/local
postfix/pickup
postfix/smtp
postfix/smtpd
sendmail
postfix/error
.
The value in the
status
field is
sent (delivered to mailbox)
.
EMAIL_UNCATEGORIZED
when the following conditions are met:
If the
application
field value contains one of the following values:
postfix/qmgr
postfix/local
postfix/pickup
postfix/smtp
postfix/smtpd
sendmail
postfix/error
EMAIL_TRANSACTION
when the following conditions are met:
The value in the
application
field is
postfix/cleanup
.
The value in the
from
field is
not
empty or the value in the
to
field is
not
empty.
GENERIC_EVENT
when none of the preceding conditions are met.
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
target_hostname1
target.asset.hostname
If the
target_ip
log field value is empty, then the
target_hostname1
log field is mapped to the
target.asset.hostname
UDM field.
from
network.email.from
If the
from
log field value matches the regular expression pattern
@
, then the
from
log field is mapped to the
network.email.from
UDM field.
to
network.email.to
If the
to
log field value matches the regular expression pattern
@
, then the
to
log field is mapped to the
network.email.to
UDM field.
status
metadata.description
security_description1
security_result.description
Field mapping reference: /var/log/auth.log
The following table lists the log fields of the
/var/log/auth.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
_timestamp
metadata.event_timestamp
dvc
target.hostname
If the
process
log field value does not match the regular expression pattern
CRON
, then the
dvc
log field is mapped to the
target.hostname
UDM field.
dvc
principal.hostname
If the
process
log field value matches the regular expression pattern
CRON
, then the
dvc
log field is mapped to the
principal.hostname
UDM field.
Else, if the
eventType
log field value matches the regular expression pattern
(su|sudo):.*authentication failure
, then the
dvc
log field is mapped to the
principal.hostname
UDM field.
dvc
intermediary.hostname
process
target.application
pid
target.process.pid
If the
message
log field value does not match the regular expression pattern
sudo(.*)TTY=(.*)COMMAND=(.*)
, then the
pid
log field is mapped to the
target.process.pid
UDM field.
pid
principal.process.pid
If the
message
log field value matches the regular expression pattern
sudo(.*)TTY=(.*)COMMAND=(.*)
, then the
pid
log field is mapped to the
principal.process.pid
UDM field.
srcUser
principal.user.userid
If the
message
log field value matches the regular expression pattern
sudo(.*)TTY=(.*)COMMAND=(.*)
, then the
srcUser
log field is mapped to the
principal.user.userid
UDM field.
username
target.user.userid
src_user
target.user.userid
srcIp
principal.ip
srcPort
principal.port
command_line, command_line_2
principal.process.command_line
If the
command_line
log field value is
not
empty and the
command_line_2
log field value is
not
empty, then the
%{command_line}%{command_line_2}
log field is mapped to the
principal.process.command_line
UDM field.
sessionId
network.session_id
action
security_result.description
If the
action
log field value does not match the regular expression pattern
authentication failure
, then the
action
log field is mapped to the
security_result.description
UDM field.
reason
security_result.description
If the
reason
log field value is
not
empty, then the
reason
log field is mapped to the
security_result.description
UDM field.
description
security_result.description
If the
description
log field value is
not
empty, then the
description
log field is mapped to the
security_result.description
UDM field.
action
security_result.summary
If the
action
log field value matches the regular expression pattern
authentication failure
, then the
action
log field is mapped to the
security_result.summary
UDM field.
network.application_protocol
If the
proto
log field value is equal to
ssh
or the
proto
log field value is equal to
ssh2
, then the
network.application_protocol
UDM field is set to
SSH
.
extensions.auth.type
The
extensions.auth.type
UDM field is set to
AUTHTYPE_UNSPECIFIED
.
extensions.auth.mechanism
The
extensions.auth.mechanism
UDM field is set to
USERNAME_PASSWORD
.
metadata.event_type
The
metadata.event_type
log field is set to one of the following values:
USER_LOGIN
when any of the following conditions are met:
The
message
log field value matches the regular expression pattern
(New session|Accepted password|authentication failure|session opened|Accepted publickey)
.
The
message
log field value matches the regular expression pattern
sudo(.*)TTY=(.*)COMMAND=.*
.
USER_LOGOUT
when the
message
log field value matches the regular expression pattern
(Removed session|session closed|Disconnected from user|Received disconnect|Connection reset by authenticating user)
.
STATUS_UPDATE
when the
message
log field value matches the regular expression pattern
Timeout, client not responding.
USER_UNCATEGORIZED
when none of the preceding conditions are met.
target.platform
The
target.platform
UDM field is set to
LINUX
.
security_result.action
The
security_result.action
UDM field is set to
BLOCK
.
command
target.process.command_line
If the
message
log field value matches the regular expression pattern
sudo(.*)TTY=(.*)COMMAND=(.*)
, then the
command
log field is mapped to the
target.process.command_line
UDM field.
pwd
target.file.full_path
If the
message
log field value matches the regular expression pattern
sudo(.*)TTY=(.*)COMMAND=(.*)
, then the
pwd
log field is mapped to the
target.file.full_path
UDM field.
rhost
additional.fields[rhost]
msg1
additional.fields[additional_msg]
euid
additional.fields[euid]
logname
additional.fields[logname]
ruser
additional.fields[ruser]
tty
additional.fields[tty]
uid
additional.fields[uid]
user
additional.fields[user]
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
eventType
metadata.product_event_type
eventType
target.application
reason
metadata.description
metadata.product_log_id
If the
sev
log field value is equal to
0
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
1
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
2
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
3
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
4
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
5
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
6
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
7
, then the
metadata.product_log_id
UDM field is set to
kern
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
8
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
9
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
10
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
11
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
12
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
13
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
14
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
15
, then the
metadata.product_log_id
UDM field is set to
user
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
16
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
17
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
18
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
19
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
20
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
21
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
22
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
23
, then the
metadata.product_log_id
UDM field is set to
mail
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
24
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
25
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
26
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
27
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
28
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
29
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
30
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
31
, then the
metadata.product_log_id
UDM field is set to
daemon
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
32
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
33
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
34
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
35
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
36
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
37
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
38
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
39
, then the
metadata.product_log_id
UDM field is set to
auth
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
40
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
41
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
42
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
43
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
44
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
45
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
46
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
47
, then the
metadata.product_log_id
UDM field is set to
syslog
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
48
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
49
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
50
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
51
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
52
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
53
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
54
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
55
, then the
metadata.product_log_id
UDM field is set to
lpr
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
56
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
57
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
58
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
59
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
60
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
61
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
62
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
63
, then the
metadata.product_log_id
UDM field is set to
news
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
64
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
65
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
66
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
67
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
68
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
69
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
70
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
71
, then the
metadata.product_log_id
UDM field is set to
uucp
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
72
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
73
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
74
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
75
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
76
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
77
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
78
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
79
, then the
metadata.product_log_id
UDM field is set to
cron
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
80
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
81
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
82
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
83
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
84
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
85
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
86
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
87
, then the
metadata.product_log_id
UDM field is set to
authpriv
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
88
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
89
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
90
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
91
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
92
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
93
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
94
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
95
, then the
metadata.product_log_id
UDM field is set to
ftp
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
96
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
97
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
98
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
99
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
100
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
101
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
102
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
103
, then the
metadata.product_log_id
UDM field is set to
ntp
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
104
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
105
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
106
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
107
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
108
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
109
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
110
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
111
, then the
metadata.product_log_id
UDM field is set to
audit
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
112
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
113
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
114
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
115
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
116
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
warning
.
Else, if the
sev
log field value is equal to
117
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
notice
.
Else, if the
sev
log field value is equal to
118
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
informational
.
Else, if the
sev
log field value is equal to
119
, then the
metadata.product_log_id
UDM field is set to
alert
and the
security_result.severity_details
UDM field is set to
debug
.
Else, if the
sev
log field value is equal to
120
, then the
metadata.product_log_id
UDM field is set to
clock
and the
security_result.severity_details
UDM field is set to
emergency
.
Else, if the
sev
log field value is equal to
121
, then the
metadata.product_log_id
UDM field is set to
clock
and the
security_result.severity_details
UDM field is set to
alert
.
Else, if the
sev
log field value is equal to
122
, then the
metadata.product_log_id
UDM field is set to
clock
and the
security_result.severity_details
UDM field is set to
critical
.
Else, if the
sev
log field value is equal to
123
, then the
metadata.product_log_id
UDM field is set to
clock
and the
security_result.severity_details
UDM field is set to
error
.
Else, if the
sev
log field value is equal to
sevs
security_result.severity_details
security_result.severity
If the
security_result.severity_details
log field value contains one of the following values, then the
security_result.severity
UDM field is set to
HIGH
.
error
warning
.
Else, if the
security_result.severity_details
log field value is equal to
critical
, then the
security_result.severity
UDM field is set to
CRITICAL
.
Else, if the
security_result.severity_details
log field value is equal to
notice
, then the
security_result.severity
UDM field is set to
MEDIUM
.
Else, if the
security_result.severity_details
log field value contains one of the following values, then the
security_result.severity
UDM field is set to
LOW
.
information
info
Field mapping reference: /var/log/samba/log.winbindd
The following table lists the log fields of the
/var/log/samba/log.winbindd
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
pid
principal.process.pid
effective_user
principal.user.attribute.labels
effective_group
principal.group.attribute.labels
principal_user_userid
principal.user.userid
effective_group_id
principal.group.product_object_id
metadata_description
metadata.description
security_description
security_result.description
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
Field mapping reference: /var/log/rkhunter.log
The following table lists the log fields of the
/var/log/rkhunter.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
time
metadata.event_timestamp
security_description
security_result.description
metadata_description
metadata.description
file_path
target.file.full_path
target.platform
The
target.platform
UDM field is set to
LINUX
.
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
security_result.severity
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
Field mapping reference: /var/log/syslog.log
The following table lists the log fields of the
/var/log/syslog.log
log type and their corresponding UDM fields.
Log field
UDM mapping
Logic
timestamp
metadata.event_timestamp
hostname
principal.hostname
pid
principal.process.pid
user_id
principal.user.userid
http_method
network.http.method
response_code
network.http.response_code
resource_name
target.url
target_ip_addr
target.ip
target_hostname1
target.hostname
target_hostname1
target.asset.hostname
received_bytes
network.received_bytes
command_line
principal.process.command_line
severity
security_result.severity
If the
severity
log field value is equal to
INFO
, then the
security_result.severity
UDM field is set to
INFORMATIONAL
.
Else, if the
severity
log field value is equal to
ERROR
, then the
security_result.severity
UDM field is set to
ERROR
.
security_description1
security_result.description
If the
security_description1
log field value is
not
empty or the
reason
log field value is
not
empty, then the
%{security_description1} %{reason}
log field is mapped to the
security_result.description
UDM field.
reason
security_result.description
If the
security_description1
log field value is
not
empty or the
reason
log field value is
not
empty, then the
%{security_description1} %{reason}
log field is mapped to the
security_result.description
UDM field.
msg
metadata.description
principal.platform
The
principal.platform
UDM field is set to
LINUX
.
metadata.event_type
The
metadata.event_type
UDM field is set to
GENERIC_EVENT
.
metadata.product_name
The
metadata.product_name
UDM field is set to
Unix System
.
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
