# Understand the Google SecOps platform

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/understand-the-secops-platform/  
**Scraped:** 2026-03-05T09:14:28.239527Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand the Google SecOps platform
Supported in:
Google secops
Following the article
Navigate the platform
you will see that there are areas divided into SIEM and SOAR. This is because the Google Security Operations platform provides tools for security information and event management (SIEM) and security orchestration, automation, and response
(SOAR). Some parts of the Google SecOps platform  are specific to either SIEM or SOAR only and therefore are labeled as such.
SIEM Search and SOAR Search
In the Google SecOps platform, there are two separate Search screens.
SIEM Search directs you to the
UDM Search
page, where you can find and investigate
 Unified Data Model (UDM) events and alerts in your Google Security Operations instance. 
 You can search individual UDM events or for groups of UDM events using shared 
 search terms. The search also includes alerts ingested from SOAR connectors and webhooks. 
 For more information, see
SIEM Search
The SOAR Search screen focuses on two main areas: cases and entities. From this screen, you can search for both open or closed cases or search for entities that were involved in cases. You can drill down to the entities you are looking for to see further information on them. You can perform bulk actions such as merge cases on your search results. For more information, see
SOAR search
.
SIEM Dashboards and SOAR Dashboards
SIEM dashboards display information about your UDM events data. This includes security telemetry, ingestion metrics, detections, alerts, IOCs, and more. For more information, see
SIEM Dashboards
.
The SOAR Dashboards display information on cases, playbooks, and  SOC analyst data. You can create new dashboards and share them with other users. For more information, see
SOAR dashboards
.
SIEM Settings and SOAR Settings
The majority of the SOAR administration and configuration are located within the SOAR Settings and the majority of the SIEM administration and configuration are located within the SIEM Settings. The permissions are set separately for each side of the platform and there is no dependency between them. For example, you could choose to limit permissions to Playbooks in the SOAR Settings for certain user groups whilst giving full permissions to all modules in the SIEM settings.
Permission changes that are managed with Identity and Access Management (IAM) are applied 
immediately. However, changes made from the SOAR settings take effect only after 
the user logs out and logs in.

These platform-wide settings includes these pages to manage user access:

*
IDP Group Mapping
: Maps all external Identity Provider (IdP) groups to Google SecOps platform user groups. 
*
Permissions Groups
: Lets you define a default landing page for each user group. Changes in permissions that are managed using Identity and Access Management (IAM) are applied immediately. However, permissions managed from the SOAR settings are only applied the next time the user logs into the platform.
For information on SIEM settings, see
SIEM settings
.
For details about data retention, see
Data Retention in your Google SecOps account
.
For information on SOAR settings, refer to
SOAR settings
.
Ingesting data using SecOps SIEM and third party SIEMS
The Google SecOps platform offers the opportunity to not only ingest alerts using the inbuilt SIEM platform (which ingests raw logs using forwarders and data feeds) but also accepts alerts from third party SIEMS (via SOAR > Connectors and Webhooks).
This provides you with the flexibility to take advantage of other SIEMs as well our own Google SecOps SIEM offering. Google recommends using the inbuilt SIEM wherever possible for a more seamless experience.
Alerts ingested from both the inbuilt SIEM and third party SIEMS can be grouped into Cases and looked at as part of the Case Management features. Alerts ingested from third party SIEMs are sent to the SIEM side of the platform and can be seen using the UDM search but are not subjected to the inbuilt SIEM rules.
Need more help?
Get answers from Community members and Google SecOps professionals.
