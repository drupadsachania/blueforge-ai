# Use the Google SecOps MCP server

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/use-google-secops-mcp/  
**Scraped:** 2026-03-05T09:46:14.347423Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the Google SecOps MCP server
Model Context Protocol
(MCP) standardizes the way large language models (LLMs) and AI applications or
agents connect to outside data sources. MCP servers let you use their tools,
resources, and prompts to take actions and get updated data from their backend
service.
Local MCP servers typically run on your local machine and use the standard input
and output streams (stdio) for communication between services on the same
device. Remote MCP servers run on the service's infrastructure and offer an HTTP
endpoint to AI applications for communication between the AI MCP client and the
MCP server. For more information on MCP architecture, see
MCP architecture
.
This document describes how to use the Google Security Operations remote MCP server
to connect to Google SecOps from AI applications such as Gemini CLI, agent mode
in Gemini Code Assist, Claude Code, or in AI applications you're developing.
Google and Google Cloud remote MCP servers have the following
features and benefits:
Simplified, centralized discovery.
Managed global or regional HTTP endpoints.
Fine-grained authorization.
Optional prompt and response security with
Model Armor protection.
Centralized audit logging.
For information about other MCP servers and information about security
and governance controls available for Google Cloud MCP servers,
see
Google Cloud MCP servers overview
.
Before you begin
Sign in to your Google Cloud account. If you're new to
        Google Cloud,
create an account
to evaluate how our products perform in
        real-world scenarios. New customers also get $300 in free credits to
        run, test, and deploy workloads.
In the Google Cloud console, on the project selector page,
        select or create a Google Cloud project.
Roles required to select or create a project
Select a project
: Selecting a project doesn't require a specific
      IAM role—you can select any project that you've been
      granted a role on.
Create a project
: To create a project, you need the Project Creator role
      (
roles/resourcemanager.projectCreator
), which contains the
resourcemanager.projects.create
permission.
Learn how to grant
      roles
.
Go to project selector
If you're using an existing project for this guide,
verify that you have
            the permissions required to complete this guide
. If you created a new
            project, then you already have the required permissions.
Verify that billing is enabled for your Google Cloud project
.
Enable the Chronicle API.
Roles required to enable APIs
To enable APIs, you need the Service Usage Admin IAM
          role (
roles/serviceusage.serviceUsageAdmin
), which
          contains the
serviceusage.services.enable
permission.
Learn how to grant
          roles
.
Enable the API
Install
the Google Cloud CLI.
If you're using an external identity provider (IdP), you must first
sign in to the gcloud CLI with your federated identity
.
To
initialize
the gcloud CLI, run the following command:
gcloud
init
In the Google Cloud console, on the project selector page,
        select or create a Google Cloud project.
Roles required to select or create a project
Select a project
: Selecting a project doesn't require a specific
      IAM role—you can select any project that you've been
      granted a role on.
Create a project
: To create a project, you need the Project Creator role
      (
roles/resourcemanager.projectCreator
), which contains the
resourcemanager.projects.create
permission.
Learn how to grant
      roles
.
Go to project selector
If you're using an existing project for this guide,
verify that you have
            the permissions required to complete this guide
. If you created a new
            project, then you already have the required permissions.
Verify that billing is enabled for your Google Cloud project
.
Enable the Chronicle API.
Roles required to enable APIs
To enable APIs, you need the Service Usage Admin IAM
          role (
roles/serviceusage.serviceUsageAdmin
), which
          contains the
serviceusage.services.enable
permission.
Learn how to grant
          roles
.
Enable the API
Install
the Google Cloud CLI.
If you're using an external identity provider (IdP), you must first
sign in to the gcloud CLI with your federated identity
.
To
initialize
the gcloud CLI, run the following command:
gcloud
init
Required roles
To set up and use the Google SecOps remote MCP server, you need the following IAM roles:
The
MCP tool user
(
roles/mcp.toolUser
) role is required for calling tools on any MCP server enabled by the parent project.
The
Chronicle API admin
(
roles/chronicle.admin
) role is required to ensure full access to the Chronicle API services, including global settings.
The
Chronicle SOAR Admin
(
roles/chronicle.soarAdmin
) role is required to grant administrator access to Google SecOps.
Enable the Google SecOps MCP server in a project
If you are using different projects for your client credentials, such as service
account keys, OAuth client ID or API keys, and for hosting your resources, then
you must enable the Google SecOps service and the
Google SecOps remote MCP server on both projects.
To enable the Google SecOps MCP server in your
Google Cloud project, run the following command:
gcloud
beta
services
mcp
enable
SERVICE
\
--project
=
PROJECT_ID
Replace the following:
PROJECT_ID
: the Google Cloud project ID.
SERVICE
: the global or regional service name
for Google SecOps. For example,
chronicle.googleapis.com
or
chronicle.us-central1.rep.googleapis.com
. For
available regions, see the
Google Security Operations MCP reference
.
The Google SecOps remote MCP server is enabled for use in
 your Google Cloud Project. If the
Google SecOps service isn't enabled for your
Google Cloud project, you are prompted to enable
the service before enabling the Google SecOps remote MCP
server.
As a security best practice, we recommend that you enable MCP servers only for
the services required for your AI application to function.
Disable the Google SecOps MCP server in a project
To disable the Google SecOps MCP server in your
Google Cloud project, run the following command:
gcloud
beta
services
mcp
disable
SERVICE
\
--project
=
PROJECT_ID
The Google SecOps MCP server is disabled for use in
your Google Cloud project.
Authentication and authorization
Google SecOps MCP servers use the
OAuth 2.0
protocol with
Identity and Access Management (IAM)
for authentication and authorization. All
Google Cloud identities
are supported for authentication to MCP servers.
We recommend creating a separate identity for agents using MCP tools so that
access to resources can be controlled and monitored. For more information on
authentication, see
Authenticate to MCP servers
.
Google SecOps MCP OAuth scopes
OAuth 2.0 uses scopes and credentials to determine if an authenticated
principal is authorized to take a specific action on a resource. For more
information about OAuth 2.0 scopes at Google, read
Using OAuth 2.0 to access Google APIs
.
Google SecOps has the following MCP tool OAuth scope:
Scope URI for gcloud CLI
Description
https://www.googleapis.com/auth/chronicle
Allows access to read and modify data.
Configure an MCP client to use the Google SecOps MCP server
AI applications and agents, such as Claude or Gemini
CLI, can instantiate an MCP client that connects to a single MCP server. An AI
application can have multiple clients that connect to different MCP servers. To
connect to a remote MCP server, the MCP client must know at a minimum the URL of
the remote MCP server.
In your AI application, look for a way to connect to a remote MCP server. You
are prompted to enter details about the server, such as its name and URL.
For the Google SecOps MCP server, enter the following as
required:
Server name
: Google SecOps MCP server
Server URL
or
Endpoint
: Select the
regional endpoint
and add /mcp at the end. For example,
chronicle.us.rep.googleapis.com/mcp
Transport
: HTTP
Authentication details
: Depending on how you want to authenticate, you can
enter your Google Cloud credentials, your OAuth Client ID
and secret, or an agent identity and credentials. For more information on
authentication, see
Authenticate to MCP servers
.
OAuth scope
: the
OAuth 2.0 scope
that
you want to use when connecting to the Google SecOps
MCP server. For Google SecOps, use
https://www.googleapis.com/auth/chronicle
.
For host specific guidance, see the following:
Claude.ai
Gemini CLI
For more general guidance, see the following resources:
Connect to remote MCP servers
.
Configure MCP in an AI application
.
Available tools
To view details of available MCP tools and their descriptions for the
Google SecOps MCP server, see the
Google SecOps MCP reference
.
List tools
Use the
MCP inspector
to list tools, or send a
tools/list
HTTP request directly to the Google Security Operations
remote MCP server. The
tools/list
method doesn't require authentication.
POST /mcp HTTP/1.1
Host: https://chronicle.europe-west2.rep.googleapis.com
Content-Type: application/json

{
  "jsonrpc": "2.0",
  "method": "tools/list",
}
Sample use cases
The following are sample use cases for the Google SecOps MCP server:
Tool
:
list_rule_errors
Sample prompt
:
List rule errors for the rule: ru_ddd45753-d749-4fee-b068-29072e750cfb
Response
:
Here are the rule errors for ru_ddd45753-d749-4fee-b068-29072e750cfb:

Error Message: query took too long to execute, see https://cloud.google.com/chronicle/docs/detection/yara-l-best-practices for tips for optimizing rules; these optimization tips are applicable to various types of queries

Time Range: 2025-02-16T10:00:00Z to 2025-02-16T11:00:00Z
Rule: projects/935934211738/locations/US/instances/eb3b937b-3ab6-47e5-8185-24837b826691/rules/ru_ddd45753-d749-4fee-b068-29072e750cfb@v_1740004374_748943000
Error Message: query took too long to execute, see https://cloud.google.com/chronicle/docs/detection/yara-l-best-practices for tips for optimizing rules; these optimization tips are applicable to various types of queries

Time Range: 2025-02-16T11:00:00Z to 2025-02-16T12:00:00Z
Rule: projects/935934211738/locations/US/instances/eb3b937b-3ab6-47e5-8185-24837b826691/rules/ru_ddd45753-d749-4fee-b068-29072e750cfb@v_1740004374_748943000
The errors indicate that the queries for this rule took too long to execute during the specified time ranges. You may want to review the YARA-L best practices for optimizing rules.
Tool
:
create_rules
Sample prompt
:
Create the following rule:
successful_user_logins_from_outside_us_test {
meta:
author = "Google SecOps Gemini"
description = "Detect successful user logins originating from outside the United States."
severity = "Medium"
events:
$e.metadata.event_type = "USER_LOGIN"
$e.security_result.action = "ALLOW"
$e.principal.ip_geo_artifact.location.country_or_region != "United States"
outcome:
$user = array($e.principal.user.userid)
$source_ip = array($e.principal.ip)
$country = array($e.principal.ip_geo_artifact.location.country_or_region)
$city = array($e.principal.ip_geo_artifact.location.city)
condition:
$e
}
Response
:
The rule successful_user_logins_from_outside_us_test has been successfully created with the following details:

Name: projects/935934211738/locations/US/instances/eb3b937b-3ab6-47e5-8185-24837b826691/rules/ru_cff9cae1-bb88-4456-b725-4c08f21803ed
Revision ID: v_1768208899_054095000
Display Name: successful_user_logins_from_outside_us_test
Author: Google SecOps Gemini
Description: Detect successful user logins originating from outside the United States.
Severity: Medium
Compilation State: SUCCEEDED
Create Time: 2026-01-12T09:08:19.054095Z
Optional security and safety configurations
MCP introduces new security risks and considerations due to the wide variety of
actions that can be taken with MCP tools. To minimize and manage these risks,
Google Cloud offers defaults and customizable policies to
control the use of MCP tools in your Google Cloud
organization or project.
For more information about MCP security and governance, see
AI security and safety
.
Model Armor
Model Armor is a
Google Cloud service designed to enhance the security and
safety of your AI applications. It works by proactively screening LLM prompts
and responses, protecting against various risks and supporting responsible AI
practices. Whether you are deploying AI in your cloud environment, or on
external cloud providers, Model Armor can help
you prevent malicious input, verify content safety, protect sensitive data,
maintain compliance, and enforce your AI safety and security policies
consistently across your diverse AI landscape.
Model Armor is only available in
specific regional locations. If Model Armor is
enabled for a project, and a call to that project comes from an unsupported
region, Model Armor makes a cross-regional call.
For more information, see
Model Armor locations
.
Enable Model Armor
You must enable Model Armor APIs before you can use Model Armor.
Console
Enable the Model Armor API.
Roles required to enable APIs
To enable APIs, you need the Service Usage Admin IAM
          role (
roles/serviceusage.serviceUsageAdmin
), which
          contains the
serviceusage.services.enable
permission.
Learn how to grant
          roles
.
Enable the API
Select the project where you want to activate Model Armor.
gcloud
Before you begin, follow these steps using the Google Cloud CLI with the
Model Armor API:
In the Google Cloud console, activate Cloud Shell.
Activate Cloud Shell
At the bottom of the Google Cloud console, a
Cloud Shell
session starts and displays a command-line prompt. Cloud Shell is a shell environment
      with the Google Cloud CLI
      already installed and with values already set for
      your current project. It can take a few seconds for the session to initialize.
Run the following command to set the API endpoint for the
Model Armor service.
gcloud
config
set
api_endpoint_overrides/modelarmor
"https://modelarmor.
LOCATION
.rep.googleapis.com/"
Replace
LOCATION
with the region where you want to use
Model Armor.
Configure protection for Google and Google Cloud remote MCP servers
To protect your MCP tool calls and responses, you create a
Model Armor floor setting and then enable
MCP content security for your project. A floor setting defines the minimum
security filters that apply across the project. This configuration applies a
consistent set of filters to all MCP tool calls and responses within
the project.
Set up a Model Armor floor setting with MCP sanitization
enabled. For more information, see
Configure Model Armor floor
settings
.
See the following example command:
gcloud
model-armor
floorsettings
update
\
--full-uri
=
'projects/
PROJECT_ID
/locations/global/floorSetting'
\
--enable-floor-setting-enforcement
=
TRUE
\
--add-integrated-services
=
GOOGLE_MCP_SERVER
\
--google-mcp-server-enforcement-type
=
INSPECT_AND_BLOCK
\
--enable-google-mcp-server-cloud-logging
\
--malicious-uri-filter-settings-enforcement
=
ENABLED
\
--add-rai-settings-filters
=
'[{"confidenceLevel": "MEDIUM_AND_ABOVE", "filterType": "DANGEROUS"}]'
Replace
PROJECT_ID
with your Google Cloud project
ID.
Note the following settings:
INSPECT_AND_BLOCK
: The enforcement type that
 inspects content for the Google MCP server and blocks prompts and
responses that match the filters.
ENABLED
: The setting that enables a filter or
enforcement.
MEDIUM_AND_ABOVE
: The confidence level for the
Responsible AI - Dangerous filter settings. You can modify this setting,
though lower values might result in more false positives. For more
information, see
Model Armor confidence levels
.
For your project, enable Model Armor protection for remote MCP servers.
gcloud
beta
services
mcp
content-security
add
modelarmor.googleapis.com
--project
=
PROJECT_ID
Replace
PROJECT_ID
with your Google Cloud
project ID. After you run this command, Model Armor sanitizes
all MCP tool calls and responses from the project, regardless of where the
calls and responses originate.
To confirm that Google MCP traffic is sent to Model Armor,
run the following command:
gcloud
beta
services
mcp
content-security
get
--project
=
PROJECT_ID
Replace
PROJECT_ID
with the Google Cloud project ID.
Disable scanning MCP traffic with Model Armor
If you want to use Model Armor in a project, and you want to stop
scanning Google MCP traffic with Model Armor, run the following
command:
gcloud
model-armor
floorsettings
update
\
--full-uri
=
'projects/
PROJECT_ID
/locations/global/floorSetting'
\
--remove-integrated-services
=
GOOGLE_MCP_SERVER
Replace
PROJECT_ID
with the Google Cloud project
ID.
Model Armor won't scan MCP traffic in the project.
Control MCP use with IAM deny policies
Identity and Access Management (IAM) deny policies
help you
secure Google Cloud remote MCP servers. Configure these policies to block
unwanted MCP tool access.
For example, you can deny or allow access based on:
The principal.
Tool properties like read-only.
The application's OAuth client ID.
For more information, see
Control MCP use with Identity and Access Management
.
What's next
Read the
Google Security Operations MCP reference documentation
.
Learn more about
Google Cloud MCP servers
.
