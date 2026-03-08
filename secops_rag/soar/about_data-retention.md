# Data retention in your Google SecOps account

**Source:** https://docs.cloud.google.com/chronicle/docs/about/data-retention/  
**Scraped:** 2026-03-05T09:46:15.704938Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Data retention in your Google SecOps account
Supported in:
Google secops
SIEM
By default, Google retains twelve months of your data in your Google Security Operations
account. This retention period can be extended as part of your Purchase Order.
The retention period applies to all of the data in your Google SecOps
instance. For example, you can't modify the data retention policy for a specific
log type.
Google uses an automated system to remove historical data based on the following:
Raw logs
: Retention is determined by the ingestion timestamp (when the log arrived in the system).
UDM events
: Retention is determined by the UDM event time (the timestamp within the normalized data structure).
View your data retention start date in Google SecOps
The
Data Retention
page is a read-only section within the SIEM settings that 
shows the date when data retention began for your account.
To view your data retention start date, follow these steps:
In the navigation bar, select
SIEM Settings
>
Data Retention
. 
The
Data Retention
page displays the retention start date in
yyyy-mm-dd
format.
To learn about where data in the Google SecOps account is stored, see
SecOps service locations
.
For more information, see
Google SecOps pricing
.
Need more help?
Get answers from Community members and Google SecOps professionals.
