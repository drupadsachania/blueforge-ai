# Remote Agent overview

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/what-is-a-remote-agent/  
**Scraped:** 2026-03-05T09:35:49.440914Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Remote Agent overview
Supported in:
Google secops
SOAR
The Remote agent securely connects a cloud Google Security Operations
  instance to remote sites. This provides Managed Security Service Provider (MSSP) and enterprise SOC
  with the following capabilities:
Execute actions and playbooks on remote sites directly from Google SecOps.
Pull alerts and security data from remote sites with remote connectors.
Connect to remote networks to pull data for incident response purposes.
Infrastructure
The Remote Agent infrastructure consists of the following two main components:
Google SecOps platform
: Deploy Google SecOps
platform to consolidate all security alerts in one place, and orchestrate security
and network products with automated workflows.
Google SecOps agent
: Deploy a Remote Agent on the remote
site. The agent pulls new tasks from Google SecOps, executes remotely
(on the remote or separate network) and updates Google SecOps with
the results.
Agent notifications
Agent notifications, such as alerts for new agent versions and agent
downtime, are enabled by default. Notifications for agent downtime trigger
when a Remote Agent has been down for more than 90 seconds. You can opt out of
these notifications at any time from your user preferences.
For more information about downtime notifications and high availability, see
Deploy high availability in Remote Agents
.
Opt out of notifications
To opt out of notifications, follow these steps:
Click your user avatar
>
User Preferences
.
Click
Notifications
.
Optional: Clear the
Remote Agent
checkbox to stop receiving notification alerts.
Need more help?
Get answers from Community members and Google SecOps professionals.
