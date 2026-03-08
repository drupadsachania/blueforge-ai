# Redeploy Remote Agents

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/redeploy-agent/  
**Scraped:** 2026-03-05T09:36:11.767101Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Redeploy Remote Agents
Supported in:
Google secops
SOAR
You can redeploy a Remote Agent to copy all the integrations and connectors
from one agent to another. For example, if you need to change your agent from an installer to a Docker image.
To redeploy the agent, Google recommends to create a new agent and then redeploy from an existing agent.
On the
Remote Agents
page, create a new Remote Agent and make sure it's live.
For more information on creating new agents, see:
Create agent with installer using RHEL
Create agent with installer using CentOS
Create agent with Docker
Click
Redeploy
.
Select the source agent and the destination agent. A list of the integrations
and connectors appears.
Click
Redeploy
. After the successful redeployment, a small
Details
box appears next to the Remote Agent.
Click
Details
to view the redeployment details including the list of
integrations and connectors.
Need more help?
Get answers from Community members and Google SecOps professionals.
