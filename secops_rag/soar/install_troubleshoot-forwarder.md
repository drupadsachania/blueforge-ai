# Troubleshoot common Linux forwarder issues

**Source:** https://docs.cloud.google.com/chronicle/docs/install/troubleshoot-forwarder/  
**Scraped:** 2026-03-05T09:47:15.585431Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Troubleshoot common Linux forwarder issues
Supported in:
Google secops
SIEM
This document helps you recognize and troubleshoot common issues that you may face
while using the Google Security Operations Linux forwarder.
Forwarder does not start
Forwarder fails to start and is in a continuous restart loop with the following
error in the logs:
F0510 06:17:39.013603 202 main_linux.go:153] open /opt/chronicle/external/*.conf: no such file or directory
Possible cause 1: Incorrect mapping in the configuration file
To resolve this issue, ensure that you are passing the correct path to the
configuration file and mapping it to an external folder.
Possible cause 2: SELinux is enabled
Check the configuration file by getting into the container without starting
the forwarder and run the following command:
docker run --name cfps --log-opt max-size=100m --log-opt   max-file=10 --net=host -v ~/configuration:/opt/chronicle/external --entrypoint=/bin/bash \
-it gcr.io/chronicle-container/cf_production_
This command will put you in a shell from within the container.
Run the following command:
ls -lrt /opt.chronicle/external/
If you get a permission denied error, it indicates that the forwarder is unable
to open the configuration file and therefore, not able to start.
To resolve this issue, do the following:
Check the SELinux status by running the following command:
sestatus
If SELinux status is enabled in the output, run the following command
  to disable it:
setenforce 0
Logs not reaching the Google SecOps tenant
Possible cause 1: DNS resolution
Check if the host is unable to resolve addresses or to reach Google SecOps by running
  the following command:
nslookup malachiteingestion-pa.googleapis.com
If the command fails, contact your networking team for resolution.
Possible cause 2: Firewall
Check if the local firewall is blocking communication between Google SecOps
  and the forwarder by running the following command:
firewall-cmd --state
If the firewall is enabled, disable it by running the following command:
systemctl stop firewalld
Possible cause 3: Buffer size
Check if it's a buffer size issue by looking for the following error in the logs:
Memory ceiling (1073741824) reached, freeing a batch from the backlog
To resolve this issue, do the following:
Enable compression in the forwarder configuration file.
Increase the buffer size
by updating the
max_memory_buffer_bytes
and
max_file_buffer_bytes
parameters in the configuration file.
These parameters indicate the buffer of backlog batches that are stored in
the memory or disk.
Forwarder and host not receiving logs
If the host and the forwarder do not receive logs, check the port status by
running the following command for each port:
netstat -a | grep
PORT
Replace
PORT
with the port ID that you want to check.
If the command does not give any output, it indicates that the host is not
listening on that port and you should consult your network administrator.
If the output from the command indicates that the host is listening on a port
and the forwarder is still not receiving logs, do the following:
Stop Docker by running the following command:
​​docker stop cfps
Run one of the following commands based on your network setup.
For TCP:
nc -l
PORT
For UDP:
nc -l -u
PORT
Replace
PORT
with the port ID that you want to
troubleshoot.
Restart your external service and check if the issue is resolved. If the issue
persists, [contact
Google SecOps support
.
Forwarder not receiving logs but host is receiving logs
If the host is receiving logs but the forwarder is not, it indicates that the
forwarder is not listening on the port specified in the configuration file.
To resolve this issue, do the following:
Open two terminal windows on your system, one to configure the forwarder and
one to send a test message to the host.
On the first terminal (forwarder), start Docker without starting the
forwarder by running the following command:
docker run \
--name cfps \
--log-opt max-size=100m \
--log-opt max-file=10 \
--net=host \
-v ~/config:/opt/chronicle/external \
--entrypoint=/bin/bash \
-it gcr.io/chronicle-container/cf_production_stable
Specify the port that the forwarder should listen on:
nc -l
PORT
Replace
PORT
with the port ID that you want to
troubleshoot.
On the second terminal (host), send the test message on the port by running
the following command:
echo "test message" | nc localhost
PORT
Replace
PORT
with the port ID that you want to
troubleshoot.
Rerun the
docker
command. Specify the
-p
flag with the ports on which the
forwarder should listen by running the following command:
docker run \
--detach \
–name cfps \
--restart=always \
--log-opt max-size=100m \
--log-opt max-file=10 --net=host \
—v /root/config:/opt/chronicle/external \
-p 11500:11800 \
gcr.io/chronicle-container/cf_production_stable
Common errors in the forwarder log file
You can view the forwarder logs by running the following command:
sudo docker logs cfps
Request contains an invalid argument
The forwarder log file shows the following error message:
I0912 18:04:15.187321 333 uploader.go:181] Sent batch error: rpc error: code = InvalidArgument desc = Request contains an invalid argument.
  E0912 18:04:15.410572 333 batcher.go:345] [2_syslog_CISCO_FIREWALL-tid-0] Error exporting batch: rpc error: code = InvalidArgument desc = Request contains an invalid argument.
  I0912 18:04:15.964923 333 uploader.go:181] Sent batch error: rpc error: code = InvalidArgument desc = Request contains an invalid argument.
Resolution:
This error can occur when an invalid log type is added. Ensure that only
valid log types are added. In the sample error message,
CISCO\_FIREWALL
is not
a valid log type. For a list of valid log types, visit
Supported log types and default parsers
.
Unable to find the server
The forwarder log file shows the following error message:
{"log":"Failure: Unable to find the server at accounts.google.com.\n","stream":"stderr","time":"2019-06-12T18:26:53.858804303Z"}`

{"log":"+ [[ 1 -ne 0 ]]\n","stream":"stderr","time":"2019-06-12T18:26:53.919837669Z"}

{"log":"+ err 'ERROR: Problem accessing the Chronicle bundle.'\n","stream":"stderr","time":"2019-06-12T18:26:53.919877852Z"}
Resolution:
Contact your networking team to ensure that the network is working.
Invalid JWT signature
The forwarder log file shows the following error message:
E0330 17:05:28.728021 162 stats_manager.go:85] send(): rpc error: code = Unauthenticated desc = transport: OAuth 2.0: cannot fetch token: 400 Bad Request Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
    E0404 17:05:28.729012 474 memory.go:483] [1_syslog_FORTINET_FIREWAL-tid-0] Error exporting batch: rpc error: code = Unauthenticated desc = transport: OAuth 2.0: cannot fetch token: 400 Bad Request Response: {"error":"invalid_grant","error_description":"Invalid JWT Signature."}
Resolution:
This error can occur when a forwarder configuration file has wrong secret key
details.
Contact Google SecOps support
to help resolve this issue.
Token must be a short-lived token
The forwarder log file shows the following error message:
token: 400 Bad Request Response:
      {"error":"invalid_grant","error_description":"Invalid JWT: Token must be a
      short-lived token (60 minutes) and in a reasonable timeframe. Check your iat and exp values in the JWT claim."} I0412 05:14:16.539060 480
      malachite.go:212] Sent batch error: rpc error: code = Unauthenticated desc =
      transport: OAuth 2.0: cannot fetch token: 400 Bad Request Response:
      {"error":"invalid_grant","error_description":"Invalid JWT: Token must be a
      short-lived token (60 minutes)
Resolution:
This error can occur when the host and the server system clocks are not in sync.
Adjust the time on the host or try using NTP to synchronize the clocks.
No such file or directory
The forwarder log file shows the following error message:
++ cat '/opt/chronicle/external/*.conf'
    cat: '/opt/chronicle/external/*.conf': No such file or directory
Resolution:
This error can occur when the forwarder is started with the wrong drive mapping. Use
the full directory path in the configuration file (you can obtain the path by running
the
pwd
command).
Failed to retrieve customer ID from configuration file
The forwarder log file shows the following error message:
+ err 'ERROR: Failed to retrieve customer ID from configuration file.'
    ++ date +%Y-%m-%dT%H:%M:%S%z
    + echo '[2023-06-28T09:53:21+0000]: ERROR: Failed to retrieve customer ID from configuration file.'
    [2023-06-28T09:53:21+0000]: ERROR: Failed to retrieve customer ID from configuration file.
    + err '==> Please contact the Chronicle support team.'
Resolution:
This error is caused by incorrect mapping or if the configuration file is not
present in the directory. Use the full directory path in the configuration file
(you can obtain the path by running the
pwd
command). Ensure that the correct
docker run
command is executed and that the configuration file exists at the
following location:
gcr.io/chronicle-container/cf_production_stable
The following code sample shows the
docker run
command:
​​docker run \
    --detach \
    --name cfps \
    --restart=always \
    --log-opt max-size=100m \
    --log-opt max-file=10 \
    --net=host \
    -v /opt/chronicle/config:/opt/chronicle/external \
    gcr.io/chronicle-container/cf_production_stable
Useful Docker commands
You can gather additional information about the Docker installation using the following command:
docker info
The Docker service could be disabled by default. To check if it is disabled,
execute the following command:
systemctl is-enabled docker
To enable the Docker service and start it immediately, execute one of the following
commands:
sudo systemctl enable --now docker
sudo systemctl enable /usr/lib/systemd/system/docker.service
Output:
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /lib/systemd/system/docker.service
When you start a forwarder, execute the following command to set the forwarder
to auto-restart:
sudo docker run --restart=always `
IMAGE_NAME
`
IMAGE_NAME
is the forwarder image name.
To check the status and details of the Docker service, execute the following command:
sudo systemctl status docker
Output:
●
docker
.
service
-
Docker
Application
Container
Engine
Loaded
:
loaded
(
/
lib
/
systemd
/
system
/
docker
.
service
;
enabled
;
vendor
preset
:
enabled
)
Active
:
active
(
running
)
since
Sat
2020
-
07
-
18
11
:
14
:
05
UTC
;
15
s
ago
TriggeredBy
:
●
docker
.
socket
Docs
:
https
:
//
docs
.
docker
.
com
Main
PID
:
263
(
dockerd
)
Tasks
:
20
Memory
:
100.4
M
CGroup
:
/
system
.
slice
/
docker
.
service
└─
263
/
usr
/
bin
/
dockerd
-
H
fd
:
//
--
containerd
=/
run
/
containerd
/
containerd
.
sock
Jul
18
11
:
14
:
05
swarm
-
kraken
dockerd
[
263
]:
time
=
"2020-07-18T11:14:05.713787002Z"
level
=
info
msg
=
"API listen on /run/docker.sock"
Jul
18
11
:
14
:
05
swarm
-
kraken
systemd
[
1
]:
Started
Docker
Application
Container
Engine
If you have any issues with Docker, the Google SecOps support team can request the
output from this command to help and debug with the issue.
Need more help?
Get answers from Community members and Google SecOps professionals.
