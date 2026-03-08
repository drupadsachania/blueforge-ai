# Use context-enriched data in reports

**Source:** https://docs.cloud.google.com/chronicle/docs/reports/use-enriched-data-in-reports/  
**Scraped:** 2026-03-05T10:09:45.924205Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use context-enriched data in reports
Supported in:
Google secops
SIEM
To support security investigations, Google Security Operations ingests contextual
data from different sources, performs analysis on the ingested data, and
provides additional context about artifacts in a customer environment. This
document provides examples of how analysts can use contextual enriched data
in dashboards and in Google SecOps schemas in BigQuery.
For more information about data enrichment, see
How Google SecOps enriches event and entity data
.
Use geolocation-enriched data
UDM events may include geolocation-enriched data to provide additional context
during an investigation. When UDM events are exported to BigQuery,
these fields are also exported. This section explains how to use geolocation-enriched fields when creating reports.
Query data in the
events
schema
Geolocation data can be queried using the Google SecOps
events
schema in BigQuery.
The following example is a SQL query that returns aggregate results for all
USER_LOGIN
events by user, country, and with the first and last observed times.
SELECT
 ip_geo_artifact.location.country_or_region,
 COUNT(ip_geo_artifact.location.country_or_region) AS count_country,
 ip_geo_artifact.location.state,
 COUNT(ip_geo_artifact.location.state) AS count_state,
 target.user.email_addresses[ORDINAL(1)] AS principal_user,
 TIMESTAMP_SECONDS(MIN(metadata.event_timestamp.seconds)) AS first_observed,
 TIMESTAMP_SECONDS(MAX(metadata.event_timestamp.seconds)) AS last_observed,
FROM `datalake.events`,
UNNEST (principal.ip_geo_artifact) as ip_geo_artifact
WHERE DATE(hour_time_bucket) = "2023-01-11"
AND metadata.event_type = 15001
AND metadata.vendor_name IN ("Google Cloud Platform","Google Workspace")
GROUP BY 1,3,5
HAVING count_country > 0
ORDER BY count_country DESC
The following table contains an example of the results that might be returned.
country_or_region
count_country
state
count_state
principal_user
first_observed
last_observed
Netherlands
5
North Holland
5
admin@acme.com
2023-01-11 14:32:51 UTC
2023-01-11 14:32:51 UTC
Israel
1
Tel Aviv District
1
omri@acme.com
2023-01-11 10:09:32 UTC
2023-01-11 15:26:38 UTC
The following SQL query illustrates how to detect the distance between two locations.
SELECT
DISTINCT principal_user,
(ST_DISTANCE(north_pole,user_location)/1000) AS distance_to_north_pole_km
FROM (
  SELECT
    ST_GeogPoint(135.00,90.00) AS north_pole,
    ST_GeogPoint(ip_geo_artifact.location.region_coordinates.longitude, ip_geo_artifact.location.region_coordinates.latitude) AS user_location,
    target.user.email_addresses[ORDINAL(1)] AS principal_user
  FROM `datalake.events`,
  UNNEST (principal.ip_geo_artifact) as ip_geo_artifact
  WHERE DATE(hour_time_bucket) = "2023-01-11"
  AND metadata.event_type = 15001
  AND metadata.vendor_name IN ("Google Cloud Platform","Google Workspace")
  AND ip_geo_artifact.location.country_or_region != ""
)
ORDER BY 2 DESC
The following table contains an example of the results that might be returned.
principal_user
distance_to_north_pole_km
omri@acme.com
6438.98507
admin@acme.com
4167.527018
You can achieve slightly more useful queries by leveraging area polygons to
calculate a reasonable area for travel from a location in a given interval.
You can also check whether multiple geography values match to identify impossible
travel detections. These solutions require having an accurate and consistent geolocation data source.
View enriched fields in dashboards
You can also build a dashboard using geolocation-enriched UDM fields. The chart
displays the city of each UDM event. You can change the chart type to see the
data in a different format.
What's next
For information about how to use enriched data with other Google SecOps
features, see the following:
Use context-enriched data in rules
.
Use context-enriched data in UDM Search
.
Need more help?
Get answers from Community members and Google SecOps professionals.
