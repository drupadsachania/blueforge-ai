# Key UDM fields for parsers

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/important-udm-fields/  
**Scraped:** 2026-03-05T10:02:59.573033Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Key UDM fields for parsers
Supported in:
Google secops
SIEM
Some Google Security Operations features depend on data populated in
certain UDM fields. If this data is missing or incorrect, the feature may not
function as intended.
When creating a parser, make sure the data mapping instructions populate as many
important Unified Data Model
(
UDM
) fields as possible.
Parser data mapping instructions control how original raw log data is mapped to
fields in the UDM data structure. For a list of all UDM fields, see the
Unified
Data Model field list
.
Feature areas
Key UDM fields fall into the following feature areas (and use cases). The
Feature area or use cases
column in the
Key UDM field list
includes the following feature areas:
Curated detections
: Prebuilt rule sets, managed by
Google SecOps, that analyze your data to detect potential threats.
Indexing
: Lets security analysts search for
information about resources, such as assets, domains, IP addresses, users, and
files. It also enriches UDM records with details about prevalence,
first time seen, last time seen, and more.
Artifact aliasing
: Enriches UDM records with additional data,
such as geolocation data using an external IP address.
Asset aliasing
: Identifies relationships across individual
UDM records related to the same physical asset, such as a server, laptop, or
mobile device.
Process aliasing
: Identifies relationships across individual
UDM records that describe one or more related processes, files, and users who
executed the process.
User aliasing
: Identifies relationships across individual UDM
records related to the same user.
Entity graph
: Identifies relationships between entities and
resources in your environment.
IoC
: Matches your data against data ingested from IoC feeds.
Threat hunting
: This is a use case, not a feature. Fields with this
value are recommended to facilitate Threat hunting activities.
Key UDM fields
Use this keyword lookup to find important UDM fields.
Fully qualified field name
Feature area or use case
<event>.security_result.threat_id_namespace
Indexing
<event>.security_result.threat_id
Indexing
<event>.security_result.category
Indexing
<event>.security_result.summary
Indexing
<event>.security_result.description
Indexing
<event>.security_result.action
Curated detections
<event>.security_result.detection_fields.key
Curated detections
<event>.security_result.detection_fields.value
Curated detections
<event>.security_result.threat_name
Threat hunting
<event>.metadata.event_timestamp
Indexing
<event>.metadata.event_type
Curated detections, Indexing
<event>.metadata.product_name
Curated detections, Indexing
<event>.metadata.vendor_name
Curated detections, Indexing
<event>.metadata.description
Curated detections
<event>.metadata.ingestion_labels.key
Curated detections
<event>.metadata.ingestion_labels.value
Curated detections
<event>.metadata.product_event_type
Curated detections
<event>.metadata.product_deployment_id
Threat hunting
<event>.metadata.product_log_id
Threat hunting
<event>.principal.ip
Curated detections, Indexing, Artifact aliasing, Asset aliasing
<event>.principal.mac
Indexing, Asset aliasing
<event>.principal.hostname
Curated detections, Indexing, Asset aliasing
<event>.principal.asset_id
Indexing, Asset aliasing
<event>.principal.asset.ip
Indexing
<event>.principal.asset.mac
Indexing
<event>.principal.asset.hostname
Indexing
<event>.principal.asset.asset_id
Indexing
<event>.principal.user.email_address
Curated detections, Indexing, User aliasing
<event>.principal.user.userid
Indexing, User aliasing
<event>.principal.user.windows_sid
Indexing, User aliasing
<event>.principal.user.product_object_id
Indexing, User aliasing
<event>.principal.user.attribute.permissions.name
Curated detections
<event>.principal.user.attribute.permissions.type
Curated detections
<event>.principal.user.attribute.roles.name
Curated detections
<event>.principal.user.attribute.roles.description
Curated detections
<event>.principal.file.sha1
Artifact aliasing
<event>.principal.file.md5
Artifact aliasing
<event>.principal.file.sha256
Artifact aliasing
<event>.principal.file.full_path
Curated detections
<event>.principal.process.parent_process
Process aliasing
<event>.principal.process.product_specific_process_id
Process aliasing
<event>.principal.process.pid
Curated detections
<event>.principal.process.command_line
Curated detections
<event>.principal.process.file.full_path
Curated detections
<event>.principal.process.parent_process.command_line
Curated detections
<event>.principal.process.parent_process.file.full_path
Curated detections
<event>.principal.cloud.environment
Curated detections
<event>.principal.resource.name
Curated detections
<event>.principal.resource.attribute.cloud.project.name
Curated detections
<event>.principal.resource.attribute.cloud.project.resource_subtype
Curated detections
<event>.principal.registry.registry_key
Curated detections
<event>.principal.registry.registry_value_name
Curated detections
<event>.principal.url
Curated detections
<event>.source.ip
Indexing, Artifact aliasing, Asset aliasing
<event>.source.mac
Indexing, Asset aliasing
<event>.source.hostname
Indexing, Asset aliasing
<event>.source.asset_id
Indexing, Asset aliasing
<event>.source.asset.ip
Indexing
<event>.source.asset.mac
Indexing
<event>.source.asset.hostname
Indexing
<event>.source.asset.asset_id
Indexing
<event>.source.user.email_address
Indexing, User aliasing
<event>.source.user.userid
Indexing, User aliasing
<event>.source.user.windows_sid
Indexing, User aliasing
<event>.source.user.product_object_id
Indexing, User aliasing
<event>.source.file.sha1
Artifact aliasing
<event>.source.file.md5
Artifact aliasing
<event>.source.file.sha256
Artifact aliasing
<event>.source.process.parent_process
Process aliasing
<event>.source.process.product_specific_process_id
Process aliasing
<event>.target.ip
Curated detections, Indexing, Artifact aliasing, Asset aliasing
<event>.target.port
Curated detections
<event>.target.mac
Indexing, Asset aliasing
<event>.target.hostname
Curated detections, Indexing, Asset aliasing
<event>.target.asset_id
Indexing, Asset aliasing
<event>.target.asset.ip
Indexing
<event>.target.asset.mac
Indexing
<event>.target.asset.hostname
Indexing
<event>.target.asset.asset_id
Indexing
<event>.target.user.email_address
Curated detections, Indexing, User aliasing
<event>.target.user.userid
Indexing, User aliasing
<event>.target.user.windows_sid
Indexing, User aliasing
<event>.target.user.product_object_id
Indexing, User aliasing
<event>.target.file.sha1
Artifact aliasing
<event>.target.file.md5
Artifact aliasing
<event>.target.file.sha256
Artifact aliasing
<event>.target.file.full_path
Curated detections
<event>.target.process.parent_process
Process aliasing
<event>.target.process.product_specific_process_id
Process aliasing
<event>.target.process.pid
Curated detections
<event>.target.process.command_line
Curated detections
<event>.target.process.file.full_path
Curated detections
<event>.target.process.parent_process.command_line
Curated detections
<event>.target.process.parent_process.file.full_path
Curated detections
<event>.target.application
Curated detections
<event>.target.cloud.environment
Curated detections
<event>.target.cloud.project.name
Curated detections
<event>.target.resource.name
Curated detections
<event>.target.resource.resource_type
Curated detections
<event>.target.registry.registry_key
Curated detections
<event>.target.registry.registry_value_name
Curated detections
<event>.network.application_protocol
Curated detections
<event>.network.ip_protocol
Curated detections
<event>.network.dns_domain
Threat hunting
<event>.network.http.method
Curated detections
<event>.network.http.user_agent
Curated detections
<event>.network.http.referral_url
Threat hunting
<event>.network.http.response_code
Threat hunting
<event>.network.dns.questions.name
Curated detections
<event>.network.dns.questions.type
Curated detections
<event>.network.dns.answers.name
Curated detections
<event>.network.dns.answers.data
Threat hunting
<event>.network.dns.answers.type
Curated detections
<event>.network.email.bcc
Threat hunting
<event>.network.email.email.cc
Threat hunting
<event>.network.email.from
Threat hunting
<event>.network.email.reply_to
Threat hunting
<event>.network.email.subject
Threat hunting
<event>.network.email.to
Threat hunting
<event>.network.ftp.command
Threat hunting
<entity>.entity.user.email_address
Entity graph, IoC
<entity>.entity.user.userid
Entity graph
<entity>.entity.user.windows_sid
Entity graph
<entity>.entity.user.product_object_id
Entity graph, IoC
<entity>.entity.user.employee_id
Entity graph
<entity>.entity.group.email_address
Entity graph
<entity>.entity.group.windows_sid
Entity graph
<entity>.entity.group.product_object_id
Entity graph, IoC
<entity>.entity.asset.ip
Entity graph
<entity>.entity.asset.mac
Entity graph
<entity>.entity.asset.hostname
Entity graph
<entity>.entity.asset.asset_id
Entity graph
<entity>.entity.asset.product_object_id
Entity graph, IoC
<entity>.entity.resource.product_object_id
Entity graph, IoC
<entity>.entity.resource.name
IoC
<entity>.entity.file
Entity graph
<entity>.entity.hostname
IoC
<entity>.entity.url
Threat hunting
<entity>.metadata.threat
IoC
<entity>.metadata.collected_timestamp
Entity graph, IoC
