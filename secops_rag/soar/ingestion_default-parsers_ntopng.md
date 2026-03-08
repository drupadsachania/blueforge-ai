# Collect ntopng logs

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ntopng/  
**Scraped:** 2026-03-05T09:58:42.579053Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect ntopng logs
Supported in:
Google secops
SIEM
Overview
This parser extracts ntopng network monitoring logs in either SYSLOG or JSON format. It parses the log message, converts the relevant fields into the UDM format, and enriches the event with metadata like product and vendor names. The parser also handles nested JSON structures and maps specific ntopng fields to UDM network events, including flow alerts and user resource access.
Before you begin
Ensure that you have the following prerequisites:
Google SecOps instance.
Privileged access to ntopng.
Set up feeds
To configure a feed, follow these steps:
Go to
SIEM Settings
>
Feeds
.
Click
Add New Feed
.
On the next page, click
Configure a single feed
.
In the
Feed name
field, enter a name for the feed; for example,
Ntopng Logs
.
Select
Webhook
as the
Source type
.
Select
Ntopng
as the
Log type
.
Click
Next
.
Optional: Specify values for the following input parameters:
Split delimiter
: the delimiter that is used to separate log lines, such as
\n
.
Click
Next
.
Review the feed configuration in the
Finalize
screen, and then click
Submit
.
Click
Generate Secret Key
to generate a secret key to authenticate this feed.
Copy and store the secret key. You cannot view this secret key again. If needed, you can regenerate a new secret key, but this action makes the previous secret key obsolete.
From the
Details
tab, copy the feed endpoint URL from the
Endpoint Information
field. You need to specify this endpoint URL in your client application.
Click
Done
.
Create an API key for the webhook feed
Go to
Google Cloud console
>
Credentials
.
Go to Credentials
Click
Create credentials
, and then select
API key
.
Restrict the API key access to the
Google Security Operations API
.
Specify the endpoint URL
In your client application, specify the HTTPS endpoint URL provided in the webhook feed.
Enable authentication by specifying the API key and secret key as part of the custom header in the following format:
X-goog-api-key =
API_KEY
X-Webhook-Access-Key =
SECRET
Recommendation
: Specify the API key as a header instead of specifying it in the URL.
If your webhook client doesn't support custom headers, you can specify the API key and secret key using query parameters in the following format:
ENDPOINT_URL
?key=
API_KEY
&secret=
SECRET
Replace the following:
ENDPOINT_URL
: the feed endpoint URL.
API_KEY
: the API key to authenticate to Google Security Operations.
SECRET
: the secret key that you generated to authenticate the feed.
Configuring a Webhook on ntopng for Google SecOps
Sign in to ntopng Web interface.
Select
System
menu from the drop-down.
Go to
Notifications
>
Endpoints
.
Click
add
.
Specify values for the following input parameters:
Endpoint Name
: Provide a unique and descriptive name (for example,
Google SecOps
).
Endpoint Type
: Select
Webhook
from the list.
Webhook URL
: Enter the Google SecOps
ENDPOINT_URL
with
API_KEY
and
SECRET
.
Click
Add
.
Go to
Notifications
>
Recipients
.
Click
add
.
Specify values for the following input parameters:
Recipient Name
: Provide a unique and descriptive name (for example,
Google SecOps
).
Select Endpoint
: Select the endpoint created earlier.
Severity
: Select the severity to send to Google SecOps (for example,
Info, Warning and Error
).
Category Filter
: Select what to send to Google SecOps.
Click
Test Recipient
to verify the connection.
Click
Add
to save the webhook.
Configuring ntopng webhook resource subscribers
Go to
Pools
.
Select the
resource
to share the events from.
Click
pencil icon
in the
Actions
column.
Click the
Recipients
drop-down.
Select the
Google SecOps
Webhook Recipient.
Click
Edit
to save the configuration.
Repeat the process for other resources.
UDM Mapping Table
Log Field
UDM Mapping
Logic
action
security_result.detection_fields.key=action
,
security_result.detection_fields.value=%{action}
The value of
action
from the raw log is mapped to a
security_result.detection_fields
object with key "action".
alert_generation.host_info.broadcast_domain_host
security_result.detection_fields.key=host_info broadcast_domain_host
,
security_result.detection_fields.value=%{alert_generation.host_info.broadcast_domain_host}
The value of
alert_generation.host_info.broadcast_domain_host
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info broadcast_domain_host".
alert_generation.host_info.dhcpHost
security_result.detection_fields.key=host_info dhcpHost
,
security_result.detection_fields.value=%{alert_generation.host_info.dhcpHost}
The value of
alert_generation.host_info.dhcpHost
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info dhcpHost".
alert_generation.host_info.is_blacklisted
security_result.detection_fields.key=host_info is_blacklisted
,
security_result.detection_fields.value=%{alert_generation.host_info.is_blacklisted}
The value of
alert_generation.host_info.is_blacklisted
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info is_blacklisted".
alert_generation.host_info.is_broadcast
security_result.detection_fields.key=host_info is_broadcast
,
security_result.detection_fields.value=%{alert_generation.host_info.is_broadcast}
The value of
alert_generation.host_info.is_broadcast
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info is_broadcast".
alert_generation.host_info.is_multicast
security_result.detection_fields.key=host_info is_multicast
,
security_result.detection_fields.value=%{alert_generation.host_info.is_multicast}
The value of
alert_generation.host_info.is_multicast
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info is_multicast".
alert_generation.host_info.localhost
security_result.detection_fields.key=host_info localhost
,
security_result.detection_fields.value=%{alert_generation.host_info.localhost}
The value of
alert_generation.host_info.localhost
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info localhost".
alert_generation.host_info.privatehost
security_result.detection_fields.key=host_info privatehost
,
security_result.detection_fields.value=%{alert_generation.host_info.privatehost}
The value of
alert_generation.host_info.privatehost
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info privatehost".
alert_generation.host_info.systemhost
security_result.detection_fields.key=host_info systemhost
,
security_result.detection_fields.value=%{alert_generation.host_info.systemhost}
The value of
alert_generation.host_info.systemhost
from the nested JSON is mapped to a
security_result.detection_fields
object with key "host_info systemhost".
alert_generation.script_key
security_result.category_details=%{alert_generation.script_key}
The value of
alert_generation.script_key
from the nested JSON is mapped to
security_result.category_details
.
alert_generation.subdir
security_result.detection_fields.key=alert_generation_subdir
,
security_result.detection_fields.value=%{alert_generation.subdir}
The value of
alert_generation.subdir
from the nested JSON is mapped to a
security_result.detection_fields
object with key "alert_generation_subdir".
alert_id
security_result.detection_fields.key=alert_id
,
security_result.detection_fields.value=%{alert_id}
The value of
alert_id
from the raw log is mapped to a
security_result.detection_fields
object with key "alert_id".
alerts_map
security_result.detection_fields.key=alerts_map
,
security_result.detection_fields.value=%{alerts_map}
The value of
alerts_map
from the raw log is mapped to a
security_result.detection_fields
object with key "alerts_map".
cli2srv_bytes
network.sent_bytes
The value of
cli2srv_bytes
from the raw log is converted to an unsigned integer and mapped to
network.sent_bytes
.
cli_asn
principal.resource.attribute.labels.key=cli_asn
,
principal.resource.attribute.labels.value=%{cli_asn}
The value of
cli_asn
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "cli_asn".
cli_blacklisted
principal.resource.attribute.labels.key=cli_blacklisted
,
principal.resource.attribute.labels.value=%{cli_blacklisted}
The value of
cli_blacklisted
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "cli_blacklisted".
cli_city_name
principal.location.city
The value of
cli_city_name
from the raw log is mapped to
principal.location.city
.
cli_continent_name
principal.resource.attribute.labels.key=cli_continent_name
,
principal.resource.attribute.labels.value=%{cli_continent_name}
The value of
cli_continent_name
from the raw log is mapped to a
principal.resource.attribute.labels
object with key "cli_continent_name".
cli_country_name
principal.location.country_or_region
The value of
cli_country_name
from the raw log is mapped to
principal.location.country_or_region
.
cli_host_pool_id
principal.resource.attribute.labels.key=cli_host_pool_id
,
principal.resource.attribute.labels.value=%{cli_host_pool_id}
The value of
cli_host_pool_id
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "cli_host_pool_id".
cli_ip
principal.ip
,
principal.asset.ip
The value of
cli_ip
from the raw log is mapped to
principal.ip
and
principal.asset.ip
.
cli_localhost
principal.resource.attribute.labels.key=cli_localhost
,
principal.resource.attribute.labels.value=%{cli_localhost}
The value of
cli_localhost
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "cli_localhost".
cli_location
principal.location.name
The value of
cli_location
from the raw log is converted to a string. If it's not "0", it's mapped to
principal.location.name
.
cli_name
principal.hostname
,
principal.asset.hostname
The value of
cli_name
from the raw log is mapped to
principal.hostname
and
principal.asset.hostname
.
cli_network
principal.resource.attribute.labels.key=cli_network
,
principal.resource.attribute.labels.value=%{cli_network}
The value of
cli_network
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "cli_network".
cli_port
principal.port
The value of
cli_port
from the raw log is converted to an integer and mapped to
principal.port
.
entity_id
principal.resource.attribute.labels.key=entity_id
,
principal.resource.attribute.labels.value=%{entity_id}
The value of
entity_id
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "entity_id".
entity_val
principal.resource.attribute.labels.key=entity_val
,
principal.resource.attribute.labels.value=%{entity_val}
The value of
entity_val
from the raw log is mapped to a
principal.resource.attribute.labels
object with key "entity_val", unless it's equal to the value of
ip
.
event.type
metadata.event_type
Determined by parser logic based on the presence of
principal
,
target
, and
network
fields.  Possible values:
NETWORK_FLOW
,
NETWORK_UNCATEGORIZED
,
USER_RESOURCE_ACCESS
,
GENERIC_EVENT
.
first_seen
principal.asset.first_seen_time
The value of
first_seen
from the raw log is converted to a string, parsed as milliseconds since epoch, and mapped to
principal.asset.first_seen_time
.
flow_risk_bitmap
security_result.detection_fields.key=flow_risk_bitmap
,
security_result.detection_fields.value=%{flow_risk_bitmap}
The value of
flow_risk_bitmap
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "flow_risk_bitmap".
granularity
security_result.detection_fields.key=granularity
,
security_result.detection_fields.value=%{granularity}
The value of
granularity
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "granularity".
hash_entry_id
security_result.detection_fields.key=hash_entry_id
,
security_result.detection_fields.value=%{hash_entry_id}
The value of
hash_entry_id
from the nested JSON is mapped to a
security_result.detection_fields
object with key "hash_entry_id".
host_ip
principal.ip
,
principal.asset.ip
The IP address extracted from the
<INT>Oct 20 15:34:53 1.1.1.1
part of the message is mapped to
principal.ip
and
principal.asset.ip
.
ifid
principal.asset_id
The value of
ifid
from the raw log is converted to a string and mapped to
principal.asset_id
with the prefix "ifid: ".
ip
principal.ip
,
principal.asset.ip
or
target.ip
,
target.asset.ip
If
is_client
is true, the value of
ip
from the raw log is mapped to
principal.ip
and
principal.asset.ip
. If
is_server
is true, it's mapped to
target.ip
and
target.asset.ip
.
is_cli_attacker
security_result.detection_fields.key=is_cli_attacker
,
security_result.detection_fields.value=%{is_cli_attacker}
The value of
is_cli_attacker
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "is_cli_attacker".
is_cli_victim
security_result.detection_fields.key=is_cli_victim
,
security_result.detection_fields.value=%{is_cli_victim}
The value of
is_cli_victim
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "is_cli_victim".
is_flow_alert
security_result.detection_fields.key=is_flow_alert
,
security_result.detection_fields.value=%{is_flow_alert}
,
security_result.detection_fields.key=alert type
,
security_result.detection_fields.value=flow
The value of
is_flow_alert
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "is_flow_alert". If
is_flow_alert
is true, a
security_result.detection_fields
object with key "alert type" and value "flow" is also created.
is_srv_attacker
security_result.detection_fields.key=is_srv_attacker
,
security_result.detection_fields.value=%{is_srv_attacker}
The value of
is_srv_attacker
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "is_srv_attacker".
is_srv_victim
security_result.detection_fields.key=is_srv_victim
,
security_result.detection_fields.value=%{is_srv_victim}
The value of
is_srv_victim
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "is_srv_victim".
metadata.product_name
metadata.product_name=NTOPNG
Hardcoded to "NTOPNG".
metadata.vendor_name
metadata.vendor_name=%{vendor_name}
The value of
vendor_name
from the message is mapped to
metadata.vendor_name
.
name
principal.hostname
,
principal.asset.hostname
or
target.hostname
,
target.asset.hostname
If
is_client
is true, the value of
name
from the raw log is mapped to
principal.hostname
and
principal.asset.hostname
. If
is_server
is true, it's mapped to
target.hostname
and
target.asset.hostname
.
ntopng_key
security_result.detection_fields.key=ntopng_key
,
security_result.detection_fields.value=%{ntopng_key}
The value of
ntopng.key
(renamed to
ntopng_key
) from the nested JSON is mapped to a
security_result.detection_fields
object with key "ntopng_key".
observation_point_id
observer.asset_id
The value of
observation_point_id
from the raw log is converted to a string. If it's not "0", it's mapped to
observer.asset_id
with the prefix "id: ".
pool_id
principal.resource.attribute.labels.key=pool_id
,
principal.resource.attribute.labels.value=%{pool_id}
The value of
pool_id
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "pool_id".
probe_ip
intermediary.ip
The value of
probe_ip
from the raw log is mapped to
intermediary.ip
.
proto.confidence
security_result.confidence_details
The value of
proto.confidence
from the raw log is converted to a string and mapped to
security_result.confidence_details
.
proto.http.last_method
network.http.method
The value of
proto.http.last_method
from the raw log is mapped to
network.http.method
.
proto.http.last_return_code
network.http.response_code
The value of
proto.http.last_return_code
from the raw log is converted to an integer and mapped to
network.http.response_code
.
proto.http.last_server_name
network.tls.client.server_name
The value of
proto.http.server_name
from the raw log is mapped to
network.tls.client.server_name
.
proto.http.last_url
network.http.referral_url
The value of
proto.http.last_url
from the raw log is mapped to
network.http.referral_url
.
proto.http.last_user_agent
network.http.user_agent
The value of
proto.http.last_user_agent
from the raw log is mapped to
network.http.user_agent
.
proto.http.server_name
network.tls.client.server_name
The value of
proto.http.server_name
from the raw log is mapped to
network.tls.client.server_name
.
proto.l4
network.ip_protocol
The value of
proto.l4
from the raw log is mapped to
network.ip_protocol
.
proto_ndpi
additional.fields.key=proto ndpi
,
additional.fields.value.string_value=%{proto_ndpi}
,
network.application_protocol
The value of
proto.ndpi
(renamed to
proto_ndpi
) from the raw log is mapped to an
additional.fields
object with key "proto ndpi". It's also used to determine the value of
network.application_protocol
based on keywords like "NTP" and "HTTP".
proto_ndpi_app
principal.application
The value of
proto_ndpi_app
from the raw log is mapped to
principal.application
.
proto_ndpi_breed
security_result.detection_fields.key=proto_ndpi_breed
,
security_result.detection_fields.value=%{proto_ndpi_breed}
The value of
proto_ndpi_breed
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "proto_ndpi_breed".
proto_ndpi_cat
security_result.category_details
The value of
proto_ndpi_cat
from the raw log is mapped to
security_result.category_details
.
proto_ndpi_cat_id
security_result.detection_fields.key=proto_ndpi_cat_id
,
security_result.detection_fields.value=%{proto_ndpi_cat_id}
The value of
proto_ndpi_cat_id
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "proto_ndpi_cat_id".
score
security_result.detection_fields.key=score
,
security_result.detection_fields.value=%{score}
The value of
score
from the raw log is converted to a string and mapped to a
security_result.detection_fields
object with key "score".
srv2cli_bytes
network.received_bytes
The value of
srv2cli_bytes
from the raw log is converted to an unsigned integer and mapped to
network.received_bytes
.
srv_asn
target.resource.attribute.labels.key=srv_asn
,
target.resource.attribute.labels.value=%{srv_asn}
The value of
srv_asn
from the raw log is converted to a string and mapped to a
target.resource.attribute.labels
object with key "srv_asn".
srv_blacklisted
target.resource.attribute.labels.key=srv_blacklisted
,
target.resource.attribute.labels.value=%{srv_blacklisted}
The value of
srv_blacklisted
from the raw log is converted to a string and mapped to a
target.resource.attribute.labels
object with key "srv_blacklisted".
srv_city_name
target.location.city
The value of
srv_city_name
from the raw log is mapped to
target.location.city
.
srv_continent_name
target.resource.attribute.labels.key=srv_continent_name
,
target.resource.attribute.labels.value=%{srv_continent_name}
The value of
srv_continent_name
from the raw log is mapped to a
target.resource.attribute.labels
object with key "srv_continent_name".
srv_country_name
target.location.country_or_region
The value of
srv_country_name
from the raw log is mapped to
target.location.country_or_region
.
srv_host_pool_id
target.resource.attribute.labels.key=srv_host_pool_id
,
target.resource.attribute.labels.value=%{srv_host_pool_id}
The value of
srv_host_pool_id
from the raw log is converted to a string and mapped to a
target.resource.attribute.labels
object with key "srv_host_pool_id".
srv_ip
target.ip
,
target.asset.ip
The value of
srv_ip
from the raw log is mapped to
target.ip
and
target.asset.ip
.
srv_localhost
target.resource.attribute.labels.key=srv_localhost
,
target.resource.attribute.labels.value=%{srv_localhost}
The value of
srv_localhost
from the raw log is converted to a string and mapped to a
target.resource.attribute.labels
object with key "srv_localhost".
srv_location
target.location.name
The value of
srv_location
from the raw log is converted to a string. If it's not "0", it's mapped to
target.location.name
.
srv_location_lat
target.location.region_coordinates.latitude
The value of
srv_location_lat
from the raw log is mapped to
target.location.region_coordinates.latitude
.
srv_location_lon
target.location.region_coordinates.longitude
The value of
srv_location_lon
from the raw log is mapped to
target.location.region_coordinates.longitude
.
srv_name
target.hostname
,
target.asset.hostname
The value of
srv_name
from the raw log is mapped to
target.hostname
and
target.asset.hostname
.
srv_network
target.resource.attribute.labels.key=srv_network
,
target.resource.attribute.labels.value=%{srv_network}
The value of
srv_network
from the raw log is converted to a string and mapped to a
target.resource.attribute.labels
object with key "srv_network".
srv_port
target.port
The value of
srv_port
from the raw log is converted to an integer and mapped to
target.port
.
tstamp
additional.fields.key=tstamp
,
additional.fields.value.string_value=%{tstamp}
The value of
tstamp
from the raw log is converted to a string and mapped to an
additional.fields
object with key "tstamp".
vlan_id
principal.resource.attribute.labels.key=vlan_id
,
principal.resource.attribute.labels.value=%{vlan_id}
The value of
vlan_id
from the raw log is converted to a string and mapped to a
principal.resource.attribute.labels
object with key "vlan_id".
when
metadata.event_timestamp
The value of
when
from the raw log is parsed as a timestamp and mapped to
metadata.event_timestamp
.
Need more help?
Get answers from Community members and Google SecOps professionals.
