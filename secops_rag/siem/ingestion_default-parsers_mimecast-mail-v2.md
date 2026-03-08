# Collect Mimecast Mail V2 logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/mimecast-mail-v2/  
**Scraped:** 2026-03-05T09:26:39.063675Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Mimecast Mail V2 logs
Supported in:
Google secops
SIEM
This document explains how to collect Mimecast Mail V2 logs by setting up a Google Security Operations feed using the Third party API.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to Mimecast Mail V2 tenant or admin console
Admin privileges in Mimecast to create API applications
Configure IP allowlisting
Before creating the feed, you must allowlist Google SecOps IP ranges in your Mimecast Mail V2 firewall or network settings.
Get Google SecOps IP ranges
Fetch IP ranges from the
Google IP address ranges JSON file
.
Add IP ranges to Mimecast Mail V2
Sign in to the Mimecast Administration Console.
Go to
Administration
>
Services
>
Firewall Policies
.
Click
Add Address
.
Enter each Google SecOps IP range in CIDR notation.
Select
Allow
for the Action.
Provide a description (for example,
Google SecOps Integration
).
Click
Save
.
Configure Mimecast Mail V2 API access
To enable Google SecOps to pull logs from Mimecast, you need to register an application in the Mimecast Administration Console and obtain OAuth credentials.
Create API application
Sign in to the
Mimecast Administration Console
.
Go to
Administration
>
Services
>
API Management
>
Applications
.
Click
Add
.
Provide the following configuration details:
Name
: Enter a descriptive name (for example,
Google SecOps Integration
).
Description
(optional): Enter a description.
Type
: Select
OAuth
.
OAuth Grant Type
: Select
Client Credentials
.
URL
: Enter your Google SecOps domain or leave blank.
Under
Access Scopes
, select the required permissions (see Required API Permissions section).
Click
Save
.
Generate API credentials
After creating the application, click the application name in the list.
Go to the
OAuth
tab.
Click
Create Credentials
.
Note the
Client ID
and
Client Secret
displayed.
Click
Close
.
Record API credentials
After generating the credentials, you'll receive the following:
Client ID
: Your OAuth 2.0 client identifier
Client Secret
: Your OAuth 2.0 client secret
Required API permissions
The API application requires the following permissions:
Permission/Scope
Access Level
Purpose
Audit/SIEM
Read
Retrieve SIEM log data
Audit/AuditEvents
Read
Retrieve audit event data
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
Mimecast Mail Logs
).
Select
Third party API
as the
Source type
.
Select
Mimecast Mail V2
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
OAuth client ID
: The client ID from the API application created earlier.
OAuth client secret
: The client secret from the API application created earlier.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
After setup, the feed begins to retrieve logs from the Mimecast Mail V2 instance in chronological order.
Regional endpoints
Mimecast Mail V2 uses different API endpoints based on your region:
Region
Base URL
US
https://us-api.mimecast.com
UK
https://uk-api.mimecast.com
EU
https://eu-api.mimecast.com
DE
https://de-api.mimecast.com
AU
https://au-api.mimecast.com
ZA
https://za-api.mimecast.com
CA
https://ca-api.mimecast.com
Offshore
https://je-api.mimecast.com
Use the base URL that corresponds to your Mimecast Mail V2 instance region.
UDM mapping table
Log Field
UDM Mapping
Logic
aCode
additional_fields.aCode
Value taken from
aCode
.
Att_AV
additional_fields.Att_AV
Value taken from
Att_AV
.
Att_Det
additional_fields.Att_Det
Value taken from
Att_Det
.
Att_Enc
additional_fields.Att_Enc
Value taken from
Att_Enc
.
Att_Key
additional_fields.Att_Key
Value taken from
Att_Key
.
Att_Mod
additional_fields.Att_Mod
Value taken from
Att_Mod
.
Att_Orig
additional_fields.Att_Orig
Value taken from
Att_Orig
.
Att_Rem
additional_fields.Att_Rem
Value taken from
Att_Rem
.
Att_State
additional_fields.Att_State
Value taken from
Att_State
.
Att_Type
additional_fields.Att_Type
Value taken from
Att_Type
.
CKS
additional_fields.CKS
Value taken from
CKS
.
Date
additional_fields.Date
Value taken from
Date
.
Delivered
additional_fields.Delivered
Value taken from
Delivered
.
dlp
additional_fields.dlp
Value taken from
dlp
.
Dmarc
additional_fields.Dmarc
Value taken from
Dmarc
.
Enc
additional_fields.Enc
Value taken from
Enc
.
Error_Code
additional_fields.Error_Code
Value taken from
Error_Code
.
Error_Type
additional_fields.Error_Type
Value taken from
Error_Type
.
Grey
additional_fields.Grey
Value taken from
Grey
.
header_id
additional_fields.header_id
Value taken from
header_id
.
Hold_For
additional_fields.Hold_For
Value taken from
Hold_For
.
Hold_Reason
additional_fields.Hold_Reason
Value taken from
Hold_Reason
.
Latency
additional_fields.Latency
Value taken from
Latency
.
Malware_Hash
additional_fields.Malware_Hash
Value taken from
Malware_Hash
.
Malware_Name
additional_fields.Malware_Name
Value taken from
Malware_Name
.
Msg_Key
additional_fields.Msg_Key
Value taken from
Msg_Key
.
MsgSize
additional_fields.MsgSize
Value taken from
MsgSize
.
Policy
additional_fields.Policy
Value taken from
Policy
.
Processing_Time
additional_fields.Processing_Time
Value taken from
Processing_Time
.
Queue_ID
additional_fields.Queue_ID
Value taken from
Queue_ID
.
rcpt_type
additional_fields.rcpt_type
Value taken from
rcpt_type
.
Receipt
additional_fields.Receipt
Value taken from
Receipt
.
sCode
additional_fields.sCode
Value taken from
sCode
.
Sent
additional_fields.Sent
Value taken from
Sent
.
Snt
additional_fields.Snt
Value taken from
Snt
.
spamLimit
additional_fields.spamLimit
Value taken from
spamLimit
.
spamScore
additional_fields.spamScore
Value taken from
spamScore
.
SpamRef
additional_fields.SpamRef
Value taken from
SpamRef
.
Tarpit
additional_fields.Tarpit
Value taken from
Tarpit
.
Time
additional_fields.Time
Value taken from
Time
.
datetime
metadata.event_timestamp
Value taken from
datetime
. The original
datetime
field is also parsed to set the event's primary
@timestamp
.
metadata.event_type
Set to
NETWORK_EMAIL
.
metadata.product_event_type
Set to
processed_email
.
dir
network.direction
Derived from
dir
:
In
-> INBOUND;
Out
-> OUTBOUND;
Int
-> UNKNOWN.
sender
,
route
,
hdr_from
network.email.from
Value taken from
sender
, then
route
. If still empty, value is taken from
hdr_from
.
MsgID
network.email.message_id
Value taken from
MsgID
.
subject
network.email.subject
Value taken from
subject
.
rcpt
network.email.to
Value taken from
rcpt
and split by ',' into an array.
IP
principal.ip
Value taken from
IP
and split by ',' into an array.
hdr_from
principal.user.email_addresses
Value taken from
hdr_from
and split by ',' into an array.
act
security_result.action
Derived from
act
:
Rej
,
T
,
Hld
,
Bnc
-> BLOCK;
U
,
A
-> ALLOW; else UNKNOWN.
Att_Hash
target.file.md5
Value taken from
Att_Hash
.
Att_Name
target.file.name
Value taken from
Att_Name
.
Att_Size
target.file.size
Value taken from
Att_Size
and converted to integer.
URL
target.url
Value taken from
URL
.
rcpt_to
target.user.email_addresses
Value taken from
rcpt_to
and split by ',' into an array.
metadata.product_name
Set to
Mail V2
.
metadata.vendor_name
Set to
Mimecast
.
Need more help?
Get answers from Community members and Google SecOps professionals.
