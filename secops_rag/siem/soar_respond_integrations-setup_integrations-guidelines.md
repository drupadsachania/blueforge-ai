# Response integrations community contribution guidelines

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/integrations-guidelines/  
**Scraped:** 2026-03-05T09:35:48.536300Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Response integrations community contribution guidelines
Supported in:
Google secops
SOAR
This document outlines the guidelines for submitting Response 
    Integrations to Google SecOps through community 
    contributions. All submitted integrations undergo a vetting process by the 
    official Google SecOps team, with a focus on the highlighted 
    requirements within this document.
Response integration metadata
Name
The
Name
should correspond to the product name with which the 
    integration is going to be integrated and shouldn't contain any 
    special characters.
The
Display Name
should be written with whitespaces; for example,
Vertex AI
and not
VertexAI
.
Integration Identifier
The
Integration Identifier
is a unique identifier of the 
    integration. After the integration is created, this value can't be changed. 
    The identifier should be the same value as
Name
, but with 
    whitespaces removed.
The identifier is available in most places across the platform.
Description
The
Description
should provide a high-level overview of the 
    product with which the integration is created and shouldn't 
    exceed 500 characters. It must contain the following information:
This integration is owned by the "{vendor name}". Support Contact: {email}.
Avoid putting URLs in the description.
Logos
Each integration should be provided with an SVG icon. This icon should 
    adapt to the themes inside the platform. Icons should only inherit the theme 
    from the platform.
You should validate the logo on the following pages:
Response
>
Integration Setup
Response
>
Playbooks
>
Playbook Designer
Cases
>
Alert
>
Alert Playbook View
The following is an example of an SVG logo, designed to match our style guide:
<?xml version="1.0" encoding="UTF-8"?><svg id="Layer_1" data-name="Layer 1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 21 23"> <defs> <style> .cls-1 { stroke-width: 0px; } </style> </defs> <path class="cls-1" d="M15.51,4.79H5.49c-.4,0-.72.32-.72.72v5.75c0,2.3,1.71,4.15,3.69,5.38.54.34,1.1.62,1.66.86l.09.04c.06.02.12.05.18.06.03,0,.07,0,.1,0,.1,0,.19-.03.28-.07l.09-.04c.76-.33,2.22-1.03,3.46-2.24,1.24-1.22,1.89-2.6,1.89-4v-5.75c0-.4-.32-.72-.72-.72ZM14.32,11.26c0,.88-.44,1.77-1.32,2.63-.65.64-1.55,1.22-2.5,1.68-.95-.46-1.84-1.04-2.5-1.68-.88-.86-1.32-1.75-1.32-2.63v-4.55h7.64v4.55ZM20.28,0H.72c-.4,0-.72.32-.72.72v10.77c0,2.56,1.18,4.99,3.51,7.21,2.29,2.18,5.12,3.56,6.61,4.2l.09.04s.1.04.15.05c.04,0,.09.01.13.01.1,0,.19-.02.28-.06l.09-.04c.53-.23,1.23-.55,2.02-.97,1.42-.75,3.11-1.82,4.59-3.23,2.33-2.22,3.51-4.64,3.51-7.21V.72c0-.4-.32-.72-.72-.72ZM16.17,17.31c-1.9,1.81-4.24,3.04-5.67,3.69-1.43-.65-3.77-1.88-5.67-3.69-1.94-1.84-2.92-3.8-2.92-5.82V1.92h17.18v9.57c0,2.02-.98,3.98-2.92,5.82Z"/></svg>
Be sure to encode the SVG before adding it to the integration definition 
    file, as can be found in other integrations in the Content Hub.
Documentation link
As part of the integration, you can add a link that will point users to 
    the documentation. This documentation is expected to be hosted on your end.
Users can access the documentation link from the
Parameters
section of the
Configure Instance
dialog.
Configuration parameters
All integrations should contain configuration parameters (API Root + Auth 
    parameters), unless the underlying API doesn't require any authentication 
    and the API Root can be hardcoded. For all integrations where authentication 
    is needed, there should be a
Verify SSL
parameter.
All parameters should have a description. The description should help 
    users configure the integration from within the platform. Avoid putting URLs 
    in the description of parameters.
Ping action
The
Ping action
is a special action that is used by the platform 
    to validate API connectivity. This action is mandatory even if your 
    integration doesn't have any other actions. Whenever the user presses the
Test
button inside the integration configuration, it should show an 
    accurate status of the connectivity.
Release notes
The general structure for the release note should follow the following 
    format:
{integration item} - {update}
For example:
Get Case Details - 
    Added ability to fetch information about affected IOCs
Depending on the situation, there are unique release notes for specific 
    scenarios:
If it's a new integration:
New Integration Added - {integration name}
If a new action is added:
New Action Added - {action name}
If a new connector is added:
New Connector Added - {connector name}
If a new job is added:
New Job Added - {job name}
If a predefined widget is added to an action:
{action name} - Added Predefined Widget.
If a predefined widget is updated:
{action name} - Updated Predefined Widget.
For changes that affect all integration items:
Integration - {Update}
For changes that affect all actions:
Integration's Actions - {Update}
For changes that affect all connectors:
Integration's Connectors - {Update}
For changes that affect all jobs:
Integration's Jobs - {Update}
If the release contained a regressive change, then in the release note 
    you need to specify
REGRESSIVE!
. For example,
Google Chronicle - Chronicle Alerts Connector - REGRESSIVE! Updated 
    mapping.
Release notes are available in the
Integration Details
side 
    drawer that's displayed when you click the
Details
button in the 
    integration.
Versioning
Each integration update should be followed by a +1 update to the 
    integration version. Versions should be represented as an integer. Minor 
    versions like 11.1.3 or 11.1 are not allowed.
Tags
Optionally, you can add tags to your integration. Avoid creating new 
    types of tags; use the ones that are already inside the platform. If you 
    don't see a tag that suits you, consult with the vetting team.
General notes
Test every integration content before submission.
Review all integration content for potential vulnerabilities and 
        vulnerable dependencies.
Always use the latest supported version of Python during development 
        (Python 3.11).
Actions
Name
The
Name
of the action should point to the activity that is being 
    performed; for example,
Get Case Details
,
List Entity Events
, 
    or
Execute Search
.
If the action is designed to work primarily with entities, then it's 
    preferred to put
Entity
in the name; for example,
Enrich Entities
.
Action names should be conveyed in 2-3 words.
Description
The
Description
of the action should highlight to the user what 
    will be the outcome of the action execution.
If the action works with entities, then you need to append information 
    about what type of entities are supported. For example:
Add a vote to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported.
If the action works in
Async
mode, then you need to provide the following 
    note in the description:
Note: Action is running as async, adjust script timeout value in Google SecOps IDE for action, as needed.
Try to limit the description to 500 characters.
Action parameters
Action configuration parameters should have an intuitive name. 
    Avoid using special characters and try to limit the action parameter name to 
    2-4 words.
The description for the parameter should explain to the user what 
    impact that parameter has on the action execution. If the parameter supports 
    a predetermined amount of supported values, then inside the description 
    provide the following section:
Possible Values: {value 1}, {value 2}
Action output (script result)
The script result should represent a simple outcome of the action. In 
    most cases, it should just point to a variable called
is_success
, which can take values
true
or
false
.
In general, if the action finished execution and performed an operation,
is_success
should be
true
.
Action output (JSON result)
The JSON Result is the most important output of the action. All of the 
    data available in the JSON result will be accessible during playbook 
    execution. Verify that a valid JSON object is being pushed to the output.
JSON Results have a limit of 15 MB in size.
When building a JSON result, make sure that there are no keys that will 
    be unique during execution. For example, the following JSON object 
    represents a poor structure as it would be unusable inside playbooks:
{
   "10.10.10.10": {
      "is_malicious": "false"
   }
}
Instead, format it like this:
[
   {
      "is_malicious": "false",
      "ip": "10.10.10.10"
   }
]
If you're using entities inside the action and return results Per 
    Entity, then the best practice is to structure the JSON Result like this:
[
   {
       "Entity": "10.10.10.10",
       "EntityResult": {
           "is_malicious": "false",
       }
   }
]
Always consider how the output of the action can be used inside 
    automation.
Make sure that there is a
JSON Sample
for your action.
The JSON sample is used by the platform inside the Expression Builder 
    during the playbook building process. An accurate JSON sample makes the 
    playbook building experience significantly better. Remove any PII 
    information from JSON samples.
Action outputs (entity enrichment)
If actions are executing on entities, then during the action execution 
    you can append additional metadata to them. The structure of that metadata 
    should follow this format:
{integration identifier}_{key}
. For 
    example:
WebRisk_is_malicious
.
You can find the added metadata in the entities details page.
Action outputs (output message)
The output message should explain to the user how the action 
    execution went in a more descriptive manner. It should point the user to the 
    outcome of the action execution.
If some entities were successfully enriched but others were not, then the 
    best practice is to provide status information for each provided entity in 
    the message.
If you believe that a critical error was encountered during the action 
    execution, then make sure there is a verbose message for this situation and 
    fail the action. When the action fails, the corresponding playbook will stop 
    execution until the error is resolved or skipped manually.
Some examples of output messages:
Successfully enriched the following entities using information from VirusTotal: {entity.identifier}
Action wasn't able to find any information for the following entities using VirusTotal: {entity.identifier}
None of the provided entities were found in VirusTotal.
Successfully executed query "{query}" in Google SecOps.
If the action should fail and stop execution of the playbook, then it's 
    recommended to have the output message in the following structure:
"Error executing action "{action name}". Reason: {error}'
Avoid putting the whole traceback for errors. Instead, try to point the 
    user to the actual problem in natural language.
Connectors
Name
The
Name
of the connector should point the user to the data that's 
    going to be ingested. In general, the structure of the name should be like 
    this:
{integration display name} - {data that is being ingested} Connector
For example:
Crowdstrike - Pull Alerts Connector
Description
The
Description
of the connector should highlight to the user what 
    will be ingested by the connector; for example,
Pull alerts from Crowdstrike
. 
    Additionally, you need to provide information about dynamic list support; 
    for example,
Dynamic List works with the
display_name
parameter.
The final description in this case would look like this:
Pull alerts from Crowdstrike. Dynamic List works with the
display_name
parameter.
Try to limit the description to 500 characters.
Connector Parameters
Connector configuration parameters should have an intuitive name. 
    Avoid using special characters and try to limit the action parameter name to 
    2-4 words.
The description for the parameter should explain to the user what 
    impact that parameter has on the connector execution.
If the parameter supports a predetermined amount of supported values, 
    then inside the description provide the following section:
Possible Values: {value 1}, {value 2}
. should have the
    following parameters:
Max Alerts To Fetch
: dictates how many {object} should be 
        processed during 1 connector iteration.
Max {Hours/Days} Backwards
: dictates the start time on the 
        first iteration of the connector. For example, if
Max Hours Backwards
is set to 1, the connector will begin pulling data from one hour earlier.
Verify SSL
: verifies the connectivity to API/instance.
Ontology Mapping
For each connector that is created, it's recommended to provide ontology 
    mapping to verify that mutual customers get the best experience.
Ontology Mapping is used to automatically create entities (IOCs and 
    Assets). Additionally, critical metadata of system fields like
Start Time
and
End Time
is defined there.
Dynamic List
The
Dynamic list
is an optional feature that lets you build an 
    advanced filter for ingestion. You have the flexibility to build any custom 
    logic with it, while having a unique UX. The most common use case is to 
    define an allowlist or a blocklist for ingestion.
If you are building any custom logic for
Dynamic List
, make sure 
    that it's provided in the description of the connector. Also, it's 
    recommended to have a
Use Dynamic List as a blocklist
parameter to 
    have inverse logic supported as well.
Jobs
Name
The
Name
of the job should explain to the user what this job is 
    performing. In general, the structure of the name should be like this:
{integration display name} - {process} Job
For example:
ServiceNow - Sync Incidents Job
Description
The
Description
of the job should highlight to the user what the 
    job is doing during the iterations; for example,
This job will 
    synchronize Security Command Center based cases created by the
Urgent Posture 
    Findings
connector.
Try to limit the description to 500 characters.
Job Parameters
Job configuration parameters should have an intuitive name. Avoid 
    using special characters and try to limit the action parameter name to 2-4 
    words.
The description for the parameter should explain to the user what 
    impact that parameter has on the job execution.
If the parameter supports a predetermined amount of supported values, 
    then inside the description provide the following section:
Possible Values: {value 1}, {value 2}
.
Beyond authentication parameters, all jobs should have the 
    following parameters:
Max {Hours/Days} Backwards
: dictates the start time on the 
        first iteration of the job.
Verify SSL
: verifies the connectivity to API/instance.
Need more help?
Get answers from Community members and Google SecOps professionals.
