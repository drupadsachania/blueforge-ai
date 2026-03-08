# Email Utilities

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/email-utilities/  
**Scraped:** 2026-03-05T10:10:04.441838Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Email Utilities
Supported in:
Google secops
SOAR
Overview
A set of utility actions to assist with working with emails. Includes actions
  to parse EMLs and analyze email headers.
Actions
Analyze EML Headers
Description
Gets a Base64 EML or list of headers and extracts/analyzes its headers.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Base64 EML
String
N/A
No
Specify the Base64 string of the EML file.
Header List
JSON
N/A
No
Specify the headers list in a JSON format
Example
In this example, we’re analyzing headers from an email in a JSON format.
Action Configurations
Parameter
Value
Entities
All entities
Base64 EML
Blank
Header List
{
"From": {
"name": "Cruz Doe",
"email": "Druzdoe@example.com"
"TO": {
"name": "Rosario Smith",
"email": "RosariaSmith@example.com"
"Cc": [
"name": "Ira Johnson",
"email": "Irajohnson@example.com"
"name": "Dani Lee",
"email": "Danilee@example.com",
"Subject": "Sample email",
"Date": "Mon, 5 Apr 2023 12:00:00 -0500",
"Message-ID": "<1234567890@example.com>"
"MIME-Version": "1.0",
"Content-Type": "text/plain; charset=UTF-8",
"Content-Transfer-Encoding": "7bit",
"X-Mailer": "Microsoft Outlook",
"X-Originating-P": "192.168.0.1",
"X-Priority": "3 (Norma)l"
}
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"extracted_headers": {"F": "r", "T": "o", "C": "c", "S": "u", 
"D": "a", "M": "e", "M_2": "I", "C_2": "o", "C_3": "o", "X": "-
", "X_2": "-", "X_3": "-"}, "html_table_all_headers": 
"<table><tbody><tr><td>F</td><td>r</td></tr><tr><td>T</td><td>o</td></tr><tr><td>C</td><td>c</td></tr><tr><td>S</td><td>u</td></tr><tr><td>D</td><td>a</td></tr><tr><td>M</td><td>e</td></tr><tr><td>M_2</td><td>I</td></tr><tr><td>C_2</td><td>o</td></tr><tr><td>C_3</td><td>o</td></tr><tr><td>X</td><td>-</td></tr><tr><td>X_2</td><td>-</td></tr><tr><td>X_3</td><td>-</td></tr></tbody></table>", "list_of_domain_address": [], "header_analysis_result": [{"message": "\"Return-Path\" header does not exist", "score": 5, "status": "<div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #FF0000;  border-radius: 50%;  display: inline-block;\"></span></div>"}, {"message": "\"X-Distribution\" header checked (does not exist)", "score": 0, "status": "<div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #00FF00;  border-radius: 50%;  display: inline-block;\"></span></div>"}, {"message": "\"Bcc\" header checked (does not exist)", "score": 0, "status": "<div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #00FF00;  border-radius: 50%;  display: inline-block;\"></span></div>"}, {"message": "\"X-UIDL\" header checked (does not exist)", "score": 0, "status": "<div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #00FF00;  border-radius: 50%;  display: inline-block;\"></span></div>"}, {"message": "\"Message-ID\" header missing from original EML", "score": 5, "status": "<div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #FF0000;  border-radius: 50%;  display: inline-block;\"></span></div>"}], "total_rules_matched": 2, "total_rules_checked": 5, "header_analysis_result_html": "<table><tr><td style=\"padding-right:12px\"><div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #FF0000;  border-radius: 50%;  display: inline-block;\"></span></div></td><td>\"Return-Path\" header does not exist</td></tr><tr><td style=\"padding-right:12px\"><div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #00FF00;  border-radius: 50%;  display: inline-block;\"></span></div></td><td>\"X-Distribution\" header checked (does not exist)</td></tr><tr><td style=\"padding-right:12px\"><div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #00FF00;  border-radius: 50%;  display: inline-block;\"></span></div></td><td>\"Bcc\" header checked (does not exist)</td></tr><tr><td style=\"padding-right:12px\"><div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #00FF00;  border-radius: 50%;  display: inline-block;\"></span></div></td><td>\"X-UIDL\" header checked (does not exist)</td></tr><tr><td style=\"padding-right:12px\"><div style=\"text-align:center\"><span style=\"height: 5px;  width: 5px;  background-color: #FF0000;  border-radius: 50%;  display: inline-block;\"></span></div></td><td>\"Message-ID\" header missing from original EML</td></tr></table>"
}
Analyze Headers
Description
Validates SPF, DMARC, ARC, and DKIM records in the email. It will also check
  to see if any of the relay servers are blocklisted by querying multiple RBLs
  and enrich them with geo-location and IP whois information. It accepts a JSON
  object containing a list of Email headers.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Header JSON
JSON
N/A
Yes
Specify the JSON object that contains email headers. TIP: Use
        “Buffer” action in Tools Powerup to convert string to JSON
        object
Example
In this scenario, we’re passing the json header to Buffer action, which
  converts a string to a json object, and then passing it to the Analyze Headers
  actions.
Action Configurations
Parameter
Value
Entities
All entities
Headers JSON
[Tools_Buffer_1.JsonResult | "header"]
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
{
"From": "\"test@example.com\" <test@examplecom>", "To": "test2@example.com, test2@example.com, mailmaster@example.com, mailmaster@example.org, webmaster@example.com, webmaster@example.org, webmaster@example.jp, mailmaster@example.jp", "Subject": "test confirmation", "MessageID": "<05c18622-f2ad-cb77-2ce9-a0bbfc7d7ad0@clear-code.com>", "Date": "Thu, 15 Aug 2019 14:54:37 +0900", "FromDomain": "clear-code.com", "FromParentDomain": "clear-code.com", "MFromDomain": "clear-code.com", "SPF": {"record": "v=spf1 ip4:219.94.234.64 ip4:153.126.206.245 ip6:2401:2500:102:3039:153:126:206:245 a:mail.clear-code.com aaaa:mail.clear-code.com ~all", "valid": true, "dns_lookups": 2, "warnings": ["The domain aaa:mail.clear-code.com does not exist"], "parsed": {"pass": [{"value": "219.94.234.64", "mechanism": "ip4"}, {"value": "153.126.206.245", "mechanism": "ip4"}, {"value": "2401:2500:102:3039:153:126:206:245", "mechanism": "ip6"}, {"value": "153.126.206.245", "mechanism": "a"}, {"value": "2401:2500:102:3039:153:126:206:245", "mechanism": "a"}], "neutral": [], "softfail": [], "fail": [], "include": [], "redirect": null, "exp": null, "all": "softfail"}, "Auth": false}, "DMARC": {"record": "v=DMARC1;p=none;sp=none", "valid": true, "location": "clear-code.com", "warnings": ["rua tag (destination for aggregate reports) not found"], "tags": {"v": {"value": "DMARC1", "explicit": true, "name": "Version", "description": "Identifies the record retrieved as a DMARC record. It MUST have the value of \"DMARC1\". The value of this tag MUST match precisely; if it does not or it is absent, the entire retrieved record MUST be ignored. It MUST be the first tag in the list."}, "p": {"value": "none", "explicit": true, "name": "Requested Mail Receiver Policy", "description": "Specifies the policy to be enacted by the Receiver at the request of the Domain Owner. The policy applies to the domain and to its subdomains, unless subdomain policy is explicitly described using the \"sp\" tag."}, "sp": {"value": "none", "explicit": true, "name": "Subdomain Policy", "description": "Indicates the policy to be enacted by the Receiver at the request of the Domain Owner. It applies only to subdomains of the domain queried, and not to the domain itself. Its syntax is identical to that of the \"p\" tag defined above. If absent, the policy specified by the \"p\" tag MUST be applied for subdomains."}, "adkim": {"value": "r", "explicit": false, "name": "DKIM Alignment Mode", "default": "r", "description": "In relaxed mode, the Organizational Domains of both the DKIM-authenticated signing domain (taken from the value of the \"d=\" tag in the signature) and that of the RFC 5322 From domain must be equal if the identifiers are to be considered aligned."}, "aspf": {"value": "r", "explicit": false, "name": "SPF alignment mode", "default": "r", "description": "In relaxed mode, the SPF-authenticated domain and RFC 5322 From domain must have the same Organizational Domain. In strict mode, only an exact DNS domain match is considered to produce Identifier Alignment."}, "fo": {"value": ["0"], "explicit": false, "name": "Failure Reporting Options", "default": "0", "description": "0: Generate a DMARC failure report if all underlying authentication mechanisms fail to produce an aligned \"pass\" result."}, "pct": {"value": 100, "explicit": false, "name": "Percentage", "default": 100, "description": "Integer percentage of messages from the Domain Owner's mail stream to which the DMARC policy is to be applied. However, this MUST NOT be applied to the DMARC-generated reports, all of which must be sent and received unhindered. The purpose of the \"pct\" tag is to allow Domain Owners to enact a slow rollout of enforcement of the DMARC mechanism."}, "rf": {"value": ["afrf"], "explicit": false, "name": "Report Format", "default": "afrf", "description": "afrf:  \"Authentication Failure Reporting Using the Abuse Reporting Format\", RFC 6591, April 2012,<http://www.rfc-editor.org/info/rfc6591>"}, "ri": {"value": 86400, "explicit": false, "name": "Report Interval", "default": 86400, "description": "Indicates a request to Receivers to generate aggregate reports separated by no more than the requested number of seconds. DMARC implementations MUST be able to provide daily reports and SHOULD be able to provide hourly reports when requested. However, anything other than a daily report is understood to be accommodated on a best-effort basis."}}}, "MX": {"hosts": [{"preference": 10, "hostname": "mail.clear-code.com", "addresses": ["153.126.206.245", "2401:2500:102:3039:153:126:206:245"], "tls": true, "starttls": true}], "warnings": []}, "DNSSec": false, "DKIMVerify": false, "ARCVerify": {"result": "none", "details": [], "reason": "Message is not ARC signed"}, "RelayInfo": [], "SourceServer": "", "StrongSPF": true
}
Parse Base64 Email
Description
Improved version of Parse EML Base64 action. It parses EML and MSG files.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Stop Transport At Header
String
N/A
No
Specify the header field you want to stop processing the transport at.
EML/MSG Base64 String
String
N/A
Yes
Specify the base64 representation of an EML or MSG file
Blocklisted Headers
String
N/A
No
Specify the headers to exclude from the response.
Use blocklist as Allowlist
Checkbox
Unchecked
No
Specify whether to include the listed headers.
Example
In this scenario, we’re parsing an EML email that’s represented in
  Base64 format.
Action Configurations
Parameter
Value
Entities
All entities
Stop Transport At Header
Blank
EML/MSG Base64 String
RGVsaXZIcmVkLVRvOiBvdGhtYWSIbUBnb29nbGUu\29tDQpSZWNl
   axZIZDogYnkgMjAwMjphMDU6NzMwMDo2MTQ30mlwojhlOmMyZjI6NTQ0OSB3aXRoIFNNVFAgaWQg
   aTdjc3AyMjcwMjMwZHliOwOKICAgICAgICBTYXQsIDE3IERIYyAyMDlyDE40j|20j|5ICOwODAwIChQ
   U1QpDQpYLUdvb2dsZ51TbXRWLVNvdXJjZTogQU1ywGRYdHIqR2cycl|XUTQvNORsNIB1MZRUOEg2VkVa
   L1|WZT]RLZV3Z2jvaERxbm94TzhhNisOMFIVbDBQNExrWnd4VF]GcHpLZgOKWC1SZWNlaXZIZDogYnkgMj
   AwMjphMDU6NmEyMDpkOTA10mlwOmFmOmIxNmI6\ZWViNSB3aXRolFNNVFAgaWQgamQ1LTIwMDIwYTA
   1NmEyMGQ5MDUWMGIWMDBhZmIxNmjIZ
Blocklisted Headers
Blank
User Blocklist As Allowlist
Blank
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
{ 
"date": "2019-08-15 14:54:37+09:00", "from": "test@example.com", "header": { "content-language": [ "en-US" ], "content-type": [ "multipart/mixed; boundary=\"------------26A45336F6C6196BD8BBA2A2\"" ], "date": [ "Thu, 15 Aug 2019 14:54:37 +0900" ], "fcc": [ "imap://test@example.com/Sent" ], "from": [ "\"test@example.com\" <piro-test@clear-code.com>" ], "message-id": [ "<05c18622-f2ad-cb77-2ce9-a0bbfc7d7ad0@clear-code.com>" ], "mime-version": [ "1.0" ], "subject": [ "test confirmation" ], "to": [ "test3@example.com, test3@example.com, mailmaster@example.com, mailmaster@example.org, webmaster@example.com, webmaster@example.org, webmaster@example.jp, mailmaster@example.jp" ], "user-agent": [ "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Thunderbird/69.0" ], "x-account-key": [ "account1" ], "x-identity-key": [ "id1" ], "x-mozilla-draft-info": [ "internal/draft; vcard=0; receipt=0; DSN=0; uuencode=0; attachmentreminder=0; deliveryformat=4" ] }, "received": [], "received_domains_internal": [], "receiving": [], "sending": [], "subject": "test confirmation", "to": [ "piro.outsider.reflex+1@gmail.com", "piro.outsider.reflex+2@gmail.com", "mailmaster@example.com", "mailmaster@example.org", "webmaster@example.com", "webmaster@example.org", "webmaster@example.jp", "mailmaster@example.jp" ]
 }
Parse Case Wall Email
Description
This action will parse an EML or MSG file that has been attached to the case
  wall.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Create Entities
Checkbox
Checked
No
When enabled, this will create User entities out of the To and From
        headers and Email Subject entity out of the Subject field.
Exclude Entities Regex
String
N/A
No
Observed entities that match the supplied regex will not be created.
Original EML Only
Checkbox
Checked
No
Extracts attachment from the original EML only.
Created Observed Entities
Dropdown
All
No
Create entities out of the observed entities in the email body.
        ‘All’ will create URL, Email, IP, and Hash entities.
Save Attachment to Case Wall.
Checkbox
Checked
No
Save the extracted attachment to the case wall
Fang Entities
Checkbox
Checked
No
When enabled, entities that are defanged will be converted to fanged
        entities.
Custom Entity Regexes
Dropdown
JSON
No
A JSON object that can parse out entities from body and subject.
Example
In this example, we’re parsing an EML file that’s attached to the
  case wall. If there are attachments within the EML file, they will be added to
  the case wall. We're also creating entities based on the data in the file.
Action Configurations
Parameter
Value
Create Entities
Checked
Exclude Entities Regex
Blank
Original EML Only
Checked
Created Observed Entities
All
Save Attachment to Case Wall.
Checked
Fang Entities
Checked
Custom Entity Regexes
Blank
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
{"parsed_emails": [{"attached_emails": [{"attachments": [{"content_header": {"content-disposition": ["attachment; filename=\"attachment.txt\""], "content-transfer-encoding": ["base64"], "content-type": ["text/plain; name=\"attachment.txt\""]}, "extension": "txt", "filename": "attachment.txt", "hash": {"md5": "6529d73ba8183760ad174644e75684fe", "sha1": "dd88508cda7bcfc71ffdbc0e26afe97d3fb9a0b6", "sha256": "1f209f1560df8cb6e983dff99d7a7d2db8dc3e439226abd38ef34facdffd82ec", "sha512": "310d2df6f770dafdf4f84d9851e3fad011d4eb0c5a8af9a5f6d237fb733bca41d41ad6b00efdc
2b5c218207f1a1ac99339923d3c389368f0c1d2ba58e8e1893a"},
 "level": 0, "mime_type": "ASCII text, with no line terminators", "mime_type_short": "text/plain", "ole_data": [{"description": "", "hide_if_false": true, "id": "ftype", "name": "File format", "risk": "info", "value": "Unknown file type"}, {"description": "Container type", "hide_if_false": true, "id": "container", "name": "Container format", "risk": "info", "value": "Unknown Container"}, {"description": "The file is not encrypted", "hide_if_false": false, "id": "encrypted", "name": "Encrypted", "risk": "none", "value": false}, {"description": "This file contains VBA macros. No suspicious keyword was found. Use olevba and mraptor for more info.", "hide_if_false": false, "id": "vba", "name": "VBA Macros", "risk": "Medium", "value": "Yes"}, {"description": "This file does not contain Excel 4/XLM macros.", "hide_if_false": false, "id": "xlm", "name": "XLM Macros", "risk": "none", "value": "No"}, {"description": "External relationships such as remote templates, remote OLE objects, etc", "hide_if_false": false, "id": "ext_rels", "name": "External Relationships", "risk": "none", "value": 0}, {"description": "Contains an ObjectPool stream, very likely to contain embedded OLE objects or files. Use oleobj to check it.", "hide_if_false": true, "id": "ObjectPool", "name": "ObjectPool", "risk": "none", "value": false}, {"description": "Number of embedded Flash objects (SWF files) detected in OLE streams. Not 100% accurate, there may be false positives.", "hide_if_false": true, "id": "flash", "name": "Flash objects", "risk": "none", "value": 0}], "size": 64}], "body": [{"content": "This is an HTML message. Please use an HTML capable mail program to read\nthis message.\n", "content_type": "text/plain", "hash": "f342fe66117848e74b7bbade740715d2bf9e0487b0386abdf54eb8f3371e9f33", "parsed_entities": []}, {"content": "<html>\n<head>\n<title>Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message</title>\n<style type=\"text/css\"><!--\nbody { color: black ; font-family: arial, helvetica, sans-serif ; background-color: #A3C5CC }\nA:link, A:visited, A:active { text-decoration: underline }\n--></style>\n</head>\n<body>\n<table background=\"cid:4c837ed463ad29c820668e835a270e8a.gif\" width=\"100%\">\n<tr>\n<td>\n<center><h1>Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message</h1></center>\n<hr>\n<P>Hello Manuel,<br><br>\nThis message is just to let you know that the <a href=\"http://www.phpclasses.org/mimemessage\">MIME E-mail message composing and sending PHP class</a> is working as expected.<br><br>\n<center><h2>Here is an image embedded in a message as a separate part:</h2></center>\n<center><img src=\"cid:ae0357e57f04b8347f7621662cb63855.gif\"></center>Thank you,<br>\nmlemos</p>\n</td>\n</tr>\n</table>\n</body>\n</html>", "content_type": "text/html", "hash": "976f0f71aa3bb9c03229231d456db63637713b156e7728e7297266b070cbb21e", "parsed_entities": [{"entity_type": "DestinationURL", "identifier": "http://www.phpclasses.org/mimemessage"}, {"entity_type": "DOMAIN", "identifier": "phpclasses.org"}]}], "header": {"bcc": [], "cc": [], "date": "2005-04-30T19:28:29-03:00", "delivered_to": [], "from": "mlemos@acm.org", "header": {"content-type": ["multipart/mixed; boundary=\"652b8c4dcb00cdcdda1e16af36781caf\""], "date": ["Sat, 30 Apr 2005 19:28:29 -0300"], "from": ["mlemos <mlemos@acm.org>"], "message-id": ["<20050430192829.0489.mlemos@acm.org>"], "mime-version": ["1.0"], "reply-to": ["mlemos <mlemos@acm.org>"], "return-path": ["<mlemos@acm.org>"], "sender": ["mlemos@acm.org"], "subject": ["Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message"], "to": ["Manuel Lemos <mlemos@linux.local>"], "x-mailer": ["http://www.phpclasses.org/mimemessage $Revision: 1.63 $ (mail)"]}, "parsed_entities": [], "received": [], "receiving": [], "reply_to": "mlemos@acm.org", "return_path": null, "sending": [], "subject": "Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message", "to": ["mlemos@linux.local"], "transport": null}, "level": 0, "source_file": "sample.eml"}], "attachment_id": 17, "attachment_name": "sample.eml", "attachments": [{"content_header": {"content-disposition": ["attachment; filename=\"attachment.txt\""], "content-transfer-encoding": ["base64"], "content-type": ["text/plain; name=\"attachment.txt\""]}, "extension": "txt", "filename": "attachment.txt", "hash": {"md5": "6529d73ba8183760ad174644e75684fe", "sha1": "dd88508cda7bcfc71ffdbc0e26afe97d3fb9a0b6", "sha256": "1f209f1560df8cb6e983dff99d7a7d2db8dc3e439226abd38ef34facdffd82ec", "sha512": "310d2df6f770dafdf4f84d9851e3fad011d4eb0c5a8af9a5f6d237fb733bca41d41ad6b00efdc
 2b5c218207f1a1ac99339923d3c389368f0c1d2ba58e8e1893a"}, 
 "level": 0, "mime_type": "ASCII text, with no line terminators", "mime_type_short": "text/plain", "ole_data": [{"description": "", "hide_if_false": true, "id": "ftype", "name": "File format", "risk": "info", "value": "Unknown file type"}, {"description": "Container type", "hide_if_false": true, "id": "container", "name": "Container format", "risk": "info", "value": "Unknown Container"}, {"description": "The file is not encrypted", "hide_if_false": false, "id": "encrypted", "name": "Encrypted", "risk": "none", "value": false}, {"description": "This file contains VBA macros. No suspicious keyword was found. Use olevba and mraptor for more info.", "hide_if_false": false, "id": "vba", "name": "VBA Macros", "risk": "Medium", "value": "Yes"}, {"description": "This file does not contain Excel 4/XLM macros.", "hide_if_false": false, "id": "xlm", "name": "XLM Macros", "risk": "none", "value": "No"}, {"description": "External relationships such as remote templates, remote OLE objects, etc", "hide_if_false": false, "id": "ext_rels", "name": "External Relationships", "risk": "none", "value": 0}, {"description": "Contains an ObjectPool stream, very likely to contain embedded OLE objects or files. Use oleobj to check it.", "hide_if_false": true, "id": "ObjectPool", "name": "ObjectPool", "risk": "none", "value": false}, {"description": "Number of embedded Flash objects (SWF files) detected in OLE streams. Not 100% accurate, there may be false positives.", "hide_if_false": true, "id": "flash", "name": "Flash objects", "risk": "none", "value": 0}], "size": 64}], "result": {"attachments": [{"content_header": {"content-disposition": ["attachment; filename=\"attachment.txt\""], "content-transfer-encoding": ["base64"], "content-type": ["text/plain; name=\"attachment.txt\""]}, "extension": "txt", "filename": "attachment.txt", "hash": {"md5": "6529d73ba8183760ad174644e75684fe", "sha1": "dd88508cda7bcfc71ffdbc0e26afe97d3fb9a0b6", "sha256": "1f209f1560df8cb6e983dff99d7a7d2db8dc3e439226abd38ef34facdffd82ec", "sha512": "310d2df6f770dafdf4f84d9851e3fad011d4eb0c5a8af9a5f6d237fb733bca41d41ad6b00efdc
 2b5c218207f1a1ac99339923d3c389368f0c1d2ba58e8e1893a"}, 
 "level": 0, "mime_type": "ASCII text, with no line terminators", "mime_type_short": "text/plain", "ole_data": [{"description": "", "hide_if_false": true, "id": "ftype", "name": "File format", "risk": "info", "value": "Unknown file type"}, {"description": "Container type", "hide_if_false": true, "id": "container", "name": "Container format", "risk": "info", "value": "Unknown Container"}, {"description": "The file is not encrypted", "hide_if_false": false, "id": "encrypted", "name": "Encrypted", "risk": "none", "value": false}, {"description": "This file contains VBA macros. No suspicious keyword was found. Use olevba and mraptor for more info.", "hide_if_false": false, "id": "vba", "name": "VBA Macros", "risk": "Medium", "value": "Yes"}, {"description": "This file does not contain Excel 4/XLM macros.", "hide_if_false": false, "id": "xlm", "name": "XLM Macros", "risk": "none", "value": "No"}, {"description": "External relationships such as remote templates, remote OLE objects, etc", "hide_if_false": false, "id": "ext_rels", "name": "External Relationships", "risk": "none", "value": 0}, {"description": "Contains an ObjectPool stream, very likely to contain embedded OLE objects or files. Use oleobj to check it.", "hide_if_false": true, "id": "ObjectPool", "name": "ObjectPool", "risk": "none", "value": false}, {"description": "Number of embedded Flash objects (SWF files) detected in OLE streams. Not 100% accurate, there may be false positives.", "hide_if_false": true, "id": "flash", "name": "Flash objects", "risk": "none", "value": 0}], "size": 64}], "body": [{"content": "This is an HTML message. Please use an HTML capable mail program to read\nthis message.\n", "content_type": "text/plain", "hash": "f342fe66117848e74b7bbade740715d2bf9e0487b0386abdf54eb8f3371e9f33", "parsed_entities": []}, {"content": "<html>\n<head>\n<title>Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message</title>\n<style type=\"text/css\"><!--\nbody { color: black ; font-family: arial, helvetica, sans-serif ; background-color: #A3C5CC }\nA:link, A:visited, A:active { text-decoration: underline }\n--></style>\n</head>\n<body>\n<table background=\"cid:4c837ed463ad29c820668e835a270e8a.gif\" width=\"100%\">\n<tr>\n<td>\n<center><h1>Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message</h1></center>\n<hr>\n<P>Hello Manuel,<br><br>\nThis message is just to let you know that the <a href=\"http://www.phpclasses.org/mimemessage\">MIME E-mail message composing and sending PHP class</a> is working as expected.<br><br>\n<center><h2>Here is an image embedded in a message as a separate part:</h2></center>\n<center><img src=\"cid:ae0357e57f04b8347f7621662cb63855.gif\"></center>Thank you,<br>\nmlemos</p>\n</td>\n</tr>\n</table>\n</body>\n</html>", "content_type": "text/html", "hash": "976f0f71aa3bb9c03229231d456db63637713b156e7728e7297266b070cbb21e", "parsed_entities": [{"entity_type": "DestinationURL", "identifier": "http://www.phpclasses.org/mimemessage"}, {"entity_type": "DOMAIN", "identifier": "phpclasses.org"}]}], "header": {"bcc": [], "cc": [], "date": "2005-04-30T19:28:29-03:00", "delivered_to": [], "from": "mlemos@acm.org", "header": {"content-type": ["multipart/mixed; boundary=\"652b8c4dcb00cdcdda1e16af36781caf\""], "date": ["Sat, 30 Apr 2005 19:28:29 -0300"], "from": ["mlemos <mlemos@acm.org>"], "message-id": ["<20050430192829.0489.mlemos@acm.org>"], "mime-version": ["1.0"], "reply-to": ["mlemos <mlemos@acm.org>"], "return-path": ["<mlemos@acm.org>"], "sender": ["mlemos@acm.org"], "subject": ["Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message"], "to": ["Manuel Lemos <mlemos@linux.local>"], "x-mailer": ["http://www.phpclasses.org/mimemessage $Revision: 1.63 $ (mail)"]}, "parsed_entities": [], "received": [], "receiving": [], "reply_to": "mlemos@acm.org", "return_path": null, "sending": [], "subject": "Testing Manuel Lemos' MIME E-mail composing and sending PHP class: HTML message", "to": ["mlemos@linux.local"], "transport": null}, "level": 0, "source_file": "sample.eml"}}]
}
Parse EML Base64 Blob
Description
Decodes a base64 string and attempts to parse it as an EML file.  It will return a list of parsed objects.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Base64 EML Blob
String
N/A
Yes
Specify the Base64 encoded string of an EML file.
Example
In this example, we're passing a base64 representation of an email file to parse its content.
Action Configurations
Parameter
Value
Entities
All entities
EML/MSG Base64 String
RkNDOiBpbWFwOi8vcGlyby10ZXN0QG1haWwuY2xlYXItY29kZS5jb20vU2VudApYLUlkZW50aXR
5LUtleTogaWQxClgtQWNjb3VudC1LZXk6IGFjY291bnQxCkZyb206ICJwaXJvLXRlc3RAY2xlYXI
tY29kZS5jb20iIDxwaXJvLXRlc3RAY2xlYXItY29kZS5jb20+ClN1YmplY3Q6IHRlc3QgY29uZ
mlybWF0aW9uClRvOiBwaXJvLm91dHNpZGVyLnJlZmxleCsxQGdtYWlsLmNvbSwgcGlyby5vdXRzaWRl
ci5yZWZsZXgrMkBnbWFpbC5jb20sCiBtYWlsbWFzdGVyQGV4YW1wbGUuY29tLCBtYWlsbWFzdGVyQGV
4YW1wbGUub3JnLCB3ZWJtYXN0ZXJAZXhhbXBsZS5jb20sCiB3ZWJtYXN0ZXJAZXhhbXBsZS5vcmcs
IHdlYm1hc3RlckBleGFtcGxlLmpwLCBtYWlsbWFzdGVyQGV4YW1wbGUuanAKTWVzc2FnZS1JRDogPDA1
YzE4NjIyLWYyYWQtY2I3Ny0yY2U5LWEwYmJmYzdkN2FkMEBjbGVhci1jb2RlLmNvbT4KRGF0Z
TogVGh1LCAxNSBBdWcgMjAxOSAxNDo1NDozNyArMDkwMApYLU1vemlsbGEtRHJhZnQtSW5mbzogaW50Z
XJuYWwvZHJhZnQ7IHZjYXJkPTA7IHJlY2VpcHQ9MDsgRFNOPTA7IHV1ZW5jb2RlPTA7CiBhdHRhY2ht
ZW50cmVtaW5kZXI9MDsgZGVsaXZlcnlmb3JtYXQ9NApVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2lu
ZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjo2OS4wKSBHZWNrby8yMDEwMDEwMQogVGh1bmRlcmJp
cmQvNjkuMApNSU1FLVZlcnNpb246IDEuMApDb250ZW50LVR5cGU6IG11bHRpcGFydC9taXhlZDsKIGJv
dW5kYXJ5PSItLS0tLS0tLS0tLS0yNkE0NTMzNkY2QzYxOTZCRDhCQkEyQTIiCkNvbnRlbnQtTGFuZ3V
hZ2U6IGVuLVVTCgpUaGlzIGlzIGEgbXVsdGktcGFydCBtZXNzYWdlIGluIE1JTUUgZm9ybWF0LgotLS0
tLS0tLS0tLS0tLTI2QTQ1MzM2RjZDNjE5NkJEOEJCQTJBMgpDb250ZW50LVR5cGU6IHRleHQvcGxh
aW47IGNoYXJzZXQ9dXRmLTg7IGZvcm1hdD1mbG93ZWQKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZ
zogN2JpdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0d
VzdAotLS0tLS0tLS0tLS0tLTI2QTQ1MzM2RjZDNjE5NkJEOEJCQTJBMgpDb250ZW50LVR5cGU6IH
RleHQvcGxhaW47IGNoYXJzZXQ9VVRGLTg7CiBuYW1lPSJzaGExaGFzaC50eHQiCkNvbnRlbnQtVH
JhbnNmZXItRW5jb2Rpbmc6IGJhc2U2NApDb250ZW50LURpc3Bvc2l0aW9uOiBhdHRhY2htZW50Ow
ogZmlsZW5hbWU9InNoYTFoYXNoLnR4dCIKTnpSak9HWXdPV1JtWVRNd1pXRmpZMlppTXpreVlqRX
pNak14Tkdaak5tSTVOemhtTXpJMVlTQXFabXhsZUMxamIyNW1hWEp0CkxXMWhhV3d1TVM0eE1DNH
dMbmh3YVFwalkyVmxOR0kwWVdFME4yWTFNVE5oWW1ObE16UXlZMlV4WlRKbFl6Sm1aRGsyTURCbA
pNekZpSUNwbWJHVjRMV052Ym1acGNtMHRiV0ZwYkM0eExqRXhMakF1ZUhCcENqQTNNV1U1WlRNM0
9HRmtNREUzT1dKbVlXUmkKTVdKa1l6WTFNR0UwT1RRMU5HUXlNRFJoT0RNZ0ttWnNaWGd0WTI5dV
ptbHliUzF0WVdsc0xqRXVNVEl1TUM1NGNHa0tPV1EzCllXRXhOVE0wTVRobFlUaG1ZbU00WW1VM1l
tRTJaalUwWTJVNFlURmpZamRsWlRRMk9DQXFabXhsZUMxamIyNW1hWEp0TFcxaAphV3d1TVM0NUxq
a3VlSEJwQ2pneE5qZzFOak5qWWpJM05tVmhOR1k1WVRKaU5qTXdZamxoTWpBM1pEa3dabUl4TVRn
MU5tVWcKS21ac1pYZ3RZMjl1Wm1seWJTMXRZV2xzTG5od2FRbz0KLS0tLS0tLS0tLS0tLS0yNkE0
NTMzNkY2QzYxOTZCRDhCQkEyQTIKQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi9qc29uOwogbmFt
ZT0ibWFuaWZlc3QuanNvbiIKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogYmFzZTY0CkNvbnRl
bnQtRGlzcG9zaXRpb246IGF0dGFjaG1lbnQ7CiBmaWxlbmFtZT0ibWFuaWZlc3QuanNvbiIKZXdvZ
0lDSnRZVzVwWm1WemRGOTJaWEp6YVc5dUlqb2dNaXdLSUNBaVlYQndiR2xqWVhScGIyNXpJam9nZ
XdvZ0lDQWdJbWRsClkydHZJam9nZXdvZ0lDQWdJQ0FpYVdRaU9pQWlabXhsZUdsaWJHVXRZMjl1Wm
1seWJTMXRZV2xzUUdOc1pXRnlMV052WkdVdQpZMjl0SWl3S0lDQWdJQ0FnSW5OMGNtbGpkRjl0YVc
1ZmRtVnljMmx2YmlJNklDSTJPQzR3SWdvZ0lDQWdmUW9nSUgwc0NpQWcKSW01aGJXVWlPaUFpUm1
4bGVDQkRiMjVtYVhKdElFMWhhV3dpTEFvZ0lDSmtaWE5qY21sd2RHbHZiaUk2SUNKRGIyNW1hWEp
0CklHMWhhV3hoWkdSeVpYTnpJR0Z1WkNCaGRIUmhZMmh0Wlc1MGN5QmlZWE5sWkNCdmJpQm1iR1Y0
YVdKc1pTQnlkV3hsY3k0aQpMQW9nSUNKMlpYSnphVzl1SWpvZ0lqSXVNQ0lzQ2dvZ0lDSnNaV2Ro
WTNraU9pQjdDaUFnSUNBaWRIbHdaU0k2SUNKNGRXd2kKTEFvZ0lDQWdJbTl3ZEdsdmJuTWlPaUI3
Q2lBZ0lDQWdJQ0p3WVdkbElqb2dJbU5vY205dFpUb3ZMMk52Ym1acGNtMHRiV0ZwCmJDOWpiMjUwW
lc1MEwzTmxkSFJwYm1jdWVIVnNJaXdLSUNBZ0lDQWdJbTl3Wlc1ZmFXNWZkR0ZpSWpvZ2RISjFa
UW9nSUNBZwpmUW9nSUgwS2ZRPT0KLS0tLS0tLS0tLS0tLS0yNkE0NTMzNkY2QzYxOTZCRDhCQkEyQ
TItLQ==
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
True
JSON Result
[{
"Entity": "test confirmation", "EntityResult": {"base64_blob": "RkNDOiBpbWFwOi8vcGlyby10ZXN0QG1haWwuY2xlYXItY29kZS5jb20vU2VudApYLUlkZW50aXR5LUtleTogaWQxCl
gtQWNjb3VudC1LZXk6IGFjY291bnQxCkZyb206ICJwaXJvLXRlc3RAY2xlYXItY29kZS5jb20iIDxwaXJvLXRlc3RAY2xlYXItY29kZS5jb20+ClN1YmplY3Q6IHRlc3QgY29uZmlybWF0aW9uClRvOiBwaXJvLm91dHNpZGVyLnJlZmxleCsxQGdtYWlsLmNvbSwgcGlyby5vdXRzaWRlci5yZWZsZXgrMkBnbWFpbC5jb20sCiBtYWlsbWFzdGVyQGV4YW1wbGUuY29tLCBtYWlsbWFzdGVyQGV4YW1wbGUub3JnLCB3ZWJtYXN0ZXJAZXhhbXBsZS5jb20sCiB3ZWJtYXN0ZXJAZXhhbXBsZS5vcmcsIHdlYm1hc3RlckBleGFtcGxlLmpwLCBtYWlsbWFzdGVyQGV4YW1wbGUuanAKTWVzc2FnZS1JRDogPDA1YzE4NjIyLWYyYWQtY2I3Ny0yY2U5LWEwYmJmYzdkN2FkMEBjbGVhci1jb2RlLmNvbT4KRGF0ZTogVGh1LCAxNSBBdWcgMjAxOSAxNDo1NDozNyArMDkwMApYLU1vemlsbGEtRHJhZnQtSW5mbzogaW50ZXJuYWwvZHJhZnQ7IHZjYXJkPTA7IHJlY2VpcHQ9MDsgRFNOPTA7IHV1ZW5jb2RlPTA7CiBhdHRhY2htZW50cmVtaW5kZXI9MDsgZGVsaXZlcnlmb3JtYXQ9NApVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjo2OS4wKSBHZWNrby8yMDEwMDEwMQogVGh1bmRlcmJpcmQvNjkuMApNSU1FLVZlcnNpb246IDEuMApDb250ZW50LVR5cGU6IG11bHRpcGFydC9taXhlZDsKIGJvdW5kYXJ5PSItLS0tLS0tLS0tLS0yNkE0NTMzNkY2QzYxOTZCRDhCQkEyQTIiCkNvbnRlbnQtTGFuZ3VhZ2U6IGVuLVVTCgpUaGlzIGlzIGEgbXVsdGktcGFydCBtZXNzYWdlIGluIE1JTUUgZm9ybWF0LgotLS0tLS0tLS0tLS0tLTI2QTQ1MzM2RjZDNjE5NkJEOEJCQTJBMgpDb250ZW50LVR5cGU6IHRleHQvcGxhaW47IGNoYXJzZXQ9dXRmLTg7IGZvcm1hdD1mbG93ZWQKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogN2JpdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAp0ZXN0dGVzdAotLS0tLS0tLS0tLS0tLTI2QTQ1MzM2RjZDNjE5NkJEOEJCQTJBMgpDb250ZW50LVR5cGU6IHRleHQvcGxhaW47IGNoYXJzZXQ9VVRGLTg7CiBuYW1lPSJzaGExaGFzaC50eHQiCkNvbnRlbnQtVHJhbnNmZXItRW5jb2Rpbmc6IGJhc2U2NApDb250ZW50LURpc3Bvc2l0aW9uOiBhdHRhY2htZW50OwogZmlsZW5hbWU9InNoYTFoYXNoLnR4dCIKTnpSak9HWXdPV1JtWVRNd1pXRmpZMlppTXpreVlqRXpNak14Tkdaak5tSTVOemhtTXpJMVlTQXFabXhsZUMxamIyNW1hWEp0CkxXMWhhV3d1TVM0eE1DNHdMbmh3YVFwalkyVmxOR0kwWVdFME4yWTFNVE5oWW1ObE16UXlZMlV4WlRKbFl6Sm1aRGsyTURCbApNekZpSUNwbWJHVjRMV052Ym1acGNtMHRiV0ZwYkM0eExqRXhMakF1ZUhCcENqQTNNV1U1WlRNM09HRmtNREUzT1dKbVlXUmkKTVdKa1l6WTFNR0UwT1RRMU5HUXlNRFJoT0RNZ0ttWnNaWGd0WTI5dVptbHliUzF0WVdsc0xqRXVNVEl1TUM1NGNHa0tPV1EzCllXRXhOVE0wTVRobFlUaG1ZbU00WW1VM1ltRTJaalUwWTJVNFlURmpZamRsWlRRMk9DQXFabXhsZUMxamIyNW1hWEp0TFcxaAphV3d1TVM0NUxqa3VlSEJwQ2pneE5qZzFOak5qWWpJM05tVmhOR1k1WVRKaU5qTXdZamxoTWpBM1pEa3dabUl4TVRnMU5tVWcKS21ac1pYZ3RZMjl1Wm1seWJTMXRZV2xzTG5od2FRbz0KLS0tLS0tLS0tLS0tLS0yNkE0NTMzNkY2QzYxOTZCRDhCQkEyQTIKQ29udGVudC1UeXBlOiBhcHBsaWNhdGlvbi9qc29uOwogbmFtZT0ibWFuaWZlc3QuanNvbiIKQ29udGVudC1UcmFuc2Zlci1FbmNvZGluZzogYmFzZTY0CkNvbnRlbnQtRGlzcG9zaXRpb246IGF0dGFjaG1lbnQ7CiBmaWxlbmFtZT0ibWFuaWZlc3QuanNvbiIKZXdvZ0lDSnRZVzVwWm1WemRGOTJaWEp6YVc5dUlqb2dNaXdLSUNBaVlYQndiR2xqWVhScGIyNXpJam9nZXdvZ0lDQWdJbWRsClkydHZJam9nZXdvZ0lDQWdJQ0FpYVdRaU9pQWlabXhsZUdsaWJHVXRZMjl1Wm1seWJTMXRZV2xzUUdOc1pXRnlMV052WkdVdQpZMjl0SWl3S0lDQWdJQ0FnSW5OMGNtbGpkRjl0YVc1ZmRtVnljMmx2YmlJNklDSTJPQzR3SWdvZ0lDQWdmUW9nSUgwc0NpQWcKSW01aGJXVWlPaUFpUm14bGVDQkRiMjVtYVhKdElFMWhhV3dpTEFvZ0lDSmtaWE5qY21sd2RHbHZiaUk2SUNKRGIyNW1hWEp0CklHMWhhV3hoWkdSeVpYTnpJR0Z1WkNCaGRIUmhZMmh0Wlc1MGN5QmlZWE5sWkNCdmJpQm1iR1Y0YVdKc1pTQnlkV3hsY3k0aQpMQW9nSUNKMlpYSnphVzl1SWpvZ0lqSXVNQ0lzQ2dvZ0lDSnNaV2RoWTNraU9pQjdDaUFnSUNBaWRIbHdaU0k2SUNKNGRXd2kKTEFvZ0lDQWdJbTl3ZEdsdmJuTWlPaUI3Q2lBZ0lDQWdJQ0p3WVdkbElqb2dJbU5vY205dFpUb3ZMMk52Ym1acGNtMHRiV0ZwCmJDOWpiMjUwWlc1MEwzTmxkSFJwYm1jdWVIVnNJaXdLSUNBZ0lDQWdJbTl3Wlc1ZmFXNWZkR0ZpSWpvZ2RISjFaUW9nSUNBZwpmUW9nSUgwS2ZRPT0KLS0tLS0tLS0tLS0tLS0yNkE0NTMzNkY2QzYxOTZCRDhCQkEyQTItLQ==", "headers": [["FCC", "imap://piro-test@mail.clear-code.com/Sent"], ["X-Identity-Key", "id1"], ["X-Account-Key", "account1"], ["From", "\"test@example.com\"
"], ["Subject", "test confirmation"], ["To", "test2@example.com, test2@example.com,\n mailmaster@example.com, mailmaster@example.org, webmaster@example.com,\n webmaster@example.org, webmaster@example.jp, mailmaster@example.jp"], ["Message-ID", "<05c18622-f2ad-cb77-2ce9-a0bbfc7d7ad0@clear-code.com>"], ["Date", "Thu, 15 Aug 2019 14:54:37 +0900"], ["X-Mozilla-Draft-Info", "internal/draft; vcard=0; receipt=0; DSN=0; uuencode=0;\n attachmentreminder=0; deliveryformat=4"], ["User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101\n Thunderbird/69.0"], ["MIME-Version", "1.0"], ["Content-Type", "multipart/mixed;\n boundary=\"------------26A45336F6C6196BD8BBA2A2\""], ["Content-Language", "en-US"]], "sender": ["test@example.com"], "to": "piro.outsider.reflex+1@gmail.com, piro.outsider.reflex+2@gmail.com,\n mailmaster@example.com, mailmaster@example.org, webmaster@example.com,\n webmaster@example.org, webmaster@example.jp, mailmaster@example.jp", "cc": "", "bcc": "", "subject": "test confirmation", "date": "Thu, 15 Aug 2019 14:54:37 +0900", "text_body": "testtest\ntesttest\ntesttest\ntesttest\ntesttest\ntesttest74c8f09dfa30eaccfb392b132314fc6b978f325a *flex-confirm-mail.1.10.0.xpi\nccee4b4aa47f513abce342ce1e2ec2fd9600e31b *flex-confirm-mail.1.11.0.xpi\n071e9e378ad0179bfadb1bdc650a49454d204a83 *flex-confirm-mail.1.12.0.xpi\n9d7aa153418ea8fbc8be7ba6f54ce8a1cb7ee468 *flex-confirm-mail.1.9.9.xpi\n8168563cb276ea4f9a2b630b9a207d90fb11856e *flex-confirm-mail.xpi\n", "html_body": "", "count": 3}
}]
Need more help?
Get answers from Community members and Google SecOps professionals.
