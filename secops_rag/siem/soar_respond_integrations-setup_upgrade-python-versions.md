# Upgrade the Python version

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/upgrade-python-versions/  
**Scraped:** 2026-03-05T09:35:26.419453Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Upgrade the Python version
Supported in:
Google secops
SOAR
This document explains how to upgrade certified and custom integrations, remote agents and 
connectors in the Content Hub to the latest Python version. 
As older Python versions are deprecated, integrations using unsupported versions must be updated to facilitate continued operation.
After you update the integration to the latest Python version, you must upgrade each connector as well.
If your certified or custom integration code uses a deprecated Python version, you must manually update it. Use
IDE Staging
mode to update integration code without impacting production environments.
Before you begin
Make sure that your permission group includes
All Environments
access.
For more information, refer to
Work with permission groups
.
Upgrade integrations
Go to
Response
>
IDE
; if any integrations are using outdated Python versions, a banner appears in the IDE, Content Hub, and Playbooks pages.
Click
View Integration
to see a list of integrations.
Click
Close
to dismiss the banner.
In the integrations list, select the integration to upgrade.
Click
more_vert
More
>
Push to staging
. This step creates a copy of the integration for testing.
Click the
Production
toggle from
Production
to
Staging
.
On the same integration, click
more_vert
More
>
Configure instance
.
Continue with either of the following upgrade paths:
Upgrade certified integrations to the latest Python version
Upgrade custom integrations to the latest Python version
For information on how to configure instances,
read
Configure instances
. This creates a staging instance that does not appear in the main configuration list. 
Only one staging instance is allowed per integration.
Make sure to
update each connector as well
.
Upgrade certified integrations to the latest Python version
In
Response
>
IDE
, click
Upgrade
to switch the integration and its dependencies to the latest Python version.
If this integration includes custom elements, update their code accordingly.
In the
Testing
section, enter the required parameters,
including the staging instance that you configured earlier.
Verify that there are no errors in the
Debug Output
.
On the same integration, click
more_vert
More
>
Push to production
.
Click the
Production
toggle back to
Production
mode, if needed.
Upgrade custom integrations to the latest Python version
Follow this procedure to update the
Script Dependencies
in custom integrations.
Click
more_vert
More
>
Configure custom integration
.
In the dialog
Running on Python
field, change the
Running on Python
field to the latest Python version (for example,
Python 3.11
).
Under
Script Dependencies
, copy and save the dependency names locally.
Delete these dependencies from the list, and click
Save
Copy each of the dependency names (without the version or target OS) from your
file to the
Libraries
field and click
Add
. For example, change
requests-2.27.1-none-any.whl
to
requests
and then add it to the
Libraries
field. The platform downloads each dependency with the latest Python version already configured.
Upgrade remote agents
If you're working with Remote Agents, you need to upgrade both the agent and its
integrations, running on them as follows:
Go to
SOAR Settings
>
Advanced
>
Remote Agents
.
Click
Update Available
.
Upgrade the agent using the appropriate method:
Docker: Follow
Perform a major upgrade of a Docker image
.
Red Hat (RHEL): See
Perform a major upgrade using installer for RHEL
.
CentOS: See
Perform a major upgrade using installer for CentOS
.
After upgrading the agent, follow the integration upgrade steps described in this document.
Upgrade connectors
You need to upgrade connectors, both custom and commercial, to the latest Python versions.
Go to
SOAR Settings
>
Ingestion
>
Connectors
.
Click the yellow
Update
button on the top of the screen.
Click
Save
.
Need more help?
Get answers from Community members and Google SecOps professionals.
