# Use context-enriched data in rules

**Source:** https://docs.cloud.google.com/chronicle/docs/detection/use-enriched-data-in-rules/  
**Scraped:** 2026-03-05T09:31:45.019878Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use context-enriched data in rules
Supported in:
Google secops
SIEM
To enable security analysts during an investigation, Google Security Operations ingests contextual
data from different sources, performs analysis on the ingested data, and
provides additional context about artifacts in a customer environment. This
document provides examples of how analysts use contextually-enriched data
in Detection Engine rules.
For more information about data enrichment, see
How Google SecOps enriches event and entity data
.
Use prevalence enriched fields in rules
The following examples demonstrate how to use the prevalence-related enriched
fields in Detection Engine. For reference, see the list of
prevalence-related enriched fields
.
Identify low prevalence domain access
This detection rule generates a detection event, not a detection alert, when a match is found. It is primarily meant as a secondary indicator when
investigating an asset. For example, there are other higher severity alerts that triggered an incident.
$enrichment.graph.metadata.entity_type = "FILE"
$enrichment.graph.metadata.product_name = "VirusTotal Relationships"
$enrichment.graph.metadata.vendor_name = "VirusTotal"
See
Add an event type filter
for more information about adding a filter to improve rule performance.
For information about each enrichment type, see
How Google SecOps enriches event and entity data
.
Use prevalence enriched fields in rules
The following examples demonstrate how to use the prevalence-related enriched
fields in Detection Engine. For reference, see the list of
prevalence-related enriched fields
.
Identify access to domains with a low prevalence score
This rule can be used to detect access to domains with a low prevalence score.
To be effective, a baseline of prevalence scores for artifacts must exist. The
following example uses
reference lists
to tune the result and applies a
threshold prevalence value.
rule network_prevalence_low_prevalence_domain_access {
  meta:
    author = "Google Security Operations"
    description = "Detects access to a low prevalence domain. Requires baseline of prevalence be in place for effective deployment."
    severity = "LOW"

  events:
        $e.metadata.event_type = "NETWORK_HTTP"
        $e.principal.ip = $ip

        // filter out URLs with RFC 1918 IP addresses, internal assets
        not re.regex($e.target.hostname, `(127(?:\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$)|(10(?:\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$)|(192\.168(?:\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){2}$)|(172\.(?:1[6-9]|2\d|3[0-1])(?:\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){2})`)

        // used an explicit exclusion reference list
        not $e.target.hostname in %exclusion_network_prevalence_low_prevalence_domain_access

        // only match valid FQDN, filter out background non-routable noise
        re.regex($e.target.hostname, `(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`)

        $domainName = $e.target.hostname

        //join event ($e) to entity graph ($d)
        $e.target.hostname = $d.graph.entity.domain.name

        $d.graph.metadata.entity_type = "DOMAIN_NAME"

        // tune prevalence as fits your results
        $d.graph.entity.domain.prevalence.rolling_max > 0
        $d.graph.entity.domain.prevalence.rolling_max <= 10

  match:
        $ip over 1h

  outcome:
    $risk_score = max(
        // increment risk score based upon rolling_max prevalence
        if ( $d.graph.entity.domain.prevalence.rolling_max >= 10, 10) +
        if ( $d.graph.entity.domain.prevalence.rolling_max >= 2 and $d.graph.entity.domain.prevalence.rolling_max <= 9 , 20) +
        if ( $d.graph.entity.domain.prevalence.rolling_max = 1, 30)
    )

    $domain_list = array_distinct($domainName)
    $domain_count = count_distinct($domainName)

  condition:
    $e and #d > 10
}
Identify low prevalence domains with an IOC match
This detection rule generates a detection alert and provides a high fidelity
match comparing a low prevalence domain that is also a known IOC.
rule network_prevalence_uncommon_domain_ioc_match {

  meta:
    author = "Google Security Operations"
    description = "Lookup Network DNS queries against Entity Graph for low prevalence domains with a matching IOC entry."
    severity = "MEDIUM"

  events:
    $e.metadata.event_type = "NETWORK_DNS"
    $e.network.dns.questions.name = $hostname

    //only match FQDNs, such as: exclude chrome dns access tests and other internal hosts
    $e.network.dns.questions.name = /(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]/

    //prevalence entity graph lookup
    $p.graph.metadata.entity_type = "DOMAIN_NAME"
    $p.graph.entity.domain.prevalence.rolling_max > 0
    $p.graph.entity.domain.prevalence.rolling_max <= 3
    $p.graph.entity.domain.name = $hostname

    //ioc entity graph lookup
    $i.graph.metadata.vendor_name = "ET_PRO_IOC"
    $i.graph.metadata.entity_type = "DOMAIN_NAME"
    $i.graph.entity.hostname = $hostname

  match:
    $hostname over 10m

  outcome:
    $risk_score = max(
        //increment risk score based upon rolling_max prevalence
        if ( $p.graph.entity.domain.prevalence.rolling_max = 3, 50) +
        if ( $p.graph.entity.domain.prevalence.rolling_max = 2, 70) +
        if ( $p.graph.entity.domain.prevalence.rolling_max = 1, 90)
    )

  condition:
    $e and $p and $i
}
Use an entity's first seen time in a rule
You can write rules that include the
first_seen_time
or
last_seen_time
fields
from entity records.
The
first_seen_time
and
last_seen_time
fields are populated with entities that
describe a domain, IP address, and file (hash). For entities that describe a user
or asset, only the
first_seen_time
field is populated. These values are not
calculated for entities that describe other types, such as a group or resource.
For a list of UDM fields that are populated, see
Calculate the first seen and last seen time of entities
.
Here is an example showing how to use the
first_seen_time
in a rule:
rule first_seen_data_exfil {
    meta:
        author = "Google Security Operations"
        description = "Example usage first_seen data"
        severity = "LOW"

    events:
        $first_access.metadata.event_type = "NETWORK_HTTP"
        $ip = $first_access.principal.ip

        // Join first_access event with entity graph to use first/last seen data.
        $ip = $first_last_seen.graph.entity.ip
        $first_last_seen.graph.metadata.entity_type = "IP_ADDRESS"

        // Check that the first_access UDM event is the first_seen occurrence in the enterprise.
        $first_last_seen.graph.entity.artifact.first_seen_time.seconds = $first_access.metadata.event_timestamp.seconds
        $first_last_seen.graph.entity.artifact.first_seen_time.nanos   = $first_access.metadata.event_timestamp.nanos

        // Check for another access event that appears shortly after the first_seen event,
        // where lots of data is being sent.
        $next_access_data_exfil.metadata.event_type = "NETWORK_CONNECTION"
        // Next access event goes to the same IP as the first.
        $next_access_data_exfil.principal.ip = $ip

        // Next access occurs within 60 seconds after first access.
        $next_access_data_exfil.metadata.event_timestamp.seconds > $first_access.metadata.event_timestamp.seconds
        60 > $next_access_data_exfil.metadata.event_timestamp.seconds  - $first_access.metadata.event_timestamp.seconds

        // Lots of data is being sent over the next access event.
        $next_access_data_exfil.network.sent_bytes > 10 * 1024 * 1024 * 1024 // 10GB

        // Extract hostname of next access event, for match section.
        $hostname = $next_access_data_exfil.principal.hostname

    match:
        $hostname over 1h

    condition:
        $first_access and $next_access_data_exfil and $first_last_seen
}
Use geolocation-enriched fields in rules
UDM fields that store geolocation-enriched data can be used in Detection Engine rules.
For a list of UDM fields that are populated, see
Enrich events with geolocation data
.
The following example illustrates how to detect if a user entity is authenticating
from multiple distinct states.
rule geoip_user_login_multiple_states_within_1d {

  meta:
    author = "Google Security Operations"
    description = "Detect multiple authentication attempts from multiple distinct locations using geolocation-enriched UDM fields."
    severity = "INFORMATIONAL"

  events:
    $geoip.metadata.event_type = "USER_LOGIN"
    (
      $geoip.metadata.vendor_name = "Google Workspace" or
      $geoip.metadata.vendor_name = "Google Cloud Platform"
    )
    /* optionally, detect distinct locations at a country */
    (
      $geoip.principal.ip_geo_artifact.location.country_or_region != "" and
      $geoip.principal.ip_geo_artifact.location.country_or_region = $country
    )
    (
      $geoip.principal.ip_geo_artifact.location.state != "" and
      $geoip.principal.ip_geo_artifact.location.state = $state
    )

    $geoip.target.user.email_addresses = $user

  match:
    $user over 1d

  condition:
    $geoip and #state > 1
}
Use Safe Browsing enriched fields in rules
Google SecOps ingests data from threat lists related to file hashes.
This enriched information is stored as Entities in Google SecOps.
For a list of UDM fields that are populated, see
Enrich entities with information from Safe Browsing threat lists
.
You can create Detection Engine rules to identify matches against entities
ingested from Safe Browsing. The following is an example Detection Engine
rule that queries against this enriched information to build context-aware analytics.
rule safe_browsing_file_execution {
    meta:
        author = "Google Security Operations"
        description = "Example usage of Safe Browsing data, to detect execution of a file that's been deemed malicious"
        severity = "LOW"

    events:
        // find a process launch event, match on hostname
        $execution.metadata.event_type = "PROCESS_LAUNCH"
        $execution.principal.hostname = $hostname

        // join execution event with Safe Browsing graph
        $sb.graph.entity.file.sha256 = $execution.target.process.file.sha256

        // look for files deemed malicious
        $sb.graph.metadata.entity_type = "FILE"
        $sb.graph.metadata.threat.severity = "CRITICAL"
        $sb.graph.metadata.product_name = "Google Safe Browsing"
        $sb.graph.metadata.source_type = "GLOBAL_CONTEXT"

    match:
        $hostname over 1h

    condition:
        $execution and $sb
}
Use WHOIS enriched fields in a rule
You can write rules that search WHOIS enriched fields in entities that
represent a domain. These entities have the
entity.metadata.entity_type
field
set to
DOMAIN_NAME
. For a list of UDM fields that are populated, see
Enrich entities with WHOIS data
.
The following is an example rule showing how to do this. This rule includes the
following filter fields in the
events
section to help optimize performance of the rule.
$whois.graph.metadata.entity_type = "DOMAIN_NAME"
$whois.graph.metadata.product_name = "WHOISXMLAPI Simple Whois"
$whois.graph.metadata.vendor_name = "WHOIS"
rule whois_expired_domain_executable_download {
 meta:
   author = "Google Security Operations"
   description = "Example usage of WHOIS data, detecting an executable file download from a domain that's recently expired"
   severity = "LOW"

 events:
        $access.metadata.event_type = "NETWORK_HTTP"
        $hostname = $access.principal.hostname

        // join access event to entity graph to use WHOIS data
        $whois.graph.entity.domain.name = $access.target.hostname

        // use WHOIS data to look for expired domains
        $whois.graph.metadata.entity_type = "DOMAIN_NAME"
        $whois.graph.metadata.product_name = "WHOISXMLAPI Simple Whois"
        $whois.graph.metadata.vendor_name = "WHOIS"
        $whois.graph.entity.domain.expiration_time.seconds < $access.metadata.event_timestamp.seconds

        // join access event with executable file creation event by principal hostname
        $creation.principal.hostname = $access.principal.hostname
        $creation.metadata.event_type = "FILE_CREATION"
        $creation.target.file.full_path = /exe/ nocase

        // file creation comes after expired domain access
        $creation.metadata.event_timestamp.seconds >
           $access.metadata.event_timestamp.seconds

   match:
       $hostname over 1h

 condition:
        $access and $whois and $creation
}
Query Google Cloud Threat Intelligence data
Google SecOps ingests data from Google Cloud Threat Intelligence (GCTI)
data sources that provide you with contextual information you can use when
investigating activity in your environment. You can query the following data sources:
GCTI Tor Exit Nodes
GCTI Benign Binaries
GCTI Remote Access Tools
For a description of these threat feeds and all fields populated, see
Ingest and store Google Cloud Threat Intelligence data
.
In this document, the placeholder
<variable_name>
represents the unique variable name
used in a rule to identify a UDM record.
Query Tor exit node IP addresses
The following example rule returns a detection when a
NETWORK_CONNECTION
event contains an IP address stored in the
target.ip
field that is also found
in the GCTI
Tor Exit Nodes
data source. Make sure to include the
<variable_name>.graph.metadata.threat.threat_feed_name
,
<variable_name>.graph.metadata.vendor_name
,
and
<variable_name>.graph.metadata.product_name
fields in the rule.
This is a timed data source. Events will match with the snapshot of the data source at
that point in time.
rule gcti_tor_exit_nodes {
  meta:
    author = "Google Cloud Threat Intelligence"
    description = "Alert on known Tor exit nodes."
    severity = "High"

  events:
    // Event
    $e.metadata.event_type = "NETWORK_CONNECTION"
    $e.target.ip = $tor_ip

    // Tor IP search in GCTI Feed
    $tor.graph.entity.artifact.ip = $tor_ip
    $tor.graph.metadata.entity_type = "IP_ADDRESS"
    $tor.graph.metadata.threat.threat_feed_name = "Tor Exit Nodes"
    $tor.graph.metadata.source_type = "GLOBAL_CONTEXT"
    $tor.graph.metadata.vendor_name = "Google Cloud Threat Intelligence"
    $tor.graph.metadata.product_name = "GCTI Feed"

  match:
    $tor_ip over 1h

  outcome:
    $tor_ips = array_distinct($tor_ip)
    $tor_geoip_country = array_distinct($e.target.ip_geo_artifact.location.country_or_region)
    $tor_geoip_state = array_distinct($e.target.ip_geo_artifact.location.state)

  condition:
    $e and $tor
}
Query for benign operating system files
The following example rule combines the
Benign Binaries
and
Tor Exit Nodes
data sources
to return an alert when a benign binary contacts a Tor exit node. The rule calculates
a risk score using the
geolocation data
that Google SecOps enriched using the target IP address. Make sure to include the
<variable_name>.graph.metadata.vendor_name
,
<variable_name>.graph.metadata.product_name
,
and
<variable_name>.graph.metadata.threat.threat_feed_name
for both the
Benign Binaries
and
Tor Exit Nodes
data sources in the rule.
This is a timeless data source. Events will always match with the latest snapshot
of the data source, regardless of time.
rule gcti_benign_binaries_contacts_tor_exit_node {
 meta:
   author = "Google Cloud Threat Intelligence"
   description = "Alert on Benign Binary contacting a Tor IP address."
   severity = "High"

 events:
   // Event
   $e.metadata.event_type = "NETWORK_CONNECTION"
   $e.principal.process.file.sha256 = $benign_hash
   $e.target.ip = $ip
   $e.principal.hostname = $hostname

   // Benign File search in GCTI Feed
   $benign.graph.entity.file.sha256 = $benign_hash
   $benign.graph.metadata.entity_type = "FILE"
   $benign.graph.metadata.threat.threat_feed_name = "Benign Binaries"
   $benign.graph.metadata.source_type = "GLOBAL_CONTEXT"
   $benign.graph.metadata.vendor_name = "Google Cloud Threat Intelligence"
   $benign.graph.metadata.product_name = "GCTI Feed"

   // Tor IP search in GCTI Feed
   $tor.graph.entity.artifact.ip = $ip
   $tor.graph.metadata.entity_type = "IP_ADDRESS"
   $tor.graph.metadata.threat.threat_feed_name = "Tor Exit Nodes"
   $tor.graph.metadata.source_type = "GLOBAL_CONTEXT"
   $tor.graph.metadata.vendor_name = "Google Cloud Threat Intelligence"
   $tor.graph.metadata.product_name = "GCTI Feed"

 match:
   $hostname over 1h

 outcome:
   $risk_score = max(
       if($tor.graph.metadata.threat.confidence = "HIGH_CONFIDENCE", 70) +
       // Unauthorized target geographies
       if($e.target.ip_geo_artifact.location.country_or_region = "Cuba", 20) +
       if($e.target.ip_geo_artifact.location.country_or_region = "Iran", 20) +
       if($e.target.ip_geo_artifact.location.country_or_region = "North Korea", 20) +
       if($e.target.ip_geo_artifact.location.country_or_region = "Russia", 20) +
       if($e.target.ip_geo_artifact.location.country_or_region = "Syria", 20)
   )
   $benign_hashes = array_distinct($benign_hash)
   $benign_files = array_distinct($e.principal.process.file.full_path)
   $tor_ips = array_distinct($ip)
   $tor_geoip_country = array_distinct($e.target.ip_geo_artifact.location.country_or_region)
   $tor_geoip_state = array_distinct($e.target.ip_geo_artifact.location.state)

 condition:
   $e and $benign and $tor
}
Query data about remote access tools
The following example rule returns a detection when a
PROCESS_LAUNCH
event type
contains a hash that is also found in the Google Cloud Threat Intelligence
Remote Access Tools data source.
This is a timeless data source. Events will always match with the latest snapshot of
the data source, regardless of time.
rule gcti_remote_access_tools {
 meta:
   author = "Google Cloud Threat Intelligence"
   description = "Alert on Remote Access Tools."
   severity = "High"

 events:
    // find a process launch event
    $e.metadata.event_type = "PROCESS_LAUNCH"
    $e.target.process.file.sha256 != ""
    $rat_hash = $e.target.process.file.sha256

    // join graph and event hashes
    $gcti.graph.entity.file.sha256 = $rat_hash

    // look for files identified as likely remote access tools
    $gcti.graph.metadata.entity_type = "FILE"
    $gcti.graph.metadata.vendor_name = "Google Cloud Threat Intelligence"
    $gcti.graph.metadata.product_name = "GCTI Feed"
    $gcti.graph.metadata.threat.threat_feed_name = "Remote Access Tools"

  match:
    $rat_hash over 5m

 outcome:
   $remote_hash = array_distinct($e.target.process.file.sha256)

  condition:
    $e and $gcti

}
Use VirusTotal enriched metadata fields in rules
The following rule detects file creation or process launch of a specific file
type, indicating that some watchlisted hashes are on the system. The risk score
is set when the files are tagged as
exploit
using VirusTotal file metadata
enrichment.
For a list of all UDM fields that are populated, see
Enrich events with VirusTotal file metadata
.
rule vt_filemetadata_hash_match_ioc {
 meta:
   author = "Google Cloud Threat Intelligence"
   description = "Detect file/process events that indicate watchlisted hashes are on a system"
   severity = "High"

 events:
   // Process launch or file creation events
   $process.metadata.event_type = "PROCESS_LAUNCH" or $process.metadata.event_type ="FILE_CREATION"
   $process.principal.hostname = $hostname
   $process.target.file.sha256 != ""
   $process.target.file.sha256 = $sha256
   $process.target.file.file_type = "FILE_TYPE_DOCX"

   // IOC matching
   $ioc.graph.metadata.product_name = "MISP"
   $ioc.graph.metadata.entity_type = "FILE"
   $ioc.graph.metadata.source_type = "ENTITY_CONTEXT"
   $ioc.graph.entity.file.sha256 = $sha256

 match:
   $hostname over 15m

 outcome:
   $risk_score = max(
       // Tag enrichment from VirusTotal file metadata
       if($process.target.file.tags = "exploit", 90)
   )
   $file_sha256 = array($process.target.file.sha256)
   $host = array($process.principal.hostname)

 condition:
   $process and $ioc
}
Use VirusTotal relationship data in rules
Google SecOps ingests data from VirusTotal related connections. This data
provides information about the relation between file hashes and files, domains,
IP addresses, and URLs. This enriched information is stored as Entities in Google SecOps.
You can create Detection Engine rules to identify matches against entities ingested
from VirusTotal. The following rule sends an alert on downloading a known file hash
from a known IP address with VirusTotal relationships. The risk score is based on
file type and tags from VirusTotal file metadata.
This data is only available for certain VirusTotal and Google SecOps licenses. 
Check your entitlements with your account manager. For a list
of all UDM fields that are populated, see
Enrich entities with VirusTotal relationship data
.
rule virustotal_file_downloaded_from_url {
  meta:
    author = "Google Cloud Threat Intelligence"
    description = "Alerts on downloading a known file hash from a known IP with VirusTotal relationships. The risk score is based on file type and tags from VirusTotal file metadata."
    severity = "High"

  events:
    // Filter network HTTP events
    $e1.metadata.event_type = "NETWORK_HTTP"
    $e1.principal.user.userid = $userid
    $e1.target.url = $url

    // Filter file creation events
    $e2.metadata.event_type = "FILE_CREATION"
    $e2.target.user.userid = $userid
    $e2.target.file.sha256 = $file_hash

    // The file creation event timestamp should be equal or greater than the network http event timestamp
    $e1.metadata.event_timestamp.seconds <= $e2.metadata.event_timestamp.seconds

    // Join event file hash with VirusTotal relationships entity graph
    $vt.graph.metadata.entity_type = "FILE"
    $vt.graph.metadata.source_type = "GLOBAL_CONTEXT"
    $vt.graph.metadata.vendor_name = "VirusTotal"
    $vt.graph.metadata.product_name = "VirusTotal Relationships"
    $vt.graph.entity.file.sha256 = $file_hash

    // Join network HTTP target URL with VirusTotal relationships entity graph
    $vt.graph.relations.entity_type = "URL"
    $vt.graph.relations.relationship = "DOWNLOADED_FROM"
    $vt.graph.relations.entity.url = $url

  match:
    $userid over 1m

  outcome:
      $risk_score = max(
        // Tag enrichment from VirusTotal file metadata
        if($e2.target.file.tags = "via-tor" or $e2.target.file.tags = "malware" or $e2.target.file.tags = "crypto", 50) +
        // File types enrichment from VirusTotal file metadata
        if($e2.target.file.file_type = "FILE_TYPE_HTML", 5) +
        if($e2.target.file.file_type = "FILE_TYPE_ELF", 10) +
        if($e2.target.file.file_type = "FILE_TYPE_PE_DLL",15) +
        if($e2.target.file.file_type = "FILE_TYPE_PE_EXE", 20)
    )

  condition:
    $e1 and $e2 and $vt and $risk_score >= 50
}
Eventual consistency
Enrichment-dependent rules rely on additional data to be processed before a rule can be fully evaluated. Over time, the enrichment process completes and the rule is re-evaluated with the latest, accurate data. This process of eventual consistency is expected and means that while there might be initial inconsistencies, the system ensures that all events will eventually be fully enriched and rules will be accurately evaluated. Learn
how Google SecOps enriches event and entity data
.
What's next
For information about how to use enriched data with other Google SecOps
features, see the following:
Use context-enriched data in UDM Search
.
Use context-enriched data in reports
.
Need more help?
Get answers from Community members and Google SecOps professionals.
