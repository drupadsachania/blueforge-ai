# Handle large alerts

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/handle-large-alerts/  
**Scraped:** 2026-03-05T10:07:41.830993Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Handle large alerts
Supported in:
Google secops
SOAR
Most security alerts ingested through connectors or webhooks don't impact performance.
The system efficiently ingests alerts up to 28 MB. Alerts exceeding this
threshold trigger an automatic, phased mitigation process to prevent system
overload and ensure processing efficiency.
The platform executes each phase sequentially, only initiating the next if the
previous one fails to resolve the size issue. Trimmed alerts display a system notification.
Phased approach for handling large alerts
The following is a breakdown of how to handle large alerts in a phased approach to
prevent system overload and ensure efficient processing:
Trim longest values
: Detect and shorten the longest string values within every event field.
Trim field count
: Reduce the total number of fields in the alert to a maximum of 100 fields.
Trim event count
: Reduce the total number of events in the alert to a maximum of 50 events.
Database parameters control these default trim values. For information about 
these values, see
Service limits
.
To update parameter values, contact
Google Support
.
Need more help?
Get answers from Community members and Google SecOps professionals.
