# Applied Threat Intelligence curated detections overview

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/ati-curated-detections/  
**Scraped:** 2026-03-05T10:04:46.438270Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Applied Threat Intelligence curated detections overview
Supported in:
Google secops
SIEM
This document provides an overview of the Curated Detection rule sets within the
Applied Threat Intelligence Curated Prioritization category, available
in Google Security Operations Enterprise Plus. These rules use 
Mandiant Threat Intelligence to proactively identify and alert on high-priority 
threats.
Curated detection rule sets
The Curated Prioritization category includes the following rule sets that support the Applied Threat
Intelligence feature in Google SecOps:
Active Breach Priority Network Indicators
: Detects network-related 
Indicators of Compromise (IoCs) in event data using Mandiant Threat Intelligence and prioritizes IoCs with the 'Active breach' label.
Active Breach Priority Host Indicators
: Detects host-related IoCs in 
event data using Mandiant Threat Intelligence and prioritizes them with the 'Active 
breach' label.
High Priority Network Indicators
: Identifies network-related IoCs in event 
data using Mandiant Threat Intelligence and prioritizes them with the 'High' label.
High Priority Host Indicators
: Detects host-related IoCs in event data 
using Mandiant Threat Intelligence and prioritizes them with the High label.
Inbound IP Address Authentication Indicators
: Identifies IP addresses that 
are authenticating to local infrastructure in an inbound network direction and prioritizes them with the 'High' label.
Medium Priority Network Indicators
: Identifies network-related IoCs in event
data using Mandiant Threat Intelligence and prioritizes them with the 'Medium' label.
Medium Priority Host Indicators
: Identifies host-related IoCs in event data 
using Mandiant Threat Intelligence and prioritizes them with the 'Medium' label.
When you enable the rule sets, Google SecOps starts evaluating 
your event data against Mandiant Threat Intelligence data. If any rule detects 
a match
to an IoC labeled 'Active breach' or 'High', an alert is generated. 
For more information about how to enable curated detection rule sets, see
Enable all rule sets
.
Supported devices and log types
You can ingest data from any log type that Google SecOps supports 
with a default parser (see
Supported log types and default parsers
).
Google SecOps evaluates your UDM event data against IoCs curated by Mandiant Threat
Intelligence and identifies matches for domains, IP addresses, file hashes, and URLs. It then analyzes UDM fields that store these rule sets.
If you replace a default parser with a custom parser, and you change the UDM field
where a domain, IP address, file hash, or URL is stored, it may impact the behavior
of these rule sets.
The rule sets use the following UDM fields from Google SecOps events.
These fields, combined with prioritization features from 
Mandiant Threat Intelligence, help determine priority levels, such as Active breach, High, 
or Medium:
network.direction
security_result.[]action
event_count
(active breach IP address only)
For IP address indicators, the
network.direction
is required. If the
network.direction
field is not populated in the UDM event, then Applied Threat
Intelligence checks the
principal.ip
and
target.ip
fields against RFC 1918
internal IP address ranges to determine the network direction. If this check
does not provide clarity, then the IP address is considered to be external to
the customer environment.
Tuning alerts returned by Applied Threat Intelligence category
You can reduce the number of detections a rule or rule set generates using
rule exclusions
.
In the rule exclusion, define the criteria of a UDM event that exclude the
event from being evaluated by the rule set. Events with values in the specified
UDM field won't be evaluated by rules in the rule set.
For example, you might exclude events based on the following information:
principal.hostname
principal.ip
target.domain.name
target.file.sha256
target.url
See
Configure rule exclusions
for information about how to create rule exclusions.
If a rule set uses a predefined reference list, the reference
list description provides detail about which UDM field is evaluated.
The Inbound IP Address Authentication rule set uses three UDM fields that could 
be used for tuning alerts from this rule set:
principal.ip
principal.asset.ip
src.ip
Need more help?
Get answers from Community members and Google SecOps professionals.
