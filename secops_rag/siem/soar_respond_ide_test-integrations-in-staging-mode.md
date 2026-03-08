# Test integrations in staging mode

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/test-integrations-in-staging-mode/  
**Scraped:** 2026-03-05T09:35:28.991888Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Test integrations in staging mode
Supported in:
Google secops
SOAR
This document outlines the best practices for managing response integrations in Content Hub.
When updates are available and to prevent disruptions, we recommend that you first download and test updates in your Integrated Development Environment (IDE) staging mode before you deploy to production.
Staging
mode offers all the basic features of the production default mode
of the IDE. For details on all available features, refer to
Use the IDE
.
Before you begin
Make sure you have
All Environments
selected in your permission group,
For more information, see
Work with permission groups
.
Use the IDE in staging mode
The IDE contains two modes:
Production (default mode)
Staging
Add an integration
These are the ways you can add an integration to the staging mode:
Install
an integration from the
Content Hub
.
Push
an integration from production to staging mode.
Import
an integration.
Install the integration from the Content Hub
To install the integration from the Content Hub, follow these steps:
In the main menu, click
Response
>
IDE
.
Click the toggle from
Production
mode to
Staging
mode to turn on staging mode.
Click
Confirm
on the warning message.
Click
list
Menu
and select
Install from Marketplace (Content Hub)
.
Choose an integration and click
Install
.
Push the integration from Production to Staging
Pushing the integration to
Staging
mode creates a copy of the production integration, 
including its version number and all its certified and custom items, in the staging environment.
To push the integration into
Staging
mode, follow these steps:
In the IDE, locate the required integration.
Click
more_vert
More
>
Push to staging
.
Click the toggle from
Production
mode to
Staging
mode; you can now
work with this integration in
Staging
mode.
Import an integration or integration items
You can import an entire package or specific integration items directly into
the
Staging
mode. To do this, follow these steps:
Click
list
Menu
and select one of these options:
Import Package
Import Items
. To import individual items, you first must select the integration to import them into.
Locate the package or items you want to import.
Click
Import
.
Configure the integration instance
Before you can perform any tests on the integration, you first must create an
instance for each integration in
Staging
mode.
The integration instance is a specific staging instance and won't appear in the
Integration Configuration
page.
To configure an instance, follow these steps:
In the IDE staging mode, locate the required integration. A yellow triangle by this
integration indicates that you need to configure a staging instance.
Click
more_vert
More
>
settings
Configure instance
.
In the
Configure Instance
dialog, enter the following information:
API Root
: The base URL for the service you're connecting to.
API Secret
: A confidential key used to authenticate your application with the service.
Click
Save
.
Update the integration in IDE staging mode
When an update is available for an integration, an
Update
icon appears. You can see the version numbers for both the staging and production integrations by hovering over their icons.
On the integration, click
more_vert
More
>
Upgrade Integration
. This upgrades the integration to the latest version.
Click
Save
.
Review the update and click
Confirm
on the override message that
describes the items affected by the upgrade.
Delete an integration
Deleting an integration in the
Staging
mode also deletes the integration and the instance.
To delete an integration, follow these steps:
On the selected integration, click
more_vert
More
>
Delete
.
Click
Confirm
.
Push an integration from Staging to Production
Once you've finished testing or upgrading the integration in
Staging
mode, you can push it to
Production
mode to replace the live version. We recommend that you
test an integration in
Testing
first.
To push an integration from
Staging
into
Production
, follow these steps:
On the selected integration, click
more_vert
More
>
Push to production
.
Review the warning prompt and click
Confirm
.
Click the toggle from
Staging
mode to
Production
mode. The integration now exists
in both modes.
Need more help?
Get answers from Community members and Google SecOps professionals.
