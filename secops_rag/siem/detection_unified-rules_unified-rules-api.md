# Manage unified rules with the Rules API

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/unified-rules/unified-rules-api/  
**Scraped:** 2026-03-05T09:31:23.243980Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Manage unified rules with the Rules API
Supported in:
Google secops
SIEM
The Rules API provides programmatic endpoints to manage both custom and
curated rules. This document outlines how to use the Rules API to to manage
custom and curated rules programmatically.
Use the Rules API to perform the following tasks:
Search and list rules:
Execute structured searches, sort results, and
retrieve expanded rule resources.
View curated rule details:
Fetch read-only metadata, applied tags, and
raw text logic for Google-authored rules.
Batch modify rule configurations:
Synchronously update live states,
alerting states, archive statuses, and tag assignments across multiple rules.
Search rules using list rules
The
rules.list
method supports expanded rule resources and structured search.
To query these detailed resources, use one of the following views:
CONFIG_ONLY
TRENDS
Both views provide expanded information, which includes the following:
Rule deployment information (live rule enablement, alerting enablement,
archived state, execution state)
Associated rule tags
Access to curated rule resources in
CONFIG_ONLY
view
Larger page size of 5,000 results in
CONFIG_ONLY
view
Robust structured search capabilities.
Sort search results on the rule resource fields using
order_by
in the
rules.list
request. The following rule fields are supported:
alerting_enabled
archived
author
create_time
display_name
execution_state
live_mode_enabled
revision_create_time
rule_id
rule_owner
severity
type
update_time
Example request:
HTTP
GET
https
:
//
chronicle
.
googleapis
.
com
/
v1alpha
/
projects
/
<
ID
>
/
locations
/
us
/
instances
/
<
ID
>
/
rules
?
filter
=
archived
%
3
Dfalse&pageSize
=
100
&
pageToken
=
&
view
=
TRENDS
Example response:
JSON
{
  "rules": [
    {
      "name": "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/rules/ru_fd3fe28c-2d7b-4f7e-9fca-4fdd6029d228",

      "revisionId": "v_1719339990_701951000",

      "displayName": "SomaMaglevProberRule",

      "author": "test@google.com",

      "metadata": {
        "description": "enabled live rule used for maglev rules latency prober"

      },

      "createTime": "2024-06-25T18:26:30.701951Z",

      "revisionCreateTime": "2024-06-25T18:26:30.701951Z",

      "type": "SINGLE_EVENT",

      "etag": "CNaX7LMGEJjY284C",

      "nearRealTimeLiveRuleEligible": true,

      "ruleOwner": "CUSTOMER",

      "alertingEnabled": true,

      "liveModeEnabled": true,

      "runFrequency": "LIVE",

      "currentDayDetectionCount": 10000,

      "executionState": "DEFAULT"

    },
    {
      "name": "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/rules/ru_fbf56bf1-ea5f-4b5b-bbe9-e91e13f3b3b3",

      "revisionId": "v_1696452642_197471000",

      "displayName": "LoadTestingRule",

      "author": "loadtesting@google.com",

      "createTime": "2023-10-04T20:50:42.197471Z",

      "revisionCreateTime": "2023-10-04T20:50:42.197471Z",

      "type": "SINGLE_EVENT",

      "etag": "CKKg96gGEJjWlF4=",

      "nearRealTimeLiveRuleEligible": true,

      "ruleOwner": "CUSTOMER",

      "alertingEnabled": true,

      "liveModeEnabled": true,

      "runFrequency": "LIVE",

      "executionState": "DEFAULT"
    }
  ]
}
View curated rule details using getRule and listRules
The
rules.getRule
and
rule.listRules
support fetching details for curated rules.
rule.listRules
responses can be filtered to only curated rules using the
rule_owner: "GOOGLE"
filter. More details on usage of the
rule_owner
filter
can be found in the rule search syntax section.
Example listRules request to read a curated rule:
HTTP
GET https://chronicle.googleapis.com/v1alpha/projects/<ID>/locations/us/instances/<ID>/rules?filter=rule_owner%3A%22GOOGLE%22pageSize=1&view=TRENDS
Example response:
JSON
{
  "rules": [
    {
      "name": "projects/<ID>/locations/us/instances/<ID>/rules/ur_e34bf150-6cfb-494c-ad9d-ec8f7216a03c",

      "revisionId": "v_1755272664_971453000",

      "displayName": "Example Curated Rule",

      "severity": {
        "displayName": "Info"
      },

      "metadata": {
        "technique": "T1136.003",
        "rule_name": "Example Curated Rule",
        "description": "Example Curated Rule Description",
        "tactic": "TA0003"
      },

      "createTime": "2024-10-02T18:10:43.647897Z",

      "revisionCreateTime": "2025-08-15T15:44:24.971453Z",

      "type": "SINGLE_EVENT",

      "etag": "CNir/cQGEMjknM8D",

      "nearRealTimeLiveRuleEligible": true,

      "ruleOwner": "GOOGLE",

      "tags": [
        "google.mitre.tactic.ta0003",
        "google.mitre.technique.t1136.003"
      ],

      "executionState": "DEFAULT"
    }
  ]
}
rule.getRule method supports fetching a curated rule using its resource name.
Example getRule request to fetch curated rules:
HTTP
GET https://chronicle.googleapis.com/v1alpha/projects/<ID>/locations/us/instances/<ID>/rules/ur_e34bf150-6cfb-494c-ad9d-ec8f7216a03c?view=BASIC
Example response:
JSON
{
  "rules": [
    {
      "name": "projects/<ID>/locations/us/instances/<ID>/rules/ur_e34bf150-6cfb-494c-ad9d-ec8f7216a03c",

      "revisionId": "v_1755272664_971453000",

      "displayName": "Example Curated Rule",

      "severity": {
        "displayName": "Info"
      },

      "metadata": {
        "technique": "T1136.003",
        "rule_name": "Example Curated Rule",
        "description": "Example curated rule description",
        "tactic": "TA0003"
      },

      "createTime": "2024-10-02T18:10:43.647897Z",

      "revisionCreateTime": "2025-08-15T15:44:24.971453Z",

      "text": "Example curated rule text",

      "type": "SINGLE_EVENT",

      "etag": "CNir/cQGEMjknM8D",

      "nearRealTimeLiveRuleEligible": true,

      "ruleOwner": "GOOGLE",

      "tags": [
        "google.mitre.tactic.ta0003",
        "google.mitre.technique.t1136.003"
      ],

      "executionState": "DEFAULT"
    }
  ]
}
Batch modify rule configuration with modifyRules
The
rules.modifyRules
method supports the following batch update on custom
rules and curated rules:
Update live rule status
Update alerting status
Update applied tags
Update archive status (for custom rules only)
Batch updates are executed synchronously and independently. The process is
non-atomic and continues despite individual failures. Partial
failures are detailed in the
failed_requests
field, a map where the key
represents the index of the failed request and the value provides the reason
for failure. Successful updates are documented in the
rule_updates
field,
where the result for each request is placed at its corresponding index
from the original batch.
Example
modifyRules
request:
HTTP
POST https://chronicle.googleapis.com/v1alpha/projects/<ID>/locations/us/instances/<ID>/rules:modifyRules
JSON
{
  "parent": "projects/<ID>/locations/us/instances/<ID>",
  "requests": [
    {
      "update_mask": "liveModeEnabled",
      "rule": {
        "name": "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/rules/ru_aaaaaaaaaaaaaaaaaaaaaaa",
        "liveModeEnabled": true
      }
    },
    {
      "update_mask": "alertingEnabled",
      "rule": {
        "name": "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/rules/ur_zzzzzzzzzzzzzzzzzzzzz",
        "alertingEnabled": false
      }
    },
    {
      "update_mask": "tags",
      "rule": {
        "name": "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/rules/ru_bbbbbbbbbbbbbbbbbbbbbbb",
        "tags": [
          "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/google.mitre.tactic.TA0043",
          "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/google.mitre.technique.T1595"
        ]
      }
    },
    {
      "update_mask": "archived",
      "rule": {
        "name": "projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/rules/ru_cccccccccccccccccccccc",
        "archived": true
      }
    }
  ]
}
Example response:
JSON
{
  "failed_requests": {
    "0": {
      "code": 5,
      "message": "rule is already enabled"
    },
    "3": {
      "code": 5,
      "message": "rule is already archived"
    }
  },
  "rule_updates": [
    {},
    { "alerting_state_updated": true },
    { "tagsUpdated": true },
    {}
  ]
}
Guidelines for updating curated rules
When you modify the live or alerting statuses for curated rules, consider the
following:
Independent control:
You can manage a rule's status independently from
its parent rule set policy. If a rule's status diverges from the parent policy,
your custom setting persists until the parent policy receives its next update.
Entitlement requirement:
You can only update these statuses if your
instance is actively entitled to the parent rule pack.
Guidelines for updating tags
You can associate tags with your rules using the following methods:
Include MITRE T-codes (tactic or technique) in the
tactic
,
technique
,
or
mitre_ttp
meta fields in the rule text.
Specify the full tag resource names in the
tags
meta field of the rule text.
Specify full tag resource names using
ModifyRule
API requests.
The
ModifyRules
API supports MITRE
tactic
and
technique
tags. Any tags
provided in an API update overwrite existing tags, except for those inferred
directly from the rule text.
Google-managed MITRE
tactic
tags use the
google.mitre.tactic
namespace prefix.
Example of a full resource name for the
TA0001
tactic tag:
projects/11344677023/locations/eu/instances/e902a911-16e3-4c39-978d-e25234232492/google.mitre.tactic.TA0001
Need more help?
Get answers from Community members and Google SecOps professionals.
