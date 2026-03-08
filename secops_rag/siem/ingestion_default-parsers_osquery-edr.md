# Collect osquery logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/osquery-edr/  
**Scraped:** 2026-03-05T09:17:58.677052Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect osquery logs
Supported in:
Google secops
SIEM
This document describes how you can collect osquery logs by configuring osquery
and a Google Security Operations forwarder. This document also lists the supported log types
and supported osquery versions.
For more information, see
Data ingestion to Google Security Operations
.
Overview
The following deployment architecture diagram shows how osquery agents and Fleet server
are configured to send logs to Google Security Operations. Each customer deployment might
differ from this representation and might be more complex.
The architecture diagram shows the following components:
Linux system
: The Linux system to be monitored in which the osquery agent
is installed
Microsoft Windows system
: The Microsoft Windows system to be monitored in which the osquery agent
is installed
Mac system
: The Mac system to be monitored in which the osquery agent
is installed
osquery agent
: Collects information from the Microsoft Windows, Linux, or Mac
system and forwards the information to the Fleet server
Fleet server
: Monitors and receives information from the
osquery agents, analyzes the logs, and forwards the logs to the Google Security Operations forwarder
Bindplane agent
: The Bindplane agent fetches logs from osquery and sends logs to Google SecOps.
Google Security Operations forwarder
: A lightweight
software component, deployed in the customer's network to forward the logs to Google Security Operations
Google Security Operations
: Retains and analyzes the logs from
the Fleet server
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with
OSQUERY_EDR
ingestion label.
Before you begin
Install Fleet server. To install Fleet server, do the following:
Set up a host
.
Install Fleet server
.
Use an osquery version that the Google Security Operations parser supports, that is, 5.2.3 and 5.3.0.
Verify that all systems in the deployment architecture are configured
in the UTC time zone.
Verify that the table names in Fleet are as per the official Fleet documentation.
Configure osquery agent, server, and Google Security Operations forwarder
To configure the Fleet server and Google Security Operations forwarder, do the following:
To configure the Fleet server, do the following:
Install and configure MYSQL
.
Install and configure Redis
.
Run the fleet server
.
Add hosts to Fleet server and install osquery agent.
You can add your host to Fleet server with an osquery installer. Fleet server helps generate an osquery installer with the fleetctl package command.
Execute the fleetctl package command by
installing the fleetctl command-line tool
.
Install osquery agent by
using the fleetctl package command
.
When you install the generated osquery installer on a host, the host automatically enrolls in the specified Fleet instance.
Fetch the logs from osquery agent. To create a query in Fleet for fetching the logs, see
Create a query
and to schedule a query, see
Schedule a query
.
Configure Google Security Operations forwarder on a central Linux device to push the logs into the Google Security Operations system. For more information, visit
Installing and configuring the forwarder on Linux
. The following is an example of a Google SecOps forwarder configuration:
- file:
      common:
        enabled: true
        data_type: OSQUERY_EDR
        data_hint:
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      skip_seek_to_end: true
      file_path: <log_file_path>
      filter:
Forward Logs to Google SecOps using Bindplane agent
Install and set up a
Linux Virtual Machine
.
Install and configure the Bindplane agent on Linux to forward logs to Google SecOps. For more information about how to install and configure the Bindplane agent, see
the Bindplane agent installation and configuration instructions
.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Supported osquery log formats
The osquery parser supports logs in JSON format.
Supported osquery sample logs
JSON:
{
  "name": "account_policy_data",
  "hostIdentifier": "dummyhostidentifier",
  "calendarTime": "Tue May 17 11:27:28 2022 UTC",
  "unixTime": 1652786848,
  "epoch": 0,
  "counter": 0,
  "numerics": false,
  "decorations": {
    "host_uuid": "dummy_host_uuid",
    "hostname": "dummyhostname"
  },
  "columns": {
    "creation_time": "1637733429.23442",
    "failed_login_count": "0",
    "failed_login_timestamp": "0.0",
    "password_last_set_time": "1645164584.43137",
    "uid": "501"
  },
  "action": "added"
}
Field mapping reference
This section explains how the Google Security Operations parser maps osquery log fields to Google Security Operations Unified Data Model (UDM) fields for the schema and operating system. For more information, see osquery schema for
version 5.2.3
and
version 5.3.0
.
account_policy_data
The following table lists the log fields and corresponding UDM mappings for the schema account_policy_data and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
uid
principal.user.userid
creation_time
principal.user.attribute.creation_time
failed_login_count
principal.user.attribute.labels.key/value
failed_login_timestamp
principal.user.attribute.labels.key/value
password_last_set_time
principal.user.attribute.labels.key/value
ad_config
The following table lists the log fields and corresponding UDM mappings for the schema ad_config and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
about.labels.key/value (deprecated)
additional.fields
domain
target.administrative_domain
option
about.labels.key (deprecated)
additional.fields.key
value
about.labels.value (deprecated)
additional.fields.value.string_value
alf
The following table lists the log fields and corresponding UDM mappings for the schema alf and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
allow_signed_enabled
about.labels.key/value (deprecated)
additional.fields
firewall_unload
about.labels.key/value (deprecated)
additional.fields
global_state
about.labels.key/value (deprecated)
additional.fields
logging_enabled
about.labels.key/value (deprecated)
additional.fields
logging_option
about.labels.key/value (deprecated)
additional.fields
stealth_enabled
about.labels.key/value (deprecated)
additional.fields
version
target.platform_version
alf_exceptions
The following table lists the log fields and corresponding UDM mappings for the schema alf_exceptions and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
state
about.labels.key/value (deprecated)
additional.fields
alf_explicit_auths
The following table lists the log fields and corresponding UDM mappings for the schema alf_explicit_auths and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
process
target.process.pid
app_schemes
The following table lists the log fields and corresponding UDM mappings for the schema app_schemes and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
scheme
about.labels.key/value (deprecated)
additional.fields
handler
about.labels.key/value (deprecated)
additional.fields
enabled
about.labels.key/value (deprecated)
additional.fields
external
about.labels.key/value (deprecated)
additional.fields
protected
about.labels.key/value (deprecated)
additional.fields
apparmor_events
The following table lists the log fields and corresponding UDM mappings for the schema apparmor_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
type
about.labels.key/value (deprecated)
additional.fields
message
metadata.description
time
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
eid
security_result.rule_id
apparmor
security_result.action
operation
about.labels.key/value (deprecated)
additional.fields
parent
target.process.parent_process.pid
profile
about.labels.key/value (deprecated)
additional.fields
name
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
comm
target.process.command_line
denied_mask
about.labels.key/value (deprecated)
additional.fields
capname
about.labels.key/value (deprecated)
additional.fields
fsuid
target.user.attribute.labels.key/value
ouid
target.user.attribute.labels.key/value
capability
about.labels.key/value (deprecated)
additional.fields
requested_mask
target.process.access_mask
info
about.labels.key/value (deprecated)
additional.fields
error
security_result.summary
namespace
about.labels.key/value (deprecated)
additional.fields
label
about.labels.key/value (deprecated)
additional.fields
apparmor_profiles
The following table lists the log fields and corresponding UDM mappings for the schema apparmor_profiles and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
name
target.resource.name
attach
about.labels.key/value (deprecated)
additional.fields
mode
about.labels.key/value (deprecated)
additional.fields
sha1
target.file.sha1
apps
The following table lists the log fields and corresponding UDM mappings for the schema apps and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
target.application
path
target.file.full_path
bundle_executable
about.labels.key/value (deprecated)
additional.fields
bundle_identifier
target.resource.product_object_id
bundle_name
target.resource.name
bundle_short_version
target.resource.attribute.labels.key/value
bundle_version
target.resource.attribute.labels.key/value
bundle_package_type
about.labels.key/value (deprecated)
additional.fields
environment
about.labels.key/value (deprecated)
additional.fields
element
about.labels.key/value (deprecated)
additional.fields
compiler
about.labels.key/value (deprecated)
additional.fields
development_region
about.location.country_or_region
display_name
about.labels.key/value (deprecated)
additional.fields
info_string
about.labels.key/value (deprecated)
additional.fields
minimum_system_version
about.labels.key/value (deprecated)
additional.fields
category
about.labels.key/value (deprecated)
additional.fields
applescript_enabled
about.labels.key/value (deprecated)
additional.fields
copyright
about.labels.key/value (deprecated)
additional.fields
last_opened_time
target.file.last_seen_time
asl
The following table lists the log fields and corresponding UDM mappings for the schema asl and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
time
about.labels.key/value (deprecated)
additional.fields
time_nano_sec
about.labels.key/value (deprecated)
additional.fields
host
target.hostname
sender
about.labels.key/value (deprecated)
additional.fields
facility
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
gid
target.user.group_identifiers
uid
target.user.userid
level
about.labels.key/value (deprecated)
additional.fields
message
metadata.description
ref_pid
about.labels.key/value (deprecated)
additional.fields
ref_proc
about.labels.key/value (deprecated)
additional.fields
extra
about.labels.key/value (deprecated)
additional.fields
authenticode
The following table lists the log fields and corresponding UDM mappings for the schema authenticode and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
original_program_name
about.labels.key/value (deprecated)
additional.fields
serial_number
network.tls.client.certificate.serial
issuer_name
network.tls.client.certificate.issuer
subject_name
network.tls.client.certificate.subject
result
security_result.summary
authorization_mechanisms
The following table lists the log fields and corresponding UDM mappings for the schema authorization_mechanisms and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
label
about.labels.key/value (deprecated)
additional.fields
plugin
about.labels.key/value (deprecated)
additional.fields
mechanism
about.labels.key/value (deprecated)
additional.fields
privileged
about.labels.key/value (deprecated)
additional.fields
entry
about.labels.key/value (deprecated)
additional.fields
authorizations
The following table lists the log fields and corresponding UDM mappings for the schema authorizations and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
label
about.labels.key/value (deprecated)
additional.fields
modified
about.labels.key/value (deprecated)
additional.fields
allow_root
about.labels.key/value (deprecated)
additional.fields
timeout
about.labels.key/value (deprecated)
additional.fields
version
about.labels.key/value (deprecated)
additional.fields
tries
about.labels.key/value (deprecated)
additional.fields
authenticate_user
about.labels.key/value (deprecated)
additional.fields
shared
about.labels.key/value (deprecated)
additional.fields
comment
about.labels.key/value (deprecated)
additional.fields
created
about.labels.key/value (deprecated)
additional.fields
class
about.labels.key/value (deprecated)
additional.fields
session_owner
about.labels.key/value (deprecated)
additional.fields
autoexec
The following table lists the log fields and corresponding UDM mappings for the schema autoexec and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
name
target.application
source
target.resource.name
bitlocker_info
The following table lists the log fields and corresponding UDM mappings for the schema bitlocker_info and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
device_id
target.resource.product_object_id
drive_letter
target.resource.name
persistent_volume_id
about.labels.key/value (deprecated)
additional.fields
conversion_status
target.resource.attirbute.labels.key/value
protection_status
target.resource.attirbute.labels.key/value
encryption_method
target.resource.attirbute.labels.key/value
version
metadata.product_version
percentage_encrypted
target.resource.attirbute.labels.key/value
lock_status
target.resource.attirbute.labels.key/value
bpf_process_events
The following table lists the log fields and corresponding UDM mappings for the schema bpf_process_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
tid
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
parent
target.process.parent_process.pid
uid
principal.user.userid
gid
principal.group.product_object_id
cid
about.labels.key/value (deprecated)
additional.fields
exit_code
about.labels.key/value (deprecated)
additional.fields
probe_error
about.labels.key/value (deprecated)
additional.fields
syscall
about.labels.key/value (deprecated)
additional.fields
path
target.process.file.full_path
cwd
about.labels.key/value (deprecated)
additional.fields
cmdline
target.process.command_line
duration
about.labels.key/value (deprecated)
additional.fields
json_cmdline
about.labels.key/value (deprecated)
additional.fields
ntime
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
bpf_socket_events
The following table lists the log fields and corresponding UDM mappings for the schema bpf_socket_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
tid
about.labels.key/value (deprecated)
additional.fields
pid
principal.process.pid
parent
principal.process.parent_process.pid
uid
principal.user.userid
gid
principal.group.product_object_id
cid
about.labels.key/value (deprecated)
additional.fields
exit_code
about.labels.key/value (deprecated)
additional.fields
probe_error
about.labels.key/value (deprecated)
additional.fields
syscall
about.labels.key/value (deprecated)
additional.fields
path
target.file.full_path
fd
about.labels.key/value (deprecated)
additional.fields
family
about.labels.key/value (deprecated)
additional.fields
type
about.labels.key/value (deprecated)
additional.fields
protocol
about.labels.key/value (deprecated)
additional.fields
local_address
principal.ip
remote_address
target.ip
local_port
principal.port
remote_port
target.port
duration
about.labels.key/value (deprecated)
additional.fields
ntime
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
certificates
The following table lists the log fields and corresponding UDM mappings for the schema certificates and OS macOS, Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
common_name
about.labels.key/value (deprecated)
additional.fields
subject
network.tls.client.certificate.subject
issuer
network.tls.client.certificate.issuer
ca
about.labels.key/value (deprecated)
additional.fields
self_signed
about.labels.key/value (deprecated)
additional.fields
not_valid_before
network.tls.client.certificate.not_before
not_valid_after
network.tls.client.certificate.not_after
signing_algorithm
about.labels.key/value (deprecated)
additional.fields
key_algorithm
about.labels.key/value (deprecated)
additional.fields
key_strength
about.labels.key/value (deprecated)
additional.fields
key_usage
about.labels.key/value (deprecated)
additional.fields
subject_key_id
about.labels.key/value (deprecated)
additional.fields
authority_key_id
about.labels.key/value (deprecated)
additional.fields
sha1
network.tls.client.certificate.sha1
path
about.labels.key/value (deprecated)
additional.fields
serial
network.tls.client.certificate.serial
sid
about.labels.key/value (deprecated)
additional.fields
store_location
about.labels.key/value (deprecated)
additional.fields
store
about.labels.key/value (deprecated)
additional.fields
username
principal.user.user_display_name
store_id
about.labels.key/value (deprecated)
additional.fields
chassis_info
The following table lists the log fields and corresponding UDM mappings for the schema chassis_info and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
audible_alarm
about.labels.key/value (deprecated)
additional.fields
breach_description
security_result.description
chassis_types
about.labels.key/value (deprecated)
additional.fields
description
metadata.description
lock
about.labels.key/value (deprecated)
additional.fields
manufacturer
principal.asset.hardware.manufacturer
model
principal.asset.hardware.model
security_breach
security_result.detection_fields.key/value
serial
principal.asset.hardware.serial_number
smbios_tag
about.labels.key/value (deprecated)
additional.fields
sku
about.labels.key/value (deprecated)
additional.fields
status
about.labels.key/value (deprecated)
additional.fields
visible_alarm
about.labels.key/value (deprecated)
additional.fields
chrome_extensions
The following table lists the log fields and corresponding UDM mappings for the schema chrome_extensions and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
browser_type
target.resource.attribute.labels.key/value
uid
principal.user.userid
name
target.resource.name
profile
target.resource.attribute.labels.key/value
profile_path
target.resource.attribute.labels.key/value
referenced_identifier
target.resource.attribute.labels.key/value
identifier
target.resource.attribute.labels.key/value
version
target.resource.attribute.labels.key/value
description
target.resource.attribute.labels.key/value
default_locale
target.resource.attribute.labels.key/value
current_locale
target.resource.attribute.labels.key/value
update_url
network.http.referral_url
author
target.resource.attribute.labels.key/value
persistent
target.resource.attribute.labels.key/value
path
target.file.full_path
permissions
target.resource.attribute.labels.key/value
permissions_json
target.resource.attribute.labels.key/value
optional_permissions
target.resource.attribute.labels.key/value
optional_permissions_json
target.resource.attribute.labels.key/value
manifest_hash
target.resource.attribute.labels.key/value
referenced
target.resource.attribute.labels.key/value
from_webstore
target.resource.attribute.labels.key/value
state
target.resource.attribute.labels.key/value
install_time
target.resource.attribute.labels.key/value
install_timestamp
target.resource.attribute.labels.key/value
manifest_json
target.resource.attribute.labels.key/value
key
target.resource.attribute.labels.key/value
connectivity
The following table lists the log fields and corresponding UDM mappings for the schema connectivity and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
disconnected
about.labels.key/value (deprecated)
additional.fields
ipv4_no_traffic
about.labels.key/value (deprecated)
additional.fields
ipv6_no_traffic
about.labels.key/value (deprecated)
additional.fields
ipv4_subnet
about.labels.key/value (deprecated)
additional.fields
ipv4_local_network
about.labels.key/value (deprecated)
additional.fields
ipv4_internet
about.labels.key/value (deprecated)
additional.fields
ipv6_subnet
about.labels.key/value (deprecated)
additional.fields
ipv6_local_network
about.labels.key/value (deprecated)
additional.fields
ipv6_internet
about.labels.key/value (deprecated)
additional.fields
cpu_info
The following table lists the log fields and corresponding UDM mappings for the schema cpu_info and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
device_id
principal.asset.product_object_id
model
principal.asset.hardware.model
manufacturer
principal.asset.hardware.manufacturer
processor_type
about.labels.key/value (deprecated)
additional.fields
availability
about.labels.key/value (deprecated)
additional.fields
cpu_status
about.labels.key/value (deprecated)
additional.fields
number_of_cores
principal.asset.hardware.cpu_number_cores
logical_processors
about.labels.key/value (deprecated)
additional.fields
address_width
about.labels.key/value (deprecated)
additional.fields
current_clock_speed
principal.asset.hardware.cpu_clock_speed
max_clock_speed
principal.asset.hardware.cpu_max_clock_speed
socket_designation
about.labels.key/value (deprecated)
additional.fields
crashes
The following table lists the log fields and corresponding UDM mappings for the schema crashes and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
type
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
path
target.process.file.full_path
crash_path
target.file.full_path
identifier
about.labels.key/value (deprecated)
additional.fields
version
about.labels.key/value (deprecated)
additional.fields
parent
target.process.parent_process.pid
responsible
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
datetime
metadata.event_timestamp
crashed_thread
about.labels.key/value (deprecated)
additional.fields
stack_trace
about.labels.key/value (deprecated)
additional.fields
exception_type
about.labels.key/value (deprecated)
additional.fields
exception_codes
about.labels.key/value (deprecated)
additional.fields
exception_notes
about.labels.key/value (deprecated)
additional.fields
registers
about.labels.key/value (deprecated)
additional.fields
crontab
The following table lists the log fields and corresponding UDM mappings for the schema crontab and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
event
about.labels.key/value (deprecated)
additional.fields
minute
about.labels.key/value (deprecated)
additional.fields
hour
about.labels.key/value (deprecated)
additional.fields
day_of_month
about.labels.key/value (deprecated)
additional.fields
month
about.labels.key/value (deprecated)
additional.fields
day_of_week
about.labels.key/value (deprecated)
additional.fields
command
principal.process.command_line
path
principal.process.file.full_path
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
curl
The following table lists the log fields and corresponding UDM mappings for the schema curl and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
url
network.http.referral_url
method
network.http.method
user_agent
network.http.user_agent
response_code
network.http.response_code
round_trip_time
network.session_duration
bytes
network.received_bytes
result
about.labels.key/value (deprecated)
additional.fields
curl_certificate
The following table lists the log fields and corresponding UDM mappings for the schema curl_certificate and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
hostname
principal.hostname
common_name
about.labels.key/value (deprecated)
additional.fields
organization
network.organization_name
organization_unit
about.labels.key/value (deprecated)
additional.fields
serial_number
network.tls.server.certificate.serial
issuer_common_name
about.labels.key/value (deprecated)
additional.fields
issuer_organization
network.tls.server.certificate.issuer
issuer_organization_unit
about.labels.key/value (deprecated)
additional.fields
valid_from
network.tls.server.certificate.not_before
valid_to
network.tls.server.certificate.not_after
sha256_fingerprint
network.tls.server.certificate.sha256
sha1_fingerprint
network.tls.server.certificate.sha1
version
network.tls.server.certificate.version
signature_algorithm
about.labels.key/value (deprecated)
additional.fields
signature
about.labels.key/value (deprecated)
additional.fields
subject_key_identifier
about.labels.key/value (deprecated)
additional.fields
authority_key_identifier
about.labels.key/value (deprecated)
additional.fields
key_usage
about.labels.key/value (deprecated)
additional.fields
extended_key_usage
about.labels.key/value (deprecated)
additional.fields
policies
about.labels.key/value (deprecated)
additional.fields
subject_alternative_names
about.labels.key/value (deprecated)
additional.fields
issuer_alternative_names
about.labels.key/value (deprecated)
additional.fields
info_access
about.labels.key/value (deprecated)
additional.fields
subject_info_access
about.labels.key/value (deprecated)
additional.fields
policy_mappings
about.labels.key/value (deprecated)
additional.fields
has_expired
about.labels.key/value (deprecated)
additional.fields
basic_constraint
about.labels.key/value (deprecated)
additional.fields
name_constraints
about.labels.key/value (deprecated)
additional.fields
policy_constraints
about.labels.key/value (deprecated)
additional.fields
dump_certificate
about.labels.key/value (deprecated)
additional.fields
timeout
about.labels.key/value (deprecated)
additional.fields
pem
about.labels.key/value (deprecated)
additional.fields
device_file
The following table lists the log fields and corresponding UDM mappings for the schema device_file and OS Linux, macOS, freebsd, Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
device
about.labels.key/value (deprecated)
additional.fields
partition
about.labels.key/value (deprecated)
additional.fields
path
target.file.full_path
filename
target.file.names
inode
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
gid
target.group.product_object_id
mode
about.labels.key/value (deprecated)
additional.fields
size
target.file.size
block_size
about.labels.key/value (deprecated)
additional.fields
atime
about.labels.key/value (deprecated)
additional.fields
mtime
target.file.last_modification_time
ctime
about.labels.key/value (deprecated)
additional.fields
hard_links
about.labels.key/value (deprecated)
additional.fields
type
about.labels.key/value (deprecated)
additional.fields
device_hash
The following table lists the log fields and corresponding UDM mappings for the schema device_hash and OS Linux, macOS, freebsd, Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
device
target.file.full_path
partition
about.labels.key/value (deprecated)
additional.fields
inode
about.labels.key/value (deprecated)
additional.fields
md5
target.file.md5
sha1
target.file.sha1
sha256
target.file.sha56
disk_info
The following table lists the log fields and corresponding UDM mappings for the schema disk_info and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
partitions
principal.asset.attribute.labels.key/value
disk_index
principal.asset.attribute.labels.key/value
type
principal.asset.attribute.labels.key/value
id
principal.asset.product_object_id
pnp_device_id
about.labels.key/value (deprecated)
additional.fields
disk_size
principal.asset.attribute.labels.key/value
manufacturer
principal.asset.hardware.manufacturer
hardware_model
principal.asset.hardware.model
name
principal.asset.attribute.labels.key/value
serial
principal.asset.hardware.serial_number
description
principal.asset.attribute.labels.key/value
dns_cache
The following table lists the log fields and corresponding UDM mappings for the schema dns_cache and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
network.dns.additional.name
type
about.labels.key/value (deprecated)
additional.fields
flags
about.labels.key/value (deprecated)
additional.fields
dns_resolvers
The following table lists the log fields and corresponding UDM mappings for the schema dns_resolvers and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
about.labels.key/value (deprecated)
additional.fields
type
about.labels.key/value (deprecated)
additional.fields
address
principal.ip
netmask
about.labels.key/value (deprecated)
additional.fields
options
about.labels.key/value (deprecated)
additional.fields
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
docker_container_networks
The following table lists the log fields and corresponding UDM mappings for the schema docker_container_networks and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.asset.product_object_id
name
network.carrier_name
network_id
about.labels.key/value (deprecated)
additional.fields
endpoint_id
about.labels.key/value (deprecated)
additional.fields
gateway
about.labels.key/value (deprecated)
additional.fields
ip_address
target.ip
ip_prefix_len
about.labels.key/value (deprecated)
additional.fields
ipv6_gateway
about.labels.key/value (deprecated)
additional.fields
ipv6_address
target.ip
ipv6_prefix_len
about.labels.key/value (deprecated)
additional.fields
mac_address
target.mac
docker_container_ports
The following table lists the log fields and corresponding UDM mappings for the schema docker_container_ports and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.asset.product_object_id
type
network.ip_protocol
port
target.port
host_ip
principal.ip
host_port
principal.port
docker_container_processes
The following table lists the log fields and corresponding UDM mappings for the schema docker_container_processes and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.asset.product_object_id
pid
target.process.pid
name
target.process.file.full_path
cmdline
target.process.command_line
state
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
gid
target.group.product_object_id
euid
target.user.attribute.labels.key/value
egid
target.group.attribute.labels.key/value
suid
target.user.attribute.labels.key/value
sgid
target.group.attribute.labels.key/value
wired_size
about.labels.key/value (deprecated)
additional.fields
resident_size
about.labels.key/value (deprecated)
additional.fields
total_size
about.labels.key/value (deprecated)
additional.fields
start_time
about.labels.key/value (deprecated)
additional.fields
parent
target.process.parent_process.pid
pgroup
about.labels.key/value (deprecated)
additional.fields
threads
about.labels.key/value (deprecated)
additional.fields
nice
about.labels.key/value (deprecated)
additional.fields
user
target.user.user_display_name
time
about.labels.key/value (deprecated)
additional.fields
cpu
about.labels.key/value (deprecated)
additional.fields
mem
about.labels.key/value (deprecated)
additional.fields
docker_container_stats
The following table lists the log fields and corresponding UDM mappings for the schema docker_container_stats and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.resource.product_object_id
name
target.resource.name
pids
about.labels.key/value (deprecated)
additional.fields
read
about.labels.key/value (deprecated)
additional.fields
preread
about.labels.key/value (deprecated)
additional.fields
interval
about.labels.key/value (deprecated)
additional.fields
disk_read
about.labels.key/value (deprecated)
additional.fields
disk_write
about.labels.key/value (deprecated)
additional.fields
num_procs
about.labels.key/value (deprecated)
additional.fields
cpu_total_usage
about.labels.key/value (deprecated)
additional.fields
cpu_kernelmode_usage
about.labels.key/value (deprecated)
additional.fields
cpu_usermode_usage
about.labels.key/value (deprecated)
additional.fields
system_cpu_usage
about.labels.key/value (deprecated)
additional.fields
online_cpus
about.labels.key/value (deprecated)
additional.fields
pre_cpu_total_usage
about.labels.key/value (deprecated)
additional.fields
pre_cpu_kernelmode_usage
about.labels.key/value (deprecated)
additional.fields
pre_cpu_usermode_usage
about.labels.key/value (deprecated)
additional.fields
pre_system_cpu_usage
about.labels.key/value (deprecated)
additional.fields
pre_online_cpus
about.labels.key/value (deprecated)
additional.fields
memory_usage
about.labels.key/value (deprecated)
additional.fields
memory_max_usage
about.labels.key/value (deprecated)
additional.fields
memory_limit
about.labels.key/value (deprecated)
additional.fields
network_rx_bytes
about.labels.key/value (deprecated)
additional.fields
network_tx_bytes
about.labels.key/value (deprecated)
additional.fields
docker_info
The following table lists the log fields and corresponding UDM mappings for the schema docker_info and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.resource.product_object_id
containers
about.labels.key/value (deprecated)
additional.fields
containers_running
about.labels.key/value (deprecated)
additional.fields
containers_paused
about.labels.key/value (deprecated)
additional.fields
containers_stopped
about.labels.key/value (deprecated)
additional.fields
images
about.labels.key/value (deprecated)
additional.fields
storage_driver
about.labels.key/value (deprecated)
additional.fields
memory_limit
about.labels.key/value (deprecated)
additional.fields
swap_limit
about.labels.key/value (deprecated)
additional.fields
kernel_memory
about.labels.key/value (deprecated)
additional.fields
cpu_cfs_period
about.labels.key/value (deprecated)
additional.fields
cpu_cfs_quota
about.labels.key/value (deprecated)
additional.fields
cpu_shares
about.labels.key/value (deprecated)
additional.fields
cpu_set
about.labels.key/value (deprecated)
additional.fields
ipv4_forwarding
about.labels.key/value (deprecated)
additional.fields
bridge_nf_iptables
about.labels.key/value (deprecated)
additional.fields
bridge_nf_ip6tables
about.labels.key/value (deprecated)
additional.fields
oom_kill_disable
about.labels.key/value (deprecated)
additional.fields
logging_driver
about.labels.key/value (deprecated)
additional.fields
cgroup_driver
about.labels.key/value (deprecated)
additional.fields
kernel_version
about.labels.key/value (deprecated)
additional.fields
os
about.labels.key/value (deprecated)
additional.fields
os_type
target.platform(enum)
architecture
about.labels.key/value (deprecated)
additional.fields
cpus
about.labels.key/value (deprecated)
additional.fields
memory
about.labels.key/value (deprecated)
additional.fields
http_proxy
about.labels.key/value (deprecated)
additional.fields
https_proxy
about.labels.key/value (deprecated)
additional.fields
no_proxy
about.labels.key/value (deprecated)
additional.fields
name
target.hostname
server_version
target.platform_version
root_dir
target.file.full_path
docker_network_labels
The following table lists the log fields and corresponding UDM mappings for the schema docker_network_labels and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.resource.product_object_id
key
target.resource.attribute.labels.key/value
value
about.labels.key/value (deprecated)
additional.fields
docker_networks
The following table lists the log fields and corresponding UDM mappings for the schema docker_networks and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
id
target.resource.product_object_id
name
about.labels.key/value (deprecated)
additional.fields
driver
about.labels.key/value (deprecated)
additional.fields
created
target.resource.attribute.creation_time
enable_ipv6
about.labels.key/value (deprecated)
additional.fields
subnet
about.labels.key/value (deprecated)
additional.fields
gateway
about.labels.key/value (deprecated)
additional.fields
ec2_instance_metadata
The following table lists the log fields and corresponding UDM mappings for the schema ec2_instance_metadata and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
instance_id
target.resource.product_object_id
instance_type
about.labels.key/value (deprecated)
additional.fields
architecture
about.labels.key/value (deprecated)
additional.fields
region
target.location.country_or_region
availability_zone
about.labels.key/value (deprecated)
additional.fields
local_hostname
target.hostname
local_ipv4
target.ip
mac
target.mac
security_groups
about.labels.key/value (deprecated)
additional.fields
iam_arn
about.labels.key/value (deprecated)
additional.fields
ami_id
about.labels.key/value (deprecated)
additional.fields
reservation_id
about.labels.key/value (deprecated)
additional.fields
account_id
target.user.userid
ssh_public_key
about.labels.key/value (deprecated)
additional.fields
es_process_events
The following table lists the log fields and corresponding UDM mappings for the schema es_process_events and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
version
target.platform_version
seq_num
about.labels.key/value (deprecated)
additional.fields
global_seq_num
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
path
target.process.file.full_path
parent
target.process.parent_process.pid
original_parent
about.labels.key/value (deprecated)
additional.fields
cmdline
target.process.command_line
cmdline_count
about.labels.key/value (deprecated)
additional.fields
env
about.labels.key/value (deprecated)
additional.fields
env_count
about.labels.key/value (deprecated)
additional.fields
cwd
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
euid
about.labels.key/value (deprecated)
additional.fields
gid
target.group.product_object_id
egid
about.labels.key/value (deprecated)
additional.fields
username
target.user.user_display_name
signing_id
about.labels.key/value (deprecated)
additional.fields
team_id
about.labels.key/value (deprecated)
additional.fields
cdhash
about.labels.key/value (deprecated)
additional.fields
platform_binary
about.labels.key/value (deprecated)
additional.fields
exit_code
about.labels.key/value (deprecated)
additional.fields
child_pid
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
event_type
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
etc_hosts
The following table lists the log fields and corresponding UDM mappings for the schema etc_hosts and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
address
target.ip
hostnames
about.hostname
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
etc_protocols
The following table lists the log fields and corresponding UDM mappings for the schema etc_protocols and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
network.ip_protocol
number
about.labels.key/value (deprecated)
additional.fields
alias
about.labels.key/value (deprecated)
additional.fields
comment
about.labels.key/value (deprecated)
additional.fields
etc_services
The following table lists the log fields and corresponding UDM mappings for the schema etc_services and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
target.resource.name
port
target.port
protocol
network.ip_protocol
aliases
about.labels.key/value (deprecated)
additional.fields
comment
about.labels.key/value (deprecated)
additional.fields
file
The following table lists the log fields and corresponding UDM mappings for the schema file and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
directory
about.labels.key/value (deprecated)
additional.fields
filename
target.file.names
inode
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
gid
target.group.product_object_id
mode
about.labels.key/value (deprecated)
additional.fields
device
target.asset.asset_id
size
target.file.size
block_size
about.labels.key/value (deprecated)
additional.fields
atime
target.file.last_seen_time
mtime
target.file.last_modification_time
ctime
about.labels.key/value (deprecated)
additional.fields
btime
about.labels.key/value (deprecated)
additional.fields
hard_links
about.labels.key/value (deprecated)
additional.fields
symlink
about.labels.key/value (deprecated)
additional.fields
type
about.labels.key/value (deprecated)
additional.fields
attributes
about.labels.key/value (deprecated)
additional.fields
volume_serial
about.labels.key/value (deprecated)
additional.fields
file_id
about.labels.key/value (deprecated)
additional.fields
file_version
about.labels.key/value (deprecated)
additional.fields
product_version
about.labels.key/value (deprecated)
additional.fields
bsd_flags
about.labels.key/value (deprecated)
additional.fields
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
mount_namespace_id
about.labels.key/value (deprecated)
additional.fields
file_events
The following table lists the log fields and corresponding UDM mappings for the schema file_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
operation
about.labels.key/value (deprecated)
additional.fields
pid
principal.process.pid
ppid
principal.process.parent_process.pid
time
about.labels.key/value (deprecated)
additional.fields
executable
about.labels.key/value (deprecated)
additional.fields
partial
about.labels.key/value (deprecated)
additional.fields
cwd
about.labels.key/value (deprecated)
additional.fields
path
src.file.full_path
dest_path
target.file.full_path
uid
principal.user.userid
gid
principal.group.product_object_id
auid
about.labels.key/value (deprecated)
additional.fields
euid
about.labels.key/value (deprecated)
additional.fields
egid
about.labels.key/value (deprecated)
additional.fields
fsuid
about.labels.key/value (deprecated)
additional.fields
fsgid
about.labels.key/value (deprecated)
additional.fields
suid
about.labels.key/value (deprecated)
additional.fields
sgid
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
gatekeeper
The following table lists the log fields and corresponding UDM mappings for the schema gatekeeper and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
assessments_enabled
about.labels.key/value (deprecated)
additional.fields
dev_id_enabled
about.labels.key/value (deprecated)
additional.fields
version
target.asset.software.version
opaque_version
about.labels.key/value (deprecated)
additional.fields
gatekeeper_approved_apps
The following table lists the log fields and corresponding UDM mappings for the schema gatekeeper_approved_apps and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
requirement
about.labels.key/value (deprecated)
additional.fields
ctime
about.labels.key/value (deprecated)
additional.fields
mtime
target.resource.attribute.last_update_time
groups
The following table lists the log fields and corresponding UDM mappings for the schema groups and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
gid
target.group.attribute.labels.key/value
gid_signed
target.group.attribute.labels.key/value
groupname
target.group.group_display_name
group_sid
target.group.product_object_id
comment
target.group.attribute.labels.key/value
is_hidden
target.group.attribute.labels.key/value
pid_with_namespace
target.group.attribute.labels.key/value
hardware_events
The following table lists the log fields and corresponding UDM mappings for the schema hardware_events and OS Linux, macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
action
security_result.action_details
path
target.asset.attribute.labels.key/value
type
target.asset.attribute.labels.key/value
driver
target.asset.attribute.labels.key/value
vendor
target.asset.attribute.labels.key/value
vendor_id
target.asset.attribute.labels.key/value
model
target.asset.hardware.model
model_id
target.asset.attribute.labels.key/value
serial
target.asset.attribute.labels.key/value
revision
target.asset.attribute.labels.key/value
time
metadata.event_timestamp
eid
metadata.product_log_id
hash
The following table lists the log fields and corresponding UDM mappings for the schema hash and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
directory
about.labels.key/value (deprecated)
additional.fields
md5
target.file.md5
sha1
target.file.sha1
sha256
target.file.sha256
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
mount_namespace_id
about.labels.key/value (deprecated)
additional.fields
interface_addresses
The following table lists the log fields and corresponding UDM mappings for the schema interface_addresses and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
interface
about.labels.key/value (deprecated)
additional.fields
address
target.ip
mask
about.labels.key/value (deprecated)
additional.fields
broadcast
about.labels.key/value (deprecated)
additional.fields
point_to_point
about.labels.key/value (deprecated)
additional.fields
type
about.labels.key/value (deprecated)
additional.fields
friendly_name
about.labels.key/value (deprecated)
additional.fields
interface_details
The following table lists the log fields and corresponding UDM mappings for the schema interface_details and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
interface
about.labels.key/value (deprecated)
additional.fields
mac
target.mac
type
about.labels.key/value (deprecated)
additional.fields
mtu
about.labels.key/value (deprecated)
additional.fields
metric
about.labels.key/value (deprecated)
additional.fields
flags
about.labels.key/value (deprecated)
additional.fields
ipackets
about.labels.key/value (deprecated)
additional.fields
opackets
about.labels.key/value (deprecated)
additional.fields
ibytes
network.sent_bytes
obytes
network.received_bytes
ierrors
about.labels.key/value (deprecated)
additional.fields
oerrors
about.labels.key/value (deprecated)
additional.fields
idrops
about.labels.key/value (deprecated)
additional.fields
odrops
about.labels.key/value (deprecated)
additional.fields
collisions
about.labels.key/value (deprecated)
additional.fields
last_change
about.labels.key/value (deprecated)
additional.fields
link_speed
about.labels.key/value (deprecated)
additional.fields
pci_slot
about.labels.key/value (deprecated)
additional.fields
friendly_name
about.labels.key/value (deprecated)
additional.fields
description
about.labels.key/value (deprecated)
additional.fields
manufacturer
target.asset.hardware.manufacturer
connection_id
about.labels.key/value (deprecated)
additional.fields
connection_status
about.labels.key/value (deprecated)
additional.fields
enabled
about.labels.key/value (deprecated)
additional.fields
physical_adapter
about.labels.key/value (deprecated)
additional.fields
speed
about.labels.key/value (deprecated)
additional.fields
service
target.application
dhcp_enabled
about.labels.key/value (deprecated)
additional.fields
dhcp_lease_expires
network.dhcp.lease_time_seconds
dhcp_lease_obtained
about.labels.key/value (deprecated)
additional.fields
dhcp_server
network.dhcp.yiaddr
dns_domain
network.dns.questions.name
dns_domain_suffix_search_order
about.labels.key/value (deprecated)
additional.fields
dns_host_name
about.labels.key/value (deprecated)
additional.fields
dns_server_search_order
about.labels.key/value (deprecated)
additional.fields
interface_ipv6
The following table lists the log fields and corresponding UDM mappings for the schema interface_ipv6 and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
interface
about.labels.key/value (deprecated)
additional.fields
hop_limit
about.labels.key/value (deprecated)
additional.fields
forwarding_enabled
about.labels.key/value (deprecated)
additional.fields
redirect_accept
about.labels.key/value (deprecated)
additional.fields
rtadv_accept
about.labels.key/value (deprecated)
additional.fields
iptables
The following table lists the log fields and corresponding UDM mappings for the schema iptables and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
filter_name
about.labels.key/value (deprecated)
additional.fields
chain
about.labels.key/value (deprecated)
additional.fields
policy
about.labels.key/value (deprecated)
additional.fields
target
about.labels.key/value (deprecated)
additional.fields
protocol
about.labels.key/value (deprecated)
additional.fields
src_port
src.port
dst_port
target.port
src_ip
src.ip
src_mask
about.labels.key/value (deprecated)
additional.fields
iniface
about.labels.key/value (deprecated)
additional.fields
iniface_mask
about.labels.key/value (deprecated)
additional.fields
dst_ip
target.ip
dst_mask
about.labels.key/value (deprecated)
additional.fields
outiface
about.labels.key/value (deprecated)
additional.fields
outiface_mask
about.labels.key/value (deprecated)
additional.fields
match
about.labels.key/value (deprecated)
additional.fields
packets
about.labels.key/value (deprecated)
additional.fields
bytes
network.received_bytes
kernel_panics
The following table lists the log fields and corresponding UDM mappings for the schema kernel_panics and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
time
about.labels.key/value (deprecated)
additional.fields
registers
about.labels.key/value (deprecated)
additional.fields
frame_backtrace
about.labels.key/value (deprecated)
additional.fields
module_backtrace
about.labels.key/value (deprecated)
additional.fields
dependencies
about.labels.key/value (deprecated)
additional.fields
name
target.process.command_line
os_version
target.platform_version
kernel_version
about.labels.key/value (deprecated)
additional.fields
system_model
target.asset.hardware.model
uptime
about.labels.key/value (deprecated)
additional.fields
last_loaded
about.labels.key/value (deprecated)
additional.fields
last_unloaded
about.labels.key/value (deprecated)
additional.fields
keychain_acls
The following table lists the log fields and corresponding UDM mappings for the schema keychain_acls and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
keychain_path
about.labels.key/value (deprecated)
additional.fields
authorizations
about.labels.key/value (deprecated)
additional.fields
path
target.file.full_path
description
metadata.description
label
about.labels.key/value (deprecated)
additional.fields
known_hosts
The following table lists the log fields and corresponding UDM mappings for the schema known_hosts and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
uid
target.user.userid
key
about.labels.key/value (deprecated)
additional.fields
key_file
target.file.full_path
last
The following table lists the log fields and corresponding UDM mappings for the schema last and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
username
target.user.user_display_name
tty
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
type
about.labels.key/value (deprecated)
additional.fields
type_name
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
host
target.hostname
listening_ports
The following table lists the log fields and corresponding UDM mappings for the schema listening_ports and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
pid
target.process.pid
port
target.port
protocol
network.ip_protocol
family
about.labels.key/value (deprecated)
additional.fields
address
target.ip
fd
about.labels.key/value (deprecated)
additional.fields
socket
about.labels.key/value (deprecated)
additional.fields
path
target.process.file.full_path
net_namespace
about.labels.key/value (deprecated)
additional.fields
logged_in_users
The following table lists the log fields and corresponding UDM mappings for the schema logged_in_users and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
type
about.labels.key/value (deprecated)
additional.fields
user
target.user.userid
tty
about.labels.key/value (deprecated)
additional.fields
host
target.hostname
time
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
sid
about.labels.key/value (deprecated)
additional.fields
registry_hive
about.labels.key/value (deprecated)
additional.fields
logon_sessions
The following table lists the log fields and corresponding UDM mappings for the schema logon_sessions and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
logon_id
about.labels.key/value (deprecated)
additional.fields
user
target.user.user_display_name
logon_domain
about.labels.key/value (deprecated)
additional.fields
authentication_package
about.labels.key/value (deprecated)
additional.fields
logon_type
about.labels.key/value (deprecated)
additional.fields
session_id
network.session_id
logon_sid
about.labels.key/value (deprecated)
additional.fields
logon_time
about.labels.key/value (deprecated)
additional.fields
logon_server
about.labels.key/value (deprecated)
additional.fields
dns_domain_name
network.dns_domain
upn
about.labels.key/value (deprecated)
additional.fields
logon_script
about.labels.key/value (deprecated)
additional.fields
profile_path
target.file.full_path
home_directory
about.labels.key/value (deprecated)
additional.fields
home_directory_drive
about.labels.key/value (deprecated)
additional.fields
lxd_certificates
The following table lists the log fields and corresponding UDM mappings for the schema lxd_certificates and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
security_result.detection_fields.key/value
type
security_result.detection_fields.key/value
fingerprint
security_result.detection_fields.key/value
certificate
security_result.detection_fields.key/value
lxd_networks
The following table lists the log fields and corresponding UDM mappings for the schema lxd_networks and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
about.labels.key/value (deprecated)
additional.fields
type
about.labels.key/value (deprecated)
additional.fields
managed
about.labels.key/value (deprecated)
additional.fields
ipv4_address
about.labels.key/value (deprecated)
additional.fields
ipv6_address
about.labels.key/value (deprecated)
additional.fields
used_by
about.labels.key/value (deprecated)
additional.fields
bytes_received
network.received_bytes
bytes_sent
network.sent_bytes
packets_received
about.labels.key/value (deprecated)
additional.fields
packets_sent
about.labels.key/value (deprecated)
additional.fields
hwaddr
about.labels.key/value (deprecated)
additional.fields
state
about.labels.key/value (deprecated)
additional.fields
mtu
about.labels.key/value (deprecated)
additional.fields
managed_policies
The following table lists the log fields and corresponding UDM mappings for the schema managed_policies and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
domain
target.administrative_domain
uuid
about.labels.key/value (deprecated)
additional.fields
name
about.labels.key/value (deprecated)
additional.fields
value
about.labels.key/value (deprecated)
additional.fields
username
target.user.user_display_name
manual
about.labels.key/value (deprecated)
additional.fields
memory_devices
The following table lists the log fields and corresponding UDM mappings for the schema memory_devices and OS Linux, macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
handle
about.labels.key/value (deprecated)
additional.fields
array_handle
about.labels.key/value (deprecated)
additional.fields
form_factor
about.labels.key/value (deprecated)
additional.fields
total_width
about.labels.key/value (deprecated)
additional.fields
data_width
about.labels.key/value (deprecated)
additional.fields
size
about.labels.key/value (deprecated)
additional.fields
set
about.labels.key/value (deprecated)
additional.fields
device_locator
about.labels.key/value (deprecated)
additional.fields
bank_locator
about.labels.key/value (deprecated)
additional.fields
memory_type
about.labels.key/value (deprecated)
additional.fields
memory_type_details
about.labels.key/value (deprecated)
additional.fields
max_speed
about.labels.key/value (deprecated)
additional.fields
configured_clock_speed
about.labels.key/value (deprecated)
additional.fields
manufacturer
target.asset.hardware.manufacturer
serial_number
target.asset.hardware.serial_number
asset_tag
target.asset.asset_id
part_number
about.labels.key/value (deprecated)
additional.fields
min_voltage
about.labels.key/value (deprecated)
additional.fields
max_voltage
about.labels.key/value (deprecated)
additional.fields
configured_voltage
about.labels.key/value (deprecated)
additional.fields
ntdomains
The following table lists the log fields and corresponding UDM mappings for the schema ntdomains and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
about.labels.key/value (deprecated)
additional.fields
client_site_name
about.labels.key/value (deprecated)
additional.fields
dc_site_name
about.labels.key/value (deprecated)
additional.fields
dns_forest_name
network.dns.questions.name
domain_controller_address
target.ip
domain_controller_name
about.labels.key/value (deprecated)
additional.fields
domain_name
target.administrative_domain
status
about.labels.key/value (deprecated)
additional.fields
ntfs_acl_permissions
The following table lists the log fields and corresponding UDM mappings for the schema ntfs_acl_permissions and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
type
about.labels.key/value (deprecated)
additional.fields
principal
about.labels.key/value (deprecated)
additional.fields
access
about.labels.key/value (deprecated)
additional.fields
inherited_from
about.labels.key/value (deprecated)
additional.fields
os_version
The following table lists the log fields and corresponding UDM mappings for the schema os_version and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
about.labels.key/value (deprecated)
additional.fields
version
principal.platform_version
major
about.labels.key/value (deprecated)
additional.fields
minor
about.labels.key/value (deprecated)
additional.fields
patch
principal.platform_patch_level
build
about.labels.key/value (deprecated)
additional.fields
platform
principal.platform
platform_like
about.labels.key/value (deprecated)
additional.fields
codename
about.labels.key/value (deprecated)
additional.fields
arch
about.labels.key/value (deprecated)
additional.fields
install_date
about.labels.key/value (deprecated)
additional.fields
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
mount_namespace_id
about.labels.key/value (deprecated)
additional.fields
osquery_events
The following table lists the log fields and corresponding UDM mappings for the schema osquery_events and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
target.resource.name
publisher
about.label.key/value
type
about.label.key/value
subscriptions
about.label.key/value
events
about.label.key/value
refreshes
about.label.key/value
active
about.label.key/value
patches
The following table lists the log fields and corresponding UDM mappings for the schema patches and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
csname
target.hostname
hotfix_id
about.labels.key/value (deprecated)
additional.fields
caption
about.labels.key/value (deprecated)
additional.fields
description
metadata.description
fix_comments
about.labels.key/value (deprecated)
additional.fields
installed_by
about.labels.key/value (deprecated)
additional.fields
install_date
about.labels.key/value (deprecated)
additional.fields
installed_on
about.labels.key/value (deprecated)
additional.fields
pci_devices
The following table lists the log fields and corresponding UDM mappings for the schema pci_devices and OS Linux, macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
pci_slot
principal.labels.key/value (deprecated)
additional.fields
pci_class
principal.labels.key/value (deprecated)
additional.fields
driver
principal.labels.key/value (deprecated)
additional.fields
vendor
principal.labels.key/value (deprecated)
additional.fields
vendor_id
principal.labels.key/value (deprecated)
additional.fields
model
principal.asset.hardware.model
model_id
principal.labels.key/value (deprecated)
additional.fields
subsystem
principal.labels.key/value (deprecated)
additional.fields
express
principal.labels.key/value (deprecated)
additional.fields
thunderbolt
principal.labels.key/value (deprecated)
additional.fields
removable
principal.labels.key/value (deprecated)
additional.fields
pci_class_id
principal.labels.key/value (deprecated)
additional.fields
pci_subclass_id
principal.labels.key/value (deprecated)
additional.fields
pci_subclass
principal.labels.key/value (deprecated)
additional.fields
subsystem_vendor_id
principal.labels.key/value (deprecated)
additional.fields
subsystem_vendor
principal.labels.key/value (deprecated)
additional.fields
subsystem_model_id
principal.labels.key/value (deprecated)
additional.fields
subsystem_model
principal.labels.key/value (deprecated)
additional.fields
pipes
The following table lists the log fields and corresponding UDM mappings for the schema pipes and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
pid
target.process.pid
name
target.resource.name
instances
about.labels.key/value (deprecated)
additional.fields
max_instances
about.labels.key/value (deprecated)
additional.fields
flags
about.labels.key/value (deprecated)
additional.fields
powershell_events
The following table lists the log fields and corresponding UDM mappings for the schema powershell_events and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
time
metadata.collected_timestamp
datetime
about.labels.key/value (deprecated)
additional.fields
script_block_id
about.labels.key/value (deprecated)
additional.fields
script_block_count
about.labels.key/value (deprecated)
additional.fields
script_text
about.labels.key/value (deprecated)
additional.fields
script_name
about.labels.key/value (deprecated)
additional.fields
script_path
target.file.full_path
cosine_similarity
about.labels.key/value (deprecated)
additional.fields
process_envs
The following table lists the log fields and corresponding UDM mappings for the schema process_envs and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
pid
target.process.pid
key
about.labels.key
value
about.labels.value
process_events
The following table lists the log fields and corresponding UDM mappings for the schema process_events and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
version
target.platform_version
seq_num
about.labels.key/value (deprecated)
additional.fields
global_seq_num
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
path
target.file.full_path
parent
target.process.parent_process.pid
original_parent
about.labels.key/value (deprecated)
additional.fields
cmdline
target.process.command_line
cmdline_count
about.labels.key/value (deprecated)
additional.fields
env
about.labels.key/value (deprecated)
additional.fields
env_count
about.labels.key/value (deprecated)
additional.fields
cwd
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
euid
about.labels.key/value (deprecated)
additional.fields
gid
target.group.product_object_id
egid
about.labels.key/value (deprecated)
additional.fields
username
target.user.user_display_name
signing_id
about.labels.key/value (deprecated)
additional.fields
team_id
about.labels.key/value (deprecated)
additional.fields
cdhash
about.labels.key/value (deprecated)
additional.fields
platform_binary
about.labels.key/value (deprecated)
additional.fields
exit_code
about.labels.key/value (deprecated)
additional.fields
child_pid
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
event_type
about.labels.key/value (deprecated)
additional.fields
eid
about.labels.key/value (deprecated)
additional.fields
process_file_events
The following table lists the log fields and corresponding UDM mappings for the schema process_file_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
operation
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
ppid
target.process.parent_process.pid
time
about.labels.key/value (deprecated)
additional.fields
executable
about.labels.key/value (deprecated)
additional.fields
partial
about.labels.key/value (deprecated)
additional.fields
cwd
about.labels.key/value (deprecated)
additional.fields
path
target.file.full_path
dest_path
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
gid
target.group.product_object_id
auid
about.labels.key/value (deprecated)
additional.fields
euid
about.labels.key/value (deprecated)
additional.fields
egid
about.labels.key/value (deprecated)
additional.fields
fsuid
about.labels.key/value (deprecated)
additional.fields
fsgid
about.labels.key/value (deprecated)
additional.fields
suid
about.labels.key/value (deprecated)
additional.fields
sgid
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
process_open_sockets
The following table lists the log fields and corresponding UDM mappings for the schema process_open_sockets and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
pid
principal.process.pid
fd
about.labels.key/value (deprecated)
additional.fields
socket
about.labels.key/value (deprecated)
additional.fields
family
about.labels.key/value (deprecated)
additional.fields
protocol
about.labels.key/value (deprecated)
additional.fields
local_address
principal.ip
remote_address
target.ip
local_port
principal.port
remote_port
target.port
path
target.file.full_path
state
about.labels.key/value (deprecated)
additional.fields
net_namespace
about.labels.key/value (deprecated)
additional.fields
processes
The following table lists the log fields and corresponding UDM mappings for the schema processes and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
pid
target.process.pid
name
about.labels.key/value (deprecated)
additional.fields
path
target.process.file.full_path
cmdline
target.process.command_line
state
target.process.attribute.labels.key/value
cwd
about.labels.key/value (deprecated)
additional.fields
root
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
gid
target.group.product_object_id
euid
about.labels.key/value (deprecated)
additional.fields
egid
about.labels.key/value (deprecated)
additional.fields
suid
about.labels.key/value (deprecated)
additional.fields
sgid
about.labels.key/value (deprecated)
additional.fields
on_disk
about.labels.key/value (deprecated)
additional.fields
wired_size
about.labels.key/value (deprecated)
additional.fields
resident_size
about.labels.key/value (deprecated)
additional.fields
total_size
about.labels.key/value (deprecated)
additional.fields
user_time
about.labels.key/value (deprecated)
additional.fields
system_time
about.labels.key/value (deprecated)
additional.fields
disk_bytes_read
about.labels.key/value (deprecated)
additional.fields
disk_bytes_written
about.labels.key/value (deprecated)
additional.fields
start_time
about.labels.key/value (deprecated)
additional.fields
parent
target.process.parent_process.pid
pgroup
about.labels.key/value (deprecated)
additional.fields
threads
about.labels.key/value (deprecated)
additional.fields
nice
about.labels.key/value (deprecated)
additional.fields
elevated_token
about.labels.key/value (deprecated)
additional.fields
secure_process
about.labels.key/value (deprecated)
additional.fields
protection_type
about.labels.key/value (deprecated)
additional.fields
virtual_process
about.labels.key/value (deprecated)
additional.fields
elapsed_time
about.labels.key/value (deprecated)
additional.fields
handle_count
about.labels.key/value (deprecated)
additional.fields
percent_processor_time
about.labels.key/value (deprecated)
additional.fields
upid
about.labels.key/value (deprecated)
additional.fields
uppid
about.labels.key/value (deprecated)
additional.fields
cpu_type
about.labels.key/value (deprecated)
additional.fields
cpu_subtype
about.labels.key/value (deprecated)
additional.fields
programs
The following table lists the log fields and corresponding UDM mappings for the schema programs and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
target.resource.name
version
target.platform_version
install_location
about.labels.key/value (deprecated)
additional.fields
install_source
about.labels.key/value (deprecated)
additional.fields
language
about.labels.key/value (deprecated)
additional.fields
publisher
about.labels.key/value (deprecated)
additional.fields
uninstall_string
target.file.full_path
install_date
about.labels.key/value (deprecated)
additional.fields
identifying_number
about.labels.key/value (deprecated)
additional.fields
scheduled_tasks
The following table lists the log fields and corresponding UDM mappings for the schema scheduled_tasks and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
target.resource.name
action
security_result.action_details
path
target.file.full_path
enabled
about.labels.key/value (deprecated)
additional.fields
state
about.labels.key/value (deprecated)
additional.fields
hidden
about.labels.key/value (deprecated)
additional.fields
last_run_time
about.labels.key/value (deprecated)
additional.fields
next_run_time
about.labels.key/value (deprecated)
additional.fields
last_run_message
about.labels.key/value (deprecated)
additional.fields
last_run_code
about.labels.key/value (deprecated)
additional.fields
seccomp_events
The following table lists the log fields and corresponding UDM mappings for the schema seccomp_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
time
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
auid
about.labels.key/value (deprecated)
additional.fields
uid
target.user.userid
gid
target.group.product_object_id
ses
about.labels.key/value (deprecated)
additional.fields
pid
target.process.pid
comm
about.labels.key/value (deprecated)
additional.fields
exe
target.file.full_path
sig
about.labels.key/value (deprecated)
additional.fields
arch
about.labels.key/value (deprecated)
additional.fields
syscall
about.labels.key/value (deprecated)
additional.fields
compat
about.labels.key/value (deprecated)
additional.fields
ip
about.labels.key/value (deprecated)
additional.fields
code
about.labels.key/value (deprecated)
additional.fields
seLinux_events
The following table lists the log fields and corresponding UDM mappings for the schema seLinux_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
type
about.labels.key/value (deprecated)
additional.fields
message
metadata.description
time
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
shadow
The following table lists the log fields and corresponding UDM mappings for the schema shadow and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
password_status
about.labels.key/value (deprecated)
additional.fields
hash_alg
about.labels.key/value (deprecated)
additional.fields
last_change
about.labels.key/value (deprecated)
additional.fields
min
about.labels.key/value (deprecated)
additional.fields
max
about.labels.key/value (deprecated)
additional.fields
warning
about.labels.key/value (deprecated)
additional.fields
inactive
about.labels.key/value (deprecated)
additional.fields
expire
about.labels.key/value (deprecated)
additional.fields
flag
about.labels.key/value (deprecated)
additional.fields
username
principal.user.user_display_name
shell_history
The following table lists the log fields and corresponding UDM mappings for the schema shell_history and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
uid
principal.user.userid
time
about.labels.key/value (deprecated)
additional.fields
command
principal.process.command_line
history_file
principal.process.file.full_path
shimcache
The following table lists the log fields and corresponding UDM mappings for the schema shimcache and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
entry
about.labels.key/value (deprecated)
additional.fields
path
target.file.full_path
modified_time
target.file.last_modification_time
execution_flag
about.labels.key/value (deprecated)
additional.fields
signature
The following table lists the log fields and corresponding UDM mappings for the schema signature and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
hash_resources
about.labels.key/value (deprecated)
additional.fields
arch
about.labels.key/value (deprecated)
additional.fields
signed
target.file.pe_file.signature_info.verified
identifier
target.file.pe_file.signature_info.signer
cdhash
about.labels.key/value (deprecated)
additional.fields
team_identifier
about.labels.key/value (deprecated)
additional.fields
authority
about.labels.key/value (deprecated)
additional.fields
sip_config
The following table lists the log fields and corresponding UDM mappings for the schema sip_config and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
config_flag
about.labels.key/value (deprecated)
additional.fields
enabled
about.labels.key/value (deprecated)
additional.fields
enabled_nvram
about.labels.key/value (deprecated)
additional.fields
socket_events
The following table lists the log fields and corresponding UDM mappings for the schema socket_events and OS Linux, macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
action
security_result.action_details
pid
target.process.pid
path
target.process.file.full_path
fd
about.labels.key/value (deprecated)
additional.fields
auid
target.user.userid
status
about.labels.key/value (deprecated)
additional.fields
family
about.labels.key/value (deprecated)
additional.fields
protocol
about.labels.key/value (deprecated)
additional.fields
local_address
principal.ip
remote_address
target.ip
local_port
principal.port
remote_port
target.port
socket
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
uptime
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
success
about.labels.key/value (deprecated)
additional.fields
sudoers
The following table lists the log fields and corresponding UDM mappings for the schema sudoers and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
source
about.labels.key/value (deprecated)
additional.fields
header
about.labels.key/value (deprecated)
additional.fields
rule_details
about.labels.key/value (deprecated)
additional.fields
syslog_events
The following table lists the log fields and corresponding UDM mappings for the schema syslog_events and OS Linux:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
time
about.labels.key/value (deprecated)
additional.fields
datetime
about.labels.key/value (deprecated)
additional.fields
host
target.hostname
severity
security_result.severity (enum)
facility
about.labels.key/value (deprecated)
additional.fields
tag
about.labels.key/value (deprecated)
additional.fields
message
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
system_info
The following table lists the log fields and corresponding UDM mappings for the schema system_info and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
hostname
principal.administrative_domain
uuid
about.labels.key/value (deprecated)
additional.fields
cpu_type
about.labels.key/value (deprecated)
additional.fields
cpu_subtype
about.labels.key/value (deprecated)
additional.fields
cpu_brand
about.labels.key/value (deprecated)
additional.fields
cpu_physical_cores
about.labels.key/value (deprecated)
additional.fields
cpu_logical_cores
principal.asset.hardware.cpu_number_cores
cpu_microcode
about.labels.key/value (deprecated)
additional.fields
physical_memory
about.labels.key/value (deprecated)
additional.fields
hardware_vendor
about.labels.key/value (deprecated)
additional.fields
hardware_model
principal.asset.hardware.model
hardware_version
about.labels.key/value (deprecated)
additional.fields
hardware_serial
principal.asset.hardware.serial_number
board_vendor
about.labels.key/value (deprecated)
additional.fields
board_model
about.labels.key/value (deprecated)
additional.fields
board_version
about.labels.key/value (deprecated)
additional.fields
board_serial
about.labels.key/value (deprecated)
additional.fields
computer_name
about.labels.key/value (deprecated)
additional.fields
local_hostname
about.labels.key/value (deprecated)
additional.fields
tpm_info
The following table lists the log fields and corresponding UDM mappings for the schema tpm_info and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
activated
about.labels.key/value (deprecated)
additional.fields
enabled
about.labels.key/value (deprecated)
additional.fields
owned
about.labels.key/value (deprecated)
additional.fields
manufacturer_version
about.labels.key/value (deprecated)
additional.fields
manufacturer_id
about.labels.key/value (deprecated)
additional.fields
manufacturer_name
principal.aseet.hardware.manufacturer
product_name
principal.resource.name
physical_presence_version
about.labels.key/value (deprecated)
additional.fields
spec_version
about.labels.key/value (deprecated)
additional.fields
usb_devices
The following table lists the log fields and corresponding UDM mappings for the schema usb_devices and OS Linux, macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
usb_address
about.labels.key/value (deprecated)
additional.fields
usb_port
about.labels.key/value (deprecated)
additional.fields
vendor
about.labels.key/value (deprecated)
additional.fields
vendor_id
about.labels.key/value (deprecated)
additional.fields
version
about.labels.key/value (deprecated)
additional.fields
model
target.asset.hardware.model
model_id
about.labels.key/value (deprecated)
additional.fields
serial
target.asset.hardware.serial_number
class
about.labels.key/value (deprecated)
additional.fields
subclass
about.labels.key/value (deprecated)
additional.fields
protocol
about.labels.key/value (deprecated)
additional.fields
removable
about.labels.key/value (deprecated)
additional.fields
user_events
The following table lists the log fields and corresponding UDM mappings for the schema user_events and OS Linux, macOS, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
uid
principal.user.userid
auid
principal.user.attribute.labels.key/value
pid
target.process.pid
message
metadata.description
type
about.labels.key/value (deprecated)
additional.fields
path
target.file.full_path
address
about.labels.key/value (deprecated)
additional.fields
terminal
about.labels.key/value (deprecated)
additional.fields
time
metadata.collected_timestamp
uptime
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
user_groups
The following table lists the log fields and corresponding UDM mappings for the schema user_groups and OS Linux, macOS, Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
uid
principal.user.userid
gid
principal.group.product_object_id
users
The following table lists the log fields and corresponding UDM mappings for the schema users and OS macOS, Linux, Windows, freebsd:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
uid
principal.user.userid
gid
principal.user.group_identifiers(repeated)
uid_signed
about.labels.key/value (deprecated)
additional.fields
gid_signed
about.labels.key/value (deprecated)
additional.fields
username
principal.user.user_display_name
description
about.labels.key/value (deprecated)
additional.fields
directory
about.labels.key/value (deprecated)
additional.fields
shell
about.labels.key/value (deprecated)
additional.fields
uuid
principal.user.product_object_id
type
about.labels.key/value (deprecated)
additional.fields
is_hidden
about.labels.key/value (deprecated)
additional.fields
pid_with_namespace
about.labels.key/value (deprecated)
additional.fields
wifi_networks
The following table lists the log fields and corresponding UDM mappings for the schema wifi_networks and OS macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
ssid
target.labels.key/value (deprecated)
additional.fields
network_name
target.labels.key/value (deprecated)
additional.fields
security_type
target.labels.key/value (deprecated)
additional.fields
last_connected
about.labels.key/value (deprecated)
additional.fields
passpoint
about.labels.key/value (deprecated)
additional.fields
possibly_hidden
about.labels.key/value (deprecated)
additional.fields
roaming
about.labels.key/value (deprecated)
additional.fields
roaming_profile
about.labels.key/value (deprecated)
additional.fields
captive_portal
about.labels.key/value (deprecated)
additional.fields
auto_login
target.labels.key/value (deprecated)
additional.fields
temporarily_disabled
target.labels.key/value (deprecated)
additional.fields
disabled
target.labels.key/value (deprecated)
additional.fields
windows_crashes
The following table lists the log fields and corresponding UDM mappings for the schema Windows_crashes and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
datetime
about.labels.key/value (deprecated)
additional.fields
module
about.labels.key/value (deprecated)
additional.fields
path
target.process.file.full_path
pid
target.process.pid
tid
about.labels.key/value (deprecated)
additional.fields
version
about.labels.key/value (deprecated)
additional.fields
process_uptime
about.labels.key/value (deprecated)
additional.fields
stack_trace
about.labels.key/value (deprecated)
additional.fields
exception_code
about.labels.key/value (deprecated)
additional.fields
exception_message
about.labels.key/value (deprecated)
additional.fields
exception_address
about.labels.key/value (deprecated)
additional.fields
registers
about.labels.key/value (deprecated)
additional.fields
command_line
target.process.command_line
current_directory
about.labels.key/value (deprecated)
additional.fields
username
target.user.user_display_name
machine_name
about.labels.key/value (deprecated)
additional.fields
major_version
about.labels.key/value (deprecated)
additional.fields
minor_version
about.labels.key/value (deprecated)
additional.fields
build_number
target.platform_version
type
about.labels.key/value (deprecated)
additional.fields
crash_path
about.labels.key/value (deprecated)
additional.fields
windows_eventlog
The Windows Event (WINEVTLOG) parser maps these events. See
Collect Microsoft Windows Event data
for more information."
windows_events
The Windows Event (WINEVTLOG) parser maps these events. See
Collect Microsoft Windows Event data
for more information.
windows_firewall_rules
The following table lists the log fields and corresponding UDM mappings for the schema Windows_firewall_rules and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
about.labels.key/value (deprecated)
additional.fields
app_name
target.application
action
security_result.action (enum)
enabled
about.labels.key/value (deprecated)
additional.fields
grouping
about.labels.key/value (deprecated)
additional.fields
direction
network.direction
protocol
network.ip_protocol
local_addresses
principal.ip
remote_addresses
target.ip
local_ports
principal.port
remote_ports
target.port
icmp_types_codes
about.labels.key/value (deprecated)
additional.fields
profile_domain
about.labels.key/value (deprecated)
additional.fields
profile_private
about.labels.key/value (deprecated)
additional.fields
profile_public
about.labels.key/value (deprecated)
additional.fields
service_name
about.labels.key/value (deprecated)
additional.fields
windows_security_center
The following table lists the log fields and corresponding UDM mappings for the schema Windows_security_center and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
firewall
security_result.detection_fields.key/value
autoupdate
security_result.detection_fields.key/value
antivirus
security_result.detection_fields.key/value
antispyware
security_result.detection_fields.key/value
internet_settings
security_result.detection_fields.key/value
Windows_security_center_service
security_result.detection_fields.key/value
user_account_control
security_result.detection_fields.key/value
windows_security_products
The following table lists the log fields and corresponding UDM mappings for the schema Windows_security_products and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
type
about.labels.key/value (deprecated)
additional.fields
name
target.resource.name
state
about.labels.key/value (deprecated)
additional.fields
state_timestamp
about.labels.key/value (deprecated)
additional.fields
remediation_path
about.labels.key/value (deprecated)
additional.fields
signatures_up_to_date
about.labels.key/value (deprecated)
additional.fields
wmi_bios_info
The following table lists the log fields and corresponding UDM mappings for the schema wmi_bios_info and OS Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
name
about.labels.key/value (deprecated)
additional.fields
value
about.labels.key/value (deprecated)
additional.fields
yara
The following table lists the log fields and corresponding UDM mappings for the schema yara and OS Linux, macOS, freebsd, Windows:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
path
target.file.full_path
matches
about.labels.key/value (deprecated)
additional.fields
count
about.labels.key/value (deprecated)
additional.fields
sig_group
security_result.detection_fields.key/value
sigfile
security_result.detection_fields.key/value
sigrule
security_result.detection_fields.key/value
strings
about.labels.key/value (deprecated)
additional.fields
tags
about.labels.key/value (deprecated)
additional.fields
sigurl
security_result.detection_fields.key/value
yara_events
The following table lists the log fields and corresponding UDM mappings for the schema yara_events and OS Linux, macOS:
Log field
UDM mapping
metadata.event_type is mapped to SETTING_MODIFICATION
target_path
target.file.full_path
category
about.labels.key/value (deprecated)
additional.fields
action
security_result.action_details
transaction_id
security_result.detection_fields.key/value
matches
about.labels.key/value (deprecated)
additional.fields
count
about.labels.key/value (deprecated)
additional.fields
strings
about.labels.key/value (deprecated)
additional.fields
tags
about.labels.key/value (deprecated)
additional.fields
time
about.labels.key/value (deprecated)
additional.fields
eid
metadata.product_log_id
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.
Last updated 2026-03-03 UTC.
