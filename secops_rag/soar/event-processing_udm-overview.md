# Overview of the Unified Data Model

**Source:** https://docs.cloud.google.com/chronicle/docs/event-processing/udm-overview/  
**Scraped:** 2026-03-05T10:02:49.159123Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Overview of the Unified Data Model
Supported in:
Google secops
SIEM
This document provides an overview of the Unified Data Model (UDM). For more
detail about UDM fields, including a description of each, see the
UDM field
list
. For more information about
parser mapping, see
Important UDM fields for parser
mapping
.
The UDM is a Google Security Operations standard data structure that stores information
about data received from sources. It is also called the
schema
.
Google SecOps stores the original data it receives in two formats, as the
original raw log and as a structured UDM record. The UDM record is a structured
representation of the original log.
If a parser exists for the specified log type, the raw log is used to create a
UDM record. Customers can also transform raw logs to structured UDM format
before sending the data to Google SecOps using the Ingestion API.
Some of the benefits of UDM include:
Stores the same type of record from different vendors using the same
semantics.
Easier to identify relationships between users, hosts, and IP addresses
because the data is normalized into the standard UDM schema.
Easier to write rules since the rules can be platform-independent.
Easier to support log types from new devices.
Although you can search for events with a raw log search, a UDM search works
faster and with more precision because of its specificity. Google SecOps collects raw log data and stores the event log details in the UDM schema. UDM provides a comprehensive framework of thousands of fields for describing and categorizing diverse event types, for example endpoint process events and network communication events.
UDM structure
UDM events are made up of multiple sections. The first section found in every
UDM event is the metadata section. It provides a basic description of the event,
including the timestamp when the event occurred and the timestamp when it was
ingested into Google SecOps. It also includes the product information,
version, and description. The ingestion parser classifies each event based on a
predefined event type, independently of the specific product log. With the
metadata fields alone, you can quickly start searching the data.
In addition to the metadata section, other sections describe additional aspects
of the event. If a section is unnecessary, it isn't included, saving memory.
principal
: Entity which originates the activity in the event.
Sections that reference the source (
src
) and destination
(
target
) are also included.
intermediary
: Systems that events pass through, like a proxy
server or an SMTP relay.
observer
: Systems such as packet sniffers that passively
monitor traffic.
Example UDM searches
This section provides examples of UDM searches that demonstrate some of the
basic syntax, features, and capabilities of UDM search.
Example: search for successful Microsoft Windows 4624 logins
The following search lists the Microsoft Windows 4624 successful login events,
along with when the events were generated, based on just two UDM fields:
metadata.event_type = "USER_LOGIN" AND metadata.product_event_type = "4624"
Example: search for all successful logins
The following search lists all successful login events, regardless of vendor or
application:
metadata.event_type = "USER_LOGIN" AND security_result.action = "ALLOW" AND
target.user.userid != "SYSTEM" AND target.user.userid != /.*$/
Example: search for successful user logins
The following example illustrates how to search for
userid "fkolzig"
and determine when the user with this user ID successfully logged in. You can
complete this search using the target section. The target section includes
subsections and fields describing the target. For example, the target in this
case is a user and has a number of associated attributes, but the target could
also be a file, a registry setting, or an asset. This example searches for
"fkolzig"
using the
target.user.userid
field.
metadata.event_type = "USER_LOGIN" AND metadata.product_event_type = "4624" AND
target.user.userid = "fkolzig"
Example: search your network data
The following example searches network data for RDP events with a
target.port
of
3389
and a
principal.ip
of
35.235.240.5
. 
It also includes a UDM field from the network section, the direction of the data 
(
network.direction
).
metadata.product_event_type = "3" AND target.port = 3389 AND network.direction =
"OUTBOUND" and principal.ip = "35.235.240.5"
Example: search for a specific process
To examine the processes created on your servers, search for instances of the
net.exe
command and search for this specific file in its expected path. The
field you are searching for is
target.process.file.full_path
. For
this search, you include the specific command issued in the
target.process.command_line
field. You can also add a field in the about section which is the description of
Microsoft Sysmon event code 1 (ProcessCreate).
Here is the UDM search:
metadata.product_event_type = "1" AND target.process.file.full_path =
"C:\Windows\System32\net.exe"
Optionally, you could add the following UDM search fields:
principal.user.userid
: Identify the user issuing the command.
principal.process.file.md5
: Identify the MD5 hash.
principal.process.command_line
: Command line.
Example: search for successful user logins associated with a specific department
The following example searches for logins by users (
metadata.event_type
is
USER_LOGIN
) associated with the marketing department (
target.user.department
is
marketing
) of your enterprise. Although
target.user.department
is not directly
connected with user login events, it is still present in the LDAP data ingested
about your users.
metadata.event_type = "USER_LOGIN" AND target.user.department = "Marketing"
Logical objects: Event and Entity
The UDM schema describes all available attributes that store data. Each UDM
record identifies whether it describes an Event or Entity. Data is stored in
different fields depending on whether the record describes an Event versus an
Entity and also which value is set in the
metadata.event_type
or
metadata.entity_type
field.
UDM Event
: Stores data for an action that occurred in the
environment. The original event log describes the action as it was recorded
by the device, such as firewall and web proxy.
UDM Entity
: Contextual representation of elements such as assets,
users, and resources in your environment. It is obtained from a
source of
truth
data source.
Here are two high level visual representations of the Event data model and the
Entity data model.
Figure: Event data model
Figure: Entity data model
Structure of a UDM Event
The UDM Event contains multiple sections that each store a subset of the data
for a single record. The sections are:
metadata
principal
target
src
observer
intermediary
about
network
security_result
extensions
Figure: Event data model
The
metadata
section stores the timestamp, defines the
event_type
, and describes the device.
The
principal
,
target
,
src
,
observer
, and
intermediary
sections store
information about the objects involved in the event. An object could be a
device, user, or process. Most of the time, only a subset of these sections are
used. The fields that store data are determined by the type of event and the
role that each object plays in the event.
The
network
section stores information related to network activity, such as
email and network related communication.
Email data: Information in the
to
,
from
,
cc
,
bcc
, and other email fields.
HTTP data: Such as
method
,
referral_url
, and
useragent
.
The
security_result
section stores an action or classification recorded by a
security product, such as an anti-virus product.
The
about
and
extensions
sections store additional vendor-specific event
information not captured by the other sections. The
extensions
section is a
free-form set of key-value pairs.
Each UDM event stores values from one original raw log event. Depending on the
type of event, certain attributes are required while others are optional. The
required versus optional attributes are determined by the
metadata.event_type
value. The Google SecOps reads
metadata.event_type
and performs field
validation specific to that event type after the logs are received.
If no data is stored in a section of the UDM record, for example the extensions
section, then that section does not appear in the UDM record.
The metadata fields
This section describes fields required in a UDM event.
The event_timestamp field
UDM events must include data for the
metadata.event_timestamp
which
is the GMT timestamp when the event occurred. The value must be encoded using
one of the following standards: RFC 3339 or Proto3 timestamp.
The following examples illustrate how to specify the timestamp using RFC 3339
format,
yyyy-mm-ddThh:mm:ss+hh:mm
(year, month, day, hour, minute,
second, and the offset from UTC time). The offset from UTC is minus 8 hours,
indicating PST.
metadata {
  "event_timestamp": "2019-09-10T20:32:31-08:00"
}

metadata {
  event_timestamp: "2021-02-23T04:00:00.000Z"
}
You can also specify the value using the epoch format.
metadata {
event_timestamp: {
  "seconds": 1588180305
 }
}
The event_type field
The most important field in the UDM event is
metadata.event_type
.
This value identifies the type of action performed and is independent of vendor,
product, or platform. Example values include
PROCESS_OPEN
,
FILE_CREATION
,
USER_CREATION
,
and
NETWORK_DNS
. For the complete list, see the
UDM field
list
document.
The
metadata.event_type
value determines which additional required
and optional fields must be included in the UDM record. For information about
which fields to include for each event type, see
UDM usage
guide
.
The principal, target, src, intermediary, observer, and about attributes
The
principal
,
target
,
src
,
intermediary
, and
observer
attributes describe assets
that are involved in the event. Each store information about objects involved in
the activity, as recorded by the original raw log. This could be the device or
user that performed the activity, the device or user that is the target of the
activity. It might also describe a security device that observed the activity,
such as an email proxy or network router.
The most commonly used attributes are:
principal
: Object that performed the activity.
src
: Object that initiates the activity, if different than
the principal.
target
: Object that is acted upon.
Every event type requires that at least one of these fields contains data.
The auxiliary fields are:
intermediary
: Any object that acted as an intermediary in the
event. This could include objects such as proxy servers and mail servers.
observer
: Any object that does not directly interact with the
traffic in question. This might be a vulnerability scanner or a packet
sniffer device.
about
: Any other objects that played a role in the event and are
optional.
The principal attributes
Represents the acting entity or the device that originated the activity. The
principal must include at least one machine detail (hostname, MAC address, IP
address, product-specific identifiers like a CrowdStrike machine GUID) or user
detail (for example, user name), and optionally include process details. It must
not include any of the following fields: email, files, registry keys or values.
If the event takes place on a single machine, that machine is described in the
principal attribute only. The machine does not need to be described in the
target or src attributes.
The following JSON snippet illustrates how the
principal
attribute
might be populated.
"principal": {
  "hostname": "jane_win10",
  "asset_id" : "Sophos.AV:C070123456-ABCDE",
    "ip" : "10.10.2.10",
    "port" : 60671,
    "user": {  "userid" : "john.smith" }
}
This attribute describes everything known about the device and user that was the
principal actor in the event. This example includes the device's IP address,
port number, and hostname. It also includes a vendor-specific asset identifier,
from Sophos, which is a unique identifier generated by the third-party security
product.
The target attributes
Represents a target device being referenced by the event, or an object on the
target device. For example, in a firewall connection from device A to device B,
device A is captured as the principal and device B is captured as the target.
For a process injection by process C into target process D, process C is the
principal and process D is the target.
Figure: Principal versus target
The following example illustrates how the target field could be populated.
target {
   ip: "192.0.2.31"
   port: 80
}
If more information is available in the original raw log, such as hostname,
additional IP addresses, MAC addresses, and proprietary asset identifiers, it
should also be included in the target and principal fields.
Both principal and target can represent actors on the same machine. For example,
process A (principal) running on machine X could act on process B (target) also
on machine X.
The src attribute
Represents a source object being acted upon by the participant along with the
device or process context for the source object (the machine where the source
object resides). For example, if user U copies file A on machine X to file B on
machine Y, both file A and machine X would be specified in the src portion of
the UDM event.
The intermediary attribute
Represents details about one or more intermediate devices processing activity
described in the event. This could include device details about devices such as
proxy servers and SMTP relay servers.
The observer attribute
Represents an observer device which is not a direct intermediary, but which
observes and reports on the event in question. This could include a packet
sniffer or network-based vulnerability scanner.
The about attribute
This store details about an object referenced by the event which is not
described in the principal, src, target, intermediary or observer fields. For
example, it could capture the following:
Email file attachments.
Domains, URLs, or IP addresses embedded within an email body.
DLLs that are loaded during a PROCESS_LAUNCH event.
The security_result attribute
This section contains information about security risks and threats that are
found by a security system and the actions taken to mitigate those risks and
threats.
Here are types of information that would be stored in the
security_result
attribute:
An email security proxy detected a phishing attempt
(
security_result.category = MAIL_PHISHING
) and blocked
(
security_result.action = BLOCK
) the email.
An email security proxy firewall detected two infected attachments
(
security_result.category = SOFTWARE_MALICIOUS
) and quarantined and
disinfected (
security_result.action = QUARANTINE or security_result.action =
ALLOW_WITH_MODIFICATION
) these attachments and then forwarded the
disinfected email.
An SSO system allows a login (
security_result.category = AUTH_VIOLATION
)
which was blocked (
security_result.action = BLOCK
).
A malware sandbox detected spyware (
security_result.category =
SOFTWARE_MALICIOUS
) in a file attachment five minutes after the file was
delivered (
security_result.action = ALLOW
) to the user in their inbox.
The network attribute
Network attributes store data about network-related events and details about
protocols within sub-messages. This includes activity, such as emails sent and
received, and HTTP requests.
The extensions attribute
Fields under this attribute store additional metadata about the event captured
in the original raw log. It can contain information about vulnerabilities or
additional authentication-related information.
Structure of a UDM Entity
A UDM entity record stores information about any entity within an organization.
If the
metadata.entity_type
is USER, the record stores information about the
user under the
entity.user
attribute. If the
metadata.entity_type
is ASSET, the
record stores information about an asset, such as workstation, laptop, phone,
and virtual machine.
Figure: Event data model
The metadata fields
This section contains fields required in a UDM Entity, such as:
collection_timestamp
: the date & time the record was collected.
entity_type
: the type of entity, such as asset, user, and resource.
The entity attribute
The fields under the entity attribute store information about the specific
entity, such as hostname and IP address if it is an asset, or windows_sid and
email address if it is a user. Notice that the field name is
entity
, but the
field type is a Noun. A Noun is a commonly used data structure that stores
information in both entities and events.
If the
metadata.entity_type
is USER, then data is stored under the
entity.user
attribute.
If the
metadata.entity_type
is ASSET, then data is stored under the
entity.asset
attribute.
The relation attribute
Fields under the relation attribute store information about other entities that
the primary entity is related to. For example, if the primary entity is a User
and the user has been issued a laptop. The laptop is a related entity.
Information about the laptop is stored as an
entity
record with a
metadata.entity_type
= ASSET. Information about the user is stored as an
entity
record with the
metadata.entity_type
= USER.
The user entity record also captures the relationship between the user and the
laptop, using fields under the
relation
attribute. The
relation.relationship
field stores the relationship that the user has to the laptop, specifically that
the user
owns
the laptop. The
relation.entity_type
field stores the value
ASSET, because the laptop is a device.
Fields under the
relations.entity
attribute store information about the laptop,
such as the hostname and MAC address. Notice again that the field name is
entity
and the field type is a Noun. A Noun is a commonly used data structure.
Fields under the
relation.entity
attribute store information about the laptop.
The
relation.direction
field stores the directionality of the relationship
between user and the laptop, specifically whether the relationship is
bidirectional versus unidirectional.
Need more help?
Get answers from Community members and Google SecOps professionals.
