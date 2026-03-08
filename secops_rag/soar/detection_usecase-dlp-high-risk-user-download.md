# Use Sensitive Data Protection data in context-aware analytics

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/usecase-dlp-high-risk-user-download/  
**Scraped:** 2026-03-05T10:04:12.737026Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use Sensitive Data Protection data in context-aware analytics
Supported in:
Google secops
SIEM
This document demonstrates how to use entity context data from
Sensitive Data Protection
and additional log sources
to add contextual understanding about the impact and
scope of a potential threat when performing an investigation.
The use case described in this document detects the execution of a malicious
file by a user (MITRE ATT&CK Technique
T1204.002
)
and whether that user also has access to sensitive data elsewhere on the
network.
This example requires that the following data has been ingested and normalized
in Google Security Operations:
User activity data using network and EDR logs.
Resource relationships from data sources like Google Cloud IAM Analysis.
Sensitive Data Protection logs that contain labels about the type and sensitivity of the stored data.
Google SecOps must be able to parse the raw data into Unified Data Model (UDM)
entity and event records.
For information about ingesting Sensitive Data Protection data into Google SecOps, see
Exporting Sensitive Data Protection data to Google SecOps
.
Google Cloud IAM Analysis data
The Google Cloud IAM Analysis log data in this example identifies users in the
organization and captures relationships each user has to other systems on the
network. The following is a snippet of an IAM Analysis log stored as a UDM
entity record. It stores information about the user,
mikeross
, who
administers a BigQuery table called
analytics:claim.patients
.
metadata.vendor_name: "Google Cloud Platform"
metadata.product_name: "GCP IAM Analysis"
metadata.entity_type: "USER"
entity.user.userid: "mikeross"
relations[2].entity.resource.name: "analytics:claim.patients"
relations[2].entity.resource.resource_type: "TABLE"
relations[2].entity_type: "RESOURCE"
relations[2].relationship: "ADMINISTERS"
Sensitive Data Protection data
The Sensitive Data Protection log data in this example stores information about a BigQuery
table. The following is a snippet of a Sensitive Data Protection log stored as a UDM entity
record. It represents the BigQuery table called
analytics:claim.patients
with
the
Predicted InfoType
label
US_SOCIAL_SECURITY_NUMBER
, indicating that the
table stores United States Social Security numbers.
metadata.vendor_name: "Google Cloud Platform"
metadata.product_name: "GCP DLP CONTEXT"
metadata.entity_type: "RESOURCE"
metadata.description: "RISK_HIGH"
entity.resource.resource_type: "TABLE"
entity.resource.resource_subtype: "BigQuery Table"
entity.resource.attribute.cloud.environment"GOOGLE_CLOUD_PLATFORM"
entity.resource.attribute.labels[0].key: "Sensitivity Score"
entity.resource.attribute.labels[0].value: "SENSITIVITY_HIGH"
entity.resource.attribute.labels[1].key: "Predicted InfoType"
entity.resource.attribute.labels[1].value: "US_SOCIAL_SECURITY_NUMBER"
entity.resource.product_object_id: "analytics:claim.patients"
Web proxy events
The web proxy event in this example captures network activity. The following
snippet is of a Zscaler web proxy log stored as a UDM event record. It captures
a network download event of an executable file by user with the
userid
value
mikeross
where the
received_bytes
value is 514605.
metadata.log_type = "ZSCALER_WEBPROXY"
metadata.product_name = "NSS"
metadata.vendor_name = "Zscaler"
metadata.event_type = "NETWORK_HTTP"
network.http.response_code = 200
network.received_bytes = 514605
principal.user.userid = "mikeross"
target.url = "http://manygoodnews.com/dow/Client%20Update.exe"
EDR events
The EDR event in this example captures activity on an endpoint device. The
following snippet is of a CrowdStrike Falcon EDR log stored as a UDM event
record. It captures a network event involving the Microsoft Excel application
and a user with the
userid
value
mikeross
.
metadata.log_type = "CS_EDR"
metadata.product_name = "Falcon"
metadata.vendor_name = "Crowdstrike"
metadata.event_type = "NETWORK_HTTP"
target.process.file.full_path = "\\Device\\HarddiskVolume1\\Program Files\\C:\\Program Files\\Microsoft Office\\Office16\\EXCEL.exe"
target.url = "http://manygoodnews.com/dow/Client%20Update.exe"
target.user.userid = "mikeross"
Notice that there is common information across these records, both the user identifier
mikeross
and table name,
analytics:claim.patients
. The next section in this document
demonstrates how these values are used in the rule to join the records.
Detection engine rule in this example
This example rule detects the execution of a malicious file by a user (MITRE
ATT&CK Technique
T1204.002
.
The rule assigns a higher risk score to a detection when the user also has
access to sensitive data elsewhere on the network. The rule correlates the
following information:
User activity, such as the download or launch of an executable.
The relationship between resources, for example the user's relationship to a
BigQuery table.
Presence of sensitive information in the resource a user has access to, for
example the type of data stored in the BigQuery table.
Here is a description of each section in the example rule.
The
events
section specifies the pattern of data that the rule looks
for and includes the following:
Group 1 and Group 2 identify network and EDR events that
capture the download of a large amount of data or an executable that is also related to
activity in the Excel application.
Group 3 identifies records where the user identified in the
network and EDR events also has permission to a BigQuery table.
Group 4 identifies Sensitive Data Protection records for the BigQuery table
that the user has access to.
Each group of expressions uses either the
$table_name
variable or the
$user
variable
to join records related to the same user and database table.
In the
outcome
section, the rule creates a
$risk_score
variable and sets a value
based on the sensitivity of the data in the table. In this case, it checks whether
the data is labeled with the
US_SOCIAL_SECURITY_NUMBER
Sensitive Data Protection infoType
.
The
outcome
section also sets additional variables such as
$principalHostname
and
$entity_resource_name
. These variables are
returned and stored with the detection, so that when you view it in Google SecOps you can
also display the variable values as columns.
The
condition
section indicates that the pattern looks for all UDM records specified
in the
events
section.
rule high_risk_user_download_executable_from_macro {
 meta:
   author = "Google Cloud Security Demos"
   description = "Executable downloaded by Microsoft Excel from High Risk User"
   severity = "High"
   technique = "T1204.002"

 events:
   //Group 1. identify a proxy event with suspected executable download
   $proxy_event.principal.user.userid = $user
   $proxy_event.target.url =  /.*\.exe$/ or
   $proxy_event.network.received_bytes > 102400

   //Group 2. correlate with an EDR event indicating Excel activity
   $edr_event.target.user.userid  = $user
   $edr_event.target.process.file.full_path = /excel/ nocase
   $edr_event.metadata.event_type = "NETWORK_HTTP"

   //Group 3. Use the entity to find the permissions
   $user_entity.graph.entity.user.userid = $user
   $user_entity.graph.relations.entity.resource.name = $table_name

   //Group 4. the entity is from Cloud DLP data
   $table_context.graph.entity.resource.product_object_id = $table_name
   $table_context.graph.metadata.product_name = "GCP DLP CONTEXT"

 match:
    $user over 5m

 outcome:
   //calculate risk score
   $risk_score = max(
       if( $table_context.graph.entity.resource.attribute.labels.value = "US_SOCIAL_SECURITY_NUMBER", 80)
       )
   $technique = array_distinct("T1204.002")
   $principalHostname = array_distinct($proxy_event.principal.hostname)
   $principalIp = array_distinct($proxy_event.principal.ip)
   $principalMac = array_distinct($proxy_event.principal.mac)
   $targetHostname = array_distinct($proxy_event.target.hostname)
   $target_url = array_distinct($proxy_event.target.url)
   $targetIp = array_distinct($proxy_event.target.ip)
   $principalUserUserid =  array_distinct($proxy_event.principal.user.userid)
   $entity_resource_name = array_distinct($table_context.graph.entity.resource.name)

condition:
   $proxy_event and $edr_event and $user_entity and $table_context
}
About the detection
If you test the rule against existing data and it identifies the pattern of
activity specified in the definition, it generates a detection. The
Detection
panel displays the detection generated after testing the rule. The
Detection
panel also displays the event and entity records that caused the
rule to create a detection. In this example, the following records are
displayed:
Google Cloud IAM Analysis UDM entity
Sensitive Data Protection UDM entity
Zscaler web proxy UDM event
CrowdStrike Falcon EDR UDM event
In the
Detection
panel, select any event or entity record to see details.
The detection also stores the variables defined in the
outcome
section of the rule. To display the variables in the
Detection
panel, select
Columns
, and then select one or more variable names from the
Columns
menu. The selected columns appear in the
Detection
panel.
What's next
To write custom rules, see
Overview of the YARA-L 2.0 language
.
To create custom context-aware analytics, see
Create context-aware analytics
To use predefined threat analytics, see
Using Google SecOps curated detections
.
Need more help?
Get answers from Community members and Google SecOps professionals.
