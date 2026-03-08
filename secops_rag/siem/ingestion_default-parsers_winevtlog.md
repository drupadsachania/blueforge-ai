# Collect Microsoft Windows Event logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/winevtlog/  
**Scraped:** 2026-03-05T09:17:49.447252Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Microsoft Windows Event logs
Supported in:
Google secops
SIEM
This document describes the deployment architecture, installation steps, and required configuration that produce logs supported by the Google Security Operations parser for Windows events. This document also includes information about how the parser maps fields in the original log to Google Security Operations Unified Data Model fields. For an overview of Google Security Operations data ingestion, see
Data ingestion to Google Security Operations
.
To ingest Windows event logs to Google Security Operations, use the Bindplane Agent or Google Cloud built-in ingestion. For more information about built-in ingestion, see
Ingest Google Cloud data to Google Security Operations
.
Information in this document applies to the parser with the WINEVTLOG ingestion label.
The ingestion label identifies which parser normalizes raw log data to structured UDM format.
Before you begin
Review the recommended deployment architecture
We recommend using Google Cloud built-in ingestion if your deployment includes a Windows server on Google Cloud. Otherwise, you can use the Bindplane Agent.
Google Cloud built-in ingestion architecture
If the Windows events have the Provider value
Microsoft-Windows-Security-Auditing
, then the WINEVTLOG parser supports Google Cloud built-in ingestion.
Configure Ops Agent to ingest Microsoft Windows Event logs into Google Security Operations
Deploy a
Windows server in Google Cloud
.
Configure an
Ops Agent on Windows Server
.
Install the
Cloud Logging agent on Windows Server
.
Enable the following export filter in the Google Security Operations instance:
(log_id("winevt.raw") OR log_id("windows_event_log"))
. For more information, see
Ingest Google Cloud data to Google Security Operations
.
Configure the Bindplane agent to ingest Microsoft Windows Event logs into Google Security Operations
Collect the Windows Event logs by using the Bindplane Agent. After installation, the Bindplane Agent service appears as the
observerIQ
service in the list of Windows services.
Install and configure the Windows servers. For more information about configuring the Windows servers, see
Configure Windows server overview
.
Install Bindplane Agent on a Windows server running the collector. For more information about installing the Bindplane Agent,
see
the Bindplane Agent installation instructions
.
Create a configuration file for the Bindplane agent with the following contents:
receivers:
  windowseventlog/dfsn_serv:
      channel: Microsoft-Windows-DFSN-Server/Admin
      raw: true
  windowseventlog/operational:
      channel: Microsoft-Windows-Forwarding/Operational
      raw: true
  windowseventlog/source0__application:
      channel: application
      raw: true
  windowseventlog/source0__security:
      channel: security
      raw: true
  windowseventlog/source0__system:
      channel: system
      raw: true
processors:
  batch:

exporters:
  chronicle/winevtlog:
    endpoint: https://malachiteingestion-pa.googleapis.com
    creds: '{
    "type": "service_account",
    "project_id": "malachite-projectname",
    "private_key_id": `
PRIVATE_KEY_ID
`,
    "private_key": `
PRIVATE_KEY
`,
    "client_email":"`
SERVICE_ACCOUNT_NAME
`@malachite-`
PROJECT_ID
`.iam.gserviceaccount.com",
    "client_id": `
CLIENT_ID
`,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/`
SERVICSERVICE_ACCOUNT_NAME
`%40malachite-`
PROJECT_ID
`.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
    }'
  log_type: 'WINEVTLOG'
  override_log_type: false
  raw_log_field: body
  customer_id: `
CUSTOMER_ID
`

service:
  pipelines:
    logs/winevtlog:
      receivers:
        - windowseventlog/source0__application
        - windowseventlog/source0__security
        - windowseventlog/source0__system
        - windowseventlog/dfsn_serv
        - windowseventlog/operational
    processors: [batch]
    exporters: [chronicle/winevtlog]
Replace the
PRIVATE_KEY_ID
,
PRIVATE_KEY
SERVICSERVICE_ACCOUNT_NAME
,
PROJECT_ID
,
CLIENT_ID
and
CUSTOMER_ID
with the respective values from the service account JSON file which you can download from Google Cloud Platform. For more information about service account keys, see
Create and delete service account keys documentation
.
To start the observerIQ agent service, select
Services
>
Extended
>
observerIQ Service
>
start
.
NXLog forwarder ingestion deployment architecture
This diagram illustrates the recommended foundational components in a deployment
architecture to collect and send Microsoft Windows Event data to Google Security Operations.
Compare this information with your environment to be sure these components are
installed. Each customer deployment will differ from this representation and may be more complex.
The following is required:
Systems in the deployment architecture are configured with the UTC time
zone.
NXLog is installed on the collector Microsoft Windows server.
The collector Microsoft Windows server receives logs from servers, endpoints, and
domain controllers.
Microsoft Windows systems in the deployment architecture use.
Source Initiated Subscriptions to collect events across
multiple devices.
WinRM service is enabled for remote system management.
NXLog is installed on the collector Window server to forward logs to
Google Security Operations forwarder.
Google Security Operations forwarder is installed on the collector Microsoft Windows or Linux server.
Review the supported devices and versions
The Google Security Operations parser supports logs from the following Microsoft Windows server versions.
Microsoft Windows server is released with the following editions: Foundation, Essentials,
Standard, and Datacenter. The event schema of logs generated by each edition do
not differ.
Microsoft Windows Server 2019
Microsoft Windows Server 2016
Microsoft Windows Server 2012
Google Security Operations parser supports logs from Microsoft Windows 10 and higher client
systems.
Google Security Operations parser supports logs collected by NXLog Community or Enterprise
Edition.
Review the supported log types
The Google Security Operations parser supports the following log types generated by Microsoft Windows
systems. For more information about these log types, see the
Microsoft Windows Event Log documentation
.
It supports logs generated with English language text and is not supported with
logs generated in non-English languages.
Log Type
Notes
Security
Security audit and event logs.
Application
Events logged by applications or programs. If the manifest isn't installed
locally, application logs will have missing / hex values.
System
Events logged by Microsoft Windows system components.
Configure the Microsoft Windows servers, endpoints, and domain controllers
Install and configure the servers, endpoints, and domain controllers.
Configure all systems with the UTC time zone.
Configure devices to forward logs to a collector Microsoft Windows server.
Configure a Source Initiated Subscription on Microsoft Windows server (Collector).
For information, see
Setting up a Source Initiated Subscription
.
Enable WinRM on Microsoft Windows servers and clients. For information, see
Installation and configuration for Microsoft Windows Remote Management
.
Configure the Microsoft Windows collector server
Set up a collector Microsoft Windows server to collect from systems.
Configure the system with the UTC time zone.
Install NXLog. Follow the
NXLog documentation
.
Create a configuration file for NXLog. Use
im_msvistalog
input module for Microsoft Windows server security channel logs. 
Replace
HOSTNAME
and
PORT
values with information about the central
Microsoft Windows or Linux server. See the NXLog documentation for information about
the
om_tcp module
.
define ROOT     C:\Program Files\nxlog
  define WINEVTLOG_OUTPUT_DESTINATION_ADDRESS
HOSTNAME
define WINEVTLOG_OUTPUT_DESTINATION_PORT
PORT
define CERTDIR  %ROOT%\cert
  define CONFDIR  %ROOT%\conf
  define LOGDIR   %ROOT%\data
  define LOGFILE  %LOGDIR%\nxlog.log
  LogFile %LOGFILE%
  Moduledir %ROOT%\modules
  CacheDir  %ROOT%\data
  Pidfile   %ROOT%\data\nxlog.pid
  SpoolDir  %ROOT%\data
  <Extension _json>
      Module      xm_json
  </Extension>
  <Input windows_security_eventlog>
      Module  im_msvistalog
      <QueryXML>
          <QueryList>
              <Query Id="0">
                  <Select Path="Application">*</Select>
                  <Select Path="System">*</Select>
                  <Select Path="Security">*</Select>
              </Query>
          </QueryList>
      </QueryXML>
      ReadFromLast  False
      SavePos  False
  </Input>
  <Output out_chronicle_windevents>
      Module      om_tcp
      Host        %WINEVTLOG_OUTPUT_DESTINATION_ADDRESS%
      Port        %WINEVTLOG_OUTPUT_DESTINATION_PORT%
      Exec        $EventTime = integer($EventTime) / 1000;
      Exec        $EventReceivedTime = integer($EventReceivedTime) / 1000;
      Exec        to_json();
  </Output>
  <Route r2>
      Path    windows_security_eventlog => out_chronicle_windevents
  </Route>
Start the NXLog service.
Configure the central Microsoft Windows or Linux server
See the
Installing and configuring the forwarder on Linux
or
Installing and configuring the forwarder on Microsoft Windows
for information about installing and configuring the forwarder.
Configure the system with the UTC time zone.
Install the Google Security Operations forwarder on the central Microsoft Windows or Linux server.
Configure the Google Security Operations forwarder to send logs to Google Security Operations. Here is an
example forwarder configuration.
- syslog:
      common:
        enabled: true
        data_type: WINEVTLOG
        batch_n_seconds: 10
        batch_n_bytes: 1048576
      tcp_address: 0.0.0.0:10518
      connection_timeout_sec: 60
Supported Windows Event log formats
The Windows Event parser supports logs in JSON, XML, SYSLOG + KV, SYSLOG + JSON and SYSLOG + XML formats.
Supported Windows Event sample logs
JSON:
{
  "EventTime": 1626244341057,
  "Hostname": "dummy_hostname",
  "Keywords": -9214364837600034816,
  "EventType": "AUDIT_SUCCESS",
  "SeverityValue": 2,
  "Severity": "INFO",
  "EventID": 4704,
  "SourceName": "Microsoft-Windows-Security-Auditing",
  "ProviderGuid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
  "Version": 0,
  "Task": 13570,
  "OpcodeValue": 0,
  "RecordNumber": 155109,
  "ActivityID": "{DB09FDBE-7A27-0000-F1FE-09DB277AD701}",
  "ProcessID": 704,
  "ThreadID": 1756,
  "Channel": "Security",
  "Message": "A user right was assigned.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-18\\r\\n\\tAccount Name:\\t\\tWIN-TEST$\\r\\n\\tAccount Domain:\\t\\tCHRONICLE2\\r\\n\\tLogon ID:\\t\\t0x3E7\\r\\n\\r\\nTarget Account:\\r\\n\\tAccount Name:\\t\\tS-1-5-21\\r\\n\\r\\nNew Right:\\r\\n\\tUser Right:\\t\\tSeTrustedCredManAccessPrivilege",
  "Category": "Authorization Policy Change",
  "Opcode": "Info",
  "SubjectUserSid": "S-1-5-18",
  "SubjectUserName": "WIN-TEST$",
  "SubjectDomainName": "CBN",
  "SubjectLogonId": "0x3e7",
  "TargetSid": "S-1-5-21",
  "PrivilegeList": "SeTrustedCredManAccessPrivilege",
  "EventReceivedTime": 1626244341057,
  "SourceModuleName": "windows_security_eventlog",
  "SourceModuleType": "im_msvistalog"
}
XML:
<Event xmlns='http://schemas.microsoft.com/win/2004/08/events/event'>
  <System>
    <Provider Name='AD FS Auditing'/>
    <EventID Qualifiers='0'>1203</EventID>
    <Version>0</Version>
    <Level>0</Level>
    <Task>3</Task>
    <Opcode>0</Opcode>
    <Keywords>0x8090000000000000</Keywords>
    <TimeCreated SystemTime='2025-02-20T13:35:25.0552620Z'/>
    <EventRecordID>54955389</EventRecordID>
    <Correlation ActivityID='{f0ae8663-79d1-0001-4787-aef0d179db01}'/>
    <Execution ProcessID='832' ThreadID='8932'/>
    <Channel>Security</Channel>
    <Computer>DA6PADFS01.ocm.ORIXUSA.CORP</Computer>
    <Security UserID='S-1-5-21-1740863675-3465329846-2508926007-133863'/>
  </System>
  <EventData>
    <Data>0d23868f-2ad0-4ff2-a774-511ef7b36a04</Data>
    <Data>&lt;?xml version=\"1.0\" encoding=\"utf-16\"?&gt;\r\n\\n&lt;AuditBase
      xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"
      xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"FreshCredentialAudit\"&gt;\r\n\\n  &lt;AuditType&gt;FreshCredentials&lt;/AuditType&gt;\r\n\\n  &lt;AuditResult&gt;Failure&lt;/AuditResult&gt;\r\n\\n  &lt;FailureType&gt;CredentialValidationError&lt;/FailureType&gt;\r\n\\n  &lt;ErrorCode&gt;N/A&lt;/ErrorCode&gt;\r\n\\n  &lt;ContextComponents&gt;\r\n\\n    &lt;Component xsi:type=\"ResourceAuditComponent\"&gt;\r\n\\n      &lt;RelyingParty&gt;http://sso.orix.com/adfs/services/trust&lt;/RelyingParty&gt;\r\n\\n      &lt;ClaimsProvider&gt;N/A&lt;/ClaimsProvider&gt;\r\n\\n      &lt;UserId&gt;kayla.cummings@orix.com&lt;/UserId&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n    &lt;Component xsi:type=\"AuthNAuditComponent\"&gt;\r\n\\n      &lt;PrimaryAuth&gt;N/A&lt;/PrimaryAuth&gt;\r\n\\n      &lt;DeviceAuth&gt;false&lt;/DeviceAuth&gt;\r\n\\n      &lt;DeviceId&gt;N/A&lt;/DeviceId&gt;\r\n\\n      &lt;MfaPerformed&gt;false&lt;/MfaPerformed&gt;\r\n\\n      &lt;MfaMethod&gt;N/A&lt;/MfaMethod&gt;\r\n\\n      &lt;TokenBindingProvidedId&gt;false&lt;/TokenBindingProvidedId&gt;\r\n\\n      &lt;TokenBindingReferredId&gt;false&lt;/TokenBindingReferredId&gt;\r\n\\n      &lt;SsoBindingValidationLevel&gt;NotSet&lt;/SsoBindingValidationLevel&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n    &lt;Component zxsi:type=\"ProtocolAuditComponent\"&gt;\r\n\\n      &lt;OAuthClientId&gt;N/A&lt;/OAuthClientId&gt;\r\n\\n      &lt;OAuthGrant&gt;N/A&lt;/OAuthGrant&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n    &lt;Component xsi:type=\"RequestAuditComponent\"&gt;\r\n\\n      &lt;Server&gt;http://sso.orix.com/adfs/services/trust&lt;/Server&gt;\r\n\\n      &lt;AuthProtocol&gt;WSFederation&lt;/AuthProtocol&gt;\r\n\\n      &lt;NetworkLocation&gt;Extranet&lt;/NetworkLocation&gt;\r\n\\n      &lt;IpAddress&gt;102.129.235.248&lt;/IpAddress&gt;\r\n\\n      &lt;ForwardedIpAddress&gt;102.129.235.248&lt;/ForwardedIpAddress&gt;\r\n\\n      &lt;ProxyIpAddress&gt;N/A&lt;/ProxyIpAddress&gt;\r\n\\n      &lt;NetworkIpAddress&gt;N/A&lt;/NetworkIpAddress&gt;\r\n\\n      &lt;ProxyServer&gt;DA6PDMZWAP02&lt;/ProxyServer&gt;\r\n\\n      &lt;UserAgentString&gt;Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0&lt;/UserAgentString&gt;\r\n\\n      &lt;Endpoint&gt;/adfs/ls/&lt;/Endpoint&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n  &lt;/ContextComponents&gt;\r\n\\n&lt;/AuditBase&gt;
    </Data>
  </EventData>
  <RenderingInfo Culture='en-US'>
    <Message>The Federation Service failed to validate a new credential. See XML for failure details. \r\n\\n\r\n\\nActivity ID: 0d23868f-2ad0-4ff2-a774-511ef7b36a04 \r\n\\n\r\n\\nAdditional Data \r\n\\nXML: &lt;?xml version=\"1.0\" encoding=\"utf-16\"?&gt;\r\n\\n&lt;AuditBase
      xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\"
      xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:type=\"FreshCredentialAudit\"&gt;\r\n\\n  &lt;AuditType&gt;FreshCredentials&lt;/AuditType&gt;\r\n\\n  &lt;AuditResult&gt;Failure&lt;/AuditResult&gt;\r\n\\n  &lt;FailureType&gt;CredentialValidationError&lt;/FailureType&gt;\r\n\\n  &lt;ErrorCode&gt;N/A&lt;/ErrorCode&gt;\r\n\\n  &lt;ContextComponents&gt;\r\n\\n    &lt;Component xsi:type=\"ResourceAuditComponent\"&gt;\r\n\\n      &lt;RelyingParty&gt;http://sso.orix.com/adfs/services/trust&lt;/RelyingParty&gt;\r\n\\n      &lt;ClaimsProvider&gt;N/A&lt;/ClaimsProvider&gt;\r\n\\n      &lt;UserId&gt;kayla.cummings@orix.com&lt;/UserId&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n    &lt;Component xsi:type=\"AuthNAuditComponent\"&gt;\r\n\\n      &lt;PrimaryAuth&gt;N/A&lt;/PrimaryAuth&gt;\r\n\\n      &lt;DeviceAuth&gt;false&lt;/DeviceAuth&gt;\r\n\\n      &lt;DeviceId&gt;N/A&lt;/DeviceId&gt;\r\n\\n      &lt;MfaPerformed&gt;false&lt;/MfaPerformed&gt;\r\n\\n      &lt;MfaMethod&gt;N/A&lt;/MfaMethod&gt;\r\n\\n      &lt;TokenBindingProvidedId&gt;false&lt;/TokenBindingProvidedId&gt;\r\n\\n      &lt;TokenBindingReferredId&gt;false&lt;/TokenBindingReferredId&gt;\r\n\\n      &lt;SsoBindingValidationLevel&gt;NotSet&lt;/SsoBindingValidationLevel&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n    &lt;Component xsi:type=\"ProtocolAuditComponent\"&gt;\r\n\\n      &lt;OAuthClientId&gt;N/A&lt;/OAuthClientId&gt;\r\n\\n      &lt;OAuthGrant&gt;N/A&lt;/OAuthGrant&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n    &lt;Component xsi:type=\"RequestAuditComponent\"&gt;\r\n\\n      &lt;Server&gt;http://sso.orix.com/adfs/services/trust&lt;/Server&gt;\r\n\\n      &lt;AuthProtocol&gt;WSFederation&lt;/AuthProtocol&gt;\r\n\\n      &lt;NetworkLocation&gt;Extranet&lt;/NetworkLocation&gt;\r\n\\n      &lt;IpAddress&gt;102.129.235.248&lt;/IpAddress&gt;\r\n\\n      &lt;ForwardedIpAddress&gt;102.129.235.248&lt;/ForwardedIpAddress&gt;\r\n\\n      &lt;ProxyIpAddress&gt;N/A&lt;/ProxyIpAddress&gt;\r\n\\n      &lt;NetworkIpAddress&gt;N/A&lt;/NetworkIpAddress&gt;\r\n\\n      &lt;ProxyServer&gt;DA6PDMZWAP02&lt;/ProxyServer&gt;\r\n\\n      &lt;UserAgentString&gt;Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0&lt;/UserAgentString&gt;\r\n\\n      &lt;Endpoint&gt;/adfs/ls/&lt;/Endpoint&gt;\r\n\\n    &lt;/Component&gt;\r\n\\n  &lt;/ContextComponents&gt;\r\n\\n&lt;/AuditBase&gt;
    </Message>
    <Level>Information</Level>
    <Task></Task>
    <Opcode>Info</Opcode>
    <Channel></Channel>
    <Provider></Provider>
    <Keywords>
      <Keyword>Audit Failure</Keyword>
      <Keyword>Classic</Keyword>
    </Keywords>
  </RenderingInfo>
</Event>
SYSLOG + KV:
2021-12-20 02:58:35 domain.com INFO Keywords="9232379236109516800" EventType="AUDIT_SUCCESS" SeverityValue="2" EventID="4634" SourceName="Microsoft-Windows-Security-Auditing" ProviderGuid="{54849625-5478-4994-A5BA-3E3B0328C30D}" Version="0" TaskValue="12545" OpcodeValue="0" RecordNumber="626878773" ExecutionProcessID="972" ExecutionThreadID="3372" Channel="Security" Message="An account was logged off.\\r\\n\\r\\nSubject:\\r\\n\\tSecurity ID:\\t\\tS-1-5-8\\r\\n\\tAccount Name:\\t\\tSYSTEM\\r\\n\\tAccount Domain:\\t\\tNT AUTHORITY\\r\\n\\tLogon ID:\\t\\t0x16864C4700\\r\\n\\r\\nLogon Type:\\t\\t\\t9\\r\\n\\r\\nThis event is generated when a logon session is destroyed. It may be positively correlated with a logon event using the Logon ID value. Logon IDs are only unique between reboots on the same computer." Category="Logoff" Opcode="Info" TargetUserSid="S-1-5-8" TargetUserName="SYSTEM" TargetDomainName="NT AUTHORITY" TargetLogonId="0x16864c4796" LogonType="9"
SYSLOG + JSON
<13>Jun 14 19: 39: 47 198.51.100.0 {
  "System": {
    "EventId": "4732",
    "Version": "0",
    "Channel": "Security",
    "ProviderName": "Microsoft-Windows-Security-Auditing",
    "Computer": "test2.dummy.rootdom.net",
    "EventRecordID": "166582496306",
    "Keywords": "AuditSuccess",
    "Level": "Information",
    "Opcode": "Info",
    "Task": "Security Group Management",
    "ProcessID": "1376",
    "ThreadID": "17824",
    "TimeCreated": "1718393972191",
    "UserId": ""
  },
  "EventData": {
    "MemberName": "CN=dummyuser,OU=Users,OU=WWC,OU=OEs,DC=dummy,DC=rootdom,DC=net",
    "MemberSid": "dummy\\\\\\\\dummyuser",
    "TargetUserName": "test-R",
    "TargetDomainName": "dummy",
    "TargetSid": "dummy\\\\\\\\test-R",
    "SubjectUserSid": "dummy\\\\\\\\giamprod_dummy",
    "SubjectUserName": "giamprod_dummy",
    "SubjectDomainName": "dummy",
    "SubjectLogonId": "0x16c425c7d",
    "PrivilegeList": "-"
  }
}
SYSLOG + XML
Dec 17 12: 59: 03 ip-10-128-38-42.ec2.internal dummyhostname <Event xmlns='http: //schemas.microsoft.com/win/2004/08/events/event'><System><Provider Name='Microsoft-Windows-Security-Auditing' Guid='{54849625-5478-4994-a5ba-3e3b0328c30d}'/><EventID>4725</EventID><Version>0</Version><Level>0</Level><Task>13824</Task><Opcode>0</Opcode><Keywords>0x8020000000000000</Keywords><TimeCreated SystemTime='2024-12-17T17:59:03.129507500Z'/><EventRecordID>205924930</EventRecordID><Correlation/><Execution ProcessID='832' ThreadID='3212'/><Channel>Security</Channel><Computer>CSP53A248TFDC.tracfone.wireless.ad</Computer><Security/></System><EventData><Data Name='TargetUserName'>dummyusername$</Data><Data Name='TargetDomainName'>dummydomain</Data><Data Name='TargetSid'>S-1-5-21-2887399753-3339080456-141373822-30323</Data><Data Name='SubjectUserSid'>S-1-5-21-117005476-2051826104-1982612992-47671</Data><Data Name='SubjectUserName'>dummy-user</Data><Data Name='SubjectDomainName'>TOPP_TELECOM</Data><Data Name='SubjectLogonId'>0x11eacfdc</Data></EventData></Event>
Field mapping reference: Common device event fields to UDM fields
The following fields are common across multiple Event IDs and are mapped the
same way.
NXLog field
UDM field
EventTime
metadata.event_timestamp
Hostname
principal.hostname
principal.asset.hostname
EventID
product_event_type
is set to "%{EventID}"
security_result.rule_name
is set to "EventID: %{EventID}"
SourceName
metadata.product_name
is set to "%25%7BSourceName}"
metadata.vendor_name
is set to "Microsoft"
Category
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Channel
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Severity
Values mapped to
security_result.severity
field as follows:
Original value
0 (None)
, is set to
UNKNOWN_SEVERITY
Original value
1 (Critical)
is set to
INFORMATIONAL
Original value
2 (Error)
is set to
ERROR
Original value
3 (Warning)
is set to
ERROR
Original value
4 (Informational)
is set to
INFORMATIONAL
Original value
5 (Verbose)
is set to
INFORMATIONAL
UserID
principal.user.windows_sid
ExecutionProcessID
principal.process.pid
ProcessID
principal.process.pid
ProviderGuid
metadata.product_deployment_id
RecordNumber
metadata.product_log_id
SourceModuleName
observer.labels.key/value
additional.fields.key
additional.fields.value.string_value
SourceModuleType
observer.application
Opcode
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Keywords
additional.fields.key
additional.fields.value.string_value
ActivityID
security_result.detection_fields.key/value
Message
additional.fields.key
additional.fields.value.string_value
HostIP
intermediary.ip
Field mapping reference: device event field to UDM field by EventID
The following section describes how NXlog/EventViewer fields are mapped
to UDM fields. Data may be mapped differently for different Microsoft Windows Event IDs.
The section heading identifies the Event Id, plus version (e.g. version 0) and 
operatiing system (e.g. Microsoft Windows 10 client) if applicable. There may be more 
than one section for an Event ID when the map for a specific version or
operating system is different.
Event ID 0
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Provider: gupdate
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: hcmon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target_resource_name set to target.resource.name
Provider: edgeupdate
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Event ID 1
Provider: Microsoft-Windows-FilterManager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
FinalStatus
Data/FinalStatus
security_result.summary
Format:
FinalStatus- %{FinalStatus}
DeviceVersionMajor
Data/DeviceVersionMajor
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceVersionMinor
Data/DeviceVersionMinor
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceNameLength
Data/DeviceNameLength
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceName
Data/DeviceNameLength
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceTime
Data/DeviceTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
version 0 / Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
version 1 / Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Reason
Data/Reason
security_result.description
ProcessName
Data/ProcessName
principal.process.command_line
ProcessID
Data/ProcessID
principal.process.pid
NewTime
Data/NewTime
additional.fields.key
additional.fields.value_string
OldTime
Data/OldTime
additional.fields.key
additional.fields.value_string
version 3 / Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
NewTime
Data/NewTime
additional.fields.key
additional.fields.value_string
OldTime
Data/OldTime
additional.fields.key
additional.fields.value_string
CmosTime
Data/CmosTime
additional.fields.key
additional.fields.value_string
TimeZoneBias
Data/TimeZoneBias
additional.fields.key
additional.fields.value_string
RealTimeIsUniversal
Data/RealTimeIsUniversal
additional.fields.key
additional.fields.value_string
SystemInCmosMode
Data/SystemInCmosMode
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Sysmon
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_LAUNCH
If
EventLevelName
contains "Information" then
security_result.severity
= INFORMATIONAL
EventData.Hashes
Based on Hash algorithm.
MD5 set to
target.process.file.md5
SHA256 set to
target.process.file.sha256
SHA1 set to
target.process.file.sha1
EventData.User
Domain set to
principal.administrative_domain
Username set to
principal.user.userid
Description
metadata.description
CommandLine
target.process.command_line
Image
target.process.file.full_path
ParentCommandLine
target.process.parent_process.command_line
ParentImage
target.process.parent_process.file.full_path
ParentProcessId
target.process.parent_process.pid
ProcessId
target.process.pid
EventOriginId
target.process.product_specific_process_id
set to "sysmon:%{EventOriginId}"
Provider: SecurityCenter
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
SourceName
Not available
target.application
Provider: telegraf
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data
security_result.description
ERROR_EVT_UNRESOLVED
security_result.detection_fields.key
security_result.detection_fields.value
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Context
Data/Context
security_result.description
hr
Data/hr
additional.fields.key
additional.fields.value_string
ErrorParam1
Data/ErrorParam1
additional.fields.key
additional.fields.value_string
ErrorParam2
Data/ErrorParam2
additional.fields.key
additional.fields.value_string
ErrorParam3
Data/ErrorParam3
additional.fields.key
additional.fields.value_string
ErrorParam4
Data/ErrorParam4
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
JobGuid
additional.fields.key
additional.fields.value_string
Title
target.resource.name
Event ID 2
Provider: MEIx64
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Provider: SecurityCenter
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
SourceName
Not available
target.application
Provider: vmci
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Provider: Microsoft-Windows-WHEA-Logger
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
RawData
Data/RawData
additional.fields.key
additional.fields.value_string
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
JobGuid
additional.fields.key
additional.fields.value_string
Title
target.resource.name
Event ID 3
version 3 / Provider: Microsoft-Windows-Power-Troubleshooter
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_STARTUP
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
SleepTime
Data/SleepTime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeTime
Data/WakeTime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeSourceType
Data/WakeSourceType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeSourceText
Data/WakeSourceText
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SleepDuration
Data/SleepDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeDuration
Data/WakeDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DriverInitDuration
Data/DriverInitDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
BiosInitDuration
Data/BiosInitDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HiberWriteDuration
Data/HiberWriteDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HiberReadDuration
Data/HiberReadDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HiberPagesWritten
Data/HiberPagesWritten
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Attributes
Data/Attributes
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TargetState
Data/TargetState
target.resource.attribute.labels.key
target.resource.attribute.labels.value
EffectiveState
Data/EffectiveState
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeSourceTextLength
Data/WakeSourceTextLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeTimerOwnerLength
Data/WakeTimerOwnerLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeTimerContextLength
Data/WakeTimerContextLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NoMultiStageResumeReason
Data/NoMultiStageResumeReason
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeTimerOwner
Data/WakeTimerOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
WakeTimerContext
Data/WakeTimerContext
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CheckpointDuration
Data/CheckpointDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Provider: Microsoft-Windows-Security-Kerberos
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = FAIL
File
target.file.full_path
ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
ErrorMessage
security_result.description
ServerRealm
target.administrative_domain
ServerName
target.hostname
TargetName
target.domain.name
Line
security_result.detection_fields.key
security_result.detection_fields.value
Provider: Virtual Disk Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Provider: vmci
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobTitle
target.resource.name
processPath
target.process.file.full_path
jobId
target.resource.product_object_id
jobOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
processId
target.process.pid
ClientProcessStartKey
additional.fields.key
additional.fields.value_string
Event ID 4
Provider: Microsoft-Windows-Security-Kerberos
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = FAIL
Server
target.hostname
TargetRealm
target.domain.name
Targetname
target.application
ClientRealm
principal.domain.name
Provider: Virtual Disk Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
name
target.resource.name
Id
target.resource.product_object_id
url
target.url
fileLength
target.file.size
jobOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
processId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClientProcessStartKey
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5
Provider: iScsiPrt
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Provider: McAfee Service Controller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Microsoft-Windows-Search-ProfileNotify
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
SourceName
target.application
User
Data/User
target.user.userid
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
User
principal.user.userid
Title
target.resource.name
Id
target.resource.product_object_id
Owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
fileCount
additional.fields.key
additional.fields.value_string
processId
target.process.pid
ClientProcessStartKey
additional.fields.key
additional.fields.value_string
Event ID 6
Provider: Microsoft-Windows-CertificateServicesClient-AutoEnrollment
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
%{ErrorCode}-%{ErrorMsg}
ErrorMsg
security_result.summary
Format:
%{ErrorCode}-%{ErrorMsg}
Context
target.application
Provider: Microsoft-Windows-FilterManager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
FinalStatus
Data/FinalStatus
security_result.summary
Format:
FinalStatus- %{FinalStatus}
DeviceVersionMajor
Data/DeviceVersionMajor
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceVersionMinor
Data/DeviceVersionMinor
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceNameLength
Data/DeviceNameLength
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceName
Data/DeviceNameLength
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DeviceTime
Data/DeviceTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Name
additional.fields.key
additional.fields.value_string
Value
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobId
target.resource.product_object_id
jobOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
program
target.resource.attribute.labels.key
target.resource.attribute.labels.value
parameters
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 7
Provider: AdmPwd
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Format:
"Error: %{Data}"
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Name
additional.fields.key
additional.fields.value_string
Value
additional.fields.key
additional.fields.value_string
Event ID 8
Provider: CylanceSvc
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Provider: WSH
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data_1
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
Data_2
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
Data_3
principal.process.command_line
Message
metadata.description
Event ID 9
Provider: volsnap
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
VolumeName
target.file.full_path
NTSTATUS
additional.fields.key
additional.fields.value_string
SourceTag
additional.fields.key
additional.fields.value_string
SourceFileID
additional.fields.key
additional.fields.value_string
SourceLine
additional.fields.key
additional.fields.value_string
Event ID 10
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Index
Data/Index
additional.fields.key
additional.fields.value_string
CLS
Data/CLS
additional.fields.key
additional.fields.value_string
INS
Data/INS
additional.fields.key
additional.fields.value_string
P1
Data/P1
additional.fields.key
additional.fields.value_string
P2
Data/P2
additional.fields.key
additional.fields.value_string
Lc
Data/Lc
additional.fields.key
additional.fields.value_string
Le
Data/Le
additional.fields.key
additional.fields.value_string
.NETServiceMethod
Data/.NETServiceMethod
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 11
Provider: Microsoft-Windows-Hyper-V-Netvsc
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
MiniportName
target.resource.name
AccountType
principal.user.attribute.roles.name
MiniportNameLen
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ExtraStringLength
Data/ExtraStringLength
additional.fields.key
additional.fields.value_string
ExtraString
Data/ExtraString
additional.fields.key
additional.fields.value_string
TmId
Data/TmId
additional.fields.key
additional.fields.value_string
RmId
Data/RmId
additional.fields.key
additional.fields.value_string
Status
Data/Status
additional.fields.key
additional.fields.value_string
InternalCode
Data/InternalCode
additional.fields.key
additional.fields.value_string
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Error
Data/Error
security_result.summary
is set to "ErrorCode: %{Error}"
MessageType
Data/MessageType
additional.fields.key
additional.fields.value_string
ICCStatus
Data/ICCStatus
additional.fields.key
additional.fields.value_string
CmdStatus
Data/CmdStatus
additional.fields.key
additional.fields.value_string
SW1
Data/SW1
additional.fields.key
additional.fields.value_string
SW2
Data/SW2
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Wininit
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
StringCount
EventData.StringCount
additional.fields.key
additional.fields.value_string
String
EventData.String
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 12
Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_STARTUP
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
MajorVersion
Data/MajorVersion
target.asset.attribute.labels.key
target.asset.attribute.labels.value
MinorVersion
Data/MinorVersion
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BuildVersion
Data/BuildVersion
target.asset.attribute.labels.key
target.asset.attribute.labels.value
QfeVersion
Data/QfeVersion
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ServiceVersion
Data/ServiceVersion
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BootMode
Data/BootMode
target.asset.attribute.labels.key
target.asset.attribute.labels.value
StartTime
Data/StartTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Provider: Microsoft-Windows-Sysmon
NXLog field
Event Viewer field
UDM field
metadata.event_type = REGISTRY_CREATION
If EventLevelName =~ "Information" then security_result.severity = INFORMATIONAL
EventOriginId
target.process.product_specific_process_id
set to "sysmon: %{EventOriginId}"
EventData/EventType
target.registry.registry_key
EventData/TargetObject
target.registry.registry_value_name
ProcessId
principal.process.pid
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: Microsoft-Windows-UserModePowerService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ProcessPath
target.process.file.full_path
NewSchemeGuid
target.resource.product_object_id
OldSchemeGuid
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProcessPid
target.process.pid
Provider: Microsoft-Windows-EnhancedStorage-EhStorTcgDrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Capabilities
EventData.Capabilities
additional.fields.key
additional.fields.value_string
KeyProtectionMechanism
EventData.KeyProtectionMechanism
additional.fields.key
additional.fields.value_string
MaxBandCount
EventData.MaxBandCount
additional.fields.key
additional.fields.value_string
BandMetadataSize
EventData.BandMetadataSize
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 13
Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_SHUTDOWN
StopTime
Data/StopTime
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Sysmon
NXLog field
Event Viewer field
UDM field
metadata.event_type = REGISTRY_MODIFICATION
If EventLevelName =~ "Information" then security_result.severity = INFORMATIONAL
ProcessId
principal.process.pid
EventOriginId
target.process.product_specific_process_id
set to "sysmon: %{EventOriginId}"
EventData/EventType
target.registry.registry_key
EventData/Details
target.registry.registry_value_data
Provider: Microsoft-Windows-CertificateServicesClient-CertEnroll
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
principal.administrative_domain
AccountName
principal.user.userid
AccountType
principal.user.attribute.roles.name
Message
metadata.description
UserID
principal.user.windows_sid
CA
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
ErrorCode
security_result.summary
Format:
security_result.summary
is set to %{error_code} - %{error_message}
Context
principal.user.attribute.labels.key
principal.user.attribute.labels.value
TemplateName
additional.fields.key
additional.fields.value_string
RequestId
principal.user.attribute.labels.key
principal.user.attribute.labels.value
Provider: NPS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
target.ip
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 14
Provider: Microsoft-Windows-Kerberos-Key-Distribution-Center
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
security_result.action = FAIL
ClientName
principal.asset.attribute.labels.key/value
Target
target.application
Account
target.hostname
ID
additional.fields.key
additional.fields.value_string
RequestedEtypes
additional.fields.key
additional.fields.value_string
AvailableEtypes
additional.fields.key
additional.fields.value_string
AccountToReset
principal.user.userid
Provider: Microsoft-Windows-Wininit
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Config
Data/Config
additional.fields.key
additional.fields.value_string
IsTestConfig
Data/IsTestConfig
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Error
Data/Error
security_result.description
Format:
Error - %{value}
Provider:TPM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
UserID
Security/UseID
principal.user.windows_sid
locationCode
Data/locationCode
additional.fields.key
additional.fields.value_string
Data
Data/Data
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 15
Provider: Disk
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_hostname set to target.hostname
Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = REGISTRY_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
NewSize
Data/NewSize
target.file.size
HiveName
Data/HiveName
target.registry.registry_key
AccountType
principal.user.attribute.roles.name
HiveNameLength
Data/HiveNameLength
additional.fields.key
additional.fields.value_string
OriginalSize
Data/OriginalSize
additional.fields.key
additional.fields.value_string
Provider: SecurityCenter
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Provider:TPM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
UserID
Security/UseID
principal.user.windows_sid
locationCode
Data/locationCode
additional.fields.key
additional.fields.value_string
Data
Data/Data
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 16
Provider: Microsoft-Windows-HAL
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: Microsoft-Windows-Kerberos-Key-Distribution-Center
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
security_result.action = FAIL
ClientName
principal.asset.attribute.labels.key/value
Target
target.application
Account
target.hostname
ID
additional.fields.key
additional.fields.value_string
RequestedEtypes
additional.fields.key
additional.fields.value_string
AvailableEtypes
additional.fields.key
additional.fields.value_string
AccountToReset
principal.user.userid
Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = REGISTRY_MODIFICATION
Domain
System/Domain
principal.administrative_domain
ProcessID
System/ProcessID
principal.process.pid
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
HiveName
Data/HiveName
target.registry.registry_key
AccountType
principal.user.attribute.roles.name
HiveNameLength
Data/HiveNameLength
additional.fields.key
additional.fields.value_string
KeysUpdated
Data/KeysUpdated
additional.fields.key
additional.fields.value_string
DirtyPages
Data/DirtyPages
additional.fields.key
additional.fields.value_string
HiveNameLength
Data/HiveNameLength
additional.fields.key
additional.fields.value_string
KeysUpdated
Data/KeysUpdated
additional.fields.key
additional.fields.value_string
DirtyPages
DirtyPages
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
metadata.description
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
version 0 / Provider: Microsoft-Windows-HAL
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 17
Provider: Microsoft-Windows-WHEA-Logger
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorSource
Data/ErrorSource
security_result.detection_fields.key
security_result.detection_fields.value
FRUId
Data/FRUId
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
FRUText
Data/FRUText
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
ValidBits
Data/ValidBits
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
PortType
Data/PortType
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Version
Data/Version
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Command
Data/Command
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Status
Data/Status
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Bus
Data/Bus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Device
Data/Device
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Function
Data/Function
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Segment
Data/Segment
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryBus
Data/SecondaryBus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryDevice
Data/SecondaryDevice
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryFunction
Data/SecondaryFunction
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
VendorID
Data/VendorID
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
DeviceID
Data/DeviceID
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
ClassCode
Data/ClassCode
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
DeviceSerialNumber
Data/DeviceSerialNumber
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
BridgeControl
Data/BridgeControl
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
BridgeStatus
Data/BridgeStatus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
UncorrectableErrorStatus
Data/UncorrectableErrorStatus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
CorrectableErrorStatus
Data/CorrectableErrorStatus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
HeaderLog
Data/HeaderLog
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
PrimaryDeviceName
Data/PrimaryDeviceName
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryDeviceName
Data/SecondaryDeviceName
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Category set to
security_result.category_details
Message
set to
metadata.description
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
peerCacheEnabled
additional.fields.key
additional.fields.value_string
peerClientEnabled
additional.fields.key
additional.fields.value_string
peerServerEnabled
additional.fields.key
additional.fields.value_string
maxPeers
additional.fields.key
additional.fields.value_string
maxClients
additional.fields.key
additional.fields.value_string
maxContentAge
additional.fields.key
additional.fields.value_string
maxCacheSize
additional.fields.key
additional.fields.value_string
minCacheDiskSize
additional.fields.key
additional.fields.value_string
cacheDenyUrls
about.url
denyUrlCount
additional.fields.key
additional.fields.value_string
denyUrls
additional.fields.key
additional.fields.value_string
Event ID 18
Provider: BTHUSB
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
EntryCount
Data/EntryCount
additional.fields.key
additional.fields.value_string
Provider: TPM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
locationCode
Data/locationCode
additional.fields.key
additional.fields.value_string
Data
Data/Data
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
packet
additional.fields.key
additional.fields.value_string
hr
additional.fields.key
additional.fields.value_string
fqdn
about.administrative_domain
sourceAddress
additional.fields.key
additional.fields.value_string
addressCount
additional.fields.key
additional.fields.value_string
addresses
additional.fields.key
additional.fields.value_string
Event ID 19
version 0 / Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Category
Data/Category
security_result.category_details
updateGuid
Data/updateGuid
additional.fields.key
additional.fields.value_string
updateRevisionNumber
Data/updateRevisionNumber
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
serviceGuid
Data/serviceGuid
additional.fields.key
additional.fields.value_string
Provider: Intel-SST-OED
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
Category
security_result.summary
status
security_result.detection_fields.key
security_result.detection_fields.value
Provider: Microsoft-Windows-WHEA-Logger
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
ErrorSource
Data/ErrorSource
security_result.detection_fields.key
security_result.detection_fields.value
ApicId
Data/ApicId
additional.fields.key
additional.fields.value_string
MCABank
Data/MCABank
additional.fields.key
additional.fields.value_string
MciStat
Data/MciStat
additional.fields.key
additional.fields.value_string
MciAddr
Data/MciAddr
additional.fields.key
additional.fields.value_string
MciMisc
Data/MciMisc
additional.fields.key
additional.fields.value_string
ErrorType
Data/ErrorType
security_result.detection_fields.key
security_result.detection_fields.value
TransactionType
Data/TransactionType
security_result.detection_fields.key
security_result.detection_fields.value
Participation
Data/Participation
additional.fields.key
additional.fields.value_string
RequestType
Data/RequestType
security_result.detection_fields.key
security_result.detection_fields.value
MemorIO
Data/MemorIO
additional.fields.key
additional.fields.value_string
MemHierarchyLvl
Data/MemHierarchyLvl
additional.fields.key
additional.fields.value_string
Timeout
Data/Timeout
security_result.detection_fields.key
security_result.detection_fields.value
OperationType
Data/OperationType
additional.fields.key
additional.fields.value_string
Channel
Data/Channel
additional.fields.key
additional.fields.value_string
Length
Data/Length
additional.fields.key
additional.fields.value_string
RawData
Data/RawData
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
fqdn
about.administrative_domain
authenticated
additional.fields.key
additional.fields.value_string
online
additional.fields.key
additional.fields.value_string
addressCount
additional.fields.key
additional.fields.value_string
addressLength
additional.fields.key
additional.fields.value_string
Event ID 20
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
Path
Data/Path
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
LastShutdownGood
Data/LastShutdownGood
additional.fields.key
additional.fields.value_string
LastBootGood
Data/LastBootGood
additional.fields.key
additional.fields.value_string
LastBootId
Data/LastBootId
additional.fields.key
additional.fields.value_string
BootStatusPolicy
Data/BootStatusPolicy
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
updateRevisionNumber
target.resource.attribute.labels.key
target.resource.attribute.labels.value
updateTitle
target.resource.name
updateGuid
target.resource.product_object_id
errorCode
security_result.detection_fields.key
security_result.detection_fields.value
serviceGuid
additional.fields.key
additional.fields.value_string
Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
UpdateReason
Data/UpdateReason
security_result.detection_fields.key
security_result.detection_fields.value
EnabledNew
Data/EnabledNew
additional.fields.key
additional.fields.value_string
CountNew
Data/CountNew
additional.fields.key
additional.fields.value_string
CountOld
Data/CountOld
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
fqdn
about.administrative_domain
authenticated
additional.fields.key
additional.fields.value_string
online
additional.fields.key
additional.fields.value_string
addressCount
additional.fields.key
additional.fields.value_string
addressLength
additional.fields.key
additional.fields.value_string
Event ID 21
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
ConfigProperty
Data/ConfigProperty
security_result.detection_fields.key
security_result.detection_fields.value
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
fqdn
about.administrative_domain
authenticated
additional.fields.key
additional.fields.value_string
online
additional.fields.key
additional.fields.value_string
addressCount
additional.fields.key
additional.fields.value_string
addressLength
additional.fields.key
additional.fields.value_string
Event ID 22
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
Path
Data/Path
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Category set to
security_result.category_details
Message
set to
metadata.description
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
updatelist
security_result.description
restarttime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Provider: Microsoft-Windows-UserModePowerService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Turn
Data/Turn
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
fqdn
about.administrative_domain
authenticated
additional.fields.key
additional.fields.value_string
online
additional.fields.key
additional.fields.value_string
addressCount
additional.fields.key
additional.fields.value_string
addressLength
additional.fields.key
additional.fields.value_string
Event ID 23
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
Path
Data/Path
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kerberos-Key-Distribution-Center
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
security_result.action = FAIL
Type
security_result.detection_fields.key
security_result.detection_fields.value
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
user
about.user.windows_sid
Event ID 24
Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
ExitReason
Data/ExitReason
security_result.detection_fields.key
security_result.detection_fields.value
CurrentBias
Data/CurrentBias
additional.fields.key
additional.fields.value_string
CurrentTimeZoneID
Data/CurrentTimeZoneID
additional.fields.key
additional.fields.value_string
TimeZoneInfoCacheUpdated
Data/TimeZoneInfoCacheUpdated
additional.fields.key
additional.fields.value_string
FirstRefresh
Data/FirstRefresh
additional.fields.key
additional.fields.value_string
version 0 / Provider: Microsoft-Windows-Kernel-General
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ExitReason
Data/ExitReason
security_result.detection_fields.key
security_result.detection_fields.value
CurrentBias
Data/CurrentBias
additional.fields.key
additional.fields.value_string
CurrentTimeZoneID
Data/CurrentTimeZoneID
additional.fields.key
additional.fields.value_string
TimeZoneInfoCacheUpdated
Data/TimeZoneInfoCacheUpdated
additional.fields.key
additional.fields.value_string
FirstRefresh
Data/FirstRefresh
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ErrorMessage
Data/ErrorMessage
security_result.description
DomainPeer
Data/DomainPeer
target.administrative_domain
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Provider:TPM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
UserID
Security/UseID
principal.user.windows_sid
locationCode
Data/locationCode
additional.fields.key
additional.fields.value_string
Data
Data/Data
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
sourceAddress
additional.fields.key
additional.fields.value_string
Event ID 25
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
BootMenuPolicy
Data/BootMenuPolicy
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
sourceAddress
additional.fields.key
additional.fields.value_string
packet
additional.fields.key
additional.fields.value_string
hr
additional.fields.key
additional.fields.value_string
Event ID 26
Provider: Application Popup
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Caption
security_result.summary
Provider: Microsoft-Windows-CertificationAuthority
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application = "Active Directory Certificate Services"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DCName
Data/DCName
target.administrative_domain
CACommonName
Data/CACommonName
target.user.userid
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
DCSpecifier
Data/DCSpecifier
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kerberos-Key-Distribution-Center
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = FAIL
Target
target.hostname
Name
target.user.userid
ID
additional.fields.key
additional.fields.value_string
RequestedEtypes
additional.fields.key
additional.fields.value_string
AvailableETypes
additional.fields.key
additional.fields.value_string
Event ID 27
version 0 / Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
NewLogFilePath
Data/NewLogFilePath
target.file.full_path
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
FailedLogFilePath
Data/FailedLogFilePath
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
BootType
Data/BootType
additional.fields.key
additional.fields.value_string
LoadOptions
Data/LoadOptions
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
metadata.description
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
searchId
security_result.detection_fields
jobId
target.resource.product_object_id
url
target.url
timestamp
additional.fields.key
additional.fields.value_string
Event ID 28
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
metadata.description
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
searchId
security_result.detection_fields
jobId
target.resource.product_object_id
Event ID 29
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
requestId
additional.fields.key
additional.fields.value_string
searchId
security_result.detection_fields
peer
additional.fields.key
additional.fields.value_string
Event ID 30
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ResetEndStart
Data/ResetEndStart
additional.fields.key
additional.fields.value_string
LoadOSImageStart
Data/LoadOSImageStart
additional.fields.key
additional.fields.value_string
StartOSImageStart
Data/StartOSImageStart
additional.fields.key
additional.fields.value_string
ExitBootServicesEntry
Data/ExitBootServicesEntry
additional.fields.key
additional.fields.value_string
ExitBootServicesExit
Data/ExitBootServicesExit
additional.fields.key
additional.fields.value_string
Provider: TPM
NXLog field
Event Viewer field
UDM field
locationCode
Data/locationCode
additional.fields.key
additional.fields.value_string
resetCountBefore
Data/resetCountBefore
additional.fields.key
additional.fields.value_string
restartCountBefore
Data/restartCountBefore
additional.fields.key
additional.fields.value_string
resetCountAfter
Data/resetCountAfter
additional.fields.key
additional.fields.value_string
restartCountAfter
Data/restartCountAfter
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
requestId
additional.fields.key
additional.fields.value_string
SearchId
security_result.detection_fields
hr
additional.fields.key
additional.fields.value_string
Event ID 31
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
requestId
additional.fields.key
additional.fields.value_string
SearchId
security_result.detection_fields
hr
additional.fields.key
additional.fields.value_string
Event ID 32
Provider: e1iexpress
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
BitlockerUserInputTime
Data/BitlockerUserInputTime
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
requestId
additional.fields.key
additional.fields.value_string
id
target.resource.product_object_id
url
target.url
rangecount
additional.fields.key
additional.fields.value_string
Range.offset
additional.fields.key
additional.fields.value_string
Range.length
additional.fields.key
additional.fields.value_string
Event ID 33
Provider: volsnap
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_UNCATEGORIZED
VolumeName
target.file.full_path
DeviceName
target.resource.name
NTSTATUS
additional.fields.key
additional.fields.value_string
SourceTag
additional.fields.key
additional.fields.value_string
SourceFileID
additional.fields.key
additional.fields.value_string
SourceLine
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
count
additional.fields.key
additional.fields.value_string
addresses
target.ip
Event ID 34
Provider: Oracle.xstore
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_READ
DBID
additional.fields.key/value
ProcessId
principal.process.pid
SourceName
principal.application
DATABASE_USER
principal.user.uerid
ACTION
target.process.command_line
USERHOST
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobName
target.resource.name
jobId
target.resource.product_object_id
FileCount
additional.fields.key
additional.fields.value_string
jobTransferPolicy
security_result.rule_labels.key
security_result.rule_labels.value
globalTransferPolicy
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 35
Provider: Microsoft-Windows-Kerberos-Key-Distribution-Center
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
security_result.action = FAIL
IssuingKDC
Data/IssuingKDC
observer.asset.asset_id
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
TimeSource
Data/TimeSource
security_result.detection_fields.key
security_result.detection_fields.value
TimeSourceRefId
Data/TimeSourceRefId
security_result.detection_fields.key
security_result.detection_fields.value
CurrentStratumNumber
Data/CurrentStratumNumber
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 36
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
UnsynchronizedTimeSeconds
Data/UnsynchronizedTimeSeconds
security_result.detection_fields.key
security_result.detection_fields.value
TimeRemainingToSetLocalClockFreeRunningSeconds
Data/TimeRemainingToSetLocalClockFreeRunningSeconds
security_result.detection_fields.key
security_result.detection_fields.value
Provider: NPS
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Message
Ip set to target.ip
Event ID 37
Provider: Microsoft-Windows-Kerberos-Key-Distribution-Center
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
security_result.action = FAIL
ClientName
principal.asset.attribute.labels.key/value
ServerName
target.hostname
IssuingKDC
additional.fields.key
additional.fields.value_string
ClientRealm
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Provider: Microsoft-Windows-Kernel-Processor-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Number
Data/Number
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CapDurationInSeconds
Data/CapDurationInSeconds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Group
Data/Group
target.group.attribute.labels.key
target.group.attribute.labels.value
PpcChanges
Data/PpcChanges
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TpcChanges
Data/TpcChanges
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PccChanges
Data/PccChanges
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
TimeSource
Data/TimeSource
security_result.detection_fields.key
security_result.detection_fields.value
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
nlmCost
additional.fields.key
additional.fields.value_string
usage
additional.fields.key
additional.fields.value_string
cap
additional.fields.key
additional.fields.value_string
isThrottled
additional.fields.key
additional.fields.value_string
isOvercap
additional.fields.key
additional.fields.value_string
isRoaming
additional.fields.key
additional.fields.value_string
globalTransferPolicy
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 38
Provider: Microsoft-Windows-CertificationAuthority
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "Active Directory Certificate Services"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
CACommonName
Data/CACommonName
target.user.userid
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 40
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ChannelPath
Data/ChannelPath
additional.fields.key
additional.fields.value_string
Event ID 41
version 8 / Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
BugcheckCode
Data/BugcheckCode
additional.fields.key
additional.fields.value_string
BugcheckParameter1
Data/BugcheckParameter1
additional.fields.key
additional.fields.value_string
BugcheckParameter2
Data/BugcheckParameter2
additional.fields.key
additional.fields.value_string
BugcheckParameter3
Data/BugcheckParameter3
additional.fields.key
additional.fields.value_string
BugcheckParameter4
Data/BugcheckParameter4
additional.fields.key
additional.fields.value_string
SleepInProgress
Data/SleepInProgress
additional.fields.key
additional.fields.value_string
PowerButtonTimestamp
Data/PowerButtonTimestamp
additional.fields.key
additional.fields.value_string
BootAppStatus
Data/BootAppStatus
additional.fields.key
additional.fields.value_string
Checkpoint
Data/Checkpoint
additional.fields.key
additional.fields.value_string
ConnectedStandbyInProgress
Data/ConnectedStandbyInProgress
additional.fields.key
additional.fields.value_string
SystemSleepTransitionsToOn
Data/SystemSleepTransitionsToOn
additional.fields.key
additional.fields.value_string
CsEntryScenarioInstanceId
Data/CsEntryScenarioInstanceId
additional.fields.key
additional.fields.value_string
BugcheckInfoFromEFI
Data/BugcheckInfoFromEFI
additional.fields.key
additional.fields.value_string
CheckpointStatus
Data/CheckpointStatus
additional.fields.key
additional.fields.value_string
CsEntryScenarioInstanceIdV2
Data/CsEntryScenarioInstanceIdV2
additional.fields.key
additional.fields.value_string
LongPowerButtonPressDetected
Data/LongPowerButtonPressDetected
additional.fields.key
additional.fields.value_string
Event ID 42
version 0 Windows 10 client / Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
TargetState
Data/TargetState
additional.fields.key
additional.fields.value_string
EffectiveState
Data/EffectiveState
additional.fields.key
additional.fields.value_string
version 2 Windows 10 client /
NXLog field
Event Viewer field
UDM field
Reason
Data/Reason
security_result.description
Flags
Data/Flags
additional.fields.key
additional.fields.value_string
version 3 Windows 10 client /
NXLog field
Event Viewer field
UDM field
TransitionsToOn
Data/TransitionsToOn
additional.fields.key
additional.fields.value_string
Event ID 43
Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
updateRevisionNumber
Data/updateRevisionNumber
target.resource.attribute.labels.key
target.resource.attribute.labels.value
updateTitle
Data/updateTitle
target.resource.name
updateGuid
Data/updateGuid
target.resource.product_object_id
Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 44
version 0 Windows 10 client / Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
AccountType
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
Category
Data/Category
security_result.category_details
updateGuid
Data/updateGuid
additional.fields.key
additional.fields.value_string
updateRevisionNumber
Data/updateRevisionNumber
additional.fields.key
additional.fields.value_string
version 1 Windows 10 client / Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
updateTitle
Data/updateTitle
additional.fields.key
additional.fields.value_string
Event ID 45
Provider: Symantec AntiVirus
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
Data
security_result.summary
Event ID 47
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorMessage
security_result.description
ManualPeer
target.ip
Provider: Microsoft-Windows-WHEA-Logger
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorSource
Data/ErrorSource
security_result.detection_fields.key
security_result.detection_fields.value
FRUId
Data/FRUId
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
FRUText
Data/FRUText
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
ValidBits
Data/ValidBits
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
PortType
Data/PortType
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Version
Data/Version
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Command
Data/Command
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Status
Data/Status
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Bus
Data/Bus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Device
Data/Device
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Function
Data/Function
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Segment
Data/Segment
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryBus
Data/SecondaryBus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryDevice
Data/SecondaryDevice
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryFunction
Data/SecondaryFunction
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
VendorID
Data/VendorID
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
DeviceID
Data/DeviceID
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
ClassCode
Data/ClassCode
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
DeviceSerialNumber
Data/DeviceSerialNumber
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
BridgeControl
Data/BridgeControl
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
BridgeStatus
Data/BridgeStatus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
UncorrectableErrorStatus
Data/UncorrectableErrorStatus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
CorrectableErrorStatus
Data/CorrectableErrorStatus
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
HeaderLog
Data/HeaderLog
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
PrimaryDeviceName
Data/PrimaryDeviceName
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
SecondaryDeviceName
Data/SecondaryDeviceName
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Event ID 49
Provider: Microsoft-Windows-Hyper-V-Netvsc
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Status
Data/Status
security_result.summary
Event ID 50
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
TimeDifferenceMilliseconds
Data/TimeDifferenceMilliseconds
security_result.detection_fields.key
security_result.detection_fields.value
TimeSampleSeconds
Data/TimeSampleSeconds
security_result.detection_fields.key
security_result.detection_fields.value
Provider: Ntfs
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 51
Provider: Disk
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_hostname set to target.hostname
Event ID 55
version 0 Windows 10 client / Provider: Microsoft-Windows-Kernel-Processor-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Group
Data/Group
additional.fields.key
additional.fields.value_string
Number
Data/Number
additional.fields.key
additional.fields.value_string
IdleStateCount
Data/IdleStateCount
additional.fields.key
additional.fields.value_string
IdleImplementation
Data/IdleImplementation
additional.fields.key
additional.fields.value_string
NominalFrequency
Data/NominalFrequency
additional.fields.key
additional.fields.value_string
MaximumPerformancePercent
Data/MaximumPerformancePercent
additional.fields.key
additional.fields.value_string
MinimumPerformancePercent
Data/MinimumPerformancePercent
additional.fields.key
additional.fields.value_string
MinimumThrottlePercent
Data/MinimumThrottlePercent
additional.fields.key
additional.fields.value_string
PerformanceImplementation
Data/PerformanceImplementation
additional.fields.key
additional.fields.value_string
version 1 Windows 10 client / Provider: Microsoft-Windows-Kernel-Processor-Power
NXLog field
Event Viewer field
UDM field
ProgrammedWakeTimeAc
Data/ProgrammedWakeTimeAc
additional.fields.key
additional.fields.value_string
Provider: Ntfs
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Outcome
security_result.summary
DriveName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DeviceName
target.resource.name
CorruptionState
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HeaderFlags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Origin
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Verb
observer.labels.key
observer.labels.value
Description
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Signature
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SampleLength
additional.fields.key
additional.fields.value_string
SourceFile
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SourceLine
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SourceTag
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AdditionalInfo
additional.fields.key
additional.fields.value_string
CallStack
additional.fields.key
additional.fields.value_string
Event ID 57
Provider: hpqilo3
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 58
Provider: partmgr
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
metadata.description
Provider: volsnap
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
metadata.description
Event ID 59
Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
name
target.resource.name
Id
target.resource.product_object_id
url
target.url
fileLength
target.file.size
transferId
additional.fields.key
additional.fields.value_string
peer
additional.fields.key
additional.fields.value_string
hr
additional.fields.key
additional.fields.value_string
fileTime
additional.fields.key
additional.fields.value_string
bytesTotal
additional.fields.key
additional.fields.value_string
bytesTransferred
additional.fields.key
additional.fields.value_string
proxy
additional.fields.key
additional.fields.value_string
peerProtocolFlags
additional.fields.key
additional.fields.value_string
bytesTransferredFromPeer
additional.fields.key
additional.fields.value_string
AdditionalInfoHr
additional.fields.key
additional.fields.value_string
PeerContextInfo
additional.fields.key
additional.fields.value_string
bandwidthLimit
additional.fields.key
additional.fields.value_string
ignoreBandwidthLimitsOnLan
additional.fields.key
additional.fields.value_string
Event ID 60
Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
name
target.resource.name
url
target.url
fileLength
target.file.size
transferId
additional.fields.key
additional.fields.value_string
peer
additional.fields.key
additional.fields.value_string
hr
additional.fields.key
additional.fields.value_string
fileTime
additional.fields.key
additional.fields.value_string
bytesTotal
additional.fields.key
additional.fields.value_string
bytesTransferred
additional.fields.key
additional.fields.value_string
proxy
additional.fields.key
additional.fields.value_string
peerProtocolFlags
additional.fields.key
additional.fields.value_string
bytesTransferredFromPeer
additional.fields.key
additional.fields.value_string
AdditionalInfoHr
additional.fields.key
additional.fields.value_string
PeerContextInfo
additional.fields.key
additional.fields.value_string
bandwidthLimit
additional.fields.key
additional.fields.value_string
ignoreBandwidthLimitsOnLan
additional.fields.key
additional.fields.value_string
Event ID 61
Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
name
target.resource.name
Id
target.resource.product_object_id
url
target.url
fileLength
target.file.size
transferId
additional.fields.key
additional.fields.value_string
peer
additional.fields.key
additional.fields.value_string
hr
additional.fields.key
additional.fields.value_string
fileTime
additional.fields.key
additional.fields.value_string
bytesTotal
additional.fields.key
additional.fields.value_string
bytesTransferred
additional.fields.key
additional.fields.value_string
proxy
additional.fields.key
additional.fields.value_string
peerProtocolFlags
additional.fields.key
additional.fields.value_string
bytesTransferredFromPeer
additional.fields.key
additional.fields.value_string
AdditionalInfoHr
additional.fields.key
additional.fields.value_string
PeerContextInfo
additional.fields.key
additional.fields.value_string
bandwidthLimit
additional.fields.key
additional.fields.value_string
ignoreBandwidthLimitsOnLan
additional.fields.key
additional.fields.value_string
Event ID 64
Provider: Microsoft-Windows-CertificateServicesClient-AutoEnrollment
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Context
target.application
ObjId
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Job
target.resource.name
Url
target.url
Pgm
target.application
hr
security_result.summary
Format:
hr - %{hr}
Event ID 75
Provider: Microsoft-Windows-CertificationAuthority
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application set to "Active Directory Certificate Services"
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
ErrorMessageText
security_result.summary
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
CAKeyIdentifier
additional.fields.key
additional.fields.value_string
URL
additional.fields.key
additional.fields.value_string
AdditionalErrorMessage
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 77
Provider: Microsoft-Windows-CertificationAuthority
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application set to "Active Directory Certificate Services"
WarningMessage
security_result.description
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Opcode
additional.fields.key
additional.fields.value_string
PolicyModuleDescription
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 80
Provider: ocz10xx
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data
target.hostname
Data_1
additional.fields.key
additional.fields.value_string
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 81
Provider: hpqilo2
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-FailoverClustering-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
Parameter1
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 98
Provider: Microsoft-Windows-Ntfs
NXLog field
Event Viewer field
UDM field
metadata.event_type =  STATUS_HEARTBEAT
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
DeviceName
Data/DeviceName
principal.hostname
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DriveName
Data/DriveName
additional.fields.key
additional.fields.value_string
CorruptionActionState
Data/CorruptionActionState
security_result.summary
Format:
CorruptionActionState- %{CorruptionActionState}
Event ID 100
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
EventID
Data/EventID
additional.fields.key
additional.fields.value_string
PubID
Data/PubID
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_ENABLE
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
TaskName
Data/TaskName
target.resource.name
InstanceId
Data/InstanceId
target.resource.product_object_id
UserContext
target.user.user_display_name
Provider: Microsoft-Windows-EnhancedStorage-EhStorTcgDrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Context
additional.fields.key
additional.fields.value_string
Param1
additional.fields.key
additional.fields.value_string
Param2
additional.fields.key
additional.fields.value_string
Param3
additional.fields.key
additional.fields.value_string
Param4
additional.fields.key
additional.fields.value_string
Event ID 101
Provider: Application Management Group Policy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.description" set to "ErrorCode - %{error_code}"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
requestId
additional.fields.key
additional.fields.value_string
responseXml
additional.fields.key
additional.fields.value_string
Event ID 102
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Message
Extract PID and map it to UDM field
target.process.pid
Category
Data/Category
security_result.category_details
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ProcessID
Data/ProcessID
principal.process.pid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
EventID
Data/EventID
additional.fields.key
additional.fields.value_string
PublisherName
Data/PublisherName
additional.fields.key
additional.fields.value_string
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.description
TaskName
Data/TaskName
target.resource.name
InstanceId
Data/InstanceId
target.resource.product_object_id
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
xferId
additional.fields.key
additional.fields.value_string
count
additional.fields.key
additional.fields.value_string
ranges.offset
additional.fields.key
additional.fields.value_string
ranges.length
additional.fields.key
additional.fields.value_string
Event ID 103
Provider: Application Management Group Policy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.description" set to "ErrorCode - %{error_code}"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Message
System/Message
Extract PID and map it to UDM field
target.process.pid
Category
Data/Category
security_result.category_details
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Reason
Data/Reason
security_result.description
SessionName
Data/SessionName
additional.fields.key
additional.fields.value_string
Provider: ocz10xx
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data
target.hostname
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 104
Windows 10 client / Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_WIPE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
Message
metadata.description
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
LogFileCleared.SubjectUserName
LogFileCleared /SubjectUserName
about.user.userid
LogFileCleared.SubjectDomainName
LogFileCleared /SubjectDomainName
about.administrative_domain
LogFileCleared.Channel
LogFileCleared /Channel
additional.fields.key
additional.fields.value_string
LogFileCleared.BackupPath
LogFileCleared /BackupPath
about.file.full_path
Windows Server 2019 /
NXLog field
Event Viewer field
UDM field
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
LogFileCleared.SubjectUserName
Data/LogFileCleared /SubjectUserName
about.user.userid
LogFileCleared.SubjectDomainName
Data/LogFileCleared /SubjectDomainName
about.administrative_domain
LogFileCleared.Channel
Data/LogFileCleared /Channel
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Forwarding
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
UserID
System/UserID
principal.user.windows_sid
SubscriptionManagerAddress
Data/SubscriptionManagerAddress
target.url
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
ErrorMessage
Data/ErrorMessage
security_result.description
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
bcdCCID
target.asset.attribute.labels.key
target.asset.attribute.labels.value
bMaxSlotIndex
target.asset.attribute.labels.key
target.asset.attribute.labels.value
bVoltageSupport
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwProtocols
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwDefaultClock
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwMaximumClock
target.asset.attribute.labels.key
target.asset.attribute.labels.value
bNumClockSupported
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwDataRate
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwMaxDataRate
target.asset.attribute.labels.key
target.asset.attribute.labels.value
bNumDataRateSupported
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwMaxIFSD
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwSyncProtocols
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwMechanical
target.asset.attribute.labels.key
target.asset.attribute.labels.value
dwFeatures
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Event ID 105
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Channel
Data/Channel
security_result.description
BackupPath
Data/BackupPath
target.file.full_path
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
AcOnline
target.asset.attribute.labels.key
target.asset.attribute.labels.value
RemainingCapacity
target.asset.attribute.labels.key
target.asset.attribute.labels.value
FullChargeCapacity
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Provider: VMTools
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
SourceName
Not available
target.application
Provider: WudfUsbccidDriver
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
dwMaxCCIDMessageLength
additional.fields.key
additional.fields.value_string
bClassGetResponse
additional.fields.key
additional.fields.value_string
bClassGetEnvelope
additional.fields.key
additional.fields.value_string
wLcdLayout
additional.fields.key
additional.fields.value_string
bPINSupport
additional.fields.key
additional.fields.value_string
bMaxCCIDBusySlots
additional.fields.key
additional.fields.value_string
Event ID 106
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Channel
Data/Channel
additional.fields.key
additional.fields.value_string
Event ID 107
version 0 Windows 10 client / Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
TargetState
Data/TargetState
additional.fields.key
additional.fields.value_string
EffectiveState
Data/EffectiveState
additional.fields.key
additional.fields.value_string
WakeFromState
Data/WakeFromState
additional.fields.key
additional.fields.value_string
version 1 Windows 10 client / Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
ProgrammedWakeTimeAc
Data/ProgrammedWakeTimeAc
additional.fields.key
additional.fields.value_string
ProgrammedWakeTimeDc
Data/ProgrammedWakeTimeDc
additional.fields.key
additional.fields.value_string
WakeRequesterTypeAc
Data/WakeRequesterTypeAc
additional.fields.key
additional.fields.value_string
WakeRequesterTypeDc
Data/WakeRequesterTypeDc
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
ProviderName
Data/ProviderName
additional.fields.key
additional.fields.value_string
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_ENABLE
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
TaskName
Data/TaskName
target.resource.name
InstanceId
Data/InstanceId
target.resource.product_object_id
Event ID 108
Provider: Application Management Group Policy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.description" set to "ErrorCode - %{error_code}"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ShutdownTime
Data/ShutdownTime
additional.fields.key
additional.fields.value_string
ActualMaxInterval
Data/ActualMaxInterval
additional.fields.key
additional.fields.value_string
DiskPmDisabledMaxInterval
Data/DiskPmDisabledMaxInterval
additional.fields.key
additional.fields.value_string
DiskPmEnabledFlag
Data/DiskPmEnabledFlag
additional.fields.key
additional.fields.value_string
DiskPmEnabledMaxInterval
Data/DiskPmEnabledMaxInterval
additional.fields.key
additional.fields.value_string
TimestampForced
Data/TimestampForced
additional.fields.key
additional.fields.value_string
DiskPmPolicy
Data/DiskPmPolicy
additional.fields.key
additional.fields.value_string
BiasValid
Data/BiasValid
additional.fields.key
additional.fields.value_string
StartBias
Data/StartBias
additional.fields.key
additional.fields.value_string
Provider: VMTools
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
SourceName
Not available
target.application
Event ID 109
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ProcessID
Data/ProcessID
principal.process.pid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
EventID
Data/EventID
additional.fields.key
additional.fields.value_string
PublisherName
Data/PublisherName
additional.fields.key
additional.fields.value_string
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
EventName
Data/EventName
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_SHUTDOWN
ShutdownReason
Data/ShutdownReason
security_result.description
ShutdownActionType
Data/ShutdownActionType
security_result.detection_fields.key
security_result.detection_fields.value
ShutdownEventCode
Data/ShutdownEventCode
security_result.summary
Format:
ShutdownEventCode- %{ShutdownEventCode}
Event ID 110
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
PublisherName
Data/PublisherName
additional.fields.key
additional.fields.value_string
Event ID 111
version 0/ Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
PublisherName
Data/PublisherName
additional.fields.key
additional.fields.value_string
EventMetaDataCount
Data/EventMetaDataCount
additional.fields.key
additional.fields.value_string
version 0/ Provider: Microsoft-Windows-AppReadiness
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Result
Data/Result
security_result.summary
Event ID 112
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
PublisherName
Data/PublisherName
additional.fields.key
additional.fields.value_string
ErrorCode
Data/ErrorCode
additional.fields.key
additional.fields.value_string
Event ID 115
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Event ID 129
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_ENABLE
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
Priority
Data/Priority
security_result.priority_details
Path
Data/Path
target.process.file.full_path
ProcessID
Data/ProcessID
target.process.pid
TaskName
Data/TaskName
target.resource.name
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorMessage
Data/ErrorMessage
security_result.description
AccountType
System/AccountType
principal.user.attribute.roles.name
RetryMinutes
Data/RetryMinutes
additional.fields.key
additional.fields.value_string
Event ID 130
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ErrorMessage
Data/ErrorMessage
security_result.description
DomainPeer
Data/DomainPeer
target.administrative_domain
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
RetryMinutes
Data/RetryMinutes
additional.fields.key
additional.fields.value_string
Event ID 131
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorMessage
Data/ErrorMessage
security_result.description
DomainPeer
Data/DomainPeer
target.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
RetryMinutes
Data/RetryMinutes
additional.fields.key
additional.fields.value_string
Event ID 132
Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
principal.administrative_domain
AccountName
principal.user.userid
AccountType
principal.user.attribute.roles.name
operationName
additional.fields.key
additional.fields.value_string
Event ID 134
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorMessage
Data/ErrorMessage
security_result.description
DomainPeer
Data/DomainPeer
target.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
RetryMinutes
Data/RetryMinutes
additional.fields.key
additional.fields.value_string
Event ID 137
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Ntfs
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 138
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DomainPeer
Data/DomainPeer
target.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 139
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 140
Provider: Microsoft-Windows-Ntfs
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
DeviceName
principal.hostname
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
VolumeId
additional.fields.key
additional.fields.value_string
Error
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_MODIFICATION
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
TaskName
Data/TaskName
target.resource.name
UserName
Data/UserName
target.user..user_display_name
Event ID 142
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Message
set to
security_result.summary
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
errorCode
security_result.summary
Domain
principal.administrative_domain
AccountName
principal.user.userid
AccountType
principal.user.attribute.roles.name
AccountName
additional.fields.key
additional.fields.value_string
Event ID 143
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 145
Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
resourceUrl
target.url
AccountName
principal.user.userid
AccountType
principal.user.attribute.roles.name
Domain
principal.administrative_domain
operationName
additional.fields.key
additional.fields.value_string
Event ID 146
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Message
set to
security_result.summary
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ChainingCountRequests
additional.fields.key
additional.fields.value_string
ChainLoggingRate
additional.fields.key
additional.fields.value_string
ChainingCountSuccess
additional.fields.key
additional.fields.value_string
ChainingCountFailure
additional.fields.key
additional.fields.value_string
Event ID 150
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 153
Provider: Disk
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Status
Data/Status
additional.fields.key
additional.fields.value_string
EnableDisableReason
Data/EnableDisableReason
security_result.detection_fields.key
security_result.detection_fields.value
VsmPolicy
Data/VsmPolicy
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 156
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
NotAffectedRdclNo
Data/NotAffectedRdclNo
additional.fields.key
additional.fields.value_string
NotAffectedAtom
Data/NotAffectedAtom
additional.fields.key
additional.fields.value_string
CacheFlushSupported
Data/CacheFlushSupported
additional.fields.key
additional.fields.value_string
SmtEnabled
Data/SmtEnabled
additional.fields.key
additional.fields.value_string
ParentHypervisorFlushes
Data/ParentHypervisorFlushes
additional.fields.key
additional.fields.value_string
DisabledLoadOption
Data/DisabledLoadOption
additional.fields.key
additional.fields.value_string
Enabled
Data/Enabled
additional.fields.key
additional.fields.value_string
CacheFlushNeeded
Data/CacheFlushNeeded
additional.fields.key
additional.fields.value_string
Event ID 157
Provider: disk
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 158
Provider: Disk
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
target_url set to target.url
Provider: Microsoft-Windows-Time-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
TimeProvider
target.resource.name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Culture
additional.fields.key
additional.fields.value_string
Level
security_result.detection_fields.key
security_result.detection_fields.value
Provider
additional.fields.key
additional.fields.value_string
Event ID 159
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 160
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 161
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Event ID 163
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Processor
Data/Processor
additional.fields.key
additional.fields.value_string
Event ID 164
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Processor
Data/Processor
additional.fields.key
additional.fields.value_string
Event ID 165
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
NotAffectedMdsNo
Data/NotAffectedMdsNo
additional.fields.key
additional.fields.value_string
NotAffectedAtom
Data/NotAffectedAtom
additional.fields.key
additional.fields.value_string
MdClearSupported
Data/MdClearSupported
additional.fields.key
additional.fields.value_string
BufferFlushNeeded
Data/BufferFlushNeeded
additional.fields.key
additional.fields.value_string
Event ID 167
Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 169
Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Status
Data/Status
security_result.summary
version 1 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Status
Data/Status
additional.fields.key
additional.fields.value_string
FailurePoint
Data/FailurePoint
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 170
Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 171
version 0 / Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Version
Data/Version/
principal.asset.software.version
Event ID 172
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Reason
Data/Reason
security_result.description
AccountType
principal.user.attribute.roles.name
State
Data/State
security_result.detection_fields.key
security_result.detection_fields.value
State
Data/State
additional.fields.key
additional.fields.value_string
version 0 / Provider: Microsoft-Windows-Kernel-Processor-Power
NXLog field
Event Viewer field
UDM field
RegisterId
Data/RegisterId
additional.fields.key
additional.fields.value_string
ParameterId
Data/ParameterId
additional.fields.key
additional.fields.value_string
BitWidth
Data/BitWidth
additional.fields.key
additional.fields.value_string
BitOffset
Data/BitOffset
additional.fields.key
additional.fields.value_string
Type
Data/Type
additional.fields.key
additional.fields.value_string
NameLength
Data/NameLength
additional.fields.key
additional.fields.value_string
Name
Data/Name
additional.fields.key
additional.fields.value_string
Event ID 173
Provider: Microsoft-Windows-Hyper-V-Hypervisor
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Event ID 181
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = status_update
Status
Data/Status
security_result.summary
Event ID 182
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 183
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 185
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Status
Data/Status
security_result.summary
Event ID 187
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ApiCallerName
principal.process.file.full_path
ApiCallerNameLength
additional.fields.key
additional.fields.value_string
SystemAction
about.resource.attribute.labels.key
about.resource.attribute.labels.value
LightestSystemState
about.resource.attribute.labels.key
about.resource.attribute.labels.value
Event ID 195
Provider: Microsoft-Windows-USB-USBHUB3
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
fid_UsbDevice
target.resource.name
fid_DripsWatchdogResult
target.resource.attribute.labels.key
target.resource.attribute.labels.value
fid_idVendor
target.resource.attribute.labels.key
target.resource.attribute.labels.value
fid_idProduct
target.resource.product_object_id
fid_bcdDevice
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 196
Provider: Microsoft-Windows-USB-USBHUB3
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
fid_UsbDevice
target.resource.name
fid_DripsWatchdogResult
target.resource.attribute.labels.key
target.resource.attribute.labels.value
fid_idVendor
target.resource.attribute.labels.key
target.resource.attribute.labels.value
fid_idProduct
target.resource.product_object_id
fid_bcdDevice
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 200
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ChannelName
Data/ChannelName
additional.fields.key
additional.fields.value_string
ChannelType
Data/ChannelType
additional.fields.key
additional.fields.value_string
Enabled
Data/Enabled
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_ENABLE
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
TaskName
Data/TaskName
target.resource.name
TaskInstanceId
Data/TaskInstanceId
target.resource.product_object_id
ActionName
Data/ActionName
security_result.action_details
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
url
target.url
hr
security_result.summary
Format:
hr - %{hr}
proxy
additional.fields.key
additional.fields.value_string
job
target.resource.name
owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
jobId
target.resource.product_object_id
xferId
additional.fields.key
additional.fields.value_string
proxyServerList
additional.fields.key
additional.fields.value_string
Event ID 201
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ChannelName
Data/ChannelName
additional.fields.key
additional.fields.value_string
Query
Data/Query
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
TaskName
Data/TaskName
target.resource.name
TaskInstanceId
Data/TaskInstanceId
target.resource.product_object_id
ActionName
Data/ActionName
security_result.action_details
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
job
target.resource.name
jobId
target.resource.product_object_id
jobOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
url
target.url
transferId
additional.fields.key
additional.fields.value_string
proxyServerList
additional.fields.key
additional.fields.value_string
proxyBypassList
additional.fields.key
additional.fields.value_string
error
security_result.summary
Format:
error- %{error}
Event ID 202
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ChannelName
Data/ChannelName
additional.fields.key
additional.fields.value_string
Query
Data/Query
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobName
target.resource.name
jobOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
jobId
target.resource.product_object_id
url
target.url
xferId
additional.fields.key
additional.fields.value_string
proxy
additional.fields.key
additional.fields.value_string
hr
security_result.summary
Format:
hr - %{hr}
fileLength
target.url_metadata.last_http_response_content_length
HTTPVersion
additional.fields.key
additional.fields.value_string
URLRange
additional.fields.key
additional.fields.value_string
Event ID 203
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ModuleNameLen
Data/ModuleNameLen
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ModuleName
Data/ModuleName
target.resource.name
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
string
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
string2
target.resource.name
string3
target.url
version 1 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
server
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
job
target.resource.name
url
target.url
scheme
additional.fields.key
additional.fields.value_string
user
target.user.userid
Event ID 204
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ModuleNameLen
Data/ModuleNameLen
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ModuleName
Data/ModuleName
target.resource.name
Provider: Microsoft-Windows-Security-Kerberos
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = FAIL
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
string
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
string2
target.resource.name
string3
target.url
version 1 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
server
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
job
target.resource.name
url
target.url
scheme
additional.fields.key
additional.fields.value_string
user
target.user.userid
Event ID 205
version 0 Windows Server 2019 / Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ModuleNameLen
Data/ModuleNameLen
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ModuleName
Data/ModuleName
target.resource.name
version 1 / Windows 10 client /
NXLog field
Event Viewer field
UDM field
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
DomainName
Data/DomainName
target.administrative_domain
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
DomainSid
Data/DomainSid
target.user.windows_sid
TdoType
Data/TdoType
security_result.detection_fields.key
security_result.detection_fields.value
TdoDirection
Data/TdoDirection
security_result.detection_fields.key
security_result.detection_fields.value
TdoAttributes
Data/TdoAttributes
security_result.detection_fields.key
security_result.detection_fields.value
SidFilteringEnabled
Data/SidFilteringEnabled
security_result.detection_fields.key
security_result.detection_fields.value
version 2 / Windows 10 client /
NXLog field
Event Viewer field
UDM field
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
DomainName
Data/DomainName
target.administrative_domain
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
DomainSid
Data/DomainSid
target.user.windows_sid
TdoType
Data/TdoType
security_result.detection_fields.key
security_result.detection_fields.value
TdoDirection
Data/TdoDirection
security_result.detection_fields.key
security_result.detection_fields.value
TdoAttributes
Data/TdoAttributes
security_result.detection_fields.key
security_result.detection_fields.value
SidFilteringEnabled
Data/SidFilteringEnabled
security_result.detection_fields.key
security_result.detection_fields.value
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
profileType
target.user.attribute.labels.key
target.user.attribute.labels.value
currSlotStartTime
additional.fields.key
additional.fields.value_string
currSlotBandwidthLimit
additional.fields.key
additional.fields.value_string
nextSlotStartTime
additional.fields.key
additional.fields.value_string
nextSlotBandwidthLimit
additional.fields.key
additional.fields.value_string
Event ID 216
version 1 / Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
version 1 / Provider: Microsoft-Windows-TerminalServices-RemoteConnectionManager
NXLog field
Event Viewer field
UDM field
updateTitle
Data/updateTitle
target.resource.name
updateGuid
Data/updateGuid
target.resource.product_object_id
updateRevisionNumber
Data/updateRevisionNumber
target.resource.attribute.labels.key
target.resource.attribute.labels.value
serviceGuid
Data/serviceGuid
additional.fields.key
additional.fields.value_string
Event ID 219
Provider: Microsoft-Windows-Kernel-PnP
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DriverName
target.hostname
FailureName
target.resource.name
DriverNameLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Status
additional.fields.key
additional.fields.value_string
FailureNameLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 218
version 0 / Provider: Microsoft-Windows-WindowsUpdateClient
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
updateTitle
Data/updateTitle
target.resource.name
updateGuid
Data/updateGuid
target.resource.product_object_id
updateRevisionNumber
Data/updateRevisionNumber
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 221
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 225
Provider: Microsoft-Windows-Kernel-PnP
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DeviceInstance
target.hostname
ProcessName
target.process.file.full_path
ProcessNameLength
additional.fields.key
additional.fields.value_string
DeviceInstanceLength
additional.fields.key
additional.fields.value_string
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 228
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 229
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 230
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 233
Provider: Microsoft-Windows-Hyper-V-VmSwitch
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
NicNameLen
additional.fields.key
additional.fields.value_string
NicName
additional.fields.key
additional.fields.value_string
NicFNameLen
additional.fields.key
additional.fields.value_string
NicFName
additional.fields.key
additional.fields.value_string
Operation
additional.fields.key
additional.fields.value_string
Event ID 231
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Code
Data/Code
security_result.summary
set to "Code - %{Code}"
KeyType
Data/KeyType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 234
Provider: Microsoft-Windows-Hyper-V-VmSwitch
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
NicNameLen
additional.fields.key
additional.fields.value_string
NicName
additional.fields.key
additional.fields.value_string
PortNameLen
additional.fields.key
additional.fields.value_string
Event ID 238
Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
System/Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
EfiTimeZoneBias
Data/EfiTimeZoneBias
additional.fields.key
additional.fields.value_string
EfiDaylightFlags
Data/EfiDaylightFlags
additional.fields.key
additional.fields.value_string
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
version 1 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
EfiTimeZoneBias
Data/EfiTimeZoneBias
additional.fields.key
additional.fields.value_string
EfiDaylightFlags
Data/EfiDaylightFlags
additional.fields.key
additional.fields.value_string
EfiTime
Data/EfiTime
additional.fields.key
additional.fields.value_string
EfiTimeZoneBias
Data/EfiTimeZoneBias
additional.fields.key
additional.fields.value_string
EfiDaylightFlags
Data/EfiDaylightFlags
additional.fields.key
additional.fields.value_string
EfiTime
Data/EfiTime
additional.fields.key
additional.fields.value_string
Event ID 241
version 0 / Provider: Microsoft-Windows-Kernel-Boot
NXLog field
Event Viewer field
UDM field
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 258
Provider: VMUpgradeHelper
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
SourceName
Not available
target.application
Event ID 260
Provider: VMUpgradeHelper
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
SourceName
Not available
target.application
Event ID 263
version 0 / Provider: Microsoft-Windows-TerminalServices-RemoteConnectionManager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
Event ID 271
Provider: VMUpgradeHelper
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
SourceName
Not available
target.application
Event ID 272
Provider: VMUpgradeHelper
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
SourceName
Not available
target.application
Event ID 299
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 300
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID and map it to
target.process.pid
Category
Data/Category
security_result.category_details
Event ID 301
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID and map it to
target.process.pid
Category
Data/Category
security_result.category_details
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 302
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID and map it to
target.process.pid
Category
Data/Category
security_result.category_details
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 304
version 0 / Provider: Microsoft-Windows-Ntfs
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Status
Data/Status
security_result.summary
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 313
version 0 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ErrorCode
Data/ErrorCode
security_result.summary
is set to "ErrorCode: %{ErrorCode}"
Event ID 325
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID and map it
target.process.pid
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
QueuedTaskInstanceId
target.resource.product_object_id
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Category
Data/Category
security_result.category_details
Event ID 326
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID and map it to
target.process.pid
Category
Data/Category
security_result.category_details
Event ID 400
Provider: PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data_2
Extract HostName from Data_2
HostName is set to target.hostname
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
version 1 /Provider: PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
NewEngineState
additional.fields.key
additional.fields.value.string_value
PreviousEngineState
additional.fields.key
additional.fields.value.string_value
HostName
additional.fields.key
additional.fields.value.string_value
HostVersion
additional.fields.key
additional.fields.value.string_value
HostId
additional.fields.key
additional.fields.value.string_value
HostApplication
principal.process.command_line
EngineVersion
additional.fields.key
additional.fields.value.string_value
RunspaceId
additional.fields.key
additional.fields.value.string_value
PipelineId
additional.fields.key
additional.fields.value.string_value
CommandName
additional.fields.key
additional.fields.value.string_value
CommandType
additional.fields.key
additional.fields.value.string_value
ScriptName
target.file.name
CommandPath
target.process.file.full_path
NewEngineState
target.process.command_line
Event ID 403
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
Data_9
network.http.user_agent
Domain
System/Domain
principal.administrative_domain
Data_8
principal.ip
Data_7
principal.port
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Data_3
target.ip
Data_5
target.url
Data
target.resource.product_object_id
Data_1
additional.fields.key
additional.fields.value_string
Data_2
metadata.event_timestamp
Data_4
target.network.http.method
Data_6
additional.fields.key
additional.fields.value_string
Data_10
additional.fields.key
additional.fields.value_string
Data_11
additional.fields.key
additional.fields.value_string
Data_12
additional.fields.key
additional.fields.value_string
Data_13
additional.fields.key
additional.fields.value_string
Data_14
additional.fields.key
additional.fields.value_string
Data_15
additional.fields.key
additional.fields.value_string
Event ID 404
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Data_3
security_description set to %{Data_3}: %{Data_4}
Data_4
security_description set to %{Data_3}: %{Data_4}
Data
target.resource.product_object_id
Data_1
additional.fields.key
additional.fields.value_string
Data_2
metadata.event_timestamp
Event ID 405
Provider: ADSync
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
principal.administrative_domain
Data_1
principal.user.userid
Event ID 410
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
Data_4
network.http.user_agent
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Data_10
target.ip
Data_8
target.url
Data
additional.fields.key
additional.fields.value_string
Data_2
additional.fields.key
additional.fields.value_string
Data_6
additional.fields.key
additional.fields.value_string
Data_12
additional.fields.key
additional.fields.value_string
Data_14
additional.fields.key
additional.fields.value_string
Event ID 412
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 424
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
client_certificate_serial set to network.tls.client.certificate.serial
client_certificate_subject set to network.tls.client.certificate.subject
security_result.action = FAIL
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 500
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 501
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 506
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.description
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
LidOpenState
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ExternalMonitorConnectedState
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScenarioInstanceId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BatteryRemainingCapacityOnEnter
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BatteryFullChargeCapacityOnEnter
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScenarioInstanceIdV2
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BootId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Event ID 507
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
reason_description set to security_result.description
Domain
System/Domain
principal.administrative_domain
Reason
security_result.description
AccountName
System/AccountName
principal.user.userid
EnergyDrain
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ActiveResidencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonDripsTimeActivatedInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
FirstDripsEntryInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DripsResidencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DripsTransitions
target.asset.attribute.labels.key
target.asset.attribute.labels.value
FullChargeCapacityRatio
target.asset.attribute.labels.key
target.asset.attribute.labels.value
AudioPlaying
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Reason
security_result.detection_fields.key
security_result.detection_fields.value
AudioPlaybackInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonActivatedCpuInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PowerStateAc
target.asset.attribute.labels.key
target.asset.attribute.labels.value
HwDripsResidencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ExitLatencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DisconnectedStandby
target.asset.attribute.labels.key
target.asset.attribute.labels.value
AoAcCompliantNic
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonAttributedCpuInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ModernSleepEnabledActionsBitmask
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ModernSleepAppliedActionsBitmask
target.asset.attribute.labels.key
target.asset.attribute.labels.value
LidOpenState
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ExternalMonitorConnectedState
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScenarioInstanceId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
IsCsSessionInProgressOnExit
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BatteryRemainingCapacityOnExit
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BatteryFullChargeCapacityOnExit
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScenarioInstanceIdV2
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BootId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
InputSuppressionActionCount
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonResiliencyTimeInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ResiliencyDripsTimeInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ResiliencyHwDripsTimeInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
GdiOnTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DwmSyncFlushTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
MonitorPowerOnTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepEntered
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffDurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepDurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffFullEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffFullEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepFullEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepFullEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
version 10 / Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Reason
Data/Reason
security_result.description
EnergyDrain
Data/EnergyDrain
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ActiveResidencyInUs
Data/ActiveResidencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonDripsTimeActivatedInUs
Data/NonDripsTimeActivatedInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
FirstDripsEntryInUs
Data/FirstDripsEntryInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DripsResidencyInUs
Data/DripsResidencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DurationInUs
Data/DurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DripsTransitions
Data/DripsTransitions
target.asset.attribute.labels.key
target.asset.attribute.labels.value
FullChargeCapacityRatio
Data/FullChargeCapacityRatio
target.asset.attribute.labels.key
target.asset.attribute.labels.value
AudioPlaying
Data/AudioPlaying
target.asset.attribute.labels.key
target.asset.attribute.labels.value
AudioPlaybackInUs
Data/AudioPlaybackInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonActivatedCpuInUs
Data/NonActivatedCpuInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PowerStateAc
Data/PowerStateAc
target.asset.attribute.labels.key
target.asset.attribute.labels.value
HwDripsResidencyInUs
Data/HwDripsResidencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ExitLatencyInUs
Data/ExitLatencyInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DisconnectedStandby
Data/DisconnectedStandby
target.asset.attribute.labels.key
target.asset.attribute.labels.value
AoAcCompliantNic
Data/AoAcCompliantNic
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonAttributedCpuInUs
Data/NonAttributedCpuInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ModernSleepEnabledActionsBitmask
Data/ModernSleepEnabledActionsBitmask
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ModernSleepAppliedActionsBitmask
Data/ModernSleepAppliedActionsBitmask
target.asset.attribute.labels.key
target.asset.attribute.labels.value
LidOpenState
Data/LidOpenState
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ExternalMonitorConnectedState
Data/ExternalMonitorConnectedState
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScenarioInstanceId
Data/ScenarioInstanceId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
IsCsSessionInProgressOnExit
Data/IsCsSessionInProgressOnExit
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BatteryRemainingCapacityOnExit
Data/BatteryRemainingCapacityOnExit
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BatteryFullChargeCapacityOnExit
Data/BatteryFullChargeCapacityOnExit
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScenarioInstanceIdV2
Data/ScenarioInstanceIdV2
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BootId
Data/BootId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
InputSuppressionActionCount
Data/InputSuppressionActionCount
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NonResiliencyTimeInUs
Data/NonResiliencyTimeInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ResiliencyDripsTimeInUs
Data/ResiliencyDripsTimeInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ResiliencyHwDripsTimeInUs
Data/ResiliencyHwDripsTimeInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
GdiOnTime
Data/GdiOnTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
DwmSyncFlushTime
Data/DwmSyncFlushTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
MonitorPowerOnTime
Data/MonitorPowerOnTime
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepEntered
Data/SleepEntered
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffEnergyCapacityAtStart
Data/ScreenOffEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffEnergyCapacityAtEnd
Data/ScreenOffEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffDurationInUs
Data/ScreenOffDurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepEnergyCapacityAtStart
Data/SleepEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepEnergyCapacityAtEnd
Data/SleepEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepDurationInUs
Data/SleepDurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffFullEnergyCapacityAtStart
Data/ScreenOffFullEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
ScreenOffFullEnergyCapacityAtEnd
Data/ScreenOffFullEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepFullEnergyCapacityAtStart
Data/SleepFullEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
SleepFullEnergyCapacityAtEnd
Data/SleepFullEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PowerSchemeInfo
Data/PowerSchemeInfo
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Event ID 508
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID and map it to
target.process.pid
Category
Data/Category
security_result.category_details
Event ID 510
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
Data_1
Data_1.Host set to target.hostname
Data_1.User-Agent set to network.http.user_agent
Data_1.X-MS-Endpoint-Absolute-Path set to target.url
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Data
target.resource.product_object_id
Data_2
additional.fields.key
additional.fields.value_string
Data_3
additional.fields.key
additional.fields.value_string
Data_4
additional.fields.key
additional.fields.value_string
Data_5
additional.fields.key
additional.fields.value_string
Data_6
additional.fields.key
additional.fields.value_string
Data_7
additional.fields.key
additional.fields.value_string
Data_8
additional.fields.key
additional.fields.value_string
Data_9
additional.fields.key
additional.fields.value_string
Data_10
additional.fields.key
additional.fields.value_string
Data_11
additional.fields.key
additional.fields.value_string
Data_12
additional.fields.key
additional.fields.value_string
Data_13
additional.fields.key
additional.fields.value_string
Data_14
additional.fields.key
additional.fields.value_string
Data_15
additional.fields.key
additional.fields.value_string
Data_16
additional.fields.key
additional.fields.value_string
Data_17
additional.fields.key
additional.fields.value_string
Data_18
additional.fields.key
additional.fields.value_string
Data_19
additional.fields.key
additional.fields.value_string
Data_20
additional.fields.key
additional.fields.value_string
Event ID 517
Provider: Microsoft-Windows-DFSN-Server
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
UserID
principal.user.windows_sid
DfsNamespace
target.resource.name
SyncFromPDC
additional.fields.key
additional.fields.value_string
Status
security_result.summary
Format:
Status: %{Status}
TimeConsumedInMilliSeconds
additional.fields.key
additional.fields.value_string
Event ID 521
Provider: Security
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = FAIL
Data
security_result.detection_fields.key
security_result.detection_fields.value
Data_1
security_result.detection_fields.key
security_result.detection_fields.value
Data_2
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 529
Provider: Security
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = BLOCK
security_result.category = AUTH_VIOLATION
LogonType
Not available
extensions.auth.mechanism
Message
Not available
username set to target.user.userid
domain set to target.administrative_domain
target_workstation set to target.hostname
Event ID 566
Provider: Microsoft-Windows-Kernel-Power
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Reason
Data/Reason
security_result.description
BootId
Data/BootId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousSessionId
Data/PreviousSessionId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousSessionType
Data/PreviousSessionType
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousSessionDurationInUs
Data/PreviousSessionDurationInUs
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousEnergyCapacityAtStart
Data/PreviousEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousFullEnergyCapacityAtStart
Data/PreviousFullEnergyCapacityAtStart
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousEnergyCapacityAtEnd
Data/PreviousEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PreviousFullEnergyCapacityAtEnd
Data/PreviousFullEnergyCapacityAtEnd
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NextSessionId
Data/NextSessionId
target.asset.attribute.labels.key
target.asset.attribute.labels.value
NextSessionType
Data/NextSessionType
target.asset.attribute.labels.key
target.asset.attribute.labels.value
PowerStateAc
Data/PowerStateAc
target.asset.attribute.labels.key
target.asset.attribute.labels.value
MonitorReason
Data/MonitorReason
target.asset.attribute.labels.key
target.asset.attribute.labels.value
Event ID 600
Provider: PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Category
metadata.description
SourceName
principal.application
HostApplication
target.file.full_path
ProviderName
target.resource.name
Event ID 601
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
metadata.description = Attempt to install a service
SubjectUserName
principal.user.userid
Summary
security_result.summary
ServiceName
target.process.command_line
ServiceFileName
target.process.file.full_path
Event ID 642
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Extract PID map it to
target.process.pid
Category
Data/Category
security_result.category_details
Event ID 653
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Event ID 654
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Event ID 663
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Event ID 700
Provider: NTDS ISAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
MessageSourceAddress
principal.ip
Event ID 701
Provider: NTDS ISAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
MessageSourceAddress
principal.ip
Event ID 719
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
Category
Data/Category
security_result.category_details
Event ID 781
Provider: Microsoft-Windows-Complus
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
target.registry.registry_key
Event ID 800
Provider: PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
metadata.description set to "Pipeline execution"
security_result.summary
set to "Pipeline execution details for command line"
SourceName
principal.application
UserId
principal.user.userid
HostApplication
principal.process.command_line
DetailSequence
additional.fields.key
additional.fields.value.string_value
DetailTotal
additional.fields.key
additional.fields.value.string_value
SequenceNumber
additional.fields.key
additional.fields.value.string_value
HostName
additional.fields.key
additional.fields.value.string_value
HostVersion
additional.fields.key
additional.fields.value.string_value
HostId
additional.fields.key
additional.fields.value.string_value
EngineVersion
additional.fields.key
additional.fields.value.string_value
RunspaceId
additional.fields.key
additional.fields.value.string_value
PipelineId
additional.fields.key
additional.fields.value.string_value
ScriptName
target.file.full_path
CommandLine
target.process.command_line
Details
additional.fields.key
additional.fields.value.string_value
Event ID 888
Provider: top_5
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 900
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = SERVICE_START
target.application = "Software Protection"
Event ID 902
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = SERVICE_START
target.application = "Software Protection"
Event ID 903
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = SERVICE_STOP
target.application = "Software Protection"
Event ID 904
Provider: Directory Synchronization
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.summary
Event ID 1000
Provider: Microsoft-Windows-SCPNP
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ReaderName
Data/ReaderName
target.resource.name
ErrorCode
Data/ErrorCode
security_result.summary
is set to "ErrorCode: %{ErrorCode}"
Provider: Microsoft-Windows-LoadPerf
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
AccountName
principal.user.attribute.roles.name
AccountType
principal.user.attribute.roles.description
UserID
principal.user.windows_sid
Provider: Application Error
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
Extracted
FaultingApplicationPath
and
FaultingModulePath
fields from the
Message
log field and mapped it to
additional.fields.key
additional.fields.value.string_value
FaultingModulePath
additional.fields.key
additional.fields.value_string
FaultingApplicationPath
additional.fields.key
additional.fields.value_string
Event ID 1001
Provider: Microsoft Antimalware
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
target_resource_product_object_id set to target.resource.product_object_id
Provider: Microsoft-Windows-WER-SystemErrorReporting
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
param2
target.file.full_path
param1
additional.fields.key
additional.fields.value_string
param3
additional.fields.key
additional.fields.value_string
Provider: SNMP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Provider: Windows Error Reporting
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-LoadPerf
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
AccountName
principal.user.attribute.roles.name
AccountType
principal.user.attribute.roles.description
UserID
principal.user.windows_sid
Event ID 1003
Provider: Microsoft-Windows-Search
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Category
Data/Category
target.application
ExtraInfo
Data/ExtraInfo
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 1004
Provider: IPMIDRV
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data
target.hostname
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Search
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
Reason
Data/Reason
security_result.description
Category
Data/Category
target.application
ExtraInfo
Data/ExtraInfo
additional.fields.key
additional.fields.value_string
Provider: SNMP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: TdIca
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_ip set to target.ip
target_port set to target_port
EventData
additional.fields.key
additional.fields.value_string
Event ID 1005
Provider: Microsoft-Windows-Search
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
Category
Data/Category
target.application
ExtraInfo
Data/ExtraInfo
additional.fields.key
additional.fields.value_string
Event ID 1007
Provider: TdIca
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_ip set to target.ip
target_port set to target_port
Event ID 1008
Provider: Microsoft-Windows-Perflib
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
EventXML.param1
target.application
EventXML.param2
target.file.full_path
EventXML.binaryDataSize
additional.fields.key
additional.fields.value_string
EventXML.binaryData
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Search
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Reason
Data/Reason
security_result.description
Category
Data/Category
target.application
ExtraInfo
Data/ExtraInfo
additional.fields.key
additional.fields.value_string
Event ID 1010
Provider: Microsoft-Windows-Search
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
Category
Data/Category
target.application
ExtraInfo
Data/ExtraInfo
additional.fields.key
additional.fields.value_string
Event ID 1013
Provider: Microsoft-Windows-Search
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
Category
Data/Category
target.application
ExtraInfo
Data/ExtraInfo
additional.fields.key
additional.fields.value_string
Event ID 1014
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_DNS
network.ip_protocol is set to "DNS"
QueryName
network.dns.questions.name
AddressLength
additional.fields.key
additional.fields.value_string
Address
additional.fields.key
additional.fields.value_string
Event ID 1016
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 1023
Provider: Microsoft-Windows-Perflib
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Library
Data/Library
target.file.full_path
Win32Error
Data/Win32Error
security_result.summary
Format:
Win32Error - %{Win32Error}
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 1025
Provider: Microsoft-Windows-TPM-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 1026
Provider: Microsoft-Windows-TPM-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ErrorCode
Data/ErrorCode
security_result.summary
is set to "ErrorCode: %{ErrorCode}
Status Information
Data/Status Information
additional.fields.key
additional.fields.value_string
Event ID 1027
Provider: Microsoft-Windows-TPM-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 1030
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
security_result.description
ErrorCode
security_result.summary
Format:
ErrorCode - %{ErrorCode}
DCName
target.administrative_domain
SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ProcessingMode
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-Kernel-PnP
NXLog field
Event Viewer field
UDM field
metadata.event_type =  SYSTEM_AUDIT_LOG_UNCATEGORIZED
Device
Data/Device
target.hostname
Event ID 1031
Provider: Microsoft-Windows-Kernel-PnP
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Device
Data/Device
target.hostname
Event ID 1033
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Extract product_name and map to target.application
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 1034
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 1037
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 1040
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Extract process_id and map it to
target.process.pid
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 1042
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Extract process_id and map it to
target.process.pid
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 1053
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
Data/ErrorDescription
security_result.description
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 1054
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
Data/ErrorDescription
security_result.description
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 1055
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
Data/ErrorDescription
security_result.description
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{ErrorCode}
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
Event ID 1056
Provider: Microsoft-Windows-TerminalServices-RemoteConnectionManager
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
server_certificate_subject set to network.tls.server.certificate.subject
security_result.action = ALLOW
Event ID 1057
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target.resource_resource_type = DATABASE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
EventData
additional.fields.key
additional.fields.value_string
Event ID 1058
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
Data/ErrorDescription
security_result.description
DCName
Data/DCName
target.administrative_domain
FilePath
Data/FilePath
target.file.full_path
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
GPOCNName
Data/GPOCNName
additional.fields.key
additional.fields.value_string
Event ID 1064
Provider: Microsoft-Windows-TerminalServices-RemoteConnectionManager
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.summary
security_result.action = FAIL
Event ID 1066
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 1067
Provider: Microsoft-Windows-TerminalServices-RemoteConnectionManager
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Event ID 1068
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
DCName
EventData.DCName
target.administrative_domain
SupportInfo1
additional.fields.key
additional.fields.value.string_value
SupportInfo2
additional.fields.key
additional.fields.value.string_value
ProcessingMode
additional.fields.key
additional.fields.value.string_value
ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value.string_value
Event ID 1069
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ResourceGroup
target.group.group_display_name
ResourceName
target.resource.name
ResTypeDll
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 1073
Provider: User32
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_SHUTDOWN
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
target.hostname
param2
Data/param2
target.user.userid
Event ID 1074
Provider: User32
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_SHUTDOWN
Provider: USER32
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_SHUTDOWN
target_process_file_full_path set to target.process.file.full_path
target_hostname set to target.hostname
Provider: User32
NXLog field
Event Viewer field
UDM field
Domain
principal.administrative_domain
Provider: USER32
NXLog field
Event Viewer field
UDM field
Domain
System/Domain
principal.administrative_domain
Provider: User32
NXLog field
Event Viewer field
UDM field
param2
Data/param2
principal.hostname
param4
Data/param4
additional.fields.key
additional.fields.value.string_value
param5
Data/param5
additional.fields.key
additional.fields.value.string_value
param1
Data/param1
principal.process.file.full_path
AccountName
principal.user.attribute.roles.name
AccountType
principal.user.attribute.roles.name
Provider: USER32
NXLog field
Event Viewer field
UDM field
AccountName
System/AccountName
principal.user.userid
Provider: User32
NXLog field
Event Viewer field
UDM field
UserID
principal.user.windows_sid
param3
Data/param3
security_result.description
param7
Data/param7
target.user.userid
Event ID 1076
Provider: User32
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
additional.fields.key
additional.fields.value_string
param2
additional.fields.key
additional.fields.value_string
param5
additional.fields.key
additional.fields.value_string
param6
additional.fields.key
additional.fields.value_string
Event ID 1085
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
Data/ErrorDescription
security_result.description
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
DCName
Data/DCName
target.administrative_domain
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ExtensionName
Data/ExtensionName
target.resource.name
ExtensionId
Data/ExtensionId
target.resource.product_object_id
Event ID 1096
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErrorCode - %{ErrorCode}
ErrorDescription
security_result.description
SupportInfo1
additional.fields.key
additional.fields.value.string_value
SupportInfo2
additional.fields.key
additional.fields.value.string_value
ProcessingMode
additional.fields.key
additional.fields.value.string_value
ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value.string_value
DCName
target.administrative_domain
FilePath
principal.process.file.full_path
GPOCNName
additional.fields.key
additional.fields.value_string
Event ID 1100
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "Event Logging Service"
Message
security_result.description
Event ID 1101
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 1102
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_ip set to  target.ip
target_url set to target.url
client_certificate_serial set to network.tls.client.certificate.serial
client_certificate_subject set to network.tls.client.certificate.subject
security_result.action = ALLOW
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: DFS Replication
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_WIPE
SubjectDomainName
principal.administrative_domain
SubjectUserName
principal.user.userid
SubjectUserSid
principal.user.windows_sid
SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 1103
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
PercentFull
Data/PercentFull
additional.fields.key
additional.fields.value_string
Event ID 1104
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 1105
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
AutoBackup.BackupPath
Data/BackupPath
target.file.full_path
AutoBackup.Channel
Data/Channel
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 1106
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Reason
Data/Reason
security_result.description
Event ID 1107
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = "Event Logging Service"
ProcessID
Data/ProcessID
principal.process.pid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
Error Code: %{value}
EventID
Data/EventID
additional.fields.key
additional.fields.value_string
PublisherName
Data/PublisherName
additional.fields.key
additional.fields.value_string
PublisherGuid
Data/PublisherGuid
additional.fields.key
additional.fields.value_string
Event ID 1108
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
Data/EventProcessingFailure/ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
EventID
Data/EventProcessingFailure/EventID
metadata.product_event_type
PubID
Data/EventProcessingFailure/PubID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 1112
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
security_result.description
ErrorCode
security_result.summary
Format:
ErrorCode - %{ErrorCode}
DCName
target.administrative_domain
ExtensionName
target.resource.name
ExtensionId
target.resource.product_object_id
SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ProcessingMode
additional.fields.key
additional.fields.value_string
Event ID 1126
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data_1
security_result.summary
set to "Error: %{Data_1} - %{Data_2}"
Data_2
security_result.summary
set to "Error: %{Data_1} - %{Data_2}"
Data
additional.fields.key
additional.fields.value_string
Event ID 1127
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErrorCode - %{ErrorCode}
ErrorDescription
security_result.description
DCName
target.administrative_domain
SupportInfo1
additional.fields.key
additional.fields.value.string_value
SupportInfo2
additional.fields.key
additional.fields.value.string_value
ProcessingMode
additional.fields.key
additional.fields.value.string_value
ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value.string_value
Event ID 1128
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ExtensionName
target.resource.name
ExtensionId
target.resource.product_object_id
SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
additional.fields.key
additional.fields.value_string
Event ID 1129
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorDescription
Data/ErrorDescription
security_result.description
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 1130
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
ErrorDescription
Data/ErrorDescription
security_result.description
GPOFileSystemPath
Data/GPOFileSystemPath
target.file.full_path
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ScriptType
Data/ScriptType
additional.fields.key
additional.fields.value_string
GPODisplayName
Data/GPODisplayName
additional.fields.key
additional.fields.value_string
GPOScriptCommandString
Data/GPOScriptCommandString
additional.fields.key
additional.fields.value_string
Event ID 1134
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1150
Provider: Microsoft Antimalware
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
platform_version set to principal.asset.platform_software.platform_version
Event ID 1162
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1173
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1196
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
StatusString
security_result.summary
ResourceName
target.resource.name
Event ID 1200
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
Message
metadata.description
UserID
target.user.windows_sid
Event ID 1201
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Message
metadata.description
UserID
target.user.windows_sid
Event ID 1202
Provider: SceCli
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
security_result.summary
Format:
summary is set to 0x%{error_code} - %{error_message}
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
Message
metadata.description
"SERVICE"
extensions.auth.mechanism
"SSO"
extensions.auth.typ
UserID
target.user.windows_sid
Event ID 1203
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Message
metadata.description
"SERVICE"
extensions.auth.mechanism
"SSO"
extensions.auth.typ
UserID
target.user.windows_sid
Event ID 1204
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PASSWORD
security_result.action = ALLOW
Message
metadata.description
Event ID 1205
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ResourceGroup
target.group.group_display_name
ResTypeDll
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PASSWORD
security_result.action = FAIL
Message
metadata.description
Event ID 1206
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGOUT
security_result.action = ALLOW
Message
metadata.description
UserID
target.user.windows_sid
Event ID 1207
Provider: AD FS Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGOUT
security_result.action = FAIL
Message
metadata.description
UserID
target.user.windows_sid
Event ID 1213
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
additional.fields.key
additional.fields.value_string
Event ID 1216
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data_3
security_result.description
Data
security_result.summary
Format:
"Error Code - %{Data}"
Data_1
additional.fields.key
additional.fields.value_string
Data_2
principal.ip
Event ID 1226
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1254
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ResourceGroup
target.group.group_display_name
Event ID 1257
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
DNSZone
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ResourceGroup
target.group.group_display_name
Event ID 1282
Provider: Microsoft-Windows-TPM-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 1307
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1311
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1317
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Event ID 1500
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DCName
Data/DCName
target.administrative_domain
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
Event ID 1501
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
Event ID 1502
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DCName
Data/DCName
target.administrative_domain
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
NumberOfGroupPolicyObjects
Data/NumberOfGroupPolicyObjects
additional.fields.key
additional.fields.value_string
Event ID 1503
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DCName
Data/DCName
target.administrative_domain
SupportInfo1
Data/SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
Data/SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
Data/ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
Data/ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
NumberOfGroupPolicyObjects
Data/NumberOfGroupPolicyObjects
additional.fields.key
additional.fields.value_string
Event ID 1531
Provider: Microsoft-Windows-User Profiles Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Domain
Not available
principal.administrative_domain
AccountName
Not available
principal.user.userid
UserID
Not available
principal.user.windows_sid
SourceName
Not available
target.application
Event ID 1532
Provider: Microsoft-Windows-User Profiles Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
Domain
Not available
principal.administrative_domain
AccountName
Not available
principal.user.userid
UserID
Not available
principal.user.windows_sid
SourceName
Not available
target.application
Event ID 1535
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data
security_result.description
Event ID 1564
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_READ
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ShareName
target.resource.name
ResourceName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
BinaryParameterLength
additional.fields.key
additional.fields.value_string
BinaryData
additional.fields.key
additional.fields.value_string
Event ID 1566
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1573
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
NodeName
target.asset.hostname
Event ID 1593
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_READ
target.resource_resource_type = DATABASE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DatabaseFilePath
target.file.full_path
BadDatabaseFilePath
additional.fields.key
additional.fields.value_string
Event ID 1643
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1644
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1645
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1653
Provider: Microsoft-Windows-FailoverClustering
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
NodeName
target.asset.hostname
Event ID 1699
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data_4
security_result.summary
set to "Error Code - %{Data_4}"
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Data_2
security_result.description
Data_3
additional.fields.key
additional.fields.value_string
Data_5
additional.fields.key
additional.fields.value_string
Event ID 1704
Provider: SceCli
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
ProcessId
principal.process.pid
Message
security_result.summary
Event ID 1865
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1925
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 1955
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
ERROR_EVT_UNRESOLVED
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 2000
Provider: Microsoft Antimalware
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
current_signature_version set to target.resource.attribute.labels.key/value
previous_signature_version set to target.resource.attribute.labels.key/value
Event ID 2001
Provider: Microsoft Antimalware
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data_14
security_result.summary
Data_17
target.url
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Data_2
additional.fields.key
additional.fields.value_string
Data_3
additional.fields.key
additional.fields.value_string
Data_4
additional.fields.key
additional.fields.value_string
Data_5
principal.administrative_domain
Data_6
principal.user.windows_sid
Data_7
additional.fields.key
additional.fields.value_string
Data_8
additional.fields.key
additional.fields.value_string
Data_9
additional.fields.key
additional.fields.value_string
Data_10
additional.fields.key
additional.fields.value_string
Data_11
security_result.detection_fields.key
security_result.detection_fields.value
Data_12
additional.fields.key
additional.fields.value_string
Data_13
additional.fields.key
additional.fields.value_string
Data_15
additional.fields.key
additional.fields.value_string
Data_16
additional.fields.key
additional.fields.value_string
Provider: NTDS ISAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
MessageSourceAddress
principal.ip
Event ID 2004
Provider: Microsoft-Windows-Resource-Exhaustion-Detector
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider : Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
LifetimeId
additional.fields.key
additional.fields.value_string
InstanceId
target.resource.product_object_id
Level
additional.fields.key
additional.fields.value_string
Service
target.application
DriverClsid
additional.fields.key
additional.fields.value_string
Event ID 2041
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Event ID 2042
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2053
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2065
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2085
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
MessageSourceAddress
principal.ip
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2089
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2108
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data_3
security_result.summary
set to "Error: %{Data_4} - %{Data_3}"
Data_4
security_result.summary
set to "Error: %{Data_4} - %{Data_3}"
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Data_2
additional.fields.key
additional.fields.value_string
Data_5
security_result.detection_fields.key
security_result.detection_fields.value
Data_6
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 2811
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2887
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2889
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Message
principal_ip
is set to
principal.ip
principal_port
is set to
principal.port
principal_user_id
is set to
principal.user.userid
Event ID 2896
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data_1
security_result.summary
set to "Error: %{Data_1} - %{Data_2}"
Data_2
security_result.summary
set to "Error: %{Data_1} - %{Data_2}"
Data
additional.fields.key
additional.fields.value_string
Event ID 2904
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2946
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 2947
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
Data_2
principal.ip
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data_3
security_result.summary
set to "Error: %{Data_3}"
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Event ID 2974
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Data_2
security_result.summary
set to "Error Code - %{Data_2}"
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Event ID 3005
Provider: LogRhythm Agent
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
Event ID 3006
Provider: LogRhythm Agent
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
Message
Message
is set to
security_result.description
ip is set to
target.ip
port is set to
target.port
Event ID 3040
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 3041
Provider: Microsoft-Windows-ActiveDirectory_DomainService
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Event ID 3072
Provider: Foundation Agents
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 3096
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Event ID 3260
Provider: Workstation
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 3261
Provider: Workstation
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 4000
version 0 Windows 10 client / Provider: Microsoft-Windows-Diagnostics-Networking
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
RepairOption
Data/RepairOption
security_result.detection_fields.key
security_result.detection_fields.value
RepairGUID
Data/RepairGUID
security_result.detection_fields.key
security_result.detection_fields.value
SecondsRequired
Data/SecondsRequired
additional.fields.key
additional.fields.value_string
SIDTypeRequired
Data/SIDTypeRequired
additional.fields.key
additional.fields.value_string
version 1 Windows 10 client / Provider: Microsoft-Windows-Diagnostics-Networking
NXLog field
Event Viewer field
UDM field
RootCause
Data/RootCause
security_result.description
RootCauseGUID
Data/RootCauseGUID
security_result.detection_fields.key
security_result.detection_fields.value
HelperClassName
Data/HelperClassName
additional.fields.key
additional.fields.value_string
InterfaceDesc
Data/InterfaceDesc
additional.fields.key
additional.fields.value_string
InterfaceGUID
Data/InterfaceGUID
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 4001
Provider: Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 4003
Provider: Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
%{ErrorCode}-%{ErrorMsg}
Event
Data/Event
security_result.detection_fields.key
security_result.detection_fields.value
ChangeReason
Data/ChangeReason
security_result.detection_fields.key
security_result.detection_fields.value
IpFamily
Data/IpFamily
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4005
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ReasonForSyncProcessing
Data/ReasonForSyncProcessing
security_result.summary
PrincipalSamName
Data/PrincipalSamName
target.hostname
PolicyActivityId
Data/PolicyActivityId
target.resource.product_object_id
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsDomainJoined
Data/IsDomainJoined
security_result.rule_labels.key
security_result.rule_labels.value
IsBackgroundProcessing
Data/IsBackgroundProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsAsyncProcessing
Data/IsAsyncProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsServiceRestart
Data/IsServiceRestart
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 4006
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
PrincipalSamName
Data/PrincipalSamName
target.hostname
PolicyActivityId
Data/PolicyActivityId
target.resource.product_object_id
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsDomainJoined
Data/IsDomainJoined
security_result.rule_labels.key
security_result.rule_labels.value
IsBackgroundProcessing
Data/IsBackgroundProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsAsyncProcessing
Data/IsAsyncProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsServiceRestart
Data/IsServiceRestart
security_result.rule_labels.key
security_result.rule_labels.value
ReasonForSyncProcessing
Data/ReasonForSyncProcessing
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 4016
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DescriptionString
Data/DescriptionString
security_result.description
CSEExtensionName
Data/CSEExtensionName
target.resource.name
CSEExtensionId
Data/CSEExtensionId
target.resource.product_object_id
IsExtensionAsyncProcessing
Data/IsExtensionAsyncProcessing
target.resource.attribute.labels.key
target.resource.attribute.labels.value
IsGPOListChanged
Data/IsGPOListChanged
security_result.rule_labels.key
security_result.rule_labels.value
GPOListStatusString
Data/GPOListStatusString
security_result.rule_labels.key
security_result.rule_labels.value
ApplicableGPOList
Data/ApplicableGPOList
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 4017
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
OperationDescription
Data/OperationDescription
security_result.description
Parameter
Data/Parameter
additional.fields.key
additional.fields.value_string
Event ID 4096
Provider: NetJoin
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DomainName
Data/DomainName
target.administrative_domain
ComputerName
Data/ComputerName
target.hostname
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 4097
Provider: Microsoft-Windows-CAPI2
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Provider: NetJoin
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
NetStatusCode
Data/NetStatusCode
security_result.description
DomainName
Data/DomainName
target.administrative_domain
ComputerName
Data/ComputerName
target.hostname
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 4100
Provider: Microsoft-Windows-Diagnostics-Networking
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ContextInfo
Data/ContextInfo
additional.fields.key
additional.fields.value_string
UserData
Data/UserData
additional.fields.key
additional.fields.value_string
Payload
Data/Payload
additional.fields.key
additional.fields.value_string
Event ID 4101
Provider: Display
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 4103
version 1 / Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_LAUNCH
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.description
AccountName
principal.user.userid
UserID
principal.user.windows_sid
Category
security_result.summary
CommandName
additional.fields.key
additional.fields.value.string_value
ScriptName
target.file.full_path
HostApplication
target.process.command_line
HostName
additional.fields.key
additional.fields.value.string_value
HostVersion
additional.fields.key
additional.fields.value.string_value
HostId
additional.fields.key
additional.fields.value.string_value
EngineVersion
additional.fields.key
additional.fields.value.string_value
RunspaceId
additional.fields.key
additional.fields.value.string_value
CommandType
additional.fields.key
additional.fields.value.string_value
PipelineID
additional.fields.key
additional.fields.value.string_value
Payload
additional.fields.key
additional.fields.value.string_value
SubjectUserSid
Field is not present in the log
ContextInfo
Data/ContextInfo
additional.fields.key
additional.fields.value_string
UserData
Data/UserData
about.user.attribute.labels.key
about.user.attribute.labels.value
Event ID 4104
Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_LAUNCH
metadata.description = Script block logging
Domain
principal.administrative_domain
MessageNumber
additional.fields.key
additional.fields.value.string_value
MessageTotal
additional.fields.key
additional.fields.value.string_value
ScriptBlockText
Data/ScriptBlockText
target.process.command_line
ScriptBlockId
principal.resource.product_object_id
UserID
principal.user.windows_sid
Category
security_result.summary
Message
security_result.description
SourceName
target.application
ScriptBlockId
principal.resource.product_object_id
Path
target.file.full_path
Event ID 4108
Provider: Microsoft-Windows-CAPI2
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Extract information from
Message
field and map it to
network.tls.client.certificate
Event ID 4109
Provider: Microsoft-Windows-CAPI2
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Extract information from
Message
field and map it to
network.tls.client.certificate
Event ID 4111
Provider: Microsoft-Windows-MSDTC
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
SourceName
Not available
target.application
Category
Data/Category
security_result.category_details
Event ID 4112
Provider: Microsoft-Windows-CAPI2
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 4113
Provider: Microsoft-Windows-CAPI2
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 4115
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsServiceRestart
Data/IsServiceRestart
security_result.rule_labels.key
security_result.rule_labels.value
IsMachineBoot
Data/IsMachineBoot
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 4116
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 4117
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsBackgroundProcessing
Data/IsBackgroundProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsAsyncProcessing
Data/IsAsyncProcessing
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 4124
Provider: Microsoft-Windows-BitLocker-API
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 4125
Provider: Microsoft-Windows-BitLocker-API
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
security_result.description
Format:
Error - %{value}
Event ID 4126
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
Event ID 4127
Provider: Microsoft-Windows-BitLocker-API
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
security_result.description
Event ID 4133
Provider: Microsoft-Windows-BitLocker-API
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 4199
Provider: Tcpip
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
principal.ip
Data_1
Data/Data_1
target.mac
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 4200
Provider: Microsoft-Windows-Iphlpsvc
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
Interface
target_resource_product_object_id set to target.resource.product_object_id
Address
target.ip
ProtocolType
additional.fields.key
additional.fields.value_string
Event ID 4202
Provider: Microsoft-Windows-MSDTC 2
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
SourceName
Not available
target.application
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
param4
Data/param4
additional.fields.key
additional.fields.value.string_value
param5
Data/param5
additional.fields.key
additional.fields.value.string_value
param6
Data/param6
additional.fields.key
additional.fields.value.string_value
param7
Data/param7
additional.fields.key
additional.fields.value.string_value
param9
Data/param9
target.user.userid
param8
Data/param8
additional.fields.key
additional.fields.value_string
param10
Data/param10
additional.fields.key
additional.fields.value_string
param11
Data/param11
additional.fields.key
additional.fields.value_string
param12
Data/param12
additional.fields.key
additional.fields.value_string
Event ID 4227
Provider: Tcpip
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
set to
security_result.summary
Event ID 4230
Provider: Tcpip
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
EventData.Binary
additional.fields.key
additional.fields.value_string
Culture
additional.fields.key
additional.fields.value_string
Level
security_result.detection_fields.key
security_result.detection_fields.value
Keywords.Keyword
additional.fields.key
additional.fields.value_string
Event ID 4257
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsBackgroundProcessing
Data/IsBackgroundProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsAsyncProcessing
Data/IsAsyncProcessing
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 4319
Provider: NetBT
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 4321
Provider: NetBT
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
Data
Data/Data
principal.hostname and principal.port
Data_1
Data/Data_1
principal.ip
Data_2
Data/Data_2
target.ip
Event ID 4326
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
Event ID 4400
Provider: NPS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data_1
principal.administrative_domain
Data
additional.fields.key
additional.fields.value_string
Event ID 4608
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_STARTUP
security_result.action = ALLOW
Event ID 4609
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_SHUTDOWN
security_result.action = ALLOW
Event ID 4610
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
AuthenticationPackageName
Data/AuthenticationPackageName
target.resource.name
Event ID 4611
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  PROCESS_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
LogonProcessName
Data/LogonProcessName
target.process.command_line
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Event ID 4612
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
AuditsDiscarded
about.labels.key
about.labels.value
Event ID 4614
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
NotificationPackageName
Data/NotificationPackageName
target.resource.name
Event ID 4615
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_UNCATEGORIZED
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
InvalidCallName
Data/InvalidCallName
additional.fields.key
additional.fields.value_string
ServerPortName
Data/ServerPortName
additional.fields.key
additional.fields.value_string
Event ID 4616
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type set to SETTING
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
PreviousDate
Data/PreviousDate
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PreviousTime
Data/PreviousTime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewDate
Data/NewDate
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewTime
Data/NewTime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
version 1 /
NXLog field
Event Viewer field
UDM field
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
NewDate
Data/NewDate
target.resource.attribute.labels.key/value
NewTime
Data/NewTime
target.resource.attribute.labels.key/value
PreviousDate
Data/PreviousDate
target.resource.attribute.labels.key/value
PreviousTime
Data/PreviousTime
target.resource.attribute.labels.key/value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4618
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
TargetUserDomain
Data/TargetUserDomain
target.administrative_domain
ComputerName
Data/ComputerName
target.hostname
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
EventId
Data/EventId
additional.fields.key
additional.fields.value_string
EventCount
Data/EventCount
additional.fields.key
additional.fields.value_string
Duration
Data/Duration
additional.fields.key
additional.fields.value_string
Event ID 4621
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
CrashOnAuditFailValue
Data/CrashOnAuditFailValue
security_result.summary
Event ID 4622
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SecurityPackageName
Data/SecurityPackageName
target.resource.name
Event ID 4624
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
LogonType
Data/LogonType
extensions.auth.mechanism and extensions.auth.details
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
WorkstationName
Data/WorkstationName
The
WorkstationName
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
WorkstationName
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
WorkstationName
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
WorkstationName
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
WorkstationName
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
WorkstationName
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
ProcessName
Data/ProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
AuthenticationPackageName
Data/AuthenticationPackageName
security_result.about.resource.name
ElevatedToken
Data/ElevatedToken
security_result.detection_fields.labels.key/value
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
LogonProcessName
Data/LogonProcessName
target.process.file.full_path
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
KeyLength
Data/KeyLength
target.labels.key/value
LmPackageName
Data/LmPackageName
target.labels.key/value
LogonGuid
Data/LogonGuid
additional.fields.key
additional.fields.value_string
version 1 /
NXLog field
Event Viewer field
UDM field
ImpersonationLevel
about.labels.key/value
version 2 /
NXLog field
Event Viewer field
UDM field
TargetOutboundUserName
Data/TargetOutboundUserName
target.user.user_display_name
RestrictedAdminMode
about.labels.key/value
TargetLinkedLogonId
about.labels.key/value
Hostname
intermediary.hostname
Event ID 4625
Provider: Microsoft-Windows-EventSystem
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
about.registry.registry_key
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.category = AUTH_VIOLATION
security_result.action = BLOCK
extensions.auth.type set to MACHINE
FailureReason
security_result.about.labels.key
security_result.about.labels.value
LogonType
Data/LogonType
extensions.auth.mechanism
and
extensions.auth.details
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
WorkstationName
Data/WorkstationName
The
WorkstationName
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
WorkstationName
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
WorkstationName
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
WorkstationName
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
WorkstationName
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
WorkstationName
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
ProcessName
Data/ProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
AuthenticationPackageName
Data/AuthenticationPackageName
security_result.about.resource.name
Status
Data/Status
security_result.summary
Populate description corresponding to the status codes. Format: Status(%{Status}): %{status_description}.
If the value coming is 0xc000006d, then store the value 'The cause is either a bad username or authentication information (referred from doc table.'
SubStatus
Data/SubStatus
security_result.description
Populate description corresponding to the substatus codes. Format: SubStatus(%{SubStatus}): %{sub_status_description}
If the value coming is 0xc000006d, then store the value 'The cause is either a bad username or authentication information (referred from doc table.'
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
LogonProcessName
Data/LogonProcessName
target.process.file.full_path
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TransmittedServices
Data/TransmittedServices
additional.fields.key
additional.fields.value_string
LmPackageName
Data/LmPackageName
additional.fields.key
additional.fields.value_string
KeyLength
Data/KeyLength
additional.fields.key
additional.fields.value_string
Hostname
intermediary.hostname
Event ID 4626
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
LogonType
Data/LogonType
extensions.auth.mechanism and extensions.auth.details
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
EventIdx
Data/EventIdx
additional.fields.key
additional.fields.value_string
EventCountTotal
Data/EventCountTotal
additional.fields.key
additional.fields.value_string
UserClaims
Data/UserClaims
additional.fields.key
additional.fields.value_string
DeviceClaims
Data/DeviceClaims
additional.fields.key
additional.fields.value_string
Event ID 4627
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_UNCATEGORIZED
security_result.action = ALLOW
LogonType
Data/LogonType
extensions.auth.mechanism and extensions.auth.details
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
GroupMembership
Data/GroupMembership
target.user.group_identifiers
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
EventIdx
Data/EventIdx
additional.fields.key
additional.fields.value_string
EventCountTotal
Data/EventCountTotal
additional.fields.key
additional.fields.value_string
Event ID 4634
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGOUT
security_result.action = ALLOW
LogonType
Data/LogonType
extensions.auth.mechanism and extensions.auth.details
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4646
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
security_result.action = BLOCK
notification
Data/notification
additional.fields.key
additional.fields.value_string
Event ID 4647
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGOUT
security_result.action = BLOCK
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4648
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
extensions.auth.mechanism set to "USERNAME_PASSWORD"
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
TargetServerName
target.hostname
TargetInfo
target.labels.key
target.labels.value
ProcessName
Data/ProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
Event ID 4649
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_UNCATEGORIZED
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
LogonProcessName
Data/LogonProcessName
principal.process.command_line
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
WorkstationName
Data/WorkstationName
The
WorkstationName
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
WorkstationName
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
WorkstationName
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
WorkstationName
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
WorkstationName
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
WorkstationName
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
ProcessName
Data/ProcessName
target.process.command_line
ProcessId
Data/ProcessId
target.process.pid
TargetUserName
Data/TargetUserName
target.user.userid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
RequestType
Data/RequestType
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationPackage
Data/AuthenticationPackage
security_result.detection_fields.key
security_result.detection_fields.value
TransmittedServices
Data/TransmittedServices
additional.fields.key
additional.fields.value_string
Event ID 4650
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
MMAuthMethod
Data/MMAuthMethod
additional.fields.key
additional.fields.value_string
MMCipherAlg
Data/MMCipherAlg
additional.fields.key
additional.fields.value_string
MMIntegrityAlg
Data/MMIntegrityAlg
additional.fields.key
additional.fields.value_string
DHGroup
Data/DHGroup
additional.fields.key
additional.fields.value_string
MMLifetime
Data/MMLifetime
additional.fields.key
additional.fields.value_string
QMLimit
Data/QMLimit
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
Event ID 4651
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalMMIssuingCA
Data/LocalMMIssuingCA
network.tls.client.certificate.issuer
RemoteMMIssuingCA
Data/RemoteMMIssuingCA
network.tls.server.certificate.issuer
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
LocalMMCertHash
Data/LocalMMCertHash
additional.fields.key
additional.fields.value_string
LocalMMRootCA
Data/LocalMMRootCA
additional.fields.key
additional.fields.value_string
RemoteMMCertHash
Data/RemoteMMCertHash
additional.fields.key
additional.fields.value_string
RemoteMMRootCA
Data/RemoteMMRootCA
additional.fields.key
additional.fields.value_string
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
MMAuthMethod
Data/MMAuthMethod
additional.fields.key
additional.fields.value_string
MMCipherAlg
Data/MMCipherAlg
additional.fields.key
additional.fields.value_string
MMIntegrityAlg
Data/MMIntegrityAlg
additional.fields.key
additional.fields.value_string
DHGroup
Data/DHGroup
additional.fields.key
additional.fields.value_string
MMLifetime
Data/MMLifetime
additional.fields.key
additional.fields.value_string
QMLimit
Data/QMLimit
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
Event ID 4652
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = FAIL
LocalMMIssuingCA
Data/LocalMMIssuingCA
network.tls.client.certificate.issuer
RemoteMMIssuingCA
Data/RemoteMMIssuingCA
network.tls.server.certificate.issuer
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
LocalMMCertHash
Data/LocalMMCertHash
additional.fields.key
additional.fields.value_string
LocalMMRootCA
Data/LocalMMRootCA
additional.fields.key
additional.fields.value_string
RemoteMMCertHash
Data/RemoteMMCertHash
additional.fields.key
additional.fields.value_string
RemoteMMRootCA
Data/RemoteMMRootCA
additional.fields.key
additional.fields.value_string
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
FailurePoint
Data/FailurePoint
security_result.detection_fields.key
security_result.detection_fields.value
FailureReason
Data/FailureReason
security_result.summary
MMAuthMethod
Data/MMAuthMethod
additional.fields.key
additional.fields.value_string
State
Data/State
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
InitiatorCookie
Data/InitiatorCookie
additional.fields.key
additional.fields.value_string
ResponderCookie
Data/ResponderCookie
additional.fields.key
additional.fields.value_string
Event ID 4653
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = FAIL
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
FailureReason
Data/FailureReason
security_result.summary
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
FailurePoint
Data/FailurePoint
security_result.detection_fields.key
security_result.detection_fields.value
MMAuthMethod
Data/MMAuthMethod
additional.fields.key
additional.fields.value_string
State
Data/State
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
InitiatorCookie
Data/InitiatorCookie
additional.fields.key
additional.fields.value_string
ResponderCookie
Data/ResponderCookie
additional.fields.key
additional.fields.value_string
Event ID 4654
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = FAIL
Protocol
Data/Protocol
network.ip_protocol
LocalAddress
Data/LocalAddress
principal.ip
LocalPort
Data/LocalPort
principal.port
FailureReason
Data/FailureReason
security_result.summary
RemoteAddress
Data/RemoteAddress
target.ip
RemotePort
Data/RemotePort
target.port
LocalAddressMask
Data/LocalAddressMask
additional.fields.key
additional.fields.value_string
LocalTunnelEndpoint
Data/calTunnelEndpoint
additional.fields.key
additional.fields.value_string
RemoteAddressMask
Data/RemoteAddressMask
additional.fields.key
additional.fields.value_string
RemoteTunnelEndpoint
Data/RemoteTunnelEndpoint
additional.fields.key
additional.fields.value_string
RemotePrivateAddress
Data/RemotePrivateAddress
additional.fields.key
additional.fields.value_string
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
FailurePoint
Data/FailurePoint
security_result.detection_fields.key
security_result.detection_fields.value
Mode
Data/Mode
additional.fields.key
additional.fields.value_string
State
Data/State
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MessageID
Data/MessageID
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
TunnelId
Data/TunnelId
additional.fields.key
additional.fields.value_string
TrafficSelectorId
Data/TrafficSelectorId
additional.fields.key
additional.fields.value_string
Event ID 4655
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalAddress
Data/LocalAddress
principal.ip
RemoteAddress
Data/RemoteAddress
target.ip
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
Event ID 4656
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
TransactionId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RestrictedSidCount
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectName
Data/ObjectName
target.file.full_path
(when ObjectType = "File")
target.process.command_line
(when ObjectType = "Process")
AccessList
Data/AccessList
target.resource.attribute.permissions.name
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
ObjectType
Data/ObjectType
target.resource.resource_subtype
ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccessMask
Data/AccessMask
principal.process.access_mask
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
ResourceAttributes
Data/ResourceAttributes
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccessReason
Data/AccessReason
security_result.description
Event ID 4657
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = REGISTRY_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
OperationType
target.labels.key
target.labels.value
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectName
Data/ObjectName
target.registry.registry_key
OldValueType
target.labels.key
target.labels.value
OldValue
target.labels.key
target.labels.value
NewValueType
target.labels.key
target.labels.value
NewValue
Data/NewValue
target.registry.registry_value_data
ObjectValueName
Data/ObjectValueName
target.registry.registry_value_name
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
HandleId
target.labels.key/value
Event ID 4658
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
HandleId
target.labels.key/value
SubjectUserName
Data/SubjectUserName
principal.user.userid
ObjectServer
target.labels.key
target.labels.value
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Event ID 4659
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectName
Data/ObjectName
target.file.full_path
(when ObjectType = "File")
target.process.command_line
(when ObjectType = "Process")
AccessList
Data/AccessList
target.resource.attribute.permissions.name
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
ObjectServer
Data/ObjectServer
additional.fields.key
additional.fields.value_string
ObjectType
Data/ObjectType
additional.fields.key
additional.fields.value_string
HandleId
Data/HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TransactionId
Data/TransactionId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccessMask
Data/AccessMask
principal.process.access_mask
principal.resource.attribute.permissions
Event ID 4660
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_DELETION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TransactionId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Event ID 4661
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
AccessReason
Data/AccessReason
security_result.description
RestrictedSidCount
target.labels.key
target.labels.value
version 0 /
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ObjectType
target.labels.key/value
ProcessName
Data/ProcessName
principal.process.file.full_path
HandleId
target.labels.key/value
TransactionId
target.labels.key
target.labels.value
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectName
Data/ObjectName
target.group.group_display_name
(when ObjectType is SAM_ALIAS, SAM_GROUP)
target.user.userid
(when ObjectType is SAM_USER)
target.administrative_domain
(when ObjectType is SAM_DOMAIN)
target.hostname
(when ObjectType is SAM_SERVER)
AccessList
Data/AccessList
target.resource.attribute.permissions.name
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
ObjectServer
target.labels.key
target.labels.value
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
AccessMask
Data/AccessMask
additional.fields.key
additional.fields.value_string
Properties
Data/Properties
additional.fields.key
additional.fields.value_string
Event ID 4662
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
ObjectType
target.resource.resource_subtype
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
AdditionalInfo
Data/AdditionalInfo
security_result.description
AdditionalInfo2
security_result.detection_fields.key/value
Properties
Data/Properties
security_result.detection_fields.key/value
AccessMask
Data/AccessMask
principal.process.access_mask
principal.resource.attribute.permissions
ObjectName
Data/ObjectName
target.resource.name
ObjectServer
Data/ObjectServer
target.resource.parent
target.resource_ancestors.name
OperationType
Data/OperationType
additional.fields.key
additional.fields.value_string
HandleId
Data/HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccessList
Data/AccessList
target.resource.attribute.permissions.name
Event ID 4663
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
FILE_OPEN (ObjectType = File, SymbolicLink)
REGISTRY_UNCATEGORIZED (ObjectType = Key)
PROCESS_OPEN (ObjectType = Process)
USER_RESOURCE_ACCESS (ObjectType = Event)
security_result.action = ALLOW
ObjectName
Data/ObjectName
Object Type              | UDM Field
--------------------------+------------------------------------
File, SymbolicLink    |
target.file.full_path
Key                             |
target.registry.registry_key
Process                      |
target.process.file.full_path
Event                          |
target.resource.name
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ObjectType
target.resource.resource_subtype
HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
AccessList
Data/AccessList
target.resource.attribute.permissions.name
ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ResourceAttributes
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccessMask
Data/AccessMask
principal.process.access_mask
principal.resource.attribute.permissions
Event ID 4664
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
FileName
Data/FileName
target.file.full_path
TransactionId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LinkName
Data/LinkName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4665
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_CREATION
security_result.action = UNKNOWN_ACTION
ClientDomain
Data/ClientDomain
principal.administrative_domain
ClientName
Data/ClientName
principal.labels.key/value
AppName
Data/AppName
target.application
AppInstance
Data/AppInstance
target.resource.product_object_id
ClientLogonId
Data/ClientLogonId
additional.fields.key
additional.fields.value_string
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 4666
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = UNKNOWN_ACTION
ClientDomain
Data/ClientDomain
principal.administrative_domain
AppInstance
target.resource.product_object_id
ClientName
Data/ClientName
principal.labels.key/value
AppName
Data/AppName
target.application
ObjectName
Data/ObjectName
target.resource.name
ScopeName
Data/ScopeName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClientLogonId
Data/ClientLogonId
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
Group
Data/Group
additional.fields.key
additional.fields.value_string
OperationName
Data/OperationName
additional.fields.key
additional.fields.value_string
OperationId
Data/OperationId
additional.fields.key
additional.fields.value_string
Event ID 4667
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_DELETION
security_result.action = UNKNOWN_ACTION
ClientDomain
Data/ClientDomain
principal.administrative_domain
AppInstance
target.resource.product_object_id
ClientName
Data/ClientName
principal.labels.key/value
AppName
Data/AppName
target.application
ClientLogonId
Data/ClientLogonId
additional.fields.key
additional.fields.value_string
Event ID 4668
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ClientDomain
Data/ClientDomain
principal.administrative_domain
ClientName
Data/ClientName
principal.labels.key/value
AppInstance
target.resource.product_object_id
AppName
Data/AppName
target.application
ClientLogonId
Data/ClientLogonId
additional.fields.key
additional.fields.value_string
StoreUrl
Data/StoreUrl
additional.fields.key
additional.fields.value_string
Event ID 4670
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
FILE_OPEN (ObjectType = File, SymbolicLink)
REGISTRY_UNCATEGORIZED (ObjectType = Key)
PROCESS_OPEN (ObjectType = Process)
USER_RESOURCE_ACCESS (ObjectType = Event)
security_result.action = ALLOW_WITH_MODIFICATION
ObjectName
Data/ObjectName
Object Type              | UDM Field
--------------------------+------------------------------------
File, SymbolicLink    |
target.file.full_path
Key                             |
target.registry.registry_key
Process                      |
target.process.file.full_path
Event                          |
target.resource.name
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldSd
Data/OldSd
security_result.detection_fields.key/value
NewSd
Data/NewSd
security_result.detection_fields.key/value
ObjectType
target.resource.resource_subtype
Event ID 4671
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
CallerDomainName
Data/CallerDomainName
principal.administrative_domain
CallerUserName
Data/CallerUserName
principal.user.userid
CallerUserSid
Data/CallerUserSid
principal.user.windows_sid
CallerLogonId
Data/CallerLogonId
principal.user.attribute.labels.key
principal.user.attribute.labels.value
Ordinal
Data/Ordinal
additional.fields.key
additional.fields.value_string
Event ID 4672
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Event ID 4673
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
If required fields for above mentioned metadata.event_type are not present, then set metadata.event_type to GENERIC_EVENT.
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
Service
target.application
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
SubjectUserSid
principal.user.windows_sid
ProcessName
Data/ProcessName
target.process.command_line
If ProcessName field not in log then extract "Process ID" and "Process Name" from "Message" field.
ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProcessId
Data/ProcessId
target.process.pid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
PrivilegeList
Data/PrivilegeList
target.resource.attribute.permissions.name
Event ID 4674
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
If the ProcessName field is absent, then set metadata.event_type to GENERIC_EVENT.
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ProcessName
Data/ProcessName
target.process.command_line
If ProcessName field not in log then extract "Process ID" and "Process Name" from "Message" field.
ProcessId
Data/ProcessId
target.process.pid
ObjectName
ObjectName
target.resource.name
ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ObjectType
Data/ObjectType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccessMask
Data/AccessMask
additional.fields.key
additional.fields.value_string
PrivilegeList
Data/PrivilegeList
principal.user.attribute.permissions.name
Event ID 4675
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TdoDirection
Data/TdoDirection
security_result.detection_fields.key
security_result.detection_fields.value
TdoAttributes
Data/TdoAttributes
security_result.detection_fields.key
security_result.detection_fields.value
TdoType
Data/TdoType
security_result.detection_fields.key
security_result.detection_fields.value
TdoSid
Data/TdoSid
security_result.detection_fields.key
security_result.detection_fields.value
SidList
Data/SidList
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4688
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_LAUNCH
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
NewProcessName
Data/NewProcessName
target.process.file.full_path
NewProcessId
Data/NewProcessId
target.process.pid
ParentProcessName
Data/ParentProcessName
principal.process.file.full_path
TokenElevationType
Data/TokenElevationType
target.labels
additional.fields.key
additional.fields.value.string_value
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
version 1 /
NXLog field
Event Viewer field
UDM field
commandLine
Data/commandLine
principal.process.command_line
version 2 /
NXLog field
Event Viewer field
UDM field
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
MandatoryLabel
Data/MandatoryLabel
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4689
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_TERMINATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ProcessName
Data/ProcessName
target.process.file.full_path
principal.process.file.full_path
ProcessId
Data/ProcessId
target.process.pid
principal.process.pid
Status
Data/Status
security_result.summary
Event ID 4690
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_CREATION
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SourceProcessId
Data/SourceProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
SourceHandleId
Data/SourceHandleId
src.resource.name
TargetProcessId
Data/TargetProcessId
target.process.pid
TargetHandleId
Data/TargetHandleId
target.resource.name
Event ID 4691
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
FILE_OPEN (ObjectType = File, SymbolicLink)
REGISTRY_UNCATEGORIZED (ObjectType = Key)
PROCESS_OPEN (ObjectType = Process)
USER_RESOURCE_ACCESS (ObjectType = Event)
security_result.action = ALLOW
ObjectName
Data/ObjectName
Object Type              | UDM Field
--------------------------+------------------------------------
File, SymbolicLink    |
target.file.full_path
Key                             |
target.registry.registry_key
Process                      |
target.process.file.full_path
Event                          |
target.resource.name
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ObjectType
Data/ObjectType
additional.fields.key
additional.fields.value_string
AccessList
Data/AccessList
additional.fields.key
additional.fields.value_string
AccessMask
Data/AccessMask
additional.fields.key
additional.fields.value_string
Event ID 4692
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW
if
FailureReason
contains "0x0"; otherwise, set it to
FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
MasterKeyId
security_result.detection_fields.key
security_result.detection_fields.value
RecoveryKeyId
security_result.detection_fields.key
security_result.detection_fields.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
FailureReason
Data/FailureReason
security_result.description
RecoveryServer
Data/RecoveryServer
target.hostname
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4693
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW
if
FailureId
contains "0x380000"; otherwise, set it to
FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
MasterKeyId
security_result.detection_fields.key
security_result.detection_fields.value
RecoveryKeyId
security_result.detection_fields.key
security_result.detection_fields.value
FailureId
security_result.detection_fields.key
security_result.detection_fields.value
RecoveryServer
target.hostname
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RecoveryReason
Data/RecoveryReason
security_result.description
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Event ID 4694
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
MasterKeyId
security_result.detection_fields.key
security_result.detection_fields.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
FailureReason
Data/FailureReason
security_result.description
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DataDescription
Data/DataDescription
security_result.detection_fields.key
security_result.detection_fields.value
ProtectedDataFlags
Data/ProtectedDataFlags
security_result.detection_fields.key
security_result.detection_fields.value
CryptoAlgorithms
Data/CryptoAlgorithms
additional.fields.key
additional.fields.value_string
Event ID 4695
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
SubjectUserName
Data/SubjectUserName
principal.user.userid
MasterKeyId
security_result.detection_fields.key
security_result.detection_fields.value
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
FailureReason
Data/FailureReason
security_result.description
DataDescription
Data/DataDescription
security_result.detection_fields.key
security_result.detection_fields.value
ProtectedDataFlags
Data/ProtectedDataFlags
security_result.detection_fields.key
security_result.detection_fields.value
CryptoAlgorithms
Data/CryptoAlgorithms
additional.fields.key
additional.fields.value_string
Event ID 4696
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetProcessName
Data/TargetProcessName
target.process.command_line
TargetProcessId
Data/TargetProcessId
target.process.pid
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4697
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ServiceType
target.labels.key
target.labels.value
ServiceStartType
target.labels.key
target.labels.value
ServiceAccount
target.resource.name
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ServiceName
Data/ServiceName
target.application
ServiceFileName
Data/ServiceFileName
target.process.file.full_path
version 1 / Windows 10 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
ClientProcessId
Data/ClientProcessId
principal.process.pid
ParentProcessId
Data/ParentProcessId
principal.process.parent_process.pid
ClientProcessStartKey
Data/ClientProcessStartKey
additional.fields.key
additional.fields.value_string
Event ID 4698
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_CREATION
target.resource.resource_type = TASK
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TaskName
Data/TaskName
target.resource.name
Message
Data/Message
URI set to target.file.full_path
Command set to target.process.command_line
TaskContent
Data/TaskContent
The XML data from
TaskContent
field is parsed and mapped as follows:
/Task/Actions/Exec/Command
is mapped to
target.process.file.full_path
.
/Task/Principals/Principal/UserId
is mapped to
target.user.userid
.
The following fields are mapped to
target.user.attribute.labels
as key-value pairs:
/Task/Principals/Principal/@id
,
/Task/Principals/Principal/RunLevel
,
/Task/Principals/Principal/LogonType
.
The following fields are mapped to
target.resource.attribute.labels
as key-value pairs:
/Task/Actions/Exec/Arguments
,
/Task/@version
,
/Task/@xmlns
,
/Task/Actions/@Context
, and all fields under
/Task/RegistrationInfo/
,
/Task/Settings/
,
/Task/Triggers/
, and
/Task/Actions/ComHandler/
.
version 1 / Windows 10 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
ParentProcessId
Data/ParentProcessId
target.process.parent_process.pid
ClientProcessId
Data/ClientProcessId
target.process.pid
ClientProcessStartKey
Data/ClientProcessStartKey
additional.fields.key
additional.fields.value_string
RpcCallClientLocality
Data/RpcCallClientLocality
additional.fields.key
additional.fields.value_string
FQDN
Data/FQDN
additional.fields.key
additional.fields.value_string
Event ID 4699
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_DELETION
target.resource.resource_type = "TASK"
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TaskName
Data/TaskName
target.resource.name
TaskContent
Data/TaskContent
The XML data from
TaskContent
field is parsed and mapped as follows:
/Task/Actions/Exec/Command
is mapped to
target.process.file.full_path
.
/Task/Principals/Principal/UserId
is mapped to
target.user.userid
.
The following fields are mapped to
target.user.attribute.labels
as key-value pairs:
/Task/Principals/Principal/@id
,
/Task/Principals/Principal/RunLevel
,
/Task/Principals/Principal/LogonType
.
The following fields are mapped to
target.resource.attribute.labels
as key-value pairs:
/Task/Actions/Exec/Arguments
,
/Task/@version
,
/Task/@xmlns
,
/Task/Actions/@Context
, and all fields under
/Task/RegistrationInfo/
,
/Task/Settings/
,
/Task/Triggers/
, and
/Task/Actions/ComHandler/
.
version 1 / Windows 10 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
ParentProcessId
Data/ParentProcessId
principal.process.parent_process.pid
ClientProcessId
Data/ClientProcessId
principal.process.pid
ClientProcessStartKey
Data/ClientProcessStartKey
additional.fields.key
additional.fields.value_string
RpcCallClientLocality
Data/RpcCallClientLocality
additional.fields.key
additional.fields.value_string
FQDN
Data/FQDN
additional.fields.key
additional.fields.value_string
Event ID 4700
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
SCHEDULED_TASK_ENABLE
target.resource.resource_type = TASK
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TaskName
Data/TaskName
target.resource.name
TaskContent
Data/TaskContent
The XML data from
TaskContent
field is parsed and mapped as follows:
/Task/Actions/Exec/Command
is mapped to
target.process.file.full_path
.
/Task/Principals/Principal/UserId
is mapped to
target.user.userid
.
The following fields are mapped to
target.user.attribute.labels
as key-value pairs:
/Task/Principals/Principal/@id
,
/Task/Principals/Principal/RunLevel
,
/Task/Principals/Principal/LogonType
.
The following fields are mapped to
target.resource.attribute.labels
as key-value pairs:
/Task/Actions/Exec/Arguments
,
/Task/@version
,
/Task/@xmlns
,
/Task/Actions/@Context
, and all fields under
/Task/RegistrationInfo/
,
/Task/Settings/
,
/Task/Triggers/
, and
/Task/Actions/ComHandler/
.
version 1 / Windows 10 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
ParentProcessId
Data/ParentProcessId
principal.process.parent_process.pid
ClientProcessId
Data/ClientProcessId
principal.process.pid
ClientProcessStartKey
Data/ClientProcessStartKey
additional.fields.key
additional.fields.value_string
RpcCallClientLocality
Data/RpcCallClientLocality
additional.fields.key
additional.fields.value_string
FQDN
Data/FQDN
additional.fields.key
additional.fields.value_string
Event ID 4701
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
SCHEDULED_TASK_DISABLE
target.resource.resource_type = TASK
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TaskName
Data/TaskName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TaskContent
Data/TaskContent
The XML data from
TaskContent
field is parsed and mapped as follows:
/Task/Actions/Exec/Command
is mapped to
target.process.file.full_path
.
/Task/Principals/Principal/UserId
is mapped to
target.user.userid
.
The following fields are mapped to
target.user.attribute.labels
as key-value pairs:
/Task/Principals/Principal/@id
,
/Task/Principals/Principal/RunLevel
,
/Task/Principals/Principal/LogonType
.
The following fields are mapped to
target.resource.attribute.labels
as key-value pairs:
/Task/Actions/Exec/Arguments
,
/Task/@version
,
/Task/@xmlns
,
/Task/Actions/@Context
, and all fields under
/Task/RegistrationInfo/
,
/Task/Settings/
,
/Task/Triggers/
, and
/Task/Actions/ComHandler/
.
version 1 / Windows 10 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
ParentProcessId
Data/ParentProcessId
principal.process.parent_process.pid
ClientProcessId
Data/ClientProcessId
principal.process.pid
ClientProcessStartKey
Data/ClientProcessStartKey
additional.fields.key
additional.fields.value_string
RpcCallClientLocality
Data/RpcCallClientLocality
additional.fields.key
additional.fields.value_string
FQDN
Data/FQDN
additional.fields.key
additional.fields.value_string
Event ID 4702
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_MODIFICATION
target.resource.resource_type = TASK
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
FQDN
target.labels.key
target.labels.value
TaskContentNew
The XML data from
TaskContentNew
field is parsed and mapped as follows:
/Task/Actions/Exec/Command
is mapped to
target.process.file.full_path
.
/Task/Principals/Principal/UserId
is mapped to
target.user.userid
.
The following fields are mapped to
target.user.attribute.labels
as key-value pairs:
/Task/Principals/Principal/@id
,
/Task/Principals/Principal/RunLevel
,
/Task/Principals/Principal/LogonType
.
The following fields are mapped to
target.resource.attribute.labels
as key-value pairs:
/Task/Actions/Exec/Arguments
,
/Task/@version
,
/Task/@xmlns
,
/Task/Actions/@Context
, and all fields under
/Task/RegistrationInfo/
,
/Task/Settings/
,
/Task/Triggers/
, and
/Task/Actions/ComHandler/
.
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TaskName
Data/TaskName
target.resource.name
version 1 / Windows 10 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
ClientProcessId
Data/ClientProcessId
target.process.pid
ParentProcessId
Data/ParentProcessId
target.process.parent_process.pid
ClientProcessStartKey
Data/ClientProcessStartKey
additional.fields.key
additional.fields.value_string
RpcCallClientLocality
Data/RpcCallClientLocality
additional.fields.key
additional.fields.value_string
Event ID 4703
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_PERMISSIONS_CHANGE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
EnabledPrivilegeList
Data/EnabledPrivilegeList
target.user.attribute.permissions.name
target.user.attribute.permissions.description
DisabledPrivilegeList
Data/DisabledPrivilegeList
target.user.attribute.permissions.name
target.user.attribute.permissions.description
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4704
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  USER_CHANGE_PERMISSIONS
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetSid
Data/TargetSid
target.user.windows_sid
Extract userId from
TargetSid
and map it to
target.user.userid
.
Extract domain from
TargetSid
and map it to
target.administrative_domain
.
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4705
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  USER_CHANGE_PERMISSIONS
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetSid
Data/TargetSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4706
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DomainName
Data/DomainName
target.administrative_domain
DomainSid
Data/DomainSid
target.user.windows_sid
TdoType
Data/TdoType
security_result.detection_fields[Trust Type]
TdoDirection
Data/TdoDirection
security_result.detection_fields[Trust Direction]
TdoAttributes
Data/TdoAttributes
security_result.detection_fields[Trust Attributes]
SidFilteringEnabled
Data/SidFilteringEnabled
security_result.detection_fields[Sid Filtering]
DomainSid
Data/DomainSid
target.user.windows_sid
TdoType
Data/TdoType
security_result.detection_fields.key
security_result.detection_fields.value
TdoDirection
Data/TdoDirection
security_result.detection_fields.key
security_result.detection_fields.value
TdoAttributes
Data/TdoAttributes
security_result.detection_fields.key
security_result.detection_fields.value
SidFilteringEnabled
Data/SidFilteringEnabled
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4707
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DomainName
Data/DomainName
target.administrative_domain
DomainSid
Data/DomainSid
target.user.windows_sid
DomainSid
Data/DomainSid
target.user.windows_sid
Event ID 4709
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application = "IPsec Policy Agent Service"
security_result.action = ALLOW
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
Event ID 4710
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "IPsec Policy Agent Service"
security_result.action = ALLOW
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
Event ID 4711
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
FAIL
if
param1
contains "failed"; Set it to
ALLOW
if
param1
contains "applied" or "loaded".
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
Event ID 4712
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "IPsec Policy Agent Service"
security_result.action = FAIL
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
Event ID 4713
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
KerberosPolicyChange
Data/KerberosPolicyChange
target.resource.attribute.labels.key = "FieldName_OLD_VALUE" and value="<old_value>" and
target.resource.attribute.labels.key = "FieldName_NEW_VALUE" and value="<new_value>"
Event ID 4714
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
EfsPolicyChange
Data/EfsPolicyChange
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4715
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
OldSd
Data/OldSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewSd
Data/NewSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4716
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DomainName
Data/DomainName
target.administrative_domain
DomainSid
Data/DomainSid
target.user.windows_sid
TdoType
Data/TdoType
security_result.detection_fields[Trust Type]
TdoDirection
Data/TdoDirection
security_result.detection_fields[Trust Direction]
TdoAttributes
Data/TdoAttributes
security_result.detection_fields[Trust Attributes]
SidFilteringEnabled
Data/SidFilteringEnabled
security_result.detection_fields[Sid Filtering]
DomainSid
Data/DomainSid
target.user.windows_sid
TdoType
Data/TdoType
security_result.detection_fields.key
security_result.detection_fields.value
TdoDirection
Data/TdoDirection
security_result.detection_fields.key
security_result.detection_fields.value
TdoAttributes
Data/TdoAttributes
security_result.detection_fields.key
security_result.detection_fields.value
SidFilteringEnabled
Data/SidFilteringEnabled
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4717
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
AccessGranted
Data/AccessGranted
target.user.attribute.permissions.name
target.user.attribute.permissions.description
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4718
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
AccessRemoved
Data/AccessRemoved
target.user.attribute.permissions.name
target.user.attribute.permissions.description
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4719
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW_WITH_MODIFICATION
SubcategoryGuid
Data/SubcategoryGuid
Populate security_result.category_details based on description received in output of command: auditpol /list /subcategory:* /v.
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
CategoryId
Data/CategoryId
security_result[0].category_details
is set to "CategoryId"
security_result[0].summary
is set to "%{CategoryId}"
security_result[0].description
is set to "%{Category}"
SubcategoryId
Data/SubcategoryId
security_result[0].category_details
is set to "SubCategoryId"
security_result[0].summary
is set to "%{SubCategoryId}"
security_result[0].description
is set to "%{SubCategory}"
extract "Subcategory" description from "Message" field.
SubcategoryGuid
Data/SubcategoryGuid
security_result[2].category_details
is set to "SubcategoryGuid"
security_result[2].summary
is set to "%{SubcategoryGuid}"
security_result[2].description
is set to "%{subcategory_guid_description}"
AuditPolicyChanges
Data/AuditPolicyChanges
security_result[3].category_details
is set to "AuditPolicyChanges"
security_result[3].summary
is set to "%{AuditPolicyChanges_description}"
extract "AuditPolicyChanges_description" description from "Message" field
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4720
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
DisplayName
Data/DisplayName
target.user.user_display_name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
SamAccountName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserPrincipalName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HomeDirectory
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HomePath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ScriptPath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProfilePath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserWorkstations
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PasswordLastSet
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccountExpires
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PrimaryGroupId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AllowedToDelegateTo
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldUacValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewUacValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserAccountControl
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserAccountControl
Data/UserAccountControl
The
UserAccountControl
raw log field value string is split into individual codes. Each code is translated to a human-readable description. These descriptions are added as key-value pairs to the
target.resource.attribute.labels
repeated field. For each entry, the key is "UserAccountControl_value" and the value is the translated description.
UserParameters
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SidHistory
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LogonHours
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4722
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PERMISSIONS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4723
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PASSWORD
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4724
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PASSWORD
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4725
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PERMISSIONS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4726
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_DELETION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4727
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4728
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Message
Data/Message
Extracted OU, CN, DC fields from the
Message
log field and mapped it to
target.user.attribute.labels
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
Data/MembershipExpirationTime
target.user.attribute.labels.key
target.user.attribute.labels.value
Event ID 4729
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4730
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Event ID 4731
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SamAccountName
principal.user.attribute.labels.key/value
SidHistory
principal.user.attribute.labels.key/value
Event ID 4732
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
version 1 /
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
target.user.attribute.labels.key/value
Event ID 4733
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
Event ID 4734
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Event ID 4735
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SamAccountName
principal.user.attribute.labels.key/value
SidHistory
principal.user.attribute.labels.key/value
Event ID 4737
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
target.group.attribute.labels.key
target.group.attribute.labels.value
Event ID 4738
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_UNCATEGORIZED
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.user_display_name
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
SamAccountName
Data/SamAccountName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DisplayName
Data/DisplayName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserPrincipalName
Data/UserPrincipalName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HomeDirectory
Data/HomeDirectory
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HomePath
Data/HomePath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ScriptPath
Data/ScriptPath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProfilePath
Data/ProfilePath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserWorkstations
Data/UserWorkstations
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PasswordLastSet
Data/PasswordLastSet
target.resource.attribute.labels.key
target.resource.attribute.labels.value
target.user.last_password_change_time
AccountExpires
Data/AccountExpires
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PrimaryGroupId
Data/PrimaryGroupId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AllowedToDelegateTo
Data/AllowedToDelegateTo
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldUacValue
Data/OldUacValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewUacValue
Data/NewUacValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserAccountControl
Data/UserAccountControl
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserAccountControl
Data/UserAccountControl
The
UserAccountControl
raw log field value string is split into individual codes. Each code is translated to a human-readable description. These descriptions are added as key-value pairs to the
target.resource.attribute.labels
repeated field. For each entry, the key is "UserAccountControl_value" and the value is the translated description.
UserParameters
Data/UserParameters
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SidHistory
Data/SidHistory
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LogonHours
Data/LogonHours
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Dummy
Data/Dummy
additional.fields.key
additional.fields.value_string
Event ID 4739
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = "SETTING"
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DomainName
Data/DomainName
target.administrative_domain
DomainPolicyChanged
Data/DomainPolicyChanged
target.resource.name
PrivilegeList
target.user.attribute.permissions.name
MinPasswordAge
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MaxPasswordAge
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ForceLogoff
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LockoutThreshold
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LockoutObservationWindow
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LockoutDuration
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PasswordProperties
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MinPasswordLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PasswordHistoryLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MachineAccountQuota
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MixedDomainMode
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DomainBehaviorVersion
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OemInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DomainSid
Data/DomainSid
target.user.windows_sid
Event ID 4740
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PERMISSIONS
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
CallerComputerName
src.hostname
Event ID 4741
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_CREATION
target.resource.resource_type = STORAGE_OBJECT
target.resource.resource_subtype = Computer Account
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.user_display_name
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
DnsHostName
Data/DnsHostName
target.asset.hostname
SamAccountName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DisplayName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserPrincipalName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HomeDirectory
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HomePath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ScriptPath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ProfilePath
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserWorkstations
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PasswordLastSet
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AccountExpires
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PrimaryGroupId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AllowedToDelegateTo
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldUacValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewUacValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserAccountControl
target.resource.attribute.labels.key
target.resource.attribute.labels.value
UserAccountControl
Data/UserAccountControl
The
UserAccountControl
raw log field value string is split into individual codes. Each code is translated to a human-readable description. These descriptions are added as key-value pairs to the
target.resource.attribute.labels
repeated field. For each entry, the key is "UserAccountControl_value" and the value is the translated description.
UserParameters
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SidHistory
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LogonHours
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ServicePrincipalNames
target.application
Event ID 4742
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_UPDATE_CONTENT
target.resource.resource_type = STORAGE_OBJECT
target.resource.resource_subtype = Computer Account
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
ServicePrincipalNames
Data/ServicePrincipalNames
target.application
ComputerAccountChange
Data/ComputerAccountChange
additional.fields.key
additional.fields.value_string
UserAccountControl
Data/UserAccountControl
The
UserAccountControl
raw log field value string is split into individual codes. Each code is translated to a human-readable description. These descriptions are added as key-value pairs to the
target.resource.attribute.labels
repeated field. For each entry, the key is "UserAccountControl_value" and the value is the translated description.
Event ID 4743
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4744
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
target.group.attribute.labels.key
target.group.attribute.labels.value
Event ID 4745
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
target.group.attribute.labels.key
target.group.attribute.labels.value
Event ID 4746
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
Data/MembershipExpirationTime
target.user.attribute.labels.key
target.user.attribute.labels.value
Event ID 4747
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4748
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4749
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SamAccountName
target.labels.key/value
SidHistory
target.labels.key/value
Event ID 4750
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SamAccountName
target.labels.key/value
SidHistory
target.labels.key/value
Event ID 4751
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
Data/MembershipExpirationTime
target.user.attribute.labels.key
target.user.attribute.labels.value
Event ID 4752
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
Event ID 4753
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Event ID 4754
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SamAccountName
Data/SamAccountName
additional.fields.key
additional.fields.value_string
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4755
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
additional.fields.key
additional.fields.value_string
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4756
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value.string_value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
Data/MembershipExpirationTime
target.user.attribute.labels.key
target.user.attribute.labels.value
Event ID 4757
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4758
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Event ID 4759
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
target.group.attribute.labels.key
target.group.attribute.labels.value
Event ID 4760
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
target.group.attribute.labels.key
target.group.attribute.labels.value
Event ID 4761
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
Data/MembershipExpirationTime
target.user.attribute.labels.key
target.user.attribute.labels.value
Event ID 4762
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4763
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4764
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
GroupTypeChange
Data/GroupTypeChange
security_result.summary
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
PrivilegeList
target.user.attribute.permissions.name (repeated)
Event ID 4765
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_UPDATE_CONTENT
target.resource.resource_type = SETTING
target.resource.resource_subtype = SID History
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
SourceUserName
Data/SourceUserName
about.user.userid
SourceSid
Data/SourceSid
about.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SidList
Data/SidList
target.user.attribute.labels.key
target.user.attribute.labels.value
Event ID 4766
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_UPDATE_CONTENT
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
SourceUserName
Data/SourceUserName
about.user.userid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Event ID 4767
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PERMISSIONS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4768
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
If LogonType field is missing then extensions.auth.mechanism = MECHANISM_UNSPECIFIED
Set
security_result.action
to
ALLOW
if
Status
contains "0x0"; otherwise, set it to
FAIL
.
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
Status
Data/Status
security_result.description
CertIssuerName
Data/CertIssuerName
security_result.detection_fields.labels.key = cert_issuer_name and value = %{cert_issuer_name}
CertSerialNumber
Data/CertSerialNumber
security_result.detection_fields.labels.key = cert_serial_number and value = %{cert_serial_number}
CertThumbprint
Data/CertThumbprint
security_result.detection_fields.labels.key = cert_thumbprint and value = %{cert_thumbprint}
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
ServiceSid
target.labels.key/value
TicketOptions
target.resource.name
TicketEncryptionType
additional.fields.key and additional.fields.value.string_value
PreAuthType
target.labels.key/value
ResponseTicket
Data/ResponseTicket
security_result.detection_fields.key and security_result.detection_fields.value
AccountSupportedEncryptionTypes
Data/AccountSupportedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
AccountAvailableKeys
Data/AccountAvailableKeys
additional.fields.key and additional.fields.value.string_value
ServiceSupportedEncryptionTypes
Data/ServiceSupportedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
ServiceAvailableKeys
Data/ServiceAvailableKeys
additional.fields.key and additional.fields.value.string_value
DCSupportedEncryptionTypes
Data/DCSupportedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
DCAvailableKeys
Data/DCAvailableKeys
additional.fields.key and additional.fields.value.string_value
ClientAdvertizedEncryptionTypes
Data/ClientAdvertizedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
SessionKeyEncryptionType
Data/SessionKeyEncryptionType
additional.fields.key and additional.fields.value.string_value
PreAuthEncryptionType
Data/PreAuthEncryptionType
additional.fields.key and additional.fields.value.string_value
Hostname
intermediary.hostname
Event ID 4769
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_UNCATEGORIZED
If LogonType field is missing then extensions.auth.mechanism = MECHANISM_UNSPECIFIED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Set
security_result.action
to
ALLOW
if
Status
contains "0x0"; otherwise, set it to
FAIL
.
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
ServiceSid
Data/ServiceSid
target.user.windows_sid
Status
Data/Status
security_result.description
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
TicketOptions
Data/TicketOptions
additional.fields.key and additional.fields.value.string_value
TicketEncryptionType
Data/TicketEncryptionType
additional.fields.key and additional.fields.value.string_value
LogonGuid
Data/LogonGuid
additional.fields.key and additional.fields.value.string_value
TransmittedServices
Data/TransmittedServices
additional.fields.key and additional.fields.value.string_value
ClientAdvertizedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
RequestTicketHash
Data/RequestTicketHash
additional.fields.key and additional.fields.value.string_value
ResponseTicketHash
Data/ResponseTicketHash
additional.fields.key and additional.fields.value.string_value
AccountSupportedEncryptionTypes
Data/AccountSupportedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
AccountAvailableKeys
Data/AccountAvailableKeys
additional.fields.key and additional.fields.value.string_value
ServiceSupportedEncryptionTypes
Data/ServiceSupportedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
ServiceAvailableKeys
Data/ServiceAvailableKeys
additional.fields.key and additional.fields.value.string_value
DCSupportedEncryptionTypes
Data/DCSupportedEncryptionTypes
additional.fields.key and additional.fields.value.string_value
DCAvailableKeys
Data/DCAvailableKeys
additional.fields.key and additional.fields.value.string_value
SessionKeyEncryptionType
Data/SessionKeyEncryptionType
additional.fields.key and additional.fields.value.string_value
Hostname
intermediary.hostname
Event ID 4770
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TicketEncryptionType
Data/TicketEncryptionType
security_result.about.resource.name
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
ServiceSid
target.user.windows_sid
TicketOptions
security_result.about.resource.attribute.labels.key/value
Hostname
intermediary.hostname
Event ID 4771
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
Set
security_result.action
to
ALLOW
if
Status
contains "0x0"; otherwise, set it to
FAIL
.
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
Status
Data/Status
security_result.description
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
TicketOptions
Data/TicketOptions
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
PreAuthType
Data/PreAuthType
additional.fields.key
additional.fields.value_string
CertIssuerName
Data/CertIssuerName
security_result.detection_fields.key
security_result.detection_fields.value
CertSerialNumber
Data/CertSerialNumber
security_result.detection_fields.key
security_result.detection_fields.value
CertThumbprint
Data/CertThumbprint
security_result.detection_fields.key
security_result.detection_fields.value
Hostname
intermediary.hostname
Event ID 4772
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
TicketOptions
Data/TicketOptions
additional.fields.key
additional.fields.value_string
FailureCode
Data/FailureCode
additional.fields.key
additional.fields.value_string
Event ID 4773
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
TicketOptions
Data/TicketOptions
additional.fields.key
additional.fields.value_string
FailureCode
Data/FailureCode
additional.fields.key
additional.fields.value_string
Event ID 4774
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
ClientUserName
Data/ClientUserName
principal.user.userid
MappingBy
Data/MappingBy
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
MappedName
Data/MappedName
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4775
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
ClientUserName
Data/ClientUserName
principal.user.userid
MappingBy
Data/MappingBy
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4776
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
Set
security_result.action
to
ALLOW
if
Status
contains "0x0"; otherwise, set it to
BLOCK
.
Hostname
target.hostname
Workstation
Data/Workstation
The
Workstation
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
Workstation
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
Workstation
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
Workstation
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
Workstation
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
Workstation
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
Status
Data/Status
security_result.description
Format:
Status - Description
TargetUserName
Data/TargetUserName
target.user.userid
Version
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Level
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Task
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Opcode
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
Keywords
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
ThreadID
Data/ThreadID
about.labels.key/value
additional.fields.key
additional.fields.value.string_value
PackageName
Data/PackageName
security_result.about.resource.name
Event ID 4777
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.category = "AUTH_VIOLATION"
security_result.action = FAIL
Status
Data/Status
security_result.summary
Workstation
Data/Workstation
The
Workstation
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
Workstation
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
Workstation
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
Workstation
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
Workstation
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
Workstation
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
TargetUserName
Data/TargetUserName
target.user.userid
ClientUserName
Data/ClientUserName
additional.fields.key
additional.fields.value_string
Event ID 4778
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SessionName
Data/SessionName
network.session_id
AccountDomain
Data/AccountDomain
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
AccountName
Data/AccountName
principal.user.userid
ClientName
Data/ClientName
principal.hostname
principal.asset.hostname
ClientAddress
Data/ClientAddress
principal.ip
Hostname
Computer
target.asset.hostname
target.hostname
LogonID
Data/LogonID
additional.fields.key
additional.fields.value_string
Event ID 4779
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SessionName
Data/SessionName
network.session_id
AccountDomain
Data/AccountDomain
principal.administrative_domain
AccountName
Data/AccountName
principal.user.userid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
ClientAddress
Data/ClientAddress
target.ip
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
LogonID
Data/LogonID
additional.fields.key
additional.fields.value_string
Event ID 4780
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_CHANGE_PERMISSIONS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
Event ID 4781
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_UNCATEGORIZED
security_result.action = ALLOW_WITH_MODIFICATION
OldTargetUserName
Data/OldTargetUserName
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
PrivilegeList
target.user.attribute.permissions.name (repeated)
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
NewTargetUserName
Data/NewTargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
Event ID 4782
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4783
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4784
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4785
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
MembershipExpirationTime
Data/MembershipExpirationTime
additional.fields.key
additional.fields.value_string
Event ID 4786
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4787
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4788
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
MemberName
Data/MemberName
target.user.user_display_name
MemberSid
Data/MemberSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4789
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4790
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4791
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SamAccountName
Data/SamAccountName
target.group.attribute.labels.key
target.group.attribute.labels.value
SidHistory
Data/SidHistory
additional.fields.key
additional.fields.value_string
Event ID 4792
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_DELETION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
PrivilegeList
Data/PrivilegeList
target.group.attribute.permissions.name
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4793
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Status
Data/Status
security_result.summary
Workstation
Data/Workstation
The
Workstation
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
Workstation
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
Workstation
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
Workstation
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
Workstation
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
Workstation
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
TargetUserName
Data/TargetUserName
target.user.userid
Event ID 4794
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_UPDATE_CONTENT
target.resource.resource_type = SETTING
target.resource.name = "Directory Services Restore Mode administrator password"
Set
security_result.action
to
ALLOW
if
Status
contains "0x0"; otherwise, set it to
FAIL
.
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
Workstation
Data/Workstation
The
Workstation
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
Workstation
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
Workstation
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
Workstation
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
Workstation
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
Workstation
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Status
Data/Status
security_result.description
Format:
Status - Description
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4797
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
Workstation
Data/Workstation
The
Workstation
field is mapped to UDM fields based on its format. The following checks are performed in order:
1. If the
Workstation
log field value matches the pattern
^principal_ip:principal_port$
, the extracted principal_ip is mapped to
principal.ip
and the optional principal_port to
principal.port
.
2. Else, if the
Workstation
log field value matches the pattern
principal_hostname\domain_name
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
3. Else, if the
Workstation
log field value matches the pattern
domain_name\principal_hostname
, the extracted
principal_hostname
is mapped to
principal.hostname
. The extracted
domain_name
is mapped to
principal.asset.network_domain
if
SubjectDomainName
is present, otherwise it's mapped to
principal.administrative_domain
.
4. Else, if the
Workstation
log field value matches the pattern
^principal_hostname$
, the extracted
principal_hostname
is mapped to
principal.hostname
.
5. If none of the above patterns match, the original
Workstation
log field value is added to
additional.fields.key
and
additional.fields.value.string_value
.
TargetUserName
Data/TargetUserName
target.user.userid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4798
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
CallerProcessName
Data/CallerProcessName
principal.process.file.full_path
CallerProcessId
Data/CallerProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.userid
Event ID 4799
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
CallerProcessName
Data/CallerProcessName
principal.process.file.full_path
CallerProcessId
Data/CallerProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
Event ID 4800
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
TargetDomainName
Data/TargetDomainName
principal.administrative_domain
TargetUserName
Data/TargetUserName
principal.user.userid
SessionID
about.labels.key
about.labels.value
TargetUserSid
Data/TargetUserSid
principal.user.windows_sid
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4801
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
TargetDomainName
Data/TargetDomainName
principal.administrative_domain
TargetUserName
Data/TargetUserName
principal.user.userid
SessionID
about.labels.key
about.labels.value
TargetUserSid
Data/TargetUserSid
principal.user.windows_sid
TargetLogonId
Data/TargetLogonId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 4816
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
PeerName
Data/PeerName
target.ip
ProtocolSequence
Data/ProtocolSequence
additional.fields.key
additional.fields.value.string_value
SecurityError
Data/SecurityError
security_result.detection_fields.key/value
param1
additional.additional.fields.key
additional.fields.value.string_value
param2
additional.additional.fields.key
additional.fields.value.string_value
param3
additional.additional.fields.key
additional.fields.value.string_value
Event ID 4817
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = "SETTING"
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
OldSd
Data/OldSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewSd
Data/NewSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectName
Data/ObjectName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ObjectServer
Data/ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectType
Data/ObjectType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4818
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
AccessReason
Data/AccessReason
security_result.description
ObjectName
Data/ObjectName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ObjectServer
Data/ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectType
Data/ObjectType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HandleId
Data/HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
StagingReason
Data/StagingReason
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4819
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ObjectServer
Data/ObjectServer
additional.fields.key
additional.fields.value_string
ObjectType
Data/ObjectType
additional.fields.key
additional.fields.value_string
AddedCAPs
Data/AddedCAPs
security_result.detection_fields.key
security_result.detection_fields.value
DeletedCAPs
Data/DeletedCAPs
security_result.detection_fields.key
security_result.detection_fields.value
ModifiedCAPs
Data/ModifiedCAPs
security_result.detection_fields.key
security_result.detection_fields.value
AsIsCAPs
Data/AsIsCAPs
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4820
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = BLOCK
DeviceName
Data/DeviceName
principal.hostname
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
ServiceSid
Data/ServiceSid
additional.fields.key
additional.fields.value_string
TicketOptions
Data/TicketOptions
additional.fields.key
additional.fields.value_string
Status
Data/Status
additional.fields.key
additional.fields.value_string
TicketEncryptionType
Data/TicketEncryptionType
additional.fields.key
additional.fields.value_string
PreAuthType
Data/PreAuthType
additional.fields.key
additional.fields.value_string
CertIssuerName
Data/CertIssuerName
security_result.detection_fields.key
security_result.detection_fields.value
CertSerialNumber
Data/CertSerialNumber
security_result.detection_fields.key
security_result.detection_fields.value
CertThumbprint
Data/CertThumbprint
security_result.detection_fields.key
security_result.detection_fields.value
SiloName
Data/SiloName
security_result.detection_fields.key
security_result.detection_fields.value
PolicyName
Data/PolicyName
security_result.detection_fields.key
security_result.detection_fields.value
TGT Lifetime
Data/TGT Lifetime
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4821
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = BLOCK
DeviceName
Data/DeviceName
principal.hostname
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
TargetDomainName
Data/TargetDomainName
target.administrative_domain
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.user.userid
ServiceSid
Data/ServiceSid
additional.fields.key
additional.fields.value_string
TicketOptions
Data/TicketOptions
additional.fields.key
additional.fields.value_string
TicketEncryptionType
Data/TicketEncryptionType
additional.fields.key
additional.fields.value_string
LogonGuid
Data/LogonGuid
additional.fields.key
additional.fields.value_string
TransitedServices
Data/TransitedServices
additional.fields.key
additional.fields.value_string
SiloName
Data/SiloName
security_result.detection_fields.key
security_result.detection_fields.value
PolicyName
Data/PolicyName
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4822
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_UNCATEGORIZED
security_result.category = AUTH_VIOLATION
security_result.action = FAIL
DeviceName
Data/DeviceName
principal.hostname
AccountName
Data/AccountName
principal.user.userid
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 4823
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_UNCATEGORIZED
security_result.category = AUTH_VIOLATION
security_result.action = FAIL
DeviceName
Data/DeviceName
principal.hostname
AccountName
Data/AccountName
principal.user.userid
Status
Data/Status
additional.fields.key
additional.fields.value_string
SiloName
Data/SiloName
security_result.detection_fields.key
security_result.detection_fields.value
PolicyName
Data/PolicyName
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4824
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_UNCATEGORIZED
security_result.category = AUTH_VIOLATION
security_result.action = FAIL
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
ServiceName
Data/ServiceName
target.application
TargetUserName
Data/TargetUserName
target.group.group_display_name
TargetSid
Data/TargetSid
target.group.windows_sid
TicketOptions
Data/TicketOptions
additional.fields.key
additional.fields.value_string
Status
Data/Status
additional.fields.key
additional.fields.value_string
TicketEncryptionType
Data/TicketEncryptionType
additional.fields.key
additional.fields.value_string
PreAuthType
Data/PreAuthType
additional.fields.key
additional.fields.value_string
CertIssuerName
Data/CertIssuerName
security_result.detection_fields.key
security_result.detection_fields.value
CertSerialNumber
Data/CertSerialNumber
security_result.detection_fields.key
security_result.detection_fields.value
CertThumbprint
Data/CertThumbprint
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4825
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
AccountDomain
Data/AccountDomain
principal.administrative_domain
ClientAddress
Data/ClientAddress
principal.ip
AccountName
Data/AccountName
principal.user.userid
LogonID
Data/LogonID
additional.fields.key
additional.fields.value_string
Event ID 4826
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
LoadOptions
principal.labels.key/value
AdvancedOptions
principal.labels.key/value
ConfigAccessPolicy
principal.labels.key/value
RemoteEventLogging
principal.labels.key/value
KernelDebug
principal.labels.key/value
VsmLaunchType
principal.labels.key/value
TestSigning
principal.labels.key/value
FlightSigning
principal.labels.key/value
DisableIntegrityChecks
principal.labels.key/value
HypervisorLoadOptions
principal.labels.key/value
HypervisorLaunchType
principal.labels.key/value
HypervisorDebug
principal.labels.key/value
Event ID 4830
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetSid
Data/TargetSid
target.user.windows_sid
SourceUserName
Data/SourceUserName
additional.fields.key
additional.fields.value_string
SourceSid
Data/SourceSid
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
PrivilegeList
Data/PrivilegeList
target.user.attribute.permissions.name
SidList
Data/SidList
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4864
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
CollisionTargetType
Data/CollisionTargetType
additional.fields.key
additional.fields.value_string
CollisionTargetName
Data/CollisionTargetName
additional.fields.key
additional.fields.value_string
ForestRoot
Data/ForestRoot
target.resource.name
TopLevelName
Data/TopLevelName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DomainSid
Data/DomainSid
target.user.windows_sid
Flags
Data/Flags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4865
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ForestRoot
Data/ForestRoot
target.resource.name
ForestRootSid
Data/ForestRootSid
target.resource.product_object_id
OperationId
Data/OperationId
target.resource.attribute.labels[Operation ID]
EntryType
Data/EntryType
target.resource.attribute.labels[Entry Type]
Flags
Data/Flags
target.resource.attribute.labels[Flags]
TopLevelName
Data/TopLevelName
target.resource.attribute.labels[Top Level Name]
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels[NetBIOS Name]
DomainSid
Data/DomainSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels[SubjectLogonId]
ForestRoot
Data/ForestRoot
target.resource.name
ForestRootSid
Data/ForestRootSid
target.resource.product_object_id
OperationId
Data/OperationId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
EntryType
Data/EntryType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Flags
Data/Flags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TopLevelName
Data/TopLevelName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DomainSid
Data/DomainSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4866
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ForestRoot
Data/ForestRoot
target.resource.name
ForestRootSid
Data/ForestRootSid
target.resource.product_object_id
OperationId
Data/OperationId
target.resource.attribute.labels[Operation ID]
EntryType
Data/EntryType
target.resource.attribute.labels[Entry Type]
Flags
Data/Flags
target.resource.attribute.labels[Flags]
TopLevelName
Data/TopLevelName
target.resource.attribute.labels[Top Level Name]
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels[NetBIOS Name]
DomainSid
Data/DomainSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels[SubjectLogonId]
ForestRoot
Data/ForestRoot
target.resource.name
ForestRootSid
Data/ForestRootSid
target.resource.product_object_id
OperationId
Data/OperationId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
EntryType
Data/EntryType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Flags
Data/Flags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TopLevelName
Data/TopLevelName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DomainSid
Data/DomainSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4867
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ForestRoot
Data/ForestRoot
target.resource.name
ForestRootSid
Data/ForestRootSid
target.resource.product_object_id
OperationId
Data/OperationId
target.resource.attribute.labels[Operation ID]
EntryType
Data/EntryType
target.resource.attribute.labels[Entry Type]
Flags
Data/Flags
target.resource.attribute.labels[Flags]
TopLevelName
Data/TopLevelName
target.resource.attribute.labels[Top Level Name]
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels[NetBIOS Name]
DomainSid
Data/DomainSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels[SubjectLogonId]
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ForestRoot
Data/ForestRoot
target.resource.name
ForestRootSid
Data/ForestRootSid
target.resource.product_object_id
OperationId
Data/OperationId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
EntryType
Data/EntryType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Flags
Data/Flags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TopLevelName
Data/TopLevelName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DnsName
Data/DnsName
target.hostname
NetbiosName
Data/NetbiosName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DomainSid
Data/DomainSid
target.user.windows_sid
Event ID 4868
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4869
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4870
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RevocationReason
Data/RevocationReason
security_result.description
CertificateSerialNumber
Data/CertificateSerialNumber
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4871
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
NextUpdate
Data/NextUpdate
additional.fields.key
additional.fields.value_string
NextPublishForBaseCRL
Data/NextPublishForBaseCRL
additional.fields.key
additional.fields.value_string
NextPublishForDeltaCRL
Data/NextPublishForDeltaCRL
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4872
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
PublishURLs
Data/PublishURLs
target.file.full_path
IsBaseCRL
Data/IsBaseCRL
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CRLNumber
Data/CRLNumber
target.resource.attribute.labels.key
target.resource.attribute.labels.value
KeyContainer
Data/KeyContainer
target.resource.name
NextPublish
Data/NextPublish
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4873
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ExtensionName
target.resource.name
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
ExtensionDataType
Data/ExtensionDataType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ExtensionPolicyFlags
Data/ExtensionPolicyFlags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ExtensionData
Data/ExtensionData
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4874
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
Attributes
Data/Attributes
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4875
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4876
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
BackupType
Data/BackupType
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4877
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4878
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 4879
Provider: Microsoft-Windows-MSDTC Client 2
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
param1
Data/param1
security_result.summary
Format:
Error Code: %{value}
SourceName
Not available
target.application
param2
Data/param2
target.hostname
Category
Data/Category
security_result.category_details
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 4880
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
CertificateDatabaseHash
Data/CertificateDatabaseHash
security_result.detection_fields.key
security_result.detection_fields.value
PrivateKeyUsageCount
Data/PrivateKeyUsageCount
security_result.detection_fields.key
security_result.detection_fields.value
CACertificateHash
Data/CACertificateHash
security_result.detection_fields.key
security_result.detection_fields.value
CAPublicKeyHash
Data/CAPublicKeyHash
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4881
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
CertificateDatabaseHash
Data/CertificateDatabaseHash
security_result.detection_fields.key
security_result.detection_fields.value
PrivateKeyUsageCount
Data/PrivateKeyUsageCount
security_result.detection_fields.key
security_result.detection_fields.value
CACertificateHash
Data/CACertificateHash
security_result.detection_fields.key
security_result.detection_fields.value
CAPublicKeyHash
Data/CAPublicKeyHash
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4882
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_PERMISSIONS_CHANGE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SecuritySettings
Data/SecuritySettings
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4883
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4884
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Certificate
Data/Certificate
security_result.detection_fields.key
security_result.detection_fields.value
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4885
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
AuditFilter
Data/AuditFilter
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4886
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
RequestId
Data/RequestId
additional.fields.key
additional.fields.value.string_value
Requester
Data/Requester
additional.fields.key
additional.fields.value.string_value
Attributes
Data/Attributes
additional.fields.key
additional.fields.value.string_value
Event ID 4887
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
RequestId
Data/RequestId
additional.fields.key
additional.fields.value.string_value
Requester
Data/Requester
additional.fields.key
additional.fields.value.string_value
Attributes
Data/Attributes
additional.fields.key
additional.fields.value.string_value
Disposition
Data/Disposition
additional.fields.key
additional.fields.value.string_value
SubjectKeyIdentifier
Data/SubjectKeyIdentifier
additional.fields.key
additional.fields.value.string_value
Subject
Data/Subject
additional.fields.key
additional.fields.value.string_value
Event ID 4888
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
Requester
Data/Requester
additional.fields.key
additional.fields.value_string
Attributes
Data/Attributes
additional.fields.key
additional.fields.value_string
Disposition
Data/Disposition
additional.fields.key
additional.fields.value_string
SubjectKeyIdentifier
Data/SubjectKeyIdentifier
additional.fields.key
additional.fields.value_string
Subject
Data/Subject
additional.fields.key
additional.fields.value_string
Event ID 4889
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
Requester
Data/Requester
additional.fields.key
additional.fields.value_string
Attributes
Data/Attributes
additional.fields.key
additional.fields.value_string
Disposition
Data/Disposition
additional.fields.key
additional.fields.value_string
SubjectKeyIdentifier
Data/SubjectKeyIdentifier
additional.fields.key
additional.fields.value_string
Subject
Data/Subject
additional.fields.key
additional.fields.value_string
Event ID 4890
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
EnableRestrictedPermissions
Data/EnableRestrictedPermissions
additional.fields.key
additional.fields.value_string
RestrictedPermissions
Data/RestrictedPermissions
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4891
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Node
Data/Node
target.resource.name
Entry
Data/Entry
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Value
Data/Value
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4892
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
PropertyName
Data/PropertyName
target.resource.name
PropertyIndex
Data/PropertyIndex
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PropertyType
Data/PropertyType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PropertyValue
Data/PropertyValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4893
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
Requester
Data/Requester
principal.user.userid
KRAHashes
Data/KRAHashes
additional.fields.key
additional.fields.value_string
Event ID 4894
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
RequestId
Data/RequestId
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4895
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
CertificateHash
Data/CertificateHash
If the
CertificateHash
log field value matches the regular expression pattern
^[a-f0-9]{32}$
, then the
CertificateHash
log field is mapped to the
network.tls.client.certificate.md5
UDM field.
If the
CertificateHash
log field value matches the regular expression pattern
^[a-f0-9]{64}$
, then the
CertificateHash
log field is mapped to the
network.tls.client.certificate.sha256
UDM field.
If the
CertificateHash
log field value matches the regular expression pattern
^[a-f0-9]{40}$
, then the
CertificateHash
log field is mapped to the
network.tls.client.certificate.sha1
UDM field.
ValidFrom
Data/ValidFrom
network.tls.client.certificate.not_before
ValidTo
Data/ValidTo
network.tls.client.certificate.not_after
Event ID 4896
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TableId
Data/TableId
target.resource.product_object_id
target.resource.resource_type = DATABASE
Filter
Data/Filter
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RowsDeleted
Data/RowsDeleted
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 4897
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
RoleSeparationEnabled
Data/RoleSeparationEnabled
target.resource.name = "Role separation enabled:  %{RoleSeparationEnabled}"
Event ID 4898
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
TemplateInternalName
Data/TemplateInternalName
target.resource.name
Event ID 4899
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
TemplateInternalName
Data/TemplateInternalName
target.resource.name
TemplateOID
target.resource.product_object_id
TemplateVersion
Data/TemplateVersion
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TemplateSchemaVersion
Data/TemplateSchemaVersion
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TemplateDSObjectFQDN
Data/TemplateDSObjectFQDN
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DCDNSName
Data/DCDNSName
about.hostname
NewTemplateContent
Data/NewTemplateContent
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldTemplateContent
Data/OldTemplateContent
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4900
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
TemplateInternalName
Data/TemplateInternalName
target.resource.name
TemplateOID
target.resource.product_object_id
TemplateVersion
Data/TemplateVersion
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TemplateSchemaVersion
Data/TemplateSchemaVersion
target.resource.attribute.labels.key
target.resource.attribute.labels.value
TemplateDSObjectFQDN
Data/TemplateDSObjectFQDN
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DCDNSName
Data/DCDNSName
about.hostname
NewTemplateContent
Data/NewTemplateContent
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewSecurityDescriptor
Data/NewSecurityDescriptor
security_result.detection_fields.key
security_result.detection_fields.value
OldTemplateContent
Data/OldTemplateContent
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldSecurityDescriptor
Data/OldSecurityDescriptor
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4902
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_CREATION
target.resource.resource_type = SETTING
security_result.action = ALLOW
PuaCount
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PuaPolicyId
Data/PuaPolicyId
target.resource.product_object_id
Event ID 4904
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
AuditSourceName
target.application
EventSourceId
target.labels.key
target.labels.value
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Event ID 4905
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
AuditSourceName
target.application
EventSourceId
target.labels.key
target.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Event ID 4906
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
CrashOnAuditFailValue
Data/CrashOnAuditFailValue
security_result.summary
Event ID 4907
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
FILE_MODIFICATION (ObjectType = File, SymbolicLink)
REGISTRY_MODIFICATION (ObjectType = Key)
PROCESS_UNCATEGORIZED (ObjectType = Process)
USER_RESOURCE_UPDATE_PERMISSIONS (ObjectType = all other)
security_result.action = ALLOW_WITH_MODIFICATION
ObjectName
Data/ObjectName
Object Type              | UDM Field
--------------------------+------------------------------------
File, SymbolicLink    |
target.file.full_path
Key                             |
target.registry.registry_key
Process                      |
target.process.file.full_path
Event                          |
target.resource.name
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectType
target.resource.resource_subtype
ProcessName
Data/ProcessName
target.process.command_line
ObjectServer
target.labels.key
target.labels.value
ProcessId
Data/ProcessId
target.process.pid
NewSd
Data/NewSd
target.resource.attribute.labels.key = "NewSd" value in target.resource.attribute.labels.value
OldSd
Data/OldSd
target.resource.attribute.labels.key = "OldSd" value in target.resource.attribute.labels.value
HandleId
target.labels.key/value
Event ID 4908
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SidList
Data/SidList
target.user.group_identifiers
Event ID 4909
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
OldBlockedOrdinals
Data/OldBlockedOrdinals
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewBlockedOrdinals
Data/NewBlockedOrdinals
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4910
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
OldIgnoreDefaultSettings
Data/OldIgnoreDefaultSettings
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewIgnoreDefaultSettings
Data/NewIgnoreDefaultSettings
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldIgnoreLocalSettings
Data/OldIgnoreLocalSettings
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewIgnoreLocalSettings
Data/NewIgnoreLocalSettings
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldBlockedOrdinals
Data/OldBlockedOrdinals
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewBlockedOrdinals
Data/NewBlockedOrdinals
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4911
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
HandleId
target.labels.key/value
ObjectType
target.resource.resource_subtype
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ObjectServer
target.labels.key
target.labels.value
OldSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectName
Data/ObjectName
target.resource.name
Event ID 4912
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
CategoryId
Data/CategoryId
security_result.category_details
SubcategoryId
Data/SubcategoryId
security_result.category_details
SubcategoryGuid
Data/SubcategoryGuid
security_result.detection_fields.key
security_result.detection_fields.value
AuditPolicyChanges
Data/AuditPolicyChanges
security_result.description
Event ID 4913
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectName
Data/ObjectName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ObjectServer
Data/ObjectServer
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectType
Data/ObjectType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HandleId
Data/HandleId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldSd
Data/OldSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewSd
Data/NewSd
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 4928
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW
if
StatusCode
contains "0"; otherwise, set it to
FAIL
SourceAddr
Data/SourceAddr
target.ip or target.hostname
If SourceAddr field value not in IP form then it map to target.hostname
StatusCode
Data/StatusCode
security_result.summary
is set to StatusCode: %{StatusCode}
DestinationDRA
Data/DestinationDRA
additional.fields.key
additional.fields.value_string
SourceDRA
Data/SourceDRA
additional.fields.key
additional.fields.value_string
NamingContext
Data/NamingContext
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
Event ID 4929
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW
if
StatusCode
contains "0"; otherwise, set it to
FAIL
SourceAddr
Data/SourceAddr
target.ip or target.hostname
If SourceAddr field value not in IP form then map to target.hostname
StatusCode
Data/StatusCode
security_result.summary
is set to StatusCode: %{StatusCode}
DestinationDRA
Data/DestinationDRA
additional.fields.key
additional.fields.value_string
SourceDRA
Data/SourceDRA
additional.fields.key
additional.fields.value_string
NamingContext
Data/NamingContext
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
Event ID 4930
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW_WITH_MODIFICATION
if
StatusCode
contains "0"; otherwise, set it to
FAIL
SourceAddr
Data/SourceAddr
target.ip or target.hostname
If SourceAddr field value not in IP form then it map to target.hostname
StatusCode
Data/StatusCode
security_result.summary
is set to StatusCode: %{StatusCode}
DestinationDRA
Data/DestinationDRA
additional.fields.key
additional.fields.value_string
SourceDRA
Data/SourceDRA
additional.fields.key
additional.fields.value_string
NamingContext
Data/NamingContext
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
Event ID 4931
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW_WITH_MODIFICATION
if
StatusCode
contains "0"; otherwise, set it to
FAIL
SourceAddr
Data/SourceAddr
target.ip or target.hostname
If SourceAddr field value not in IP form then it map to target.hostname
StatusCode
Data/StatusCode
security_result.summary
is set to StatusCode: %{StatusCode}
DestinationDRA
Data/DestinationDRA
additional.fields.key
additional.fields.value_string
SourceDRA
Data/SourceDRA
additional.fields.key
additional.fields.value_string
NamingContext
Data/NamingContext
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
Event ID 4932
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
DestinationDRA
Data/DestinationDRA
target.resource.name
SourceDRA
Data/SourceDRA
src.resource.name
NamingContext
Data/NamingContext
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
SessionID
Data/SessionID
network.session_id
StartUSN
Data/StartUSN
additional.fields.key
additional.fields.value_string
Event ID 4933
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Set
security_result.action
to
ALLOW
if
StatusCode
contains "0"; otherwise, set it to
FAIL
StatusCode
Data/StatusCode
security_result.summary
is set to StatusCode: %{StatusCode}
DestinationDRA
Data/DestinationDRA
target.resource.name
SourceDRA
Data/SourceDRA
src.resource.name
NamingContext
Data/NamingContext
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
SessionID
Data/SessionID
network.session_id
EndUSN
Data/EndUSN
additional.fields.key
additional.fields.value_string
Event ID 4934
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
NewValue
target.registry.registry_value_data
SessionID
Data/SessionID
network.session_id
Object
Data/Object
additional.fields.key
additional.fields.value_string
Attribute
Data/Attribute
additional.fields.key
additional.fields.value_string
TypeOfChange
Data/TypeOfChange
additional.fields.key
additional.fields.value_string
USN
Data/USN
additional.fields.key
additional.fields.value_string
StatusCode
Data/StatusCode
security_result.summary
Format:
StatusCode: %{StatusCode}
Event ID 4935
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ReplicationEvent
Data/ReplicationEvent
additional.fields.key
additional.fields.value_string
AuditStatusCode
Data/AuditStatusCode
additional.fields.key
additional.fields.value_string
Event ID 4936
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ReplicationEvent
Data/ReplicationEvent
additional.fields.key
additional.fields.value_string
AuditStatusCode
Data/AuditStatusCode
additional.fields.key
additional.fields.value_string
ReplicationStatusCode
Data/ReplicationStatusCode
additional.fields.key
additional.fields.value_string
Event ID 4937
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
StatusCode
Data/StatusCode
security_result.summary
is set to StatusCode: %{StatusCode}
DestinationDRA
Data/DestinationDRA
target.resource.name
SourceDRA
Data/SourceDRA
src.resource.name
Object
Data/Object
additional.fields.key
additional.fields.value_string
Options
Data/Options
additional.fields.key
additional.fields.value_string
Event ID 4944
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
GroupPolicyApplied
about.labels.key/value
Profile
about.labels.key/value
OperationMode
about.labels.key/value
RemoteAdminEnabled
about.labels.key/value
MulticastFlowsEnabled
about.labels.key/value
LogDroppedPacketsEnabled
about.labels.key/value
LogSuccessfulConnectionsEnabled
about.labels.key/value
Event ID 4945
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.resource.resource_type = "FIREWALL_RULE"
security_result.action = ALLOW
ProfileUsed
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RuleId
Data/RuleId
target.resource.product_object_id
RuleName
Data/RuleName
target.resource.name
Event ID 4946
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RuleName
Data/RuleName
target.resource.name
RuleId
Data/RuleId
target.resource.product_object_id
Event ID 4947
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
ProfileUsed
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RuleId
Data/RuleId
target.resource.product_object_id
RuleName
Data/RuleName
target.resource.name
Event ID 4948
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_DELETION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RuleId
Data/RuleId
target.resource.product_object_id
RuleName
Data/RuleName
target.resource.name
Event ID 4949
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
Event ID 4950
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SettingValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SettingType
Data/SettingType
target.resource.name
Event ID 4951
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
RuleId
Data/RuleId
security_result.rule_id
RuleName
Data/RuleName
security_result.rule_name
Profile
Data/Profile
additional.fields.key
additional.fields.value_string
Event ID 4952
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
RuleId
Data/RuleId
security_result.rule_id
RuleName
Data/RuleName
security_result.rule_name
Profile
Data/Profile
additional.fields.key
additional.fields.value_string
Event ID 4953
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ReasonForRejection
Data/ReasonForRejection
security_result.description
RuleId
Data/RuleId
security_result.rule_id
RuleName
Data/RuleName
security_result.rule_name
Profile
Data/Profile
additional.fields.key
additional.fields.value_string
Event ID 4954
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
Event ID 4956
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
ActiveProfile
target.labels.key
target.labels.value
Event ID 4957
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
RuleId
Data/RuleId
security_result.rule_id
RuleName
Data/RuleName
security_result.rule_name
RuleAttr
Data/RuleAttr
security_result.summary
Event ID 4958
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Reason
Data/Reason
security_result.description
RuleId
Data/RuleId
security_result.rule_id
RuleName
Data/RuleName
security_result.rule_name
Error
Data/Error
security_result.summary
Event ID 4960
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RemoteAddress
Data/RemoteAddress
target.ip
SPI
Data/SPI
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4961
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RemoteAddress
Data/RemoteAddress
target.ip
SPI
Data/SPI
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4962
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RemoteAddress
Data/RemoteAddress
target.ip
SPI
Data/SPI
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4963
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RemoteAddress
Data/RemoteAddress
target.ip
SPI
Data/SPI
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4964
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetDomainName
Data/TargetDomainName
target.administrative_domain
TargetUserName
Data/TargetUserName
target.user.userid
TargetUserSid
Data/TargetUserSid
target.user.windows_sid
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
LogonGuid
Data/LogonGuid
additional.fields.key
additional.fields.value_string
TargetLogonGuid
Data/TargetLogonGuid
additional.fields.key
additional.fields.value_string
SidList
Data/SidList
target.user.group_identifiers
Event ID 4965
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RemoteAddress
Data/RemoteAddress
target.ip
SPI
Data/SPI
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 4976
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
LocalAddress
Data/LocalAddress
principal.ip
RemoteAddress
Data/RemoteAddress
target.ip
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
Event ID 4977
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
LocalAddress
Data/LocalAddress
principal.ip
RemoteAddress
Data/RemoteAddress
target.ip
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
Event ID 4978
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
LocalAddress
Data/LocalAddress
principal.ip
RemoteAddress
Data/RemoteAddress
target.ip
KeyModName
Data/KeyModName
additional.fields.key
additional.fields.value_string
Event ID 4979
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
MMAuthMethod
Data/MMAuthMethod
additional.fields.key
additional.fields.value_string
MMCipherAlg
Data/MMCipherAlg
additional.fields.key
additional.fields.value_string
MMIntegrityAlg
Data/MMIntegrityAlg
additional.fields.key
additional.fields.value_string
DHGroup
Data/DHGroup
additional.fields.key
additional.fields.value_string
MMLifetime
Data/MMLifetime
additional.fields.key
additional.fields.value_string
QMLimit
Data/QMLimit
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
LocalEMPrincipalName
Data/LocalEMPrincipalName
about.hostname
RemoteEMPrincipalName
Data/RemoteEMPrincipalName
about.hostname
EMAuthMethod
Data/EMAuthMethod
additional.fields.key
additional.fields.value_string
EMImpersonationState
Data/EMImpersonationState
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
Event ID 4980
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
MMAuthMethod
Data/MMAuthMethod
additional.fields.key
additional.fields.value_string
MMCipherAlg
Data/MMCipherAlg
additional.fields.key
additional.fields.value_string
MMIntegrityAlg
Data/MMIntegrityAlg
additional.fields.key
additional.fields.value_string
DHGroup
Data/DHGroup
additional.fields.key
additional.fields.value_string
MMLifetime
Data/MMLifetime
additional.fields.key
additional.fields.value_string
QMLimit
Data/QMLimit
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
LocalEMPrincipalName
Data/LocalEMPrincipalName
about.hostname
LocalEMCertHash
Data/LocalEMCertHash
additional.fields.key
additional.fields.value_string
LocalEMIssuingCA
Data/LocalEMIssuingCA
additional.fields.key
additional.fields.value_string
LocalEMRootCA
Data/LocalEMRootCA
additional.fields.key
additional.fields.value_string
RemoteEMPrincipalName
Data/RemoteEMPrincipalName
about.hostname
RemoteEMCertHash
Data/RemoteEMCertHash
additional.fields.key
additional.fields.value_string
RemoteEMIssuingCA
Data/RemoteEMIssuingCA
additional.fields.key
additional.fields.value_string
RemoteEMRootCA
Data/RemoteEMRootCA
additional.fields.key
additional.fields.value_string
EMImpersonationState
Data/EMImpersonationState
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
Event ID 4981
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
LocalMMCertHash
Data/LocalMMCertHash
additional.fields.key
additional.fields.value_string
LocalMMIssuingCA
Data/LocalMMIssuingCA
network.tls.client.certificate.issuer
LocalMMRootCA
Data/LocalMMRootCA
additional.fields.key
additional.fields.value_string
RemoteMMCertHash
Data/RemoteMMCertHash
additional.fields.key
additional.fields.value_string
RemoteMMIssuingCA
Data/RemoteMMIssuingCA
network.tls.server.certificate.issuer
RemoteMMRootCA
Data/RemoteMMRootCA
additional.fields.key
additional.fields.value_string
MMCipherAlg
Data/MMCipherAlg
additional.fields.key
additional.fields.value_string
MMIntegrityAlg
Data/MMIntegrityAlg
additional.fields.key
additional.fields.value_string
DHGroup
Data/DHGroup
additional.fields.key
additional.fields.value_string
MMLifetime
Data/MMLifetime
additional.fields.key
additional.fields.value_string
QMLimit
Data/QMLimit
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
LocalEMPrincipalName
Data/LocalEMPrincipalName
about.hostname
RemoteEMPrincipalName
Data/RemoteEMPrincipalName
about.hostname
EMAuthMethod
Data/EMAuthMethod
additional.fields.key
additional.fields.value_string
EMImpersonationState
Data/EMImpersonationState
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
Event ID 4982
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = ALLOW
LocalMMPrincipalName
Data/LocalMMPrincipalName
principal.hostname
LocalKeyModPort
Data/LocalKeyModPort
principal.port
RemoteMMPrincipalName
Data/RemoteMMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
LocalMMCertHash
Data/LocalMMCertHash
additional.fields.key
additional.fields.value_string
LocalMMIssuingCA
Data/LocalMMIssuingCA
network.tls.client.certificate.issuer
LocalMMRootCA
Data/LocalMMRootCA
additional.fields.key
additional.fields.value_string
RemoteMMCertHash
Data/RemoteMMCertHash
additional.fields.key
additional.fields.value_string
RemoteMMIssuingCA
Data/RemoteMMIssuingCA
network.tls.server.certificate.issuer
RemoteMMRootCA
Data/RemoteMMRootCA
additional.fields.key
additional.fields.value_string
MMCipherAlg
Data/MMCipherAlg
additional.fields.key
additional.fields.value_string
MMIntegrityAlg
Data/MMIntegrityAlg
additional.fields.key
additional.fields.value_string
DHGroup
Data/DHGroup
additional.fields.key
additional.fields.value_string
MMLifetime
Data/MMLifetime
additional.fields.key
additional.fields.value_string
QMLimit
Data/QMLimit
additional.fields.key
additional.fields.value_string
Role
Data/Role
additional.fields.key
additional.fields.value_string
MMImpersonationState
Data/MMImpersonationState
additional.fields.key
additional.fields.value_string
MMFilterID
Data/MMFilterID
additional.fields.key
additional.fields.value_string
MMSAID
Data/MMSAID
additional.fields.key
additional.fields.value_string
LocalEMPrincipalName
Data/LocalEMPrincipalName
about.hostname
LocalEMCertHash
Data/LocalEMCertHash
additional.fields.key
additional.fields.value_string
LocalEMIssuingCA
Data/LocalEMIssuingCA
additional.fields.key
additional.fields.value_string
LocalEMRootCA
Data/LocalEMRootCA
additional.fields.key
additional.fields.value_string
RemoteEMPrincipalName
Data/RemoteEMPrincipalName
about.hostname
RemoteEMCertHash
Data/RemoteEMCertHash
additional.fields.key
additional.fields.value_string
RemoteEMIssuingCA
Data/RemoteEMIssuingCA
additional.fields.key
additional.fields.value_string
RemoteEMRootCA
Data/RemoteEMRootCA
additional.fields.key
additional.fields.value_string
EMImpersonationState
Data/EMImpersonationState
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
Event ID 4983
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = FAIL
LocalEMPrincipalName
Data/LocalEMPrincipalName
principal.hostname
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
FailureReason
Data/FailureReason
security_result.description
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
RemoteEMPrincipalName
Data/RemoteEMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
LocalEMCertHash
Data/LocalEMCertHash
additional.fields.key
additional.fields.value_string
LocalEMIssuingCA
Data/LocalEMIssuingCA
additional.fields.key
additional.fields.value_string
LocalEMRootCA
Data/LocalEMRootCA
additional.fields.key
additional.fields.value_string
RemoteEMCertHash
Data/RemoteEMCertHash
additional.fields.key
additional.fields.value_string
RemoteEMIssuingCA
Data/RemoteEMIssuingCA
additional.fields.key
additional.fields.value_string
RemoteEMRootCA
Data/RemoteEMRootCA
additional.fields.key
additional.fields.value_string
FailurePoint
Data/FailurePoint
security_result.detection_fields.key
security_result.detection_fields.value
State
Data/State
security_result.detection_fields.key
security_result.detection_fields.value
Role
Data/Role
additional.fields.key
additional.fields.value_string
EMImpersonationState
Data/EMImpersonationState
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
Event ID 4984
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = FAIL
LocalEMPrincipalName
Data/LocalEMPrincipalName
principal.hostname
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
LocalAddress
Data/LocalAddress
principal.ip
LocalKeyModPort
Data/LocalKeyModPort
principal.port
FailureReason
Data/FailureReason
security_result.description
RemoteEMPrincipalName
Data/RemoteEMPrincipalName
target.hostname
RemoteAddress
Data/RemoteAddress
target.ip
RemoteKeyModPort
Data/RemoteKeyModPort
target.port
FailurePoint
Data/FailurePoint
security_result.detection_fields.key
security_result.detection_fields.value
EMAuthMethod
Data/EMAuthMethod
additional.fields.key
additional.fields.value_string
State
Data/State
security_result.detection_fields.key
security_result.detection_fields.value
Role
Data/Role
additional.fields.key
additional.fields.value_string
EMImpersonationState
Data/EMImpersonationState
additional.fields.key
additional.fields.value_string
QMFilterID
Data/QMFilterID
additional.fields.key
additional.fields.value_string
Event ID 4985
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ProcessName
Data/ProcessName
principal.process.file.full_path
NewState
target.labels.key
target.labels.value
ResourceManager
target.labels.key
target.labels.value
TransactionId
target.labels.key
target.labels.value
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Event ID 5002
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 5005
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 5007
Provider: Microsoft Antimalware
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 5009
Provider: Microsoft-Windows-WAS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
AppPoolID
target.resource.name
ExitCode
additional.fields.key
additional.fields.value_string
Event ID 5016
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
CSEExtensionName
Data/CSEExtensionName
target.resource.name
CSEExtensionId
Data/CSEExtensionId
target.resource.product_object_id
CSEElaspedTimeInMilliSeconds
Data/CSEElaspedTimeInMilliSeconds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5017
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
OperationDescription
Data/OperationDescription
security_result.description
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
OperationElapsedTimeInMilliSeconds
Data/OperationElapsedTimeInMilliSeconds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Parameter
Data/Parameter
additional.fields.key
additional.fields.value_string
Event ID 5024
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5025
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5027
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
Event ID 5028
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
Event ID 5029
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
Event ID 5030
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
Event ID 5031
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
metadata.event_type = STATUS_UPDATE
and
security_result.action=BLOCK
Profiles
target.labels.key
target.labels.value
Application
Data/Application
target.application
Event ID 5032
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
and
security_result.action=BLOCK
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
Event ID 5033
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5034
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5035
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
ErrorCode
Data/ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5037
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
ErrorCode
Data/ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5038
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_UNCATEGORIZED
security_result.action = FAIL
param1
Data/param1
target.file.full_path
Event ID 5039
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = REGISTRY_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ProcessName
Data/ProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
ObjectPath
Data/ObjectPath
principal.registry.registry_key
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectVirtualPath
Data/ObjectVirtualPath
target.registry.registry_key
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 5040
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
AuthenticationSetName
Data/AuthenticationSetName
target.resource.name
AuthenticationSetId
Data/AuthenticationSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5041
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
AuthenticationSetName
Data/AuthenticationSetName
target.resource.name
AuthenticationSetId
Data/AuthenticationSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5042
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
AuthenticationSetName
Data/AuthenticationSetName
target.resource.name
AuthenticationSetId
Data/AuthenticationSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5043
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
ConnectionSecurityRuleId
Data/ConnectionSecurityRuleId
security_result.rule_id
ConnectionSecurityRuleName
Data/ConnectionSecurityRuleName
security_result.rule_name
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5044
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
ConnectionSecurityRuleId
Data/ConnectionSecurityRuleId
security_result.rule_id
ConnectionSecurityRuleName
Data/ConnectionSecurityRuleName
security_result.rule_name
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5045
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
AuthenticationSetName
Data/AuthenticationSetName
target.resource.name
AuthenticationSetId
Data/AuthenticationSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5046
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
CryptographicSetName
Data/CryptographicSetName
target.resource.name
CryptographicSetId
Data/CryptographicSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5047
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
CryptographicSetName
Data/CryptographicSetName
target.resource.name
CryptographicSetId
Data/CryptographicSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5048
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
security_result.action = ALLOW_WITH_MODIFICATION
CryptographicSetName
Data/CryptographicSetName
target.resource.name
CryptographicSetId
Data/CryptographicSetId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5049
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_DELETION
security_result.action = ALLOW
IpSecSecurityAssociationName
Data/IpSecSecurityAssociationName
target.resource.name
IpSecSecurityAssociationId
Data/IpSecSecurityAssociationId
target.resource.product_object_id
ProfileChanged
Data/ProfileChanged
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5050
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "Windows Firewall"
security_result.action = BLOCK
CallerProcessName
Data/CallerProcessName
principal.process.command_line
ProcessId
Data/ProcessId
principal.process.pid
Publisher
Data/Publisher
additional.fields.key
additional.fields.value_string
Event ID 5051
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
FileName
Data/FileName
principal.file.full_path
ProcessName
Data/ProcessName
principal.process.file.full_path
ProcessId
Data/ProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
VirtualFileName
Data/VirtualFileName
target.file.full_path
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 5056
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Module
Data/Module
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5057
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_UNCATEGORIZED
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Reason
Data/Reason
security_result.description
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ProviderName
Data/ProviderName
additional.fields.key
additional.fields.value_string
AlgorithmName
Data/AlgorithmName
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5058
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_UNCATEGORIZED
Set
security_result.action
to
ALLOW
if
ReturnCode
contains "0x0"; otherwise, set it to
FAIL
.
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
KeyUserPath
Data/KeyFilePath
target.file.full_path and security_result.about.file.full_path
KeyName
Data/KeyName
target.resource.name
ProviderName
Data/ProviderName
target.resource.attribute.labels.key/value
AlgorithmName
Data/AlgorithmName
target.resource.attribute.labels.key/value
KeyType
Data/KeyType
target.resource.attribute.labels.key/value
ReturnCode
Data/ReturnCode
target.labels.key/value
Operation
Data/Operation
target.resource.attribute.labels.key/value
version 1 /
NXLog field
Event Viewer field
UDM field
ClientProcessId
Data/ClientProcessId
principal.process.pid
ClientCreationTime
Data/ClientCreationTime
principal.labels.key/value
Event ID 5059
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
Set
security_result.action
to
ALLOW
if
ReturnCode
contains "0x0"; otherwise, set it to
FAIL
.
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ReturnCode
Data/ReturnCode
security_result.summary
Format:
Error Code - %{value}
KeyName
Data/KeyName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ProviderName
Data/ProviderName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AlgorithmName
Data/AlgorithmName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
KeyType
Data/KeyType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Operation
Data/Operation
additional.fields.key
additional.fields.value_string
version 1 /
NXLog field
Event Viewer field
UDM field
ClientProcessId
Data/ClientProcessId
target.process.pid
ClientCreationTime
Data/ClientCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5060
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_UNCATEGORIZED
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Reason
Data/Reason
security_result.description
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ProviderName
Data/ProviderName
additional.fields.key
additional.fields.value_string
AlgorithmName
Data/AlgorithmName
additional.fields.key
additional.fields.value_string
KeyName
Data/KeyName
additional.fields.key
additional.fields.value_string
KeyType
Data/KeyType
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5061
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
Set
security_result.action
to
ALLOW
if
ReturnCode
contains "0x0"; otherwise, set it to
FAIL
.
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
Operation
Data/Operation
security_result.description
ReturnCode
Data/ReturnCode
security_result.summary
Format:
Return Code - %{value}
KeyName
Data/KeyName
target.resource.name
AlgorithmName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
KeyName
target.resource.name
KeyType
target.resource.resource_subtype
Event ID 5062
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Module
Data/Module
target.resource.name
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5063
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ModuleName
Data/ModuleName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ProviderName
Data/ProviderName
additional.fields.key
additional.fields.value_string
Operation
Data/Operation
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5064
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
additional.fields.key
additional.fields.value_string
ContextName
Data/ContextName
additional.fields.key
additional.fields.value_string
Operation
Data/Operation
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5065
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ContextName
Data/ContextName
target.resource.name
OldValue
Data/OldValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewValue
Data/NewValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5066
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ContextName
Data/ContextName
target.resource.name
InterfaceId
Data/InterfaceId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
FunctionName
Data/FunctionName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Position
Data/Position
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Operation
Data/Operation
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5067
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ContextName
Data/ContextName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
InterfaceId
Data/InterfaceId
target.resource.product_object_id
FunctionName
Data/FunctionName
target.resource.name
OldValue
Data/OldValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewValue
Data/NewValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5068
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ContextName
Data/ContextName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
InterfaceId
Data/InterfaceId
target.resource.product_object_id
FunctionName
Data/FunctionName
target.resource.name
ProviderName
Data/ProviderName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Position
Data/Position
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Operation
Data/Operation
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5069
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ContextName
Data/ContextName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
InterfaceId
Data/InterfaceId
target.resource.product_object_id
FunctionName
Data/FunctionName
target.resource.name
PropertyName
Data/PropertyName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Operation
Data/Operation
additional.fields.key
additional.fields.value_string
Value
Data/Value
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5070
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Scope
Data/Scope
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ContextName
Data/ContextName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
InterfaceId
Data/InterfaceId
target.resource.product_object_id
FunctionName
Data/FunctionName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PropertyName
Data/PropertyName
target.resource.name
OldValue
Data/OldValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewValue
Data/NewValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ReturnCode
Data/ReturnCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5071
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SecurityDescriptor
Data/SecurityDescriptor
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5074
Provider: Microsoft-Windows-WAS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_process_pid set to target.process.pid
AppPoolID
target.resource.name
Event ID 5077
Provider: Microsoft-Windows-WAS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_process_pid set to target.process.pid
AppPoolID
target.resource.name
Event ID 5116
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
GpsvcInitTimeElapsedInMilliseconds
Data/GpsvcInitTimeElapsedInMilliseconds
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 5117
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
SessionTimeElapsedInMilliseconds
Data/SessionTimeElapsedInMilliseconds
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 5120
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5121
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5122
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
CAConfigurationId
Data/CAConfigurationId
additional.fields.key
additional.fields.value_string
NewValue
Data/NewValue
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
NewValue
Data/NewValue
additional.fields.key
additional.fields.value_string
Event ID 5123
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
PropertyName
Data/PropertyName
target.resource.name
NewValue
Data/NewValue
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 5124
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
NewSecuritySettings
Data/NewSecuritySettings
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 5125
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
SerialNumber
Data/SerialNumber
network.tls.client.certificate.serial
CAName
Data/CAName
network.tls.client.certificate.issuer
Status
Data/Status
additional.fields.key
additional.fields.value_string
Event ID 5126
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsBackgroundProcessing
Data/IsBackgroundProcessing
security_result.rule_labels.key
security_result.rule_labels.value
IsAsyncProcessing
Data/IsAsyncProcessing
security_result.rule_labels.key
security_result.rule_labels.value
NumberOfGPOsDownloaded
Data/NumberOfGPOsDownloaded
security_result.rule_labels.key
security_result.rule_labels.value
NumberOfGPOsApplicable
Data/NumberOfGPOsApplicable
security_result.rule_labels.key
security_result.rule_labels.value
GPODownloadTimeElapsedInMilliseconds
Data/GPODownloadTimeElapsedInMilliseconds
security_result.rule_labels.key
security_result.rule_labels.value
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
security_result.action = ALLOW_WITH_MODIFICATION
CAConfigurationId
Data/CAConfigurationId
additional.fields.key
additional.fields.value_string
NewSigningCertificateHash
Data/NewSigningCertificateHash
additional.fields.key
additional.fields.value_string
Event ID 5127
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
security_result.action = ALLOW_WITH_MODIFICATION
CAConfigurationId
Data/CAConfigurationId
additional.fields.key
additional.fields.value_string
BaseCRLNumber
Data/BaseCRLNumber
additional.fields.key
additional.fields.value_string
BaseCRLThisUpdate
Data/BaseCRLThisUpdate
additional.fields.key
additional.fields.value_string
BaseCRLHash
Data/BaseCRLHash
additional.fields.key
additional.fields.value_string
DeltaCRLNumber
Data/DeltaCRLNumber
additional.fields.key
additional.fields.value_string
DeltaCRLIndicator
Data/DeltaCRLIndicator
additional.fields.key
additional.fields.value_string
DeltaCRLThisUpdate
Data/DeltaCRLThisUpdate
additional.fields.key
additional.fields.value_string
DeltaCRLHash
Data/DeltaCRLHash
additional.fields.key
additional.fields.value_string
Event ID 5136
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_MODIFICATION (ObjectClass="group")
metadata.event_type = USER_RESOURCE_UPDATE_CONTENT (other ObjectClass)
security_result.action = ALLOW_WITH_MODIFICATION
ObjectGUID
Data/ObjectGUID
based on type of object class.
target.group.product_object_id (ObjectClass="group")
target.resource.product_object_id (other ObjectClass)
AttributeValue
Data/AttributeValue
If
AttributeLDAPDisplayName
is "member" then attribute_value set to
target.user.user_display_name
, else attribute_value set to
target.resource.name
ObjectDN
Data/ObjectDN
If
ObjectClass
is "group" then object_name set to
target.group.group_display_name
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
OperationType
about.labels.key
about.labels.value
DSName
target.administrative_domain
OpCorrelationID
about.labels.key/value
AppCorrelationID
about.labels.key/value
DSType
target.labels.key/value
ObjectClass
target.labels.key/value
AttributeLDAPDisplayName
about.labels.key/value
AttributeSyntaxOID
about.labels.key/value
Event ID 5137
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  SETTING_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectGUID
Data/ObjectGUID
target.resource.product_object_id
DSName
Data/DSName
target.administrative_domain
DSType
Data/DSType
target.application
OpCorrelationID
about.labels.key/value
AppCorrelationID
about.labels.key/value
ObjectDN
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
ObjectClass
target.labels.key/value
Event ID 5138
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  SETTING_CREATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectGUID
Data/ObjectGUID
target.resource.product_object_id
OpCorrelationID
Data/OpCorrelationID
additional.fields.key
additional.fields.value_string
AppCorrelationID
Data/AppCorrelationID
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
DSName
Data/DSName
target.administrative_domain
DSType
Data/DSType
additional.fields.key
additional.fields.value_string
OldObjectDN
Data/OldObjectDN
additional.fields.key
additional.fields.value_string
NewObjectDN
Data/NewObjectDN
additional.fields.key
additional.fields.value_string
ObjectClass
Data/ObjectClass
additional.fields.key
additional.fields.value_string
Event ID 5139
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  SETTING_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectGUID
Data/ObjectGUID
target.resource.product_object_id
OldObjectDN
Data/OldObjectDN
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
NewObjectDN
Data/NewObjectDN
additional.fields.key
additional.fields.value.string_value
If
ObjectClass
= "computer", object_name is set to
target.hostname
If
ObjectClass
= "user", object_name is set to
target.user.user_display_name
.
If
ObjectClass
= "group", object_name is set to
target.group.group_display_name
.
ObjectClass
Data/ObjectClass
additional.fields.key
additional.fields.value.string_value
OpCorrelationID
Data/OpCorrelationID
additional.fields.key
additional.fields.value_string
AppCorrelationID
Data/AppCorrelationID
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
DSName
Data/DSName
target.administrative_domain
DSType
Data/DSType
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-WAS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_process_pid set to target.process.pid
ProtocolID
network.application_protocol
AppPoolID
target.resource.name
param3
additional.fields.key
additional.fields.value_string
Event ID 5140
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ShareName
Data/ShareName
target.resource.name
Hostname
target.hostname
version 1 /
NXLog field
Event Viewer field
UDM field
ShareLocalPath
Data/ShareLocalPath
target.file.full_path
AccessList
Data/AccessList
target.resource.attribute.permissions.name
AccessMask
Data/AccessMask
principal.process.access_mask
Event ID 5141
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_DELETION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
additional.fields.key
additional.fields.value.string_value
ObjectGUID
Data/ObjectGUID
target.resource.product_object_id
ObjectClass
Data/ObjectClass
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
ObjectDN
Data/ObjectDN
If
ObjectClass
== "group" then
object_name is set to
target.group.group_display_name
If
ObjectClass
= "computer", then
object_name is set to
target.hostname
If
ObjectClass
= "user", then
object_name is set to
target.user.user_display_name
else
ObjectDN
is set to
target.labels.key/value
ObjectClass
is set to
target.labels.key/value
ObjectDN
is set to
additional.fields.key
and
additional.fields.value.string_value
ObjectClass
is set to
additional.fields.key
and
additional.fields.value.string_value
ObjectDN
Data/ObjectDN
additional.fields.key
additional.fields.value.string_value
DSName
Data/DSName
target.administrative_domain
DSType
Data/DSType
target.application
OpCorrelationID
about.labels.key/value
AppCorrelationID
about.labels.key/value
TreeDelete
Data/TreeDelete
additional.fields.key
additional.fields.value_string
Event ID 5142
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  USER_RESOURCE_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ShareName
Data/ShareName
target.resource.name
Data/ShareLocalPath
target.file.full_path
Event ID 5143
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  USER_RESOURCE_UPDATE_CONTENT
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ShareLocalPath
Data/ShareLocalPath
target.file.full_path
ShareName
Data/ShareName
target.resource.name
OldRemark
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewRemark
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldMaxUsers
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewMaxUsers
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldShareFlags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewShareFlags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OldSD
target.resource.attribute.labels.key
target.resource.attribute.labels.value
NewSD
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectType
target.resource.resource_subtype
Event ID 5144
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =  USER_RESOURCE_DELETION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ShareLocalPath
Data/ShareLocalPath
target.file.full_path
ShareName
Data/ShareName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Event ID 5145
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
IpAddress
Data/IpAddress
principal.ip
IpPort
Data/IpPort
principal.port
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
AccessReason
Data/AccessReason
security_result.description
ShareLocalPath
Data/ShareLocalPath
target.file.full_path
AccessList
Data/AccessList
target.resource.attribute.permissions.name
ShareName
Data/ShareName
target.resource.name
RelativeTargetName
Data/RelativeTargetName
target.file.names
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
AccessMask
Data/AccessMask
principal.process.access_mask
Event ID 5146
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = BLOCK
Direction
Data/Direction
network.direction
EtherType
Data/EtherType
network.ip_protocol
SourceAddress
Data/SourceAddress
principal.ip
SourcevSwitchPort
Data/SourcevSwitchPort
principal.port
DestAddress
Data/DestAddress
target.ip
DestinationvSwitchPort
Data/DestinationvSwitchPort
target.port
VlanTag
Data/VlanTag
security_result.detection_fields.key
security_result.detection_fields.value
vSwitch ID
Data/vSwitch ID
security_result.detection_fields.key
security_result.detection_fields.value
FilterRTID
Data/FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
vSwitch ID
Data/LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5147
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = BLOCK
Direction
Data/Direction
network.direction
EtherType
Data/EtherType
network.ip_protocol
SourceAddress
Data/SourceAddress
principal.ip
DestAddress
Data/DestAddress
target.ip
VlanTag
Data/VlanTag
security_result.detection_fields.key
security_result.detection_fields.value
vSwitch ID
Data/vSwitch ID
security_result.detection_fields.key
security_result.detection_fields.value
SourcevSwitchPort
Data/SourcevSwitchPort
principal.port
DestinationvSwitchPort
Data/DestinationvSwitchPort
target.port
FilterRTID
Data/FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
Data/LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5148
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.category=NETWORK_DENIAL_OF_SERVICE
security_result.action = BLOCK
Type
Data/Type
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5149
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Type
Data/Type
security_result.detection_fields.key
security_result.detection_fields.value
PacketsDiscarded
Data/PacketsDiscarded
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5150
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = BLOCK
Direction
Data/Direction
network.direction
EtherType
Data/EtherType
network.ip_protocol
SourceAddress
Data/SourceAddress
principal.ip
DestAddress
Data/DestAddress
target.ip
MediaType
Data/MediaType
security_result.detection_fields.key
security_result.detection_fields.value
InterfaceType
Data/InterfaceType
security_result.detection_fields.key
security_result.detection_fields.value
VlanTag
Data/VlanTag
security_result.detection_fields.key
security_result.detection_fields.value
FilterRTID
Data/FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
Data/LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5151
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = BLOCK
Direction
Data/Direction
network.direction
EtherType
Data/EtherType
network.ip_protocol
SourceAddress
Data/SourceAddress
principal.ip
DestAddress
Data/DestAddress
target.ip
MediaType
Data/MediaType
security_result.detection_fields.key
security_result.detection_fields.value
InterfaceType
Data/InterfaceType
security_result.detection_fields.key
security_result.detection_fields.value
VlanTag
Data/VlanTag
security_result.detection_fields.key
security_result.detection_fields.value
FilterRTID
Data/FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
Data/LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5152
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
security_result.action = BLOCK
Direction
Data/Direction
network.direction
Protocol
Data/Protocol
network.ip_protocol
Application
Data/Application
principal.application
SourceAddress
Data/SourceAddress
principal.ip
SourcePort
Data/SourcePort
principal.port
ProcessId
Data/ProcessId
principal.process.pid
FilterRTID
Data/FilterRTID
security_result.detection_fields.key/value
LayerName
Data/LayerName
security_result.detection_fields.key/value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key/value
DestAddress
Data/DestAddress
target.ip
DestPort
Data/DestPort
target.port
version 1 / Windows 11 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
FilterOrigin
Data/FilterOrigin
security_result.detection_fields.key/value
Event ID 5153
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
security_result.action = BLOCK
Direction
Data/Direction
network.direction
Protocol
Data/Protocol
network.ip_protocol
SourceAddress
Data/SourceAddress
principal.ip
SourcePort
Data/SourcePort
principal.port
ProcessId
Data/ProcessId
principal.process.pid
Application
Data/Application
target.application
FilterRTID
Data/FilterRTID
security_result.detection_fields.key/value
LayerName
Data/LayerName
security_result.detection_fields.key/value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key/value
DestAddress
Data/DestAddress
target.ip
DestPort
Data/DestPort
target.port
version 1 / Windows 11 and Windows Server 2022/
NXLog field
Event Viewer field
UDM field
FilterOrigin
Data/FilterOrigin
security_result.detection_fields.key/value
Event ID 5154
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Protocol
Data/Protocol
network.ip_protocol
FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Application
Data/Application
target.application
SourceAddress
Data/SourceAddress
target.ip
SourcePort
Data/SourcePort
target.port
ProcessId
Data/ProcessId
target.process.pid
Event ID 5155
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
Protocol
Data/Protocol
network.ip_protocol
SourceAddress
Data/SourceAddress
principal.ip
SourcePort
Data/SourcePort
principal.port
ProcessId
Data/ProcessId
principal.process.pid
Application
Data/Application
target.application
FilterRTID
Data/FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
Data/LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5156
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
security_result.action = ALLOW
Direction
Data/Direction
network.direction
Protocol
Data/Protocol
network.ip_protocol
Application
Data/Application
principal.application
SourceAddress
Data/SourceAddress
principal.ip
SourcePort
Data/SourcePort
principal.port
ProcessId
Data/ProcessId
principal.process.pid
FilterRTID
Data/FilterRTID
security_result.detection_fields.key/value
LayerName
Data/LayerName
security_result.detection_fields.key/value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key/value
DestAddress
Data/DestAddress
target.ip
DestPort
Data/DestPort
target.port
version 1 /
NXLog field
Event Viewer field
UDM field
RemoteUserID
Data/RemoteUserID
target.user.userid
RemoteMachineID
Data/RemoteMachineID
target.user.windows_sid
Event ID 5157
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
security_result.action = BLOCK
Direction
Data/Direction
network.direction
Protocol
Data/Protocol
network.ip_protocol
Application
Data/Application
principal.application
SourceAddress
Data/SourceAddress
principal.ip
SourcePort
Data/SourcePort
principal.port
ProcessId
Data/ProcessId
principal.process.pid
DestAddress
Data/DestAddress
target.ip
DestPort
Data/DestPort
target.port
FilterRTID
Data/FilterRTID
security_result.detection_fields.key/value
LayerName
Data/LayerName
security_result.detection_fields.key/value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key/value
version 1 /
NXLog field
Event Viewer field
UDM field
FilterOrigin
Data/FilterOrigin
security_result.detection_fields.key/value
RemoteUserID
Data/RemoteUserID
target.user.userid
RemoteMachineID
Data/RemoteMachineID
target.user.windows_sid
version 3 /
NXLog field
Event Viewer field
UDM field
OriginalProfile
Data/OriginalProfile
security_result.detection_fields.key
security_result.detection_fields.value
CurrentProfile
Data/CurrentProfile
security_result.detection_fields.key
security_result.detection_fields.value
IsLoopback
Data/IsLoopback
security_result.detection_fields.key
security_result.detection_fields.value
HasRemoteDynamicKeywordAddress
Data/HasRemoteDynamicKeywordAddress
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5158
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Protocol
Data/Protocol
network.ip_protocol
FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Application
Data/Application
target.application
SourceAddress
Data/SourceAddress
target.ip
SourcePort
Data/SourcePort
target.port
ProcessId
Data/ProcessId
target.process.pid
Event ID 5159
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
Protocol
Data/Protocol
network.ip_protocol
Application
Data/Application
target.application
SourceAddress
Data/SourceAddress
target.ip
SourcePort
Data/SourcePort
target.port
ProcessId
Data/ProcessId
target.process.pid
FilterRTID
Data/FilterRTID
security_result.detection_fields.key
security_result.detection_fields.value
LayerName
Data/LayerName
security_result.detection_fields.key
security_result.detection_fields.value
LayerRTID
Data/LayerRTID
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5168
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
IpAddresses
Data/IpAddresses
target.ip
ErrorCode
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SpnName
Data/SpnName
target.resource.name
ServerNames
Data/ServerNames
additional.fields.key
additional.fields.value_string
ConfiguredNames
Data/ConfiguredNames
additional.fields.key
additional.fields.value_string
Event ID 5169
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
DSName
Data/DSName
target.application
ObjectGUID
Data/ObjectGUID
target.resource.product_object_id
OpCorrelationID
Data/OpCorrelationID
additional.fields.key
additional.fields.value_string
AppCorrelationID
Data/AppCorrelationID
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
DSType
Data/DSType
additional.fields.key
additional.fields.value_string
ObjectDN
Data/ObjectDN
target.resource.name
ObjectClass
Data/ObjectClass
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AttributeLDAPDisplayName
Data/AttributeLDAPDisplayName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AttributeSyntaxOID
Data/AttributeSyntaxOID
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AttributeValue
Data/AttributeValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ExpirationTime
Data/ExpirationTime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OperationType
Data/OperationType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5170
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
DSName
Data/DSName
target.application
ObjectGUID
Data/ObjectGUID
target.resource.product_object_id
OpCorrelationID
Data/OpCorrelationID
additional.fields.key
additional.fields.value_string
AppCorrelationID
Data/AppCorrelationID
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
DSType
Data/DSType
additional.fields.key
additional.fields.value_string
ObjectDN
Data/ObjectDN
target.resource.name
ObjectClass
Data/ObjectClass
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AttributeLDAPDisplayName
Data/AttributeLDAPDisplayName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AttributeSyntaxOID
Data/AttributeSyntaxOID
target.resource.attribute.labels.key
target.resource.attribute.labels.value
AttributeValue
Data/AttributeValue
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ExpirationTime
Data/ExpirationTime
target.resource.attribute.labels.key
target.resource.attribute.labels.value
OperationType
Data/OperationType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5186
Provider: Microsoft-Windows-WAS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
AppPoolID
target.resource.name
Minutes
additional.fields.key
additional.fields.value_string
Event ID 5257
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
PolicyDownloadTimeElapsedInMilliseconds
Data/PolicyDownloadTimeElapsedInMilliseconds
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 5308
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DCName
Data/DCName
target.administrative_domain
DCIPAddress
Data/DCIPAddress
target.ip
Event ID 5309
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
MachineRole
Data/MachineRole
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5310
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
PrincipalCNName
Data/PrincipalCNName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
DCDomainName
Data/DCDomainName
target.administrative_domain
DCName
Data/DCName
target.hostname
PrincipalDomainName
Data/PrincipalDomainName
additional.fields.key
additional.fields.value_string
Event ID 5311
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
PolicyProcessingMode
Data/PolicyProcessingMode
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5312
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DescriptionString
Data/DescriptionString
security_result.description
GPOInfoList
Data/GPOInfoList
target.resource.name
Event ID 5313
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
DescriptionString
Data/DescriptionString
security_result.description
GPOInfoList
Data/GPOInfoList
target.resource.name
Event ID 5314
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
LinkDescription
Data/LinkDescription
security_result.description
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
PolicyApplicationMode
Data/PolicyApplicationMode
target.resource.attribute.labels.key
target.resource.attribute.labels.value
BandwidthInkbps
Data/BandwidthInkbps
security_result.detection_fields.key
security_result.detection_fields.value
IsSlowLink
Data/IsSlowLink
security_result.detection_fields.key
security_result.detection_fields.value
ThresholdInkbps
Data/ThresholdInkbps
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5315
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
PrincipalSamName
Data/PrincipalSamName
target.hostname
NextPolicyApplicationTime
Data/NextPolicyApplicationTime
security_result.rule_labels.key
security_result.rule_labels.value
NextPolicyApplicationTimeUnit
Data/NextPolicyApplicationTimeUnit
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 5320
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
InfoDescription
Data/InfoDescription
security_result.description
Event ID 5321
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
InfoDescription
Data/InfoDescription
security_result.description
OperationParameter1
Data/OperationParameter1
target.resource.product_object_id
Event ID 5324
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
SessionId
Data/SessionId
network.session_id
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
NotificationType
Data/NotificationType
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 5326
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
DCDiscoveryTimeInMilliSeconds
Data/DCDiscoveryTimeInMilliSeconds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5327
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
NetworkBandwidthInKbps
Data/NetworkBandwidthInKbps
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5340
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
PolicyApplicationMode
Data/PolicyApplicationMode
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5351
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
WinlogonReturnTimeElapsedInMilliseconds
Data/WinlogonReturnTimeElapsedInMilliseconds
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 5376
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
BackupFileName
Data/BackupFileName
target.file.full_path
ClientProcessId
Data/ClientProcessId
target.process.pid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
ProcessCreationTime
Data/ProcessCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5377
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
BackupFileName
Data/BackupFileName
target.file.full_path
ClientProcessId
Data/ClientProcessId
target.process.pid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
ProcessCreationTime
Data/ProcessCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5378
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
and
security_result.category=POLICY_VIOLATION
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
TargetServer
Data/TargetServer
target.hostname
UserUPN
Data/UserUPN
target.user.userid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Package
Data/Package
additional.fields.key
additional.fields.value_string
CredType
Data/CredType
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5379
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = RESOURCE_READ
target.resource.name = Credential Manager credentials
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClientProcessId
Data/ClientProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
TargetName
Data/TargetName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Type
Data/Type
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CountOfCredentialsReturned
Data/CountOfCredentialsReturned
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ReadOperation
Data/ReadOperation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ReturnCode
Data/ReturnCode
additional.fields.key
additional.fields.value_string
ProcessCreationTime
Data/ProcessCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5380
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClientProcessId
Data/ClientProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SearchString
Data/SearchString
additional.fields.key
additional.fields.value_string
SchemaFriendlyName
Data/SchemaFriendlyName
additional.fields.key
additional.fields.value_string
Schema
Data/Schema
additional.fields.key
additional.fields.value_string
CountOfCredentialsReturned
Data/CountOfCredentialsReturned
additional.fields.key
additional.fields.value_string
ProcessCreationTime
Data/ProcessCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5381
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClientProcessId
Data/ClientProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
Flags
Data/Flags
additional.fields.key
additional.fields.value_string
CountOfCredentialsReturned
Data/CountOfCredentialsReturned
additional.fields.key
additional.fields.value_string
ProcessCreationTime
Data/ProcessCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5382
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClientProcessId
Data/ClientProcessId
principal.process.pid
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
Resource
Data/Resource
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
SchemaFriendlyName
Data/SchemaFriendlyName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Schema
Data/Schema
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Identity
Data/Identity
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PackageSid
Data/PackageSid
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Flags
Data/Flags
additional.fields.key
additional.fields.value_string
ReturnCode
Data/ReturnCode
additional.fields.key
additional.fields.value_string
ProcessCreationTime
Data/ProcessCreationTime
additional.fields.key
additional.fields.value_string
Event ID 5440
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutKey
Data/CalloutKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutName
Data/CalloutName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutType
Data/CalloutType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutId
Data/CalloutId
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerKey
Data/LayerKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerName
Data/LayerName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerId
Data/LayerId
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5441
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
FilterKey
Data/FilterKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
FilterName
Data/FilterName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
FilterType
Data/FilterType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
FilterId
Data/FilterId
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerKey
Data/LayerKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerName
Data/LayerName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerId
Data/LayerId
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Weight
Data/Weight
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Conditions
Data/Conditions
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Action
Data/Action
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutKey
Data/CalloutKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutName
Data/CalloutName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5442
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderType
Data/ProviderType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5443
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProviderKey
Data/ProviderKey
additional.fields.key
additional.fields.value_string
ProviderName
Data/ProviderName
additional.fields.key
additional.fields.value_string
ProviderContextKey
Data/ProviderContextKey
additional.fields.key
additional.fields.value_string
ProviderContextName
Data/ProviderContextName
additional.fields.key
additional.fields.value_string
ProviderContextType
Data/ProviderContextType
additional.fields.key
additional.fields.value_string
Event ID 5444
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProviderKey
Data/ProviderKey
about.resource.product_object_id
ProviderName
Data/ProviderName
about.resource.name
SubLayerKey
Data/SubLayerKey
about.resource.product_object_id
SubLayerName
Data/SubLayerName
about.resource.name
SubLayerType
Data/SubLayerType
about.resource.attribute.labels.key
about.resource.attribute.labels.value
Weight
Data/Weight
about.resource.attribute.labels.key
about.resource.attribute.labels.value
Event ID 5446
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
ProcessId
Data/ProcessId
principal.process.pid
UserName
Data/UserName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ChangeType
Data/ChangeType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutKey
Data/CalloutKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutName
Data/CalloutName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutType
Data/CalloutType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
CalloutId
Data/CalloutId
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerKey
Data/LayerKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerName
Data/LayerName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
LayerId
Data/LayerId
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5447
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type set to SETTING
security_result.action = ALLOW_WITH_MODIFICATION
ProviderKey
Data/ProviderKey
about.resource.attribute.labels.key / value
ProviderName
Data/ProviderName
about.resource.attribute.labels.key / value
ChangeType
Data/ChangeType
about.resource.attribute.labels.key / value
FilterKey
Data/FilterKey
about.resource.attribute.labels.key / value
FilterType
Data/FilterType
about.resource.attribute.labels.key / value
LayerKey
Data/LayerKey
about.resource.attribute.labels.key / value
LayerName
Data/LayerName
about.resource.attribute.labels.key / value
LayerId
Data/LayerId
about.resource.attribute.labels.key / value
Weight
Data/Weight
about.resource.attribute.labels.key / value
Conditions
Data/Conditions
about.resource.attribute.labels.key / value
Action
Data/Action
about.resource.attribute.labels.key / value
CalloutKey
Data/CalloutKey
about.resource.attribute.labels.key / value
CalloutName
Data/CalloutName
about.resource.attribute.labels.key / value
Data/ProcessId
principal.process.pid
UserName
Data/UserName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
FilterName
Data/FilterName
target.resource.name
FilterId
Data/FilterId
target.resource.product_object_id
Event ID 5448
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
ProcessId
Data/ProcessId
principal.process.pid
UserName
Data/UserName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
ChangeType
Data/ChangeType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderType
Data/ProviderType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5449
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
ProcessId
Data/ProcessId
principal.process.pid
UserName
Data/UserName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ChangeType
Data/ChangeType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderContextKey
Data/ProviderContextKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderContextName
Data/ProviderContextName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderContextType
Data/ProviderContextType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5450
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
ProcessId
Data/ProcessId
principal.process.pid
UserName
Data/UserName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
ProviderKey
Data/ProviderKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ProviderName
Data/ProviderName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
ChangeType
Data/ChangeType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
SubLayerKey
Data/SubLayerKey
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
SubLayerName
Data/SubLayerName
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
SubLayerType
Data/SubLayerType
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Weight
Data/Weight
security_result.about.resource.attribute.labels.key
security_result.about.resource.attribute.labels.value
Event ID 5451
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
IpProtocol
Data/IpProtocol
network.ip_protocol
LocalAddress
Data/LocalAddress
principal.ip
LocalPort
Data/LocalPort
principal.port
RemoteAddress
Data/RemoteAddress
target.ip
RemotePort
Data/RemotePort
target.port
LocalAddressMask
Data/LocalAddressMask
additional.fields.key
additional.fields.value_string
LocalTunnelEndpoint
Data/LocalTunnelEndpoint
additional.fields.key
additional.fields.value_string
RemoteAddressMask
Data/RemoteAddressMask
additional.fields.key
additional.fields.value_string
PeerPrivateAddress
Data/PeerPrivateAddress
target.nat_ip
RemoteTunnelEndpoint
Data/RemoteTunnelEndpoint
additional.fields.key
additional.fields.value_string
KeyingModuleName
Data/KeyingModuleName
additional.fields.key
additional.fields.value_string
AhAuthType
Data/AhAuthType
security_result.detection_fields.key
security_result.detection_fields.value
EspAuthType
Data/EspAuthType
security_result.detection_fields.key
security_result.detection_fields.value
CipherType
Data/CipherType
security_result.detection_fields.key
security_result.detection_fields.value
LifetimeSeconds
Data/LifetimeSeconds
security_result.detection_fields.key
security_result.detection_fields.value
LifetimeKilobytes
Data/LifetimeKilobytes
security_result.detection_fields.key
security_result.detection_fields.value
LifetimePackets
Data/LifetimePackets
security_result.detection_fields.key
security_result.detection_fields.value
Mode
Data/Mode
security_result.detection_fields.key
security_result.detection_fields.value
Role
Data/Role
security_result.detection_fields.key
security_result.detection_fields.value
TransportFilterId
Data/TransportFilterId
additional.fields.key
additional.fields.value_string
MainModeSaId
Data/MainModeSaId
security_result.detection_fields.key
security_result.detection_fields.value
QuickModeSaId
Data/QuickModeSaId
security_result.detection_fields.key
security_result.detection_fields.value
InboundSpi
Data/InboundSpi
additional.fields.key
additional.fields.value_string
OutboundSpi
Data/OutboundSpi
additional.fields.key
additional.fields.value_string
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
TunnelId
Data/TunnelId
additional.fields.key
additional.fields.value_string
TrafficSelectorId
Data/TrafficSelectorId
additional.fields.key
additional.fields.value_string
Event ID 5452
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
IpProtocol
Data/IpProtocol
network.ip_protocol
LocalAddress
Data/LocalAddress
principal.ip
LocalPort
Data/LocalPort
principal.port
RemoteAddress
Data/RemoteAddress
target.ip
RemotePort
Data/RemotePort
target.port
LocalTunnelEndpoint
Data/LocalTunnelEndpoint
additional.fields.key
additional.fields.value_string
RemoteTunnelEndpoint
Data/RemoteTunnelEndpoint
additional.fields.key
additional.fields.value_string
QuickModeSaId
Data/QuickModeSaId
security_result.detection_fields.key
security_result.detection_fields.value
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
LocalAddressMask
Data/LocalAddressMask
additional.fields.key
additional.fields.value_string
RemoteAddressMask
Data/RemoteAddressMask
additional.fields.key
additional.fields.value_string
TunnelId
Data/TunnelId
additional.fields.key
additional.fields.value_string
TrafficSelectorId
Data/TrafficSelectorId
additional.fields.key
additional.fields.value_string
Event ID 5453
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Event ID 5456
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Policy
Data/Policy
target.resource.name
Event ID 5457
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Policy
Data/Policy
target.resource.name
Error
Data/Error
security_result.summary
Format:
Error Code: %{value}
Event ID 5458
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Policy
Data/Policy
target.resource.name
Event ID 5459
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Policy
Data/Policy
target.resource.name
Event ID 5460
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Policy
Data/Policy
target.resource.name
Event ID 5461
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Policy
Data/Policy
target.resource.name
Event ID 5462
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Policy
Data/Policy
target.resource.name
Event ID 5463
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5464
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW_WITH_MODIFICATION
Event ID 5465
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5466
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Event ID 5467
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5468
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Event ID 5471
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Policy
Data/Policy
target.resource.name
Event ID 5472
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Policy
Data/Policy
target.resource.name
Event ID 5473
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Policy
Data/Policy
target.resource.name
Event ID 5474
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Policy
Data/Policy
target.resource.name
Event ID 5477
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
QuickModeFilter
Data/QuickModeFilter
additional.fields.key
additional.fields.value_string
Error
Data/Error
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5478
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application = "IPsec Policy Agent service"
security_result.action = ALLOW
Event ID 5479
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "IPsec Policy Agent service"
security_result.action = ALLOW
Event ID 5480
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Event ID 5483
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Event ID 5484
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Error
Data/Error
security_result.summary
Format -
Error Code: %{value}
Event ID 5485
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Event ID 5615
Provider: Microsoft-Windows-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application = "Windows Management Instrumentation"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 5617
Provider: Microsoft-Windows-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application = "Windows Management Instrumentation"
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 5632
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
LocalMac
Data/LocalMac
principal.mac
SubjectUserName
Data/SubjectUserName
principal.user.userid
ReasonText
Data/ReasonText
security_result.description
PeerMac
Data/PeerMac
target.mac
SSID
Data/SSID
security_result.detection_fields.key
security_result.detection_fields.value
Identity
Data/Identity
security_result.detection_fields.key
security_result.detection_fields.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
IntfGuid
Data/IntfGuid
additional.fields.key
additional.fields.value_string
ReasonCode
Data/ReasonCode
security_result.detection_fields.key
security_result.detection_fields.value
ErrorCode
Data/ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
EAPReasonCode
Data/EAPReasonCode
security_result.detection_fields.key
security_result.detection_fields.value
EapRootCauseString
Data/EapRootCauseString
security_result.detection_fields.key
security_result.detection_fields.value
EAPErrorCode
Data/EAPErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5633
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
ReasonText
Data/ReasonText
security_result.description
InterfaceName
Data/InterfaceName
additional.fields.key
additional.fields.value_string
Identity
Data/Identity
additional.fields.key
additional.fields.value_string
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ReasonCode
Data/ReasonCode
security_result.detection_fields.key
security_result.detection_fields.value
ErrorCode
Data/ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5712
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = UNKNOWN_ACTION
ProcessName
Data/ProcessName
principal.process.file.full_path
SubjectUserSid
principal.user.windows_sid
SubjectUserName
principal.user.userid
SubjectDomainName
principal.administrative_domain
ProcessId
Data/ProcessId
principal.process.pid
RemoteIpAddress
Data/RemoteIpAddress
target.ip
RemotePort
Data/RemotePort
target.port
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
InterfaceUuid
Data/InterfaceUuid
additional.fields.key
additional.fields.value_string
ProtocolSequence
Data/ProtocolSequence
additional.fields.key
additional.fields.value_string
AuthenticationService
Data/AuthenticationService
additional.fields.key
additional.fields.value_string
AuthenticationLevel
AuthenticationLevel
additional.fields.key
additional.fields.value_string
Event ID 5719
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 5721
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 5722
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data_2
security_result.summary
Format:
%{Data_2} - %{Extract description from Message}
Data
target.hostname
Data_1
principal.user.userid
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5723
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
target.hostname
Data_1
principal.user.userid
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5774
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
Data_1
Data/Data_1
additional.fields.key
additional.fields.value_string
Data_2
Data/Data_2
additional.fields.key
additional.fields.value_string
Data_3
Data/Data_3
additional.fields.key
additional.fields.value_string
Data_4
Data/Data_4
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5775
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
Data_1
Data/Data_1
additional.fields.key
additional.fields.value_string
Data_2
Data/Data_2
additional.fields.key
additional.fields.value_string
Data_3
Data/Data_3
additional.fields.key
additional.fields.value_string
Data_4
Data/Data_4
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5781
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5782
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5802
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Culture
additional.fields.key
additional.fields.value_string
Level
security_result.detection_fields.key
security_result.detection_fields.value
Keywords.Keyword
additional.fields.key
additional.fields.value_string
Event ID 5805
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
target.hostname
Data_1
additional.fields.key
additional.fields.value_string
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 5807
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Data_2
additional.fields.key
additional.fields.value_string
Data_3
additional.fields.key
additional.fields.value_string
Event ID 5823
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 5827
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
target.hostname
Data_1
target.domain.name
Data_2
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Data_3
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Data_4
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Data_5
principal.asset.attribute.labels.key
principal.asset.attribute.labels.value
Event ID 5830
Provider: NETLOGON
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target_hostname set to target.hostname
Event ID 5857
Provider: Microsoft-Windows-WMI-Activity
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ProcessID
Data/ProcessID
target.process.pid
Code
Data/Code
security_result.summary
is set to "Code - %{Code}"
HostProcess
Data/HostProcess
target.process.file.full_path
ProviderPath
Data/ProviderPath
target.file.full_path
ProviderName
Data/ProviderName
about.resource.attribute.labels.key
about.resource.attribute.labels.value
Event ID 5858
Provider: Microsoft-Windows-WMI-Activity
NXLog field
Event Viewer field
UDM field
metadata.event_type =  STATUS_UPDATE
ClientMachine
Data/ClientMachine
principal.hostname
User
Data/User
principal.user.windows_sid
ClientProcessId
Data/ClientProcessId
principal.process.pid
PossibleCause
Data/PossibleCause
security_result.description
Id
additional.fields.key
additional.fields.value_string
Component
Data/Component
security_result.detection_fields.key
security_result.detection_fields.value
Operation
Data/Operation
security_result.detection_fields.key
security_result.detection_fields.value
ResultCode
Data/ResultCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 5859
Provider: Microsoft-Windows-WMI-Activity
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
NamespaceName
Data/NamespaceName
target.file.full_path
User
Data/User
principal.user.windows_sid
ProcessID
Data/ProcessID
target.process.pid
PossibleCause
Data/PossibleCause
security_result.description
Query
Data/Query
additional.fields.key
additional.fields.value_string
Provider
Data/Provider
about.resource.attribute.labels.key
about.resource.attribute.labels.value
queryid
Data/queryid
additional.fields.key
additional.fields.value_string
Event ID 5860
Provider: Microsoft-Windows-WMI-Activity
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
NamespaceName
Data/NamespaceName
target.file.full_path
User
Data/User
principal.user.windows_sid
Processid
Data/User
target.process.pid
ClientMachine
Data/ClientMachine
principal.hostname
PossibleCause
Data/PossibleCause
security_result.description
Query
Data/Query
additional.fields.key
additional.fields.value_string
Event ID 5861
Provider: Microsoft-Windows-WMI-Activity
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application" set to "%{SourceName}"
security_result.summary" set to "%{Channel}"
Message
System/Message
Namespace set to target.file.full_path
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
PossibleCause
Data/PossibleCause
security_result.description
AccountType
System/AccountType
principal.user.attribute.roles.name
ESS
Data/ESS
additional.fields.key
additional.fields.value_string
CONSUMER
Data/CONSUMER
additional.fields.key
additional.fields.value_string
Event ID 5888
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_UPDATE_CONTENT
security_result.action = ALLOW_WITH_MODIFICATION
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ObjectCollectionName
Data/ObjectCollectionName
target.resource.name
ModifiedObjectProperties
Data/ModifiedObjectProperties
We can use target.resource.attribute.labels.key/value UDM mappings as follows (check whether it is possible by using kv in conf):
target.resource.attribute.labels.key = "<Property_Name>_OLD_VALUE"
target.resource.attribute.labels.value= "<OLD_VALUE>"
target.resource.attribute.labels.key = "<Property_Name>_NEW_VALUE"
target.resource.attribute.labels.value= "<NEW_VALUE>"
ObjectIdentifyingProperties
Data/ObjectIdentifyingProperties
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5889
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_DELETION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ObjectCollectionName
target.resource.name
ObjectIdentifyingProperties
Data/ObjectIdentifyingProperties
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectProperties
Data/ObjectProperties
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 5890
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_CREATION
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ObjectCollectionName
Data/ObjectCollectionName
target.resource.name
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
ObjectIdentifyingProperties
Data/ObjectIdentifyingProperties
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ObjectProperties
Data/ObjectProperties
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6000
Windows 10 client / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.application = "winlogon notification subscriber"
Provider: Microsoft-Windows-Eventlog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Channel
Data/Channel
target.file.full_path
Windows Server 2019 / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
Data
Data/Data
additional.fields.key
additional.fields.value_string
Event ID 6001
Windows 10 client / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.application = "winlogon notification subscriber"
Windows Server 2019 / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
Data
Data/Data
additional.fields.key
additional.fields.value_string
Event ID 6003
Windows 10 client / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.application = "winlogon notification subscriber"
Windows Server 2019 / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
Data
Data/Data
additional.fields.key
additional.fields.value_string
Event ID 6005
Windows Server 2019 / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.application = "winlogon notification subscriber"
Data
Data/Data
additional.fields.key
additional.fields.value_string
Data1
Data/Data1
additional.fields.key
additional.fields.value_string
Provider: EventLog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
metadata.event_type = SERVICE_START
target.application = "%{SourceName}"
SourceName
target.application
Event ID 6006
Windows 10 client / Provider: EventLog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
SourceName
target.application
metadata.event_type = SERVICE_STOP
target.application = "%{SourceName}"
Windows Server 2019 / Provider: EventLog
NXLog field
Event Viewer field
UDM field
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-W3LOGSVC
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
Message
security_result.summary
SourceName
target.application
ProcessId
target.process.pid
Event ID 6008
Provider: EventLog
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
target.application = "%{SourceName}"
Event ID 6009
Provider: EventLog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 6011
Provider: EventLog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
Extract hostnames and map old value with
principal.hostname
and new modified value to
target.hostname
Event ID 6013
Provider: EventLog
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 6038
Provider: LsaSrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 6062
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 6100
Provider: Microsoft-Windows-Diagnostics-Networking
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
HelperClassName
Data/HelperClassName
additional.fields.key
additional.fields.value_string
EventDescription
Data/EventDescription
additional.fields.key
additional.fields.value_string
EventVerbosity
Data/EventVerbosity
additional.fields.key
additional.fields.value_string
Event ID 6144
Provider: LsaSrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
GPOList
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6145
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
GPOList
Data/GPOList
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6148
Provider: LsaSrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
Event ID 6149
Provider: LsaSrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
Event ID 6272
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectMachineName
Data/SubjectMachineName
principal.user.userid
SubjectMachineSID
Data/SubjectMachineSID
principal.user.windows_sid
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
additional.fields.key
additional.fields.value_string
MachineInventory
Data/MachineInventory
principal.asset.platform_software.platform_version
CalledStationID
Data/CalledStationID
additional.fields.key
additional.fields.value_string
CallingStationID
Data/CallingStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/AuthenticationProvider
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineState
Data/QuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSessionIdentifier
Data/QuarantineSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
LoggingResult
Data/LoggingResult
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6273
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
SubjectMachineName
Data/SubjectMachineName
principal.user.userid
SubjectMachineSID
Data/SubjectMachineSID
principal.user.windows_sid
Reason
Data/Reason
security_result.summary
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
additional.fields.key
additional.fields.value_string
MachineInventory
Data/MachineInventory
principal.asset.platform_software.platform_version
CalledStationID
Data/CalledStationID
additional.fields.key
additional.fields.value_string
CallingStationID
Data/CallingStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
ReasonCode
Data/ReasonCode
security_result.detection_fields.key
security_result.detection_fields.value
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
LoggingResult
Data/LoggingResult
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6274
version 1 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
SubjectMachineName
Data/SubjectMachineName
principal.user.userid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
SubjectMachineSID
Data/SubjectMachineSID
principal.user.windows_sid
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
additional.fields.key
additional.fields.value_string
MachineInventory
Data/MachineInventory
principal.asset.platform_software.platform_version
CalledStationID
Data/CalledStationID
additional.fields.key
additional.fields.value_string
CallingStationID
Data/CallingStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/AuthenticationProvider
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
ReasonCode
Data/ReasonCode
security_result.detection_fields.key
security_result.detection_fields.value
Reason
Data/Reason
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6275
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
SubjectMachineName
Data/SubjectMachineName
principal.user.userid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
SubjectMachineSID
Data/SubjectMachineSID
principal.user.windows_sid
Reason
Data/Reason
security_result.summary
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
additional.fields.key
additional.fields.value_string
MachineInventory
Data/MachineInventory
principal.asset.platform_software.platform_version
CalledStationID
Data/CalledStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/AuthenticationProvider
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
ReasonCode
Data/ReasonCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6276
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
USER_CHANGE_PERMISSIONS
security_result.action = QUARANTINE
MachineInventory
Data/MachineInventory
principal.asset.platform_software.platform_version
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
SubjectMachineName
Data/SubjectMachineName
principal.user.userid
SubjectMachineSID
Data/SubjectMachineSID
principal.user.windows_sid
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
additional.fields.key
additional.fields.value_string
CalledStationID
Data/CalledStationID
additional.fields.key
additional.fields.value_string
CallingStationID
Data/CallingStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/AuthenticationProvider
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineState
Data/QuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
ExtendedQuarantineState
Data/ExtendedQuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSessionID
Data/QuarantineSessionID
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineHelpURL
Data/QuarantineHelpURL
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSystemHealthResult
Data/QuarantineSystemHealthResult
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6277
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
USER_CHANGE_PERMISSIONS
security_result.action = ALLOW_WITH_MODIFICATION
CalledStationID
Data/CalledStationID
principal.asset.platform_software.platform_version
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
principal.user.userid
SubjectMachineName
Data/SubjectMachineName
principal.user.windows_sid
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
SubjectMachineSID
Data/SubjectMachineSID
additional.fields.key
additional.fields.value_string
MachineInventory
Data/MachineInventory
additional.fields.key
additional.fields.value_string
CallingStationID
Data/CallingStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/AuthenticationProvider
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineState
Data/QuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
ExtendedQuarantineState
Data/ExtendedQuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSessionID
Data/QuarantineSessionID
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineHelpURL
Data/QuarantineHelpURL
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSystemHealthResult
Data/QuarantineSystemHealthResult
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineGraceTime
Data/QuarantineGraceTime
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6278
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
USER_CHANGE_PERMISSIONS
security_result.action = ALLOW
MachineInventory
Data/MachineInventory
principal.asset.platform_software.platform_version
SubjectMachineName
Data/SubjectMachineName
principal.user.userid
SubjectMachineSID
Data/SubjectMachineSID
principal.user.windows_sid
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
FullyQualifiedSubjectMachineName
Data/FullyQualifiedSubjectMachineName
additional.fields.key
additional.fields.value_string
CalledStationID
Data/CalledStationID
additional.fields.key
additional.fields.value_string
CallingStationID
Data/CallingStationID
additional.fields.key
additional.fields.value_string
NASIPv4Address
Data/NASIPv4Address
additional.fields.key
additional.fields.value_string
NASIPv6Address
Data/NASIPv6Address
additional.fields.key
additional.fields.value_string
NASIdentifier
Data/NASIdentifier
additional.fields.key
additional.fields.value_string
NASPortType
Data/NASPortType
additional.fields.key
additional.fields.value_string
NASPort
Data/NASPort
target.port
ClientIPAddress
Data/ClientIPAddress
principal.ip
ProxyPolicyName
Data/ProxyPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
NetworkPolicyName
Data/NetworkPolicyName
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationProvider
Data/AuthenticationProvider
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationServer
Data/AuthenticationServer
security_result.detection_fields.key
security_result.detection_fields.value
AuthenticationType
Data/AuthenticationType
security_result.detection_fields.key
security_result.detection_fields.value
EAPType
Data/EAPType
security_result.detection_fields.key
security_result.detection_fields.value
AccountSessionIdentifier
Data/AccountSessionIdentifier
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineState
Data/QuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
ExtendedQuarantineState
Data/ExtendedQuarantineState
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSessionID
Data/QuarantineSessionID
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineHelpURL
Data/QuarantineHelpURL
security_result.detection_fields.key
security_result.detection_fields.value
QuarantineSystemHealthResult
Data/QuarantineSystemHealthResult
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6279
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
USER_CHANGE_PERMISSIONS
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
ClientName
Data/ClientName
principal.asset.attribute.labels.key/value
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
Event ID 6280
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type =
USER_CHANGE_PERMISSIONS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
target.administrative_domain
SubjectUserName
Data/SubjectUserName
target.user.userid
SubjectUserSid
Data/SubjectUserSid
target.user.windows_sid
FullyQualifiedSubjectUserName
Data/FullyQualifiedSubjectUserName
additional.fields.key
additional.fields.value_string
Event ID 6281
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_UNCATEGORIZED
security_result.action = ALLOW_WITH_MODIFICATION
param1
Data/param1
target.file.full_path
Event ID 6313
Provider: ADSync
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
principal.administrative_domain
Event ID 6400
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ClientIPAddress
Data/ClientIPAddress
principal.ip
Event ID 6401
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ClientIPAddress
Data/ClientIPAddress
principal.ip
Event ID 6402
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ClientIPAddress
Data/ClientIPAddress
principal.ip
Event ID 6403
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
HostedCacheName
Data/HostedCacheName
additional.fields.key
additional.fields.value_string
Event ID 6404
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ErrorCode
Data/ErrorCode
security_result.description
set to
Error Code - %{ErrorCode}
HostedCacheName
Data/HostedCacheName
additional.fields.key
additional.fields.value_string
Event ID 6405
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
EventId
Data/EventId
additional.fields.key
additional.fields.value_string
Count
Data/Count
additional.fields.key
additional.fields.value_string
Event ID 6406
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProductName
Data/ProductName
additional.fields.key
additional.fields.value_string
Categories
Data/Categories
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6407
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
Message
Data/Message
additional.fields.key
additional.fields.value_string
Event ID 6408
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ProductName
Data/ProductName
additional.fields.key
additional.fields.value_string
Categories
Data/Categories
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6409
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
GUID
Data/GUID
additional.fields.key
additional.fields.value_string
Event ID 6410
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = FILE_UNCATEGORIZED
security_result.action = BLOCK
param1
Data/param1
target.file.full_path
Event ID 6416
version 0 / Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
resource.resource_type set to "DEVICE"
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
ClassId
Data/ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
VendorIds
Data/VendorIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
Data/CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
Data/LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
version 1 /
NXLog field
Event Viewer field
UDM field
DeviceDescription
Data/DeviceDescription
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassName
Data/ClassName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DeviceId
Data/DeviceId
target.resource.product_object_id
Event ID 6417
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
ProcessId
Data/ProcessId
principal.process.pid
ProcessName
principal.process.command_line
Event ID 6418
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
ProcessId
Data/ProcessId
principal.process.pid
ProcessName
principal.process.command_line
FatalCode
Data/FatalCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 6419
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClassName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DeviceId
Data/DeviceId
target.resource.id
DeviceDescription
Data/DeviceDescription
target.resource.name
HardwareIds
Data/HardwareIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6420
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClassName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DeviceId
Data/DeviceId
target.resource.id
DeviceDescription
Data/DeviceDescription
target.resource.name
HardwareIds
Data/HardwareIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6421
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClassName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DeviceId
Data/DeviceId
target.resource.id
DeviceDescription
Data/DeviceDescription
target.resource.name
HardwareIds
Data/HardwareIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6422
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
ClassName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
SubjectLogonId
Data/SubjectLogonId
principal.labels.key/value
DeviceId
Data/DeviceId
target.resource.id
DeviceDescription
Data/DeviceDescription
target.resource.name
HardwareIds
Data/HardwareIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6423
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = BLOCK
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
DeviceId
Data/DeviceId
target.resource.id
DeviceDescription
Data/DeviceDescription
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ClassId
Data/ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassName
Data/Data/SubjectUserName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HardwareIds
Data/HardwareIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
Data/CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
Data/LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6424
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_RESOURCE_ACCESS
security_result.action = ALLOW
SubjectDomainName
Data/SubjectDomainName
principal.administrative_domain
SubjectUserName
Data/SubjectUserName
principal.user.userid
SubjectUserSid
Data/SubjectUserSid
principal.user.windows_sid
DeviceId
Data/DeviceId
target.resource.id
DeviceDescription
Data/DeviceDescription
target.resource.name
SubjectLogonId
Data/SubjectLogonId
additional.fields.key
additional.fields.value_string
ClassId
Data/ClassId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ClassName
Data/Data/SubjectUserName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
HardwareIds
Data/HardwareIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
CompatibleIds
Data/CompatibleIds
target.resource.attribute.labels.key
target.resource.attribute.labels.value
LocationInformation
Data/LocationInformation
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 6946
Provider: ADSync
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.description
Event ID 6952
Provider: ADSync
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
If required fields for above mentioned
metadata.event_type
are not present, then set
metadata.event_type
to
STATUS_UPDATE
.
Data
security_result.description
Event ID 7000
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Extract error and map it to
security_result.summary
param1
Data/param1
target.application
Event ID 7001
Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
UserSid
Data/UserSid
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
TSId
Data/TSId
additional.fields.key
additional.fields.value_string
Event ID 7002
Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
TSId
Data/TSId
additional.fields.key
additional.fields.value_string
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7003
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7005
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7009
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
target.application
Event ID 7010
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7011
Windows Server 2019 / Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
param1
Data/param1
target.application
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7012
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7017
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7021
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
metadata.event_type = STATUS_UNCATEGORIZED
Data
target.hostname
Data_1
target.resource.name
Netwwt01
NXLog field
Event Viewer field
UDM field
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 7022
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
param1
Not available
target.application
Event ID 7023
Windows 10 client / Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
Extract error and map it to
security_result.summary
param1
Data/param1
target.application
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
metadata.event_type = SERVICE_STOP
param2
Not available
security_result.description
Format:
Error Code - %{value}
param1
Not available
target.application
Windows Server 2019 / Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 7024
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
param2
Not available
security_result.description
Format:
Error Code - %{value}
param1
Not available
target.application
Event ID 7025
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Event ID 7026
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.resource.resource_type = DEVICE
target.resource.resource_subtype = "boot-start or system-start driver"
param1
Not available
target.application
Event ID 7031
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
param1
Not available
target.application
param2
additional.fields.key
additional.fields.value_string
param3
additional.fields.key
additional.fields.value_string
param4
additional.fields.key
additional.fields.value_string
param5
Not available
security_result.action_details
Event ID 7032
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
param2
Not available
security_result.action_details
param4
Not available
security_result.description
Error Code: %{value}
param3
Not available
target.application
param1
Not available
additional.fields.key
additional.fields.value_string
Event ID 7034
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
security_result.action = BLOCK
param1
Not available
target.application
param2
Not available
additional.fields.key
additional.fields.value_string
Event ID 7036
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
If the
param2
log field value is equal to
stopped
, then the
metadata.event_type
UDM field is set to
SERVICE_STOP
.
Else, if the
param2
log field value is equal to
start
, then the
metadata.event_type
UDM field is set to
SERVICE_START
.
Else, if the
param2
log field value is equal to
running
, 
then the
metadata.event_type
UDM field is set to
SERVICE_UNSPECIFIED
.
param1
Not available
target.application
param2
Not available
security_result.action_details
If the
param2
log field value is equal to
stopped
, 
then the
security_result.action
UDM field is set to
ALLOW
.
Event ID 7038
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
param2
principal.hostname
param3
security_result.description
Format:
%{param3} - %{Extract description from Message}
param1
target.application
Event ID 7040
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_MODIFICATION
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
target.application
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
param4
Data/param4
additional.fields.key
additional.fields.value.string_value
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 7042
Windows Server 2019 / Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
target.application
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
param4
Data/param4
additional.fields.key
additional.fields.value.string_value
param5
Data/param5
additional.fields.key
additional.fields.value.string_value
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 7045
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_CREATION
ServiceName
Data/ServiceName
target.application
ImagePath
Data/ImagePath
target.process.file.full_path
UserID
System/UserID
target.user.windows_sid
ServiceType
additional.fields.key
additional.fields.value.string_value
StartType
additional.fields.key
additional.fields.value.string_value
ServiceType
Data/ServiceType
additional.fields.key
additional.fields.value_string
StartType
Data/StartType
additional.fields.key
additional.fields.value_string
Event ID 8000
Provider: Netwtw10
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
Status
security_result.summary
Event ID 8003
Provider: bowser
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Data_1
target.hostname
Data_2
target.resource.product_object_id
Data
additional.fields.key
additional.fields.value_string
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
FullFilePath
target.process.file.full_path
FilePath
target.file.full_path
FileHash
target.file.sha256
Fqbn
target.group.group_display_name
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
FilePathLength
additional.fields.key
additional.fields.value_string
FileHashLength
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
FullFilePathLength
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
InterfaceGuid
additional.fields.key
additional.fields.value_string
InterfaceDescription
additional.fields.key
additional.fields.value_string
ConnectionMode
additional.fields.key
additional.fields.value_string
ProfileName
target.hostname
ProfileName
target.asset.hostname
SSID
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BSSType
additional.fields.key
additional.fields.value_string
Reason
security_result.summary
ConnectionId
additional.fields.key
additional.fields.value_string
ReasonCode
security_result.detection_fields
Event ID 8004
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
FullFilePath
target.process.file.full_path
FilePath
target.file.full_path
FileHash
target.file.sha256
Fqbn
target.group.group_display_name
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
FilePathLength
additional.fields.key
additional.fields.value_string
FileHashLength
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
FullFilePathLength
additional.fields.key
additional.fields.value_string
Event ID 8005
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.description
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
PrincipalSamName
Data/PrincipalSamName
target.hostname
TargetLogonId
Data/TargetLogonId
additional.fields.key
additional.fields.value.string_value
PolicyElaspedTimeInSeconds
Data/PolicyElaspedTimeInSeconds
security_result.rule_labels.key
security_result.rule_labels.value
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsConnectivityFailure
Data/IsConnectivityFailure
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 8006
Provider: Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.attribute.roles.name
UserID
System/UserID
principal.user.windows_sid
ErrorCode
Data/ErrorCode
security_result.summary
Format:
ErrorCode - %{value}
PrincipalSamName
Data/PrincipalSamName
target.hostname
PolicyElaspedTimeInSeconds
Data/PolicyElaspedTimeInSeconds
security_result.rule_labels.key
security_result.rule_labels.value
IsMachine
Data/IsMachine
security_result.rule_labels.key
security_result.rule_labels.value
IsConnectivityFailure
Data/IsConnectivityFailure
security_result.rule_labels.key
security_result.rule_labels.value
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
FullFilePath
target.process.file.full_path
FilePath
target.file.full_path
FileHash
target.file.sha256
Fqbn
target.group.group_display_name
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
FilePathLength
additional.fields.key
additional.fields.value_string
FileHashLength
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
FullFilePathLength
additional.fields.key
additional.fields.value_string
Event ID 8007
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
FullFilePath
target.process.file.full_path
FilePath
target.file.full_path
FileHash
target.file.sha256
Fqbn
target.group.group_display_name
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
FilePathLength
additional.fields.key
additional.fields.value_string
FileHashLength
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
FullFilePathLength
additional.fields.key
additional.fields.value_string
Event ID 8008
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 8009
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
Data/ErrorCode
security_result.summary
set to ErrorCode - %{ErrorCode}
Event ID 8010
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8015
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8017
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8018
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8019
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8020
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8021
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: BROWSER
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
additional.fields.key
additional.fields.value_string
Data
additional.fields.key
additional.fields.value_string
Binary
additional.fields.key
additional.fields.value_string
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = FAIL
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
Fqbn
target.group.group_display_name
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
PackageLength
additional.fields.key
additional.fields.value_string
Package
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
Event ID 8022
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
Fqbn
target.group.group_display_name
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
PackageLength
additional.fields.key
additional.fields.value_string
Package
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
Event ID 8025
Provider: Microsoft-Windows-AppLocker
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = BLOCK
RuleId
security_result.rule_id
TargetUser
target.user.userid
TargetProcessId
target.process.pid
Fqbn
target.group.group_display_name
PolicyNameLength
additional.fields.key
additional.fields.value_string
PolicyName
additional.fields.key
additional.fields.value_string
RuleNameLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleName
security_result.rule_name
RuleSddlLength
security_result.rule_labels.key
security_result.rule_labels.value
RuleSddl
security_result.rule_labels.key
security_result.rule_labels.value
PackageLength
additional.fields.key
additional.fields.value_string
Package
additional.fields.key
additional.fields.value_string
FqbnLength
additional.fields.key
additional.fields.value_string
Event ID 8027
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8030
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 8033
Provider: Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
DnsServerList
intermediary.ip
Ipaddress
target.ip
ErrorCode
Data/ErrorCode
security_result.summary
security_result.summary
set to
ErrorCode - %{ErrorCode}
AdapterName
security_result.detection_fields.key
security_result.detection_fields.value
HostName
security_result.detection_fields.key
security_result.detection_fields.value
AdapterSuffixName
security_result.detection_fields.key
security_result.detection_fields.value
Sent UpdateServer
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 8191
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = UNKNOWN_ACTION
Event ID 8193
Provider: VSS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.application = %{SourceName}
Data
Data/Data
additional.fields.key
additional.fields.value_string
Data_1
Data/Data_1
additional.fields.key
additional.fields.value_string
Data_2
Data/Data_2
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Powershell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
param1
target.resource.product_object_id
Event ID 8198
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 8222
Provider: VSSAudit
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
principal.administrative_domain
AccountType
principal.user.attribute.roles.name
Data_3
target.process.file.full_path
Data_8
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Data_9
target.resource.name
Data
additional.fields.key
additional.fields.value_string
Data_1
additional.fields.key
additional.fields.value_string
Data_2
target.process.pid
Data_4
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Data_5
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Data_6
additional.fields.key
additional.fields.value_string
Data_7
additional.fields.key
additional.fields.value_string
Event ID 8223
Provider: VSSAudit
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
Data_7
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Data_8
target.resource.name
Data
principal.user.windows_sid
Data_1
principal.user.attribute.labels.key
principal.user.attribute.labels.value
Data_2
principal.user.attribute.labels.key
principal.user.attribute.labels.value
Data_3
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Data_4
target.resource.product_object_id
Data_5
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Data_6
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 8224
Provider: VSS
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
SourceName
Not available
target.application
Event ID 8225
Provider: VSS
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
SourceName
Not available
target.application
Event ID 8230
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Event ID 9007
Provider: nhi
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 9008
Provider: nhi
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 9027
Provider: Desktop Window Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Event ID 10000
Windows Server 2019 / Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
target.process.command_line
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
AccountType
System/AccountType
principal.user.attribute.roles.name
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target.resource.id
Event ID 10001
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
target.process.command_line
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
target.application
param4
Data/param4
additional.fields.key
additional.fields.value.string_value
param5
Data/param5
additional.fields.key
additional.fields.value.string_value
AccountType
System/AccountType
principal.user.attribute.roles.name
Provider: Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ExtensibleModulePath
Data/ExtensibleModulePath
target.process.file.full_path
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
ServiceName
target.application
CLSID
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
MinimumFxVersion
additional.fields.key
additional.fields.value_string
Upgrade
additional.fields.key
additional.fields.value_string
Event ID 10002
Provider: Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ExtensibleModulePath
Data/ExtensibleModulePath
target.process.file.full_path
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
ServiceName
target.application
CLSID
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
MinimumFxVersion
additional.fields.key
additional.fields.value_string
Upgrade
additional.fields.key
additional.fields.value_string
Event ID 10004
Provider: Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ExtensibleModulePath
target.process.file.full_path
Event ID 10005
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
Data/param2
target.application
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 10010
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 10016
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type set to SETTING
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param7
Data/param7
target.administrative_domain
param10
Data/param10
target.application
param1
Data/param1
target.resource.attribute.permissions.name
param2
Data/param2
additional.fields.key
additional.fields.value.string_value
param3
Data/param3
additional.fields.key
additional.fields.value.string_value
param4
Data/param4
additional.fields.key
additional.fields.value.string_value
param5
Data/param5
target.resource.product_object_id
param6
Data/param6
target.user.userid
param8
Data/param8
target.user.windows_sid
param9
Data/param9
additional.fields.key
additional.fields.value_string
param11
Data/param11
additional.fields.key
additional.fields.value_string
Event ID 10100
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 10111
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
InstanceId
target.resource.id
LifetimeId
additional.fields.key
additional.fields.value_string
FriendlyName
target.resource.name
Location
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RestartCount
additional.fields.key
additional.fields.value_string
Event ID 10118
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_AUDIT_LOG_UNCATEGORIZED
Event ID 10020
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
param1
Data/param1
additional.fields.key
additional.fields.value.string_value
param2
security_result.summary
Event ID 10028
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
param3
Data/param3
principal.process.file.full_path
param2
Data/param2
principal.process.pid
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
param1
Data/param1
target.ip
param4
Data/param4
additional.fields.key
additional.fields.value
string
binLength
Data/_binLength
additional.fields.key
additional.fields.value_string
binary
Data/binary
additional.fields.key
additional.fields.value_string
Event ID 10036
Provider: Microsoft-Windows-DistributedCOM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Domain Name
Data/Domain Name
target.administrative_domain
Client IP Address
Data/Client IP Address
target.ip
User Name
Data/User Name
target.user.user_display_name
SID
Data/SID
target.user.windows_sid
Event ID 10110
Provider: Microsoft-Windows-DriverFrameworks-UserMode
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Status
security_result.summary
LifetimeId
additional.fields.key
additional.fields.value_string
Problem
additional.fields.key
additional.fields.value_string
DetectedBy
additional.fields.key
additional.fields.value_string
ActiveOperation
additional.fields.key
additional.fields.value_string
ExitCode
additional.fields.key
additional.fields.value_string
Message
additional.fields.key
additional.fields.value_string
Event ID 10148
Windows 10 client / Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Windows Server 2019 / Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 10149
Windows 10 client / Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Windows Server 2019 / Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 10154
Windows 10 client / Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Windows Server 2019 / Provider: Microsoft-Windows-WinRM
NXLog field
Event Viewer field
UDM field
spn1
Data/spn1
additional.fields.key
additional.fields.value_string
spn2
Data/spn2
additional.fields.key
additional.fields.value_string
error
Data/error
security_result.summary
Event ID 10317
Provider: Microsoft-Windows-NDIS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
AdapterName
target.resource.name
UserID
principal.user.windows_sid
IfGuid
target.resource.product_object_id
IfIndex
target.resource.attribute.labels.key
target.resource.attribute.labels.value
IfLuid
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ResetReason
additional.fields.key
additional.fields.value_string
ResetCount
additional.fields.key
additional.fields.value_string
Event ID 10400
Provider: Microsoft-Windows-NDIS
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
AdapterName
target.resource.name
IfGuid
target.resource.product_object_id
IfIndex
target.resource.attribute.labels.key
target.resource.attribute.labels.value
IfLuid
target.resource.attribute.labels.key
target.resource.attribute.labels.value
ResetReason
additional.fields.key
additional.fields.value_string
ResetCount
additional.fields.key
additional.fields.value_string
Event ID 11707
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Message
target.application
Extract product_name from
Message
field and map it to
target.application
AccountType
principal.user.attribute.roles.name
Event ID 12294
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
UserName
target.user.userid
Event ID 14204
Provider: Microsoft-Windows-WMPNSS-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
ServiceName
target.application
Event ID 14205
Provider: Microsoft-Windows-WMPNSS-Service
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_STOP
ServiceName
target.application
Event ID 14531
Provider: Microsoft-Windows-DfsSvc
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 14533
Provider: Microsoft-Windows-DfsSvc
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 14554
Provider: Microsoft-Windows-DfsSvc
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 15007
Provider: Microsoft-Windows-HttpEvent
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Url
Data/Url
target.url
Event ID 15008
Provider: Microsoft-Windows-HttpEvent
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Url
Data/Url
target.url
Event ID 15021
Provider: Microsoft-Windows-HttpEvent
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Endpoint
target.ip and target.port
DeviceObject
target.resource.name
Event ID 15301
Provider: Microsoft-Windows-HttpEvent
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_CREATION
Endpoint
Data/Endpoint
target.ip and target.port
Event ID 16384
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = SERVICE_START
target.application = "Software Protection"
version 0 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Title
Data/Title
security_result.summary
User
Data/User
target.user.userid
Id
Data/Id
additional.fields.key
additional.fields.value_string
Owner
Data/Owner
additional.fields.key
additional.fields.value_string
Event ID 16385
version 0 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Id
Data/Id
target.resource.product_object_id
Title
Data/Title
target.resource.name
User
Data/User
target.user.userid
FileList
Data/FileList
target.file.full_path
Owner
Data/Owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 16388
version 0 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Title
Data/Title
security_result.summary
User
Data/User
target.user.userid
Id
Data/Id
additional.fields.key
additional.fields.value_string
Owner
Data/Owner
additional.fields.key
additional.fields.value_string
Event ID 16392
version 0 / Provider: Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
ErrorCode
Data/ErrorCode
security_result.summary
is set to "ErrorCode: %{ErrorCode}"
Event ID 16394
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
Not available
metadata.event_type = STATUS_UPDATE
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 16401
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorMessage
Data/ErrorMessage
security_result.description
GroupName
Data/GroupName
target.group.group_display_name
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
entityName
security_result.rule_labels.key
security_result.rule_labels.value
currentSize
security_result.rule_labels.key
security_result.rule_labels.value
currentLimit
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 16413
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = GROUP_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorString
Data/ErrorString
security_result.description
GroupName
Data/GroupName
target.group.group_display_name
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 16647
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 16648
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
EventData.Name
EventData.Name
security_result.detection_fields.key
security_result.detection_fields.value
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 16962
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
Default SD String:
Data/Default SD String:
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 16963
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Registry SD String
Data/Registry SD String
target.registry.registry_value_name
AccountType
System/AccountType
principal.user.attribute.roles.name
Event ID 16966
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
UserID
System/UserID
principal.user.windows_sid
Event ID 16969
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Throttle window
additional.fields.key
additional.fields.value_string
Suppressed Message Count:
additional.fields.key
additional.fields.value_string
Event ID 16977
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AccountType
System/AccountType
principal.user.attribute.roles.name
MinimumPasswordLength
Data/MinimumPasswordLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RelaxMinimumPasswordLengthLimits
Data/RelaxMinimumPasswordLengthLimits
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MinimumPasswordLengthAudit
Data/MinimumPasswordLengthAudit
target.resource.attribute.labels.key
target.resource.attribute.labels.value
version 0 / Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
MinimumPasswordLength
Data/MinimumPasswordLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RelaxMinimumPasswordLengthLimits
Data/RelaxMinimumPasswordLengthLimits
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MinimumPasswordLengthAudit
Data/MinimumPasswordLengthAudit
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 16978
version 0 / Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
AccountName
Data/AccountName
target.user.userid
MinimumPasswordLength
Data/MinimumPasswordLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
MinimumPasswordLengthAudit
Data/MinimumPasswordLengthAudit
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 16979
version 0 / Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type = SETTING
MinimumPasswordLength
Data/MinimumPasswordLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 16982
version 0 / Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Event ID 16983
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
version 0 / Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 16984
Provider: Microsoft-Windows-Directory-Services-SAM
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Number of RPC methods:
additional.fields.key
additional.fields.value_string
Throttle Window:
additional.fields.key
additional.fields.value_string
Number of RPC methods:
additional.fields.key
additional.fields.value_string
Throttle Window:
additional.fields.key
additional.fields.value_string
Event ID 18452
Provider: MSSQL$ENTERPRISE191
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN, If complete_username or database_name is not empty, otherwise metadata.event_type = USER_UNCATEGORIZED
security_result.category = AUTH_VIOLATION
Message
System/Message
client_ip set to principal.ip
database_name set to target.hostname
SourceName
System/SourceName
principal.application
Event ID 18456
Provider: MSSQL$ENTERPRISE100
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN, if complete_username or database_name is not empty, otherwise metadata.event_type = USER_UNCATEGORIZED
security_result.category = AUTH_VIOLATION
Message
System/Message
client_ip set to principal.ip
database_name set to target.hostname
complete_username set to target.user.userid (if UserID is empty)
SourceName
System/SourceName
principal.application
Provider: MSSQLSERVER
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN, if complete_username or database_name is not empty, otherwise metadata.event_type = USER_UNCATEGORIZED
security_result.category = AUTH_VIOLATION
Message
System/Message
client_ip set to principal.ip
database_name set to target.hostname
complete_username set to target.user.userid (if UserID is empty)
SourceName
System/SourceName
principal.application
Event ID 20001
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
target_resource_name set to target.resource.name
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
Event ID 20003
Provider: Microsoft-Windows-UserPnp
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Category set to
security_result.category_details
Message
set to
metadata.description
target_resource_name set to target.resource.name
metadata.event_type = STATUS_UPDATE
target_resource_name set to target.resource.name
Event ID 20063
Provider: RemoteAccess
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
Data_1
Data/Data_1
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 20171
Provider: RemoteAccess
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Data
Data/Data
additional.fields.key
additional.fields.value_string
Data_1
Data/Data_1
additional.fields.key
additional.fields.value_string
EventData.Binary
EventData.Binary
additional.fields.key
additional.fields.value_string
Event ID 20192
Provider: RemoteAccess
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 28680
Provider: PRIVMAN
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 28701
Provider: PRIVMAN
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_HEARTBEAT
target_hostname set to target.hostname
target_ip set to target.ip
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 33205
Provider: MSSQL$LABX2010$AUDIT
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: MSSQL$SQL16$AUDIT
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
target_resource_name set to target.resource.name
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: MSSQL$SYNEL$AUDIT
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: MSSQLSERVER$AUDIT
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Provider: MSSQL
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
EventData/Data/audit_schema_version
security_result.detection_fields.key/value
EventData/Data/audit_event
security_result.detection_fields.key/value
EventData/Data/event_time
security_result.detection_fields.key/value
EventData/Data/sequence_number
security_result.detection_fields.key/value
EventData/Data/action_id
security_result.detection_fields.key/value
EventData/Data/succeeded
security_result.detection_fields.key/value
EventData/Data/is_column_permission
security_result.detection_fields.key/value
EventData/Data/session_id
security_result.detection_fields.key/value
EventData/Data/server_principal_id
security_result.detection_fields.key/value
EventData/Data/database_principal_id
security_result.detection_fields.key/value
EventData/Data/target_server_principal_id
security_result.detection_fields.key/value
EventData/Data/target_database_principal_id
security_result.detection_fields.key/value
EventData/Data/object_id
security_result.detection_fields.key/value
EventData/Data/user_defined_event_id
security_result.detection_fields.key/value
EventData/Data/transaction_id
security_result.detection_fields.key/value
EventData/Data/class_type
security_result.detection_fields.key/value
EventData/Data/duration_milliseconds
security_result.detection_fields.key/value
EventData/Data/response_rows
security_result.detection_fields.key/value
EventData/Data/affected_rows
security_result.detection_fields.key/value
EventData/Data/client_tls_version
security_result.detection_fields.key/value
EventData/Data/database_transaction_id
security_result.detection_fields.key/value
EventData/Data/ledger_start_sequence_number
security_result.detection_fields.key/value
EventData/Data/is_local_secondary_replica
security_result.detection_fields.key/value
EventData/Data/client_ip
security_result.detection_fields.key/value
EventData/Data/permission_bitmask
security_result.detection_fields.key/value
EventData/Data/session_server_principal_name
security_result.detection_fields.key/value
EventData/Data/server_principal_name
security_result.detection_fields.key/value
EventData/Data/sequence_group_id
security_result.detection_fields.key/value
EventData/Data/server_principal_sid
security_result.detection_fields.key/value
EventData/Data/database_principal_name
security_result.detection_fields.key/value
EventData/Data/target_server_principal_name
security_result.detection_fields.key/value
EventData/Data/target_server_principal_sid
security_result.detection_fields.key/value
EventData/Data/target_database_principal_name
security_result.detection_fields.key/value
EventData/Data/server_instance_name
security_result.detection_fields.key/value
EventData/Data/database_name
security_result.detection_fields.key/value
EventData/Data/schema_name
security_result.detection_fields.key/value
EventData/Data/object_name
security_result.detection_fields.key/value
EventData/Data/statement
security_result.detection_fields.key/value
EventData/Data/network_protocol
security_result.detection_fields.key/value
EventData/Data/additional_information/connection_id
security_result.detection_fields.key/value
EventData/Data/additional_information/host_name
security_result.detection_fields.key/value
EventData/Data/additional_information/user_defined_information
security_result.detection_fields.key/value
EventData/Data/additional_information/application_name
security_result.detection_fields.key/value
EventData/Data/additional_information/client_tls_version_name
security_result.detection_fields.key/value
EventData/Data/additional_information/external_policy_permissions_checked
security_result.detection_fields.key/value
EventData/Data/additional_information/obo_middle_tier_app_id
security_result.detection_fields.key/value
Event ID 36867
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Type
Data/Type
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 36868
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
CSPName
target.resource.name
KeyName
target.resource.product_object_id
Type
security_result.detection_fields.key
security_result.detection_fields.value
CSPType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
KeyType
target.resource.attribute.labels.key
target.resource.attribute.labels.value
KeyFlags
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 36870
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Type
security_result.detection_fields.key
security_result.detection_fields.value
ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
ErrorStatus
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 36871
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Type
Data/Type
security_result.detection_fields.key
security_result.detection_fields.value
ErrorState
Data/ErrorState
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 36874
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Protocol
network.application_protocol
Event ID 36877
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
ErrorCode
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 36880
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 36881
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 36882
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
metadata.event_type = STATUS_UNCATEGORIZED
Message
set to
security_result.summary
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 36886
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Event ID 36887
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AlertDesc
security_result.summary
Format:
AlertDesc - %{AlertDesc}
Event ID 36888
Provider: Schannel
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountType
System/AccountType
principal.user.attribute.roles.name
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
AlertDesc
security_result.summary
Format:
AlertDesc - %{AlertDesc}
ErrorState
security_result.detection_fields.key
security_result.detection_fields.value
Event ID 40960
Provider: LsaSrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = SYSTEM_AUDIT_LOG_UNCATEGORIZED
Domain
System/Domain
principal.administrative_domain
AccountName
System/AccountName
principal.user.userid
UserID
System/UserID
principal.user.windows_sid
Error
security_result.summary
Target
target.hostname
Protocol
network.application_protocol
Event ID 40970
Provider: LsaSrv
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Target
Data/Target
network.application_protocol/target.hostname/target.administrative_domain
Error
Data/Error
security_result.summary
Event ID 2147487656
version 0 / Provider: Microsoft-Windows-Winlogon
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 3221228478
Provider: Microsoft-Windows-Wininit
NXLog field
Event Viewer field
UDM field
metadata.event_type = metadata.event_type = STATUS_SHUTDOWN
security_result.description" set to "ErrorCode - %{error_code}"
Event ID 5447
Provider: Microsoft Corporation
NXLog field
Event Viewer field
UDM field
metadata.event_type = SETTING_MODIFICATION
target.resource.resource_type set to SETTING
ProviderKey
Data/ProviderKey
about.resource.attribute.labels.key/value
ProviderName
Data/ProviderName
about.resource.attribute.labels.key/value
ChangeType
Data/ChangeType
about.resource.attribute.labels.key/value
FilterKey
Data/FilterKey
about.resource.attribute.labels.key/value
FilterType
Data/FilterType
about.resource.attribute.labels.key/value
LayerKey
Data/LayerKey
about.resource.attribute.labels.key/value
LayerName
Data/LayerName
about.resource.attribute.labels.key/value
LayerId
Data/LayerId
about.resource.attribute.labels.key/value
Weight
Data/Weight
about.resource.attribute.labels.key/value
Conditions
Data/Conditions
about.resource.attribute.labels.key/value
Action
Data/Action
about.resource.attribute.labels.key/value
Data/ProcessId
principal.process.pid
UserName
Data/UserName
principal.user.userid
UserSid
Data/UserSid
principal.user.windows_sid
FilterName
Data/FilterName
target.resource.name
FilterId
Data/FilterId
target.resource.product_object_id
Event ID 403
Provider: PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
NewEngineState is set to target.labels.key/value
PreviousEngineState is set to target.labels.key/value
HostName is set to additional.fields.key/value.string_value
HostVersion is set to target.labels.key/value
HostId is set to target.labels.key/value
HostApplication is set to principal.process.command_line
EngineVersion is set to target.labels.key/value
RunspaceId is set to target.labels.key/value
PipelineId is set to target.labels.key/value
CommandName is set to target.labels.key/value
CommandType is set to target.labels.key/value
ScriptName is set to target.file.names
CommandPath is set to target.process.file.full_path
CommandLine is set to target.process.command_line
NewEngineState is set to additional.fields.key and additional.fields.value.string_value
PreviousEngineState is set to additional.fields.key and additional.fields.value.string_value
HostVersion is set to additional.fields.key and additional.fields.value.string_value
HostId is set to additional.fields.key and additional.fields.value.string_value
EngineVersion is set to additional.fields.key and additional.fields.value.string_value
RunspaceId is set to additional.fields.key and additional.fields.value.string_value
PipelineId is set to additional.fields.key and additional.fields.value.string_value
CommandName is set to additional.fields.key and additional.fields.value.string_value
CommandType is set to additional.fields.key and additional.fields.value.string_value
Event ID 4105
Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
UserID
principal.user.windows_sid
Domain
principal.administrative_domain
ScriptBlockId
principal.resource.product_object_id
SourceName
target.application
Category
security_result.summary
Message
security_result.description
ProcessID
principal.process.pid
AccountType
principal.user.userid
RunspaceId
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 105
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
pid is set to target.process.pid
additional_data is set to about.labels.key/value
additional_data is set to additional.fields.key and additional.fields.value.string_value
Event ID 4440
Provider: Microsoft-Windows-Complus
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
param1
target.labels.key/value
additional.fields.key
additional.fields.value.string_value
Event ID 8200
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
Event ID 1004
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
Event ID 1014
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
Event ID 8197
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
RuleId is set to security_result.rule_id
Action is set to security_result.action_details
app_name is set to target.application
AppId is set to target.labels.key/value
SkuId is set to target.labels.key/value
NotificationInterval is set to target.labels.key/value
Trigger is set to target.labels.key/value
AppId is set to additional.fields.key and additional.fields.value.string_value
SkuId is set to additional.fields.key and additional.fields.value.string_value
NotificationInterval is set to additional.fields.key and additional.fields.value.string_value
Trigger is set to additional.fields.key and additional.fields.value.string_value
Provider : Microsoft-Windows-Powershell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
param1
additional.fields.key
additional.fields.value_string
Event ID 20482
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 1033
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
DirectiveName is set to target.labels.key/value
AppId is set to target.labels.key/value
SkuId is set to target.labels.key/value
DirectiveName is set to additional.fields.key and additional.fields.value.string_value
AppId is set to additional.fields.key and additional.fields.value.string_value
SkuId is set to additional.fields.key and additional.fields.value.string_value
Event ID 1013
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
SkuId is set to target.labels.key/value
SkuId is set to additional.fields.key and additional.fields.value.string_value
Event ID 1067
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 12304
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 1036
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 20489
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 20481
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 1025
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
product_name is set to target.application
ProcessPath is set to target.process.file.full_path
ProcessName is set to target.process.command_line
ProcessId is set to target.process.pid
Domain
principal.administrative_domain
AccountName
principal.user.userid
UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 12305
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 12311
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 20488
Provider: Microsoft-Windows-Security-SPP
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 1281
Provider: Microsoft-Windows-TPM-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Domain
principal.administrative_domain
AccountName
principal.user.userid
UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 63
Provider: Microsoft-Windows-WMI
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Job
target.resource.name
Url
target.url
Pgm
target.application
hr
security_result.summary
Format:
hr - %{hr}
Event ID 1025
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
product_name is set to target.application
ProcessPath is set to target.process.file.full_path
ProcessName is set to target.process.command_line
ProcessId is set to target.process.pid
Domain
principal.administrative_domain
AccountName
principal.user.userid
UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 11724
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Message
metadata.description
Product is set to target.application
Event ID 1005
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Domain
principal.administrative_domain
AccountName
principal.user.userid
UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 1038
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Domain
principal.administrative_domain
AccountName
principal.user.userid
UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 1029
Provider: MsiInstaller
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Domain
principal.administrative_domain
AccountName
principal.user.userid
UserID
principal.user.windows_sid
AccountType
principal.user.attribute.roles.name
Event ID 7030
Provider: Service Control Manager
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.appliaction is set to Printer Extensions and Notifications service
Message
metadata.description
Event ID 202
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
ActionName
security_result.action_details
TaskInstanceId
target.resource.product_object_id
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Event ID 103
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
TaskInstanceId
target.resource.product_object_id
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Event ID 119
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
InstanceId
target.resource.product_object_id
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
UserName
target.user.user_display_name
Event ID 141
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_DELETION
target.resource.resource_type = TASK
TaskName
target.resource.name
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
UserName
principal.user.user_display_name
Event ID 106
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
UserContext
target.user.user_display_name
Event ID 108
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
InstanceId
target.resource.product_object_id
Event ID 110
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
InstanceId
target.resource.product_object_id
UserContext
principal.user.user_display_name
Event ID 118
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_UNCATEGORIZED
target.resource.resource_type = TASK
TaskName
target.resource.name
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
InstanceId
target.resource.product_object_id
Event ID 142
Provider: Microsoft-Windows-TaskScheduler
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCHEDULED_TASK_DISABLE
target.resource.resource_type = TASK
TaskName
target.resource.name
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
UserName
principal.user.user_display_name
Event ID 2006
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Event ID 2001
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Event ID 216
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Event ID 2003
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Event ID 2005
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Event ID 637
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Event ID 327
Provider: ESENT
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
Message
metadata.description
Extract PID and map it to UDM field
target.process.pid
Extract src_path and map it to UDM field
src.file.full_path
Extract target_path and map it to UDM field
target.file.full_path
Event ID 17063
Provider: MSSQLSERVER
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
security_result.description
Event ID 17137
Provider: MSSQLSERVER
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Message
metadata.description
Extract database_name and map it to UDM field
target.application
Event ID 49930
Provider: MSSQLSERVER
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 852
Provider: MSSQLSERVER
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Message
metadata.description
Event ID 53504
Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
target.application = IPC
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Message
metadata.description
param2
target.domain.name
Event ID 40962
Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Message
metadata.description
Event ID 40961
Provider: Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_START
Domain
principal.administrative_domain
AccountName
principal.user.attribute.roles.name
UserID
principal.user.windows_sid
AccountType
principal.user.roles.description
Message
metadata.description
Event ID 530
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 531
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 532
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 533
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 534
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 535
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 536
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 537
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 539
Provider: Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = USER_LOGIN
security_result.action = FAIL
Event ID 1116
Provider: Microsoft-Windows-Windows Defender
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
security_result.action = UNKNOWN_ACTION
FWLink
additional.fields.key
additional.fields.value.string_value
ThreatName
security_result.threat_name
ThreatID
security_result.threat_id
SeverityName
security_result.detection_fields.key/value
CategoryName
security_result.category = SOFTWARE_PUA
security_result.category_details
Path
target.file.full_path
DetectionOrigin
security_result.detection_fields.key/value
DetectionType
security_result.detection_fields.key/value
DetectionSource
security_result.detection_fields.key/value
DetectionUser
target.user.userid
ProcessName
target.process.file.full_path
SecurityintelligenceVersion
security_result.detection_fields.key/value
EngineVersion
security_result.detection_fields.key/value
Product Name
additional.fields.key
additional.fields.value.string_value
Product Version
additional.fields.key
additional.fields.value.string_value
Detection ID
security_result.detection_fields.key/value
Detection Time
security_result.first_discovered_time
Severity ID
security_result.detection_fields.key/value
Category ID
security_result.detection_fields.key/value
Status Code
security_result.detection_fields.key/value
State
security_result.detection_fields.key/value
Source ID
security_result.detection_fields.key/value
Origin ID
security_result.detection_fields.key/value
Execution ID
security_result.detection_fields.key/value
Execution Name
security_result.detection_fields.key/value
Type ID
security_result.detection_fields.key/value
Pre Execution Status
security_result.detection_fields.key/value
Action ID
security_result.detection_fields.key/value
Action Name
security_result.action_details
Error Code
security_result.detection_fields.key/value
Error Description
security_result.description
Post Clean Status
security_result.detection_fields.key/value
Additional Actions ID
security_result.detection_fields.key/value
Additional Actions String
security_result.detection_fields.key/value
Event ID 10025
Provider: Microsoft-AzureADPasswordProtection-DCAgent
NXLog field
Event Viewer field
UDM field
Message
Extracted UserName field from the
Message
log field and mapped it to
target.user.userid
Message
Extracted FullName field from the
Message
log field and mapped it to
target.user.user_display_name
Event ID 32850
Provider : Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
param1
additional.fields.key
additional.fields.value_string
param2
principal.user.user_display_name
param3
additional.fields.key
additional.fields.value_string
Event ID 32867
Provider : Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ObjectId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
FragmentId
target.resource.product_object_id
sFlag
additional.fields.key
additional.fields.value_string
eFlag
additional.fields.key
additional.fields.value_string
FragmentLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
FragmentPayload
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 32868
Provider : Microsoft-Windows-PowerShell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ObjectId
target.resource.attribute.labels.key
target.resource.attribute.labels.value
FragmentId
target.resource.product_object_id
sFlag
additional.fields.key
additional.fields.value_string
eFlag
additional.fields.key
additional.fields.value_string
FragmentLength
target.resource.attribute.labels.key
target.resource.attribute.labels.value
FragmentPayload
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 24577
Provider : Microsoft-Windows-Powershell
NXLog field
Event Viewer field
UDM field
metadata.event_type = PROCESS_LAUNCH
FileName
target.process.file.full_path
Event ID 8194
Provider : Microsoft-Windows-Powershell
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
InstanceId
target.resource.product_object_id
MaxRunspaces
additional.fields.key
additional.fields.value_string
MinRunspaces
additional.fields.key
additional.fields.value_string
Event ID 4802
Provider : Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
TargetUserSid
principal.user.windows_sid
TargetUserName
principal.user.userid
TargetDomainName
principal.administrative_domain
TargetLogonId
additional.fields.key
additional.fields.value_string
SessionId
network.session_id
Event ID 4803
Provider : Microsoft-Windows-Security-Auditing
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
security_result.action = ALLOW
TargetUserSid
principal.user.windows_sid
TargetUserName
principal.user.userid
TargetDomainName
principal.administrative_domain
TargetLogonId
additional.fields.key
additional.fields.value_string
SessionId
network.session_id
Event ID 8001
Provider : Microsoft-Windows-WLAN-AutoConfig
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_CONNECTION
InterfaceGuid
additional.fields.key
additional.fields.value_string
InterfaceDescription
additional.fields.key
additional.fields.value_string
ConnectionMode
additional.fields.key
additional.fields.value_string
ProfileName
target.hostname
ProfileName
target.asset.hostname
SSID
target.asset.attribute.labels.key
target.asset.attribute.labels.value
BSSType
additional.fields.key
additional.fields.value_string
PHYType
additional.fields.key
additional.fields.value_string
AuthenticationAlgorithm
additional.fields.key
additional.fields.value_string
CipherAlgorithm
additional.fields.key
additional.fields.value_string
OnexEnabled
additional.fields.key
additional.fields.value_string
ConnectionId
additional.fields.key
additional.fields.value_string
NonBroadcast
additional.fields.key
additional.fields.value_string
Event ID 62
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Title
target.resource.name
Owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Url
target.url
Id
target.resource.product_object_id
Event ID 70
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
clientAddress
principal.ip
Event ID 71
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
url
target.url
timestamp
additional.fields.key
additional.fields.value_string
Event ID 72
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
id
target.resource.product_object_id
url
target.url
rangecount
additional.fields.key
additional.fields.value_string
Range.offset
additional.fields.key
additional.fields.value_string
Range.length
additional.fields.key
additional.fields.value_string
Event ID 73
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 74
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
status
security_result.description
Event ID 76
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 78
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 79
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 82
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Title, PolicyValue
Title
set to
security_results.rule_labels.key
PolicyValue
set to
security_results.rule_labels.value
Event ID 83
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Title,PolicyValue
Title
set to
security_results.rule_labels.key
PolicyValue
set to
security_results.rule_labels.value
Event ID 206
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobName
target.resource.name
url
target.url
Event ID 207
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobName
target.resource.name
url
target.url
Event ID 208
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
jobName
target.resource.name
url
target.url
Event ID 209
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobName
target.resource.name
jobId
target.resource.product_object_id
isRoaming
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 210
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
jobName
target.resource.name
url
target.url
Event ID 211
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
JobGuid
additional.fields.key
additional.fields.value_string
Title
target.resource.name
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Message
additional.fields.key
additional.fields.value_string
Event ID 212
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
SystemEvent
security_result.detection_fields
Event ID 213
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
jobName
target.resource.name
jobId
target.resource.product_object_id
FileCount
additional.fields.key
additional.fields.value_string
BlockReasonErrorCode
security_result.summary
Format:
BlockReasonErrorCode - %{BlockReasonErrorCode}
Event ID 281
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 282
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 283
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 284
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 285
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 286
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 287
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 288
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 289
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 290
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 291
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 303
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 305
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 306
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
Event ID 307
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
number
additional.fields.key
additional.fields.value_string
Event ID 308
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
number
additional.fields.key
additional.fields.value_string
Event ID 309
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 310
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 311
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
JobId
target.resource.product_object_id
JobName
target.resource.name
url
target.url
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
ErrorContext
security_result.description
bytesTransferredFromPeer
additional.fields.key
additional.fields.value_string
PeerProtocolFlags
additional.fields.key
additional.fields.value_string
Event ID 312
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 16386
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Id
target.resource.product_object_id
Title
target.resource.name
FileList
additional.fields.key
additional.fields.value_string
Event ID 16387
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Id
target.resource.product_object_id
Title
target.resource.name
Owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
PropertyName
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 16389
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Id
target.resource.product_object_id
Title
target.resource.name
Owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
DayCount
target.resource.attribute.labels.key
target.resource.attribute.labels.value
Event ID 16390
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Id
target.resource.product_object_id
Title
target.resource.name
Owner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
RetryWaitTime
additional.fields.key
additional.fields.value_string
Event ID 16391
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 16393
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
Event ID 16395
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Event ID 16396
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
rule
security_result.rule_labels.key
security_result.rule_labels.value
enabled
security_result.rule_labels.key
security_result.rule_labels.value
status
security_result.summary
Format:
status - %{status}
Event ID 16397
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
entityName
security_result.rule_labels.key
security_result.rule_labels.value
currentSize
security_result.rule_labels.key
security_result.rule_labels.value
currentLimit
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 16398
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
entityName
target.user.userid
currentSize
security_result.rule_labels.key
security_result.rule_labels.value
currentLimit
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 16400
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
entityName
target.hostname
currentSize
security_result.rule_labels.key
security_result.rule_labels.value
currentLimit
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 16402
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
entityName
security_result.rule_labels.key
security_result.rule_labels.value
currentSize
security_result.rule_labels.key
security_result.rule_labels.value
currentLimit
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 16403
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
User
principal.user.userid
jobTitle
target.resource.name
jobId
target.resource.product_object_id
jobOwner
target.resource.attribute.labels.key
target.resource.attribute.labels.value
fileCount
additional.fields.key
additional.fields.value_string
RemoteName
additional.fields.key
additional.fields.value_string
LocalName
additional.fields.key
additional.fields.value_string
processId
target.process.pid
ClientProcessStartKey
additional.fields.key
additional.fields.value_string
Event ID 16404
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SCAN_UNCATEGORIZED
function
security_result.detection_fields
line
security_result.detection_fields
hr
security_result.summary
Format:
hr - %{hr}
Event ID 16405
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
Key
security_result.rule_labels.key
security_result.rule_labels.value
SubKeyOrValueName
security_result.rule_labels.key
security_result.rule_labels.value
Event ID 17005
Provider : Microsoft-Windows-Bits-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = SERVICE_UNSPECIFIED
target.application = BITS
string
additional.fields.key
additional.fields.value_string
string2
additional.fields.key
additional.fields.value_string
string3
additional.fields.key
additional.fields.value_string
Event ID 1125
Provider : Microsoft-Windows-GroupPolicy
NXLog field
Event Viewer field
UDM field
metadata.event_type = STATUS_UPDATE
SupportInfo1
additional.fields.key
additional.fields.value_string
SupportInfo2
additional.fields.key
additional.fields.value_string
ProcessingMode
additional.fields.key
additional.fields.value_string
ProcessingTimeInMilliseconds
additional.fields.key
additional.fields.value_string
ErrorCode
security_result.summary
Format:
ErroCode - %{ErrorCode}
ErrorDescription
security_result.description
Event ID 3008
Provider : Microsoft-Windows-DNS-Client
NXLog field
Event Viewer field
UDM field
metadata.event_type = NETWORK_DNS
network.ip_protocol = DNS
QueryName
network.dns.questions.name
QueryType
network.dns.questions.type
QueryOptions
security_result.detection_fields
QueryStatus
security_result.detection_fields
QueryResults
security_result.summary
Format:
QueryResults - %{QueryResults}
Need more help?
Get answers from Community members and Google SecOps professionals.
