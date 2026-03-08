# Google SecOps Content Hub overview

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/content_hub/  
**Scraped:** 2026-03-05T09:36:50.155292Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Google SecOps Content Hub overview
Supported in:
Google secops
Permissions for Content Hub
To access modules within Content Hub, you must configure permissions in the 
IAM module.
IAM permission name
Display name
Role in IAM
chronicle.googleapis.com/featuredContentSearchQueries.get
Get Search Query Content
chronicle.reader
chronicle.googleapis.com/featuredContentSearchQueries.list
List Search Query Contents
chronicle.reader
chronicle.googleapis.com/featuredContentSearchQueries.install
Install Search Query Content
chronicle.writer
chronicle.googleapis.com/featuredContentRules.list
List Featured Content Rules
chronicle.reader
chronicle.googleapis.com/featuredContentNativeDashboards.get
Get Dashboard Content
chronicle.reader
chronicle.googleapis.com/featuredContentNativeDashboards.list
List Dashboard Contents
chronicle.reader
chronicle.googleapis.com/featuredContentNativeDashboards.install
Install Dashboard Content
chronicle.writer
chronicle.googleapis.com/feedPacks.get
Get feed packs
chronicle.reader
chronicle.googleapis.com/feedPacks.list
List feed packs
chronicle.reader
chronicle.googleapis.com/featuredContentPlaybooks.get
Get Featured Content Playbook
chronicle.reader
chronicle.googleapis.com/featuredContentPlaybooks.list
List Featured Content Playbook
chronicle.reader
chronicle.googleapis.com/featuredContentPlaybooks.install
Install Featured Content Playbook
chronicle.writer
Overview
The Content Hub serves as a centralized platform for discovering, deploying, and managing content within Google SecOps.
From the Content Hub, you can do the following:
Deploy end-to-end content packs (including log ingestion, curated detections and dashboards) to enable your Google SecOps 
instance to work with products from the top supported list that we have defined.
Install third-party integrations for SOAR playbooks and connectors.
View and filter curated detections, inspect individual rule attributes 
and respective rule definitions (curated detections transparency). Navigate to the 
Rule Set page for full management capabilities.
Add dashboards to enhance your visibility.
Add saved search queries to SIEM search for quick reuse.
Install and run Power Ups to extend playbook capabilities.
Install and run playbooks to provide SOAR responses.
Access legacy SOAR use cases on the
Home
page.
What can I do on the Home page?
The
Home
page is the main landing page for the Content Hub. From here, you can access the following:
Content Packs, response integrations, dashboards, search queries, Power Ups, and curated detections.
Legacy SOAR use cases. Google recommends using the new Content Packs instead of the legacy use cases
because they offer more comprehesive and integrated solutions.
What can I do on the Content Packs page?
On the
Content Packs
page, you can configure single and multiple feeds, 
and access all other Content Hub options.
To onboard all data on the
Content Packs
page, follow these steps:
Configure multiple feeds for product families
based on the log type you need.
After you set up the feed, you can optionally configure the remaining components of the Content Pack (automatically downloaded in the background).
Before you can use any playbook, you must click
Configure Integrations
and set up an instance in order for the playbooks to work. For more 
information, see
Configure integration instances
.
To view or make changes to the downloaded playbook or run it using the simulator, click
View Playbooks
. For more information, see
Working with the playbook simulator
.
You need to copy the playbook name and search for it in the Default folder in the
Playbooks
page.
Click
See all Detection Rules
to open the
Curated Detections
page.
Click
See all Search Queries
to open the
SIEM Search
page.
Click
See all Dashboards
to open the
Dashboards
page.
What can I do on the Curated Detections page?
On the
Curated Detections
page, you can view all supported detection rule definitions in Google SecOps, including rule logic and code.
To view and modify curated detections (rules), do the following:
Find the required rule set you want to update and click
View & Manage
.
In the side bar that opens on the
Overview
tab, click
Manage Rule
. You'll be directed to the 
entire rule set on the
Curated Detections
page.
Alternatively, in the side bar that opens, click the tab that says
Rule Definition
.
This displays the rule logic. You cannot modify the rule from here, but you can create 
a new rule in the
Rules
page. Click
View Rule Performance
to pivot to the
Detections
page to manage the rule.
What can I do on the Response Integrations page?
On the
Response Integrations
page, you can view
integration details
, including Release Notes,
and configure the individual response integrations. These can be used for SOAR connectors and for playbooks.
You can also
roll back an integration to a previous version
if an update causes issues or if you need to revert custom code changes.
To install and configure an integration:
Find the required integration and click
Install
.
After successful installation, click
Configure
on the same integration to begin the setup.
For more information, see
Configure integration instances
.
What can I do on the Dashboards page?
On the
Dashboards
page, you can view details of pre-installed dashboards and add new dashboards. To view or manage any dashboard, pre-installed or added from the Content Hub, go to the
Dashboards
page. Note: Dashboards added through the Content Hub are labeled as
Marketplace
.
What can I do on the Playbooks and Blocks page?
On the
Playbooks and Blocks
page, you can view and install both playbooks and playbook blocks (nested playbooks). 
You can display playbooks according to various filters and categories. For example, you can display only playbooks that contain integrations you have installed on your instance already, or you can choose to only display playbooks with specific integrations.
To view and install a playbook or playbook block:
Find the required playbook or block and click
View Details
.
In the side drawer that opens, look through the information and click
Add
.
Select the environment on which to add the playbook or block to.
Click the link to be redirected to the Playbook designer page with the playbook you just added on display. 
You can add the same playbook multiple times. Each playbook will be titled with an ascending number.
For more information, see the
Playbooks
page.
What can I do on the Search Queries page?
On the
Search Queries
page, you can view search query details and add new queries. Once
you add a search query, it is added to the saved searches and shared within the instance. To view or manage saved queries, go to the
SIEM Search
page.
What can I do on the Power Ups page?
On the
Power Ups
page, you can view details, install, and configure Google SecOps Power Ups for use in playbooks.
For setup instructions, see
Use Power Ups
.
Need more help?
Get answers from Community members and Google SecOps professionals.
