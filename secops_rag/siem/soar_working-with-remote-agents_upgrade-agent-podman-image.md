# Perform a major upgrade of a Podman image

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-podman-image/  
**Scraped:** 2026-03-05T09:36:06.579617Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Perform a major upgrade of a Podman image
Supported in:
Google secops
SOAR
This document explains how to perform a major upgrade for an existing remote 
agent using the Podman image. The procedure assumes you're viewing the
Major Upgrade
dialog in the Google Security Operations SOAR platform.
On the
Major Upgrade
dialog, copy the provided Podman run command:
PODMAN_COMMAND
List the current running Podman containers:
podman
ps
Enter your agent's container ID:
CONTAINER_ID
Enter your agent's container name:
AGENT_NAME
.
Pull the latest Podman image to your machine using the following command.
    You can replace the
:latest
tag with a specific version, such as
1.4.8.3
.
podman
pull
us-docker.pkg.dev/siem-ar-public/images/agent:latest
Copy the original environment variables (
.bash_profile
) to a local temporary file.
podman
exec
CONTAINER_ID
cat
/home/siemplify_agent/.bash_profile
>
temp_bash_profile.txt
Stop the agent's Podman container.
podman
stop
CONTAINER_ID
Rename the container for backup.
podman
rename
AGENT_NAME
AGENT_NAME
_backup
Run the new agent image. If you changed the
latest
tag, make 
    sure the image tag matches the one pulled in.
PODMAN
List the running Podman containers.
podman
ps
Enter your agent's new container ID:
NEW_CONTAINER_ID
Copy the environment variables
.bash_profile
from the temporary file to the new container.
cat
temp_bash_profile.txt
|
podman
exec
-i
NEW_CONTAINER_ID
sh
-c
'cat > /home/siemplify_agent/.bash_profile'
Restart the agent service to apply the modified environment variables.
podman
exec
NEW_CONTAINER_ID
supervisorctl
restart
all
Need more help?
Get answers from Community members and Google SecOps professionals.
