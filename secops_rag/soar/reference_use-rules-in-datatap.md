# Use rules to filter events in a DataTap configuration

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/use-rules-in-datatap/  
**Scraped:** 2026-03-05T10:04:09.412236Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use rules to filter events in a DataTap configuration
Supported in:
Google secops
SIEM
In a DataTap configuration, you can use Detection Engine rules as a filter to define the events that are published to a
Pub/Sub topic
.
To use rules in a DataTap configuration, follow these steps:
Use the Detection Engine API's
CreateRule
endpoint to 
create one or more
single event rules
. When creating each rule, specify a
data_tap_label
in the request body. Keep the rules simple (under 100 lines). For general information about the Detection Engine API, such as how to authenticate, see
Chronicle Detection Engine API
.
Use the DataTap Configuration API's
Create
endpoint to create a DataTap configuration that specifies a
LABELED_UDM_EVENTS
filter.
CreateRule
Create a new rule without setting the rule to live.
Request
POST https://backstory.googleapis.com/v2/detect/rules
Request body
{
  "ruleText": "<rule text here>"
  "labels": "<labels here>"
}
Body parameters
Parameter Name
Type
Required
Description
ruleText
string
Required
Text of the new rule in YARA-L 2.0 format.
labels
RuleLabels
Optional
A set of labels to apply on events that match the rule.
labels.label
RuleLabel
Optional
A label to apply on events that match the rule.
labels.label.state
enum
Optional
Specifies the status of the label. Valid values are:
ENABLED
DISABLED
labels.label.data_tap_label
string
Optional
This label is used to filter the data published on a DataTap 
      configuration that specifies the
LABELED_UDM_EVENTS
filter. If a rule applies a
data_tap_label
to an event, then that event will be published for any
LABELED_UDM_EVENTS
DataTap configuration whose
topicId
matches the
sink_name
specified in the
data_tap_label
.
labels.label.data_tap_label.sink_name
string
Optional
The name of the DataTap configuration. This should match the value of the
displayName
specified in a DataTap configuration.
Sample request
https://backstory.googleapis.com/v2/detect/rules
{
  "ruleText": "rule singleEventRule2 {
    meta:
      author = \"securityuser\"
      description = \"single event rule that should generate detections\"

    events:
      $e.metadata.event_type = \"NETWORK_DNS\"

    condition:
      $e
  }"
  "labels": {
    "label": [
      {
        "state": "ENABLED",
        "data_tap_label": {
          "sink_name": "tap1",
        }
      }
    ]
  }
}
Response
Response fields
The response is the same as for
GetRule
, and it also includes the label fields.
Sample response
{
  "ruleId": "ru_1f54ab4b-e523-48f7-ae25-271b5ea8337d",
  "versionId": "ru_1f54ab4b-e523-48f7-ae25-271b5ea8337d@v_1605892700_409247000",
  "ruleName": "singleEventRule2",
  "metadata": {
    "author": "securityuser",
    "description": "single event rule that should generate detections"
  },
  "ruleText": "rule singleEventRule2 {
      meta:
        author = \"securityuser\"
        description = \"single event rule that should generate detections\"
      events:
        $e.metadata.event_type = \"NETWORK_DNS\"
      condition:
        $e
      }",
  "ruleType": "SINGLE_EVENT",
  "versionCreateTime": "2020-11-20T17:18:20.409247Z",
  "compilationState": "SUCCEEDED",
  "labels": {
    "label": [
      {
        "state": "ENABLED",
        "data_tap_label": {
          "sink_name": "tap1",
        }
      }
    ]
  }
}
