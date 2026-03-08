# Set up and manage data processing pipelines

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/data-processing-pipeline/  
**Scraped:** 2026-03-05T09:16:37.593256Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set up and manage data processing pipelines
Supported in:
Google secops
SIEM
The
Data Processing
feature gives you robust, pre-parsing control over
Google Security Operations data ingestion. You can filter events, transform fields, or redact sensitive values to optimize data compatibility, reduce costs, and protect sensitive information within Google SecOps.
Data processing simplifies log management through three core actions:
Filter
: Reduce noise and costs by ingesting only relevant events.
Transform
: Modify data formats, parse fields, and enrich logs for better usability.
Redact
: Protect sensitive information by masking or removing sensitive values before storage.
The following diagram illustrates how your data flows into Google SecOps and how the system processes that data.
This document guides you through the full data ingestion and processing workflow using the Bindplane console. As such, you can learn how to:
Configure the connection to a Google SecOps destination instance.
Create a new Google SecOps pipeline.
Set up data processing, including streams and processors.
Roll out the pipeline to initiate data ingestion and processing.
Monitor pipeline streams and processors in the Google SecOps console.
You can configure data processing for both on-premises and cloud data
streams, using either the Bindplane management console or directly using the
public
Google SecOps Data Pipeline APIs
.
Data processing consists of the following elements:
Streams
: One or more streams feed data into the data processing pipeline. Each stream is configured for a specific stream type.
Processor node
: Data processing has one
Processor node
that contains one or more processors. Each processor specifies an action to perform on the data (for example, filter, transform, and redact) as it flows through the pipeline.
Destination
: The Google SecOps destination instance is
where the processed data is sent.
Use cases
Example use cases include:
Remove empty key-value pairs from raw logs.
Redact sensitive data.
Add ingestion labels from raw log content.
In multi-instance environments, apply ingestion labels to
direct-ingestion log data to identify the source stream instance (such as 
Google Cloud Workspace).
Filter Palo Alto Cortex data by field values.
Reduce SentinelOne data by category.
Extract host information from feeds and direct-ingestion logs and map it to the
ingestion_source
field for Cloud Monitoring.
Prerequisites
If you intend to use the Bindplane console to manage your
Google SecOps data processing, perform the following
steps:
If you intend to use the Bindplane Server console, in the Google SecOps console, grant one of the following roles:
A custom role with the following permissions:
chronicle.logProcessingPipelines.associateStreams
chronicle.logProcessingPipelines.create
chronicle.logProcessingPipelines.delete
chronicle.logProcessingPipelines.dissociateStreams
chronicle.logProcessingPipelines.fetchAssociatedPipeline
chronicle.logProcessingPipelines.fetchSampleLogsByStreams
chronicle.logProcessingPipelines.get
chronicle.logProcessingPipelines.list
chronicle.logProcessingPipelines.testPipeline
chronicle.logProcessingPipelines.update
chronicle.logTypes.get
chronicle.logTypes.list
chronicle.feeds.get
chronicle.feeds.list
chronicle.logs.list
Google recommends using a custom role with the specified required permissions.
For instructions and related information, see
Create and manage custom roles
and
Configure feature access control using IAM
.
The predefined Chronicle API Admin
roles/chronicle.admin
role
.
For details, see
Assign the Project IAM Admin role in a dedicated project
.
Under
Assign Roles
, select the role from the previous step:
The custom role with the specified required permissions.
The predefined Chronicle API Admin
roles/chronicle.admin
role, which is also the predefined Identity and Access Management role.
Install the Bindplane Server console. For SaaS or on-premises, see
Install the Bindplane Server console
.
Ensure that you install the latest version of Bindplane (or Bindplane version 1.96.4 or later).
In the Bindplane console, connect a Google SecOps destination instance to your
Bindplane project
. For details, see
Connect to a Google SecOps instance
.
Manage low-volume SecOps data acknowledgment delays
Ingestion API users who configure their own agent can experience a potential
increase in acknowledgment time for low-volume SecOps pipelines in the data 
processing pipeline.
Latency averages can rise from 700 ms up to 2 seconds. Increase timeout periods and memory as needed. Acknowledgment time drops when data throughput exceeds 4 MB.
Connect to a Google SecOps instance
Before you begin, confirm that you have the Bindplane
project administrator permissions
to access the
Project Integrations
page.
The Google SecOps instance serves as the destination for your data output.
To connect to a Google SecOps instance using the Bindplane Server console, do the following:
In the Bindplane Server console, click
menu
Menu
and select
Project Settings
.
On the
Project Settings
page, go to the
Integrations
card and click
Connect to Google SecOps
to open the
Edit Integration
window.
Enter the details for the Google SecOps destination instance.
This instance ingests the processed data (output from your data processing), as follows:
Field
Description
Region
Region of your Google SecOps instance.
To find the instance in the Google Cloud console, go to
Security
>
Detections and Controls
>
Google Security Operations
>
Instance details
.
Customer ID
Customer ID of your Google SecOps instance.
In the Google SecOps console, go to
SIEM Settings
>
Profile
>
Organization Details
.
Google Cloud project number
Google Cloud Project Number of your Google SecOps instance.
To find the project number in the Google SecOps console, go to
SIEM Settings
>
Profile
>
Organization Details
.
Credentials
Service Account credentials are the JSON value required to authenticate and access the Google SecOps Data Pipeline APIs. Get this JSON value from the Google Service Account credential file.
The Service Account must be located in the same Google Cloud project as your Google SecOps instance and requires either the Chronicle API Admin role (
roles/chronicle.admin
) privileges or a custom role with the required permissions (see
Prerequisites
) .
For information about how to create a Service Account and download the JSON file, see
Create and delete Service Account keys
.
Click
Connect
. If your connection details are correct and you
successfully connect to Google SecOps, you can expect the
following:
A connection to the Google SecOps instance opens.
The first time you connect, the
SecOps Pipelines
appears 
in the
Bindplane console
.
The Bindplane console displays any processed data you previously set up for this instance using the API. The system converts some processors you configured using the API into Bindplane processors, and displays others in their raw OpenTelemetry Transformation Language (OTTL) format. You can use the Bindplane console to edit pipelines and processors previously set up using the API.
After you successfully create a connection to a Google SecOps instance, you can create a SecOps pipeline and
set up data processing using the Bindplane console
.
Set up data processing using the Bindplane console
Using the Bindplane console, you can manage your Google SecOps
processed data, including pipelines setup using the API.
Before you begin
Before you begin, we recommend that you read these important recommendations:
Data processing is not supported for push-based streams calling the Backstory API. To enable the support, migrate to the
Ingestion API
.
To install the Bindplane console for the first time or to connect a
Google SecOps destination instance to your
Bindplane
project
, see
Prerequisites
.
As an alternative to using the Bindplane console, you can call Google SecOps APIs directly to set up and manage data processing. For details, see
Use Google SecOps Data Pipeline APIs
.
Data ingested from forwarders and Bindplane is tagged with a distinct
collectorID
from direct ingestion streams. To support full log visibility, you must either select all ingestion methods when querying data sources or explicitly reference the relevant
collectorID
when interacting with the API.
Follow these steps to provision and deploy a new log processing pipeline in Google SecOps, typically using the Bindplane console:
Create a new SecOps pipeline
.
Configure data processing
.
Configure streams
.
Configure processors
.
Roll out a data processing pipeline
.
Create a new Google SecOps pipeline
A Google SecOps pipeline is a container for you to configure one data processing container. To create a new Google SecOps pipeline container, do the following:
In the
Bindplane console
, click the
SecOps Pipelines
tab to open the
SecOps Pipelines
page.
Click
Create SecOps Pipeline
.
In the
Create new SecOps Pipeline
window, set the
SecOps Pipeline type
to
Google SecOps
(default).
Enter a
SecOps Pipeline name
and
Description
.
Click
Create
. You can see the new pipeline container on the
SecOps Pipelines
page.
Configure the data processing container
streams and processors within this container.
Configure a data processing container
A data processing container specifies data
streams
to ingest and
processors
(for example, filter, transform, or redact) to manipulate the data as it flows
to the Google SecOps
Destination
instance.
A
pipeline
configuration card is a visualization of the data processing
pipeline where you can configure the data
streams
and the
processor
node
:
A
stream
ingests data according to its configured specifications, and feeds it into the container. A data processing container can have one or more streams, each configured for a different stream.
The
processor node
consists of processors that manipulate the data as it flows to the Google SecOps
Destination
instance.
To configure a data processing container, do the following:
Create a new SecOps pipeline
.
In the
Bindplane console
, click the
SecOps Pipelines
tab to open the
SecOps Pipelines
page.
Select the SecOps pipeline where you want to configure the new data processing container.
On the
Pipeline
configuration card:
Add a stream
.
Configure the
processor node
. To add a processor using the Bindplane console, see
Configure processors
for details.
Once these configurations are complete, see
Roll out data processing
to begin processing the data.
Add a stream
To add a stream, do the following:
In the
Pipeline
configuration card, click
add
Add Stream
to open the
Create Stream
window.
In the
Create SecOps Stream
window, enter details for these fields:
Field
Description
Log type
Select the
log type
of the data to ingest. For example,
CrowdStrike Falcon (CS_EDR)
.
Note
: A
warning
warning
icon indicates that the log type is already configured in another stream (either in this pipeline or another pipeline in your Google SecOps instance).
To use an unavailable log type, you must first delete it from the other stream configuration.
For instructions on how to find the stream configuration where the log type is configured, see
Filter SecOps Pipeline configurations
.
Ingestion method
Select the
ingestion method
to use to ingest the data for the selected
log type
. These ingestion methods were previously defined for your Google SecOps instance.
You must select one of the following options:
All Ingestion Methods
: Includes all ingestion methods for the selected log type. When you select this option, it prevents you from adding subsequent streams that use specific ingestion methods for that same log type.
Exception
: You can select other unconfigured specific ingestion methods for this log type in other streams.
Specific
ingestion method, such as
Cloud Native Ingestion
,
Feed
,
Ingestion API
, or
Workspace
.
Feed
If you select
Feed
as the ingestion method, a subsequent field appears with a list of available feed names (pre-configured in your Google SecOps instance) for the selected log type. You must select the relevant feed to complete the configuration. To view and manage your available feeds, go to
SIEM Settings > Feeds table
.
Click
Add Stream
to save the new stream.The new data stream immediately appears on the
Pipeline
configuration card. The stream is automatically connected to the processor node and the Google SecOps
Destination
.
Filter SecOps Pipeline configurations
The search bar on the
SecOps Pipelines
page lets you filter and locate your SecOps pipelines (data processing containers) based on multiple configuration elements. You can filter pipelines by searching for specific criteria, such as log type, ingestion method, or feed name.
Use the following syntax to filter:
logtype:value
ingestionmethod:value
feed:value
For example, to identify stream configurations that contain a specific log type, in the search bar, enter
logtype:
and select the log type from the resulting list.
Configure processors
A data processing container has one processor node, which holds one or more processors. Each processor manipulates the stream data sequentially:
The first processor processes the raw stream data.
The resulting output from the first processor immediately becomes the input for the next processor in the sequence.
This sequence continues for all subsequent processors, in the exact order they appear in the
Processors
pane, with the output of one becoming the input of the next.
Configure the processor node by adding, removing, or changing the sequence of one or more processors.
The following table lists the processors:
Processor type
Capability
Filter
Filter by condition
Filter
Filter by HTTP status
Filter
Filter by metric name
Filter
Filter by regex
Filter
Filter by severity
Redaction
Redact sensitive data
Transform
Add fields
Transform
Coalesce
Transform
Concat
Transform
Copy field
Transform
Delete fields
Transform
Marshal
Transform
Move field
Transform
Parse CSV
Transform
Parse JSON
Transform
Parse key value
Transform
Parse severity fields
Transform
Parse timestamp
Transform
Parse with regex
Transform
Parse XML
Transform
Rename fields
Transform
Rewrite timestamp
Transform
Split
Transform
Transform
Add a processor
To add a processor, follow these steps:
In the
Pipeline
configuration card, click the
Processor
node to open the
Edit Processors
window.
The
Edit Processors
window is divided in these panes, arranged by data flow:
Input
(or source data): Recent incoming stream log data (before processing)
Configuration
(or processor list): Processors and their configurations
Output
(or results): Recent outgoing result log data (after processing)
If the pipeline was previously rolled out, the system shows the recent incoming log data (before processing) and the recent outgoing log data (after processing) in the panes.
Click
Add Processor
to display the processor list.
For your convenience, the processor list is grouped by processor type. To organize the list and add your own bundles, select one or more processors and click
Add new Processor bundles
.
In the processor list, select a
Processor
to add.
Configure the processor as required.
Click
Save
to save the processor configuration in the
Processor
node.
The system immediately tests the new configuration by processing a fresh sample of the incoming stream data (from the
Input
pane) and displays the resulting outgoing data in the
Output
pane.
Roll out data processing pipeline
Once the stream and processor configurations are complete, you must roll out the pipeline to begin processing data, as follows:
Click
Start rollout
. This immediately activates the data processing and lets Google's secure infrastructure begin processing data according to your configuration.
If the rollout is successful, the data processing container's version number is incremented and displayed next to the container's
name
.
View data processing details in the Google SecOps console
The following sections describe how to view data processing details from the Google SecOps console:
View all data processing configurations
In the Google SecOps console, go to
SIEM Settings > Data Processing
where you can view all of your configured pipelines.
In the
Incoming Data Pipelines
search bar, search for any pipeline you built. You can search by elements, such as
pipeline name
or
components
. The search results display the pipeline's processors and a summary of its configuration.
From the pipeline summary, you can do any of the following actions:
Review the processor configurations.
Copy configuration details.
Click
Open in Bindplane
to access and manage the pipeline directly within the Bindplane console.
View configured feeds
To view configured feeds in your system, do the following:
In the Google SecOps console, go to
SIEM Settings > Feeds
. The
Feeds
page shows all the feeds that you configured in your system.
Hold the pointer over each row to display the ⋮
More
menu, where you can view feed details, edit, disable, or delete the feed.
Click
View Details
to view the details window.
Click
Open in Bindplane
to open the stream configuration for that feed in the Bindplane console.
View data processing details (available log types)
To view data processing details on the
Available Log Types
page, where you can view all available log types, do the following:
In the Google SecOps console, go to
SIEM Settings > Available Log Types
. The main page displays all your log types.
Hold the pointer over each feed row to display the
more_vert
More
menu. This menu lets you view, edit, disable, or delete feed details.
Click
View Data Processing
to view the feed's configuration.
Click
Open in Bindplane
to open the processor configuration for that processor in the Bindplane console.
Use Google SecOps data pipeline methods
The
Google SecOps data pipeline methods
provide comprehensive tools to manage your processed data. These data pipeline methods include creating, updating, deleting, and listing pipelines, and associating feeds and log types with pipelines.
Use cases
This section contains examples of typical uses cases that relate to data pipeline methods.
To use the examples in this section, do the following:
Replace the customer-specific parameters (for example, URLs and feed IDs) with parameters that suit your own environment.
Insert your own authentication. In this section, the bearer tokens are redacted with
******
.
List all pipelines in a specific Google SecOps instance
The following command lists all pipelines that exist in a specific Google SecOps instance:
curl --location 'https://abc.def.googleapis.com/v123/projects/projectabc-byop/locations/us/instances/aaaa1aa1-111a-11a1-1111-11111a1aa1aa/logProcessingPipelines' \
--header 'Authorization: Bearer ******'
Create a basic pipeline with the one processor
To create a basic pipeline with the Transform processor and associate three sources with it, do the following:
Run the following command:
curl --location 'https://abc.def.googleapis.com/v123/projects/projectabc-byop/locations/us/instances/aaaa1aa1-111a-11a1-1111-11111a1aa1aa/logProcessingPipelines' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ******' \
--data '{
    "displayName": "Example Pipeline",
    "description": "My description",
    "processors": [
        {
            "transformProcessor": {
                "statements": [
                    "set(attributes[\"myKey1\"], \"myVal1\")",
                    "set(attributes[\"myKey2\"], \"myVal2\")"
                ]
            }
        }
    ]
}'
From the response, copy the value of the
displayName
field.
Run the following command to associate three streams (log type, log type with collector ID, and feed) with the pipeline. Use the value of the
displayName
field as the
{pipelineName}
value.
curl --location 'https://abc.def.googleapis.com/v123/{pipelineName}:associateStreams' \
    --header 'Content-Type: application/json' \
--header 'Authorization: Bearer ******' \
--data '{
    "streams": [
        {
            "logType": "MICROSOFT_SENTINEL"
        },
        {
            "logType": "A10_LOAD_BALANCER",
            "collectorId": "dddddddd-dddd-dddd-dddd-dddddddddddd"
        },
        {
            "feed": "1a1a1a1a-1a1a-1a1a-1a1a-1a1a1a1a1a1a"
        }
    ]
}'
Create a pipeline with three processors
The pipeline uses the following processors:
Transform
: Transforms and parses the log body as JSON.
Filter
: Filters out logs that match a condition based on the parsed body.
Redaction
: Redacts data that matches Bindplane's preset sensitive values.
To create a pipeline and associate a three sources with it, do the following:
Run the following command:
curl --location 'https://abc.def.googleapis.com/v123/projects/projectabc-byop/locations/us/instances/aaaa1aa1-111a-11a1-1111-11111a1aa1aa/logProcessingPipelines' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ******' \
--data-raw '{
    "displayName": "My Pipeline 2",
    "description": "My description 2",
    "processors": [
        {
            "transformProcessor": {
                "statements": [
                    "merge_maps(\n  body,\n  ParseJSON(\n    body\n  ),\n  \"upsert\"\n) where IsMap(body) and true\n",
                    "set(\n  body,\n  ParseJSON(\n    body\n  )\n) where not IsMap(body) and true\n"
                ],
                "errorMode": "IGNORE"
            }
        },
        {
            "filterProcessor": {
                "logConditions": [
                    "true and severity_number != 0 and severity_number < 9"
                ]
            }
        },
        {
            "redactProcessor": {
                "blockedValues": [
                    "\\b[A-Z]{2}\\d{2}(?: ?[A-Z0-9]){11,31}(?:\\s[A-Z0-9])*\\b",
                    "\\b([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}\\b",
                    "\\b(?:(?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))\\b",
                    "\\b(?:(?:19|20)?\\d{2}[-/])?(?:0?[1-9]|1[0-2])[-/](?:0?[1-9]|[12]\\d|3[01])(?:[-/](?:19|20)?\\d{2})?\\b",
                    "\\b[a-zA-Z0-9._/\\+\\-—|]+@[A-Za-z0-9\\-—|]+\\.[a-zA-Z|]{2,6}\\b",
                    "\\b(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\\b",
                    "\\b(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\\b",
                    "\\b((\\+|\\b)[1l][\\-\\. ])?\\(?\\b[\\dOlZSB]{3,5}([\\-\\. ]|\\) ?)[\\dOlZSB]{3}[\\-\\. ][\\dOlZSB]{4}\\b",
                    "\\+[1-9]\\d{0,2}(?:[-.\\s]?\\(?\\d+\\)?(?:[-.\\s]?\\d+)*)\\b",
                    "\\b\\d{3}[- ]\\d{2}[- ]\\d{4}\\b",
                    "\\b[A-Z][A-Za-z\\s\\.]+,\\s{0,1}[A-Z]{2}\\b",
                    "\\b\\d+\\s[A-z]+\\s[A-z]+(\\s[A-z]+)?\\s*\\d*\\b",
                    "\\b\\d{5}(?:[-\\s]\\d{4})?\\b",
                    "\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\\b"
                ],
                "allowAllKeys": true,
                "allowedKeys": [
                    "__bindplane_id__"
                ],
                "ignoredKeys": [
                    "__bindplane_id__"
                ],
                "redactAllTypes": true
            }
        }
    ]
}'
From the response, copy the value of the
displayName
field.
Run the following command to associate three streams (log type, log type with collector ID, and feed) with the pipeline. Use the value of the
displayName
field as the
{pipelineName}
value.
curl --location 'https://abc.def.googleapis.com/v123/{pipelineName}:associateStreams' \
    --header 'Content-Type: application/json' \
--header 'Authorization: Bearer ******' \
--data '{
    "streams": [
        {
            "logType": "MICROSOFT_SENTINEL"
        },
        {
            "logType": "A10_LOAD_BALANCER",
            "collectorId": "dddddddd-dddd-dddd-dddd-dddddddddddd"
        },
        {
            "feed": "1a1a1a1a-1a1a-1a1a-1a1a-1a1a1a1a1a1a"
        }
    ]
}'
Need more help?
Get answers from Community members and Google SecOps professionals.
