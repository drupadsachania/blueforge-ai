# Redeploy connectors

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/redeploy-connectors-remote-agents/  
**Scraped:** 2026-03-05T10:09:27.782425Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Redeploy connectors
Supported in:
Google secops
SOAR
When you redeploy connectors, the connector's scheduler moves from the Remote Agent
to the Google Security Operations server. You can manually redeploy connectors
for each Remote Agent.
The connector redeployment process is connected to the
Remote Agent's high availability
feature. During redeployment, the system validates each connector. If it detects
any issues, it automatically reverts all changes and restores the connector to its
previous working state.
The redeployment process may take some time. You can track its completion on the
Remote Agent
page. If you get an error message, repeat the redeployment process.
If you continue to get an error, contact
Google Support
.
Need more help?
Get answers from Community members and Google SecOps professionals.
