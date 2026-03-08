# Collect Fortinet FortiSASE logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/fortinet-fortianalyzer/  
**Scraped:** 2026-03-05T09:56:24.150578Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Fortinet FortiSASE logs
Supported in:
Google secops
SIEM
This document explains how to export Fortinet FortiSASE logs by setting up the Bindplane agent.
For more information, see
Data ingestion to Google SecOps overview
.
A typical deployment consists of FortiSASE configured to forward logs to a FortiAnalyzer behind a Secure Private Access FortiGate hub. The FortiAnalyzer is configured to forward logs to a Bindplane agent using syslog. The Bindplane agent forwards the logs to Google SecOps. Each customer deployment can differ and might be more complex.
The deployment contains the following components:
FortiSASE
: The platform from which you collect logs.
FortiAnalyzer
: the log aggregation destination for exporting FortiSASE logs.
Bindplane agent
: The Bindplane agent fetches logs from Fortinet FortiSASE and sends logs to Google SecOps.
Google SecOps
: Retains and analyzes the logs.
An ingestion label identifies the parser which normalizes raw log data to structured UDM format.
The information in this document applies to the parser with the
FORTINET_FORTIANALYZER
label.
Configure FortiSASE log export to FortiAnalyzer
Follow the Fortinet documentation for
Forwarding logs to an external server
to configure FortiSASE to send logs to FortiAnalyzer.
Configure syslog on the FortiAnalyzer platform
Configure the FortiAnalyzer to export log data to a Bindplane agent by following the
Collect Fortinet FortiAnalyzer logs
documentation.
If you encounter issues when you create feeds, contact
Google SecOps support
.
Need more help?
Get answers from Community members and Google SecOps professionals.
