# Onboard Google SecOps SOAR platform

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/onboard-chronicle-soar/  
**Scraped:** 2026-03-05T10:10:41.429529Z

---

Home
Documentation
Security
Google Security Operations
Stay organized with collections
Save and categorize content based on your preferences.
Onboard Google SecOps SOAR platform
Supported in:
SOAR
This document provides a comprehensive, step-by-step guide to onboarding and configuring the Google Security Operations SOAR platform. The process is structured to establish user access, secure data ingestion, normalize data, build automation, and prepare for live operations.
Before you begin
We strongly recommend taking the training in our
Google SIEM and SOAR learning path
first.
Set up user access and roles
To get started, you must define a
role
and
permission groups
.
If you're an MSSP or you manage a multi-tenant environment, you also need to set up an
environment
and associate it with new users.

If required, you can also provision users to sign in using a SAML provider.
For detailed instructions for each of these tasks, see the following documents:
Manage roles and workloads
Manage permission groups
Add a new environment
(relevant mainly for MSSPs)
Add a new user to the platform
Authenticate users using SSO (SOAR only)
Set up data ingestion points using connectors or webhooks
Configure connectors or webhooks to ingest alerts for analysis. This can also be achieved by downloading an entire Use Case. For 
detailed instructions for each of these tasks, see the following documents:
Ingest data using SOAR connectors
Set up a webhook
Run use cases
Develop your first email connector
(for advanced users)
Map and model incoming data (ontology)
Control how incoming products, events, and entities are mapped and modeled. This ensures the correct information is captured and visualized. You can define this ontology configuration 
for yourself or choose the default mapping and modeling configuration. 
For detailed instructions for each of these tasks, see the following documents:
Ontology overview
Map security event relationships with visual families
Create entities (mapping and modeling)
Create and test automation (playbooks)
Build automated responses using playbooks—sequential sets of manual and automated steps that respond to threats. For more information about playbooks, see the following documents:
Explore the playbooks page
Create your first automation
Run use cases from the 
Content Hub
Work with the Playbook Simulator
Analyze cases and alerts
Use simulated cases and test alerts to verify configurations. Once live, analyze cases and alerts to determine triage or remediation steps. For detailed instructions for each of these tasks, see the following documents:
Cases overview
Take actions on a case
Perform manual actions
View alert overview tab
Navigate the Entity Explorer page
Need more help?
Get answers from Community members and Google SecOps professionals.
