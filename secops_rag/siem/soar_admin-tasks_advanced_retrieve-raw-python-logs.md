# Retrieve raw Python logs

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/retrieve-raw-python-logs/  
**Scraped:** 2026-03-05T09:16:07.175730Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Retrieve raw Python logs
Supported in:
Google secops
SOAR
This document explains how to use the
/api/external/v1/logging/python
endpoint with filters to retrieve only the log data you need. It provides an overview of Google Security Operations-specific and generic filters, along with example queries for common use cases.

For details on
/api/external/v1/logging/python
and other API endpoints, refer to your localized Swagger documentation.
Filter to retrieve specific details
You can use two types of filters: Google SecOps-specific filters and generic filters.
Google SecOps-specific filters
labels.integration_name
labels.integration_instance
labels.integration_version
labels.connector_name
labels.connector_instance
labels.action_name
labels.job_name
labels.correlation_id
Google SecOps-generic filters
For more information about built-in log filters, see
Build queries by using the Logging query language
.
Examples of common filters
You can using the examples in this section to retrieve specific information.
Integration version
To retrieve logs for a specific integration version, use the following filters:
labels.integration_name=
"INTEGRATION_NAME"
AND
labels.integration_version=
"INTEGRATION_NUMBER"
For example:
labels.integration_name="Exchange" AND labels.integration_version="19"
Integration instance
To retrieve logs for a specific integration instance, use the following filter:
labels.integration_instance=
"INTEGRATION_NAME"
For example:
labels.integration_instance="GoogleAlertCenter_1"
All connectors
To retrieve logs for all connectors, use the following filter with the regular expression:
labels.connector_name=~"^."
Specific connector
To retrieve logs for a specific connector, use the following filter:
labels.connector_name=
"CONNECTOR_NAME"
For example:
labels.connector_name="Exchange Mail Connector v2 with Oauth Authentication"
All jobs
To retrieve logs for all jobs, use the following filter with the regular expression:
labels.job_name=~"^."
Specific job
To retrieve logs for a specific job, use the following filter:
labels.job_name=
"JOB_NAME"
For example:
labels.job_name="Cases Collector"
All actions
To retrieve logs for all actions, use the following filter with the regular expression:
labels.action_name=~"^."
Specific action
To retrieve logs for a specific action, use the following filter:
labels.action_name=
"ACTION_NAME"
For example:
labels.action_name="Enrich Entities"
Failed actions
To retrieve logs for a failed action, use the following filters together:
labels.action_name="
ACTION_NAME
" AND SEARCH("Result Value: False")
For example:
labels.action_name="Enrich Entities" AND SEARCH("Result Value: False")
Search
Use the
SEARCH
operator for free-text searches and for filtering based on specific labels. It lets you search for keywords, phrases, or values within various fields of the log entries, including labels. It searches across multiple fields within the log entry, making it useful for finding records that contain specific text in any of the fields. You can use the operator for case-sensitive or case-insensitive searches.
To perform a search, use the following filter:
SEARCH("
FREE_TEXT
")
For example:
SEARCH("Result Value: False")
searches for the exact phrase
Result Value: False
in any field of the log entry.
For example:
SEARCH("Find my CASE SensiTive stRing")
performs a case-sensitive search for the phrase
Find my CASE SensiTive stRing
.
Specific message text
Use the
textPayload
filter to search within the
textPayload
field of the log entry, which is the main body of the log message. It's useful for filtering based on the actual text content of the log message.
To retrieve logs for a specific message, use the following filter:
textPayload=~"
FREE_TEXT
"
For example:
textPayload=~"Invalid JSON payload"
searches for log entries where the payload contains the phrase "Invalid JSON payload".
Siemplify Cases Collector job
To retrieve logs for cases collector errors, use the following filters together:
textPayload=~(\\".\*----Cases Collector DB started---\*\\") AND
severity>="Error"
Server errors
To retrieve logs for server errors, use the following filter:
textPayload=~"Internal Server Error"
Correlation ID
To retrieve logs for a correlation ID, use the following filter:
labels.correlation_id="
CORRELATION_ID
"
For example:
labels.correlation_id="e4a0b1f4afeb43e5ab89dafb5c815fa7"
Timestamp filter
To retrieve logs, use timestamps in either
RFC 3339
or
ISO 8601
format. In query
expressions, RFC 3339 timestamps can specify a timezone with
Z
or
±hh:mm
. All timestamps have nanosecond accuracy.
For more information, see
Values and conversions
.
To retrieve logs newer than a specific timestamp (UTC), use the following
filter:
timestamp>=
"ISO_8601_format"
For example:
timestamp>="2023-12-02T21:28:23.045Z"
To retrieve logs for a specific day, use the following filters together:
timestamp>=
"YYYY-MM-DD"
AND
timestamp<
"YYYY-MM-DD"
For example:
timestamp>="2023-12-01" AND timestamp<"2023-12-03"
Need more help?
Get answers from Community members and Google SecOps professionals.
