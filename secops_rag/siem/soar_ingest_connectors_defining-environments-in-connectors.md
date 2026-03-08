# Define environments in connectors

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/defining-environments-in-connectors/  
**Scraped:** 2026-03-05T09:31:02.611630Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Define environments in connectors
Supported in:
Google secops
SOAR
You can set up connectors in various ways, as each connector has its own 
  configuration. Here are some ways you can define connectors:
Set a static environment:
define the environment in the
Environment
field in the specific connector on the Google Security Operations platform.
Extract environment dynamically
: define the environment in the
Environment Field Name
field. The environment is extracted from that
  field.
Extract environment dynamically + regular expression pattern
: define 
  the option in the
Environment Regex Pattern
field and
  the environment is extracted from that field by the regular expression
  pattern.
Use third-party multi-tenant mechanism
: Define the
  environment in the
Environment
field using the third-party tenant name. Some
  integrations have a built-in, multi-tenant mechanism with a checkbox that lets you set the
Environment
field by the third-party tenant name.
In some cases, the extracted environment field value is different from the
  Google SecOps environment. For example, the
Environment
field is
altostrat.com
, while the Google SecOps 
  environment is called
altostrat
.
Define alias names
To define an alias name, follow these steps:
Go to
SOAR Settings
>
Organization
>
Environments
.
Click
add
Add Environment
to match the name in the integration
with the name of the environment in the Google SecOps platform.
Troubleshooting
If after the entire process, the connector has no environment or an empty
  environment (
""
), the default overrides the empty result. If the
  connector contains values that define an uncreated environment, then alerts
  are ingested in the database and playbooks start to run. As soon as the new
  environment is created, the cases and playbooks are displayed in the platform.
To stop alerts related to non-existent environments from being ingested into
  the database, you can contact
Google SecOps Support
and request they make the change in the database configuration.
Need more help?
Get answers from Community members and Google SecOps professionals.
