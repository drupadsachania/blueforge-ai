# Troubleshoot common issues

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting/  
**Scraped:** 2026-03-05T09:36:19.414593Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Troubleshoot common issues
Supported in:
Google secops
SOAR
This document provides a collection of tips and procedures to help you diagnose
and resolve common issues encountered during the deployment and operation of the
Google Security Operations Remote Agent.
Key mismatch issue
This issue occurs when the private keys in Google Security Operations
and the Remote Agent don't match. To solve this, make sure the key in the agent
resources matches the key in the Siemplify
agent_db
.
Remote connector failure
If a remote connector fails, follow these steps:
Verify that an integrations instance is successfully installed on the agent.
Check the agent logs at the error level to find any failures in the connection process.
Test the same connector configuration locally and see if there are errors.
Docker agent deployment failure
If the Docker deployment fails, follow these steps:
Remove the Docker container:
Run the following command to list the running containers:
docker ps
Run the following command to remove the failed containers:
docker rm  -f
container_id_or_name
Remove images:
Run the following command to list the images:
docker images
Run the following command to remove the image:
docker rmi
image_id_or_name
Remove volumes:
Run the following command to list the volumes:
docker volume ls
Run the following command to remove the volumes:
docker volume rm
volume_name
Redeploy the agent. For more information, see
Create an agent using Docker
.
Agent stuck in 'Waiting for agent' status
If the agent was successfully deployed but the status remains "waiting for agent",
follow these steps to troubleshoot the issue:
Check host connectivity
: Test the Agent host machine's internet
  connectivity (for example,
curl www.google.com
or
ping 8.8.8.8
).
  If this fails, the issue is with the host's internet connection.
Check container connectivity
: If the host test passes, enter the
  container shell using
docker exec -it
container_ID
bash
and recheck connectivity.
  If the container lacks connectivity, restart the Docker service on the host machine
  (service docker restart).
Run the following command:
docker exec -it
bash
Check the connectivity again as you did previously.
If there is no connectivity, run the following command to restart the Docker service from the host
    machine (not the container):
service docker restart
Run the following command to start container again:
docker start
Review container logs for errors
If the previous step did not help, and the agent status is still 'waiting for agent'
    after refreshing the
Remote agent
page in
  Google SecOps, log back in the container and pull the logs.
Find the logs in the
/var/log/SiemplifyAgent/
directory.
Look for any errors in the log files to identify the root cause.
Docker image fails to load (IP4 forwarding is disabled)
If you see an error in the CLI when you try to load a Google SecOps
Docker image (system) or agent, IP4 forwarding might be disabled. Follow these
steps to enable it and restart your agent:
Add the following line to the
/etc/sysctl.conf
file:
net.ipv4.ip_forward=1
Note that you will need to use a file editor (like nano for example use:
yum install nano -y
Run the following command to restart network service:
systemctl restart network
Run the following command to restart the Docker service:
sudo systemctl restart docker
Run the following command to check if the container is running:
docker ps
If the container is not running, run the following command to list all containers (including stopped ones):
docker ps -a
If the container is listed but stopped, run the following command to start it:
docker start
container_id_or_name
If the agent or system is still not running after restarting Docker and the container:
Run the following command to stop the container:
docker stop
container_id_or_name
Run the following command to delete the container:
docker rm
container_id_or_name
Run the following command to delete the image:
docker rmi
image_name
Load the image again.
Error after shutdown or reboot of Agent
Run the following command to force start of Installer agent:
systemctl start supervisord
Run the following command to force start of the Docker agent:
docker start
Need more help?
Get answers from Community members and Google SecOps professionals.
