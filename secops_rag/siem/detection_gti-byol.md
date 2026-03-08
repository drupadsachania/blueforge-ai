# BYOL Threat Intelligence integration

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/gti-byol/  
**Scraped:** 2026-03-05T09:33:19.917533Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
BYOL Threat Intelligence integration
Supported in:
Google secops
SIEM
Integrate your licensed Google Threat Intelligence (GTI) data directly into
Google SecOps using the Bring Your Own License (BYOL)
integration. Ingest threat lists, IoC streams, and adversary context to enhance
your threat detection and hunting capabilities.
The Google Threat Intelligence BYOL integration ingests your threat
intelligence data into Google SecOps and normalizes it
into Unified Data Model (UDM) format. Google SecOps correlates this threat telemetry with
your security events, immediately improving your threat hunting and detection.
Availability
This integration is available to
Google SecOps Standard
and
Enterprise
customers who have an active Google Threat Intelligence
license.
Standard and Enterprise:
This integration provides a customer-deployed
pipeline to bring Google Threat Intelligence data into your Google SecOps
environment for detection and hunting.
Enterprise+:
Enterprise+ customers already benefit
from
Applied Threat Intelligence (ATI)
, a fully managed, built-in
pipeline that automatically curates and applies Google's threat
intelligence. While this BYOL integration is compatible with Enterprise+,
the ATI service is the recommended solution.
Key capabilities
Unified data ingestion:
Ingests GTI threat lists (categorized IoCs)
and IoC stream data, providing near real-time updates for file hashes, IPs,
URLs, and domains.
UDM normalization:
Automatically parses data into the
Unified
Data Model (UDM)
under the log type
GCP_THREATINTEL
, making it instantly
searchable and ready for correlation rules.
Adversary context:
Ingests associations for malware, threat actors, campaigns, and reports, including MITRE ATT&CK mappings.
Pre-built dashboards:
Includes out-of-the-box
dashboards
for
visualizing threat lists, adversary intelligence, and
IoC streams
.
Prerequisites
Before you set up the integration, ensure you have the following:
A valid and active Google Threat Intelligence license (BYOL), to access the GTI API.
Access to a Google Cloud project to deploy the necessary resources (Cloud Run functions,
Cloud Scheduler, Secret Manager).
Access to your Google SecOps instance.
Deployment
This integration is a customer-deployed solution that uses Google Cloud
resources to fetch data from the GTI API and stream it to Google SecOps.
Follow the instructions and user guide to run the deployment scripts and configure the Google Threat Intelligence integration. For details, see the official GitHub repository readme file:
Google Threat Intelligence ingestion scripts on GitHub
Once deployed, the BYOL ingestion process is triggered by a Cloud Scheduler job, which activates a Cloud Function to securely fetch API credentials from Secret Manager. The function then queries the external GTI API for the latest threat data, streams it to the Chronicle API, and a default parser transforms (normalizes) the raw data into UDM entities.
Dashboards
Google Threat Intelligence gives you the visibility needed to understand and anticipate threat actor tactics 
and protect your organization against emerging threats.
Use the following dashboards to visualize the ingested data:
Threat lists dashboard
: Focuses on detection and blocking, showing
IoC counts by severity and entity type.
Adversary intelligence dashboard
: Focuses on context and lets you
drill down into malware families, threat actors, and campaigns.
Google Threat Intelligence dashboard
: Provides a real-time overview of the
IoC stream, including severity distribution and geographical breakdown.
Unified workflow: SIEM and SOAR
The BYOL integration combines SIEM's detection and hunting capabilities with
SOAR's
Google Threat Intelligence
features in a closed-loop security workflow.
SIEM helps you
find
threats, and SOAR lets you
respond
to them.
The following scenarios illustrate how these capabilities work together:
Enriched investigation (SIEM to SOAR):
Action:
An analyst identifies a suspicious domain in Google SecOps
SIEM using the ingested GTI data.
Response:
They trigger a SOAR search action to query GTI for
deep context on that domain (for example, associated threat actors, passive
DNS) without leaving the investigation flow.
Advanced artifact analysis (SIEM to SOAR):
Action:
During an investigation in Google SecOps SIEM, an analyst
encounters a suspicious file hash or URL that lacks definitive reputation data.
Response:
Using the SOAR integration, the analyst triggers an action
to
privately submit
the URL or file to
Google Threat Intelligence for advanced analysis. This
performs deep scanning and sandbox detonations to determine maliciousness,
while keeping the submission private and not sharing it with the
broader community immediately.
Need more help?
Get answers from Community members and Google SecOps professionals.
