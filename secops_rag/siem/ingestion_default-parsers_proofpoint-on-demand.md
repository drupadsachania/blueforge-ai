# Collect Proofpoint On-Demand logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/proofpoint-on-demand/  
**Scraped:** 2026-03-05T09:27:29.534389Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Proofpoint On-Demand logs
Supported in:
Google secops
SIEM
This document explains how to ingest Proofpoint On-Demand logs to
Google Security Operations using built-in API integration. The parser extracts
fields from JSON logs, transforming them into the Chronicle UDM format.
It handles two primary log formats: one containing email metadata and the other
containing SMTP transaction details, using conditional logic to parse fields
appropriately and populate the Unified Data Model (UDM) fields based on the
available data. The parser also performs data cleaning, such as removing
extraneous characters and converting timestamps.
Before you begin
Make sure you have the following prerequisites:
Google SecOps instance
Proofpoint On-Demand Remote Syslog
license
Privileged access to Proofpoint
Configure Proofpoint On-Demand API access
Sign in to the
Proofpoint Admin
portal.
Copy your
Cluster ID
(displayed on the upper-right corner of your
management interface, next to the release number).
Go to
Settings
>
API Key Management
.
Click
Create New
to open the
Create New API Key
dialog.
Enter a unique
Name
(for example,
Google SecOps Key
).
Generate the
API Key
.
Select
View Details
from the ellipsis menu on the new API Key.
Copy the
API Key
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
Click the
Proofpoint
feed pack.
Select the
Proofpoint On-Demand
log type.
Click
Next
.
Specify values for the following input parameters:
Source Type
: Third party API
Authentication HTTP headers
: Enter the Proofpoint API Key in a
Authorization: Bearer {API_KEY}
format, and add in a new line with the following WebSocket-Key data:
Sec-WebSocket-Key: SGVsbG8sIHdvcmxkIQ==
.
Cluster ID
: Enter the Proofpoint Cluster ID that you copied earlier.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create Feed
.
UDM mapping table
Log Field
UDM Mapping
Logic
classification
security_result.detection_fields.classification
The value comes directly from the
classification
field in the raw log.
cluster
security_result.detection_fields.cluster
The value comes directly from the
cluster
field in the raw log.
completelyRewritten
security_result.detection_fields.completelyRewritten
The value comes directly from the
completelyRewritten
field in the raw log.
connection.country
principal.location.country_or_region
The value comes directly from the
connection.country
field in the raw log, unless it is "**".
connection.host
principal.hostname
The value comes directly from the
connection.host
field in the raw log.
connection.ip
principal.ip
The value comes directly from the
connection.ip
field in the raw log, if it is a valid IPv4 address. It is also merged with
senderIP
if present.
connection.protocol
network.application_protocol
The protocol part before the colon in
connection.protocol
is extracted using gsub and mapped.  For example, "smtp:smtp" becomes "SMTP".
connection.tls.inbound.cipher
network.tls.cipher
The value comes directly from the
connection.tls.inbound.cipher
field in the raw log, unless it is "NONE".
connection.tls.inbound.version
network.tls.version
The value comes directly from the
connection.tls.inbound.version
field in the raw log, unless the cipher is "NONE".
envelope.from
network.email.from
The value comes directly from the
envelope.from
field in the raw log. It is also replaced by
sm.from
or
fromAddress
if present.
envelope.rcpts
network.email.to
The email addresses in
envelope.rcpts
are merged into the
network.email.to
field if they are valid email addresses. It is also merged with
sm.to
or
toAddresses
if present.
envelope.rcptsHashed
read_only_udm.additional.fields
The hashed email addresses in
envelope.rcptsHashed
are added as additional fields with keys like "toHashed_0", "toHashed_1", etc.
eventTime
@timestamp
The value is parsed from the
eventTime
field using the ISO8601 or RFC 3339 format.
eventType
security_result.summary
The value comes directly from the
eventType
field in the raw log.
filter.disposition
security_result.action_details
The value comes directly from the
filter.disposition
field in the raw log, unless
tls.verify
is present.
filter.modules.av.virusNames.0
security_result.threat_name
The value comes directly from the
filter.modules.av.virusNames.0
field in the raw log.
filter.modules.dmarc.authResults
read_only_udm.additional.fields
The method and result from each entry in
filter.modules.dmarc.authResults
are added as additional fields with keys like "authResultsMethod_0", "authResults_result_0", "authResultsMethod_1", etc.
filter.modules.spam.langs
read_only_udm.additional.fields
Each language in
filter.modules.spam.langs
is added as an additional field with keys like "lang_0", "lang_1", etc.
filter.modules.spam.safeBlockedListMatches.0.listType
security_result.detection_fields.safeBlockedListMatches_listType
The value comes directly from the
filter.modules.spam.safeBlockedListMatches.0.listType
field in the raw log.
filter.modules.spam.safeBlockedListMatches.0.rule
security_result.detection_fields.safeBlockedListMatches_rule
The value comes directly from the
filter.modules.spam.safeBlockedListMatches.0.rule
field in the raw log.
filter.modules.spam.scores.classifiers.adult
security_result.detection_fields.adult
The value comes directly from the
filter.modules.spam.scores.classifiers.adult
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.bulk
security_result.detection_fields.bulk
The value comes directly from the
filter.modules.spam.scores.classifiers.bulk
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.impostor
security_result.detection_fields.impostor
The value comes directly from the
filter.modules.spam.scores.classifiers.impostor
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.lowpriority
security_result.detection_fields.lowpriority
The value comes directly from the
filter.modules.spam.scores.classifiers.lowpriority
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.malware
security_result.detection_fields.malware
The value comes directly from the
filter.modules.spam.scores.classifiers.malware
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.mlx
security_result.detection_fields.mlx
The value comes directly from the
filter.modules.spam.scores.classifiers.mlx
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.mlxlog
security_result.detection_fields.mlxlog
The value comes directly from the
filter.modules.spam.scores.classifiers.mlxlog
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.phish
security_result.detection_fields.phish
The value comes directly from the
filter.modules.spam.scores.classifiers.phish
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.spam
security_result.detection_fields.spam
The value comes directly from the
filter.modules.spam.scores.classifiers.spam
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.classifiers.suspect
security_result.detection_fields.suspect
The value comes directly from the
filter.modules.spam.scores.classifiers.suspect
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.engine
security_result.detection_fields.engine
The value comes directly from the
filter.modules.spam.scores.engine
field in the raw log, if it is not empty or 0.
filter.modules.spam.scores.overall
security_result.detection_fields.overall
The value comes directly from the
filter.modules.spam.scores.overall
field in the raw log, if it is not empty or 0.
filter.modules.spam.version.definitions
security_result.summary
The value comes directly from the
filter.modules.spam.version.definitions
field in the raw log.
filter.modules.spam.version.engine
metadata.product_version
The value comes directly from the
filter.modules.spam.version.engine
field in the raw log.
filter.modules.urldefense.counts.rewritten
read_only_udm.additional.fields.urldefenseCountsRewritten
The value comes directly from the
filter.modules.urldefense.counts.rewritten
field in the raw log.
filter.modules.urldefense.counts.total
security_result.detection_fields.urldefense_total
The value comes directly from the
filter.modules.urldefense.counts.total
field in the raw log.
filter.modules.zerohour.score
read_only_udm.additional.fields.zeroHourScore
The value comes directly from the
filter.modules.zerohour.score
field in the raw log.
filter.origGuid
read_only_udm.additional.fields.origGuid
The value comes directly from the
filter.origGuid
field in the raw log.
filter.qid
read_only_udm.additional.fields.filterQid
The value comes directly from the
filter.qid
field in the raw log.
filter.quarantine.folder
security_result.detection_fields.filter_quarantine_folder
The value comes directly from the
filter.quarantine.folder
field in the raw log.
filter.quarantine.folderId
security_result.detection_fields.filter_quarantine_folderId
The value comes directly from the
filter.quarantine.quarantine.folderId
field in the raw log.
filter.quarantine.module
security_result.detection_fields.filter_quarantine_module
The value comes directly from the
filter.quarantine.module
field in the raw log.
filter.quarantine.rule
security_result.detection_fields.filter_quarantine_rule
The value comes directly from the
filter.quarantine.rule
field in the raw log.
filter.quarantine.type
security_result.detection_fields.filter_quarantine_type
The value comes directly from the
filter.quarantine.type
field in the raw log.
filter.routeDirection
network.direction
If
filter.routeDirection
is "inbound",
network.direction
is set to "INBOUND". If
filter.routeDirection
is "outbound",
network.direction
is set to "OUTBOUND".
filter.routes
read_only_udm.additional.fields
Each route in
filter.routes
is added as an additional field with keys like "filterRoutes_0", "filterRoutes_1", etc.
fromAddress
network.email.from
The email addresses in
fromAddress
are replaced into the
network.email.from
field if they are valid email addresses.
guid
metadata.product_log_id
The value comes directly from the
guid
field in the raw log.
GUID
metadata.product_log_id
The value comes directly from the
GUID
field in the raw log.
headerFrom
network.email.from
The value comes directly from the
headerFrom
field in the raw log.
impostorScore
security_result.detection_fields.impostorScore
The value comes directly from the
impostorScore
field in the raw log.
malwareScore
security_result.detection_fields.malwareScore
The value comes directly from the
malwareScore
field in the raw log.
messageID
network.email.mail_id
The value comes directly from the
messageID
field in the raw log.
messageSize
security_result.detection_fields.messageSize
The value comes directly from the
messageSize
field in the raw log.
messageTime
@timestamp
The value is parsed from the
messageTime
field using the ISO8601 or RFC 3339 format.
metadata.customerId
principal.labels.customerId
The value comes directly from the
metadata.customerId
field in the raw log.
metadata.origin.data.agent
network.http.user_agent
The value comes directly from the
metadata.origin.data.agent
field in the raw log.
metadata.origin.data.cid
principal.user.userid
The value comes directly from the
metadata.origin.data.cid
field in the raw log.
metadata.origin.data.version
metadata.product_version
The value comes directly from the
metadata.origin.data.version
field in the raw log.
msg.header.from
read_only_udm.additional.fields.msgHeaderFrom
The value comes directly from the
msg.header.from.0
field in the raw log.
msg.header.reply-to
network.email.reply_to
The email address enclosed in <> in
msg.header.reply-to.0
is extracted and mapped.
msg.header.subject
network.email.subject
The value comes directly from the
msg.header.subject
field in the raw log.
msg.header.to
read_only_udm.additional.fields.msgHeaderTo
The value comes directly from the
msg.header.to
field in the raw log.
msg.normalizedHeader.subject
network.email.subject
The value comes directly from the
msg.normalizedHeader.subject
field in the raw log.
msg.parsedAddresses.cc
network.email.cc
The email addresses in
msg.parsedAddresses.cc
are merged into the
network.email.cc
field if they are valid email addresses.
msg.parsedAddresses.ccHashed
read_only_udm.additional.fields
The hashed email addresses in
msg.parsedAddresses.ccHashed
are added as additional fields with keys like "ccHashed_0", "ccHashed_1", etc.
msg.parsedAddresses.from
read_only_udm.additional.fields.msgParsedAddressesFrom
The value comes directly from the
msg.parsedAddresses.from.0
field in the raw log.
msg.parsedAddresses.from.0
principal.user.email_addresses
The value comes directly from the
msg.parsedAddresses.from.0
field in the raw log.
msg.parsedAddresses.fromHashed
read_only_udm.additional.fields.fromHashed
The value comes directly from the
msg.parsedAddresses.fromHashed.0
field in the raw log.
msg.parsedAddresses.to
target.user.email_addresses
The email addresses in
msg.parsedAddresses.to
are merged into the
target.user.email_addresses
field if they are valid email addresses.
msgParts
read_only_udm.about
Multiple about objects are created, one for each entry in
msgParts
.  File hashes, MIME type, size, and other metadata are extracted.
QID
security_result.detection_fields.QID
The value comes directly from the
QID
field in the raw log.
recipient
target.user.email_addresses
The email addresses in
recipient
are merged into the
target.user.email_addresses
field if they are valid email addresses.
replyToAddress
network.email.reply_to
The email addresses in
replyToAddress
are replaced into the
network.email.reply_to
field if they are valid email addresses.
sender
principal.user.email_addresses
The value comes directly from the
sender
field in the raw log, if it is a valid email address.
senderIP
principal.ip
The value comes directly from the
senderIP
field in the raw log.
sm.from
network.email.from
The value comes directly from the
sm.from
field in the raw log.
sm.msgid
network.email.mail_id
The value comes directly from the
sm.msgid
field in the raw log, after removing "<" and ">".
sm.proto
network.application_protocol
The value comes directly from the
sm.proto
field in the raw log.
sm.qid
security_result.detection_fields.QUID
The value comes directly from the
sm.qid
field in the raw log.
sm.relay
intermediary.hostname
,
intermediary.ip
The hostname and IP address are extracted from
sm.relay
using grok.
sm.stat
security_result.detection_fields.Stat
The first word of
sm.stat
is extracted using grok and mapped.
sm.to
network.email.to
The email addresses in
sm.to
are merged into the
network.email.to
field if they are valid email addresses.
spamScore
security_result.detection_fields.spamScore
The value comes directly from the
spamScore
field in the raw log.
subject
network.email.subject
The value comes directly from the
subject
field in the raw log.
threat
security_result.detection_fields.threat
The value comes directly from the
threat
field in the raw log.
threatsInfoMap
security_result.detection_fields
Key-value pairs from each entry in
threatsInfoMap
are added as detection fields.
threatType
security_result.detection_fields.threatType
The value comes directly from the
threatType
field in the raw log.
tls.cipher
network.tls.cipher
The value comes directly from the
tls.cipher
field in the raw log, unless it is "NONE".
tls.verify
security_result.action_details
The value comes directly from the
tls.verify
field in the raw log.
tls.version
network.tls.version
The value comes directly from the
tls.version
field in the raw log, unless the cipher is "NONE".
toAddresses
network.email.to
The email addresses in
toAddresses
are merged into the
network.email.to
field if they are valid email addresses.
ts
@timestamp
The value is parsed from the
ts
field using the ISO8601 or RFC 3339 format, after some preprocessing to handle extra fractional seconds.
Need more help?
Get answers from Community members and Google SecOps professionals.
