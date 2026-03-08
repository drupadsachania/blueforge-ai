# Collect AWS EC2 Instance logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/aws-ec2-instances/  
**Scraped:** 2026-03-05T09:16:51.851173Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS EC2 Instance logs
Supported in:
Google secops
SIEM
This document explains how to configure AWS EC2 Instance logs into Google Security Operations for monitoring and analysis. The parser extracts data from instance reservation JSON logs, restructures and renames fields to conform to the UDM, handling various data types and nested structures, including network interfaces, groups, and tags, while also generating asset relationships and metadata. It also performs error handling and dropping malformed JSON messages.
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
Configure EC2 to send logs to CloudWatch Logs
Use SSH to connect to your EC2 instance, providing your key pair for authentication.
ssh
-i
your-key.pem
ec2-user@your-ec2-public-ip
Install the CloudWatch Logs agent:
To install the CloudWatch Logs agent on Amazon Linux, use the following command:
sudo
yum
install
-y
awslogs
To install the CloudWatch Logs agent on Ubuntu, use the following command:
sudo
apt-get
install
-y
awslogs
Open the CloudWatch Logs configuration file:
sudo
vi
/etc/awslogs/awslogs.conf
Create a script that fetches this Log Instance Metadata and writes it to a file:
#!/bin/bash
echo
"Architecture:
$(
curl
-s
http://169.254.169.254/latest/meta-data/architecture
)
"
>>
/var/log/instance_metadata.log
echo
"AmiLaunchIndex:
$(
curl
-s
http://169.254.169.254/latest/meta-data/ami-launch-index
)
"
>>
/var/log/instance_metadata.log
echo
"BootMode:
$(
curl
-s
http://169.254.169.254/latest/meta-data/boot-mode
)
"
>>
/var/log/instance_metadata.log
Save the script as
/etc/init.d/metadata_script.sh
and run it at instance startup using
crontab
or
rc.local
.
Open the configuration file for the CloudWatch Logs agent:
sudo
vi
/etc/awslogs/awslogs.conf
Add the following to the configuration file:
[/var/log/messages]
file
=
/var/log/messages
log_group_name
=
/ec2/system/logs
log_stream_name
=
{instance_id}
[/var/log/secure]
file
=
/var/log/secure
log_group_name
=
/ec2/security/logs
log_stream_name
=
{instance_id}
[/var/log/auth.log]
file
=
/var/log/auth.log
log_group_name
=
/ec2/auth/logs
log_stream_name
=
{instance_id}
[/var/log/httpd/access_log]
file
=
/var/log/httpd/access_log
log_group_name
=
/ec2/application/apache/access_logs
log_stream_name
=
{instance_id}
[/var/log/httpd/error_log]
file
=
/var/log/httpd/error_log
log_group_name
=
/ec2/application/apache/error_logs
log_stream_name
=
{instance_id}
Save the configuration and exit the editor.
Start the CloudWatch Logs agent:
On Amazon Linux:
sudo
service
awslogs
start
On Ubuntu:
sudo
service
awslogs
start
Verify that the agent is running:
sudo
service
awslogs
status
Configure IAM Permissions for Lambda and S3
In the
AWS IAM console
, create a new
IAM role
with the following permissions:
logs:PutSubscriptionFilter
logs:DescribeLogGroups
logs:GetLogEvents
s3:PutObject
Attach this role to your
Lambda function
that will export the logs to S3.
Configure Lambda to Export Logs to S3
Go to the
Lambda console
and create a new function.
import
boto3
import
gzip
from
io
import
BytesIO
s3
=
boto3
.
client
(
's3'
)
logs
=
boto3
.
client
(
'logs'
)
def
lambda_handler
(
event
,
context
):
log_group
=
event
[
'logGroup'
]
log_stream
=
event
[
'logStream'
]
log_events
=
logs
.
get_log_events
(
logGroupName
=
log_group
,
logStreamName
=
log_stream
,
startFromHead
=
True
)
log_data
=
"
\n
"
.
join
([
event
[
'message'
]
for
event
in
log_events
[
'events'
]])
# Compress and upload to S3
compressed_data
=
gzip
.
compress
(
log_data
.
encode
(
'utf-8'
))
s3
.
put_object
(
Bucket
=
'your-s3-bucket-name'
,
Key
=
'logs/ec2-log.gz'
,
Body
=
compressed_data
)
```
Replace
your-s3-bucket-name
with the actual name of your
S3 bucket
.
Attach the IAM role to the Lambda function created earlier.
In the
CloudWatch
console, go to the
Logs section
.
Select the
log group
; for example,
/ec2/system/logs
.
Click
Actions
>
Create Subscription Filter
.
Set the
destination
to the
Lambda function
created previously.
Configure a feed in Google SecOps to ingest AWS EC2 Instance logs
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
In the
Feed name
field, enter a name for the feed; for example,
AWS EC2 Instance Logs
.
Select
Amazon S3 V2
as the
Source type
.
Select
AWS EC2 Instance
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
UDM Mapping Table
Log Field
UDM Mapping
Logic
Architecture
entity.entity.asset.attribute.labels.key=instances_set_architecture
,
entity.entity.asset.attribute.labels.value
The value is taken directly from the
Instances.Architecture
field in the raw log.
AmiLaunchIndex
entity.entity.asset.attribute.labels.key=instances_set_ami_launch_index
,
entity.entity.asset.attribute.labels.value
The value is taken directly from the
Instances.AmiLaunchIndex
field in the raw log.
BlockDeviceMapping.Ebs.AttachTime
entity.entity.resource_ancestors.attribute.labels.key=instances_set_block_device_mapping_ebs_attach_time
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.BlockDeviceMapping.Ebs.AttachTime
.
BlockDeviceMapping.Ebs.DeleteOnTermination
entity.entity.resource_ancestors.attribute.labels.key=instances_set_block_device_mapping_ebs_delete_on_termination
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.BlockDeviceMapping.Ebs.DeleteOnTermination
.
BlockDeviceMapping.Ebs.Status
entity.entity.resource_ancestors.attribute.labels.key=instances_set_block_device_mapping_ebs_volume_status
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.BlockDeviceMapping.Ebs.Status
.
BlockDeviceMapping.Ebs.VolumeID
entity.entity.resource_ancestors.product_object_id
,
entity.entity.resource_ancestors.resource_type=VOLUME
The value is taken from
Instances.BlockDeviceMapping.Ebs.VolumeID
.
BlockDeviceMapping.Name
entity.entity.resource_ancestors.attribute.labels.key=instances_set_block_device_mapping_device_name
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.BlockDeviceMapping.Name
.
BootMode
entity.entity.asset.attribute.labels.key=instances_set_boot_mode
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.BootMode
.
CapacityReservationID
entity.entity.asset.attribute.labels.key=instances_set_capacity_reservation_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.CapacityReservationID
.
CapacityReservationSpecification.CapacityReservationPreference
entity.entity.asset.attribute.labels.key=instances_set_capacity_reservation_specification_capacity_reservation_preference
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.CapacityReservationSpecification.CapacityReservationPreference
.
CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationID
entity.entity.asset.attribute.labels.key=instances_set_capacity_reservation_specification_capacity_reservation_target_capacity_reservation_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationID
.
CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationResourceGroupArn
entity.entity.resource_ancestors.name
,
entity.entity.resource_ancestors.resource_subtype=Capacity Reservation Arn
The value is taken from
Instances.CapacityReservationSpecification.CapacityReservationTarget.CapacityReservationResourceGroupArn
.
ClientToken
entity.entity.asset.attribute.labels.key=instances_set_client_token
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ClientToken
.
CPU.AmdSevSnp
entity.entity.asset.attribute.labels.key=instances_set_cpu_options_amd_sev_snp
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.CPU.AmdSevSnp
.
CPU.CoreCount
entity.entity.asset.hardware.cpu_number_cores
The value is taken from
Instances.CPU.CoreCount
.
CPU.ThreadsPerCore
entity.entity.asset.attribute.labels.key=instances_set_cpu_options_threads_per_core
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.CPU.ThreadsPerCore
.
CurrentInstanceBootMode
entity.entity.asset.attribute.labels.key=instances_set_current_instance_boot_mode
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.CurrentInstanceBootMode
.
DNSName
entity.entity.network.dns_domain
The value is taken from
Instances.DNSName
.
EbsOptimized
entity.entity.asset.attribute.labels.key=instances_set_ebs_optimized
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.EbsOptimized
.
ElasticGpuAssociationSet.ElasticGpuAssociationID
entity.entity.asset.attribute.labels.key=instances_set_elastic_gpu_association_set_elastic_gpu_association_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ElasticGpuAssociationSet.ElasticGpuAssociationID
.
ElasticGpuAssociationSet.ElasticGpuAssociationState
entity.entity.asset.attribute.labels.key=instances_set_elastic_gpu_association_set_elastic_gpu_association_state
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ElasticGpuAssociationSet.ElasticGpuAssociationState
.
ElasticGpuAssociationSet.ElasticGpuAssociationTime
entity.entity.asset.attribute.labels.key=instances_set_elastic_gpu_association_set_elastic_gpu_association_time
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ElasticGpuAssociationSet.ElasticGpuAssociationTime
.
ElasticGpuAssociationSet.ElasticGpuID
entity.entity.asset.attribute.labels.key=instances_set_elastic_gpu_association_set_elastic_gpu_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ElasticGpuAssociationSet.ElasticGpuID
.
ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorArn
entity.entity.resource_ancestors.name
,
entity.entity.resource_ancestors.resource_subtype=Elastic Interface Accelerator Arn
The value is taken from
Instances.ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorArn
.
ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorAssociationID
entity.entity.resource_ancestors.attribute.labels.key=instances_set_elastic_inference_accelerator_association_set_elastic_inference_accelerator_association_id
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorAssociationID
.
ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorAssociationState
entity.entity.resource_ancestors.attribute.labels.key=instances_set_elastic_inference_accelerator_association_set_elastic_inference_accelerator_association_state
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorAssociationState
.
ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorAssociationTime
entity.entity.resource_ancestors.attribute.labels.key=instances_set_elastic_inference_accelerator_association_set_elastic_inference_accelerator_association_time
,
entity.entity.resource_ancestors.attribute.labels.value
The value is taken from
Instances.ElasticInferenceAcceleratorAssociationSet.ElasticInferenceAcceleratorAssociationTime
.
EnaSupport
entity.entity.asset.attribute.labels.key=instances_set_ena_support
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.EnaSupport
.
EnclaveOptions.Enabled
entity.entity.asset.attribute.labels.key=instances_set_enclave_options_enabled
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.EnclaveOptions.Enabled
.
GroupSet.GroupID
entity.entity.group.product_object_id
,
entity.entity.group.attribute.labels.key=group_set_group_id
,
entity.entity.group.attribute.labels.value
,
entity.entity.group.attribute.labels.key=instances_set_group_set_group_id
,
entity.entity.group.attribute.labels.value
,
entity.entity.group.attribute.labels.key=instances_set_network_interface_set_group_set_group_id
,
entity.entity.group.attribute.labels.value
The value is taken from
GroupSet.GroupID
. The first
GroupID
in the array is mapped to
entity.entity.group.product_object_id
. Subsequent
GroupID
values are mapped as labels.
GroupSet.GroupName
entity.entity.group.group_display_name
,
entity.entity.group.attribute.labels.key=group_set_group_name
,
entity.entity.group.attribute.labels.value
,
entity.entity.group.attribute.labels.key=instances_set_group_set_group_name
,
entity.entity.group.attribute.labels.value
,
entity.entity.group.attribute.labels.key=instances_set_network_interface_set_group_set_group_name
,
entity.entity.group.attribute.labels.value
The value is taken from
GroupSet.GroupName
. The first
GroupName
in the array is mapped to
entity.entity.group.group_display_name
. Subsequent
GroupName
values are mapped as labels.
HibernationOptions
entity.entity.asset.attribute.labels.key=instances_set_hibernation_options
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.HibernationOptions
.
HibernationOptions.Configured
entity.entity.asset.attribute.labels.key=instances_set_hibernation_options_configured
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.HibernationOptions.Configured
.
Hypervisor
entity.entity.asset.attribute.labels.key=instances_set_hypervisor
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Hypervisor
.
IamInstanceProfile.Arn
entity.entity.resource_ancestors.name
,
entity.entity.resource_ancestors.resource_subtype=Instance Profile Arn
The value is taken from
Instances.IamInstanceProfile.Arn
.
IamInstanceProfile.ID
entity.entity.resource_ancestors.product_object_id
The value is taken from
Instances.IamInstanceProfile.ID
.
ImageID
entity.entity.resource_ancestors.product_object_id
,
entity.entity.resource_ancestors.resource_type=IMAGE
The value is taken from
Instances.ImageID
.
InstanceID
entity.metadata.product_entity_id
,
entity.entity.asset.asset_id
The value is taken from
Instances.InstanceID
.
InstanceLifecycle
entity.entity.asset.attribute.labels.key=instances_set_instance_lifecycle
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.InstanceLifecycle
.
InstanceState.Code
entity.entity.asset.attribute.labels.key=instances_set_instance_state_code
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.InstanceState.Code
.
InstanceState.Name
entity.entity.asset.deployment_status
The value is derived from
Instances.InstanceState.Name
.  If the value is
running
, the UDM field is set to
ACTIVE
. If the value is
shutting-down
or
stopping
, the UDM field is set to
PENDING_DECOMMISSION
. If the value is
stopped
or
terminated
, the UDM field is set to
DECOMMISSIONED
.
InstanceType
entity.entity.asset.category
The value is taken from
Instances.InstanceType
.
IPAddress
entity.entity.asset.ip
The value is taken from
Instances.IPAddress
.
Ipv6Address
entity.entity.asset.ip
The value is taken from
Instances.Ipv6Address
.
KernelID
entity.entity.asset.attribute.labels.key=instances_set_kernel_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.KernelID
.
KeyName
entity.entity.asset.attribute.labels.key=instances_set_key_name
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.KeyName
.
LaunchTime
entity.metadata.creation_timestamp
The value is taken from
Instances.LaunchTime
.
LicenseSet.LicenseConfigurationArn
entity.entity.resource_ancestors.name
,
entity.entity.resource_ancestors.resource_subtype=License Configuration Arn
The value is taken from
Instances.LicenseSet.LicenseConfigurationArn
.
MaintenanceOptions
entity.entity.asset.attribute.labels.key=instances_set_maintenance_options_auto_recovery
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MaintenanceOptions
.
MetadataOptions.HTTPEndpoint
entity.entity.asset.attribute.labels.key=instances_set_metadata_options_http_endpoint
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MetadataOptions.HTTPEndpoint
.
MetadataOptions.HTTPProtocolIpv6
entity.entity.asset.attribute.labels.key=instances_set_metadata_options_http_protocol_ipv6
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MetadataOptions.HTTPProtocolIpv6
.
MetadataOptions.HTTPPutResponseHopLimit
entity.entity.asset.attribute.labels.key=instances_set_metadata_options_http_put_response_hop_limit
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MetadataOptions.HTTPPutResponseHopLimit
.
MetadataOptions.HTTPTokens
entity.entity.asset.attribute.labels.key=instances_set_metadata_options_http_tokens
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MetadataOptions.HTTPTokens
.
MetadataOptions.InstanceMetadataTags
entity.entity.asset.attribute.labels.key=instances_set_metadata_options_instance_metadata_tags
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MetadataOptions.InstanceMetadataTags
.
MetadataOptions.State
entity.entity.asset.attribute.labels.key=instances_set_metadata_options_state
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.MetadataOptions.State
.
Monitoring.State
entity.entity.asset.attribute.labels.key=instances_set_monitoring_state
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Monitoring.State
.
NetworkInterfaceSet.Association.CarrierIP
entity.entity.asset.nat_ip
The value is taken from
Instances.NetworkInterfaceSet.Association.CarrierIP
.
NetworkInterfaceSet.Association.CustomerOwnedIP
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_association_customer_owned_ip
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Association.CustomerOwnedIP
.
NetworkInterfaceSet.Association.IPOwnerID
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_association_ip_owner_id
,
entity.entity.asset.attribute.labels.value
,
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_private_ip_addresses_set_association_ip_owner_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Association.IPOwnerID
.
NetworkInterfaceSet.Association.PublicDNSName
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_association_public_dns_name
,
entity.entity.asset.attribute.labels.value
,
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_private_ip_addresses_set_association_public_dns_name
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Association.PublicDNSName
.
NetworkInterfaceSet.Association.PublicIP
entity.entity.asset.ip
The value is taken from
Instances.NetworkInterfaceSet.Association.PublicIP
.
NetworkInterfaceSet.Attachment.AttachTime
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_attachment_attach_time
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Attachment.AttachTime
.
NetworkInterfaceSet.Attachment.AttachmentID
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_attachment_attachment_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Attachment.AttachmentID
.
NetworkInterfaceSet.Attachment.DeleteOnTermination
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_attachment_delete_on_termination
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Attachment.DeleteOnTermination
.
NetworkInterfaceSet.Attachment.DeviceIndex
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_attachment_device_index
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Attachment.DeviceIndex
.
NetworkInterfaceSet.Attachment.NetworkCardIndex
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_attachment_network_card_index
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Attachment.NetworkCardIndex
.
NetworkInterfaceSet.Attachment.Status
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_attachment_status
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Attachment.Status
.
NetworkInterfaceSet.Description
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_description
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Description
.
NetworkInterfaceSet.GroupSet.GroupID
entity.entity.group.attribute.labels.key=instances_set_network_interface_set_group_set_group_id
,
entity.entity.group.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.GroupSet.GroupID
.
NetworkInterfaceSet.GroupSet.GroupName
entity.entity.group.attribute.labels.key=instances_set_network_interface_set_group_set_group_name
,
entity.entity.group.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.GroupSet.GroupName
.
NetworkInterfaceSet.InterfaceType
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_interface_type
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.InterfaceType
.
NetworkInterfaceSet.Ipv6AddressesSet.Ipv6Address
entity.entity.asset.ip
The value is taken from
Instances.NetworkInterfaceSet.Ipv6AddressesSet.Ipv6Address
.
NetworkInterfaceSet.Ipv6AddressesSet.IsPrimaryIpv6
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_ipv6_addresses_set_is_primary_ipv6
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Ipv6AddressesSet.IsPrimaryIpv6
.
NetworkInterfaceSet.MacAddress
entity.entity.asset.mac
The value is taken from
Instances.NetworkInterfaceSet.MacAddress
.
NetworkInterfaceSet.NetworkInterfaceID
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_network_interface_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.NetworkInterfaceID
.
NetworkInterfaceSet.OwnerID
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_owner_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.OwnerID
.
NetworkInterfaceSet.PrivateDNSName
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_private_dns_name
,
entity.entity.asset.attribute.labels.value
,
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_private_ip_addresses_set_private_dns_name
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.PrivateDNSName
.
NetworkInterfaceSet.PrivateIPAddress
entity.entity.asset.ip
The value is taken from
Instances.NetworkInterfaceSet.PrivateIPAddress
.
NetworkInterfaceSet.PrivateIPAddressesSet.Primary
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_private_ip_addresses_set_primary
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.PrivateIPAddressesSet.Primary
.
NetworkInterfaceSet.PrivateIPAddressesSet.PrivateIPAddress
entity.entity.asset.ip
The value is taken from
Instances.NetworkInterfaceSet.PrivateIPAddressesSet.PrivateIPAddress
.
NetworkInterfaceSet.SourceDestCheck
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_source_dest_check
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.SourceDestCheck
.
NetworkInterfaceSet.Status
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_status
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.Status
.
NetworkInterfaceSet.SubnetID
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_subnet_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.SubnetID
.
NetworkInterfaceSet.VpcID
entity.entity.asset.attribute.labels.key=instances_set_network_interface_set_vpc_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.NetworkInterfaceSet.VpcID
.
OutpostArn
entity.relations.entity.asset.product_object_id
The value is taken from
Instances.OutpostArn
.
Placement.Affinity
entity.entity.asset.attribute.labels.key=instances_set_placement_affinity
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Placement.Affinity
.
Placement.AvailabilityZone
entity.entity.asset.attribute.cloud.availability_zone
The value is taken from
Instances.Placement.AvailabilityZone
.
Placement.GroupID
entity.entity.group.attribute.labels.key=instances_set_placement_group_id
,
entity.entity.group.attribute.labels.value
The value is taken from
Instances.Placement.GroupID
.
Placement.GroupName
entity.entity.group.attribute.labels.key=instances_set_placement_group_name
,
entity.entity.group.attribute.labels.value
The value is taken from
Instances.Placement.GroupName
.
Placement.HostID
entity.relations.entity.asset.asset_id
The value is taken from
Instances.Placement.HostID
.
Placement.HostResourceGroupArn
entity.relations.entity.asset.attribute.labels.key=instances_set_placement_host_resource_group_arn
,
entity.relations.entity.asset.attribute.labels.value
The value is taken from
Instances.Placement.HostResourceGroupArn
.
Placement.PartitionNumber
entity.entity.asset.attribute.labels.key=instances_set_placement_partition_number
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Placement.PartitionNumber
.
Placement.SpreadDomain
entity.entity.asset.attribute.labels.key=instances_set_placement_spread_domain
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Placement.SpreadDomain
.
Placement.Tenancy
entity.entity.asset.attribute.labels.key=instances_set_placement_tenancy
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Placement.Tenancy
.
PlatformDetails
entity.entity.asset.attribute.labels.key=instances_set_platform_details
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.PlatformDetails
.
PrivateDNSName
entity.entity.network.dns.questions.name
The value is taken from
Instances.PrivateDNSName
.
PrivateDNSNameOptions.EnableResourceNameDnsAAAARecord
entity.entity.network.dns.questions.type
If the value is
true
, the UDM field is set to 28.
PrivateDNSNameOptions.EnableResourceNameDnsARecord
entity.entity.network.dns.questions.type
If the value is
true
, the UDM field is set to 1.
PrivateDNSNameOptions.HostnameType
entity.entity.asset.attribute.labels.key=instances_set_private_dns_name_options_hostname_type
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.PrivateDNSNameOptions.HostnameType
.
PrivateIPAddress
entity.entity.asset.ip
The value is taken from
Instances.PrivateIPAddress
.
ProductCodes.ProductCode
entity.entity.asset.attribute.labels.key=instances_set_product_codes_product_code
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ProductCodes.ProductCode
.
ProductCodes.Type
entity.entity.asset.attribute.labels.key=instances_set_product_codes_type
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.ProductCodes.Type
.
RamdiskID
entity.entity.asset.attribute.labels.key=instances_set_ramdisk_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.RamdiskID
.
Reason
entity.entity.asset.attribute.labels.key=instances_set_reason
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.Reason
.
ReservationID
entity.additional.fields.key=reservation_id
,
entity.additional.fields.value.string_value
The value is taken from
ReservationID
.
RequesterID
entity.additional.fields.key=requester_id
,
entity.additional.fields.value.string_value
The value is taken from
RequesterID
.
RootDeviceName
entity.entity.asset.attribute.labels.key=instances_set_root_device_name
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.RootDeviceName
.
RootDeviceType
entity.entity.asset.attribute.labels.key=instances_set_root_device_type
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.RootDeviceType
.
SourceDestCheck
entity.entity.asset.attribute.labels.key=instances_set_source_dest_check
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.SourceDestCheck
.
SpotInstanceRequestID
entity.entity.asset.attribute.labels.key=instances_set_spot_instance_request_id
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.SpotInstanceRequestID
.
SriovNetSupport
entity.entity.asset.attribute.labels.key=instances_set_sriov_net_support
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.SriovNetSupport
.
StateReason
entity.entity.asset.attribute.labels.key=instances_set_state_reason_code
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.StateReason
.
StateReason.Code
entity.entity.asset.attribute.labels.key=instances_set_state_reason_code
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.StateReason.Code
.
StateReason.Message
entity.entity.asset.attribute.labels.key=instances_set_state_reason_message
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.StateReason.Message
.
SubnetID
entity.entity.resource_ancestors.product_object_id
,
entity.entity.resource_ancestors.resource_type=SUBNET
The value is taken from
Instances.SubnetID
.
TagSet.Key
entity.entity.asset.attribute.labels.key
The value is taken from
Instances.TagSet.Key
.
TagSet.Value
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.TagSet.Value
.
TpmSupport
entity.entity.asset.attribute.labels.key=instances_set_tpm_support
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.TpmSupport
.
UsageOperation
entity.entity.asset.attribute.labels.key=instances_set_usage_operation
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.UsageOperation
.
UsageOperationUpdateTime
entity.entity.asset.attribute.labels.key=instances_set_usage_operation_update_time
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.UsageOperationUpdateTime
.
VirtualizationType
entity.entity.asset.attribute.labels.key=instances_set_virtualization_type
,
entity.entity.asset.attribute.labels.value
The value is taken from
Instances.VirtualizationType
.
VpcID
entity.entity.resource_ancestors.product_object_id
,
entity.entity.resource_ancestors.resource_type=VPC_NETWORK
The value is taken from
Instances.VpcID
.
collection_time
entity.metadata.collected_timestamp
The value is taken directly from the
collection_time
field in the raw log.  Hardcoded to
AMAZON_WEB_SERVICES
. Hardcoded to
AMAZON_WEB_SERVICES
for IMAGE, VOLUME, SUBNET, VPC_NETWORK, Instance Profile Arn, Capacity Reservation Arn, Elastic Interface Accelerator Arn, and License Configuration Arn resource types. Hardcoded to
SERVER
. Hardcoded to
Amazon EC2
. Hardcoded to
AWS
. Hardcoded to
ASSET
if
Instances.Placement.HostID
is present and not empty. Hardcoded to
EXECUTES
if
Instances.Placement.HostID
is present and not empty. Hardcoded to ASSET.
Need more help?
Get answers from Community members and Google SecOps professionals.
