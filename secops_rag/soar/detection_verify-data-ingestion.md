# Verify data ingestion using test rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/verify-data-ingestion/  
**Scraped:** 2026-03-05T10:04:47.896128Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Verify data ingestion using test rules
Supported in:
Google secops
SIEM
Google Security Operations curated detections include a set of test rule sets that help you
verify that data required for each rule set is in the correct format.
These test rules are under the
Managed Detection Testing
category. Each rule set
validates that data received by the test device is in a format expected by rules
for that specified category.
Rule set name
Description
Google Cloud Managed Detection Testing
Verifies that Google Cloud data is successfully ingested from devices supported by the Cloud Threats category.
See
Verify Google Cloud data ingestion for Cloud Threats category
for more information.
Chrome Enterprise Managed Detection Testing
Verifies that data is successfully ingested from devices supported by the Chrome Enterprise Threats category.
See
Verify data ingestion for Chrome Enterprise Threats category
for more information.
AWS Managed Detection Testing
Verifies that AWS data is successfully ingested from devices supported by the Cloud Threats category.
See
Verify AWS data ingestion for Cloud Threats category
for more information.
Linux Managed Detection Testing
Verifies  that data is successfully ingested from devices supported by the Linux Threats category.
See
Verify data ingestion for Linux Threats category
for more information.
Windows Managed Detection Testing
Verifies that data is successfully ingested from devices supported by the Windows Threats category.
See
Verify data ingestion for Windows Threats category
for more information.
Office 365 Data Detection Testing
Verifies that data is ingested correctly and is in the proper format to use curated detections for Office 365 data.
See
Verify data ingestion for Office 365 category
for more information.
Okta Data Detection Testing
Verifies that data is ingested correctly and is in the proper format to use curated detections for Okta data.
See
Verify data ingestion for Okta Threats category
for more information.
Follow the steps in this document to test and verify that incoming data is ingested
correctly and is in the correct format.
Verify Google Cloud data ingestion for Cloud Threats category
These rules help verify whether log data is being ingested
as expected for Google SecOps Curated Detections.
Use the following rules to test data with the steps that follow:
Cloud Audit Metadata Testing
rule: To trigger this rule, add a unique and
expected Custom Metadata key to any Compute Engine virtual machine that is
sending data to Google SecOps.
Cloud DNS Testing
rule: To trigger this rule, perform a DNS lookup to the
domain (
chronicle.security
) within any virtual machine that has access to the
internet and is sending log data to Google SecOps.
SCC Managed Detection Testing
rules: To trigger these rules, perform multiple
actions in the Google Cloud console.
Cloud Kubernetes Node Testing
rule: To trigger this rule, create a test project
that is sending log data to Google SecOps, and create a unique node pool
in an existing Google Kubernetes Engine cluster.
Step 1. Enable the test rules
Log in to Google SecOps
.
Open the Curated Detections page
.
Click
Rules & Detections
>
Rule Sets
.
Expand the
Managed Detection Testing
section. You may need to scroll the page.
Click
Google Cloud Managed Detection Testing
in the list to open the detail page.
Enable both
Status
and
Alerting
for the
Cloud Managed Detection Testing
rules.
Step 2. Send data for the Cloud Audit Metadata Testing rule
To trigger the test, complete the following steps:
Choose a project within your organization.
Go to
Compute Engine
, and then choose a virtual machine within the project.
Within the virtual machine, click
Edit
, and then perform the following steps under
the
Custom MetaData
section:
Click
Add Item
.
Enter the following information:
Key:
GCTI_ALERT_VALIDATION_TEST_KEY
Value:
works
Click
Save
.
Perform the following steps to verify the alert was triggered:
Log in to Google SecOps
.
Open the Curated Detections page
, and then click
Dashboard
.
Check that the
ur_tst_Google Cloud_Cloud_Audit_Metadata
rule was triggered in the detection list.
Step 3. Send data for
Cloud DNS Testing
rule
Important:
The following steps must be performed as an IAM user in the chosen
project that has access to a Compute Engine virtual machine.
To trigger the test, complete the following steps:
Choose a project within your organization.
Go to Compute Engine, then choose a virtual machine within the project.
If it is a Linux virtual machine, make sure you have Secure Shell (SSH) access.
If it is a Windows virtual machine, make sure you have Remote Desktop Protocol (RDP) access.
Click
SSH (Linux)
or
RDP (Microsoft Windows)
to access the virtual machine.
Send test data using one of the following steps:
Linux virtual machine: After accessing the virtual machine using SSH, run one of these
commands:
nslookup chronicle.security
or
host chronicle.security
If the command fails, install
dnsutils
on the virtual machine using one of the
following commands:
sudo apt-get install dnsutils
(for Debian/Ubuntu)
dnf install bind-utils
(for RedHat/CentOS)
yum install bind-utils
Microsoft Windows virtual machine: After accessing the virtual machine using RDP, go to any installed browser and
browse to
https://chronicle.security
.
Perform the following steps to verify the alert was triggered:
Log in to Google SecOps
.
Open the Curated Detections page
, and then click
Dashboard
.
Check that the
ur_tst_Google Cloud_Cloud_DNS_Test_Rule
rule was triggered in the detection list.
Step 4. Send data for
Cloud Kubernetes Node Testing
rules
Important:
The following steps must be performed as an IAM user in the chosen project that has access to
Google Kubernetes Engine resources. For more detailed information about creating regional clusters and node pools,
see
Create a regional cluster with a single-zone node pool
. These test rules are intended to verify data ingestion from the
KUBERNETES_NODE
log type.
To trigger the test rules, complete the following steps:
Create a project within your organization, named
chronicle-kube-test-project
. This project is used for testing only.
Navigate to the Google Kubernetes Engine page in the Google Cloud console.
Go to the Google Kubernetes Engine page
Click
Create
to create a new regional cluster in the project.
Configure the cluster per your organization requirements.
Click
add_box
Add node pool
.
Name the node pool
kube-node-validation
, and then adjust the pool size to 1 node per zone.
Delete the test resources:
After the
kube-node-validation
node pool has been created, delete the node pool.
Delete the
chronicle-kube-test-project
test project.
Log in to Google SecOps
.
Open the Curated Detections page
, and then click
Dashboard
.
Check that the
tst_Google Cloud_Kubernetes_Node
rule was triggered in the detection list.
Check that the
tst_Google Cloud_Kubernetes_CreateNodePool
rule was triggered in the detection list.
Step 5. Send data for
SCC Managed Detection Testing
rules
The substeps in this step verify that Security Command Center findings, and related data, are ingested correctly and in the expected format.
The
SCC Managed Detection Testing
rule sets under the
Managed Detection Testing
category enable you to verify that data required for the
CDIR SCC Enhanced
rule sets is
sent to Google SecOps and is in the correct format.
Each test rule validates that data is received in a format expected by rules.
You perform actions in your Google Cloud environment to send data that will
generate a Google SecOps alert.
Make sure to complete the following sections of this document required to configure
logging in Google Cloud services, collect Security Command Center Premium findings, and send Security Command Center
findings to Google SecOps:
Required data sets and log types
Enable and configure CDIR SCC Enhanced rule sets
To learn more about the Security Command Center alerts described in this section, see the Security Command Center document
Investigating and Responding to Threats
.
Trigger the CDIR SCC Persistence test rule
To send data that triggers this alert in Google SecOps, perform the following steps:
In the Google Cloud console, create a new VM instance and temporarily
assign the Compute Engine default service account with
Editor
privileges.
You will remove this after the test is complete.
When the new instance is available, assign the
Access Scope
to
Allow
Full Access to all APIs
.
Create a new service account with following information:
Set
Service account name
to
scc-test
.
Set
Service account ID
to
scc-test
.
Optionally, enter a
Description
for the service account.
See the
Create service accounts
document for information about how to create service accounts.
Connect using SSH to the test instance created in the earlier step, and then
execute the following
gcloud
command:
gcloud
projects
add-iam-policy-binding
PROJECT_NAME
--member
=
"serviceAccount:scc-test@
PROJECT_NAME
.iam.gserviceaccount.com"
--role
=
"roles/owner`"
Replace
PROJECT_NAME
with the name of the project where the Compute Engine instance is running and where the
scc-test
account was created.
The
Persistence: IAM Anomalous Grant
Security Command Center alert should fire.
Log in to Google SecOps, and then open the
Alerts & IOCs
page.
You should see a Google SecOps alert titled
Test SCC Alert: IAM Anomalous Grant
given to test account
.
Open the Google Cloud console, and then do the following:
Remove the
scc-test
test account access from IAM and
Admin Console.
Delete the service account using the
Service Accounts
portal.
Delete the VM instance that you just created.
Trigger the CDIR SCC Malware test rule
To send data that triggers this alert in Google SecOps, perform the following steps:
In the Google Cloud console, connect using SSH to any VM instance where
the
curl
command is installed.
Execute the following command:
curl
etd-malware-trigger.goog
After you execute this command, the
Malware: Bad Domain
Security Command Center alert should fire.
Sign in to Google SecOps, and then open the
Alerts & IOCs
page.
Verify that you see a Google SecOps alert titled
Test SCC Alert: Malware Bad Domain
.
Trigger the CDIR SCC Defense Evasion test rule
To send data that triggers this alert in Google SecOps, perform the following steps:
Sign in to Google Cloud console using an account that has access at the
organization level to modify
VPC Service Control Perimeters
.
In the Google Cloud console, go to the
VPC Service Controls
page.
Go to VPC Service Controls
Click
+New Perimeter
and configure the following fields in the
Details
page:
Perimeter Title
:
scc_test_perimeter
.
Perimeter Type
to
Regular perimeter (default)
.
Config Type
to
Enforced
.
In the left navigation, select
3 Restricted Services
.
In the
Specify services to restrict
dialog, select
Google Compute Engine API
, and then click
Add Google Compute Engine API
.
In the left navigation, click
Create Perimeter
.
To modify the perimeter, go to the
VPC Service Perimeters
page.
For more detailed information about how to access this page, see
List and describe service perimeters
.
Select
scc_test_perimeter
, and then select
Edit Perimeter
.
Under
Restricted Services
, click the
Delete
icon to remove the
Google Compute Engine API
service. This should trigger the
Defense
Evasion: Modify VPC Service Control Perimeter
alert in SCC.
Sign in to Google SecOps, and then open the
Alerts & IOCs
page.
Verify that you see a Google SecOps alert titled
Test SCC Alert: Modify VPC Service
Control Test Alert
.
Trigger the CDIR SCC Exfiltration test rule
To send data that triggers this alert in Google SecOps, perform the following steps:
In the Google Cloud console, go to a Google Cloud project, and then open
BigQuery.
Go to BigQuery
Create a CSV file with the following data, and then save it to your home directory:
column1, column2, column3
data1, data2, data3
data4, data5, data6
data7, data8, data9
In the left navigation, choose
Create Dataset
.
Set the following configuration, and then click
Create Dataset
:
Dataset ID
set to
scc_test_dataset
.
Location type
set to
Multi-region
.
Enable Table expiration
: do not select this option.
For more detailed information about creating a dataset, see the BigQuery document
Creating datasets
.
In the left navigation, to the right of
scc_test_dataset
, click the
more_vert
icon, then select
Create Table
.
Create a table and set the following configuration:
Create table from
: set to
Upload
.
Select file
: browse to your home directory and select the CSV file you created earlier.
File format
: set to
CSV
.
Dataset
: set to
css_test_dataset
.
Table type
: set to
Native table
.
Accept the default configuration for all other fields, and then click
Create Table
.
For more detailed information about creating a table, see
Create and use tables
.
In the resources list, select the
css_test_dataset
table, then click
Query
and choose
in New Tab
.
Run the following query:
SELECT
*
FROM
TABLE_NAME
LIMIT
1000
`
Replace
TABLE_NAME
with the fully qualified table name.
After the query executes, click
Save Results
, and then choose
CSV in
Google Drive
. This should trigger the
Exfiltration: BigQuery Exfiltration
to Google Drive
Security Command Center alert. The Security Command Center finding should be sent to Google SecOps
and trigger a Google SecOps alert.
Log in to Google SecOps, and then open the
Alerts & IOCs
page.
Verify that you see a Google SecOps alert titled
Test SCC Alert: BigQuery Exfiltration to
Google Drive
.
Step 6. Disable the test rules
When you are finished, disable the
Google Cloud Managed Detection Testing
rules.
Log in to Google SecOps
.
Open the Curated Detections page
.
Disable both
Status
and
Alerting
for the Google Cloud Managed Detection Testing rules.
Verify data ingestion for Chrome Enterprise Threats category
The Chrome Enterprise Test rule verifies that Chrome Enterprise logging is working correctly
for Google SecOps curated detections. This test uses a
Safe Browsing test URL that should show a phishing warning.
Step 1. Enable the test rules
To enable the test rules, do the following:
Log in to Google SecOps
.
Open the
Curated Detections
page
.
Expand the
Managed Detection Testing
section. You may need to scroll the page.
Click
Chrome Enterprise Managed Detection Testing
in the list to open the detail page.
Enable both
Status
and
Alerting
for the
Chrome Enterprise Managed Detection Testing
rules.
Step 2. Send test data from a managed Chrome browser
To trigger the Chrome Enterprise test rule, do the following:
Open a Chrome browser that's managed by a Chrome Enterprise account.
Open a new tab and go to the
Safe Browsing test URL
;
you should see a warning message.
Close the browser.
Step 3. Verify that an alert was triggered
Confirm that accessing the Safe Browsing test URL triggered the
tst_chrome_enterprise_phishing_url
rule in Google SecOps.
This indicates that Chrome Enterprise logging is sending data, as expected.
To verify the alert in Google SecOps, do the following:
Log in to Google SecOps
.
Open the
Curated Detections
page
.
Click
Dashboard
.
Verify that the
tst_chrome_enterprise_phishing_url
rule was triggered in the detection list.
Step 4. Disable the test rules
When you're finished testing, disable the Chrome Enterprise Managed Detection Testing rules:
Log in to Google SecOps
.
Open the
Curated Detections
page
.
Disable both
Status
and
Alerting
for the Chrome Enterprise Managed
Detection Testing rules.
Verify AWS data ingestion for Cloud Threats category
You can use
AWS Managed Detection Testing
test rules to verify that AWS data
is being ingested to Google SecOps. These test rules help verify that AWS data
was ingested and is in the expected format. After setting up the ingestion of
AWS data, you perform actions in AWS that should trigger the test rules.
The user who enables these rules in Detection Engine must have the
curatedRuleSetDeployments.batchUpdate
IAM permission.
The user who performs the steps to send AWS data must have the AWS IAM
permissions to edit the tags of an EC2 instance in the chosen account. For
more information about tagging EC2 instances, see the AWS document
Tag your Amazon EC2 resources
.
Enable the AWS Managed Detection Testing test rules
In Google SecOps, click
Detections
>
Rules & Detections
to
open the Curated Detections page
.
Select the
Managed Detection Testing
>
AWS Managed Detection Testing
.
Enabled both
Status
and
Alerting
for the
Broad
and
Precise
rules.
Verify that tag actions in AWS trigger the test rule
Perform the following steps to verify that the tag actions in AWS trigger the
rule set.
Step 1. Generate a log event in AWS.
Choose an account within your AWS environment.
Go to the EC2 Dashboard, and then choose an Instance within the account.
Within the EC2 Instance, click
Actions
>
Instance Settings
, and
perform the following under the
Manage Tags
section:
Click
Add new tag
.
Enter the following information:
Key
:
GCTI_ALERT_VALIDATION_TEST_KEY
Value
:
works
Click
Save
.
For more detailed information, see
Add or remove EC2 instance tags
.
Step 2. Verify that the test alerts are triggered.
After performing the task in the previous step, verify that the
AWS CloudTrail Test Rule
rule is triggered. This indicates that CloudTrail logs were recorded
and sent to Google SecOps as expected. Perform the following steps to verify the alert:
In Google SecOps, click
Detections
>
Rules & Detections
to
open the Curated Detections page
.
Click
Dashboard
.
In the list of detections, check that the
tst_AWS_Cloud_Trail_Tag
rule
was triggered.
Verify that AWS GuardDuty sample findings trigger test rules
To ensure GuardDuty alerts will work as intended in your environment, you can
send GuardDuty sample findings to Google SecOps.
Step 1. Generate GuardDuty sample findings data.
Navigate to the AWS Console home.
Under
Security, Identity, and Compliance
, open
GuardDuty
.
Navigate to GuardDuty's
Settings
.
Click
Generate Sample findings
.
For more information about how to generate sample GuardDuty findings, see
Generating sample findings in GuardDuty
.
Step 2. Verify the test alerts were triggered.
In Google SecOps, click
Detection
>
Rules & Detections
to
open the Curated Detections page
.
Click
Dashboard
.
Check that
AWS CloudTrail Test Rule
was triggered in the detection
list.
Disable the AWS Managed Detection Testing rule sets
In Google SecOps, click
Detection
>
Rules & Detections
to
open the Curated Detections page
.
Select the
Managed Detection Testing
>
AWs Managed Detection Testing
rules.
Disable both
Status
and
Alerting
for the
Broad
and
Precise
rules.
Verify data ingestion for Linux Threats category
The
Linux Managed Detection Testing
rules verify that logging on a Linux system is
working correctly for Google SecOps curated detections. The tests involve
using the Bash prompt in a Linux environment to run various commands and can be
performed by any user that has access to the Linux Bash prompt.
Step 1. Enable the test rules
Log in to Google SecOps
.
Open the Curated Detections page
.
Click
Rules & Detections
>
Rule Sets
.
Expand the
Managed Detection Testing
section. You may need to scroll the page.
Click
Linux Managed Detection Testing
in the list to open the detail page.
Enable both
Status
and
Alerting
for the
Linux Managed Detection Testing
rules.
Step 2. Send test data from a Linux device
To trigger the
Linux Managed Detection Testing
test rules, perform the following steps:
Access any Linux device where data is being sent to Google SecOps.
Open a new Linux Bash prompt command line interface as any user.
Enter the following command, and then press
Enter
:
/bin/echo hello_chronicle_world!
Note:
You must use the
echo
binary, rather than the Linux
shell, built-in
echo
command.
Enter the following command, and then press
Enter
:
sudo useradd test_chronicle_account
Remove the test account created in the previous step. Execute the following command:
sudo userdel test_chronicle_account
Enter the following command, and then press
Enter
:
su
When prompted for the password, enter any random string. Notice that the
su: Authentication failure
message is displayed.
Close the Bash window.
Step 3. Verify that alerts were triggered in Google SecOps
Verify that the command triggered the
tst_linux_echo
,
tst_linux_failed_su_login
, and
tst_linux_test_account_creation
rules in
Google SecOps. This indicates that the Linux logs are written and sent as expected.
To verify the alert in Google SecOps, perform the following steps:
Log in to Google SecOps
.
Open the Curated Detections page
.
Click
Dashboard
.
Verify that the
tst_linux_echo
,
tst_linux_failed_su_login
, and
tst_linux_test_account_creation
rules were triggered in the detection list.
Step 4. Disable the test rules
When you're finished, disable the
Linux Managed Detection Testing
rules.
Log in to Google SecOps
.
Open the Curated Detections page
.
Disable both
Status
and
Alerting
for the
Linux Managed Detection Testing
rules.
Verify data ingestion for Windows Threats category
The
Windows Echo Test Rule
verifies that Microsoft Windows logging is working correctly
for Google SecOps curated detections. The test involves using the command prompt
in a Microsoft Windows environment to run the
echo
command with an expected and unique string.
You can run the test while logged on as any user that has access to the Windows Command Prompt.
Step 1. Enable the test rules
Log in to Google SecOps
.
Open the Curated Detections page
.
Expand the
Managed Detection Testing
section. You may need to scroll the page.
Click
Windows Managed Detection Testing
in the list to open the detail page.
Enable both
Status
and
Alerting
for the
Windows Managed Detection Testing
rules.
Step 2. Send test data from a Windows device
To trigger the
Windows Echo Test Rule
, perform the following steps:
Access any device that generates data that is to be sent to Google SecOps.
Open a new Microsoft Windows Command Prompt window as any user.
Enter the following case-insensitive command, and then press
Enter
:
cmd.exe /c "echo hello_chronicle_world!"
Close the Command Prompt window.
Step 3. Verify that an alert was triggered
Verify that the command triggered the
tst_Windows_Echo
rule in Google SecOps.
This indicates that Microsoft Windows logging is sending data as expected.
To verify the alert in Google SecOps, perform the following steps:
Log in to Google SecOps
.
Open the Curated Detections page
.
Click
Dashboard
.
Verify that the
tst_Windows_Echo
rule was triggered in the detection list.
Note:
There will be a slight delay for the alert to display in Google SecOps.
Step 4. Disable the test rules
When you're finished, disable the
Windows Managed Detection Testing
rules.
Log in to Google SecOps
.
Open the Curated Detections page
.
Disable both
Status
and
Alerting
for the
Windows Managed Detection Testing
rules.
Verify data ingestion for the Office 365 data category
Verify that data is ingested correctly and is in the proper format to use curated 
detections for Office 365 data.
Step 1. Ingest Office 365 data
You must ingest data from every data source listed in the Google SecOps 
ingestion instructions to have maximum rule coverage. For more information about 
how to ingest data for Office 365 services,
 see
Collect Microsoft Office 365 logs
.
Step 2. Verify ingestion of Office 365 data
The Google SecOps
Data Ingestion and Health dashboard
lets you see 
information about the type, volume, and health of all data being ingested into
 Google SecOps using SIEM ingestion features.
You can also use Office 365 Managed Detection test rules to verify the 
ingestion of Office 365 data. Once the ingestion is set up, you trigger the test 
rules by performing actions within Office 365. These rules ensure that the data 
is ingested correctly and is in the proper format to use curated detections for 
Office 365 data.
Step 3. Enable the Azure Managed Detection Testing test rules
In Google SecOps, click
Detections
>
Rules & Detections
to
Open the Curated Detections page and rule sets
.
Select
Managed Detection Testing
>
Office 365 Managed Detection Testing
.
Enable both
Status
and
Alerting
for the
Broad
and
Precise
rules.
Step 4. Send user action data to trigger the test rules
To verify that data is ingested as expected, create an inbox rule with a specific 
name to verify that these actions trigger the test rules. For information 
about creating inbox rules in Outlook, see
Manage email messages by using rules in Outlook
.
To create an inbox rule in Outlook 365, you can use the Rules feature in the Mail 
section. You can also create a rule by right-clicking an email.
Step 5. Create an inbox rule using the Rules feature
Here are some use cases for creating an inbox rule using the Rules feature:
Test Rule 1
Click
Mail
and select
Rules
.
Enter
GoogleSecOpsTest
for the rule name.
Select a condition from the list.
Select an action from the list.
Click
Add a condition
or
Add an action
to add additional conditions or actions, as needed.
Click
OK
.
Test Rule 2
Go to SharePoint or OneDrive.
In the search bar, enter
GoogleSecOpsTest
.
Validate results
Do the following to verify that alerts are created in Google SecOps:
In Google SecOps, click
Detections
>
Rules & Detections
to
open the Curated Detections page
.
Click
Dashboard
.
In the list of detections, check that the following rules were triggered:
tst_o365_email.yl2
tst_of65_sharepoint_onedrive.yl2
Once you confirm that the data is sent and the rules are triggered, 
deactivate the inbox rule created in
Test Rule 1
.
Verify data ingestion for the Okta Threat category
Verifies that data is ingested correctly and is in the proper format to use 
curated detections for Okta data.
Step 1. Ingest Okta data
To ensure maximum rule coverage, you must ingest data from every data source
listed in the Google SecOps ingestion instructions. For more 
information about how to ingest data for Okta services, 
see
Collect Okta logs
.
Step 2. Verify ingestion of Okta data
The Google SecOps
Data Ingestion and Health dashboard
lets you see 
information about the type, volume, and health of all data being ingested into
 Google SecOps using SIEM ingestion features.
You can also use Okta Managed Detection test rules to verify the 
ingestion of Office 365 data. Once the ingestion is set up, you trigger the test 
rules by performing actions within Office 365. These rules ensure that the data 
is ingested correctly and is in the proper format to use curated detections for 
Office 365 data.
Step 3. Enable the Okta Managed Detection Testing rules
In Google SecOps, click
Detections
>
Rules & Detections
to
Open the Curated Detections page and rule sets
.
Select
Managed Detection Testing
>
Office 365 Managed Detection Testing
.
Enable both
Status
and
Alerting
for the
Broad
and
Precise
rules.
Step 4. Send user action data to trigger the test rules
To verify that data is ingested as expected, create an inbox rule with a specific 
name to verify that these actions trigger the test rules. This event will then trigger
a failed Okta login event for an unknown user.
Test Rule 1
Access your Okta tenant URL.
In the
Username
field, enter
GoogleSecOpsTest
.
In the
Password
field, enter any string.
Click
Sign In
.
Validate results
Do the following to verify that alerts are created in Google SecOps:
    1. In Google SecOps, click
Detections
>
Rules & Detections
to
open the Curated Detections page
.
    1. Click
Dashboard
.
    1. In the list of detections, check that the following rules were triggered:
        *
Okta Unknown User Login Test (tst_okta_login_by_unknown_user.yl2)
Need more help?
Get answers from Community members and Google SecOps professionals.
