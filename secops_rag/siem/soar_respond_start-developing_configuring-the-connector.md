# Configure the connector

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/configuring-the-connector/  
**Scraped:** 2026-03-05T09:35:42.531876Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure the connector
Supported in:
Google secops
SOAR
When you configure a  new connector, the platform uses the connector script in
an integration as a template only. The configured connector is an instance of
that connector template. You can add multiple connectors with different
configurations using the same code you created for the connector in the IDE.
To configure a connector, follow these steps:
Go to
SOAR Settings
>
Ingestion
>
Connectors
to access
    the connectors module and configure a connector under the relevant environment.
Click
add
Create new Connector
.
In the
Add Connector
dialog, select the connector type from the list.
Optional: Select the
Remote Connector
checkbox.
Click
Create
.
In the
Parameters
section, enter the following connector parameters:
Environment
: Defines which environment this connector connects to.
    If you don't need to define the environment, select
Default Environment
.
Run Every
: Defines the interval of connector runs.
Product Field Name
: Required by the connector to identify the product that generates the alerts pulled into Google Security Operations. Don't enter the product name here. Instead, enter the event field (a key from your JSON event) instead of the product name. For example: Put
_index
to indicate that
cloudtrail
is the product that generated the alert.
Event Field Name
: Required by the connector to identify the type of the security event pulled into Google SecOps. Don't enter the event name or type here. Enter the event field (a key from your JSON event) instead of the event name or type.
For example: Enter "
_source.userIdentity.type
" to indicate that
AssumedRole
is the type of the security event.
Event Count Limit
: If you're pulling a correlation alert, indicate the limit of the underlying events Google SecOps should fetch with it. This is required to make a connector run faster (in case the alerts are heavy on redundant events) and reduce the redundancy for security analysts.
The connector is configured under
Default Environment
. Once you fill in all the parameters, click
Save
to save the connector.
For a full list of parameters for each connector, see
Google SecOps response integrations
.
Need more help?
Get answers from Community members and Google SecOps professionals.
