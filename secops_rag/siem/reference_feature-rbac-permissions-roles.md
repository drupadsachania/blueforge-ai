# Permissions to Chronicle API

**Source:** https://docs.cloud.google.com/chronicle/docs/reference/feature-rbac-permissions-roles/  
**Scraped:** 2026-03-05T09:37:32.043442Z

---

Home
Documentation
Security
Google Security Operations
Reference
Stay organized with collections
Save and categorize content based on your preferences.
Permissions to Chronicle API
Supported in:
Google secops
SIEM
This documentation describes the Chronicle API methods, the permission
required to call each method, the Google Security Operations UI pages where the permission is 
used, and the information recorded in Cloud Audit Logs when the API is called.
You can find a list of all Google SecOps permissions in
IAM permissions reference
.
Under the
Search for a permission
section, search for the term
chronicle
.
You can find the latest list of all predefined Google SecOps roles
in
IAM basic and predefined roles reference
.
Under
Predefined roles
, select the
Chronicle API roles
service or search for
chronicle
.
For more information about audit logs, see
Google SecOps audit logs
.
The information in this document is grouped by the following Google SecOps resource groups:
Basic: Instances
Curated detections: CuratedRules, CuratedRuleSets,
CuratedRuleSetDeployments, and CuratedRuleSetCategories
Data tables: dataTables and dataTableRows
Dashboards resources
Emerging Threats: threatCollections and iocAssociations
Forwarder management: Collectors and Forwarders
Feed management: Feeds and LogTypes
Gemini: Conversations, translation, and feedback
Legacy resources
Operations resources
Parser management: Parsers, ParserExtensions, ValidationReports,
ExtensionValidationReports, and ValidationErrors
Risk Analytics
Rules: Rules and Retrohunts
Reference list resources
Search: Events and Entities
Triage and Investigation Agent (TIN)
User data: SearchQueries and PreferenceSet
You can programmatically access security data using API calls to
Google Security Operations. This is the same security data presented in the
Google SecOps UI through your Google SecOps account.
Permissions and API methods by resource group
The Chronicle API follows a
Resource-oriented design
paradigm. This model is the foundation for controlling access to features using IAM auditing application actions using Cloud Audit Logs.
IAM permissions define access to specific Chronicle API methods. Each method represents an action applied to a specific resource. Permissions are grouped into roles you grant to users or groups. For more information on these concepts, see
IAM overview
.
Audit logs in the Google Cloud console Logs Explorer contain information
about method name and the permission related to access of a feature.
IAM permission names (recorded in the
authorizationInfo
>
permission
field)
in audit logs take the form
chronicle.{resource}.{verb}
. For example, the
permission
forwarders.list
refers to
chronicle.forwarders.list
. For brevity,
this documentation omits the common service name (
chronicle
).
Method names in Google SecOps logs (recorded in the
methodName
field)
follow a namespace format. The fully qualified name of API methods is
google.cloud.chronicle.{version}.{service}.{method}
. For example, the method
ForwarderService.ListForwarders
refers to
google.cloud.chronicle.v1alpha.ForwarderService.ListForwarders.
For brevity, this document omits the common method name prefix
(
google.cloud.chronicle.v1alpha
).
After you
migrate your Google SecOps instance to IAM for feature access control
,
IAM audit logs are written for all UI access and programmatic
Chronicle API access. For example, if a user tries to load the
Settings > Forwarders
page in the UI, Google SecOps first verifies that
the user has access to the
chronicle.forwarders.list
permission.
The access attempt and the result is written to an audit log.
Basic: Instances
Instances
: Parent resources for all Google SecOps data. Each
Google SecOps tenant is associated with exactly one instance resource.
Permissions in this section are used by the following Google SecOps UI pages: Multiple.
IAM permission and method name
Description
Predefined roles
chronicle.instances.get
InstanceService.Get/
Gets basic information about the Google SecOps instance.
The UI does not call this method. The
instances.get
permission is required for all Google SecOps users.
Admin
Editor
Viewer
Limited Viewer
Restricted Data Access Viewer
chronicle.instances.report
InstanceService.Report/
Generates and returns a usage report for this Google SecOps
      instance. This usage report contains things like bytes ingested and most
      recent available detection time.
This method is not yet used by the UI.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocs.getIoc
IocService.GetIoc
Retrieves information about a single IoC from either GTI or internal SecOps data.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.fetchRuleMetadata
ThreatCollectionService.FetchRuleMetadata
A legacy role needed for backward compatibility.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.fetchEntityMetadata
ThreatCollectionService.FetchThreatCollectionEntityMetadata
Gets information about entities with entity risk scores that are associated to a threat.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollectionFilterSet.get
ThreatCollectionService.GetThreatCollectionFilterSet
Gets information about entities with entity risk scores that are associated to a threat.
Admin
Editor
Viewer
Limited Viewer
Data tables: dataTables and dataTableRows
dataTables
: Represents the data table resource.
dataTableRows
: Represents a data table row.
The
Investigation
>
Data tables
page uses the permissions in this section.
For more information, see
Use data tables
.
IAM permission and method name
Description
Predefined roles
chronicle.dataTableRows.bulkAppendAsync
Appends data table rows in bulk from a file asynchronously.
Admin
Editor
chronicle.dataTableRows.bulkCreate
Creates data table rows in bulk.
Admin
Editor
chronicle.dataTableRows.bulkCreateAsync
Creates data table rows in bulk asynchronously.
Admin
Editor
chronicle.dataTableRows.bulkGet
Gets multiple data table rows in a single request.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.dataTableRows.bulkReplace
Replaces all existing data table rows with new rows.
Admin
Editor
chronicle.dataTableRows.bulkReplaceAsync
Replaces all existing data table rows with new rows asynchronously.
Admin
Editor
chronicle.dataTableRows.bulkUpdate
Updates data table rows in bulk.
Admin
Editor
chronicle.dataTableRows.bulkUpdateAsync
Updates data table rows in bulk asynchronously.
Admin
Editor
chronicle.dataTableRows.create
Creates a data table row.
Admin
Editor
chronicle.dataTableRows.delete
Deletes a data table row.
Admin
Editor
chronicle.dataTableRows.get
Gets details for a data table row.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.dataTableRows.list
Lists the rows within a data table.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.dataTableRows.update
Updates a data table row.
Admin
Editor
chronicle.dataTables.bulkCreateAsync
Creates a data table from a bulk file asynchronously.
Admin
Editor
chronicle.dataTables.create
Creates a data table.
Admin
Editor
chronicle.dataTables.delete
Deletes a data table.
Admin
Editor
chronicle.dataTables.get
Gets information about a data table.
Admin
Editor
Viewer
chronicle.dataTables.list
Lists the data tables in a parent resource.
Admin
Editor
Viewer
chronicle.dataTables.update
Updates a data table configuration.
Admin
Editor
Emerging Threats: threatCollections and iocAssociations
threatCollections
: Reports and tracked threat campaigns from GTI.
iocAssociations
: Related threat associations (threat actors or malware families)
linked to a given threat resource.
Permissions in this section are used by the
Detection
>
Emerging Threats
pages.
For more information, see
Emerging Threats overview
.
IAM permission and method name
Description
Predefined roles
chronicle.threatCollections.get
ThreatCollectionService.GetThreatCollection
Gets detailed information about a threat collection from GTI,
      including associated IoCs.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.list
ThreatCollectionService.ListThreatCollections
Lists threat collections within a Google SecOps instance, retrieved
      from GTI, with support for filtering and pagination.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.fetchIocMatchMetadata
ThreatCollectionService.FetchIocMatchMetadata
Fetches the count of IoC matches for a list of threat collections.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.fetchRelated
ThreatCollectionService.FetchRelatedThreatCollections
Fetches related threat collections (reports or campaigns) from GTI for
      a given threat artifact (IoC, threat collection, or threat association).
Admin
Editor
Viewer
Limited Viewer
chronicle.iocs.getIoc
IocService.GetIoc
Retrieves information about a single IoC from either GTI or internal SecOps data.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.fetchRuleMetadata
ThreatCollectionService.FetchRuleMetadata
A legacy role needed for backward compatibility.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollections.fetchEntityMetadata
ThreatCollectionService.FetchThreatCollectionEntityMetadata
Gets information about entities with entity risk scores that are associated to a threat.
Admin
Editor
Viewer
Limited Viewer
chronicle.threatCollectionFilterSet.get
ThreatCollectionService.GetThreatCollectionFilterSet
Gets information about entities with entity risk scores that are associated to a threat.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocAssociations.get
IocService.GetIocAssociation
Gets an IoC association, which represents a threat actor or malware,
      from GTI, including its associated IoCs.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocAssociations.batchGet
IocService.BatchGetIocAssociations
Retrieves a list of IoC associations from GTI in a single batch request.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocAssociations.fetchRelated
IocService.FetchRelatedAssociations
Fetches related threat associations (malware or threat actors) for a given threat resource from GTI.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocs.batchGet
IocService.BatchGetIocs
Retrieves information about a batch of IoCs from either GTI or internal Google SecOps data.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocs.fetchRelated
IocService.FetchRelatedIocs
Fetches related IoCs for a given threat artifact from GTI.
Admin
Editor
Viewer
Limited Viewer
chronicle.coverageDetails.list
CoverageDetailsService.ListCoverageDetails
Lists details about which detection rules provide coverage for which threat collections.
Admin
Editor
Viewer
Limited Viewer
chronicle.coverageDetails.get
CoverageDetailsService.GetCoverageDetails
Gets coverage details for a specific threat collection or rule.
Admin
Editor
Viewer
Limited Viewer
chronicle.iocs.findIocs
IocService.FindIocs
Gets a list of IOCs given a list of parameters that uniquely identify
      them by their type and value with support for file hashes (MD5, SHA-1, SHA256),
      domain names, and IP addresses.
Admin
Editor
Viewer
Limited Viewer
Forwarder management: Collectors and Forwarders
Collectors
: Encapsulate configuration for a specific data type produced
by each Forwarder. Each Forwarder might contain 0 or more Collectors.
Forwarders
: Encapsulate configuration for a client which sends data
from the customer instance to Chronicle's Ingestion API. Each
Google SecOps instance might contain 0 or more Forwarders.
Permissions in this section are used by the following Google SecOps UI pages:
Settings > Forwarders
Learn more about
Forwarder Management
.
IAM permission and method name
Description
Predefined roles
chronicle.collectors.create
ForwarderService.CreateCollector/
Creates a new collector.
Called by the UI when it needs to create a collector, for example when
      adding or cloning a collector on the
Settings > Forwarders
page.
Admin
chronicle.collectors.delete
ForwarderService.DeleteCollector/
Deletes a collector.
Called by the UI when it needs to delete a collector, for example when
      deleting a collector on the
Settings > Forwarders
page.
Admin
chronicle.collectors.get
ForwarderService.GetCollector/
Get detailed information about a Collector.
Called by the UI when it needs access to information about a collector, for example when loading the
Edit Collector Configuration
dialog on the
Settings > Forwarders
page.
Admin
Editor
Viewer
chronicle.collectors.list
ForwarderService.ListCollectors/
Lists Collectors within a Google SecOps instance.
Called by the UI when it needs to list multiple collectors within the Google SecOps instance, for example when loading the collectors for a Forwarder on the
Settings > Forwarders
page.
Admin
Editor
Viewer
chronicle.collectors.update
ForwarderService.UpdateCollector/
Updates a Collector.
Called by the UI when it needs to update a collector, for example when finalizing an update from the
Edit Collector Configuration
dialog on the
Settings > Forwarders
page.
Admin
chronicle.forwarders.create
ForwarderService.CreateForwarder/
Creates a Forwarder.
Called by the UI when it needs to create a Forwarder, for example when creating a Forwarder on the
Settings > Forwarders
page.
Admin
chronicle.forwarders.delete
ForwarderService.DeleteForwarder/
Deletes a Forwarder.
Called by the UI when it needs to delete a Forwarder, for example when deleting a Forwarder on the
Settings > Forwarders
page.
Admin
chronicle.forwarders.generate
ForwarderService.GenerateForwarder/
Generates and returns configuration files for a Forwarder.
Called by the UI when it needs to generate configuration files for a Forwarder, for example when downloading a Forwarder on the
Settings > Forwarders
page.
Admin
chronicle.forwarders.get
ForwarderService.GetForwarder/
Gets detailed information about a Forwarder.
Called by the UI when it needs to access information about a Forwarder, for example when loading the
Edit Forwarder Configuration
dialog on the
Settings > Forwarders
page.
Admin
Editor
Viewer
chronicle.forwarders.list
ForwarderService.ListForwarders/
Lists Forwarders within a Google SecOps instance.
Called by the UI when it needs to list multiple Forwarders within the Google SecOps instance, for example when loading the
Settings > Forwarders
page.
Admin
Editor
Viewer
chronicle.forwarders.update
ForwarderService.UpdateForwarder/
Updates a Forwarder.
Called by the UI when it needs to update a Forwarder, for example when finalizing an update from the
Edit Forwarder Configuration
dialog on the
Settings > Forwarders
page.
Admin
Feed management: Feeds and LogTypes
Feeds
: Encapsulates the configuration for a data feed being ingested
into a Google SecOps instance.
FeedSourceTypeSchemas
: Contains metadata about the feed source types
that are available within the Google SecOps instance. A feed source is the
origin of the data that is ingested through a feed. For example,
Google Cloud
Storage
and
Third party API
are feed source types.
LogTypeSchemas
: Contains metadata about log types that are available
for ingestion within the context of a feed source type. For example,
Azure AD
is a log type which might be ingested using a
Third Party API
feed source.
Permissions in this section are used by the following Google SecOps UI pages:
Settings > Feeds
For more information, see
Feed Management
.
IAM permission and method name
Description
Predefined roles
chronicle.feeds.create
FeedsService.CreateFeed/
Creates a new feed.
Called by the UI when it needs to create a feed, for example when adding a new feed on the
Settings > Feeds
page.
Admin
chronicle.feeds.delete
FeedsService.DeleteFeed/
Deletes a Collector.
Called by the UI when it needs to delete a feed, for example when deleting a feed on the
Settings > Feeds
page.
Admin
chronicle.feeds.disable
FeedsService.DisableFeed/
Disables a feed, stopping ingestion of that feed's data into Google SecOps.
Called by the UI when it needs to disable a feed, for example when toggling the enabled status of a feed on the
Settings > Feeds
page.
Admin
chronicle.feeds.enable
FeedsService.EnableFeed/
Disables a feed, starting ingestion of that feed's data into Google SecOps.
Called by the UI when it needs to enable a feed, for example when toggling the enabled status of a feed on the
Settings > Feeds
page.
Admin
chronicle.feeds.get
FeedsService.GetFeed/
Get detailed information about a feed.
Called by the UI when it needs to access information about a feed, for example when loading the
Edit feed
dialog on the
Settings > Feeds
page.
Admin
Editor
Viewer
chronicle.feeds.generateSecret
FeedsService.GenerateSecret
Generates a secret for an HTTPS PUSH feed.
Called by the UI when it needs to generate a secret for the HTTPS PUSH feed.
Admin
chronicle.feeds.list
FeedsService.ListFeeds/
Lists feeds within a Google SecOps instance.
Called by the UI when it needs to list multiple feeds within the Google SecOps instance, for example when loading feeds on the
Settings > Feeds
page.
Admin
Editor
Viewer
chronicle.feeds.update
FeedsService.UpdateFeed/
Updates a feed.
Called by the UI to update a feed, for example when editing feeds on the
Settings > Feeds
page.
Admin
chronicle.feedSourceTypeSchemas.list
FeedsService.ListFeedSourceTypeSchemas/
Lists all FeedSourceSchemas available for a Google SecOps instance.
Called by the UI to populate a list of available FeedSourceSchema, for example when loading the
Settings > Feeds
page or a Create Feed dialog.
Admin
Editor
Viewer
chronicle.logTypeSchemas.list
FeedsService.ListLogTypeSchemas
Lists all LogTypeSchemas available for a FeedSourceSchema.
Called by the UI to populate a list of available LogTypeSchemas, for example when loading the
Settings > Feeds
page or a
Create Feed
dialog.
Admin
Editor
Viewer
Parser management: Parsers, ParserExtensions, ValidationReports, ExtensionValidationReports, and ValidationErrors
Parsers
: Encapsulates configuration metadata for the logic used to
convert incoming logs for a LogType into UDM Events.
ParserExtensions
: Encapsulates configuration metadata to extend the
logic contained within parsers for a LogType.
ValidationReports
: Describes the validation status of a parser or
extension at the time of its creation.
ParsingErrors
: Encapsulates error information from a ValidationReport
for a parser.
ExtensionValidationReports
: ValidationReports specific to one or more parser extensions.
ValidationErrors
: Encapsulates error information from an
ExtensionValidationReport for a ParserExtension.
Permissions in this section are used by the following Google SecOps UI pages:
Settings > Parser Extensions
and
Settings > Parsers
For more information, see
Parser Management
.
IAM permission and method name
Description
Predefined roles
chronicle.parsers.activate
ParserService.ActivateParser/
Activates a parser used to parse logs of each type.
Called by the UI to activate a custom parser as part of the action menu on
Settings > Parsers
page.
Admin
chronicle.parsers.activateReleaseCandidate
ParserService.activateReleaseCandidate/
Activates the release candidate parser for this log type.
Called by the UI when it selects a new prebuilt parser version. For example, on the
Settings > Parsers
page, click
View Pending Update
for a parser which has the status
Pending Update
. In the prebuilt parser diff viewer page, there is now a button to activate the newer version.
Admin
chronicle.parsers.copyPrebuiltParser
ParserService.CopyPrebuiltParser/
Creates a copy of a prebuilt parser and returns it.
Not used by the UI.
Admin
chronicle.parsers.create
ParserService.CreateParser/
Creates a parser.
Admin
chronicle.parsers.deactivate
ParserService.DeactivateParser/
Deactivates the requested parser and activates the prebuilt release parser.
Called by the UI to deactivate a custom parser as part of the action menu in the
Settings > Parsers
page.
Admin
chronicle.parsers.delete
ParserService.DeleteParser/
Deletes a parser.
Called by the UI to delete a custom parser as part of the action menu on the
Settings > Parsers
page.
Admin
chronicle.parsers.generateEventTypesSuggestions
ParserService.GenerateEventTypesSuggestions/
GenerateEventTypesSuggestions generates event types suggestions that can be mapped by a lowcode parser.
Used in Low Code parser creation and editing to display the available event types along with their confidence scores. Event types are mapped to the UDM Path "
udm.metadata.event_type"
Admin
chronicle.parsers.get
ParserService.GetParser/
Gets detailed information about a parser.
Not used by the UI.
Admin
chronicle.parsers.list
ParserService.ListParsers/
Lists all parsers for each log type.
Called by the UI to list all the parsers, for example when loading the
Settings > Parsers
page.
Admin
chronicle.parsers.run
ParserService.RunParser/
RunParser runs the parser against a log and returns normalized events or any error that occurred during normalization.
Admin
chronicle.parsingErrors.list
ParserService.ListParsingErrors/
List parsing errors within a validation report.
Used to fetch parser errors when creating a new custom parser in the
Create Custom Parser
view.
Admin
chronicle.parserExtensions.activate
ParserService.ActivateParserExtensions/
Activates a parser extension to parse the logs of the corresponding log type.
Called by the UI when activating a parser extension, for example when activating a parser extension from within the
Parser Extension Management
view.
Admin
chronicle.parserExtensions.create
ParserService.CreateParserExtension/
Creates a new parser extension.
Called by the UI when creating a new parser extension, for example when finalizing a new parser extension from the
Parser Extension Management
view.
Admin
chronicle.parserExtensions.delete
ParserService.DeleteParserExtension/
Deletes a parser extension.
Deletes a parser extension. For example, this method is used to delete a parser extension from the
Parser Extension Management
view.
Admin
chronicle.parserExtensions.generateUdmKeyValueMapping
ParserService.GenerateUDMKeyValueMappings/
Utility function for writing parser extensions which generates and returns key value mappings for a raw log.
Called by the UI to list the generated UDM key value mappings when writing a custom parser.
Admin
chronicle.parserExtensions.get
ParserService.GetParserExtension/
Gets detailed information about a parser extension.
For example, this method is used when rendering the
Parser Extension Management
view.
Admin
chronicle.parserExtensions.legacySubmitParserExtension
ParserService.LegacySubmitParserExtension/
A function supporting legacy workflows. It creates, validates, and then makes a parser extension live.
Method used by customers who don't have parser_management enabled and are still using the legacy
Parser Extension
view. For example, this method is used when adding a new extension in
Settings > Parser Extensions
page.
Admin
chronicle.parserExtensions.list
ParserService.ListParserExtensions/
Lists all parser extensions for a log type.
Lists the parser extensions setup for the Google SecOps instance. For example, this method is used when rendering the
Parser Extension Management
view.
Admin
chronicle.parserExtensions.removeSyslog
ParserService.ExtractSyslog/
Utility function for writing parser extensions which extracts the structured part of a log from an unstructured log.
Admin
chronicle.extensionValidationReports.list
ParserService.ListExtensionValidationReports
Lists all validation reports for a parser extension.
Lists the parser extension validation reports. For example, this method is used when rendering the
Parser Extension Management
view.
Admin
chronicle.extensionValidationReports.get
ParserService.GetExtensionValidationReport/
Gets detailed information about a parser extension validation report.
For example, this method is used when rendering the
Parser Extension Management
view.
Admin
chronicle.validationReports.get
ParserService.GetValidationReport/
Gets detailed information about a parser validation report.
Used by the UI to get detailed information about a parser's or parserExtenion's validation report, for example when rendering the
Parser Extension Management
view.
Admin
chronicle.validationErrors.list
ParserService.ListValidationErrors/
Lists all validation errors for a parser extension's validation report.
Used by the UI to list the parser extension validation errors, for example when rendering the detailed view of a parser extension with the validation errors.
Admin
Curated detections: CuratedRules, CuratedRuleSets, CuratedRuleSetDeployments, and CuratedRuleSetCategories
CuratedRules
: Represents the Google Cloud Threat Intelligence (GCTI)
authored rules.
CuratedRuleSets
: Groups of GCTI rules. For example, the CuratedRuleSet
OS Privilege Escalation Tools
might contain several CuratedRules designed to
detect the presence of the same. Each item in CuratedRules is a member of exactly one CuratedRuleSet.
CuratedRuleSetCategories
: Groups of CuratedRuleSets. For example, the
Linux Threats
CuratedRuleSetCategory contains several CuratedRuleSets,
including the
OS Privilege Escalation Tools
CuratedRuleSet described
previously. Each item in CuratedRuleSets is a member of exactly one
CuratedRuleSetCategory.
CuratedRuleSetDeployments
: Contains the configuration state
(enablement, alerting state, etc) of each CuratedRuleSet within the
Google SecOps instance. CuratedRuleSets might contain multiple deployments,
but each CuratedRuleSetDeployment within the CuratedRuleSet is associated with a
unique precision level (either
Precise
or
Broad
)
Permissions in this section are used by the following Google SecOps UI pages:
Detection > Rules
and
Detections > Curated Detections
For more information, see
Curated Detections
.
IAM permission and method name
Description
Predefined roles
chronicle.curatedRules.get
CuratedRuleService.GetCuratedRule/
Gets detailed information about a CuratedRule.
Called by the UI when it needs to load the detailed view of a CuratedRule.
Admin
Editor
Viewer
chronicle.curatedRules.list
CuratedRuleService.ListCuratedRules/
Lists CuratedRules within a CuratedRuleSet.
Called by the UI when it needs to list multiple CuratedRules within the Google SecOps instance, for example when pivoting into a specific CuratedRuleSet from the
Curated Detections
view.
Admin
Editor
Viewer
chronicle.curatedRuleSets.countCuratedRuleSetDetections
CuratedRuleService.CountCuratedRuleSetDetections/
Provides a count of the number of detections generated by a CuratedRuleSet.
Called by the UI when it needs to retrieve detection metadata for CuratedRuleSets, for example when loading the
Curated Detections
tab of the
Detection > Rules & Detections
page.
Admin
Editor
Viewer
chronicle.curatedRuleSets.get
CuratedRuleService.GetCuratedRuleSet/
Gets detailed information about a CuratedRuleSet.
Called by the UI when it needs to load the detailed view of a CuratedRuleSet, for example when pivoting into a specific CuratedRuleSet from the
Curated Detections
view.
Admin
Editor
Viewer
chronicle.curatedRuleSets.list
CuratedRuleService.ListCuratedRuleSets/
Lists CuratedRuleSets within a CuratedRuleSetCategory.
Called by the UI when it needs to list multiple CuratedRuleSets within the Google SecOps instance, for example when loading the
Curated Detections
tab of the
Detection > Rules & Detections
page.
Admin
Editor
Viewer
chronicle.curatedRuleSetCategories.countAllCuratedRuleSetDetections
CuratedRuleService.CountAllCuratedRuleSetDetections/
Provides a count of the number of detections generated by all CuratedRuleSets within a CuratedRuleSetCategory
Called by the UI when it needs to retrieve detection metadata for CuratedRuleSetCategories, for example when loading the
Curated Detections
tab of the
Detection > Rules & Detections
page.
Admin
Editor
Viewer
chronicle.curatedRuleSetCategories.get
CuratedRuleService.GetCuratedRuleSetCategory/
Gets detailed information about a CuratedRuleSetCategory.
Called by the UI when it needs to load the detailed view of a CuratedRuleSetCategory, for example when loading the
Curated Detections
tab of the
Detection > Rules & Detections
page.
Admin
Editor
Viewer
chronicle.curatedRuleSetCategories.list
CuratedRuleSetCategories.ListCuratedRuleSetCategories/
Lists CuratedRuleSetCategories within a Google SecOps instance.
Called by the UI when it needs to list multiple CuratedRuleSetCategories within a Google SecOps instance, for example when loading the
Curated Detections
tab of the
Detection > Rules & Detections
page.
Admin
Editor
Viewer
chronicle.curatedRuleSetDeployments.batchUpdate
Updates multiple deployments of multiple different CuratedRuleSets.
Called by the UI when it needs to update multiple deployment statuses simultaneously, for example when modifying the Alerting or Enabled state for several CuratedRuleSets from the
Curated Detections
tab of the
Detection > Rules & Detections
page.
Admin
Editor
chronicle.curatedRuleSetDeployments.get
Gets detailed information about a CuratedRuleSetDeployment.
Called by the UI when it needs to display the deployment status of a CuratedRuleSet, for example when loading the detailed view page for that CuratedRuleSet.
Admin
Editor
Viewer
chronicle.curatedRuleSetDeployments.list
Lists all CuratedRuleSetDeployments within a CuratedRuleSet.
Called by the UI when it needs to display the deployment status of a CuratedRuleSet, for example when loading the detailed view page for that CuratedRuleSet.
Admin
Editor
Viewer
chronicle.curatedRuleSetDeployments.update
Updates a CuratedRuleSetDeployment.
Called by the UI when it needs to update a single CuratedRuleSetDeployment, for example when modifying the Alerting or Enabled state for a single CuratedRuleSet using the toggles on the CuratedRuleSet details page.
Admin
Editor
Risk Analytics
EntityRiskScore
: Risk scores are set by the source when a finding is created. The original risk score cannot be changed, but it can be modified using the scaling modifiers. For more information, see
Modify an entity risk score
.
riskConfigs
: The risk configurations change how risk scores are generated and calculated. You can specify the risk configurations on the
SIEM settings > Entity risk scores
page. For more information, see
Entity risk scores
.
watchlists
: Identifiers for all of the watchlists that are configured within the
Google SecOps instance.
Permissions in this section are used by the following Google SecOps UI page:
Detection > Risk Analytics
For more information, see
Risk Analytics
.
The Risk Analytics permissions are as follows:
IAM permission and method name
Description
Predefined roles
chronicle.entities.modifyEntityRiskScore
Updates an entity risk score.
Called by the UI when it needs to modify an entity risk score, for example when you modify an entity risk score using
Update Entity Risk Score
from the
Behavioral Analytics
tab.
Admin
Editor
chronicle.entities.queryEntityRiskScoreModifications
Displays the entity risk scores.
Called by the UI when it needs to display the entity risk scores, for example when the entity risk scores are displayed on the
Behavioral Analytics
tab.
Admin
Editor
Viewer
chronicle.riskConfigs.get
Displays the risk configurations.
The risk configurations change how risk scores are generated and calculated, for example when you specify the risk configurations on the
SIEM settings > Entity risk scores
page. For more information, see [Entity risk scores](/chronicle/docs/detection/risk-analytics-overview#risk_score_calculation).
Admin
Editor
Viewer
chronicle.riskConfigs.update
Updates the risk calculation window.
Called by the UI when it needs to modify the risk calculation window, for example when you change the
Risk calculation window
from a
7 day window
to a
24 hour window
on the
Behavioral Analytics
tab.
Admin
Editor
chronicle.watchlists.create
Creates a new watchlist.
Called by the UI when it needs to create a new watchlist, for example when you create a new watchlist by clicking
Create Watchlist
from the
Create Watchlist
window.
Admin
Editor
chronicle.watchlists.delete
Deletes a watchlist.
Called by the UI when it needs to delete a watchlist, for example when you delete a watchlist by clicking
Delete Watchlist
from the menu option for a watchlist on the
Watchlists
tab.
Admin
Editor
chronicle.watchlists.get
Displays a single watchlist.
Called by the UI when it needs to display a single watchlist, for example each time you click a single watchlist within the
Edit display
window.
Admin
Editor
Viewer
chronicle.watchlists.list
Displays all of the watchlists.
Called by the UI when it needs to display the watchlists, for example when you navigate to the
Watchlists
tab.
Admin
Editor
Viewer
chronicle.watchlists.update
Modifies a watchlist.
Called by the UI when it needs to modify a watchlist, for example when you modify a watchlist by clicking
Edit Watchlist
from the menu option for a watchlist on the
Watchlists
tab.
Admin
Editor
Rules: Rules and Retrohunts
Rules
: Represent user-created rules.
RuleDeployments
: Deployment state of a rule. Each rule has exactly one
RuleDeployment.
Retrohunts
: Executions of a rule over a time range in the past.
Retrohunts that are in progress are represented by the Operation resource.
Permissions in this section are used by the following Google SecOps UI pages:
Detection > Rules & Detections > Rules Dashboard
and
Detection > Rules & Detections > Rules Editor
Learn more about
detection engine
.
IAM permission and method name
Description
Predefined roles
chronicle.rules.create
RuleService.CreateRule/
Creates a new rule.
Called by the UI when it needs to create a new rule, for example when creating a new rule from the Rules Editor.
Admin
Editor
chronicle.rules.delete
RuleService.DeleteRule/
Deletes a rule.
Called by the UI when it needs to delete a rule, for example when deleting a rule from the Rules Editor.
Admin
Editor
chronicle.rules.get
RuleService.GetRule/
Gets detailed information about a rule.
Called by the UI when it needs to render detailed information about a rule, for example when displaying the detections page for a rule.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.rules.list
RuleService.ListRules/
Lists multiple rules within a Google SecOps instance.
Called by the UI when it needs to list multiple rules within a Google SecOps instance, for example when rendering the Rules Dashboard.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.rules.update
RuleService.UpdateRule/
Updates a rule.
Called by the UI when it needs to apply updates to a rule, for example when saving changes from the Rules Editor.
Admin
Editor
chronicle.rules.verifyRuleText
RuleService.VerifyRuleText/
A utility function which verifies the rule text.
Called by the UI when needed to verify rule text, for example the Rules Editor calls this function interactively.
Admin
Editor
Restricted Data Access Viewer
chronicle.rules.listRevisions
RuleService.ListRuleRevisions/
Lists all revisions of a rule.
Called by the UI when needed to list rule revisions, for example when performing the
view rule versions
action from the Rules Editor.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.retrohunts.create
RuleService.CreateRetrohunt/
Creates and starts a new retrohunt.
Called by the UI when needed to create a retrohunt, for example when performing the YARA-L retrohunt action from the Rules Dashboard.
Admin
Editor
chronicle.retrohunts.get
RuleService.GetRetrohunts/
Gets detailed information about a retrohunt.
Called by the UI when needed to render detailed information about a retrohunt, for example the UI calls this function interactively after creating a retrohunt to display hunt progress.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.retrohunts.list
RuleService.ListRetrohunts/
Lists all retrohunts for a rule.
Called by the UI when needed to list all retrohunts for a rule, for example when rendering the detections page for a rule.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.ruleDeployments.get
RuleService.GetRuleDeployments/
Gets detailed information about a rule deployment.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.ruleDeployments.list
RuleService.ListRuleDeployments/
Lists multiple rule deployments for a rule or Google SecOps instance.
Called by the UI to render multiple rule deployments, for example when loading the Rules Editor page.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.ruleDeployments.update
RuleService.UpdateRuleDeployment/
Updates a rule deployment.
Called by the UI to update a rule deployment, for example when toggling a rule's liveness or alerting properties from the Rules Editor page.
Admin
Editor
Reference list resources
The
ReferenceLists
resource represents user-defined lists of values you use throughout the
product, for example multiple rules might compare values against one or more
ReferenceLists
.
Permissions in this section are used by the following Google SecOps UI pages:
Detection > Rules
and
Detections > Rules Editor ( > ListManager)
Learn more about
reference lists
.
IAM permission and method name
Description
Predefined roles
chronicle.referenceLists.create
ReferenceListService.CreateReferenceList/
Creates a new reference list.
Called by the UI when it needs to create a reference list, for example when creating a new reference list from within the Rules Editor's List Manager.
Admin
Editor
chronicle.referenceLists.get
ReferenceListService.GetReferenceList/
Gets detailed information about a reference list.
Called by the UI when it needs to render detailed information about a reference list, for example when rendering a specific list from within the Rules Editor's List Manager.
Admin
Editor
chronicle.referenceLists.list
ReferenceListService.ListReferenceLists/
Lists all reference lists within a Google SecOps instance.
Called by the UI when it needs to render all reference lists within a Google SecOps instance, for example when rendering the Rules Editor's List Manager.
Admin
Editor
Viewer
chronicle.referenceLists.update
ReferenceListService.UpdateReferenceLists/
Updates a reference list.
Called by the UI when it needs to apply updates to a reference list, for example when saving updates to a reference list from within the Rules Editor's List Manager.
Admin
Editor
chronicle.referenceLists.verifyReferenceList
ReferenceListService.VerifyReferenceLists/
A utility function which can validate reference list content and return line errors, if any.
Called by the UI when it needs to validate reference list content, for example this is called interactively when creating a new reference list from within the Rules Editor's List Manager.
Admin
Editor
Viewer
Dashboard resources
Dashboards
encapsulate Looker dashboard metadata within a
Google SecOps instance.
Permissions in this section impact the following Google SecOps UI pages:
Dashboards
Learn more about Google SecOps
dashboards
.
IAM permission and method name
Description
Predefined roles
chronicle.dashboards.copy
DashboardService.CopyDashboard/
Copies a dashboard.
Called by the UI when it needs to copy a dashboard, for example when performing the
Copy to Personal
or
Copy to Shared
actions from the Dashboards view.
Admin
Editor
chronicle.dashboards.create
DashboardService.CreateDashboard/
Creates a dashboard.
Called by the UI when it needs to create a dashboard, for example when creating a dashboard from the Dashboards view.
Admin
Editor
chronicle.dashboards.delete
DashboardService.DeleteDashboard/
Deletes a dashboard.
Called by the UI when it needs to delete a dashboard, for example when deleting a dashboard from the Dashboards view.
Admin
Editor
chronicle.dashboards.get
DashboardService.GetDashboard/
Gets detailed information about a dashboard.
Called by the UI when it needs to render detailed information about a dashboard.
Admin
Editor
Viewer
chronicle.dashboards.list
DashboardService.ListDashboards/
Lists all dashboards within a Google SecOps instance.
Called by the UI when it needs to list all dashboards within a Google SecOps instance, for example when rendering the Dashboards view.
Admin
Editor
Viewer
Search: Events and Entities
Events
: Encapsulate information about activity data.
Entities
: Encapsulate additional context about something within a UDM
event (asset, user, etc.). For example, a
PROCESS_LAUNCH
event describes that
user
abc@example.corp
launched process
shady.exe
. The event does not include
information that user
abc@example.com
is a recently terminated employee who
administers a server storing finance data. Information stored in one or more
Entities can add this additional context.
Permissions in this section are used by the following Google SecOps UI pages: Multiple
IAM permission and method name
Description
Predefined roles
chronicle.events.get
EventService.GetEvent/
Gets detailed information about an event.
Admin
Editor
Restricted Data Access Viewer
chronicle.events.batchGetEvents
EventService.BatchGetEvents/
A batch endpoint for getting detailed information about multiple events.
Admin
Editor
Restricted Data Access Viewer
chronicle.events.udmSearch
EventService.UdmSearch/
Performs a UDM search that returns matching events for the query.
Admin
Editor
Restricted Data Access Viewer
chronicle.events.validateQuery
EventService.ValidateQuery/
Validates a UDM search query by compiling that query.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.events.queryProductSourceStats
EventService.QueryProductSourceStats/
Gets available product sources along with their statistics.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.events.findUdmFieldValues
EventService.FindUdmFieldValues/
Finds ingested UDM field values that match a query.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.entities.get
EntityService.GetEntity/
Gets detailed information about an entity.
Admin
Editor
Restricted Data Access Viewer
chronicle.entities.summarize
EntityService.SummarizeEntity/
Returns all entity data over specified time.
Admin
Editor
Restricted Data Access Viewer
chronicle.entities.findRelatedEntities
EntityService.FindRelatedEntities/
Finds all the entities associated with the provided entity.
Admin
Editor
Restricted Data Access Viewer
chronicle.entities.searchEntities
EntityService.SearchEntities/
Identifies the entity type and retrieves relevant data associated with a specified indicator.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.entities.summarizeEntitiesFromQuery
EntityService.SummarizeEntitiesFromQuery
Parses the query and identifies the entities contained within the search query.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.entities.find
EntityService.FindEntity
Identifies the entity type and retrieves relevant data associated with a specified indicator.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.entities.findEntityAlerts
EntityService.FindEntityAlerts
Get alerts for an entity.
Admin
Editor
Viewer
Restricted Data Access Viewer
Triage and Investigation Agent (TIN)
The following Google SecOps UI pages use the permissions in this section:
Detections
>
Alerts & IOCs
Note:
Use the
gcloud
command to add permissions.
For example,
gcloud iam roles update MYROLE --project=MYPROJECT --add-permissions=chronicle.conversations.create,chronicle.notebooks.get,chronicle.notebooks.list,chronicle.investigations.get,chronicle.investigations.list,chronicle.investigationSteps.get,chronicle.investigationSteps.list,chronicle.investigations.trigger,chronicle.ais.createFeedback.
For more details, see
Use Triage and Investigation Agent (TIN) in Google Security Operations
.
IAM permission and method name
Description
Predefined roles
chronicle.notebooks.get
Gets an existing agent notebook.
Limited Viewer
chronicle.notebooks.list
Lists all existing agent notebooks.
Limited Viewer
chronicle.investigations.get
Gets an existing agent investigation.
Viewer
chronicle.investigations.list
Lists all existing investigationsr.
Viewer
chronicle.investigationSteps.get
Gets an existing investigation step performed by Gemini for an investigation.
Limited Viewer
chronicle.investigationSteps.list
Lists all investigation steps performed by Gemini for an investigation.
Limited Viewer
chronicle.investigations.trigger
Lets you manually run a TIN investigation on alerts.
Editor
chronicle.ais.createFeedback
Lets you provide feedback on an investigation performed by the TIN.
Restricted Data Access Viewer
Legacy resources
Legacies
are generic container resources for legacy operations that are
used by the Google SecOps but have not been modeled as part of the
Chronicle API resource-oriented paradigm.
Permissions in this section are used by the following Google SecOps UI pages: Multiple
IAM permission and method name
Description
Predefined roles
chronicle.legacies.legacyFetchAlertsView
LegacyAlertService.LegacyFetchAlertsView/
Fetches data required for rendering an alert view, including a histogram.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyUpdateAlert
LegacyAlertService.LegacyUpdateAlert/
Updates an alert.
Admin
Editor
chronicle.legacies.legacyGetAlert
LegacyAlertService.LegacyGetAlert/
Gets an alert based on its alert ID.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchEnterpriseWideAlerts
LegacyAlertService.LegacySearchEnterpriseWideAlerts/
Queries for multiple alerts within a Google SecOps instance for a specific time range.
Admin
Editor
Limited Viewer
chronicle.legacies.legacySearchEnterpriseWideIoCs
LegacyAlertService.LegacySearchEnterpriseWideIoCs/
Lists IoC matches against ingested events.
Admin
Editor
Limited Viewer
chronicle.legacies.legacySearchArtifactIoCDetails
LegacyAlertService.LegacySearchArtifactIoCDetails/
Queries for IoC details for a particular artifact.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchIoCInsights
LegacyAlertService.LegacySearchIoCInsights/
Lists IoC insights on a particular artifact.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyBatchGetCases
LegacyCaseService.LegacyBatchGetCases/
Fetches cases for a set of names.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchFindings
LegacyDetectionService.LegacySearchFindings/
Lists findings.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyFetchUdmSearchView
LegacyEventService.LegacyFetchUdmSearchView/
Fetches events, filters, and histograms matching UDM search.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchAssetEvents
LegacyEventService.LegacySearchAssetEvents/
Gets the events associated with an asset.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchArtifactEvents
LegacyEventService.LegacySearchArtifactEvents/
Gets the events associated with an artifact.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchUserEvents
LegacyEventService.LegacySearchUserEvents/
Gets the events associated with a user.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchRawLogs
LegacyEventService.LegacySearchRawLogs/
Gets the events associated with a raw log search.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyFindAssetEvents
LegacyEventService.LegacyFindAssetEvents/
Gets events for an asset indicator.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyFindRawLogs
LegacyEventService.LegacyFindRawLogs/
Gets events for a raw log search query.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyFetchUdmSearchCsv
LegacyEventService.LegacyFetchUdmSearchCsv/
Fetches CSV rows for matching UDM search.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyFindUdmEvents
LegacyEventService.LegacyFindUdmEvents/
Finds UDM/entity events using tokens or IDs.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchDomainsRecentlyRegistered
LegacyEventService.LegacySearchDomainsTimingStats/
Given a list of domain names and a time, returns only the domains that were recently registered relative to that time.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchDomainsTimingStats
LegacyEventService.LegacySearchDomainsTimingStats/
Given a list of domain names, returns time-related statistics for those domains such as the first seen in the enterprise time.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyGetRulesTrends
LegacyRuleService.LegacyGetRulesTrends/
Lists detection counts and last detection timestamp for a list of user-defined rule IDs.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacyGetRuleCounts
LegacyRuleService.LegacyGetRuleCounts/
Gets rule counts.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacySearchRuleDetectionCountBuckets
LegacyRuleService.LegacySearchRuleDetectionCountBuckets/
Lists detection count buckets for a Rules Engine rule.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacySearchRuleResults
LegacyRuleService.LegacySearchRuleResults/
Lists aggregated results for a Rules Engine rule.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacySearchRulesAlerts
LegacyRuleService.LegacySearchRulesAlerts/
Gets the list of alerts generated by the Rules Engine for a customer.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacyRunTestRule
LegacyRuleService.LegacyRunTestRule/
Tests a rule and streams back the responses without persisting them.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacySearchRuleDetectionEvents
LegacyRuleService.LegacySearchRuleDetectionEvents/
Lists events associated with a particular detection generated by a Rules Engine rule.
Admin
Editor
Restricted Data Access Viewer
chronicle.legacies.legacyGetDetection
LegacyRulesEngineService.LegacyGetDetection/
Gets a detection.
Admin
Editor
Viewer
chronicle.legacies.legacyStreamDetectionAlerts
LegacyRulesEngineService.LegacyStreamDetectionAlerts/
Continuously streams new detection alerts as they are discovered.
Admin
Editor
Viewer
chronicle.legacies.legacyTestRuleStreaming
LegacyRulesEngineService.LegacyTestRuleStreaming/
Tests the rule text over a specified time range and streams detections/errors back without persisting them.
Admin
Editor
Viewer
chronicle.legacies.legacyBatchGetCollections
LegacyCaseService.LegacyBatchGetCollections/
Gets a batch of collections based on Collection ID.
Admin
Editor
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacyGetEventForDetection
LegacyRulesEngineService.legacyGetEventForDetection/
Legacy endpoint for getting an event for curated detection.
Admin
Editor
Viewer
chronicle.legacies.legacySearchCuratedDetections
LegacyEventService.legacySearchCuratedDetections/
Legacy endpoint for searching detections for a curated rule.
Admin
Editor
Viewer
chronicle.legacies.legacySearchCustomerStats
LegacyEventService.legacySearchCustomerStats/
Gets data collection stats about a customer, such as the first or last time data was seen from a customer.
Admin
Editor
Viewer
Limited Viewer
Restricted Data Access Viewer
chronicle.legacies.legacySearchDetections
LegacyEventService.legacySearchDetections/
Legacy endpoint for searching detections for a rule version.
Admin
Editor
Viewer
chronicle.legacies.legacySearchIngestionStats
LegacyEventService.legacySearchIngestionStats/
Gets data ingestion stats about a given customer.
Admin
Editor
Viewer
Limited Viewer
Restricted Data Access Viewer
Operations resources
Certain Chronicle API calls, such as retrohunt creation, take a long
time to complete. These calls are modeled using long-running operations.
Operations
represent long-running work for an API.
Learn more about
long-running operations
.
IAM permission and method name
Description
Predefined roles
chronicle.operations.cancel
OperationService.CancelOperation/
Cancels an operation.
Admin
Editor
chronicle.operations.delete
OperationService.DeleteOperation/
Deletes an operation.
Admin
Editor
chronicle.operations.get
OperationService.GetOperation/
Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.operations.list
OperationService.ListOperation/
Lists service operations that match the specified filter in the request.
Admin
Editor
Viewer
Restricted Data Access Viewer
chronicle.operations.wait
OperationService.WaitOperation/
Not implemented.
Admin
Editor
Viewer
Restricted Data Access Viewer
User preference: SearchQueries and PreferenceSet
SearchQueries
represent a saved UDM search query from a Google SecOps
user. This includes both the query and metadata for the entry.
PreferenceSet
is a singleton resource that contains a collection of
preferences for UI configuration for users.
Permissions in this section are used by the following Google SecOps UI pages: Search tab.
Learn more about
saved searches
.
IAM permission and method name
Description
Predefined roles
chronicle.searchQueries.create
UserDataService.CreateSearchQuery/
Adds a new saved query entry to the specified collection of user data
Called by the UI when a user saves a search query.
Viewer
chronicle.searchQueries.get
UserDataService.GetSearchQuery/
Gets the user's saved query entry.
Called by the UI when the user selects a saved search from the Search Manager.
Viewer
chronicle.searchQueries.delete
UserDataService.DeleteSearchQuery/
Deletes a user data saved query entry.
Called by the UI when the user deletes a saved search they created.
Viewer
chronicle.searchQueries.list
UserDataService.ListSearchQueries/
Lists the shared saved queries or user-specific saved queries owned by the specified user.
Called by the UI when the user opens the Search Manager.
Viewer
chronicle.searchQueries.update
UserDataService.UpdateSearchQuery/
Updates user data saved query
Called by the UI when the user saves modifications to a saved search query they own.
Viewer
chronicle.preferenceSets.update
UserDataService.UpdatePreferenceSet/
Updates a user's PreferenceSet
Called by the UI when the user changes their localization.
Viewer
chronicle.preferenceSets.get
UserDataService.GetPreferenceSet/
Fetches a user's PreferenceSet
Called by the UI when the user opens the localization toast.
Viewer
Gemini: Conversations, translation, and feedback
Conversations
: Operations for managing Gemini chat sessions in the web interface.
These permissions support creating, retrieving, deleting, or listing past conversations
between the user and Gemini.
Translations
: AI-powered operations that convert natural-language
prompts into structured query formats.
Feedback
: Permissions that let users give feedback on Gemini-generated
responses.
IAM permission and method name
Description
Predefined roles
chronicle.ais.createFeedback
Submits feedback on responses generated by the Google SecOps AI services.
Restricted Data Access Viewer
chronicle.ais.translateUdmQuery
Translates natural-language prompts into structured UDM queries.
Restricted Data Access Viewer
chronicle.ais.translateYlRule
Translates natural-language prompts into YARA-L rules.
Restricted Data Access Viewer
chronicle.conversations.create
Creates a new Gemini chat session.
For example, click
more_vert
Menu
>
New Chat
in Gemini.
Admin
Editor
chronicle.conversations.delete
Deletes the current Gemini chat session.
For example, click
more_vert
Menu
>
Delete Chat Session
in Gemini.
Admin
Editor
chronicle.conversations.get
Retrieves the contents of a specific Gemini chat session.
Limited Viewer
chronicle.conversations.list
Lists all past Gemini chat sessions.
Limited Viewer
chronicle.conversations.update
Updates an existing Gemini chat session.
Admin
Editor
chronicle.messages.create
Creates a new message in a Gemini chat session.
Admin
Editor
