# Create an agent with the installer for Debian

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-debian/  
**Scraped:** 2026-03-05T10:09:08.011523Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create an agent with the installer for Debian
Supported in:
Google secops
SOAR
This document provides the procedure to deploy a Remote Agent using the 
  Google Security Operations platform's installation wizard. The Remote Agent acts 
  as a crucial link, enabling your SOAR environment to securely communicate with 
  local security tools and devices.
Before you begin
Before you begin, we recommend that you run the commands individually to make 
 sure that each action runs successfully.
Follow this procedure to install the Remote Agent on Debian 12 using the 
native installer package:
Install Linux pages:
apt
update
-y
apt
install
wget
-y
apt
install
make
-y
apt
install
build-essential
-y
apt
install
libbz2-dev
-y
apt
install
sqlite3
-y
apt
install
libffi-dev
-y
apt
install
python3-dev
-y
apt
install
zlib1g-dev
-y
apt
install
libssl-dev
-y
apt
install
supervisor
-y
apt
install
at
-y
apt
install
sharutils
-y
apt
install
xz-utils
-y
apt
install
curl
-y
apt
install
gnupg2
-y
apt
install
coreutils
-y
apt
install
libc6-dev
-y
apt
install
pkg-config
-y
Start system services:
systemctl
start
atd
systemctl
enable
atd
Install Python 3.11.8:
cd
/usr/local/src
wget
https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz
tar
-xzf
Python-3.11.8.tgz
cd
Python-3.11.8
./configure
--prefix
=
/usr/local
make
-j
$(
nproc
)
altinstall
ln
-s
/usr/local/bin/python3.11
/usr/local/bin/python3
Configure
pip
:
cd
/usr/local/src
wget
-O
get-pip-3.11.py
https://bootstrap.pypa.io/get-pip.py
/usr/local/bin/python3.11
get-pip-3.11.py
Add the agent user:
groupadd
-r
siemplify_agent
&&
useradd
-r
-s
/bin/bash
-g
siemplify_agent
siemplify_agent
-m
cp
-n
/home/siemplify_agent/.profile
/home/siemplify_agent/.bash_profile
2
>/dev/null
mkdir
-p
/opt/SiemplifyAgent
chown
-R
siemplify_agent:siemplify_agent
/opt/*
/var/log/
Add the
supervisor.service
for the agent user:
echo
-e
"[Unit]\nDescription=Process Monitoring and Control Daemon\nAfter=rc-local.service\n\n[Service]\nType=forking\nExecStart=/usr/bin/supervisord -c /etc/supervisord.conf\nRuntimeDirectory=supervisor\nRuntimeDirectoryMode=755\n\n[Install]\nWantedBy=multi-user.target"
>
/etc/systemd/system/supervisord.service
Use the Microsoft SQL integration (optional)
If you're using the Microsoft SQL Integration, run the following commands 
(sequentially) to install the necessary Microsoft ODBC SQL drivers and tools.
Remove any existing Open Database Connectivity (ODBC) packages to prevent 
conflicts:
apt -y remove unixodbc unixodbc-dev
Add the Microsoft package repository and update the local package list:
curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg
curl https://packages.microsoft.com/config/debian/12/prod.list | tee /etc/apt/sources.list.d/mssql-release.list
apt update
Install the ODBC driver and the SQL command-line utilities:
apt install -y msodbcsql18 mssql-tools unixodbc-dev
Create symbolic links for
bcp
and
sqlcmd
to 
ensure the tools are accessible via the standard
PATH
:
ln -sfn /opt/mssql-tools/bin/bcp /usr/bin/bcp
ln -sfn /opt/mssql-tools/bin/sqlcmd /usr/bin/sqlcmd
Install a Remote Agent
This procedure details the manual installation of a Remote Agent after you've 
met all necessary prerequisites.
Initiate agent setup in the platform
In the platform, go to
Settings
>
Advanced
>
Remote Agents
.
Click
add
Add Agent
to 
    start the installation wizard.
Click the
Manual installation
link.
In the first step, enter the agent's name, choose the environment it will be 
    associated with, and click
Next
.
In the second step, choose one of the following distribution methods:
Download the agent package directly to your machine.
Enter an email address to send a download link (verify that the Email 
Integration is configured for the correct environment).
Click
Add environment contact
to automatically use the environment's 
Contact Person email.
Click
Next
. The package is either downloaded or a link is sent via 
email.
Prepare the installation machine
The download link provides the following zipped files:
env
: Siemplify environment variables
SiemplifyAgent_*.sh
: Installer script file
Use
WinSCP
or a similar tool to copy these files to the target 
installation machine.
Log in to the machine using SSH and enter your username and password.
Run the installation
Set execution permissions on the installer script:
sudo chmod +x SiemplifyAgent_*.sh
Install the agent using the saved command from the installation screen.
Wait for the script to finish; completion will be clearly marked.
Verify the connection
Return to the platform wizard and click
Next
. The system displays a 
    confirmation message indicating the agent is connected.
Need more help?
Get answers from Community members and Google SecOps professionals.
