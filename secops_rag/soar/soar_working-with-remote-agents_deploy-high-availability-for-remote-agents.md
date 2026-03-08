# Deploy high availability for Remote Agents

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/deploy-high-availability-for-remote-agents/  
**Scraped:** 2026-03-05T10:09:26.599008Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Deploy high availability for Remote Agents
Supported in:
Google secops
SOAR
This document describes how to configure a secondary Remote Agent as a backup
to achieve high availability. By doing so, it eliminates a single point of failure
in your execution environment.
Failover mechanism and configuration
To ensure system resilience, the following rules apply:
Automatic takeover
: If the primary agent becomes unavailable,
  the secondary agent automatically takes over the remote execution of actions,
  jobs, and connectors after a 30-second downtime.
Task failure
: If the primary agent fails during a task
  execution, that specific task fails and must be manually re-run. All other
  pending tasks are immediately routed to the secondary agent.
Set up high availability
Follow these steps to configure a secondary agent for high availability:
Go to
SOAR settings
>
Advanced
>
Remote Agents
.
On the primary agent, click
View more
to view the agent's details.
Click
Add secondary agent
.
To update the primary agent to the latest version, click
Update
If your connectors are an older version, you must deploy them to support high availability.
For more information, see
Redeploy connectors
.
Follow the process to set up a secondary agent (using either manual installation or Docker).
Check the status of the secondary agent on the
Remote Agents
page, under the
High Availability
column.
Operational notes (high availability)
This section details the system's operational behavior following the high availability setup, including the
failover rules for configuration deployment
and the
default notification settings
for agent status and downtime.
Failover and configuration
Primary agent focus
: After setting up high availability, continue to interact and work primarily with the designated Primary Agent across the platform.
Secondary configuration role
: If the primary agent is inactive, the secondary agent automatically becomes active to ensure any configuration deployment tasks are completed successfully.
Agent notifications
Default behavior
: Agent notifications are enabled by default for events, such as new agent versions and agent downtime.
Downtime trigger
: Notifications for agent downtime are specifically triggered when a Remote Agent has been down for more than 90 seconds.
Opt-out
: You can opt out of these notifications at any time from your user preferences.
For more detailed information on configuring notifications, see
Agent notifications
.
Need more help?
Get answers from Community members and Google SecOps professionals.
