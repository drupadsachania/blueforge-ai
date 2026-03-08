# Collect Cribl Stream logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cribl-stream/  
**Scraped:** 2026-03-05T09:53:39.207844Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Cribl Stream logs
Supported in:
Google secops
SIEM
This document explains how to ingest Cribl Stream logs to
Google Security Operations using the built-in Google SecOps
destination. Cribl Stream produces operational data in the form of logs, metrics,
and events. This integration lets you send these logs to
Google SecOps for analysis and monitoring.
Before you begin
Make sure you have the following prerequisites:
A Google SecOps instance.
Access to Cribl Stream management console or cluster.
Google Cloud service account credentials.
Get Google SecOps ingestion authentication file
Sign in to the Google SecOps console.
Go to
SIEM Settings
>
Collection Agents
.
Download the
Ingestion Authentication File
.
Configure Google SecOps destination in Cribl Stream
Sign in to the
Cribl Stream Management Console
.
Go to
Data
>
Destinations
.
Click
Add Destination
.
Select
Google Cloud
>
Security Operations (SecOps)
.
Provide the following configuration details:
Output ID
: Enter a unique name (for example,
google-secops-destination
).
Description
: Enter a description for this destination.
Send events as
: Select
Unstructured
(recommended for standard log parsing).
API version
: Select
V2
.
Default log type
: Select
CRIBL_STREAM
from the list.
Optional:
Namespace
: Enter a namespace to identify logs from this source (for example,
cribl-logs
).
In the
Authentication
section:
Authentication method
: Service account (JSON).
Service account key
: Upload or paste the JSON credentials file content.
In the
Processing
section:
Log text field
: Optionally enter
_raw
. If not set, Cribl will send
JSON representation of the entire event; use
_raw
only if you actually store raw text in this field.
Click
Save
.
Create a route to send Cribl Stream logs
Go to
Data
>
Routes
.
Click
Add Route
.
Provide the following configuration details:
Route name
: Enter a meaningful name (for example,
cribl-logs-to-secops
).
Filter
: Enter
source.match(/cribl.*/)
to capture Cribl internal logs
(operational logs from Cribl itself).
Output
: Select the Google SecOps destination created in
the previous section.
Pipeline
: Select
passthru
or create a custom pipeline for log enrichment.
Click
Save
.
Commit & Deploy
the configuration to apply changes.
Configure log filtering and enrichment (Optional)
If you need to filter or enrich Cribl Stream logs before sending to Google SecOps:
Go to
Data
>
Pipelines
in Cribl Stream.
Click
Add Pipeline
.
Provide the following configuration details:
Pipeline ID
: Enter a meaningful name (for example,
cribl-log-processing
).
Description
: Enter a description for the pipeline.
Add functions as needed:
Eval
: Add metadata fields or modify existing fields.
Regex Extract
: Extract specific information from log messages.
Drop
: Remove unnecessary events or fields.
Mask
: Redact sensitive information.
Click
Save
.
Update your route to use this pipeline instead of
passthru
.
Need more help?
Get answers from Community members and Google SecOps professionals.
