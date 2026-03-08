# Perform a major upgrade of a Docker image

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-docker-image/  
**Scraped:** 2026-03-05T09:36:05.522191Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Perform a major upgrade of a Docker image
Supported in:
Google secops
SOAR
This document explains how to perform a major upgrade for an existing Remote
Agent using its Docker image. This procedure covers pulling the latest image,
creating a backup of the existing container, preserving essential environment
variables, and restarting the newly upgraded agent.
Before you begin
This procedure assumes you've already selected the Remote Agent upgrade option
and are viewing the
Major Upgrade
dialog.
In the
Major Upgrade
dialog, copy the Docker command and paste it 
here. This command will be automatically populated in
Step 7
:
DOCKER_COMMAND
Upgrade existing Remote Agent
To upgrade an existing Remote Agent using its Docker image, follow these steps:
Run the following command to list the current running Docker containers to identify your agent's container ID and name:
docker
ps
Enter your agent's container ID and name:
CONTAINER_ID
AGENT_NAME
Run the following command to pull the latest Docker image to your machine:
  You can change the
latest
tag to a specific version, such as
1.4.8.3
.
docker
pull
us-docker.pkg.dev/siem-ar-public/images/agent:latest
Run the following command to copy the modified environment variables to a local temporary file:
docker
exec
CONTAINER_ID
cat
/home/siemplify_agent/.bash_profile
>
temp_bash_profile.txt
Run the following command to stop the agent's Docker container:
docker
stop
CONTAINER_ID
Run the following command to rename the container to create a backup:
docker
rename
AGENT_NAME
AGENT_NAME
_backup
Run the new agent image. If you used a specific version for 
  the
latest
tag in
Step 3
, use the same tag 
  here:
Note: This command is populated from the
Before you begin
section.
DOCKER_COMMAND
Run the following command to list the running Docker containers to find the new container ID:
docker
ps
Enter your agent's new container ID:
NEW_CONTAINER_ID
Run the following command to copy the original contents of
.bash_profile
to the new container:
cat
temp_bash_profile.txt
|
docker
exec
-i
NEW_CONTAINER_ID
sh
-c
'cat > /home/siemplify_agent/.bash_profile'
Run the following command to restart the agent service to apply the modified environment variables:
docker
exec
NEW_CONTAINER_ID
supervisorctl
restart
all
Need more help?
Get answers from Community members and Google SecOps professionals.
