# Collect AWS GuardDuty logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/guardduty/  
**Scraped:** 2026-03-05T09:19:42.893349Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect AWS GuardDuty logs
Supported in:
Google secops
SIEM
This document describes how you can collect AWS GuardDuty logs by
setting up a Google Security Operations feed.
For more information, see
Data ingestion to Google Security Operations
.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the parser
with the
GUARDDUTY
ingestion label.
Before you begin
Ensure that you have the following prerequisites:
AWS S3 bucket is created. To create the AWS S3 bucket, see
Create your first S3 bucket
.
KMS key is created. To create the KMS key, see
Creating asymmetric KMS keys
.
AWS GuardDuty has permission to access the KMS key. To grant
access to the KMS key, see
Exporting findings
.
GuardDuty encrypts the findings data in your bucket by using an AWS KMS key.
Configure AWS GuardDuty
To configure AWS GuardDuty, do the following:
Sign in to the AWS console.
Search for
GuardDuty
.
Select
Settings
.
In the
Finding export option
section, do the following:
From the
Frequency for updated findings
list, select
Update CWE and
S3 every 15 minutes
. The frequency selection is for the updated findings. The
new findings are exported after 5 minutes from the time of creation.
In the
S3 bucket
section, select the S3 bucket in which you want to export
the GuardDuty findings.
In the
Log file prefix
section, provide the log file prefix.
In the
KMS encryption
section, select the KMS encryption.
From the
Key alias
list, select the key.
Click
Save
.
After the log files are stored in the S3 bucket, create an SQS queue and
attach it with the S3 bucket.
Sample KMS policy
The following is a sample KMS policy:
{
            "Sid": "Allow GuardDuty to encrypt findings",
            "Effect": "Allow",
            "Principal": {
                "Service": "guardduty.
AWS_REGION
.amazonaws.com"
            },
            "Action": [
                "kms:Encrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "
KEY_ARN
"
        }
Replace the following:
AWS_REGION
: the chosen region.
KEY_ARN
: Amazon Resource Name (ARN) of the KMS key.
Check the required IAM user and KMS key policies for S3, SQS, and KMS.
Based on the service and region, identify the endpoints for connectivity by
referring to the following AWS documentation:
For information about any logging sources, see
AWS Identity and Access Management endpoints and quotas
.
For information about S3 logging sources, see
Amazon Simple Storage Service endpoints and quotas
.
For information about SQS logging sources, see
Amazon Simple Queue Service endpoints and quotas
.
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
Enter a unique name for the
Feed name
.
Select
Amazon S3 V2
or
Amazon SQS V2
as the
Source type
.
Select
AWS GuardDuty
as the
Log type
.
Click
Next
and then click
Submit
.
Google Security Operations supports log collection using an access key ID and secret method.
To create the access key ID and secret, see
Configure tool authentication with AWS
.
Based on the AWS GuardDuty configuration that you created, specify values for
the following fields.
If using Amazon S3 V2
**S3 URI**
**Source deletion option**
**Maximum File Age**
If using Amazon SQS V2
Queue name
Account number
Queue access key ID
Queue secret access key
Source deletion option
Maximum File Age
Click
Next
and then click
Submit
.
For more information about Google Security Operations feeds, see
Google Security Operations feeds documentation
. For information about requirements for each
feed type, see
Feed configuration by type
.
If you encounter issues when you create feeds,
contact Google Security Operations support
Field mapping reference
This parser code processes AWS GuardDuty findings in JSON format, extracting relevant fields and mapping them to a unified data model (UDM). It performs data transformations, including string replacements, merging arrays, and converting data types, to create a structured representation of the security event for analysis and correlation.
UDM mapping table
Log Field
UDM Mapping
Logic
accountId
principal.group.product_object_id
The AWS account ID associated with the finding.
additionalInfo.portsScannedSample
event.idm.read_only_udm.about.port
List of ports scanned during a port sweep.
additionalInfo.sample
security_result.about.labels.value
Indicates whether the finding is a sample finding.
additionalInfo.threatListName
security_result.threat_feed_name
The name of the threat list that triggered the finding.
additionalInfo.threatName
security_result.threat_name
The name of the threat that triggered the finding.
additionalInfo.userAgent
.fullUserAgent
network.http.user_agent
The full user agent string associated with the finding.
additionalInfo.userAgent
.userAgentCategory
security_result.detection_fields.value
The category of the user agent associated with the finding.
arn
target.asset.attribute
.cloud.project.product_object_id
The Amazon Resource Name (ARN) of the finding.
detail.accountId
principal.group.product_object_id
The AWS account ID associated with the finding.
detail.description
security_result.description
A detailed description of the finding.
detail.id
target.asset.attribute.cloud.project.id
A unique ID for the finding.
detail.resource.accessKeyDetails
principal.user
Details about the AWS access key involved in the finding.
detail.resource.accessKeyDetails
.accessKeyId
principal.user.userid
The ID of the AWS access key involved in the finding.
detail.resource.accessKeyDetails
.principalId
principal.user.userid
The principal ID of the AWS access key involved in the finding.
detail.resource.accessKeyDetails
.userType
principal.user.attribute.roles.name
The type of user associated with the AWS access key involved in the finding.
detail.resource.accessKeyDetails
.userName
principal.user.user_display_name
The name of the user associated with the AWS access key involved in the finding.
detail.resource.s3BucketDetails
.0.arn
target.resource.name
The ARN of the S3 bucket involved in the finding.
detail.resource.s3BucketDetails
.0.defaultServerSideEncryption.encryptionType
network.tls.client.supported_ciphers
The type of server-side encryption used for the S3 bucket involved in the finding.
detail.resource.s3BucketDetails
.0.name
target.resource.name
The name of the S3 bucket involved in the finding.
detail.resource.s3BucketDetails
.0.owner.id
target.resource.attribute.labels.value
The ID of the owner of the S3 bucket involved in the finding.
detail.resource.s3BucketDetails
.0.publicAccess.effectivePermission
target.resource.attribute.labels.value
The effective permission of the S3 bucket involved in the finding.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.blockPublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.blockPublicPolicy
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.ignorePublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.restrictPublicBuckets
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.accessControlList
.allowsPublicReadAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the access control list (ACL) allows public read access.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.accessControlList
.allowsPublicWriteAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the access control list (ACL) allows public write access.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.blockPublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.blockPublicPolicy
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.ignorePublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.restrictPublicBuckets
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.bucketPolicy
.allowsPublicReadAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the bucket policy allows public read access.
detail.resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.bucketPolicy
.allowsPublicWriteAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the bucket policy allows public write access.
detail.resource.s3BucketDetails
.0.type
target.resource.attribute.labels.value
The type of S3 bucket involved in the finding.
detail.service.action
.actionType
principal.group.attribute.labels.value
The type of action associated with the finding.
detail.service.action
.awsApiCallAction.api
principal.application
The name of the AWS API call involved in the finding.
detail.service.action
.awsApiCallAction.callerType
principal.group.attribute.labels.value
The type of caller that made the AWS API call involved in the finding.
detail.service.action
.awsApiCallAction.domainDetails.domain
network.dns.questions.name
The domain name associated with the AWS API call involved in the finding.
detail.service.action.awsApiCallAction
.remoteIpDetails.country.countryName
target.location.country_or_region
The country name associated with the remote IP address that made the AWS API call involved in the finding.
detail.service.action.awsApiCallAction
.remoteIpDetails.geoLocation.lat
target.location.region_latitude
The latitude of the remote IP address that made the AWS API call involved in the finding.
detail.service.action.awsApiCallAction
.remoteIpDetails.geoLocation.lon
target.location.region_longitude
The longitude of the remote IP address that made the AWS API call involved in the finding.
detail.service.action
.awsApiCallAction.remoteIpDetails.ipAddressV4
target.ip
The IP address that made the AWS API call involved in the finding.
detail.service.action
.awsApiCallAction.serviceName
metadata.description
The name of the AWS service involved in the finding.
detail.service.action
.dnsRequestAction.blocked
security_result.action
Whether the DNS request was blocked.
detail.service.action
.dnsRequestAction.domain
principal.administrative_domain
The domain name associated with the DNS request involved in the finding.
detail.service.action
.dnsRequestAction.protocol
network.ip_protocol
The protocol used for the DNS request involved in the finding.
detail.service.action
.networkConnectionAction.blocked
security_result.action
Whether the network connection was blocked.
detail.service.action
.networkConnectionAction.connectionDirection
network.direction
The direction of the network connection involved in the finding.
detail.service.action
.networkConnectionAction.localIpDetails
.ipAddressV4
principal.ip
The local IP address involved in the network connection.
detail.service.action
.networkConnectionAction.localPortDetails
.port
principal.port
The local port involved in the network connection.
detail.service.action
.networkConnectionAction.localPortDetails
.portName
principal.application
The name of the local port involved in the network connection.
detail.service.action
.networkConnectionAction.protocol
network.ip_protocol
The protocol used for the network connection involved in the finding.
detail.service.action
.networkConnectionAction.remoteIpDetails
.city.cityName
target.location.city
The city name associated with the remote IP address involved in the network connection.
detail.service.action
.networkConnectionAction.remoteIpDetails
.country.countryName
target.location.country_or_region
The country name associated with the remote IP address involved in the network connection.
detail.service.action
.networkConnectionAction.remoteIpDetails
.ipAddressV4
target.ip
The remote IP address involved in the network connection.
detail.service.action
.networkConnectionAction.remotePortDetails
.port
target.port
The remote port involved in the network connection.
detail.service.action
.networkConnectionAction.remotePortDetails
.portName
target.application
The name of the remote port involved in the network connection.
detail.service.action
.portProbeAction.blocked
security_result.action
Whether the port probe was blocked.
detail.service.action
.portProbeAction.portProbeDetails
.0.localPortDetails.port
target.port
The local port that was probed.
detail.service.action
.portProbeAction.portProbeDetails
.0.localPortDetails.portName
principal.application
The name of the local port that was probed.
detail.service.action
.portProbeAction.portProbeDetails
.0.remoteIpDetails.city.cityName
target.location.city
The city name associated with the remote IP address that performed the port probe.
detail.service.action
.portProbeAction.portProbeDetails
.0.remoteIpDetails.country.countryName
target.location.country_or_region
The country name associated with the remote IP address that performed the port probe.
detail.service.action
.portProbeAction.portProbeDetails
.0.remoteIpDetails.geoLocation.lat
target.location.region_latitude
The latitude of the remote IP address that performed the port probe.
detail.service.action
.portProbeAction.portProbeDetails
.0.remoteIpDetails.geoLocation.lon
target.location.region_longitude
The longitude of the remote IP address that performed the port probe.
detail.service.action
.portProbeAction.portProbeDetails
.0.remoteIpDetails.ipAddressV4
target.ip
The remote IP address that performed the port probe.
detail.service.additionalInfo
.threatListName
security_result.threat_feed_name
The name of the threat list that triggered the finding.
detail.service.additionalInfo
.threatName
security_result.threat_name
The name of the threat that triggered the finding.
detail.service.additionalInfo
.userAgent.fullUserAgent
network.http.user_agent
The full user agent string associated with the finding.
detail.service.additionalInfo
.userAgent.userAgentCategory
security_result.detection_fields.value
The category of the user agent associated with the finding.
detail.service.additionalInfo
.value
security_result.about
.resource.attribute.labels.value
Additional information about the finding.
detail.title
security_result.summary
A short title for the finding.
detail.type
metadata.product_event_type
The type of finding.
detail.updatedAt
metadata.event_timestamp
The time the finding was last updated.
detail-type
event.idm.read_only_udm
.additional.fields.value.string_value
The type of event that triggered the finding.
partition
target.asset.attribute
.cloud.project.type
The AWS partition that the finding occurred in.
resource.accessKeyDetails
principal.user
Details about the AWS access key involved in the finding.
resource.accessKeyDetails.accessKeyId
principal.user.userid
The ID of the AWS access key involved in the finding.
resource.accessKeyDetails.principalId
principal.user.userid
The principal ID of the AWS access key involved in the finding.
resource.accessKeyDetails.userType
principal.user.attribute.roles.name
The type of user associated with the AWS access key involved in the finding.
resource.accessKeyDetails.userName
principal.user.user_display_name
The name of the user associated with the AWS access key involved in the finding.
resource.instanceDetails.availabilityZone
target.asset.attribute.cloud.availability_zone
The availability zone of the EC2 instance involved in the finding.
resource.instanceDetails.imageDescription
event.idm.read_only_udm
.principal.resource.attribute.labels.value
The description of the AMI used to launch the EC2 instance involved in the finding.
resource.instanceDetails.imageId
event.idm.read_only_udm
.additional.fields.value.string_value
The ID of the AMI used to launch the EC2 instance involved in the finding.
resource.instanceDetails
.iamInstanceProfile.arn
target.resource.attribute.labels.value
The ARN of the IAM instance profile associated with the EC2 instance involved in the finding.
resource.instanceDetails
.iamInstanceProfile.id
target.resource.attribute.labels.value
The ID of the IAM instance profile associated with the EC2 instance involved in the finding.
resource.instanceDetails.instanceId
target.resource.product_object_id
The ID of the EC2 instance involved in the finding.
resource.instanceDetails.instanceState
target.resource.attribute.labels.value
The state of the EC2 instance involved in the finding.
resource.instanceDetails.instanceType
target.resource.attribute.labels.value
The type of the EC2 instance involved in the finding.
resource.instanceDetails
.launchTime
target.resource.attribute.creation_time
The time the EC2 instance involved in the finding was launched.
resource.instanceDetails
.networkInterfaces.0.networkInterfaceId
target.resource.attribute.labels.value
The ID of the network interface associated with the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.privateDnsName
target.resource.attribute.labels.value
The private DNS name of the network interface associated with the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.publicDnsName
target.resource.attribute.labels.value
The public DNS name of the network interface associated with the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.publicIp
principal.ip
The public IP address of the network interface associated with the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.privateIpAddress
principal.ip
The private IP address of the network interface associated with the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.securityGroups
.0.groupId
target.user.group_identifiers
The ID of the security group associated with the network interface of the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.securityGroups
.0.groupName
target.user.group_identifiers
The name of the security group associated with the network interface of the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.subnetId
target.resource.attribute.labels.value
The ID of the subnet associated with the network interface of the EC2 instance involved in the finding.
resource.instanceDetails
.networkInterfaces.0.vpcId
target.asset.attribute.cloud.vpc.id
The ID of the VPC associated with the network interface of the EC2 instance involved in the finding.
resource.instanceDetails.outpostArn
target.resource.attribute.labels.value
The ARN of the outpost associated with the EC2 instance involved in the finding.
resource.instanceDetails.platform
target.asset.platform_software.platform_version
The platform of the EC2 instance involved in the finding.
resource.instanceDetails
.productCodes.0.productCodeType
target.resource.type
The type of product code associated with the EC2 instance involved in the finding.
resource.instanceDetails.tags
target.asset.attribute.labels
The tags associated with the EC2 instance involved in the finding.
resource.kubernetesDetails
.kubernetesUserDetails.username
principal.user.userid
The username of the Kubernetes user involved in the finding.
resource.rdsDbInstanceDetails
.dbClusterIdentifier
event.idm.read_only_udm
.target.resource_ancestors.product_object_id
The identifier of the RDS DB cluster involved in the finding.
resource.rdsDbInstanceDetails
.dbInstanceArn
target.resource.name
The ARN of the RDS DB instance involved in the finding.
resource.rdsDbInstanceDetails
.dbInstanceIdentifier
target.resource.product_object_id
The identifier of the RDS DB instance involved in the finding.
resource.rdsDbUserDetails.user
principal.user.userid
The username of the RDS DB user involved in the finding.
resource.resourceType
target.resource.resource_subtype
The type of resource involved in the finding.
resource.s3BucketDetails
principal.resource.attribute.labels
Details about the S3 bucket involved in the finding.
resource.s3BucketDetails.0.arn
target.resource.name
The ARN of the S3 bucket involved in the finding.
resource.s3BucketDetails.0.createdAt
event.idm.read_only_udm
.principal.resource.attribute.labels.value
The time the S3 bucket involved in the finding was created.
resource.s3BucketDetails.0
.defaultServerSideEncryption.encryptionType
network.tls.client.supported_ciphers
The type of server-side encryption used for the S3 bucket involved in the finding.
resource.s3BucketDetails.0.name
target.resource.name
The name of the S3 bucket involved in the finding.
resource.s3BucketDetails.0.owner.id
target.resource.attribute.labels.value
The ID of the owner of the S3 bucket involved in the finding.
resource.s3BucketDetails
.0.publicAccess.effectivePermission
target.resource.attribute.labels.value
The effective permission of the S3 bucket involved in the finding.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.blockPublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.blockPublicPolicy
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.ignorePublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.accountLevelPermissions.blockPublicAccess
.restrictPublicBuckets
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the account.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.accessControlList
.allowsPublicReadAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the access control list (ACL) allows public read access.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.accessControlList
.allowsPublicWriteAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the access control list (ACL) allows public write access.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.blockPublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.blockPublicPolicy
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.ignorePublicAcls
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.blockPublicAccess
.restrictPublicBuckets
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether public access blocks are enabled for the bucket.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.bucketPolicy
.allowsPublicReadAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the bucket policy allows public read access.
resource.s3BucketDetails
.0.publicAccess.permissionConfiguration
.bucketLevelPermissions.bucketPolicy
.allowsPublicWriteAccess
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the bucket policy allows public write access.
resource.s3BucketDetails.0.tags
event.idm.read_only_udm
.principal.resource.attribute.labels
The tags associated with the S3 bucket involved in the finding.
resource.s3BucketDetails.0.type
target.resource.attribute.labels.value
The type of S3 bucket involved in the finding.
service.action
.actionType
principal.group.attribute.labels.value
The type of action associated with the finding.
service.action
.awsApiCallAction.affectedResources
.AWS_CloudTrail_Trail
event.idm.read_only_udm
.principal.resource.attribute.labels.value
The name of the AWS CloudTrail trail involved in the finding.
service.action
.awsApiCallAction.affectedResources
.AWS_S3_Bucket
event.idm.read_only_udm
.principal.resource.attribute.labels.value
The name of the S3 bucket involved in the finding.
service.action
.awsApiCallAction.api
principal.application
The name of the AWS API call involved in the finding.
service.action
.awsApiCallAction.callerType
principal.group.attribute.labels.value
The type of caller that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.domainDetails.domain
network.dns.questions.name
The domain name associated with the AWS API call involved in the finding.
service.action
.awsApiCallAction.errorCode
security_result.rule_type
The error code associated with the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.country.countryName
target.location.country_or_region
The country name associated with the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.geoLocation.lat
target.location.region_latitude
The latitude of the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.geoLocation.lon
target.location.region_longitude
The longitude of the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.ipAddressV4
target.ip
The IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.organization.asn
event.idm.read_only_udm
.additional.fields.value.string_value
The Autonomous System Number (ASN) of the organization associated with the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.organization.asnOrg
event.idm.read_only_udm
.additional.fields.value.string_value
The name of the organization associated with the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.organization.isp
event.idm.read_only_udm
.additional.fields.value.string_value
The name of the internet service provider (ISP) associated with the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.remoteIpDetails
.organization.org
event.idm.read_only_udm
.additional.fields.value.string_value
The name of the organization associated with the remote IP address that made the AWS API call involved in the finding.
service.action
.awsApiCallAction.serviceName
metadata.description
The name of the AWS service involved in the finding.
service.action
.dnsRequestAction.blocked
security_result.action
Whether the DNS request was blocked.
service.action
.dnsRequestAction.domain
principal.administrative_domain
The domain name associated with the DNS request involved in the finding.
service.action
.dnsRequestAction.protocol
network.ip_protocol
The protocol used for the DNS request involved in the finding.
service.action
.kubernetesApiCallAction.remoteIpDetails
.country.countryName
target.location.country_or_region
The country name associated with the remote IP address that made the Kubernetes API call involved in the finding.
service.action
.kubernetesApiCallAction.remoteIpDetails
.geoLocation.lat
target.location.region_latitude
The latitude of the remote IP address that made the Kubernetes API call involved in the finding.
service.action
.kubernetesApiCallAction.remoteIpDetails
.geoLocation.lon
target.location.region_longitude
The longitude of the remote IP address that made the Kubernetes API call involved in the finding.
service.action
.kubernetesApiCallAction.remoteIpDetails
.ipAddressV4
target.ip
The IP address that made the Kubernetes API call involved in the finding.
service.action
.networkConnectionAction.blocked
security_result.action
Whether the network connection was blocked.
service.action
.networkConnectionAction.connectionDirection
network.direction
The direction of the network connection involved in the finding.
service.action
.networkConnectionAction.localIpDetails
.ipAddressV4
principal.ip
The local IP address involved in the network connection.
service.action
.networkConnectionAction.localPortDetails
.port
principal.port
The local port involved in the network connection.
service.action
.networkConnectionAction.localPortDetails
.portName
principal.application
The name of the local port involved in the network connection.
service.action
.networkConnectionAction.protocol
network.ip_protocol
The protocol used for the network connection involved in the finding.
service.action
.networkConnectionAction.remoteIpDetails
.city.cityName
target.location.city
The city name associated with the remote IP address involved in the network connection.
service.action
.networkConnectionAction.remoteIpDetails
.country.countryName
target.location.country_or_region
The country name associated with the remote IP address involved in the network connection.
service.action
.networkConnectionAction.remoteIpDetails
.ipAddressV4
target.ip
The remote IP address involved in the network connection.
service.action
.networkConnectionAction.remotePortDetails
.port
target.port
The remote port involved in the network connection.
service.action
.networkConnectionAction.remotePortDetails
.portName
target.application
The name of the remote port involved in the network connection.
service.action
.portProbeAction.blocked
security_result.action
Whether the port probe was blocked.
service.action.portProbeAction
.portProbeDetails
.0.localPortDetails.port
target.port
The local port that was probed.
service.action.portProbeAction
.portProbeDetails
.0.localPortDetails.portName
principal.application
The name of the local port that was probed.
service.action.portProbeAction
.portProbeDetails
.0.remoteIpDetails.city
.cityName
target.location.city
The city name associated with the remote IP address that performed the port probe.
service.action.portProbeAction
.portProbeDetails
.0.remoteIpDetails.country
.countryName
target.location.country_or_region
The country name associated with the remote IP address that performed the port probe.
service.action.portProbeAction
.portProbeDetails
.0.remoteIpDetails.geoLocation
.lat
target.location.region_latitude
The latitude of the remote IP address that performed the port probe.
service.action.portProbeAction
.portProbeDetails
.0.remoteIpDetails.geoLocation
.lon
target.location.region_longitude
The longitude of the remote IP address that performed the port probe.
service.action.portProbeAction
.portProbeDetails
.0.remoteIpDetails.ipAddressV4
target.ip
The remote IP address that performed the port probe.
service.additionalInfo
.portsScannedSample
event.idm.read_only_udm.about.port
A sample of the ports that were scanned.
service.additionalInfo
.recentCredentials
event.idm.read_only_udm.intermediary
A list of recent credentials that were used.
service.additionalInfo.sample
security_result.about
.labels.value
Indicates whether the finding is a sample finding.
service.additionalInfo.threatListName
security_result.threat_feed_name
The name of the threat list that triggered the finding.
service.additionalInfo.threatName
security_result.threat_name
The name of the threat that triggered the finding.
service.additionalInfo
.userAgent.fullUserAgent
network.http.user_agent
The full user agent string associated with the finding.
service.additionalInfo
.userAgent.userAgentCategory
security_result.detection_fields
.value
The category of the user agent associated with the finding.
service.additionalInfo.value
security_result.about
.resource.attribute.labels.value
Additional information about the finding.
service.archived
event.idm.read_only_udm
.additional.fields.value.bool_value
Whether the finding is archived.
service.count
event.idm.read_only_udm
.principal.resource.attribute.labels.value
The number of times the event occurred.
service.detectorId
event.idm.read_only_udm
.additional.fields.value.string_value
The ID of the GuardDuty detector that generated the finding.
service.ebsVolumeScanDetails
.scanDetections
.threatDetectedByName.itemCount
The total number of threats detected during the EBS volume scan.
Need more help?
Get answers from Community members and Google SecOps professionals.
