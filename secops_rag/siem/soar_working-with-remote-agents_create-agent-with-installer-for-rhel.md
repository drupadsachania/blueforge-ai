# Create an agent using an installer for RHEL

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-for-rhel/  
**Scraped:** 2026-03-05T09:36:01.442315Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create an agent using an installer for RHEL
Supported in:
Google secops
SOAR
This guide provides the required packages to install an agent on Red Hat Enterprise
Linux (RHEL) 8.7. Before you install an agent, you must install and configure required packages listed in this document.
Google recommends running the commands one by one to make sure each action is run successfully.
Install and configure required packages
To install and configure required packages, follow these steps:
Run the following commands to configure the
PATH
variable:
echo
'export PATH=/usr/local/bin:$PATH'
>>
~/.bashrc
source
~/.bashrc
Run the following commands to install Linux packages:
dnf
update
-y
dnf
groupinstall
-y
'Development Tools'
dnf
install
bzip2-devel
-y
dnf
install
sqlite
-y
dnf
install
libffi-devel
-y
dnf
install
gcc
-y
dnf
install
gcc-c++
-y
dnf
install
python2-devel
-y
dnf
install
python3-devel
-y
dnf
install
zlib-devel
-y
dnf
install
openssl-devel
-y
dnf
install
https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
dnf
install
epel-release
-y
subscription-manager
repos
--enable
codeready-builder-for-rhel-8-x86_64-rpms
dnf
install
perl-core
-y
dnf
update
-y
dnf
install
supervisor
-y
dnf
install
at
-y
dnf
install
sharutils
-y
Run the following commands to start the
atd
service:
systemctl
start
atd
systemctl
enable
atd
Run the following commands to install OpenSSL 3.0.7:
cd
/usr/local/src
wget
https://www.openssl.org/source/openssl-3.0.7.tar.gz
tar
-xf
openssl-3.0.7.tar.gz
cd
openssl-3.0.7
./config
--prefix
=
/usr/local/ssl
--openssldir
=
/usr/local/ssl
shared
zlib
make
-j
$((
`
nproc
`
+
1
))
make
install
cd
/etc/ld.so.conf.d/
echo
/usr/local/ssl/lib64
>
openssl-3.0.7.conf
ldconfig
-v
echo
PATH
=
"/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ssl/bin"
>
/etc/environment
source
/etc/environment
ln
-sf
/usr/local/ssl/bin/openssl
/usr/bin/openssl
export
LDFLAGS
=
"
$LDFLAGS
-L/usr/local/ssl/lib64"
export
LD_LIBRARY_PATH
=
/usr/local/ssl/lib64
Run the following commands to install Python 3.11.8:
cd
/usr/src
wget
http://www.python.org/ftp/python/3.11.8/Python-3.11.8.tgz
tar
xzf
Python-3.11.8.tgz
cd
Python-3.11.8
make
clean
./configure
--prefix
=
/usr/local
--enable-unicode
=
ucs4
--with-openssl
=
/usr/local/ssl
make
make
altinstall
Run the following command to create a Python symlink:
ln
-s
/usr/local/bin/python3.11
/usr/local/bin/python3
Run the following commands to configure
pip
for all Python versions:
/usr/local/bin/python3
get-pip.py
/usr/local/bin/pip3
install
--upgrade
pip
wget
-O
get-pip-3.11.py
https://bootstrap.pypa.io/get-pip.py
/usr/local/bin/python3.11
get-pip-3.11.py
/usr/local/bin/python3.11
-m
pip
install
--upgrade
pip
Optional: If you're using Microsoft SQL Integration, run the following commands to install
MsOdbc SQL driver utils
:
dnf
-y
remove
unixODBC
unixODBC-devel
curl
https://packages.microsoft.com/config/rhel/8/prod.repo
>
/etc/yum.repos.d/mssql-release.repo
dnf
install
-y
msodbcsql17
mssql-tools
unixODBC-devel
ln
-sfn
/opt/mssql-tools/bin/bcp
/usr/bin/bcp
ln
-sfn
/opt/mssql-tools/bin/sqlcmd
/usr/bin/sqlcmd
Install a remote agent
Before you install a remote agent, make sure you've completed all the
required configurations
.
To install a remote agent, follow these steps:
In the platform, go to
Settings
>
Advanced
>
Remote Agents
.
On the
Remote Agents
page, click
add
Add
>
click
Manual installation
.
Enter a name for the agent and select an environment.
Click
Next
.
Select an option to download the agent files:
Download the agent on your machine.
Enter an email address to send the download to the configured email address. Make sure you have configured the email integration to the correct environment.
Optional: Click
Add environment contact
to add a contact person for the environment.
The following files are downloaded:
.env
: Siemplify environment variables
SiemplifyAgent_Centos.sh
: Installer script file
Click
Next
.
Store the installer command in a secure location.
Use
WinSCP
(or a similar tool) to copy the files to the machine where you want to install the agent.
Sign in to the machine using SSH with your username and password.
Run the following command to set the permissions for the installer script:
sudo chmod +x SiemplifyAgent_Centos.sh
Run the installer command you saved to install the agent.
Return to the installation process on your platform and then click
Next
. A confirmation message for agent connection appears.
Need more help?
Get answers from Community members and Google SecOps professionals.
