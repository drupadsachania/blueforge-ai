# Use the Content Hub on SOAR standalone platform

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/marketplace/using-the-marketplace/  
**Scraped:** 2026-03-05T09:37:27.697080Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the Content Hub on SOAR standalone platform
Supported in:
SOAR
The Content Hub acts as the customer's toolbox, 
holding a wide range of utilities and options to choose from, including the following:
Integrations
: Integrations to third-party applications and 
custom integrations that you've built in the IDE.
Use Cases
: Prebuilt playbook workflows you can integrate 
into the platform and use to optimize your Google Security Operations installation. 
They include predefined use cases from Google SecOps and customer-uploaded 
use cases to test drive Google SecOps functionality or incorporate into your own use cases.
Power Ups
: Tools created by Google SecOps that enhance your ability to automate processes for playbooks.
Integration types
There are three types of integrations in the Content Hub:
Commercial
: Integrations to third-party applications that 
have been developed by Google SecOps. This category includes both new and updated integrations.
Community
: Integrations published by users. These integrations have been validated 
by Google SecOps and are displayed with the user's details next to them.
Custom
: Integrations that you created and which are only displayed 
on your own Content Hub. These integrations are private to your instance.
Filter integrations
You can filter the integrations according to integration type or by status.
Configure integrations
For more information on installing and configuring an integration, see
Configure integrations
.
For more information about configuring an integration on several instances, see
Supporting multiple instances
.
For more information on integrations, see
Response integrations
.
If an integration update introduces issues, you can revert to the previously 
installed version. For more information, see
Roll back response integration version
.
Ontology override
When you install or upgrade an integration, an on-screen dialog offers you the following two options:
Override (replace mapping)
: This action completely replaces the existing ontology mapping rules. All existing mappings (source, product, event type) are overwritten by the corresponding rules defined in the new integration. This includes the deletion of any custom modifications you may have previously made.
Retain (keep existing mapping)
: This action preserves the existing mapping in its entirety. Use this action if you've implemented significant custom changes to the ontology to meet specific instance requirements.
We recommend exporting the existing ontology mapping rules for each specific integration as a backup, before initiating an override.
For more information about ontology, see
Ontology status
.
Use cases
Use cases provide an end-to-end solution that significantly shortens your time to value by providing predefined solutions to specific SOC challenges. They demonstrate how Google SecOps experts or community users approach common security problems.
Each use case contains relevant items, such as integrations and playbooks, to simulate an entire workflow from end-to-end. After you download one of these use cases, you can choose to simulate it in the
Cases
page. Optionally, you can configure the connector and edit the playbook of a predefined use case and run it on your organization's live data.
Power Ups
Power Ups
are built-in actions provided by Google SecOps, designed to enhance your existing playbooks. These actions require no special configuration as they're inherently included within the Google SecOps platform. 
For specific technical details and usage examples of each available action, click
Read More
within the platform documentation.
Need more help?
Get answers from Community members and Google SecOps professionals.
