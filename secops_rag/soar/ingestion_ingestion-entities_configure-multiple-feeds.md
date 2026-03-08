# Configure feeds by product

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/configure-multiple-feeds/  
**Scraped:** 2026-03-05T09:47:32.554711Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure feeds by product
Supported in:
Google secops
SIEM
Before you begin
If you are using IAM custom roles, you need to do the following:
Go to
IAM & Admin
>
Roles
.
Select the existing custom role and click
Edit Role
.
Click
Add permissions
.
Enter the following:
chronicle.feedPacks.get
chronicle.feedPacks.list
Click
Save
.
Configure log feeds
To enable effective threat detection and investigation, Google Security Operations relies on structured log ingestion. Properly configuring log feeds makes sure that relevant data is normalized and made available for correlation, alerting, and analysis.
This document explains how to set up and manage log feeds within Google SecOps.
You can configure multiple feeds per product family according to the log type. 
Log types identified by Google as a baseline, are marked as
required
.
The platform provides setup instructions, required procedures, 
and explanations of configuration parameters. 
Some parameters are predefined to simplify the configuration process. 
For example, you can create multiple feeds under both required and optional log types 
within a product, such as CrowdStrike Falcon:
Access the multiple feeds configuration page
There are two ways to reach the multiple feeds configuration screen:
Content Hub
>
Content Packs
Settings
>
Feeds
Configure the feed for CrowdStrike EDR
Follow these steps to configure a log feed for CrowdStrike EDR.
From
Settings
>
Feeds
, click
Add New Feed
Click the
CrowdStrike Falcon
product:.
Select
CrowdStrike EDR
log type.
Alternatively, from
Content Hub
>
Content Packs
, click the
CrowdStrike Falcon
product:
Click
Get Started
.
Select
CrowdStrike EDR
log type.
Specify values for the following fields:
Field
Description
Source Type
Amazon SQS
Region
The AWS S3 region associated with the URI.
Queue Name
The SQS queue name to read from.
Account Number
The SQS account number.
Source Deletion Option
Indicates whether to delete files and directories after the transfer.
Queue Access Key ID
A 20-character alphanumeric access key for the account, such as
AKIAOSFOODNN7EXAMPLE
.
Queue Secret Access Key
A 40-character alphanumeric secret access key for the account, such as,
wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
.
Optional: Configure the following parameters:
Feed Name: prepopulated unique name for the feed.
Asset namespace: namespace associated with the feed.
Ingestion labels: labels applied to the events from this feed.
Click
Create Feed
.
You can repeat this process to create additional feeds for the same log type. You can also configure feeds for other available log types directly from this page. When finished, go to the
Feed Management
page to view a detailed summary of all configured log types.
Need more help?
Get answers from Community members and Google SecOps professionals.
