# Enrichment

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/enrichment/  
**Scraped:** 2026-03-05T10:10:06.039841Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Enrichment
Supported in:
Google secops
SOAR
Overview
Enrichment is a set of actions created to power up playbook capabilities.
Configuration
In the configuration screen, add the Chronicle SOAR API to enrich entities from
  Explorer. To retrieve an API key, go to Settings -> Advanced -> API
  Keys.
Parameter
Type
Default Value
Is Mandatory
Description
API Key
String
N/A
No
Specify the Chronicle SOAR API key, which is required to enrich entities from
        Explorer.
Actions
Enrich Entity from Event Field
Description
Extracts fields from an event and adds them to the entity fields.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Fields to enrich
String
N/A
Yes
Specify the name of the field(s) in the event that will be used to
        enrich the entity. Supports comma separated list.
Example
In this scenario, fields payload_id and event_description are extracted from a
  case event and added to entity fields for all file name entities.
Action Configurations
Parameter
Value
Entities
All file names entities
Fields to enrich
payload_id, event_description
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of entitled successfully enriched
1
Enrich Entity from Explorer Attributes
Description
Enriches entities with historic enrichment data using the entity explorer.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Field Name
String
N/A
No
Specify the fields from the entity explorer that will be used to enrich
        the target entity. Supports comma delimited string.
Use field Name as Allowlist
Checkbox
Checked
No
If checked, entities will be enriched with fields from the “Field
        Name” parameter. If unchecked, the list will be used as a
        blocklist and other fields added.
Example
In this scenario, we’re enriching all entities with data from entity
  explorer. All available fields are listed in “Entity Details”
  within Entity Explorer. Return JSON result of the key/value pairs in entity
  details.
Action Configurations
Parameter
Value
Entities
All entities
Field Name
Blank
User Field Name as Allowlist
Unchecked
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
JSON Result
Result Shown below
JSON Result
{
"193.0.0.44": {}, "ATTACHMENT.TXT": {"Source": "Added by
", "size": "64", "extension": "txt", "hash_md5": "6529d73ba8183760ad174644e75684fe", "hash_sha1": "dd88508cda7bcfc71ffdbc0e26afe97d3fb9a0b6", "hash_sha256": "1f209f1560df8cb6e983dff99d7a7d2db8dc3e439226abd38ef34facdffd82ec", "hash_sha512": "310d2df6f770dafdf4f84d9851e3fad011d4eb0c5a8af9a5f6d237fb733bca41d41ad6b00efdc2b5c218207
f1a1ac99339923d3c389368f0c1d2ba58e8e1893a", "mime_type": "ASCII text, with no line terminators", "mime_type_short": "text/plain", "ole_data_1_id": "ftype", "ole_data_1_value": "Unknown file type", "ole_data_1_name": "File format", "ole_data_1_description": "", "ole_data_1_risk": "info", "ole_data_1_hide_if_false": "true", "ole_data_2_id": "container", "ole_data_2_value": "Unknown Container", "ole_data_2_name": "Container format", "ole_data_2_description": "Container type", "ole_data_2_risk": "info", "ole_data_2_hide_if_false": "true", "ole_data_3_id": "encrypted", "ole_data_3_value": "", "ole_data_3_name": "Encrypted", "ole_data_3_description": "The file is not encrypted", "ole_data_3_risk": "none", "ole_data_3_hide_if_false": "", "ole_data_4_id": "vba", "ole_data_4_value": "Yes", "ole_data_4_name": "VBA Macros", "ole_data_4_description": "This file contains VBA macros. No suspicious keyword was found. Use olevba and mraptor for more info.", "ole_data_4_risk": "Medium", "ole_data_4_hide_if_false": "", "ole_data_5_id": "xlm", "ole_data_5_value": "No", "ole_data_5_name": "XLM Macros", "ole_data_5_description": "This file does not contain Excel 4/XLM macros.", "ole_data_5_risk": "none", "ole_data_5_hide_if_false": "", "ole_data_6_id": "ext_rels", "ole_data_6_value": "", "ole_data_6_name": "External Relationships", "ole_data_6_description": "External relationships such as remote templates, remote OLE objects, etc", "ole_data_6_risk": "none", "ole_data_6_hide_if_false": "", "ole_data_7_id": "ObjectPool", "ole_data_7_value": "", "ole_data_7_name": "ObjectPool", "ole_data_7_description": "Contains an ObjectPool stream, very likely to contain embedded OLE objects or files. Use oleobj to check it.", "ole_data_7_risk": "none", "ole_data_7_hide_if_false": "true", "ole_data_8_id": "flash", "ole_data_8_value": "", "ole_data_8_name": "Flash objects", "ole_data_8_description": "Number of embedded Flash objects (SWF files) detected in OLE streams. Not 100% accurate, there may be false positives.", "ole_data_8_risk": "none", "ole_data_8_hide_if_false": "true", "content_header_content-type_1": "text/plain; name=\"attachment.txt\"", "content_header_content-transfer-encoding_1": "base64", "content_header_content-disposition_1": "attachment; filename=\"attachment.txt\"", "level": "", "attachment_id": "18"}
}
Enrich Entity from JSON
Description
Adds the source and destination links to IPs and Hostnames in an alert.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Enrichment JSON
JSON
N/A
Yes
Specify the JSON to enrich an entity.
Identifier KeyPath
String
N/A
Yes
Specify the keypath to the entity identifier in the JSON
Separator
String
.
Yes
Specify the key path separator/delimiter.
PrefixForErichment
String
N/A
No
Specify a prefix to use for the enrichment.
Enrichment JSON Path
String
N/A
No
Specify the JSON
Example
In this scenario, we’re using an entity identifier of a hash value with
  field “sha1” to enrich it with data in the Enrichment JSON field.
  Note the entity needs to exist in the alert before running this action.
Action Configurations
Parameter
Value
Entities
All entities
Enrichment JSON
[ { "EntityResult": {"permalink":
"https://www.virustotal.com/file/275a021bbfb6489e54d4718
99f7db9d1663fc695ec2fe2a2c4538aabf651fd0f/analysis/15
49381312", "sha1": 
"3395856ce81f267382dee72602f798b642f14140",
"resource":"275A021BBFB6489E54D471899F7DB9D1663
FC695EC2FE2A24538AABF651FDOF","response_code":1,
"scan_date":"2019-02-05 15:41:52",
"scan_id":"275a021bbfb6489e54d471899f7db9d1663fc695
ec2fe2a2c453Saab651fd0f-1549381312","verbose_msg" : 
"Scan finished,information embedded","total": 
60,"positives": 54, 
"sha256":"75a021bbfb6489e54d471899f7db9d1663fc695e
c2fe2a2c4538aabf651fd0f",
"Mas":"44d88612fea8a8f36de82e1278abb02f",
"Bkav": {"detected": true,"result": "DOS. Eirac 
A.Trojan","MicroWorld-eScan": {"version": 
"14.0.297.0","update": "20190205""scans": 
{"version":"1.1.1.1","update": "20190201"
"detected": true,"result*: "EICAR-Test-File","Entity": 
"275A021BBFB6489E54D471899F7DB9D1663FC695EC2
FE2A24538AABF651FD0F" }]
Identifier KeyPath
EntityResult.sha1
Separator
.
PrefixForEnrichment
Blank
Enrichment JSON Path
Blank
Action Results
Script Result
Script Result Name
Value options
Example
Script Result
# of entities enriched
1
Enrich Entity from List with Field
Description
Enriches list of supplied entities with a field and a value. This action is
  often used with “Entity Selection” action to list the entities.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
List of Entities
String
N/A
Yes
Specify a list of entities of the same type.
Entity Type
String
N/A
Yes
Specify the type of entity.
Entity Delimiter
String
,
Yes
Specify delimiter of list entities.
Enrichment Field
String
N/A
Yes
Specify the field name that will be added to the entity.
Enrichment Value
String
N/A
Yes
Specify the value of the field that will be enriched to the entity.
Example
In this scenario, we’re selecting IP Address entities using the
  EntitySelection action and passing the results to the “List of
  Entities” field for enrichment.
Action Configurations (EntitySelection)
Parameter
Condition
Value
Entity.Type
=
ADDRESS
Action Configurations (Enrich Entities from List with Field)
Parameter
Value
Entities
All entities
List of Entities
[Entity Selection_1.SelectedEntities]
Entity Type
ADDRESS
Entity Delimiter
,
Enrichment Field
is_risky
Enrichment Value
yes
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of entitled successfully enriched
3
Enrich Entity With Field
Description
Adds enrichment fields to the entity based on a list of key values.
Parameters
Parameter
Type
Default Value
Is Mandatory
Description
Example
Fields to enrich
JSON
N/A
Yes
Specify a list of key value pairs that will be used to enrich the
        entity. It needs to be in JSON format.
[ { "entity_field_name": "Title",
        "entity_field_value": "SalseManager" }, {
        "entity_field_name": "City",
        "entity_field_value": "NewYork" } ]
Example
In this example we’re enriching user entities with two fields: Title and
  City.
Action Configurations
Parameter
Value
Entities
All file names entities
Fields to enrich
[ { "entity_field _name": "Title", "entity_field_value":
"Manager"}, { "entity_field _name": "City", "entity_field_value": "Newyork"}]
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of entities successfully enriched
13
Enrich FileName Entity With Path
Description
Parses path, file name and extension from an entity and enriches it with
  file_path, file_name, and file_extensions.
Parameters
Specify the file entity scope you want to parse the fields from.
Example
In this scenario, we’re looping through all file name entities and
  parsing any paths, file names and extensions from the entity identifier.
Action Configurations
Parameter
Value
Entities
All file name entities
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
List of entities enriched.
WORD/THEME/THEME1.XML,WORD/DOCUMENT.XML
Enrich Source and Destinations
Description
Adds the source and destination links to IPs and Hostnames in an alert.
Parameters
Specify the entity scope you want to parse the fields from.
Example
In this scenario, we’re looping through all IP and hostname entities and
  enriching them with source and destination links. Even if the entity scope is 
  set to "All entities", it will automatically select IP and hostname entities.
Action Configurations
Parameter
Value
Entities
All entities
Action Results
Script Result
Script Result Name
Value options
Example
N/A
N/A
N/A
Mark Entity as Suspicious
Description
Marks entities in scope as suspicious.
Parameters
Specify the entity scope you want to mark as suspicious.
Example
In this scenario, we’re marking all external IP entities suspicious.
  Entity field “is_suspicious” in entity explorer is updated to
  “true”.
Action Configurations
Parameter
Value
Entities
External IP addresses
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
Number of entitled marked as suspicious
3
Whois
Description
Queries WHOIS servers for domain registration information. Supports IP
  Addresses, URLs, Email, Domains. Supports creation of Domain entities linked
  to target entity and a domain age threshold to set the entity to suspicious.
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
Specify whether you want to create and link domain entities to URL
        Email/User Names.
Domain Age Threshold
Integer
Checked
No
If the domain's age is less than the supplied number of days, it
        will be marked as suspicious.
Example
In this scenario, any external hostname entities attached to a case with a
  domain age of less than 365 days will be marked as suspicious.
Action Configurations
Parameter
Value
Entities
External hostnames
Create Entities
Checked
Domain Age Threshold
365
Action Results
Script Result
Script Result Name
Value options
Example
ScriptResult
True/False
true
JSON Result
{
"Entity": "badsite.com", 
"EntityResult": 
{"id": ["32621649_DOMAIN_COM-VRSN"], 
"status": ["clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited", "clientRenewProhibited https://icann.org/epp#clientRenewProhibited", "clientTransferProhibited https://icann.org/epp#clientTransferProhibited", "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited"], "creation_date": ["2000-08-09T11:17:46"], 
"expiration_date": ["2023-08-09T11:17:46"], 
"updated_date": ["2022-09-18T23:31:54"], 
"registrar": ["GoDaddy.com, LLC"], 
"whois_server": ["whois.godaddy.com"], 
"nameservers": ["NS49.DOMAINCONTROL.COM", "NS50.DOMAINCONTROL.COM"], 
"emails": ["abuse@godaddy.com"], 
"contacts": {"registrant": null, "tech": null, "admin": null, "billing": null}, "age_in_days": 8092}
}
Need more help?
Get answers from Community members and Google SecOps professionals.
