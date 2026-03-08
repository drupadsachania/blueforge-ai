# Collect AWS Network Firewall logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-network-firewall/  
**Scraped:** 2026-03-05T09:19:47.722651Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS Network Firewall logs
Supported in:
Google secops
SIEM
This document explains how to ingest AWS Network Firewall logs to Google Security Operations. AWS Network Firewall is a managed service that provides protection to your VPC against malicious traffic. By sending Network Firewall logs to Google SecOps, you can improve your monitoring, analysis, and threat detection.
Before you begin
Ensure you have the following prerequisites:
Google SecOps instance
Privileged access to AWS
How to configure Logging for AWS Network Firewall
Sign in to the
AWS Management Console
.
Open the
Amazon VPC console
.
In the navigation pane, select
Firewalls
.
Select the name of the firewall that you want to edit.
Select the
Firewall details
tab.
In the
Logging
section, click
Edit
.
Select the log types:
Flow
,
Alert
and
TLS
.
For each selected log type, choose
S3
for the destination type.
Click
Save
.
Set up feeds
There are two different entry points to set up feeds in the
Google SecOps platform:
SIEM Settings
>
Feeds
>
Add New Feed
Content Hub
>
Content Packs
>
Get Started
How to set up the AWS Network Firewall feed
Click the
Amazon Cloud Platform
pack.
Locate the
AWS Network Firewall
log type.
Specify the values in the following fields.
Source Type
: Amazon SQS V2
Queue Name
: The SQS queue name to read from
S3 URI
: The bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of your S3 bucket.
Source deletion options
: Select the deletion option according to your ingestion preferences.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
SQS Queue Access Key ID
: An account access key that is a 20-character alphanumeric string.
SQS Queue Secret Access Key
: An account access key that is a 40-character alphanumeric string.
Advanced options
Feed Name
: A prepopulated value that identifies the feed.
Asset Namespace
: Namespace associated with the feed.
Ingestion Labels
: Labels applied to all events from this feed.
Click
Create feed
.
For more information about configuring multiple feeds for different log types within this product family, see
Configure feeds by product
.
UDM Mapping Table
Log Field
UDM Mapping
Logic
availability_zone
target.resource.attribute.cloud.availability_zone
Directly mapped from the
availability_zone
field.
event.app_proto
network.application_protocol
Directly mapped from the
event.app_proto
field, converted to uppercase if not one of the specified values (ikev2, tftp, failed, snmp, tls, ftp). HTTP2 is replaced with HTTP.
event.dest_ip
target.ip
Directly mapped from the
event.dest_ip
field.
event.dest_port
target.port
Directly mapped from the
event.dest_port
field, converted to integer.
event.event_type
additional.fields[event_type_label].key
The key is hardcoded as "event_type".
event.event_type
additional.fields[event_type_label].value.string_value
Directly mapped from the
event.event_type
field.
event.flow_id
network.session_id
Directly mapped from the
event.flow_id
field, converted to string.
event.netflow.age
additional.fields[netflow_age_label].key
The key is hardcoded as "netflow_age".
event.netflow.age
additional.fields[netflow_age_label].value.string_value
Directly mapped from the
event.netflow.age
field, converted to string.
event.netflow.bytes
network.sent_bytes
Directly mapped from the
event.netflow.bytes
field, converted to unsigned integer.
event.netflow.end
additional.fields[netflow_end_label].key
The key is hardcoded as "netflow_end".
event.netflow.end
additional.fields[netflow_end_label].value.string_value
Directly mapped from the
event.netflow.end
field.
event.netflow.max_ttl
additional.fields[netflow_max_ttl_label].key
The key is hardcoded as "netflow_max_ttl".
event.netflow.max_ttl
additional.fields[netflow_max_ttl_label].value.string_value
Directly mapped from the
event.netflow.max_ttl
field, converted to string.
event.netflow.min_ttl
additional.fields[netflow_min_ttl_label].key
The key is hardcoded as "netflow_min_ttl".
event.netflow.min_ttl
additional.fields[netflow_min_ttl_label].value.string_value
Directly mapped from the
event.netflow.min_ttl
field, converted to string.
event.netflow.pkts
network.sent_packets
Directly mapped from the
event.netflow.pkts
field, converted to integer.
event.netflow.start
additional.fields[netflow_start_label].key
The key is hardcoded as "netflow_start".
event.netflow.start
additional.fields[netflow_start_label].value.string_value
Directly mapped from the
event.netflow.start
field.
event.proto
network.ip_protocol
Directly mapped from the
event.proto
field. If the value is "IPv6-ICMP", it's replaced with "ICMP".
event.src_ip
principal.ip
Directly mapped from the
event.src_ip
field.
event.src_port
principal.port
Directly mapped from the
event.src_port
field, converted to integer.
event.tcp.syn
additional.fields[syn_label].key
The key is hardcoded as "syn".
event.tcp.syn
additional.fields[syn_label].value.string_value
Directly mapped from the
event.tcp.syn
field, converted to string.
event.tcp.tcp_flags
additional.fields[tcp_flags_label].key
The key is hardcoded as "tcp_flags".
event.tcp.tcp_flags
additional.fields[tcp_flags_label].value.string_value
Directly mapped from the
event.tcp.tcp_flags
field.
event_timestamp
metadata.event_timestamp.seconds
Directly mapped from the
event_timestamp
field, parsed as a timestamp.
event_timestamp
timestamp.seconds
Directly mapped from the
event_timestamp
field, parsed as a timestamp.
firewall_name
metadata.product_event_type
Directly mapped from the
firewall_name
field. Set to "NETWORK_CONNECTION" if both
event.src_ip
and
event.dest_ip
are present, otherwise set to "GENERIC_EVENT". Hardcoded to "AWS Network Firewall". Hardcoded to "AWS".
Need more help?
Get answers from Community members and Google SecOps professionals.
