# Work with an external vault system

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/working-with-an-external-vault-system/  
**Scraped:** 2026-03-05T09:35:30.442428Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Work with an external vault system
Supported in:
Google secops
SOAR
This document explains how you can store secrets (such as passwords, API keys,
  or certificates) in an external vault—such as CyberArk—and securely pull them
  into the Google Security Operations platform for use in various configurations.
You can reference vault credentials in the following locations:
Integrations
Connectors
Jobs
The following deployment types are supported:
Cloud vault instance
On-premises vault instance (using remote agent)
Use cases
Enterprise organizations can pull credentials from their central vault to
      reduce the risk of unauthorized use of passwords.
Managed Security Service Providers (MSSPs) can pull client credentials
      directly from the client's vault, without exposing passwords to their staff.
Download and configure the vault integration
To install and configure the vault integration, follow these steps:
Go to
Content Hub
and install the CyberArk PAM integration.
Configure the integration using one of these methods:
During installation (for the default environment).
Go to
Response
>
Integrations Setup
and select the appropriate environment.
If you're using an on-premises vault with a remote agent, all third-party
      integrations (whether cloud-based or on-premises) must be configured under
      the same remote agent so it can access the vault.
Once saved, the vault credentials become available to other integrations.
Use vault secrets in configurations
Use the following syntax to securely reference secrets stored in the external vault:
Syntax
:
[EnvironmentName:::VaultIntegrationName:::VaultIntegrationInstanceName:::PasswordID]
EnvironmentName
: Name of the environment where the integration is configured (see
Settings
>
Integrations
).
VaultIntegrationName
: Name of the vault integration downloaded from the Content Hub.
VaultIntegrationInstanceName
: Name of the integration instance (the configured vault within the environment).
PasswordID
: The password identifier from your vault directory.
Example:
[Default
  Environment:::CyberArkPAM:::CyberArkPAM_1:::33_3]
Configure an integration with a vault password
The following example shows how to configure the email integration with a CyberArk password:
Go to
Response
>
Integrations Setup
; the
Integrations
screen appears.
Select the target environment where you want to configure the integration.
Click
add
Add
, then choose the
Email
integration.
Fill in the integration parameters. For
Password
, use the vault syntax:
[DefaultEnvironment:::CyberArkPAM:::CyberArkPAM_1:::33_3]
.
Select the
Remote Agent Run Remotely
checkbox, as CyberArk PAM
    is an on-premises vault.
Click
Save
. At runtime, the platform retrieves the password from the external vault.
Considerations
For on-premises vaults
: Make sure both the vault and integration run remotely under the same agent.
For cloud vaults with on-prem integrations
: Make sure the remote agent has access to the cloud vault.
Configure a connector with a vault password
To configure a connector with a vault password, follow these steps:
Go to
Settings
>
Ingestion
>
Connectors
.
Click
add
Add
to create a new connector. For this example, choose the
Generic
    IMAP Email
connector.
Enter the appropriate parameters.
In the
Password
field, add the following:
[Default Environment:::CyberArkPAM:::CyberArkPAM_1:::33_3]
.
Configure a job with a vault password
To configure a job with a vault password, follow these steps:
Go to
Response
>
Jobs Scheduler
.
Click
add
Add
and choose an integration (for example,
Google SecOps Sync Job
).
In the
API Root
field, enter the vault syntax.
Create a custom integration to use vault credentials
Use
Actions
,
Connectors
, or
Jobs
to pull vault credentials from the external vault by configuring the relevant
  integration parameter with the external vault syntax.
Use the following snippet on your code (
Param A
, which should contain the vault
  pattern):
integration_param = siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,param_name="Param A")
Connectors
can pull credentials from external vault by
  configuring  the relevant connector parameters with the external vault
  syntax.
Use the following snippet on your code (
Param B
, which should contain the vault
  pattern):
connector_param = siemplify.extract_connector_param("Param B", default_value=None, input_type=str)
Jobs
can pull credentials from external vault by configuring
  the relevant job param with the external vault syntax.
Use the following snippet on your code (
Param C
should contain the vault
  pattern):
job_param = siemplify.extract_job_param(param_name"Param C", print_value=True)
If you've configured the vault configuration as integration in
Shared
  instances
, you can pull the credentials from the integration
  configuration instead of the job configuration. Use the following snippet
  (
Param A
should contain the vault pattern):
integration_param =
  siemplify.extract_configuration_param(provider_name=INTEGRATION_NAME,param_name="Param
  A")
Additional information
Only commercial vault integrations from the Google SecOps
  Marketplace are supported.
Updating the vault configuration automatically applies new credentials
  across actions, jobs, and connectors.
There's a server validation for the vault placeholder. You can save a vault
  placeholder only if the referenced vault exists and you're authorized to access it.
Vault access using an agent is supported only in version
      1.4.1.52 or later.
Known limitations
When you create custom vault integrations with the vault credential feature, you
  must match the dependency versions exactly to the following table:
Dependencies
Python 2.7 / Python 3.7
requests
2.25.1
urllib3
1.26.2
six
1.15.0
requests_toolbelt
0.10.1
pyOpenSSL
19.1.0
pycparser
2.20
idna
2.10
cryptography
3.3.1
chardet
4.0.0
cffi
1.14.4
certifi
2020.12.5
importlib-metadata
2.1.3 (Python 2.7)
4.12.0 (Python 3.7)
Need more help?
Get answers from Community members and Google SecOps professionals.
