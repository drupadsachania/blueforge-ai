# Applied Threat Intelligence overview

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/applied-threat-intel-overview/  
**Scraped:** 2026-03-05T10:05:53.426115Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Applied Threat Intelligence overview
Supported in:
Google secops
SIEM
Applied Threat Intelligence (ATI) helps you identify and respond to threats. It continually
analyzes and evaluates your security telemetry against Indicators of Compromise 
(IoCs) curated by Mandiant threat intelligence.
When ATI is enabled, Google SecOps ingests IoCs curated
by Mandiant threat intelligence that are classified as
malicious
by the Google
Threat Indicator (GTI) verdict.
When a match is found, an alert is generated. You can then investigate the IoC on the
IoC matches
page, which displays possible IoC matches for domains, IP addresses, file hashes, and URLs. Information about the IoC is displayed, including the following:
GCTI priority
GTI verdict
Associations
Campaigns
You can also view detailed information about the events that triggered the IoC match, information from the threat intelligence source,
and the rationale for the GTI score. For more information, see
View IoCs using Applied Threat Intelligence
.
Google SecOps curated detections evaluate your event data against
Mandiant threat intelligence data, and generates an alert when one or more rules
identify a match to an IoC with an active breach or high priority.
To use Applied Threat Intelligence, do the following:
Enable the
Applied Threat Intelligence curated detections
.
Investigate alerts using the
IOC matches
page.
You can also learn more about how the IC-Score is assigned in the
IC-Score overview
.
Need more help?
Get answers from Community members and Google SecOps professionals.
