# Monitor and manage Remote Agents

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/manage-remote-agents/  
**Scraped:** 2026-03-05T09:35:55.549635Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Monitor and manage Remote Agents
Supported in:
Google secops
SOAR
This document provides a reference for the
Remote Agents
page, detailing
the information displayed for agent monitoring and the actions available for agent
lifecycle management.
Name
: The configured name of the agent.
Agent Status
: The current operational state of the agent.
Live
: The agent is active and communicating.
Failed
: The agent has experienced a connection or operational issue.
Pending
: The agent has been provisioned but isn't yet connected.
Disabled
: The agent has been manually disabled and can't perform tasks.
Environment
: The specific environment associated with the agent.
Agent Version
: The current version of the agent software.
Last Communication
: The timestamp of the agent's last successful communication.
High Availability
: Displays if the agent is configured as a primary or secondary high availability component.
For more details about HA, see
Deploy high availability for Remote Agents
.
Available update
: Notification if a new version of the agent software is available to install.
Available management actions
For more detailed information and actions, click
more_vert
More
.
Send installer/docker command
: Generates a unique download link for
  the agent installer or the Docker command string, necessary for deployment on a remote machine.
Edit
: Modify the agent's name or its log level.
Download logs
: Download agent's log for troubleshooting.
Disable agent
: Temporarily prevent the agent from running actions or
connectors and stop it from communicating with Google Security Operations.
Delete agent
: Permanently remove the agent from the platform.
Need more help?
Get answers from Community members and Google SecOps professionals.
