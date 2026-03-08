# DataTap Configuration

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/datatapconfig-api/  
**Scraped:** 2026-03-05T09:37:38.732819Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
DataTap Configuration
Supported in:
Google secops
SIEM
This document explains how to use DataTap Configuration to transmit normalized or filtered events to Cloud Pub/Sub. It also describes how to manage the Pub/Sub topics where events are delivered.
Examples (in Python) for making OAuth authenticated requests to the Backstory API are provided for each API call referenced in this document.
Regional Endpoints
Google SecOps provides regional endpoints for each API.
Canada                      https://northamerica-northeast2-backstory.googleapis.com
Dammam                      https://me-central2-backstory.googleapis.com
Doha                        https://me-central1-backstory.googleapis.com
Europe Multi-Region         https://europe-backstory.googleapis.com
Frankfurt                   https://europe-west3-backstory.googleapis.com
London                      https://europe-west2-backstory.googleapis.com
Mumbai                      https://asia-south1-backstory.googleapis.com
Singapore                   https://asia-southeast1-backstory.googleapis.com
Sydney                      https://australia-southeast1-backstory.googleapis.com
Tel Aviv                    https://me-west1-backstory.googleapis.com
Tokyo                       https://asia-northeast1-backstory.googleapis.com
Turin                       https://europe-west12-backstory.googleapis.com
United States Multi-Region  https://backstory.googleapis.com
Zurich                      https://europe-west6-backstory.googleapis.com
For example:
https://backstory.googleapis.com/v1/dataTaps
https://europe-backstory.googleapis.com/v1/dataTaps
https://asia-southeast1-backstory.googleapis.com/v1/dataTaps
Before you begin
Give publisher role to
publisher@chronicle-data-tap.iam.gserviceaccount.com
on your Pub/Sub Topic.
Specifying Topic
When creating or updating DataTap configurations, it's necessary to specify the Pub/Sub topic where the events are sent to. This is done by specifying the Pub/Sub topic using the following format:
projects/<project_id>/topics/<topicId>
Specifying Filter
Filter defines which events are published to the topic specified by the DataTap configuration. Valid values for filter are as follows:
ALL_UDM_EVENTS
: All events are sent to the topic.
LABELED_UDM_EVENTS
: Only events detected for Google Security Operations Detection Engine rules that filter on a single event and specify a
dataTapLabel
that is
ENABLED
. To create a rule with a
dataTapLabel
, see
Use rules in a DataTap configuration
.
Specifying serializationFormat
serializationFormat defines the format for sent events. Valid values for serializationFormat include:
JSON: Events are sent in JSON format.
MARSHALLED_PROTO: Events are sent in proto format.
The default value is MARSHALLED_PROTO.
DataTap Configuration API Reference
This section describes the DataTap Configuration API methods.
Create
Creates a DataTap configuration.
Request
POST https://backstory.googleapis.com/v1/dataTaps
URL parameters
None
Request Body
{
  "displayName": "<Name of the DataTap>",
  "cloudPubsubSink": {
    "topic": "<topicId>",
  },
  "filter": "<filter>",
  "serializationFormat": "<serializationFormat>"
}
Body Parameters
Parameter Name
Type
Required
Description
displayName
string
Yes
Name for the DataTap configuration being created.
topic
string
Yes
TopicId where events are to be sent.
Use the following format:
projects/<project_id>/topics/<topicId>
filter
enum
Yes
ALL_UDM_EVENTS: Retrieve all normalized events.
ALERT_UDM_EVENTS: Retrieve all alert events.
LABELED_UDM_EVENTS: Retrieves events detected for Google SecOps Detection Engine rules that filter on a single event and specify a
dataTapLabel
that is
ENABLED
. To create a rule with a
dataTapLabel
, see
Use rules in a DataTap configuration
.
serializationFormat
enum
No
JSON: Retrieve events in JSON format.
MARSHALLED_PROTO: Retrieve events in proto format.
Sample Request
https://backstory.googleapis.com/v1/dataTaps
{
  "displayName": "tap1",
  "cloudPubsubSink": {
    "topic": "projects/sample-project/topics/sample-topic",
  },
  "filter": "LABELED_UDM_EVENTS",
  "serializationFormat": "JSON"
}
Response
Sample Response
{
  "customerId": "cccccccc-cccc-cccc-cccc-cccccccccccc",
  "tapId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
  "displayName": "tap1",
  "cloudPubsubSink": {
    "topic": "projects/sample-project/topics/sample-topic",
  },
  "filter": "LABELED_UDM_EVENTS",
  "serializationFormat": "JSON"
}
Update
Updates a DataTap configuration.
Request
PATCH https://backstory.googleapis.com/v1/dataTaps/<tapId>
URL parameters
Parameter Name
Type
Required
Description
tapId
string
Yes
tapId given in response when the DataTap configuration was created.
Request Body
{
  "name": "dataTaps/<tapId>",
  "displayName": "<Name of the DataTap>",
  "cloudPubsubSink": {
    "topic": "<topicId>",
  },
  "filter": "<filter>",
  "serializationFormat": "<serializationFormat>"
}
Body Parameters
Parameter Name
Type
Required
Description
name
string
Yes
Use format: dataTaps/<tapId>
tapId given in response when the DataTap configuration was created.
displayName
string
Yes
Name for the DataTap configuration being created.
topic
string
Yes
TopicId where events are to be sent.
Use the following format:
projects/<project_id>/topics/<topicId>
filter
enum
Yes
ALL_UDM_EVENTS: Retrieve all normalized events.
ALERT_UDM_EVENTS: Retrieve all alert events.
serializationFormat
enum
No
JSON: Retrieve events in JSON format.
MARSHALLED_PROTO: Retrieve events in proto format.
Sample Request
https://backstory.googleapis.com/v1/dataTaps/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa

{
  "name": "dataTaps/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
  "displayName": "tap1",
  "cloudPubsubSink": {
    "topic": "projects/sample-project/topics/sample-topic",
  },
  "filter": "ALL_UDM_EVENTS",
  "serializationFormat": "JSON"
}
Response
Sample Response
{
  "customerId": "cccccccc-cccc-cccc-cccc-cccccccccccc",
  "tapId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
  "displayName": "tap1",
  "cloudPubsubSink": {
    "topic": "projects/sample-project/topics/sample-topic",
  },
  "filter": "ALL_UDM_EVENTS",
  "serializationFormat": "JSON"
}
Delete
Deletes a DataTap configuration.
Request
DELETE https://backstory.googleapis.com/v1/dataTaps/<tapId>
URL parameters
Parameter Name
Type
Required
Description
tapId
string
Yes
tapId given in response when the DataTap configuration was created.
Request Body
{
  "name": "dataTaps/<tapId>",
}
Body Parameters
Parameter Name
Type
Required
Description
name
string
Yes
Use the following format: dataTaps/<tapId>
tapId given in response when the DataTap configuration was created.
Sample Request
https://backstory.googleapis.com/v1/dataTaps/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa

{
  "name": "dataTaps/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
}
Response
Sample Response
Returns an empty JSON with 200 OK, indicating the operation has completed successfully.
Get
Get a specific DataTap configuration.
Request
GET https://backstory.googleapis.com/v1/dataTaps/<tapId>
URL parameters
Parameter Name
Type
Required
Description
tapId
string
Yes
tapId given in response when the DataTap configuration was created.
Request Body
{
  "name": "dataTaps/<tapId>",
}
Body Parameters
Parameter Name
Type
Required
Description
name
string
Yes
Use format: dataTaps/<tapId>
tapId given in response when the DataTap configuration was created.
Sample Request
https://backstory.googleapis.com/v1/dataTaps/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa

{
  "name": "dataTaps/aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
}
Response
Sample Response
{
  "customerId": "cccccccc-cccc-cccc-cccc-cccccccccccc",
  "tapId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
  "displayName": "tap1",
  "cloudPubsubSink": {
    "topic": "projects/sample-project/topics/sample-topic",
  },
  "filter": "ALL_UDM_EVENTS",
  "serializationFormat": "MARSHALLED_PROTO"
}
List
List all the DataTap configurations of a customer.
Request
GET https://backstory.googleapis.com/v1/dataTaps
URL parameters
None
Request Body
Empty
Body Parameters
None
Sample Request
https://backstory.googleapis.com/v1/dataTaps
Response
Sample Response
[
  {
    "customerId": "cccccccc-cccc-cccc-cccc-cccccccccccc",
    "tapId": "aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa",
    "displayName": "tap1",
    "cloudPubsubSink": {
      "topic": "projects/sample-project/topics/sample-topic",
    },
    "filter": "ALL_UDM_EVENTS",
    "serializationFormat": "JSON"
  },
  "filter": "ALERT_UDM_EVENTS",
  "serializationFormat": "MARSHALLED_PROTO"
  }
]
