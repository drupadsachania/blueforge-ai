# Ingest data using the entity data model

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-entities/  
**Scraped:** 2026-03-05T09:30:29.910257Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Ingest data using the entity data model
Supported in:
Google secops
SIEM
Entities provide context to network events which typically do not surface all the information known about the systems they connect to. For example, while a PROCESS_LAUNCH event might be linked to a user (abc@foo.corp) who launched the shady.exe process, the PROCESS_LAUNCH event won't indicate that the user (abc@foo.corp) was a recently-terminated employee on a highly-sensitive project. This context would normally only be provided by further research conducted by a security analyst.
The entity data model enables you to ingest these types of entity relationships, providing a richer and more focused IOC threat intelligence data. It also introduces and expands the Permission, Role, Vulnerability, and Resource messages to capture new context available from IAM, vulnerability management systems, and data protection systems.
For details on the entity data model syntax, see the
Entity Data Model Reference
documentation.
Default parsers
The following
default parsers
and
API feeds
support the
ingestion of asset or user context data:
Azure AD Organizational Context
Duo User Context
Google Cloud IAM Analysis
Google Cloud IAM Context
Google Cloud Identity Context
JAMF
Microsoft AD
Microsoft Defender for Endpoint
Nucleus Unified Vulnerability Management
Nucleus Asset Metadata
Okta User Context
Rapid7 Insight
SailPoint IAM
ServiceNow CMDB
Tanium Asset
Workday
Workspace ChromeOS Devices
Workspace Mobile Devices
Workspace Privileges
Workspace Users
Ingestion API
Use the Ingestion API to ingest entity data into your Google Security Operations account directly.
See the
Ingestion API
documentation.
Need more help?
Get answers from Community members and Google SecOps professionals.
