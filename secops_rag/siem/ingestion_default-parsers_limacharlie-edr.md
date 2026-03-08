# Collect LimaCharlie EDR logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/limacharlie-edr/  
**Scraped:** 2026-03-05T09:26:04.883590Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect LimaCharlie EDR logs
Supported in:
Google secops
SIEM
This document explains how to ingest the LimaCharlie EDR logs to
Google Security Operations using Google Cloud Storage. The parser extracts events
from JSON formatted logs, normalizes fields into the UDM, and handles both
top-level and nested events. It specifically parses various event types,
including DNS requests, process creation, file modifications, network
connections, and registry changes, mapping relevant fields to their
Unified Data Model (UDM) equivalents and enriching the data with LimaCharlie
specific context.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Privileged access to Google Cloud
Privileged access to LimaCharlie
Create a Google Cloud Storage Bucket
Sign in to the Google Cloud console.
Go to the
Cloud Storage Buckets
page.
Go to Buckets
Click
Create
.
On the
Create a bucket
page, enter your bucket information. After each of the following steps, click
Continue
to proceed to the next step:
In the
Get started
section, do the following:
Enter a unique name that meets the bucket name requirements (for example,
cloudrun-logs
).
To enable hierarchical namespace, click the expander arrow to expand the
Optimize for file oriented and data-intensive workloads
section, and then select
Enable Hierarchical namespace on this bucket
.
To add a bucket label, click the expander arrow to expand the
Labels
section.
Click
Add label
, and specify a key and a value for your label.
In the
Choose where to store your data
section, do the following:
Select a
Location type
.
Use the location type's menu to select a
Location
where object data within your bucket will be permanently stored.
To set up cross-bucket replication, expand the
Set up cross-bucket replication
section.
In the
Choose a storage class for your data
section, either select a
default storage class
for the bucket, or select
Autoclass
for automatic storage class management of your bucket's data.
In the
Choose how to control access to objects
section, select
not
to enforce
public access prevention
, and select an
access control model
for your bucket's objects.
In the
Choose how to protect object data
section, do the following:
Select any of the options under
Data protection
that you want to set for your bucket.
To choose how your object data will be encrypted, click the
Data encryption
expander arrow, and then select a
Data encryption method
.
Click
Create
.
Configure Log Export in LimaCharlie EDR
Sign in to the
LimaCharlie
portal.
Select
Outputs
from the left menu.
Click
Add Output
.
Choose output stream
: Select
Events
.
Choose output destination
: Select
Google Cloud Storage
.
Provide the following configuration details:
Bucket
: Path to the Google Cloud Storage bucket.
Secret Key
: Secret json key identifying a service account.
Sec per File
: Number of seconds after which a file is cut and uploaded.
Compression
: Set to
False
.
Indexing
: Set to
False
.
Dir
: Directory prefix where to output the files on the remote host.
Click
Save output
.
Set up feeds
To configure a feed, follow these steps:
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
Limacharlie EDR Logs
).
Select
Google Cloud Storage V2
as the
Source type
.
Select
LimaCharlie
as the
Log type
.
Click
Get Service Account
as the
Chronicle Service Account
.
Click
Next
.
Specify values for the following input parameters:
Storage Bucket URI
: Google Cloud Storage bucket URL in
gs://my-bucket/<value>/
format. This URL must end with a trailing forward slash (/).
Source deletion options
: Select deletion option according to your preference.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Supported LimaCharlie Sample Logs
DNS_REQUEST
{
"routing"
:
{
"oid"
:
"406b0c42-af98-4b82-b78f-caecee64e3db"
,
"iid"
:
"811d1c22-d9a2-4b99-b1ac-6f7547998177"
,
"sid"
:
"98e97377-ad12-4fb7-a2e5-b492e18cf17a"
,
"arch"
:
2
,
"plat"
:
268435456
,
"hostname"
:
"masked-hostname.internal.net"
,
"int_ip"
:
"10.10.10.10"
,
"ext_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"event_type"
:
"DNS_REQUEST"
,
"event_time"
:
1584131972237
,
"event_id"
:
"42a5b328-dccb-4972-8b3e-d28c6298da1d"
,
"tags"
:
[
"workstations"
],
"this"
:
"d8856b9e783083c120fff45eadef092e"
},
"event"
:
{
"DOMAIN_NAME"
:
"sanitized.domain.net"
,
"PROCESS_ID"
:
1556
,
"MESSAGE_ID"
:
52513
,
"DNS_TYPE"
:
28
,
"IP_ADDRESS"
:
"2001:db8::1"
}
}
NEW_PROCESS
{
"routing"
:
{
"oid"
:
"406b0c42-af98-4b82-b78f-caecee64e3db"
,
"iid"
:
"811d1c22-d9a2-4b99-b1ac-6f7547998177"
,
"sid"
:
"7812dc27-5b53-475b-9a9c-b86964355986"
,
"arch"
:
2
,
"plat"
:
268435456
,
"hostname"
:
"masked-hostname.internal.net"
,
"int_ip"
:
"10.10.10.10"
,
"ext_ip"
:
"10.10.10.12"
,
"moduleid"
:
2
,
"event_type"
:
"NEW_PROCESS"
,
"event_time"
:
1584121663200
,
"event_id"
:
"519be559-6f48-4c4c-8374-55cf4b80bedc"
,
"tags"
:
[
"workstations"
],
"this"
:
"bfc2100277f0cc05e7f821c6011e5c54"
,
"parent"
:
"500e2ef6f130fc184889800b4d8403e3"
},
"event"
:
{
"PARENT_PROCESS_ID"
:
3452
,
"FILE_PATH"
:
"C:\\Program Files\\Git\\usr\\bin\\bash.exe"
,
"COMMAND_LINE"
:
"\"C:\\Program Files\\Git\\usr\\bin\\bash.exe\""
,
"MEMORY_USAGE"
:
20480
,
"USER_NAME"
:
"CTC\\masked_user"
,
"PROCESS_ID"
:
676
,
"PARENT"
:
{
"PARENT_PROCESS_ID"
:
18900
,
"FILE_PATH"
:
"C:\\Program Files\\Git\\usr\\bin\\bash.exe"
,
"COMMAND_LINE"
:
"\"C:\\Program Files\\Git\\usr\\bin\\bash.exe\""
,
"BASE_ADDRESS"
:
4299161600
,
"PROCESS_ID"
:
3452
,
"THREADS"
:
5
,
"MEMORY_USAGE"
:
9437184
,
"USER_NAME"
:
"CTC\\masked_user"
,
"TIMESTAMP"
:
1584121249676
,
"THIS_ATOM"
:
"500e2ef6f130fc184889800b4d8403e3"
,
"PARENT_ATOM"
:
"699c825429b894129b26dfe488225315"
,
"FILE_IS_SIGNED"
:
0
,
"HASH"
:
"744343e01351ba92e365b7e24eedd4ed18ed3ebe26e68c69d9b5e324fe64a1b5"
},
"FILE_IS_SIGNED"
:
0
,
"HASH"
:
"744343e01351ba92e365b7e24eedd4ed18ed3ebe26e68c69d9b5e324fe64a1b5"
}
}
TERMINATE_PROCESS
{
"routing"
:
{
"oid"
:
"406b0c42-af98-4b82-b78f-caecee64e3db"
,
"iid"
:
"811d1c22-d9a2-4b99-b1ac-6f7547998177"
,
"sid"
:
"7812dc27-5b53-475b-9a9c-b86964355986"
,
"arch"
:
2
,
"plat"
:
268435456
,
"hostname"
:
"masked-hostname.internal.net"
,
"int_ip"
:
"10.10.10.10"
,
"ext_ip"
:
"10.10.10.12"
,
"moduleid"
:
2
,
"event_type"
:
"TERMINATE_PROCESS"
,
"event_time"
:
1584121663547
,
"event_id"
:
"8abfd85b-71b1-4495-bd18-1f4b6f55103b"
,
"tags"
:
[
"workstations"
],
"this"
:
"2932ce40bde71d9b6bf2f648600badec"
,
"parent"
:
"bfc2100277f0cc05e7f821c6011e5c54"
},
"event"
:
{
"PARENT_PROCESS_ID"
:
3452
,
"PROCESS_ID"
:
676
}
}
CODE_IDENTITY
{
"routing"
:
{
"oid"
:
"406b0c42-af98-4b82-b78f-caecee64e3db"
,
"iid"
:
"811d1c22-d9a2-4b99-b1ac-6f7547998177"
,
"sid"
:
"c81a8699-8f37-4f74-a71f-3edf7a7ae80c"
,
"arch"
:
2
,
"plat"
:
268435456
,
"hostname"
:
"masked-hostname.internal.net"
,
"int_ip"
:
"10.10.10.10"
,
"ext_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"event_type"
:
"CODE_IDENTITY"
,
"event_time"
:
1584116496391
,
"event_id"
:
"4810161f-1c87-4069-89e0-1ea84a3f3b63"
,
"tags"
:
[
"workstations"
],
"this"
:
"72198f6f157681b611dc36cde1589b1d"
,
"parent"
:
"c167e778592b4da6cbf705249752d6e6"
},
"event"
:
{
"FILE_PATH"
:
"C:\\Windows\\System32\\psapi.dll"
,
"HASH"
:
"6dae0b5bac5b2c34fd313b51ac793b6f0c270da01474e4d1016b119fc1f9ce8f"
,
"HASH_MD5"
:
"89d92079f45d2f2539bcd1eef73a701e"
,
"HASH_SHA1"
:
"354fbac912764bbf6595f97a59d5e32041926194"
,
"ERROR"
:
0
,
"SIGNATURE"
:
{
"FILE_PATH"
:
"C:\\Windows\\System32\\psapi.dll"
,
"CERT_ISSUER"
:
"C=US, S=Washington, L=Redmond, O=Microsoft Corporation, "
"CN=Microsoft Windows Production PCA 2011"
,
"CERT_SUBJECT"
:
"C=US, S=Washington, L=Redmond, O=Microsoft Corporation, "
"CN=Microsoft Windows"
,
"FILE_IS_SIGNED"
:
1
,
"FILE_CERT_IS_VERIFIED_LOCAL"
:
1
},
"FILE_INFO"
:
"10.0.18362.1"
,
"ORIGINAL_FILE_NAME"
:
"PSAPI"
}
}
EXISTING_PROCESS
{
"source"
:
"129538ba-8970-4421-92dc-5bd958f8308e.05da2702-0aef-43e5-afa1-1bd747dc6161."
"fcdd2eb7-9737-4dac-b639-c11c7a149c71.10000000.2"
,
"routing"
:
{
"oid"
:
"129538ba-8970-4421-92dc-5bd958f8308e"
,
"iid"
:
"05da2702-0aef-43e5-afa1-1bd747dc6161"
,
"sid"
:
"fcdd2eb7-9737-4dac-b639-c11c7a149c71"
,
"arch"
:
2
,
"plat"
:
268435456
,
"hostname"
:
"masked-hostname.internal.net"
,
"int_ip"
:
"10.10.10.10"
,
"ext_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"event_type"
:
"NEW_PROCESS"
,
"event_time"
:
1584039879031
,
"event_id"
:
"f2dd9f86-91fc-4566-8e7d-3235407ebc88"
,
"tags"
:
[],
"this"
:
"c8b9305d9358fea725096f354779ddec"
,
"parent"
:
"1deb4f32a9fc7d4d51e155a5c748ca74"
},
"cat"
:
"Whoami Execution"
,
"namespace"
:
"general"
,
"detect"
:
{
"routing"
:
{
"oid"
:
"129538ba-8970-4421-92dc-5bd958f8308e"
,
"iid"
:
"05da2702-0aef-43e5-afa1-1bd747dc6161"
,
"sid"
:
"fcdd2eb7-9737-4dac-b639-c11c7a149c71"
,
"arch"
:
2
,
"plat"
:
268435456
,
"hostname"
:
"masked-hostname.internal.net"
,
"int_ip"
:
"10.10.10.10"
,
"ext_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"event_type"
:
"NEW_PROCESS"
,
"event_time"
:
1584039879031
,
"event_id"
:
"f2dd9f86-91fc-4566-8e7d-3235407ebc88"
,
"tags"
:
[],
"this"
:
"c8b9305d9358fea725096f354779ddec"
,
"parent"
:
"1deb4f32a9fc7d4d51e155a5c748ca74"
},
"event"
:
{
"PARENT_PROCESS_ID"
:
8396
,
"FILE_PATH"
:
"C:\\Windows\\system32\\whoami.exe"
,
"COMMAND_LINE"
:
"whoami.exe"
,
"PROCESS_ID"
:
4456
,
"PARENT"
:
{
"PARENT_PROCESS_ID"
:
5072
,
"FILE_PATH"
:
"C:\\Windows\\system32\\cmd.exe"
,
"COMMAND_LINE"
:
"\"C:\\Windows\\system32\\cmd.exe\" "
,
"BASE_ADDRESS"
:
140699014070272
,
"PROCESS_ID"
:
8396
,
"THREADS"
:
3
,
"MEMORY_USAGE"
:
3645440
,
"USER_NAME"
:
"masked-hostname.internal.net\\masked_user"
,
"TIMESTAMP"
:
1584039874151
,
"THIS_ATOM"
:
"1deb4f32a9fc7d4d51e155a5c748ca74"
,
"PARENT_ATOM"
:
"f6abd6b90dd752db2d2670a35f261ecb"
,
"FILE_IS_SIGNED"
:
1
,
"HASH"
:
"ff79d3c4a0b7eb191783c323ab8363ebd1fd10be58d8bcc96b07067743ca81d5"
},
"FILE_IS_SIGNED"
:
1
,
"HASH"
:
"a8a4c4719113b071bb50d67f6e12c188b92c70eeafdfcd6f5da69b6aaa99a7fd"
}
},
"detect_id"
:
"996b32e7-9e92-4adb-9503-a53f1d52090a"
,
"detect_mtd"
:
{
"level"
:
"high"
,
"references"
:
[
"https://sanitized.domain.net/alerts/alert/public/1247926/"
"agent-tesla-keylogger-delivered-inside-a-power-iso-daa-archive/"
,
"https://sanitized.domain.net/tasks/7eaba74e-c1ea-400f-9c17-5e30eee89906/"
],
"description"
:
"Detects the execution of whoami, which is often used by attackers after "
"exloitation / privilege escalation but rarely used by administrators"
,
"tags"
:
[
"attack.discovery"
,
"attack.t1033"
,
"car.2016-03-001"
],
"author"
:
"Florian Roth"
},
"ts"
:
1584451579789
}
SERVICE_CHANGE
{
"event"
:
{
"DLL"
:
"%systemroot%\\system32\\wuaueng.dll"
,
"EXECUTABLE"
:
"%systemroot%\\system32\\svchost.exe -k netsvcs"
,
"FILE_IS_SIGNED"
:
1
,
"HASH"
:
"bce4a05d601d358f06f4d8f996aaa1923a8ee9d37262cc9b20b143be070c4641"
,
"PROCESS_ID"
:
836
,
"SVC_DISPLAY_NAME"
:
"Windows Update"
,
"SVC_NAME"
:
"wuauserv"
,
"SVC_STATE"
:
4
,
"SVC_TYPE"
:
32
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"baec41a4-0849-46c6-a78a-86fd3c61348f"
,
"event_time"
:
1584131972237
,
"event_type"
:
"SERVICE_CHANGE"
,
"ext_ip"
:
"10.10.10.12"
,
"hostname"
:
"masked-hostname.internal.net"
,
"iid"
:
"82fa9eb7-8f1c-474d-b68b-61825f4773d2"
,
"int_ip"
:
"10.10.10.13"
,
"moduleid"
:
2
,
"oid"
:
"3fb2aff0-a135-49f3-8231-b773a773da43"
,
"plat"
:
268435456
,
"sid"
:
"72a4fc32-46a3-4e34-9e07-3295aa59b3b6"
,
"tags"
:
[
"server"
],
"this"
:
"c624bb9dfb0dd39214de202d615a3027"
}
}
NETWORK_CONNECTIONS
{
"event"
:
{
"COMMAND_LINE"
:
"C:\\windows\\system32\\svchost.exe -k NetworkService -p -s Dnscache"
,
"FILE_IS_SIGNED"
:
1
,
"FILE_PATH"
:
"C:\\windows\\system32\\svchost.exe"
,
"HASH"
:
"643ec58e82e0272c97c2a59f6020970d881af19c0ad5029db9c958c13b6558c7"
,
"NETWORK_ACTIVITY"
:
[
{
"DESTINATION"
:
{
"IP_ADDRESS"
:
"2001:db8::10"
,
"PORT"
:
53
},
"IS_OUTGOING"
:
1
,
"PROTOCOL"
:
"udp6"
,
"SOURCE"
:
{
"IP_ADDRESS"
:
"2001:db8::20"
,
"PORT"
:
49285
},
"TIMESTAMP"
:
1633325249854
},
{
"DESTINATION"
:
{
"IP_ADDRESS"
:
"10.10.10.14"
,
"PORT"
:
53
},
"IS_OUTGOING"
:
1
,
"PROTOCOL"
:
"udp4"
,
"SOURCE"
:
{
"IP_ADDRESS"
:
"10.10.10.15"
,
"PORT"
:
50364
},
"TIMESTAMP"
:
1633325249898
}
],
"PARENT_PROCESS_ID"
:
1356
,
"PROCESS_ID"
:
2544
,
"USER_NAME"
:
"NT AUTHORITY\\NETWORK SERVICE"
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"c0556a7a-9580-4ed4-a75a-25ab4fa33302"
,
"event_time"
:
1584131972237
,
"event_type"
:
"NETWORK_CONNECTIONS"
,
"ext_ip"
:
"10.10.10.16"
,
"hostname"
:
"masked-hostname.internal.net"
,
"iid"
:
"6c989fbd-c296-4881-a0a2-b9f165f0ab1a"
,
"int_ip"
:
"10.10.10.15"
,
"moduleid"
:
2
,
"oid"
:
"bb479180-e2dc-422b-a54b-f48a572fcb32"
,
"parent"
:
"a48b0fd4e065922eaa452a2661588411"
,
"plat"
:
268435456
,
"sid"
:
"437a4196-9fb8-440b-9c90-cb49bee78d8c"
,
"tags"
:
[
"windows-end-users"
],
"this"
:
"b4659600ca9f18d5be4eaee6615a90e1"
}
}
CLOUD_NOTIFICATION
{
"event"
:
{
"EXPIRY"
:
1633293567
,
"HCP_IDENT"
:
{
"HCP_ARCHITECTURE"
:
2
,
"HCP_INSTALLER_ID"
:
"907e4bc5e4224a20a0b47618017ed09c"
,
"HCP_ORG_ID"
:
"1367c836c1ed4d4cadeb47bd2bbaf962"
,
"HCP_PLATFORM"
:
536870912
,
"HCP_SENSOR_ID"
:
"fcc8cd7d93a24afab58c9658350d6f66"
},
"NOTIFICATION"
:
{
"DOMAIN_NAME"
:
"sanitized.domain.net"
},
"NOTIFICATION_ID"
:
"DNS_RESOLVE_REQ"
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"e37fe0cf-7c09-424e-acc1-d821225cf2e0"
,
"event_time"
:
1584131972237
,
"event_type"
:
"CLOUD_NOTIFICATION"
,
"ext_ip"
:
"10.10.10.17"
,
"hostname"
:
"masked-hostname.internal.net"
,
"iid"
:
"907e4bc5-e422-4a20-a0b4-7618017ed09c"
,
"int_ip"
:
"10.10.10.18"
,
"moduleid"
:
2
,
"oid"
:
"1367c836-c1ed-4d4c-adeb-47bd2bbaf962"
,
"plat"
:
536870912
,
"sid"
:
"fcc8cd7d-93a2-4afa-b58c-9658350d6f66"
,
"tags"
:
[
"cloudlinuxworkloads"
]
}
}
RECEIPT
{
"event"
:
{
"ERROR"
:
0
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"832008f0-75af-401f-97de-b9a4d96e6e0c"
,
"event_time"
:
1584131972237
,
"event_type"
:
"RECEIPT"
,
"ext_ip"
:
"10.10.10.17"
,
"hostname"
:
"masked-hostname.internal.net"
,
"iid"
:
"907e4bc5-e422-4a20-a0b4-7618017ed09c"
,
"int_ip"
:
"10.10.10.18"
,
"moduleid"
:
2
,
"oid"
:
"1367c836-c1ed-4d4c-adeb-47bd2bbaf962"
,
"plat"
:
536870912
,
"sid"
:
"fcc8cd7d-93a2-4afa-b58c-9658350d6f66"
,
"tags"
:
[
"cloudlinuxworkloads"
]
}
}
MODULE_LOAD
{
"event"
:
{
"BASE_ADDRESS"
:
140710068617216
,
"FILE_IS_SIGNED"
:
1
,
"FILE_PATH"
:
"C:\\Windows\\System32\\cryptbase.dll"
,
"HASH"
:
"b50d007ee8764f7cada9d9a395da396201c8b18e6501b50ab809914a7588baf1"
,
"MEMORY_SIZE"
:
49152
,
"MODULE_NAME"
:
"cryptbase.dll"
,
"PROCESS_ID"
:
1736
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"1bd26937-ac7f-4f61-bab6-f83f796d2ecd"
,
"event_time"
:
1584131972237
,
"event_type"
:
"MODULE_LOAD"
,
"ext_ip"
:
"10.10.10.19"
,
"hostname"
:
"masked-hostname.internal.net"
,
"iid"
:
"efc77307-2d8a-4db5-a10f-f45fab19d1f3"
,
"int_ip"
:
"10.10.10.20"
,
"moduleid"
:
2
,
"oid"
:
"8cbe27f4-bfa1-4afb-ba19-138cd51389cd"
,
"parent"
:
"3da6ecb6ef74802bda4da2fa6159c7b3"
,
"plat"
:
268435456
,
"sid"
:
"41459c8d-977c-40cb-aa84-a5d2413a72e1"
,
"tags"
:
[
"proj-simulated-data"
],
"this"
:
"9804e2ec76caa07d743631ee6159c7b5"
}
}
FILE_READ
{
"event"
:
{
"FILE_PATH"
:
"C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Microsoft\\"
"Windows\\PowerShell\\ModuleAnalysisCache"
,
"PROCESS_ID"
:
4020
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"f4a6a55a-6035-4bdc-8fca-d63cd39b9b7c"
,
"event_time"
:
1584131972237
,
"event_type"
:
"FILE_READ"
,
"ext_ip"
:
"10.10.10.19"
,
"hostname"
:
"DESKTOP-masked-hostname.internal.net"
,
"iid"
:
"efc77307-2d8a-4db5-a10f-f45fab19d1f3"
,
"int_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"oid"
:
"8cbe27f4-bfa1-4afb-ba19-138cd51389cd"
,
"parent"
:
"2d1eff5f675337956bb09e206159c792"
,
"plat"
:
268435456
,
"sid"
:
"41459c8d-977c-40cb-aa84-a5d2413a72e1"
,
"tags"
:
[
"proj-simulated-data"
],
"this"
:
"43018962d7e64857797adbd56159c7b3"
}
}
NEW_NAMED_PIPE
{
"event"
:
{
"FILE_PATH"
:
"\\Device\\NamedPipe\\masked.pipe.name"
,
"PROCESS_ID"
:
1736
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"c2381353-bddf-4ba2-92bf-15b1c4cd06d1"
,
"event_time"
:
1584131972237
,
"event_type"
:
"NEW_NAMED_PIPE"
,
"ext_ip"
:
"10.10.10.19"
,
"hostname"
:
"DESKTOP-masked-hostname.internal.net"
,
"iid"
:
"efc77307-2d8a-4db5-a10f-f45fab19d1f3"
,
"int_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"oid"
:
"8cbe27f4-bfa1-4afb-ba19-138cd51389cd"
,
"parent"
:
"3da6ecb6ef74802bda4da2fa6159c7b3"
,
"plat"
:
268435456
,
"sid"
:
"41459c8d-977c-40cb-aa84-a5d2413a72e1"
,
"tags"
:
[
"proj-simulated-data"
],
"this"
:
"75c28d52c8cb8bd841d1b8ad6159c7b4"
}
}
REGISTRY_WRITE
{
"event"
:
{
"PROCESS_ID"
:
1736
,
"REGISTRY_KEY"
:
"\\REGISTRY\\USER\\.DEFAULT\\Software\\Microsoft\\Windows\\"
"CurrentVersion\\Internet Settings\\ZoneMap\\ProxyBypass"
,
"REGISTRY_VALUE"
:
"AQAAAA=="
,
"SIZE"
:
4
,
"TYPE"
:
4
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"3fbd9a14-4605-4447-a8e4-ab6c0cda6852"
,
"event_time"
:
1584131972237
,
"event_type"
:
"REGISTRY_WRITE"
,
"ext_ip"
:
"10.10.10.19"
,
"hostname"
:
"DESKTOP-masked-hostname.internal.net"
,
"iid"
:
"efc77307-2d8a-4db5-a10f-f45fab19d1f3"
,
"int_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"oid"
:
"8cbe27f4-bfa1-4afb-ba19-138cd51389cd"
,
"parent"
:
"3da6ecb6ef74802bda4da2fa6159c7b3"
,
"plat"
:
268435456
,
"sid"
:
"41459c8d-977c-40cb-aa84-a5d2413a72e1"
,
"tags"
:
[
"proj-simulated-data"
],
"this"
:
"dd0f92df3b5e26a6be12cd186159c7b4"
}
}
THREAD_INJECTION
{
"event"
:
{
"EVENTS"
:
[
{
"event"
:
{
"ACCESS_FLAGS"
:
2097151
,
"PARENT_PROCESS_ID"
:
3136
,
"PROCESS_ID"
:
2644
,
"SOURCE"
:
{
"COMMAND_LINE"
:
"\"C:\\Windows\\system32\\HOSTNAME.EXE\""
,
"FILE_IS_SIGNED"
:
1
,
"FILE_PATH"
:
"C:\\Windows\\system32\\HOSTNAME.EXE"
,
"HASH"
:
"a90c3fb350a11c6f6a6efa9607987d924d1de65e09ca9faf2e0e0e00531ee335"
,
"MEMORY_USAGE"
:
32768
,
"PARENT_ATOM"
:
"eab4177ebe39abb8c934b15c6159bd9e"
,
"PARENT_PROCESS_ID"
:
3728
,
"PROCESS_ID"
:
3136
,
"THIS_ATOM"
:
"a20ec63b1d44ef8111c596666159bdc2"
,
"TIMESTAMP"
:
1633271233872
,
"USER_NAME"
:
"BUILTIN\\Administrators"
},
"TARGET"
:
{
"BASE_ADDRESS"
:
140702461788160
,
"COMMAND_LINE"
:
"C:\\Windows\\system32\\disksnapshot.exe -z"
,
"FILE_IS_SIGNED"
:
1
,
"FILE_PATH"
:
"C:\\Windows\\system32\\disksnapshot.exe"
,
"HASH"
:
"f9a712caed73ec1392224aa13f48b154832151488e53410f1130cdf81aacf2ae"
,
"MEMORY_USAGE"
:
1273856
,
"PARENT_ATOM"
:
"2de44917d7d1e657951b6b5d614dff96"
,
"PARENT_PROCESS_ID"
:
380
,
"PROCESS_ID"
:
2644
,
"THIS_ATOM"
:
"0131cb216eb106953b0ee220615e9f7e"
,
"THREADS"
:
1
,
"TIMESTAMP"
:
1633591166179
,
"USER_NAME"
:
"NT AUTHORITY\\SYSTEM"
}
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"82aac6d1-0bf5-43b4-911a-13e18a5044ab"
,
"event_time"
:
1584131972237
,
"event_type"
:
"REMOTE_PROCESS_HANDLE"
,
"ext_ip"
:
"10.10.10.19"
,
"hostname"
:
"DESKTOP-masked-hostname.internal.net"
,
"iid"
:
"efc77307-2d8a-4db5-a10f-f45fab19d1f3"
,
"int_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"oid"
:
"8cbe27f4-bfa1-4afb-ba19-138cd51389cd"
,
"parent"
:
"a20ec63b1d44ef8111c596666159bdc2"
,
"plat"
:
268435456
,
"sid"
:
"41459c8d-977c-40cb-aa84-a5d2413a72e1"
,
"tags"
:
[
"proj-simulated-data"
],
"target"
:
"0131cb216eb106953b0ee220615e9f7e"
,
"this"
:
"2b96934869a59d19ced528436159d3fa"
}
}
]
},
"routing"
:
{
"arch"
:
2
,
"did"
:
""
,
"event_id"
:
"3349f656-ebd3-4ecf-b510-91d698af11b8"
,
"event_time"
:
1584131972237
,
"event_type"
:
"THREAD_INJECTION"
,
"ext_ip"
:
"10.10.10.19"
,
"hostname"
:
"DESKTOP-masked-hostname.internal.net"
,
"iid"
:
"efc77307-2d8a-4db5-a10f-f45fab19d1f3"
,
"int_ip"
:
"10.10.10.11"
,
"moduleid"
:
2
,
"oid"
:
"8cbe27f4-bfa1-4afb-ba19-138cd51389cd"
,
"parent"
:
"a20ec63b1d44ef8111c596666159bdc2"
,
"plat"
:
268435456
,
"sid"
:
"41459c8d-977c-40cb-aa84-a5d2413a72e1"
,
"tags"
:
[
"proj-simulated-data"
],
"target"
:
"0131cb216eb106953b0ee220615e9f7e"
,
"this"
:
"ff59af10d5ef682d206adfeb6159d3fa"
}
}
UDM mapping table
Log Field
UDM Mapping
Logic
cat
security_result.summary
Renamed from
cat
.  Applies when
detect
is not empty.
detect.event.COMMAND_LINE
principal.process.command_line
Renamed from
detect.event.COMMAND_LINE
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.COMMAND_LINE
principal.process.command_line
Renamed from
detect.event.COMMAND_LINE
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.FILE_PATH
principal.process.file.full_path
Renamed from
detect.event.FILE_PATH
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.FILE_PATH
principal.process.file.full_path
Renamed from
detect.event.FILE_PATH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.HASH
principal.process.file.sha256
Renamed from
detect.event.HASH
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.HASH
principal.process.file.sha256
Renamed from
detect.event.HASH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.HASH_MD5
principal.process.file.md5
Renamed from
detect.event.HASH_MD5
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.HASH_SHA1
principal.process.file.sha1
Renamed from
detect.event.HASH_SHA1
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT.COMMAND_LINE
principal.process.command_line
Renamed from
detect.event.PARENT.COMMAND_LINE
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT.COMMAND_LINE
principal.process.parent_process.command_line
Renamed from
detect.event.PARENT.COMMAND_LINE
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT.FILE_PATH
principal.process.file.full_path
Renamed from
detect.event.PARENT.FILE_PATH
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT.FILE_PATH
principal.process.parent_process.file.full_path
Renamed from
detect.event.PARENT.FILE_PATH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT.HASH
principal.process.file.sha256
Renamed from
detect.event.PARENT.HASH
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT.HASH
principal.process.parent_process.file.sha256
Renamed from
detect.event.PARENT.HASH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT_PROCESS_ID
principal.process.pid
Renamed from
detect.event.PARENT_PROCESS_ID
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PARENT_PROCESS_ID
principal.process.parent_process.pid
Renamed from
detect.event.PARENT_PROCESS_ID
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PROCESS_ID
target.process.pid
Renamed from
detect.event.PROCESS_ID
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.PROCESS_ID
principal.process.pid
Renamed from
detect.event.PROCESS_ID
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect.event.USER_NAME
principal.user.userid
Renamed from
detect.event.USER_NAME
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is not empty.
detect_mtd.description
security_result.description
Renamed from
detect_mtd.description
. Applies when
detect
is not empty.
detect_mtd.level
security_result.severity
Copied from
detect_mtd.level
and converted to uppercase. Applies when
detect
is not empty.
event.COMMAND_LINE
principal.process.command_line
Renamed from
event.COMMAND_LINE
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.COMMAND_LINE
principal.process.command_line
Renamed from
event.COMMAND_LINE
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.DLL
target.file.full_path
Copied from
event.DLL
. Applies when
event_type
is
SERVICE_CHANGE
.
event.DOMAIN_NAME
network.dns.questions.0.name
,
network.dns.answers.0.name
Renamed to
a.name
, then copied to
q.name
, then merged into
network.dns.questions
and
network.dns.answers
arrays. Applies when
event_type
is
DNS_REQUEST
.
event.DNS_TYPE
network.dns.answers.0.type
Renamed to
a.type
, then merged into
network.dns.answers
array. Applies when
event_type
is
DNS_REQUEST
.
event.ERROR
security_result.severity_details
Copied from
event.ERROR
. Applies when
event.ERROR
is not empty.
event.EXECUTABLE
target.process.command_line
Copied from
event.EXECUTABLE
. Applies when
event_type
is
SERVICE_CHANGE
.
event.FILE_PATH
target.file.full_path
Renamed from
event.FILE_PATH
. Applies when
event_type
is one of
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
, or
FILE_READ
and
detect
is empty.
event.FILE_PATH
principal.process.file.full_path
Renamed from
event.FILE_PATH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.FILE_PATH
target.process.file.full_path
Renamed from
event.FILE_PATH
. Applies when
event_type
is one of
NEW_PROCESS
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.HASH
target.file.sha256
Renamed from
event.HASH
. Applies when
event_type
is one of
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
, or
FILE_READ
and
detect
is empty.
event.HASH
principal.process.file.sha256
Renamed from
event.HASH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.HASH
target.process.file.sha256
Renamed from
event.HASH
. Applies when
event_type
is one of
NEW_PROCESS
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.HASH_MD5
principal.process.file.md5
Renamed from
event.HASH_MD5
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.HASH_SHA1
principal.process.file.sha1
Renamed from
event.HASH_SHA1
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.IP_ADDRESS
network.dns.answers.0.data
Renamed to
a.data
, then merged into
network.dns.answers
array. Applies when
event_type
is
DNS_REQUEST
and
event.IP_ADDRESS
is not empty.
event.MESSAGE_ID
network.dns.id
Renamed from
event.MESSAGE_ID
. Applies when
event_type
is
DNS_REQUEST
.
event.NETWORK_ACTIVITY[].DESTINATION.IP_ADDRESS
target.ip
Merged from
event.NETWORK_ACTIVITY[].DESTINATION.IP_ADDRESS
. Applies when
event_type
is
NETWORK_CONNECTIONS
.
event.NETWORK_ACTIVITY[].SOURCE.IP_ADDRESS
principal.ip
Merged from
event.NETWORK_ACTIVITY[].SOURCE.IP_ADDRESS
. Applies when
event_type
is
NETWORK_CONNECTIONS
.
event.PARENT.COMMAND_LINE
principal.process.command_line
Renamed from
event.PARENT.COMMAND_LINE
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT.COMMAND_LINE
principal.process.parent_process.command_line
Renamed from
event.PARENT.COMMAND_LINE
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT.FILE_PATH
principal.process.file.full_path
Renamed from
event.PARENT.FILE_PATH
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT.FILE_PATH
principal.process.parent_process.file.full_path
Renamed from
event.PARENT.FILE_PATH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT.HASH
principal.process.file.sha256
Renamed from
event.PARENT.HASH
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT.HASH
principal.process.parent_process.file.sha256
Renamed from
event.PARENT.HASH
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT_PROCESS_ID
principal.process.pid
Renamed from
event.PARENT_PROCESS_ID
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PARENT_PROCESS_ID
principal.process.parent_process.pid
Renamed from
event.PARENT_PROCESS_ID
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PROCESS_ID
target.process.pid
Renamed from
event.PROCESS_ID
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.PROCESS_ID
principal.process.pid
Renamed from
event.PROCESS_ID
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
event.REGISTRY_KEY
target.registry.registry_key
Copied from
event.REGISTRY_KEY
. Applies when
event_type
is
REGISTRY_WRITE
.
event.REGISTRY_VALUE
target.registry.registry_value_data
Copied from
event.REGISTRY_VALUE
. Applies when
event_type
is
REGISTRY_WRITE
.
event.SVC_DISPLAY_NAME
metadata.description
Copied from
event.SVC_DISPLAY_NAME
. Applies when
event_type
is
SERVICE_CHANGE
.
event.SVC_NAME
target.application
Copied from
event.SVC_NAME
. Applies when
event_type
is
SERVICE_CHANGE
.
event.USER_NAME
principal.user.userid
Renamed from
event.USER_NAME
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
routing.event_time
metadata.event_timestamp
Parsed as a timestamp from
routing.event_time
using either UNIX_MS or ISO8601 format.
routing.event_type
metadata.product_event_type
Copied from
routing.event_type
.
routing.ext_ip
principal.ip
Copied from
routing.ext_ip
. Applies when
routing.ext_ip
is not empty.
routing.hostname
principal.hostname
Copied from
routing.hostname
. Applies when
routing.hostname
is not empty.
routing.int_ip
principal.ip
Copied from
routing.int_ip
. Applies when
routing.int_ip
is not empty.
routing.parent
target.process.product_specific_process_id
Prepended with "LC:" from
routing.parent
. Applies when
detect
is not empty.
routing.parent
principal.process.product_specific_process_id
Prepended with "LC:" from
routing.parent
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
routing.this
is empty and
routing.parent
is not empty.
routing.this
principal.process.product_specific_process_id
Prepended with "LC:" from
routing.this
. Applies when
event_type
is one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
detect
is empty.
routing.this
principal.process.product_specific_process_id
Prepended with "LC:" from
routing.this
. Applies when
event_type
is not one of
NEW_PROCESS
,
NEW_DOCUMENT
,
FILE_MODIFIED
,
FILE_DELETE
,
FILE_CREATE
,
FILE_READ
,
MODULE_LOAD
,
TERMINATE_PROCESS
, or
SENSITIVE_PROCESS_ACCESS
and
routing.this
is not empty. Set to
true
when
detect
is not empty. Set to
true
when
detect
is not empty and
detect_mtd.level
is one of
high
,
medium
, or
critical
. Set to a value based on
event_type
:
NETWORK_DNS
for
DNS_REQUEST
,
PROCESS_LAUNCH
for
NEW_PROCESS
,
PROCESS_UNCATEGORIZED
for
EXISTING_PROCESS
,
NETWORK_CONNECTION
for
CONNECTED
or
NETWORK_CONNECTIONS
,
REGISTRY_MODIFICATION
for
REGISTRY_WRITE
,
SERVICE_MODIFICATION
for
SERVICE_CHANGE
,
FILE_UNCATEGORIZED
for
NEW_DOCUMENT
,
FILE_READ
for
FILE_READ
,
FILE_DELETION
for
FILE_DELETE
,
FILE_CREATION
for
FILE_CREATE
,
FILE_MODIFICATION
for
FILE_MODIFIED
,
PROCESS_MODULE_LOAD
for
MODULE_LOAD
,
PROCESS_TERMINATION
for
TERMINATE_PROCESS
,
STATUS_UNCATEGORIZED
for
CLOUD_NOTIFICATION
or
RECEIPT
,
PROCESS_UNCATEGORIZED
for
REMOTE_PROCESS_HANDLE
or
NEW_REMOTE_THREAD
, or
GENERIC_EVENT
otherwise. Set to "LimaCharlie EDR". Set to "LimaCharlie". Set to "DNS" when
event_type
is
DNS_REQUEST
. Set to "ERROR" when
event.ERROR
is not empty. Copied from
event.HOST_NAME
. Applies when
event_type
is
CONNECTED
.
Need more help?
Get answers from Community members and Google SecOps professionals.
