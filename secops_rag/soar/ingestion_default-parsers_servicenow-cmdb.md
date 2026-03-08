# Collect ServiceNow CMDB data

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/servicenow-cmdb/  
**Scraped:** 2026-03-05T10:00:09.576413Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ServiceNow CMDB data
Supported in:
Google secops
SIEM
This document explains how to collect ServiceNow CMDB data by setting up a Google Security Operations feed using the Third party API.
Before you begin
Ensure that you have the following prerequisites:
A Google SecOps instance
Privileged access to ServiceNow instance with admin console access
ServiceNow user account with
cmdb_read
role (minimum requirement for read access)
REST API enabled in your ServiceNow instance (enabled by default)
Configure IP allowlisting
Before creating the feed, you must allowlist Google SecOps IP ranges in your ServiceNow firewall or network settings.
Get Google SecOps IP ranges
Fetch IP ranges from the
Google IP address ranges JSON file
.
Add IP ranges to ServiceNow
Sign in to your
ServiceNow instance
as an administrator.
Go to
All
>
System Security
>
IP Address Access Control
.
Click
New
.
Provide the following configuration details:
Type
: Select
Allow
.
IP Address
: Enter oneGoogle SecOps IP range in CIDR notation (for example,
192.0.2.0/24
).
Name
: Enter a descriptive name (for example,
GGoogle SecOps IP Range 1
).
Active
: Select the checkbox to enable the rule.
Click
Submit
.
Repeat steps 3-5 for each additional Google SecOps IP range.
Configure ServiceNow API access
To enable Google SecOps to pull CMDB data, you need to create a ServiceNow user with appropriate permissions.
Create dedicated integration user (recommended)
Sign in to the
ServiceNow Admin Console
.
Go to
All
>
User Administration
>
Users
.
Click
New
.
Provide the following configuration details:
User ID
: Enter a descriptive username (for example,
google_secops_integration
).
First name
: Enter
Google
.
Last name
: Enter
SecOps Integration
.
Email
: Enter a valid email address for notifications.
Password
: Click
Set Password
and create a strong password.
Active
: Select the checkbox.
Web service access only
: Select the checkbox (recommended for API-only access).
Click
Submit
.
Assign required permissions
After creating the user, open the user record.
Go to the
Roles
section.
Click
Edit
.
In the
Collection
list, search for and add the following role:
cmdb_read
: Provides read access to CMDB tables.
Click
Save
.
Record API credentials
After creating the user, record the following credentials:
Username
: The User ID you created (for example,
google_secops_integration
)
Password
: The password you set for the user
API Hostname
: Your ServiceNow instance FQDN (for example,
myinstance.servicenow.com
)
Do not include
https://
or any paths.
Do not include trailing slash.
Table Name
: The CMDB table to query (for example,
cmdb_ci
,
cmdb_ci_server
,
cmdb_ci_computer
)
Understanding ServiceNow CMDB tables
The ServiceNow CMDB is organized in a hierarchical structure of tables. The most common tables for asset data ingestion include:
Table Name
Description
Use Case
cmdb_ci
Base Configuration Item table (parent of all CI tables)
All configuration items
cmdb_ci_server
Server configuration items
Physical and virtual servers
cmdb_ci_computer
Computer configuration items
Workstations, laptops, desktops
cmdb_ci_linux_server
Linux server configuration items
Linux servers specifically
cmdb_ci_win_server
Windows server configuration items
Windows servers specifically
cmdb_ci_vm_instance
Virtual machine instances
Virtual machines
cmdb_ci_network_adapter
Network adapters
Network interface cards
cmdb_ci_ip_address
IP addresses
IP address records
cmdb_ci_service
Business services
Service catalog items
cmdb_ci_appl
Applications
Application configuration items
Verify REST API access
Before creating the feed, verify that your ServiceNow API credentials work correctly.
Test using REST API Explorer (optional)
Sign in to your
ServiceNow instance
as the integration user.
Go to
All
>
System Web Services
>
REST
>
REST API Explorer
.
Select
Table API
from the namespace drop-down.
Select
Retrieve records from a table (GET)
.
In
Path Parameters
, enter the table name (for example,
cmdb_ci
).
Click
Send
.
Verify that the response status is
200 OK
and records are returned.
Test using curl (optional)
Alternatively, test the API using curl:
curl
"https://your-instance.service-now.com/api/now/table/cmdb_ci?sysparm_limit=10"
\
--request
GET
\
--header
"Accept: application/json"
\
--user
'your-username'
:
'your-password'
Replace:
your-instance.service-now.com
: Your ServiceNow instance hostname
your-username
: Your integration user username
your-password
: Your integration user password
A successful response will return JSON data with configuration items.
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
ServiceNow CMDB - All CIs
or
ServiceNow CMDB - Servers
).
Select
Third party API
as the
Source type
.
Select
ServiceNow CMDB
as the
Log type
.
Click
Next
.
Specify values for the following input parameters:
Username
: Enter the ServiceNow user ID (for example,
google_secops_integration
).
Secret
: Enter the ServiceNow user password.
Important: This is a sensitive field. The password is encrypted and cannot be viewed after saving.
API Hostname
: Enter the fully qualified domain name of your ServiceNow instance.
Example:
myinstance.servicenow.com
Do not include:
Protocol (
https://
)
Paths (
/api/now/table/
)
Trailing slash
Regional instances:
If your ServiceNow instance is in a specific region, use the correct hostname format:
Standard:
instance.service-now.com
European Union:
instance.service-now.eu
Other regions: Verify with your ServiceNow administrator
Table Name
: Enter the ServiceNow CMDB table to query.
Examples:
cmdb_ci
(all configuration items)
cmdb_ci_server
(all servers)
cmdb_ci_computer
(workstations and computers)
cmdb_ci_linux_server
(Linux servers only)
cmdb_ci_win_server
(Windows servers only)
Note: The table name is case-sensitive and must match exactly. You can query only one table per feed. To ingest multiple tables, create separate feeds for each table.
Asset namespace
: The
asset namespace
.
Ingestion labels
: The label to be applied to the events from this feed.
Click
Next
.
Review your new feed configuration in the
Finalize
screen, and then click
Submit
.
After setup, the feed begins to retrieve CMDB records from the ServiceNow instance. The initial sync may take several minutes depending on the number of records in the table.
Ingesting multiple CMDB tables
To ingest data from multiple CMDB tables, create separate feeds for each table:
Create the first feed using the steps above (for example, for
cmdb_ci_server
).
Click
Add New Feed
to create additional feeds.
Use the same ServiceNow credentials but specify different table names.
Example configuration:
Feed Name
Table Name
Purpose
ServiceNow CMDB - Servers
cmdb_ci_server
All server CIs
ServiceNow CMDB - Computers
cmdb_ci_computer
Workstation CIs
ServiceNow CMDB - Network Adapters
cmdb_ci_network_adapter
Network interface CIs
ServiceNow CMDB - Applications
cmdb_ci_appl
Application CIs
Required API permissions
The integration user requires the following ServiceNow permissions:
Permission/Role
Access Level
Purpose
cmdb_read
Read
Retrieve CMDB configuration item data
Additional roles (optional):
itil
: Required if you need write access to create or update CIs (not required for Google SecOps ingestion)
rest_api_explorer
: Useful for testing API access during setup
UDM mapping table
ServiceNow Field
UDM Mapping
Logic
name
entity.asset.hostname
Primary hostname of the asset
ip_address
entity.asset.ip
Primary IP address of the asset
mac_address
entity.asset.mac
MAC address of the asset
serial_number
entity.asset.hardware.serial_number
Hardware serial number
asset_tag
entity.asset.asset_id
Asset tag or identifier
sys_class_name
entity.asset.asset_type
CI class (server, computer, etc.)
os
entity.asset.platform_software.platform
Operating system
sys_created_on
entity.asset.first_seen_time
Asset creation timestamp
sys_updated_on
entity.asset.last_seen_time
Last update timestamp
location
entity.asset.location.name
Physical location
company
entity.asset.attribute.labels.value
Owning company/organization
Need more help?
Get answers from Community members and Google SecOps professionals.
