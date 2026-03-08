# Collect AWS EC2 Hosts logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-hosts/  
**Scraped:** 2026-03-05T09:16:50.590703Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS EC2 Hosts logs
Supported in:
Google secops
SIEM
This document explains how to integrate AWS EC2 Hosts logs into Google Security Operations for monitoring and analysis. The integration involves parsing and mapping EC2 host logs to the Unified Data Model (UDM), performing data transformation, and creating relationships between EC2 hosts and instances. The logs provide valuable information about the instances, host properties, instance types, and performance metrics that can be used for security monitoring, audit, and compliance.
Before you begin
Ensure that you have a Google SecOps instance.
Ensure that you have privileged access to AWS.
Configure AWS IAM and S3
Create an
Amazon S3 bucket
following this user guide:
Creating a bucket
.
Save the bucket
Name
and
Region
for later use.
Create a user following this user guide:
Creating an IAM user
.
Select the created
User
.
Select the
Security credentials
tab.
Click
Create Access Key
in the
Access Keys
section.
Select
Third-party service
as the
Use case
.
Click
Next
.
Optional: add a description tag.
Click
Create access key
.
Click
Download CSV file
to save the
Access Key
and
Secret Access Key
for later use.
Click
Done
.
Select the
Permissions
tab.
Click
Add permissions
in the
Permissions policies
section.
Select
Add permissions
.
Select
Attach policies directly
Search for and select the
AmazonS3FullAccess
policy.
Click
Next
.
Click
Add permissions
.
Configure CloudTrail for AWS KMS
Sign in to the
AWS Management Console
.
In the search bar, type and select
CloudTrail
from the services list.
Click
Create trail
.
Provide a
Trail name
; for example,
EC2-Activity-Trail
.
Select the
Enable for all accounts in my organization
checkbox.
Type the S3 bucket URI created earlier (the format should be:
s3://your-log-bucket-name/
), or create a new S3 bucket.
If SSE-KMS is enabled, provide a name for
AWS KMS alias
, or choose an
existing AWS KMS Key
.
You can leave the other settings as default.
Click
Next
.
Select
Management events
and
Data events
under
Event Types
to capture EC2 host activity.
Click
Next
.
Review the settings in
Review and create
.
Click
Create trail
.
Optional: if you created a new bucket, continue with the following process:
Go to
S3
.
Identify and select the newly created log bucket.
Select the folder
AWSLogs
.
Click
Copy S3 URI
and save it.
Configure a feed in Google SecOps to ingest AWS EC2 Hosts
Go to
SIEM Settings
>
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed; for example,
AWS EC2 Hosts Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select
AWS EC2 Hosts
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
S3 URI
: the bucket URI.
s3://your-log-bucket-name/
Replace
your-log-bucket-name
with the actual name of the bucket.
Source deletion options
: select the deletion option according to your preference.
Maximum File Age
: Include files modified in the last number of days. Default is 180 days.
Access Key ID
: the User access key with access to the s3 bucket.
Secret Access Key
: the User secret key with access to the s3 bucket.
Asset namespace
: the
asset namespace
.
Ingestion labels
: the label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
Supported AWS EC2 Hosts log formats
The AWS EC2 Hosts parser supports logs in JSON format.
Supported AWS EC2 Hosts Sample Logs
JSON
{
    "AllocationTime": "2018-01-23T12:33:31.692Z",
    "AllowsMultipleInstanceTypes": "",
    "AssetID": "",
    "AutoPlacement": "off",
    "AvailabilityZone": "us-east-1a",
    "AvailabilityZoneID": "",
    "AvailableCapacity": {
      "VCPUs": 96,
      "Instance": {
        "Available": 48,
        "Total": 48,
        "Type": "m5.large"
      }
    },
    "ClientToken": "",
    "ID": "h-05abcdd12ee9ca123",
    "Maintenance": "",
    "Properties": {
      "Cores": 48,
      "InstanceFamily": "",
      "InstanceType": "m5.large",
      "Sockets": 2,
      "TotalVCPUs": 96
    },
    "Recovery": "off",
    "ReservationID": "",
    "Instances": null,
    "MemberOfServiceLinkedResourceGroup": false,
    "OutpostARN": "",
    "OwnerID": "",
    "ReleaseTime": "",
    "State": "available",
    "TagSet": null
  }
UDM Mapping Table
Log Field
UDM Mapping
Logic
AllocationTime
entity.metadata.creation_timestamp
The
AllocationTime
field is parsed as a timestamp and mapped to the
creation_timestamp
field.  The parser attempts various formats (yyyy-MM-dd HH:mm:ss, RFC 3339, UNIX, ISO8601).
AllowsMultipleInstanceTypes
entity.entity.asset.attribute.labels.value
The value of
AllowsMultipleInstanceTypes
from the raw log is used as the value of a label. The key for this label is set to
allows_multiple_instance_types
.
AutoPlacement
entity.entity.asset.attribute.labels.value
The value of
AutoPlacement
from the raw log is used as the value of a label. The key for this label is set to
auto_placement
.
AvailabilityZone
entity.entity.asset.attribute.cloud.availability_zone
The
AvailabilityZone
field is directly mapped to the
availability_zone
field.
AvailabilityZoneID
entity.entity.asset.attribute.labels.value
The value of
AvailabilityZoneID
from the raw log is used as the value of a label. The key for this label is set to
availability_zone_id
.
AvailableCapacity.AvailableInstanceCapacity.AvailableCapacity
entity.entity.asset.attribute.labels.value
The value of
AvailableCapacity.AvailableInstanceCapacity.AvailableCapacity
(or
AvailableCapacity.Instance.Available
after renaming) is converted to a string and used as the value of a label. The key is set to
available_instance_capacity_available_capacity
.
AvailableCapacity.AvailableInstanceCapacity.InstanceType
entity.entity.asset.attribute.labels.value
The value of
AvailableCapacity.AvailableInstanceCapacity.InstanceType
(or
AvailableCapacity.Instance.Type
after renaming) is used as the value of a label. The key is set to
available_instance_capacity_instance_type
.
AvailableCapacity.AvailableInstanceCapacity.TotalCapacity
entity.entity.asset.attribute.labels.value
The value of
AvailableCapacity.AvailableInstanceCapacity.TotalCapacity
(or
AvailableCapacity.Instance.Total
after renaming) is converted to a string and used as the value of a label. The key is set to
total_capacity
.
AvailableCapacity.AvailableVCpus
entity.entity.asset.attribute.labels.value
The value of
AvailableCapacity.AvailableVCpus
(or
AvailableCapacity.VCPUs
after renaming) is converted to a string and used as the value of a label. The key is set to
available_v_cpus
.
ClientToken
entity.entity.asset.attribute.labels.value
The value of
ClientToken
from the raw log is used as the value of a label. The key for this label is set to
client_token
.
HostID
entity.metadata.product_entity_id
The
HostID
(or
ID
after renaming) field is directly mapped to the
product_entity_id
field.
HostID
entity.entity.asset.asset_id
The
HostID
(or
ID
after renaming) field is directly mapped to the
asset_id
field.
HostMaintenance
entity.entity.asset.attribute.labels.value
The value of
HostMaintenance
(or
Maintenance
after renaming) from the raw log is used as the value of a label. The key for this label is set to
host_maintenance
.
HostProperties.Cores
entity.entity.asset.hardware.cpu_number_cores
The value of
HostProperties.Cores
is converted to an unsigned integer and mapped to
cpu_number_cores
.
HostProperties.InstanceFamily
entity.entity.asset.attribute.labels.value
The value of
HostProperties.InstanceFamily
from the raw log is used as the value of a label. The key for this label is set to
host_properties_instance_family
.
HostProperties.InstanceType
entity.entity.asset.attribute.labels.value
The value of
HostProperties.InstanceType
from the raw log is used as the value of a label. The key for this label is set to
host_properties_instance_type
.
HostProperties.Sockets
entity.entity.asset.attribute.labels.value
The value of
HostProperties.Sockets
is converted to a string and used as the value of a label. The key is set to
host_properties_sockets
.
HostProperties.TotalVCpus
entity.entity.asset.attribute.labels.value
The value of
HostProperties.TotalVCpus
(or
HostProperties.TotalVCPUs
after renaming) is converted to a string and used as the value of a label. The key is set to
host_properties_total_v_cpus
.
HostRecovery
entity.entity.asset.attribute.labels.value
The value of
HostRecovery
(or
Recovery
after renaming) from the raw log is used as the value of a label. The key for this label is set to
host_recovery
.
HostReservationID
entity.entity.asset.attribute.labels.value
The value of
HostReservationID
(or
ReservationID
after renaming) from the raw log is used as the value of a label. The key for this label is set to
host_reservation_id
.
MemberOfServiceLinkedResourceGroup
entity.entity.asset.attribute.labels.value
The value of
MemberOfServiceLinkedResourceGroup
is converted to a string and used as the value of a label. The key is set to
member_of_service_linked_resource_group
.
OwnerID
entity.entity.asset.attribute.labels.value
The value of
OwnerID
from the raw log is used as the value of a label. The key for this label is set to
owner_id
.
ReleaseTime
entity.entity.asset.attribute.labels.value
The value of
ReleaseTime
from the raw log is used as the value of a label. The key for this label is set to
release_time
.
State
entity.entity.asset.attribute.labels.value
The value of
State
from the raw log is used as the value of a label. The key for this label is set to
state
.
TagSet
entity.entity.asset.attribute.labels
The
TagSet
array is iterated over, and each tag's
Key
and
Value
are used as the key and value of a label, respectively.  The value
AMAZON_WEB_SERVICES
is assigned to this field by the parser. The
collection_time
from the raw log is mapped to the
collected_timestamp
field. The value
ASSET
is assigned to this field by the parser. The value
AWS EC2 HOSTS
is assigned to this field by the parser. The value
AWS
is assigned to this field by the parser. Relations are derived from
Instances
and
OutpostArn
fields, but these fields themselves are not directly mapped to the IDM object. The parser logic creates relation objects based on these fields and merges them into the
relations
array.
collection_time
entity.metadata.collected_timestamp
The log's
collection_time
is used as the event's
collected_timestamp
.
Need more help?
Get answers from Community members and Google SecOps professionals.
