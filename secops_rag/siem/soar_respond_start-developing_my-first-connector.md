# Develop your first email connector

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/my-first-connector/  
**Scraped:** 2026-03-05T09:35:38.784755Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Develop your first email connector
Supported in:
Google secops
SOAR
Connectors
are the entry point for alerts into Google SecOps.
  Their job is to translate raw input data from multiple sources into
  Google SecOps format. The connectors get alerts (or equivalent
  data, such as alarms or correlation events) from third-party tools sent to the
  data processing layer and send them for ingestion as Google SecOps alerts
  and events.
This document explains how to develop an email connector in the Integrated
Development Environment (IDE). The process involves:
Ingesting raw data from an email source (Gmail).
Translating that data into Google Security Operations format.
Creating cases within the platform from the translated data.
The connector scans each email message body to extract URLs. You can then use
the product integrated in
Develop your first action
to check if these URLs are malicious.
Before you begin
Before the connector can connect to your email inbox, complete the following steps:
For testing purposes, create a new Gmail account or use an existing one.
Enable two-step verification to grant Google SecOps secure access to the email inbox.
Create an App Password that grants the Google SecOps platform permission to access your account. You can only use App Passwords with accounts that have two-step verification enabled.
In your Google Account, click
App Passwords
and then fill in the required fields:
In
Select app
, select
Other (Custom name)
.
Add the URL associated with your Google SecOps platform (DNS)
.
Create the email connector in the IDE. For details, see
Develop the connector
.
Need more help?
Get answers from Community members and Google SecOps professionals.
