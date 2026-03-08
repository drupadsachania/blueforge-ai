# Test the Remote Agent connection flow

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/test-agents/  
**Scraped:** 2026-03-05T10:09:25.234177Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Test the Remote Agent connection flow
Supported in:
Google secops
SOAR
This document outlines how to perform a basic, end-to-end test of the Remote
Agent deployment by installing an agent locally and verifying its connection to
an integrated security tool. The goal is to confirm the full communication path
from the Google Security Operations platform, through the agent, and back.
Create and deploy an agent:
Create a new agent and send the download link to an email address you can access.
Click the link in the email and download the agent installation package.
Deploy the agent locally.
Verify the agent status is live in the Google SecOps platform.
Confirm the agent can successfully communicate with another product (for example,
  Active Directory or ServiceNow). This test confirms the flow from Google SecOps to the agent and back.
Set up the relevant integration to run remotely and test the specific actions.
Both integrations and connectors provide testing features and display the
status of the assigned Remote Agents directly within the platform. This same flow
can be repeated for agents deployed on remote sites.
Need more help?
Get answers from Community members and Google SecOps professionals.
