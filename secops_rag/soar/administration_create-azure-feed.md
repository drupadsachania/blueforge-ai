# Create an Azure Event Hub feed

**Source:** https://docs.cloud.google.com/chronicle/docs/administration/create-azure-feed/  
**Scraped:** 2026-03-05T09:47:21.944341Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create an Azure Event Hub feed
Supported in:
Google secops
SIEM
This document shows you how to set up an Azure Event Hub to send security data
to Google Security Operations. You can create up to 10 Azure Event Hub feeds, which 
includes both active and inactive feeds.
To set up an Azure feed, complete the following processes:
Create an event hub in Azure
:
set up the
required infrastructure in your Azure environment to receive and store the
security data stream.
Configure the feed in Google SecOps
:
configure the feed in Google SecOps to connect to your Azure
event hub and to begin ingesting data.
Create an Azure Event Hub
To create an event hub in Azure, do the following:
Create an
event hub namespace and event hub
.
To ensure optimal data ingestion, deploy the Event Hub namespace in the same region
as your Google SecOps instance. Deploying the event hub in a
different region can reduce the throughput ingested into Google SecOps.
Set the partition count to 40 for optimal scaling.
To help prevent data loss due to Google SecOps quota limits, set a
long retention time for your event hub. This ensures that logs aren't
deleted before ingestion resumes after a quota throttle. For more information
about event retention and retention time limitations, see
Event retention
.
For standard tier event hubs, enable
Auto inflate
to automatically scale
throughput as needed. See
Automatically scale up Azure Event Hubs throughput units
for more information.
For basic and standard tiers, one throughput unit (TU) in Azure Event Hub supports
up to 1 MB per second of data ingestion. If the incoming event volume exceeds
the capacity of the configured TUs, data loss may occur. For example, if you
configure 5 TUs, the maximum supported ingestion rate is 5 MB per second. If 
events are sent at 20 MB per second, the Event Hub may crash. As a result, logs may
be lost at the Event Hub level before they reach Google SecOps.
Obtain the event hub connection string
required for
Google SecOps to ingest data from the Azure event hub. This
connection string authorizes Google SecOps to access and collect
security data from your event hub. You have two options for providing a
connection string:
Event hub namespace level
: works for all event
hubs within the namespace. It's a simpler option if you're using multiple
event hubs and want to use the same connection string for all of them in
your feed setup.
Event hub level
: applies to a single event hub.
This is a secure option if you need to grant access to only one event hub.
Ensure that you remove
EntityPath
from the end of the connection string.
For example, change
Endpoint=<ENDPOINT>;SharedAccessKeyName=<KEY_NAME>;SharedAccessKey=<KEY>;EntityPath=<EVENT_HUB_NAME>
to
Endpoint=<ENDPOINT>;SharedAccessKeyName=<KEY_NAME>;SharedAccessKey=<KEY>
.
Configure your applications, such as
Web Application Firewall
or
Microsoft Defender
,
to send their logs to the event hub.
Microsoft Defender users:
When configuring Microsoft Defender streaming,
ensure that you enter your existing event hub name. If you leave this field blank, the
system might create unnecessary event hubs and consume your limited feed quota.
To keep things organized, use event hub names that match the log type.
Configure the Azure feed
To configure the Azure feed in Google SecOps, do the following:
In the Google SecOps menu, select
SIEM Settings
, and then
click
Feeds
.
Click
Add new
.
In the
Feed name
field, enter a name for the feed.
In the
Source type
list, select
Microsoft Azure Event Hub
.
Select the
Log type
. For example, to create a feed for Open Cybersecurity
Schema Framework, select
Open Cybersecurity Schema Framework (OCSF)
as the
Log type
.
Click
Next
. The
Add feed
window appears.
Retrieve the information from the event hub that you created earlier in the
Azure portal to fill in the following fields:
Event hub name
: the event hub name
Event hub consumer group
: the consumer group associated with your
event hub
Event hub connection string
: the event hub connection string
Azure storage connection string
: Optional. The blob storage connection string
Azure storage container name
: Optional. The blob storage container name
Azure SAS token
: Optional. The SAS token
Asset namespace
: Optional. The
asset namespace
Ingestion labels
: Optional. The label to be applied to the events from this feed
Click
Next
. The
Finalize
screen appears.
Review your feed configuration, and then click
Submit
.
Verify data flow
To verify that your data is flowing into Google SecOps and your
event hub is functioning correctly, you can perform these checks:
In Google SecOps, examine the dashboards and use the Raw Log Scan
or Unified Data Model (UDM) search to verify that the ingested data
is present in the correct format.
In the Azure portal, navigate to your event hub's page and inspect the
graphs that display incoming and outgoing bytes. Ensure that the incoming and
outgoing rates are roughly equivalent, indicating that messages are being
processed and there is no backlog.
Need more help?
Get answers from Community members and Google SecOps professionals.
