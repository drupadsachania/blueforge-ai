# Migrate remote agents to Google Cloud

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/migrate-remote-agent-to-google/  
**Scraped:** 2026-03-05T09:16:13.421684Z

---

Stay organized with collections
Save and categorize content based on your preferences.
Migrate remote agents to Google Cloud
Migrate remote agents to Google Cloud
Supported in:
Google secops
SOAR
This document describes how to migrate remote agents to Google Cloud and use a Google Cloud 
service account for authentication and communication.
Before you begin
Make sure you have the following:
Necessary permissions to create service accounts in Google Cloud.
Required roles to create service account keys.
Minimum required Remote Agent version 2.6.2 and later.
Create a service account
A service account is a special type of Google Account that is used by an application to make authorized API calls. To create a service account, follow these steps:
In Google Cloud console, go to the
Service Accounts
page.
Go to Service Accounts
Click
Create Service Account
.
In the
Service account details
section, do the following:
Enter a name for the service account.
Enter a description for the service account.
Click
Create and Continue
.
In the
Permissions
section, do the following:
In the
Select a role
list, select the
Chronicle SOAR Remote Agent
role.
Click
Continue
.
In the
Grant users access to this service account
section, click
Done
.
Create a service account key
The service account key is required to authenticate the remote agent. To create this key, follow these steps:
In Google Cloud console, go to the
Service Accounts
page.
Go to Service Accounts
Click the name of the service account that you created.
Click the
Keys
tab.
Click
Add Key
>
Create new key
.
Select
JSON
as the key type and click
Create
.
A
JSON
file
containing
the
key
is
downloaded
to
your
computer
.
Click
Close
.
Securely store the key file
After downloading the service account key, you must move it to the host
machine where the remote agent will run.
Docker
Locate the downloaded JSON file on your computer.
Store the file in a secure location on the host machine where the agent process can access it.
Enter your agent's service account key full path on the host machine.
AGENT_SERVICE_ACCOUNT_PATH
Installer
Locate the downloaded JSON file on your computer.
Store the file in the following location:
/opt/SiemplifyAgent/agent-key.json
Make a note of the full path to this file, as it will be required when you configure the remote agent.
Prepare REP environment variable for agent
Retrieve your Regional Service Endpoint (REP) from the
Chronicle API
reference. Use this REP as your base domain.
Enter your REP in the following command. You will be using it in the migration procedure.
REP
Go to
SOAR Settings
>
Advanced
>
Remote Agents
and select the required remote agent.
.
Copy the following values from the
Docker Command
field and paste them 
  in the following commands. 
  You will be using them in the migration procedure:
ONE PLATFORM URL PROJECT
.
ONE_PLATFORM_URL_PROJECT
ONE PLATFORM URL LOCATION
.
ONE_PLATFORM_URL_LOCATION
ONE PLATFORM URL INSTANCE
.
ONE_PLATFORM_URL_INSTANCE
Migrate the remote agent to Google Cloud
Docker
If you're deploying a new agent, read
Deploy an agent with Docker.
If you're upgrading an agent, read
Upgrade an agent with Docker.
To migrate the remote agent, follow these steps:
List running Docker containers.
docker
ps
Enter your agent's container ID:
CONTAINER_ID
Use the following command to copy the service account key to a dedicated path in the container.
docker
cp
AGENT_SERVICE_ACCOUNT_PATH
CONTAINER_ID
:/opt/SiemplifyAgent/agent-key.json
Use the following command to change the owner of the service account key in the container:
docker
exec
-u
0
CONTAINER_ID
chown
siemplify_agent:siemplify_agent
/opt/SiemplifyAgent/agent-key.json
Paste the following environment variables from the earlier procedures and run this command:
docker
exec
CONTAINER_ID
sh
-c
'printf "export ONE_PLATFORM_URL_DOMAIN=
REP
\nexport ONE_PLATFORM_URL_PROJECT=
ONE_PLATFORM_URL_PROJECT
\nexport ONE_PLATFORM_URL_LOCATION=
ONE_PLATFORM_URL_LOCATION
\nexport ONE_PLATFORM_URL_INSTANCE=
ONE_PLATFORM_URL_INSTANCE
\nexport GOOGLE_APPLICATION_CREDENTIALS=/opt/SiemplifyAgent/agent-key.json" >> /home/siemplify_agent/.bash_profile'
Run the following command to apply the changes:
docker
restart
CONTAINER_ID
Installer
If you're deploying a new agent, read either
Deploy an agent with CentOS
or
Deploy an agent with RHEL.
If you're upgrading an agent, read either
Upgrade an agent with CentOS
or
Upgrade an agent with RHEL
To migrate the remote agent, follow these steps:
Use the following command to change the owner of the service account key in the container:
chown
siemplify_agent:siemplify_agent
/opt/SiemplifyAgent/agent-key.json
Paste the following environment variables from the earlier procedures and run this command:
cat
<< EOF >> /home/siemplify_agent/.bash_profile
export ONE_PLATFORM_URL_DOMAIN=
REP
export ONE_PLATFORM_URL_PROJECT=
ONE_PLATFORM_URL_PROJECT
export ONE_PLATFORM_URL_LOCATION=
ONE_PLATFORM_URL_LOCATION
export ONE_PLATFORM_URL_INSTANCE=
ONE_PLATFORM_URL_INSTANCE
export GOOGLE_APPLICATION_CREDENTIALS=/opt/SiemplifyAgent/agent-key.json
EOF
Run the following command to restart the agent service:
supervisorctl
restart
siemplify_agent
Need more help?
Get answers from Community members and Google SecOps professionals.
