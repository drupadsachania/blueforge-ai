# Create an agent using an installer for CentOS

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/create-agent-with-installer-on-centos/  
**Scraped:** 2026-03-05T10:09:11.103017Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create an agent using an installer for CentOS
Supported in:
Google secops
SOAR
This document provides the required packages for installing an agent on CentOS 7.9.
Before you install the agent, you must install and configure required packages listed in this document.
Google recommends running the commands one by one to make sure each action is run successfully.
Install and configure required packages
To install and configure required packages, follow these steps:
Run the following commands to install Linux packages:
yum
update
-y
yum
groupinstall
-y
'development tools'
yum
install
bzip2-devel
-y
yum
install
sqlite
-y
yum
install
libffi-devel
-y
yum
install
gcc
-y
yum
install
gcc-c++
-y
yum
install
python-devel
-y
yum
install
python3-devel
-y
yum
install
zlib-devel
-y
yum
install
openssl-devel
-y
yum
install
epel-release
-y
yum
install
perl-core
-y
yum
update
-y
yum
install
supervisor
-y
yum
install
at
-y
yum
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
Install OpenSSL 3.0.7.
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
:
wget
-O
get-pip.py
https://bootstrap.pypa.io/pip/2.7/get-pip.py
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
yum
-y
remove
unixODBC
unixODBC-devel
rpm
-Uvh
--replacepkgs
https://packages.microsoft.com/config/rhel/7/packages-microsoft-prod.rpm
yum
install
-y
msodbcsql-13.0.1.0-1
mssql-tools-14.0.2.0-1
unixODBC-utf16-devel
ln
-sfn
/opt/mssql-tools/bin/bcp-13.0.1.0
/usr/bin/bcp
ln
-sfn
/opt/mssql-tools/bin/sqlcmd-13.0.1.0
/usr/bin/sqlcmd
Install a remote agent
Before you install a remote agent, make sure you have completed all the
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
Enter an agent name and select an environment.
Click
Next
.
Select an option to download the agent.
Download the agent to your machine.
Enter an email address to send download to the configured email address. Make sure you have configured the email integration to the correct environment.
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
Run the following command to set the permissions:
sudo chmod +x SiemplifyAgent_Centos.sh
Run the installer command you saved earlier to install the agent.
Return to the installation process on your platform and then click
Next
. A confirmation message for agent connection appears.
Need more help?
Get answers from Community members and Google SecOps professionals.
