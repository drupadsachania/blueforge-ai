# Applied Threat Intelligence Fusion Feed overview

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/ati-fusion-feed/  
**Scraped:** 2026-03-05T09:33:18.791718Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Applied Threat Intelligence Fusion Feed overview
Supported in:
Google secops
SIEM
The Applied Threat Intelligence (ATI) Fusion Feed is a collection of Indicators of Compromise
(IoCs), including hashes, IPs, domains, and URLs, that are associated with known
threat actors, malware strains, active campaigns, and finished intelligence reporting. The feed also includes IoCs from open-source feeds that Mandiant Intelligence has carefully checked and validated, which maximizes value and provides high accuracy.
Mandiant's curation process includes the following phases:
Frontline incident response: While investigating breaches, Mandiant analysts gain first-hand knowledge of
attacker tools and techniques.
Threat research: Dedicated teams track threat actors, analyze malware, and
uncover emerging attack infrastructure.
Contextualization: IoCs are mapped to specific threats and campaigns, which
helps in understanding and prioritizing incidents.
The Breach Analytics feed builds upon the ATI Fusion Feed by including indicators from new and active Mandiant breach investigations. It provides real-time insights into the latest attack trends. To enhance indicator matching, YARA-L rules can use contextual information from the ATI Fusion Feed, such as associated threat groups, an indicator's presence in compromised environments, or Mandiant's automated maliciousness score.
Write YARA-L rules with the ATI Fusion Feed
Writing YARA-L rules that use the ATI Fusion Feed in Google Security Operations follows a similar process to writing YARA-L rules that use other context entity sources. For more information, see
Create context-aware analytics
.
Events and match sections
To write a rule, follow these steps:
1. Filter the selected context entity graph. In this case,
Fusion Feed
. 
1. Filter a specific indicator type. For example,
FILE
. See the following example:
events:
   $context_graph.graph.metadata.product_name = "MANDIANT_FUSION_IOC"
   $context_graph.graph.metadata.vendor_name = "MANDIANT_FUSION_IOC"
   $context_graph.graph.metadata.source_type = "GLOBAL_CONTEXT"
   $context_graph.graph.metadata.entity_type = "FILE"
You can add any other conditions of the event or context entity in the
events
section. You can join a field from the context entity and UDM event field.
In the following example, the placeholder variable
ioc
is used to do a transitive join between the context entity and the event. The
ioc
variable is then used in the
match
section to make sure there's a match in a specific timeframe.
$ioc = $context_graph.graph.entity.file.md5
   $ioc = $e1.principal.process.file.md5

match:
   $ioc over 1h
For more information about context entity fields that can be used in YARA-L rules, see the
Fusion Feed context entity fields
section.
Outcome section
Continuing with the previous example, the basic indicator matching rule is set up
against file hashes in the context entities in the
graph.entity.file.md5
field and
principal.process.file.md5
UDM field.
Because this rule can match a large number of events, it is recommended that you refine the rule to match on context entities that have specific intelligence. For example, you may want to match on the confidence score that Mandiant assigned to the indicator, whether it was seen in a breached environment or the malware family associated with the indicator. This can all be done in the
outcome
section of the rule.
outcome:
   // Extract the Mandiant Automated Intel confidence score of maliciousness
   $confidence_score = max(if($context_graph.graph.metadata.threat.verdict_info.source_provider = "Mandiant Automated Intel", $context_graph.graph.metadata.threat.verdict_info.confidence_score, 0))
   // Extract the status of the indicator as seen in a breached environment
   $breached = max(if($context_graph.graph.metadata.threat.verdict_info.pwn = true, 1, 0))

   // Intermediary outcome variable to combine conditions of intelligence extracted in the previous outcome variables.
   // Return 1 if conditions are met, otherwise return 0.
   $matched_conditions = if($confidence_score >= 80 AND $breached = 1, 1, 0)
In the
outcome
section of the YARA-L rule, the confidence score is
extracted using an
if statement
wrapped in a
max
function. This technique is
required for multi-event rules. The same technique is used to extract the
pwn
variable from
verdict_info
, which indicates whether an
indicator has been seen in a breached environment identified by Mandiant.
These two outcome variables are then combined together in another
matched_conditions
variable, which allows the use of chained logic
in the
condition
section.
Condition section
The
condition
section ensures that
e1
,
context_graph
, and
matched_conditions
exist and or
match the specified condition.
condition:
   // Ensure $e1, $context_graph and $matched_conditions conditions are met.
   $e1 AND $context_graph AND $matched_conditions = 1
Complete YARA-L rule
At this point the rule is ready for use and should look like the following:
rule fusion_feed_example_principal_process_file_md5 {
 meta:
   rule_name = "File Hash - Applied Threat Intelligence"
   description = "Matches file hashes against the Applied Threat Intelligence Fusion Feed."

 events:
   // Filter graph
   $context_graph.graph.metadata.product_name = "MANDIANT_FUSION_IOC"
   $context_graph.graph.metadata.vendor_name = "MANDIANT_FUSION_IOC"
   $context_graph.graph.metadata.entity_type = "FILE"
   $context_graph.graph.metadata.source_type = "GLOBAL_CONTEXT"

   // Do join
   $ioc = $context_graph.graph.entity.file.md5
   $ioc = $e1.principal.process.file.md5

 match:
   $ioc over 1h

 outcome:
   // Extract the Mandiant Automated Intel confidence score of maliciousness
   $confidence_score = max(if($context_graph.graph.metadata.threat.verdict_info.source_provider = "Mandiant Automated Intel", $context_graph.graph.metadata.threat.verdict_info.confidence_score, 0))
   // Extract the status of the indicator as seen in a breached environment
   $breached = max(if($context_graph.graph.metadata.threat.verdict_info.pwn = true, 1, 0))

   // Intermediary outcome variable to combine conditions of intelligence extracted in the previous outcome variables.
   // Return 1 if conditions are met, otherwise return 0.
   $matched_conditions = if($confidence_score >= 80 AND $breached = 1, 1, 0)

 condition:
   // Ensure $e1, $context_graph and $matched_conditions conditions are met.
   $e1 AND $context_graph AND $matched_conditions = 1
}
ATI Fusion Feed context entity fields
You can use many fields from the ATI Fusion Feed in rules. These fields
are all defined in the
Unified Data Model field list
.
The following fields are relevant for prioritizing indicators:
Entity field
Possible values
metadata.threat.associations.type
MALWARE
,
THREAT_ACTOR
metadata.threat.associations.name
Threat association name
metadata.threat.verdict_info.pwn
TRUE
,
FALSE
metadata.threat.verdict_info.pwn_first_tagged_time.seconds
Timestamp (seconds)
Some fields have key-value pairs that need to be used in combination to access
the correct values. For example:
Entity field 1
Values
Entity field 2
Values
metadata.threat.verdict_info.source_provider
Mandiant Global Intel
metadata.threat.verdict_info.global_hits_count
Integer
metadata.threat.verdict_info.source_provider
Mandiant Global Intel
metadata.threat.verdict_info.global_customer_count
Integer
metadata.threat.verdict_info.source_provider
Mandiant Analyst Intel
metadata.threat.verdict_info.confidence_score
Integer
metadata.threat.verdict_info.source_provider
Mandiant Automated Intel
metadata.threat.verdict_info.confidence_score
Integer
In the
outcome
section of a YARA-L rule, you can access a value designated
by a specific key using the following command:
$hit_count = max(if($context_graph.graph.metadata.threat.verdict_info.source_provider = "Mandiant Global Intel", $context_graph.graph.metadata.threat.verdict_info.global_hits_count, 0))
Examining entity matches in Google Security Operations helps you gain a comprehensive view of
the data, revealing additional fields that can be valuable in assessing the
priority and context of an indicator alert.
The following example shows a Fusion Feed context entity as an initial reference point:
{
  "metadata": {
    "product_entity_id": "md5--147d19e6-cdae-57bb-b9a1-a8676265fa4c",
    "collected_timestamp": {
      "seconds": "1695165683",
      "nanos": 48000000
    },
    "vendor_name": "MANDIANT_FUSION_IOC",
    "product_name": "MANDIANT_FUSION_IOC",
    "product_version": "1710194393",
    "entity_type": "FILE",
    "creation_timestamp": {
      "seconds": "1710201600"
    },
    "interval": {
      "start_time": {
        "seconds": "1"
      },
      "end_time": {
        "seconds": "253402300799"
      }
    },
    "threat": [
      {
        "category_details": [
          "A phishing email message or the relevant headers from a phishing email."
        ],
        "severity_details": "HIGH",
        "confidence_details": "75",
        "risk_score": 75,
        "first_discovered_time": {
          "seconds": "1683294326"
        },
        "associations": [
          {
            "id": "threat-actor--3e5e6bdf-5b4e-5166-84fa-83045e637f23",
            "type": "THREAT_ACTOR",
            "name": "UNC2633"
          },
          {
            "id": "threat-actor--3e5e6bdf-5b4e-5166-84fa-83045e637f23",
            "country_code": [
              "unknown"
            ],
            "type": "THREAT_ACTOR",
            "name": "UNC2633",
            "description": "UNC2633 is a distribution threat cluster that delivers emails containing malicious attachments or links that lead to malware payloads, primarily QAKBOT, but also SNOWCONE.GZIPLOADER (which leads to ICEDID) and MATANBUCHUS. Historically, UNC2633 has distributed ZIP files containing malicious Excel files that download malware payloads. In early 2023, UNC2633 started distributing OneNote files (.one) that usually led to QAKBOT. It has also leveraged HTML smuggling to distribute ZIP files containing IMG files that contain LNK files and malware payloads.",
            "alias": [
              {
                "name": "TA570 (Proofpoint)"
              }
            ],
            "first_reference_time": {
              "seconds": "1459085092"
            },
            "last_reference_time": {
              "seconds": "1687392000"
            },
            "industries_affected": [
              "Aerospace & Defense",
              "Agriculture",
              "Automotive",
              "Chemicals & Materials",
              "Civil Society & Non-Profits",
              "Construction & Engineering",
              "Education",
              "Energy & Utilities",
              "Financial Services",
              "Governments",
              "Healthcare",
              "Hospitality",
              "Insurance",
              "Legal & Professional Services",
              "Manufacturing",
              "Media & Entertainment",
              "Oil & Gas",
              "Pharmaceuticals",
              "Retail",
              "Technology",
              "Telecommunications",
              "Transportation"
            ]
          }
        ],
        "campaigns": [
          "CAMP.23.007"
        ],
        "last_updated_time": {
          "seconds": "1695165683",
          "nanos": 48000000
        },
        "verdict_info": [
          {
            "source_provider": "Mandiant Automated Intel",
            "confidence_score": 75
          },
          {
            "verdict_type": "ANALYST_VERDICT",
            "confidence_score": 75
          },
          {
            "source_count": 91,
            "response_count": 1,
            "verdict_type": "PROVIDER_ML_VERDICT",
            "malicious_count": 1,
            "ioc_stats": [
              {
                "ioc_stats_type": "MANDIANT_SOURCES",
                "second_level_source": "Knowledge Graph",
                "quality": "HIGH_CONFIDENCE",
                "malicious_count": 1,
                "response_count": 1,
                "source_count": 8
              },
              {
                "ioc_stats_type": "MANDIANT_SOURCES",
                "second_level_source": "Malware Analysis",
                "source_count": 4
              },
              {
                "ioc_stats_type": "MANDIANT_SOURCES",
                "second_level_source": "Spam Monitoring",
                "source_count": 1
              },
              {
                "ioc_stats_type": "THIRD_PARTY_SOURCES",
                "second_level_source": "Crowdsourced Threat Analysis",
                "source_count": 71
              },
              {
                "ioc_stats_type": "THIRD_PARTY_SOURCES",
                "first_level_source": "MISP",
                "second_level_source": "Trusted Software List",
                "source_count": 3
              },
              {
                "ioc_stats_type": "THIRD_PARTY_SOURCES",
                "first_level_source": "Threat Intelligence Feeds",
                "second_level_source": "Digitalside It Hashes",
                "source_count": 1
              },
              {
                "ioc_stats_type": "THIRD_PARTY_SOURCES",
                "first_level_source": "Threat Intelligence Feeds",
                "second_level_source": "Tds Harvester",
                "source_count": 1
              },
              {
                "ioc_stats_type": "THIRD_PARTY_SOURCES",
                "first_level_source": "Threat Intelligence Feeds",
                "second_level_source": "Urlhaus",
                "source_count": 1
              }
            ]
          },
          {
            "source_provider": "Mandiant Analyst Intel",
            "confidence_score": 75,
            "pwn": true,
            "pwn_first_tagged_time": {
              "seconds": "1683911695"
            }
          }
        ],
        "last_discovered_time": {
          "seconds": "1683909854"
        }
      }
    ],
    "source_type": "GLOBAL_CONTEXT",
    "source_labels": [
      {
        "key": "is_scanner",
        "value": "false"
      },
      {
        "key": "osint",
        "value": "false"
      },
      {
        "key": "misp_akamai",
        "value": "false"
      },
...
      {
        "key": "has_pwn",
        "value": "2023-05-12T17:14:55.000+0000"
      }
    ],
    "event_metadata": {
      "id": "\\000\\000\\000\\000\\034Z\\n\\2545\\237\\367\\353\\271\\357\\302\\215t\\330\\275\\237\\000\\000\\000\\000\\007\\000\\000\\000\\206\\000\\000\\000",
      "base_labels": {
        "log_types": [
          "MANDIANT_FUSION_IOC"
        ],
        "allow_scoped_access": true
      }
    }
  },
  "entity": {
    "file": {
      "sha256": "000bc5900dc7a32851e380f418cc178ff0910242ee0561ae37ff424e6d3ec64a",
      "md5": "f0095b0a7480c826095d9ffc9d5d2d8f",
      "sha1": "8101315b9fbbf6a72bddbfe64837d246f4c8b419"
    },
    "labels": [
      {
        "key": "is_scanner",
        "value": "false"
      },
      {
        "key": "osint",
        "value": "false"
      },
      {
        "key": "misp_akamai",
        "value": "false"
      },
...
    ]
  }
}
Complex conditions
To use multiple fields in a context entity, you can combine
multiple outcome variables to create more complex conditional logic. Intermediary outcome variables can be used to combine multiple fields. These variables are then combined to form a new outcome variable that can be used in the
condition
section.
For example:
// Value will be 1 if threat.associations.type = "MALWARE"
// Wrapper max function required for multi-event rules
$is_attributed_malware = max(if($entity_context.graph.metadata.threat.associations.type = "MALWARE", 1, 0))

// Value will be 1 if threat.associations.type = "THREAT_ACTOR"
$is_attributed_actor = max(if($entity_context.graph.metadata.threat.associations.type = "THREAT_ACTOR", 1,0))

// Value will be the sum of the $is_attributed_malware $is_attributed_malware and $is_attributed_actor
$is_attributed = if($is_attributed_malware = 1, 1, 0)
                    +
                    if($is_attributed_actor = 1, 1, 0)

// If the value of $is_attributed is greater than 1, this indicates the indicator has been attributed at least once with the type "MALWARE" or "THREAT_ACTOR"
In this example, two intermediary outcome variables,
is_attributed_malware
and
is_attributed_actor
, are combined in an outcome variable
is_attributed
.
The intermediary outcome values return numerical values, which
allows numerical comparisons in the new outcome variable.
The value in
is_attributed
will be 1 or greater if
the indicator has at least one threat association of type
MALWARE
or
THREAT_ACTOR
.
Flexible joins in YARA-L rule
To reduce the number of rules required, you can use flexible joins between IoCs to connect multiple UDM fields to a context entity.
The following example shows the use of flexible joins for multiple UDM fields in the
event
section:
events:
    // Filter graph
    $mandiant.graph.metadata.product_name = "MANDIANT_FUSION_IOC"
    $mandiant.graph.metadata.vendor_name = "MANDIANT_FUSION_IOC"
    $mandiant.graph.metadata.entity_type = "FILE"
    $mandiant.graph.metadata.source_type = "GLOBAL_CONTEXT"

    $mandiant.graph.entity.file.md5 = strings.coalesce($e.target.process.file.md5, $e.target.process.file.md5) OR
    $mandiant.graph.entity.file.md5 = strings.coalesce($e.principal.process.file.md5, $e.principal.process.file.md5)
Need more help?
Get answers from Community members and Google SecOps professionals.
