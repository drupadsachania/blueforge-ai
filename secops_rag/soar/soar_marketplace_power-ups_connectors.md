# Connectors

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/power-ups/connectors/  
**Scraped:** 2026-03-05T10:10:03.164649Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Connectors
Supported in:
Google secops
SOAR
Overview
A set of custom connectors used to power up automation capabilities.
Connectors
Cron Scheduled Connector
Description
A custom connector created to trigger playbooks by a given alert product, name
  and type and enables editing the parameters according to your specific use
  case. Allows the use of a cron expression.
Using the
Run Every
parameter, we recommend updating the connector's scheduled execution from 59 seconds to 1 hour
  and the cron expression accordingly (* 16 * * FRI) to reflect the new schedule.
  This change ensures that the connector code runs once every hour. The execution 
  is not guaranteed to occur exactly at the top of the hour—it will be triggered once at some point during the specified hour.
Configuration
To configure a connector, go to Settings -> Connectors -> Create New
  Connector and search for Cron Scheduled Connector.
Parameters
-
Parameter
Type
Default value
Is Mandatory
Description
Run Every
Integers
10 seconds
No
Specify the run schedule.
Product Field Name
String
Yes
Specify the source field name to retrieve the Product Field name.
Event Field Name
String
event_type
Yes
Specify the source field name to retrieve the Event Field name.
Alert fields
JSON
Yes
Specify the Alert fields you would like to insert in JSON format.
Alert name
String
Yes
Specify the Alert fields associated with the alert that will be created.
Alert type
String
No
Specify the Alert type associated with the alert that will be created.
Cron expression
String
* * * * *
No
If defined, will determine when the connector should create a case.
Product Name
String
No
Specify the product name associated with the alert that will be created.
PythonProcessTimeout
Integer
30
Yes
Specify the timeout limit (in seconds) for the python process running
        the current script.
Scheduled Connector
Description
A custom connector created to trigger playbooks by a given alert product, name
  and type and enables editing the parameters according to your specific use
  case.
Configuration
To configure a connector, go to Settings -> Connectors -> Create New
  Connector and search for Scheduled Connector.
Parameters
Parameter
Type
Default value
Is Mandatory
Description
Run Every
Integers
10 seconds
No
Specify the run schedule.
Product Field Name
String
Yes
Specify the source field name to retrieve the Product Field name.
Event Field Name
String
event_type
Yes
Specify the source field name to retrieve the Event Field name.
Alert fields
JSON
Yes
Specify the Alert fields you want to insert in JSON format.
Alert name
String
Yes
Specify the Alert fields associated with the alert that will be created.
Alert type
String
No
Specify the Alert type associated with the alert that will be created.
Product Name
String
No
Specify the product name associated with the alert that will be created.
PythonProcessTimeout
Integer
30
Yes
Specify the timeout limit (in seconds) for the python process running
        the current script.
Need more help?
Get answers from Community members and Google SecOps professionals.
