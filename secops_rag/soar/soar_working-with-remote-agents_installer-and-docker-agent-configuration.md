# Configure the Installer and Docker

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/installer-and-docker-agent-configuration/  
**Scraped:** 2026-03-05T10:09:22.889583Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Configure the Installer and Docker
Supported in:
Google secops
SOAR
This document describes how to configure an agent, including how to view and
change configuration options. It also explains how to configure proxy settings
for both agent-publisher communication and integrations.
Manage the Remote Agent configuration
To make changes to an agent, follow these steps:
Sign in to the agent machine using SSH.
Go to the
/home/siemplify_agent/agent_source
directory. If you're
using Docker, make sure you're inside the container.
Run the following command to view all primary configuration options for the
cli
utility:
python
agent_cli.py
-h
Run the
printenv
command to check the current values for the actively used configurations.
Use the
set_
option
format to change the value of a single, primary configuration option:
python
agent_cli
.
py
set_verify_ssl_slave
false
Use the
update_environment
command to modify a broader set of configurations stored as environment variables:
View the list of environment variables available for modification:
python
agent_cli.py
update_environment
-h
Change the value of one of these configurations:
python
agent_cli.py
update_environment
VARIABLE_NAME
VALUE
For example:
python
agent_cli.py
update_environment_status
RETRANSMISSION_LOOP_INTERVAL_SECONDS
30
Remote Agent environment variables
The following table provides detailed information about the environment variables configurable using the
python agent_cli.py update_environment
command:
Option
Description
Values
TASK_TIMEOUT
Sets the timeout (in seconds) for tasks that the agent has pulled but hasn't executed.
Time (in seconds)
SERVER_API_ROOT
The primary Publisher API server address. Defines where the agent pulls tasks from and publishes results to..
API Address
SERVER_API_TOKEN
The authentication token used for all requests sent to the Publisher.
Server API token (string)
VERIFY_SSL
Determines if the agent must connect to a Publisher only if it presents a signed SSL certificate.
Boolean (
True
or
False
)
RETRANSMISSION_LOOP_INTERVAL_SECONDS
Sets the time delay (in seconds) between checks to confirm the Publisher
    received the
CASE_ACK
for a connector package.
Time (in seconds)
RETRANSMISSION_SAVE_PERIOD_DAYS
Maximum time (in days) a connector package can remain in the retransmission
    folder before deletion, assuming the
CASE_ACK
hasn't been received.
Time (in days)
RETRANSMISSION_FOLDER_MAX_SIZE_MB
The maximum size (in MB) the retransmission folder can reach before the
    agent starts deleting the oldest connector packages to maintain the boundary.
Size (MB)
VERIFY_SSL_SLAVE
If set to
True
, the agent requires the secondary Publisher
    to have a signed SSL certificate before establishing communication.
Boolean (
True
or
False
)
PROXY_ADDRESS
The IP address of the proxy server the agent uses to communicate with the primary Publisher.
Proxy IP address
AGENT_KEY
An encrypted key that the agent uses to decrypt packages pulled from the
    Publisher and encrypt results before publishing them back.
Encrypted agent key
SERVER_API_ROOT_SLAVE
The secondary Publisher API server address where the agent pulls tasks from and publishes results to.
API address
PROXY_ADDRESS_SLAVE
The IP address of the proxy server the agent uses to communicate with the secondary Publisher.
Proxy IP address
DEPLOYMENT_TYPE
Indicates the installation method used for the agent.
Docker
or
Installer
(string)
Configure an Agent-Publisher proxy
Configure a proxy server to handle all communication between the Remote Agent
service and the Publisher. This configuration only applies to the Agent-Publisher
communication channel.
To configure an Agent-Publisher proxy, follow these steps:
Run the
update_environment
command on the agent machine to configure a proxy on an existing deployed agent:
python3 /opt/SiemplifyAgent/agent_cli.py update_environment PROXY_ADDRESS https://{proxy_host}
Download the package, and then edit the
.env
file to include the proxy address:
PROXY_ADDRESS=https://{proxy_host}
Add the proxy address as an environment variable (`-e`) to the Docker command before running the deployment:
-e PROXY_ADDRESS=https://{proxy_host}
.
Configure an integration proxy
This procedure defines the proxy settings for integrations running on the Remote Agent, making sure that integration traffic is routed through the specified proxy server.
To configure an integration proxy, add the required variables to the agent's environment before running the Docker command:
Variable
Description
Example
HTTP_PROXY
Proxy address for HTTP requests
https://{HTTP_PROXY}
HTTPS_PROXY
Proxy address for HTTPS requests
https://{HTTPS_PROXY}
NO_PROXY
Comma-separated list of hostnames/IPs to bypass proxy routing
https://{NO_PROXY}
Need more help?
Get answers from Community members and Google SecOps professionals.
