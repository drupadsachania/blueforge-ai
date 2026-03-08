# Collect Lacework Cloud Security logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/lacework/  
**Scraped:** 2026-03-05T09:57:38.469678Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Lacework Cloud Security logs
Supported in:
Google secops
SIEM
Overview
This parser extracts fields from Lacework Cloud Security JSON logs, transforming them into UDM format. It maps raw log fields to UDM fields, handling various data types and enriching the event with additional context from tags, ultimately classifying the event type based on the presence of principal and target information.
Before you begin
Ensure that you have the following prerequisites:
Google Security Operations instance.
Privileged access to FortiCNAPP Lacework.
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
In the
Feed name
field, enter a name for the feed (for example,
Lacework Logs
).
Select
Webhook
as the
Source type
.
Select
Lacework
as the
Log type
.
Click
Next
.
Optional: Specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
From the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. You need to specify this endpoint URL in your client application.
Click
Done
.
Create an API key for the webhook feed
Go to
Google Cloud console
>
Credentials
.
Go to Credentials
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Chronicle API
.
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL.
If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google SecOps.
SECRET
: the secret key that you generated to authenticate the feed.
Configure a Lacework Webhook for Google SecOps
Sign in to the Lacework FortiCNAPP Console with administrative privileges.
Go to
Settings
>
Notifications
>
Alert channels
.
Click
+ Add new
.
Select
Webhook
.
Click
Next
.
Specify a unique name to the channel (for example,
Google SecOps
).
Webhook URL
: enter the
<ENDPOINT_URL>
followed by
<API_KEY>
and
<SECRET>
.
Click
Save
.
Select
Alert rules
and configure your required alert routing details.
Supported Lacework Cloud Security Sample Logs
Agent or Machine Information (Host Inventory)
{
"AGENT_VERSION"
:
"6.7.6-4ce73a7b"
,
"CREATED_TIME"
:
"Thu, 03 Nov 2022 02:09:36 -0700"
,
"HOSTNAME"
:
"host-agent-1"
,
"IP_ADDR"
:
"10.0.0.1"
,
"LAST_UPDATE"
:
"Wed, 18 Oct 2023 17:59:09 -0700"
,
"MID"
:
6516601498285932156
,
"MODE"
:
"ebpf"
,
"OS"
:
"Linux"
,
"STATUS"
:
"ACTIVE"
,
"TAGS"
:
{
"Account"
:
"999999999999"
,
"AmiId"
:
"ami-00000000000000000"
,
"ExternalIp"
:
"203.0.113.10"
,
"Hostname"
:
"internal-host-1.zone.compute.internal"
,
"InstanceId"
:
"i-00000000000000000"
,
"InternalIp"
:
"172.16.1.10"
,
"LwTokenShort"
:
"DUMMYTOKENABCD123456"
,
"Name"
:
"proxy-DMZ-app-1"
,
"ResourceType"
:
"proxy-machines"
,
"SubnetId"
:
"subnet-00000000000000000"
,
"VmInstanceType"
:
"t3.small"
,
"VmProvider"
:
"AWS"
,
"VpcId"
:
"vpc-00000000000000000"
,
"Zone"
:
"us-west-2a"
,
"arch"
:
"amd64"
,
"falconx.io/application"
:
"proxy-machines"
,
"falconx.io/environment"
:
"prod"
,
"falconx.io/project"
:
"edge"
,
"falconx.io/team"
:
"edge"
,
"os"
:
"linux"
}
}
File Metadata or Integrity
{
"CREATED_TIME"
:
"Wed, 18 Oct 2023 17:02:01 -0700"
,
"FILEDATA_HASH"
:
"DUMMYHASH582C741AD91CA817B4718DEAA4E8A83C0B9D92E2"
,
"FILE_PATH"
:
"/usr/local/bin/secure_config"
,
"MID"
:
7371220731851617371
,
"MTIME"
:
"Fri, 25 Aug 2023 13:03:09 -0700"
,
"SIZE"
:
8078
}
Host Vulnerability Assessment
{
"CVE_PROPS"
:
{
"description"
:
"DOCUMENTATION: The MITRE CVE dictionary describes this issue as: "
"This CVE ID has been rejected or withdrawn by its CVE Numbering "
"Authority for the following reason: This CVE ID has been rejected "
"or withdrawn by its CVE Numbering Authority."
,
"link"
:
"https://vendor.example.com/security/cve/CVE-2021-47472"
,
"metadata"
:
null
},
"CVE_RISK_INFO"
:
{
"HOST_COUNT"
:
1249
,
"IMAGE_COUNT"
:
0
,
"PKG_COUNT"
:
0
,
"SEVERITY_LEVEL"
:
2
,
"score"
:
0.5154245281584533
},
"CVE_RISK_SCORE"
:
3.77
,
"END_TIME"
:
"2024-09-04 07:00:00.000"
,
"EVAL_CTX"
:
{
"collector_type"
:
"Agent"
,
"exception_props"
:
[],
"hostname"
:
"vuln-host-1.example.net"
},
"EVAL_GUID"
:
"3dc61df780e3b722aa59b0ffcac85683"
,
"FEATURE_KEY"
:
{
"name"
:
"kernel-headers"
,
"namespace"
:
"centos:7"
,
"package_active"
:
1
,
"package_path"
:
""
,
"version_installed"
:
"0:3.10.0-1160.119.1.el7.tuxcare.els2"
},
"MACHINE_TAGS"
:
{
"Account"
:
"999999999999"
,
"AmiId"
:
"ami-00000000000000000"
,
"ExternalIp"
:
"203.0.113.10"
,
"Hostname"
:
"ip-172-16-1-10.example-prod.aws.featurespace.net"
,
"InternalIp"
:
"10.0.0.1"
,
"LwTokenShort"
:
"DUMMYTOKENABCD123456"
,
"VmProvider"
:
"AWS"
,
"VpcId"
:
"vpc-00000000000000000"
,
"os"
:
"linux"
},
"MID"
:
5746003737030963813
,
"PACKAGE_STATUS"
:
"ACTIVE"
,
"REGION"
:
"eu-west-2"
,
"RISK_SCORE"
:
10
,
"SEVERITY"
:
"Low"
,
"START_TIME"
:
"2024-09-04 06:00:00.000"
,
"STATUS"
:
"Exception"
,
"VULN_ID"
:
"CVE-2021-47472"
}
Cloud Configuration Compliance (Audit)
{
"ACCOUNT"
:
{
"AccountId"
:
"999999999999"
,
"Account_Alias"
:
""
},
"EVAL_TYPE"
:
"LW_SA"
,
"ID"
:
"lacework-global-87"
,
"REASON"
:
"Default security group does not restrict traffic"
,
"RECOMMENDATION"
:
"Ensure the default security group of every Virtual Private Cloud (VPC) restricts all traffic"
,
"REGION"
:
"eu-north-1"
,
"REPORT_TIME"
:
"2024-11-10 18:00:00.000"
,
"RESOURCE_ID"
:
"arn:aws:ec2:eu-west-1:999999999999:security-group/sg-00000000000000000"
,
"SECTION"
:
""
,
"SEVERITY"
:
"High"
,
"STATUS"
:
"NonCompliant"
}
DNS Query or Resolution
{
"CREATED_TIME"
:
"2024-11-06 05:14:44.329"
,
"DNS_SERVER_IP"
:
"10.0.0.53"
,
"FQDN"
:
"data-service-prod-1234567890.s3.eu-west-2.amazonaws.com"
,
"HOST_IP_ADDR"
:
"172.16.1.20"
,
"MID"
:
8843985456817096491
,
"TTL"
:
5
}
Image Vulnerability Assessment
{
"CVE_PROPS"
:
null
,
"EVAL_CTX"
:
{
"collector_type"
:
"Agentless"
,
"image_info"
:
{
"digest"
:
"sha256:52d5cb782dad7a8a03c8bd1b285bbd32bdbfa8fcc435614bb1e6ceefcf26ae1d"
,
"id"
:
"sha256:31427c44cac7ab632d541181073bbd46a964e4ed38d087d8a47f60bb66eef4df"
,
"registry"
:
"999999999999.dkr.ecr.eu-west-1.amazonaws.com"
,
"repo"
:
"amazon/aws-network-policy-agent"
}
},
"EVAL_GUID"
:
"3a17a74f0a65eed2bddd2d37bb02e6af"
,
"FEATURE_KEY"
:
{
"name"
:
"perl-threads"
,
"namespace"
:
"amzn:2"
,
"version"
:
"1.87-4.amzn2.0.2"
},
"FIX_INFO"
:
{
"fix_available"
:
0
,
"fixed_version"
:
""
},
"IMAGE_ID"
:
"sha256:31427c44cac7ab632d541181073bbd46a964e4ed38d087d8a47f60bb66eef4df"
,
"IMAGE_RISK_INFO"
:
{
"factors"
:
[
"cve"
,
"reachability"
],
"factors_breakdown"
:
{
"cve_counts"
:
{
"Critical"
:
0
,
"High"
:
21
,
"Medium"
:
73
},
"internet_reachability"
:
"Unknown"
}
},
"IMAGE_RISK_SCORE"
:
6.4
,
"PACKAGE_STATUS"
:
"NO_AGENT_AVAILABLE"
,
"RISK_SCORE"
:
6.4
,
"START_TIME"
:
"2024-11-05 19:05:03.553"
,
"STATUS"
:
"GOOD"
}
Network Traffic or Connection Summary
{
"DST_ENTITY_ID"
:
{
"hostname"
:
"service-A.region.amazonaws.com"
,
"ip_internal"
:
0
,
"port"
:
443
,
"protocol"
:
"TCP"
},
"DST_ENTITY_TYPE"
:
"DnsSep"
,
"DST_IN_BYTES"
:
0
,
"DST_OUT_BYTES"
:
0
,
"ENDPOINT_DETAILS"
:
[
{
"dst_ip_addr"
:
"203.0.113.10"
,
"dst_port"
:
443
,
"protocol"
:
"TCP"
,
"src_ip_addr"
:
"192.168.1.10"
},
{
"dst_ip_addr"
:
"198.51.100.5"
,
"dst_port"
:
443
,
"protocol"
:
"TCP"
,
"src_ip_addr"
:
"192.168.1.10"
}
],
"END_TIME"
:
"2024-11-05 21:00:00.000"
,
"NUM_CONNS"
:
4
,
"SRC_ENTITY_ID"
:
{
"mid"
:
2080882850610892909
,
"pid_hash"
:
744766973756676842
},
"SRC_ENTITY_TYPE"
:
"Process"
,
"SRC_IN_BYTES"
:
25028
,
"SRC_OUT_BYTES"
:
11962
,
"START_TIME"
:
"2024-11-05 20:00:00.000"
}
Package Information or Update
{
"ARCH"
:
"x86_64"
,
"CREATED_TIME"
:
"2024-11-08 01:28:30.566"
,
"MID"
:
4172267319977985370
,
"PACKAGE_NAME"
:
"grub2"
,
"VERSION"
:
"2:2.02-0.87.0.2.el7.el7.centos.14.tuxcare.els2"
}
Container Process Activity
{
"CONTAINER_ID"
:
"4853339865add970f72213ec5d76ff51d1308c61a7680cc23c8de20c38c0a8e1"
,
"END_TIME"
:
"2024-11-08 02:00:00.000"
,
"FILE_PATH"
:
"/app/grpc-health-probe"
,
"MID"
:
3708952045169222383
,
"PID"
:
177267
,
"POD_NAME"
:
"kubernetes-pod-abc"
,
"PPID"
:
177257
,
"PROCESS_START_TIME"
:
"2024-11-08 01:43:29.960"
,
"START_TIME"
:
"2024-11-08 01:00:00.000"
,
"UID"
:
0
,
"USERNAME"
:
"serviceuser"
}
General Alert or Event (CloudTrail)
{
"EVENT_ID"
:
"413328"
,
"EVENT_NAME"
:
"Unauthorized API Call"
,
"EVENT_TYPE"
:
"CloudTrailDefaultAlert"
,
"SUMMARY"
:
" For account: 999999999999 (and 22 more) : event Unauthorized API Call from a username other "
"than whitelisted ones. Replaces lacework-global-29 occurred 3772 times by user "
"UDM-PRINCIPAL-ID:UDM-SERVICE-ROLE (and 167 more) "
,
"START_TIME"
:
"07 Feb 2025 12:00 GMT"
,
"EVENT_CATEGORY"
:
"Aws"
,
"LINK"
:
"https://security.example.net/ui/alert/12345/details"
,
"ACCOUNT"
:
"UDM_ACCOUNT"
,
"SOURCE"
:
"CloudTrail"
,
"subject"
:
{
"srcEvent"
:
{
"event"
:
{
"errorCode"
:
"AccessDenied"
,
"errorMessage"
:
"User: arn:aws:sts::999999999999:assumed-role/UDM-SERVICE-ROLE-IngestionApiRole/UDM-SERVICE-PRINCIPAL "
"is not authorized to perform: kinesis:ListShards on resource: "
"arn:aws:kinesis:us-east-1:999999999999:stream/ingestion-qa-rel-fraud-review-Stream "
"because no identity-based policy allows the kinesis:ListShards action"
,
"eventName"
:
"ListShards"
,
"eventSource"
:
"kinesis.amazonaws.com"
,
"eventTime"
:
"2025-02-07T12:00:24Z"
,
"recipientAccountId"
:
"999999999999"
,
"sourceIPAddress"
:
"firehose.amazonaws.com"
,
"userIdentity"
:
{
"accessKeyId"
:
"ACCESSKEYIDDUMMY"
,
"accountId"
:
"999999999999"
,
"arn"
:
"arn:aws:sts::999999999999:assumed-role/UDM-SERVICE-ROLE-IngestionApiRole/UDM-SERVICE-PRINCIPAL"
,
"sessionContext"
:
{
"sessionIssuer"
:
{
"accountId"
:
"999999999999"
,
"arn"
:
"arn:aws:iam::999999999999:role/UDM-SERVICE-ROLE-IngestionApiRole"
,
"principalId"
:
"PRINCIPALIDDUMMY"
,
"userName"
:
"UDM-SERVICE-ROLE-IngestionApiRole"
}
}
},
"vpcEndpointId"
:
"vpce-00000000000000000"
},
"principalId"
:
"PRINCIPALIDDUMMY:UDM-SERVICE-PRINCIPAL"
,
"recipientAccountId"
:
"999999999999"
,
"sourceIPAddress"
:
"firehose.amazonaws.com"
,
"userIdentityName"
:
"UDM-SERVICE-ROLE-IngestionApiRole"
}
}
}
UDM Mapping Table
Log Field
UDM Mapping
Logic
AGENT_VERSION
metadata.product_version
Directly mapped from the
AGENT_VERSION
field.
CREATED_TIME
metadata.event_timestamp
Directly mapped from the
CREATED_TIME
field, converted to a timestamp.
FILEDATA_HASH
target.file.sha256
Directly mapped from the
FILEDATA_HASH
field.
FILE_PATH
target.file.full_path
Directly mapped from the
FILE_PATH
field.
IP_ADDR
principal.ip
Directly mapped from the
IP_ADDR
field.
OS
target.platform
Mapped from the
OS
field.  Logic converts various OS strings (Linux, Windows, Mac) to UDM enum values (LINUX, WINDOWS, MAC). Defaults to UNKNOWN_PLATFORM if no match is found.
STATUS
additional.fields[].key:"STATUS", value.string_value
Directly mapped from the
STATUS
field as an additional field.
TAGS.Account
metadata.product_deployment_id
Directly mapped from the
TAGS.Account
field.
TAGS.AmiId
additional.fields[].key:"AmiId", value.string_value
Directly mapped from the
TAGS.AmiId
field as an additional field.
TAGS.ExternalIp
target.ip
Directly mapped from the
TAGS.ExternalIp
field.
TAGS.Hostname
principal.hostname
Directly mapped from the
TAGS.Hostname
field.
TAGS.InstanceId
target.asset_id
Directly mapped from the
TAGS.InstanceId
field, prefixed with "Device Instance Id: ".
TAGS.LwTokenShort
additional.fields[].key:"LwTokenShort", value.string_value
Directly mapped from the
TAGS.LwTokenShort
field as an additional field.
TAGS.MID
additional.fields[].key:"MID", value.string_value
Directly mapped from the
MID
field as an additional field.
TAGS.MODE
additional.fields[].key:"MODE", value.string_value
Directly mapped from the
MODE
field as an additional field.
TAGS.Name
additional.fields[].key:"Name", value.string_value
Directly mapped from the
TAGS.Name
field as an additional field.
TAGS.QSConfigName-vfzg0
additional.fields[].key:"QSConfigName", value.string_value
Directly mapped from the
TAGS.QSConfigName-vfzg0
field as an additional field.
TAGS.ResourceType
target.resource.resource_subtype
Directly mapped from the
TAGS.ResourceType
field.
TAGS.SubnetId
target.resource.attribute.labels[].key:"Subnet Id", value
Directly mapped from the
TAGS.SubnetId
field as a label within target.resource.attribute.
TAGS.VmInstanceType
target.resource.attribute.labels[].key:"VmInstanceType", value
Directly mapped from the
TAGS.VmInstanceType
field as a label within target.resource.attribute.
TAGS.VmProvider
target.resource.attribute.labels[].key:"VmProvider", value
Directly mapped from the
TAGS.VmProvider
field as a label within target.resource.attribute.
TAGS.VpcId
target.resource.product_object_id
Directly mapped from the
TAGS.VpcId
field.
TAGS.Zone
target.cloud.availability_zone
Directly mapped from the
TAGS.Zone
field.
TAGS.alpha.eksctl.io/nodegroup-name
additional.fields[].key:"eksctl_nodegroup_name", value.string_value
Directly mapped from the
TAGS.alpha.eksctl.io/nodegroup-name
field as an additional field.
TAGS.alpha.eksctl.io/nodegroup-type
additional.fields[].key:"eksctl_nodegroup_type", value.string_value
Directly mapped from the
TAGS.alpha.eksctl.io/nodegroup-type
field as an additional field.
TAGS.arch
principal.platform_version
Directly mapped from the
TAGS.arch
field.
TAGS.aws:autoscaling:groupName
additional.fields[].key:"autoscaling_groupName", value.string_value
Directly mapped from the
TAGS.aws:autoscaling:groupName
field as an additional field.
TAGS.aws:ec2:fleet-id
additional.fields[].key:"ec2_fleetid", value.string_value
Directly mapped from the
TAGS.aws:ec2:fleet-id
field as an additional field.
TAGS.aws:ec2launchtemplate:id
additional.fields[].key:"ec2launchtemplate_id", value.string_value
Directly mapped from the
TAGS.aws:ec2launchtemplate:id
field as an additional field.
TAGS.aws:ec2launchtemplate:version
additional.fields[].key:"ec2launchtemplate_ver", value.string_value
Directly mapped from the
TAGS.aws:ec2launchtemplate:version
field as an additional field.
TAGS.aws:eks:cluster-name
additional.fields[].key:"eks_cluster_name", value.string_value
Directly mapped from the
TAGS.aws:eks:cluster-name
field as an additional field.
TAGS.enableCrowdStrike
additional.fields[].key:"enableCrowdStrike", value.string_value
Directly mapped from the
TAGS.enableCrowdStrike
field as an additional field.
TAGS.falconx.io/application
additional.fields[].key:"io/application", value.string_value
Directly mapped from the
TAGS.falconx.io/application
field as an additional field.
TAGS.falconx.io/environment
additional.fields[].key:"io/environment", value.string_value
Directly mapped from the
TAGS.falconx.io/environment
field as an additional field.
TAGS.falconx.io/managedBy
additional.fields[].key:"io/managedBy", value.string_value
Directly mapped from the
TAGS.falconx.io/managedBy
field as an additional field.
TAGS.falconx.io/project
additional.fields[].key:"io/project", value.string_value
Directly mapped from the
TAGS.falconx.io/project
field as an additional field.
TAGS.falconx.io/proxy-type
additional.fields[].key:"io/proxy_type", value.string_value
Directly mapped from the
TAGS.falconx.io/proxy-type
field as an additional field.
TAGS.falconx.io/service
additional.fields[].key:"io/service", value.string_value
Directly mapped from the
TAGS.falconx.io/service
field as an additional field.
TAGS.falconx.io/team
additional.fields[].key:"io/team", value.string_value
Directly mapped from the
TAGS.falconx.io/team
field as an additional field.
TAGS.k8s.io/cluster-autoscaler/enabled
additional.fields[].key:"k8s_autoscaler_enabled", value.string_value
Directly mapped from the
TAGS.k8s.io/cluster-autoscaler/enabled
field as an additional field.
TAGS.k8s.io/cluster-autoscaler/falcon
additional.fields[].key:"k8s_cluster_autoscaler", value.string_value
Directly mapped from the
TAGS.k8s.io/cluster-autoscaler/falcon
field as an additional field.
TAGS.kubernetes.io/cluster/falcon
additional.fields[].key:"kubernetes_io_cluster", value.string_value
Directly mapped from the
TAGS.kubernetes.io/cluster/falcon
field as an additional field.
TAGS.lw_KubernetesCluster
additional.fields[].key:"lw_KubernetesCluster", value.string_value
Directly mapped from the
TAGS.lw_KubernetesCluster
field as an additional field.
LAST_UPDATE
additional.fields[].key:"LAST_UPDATE", value.string_value
Directly mapped from the
LAST_UPDATE
field as an additional field. Hardcoded to "LACEWORK". Hardcoded to "Lacework Cloud Security".
metadata.event_type
metadata.event_type
Determined by logic. Set to "NETWORK_CONNECTION" if both principal.ip and target.ip are present, "STATUS_UPDATE" if only principal.ip is present, and "GENERIC_EVENT" otherwise.
Need more help?
Get answers from Community members and Google SecOps professionals.
