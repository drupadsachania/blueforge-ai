# Format log data as UDM

**Source:** https://docs.cloud.google.com/chronicle/docs/unified-data-model/format-events-as-udm/  
**Scraped:** 2026-03-05T10:03:02.295873Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Format log data as UDM
Supported in:
Google secops
SIEM
Common UDM event fields
All Unified Data Model (
UDM
)
events have a set of common fields and messages that partners can populate
regardless of event type. These fields include the following:
Entities
: Devices, users, and processes involved in an event.
Event metadata
: When the event occurred, the event's type, where it came from, etc.
Network metadata
: High-level network metadata for network-oriented events as well as protocol details within sub-messages:
Email metadata
: Information in the to, from, cc, bcc, and other email fields.
HTTP metadata
: Method, referral_url, useragent, etc.
Security results
: Any classification or action made by a security product.
Additional metadata
: Any important vendor-specific event data that cannot be adequately represented within the formal sections of the UDM model can be added using a free-form json payload field.
The following sections describe how to encode and format events for the UDM.
UDM encoding
UDM events must be submitted to Google Security Operations using one of the following formats:
JSON (
https://developers.google.com/protocol-buffers/docs/proto3#json
)
Proto3
For the purposes of this document, fields are represented using a dot notation.
For example, the following JSON syntax:
{"menu":
  {
    "id": "file",
    "value": "File",
    "popup": {
      "menuitem": [
        {"value": "New", "onclick": "CreateNewDoc()"}
      ]
    }
  }
}
Is documented as follows:
menu.id = "file"
menu.value = "File"
menu.popup.menuitem.value = "New"
menu.popup.menuitem.onclick = "CreateNewDoc()"
Formatting a UDM Event
To format a UDM event to make it ready to send to Google, you must complete the following steps:
Specify the event type
—Your selected event type determines which fields you must also include with the event.
Specify the event timestamp
—Specify the event timestamp.
Specify nouns (entities)
—Each event must include at least one
noun
which describes a participant device or user that is involved in the event.
Specify the security result
—(Optional) Specify security results by including details about security risks and threats that were found by a security system as well as the actions taken to mitigate those risks and threats.
Fill in the remainder of the required and optional event information using the UDM event fields.
Specify the event type
The most important value defined for any event submitted in UDM format is the event type, specified using one of the possible values available for Metadata.event_type. These include values such as PROCESS_OPEN, FILE_CREATION, USER_CREATION, NETWORK_DNS, etc. (for the complete list, see Metadata.event_type. Each event type requires you to also populate a set of other fields and values with the information tied to the original event.
See
Required and Optional Fields for Each UDM Event Type
for detail on which fields to include for each event type.
The following example illustrates how you would specify PROCESS_OPEN as the event type using Proto3 text notation:
metadata {
    event_type: PROCESS_OPEN
}
Specify the event timestamp
You must specify the GMT timestamp for any event submitted in UDM format using Metadata.event_timestamp. The stamp must be encoded using one of the following standards:
For JSON, use RFC 3339
Proto3 timestamp
The following example illustrates how you would specify the timestamp using RFC 3339 format. For this example, yyyy-mm-ddThh:mm:ss+hh:mm—year, month, day, hour, minute, second, and the offset from UTC time. The offset from UTC is minus 8 hours, indicating PST.
metadata {
  event_timestamp: "2019-09-10T20:32:31-08:00"
}
Specify nouns (entities)
For each UDM event, you must define one or more nouns. A noun represents a participant or entity in a UDM event. A noun could be, for example, the device/user that performs the activity described in an event, or the device/user that is the target of such activity described in the event. Nouns can also be things like attachments or URLs. Finally, a noun might also be used to describe a security device that observed the activity described in the event (for example, an email proxy or network router).
A UDM event must have one or more of the following nouns specified:
principal
: Represents the acting entity or the device that originates the activity described in the event. The principal must include at least one machine detail (hostname, MACs, IPs, port, product-specific identifiers like a CrowdStrike machine GUID) or user detail (for example, user name), and optionally include process details. It must NOT include any of the following fields: email, files, registry keys or values.
If all events are taking place on the same machine, that machine only needs to be described in
principal
. The machine does not need to also be described in
target
or in
src
.
The following example illustrates how the
principal
fields could be populated:
principal {
  hostname: "jane_win10"
  asset_id: "Sophos.AV:C070123456-ABCDE"
      ip: "10.0.2.10"
      port: 60671
      user {  userid: "john.smith" }
}
This example provides details about the device and the user who was the principle actor in the event. It includes the device's IP address, port number, and hostname, along with a vendor-specific asset identifier (from Sophos), which is a unique ID generated by the third-party security product.
target:
Represents a target device being referenced by the event, or an object on the target device. For example, in a firewall connection from device A to device B, A is described as the principal and B is described as the target. For a process injection by process C into target process D, process C is described as the principal and process D is described as the target.
Principal versus target in UDM
The following example illustrates how the fields for a target are populated:
target {
   ip: "198.51.100.31"
   port: 80
}
Again, if more information is available, such as hostname, additional IP address(es), MAC address(es), proprietary asset identifiers, etc., they should also be included in
target
.
Both
principal
and
target
(as well as other nouns) can reference actors on the same machine. For example, process A (
principal
) running on machine X acts on process B (
target
) also on machine X.
src:
Represents a source object being acted upon by the participant along with the device or process context for the source object (the machine where the source object resides). For example, if user U copies file A on machine X to file B on machine Y, both file A and machine X would be specified in the
src
portion of the UDM event.
intermediary:
Represents details on one or more intermediate devices processing activity described in the event. This includes device details about a proxy server, SMTP relay server, etc.
observer:
Represents an observer device (for example, a packet sniffer or network-based vulnerability scanner), which is not a direct intermediary, but which observes and reports on the event in question.
about:
Used to store details on all objects referenced by the event that are not otherwise described in
participant
,
src
,
target
,
intermediary
or
observer
. For example, it could be used to track the following:
Email file attachments
Domains/URLs/IPs embedded within an email body
DLLs that are loaded during a PROCESS_LAUNCH event
The entity sections of UDM events include information on the various participants (devices, users, objects like URLs, files, etc.) described in the event. The Google Security Operations UDM has mandatory requirements when it comes to populating Noun fields. These requirements are described in
Required and Optional Fields for Each UDM Event Type
. The set of entity fields that must be filled-in differs based on the event type.
Specify the security result
You can optionally specify security results by populating the SecurityResult fields, including details about security risks and threats that were found by the security system as well as the actions taken to mitigate those risks and threats.
The following are examples of some of the types of security events that would require populating SecurityResult fields:
An email security proxy detected a phishing attempt (MAIL_PHISHING) and blocked (BLOCK) the email.
An email security proxy firewall detected two infected attachments (SOFTWARE_MALICIOUS) and quarantined and disinfected (QUARANTINE, ALLOW_WITH_MODIFICATION) these attachments and then forwarded the disinfected email.
An SSO system facilitated a login (AUTH_VIOLATION) which was blocked (BLOCK).
A malware sandbox detected spyware (SOFTWARE_MALICIOUS) in a file attachment five minutes after the file was delivered (ALLOW) to the user in their inbox.
Need more help?
Get answers from Community members and Google SecOps professionals.
