# Google SecOps data ingestion

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/secops-ingestion/  
**Scraped:** 2026-03-05T09:16:18.866585Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Google SecOps data ingestion
Supported in:
Google secops
SIEM
Google Security Operations ingests customer logs, normalizes the data, and detects
security alerts. It provides self-service features for
data ingestion, threat detection, alerts, and case management.
Google SecOps can also receive alerts from other SIEM systems and
analyze them.
Google SecOps log ingestion
The Google SecOps ingestion service acts as a gateway for all data.
Google SecOps ingests data using the following systems:
Google Cloud
: Google SecOps retrieves data directly from your Google Cloud organization, which is the primary method for all standard Google Cloud logs (for example, Audit, VPC Flow, DNS, and Firewall).
It is the most cost-effective and performant way to bring in Google Cloud telemetry to Google SecOps.
For more information, see
Ingest Google Cloud data to Google SecOps
.
Bindplane agent
: This is a managed agent for collecting logs from on-premises 
environments and servers (Windows or Linux). 
Bindplane is a telemetry pipeline that can collect, refine, and export logs from any source into Google SecOps, and therefore provides flexibility in collecting different types of logs that don't work with other methods.
You can use it for on-premises data, such as Firewall logs, Windows and Linux logs, or for cloud data you want to preprocess (for example, refine or filter) before ingesting into Google SecOps.
You can also manage this agent by using the Bindplane OP Management console. For more information,
see
Use the Bindplane agent
.
Data feeds
: Data feeds are used primarily for cloud-based logs where the third-party logs are already aggregated into an object store, such as Cloud Storage or Amazon S3, or when the third party supports 'push'-based methods, such as webhook.
Data feeds also provide out-of-the-box support for a predefined set of API based integrations.
Use Data feeds for cloud-based logs such as EDRs or any SaaS application and for the specific integrations predefined as
Direct API
.
The data feeds send logs directly to the Google SecOps ingestion service. For more information,
see the
feed management documentation
. Data feeds support log lines up to 4 MB in size.
Ingestion APIs
: Use the Ingestion API for custom, high-volume, or home-grown applications that don't fit into other methods. This method is slightly more complex to use than other ingestion methods. For more information, see the
Ingestion API
.
Forwarders
: The Forwarder is now end of life. Google recommends you use the Bindplane agent instead.
Parsers convert logs from customer systems
into a Unified Data Model (UDM). Downstream systems within
Google SecOps use the UDM to provide additional capabilities,
including rules and UDM search.
See
Understand data availability for search
for full details of the data ingestion lifecycle, including end-to-end data flow and latency, and how these factors impact the availability of recently ingested data for querying and analysis.
Types of Google SecOps ingestion
Google SecOps can ingest both
logs and alerts, but supports only single-event alerts. You can use UDM search 
to find both ingested and
built-in Google SecOps alerts.
Google SecOps supports the following types of data ingestion:
Raw logs
Google SecOps ingests raw logs using forwarders, the ingestion
API, data feeds, or directly from Google Cloud.
Use a single-line JSON payload for raw log ingestion. For example,
{ "firstName": "Alex", "lastName": "N", "age": 30, "isStudent": false, "address": { "streetAddress": "1800 Amphibious Blvd", "city": "Anytown", "state": "CA", "postalCode": "94045" }, "phoneNumbers": [ { "type": "home", "number": "800-555-0199" }, { "type": "mobile", "number": "800-554-0199" } ], "hobbies": ["reading", "hiking", "cooking"]}
If you submit a multi-line payload, the system interprets each line as a separate log entry.
Alerts from other SIEM systems
Google SecOps can ingest alerts from other SIEM systems, EDRs, or
ticketing systems, as follows:
Receive alerts using Google SecOps
connectors
or Google SecOps
webhooks
.
Ingest the events associated with each alert and create a corresponding
detection.
Process both the ingested events and detections.
You can create detection engine rules to identify patterns in the ingested
events and generate additional detections.
Data ingestion flow
The following diagram illustrates how your security data flows into
Google SecOps and how the system processes that data for analysis in 
the interface.
Process customer security data in Google SecOps
Google SecOps processes your security data as follows:
Retrieves security data from cloud services like Amazon S3 or the
Google Cloud. Google SecOps encrypts this data in transit.
Separates and stores your encrypted security data in your account. Access is 
limited to you and a small number of Google personnel for product support, development, and maintenance.
Parses and validates raw security data, making it easier to process and view.
Indexes the data for quick searches.
Stores the parsed and indexed data within your account.
Offers secure access for users to search and review their security data.
Compares your security data with the VirusTotal malware database to identify
matches. In a Google SecOps event view, such as the Asset view,
click
VT Context
to see VirusTotal information.
Google SecOps doesn't share your security data with
VirusTotal.
Need more help?
Get answers from Community members and Google SecOps professionals.
