# Major upgrade using installer for CentOS

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/upgrade-agent-requirements-for-centos/  
**Scraped:** 2026-03-05T09:36:09.063122Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Major upgrade using installer for CentOS
Supported in:
Google secops
SOAR
This document explains how to perform a major upgrade for an
existing Remote Agent using the installer for CentOs 7.9 or later.
This procedure involves installing and configuring prerequisite packages before executing the upgrade script.
For more information on how to install an agent on a new deployment, see
Create an agent using installer on CentOS
.
Install and configure required packages to upgrade Remote Agents with version 2.0.0 and higher.
To install and configure required packages, follow these steps:
Run the following command to install Linux packages:
yum
install
perl-core
-y
Run the following commands separately to install OpenSSL 3.0.7:
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
Run the following commands separately to configure OpenSSL environment variables:
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
Need more help?
Get answers from Community members and Google SecOps professionals.
