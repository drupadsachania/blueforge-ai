# Set up integrations, connectors, and jobs

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/set-up-integrations-and-connectors/  
**Scraped:** 2026-03-05T10:09:24.069153Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set up integrations, connectors, and jobs
Supported in:
Google secops
SOAR
This document provides the procedures necessary to configure Google Security Operations
components to run remotely using the deployed Remote Agent. After the Remote Agent
is created, you must explicitly configure integrations, connectors, and jobs to use the new remote infrastructure.
Set up integrations
Configure integrations to let manual and Playbook actions run on cases to execute remotely:
Go to the Content Hub.
Select the required environment.
Select the required integration and click
Configure Integration
.
Select
Run Remotely
and click
Save
.
You can run actions from this environment remotely, including manual and playbook actions.
Set up connectors
You can assign any number of connectors to a Remote Agent:
Go to
SOAR Settings
>
Ingestion
>
Connectors
.
Click
add
Create New Connector
.
Select
Remote Connector
.
Click
Create
.
Select the required environment.
Select the required Remote Agent. The Remote Agent's status appears on the top of the page.
Set up jobs
Before you set up jobs to run on the Remote Agents, complete these prerequisites:
Go to the
Integrations Setup
page.
Create a new instance configured to run remotely with this Remote Agent.
Go to the
Permissions Groups
page and make sure you have the required
  permissions for the
Jobs Scheduler
page and for
Remote Agents
.
Configure a remote job
Go to
Response
>
Jobs Scheduler
.
Click
add
Create New Job
.
Select
Remote Job
.
Click
Create
.
From the menu, select the required Remote Agent. Only agents configured with a remote instance will be available.
Jobs can access information in all environments.
Jobs can access information in all environments.
Need more help?
Get answers from Community members and Google SecOps professionals.
