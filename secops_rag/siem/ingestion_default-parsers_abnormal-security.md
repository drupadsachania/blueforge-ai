# Collect Abnormal Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/abnormal-security/  
**Scraped:** 2026-03-05T09:18:27.224435Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Abnormal Security logs
Supported in:
Google secops
SIEM
This document explains how to ingest Abnormal Security logs to
Google Security Operations. The parser handles email logs in both JSON and Syslog
formats. It first attempts to process the input as JSON, and if unsuccessful,
it uses Grok patterns to extract data from the Syslog format. The extracted
fields are then mapped to the Unified Data Model (UDM), enriching the data with
relevant security context and standardizing the format for further analysis.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
Privileged access to Abnormal Security.
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
Configure Abnormal Security to send logs to Google SecOps
Sign in to the
Abnormal Security
Web UI.
Click
Settings
>
Integrations
.
Find the
Google Chronicle
icon and click
Connect
.
Enter your
Google SecOps Customer ID
.
Enter your
Google SecOps instance Endpoint address
.
Canada
:
https://northamerica-northeast2-malachiteingestion-pa.googleapis.com
Dammam
:
https://me-central2-malachiteingestion-pa.googleapis.com
Europe Multi-Region
:
https://europe-malachiteingestion-pa.googleapis.com
Frankfurt
:
https://europe-west3-malachiteingestion-pa.googleapis.com
London
:
https://europe-west2-malachiteingestion-pa.googleapis.com
Mumbai
:
https://asia-south1-malachiteingestion-pa.googleapis.com
Singapore
:
https://asia-southeast1-malachiteingestion-pa.googleapis.com
Sydney
:
https://australia-southeast1-malachiteingestion-pa.googleapis.com
Tel Aviv
:
https://me-west1-malachiteingestion-pa.googleapis.com
Tokyo
:
https://asia-northeast1-malachiteingestion-pa.googleapis.com
United States Multi-Region
:
https://malachiteingestion-pa.googleapis.com
Zurich
:
https://europe-west6-malachiteingestion-pa.googleapis.com
Upload the
Ingestion Authentication File
downloaded earlier as Google Service Account.
Click
Save
>
Confirm
.
Supported Abnormal Security log formats
The Abnormal Security parser supports logs in SYSLOG and JSON formats.
Supported Abnormal Security Sample Logs
JSON
{
"threatId"
:
"3fd4ed1a-9237-7e6f-d434-eacdcc41f47b"
,
"messages"
:
[
{
"abxMessageId"
:
3405268390454580698
,
"abxPortalUrl"
:
"https://portal.abnormalsecurity.com/home/threat-center/remediation-history/3405268390454580698"
,
"attachmentCount"
:
0
,
"attachmentNames"
:
[],
"attackStrategy"
:
"Unknown Sender"
,
"attackType"
:
"Spam"
,
"attackVector"
:
"Link"
,
"attackedParty"
:
"VIP"
,
"autoRemediated"
:
true
,
"fromAddress"
:
"masked.from@example.com"
,
"fromName"
:
"Masked User Name"
,
"impersonatedParty"
:
"None / Others"
,
"internetMessageId"
:
"<20eb9e7c1c3046fda97f6564c81ced64@530566577>"
,
"isRead"
:
false
,
"postRemediated"
:
false
,
"receivedTime"
:
"2023-08-28T14:09:31Z"
,
"recipientAddress"
:
"masked.recipient@example.com"
,
"remediationStatus"
:
"Auto-Remediated"
,
"remediationTimestamp"
:
"2023-08-28T14:09:35.618Z"
,
"sentTime"
:
"2023-08-28T14:08:44Z"
,
"subject"
:
"Banking Insights | A deep dive into the global M&A landscape"
,
"threatId"
:
"3fd4ed1a-9237-7e6f-d434-eacdcc41f47b"
,
"toAddresses"
:
[
"masked.to@example.com"
],
"ccEmails"
:
[],
"replyToEmails"
:
[
"masked.reply@example.com"
],
"returnPath"
:
"masked.returnPath@example.com"
,
"senderDomain"
:
"masked.sender.domain"
,
"senderIpAddress"
:
null
,
"summaryInsights"
:
[
"Suspicious Link"
,
"Unusual Sender"
,
"Abnormal Email Body HTML"
,
"Invisible characters found in Email"
,
"Unusual Sender Domain"
,
"Suspicious Financial Request"
,
"Unusual Reply To"
],
"urlCount"
:
19
,
"urls"
:
[
"https://masked.comm.link/e/es?s=530566577&e=2595782&elqTrackId=MASKEDID&elq=MASKEDID&elqaid=119820&elqat=1"
,
"https://www.masked.group/en/simplifying-the-brand?utm_source=Eloqua&utm_medium=email&utm_campaign=MASKED_CAMPAIGN&elqCampaignId=20995&elq=MASKEDID"
,
"https://masked.group.link/e/er?utm_source=Eloqua&utm_medium=email&utm_campaign=MASKED_CAMPAIGN&elqCampaignId=20995&s=530566577&lid=192730&elqTrackId=MASKEDID&elq=MASKEDID&elqaid=119820&elqat=1"
// ... (16 additional masked URLs omitted for brevity)
]
}
]
}
SYSLOG + JSON
<14> {
  "threatId": "83da593b-3778-9d2f-da8c-e305dc1425e1",
  "messages": [
    {
      "abxMessageId": 8274341447487143770,
      "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/8274341447487143770",
      "attackType": "Spam",
      "fromAddress": "masked.from.1@example.com",
      "fromName": "Masked User Name",
      "internetMessageId": "<PUZPR06MB45764FCED76739D0BC8A1B69E3DFA@masked.server.prod.outlook.com>",
      "recipientAddress": "masked.recipient.1@example.com",
      "remediationStatus": "Auto-Remediated",
      "subject": "Freightview, FreightPOP Users List",
      "toAddresses": [
        "masked.to.1@example.com"
      ],
      "returnPath": "masked.returnPath.1@example.com",
      "senderDomain": "outlook.com",
      "senderIpAddress": null,
      "urlCount": 0,
      "urls": []
    },
    {
      "abxMessageId": -4495524442058864563,
      "abxPortalUrl": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-4495524442058864563",
      "attackType": "Spam",
      "fromAddress": "masked.user.2@outlook.com",
      "fromName": "Masked User Name",
      "internetMessageId": "<PUZPR06MB4576BF221988D780C8412731E3DFA@masked.server.prod.outlook.com>",
      "recipientAddress": "masked.recipient.2@example.com",
      "remediationStatus": "Auto-Remediated",
      "subject": "Freightview, FreightPOP Users List",
      "toAddresses": [
        "masked.to.2@example.com"
      ],
      "returnPath": "masked.user.2@outlook.com",
      "senderDomain": "outlook.com",
      "senderIpAddress": null,
      "urlCount": 0,
      "urls": []
    }
  ]
}
JSON (threat_log) Schema
{
  "event": {
    "abx_message_id": -3325933065721657641,
    "abx_portal_url": "https://portal.abnormalsecurity.com/home/threat-center/remediation-history/-3325933065721657641",
    "threat_id": "1c3736ab-9e3a-883f-62b5-6fe36ac9672c",
    "subject": "[EXTERNAL] RE: Masked Name PUP094439581",
    "from_address": "masked.sender@maskeddomain.xyz",
    "from_name": "masked.sender@maskeddomain.xyz",
    "to_addresses": "masked.recipient@maskedcorp.com",
    "recipient_address": "masked.recipient@maskedcorp.com",
    "internet_message_id": "<MASKEDID@masked-insurance-group.com>",
    "attack_type": "Phishing: Credential",
    "return_path": "masked.sender@maskeddomain.xyz",
    "sender_ip_address": "",
    "urls": [
      "www.masked-insurance-group.com",
      "http://www.masked-insurance-group.com/"
    ],
    "sender_domain": "masked-insurance-group.com",
    "tenant": "Auto Club Group"
  },
  "sourcetype": "threat_log"
}
JSON (abuse_mailbox) Schema
{
  "event": {
    "abx_metadata": {
      "event_type": "ABUSE_MAILBOX",
      "timestamp": "2024-04-27T15:25:53.374227319Z",
      "trace_id": "00bc67b5-eb26-41c2-9f95-021eb435fc49"
    },
    "abx_body": {
      "campaign_id": "28b9c99f-f4a4-3032-bd99-3b7bac532471",
      "subject": "[EXTERNAL] News you might have missed",
      "recipient_name": "Masked PII Name",
      "recipient_address": "masked.abuse.recipient@secops.com",
      "internet_message_id": "<AutoNewsDigest-MASKED@odspnotify>",
      "email_label_or_location": "inbox"
    }
  },
  "sourcetype": "abuse_mailbox"
}
JSON (audit_log) Schema
{
  "event": {
    "abx_metadata": {
      "event_type": "AUDIT_LOG",
      "timestamp": "2024-04-01T17:50:55.194231924Z",
      "trace_id": "6f95188c-cba2-4e86-a3ae-3eaf22c869e4"
    },
    "abx_body": {
      "category": "login",
      "details": {
        "request_url": "/api-token-auth/"
      },
      "source_ip": "0.0.0.0",
      "status": "SUCCESS",
      "tenant_name": "masked_secops_tenant",
      "timestamp": "2024-04-01T17:50:54.632Z",
      "user": {
        "email": "masked.audit.user@secops.net"
      }
    }
  },
  "sourcetype": "audit_log"
}
JSON (case) Schema
{
  "event": {
    "abx_metadata": {
      "event_type": "CASE",
      "timestamp": "2024-08-08T12:42:45.104485389Z",
      "trace_id": "e4ad638f-439a-4c5f-839d-b650ecab9156"
    },
    "abx_body": {
      "schema_version": "1.0.0",
      "case_id": 11188520,
      "tenant": "masked name",
      "entity": {
        "entity_type": "USER_ACCOUNT",
        "identifier": "masked.case.user@secops.com"
      },
      "description": "Account Compromised",
      "event_timeline": [
        {
          "timestamp": "2024-09-07T20:17:25+00:00",
          "event_type": "SIGN_IN",
          "platform": "AZURE_AD",
          "insights": [
            {
              "signal": "Risky Browser",
              "description": "The browser associated with this sign-in, None, is considered risky and has been blocklisted by Abnormal or your organization."
            }
          ],
          "ip_address": "0.0.0.0 ",
          "operating_system": "ios 17.6",
          "isp": "verizon wireless",
          "location": {
            "city": "Huntley",
            "state": "Illinois",
            "country": "United States"
          }
        },
        {
          "timestamp": "2024-09-07T20:17:25+00:00",
          "event_type": "SIGN_IN",
          "platform": "AZURE_AD",
          "ip_address": "0.0.0.0 ",
          "operating_system": "ios 15.6"
        }
      ],
      "event_type": "CASE"
    }
  },
  "sourcetype": "case"
}
UDM mapping table
Log field
UDM mapping
Logic
attachmentCount
additional.fields.attachmentCount.value.number_value
Mapped directly
attachmentNames
additional.fields.attachmentNames.value
Concatenated into a comma-separated string
attackStrategy
security_result.detection_fields.attackStrategy.value
Mapped directly
attackType
security_result.threat_name
Mapped directly
attackVector
security_result.detection_fields.attackVector.value
Mapped directly
attackedParty
security_result.detection_fields.attackedParty.value
Mapped directly
autoRemediated
Not mapped to the IDM object
ccEmails
network.email.cc
Each email address is extracted and added to the array
fromAddress
network.email.from
Email address is extracted and mapped directly
fromName
principal.user.user_display_name
Mapped directly
impersonatedParty
security_result.detection_fields.impersonatedParty.value
Mapped directly
internetMessageId
additional.fields.internetMessageId.value.string_value
Mapped directly
isRead
additional.fields.isRead.value.bool_value
Mapped directly
postRemediated
additional.fields.postRemediated.value.bool_value
Mapped directly
receivedTime
additional.fields.mailReceivedTime.value.string_value
Mapped directly
remediationStatus
additional.fields.remediationStatus.value.string_value
Mapped directly
remediationTimestamp
additional.fields.mailRemediationTimestamp.value.string_value
Mapped directly
replyToEmails
network.email.reply_to
The first email address is extracted and mapped directly
returnPath
additional.fields.returnPath.value.string_value
Mapped directly
senderDomain
principal.administrative_domain
Mapped directly
senderIpAddress
principal.ip, principal.asset.ip
IP address is extracted and mapped to both fields
sentTime
additional.fields.mailSentTime.value.string_value
Mapped directly
subject
network.email.subject
Mapped directly
summaryInsights
security_result.summary
Concatenated into a comma-separated string
threatId
security_result.threat_id
Mapped directly
toAddresses
network.email.to
Each email address is extracted and added to the array
urlCount
additional.fields.urlCount.value.number_value
Mapped directly
URLs
additional.fields.detectedUrls.value
Concatenated into a comma-separated string
additional.fields.campaign_id.value.string_value
Mapped from event_data.abx_body.campaign_id if present
additional.fields.trace_id.value.string_value
Mapped from event_data.abx_metadata.trace_id if present
additional.fields.messageReportedTime.value.string_value
Mapped from event_data.abx_body.message_reported_time if present
metadata.event_type
Set to
EMAIL_TRANSACTION
if messages array is present, otherwise determined based on other fields and can be
USER_LOGIN
,
STATUS_UPDATE
, or
GENERIC_EVENT
metadata.product_name
Always set to
ABNORMAL_SECURITY
metadata.vendor_name
Always set to
ABNORMAL_SECURITY
metadata.product_event_type
Mapped from event_data.abx_metadata.event_type if present
extensions.auth.type
Set to
AUTHTYPE_UNSPECIFIED
if event_type is
USER_LOGIN
security_result.category
Set to
MAIL_SPAM
and
MAIL_PHISHING
if messages array is present, otherwise set to
MAIL_PHISHING
and/or
MAIL_SPAM
based on other fields
security_result.category_details
Set to
ABUSE_MAILBOX
if abx_metadata.event_type is
ABUSE_MAILBOX
, otherwise set to
login
if abx_body.category is
login
security_result.detection_fields.reported.value
Mapped from event_data.abx_body.reported if present
security_result.detection_fields.judgement.value
Mapped from event_data.abx_body.judgement if present
target.url
Mapped from event_data.abx_body.details.request_url if present
target.user.userid
Mapped from event_data.abx_body.user.email if present
target.user.email_addresses
Mapped from event_data.abx_body.user.email if present
Need more help?
Get answers from Community members and Google SecOps professionals.
