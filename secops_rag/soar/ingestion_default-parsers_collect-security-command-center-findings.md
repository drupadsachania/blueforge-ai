# Collect Security Command Center findings

**Source:** https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-security-command-center-findings/  
**Scraped:** 2026-03-05T09:48:51.243527Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Collect Security Command Center findings
Supported in:
Google secops
SIEM
This document describes how you can collect Security Command Center logs by configuring Security Command Center
and ingesting findings to Google Security Operations. This document also lists the supported events.
For more information, see
Data ingestion to Google Security Operations
and
Exporting Security Command Center findings to Google Security Operations
.
A typical deployment consists of Security Command Center and the Google Security Operations feed configured to send logs to Google Security Operations. Each customer deployment might differ and might be more complex.
The deployment contains the following components:
Google Cloud
: The system to be monitored in which Security Command Center is installed.
Security Command Center Event Threat Detection Findings
: Collects information from the data source and generates findings.
Google Security Operations
: Retains and analyzes the logs from the Security Command Center.
An ingestion label identifies the parser which normalizes raw log data
to structured UDM format. The information in this document applies to the Security Command Center parser
with the following ingestion labels:
GCP_SECURITYCENTER_ERROR
GCP_SECURITYCENTER_MISCONFIGURATION
GCP_SECURITYCENTER_OBSERVATION
GCP_SECURITYCENTER_THREAT
GCP_SECURITYCENTER_UNSPECIFIED
GCP_SECURITYCENTER_VULNERABILITY
GCP_SECURITYCENTER_POSTURE_VIOLATION
GCP_SECURITYCENTER_TOXIC_COMBINATION
GCP_SECURITYCENTER_CHOKEPOINT
GCP_SECURITYCENTER_SENSITIVE_DATA_RISK
Configure Security Command Center and Google Cloud to send findings to Google Security Operations
Activate Security Command Center
.
Ensure that all systems in the deployment are configured
in the UTC time zone.
Enable the ingestion of
Security Command Center findings
.
Supported Event Threat Detection findings
This section lists the supported Event Threat Detection findings. For information about the Security Command Center Event Threat Detection rules and findings, see
Event Threat Detection rules
.
Finding name
Description
Active Scan: Log4j Vulnerable to RCE
Detects active Log4j vulnerabilities by identifying DNS queries for unobfuscated domains that were initiated by supported Log4j vulnerability scanners.
Brute Force: SSH
Detection of successful brute force of SSH on a host.
Credential Access: External Member Added To Privileged Group
Detects when an external member is added to a privileged Google Group (a group granted sensitive roles or permissions). A finding is generated only if the group doesn't already contain other external members from the same organization as the newly added member. To learn more, see
Unsafe Google Group changes
.
Credential Access: Privileged Group Opened To Public
Detects when a privileged Google Group (a group granted sensitive roles or permissions) is changed to be accessible to the general public. To learn more, see
Unsafe Google Group changes
.
Credential Access: Sensitive Role Granted To Hybrid Group
Detects when sensitive roles are granted to a Google Group with external members. To learn more, see
Unsafe Google Group changes
.
Defense Evasion: Modify VPC Service Control
Detects a change to an existing VPC Service Control perimeter that would lead to a reduction in the protection offered by that perimeter.
Discovery: Can get sensitive Kubernetes object checkPreview
A malicious actor attempted to determine what sensitive objects in Google Kubernetes Engine (GKE) they can query for, by using the kubectl auth can-i get command.
Discovery: Service Account Self-Investigation
Detection of an Identity and Access Management (IAM) service account credential that is used to investigate the roles and permissions associated with that same service account.
Evasion: Access from Anonymizing Proxy
Detection of Google Cloud service modifications that originated from anonymous proxy IP addresses, like Tor IP addresses.
Exfiltration: BigQuery Data Exfiltration
Detects the following scenarios:
Resources owned by the protected organization that are saved outside of the organization, including copy or transfer operations.
Attempts to access BigQuery resources that are protected by VPC Service Control.
Exfiltration: BigQuery Data Extraction
Detects the following scenarios:
A BigQuery resource owned by the protected organization is saved, through extraction operations, to a Cloud Storage bucket outside the organization.
A BigQuery resource owned by the protected organization is saved, through extraction operations, to a publicly accessible Cloud Storage bucket owned by that organization.
Exfiltration: BigQuery Data to Google Drive
Detects the following scenarios:
A BigQuery resource owned by the protected organization is saved, through extraction operations, to a Google Drive folder.
Exfiltration: Cloud SQL Data Exfiltration
Detects the following scenarios:
Live instance data exported to a Cloud Storage bucket outside of the organization.
Live instance data exported to a Cloud Storage bucket that is owned by the organization and is publicly accessible.
Exfiltration: Cloud SQL Restore Backup to External Organization
Detects when a Cloud SQL instance's backup is restored to an instance outside of the organization.
Exfiltration: Cloud SQL SQL Over-Privileged Grant
Detects when a Cloud SQL Postgres user or role has been granted all privileges to a database or to all tables, procedures, or functions in a schema.
Impair Defenses: Strong Authentication Disabled
2-step verification was disabled for the organization.
Impair Defenses: Two Step Verification Disabled
A user disabled 2-step verification.
Initial Access: Account Disabled Hijacked
A user's account was suspended due to suspicious activity.
Initial Access: Disabled Password Leak
A user's account is disabled because a password leak was detected.
Initial Access: Government Based Attack
Government-backed attackers might have tried to compromise a user account or computer.
Initial Access: Log4j Compromise Attempt
Detects Java Naming and Directory Interface (JNDI) lookups within headers or URL parameters. These lookups may indicate attempts at Log4Shell exploitation. These findings have low severity, because they only indicate a detection or exploit attempt, not a vulnerability or a compromise.
Initial Access: Suspicious Login Blocked
A suspicious login to a user's account was detected and blocked.
Log4j Malware: Bad Domain
Detection of Log4j exploit traffic based on a connection to, or a lookup of, a known domain used in Log4j attacks.
Log4j Malware: Bad IP
Detection of Log4j exploit traffic based on a connection to a known IP address used in Log4j attacks.
Malware: Bad Domain
Detection of malware based on a connection to, or a lookup of, a known bad domain.
Malware: Bad IP
Detection of malware based on a connection to a known bad IP address.
Malware: Cryptomining Bad Domain
Detection of cryptomining based on a connection to, or a lookup of, a known cryptocurrency mining domain.
Malware: Cryptomining Bad IP
Detection of cryptocurrency mining based on a connection to a known mining IP address.
Outgoing DoS
Detection of outgoing denial of service traffic.
Persistence: Compute Engine Admin Added SSH Key
Detection of a modification to the Compute Engine instance metadata SSH key value on an established instance (older than 1 week).
Persistence: Compute Engine Admin Added Startup Script
Detection of a modification to the Compute Engine instance metadata startup script value on an established instance (older than 1 week).
Persistence: IAM Anomalous Grant
Detection of privileges granted to IAM users and service accounts that are not members of the organization. This detector uses an organization's existing IAM policies as context. If a sensitive IAM grant to an external member occurs, and there are less than three existing IAM policies that are similar to it, this detector generates a finding.
Persistence: New API MethodPreview
Detection of anomalous usage of Google Cloud services by IAM service accounts.
Persistence: New Geography
Detection of IAM user and service accounts accessing Google Cloud from anomalous locations, based on the geolocation of the requesting IP addresses.
Persistence: New User Agent
Detection of IAM service accounts accessing Google Cloud from anomalous or suspicious user agents.
Persistence: SSO Enablement Toggle
The Enable SSO (single sign-on) setting on the admin account was disabled.
Persistence: SSO Settings Changed
The SSO settings for the admin account were changed.
Privilege Escalation: Changes to sensitive Kubernetes RBAC objectsPreview
To escalate privilege, a malicious actor attempted to modify
cluster-admin
ClusterRole and ClusterRoleBinding objects by using a PUT or PATCH request.
Privilege Escalation: Create Kubernetes CSR for master certPreview
A potentially malicious actor created a Kubernetes master certificate signing request (CSR), which gives them cluster-admin  access.
Privilege Escalation: Creation of sensitive Kubernetes bindingsPreview
A malicious actor attempted to create new cluster-admin RoleBinding or ClusterRoleBinding objects to escalate their privilege.
Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentialsPreview
A malicious actor queried for a certificate signing request (CSR), with the kubectl command, using compromised bootstrap credentials.
Privilege Escalation: Launch of privileged Kubernetes containerPreview
A malicious actor created Pods containing privileged containers or containers with privilege escalation capabilities.
A privileged container has the privileged field set to true. A container with privilege escalation capabilities has the allowPrivilegeEscalation field set to true.
Initial Access: Dormant Service Account Key Created
Detects events where a key is created for a dormant user-managed service account. In this context, a service account is considered dormant if it has been inactive for more than 180 days.
Process Tree
The detector checks the process tree of all running processes. If a process is a shell binary, the detector checks its parent process. If the parent process is a binary that should not spawn a shell process, the detector triggers a finding.
Unexpected Child Shell
The detector checks the process tree of all running processes. If a process is a shell binary, the detector checks its parent process. If the parent process is a binary that should not spawn a shell process, the detector triggers a finding.
Execution: Added Malicious Binary Executed
The detector looks for a binary being executed that was not part of the original container image, and was identified as malicious based on threat intelligence.
Execution: Modified Malicious Binary Executed
The detector looks for a binary being executed that was originally included in the container image but modified during run time, and was identified as malicious based on threat intelligence.
Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity
Detects when an anomalous multistep delegated request is found for an administrative activity.
Breakglass Account Used: break_glass_account
Detects the usage of an emergency access (breakglass) account
Configurable Bad Domain: APT29_Domains
Detects a connection to a specified domain name
Unexpected Role Grant: Forbidden roles
Detects when a specified role is granted to a user
Configurable Bad IP
Detects a connection to a specified IP address
Unexpected Compute Engine instance type
Detects the creation of Compute Engine instances that do not match a specified instance type or configuration.
Unexpected Compute Engine source image
Detects the creation of a Compute Engine instance with an image or image family that does not match a specified list
Unexpected Compute Engine region
Detects the creation of a Compute Engine instance in a region that is not in a specified list.
Custom role with prohibited permission
Detects when a custom role with any of the specified IAM permissions is granted to a principal.
Unexpected Cloud API Call
Detects when a specified principal calls a specified method against a specified resource. A finding is generated only if all regular expressions are matched in a single log entry.
Supported GCP_SECURITYCENTER_ERROR findings
You can find the UDM mapping in the
Field mapping reference: ERROR
table.
Finding name
Description
VPC_SC_RESTRICTION
Security Health Analytics can't produce certain findings for a project. The project is protected by a service perimeter, and the Security Command Center service account doesn't have access to the perimeter.
MISCONFIGURED_CLOUD_LOGGING_EXPORT
The project configured for continuous export to Cloud Logging is unavailable. Security Command Center can't send findings to Logging.
API_DISABLED
A required API is disabled for the project. The disabled service can't send findings to Security Command Center.
KTD_IMAGE_PULL_FAILURE
Container Threat Detection can't be enabled on the cluster because a required container image can't be pulled (downloaded) from gcr.io, the Container Registry image host. The image is needed to deploy the Container Threat Detection DaemonSet that Container Threat Detection requires.
KTD_BLOCKED_BY_ADMISSION_CONTROLLER
Container Threat Detection can't be enabled on a Kubernetes cluster. A third-party admission controller is preventing the deployment of a Kubernetes DaemonSet object that Container Threat Detection requires.
When viewed in the Google Cloud console, the finding details include the error message that was returned by Google Kubernetes Engine when Container Threat Detection attempted to deploy a Container Threat Detection DaemonSet Object.
KTD_SERVICE_ACCOUNT_MISSING_PERMISSIONS
A service account is missing permissions that Container Threat Detection requires. Container Threat Detection could stop functioning properly because the detection instrumentation cannot be enabled, upgraded, or disabled.
GKE_SERVICE_ACCOUNT_MISSING_PERMISSIONS
Container Threat Detection can't generate findings for a Google Kubernetes Engine cluster, because the GKE default service account on the cluster is missing permissions. This prevents Container Threat Detection from being successfully enabled on the cluster.
SCC_SERVICE_ACCOUNT_MISSING_PERMISSIONS
The Security Command Center service account is missing permissions required to function properly. No findings are produced.
Supported GCP_SECURITYCENTER_OBSERVATION findings
You can find the UDM mapping in the
Field mapping reference: OBSERVATION
table.
Finding name
Description
Persistence: Project SSH Key Added
A project-level SSH key was created in a project, for a project that is more than 10 days old.
Persistence: Add Sensitive Role
A sensitive or highly-privileged organization-level IAM role was granted in an organization that is more than 10 days old.
Supported GCP_SECURITYCENTER_UNSPECIFIED findings
You can find the UDM mapping in the
Field mapping reference: UNSPECIFIED
table.
Finding name
Description
OPEN_FIREWALL
A firewall is configured to be open to public access.
Supported GCP_SECURITYCENTER_VULNERABILITY findings
You can find UDM mapping in the
Field mapping reference: VULNERABILITY
table.
Finding name
Description
DISK_CSEK_DISABLED
Disks on this VM are not encrypted with Customer Supplied Encryption Keys (CSEK). This detector requires additional configuration to enable. For instructions, see
Special-case detector
.
ALPHA_CLUSTER_ENABLED
Alpha cluster features are enabled for a GKE cluster.
AUTO_REPAIR_DISABLED
A GKE cluster's auto repair feature, which keeps nodes in a healthy, running state, is disabled.
AUTO_UPGRADE_DISABLED
A GKE cluster's auto upgrade feature, which keeps clusters and node pools on the latest stable version of Kubernetes, is disabled.
CLUSTER_SHIELDED_NODES_DISABLED
Shielded GKE nodes are not enabled for a cluster
COS_NOT_USED
Compute Engine VMs aren't using the Container-Optimized OS that is designed for running Docker containers on Google Cloud securely.
INTEGRITY_MONITORING_DISABLED
Integrity monitoring is disabled for a GKE cluster.
IP_ALIAS_DISABLED
A GKE cluster was created with alias IP ranges disabled.
LEGACY_METADATA_ENABLED
Legacy metadata is enabled on GKE clusters.
RELEASE_CHANNEL_DISABLED
A GKE cluster is not subscribed to a release channel.
DATAPROC_IMAGE_OUTDATED
A Dataproc cluster was created with a Dataproc image version that is impacted by security vulnerabilities in the Apache Log4j 2 utility (
CVE-2021-44228
and
CVE-2021-45046)
.
PUBLIC_DATASET
A dataset is configured to be open to public access.
DNSSEC_DISABLED
DNSSEC is disabled for Cloud DNS zones.
RSASHA1_FOR_SIGNING
RSASHA1 is used for key signing in Cloud DNS zones.
REDIS_ROLE_USED_ON_ORG
A Redis IAM role is assigned at the organization or folder level.
KMS_PUBLIC_KEY
A Cloud KMS cryptographic key is publicly accessible.
SQL_CONTAINED_DATABASE_AUTHENTICATION
The contained database authentication database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_CROSS_DB_OWNERSHIP_CHAINING
The cross_db_ownership_chaining database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_EXTERNAL_SCRIPTS_ENABLED
The external scripts enabled database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_LOCAL_INFILE
The local_infile database flag for a Cloud SQL for MySQL instance is not set to off.
SQL_LOG_ERROR_VERBOSITY
The log_error_verbosity database flag for a Cloud SQL for PostgreSQL instance is not set to default or stricter.
SQL_LOG_MIN_DURATION_STATEMENT_ENABLED
The log_min_duration_statement database flag for a Cloud SQL for PostgreSQL instance is not set to "-1".
SQL_LOG_MIN_ERROR_STATEMENT
The log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance is not set appropriately.
SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY
The log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance does not have an appropriate severity level.
SQL_LOG_MIN_MESSAGES
The log_min_messages database flag for a Cloud SQL for PostgreSQL instance is not set to warning.
SQL_LOG_EXECUTOR_STATS_ENABLED
The log_executor_status database flag for a Cloud SQL for PostgreSQL instance is not set to off.
SQL_LOG_HOSTNAME_ENABLED
The log_hostname database flag for a Cloud SQL for PostgreSQL instance is not set to off.
SQL_LOG_PARSER_STATS_ENABLED
The log_parser_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.
SQL_LOG_PLANNER_STATS_ENABLED
The log_planner_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.
SQL_LOG_STATEMENT_STATS_ENABLED
The log_statement_stats database flag for a Cloud SQL for PostgreSQL instance is not set to off.
SQL_LOG_TEMP_FILES
The log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not set to "0".
SQL_REMOTE_ACCESS_ENABLED
The remote access database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_SKIP_SHOW_DATABASE_DISABLED
The skip_show_database database flag for a Cloud SQL for MySQL instance is not set to on.
SQL_TRACE_FLAG_3625
The 3625 (trace flag) database flag for a Cloud SQL for SQL Server instance is not set to on.
SQL_USER_CONNECTIONS_CONFIGURED
The user connections database flag for a Cloud SQL for SQL Server instance is configured.
SQL_USER_OPTIONS_CONFIGURED
The user options database flag for a Cloud SQL for SQL Server instance is configured.
SQL_WEAK_ROOT_PASSWORD
A Cloud SQL database has a weak password configured for the root account. This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
PUBLIC_LOG_BUCKET
A storage bucket used as a log sink is publicly accessible.
ACCESSIBLE_GIT_REPOSITORY
A Git repository is exposed publicly. To resolve this finding, remove unintentional public access to the GIT repository.
ACCESSIBLE_SVN_REPOSITORY
An SVN repository is exposed publicly. To resolve this finding, remove public unintentional access to the SVN repository.
ACCESSIBLE_ENV_FILE
An ENV file is exposed publicly. To resolve this finding, remove public unintentional access to the ENV file.
CACHEABLE_PASSWORD_INPUT
Passwords entered on the web application can be cached in a regular browser cache instead of a secure password storage.
CLEAR_TEXT_PASSWORD
Passwords are being transmitted in clear text and can be intercepted. To resolve this finding, encrypt the password transmitted over the network.
INSECURE_ALLOW_ORIGIN_ENDS_WITH_VALIDATION
A cross-site HTTP or HTTPS endpoint validates only a suffix of the Origin request header before reflecting it inside the Access-Control-Allow-Origin response header. To resolve this finding, validate that the expected root domain is part of the Origin header value before reflecting it in the Access-Control-Allow-Origin response header. For subdomain wildcards, prepend the dot to the root domain—for example, .endsWith("".google.com"").
INSECURE_ALLOW_ORIGIN_STARTS_WITH_VALIDATION
A cross-site HTTP or HTTPS endpoint validates only a prefix of the Origin request header before reflecting it inside the Access-Control-Allow-Origin response header. To resolve this finding, validate that the expected domain fully matches the Origin header value before reflecting it in the Access-Control-Allow-Origin response header—for example, .equals("".google.com"").
INVALID_CONTENT_TYPE
A resource was loaded that doesn't match the response's Content-Type HTTP header. To resolve this finding, set X-Content-Type-Options HTTP header with the correct value.
INVALID_HEADER
A security header has a syntax error and is ignored by browsers. To resolve this finding, set HTTP security headers correctly.
MISMATCHING_SECURITY_HEADER_VALUES
A security header has duplicated, mismatching values, which result in undefined behavior. To resolve this finding, set HTTP security headers correctly.
MISSPELLED_SECURITY_HEADER_NAME
A security header is misspelled and is ignored. To resolve this finding, set HTTP security headers correctly.
MIXED_CONTENT
Resources are being served over HTTP on an HTTPS page. To resolve this finding, make sure that all resources are served over HTTPS.
OUTDATED_LIBRARY
A library was detected that has known vulnerabilities. To resolve this finding, upgrade libraries to a newer version.
SERVER_SIDE_REQUEST_FORGERY
A server-side request forgery (SSRF) vulnerability was detected. To resolve this finding, use an allowlist to limit the domains and IP addresses that the web application can make requests to.
SESSION_ID_LEAK
When making a cross-domain request, the web application includes the user's session identifier in its Referer request header. This vulnerability gives the receiving domain access to the session identifier, which can be used to impersonate or uniquely identify the user.
SQL_INJECTION
A potential SQL injection vulnerability was detected. To resolve this finding, use parameterized queries to prevent user inputs from influencing the structure of the SQL query.
STRUTS_INSECURE_DESERIALIZATION
The use of a vulnerable version of Apache Struts was detected. To resolve this finding, upgrade Apache Struts to the latest version.
XSS
A field in this web application is vulnerable to a cross-site scripting (XSS) attack. To resolve this finding, validate and escape untrusted user-supplied data.
XSS_ANGULAR_CALLBACK
A user-provided string isn't escaped and AngularJS can interpolate it. To resolve this finding, validate and escape untrusted user-supplied data handled by Angular framework.
XSS_ERROR
A field in this web application is vulnerable to a cross-site scripting attack. To resolve this finding, validate and escape untrusted user-supplied data.
XXE_REFLECTED_FILE_LEAKAGE
An XML External Entity (XXE) vulnerability was detected. This vulnerability can cause the web application to leak a file on the host. To resolve this finding, configure your XML parsers to disallow external entities.
BASIC_AUTHENTICATION_ENABLED
IAM or client certificate authentication should be enabled on Kubernetes Clusters.
CLIENT_CERT_AUTHENTICATION_DISABLED
Kubernetes Clusters should be created with Client Certificate enabled.
LABELS_NOT_USED
Labels can be used to break down billing information.
PUBLIC_STORAGE_OBJECT
Storage object ACL should not grant access to allUsers.
SQL_BROAD_ROOT_LOGIN
Root access to a SQL database should be limited to allowlisted trusted IPs.
WEAK_CREDENTIALS
This detector checks for weak credentials using ncrack brute force methods.
Supported services: SSH, RDP, FTP, WordPress, TELNET, POP3, IMAP, VCS, SMB, SMB2, VNC, SIP, REDIS, PSQL, MYSQL, MSSQL, MQTT, MONGODB, WINRM, DICOM
ELASTICSEARCH_API_EXPOSED
The Elasticsearch API lets callers perform arbitrary queries, write and execute scripts, and add additional documents to the service.
EXPOSED_GRAFANA_ENDPOINT
In Grafana 8.0.0 to 8.3.0, users can access without authentication an endpoint that has a directory traversal vulnerability that allows any user to read any file on the server without authentication. For more information, see
CVE-2021-43798
.
EXPOSED_METABASE
Versions x.40.0 to x.40.4 of Metabase, an open source data analytics platform, contain a vulnerability in the custom GeoJSON map support and potential local file inclusion, including environment variables. URLs were not validated prior to being loaded. For more information, see
CVE-2021-41277
.
EXPOSED_SPRING_BOOT_ACTUATOR_ENDPOINT
This detector checks whether sensitive Actuator endpoints of Spring Boot applications are exposed. Some of the default endpoints, like /heapdump, might expose sensitive information. Other endpoints, like /env, might lead to remote code execution. Currently, only /heapdump is checked.
HADOOP_YARN_UNAUTHENTICATED_RESOURCE_MANAGER_API
This detector checks whether the Hadoop Yarn ResourceManager API, which controls the computation and storage resources of a Hadoop cluster, is exposed and allows unauthenticated code execution.
JAVA_JMX_RMI_EXPOSED
The Java Management Extension (JMX) allows remote monitoring and diagnostics for Java applications. Running JMX with unprotected Remote Method Invocation endpoint allows any remote users to create a javax.management.loading.MLet MBean and use it to create new MBeans from arbitrary URLs.
JUPYTER_NOTEBOOK_EXPOSED_UI
This detector checks whether an unauthenticated Jupyter Notebook is exposed. Jupyter allows remote code execution by design on the host machine. An unauthenticated Jupyter Notebook puts the hosting VM at risk of remote code execution.
KUBERNETES_API_EXPOSED
The Kubernetes API is exposed, and can be accessed by unauthenticated callers. This allows arbitrary code execution on the Kubernetes cluster.
UNFINISHED_WORDPRESS_INSTALLATION
This detector checks whether a WordPress installation is unfinished. An unfinished WordPress installation exposes the /wp-admin/install.php page, which allows attacker to set the admin password and, possibly, compromise the system.
UNAUTHENTICATED_JENKINS_NEW_ITEM_CONSOLE
This detector checks for an unauthenticated Jenkins instance by sending a probe ping to the /view/all/newJob endpoint as an anonymous visitor. An authenticated Jenkins instance shows the createItem form, which allows the creation of arbitrary jobs that could lead to remote code execution.
APACHE_HTTPD_RCE
A flaw was found in Apache HTTP Server 2.4.49 that allows an attacker to use a path traversal attack to map URLs to files outside the expected document root and see the source of interpreted files, like CGI scripts. This issue is known to be exploited in the wild. This issue affects Apache 2.4.49 and 2.4.50 but not earlier versions. For more information about this vulnerability, see:
CVE record CVE-2021-41773
Apache HTTP Server 2.4 vulnerabilities
APACHE_HTTPD_SSRF
Attackers can craft a URI to the Apache web server that causes mod_proxy to forward the request to an origin server that is chosen by the attacker. This issue affects Apache HTTP server 2.4.48 and earlier. For more information about this vulnerability, see:
CVE record CVE-2021-40438
Apache HTTP Server 2.4 vulnerabilities
CONSUL_RCE
Attackers can execute arbitrary code on a Consul server because the Consul instance is configured with -enable-script-checks set to true and the Consul HTTP API is unsecured and accessible over the network. In Consul 0.9.0 and earlier, script checks are on by default. For more information, see
Protecting Consul from RCE Risk in Specific Configurations
. To check for this vulnerability, Rapid Vulnerability Detection registers a service on the Consul instance by using the /v1/health/service REST endpoint, which then executes one of the following:

* A curl command to a remote server outside of the network. An attacker can use the curl command to exfiltrate data from the server.

* A printf command. Rapid Vulnerability Detection then verifies the output of the command by using the /v1/health/service REST endpoint.

* After the check, Rapid Vulnerability Detection cleans up and deregisters the service by using the /v1/agent/service/deregister/ REST endpoint.
DRUID_RCE
Apache Druid includes the ability to execute user-provided JavaScript code embedded in various types of requests. This functionality is intended for use in high-trust environments, and is disabled by default. However, in Druid 0.20.0 and earlier, it is possible for an authenticated user to send a specially-crafted request that forces Druid to run user-provided JavaScript code for that request, regardless of server configuration. This can be leveraged to execute code on the target machine with the privileges of the Druid server process. For more information, see
CVE-2021-25646 Detail
.
DRUPAL_RCE
Drupal versions before 7.58, 8.x before 8.3.9, 8.4.x before 8.4.6, and 8.5.x before 8.5.1 are vulnerable to remote code execution on Form API AJAX requests.
Drupal versions 8.5.x before 8.5.11 and 8.6.x before 8.6.10 are vulnerable to remote code execution when either the RESTful Web Service module or the JSON:API is enabled. This vulnerability can be exploited by an unauthenticated attacker using a custom POST request.
FLINK_FILE_DISCLOSURE
A vulnerability in Apache Flink versions 1.11.0, 1.11.1, and 1.11.2 lets attackers read any file on the local filesystem of the JobManager through the REST interface of the JobManager process. Access is restricted to files accessible by the JobManager process.
GITLAB_RCE
In GitLab Community Edition (CE) and Enterprise Edition (EE) versions 11.9 and later, GitLab does not properly validate image files that are passed to a file parser. An attacker can exploit this vulnerability for remote command execution.
GoCD_RCE
In GoCD 21.2.0 and earlier, there is an endpoint that can be accessed without authentication. This endpoint has a directory traversal vulnerability that allows a user to read any file on the server without authentication.
JENKINS_RCE
Jenkins versions 2.56 and earlier, and 2.46.1 LTS and earlier are vulnerable to remote code execution. This vulnerability can be triggered by an unauthenticated attacker using a malicious serialized Java object.
JOOMLA_RCE
Joomla versions 1.5.x, 2.x, and 3.x before 3.4.6 are vulnerable to remote code execution. This vulnerability can be triggered with a crafted header containing serialized PHP objects.
Joomla versions 3.0.0 through 3.4.6 are vulnerable to remote code execution. This vulnerability can be triggered by sending a POST request that contains a crafted serialized PHP object.
LOG4J_RCE
In Apache Log4j2 2.14.1 and earlier, JNDI features that are used in configurations, log messages, and parameters do not protect against attacker-controlled LDAP and other JNDI related endpoints. For more information, see
CVE-2021-44228
.
MANTISBT_PRIVILEGE_ESCALATION
MantisBT through version 2.3.0 allows arbitrary password reset and unauthenticated admin access by supplying an empty confirm_hash value to verify.php.
OGNL_RCE
Confluence Server and Data Center instances contain an OGNL injection vulnerability that allows an unauthenticated attacker to execute arbitrary code. For more information, see
CVE-2021-26084
.
OPENAM_RCE
OpenAM server 14.6.2 and earlier and ForgeRock AM server 6.5.3 and earlier have a Java deserialization vulnerability in the jato.pageSession parameter on multiple pages. The exploitation does not require authentication, and remote code execution can be triggered by sending a single crafted /ccversion/* request to the server. The vulnerability exists due to the usage of Sun ONE Application. For more information, see
CVE-2021-35464
.
ORACLE_WEBLOGIC_RCE
Certain versions of the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Console) contain a vulnerability, including versions 10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0, 12.2.1.4.0 and 14.1.1.0.0. This easily exploitable vulnerability allows an unauthenticated attacker with network access via HTTP to compromise an Oracle WebLogic Server. Successful attacks of this vulnerability can result in a takeover of Oracle WebLogic Server. For more information, see
CVE-2020-14882
.
PHPUNIT_RCE
PHPUnit
versions prior to 5.6.3 allow remote code execution with a single unauthenticated POST request.
PHP_CGI_RCE
PHP versions before 5.3.12, and versions 5.4.x before 5.4.2, when configured as a CGI script, allow remote code execution. The vulnerable code does not properly handle query strings that lack an = (equals sign) character. This lets attackers add command line options that are executed on the server.
PORTAL_RCE
Deserialization of untrusted data in Liferay Portal versions prior to 7.2.1 CE GA2 allows remote attackers to execute arbitrary code through JSON web services.
REDIS_RCE
If a Redis instance does not require authentication to execute admin commands, attackers might be able to execute arbitrary code.
SOLR_FILE_EXPOSED
Authentication is not enabled in Apache Solr, an open source search server. When Apache Solr does not require authentication, an attacker can directly craft a request to enable a specific configuration, and eventually implement a server-side request forgery (SSRF) or read arbitrary files.
SOLR_RCE
Apache Solr versions 5.0.0 through Apache Solr 8.3.1 are vulnerable to remote code execution through the VelocityResponseWriter if params.resource.loader.enabled is set to true. This allows attackers to create a parameter that contains a malicious Velocity template.
STRUTS_RCE
Apache Struts versions before 2.3.32 and 2.5.x before 2.5.10.1 are vulnerable to remote code execution. The vulnerability can be triggered by an unauthenticated attacker providing a crafted Content-Type header.
The REST plugin in Apache Struts versions 2.1.1 through 2.3.x before 2.3.34 and 2.5.x before 2.5.13 are vulnerable to remote code execution when deserializing crafted XML payloads.
Apache Struts versions 2.3 to 2.3.34 and 2.5 to 2.5.16 are vulnerable to remote code execution when alwaysSelectFullNamespace is set to true and certain other action configurations exist.
TOMCAT_FILE_DISCLOSURE
Apache Tomcat versions 9.x before 9.0.31, 8.x before 8.5.51, 7.x before 7.0.100, and all 6.x are vulnerable to source code and configuration disclosure through an exposed Apache JServ Protocol connector. In some cases, this is leveraged to perform remote code execution if file uploading is allowed.
VBULLETIN_RCE
vBulletin servers running versions 5.0.0 up to 5.5.4 are vulnerable to remote code execution. This vulnerability can be exploited by an unauthenticated attacker using a query parameter in a routestring request.
VCENTER_RCE
VMware vCenter Server versions 7.x before 7.0 U1c, 6.7 before 6.7 U3l and 6.5 before 6.5 U3n are vulnerable to remote code execution. This vulnerability can be triggered by an attacker uploading a crafted Java Server Pages file to a web-accessible directory, then triggering execution of that file.
WEBLOGIC_RCE
Certain versions of the Oracle WebLogic Server product of Oracle Fusion Middleware (component: Console) contain a remote code execution vulnerability, including versions 10.3.6.0.0, 12.1.3.0.0, 12.2.1.3.0, 12.2.1.4.0, and 14.1.1.0.0. This vulnerability is related to CVE-2020-14750, CVE-2020-14882, CVE-2020-14883. For more information, see
CVE-2020-14883
.
OS_VULNERABILITY
VM Manager detected a vulnerability in the installed operating system (OS) package for a Compute Engine VM.
UNUSED_IAM_ROLE
IAM recommender detected a user account that has an IAM role that has not been used in the last 90 days.
GKE_RUNTIME_OS_VULNERABILITY
GKE continuously scans container images that run on enrolled
   GKE clusters  for vulnerabilities. GKE uses vulnerability data from
   public CVE databases, such as
NIST
.
   While GKE can scan images from any registry, the OS version must be supported.  For a list of supported operating systems, see
Supported Linux versions
.
GKE_SECURITY_BULLETIN
When a vulnerability is discovered in GKE, a security
   bulletin is published after the vulnerability is patched. For detailed
   information about vulnerability patching process and timelines, see
GKE security patching
.
SERVICE_AGENT_ROLE_REPLACED_WITH_BASIC_ROLE
IAM recommender detected that the original default IAM role granted to a service agent was replaced with one of the basic IAM roles: Owner, Editor, or Viewer. Basic roles are excessively permissive legacy roles and should not be granted to service agents.
Supported GCP_SECURITYCENTER_MISCONFIGURATION findings
You can find the UDM mapping in the
Field mapping reference: MISCONFIGURATION
table.
Finding name
Description
API_KEY_APIS_UNRESTRICTED
There are API keys being used too broadly. To resolve this, limit API key usage to allow only the APIs needed by the application.
API_KEY_APPS_UNRESTRICTED
There are API keys being used in an unrestricted way, allowing use by any untrusted app
API_KEY_EXISTS
A project is using API keys instead of standard authentication.
API_KEY_NOT_ROTATED
The API key hasn't been rotated for more than 90 days
PUBLIC_COMPUTE_IMAGE
A Compute Engine image is publicly accessible.
CONFIDENTIAL_COMPUTING_DISABLED
Confidential Computing is disabled on a Compute Engine instance.
COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED
Project-wide SSH keys are used, allowing login to all instances in the project.
COMPUTE_SECURE_BOOT_DISABLED
This Shielded VM does not have Secure Boot enabled. Using Secure Boot helps protect virtual machine instances against advanced threats such as rootkits and bootkits.
DEFAULT_SERVICE_ACCOUNT_USED
An instance is configured to use the default service account.
FULL_API_ACCESS
An instance is configured to use the default service account with full access to all Google Cloud APIs.
OS_LOGIN_DISABLED
OS Login is disabled on this instance.
PUBLIC_IP_ADDRESS
An instance has a public IP address.
SHIELDED_VM_DISABLED
Shielded VM is disabled on this instance.
COMPUTE_SERIAL_PORTS_ENABLED
Serial ports are enabled for an instance, allowing connections to the instance's serial console.
DISK_CMEK_DISABLED
Disks on this VM are not encrypted with customer- managed encryption keys (CMEK). This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
HTTP_LOAD_BALANCER
An instance uses a load balancer that is configured to use a target HTTP proxy instead of a target HTTPS proxy.
IP_FORWARDING_ENABLED
IP forwarding is enabled on instances.
WEAK_SSL_POLICY
An instance has a weak SSL policy.
BINARY_AUTHORIZATION_DISABLED
Binary Authorization is disabled on a GKE cluster.
CLUSTER_LOGGING_DISABLED
Logging isn't enabled for a GKE cluster.
CLUSTER_MONITORING_DISABLED
Monitoring is disabled on GKE clusters.
CLUSTER_PRIVATE_GOOGLE_ACCESS_DISABLED
Cluster hosts are not configured to use only private, internal IP addresses to access Google APIs.
CLUSTER_SECRETS_ENCRYPTION_DISABLED
Application-layer secrets encryption is disabled on a GKE cluster.
INTRANODE_VISIBILITY_DISABLED
Intranode visibility is disabled for a GKE cluster.
MASTER_AUTHORIZED_NETWORKS_DISABLED
Control Plane Authorized Networks is not enabled on GKE clusters.
NETWORK_POLICY_DISABLED
Network policy is disabled on GKE clusters.
NODEPOOL_SECURE_BOOT_DISABLED
Secure Boot is disabled for a GKE cluster.
OVER_PRIVILEGED_ACCOUNT
A service account has overly broad project access in a cluster.
OVER_PRIVILEGED_SCOPES
A node service account has broad access scopes.
POD_SECURITY_POLICY_DISABLED
PodSecurityPolicy is disabled on a GKE cluster.
PRIVATE_CLUSTER_DISABLED
A GKE cluster has a Private cluster disabled.
WORKLOAD_IDENTITY_DISABLED
A GKE cluster is not subscribed to a release channel.
LEGACY_AUTHORIZATION_ENABLED
Legacy Authorization is enabled on GKE clusters.
NODEPOOL_BOOT_CMEK_DISABLED
Boot disks in this node pool are not encrypted with customer-managed encryption keys (CMEK). This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
WEB_UI_ENABLED
The GKE web UI (dashboard) is enabled.
AUTO_REPAIR_DISABLED
A GKE cluster's auto repair feature, which keeps nodes in a healthy, running state, is disabled.
AUTO_UPGRADE_DISABLED
A GKE cluster's auto upgrade feature, which keeps clusters and node pools on the latest stable version of Kubernetes, is disabled.
CLUSTER_SHIELDED_NODES_DISABLED
Shielded GKE nodes are not enabled for a cluster
RELEASE_CHANNEL_DISABLED
A GKE cluster is not subscribed to a release channel.
BIGQUERY_TABLE_CMEK_DISABLED
A BigQuery table is not configured to use a customer-managed encryption key (CMEK). This detector requires additional configuration to enable.
DATASET_CMEK_DISABLED
A BigQuery dataset is not configured to use a default CMEK. This detector requires additional configuration to enable.
EGRESS_DENY_RULE_NOT_SET
An egress deny rule is not set on a firewall. Egress deny rules should be set to block unwanted outbound traffic.
FIREWALL_RULE_LOGGING_DISABLED
Firewall rule logging is disabled. Firewall rule logging should be enabled so you can audit network access.
OPEN_CASSANDRA_PORT
A firewall is configured to have an open Cassandra port that allows generic access.
OPEN_SMTP_PORT
A firewall is configured to have an open SMTP port that allows generic access.
OPEN_REDIS_PORT
A firewall is configured to have an open REDIS port that allows generic access.
OPEN_POSTGRESQL_PORT
A firewall is configured to have an open PostgreSQL port that allows generic access.
OPEN_POP3_PORT
A firewall is configured to have an open POP3 port that allows generic access.
OPEN_ORACLEDB_PORT
A firewall is configured to have an open NETBIOS port that allows generic access.
OPEN_NETBIOS_PORT
A firewall is configured to have an open NETBIOS port that allows generic access.
OPEN_MYSQL_PORT
A firewall is configured to have an open MYSQL port that allows generic access.
OPEN_MONGODB_PORT
A firewall is configured to have an open MONGODB port that allows generic access.
OPEN_MEMCACHED_PORT
A firewall is configured to have an open MEMCACHED port that allows generic access.
OPEN_LDAP_PORT
A firewall is configured to have an open LDAP port that allows generic access.
OPEN_FTP_PORT
A firewall is configured to have an open FTP port that allows generic access.
OPEN_ELASTICSEARCH_PORT
A firewall is configured to have an open ELASTICSEARCH port that allows generic access.
OPEN_DNS_PORT
A firewall is configured to have an open DNS port that allows generic access.
OPEN_HTTP_PORT
A firewall is configured to have an open HTTP port that allows generic access.
OPEN_DIRECTORY_SERVICES_PORT
A firewall is configured to have an open DIRECTORY_SERVICES port that allows generic access.
OPEN_CISCOSECURE_WEBSM_PORT
A firewall is configured to have an open CISCOSECURE_WEBSM port that allows generic access.
OPEN_RDP_PORT
A firewall is configured to have an open RDP port that allows generic access.
OPEN_TELNET_PORT
A firewall is configured to have an open TELNET port that allows generic access.
OPEN_FIREWALL
A firewall is configured to be open to public access.
OPEN_SSH_PORT
A firewall is configured to have an open SSH port that allows generic access.
SERVICE_ACCOUNT_ROLE_SEPARATION
A user has been assigned the Service Account Admin and Service Account User roles. This violates the "Separation of Duties" principle.
NON_ORG_IAM_MEMBER
There is a user who isn't using organizational credentials. As per CIS Google Cloud Foundations 1.0, currently, only identities with @gmail.com email addresses trigger this detector.
OVER_PRIVILEGED_SERVICE_ACCOUNT_USER
A user has the Service Account User or Service Account Token Creator role at the project level, instead of for a specific service account.
ADMIN_SERVICE_ACCOUNT
A service account has Admin, Owner, or Editor privileges. These roles shouldn't be assigned to user-created service accounts.
SERVICE_ACCOUNT_KEY_NOT_ROTATED
A service account key hasn't been rotated for more than 90 days.
USER_MANAGED_SERVICE_ACCOUNT_KEY
A user manages a service account key.
PRIMITIVE_ROLES_USED
A user has the basic role, Owner, Writer, or Reader. These roles are too permissive and shouldn't be used.
KMS_ROLE_SEPARATION
Separation of duties is not enforced, and a user exists who has any of the following Cloud Key Management Service (Cloud KMS) roles at the same time: CryptoKey Encrypter/Decrypter, Encrypter, or Decrypter.
OPEN_GROUP_IAM_MEMBER
A Google Groups account that can be joined without approval is used as an IAM allow policy principal.
KMS_KEY_NOT_ROTATED
Rotation isn't configured on a Cloud KMS encryption key. Keys should be rotated within a period of 90 days.
KMS_PROJECT_HAS_OWNER
A user has Owner permissions on a project that has cryptographic keys.
TOO_MANY_KMS_USERS
There are more than three users of cryptographic keys.
OBJECT_VERSIONING_DISABLED
Object versioning isn't enabled on a storage bucket where sinks are configured.
LOCKED_RETENTION_POLICY_NOT_SET
A locked retention policy is not set for logs.
BUCKET_LOGGING_DISABLED
There is a storage bucket without logging enabled.
LOG_NOT_EXPORTED
There is a resource that doesn't have an appropriate log sink configured.
AUDIT_LOGGING_DISABLED
Audit logging has been disabled for this resource.
MFA_NOT_ENFORCED
There are users who aren't using 2-step verification.
ROUTE_NOT_MONITORED
Log metrics and alerts aren't configured to monitor VPC network route changes.
OWNER_NOT_MONITORED
Log metrics and alerts aren't configured to monitor Project Ownership assignments or changes.
AUDIT_CONFIG_NOT_MONITORED
Log metrics and alerts aren't configured to monitor Audit Configuration changes.
BUCKET_IAM_NOT_MONITORED
Log metrics and alerts aren't configured to monitor Cloud Storage IAM permission changes.
CUSTOM_ROLE_NOT_MONITORED
Log metrics and alerts aren't configured to monitor Custom Role changes.
FIREWALL_NOT_MONITORED
Log metrics and alerts aren't configured to monitor Virtual Private Cloud (VPC) Network Firewall rule changes.
NETWORK_NOT_MONITORED
Log metrics and alerts aren't configured to monitor VPC network changes.
SQL_INSTANCE_NOT_MONITORED
Log metrics and alerts aren't configured to monitor Cloud SQL instance configuration changes.
DEFAULT_NETWORK
The default network exists in a project.
DNS_LOGGING_DISABLED
DNS logging on a VPC network is not enabled.
PUBSUB_CMEK_DISABLED
A Pub/Sub topic is not encrypted with customer-managed encryption keys (CMEK). This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
PUBLIC_SQL_INSTANCE
A Cloud SQL database instance accepts connections from all IP addresses.
SSL_NOT_ENFORCED
A Cloud SQL database instance doesn't require all incoming connections to use SSL.
AUTO_BACKUP_DISABLED
A Cloud SQL database doesn't have automatic backups enabled.
SQL_CMEK_DISABLED
A SQL database instance is not encrypted with customer-managed encryption keys (CMEK). This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
SQL_LOG_CHECKPOINTS_DISABLED
The log_checkpoints database flag for a Cloud SQL for PostgreSQL instance is not set to on.
SQL_LOG_CONNECTIONS_DISABLED
The log_connections database flag for a Cloud SQL for PostgreSQL instance is not set to on.
SQL_LOG_DISCONNECTIONS_DISABLED
The log_disconnections database flag for a Cloud SQL for PostgreSQL instance is not set to on.
SQL_LOG_DURATION_DISABLED
The log_duration database flag for a Cloud SQL for PostgreSQL instance is not set to on.
SQL_LOG_LOCK_WAITS_DISABLED
The log_lock_waits database flag for a Cloud SQL for PostgreSQL instance is not set to on.
SQL_LOG_STATEMENT
The log_statement database flag for a Cloud SQL for PostgreSQL instance is not set to Ddl (all data definition statements).
SQL_NO_ROOT_PASSWORD
A Cloud SQL database doesn't have a password configured for the root account. This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
SQL_PUBLIC_IP
A Cloud SQL database has a public IP address.
SQL_CONTAINED_DATABASE_AUTHENTICATION
The contained database authentication database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_CROSS_DB_OWNERSHIP_CHAINING
The cross_db_ownership_chaining database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_LOCAL_INFILE
The local_infile database flag for a Cloud SQL for MySQL instance is not set to off.
SQL_LOG_MIN_ERROR_STATEMENT
The log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance is not set appropriately.
SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY
The log_min_error_statement database flag for a Cloud SQL for PostgreSQL instance does not have an appropriate severity level.
SQL_LOG_TEMP_FILES
The log_temp_files database flag for a Cloud SQL for PostgreSQL instance is not set to "0".
SQL_REMOTE_ACCESS_ENABLED
The remote access database flag for a Cloud SQL for SQL Server instance is not set to off.
SQL_SKIP_SHOW_DATABASE_DISABLED
The skip_show_database database flag for a Cloud SQL for MySQL instance is not set to on.
SQL_TRACE_FLAG_3625
The 3625 (trace flag) database flag for a Cloud SQL for SQL Server instance is not set to on.
SQL_USER_CONNECTIONS_CONFIGURED
The user connections database flag for a Cloud SQL for SQL Server instance is configured.
SQL_USER_OPTIONS_CONFIGURED
The user options database flag for a Cloud SQL for SQL Server instance is configured.
PUBLIC_BUCKET_ACL
A Cloud Storage bucket is publicly accessible.
BUCKET_POLICY_ONLY_DISABLED
Uniform bucket-level access, previously called Bucket Policy Only, isn't configured.
BUCKET_CMEK_DISABLED
A bucket is not encrypted with customer-managed encryption keys (CMEK). This detector requires additional configuration to enable. For instructions, see
Enable and disable detectors
.
FLOW_LOGS_DISABLED
There is a VPC subnetwork that has flow logs disabled.
PRIVATE_GOOGLE_ACCESS_DISABLED
There are private subnetworks without access to Google public APIs.
kms_key_region_europe
Due to company policy, all encryption keys should remain stored in Europe.
kms_non_euro_region
Due to company policy, all encryption keys should remain stored in Europe.
LEGACY_NETWORK
A legacy network exists in a project.
LOAD_BALANCER_LOGGING_DISABLED
Logging is disabled for the load balancer.
Supported GCP_SECURITYCENTER_POSTURE_VIOLATION findings
You can find the UDM mapping in the
Field mapping reference: POSTURE VIOLATION
table.
Finding name
Description
SECURITY_POSTURE_DRIFT
Drift from the defined policies within security posture. This is detected by the security posture service.
SECURITY_POSTURE_POLICY_DRIFT
The security posture service detected a change to an organization policy that occurred outside of a posture update.
SECURITY_POSTURE_POLICY_DELETE
The security posture service detected that an organization policy was deleted. This deletion occurred outside of a posture update.
SECURITY_POSTURE_DETECTOR_DRIFT
The security posture service detected a change to a Security Health Analytics detector that occurred outside of a posture update.
SECURITY_POSTURE_DETECTOR_DELETE
The security posture service detected that a Security Health Analytics custom module was deleted. This deletion occurred outside of a posture update.
Supported Security Center log formats
The Security Center parser supports logs in JSON format.
Supported Security Center sample logs
GCP_SECURITYCENTER_THREAT sample logs
JSON
{
  "finding": {
    "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
    "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
    "resourceName": "//cloudidentity.googleapis.com/groups/GROUP_NAME@ORGANIZATION_NAME",
    "state": "ACTIVE",
    "category": "Credential Access: External Member Added To Privileged Group",
    "sourceProperties": {
      "sourceId": {
        "organizationNumber": "ORGANIZATION_ID",
        "customerOrganizationNumber": "ORGANIZATION_ID"
      },
      "detectionCategory": {
        "technique": "persistence",
        "indicator": "audit_log",
        "ruleName": "external_member_added_to_privileged_group"
      },
      "detectionPriority": "HIGH",
      "affectedResources": [
        {
          "gcpResourceName": "//cloudidentity.googleapis.com/groups/GROUP_NAME@ORGANIZATION_NAME"
        },
        {
          "gcpResourceName": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID"
        }
      ],
      "evidence": [
        {
          "sourceLogId": {
            "resourceContainer": "organizations/ORGANIZATION_ID",
            "timestamp": {
              "seconds": "1633622881",
              "nanos": 6.73869E8
            },
            "insertId": "INSERT_ID"
          }
        }
      ],
      "properties": {
        "externalMemberAddedToPrivilegedGroup": {
          "principalEmail": "abc@gmail.com",
          "groupName": "group:GROUP_NAME@ORGANIZATION_NAME",
          "externalMember": "user:abc@gamil.com",
          "sensitiveRoles": [
            {
              "resource": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
              "roleName": [
                "ROLES"
              ]
            }
          ]
        }
      },
      "findingId": "FINDING_ID",
      "contextUris": {
        "mitreUri": {
          "displayName": "dummy display name",
          "url": " dummy.url.com"
        },
        "cloudLoggingQueryUri": [
          {
            "displayName": "Cloud Logging Query Link",
            "url": "https://console.test.com/logs/query;query\\u003dtimestamp%3D%222022-10-01T16:08:01.673869Z%22%0AinsertId%3D%22INSERT_ID%22%0Aresource.labels.project_id%3D%22%22?project\\u003d"
          }
        ]
      }
    },
    "securityMarks": {
      "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
    },
    "eventTime": "2022-10-01T16:08:03.888Z",
    "createTime": "2022-10-01T16:08:04.516Z",
    "severity": "HIGH",
    "workflowState": "NEW",
    "canonicalName": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
    "findingClass": "THREAT"
  },
  "resource": {
    "name": "//cloudidentity.googleapis.com/groups/GROUP_NAME@ORGANIZATION_NAME"
  }
}
GCP_SECURITYCENTER_MISCONFIGURATION sample logs
JSON
{
  "findings": {
    "access": {},
    "assetDisplayName": "eventApps",
    "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
    "canonicalName": "projects/1032183397765/sources/4563429019522465317/findings/fdb789f992c67f6386ec735aca337bab",
    "category": "API_KEY_APIS_UNRESTRICTED",
    "compliances": [
      {
        "standard": "cis",
        "version": "1.0",
        "ids": [
          "1.12"
        ]
      },
      {
        "standard": "cis",
        "version": "1.1",
        "ids": [
          "1.14"
        ]
      },
      {
        "standard": "cis",
        "version": "1.2",
        "ids": [
          "1.14"
        ]
      }
    ],
    "contacts": {
      "security": {
        "contacts": [
          {
            "email": "test@domainname.com"
          }
        ]
      },
      "technical": {
        "contacts": [
          {
            "email": "test@domainname.com"
          }
        ]
      }
    },
    "createTime": "2022-12-01T15:16:21.119Z",
    "database": {},
    "description": "Unrestricted API keys are insecure because they can be retrieved on devices on which the key is stored or can be seen publicly, e.g., from within a browser. In accordance with the principle of least privileges, it is recommended to restrict the APIs that can be called using each API key to only those required by an application. For more information, see https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions",
    "eventTime": "2022-12-01T14:35:42.317Z",
    "exfiltration": {},
    "externalUri": "https://console.test.com/apis/credentials?project=eventapps-27705",
    "findingClass": "MISCONFIGURATION",
    "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/security_health_advisor",
    "indicator": {},
    "kernelRootkit": {},
    "kubernetes": {},
    "mitreAttack": {},
    "mute": "UNDEFINED",
    "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
    "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
    "parentDisplayName": "Security Health Analytics",
    "resourceName": "//cloudresourcemanager.googleapis.com/projects/1032183397765",
    "severity": "MEDIUM",
    "sourceDisplayName": "Security Health Analytics",
    "state": "ACTIVE",
    "vulnerability": {},
    "workflowState": "NEW"
  },
  "resource": {
    "name": "//cloudresourcemanager.googleapis.com/projects/1032183397765",
    "display_name": "dummy-display-name",
    "project_name": "//cloudresourcemanager.googleapis.com/projects/1032183397765",
    "project_display_name": "dummy-project",
    "parent_name": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
    "parent_display_name": "domainname.com",
    "type": "google.cloud.resourcemanager.Project",
    "folders": []
  },
  "sourceProperties": {
    "Recommendation": "Go to https://console.test.com/apis/credentials?project=eventapps-27705. In the section \\"API keys,\\" for each API key, click the name of the key. It will display API Key properties on a new page. In the \\"Key restrictions\\" section, set API restrictions to \\"Restrict key.\\" Click the \\"Select APIs\\" drop-down menu to choose which APIs to allow. Click \\"Save.\\"
    "ExceptionInstructions": "Add the security mark \\"allow_api_key_apis_unrestricted\\" to the asset with a value of \\"true\\" to prevent this finding from being activated again.",
    "Explanation": "Unrestricted API keys are insecure because they can be retrieved on devices on which the key is stored or can be seen publicly, e.g., from within a browser. In accordance with the principle of least privileges, it is recommended to restrict the APIs that can be called using each API key to only those required by an application. For more information, see https://cloud.google.com/docs/authentication/api-keys#api_key_restrictions",
    "ScannerName": "API_KEY_SCANNER",
    "ResourcePath": [
      "projects/eventapps-27705/",
      "organizations/ORGANIZATION_ID/"
    ],
    "compliance_standards": {
      "cis": [
        {
          "version": "1.0",
          "ids": [
            "1.12"
          ]
        },
        {
          "version": "1.1",
          "ids": [
            "1.14"
          ]
        },
        {
          "version": "1.2",
          "ids": [
            "1.14"
          ]
        }
      ]
    },
    "ReactivationCount": 0
  }
}
GCP_SECURITYCENTER_OBSERVATION sample logs
JSON
{
  "findings": {
    "access": {
      "principalEmail": "dummy.user@dummy.com",
      "callerIp": "198.51.100.1",
      "callerIpGeo": {
        "regionCode": "SG"
      },
      "serviceName": "compute.googleapis.com",
      "methodName": "v1.compute.projects.setCommonInstanceMetadata",
      "principalSubject": "user:dummy.user@dummy.com"
    },
    "canonicalName": "projects/856289305908/sources/SOURCE_ID/findings/FINDING_ID",
    "category": "Persistence: Project SSH Key Added",        
    "contacts": {
      "security": {
        "contacts": [
          {
            "email": "dummy.user@dummy.com"
          }
        ]
      },
      "technical": {
        "contacts": [
          {
            "email": "dummy.user@dummy.xyz"
          }
        ]
      }
    },
    "createTime": "2022-11-10T18:33:07.631Z",
    "database": {},
    "eventTime": "2022-11-10T18:33:07.271Z",
    "exfiltration": {},
    "findingClass": "OBSERVATION",
    "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/sensitive_actions",
    "indicator": {},
    "kernelRootkit": {},
    "kubernetes": {},
    "mitreAttack": {
      "primaryTactic": "PERSISTENCE",
      "primaryTechniques": [
        "ACCOUNT_MANIPULATION",
        "SSH_AUTHORIZED_KEYS"
      ]
    },
    "mute": "UNDEFINED",
    "name": "organizations/595779152576/sources/SOURCE_ID/findings/FINDING_ID",
    "parent": "organizations/595779152576/sources/SOURCE_ID",
    "parentDisplayName": "Sensitive Actions Service",
    "resourceName": "//compute.googleapis.com/projects/spring-banner-350111",
    "severity": "LOW",
    "sourceDisplayName": "Sensitive Actions Service",
    "state": "ACTIVE",
    "vulnerability": {},
    "workflowState": "NEW"
  },
  "resource": {
    "name": "//compute.googleapis.com/projects/spring-banner-350111",
    "display_name": "spring-banner-350111",
    "project_name": "//cloudresourcemanager.googleapis.com/projects/856289305908",
    "project_display_name": "dummy-project",
    "parent_name": "//cloudresourcemanager.googleapis.com/projects/856289305908",
    "parent_display_name": "spring-banner-350111",
    "type": "google.compute.Project",
    "folders": []
  },
  "sourceProperties": {
    "sourceId": {
      "projectNumber": "856289305908",
      "customerOrganizationNumber": "ORGANIZATION_ID"
    },
    "detectionCategory": {
      "ruleName": "sensitive_action",
      "subRuleName": "add_ssh_key"
    },
    "detectionPriority": "LOW",
    "affectedResources": [
      {
        "gcpResourceName": "//compute.googleapis.com/projects/spring-banner-350111"
      },
      {
        "gcpResourceName": "//cloudresourcemanager.googleapis.com/projects/856289305908"
      }
    ],
    "evidence": [
      {
        "sourceLogId": {
          "projectId": "spring-banner-350111",
          "resourceContainer": "projects/spring-banner-350111",
          "timestamp": {
            "seconds": "1668105185",
            "nanos": 642158000
          },
          "insertId": "v2stobd9ihi"
        }
      }
    ],
    "properties": {},
    "findingId": "findingId",
    "contextUris": {
      "mitreUri": {
        "displayName": "MITRE Link",
        "url": "dummy.domain.com"
      }
    }
  }
}
GCP_SECURITYCENTER_VULNERABILITY sample logs
JSON
{
  "findings": {
    "access": {},
    "assetDisplayName": "Sample-00000",
    "assetId": "organizations/ORGANIZATION_ID/assets/ASSET_ID",
    "canonicalName": "projects/PROJECT_ID/sources/SOURCE_ID/findings/FINDING_ID",
    "category": "CLEAR_TEXT_PASSWORD",
    "compliances": [
      {
        "standard": "owasp",
        "version": "2017",
        "ids": [
          "A3"
        ]
      },
      {
        "standard": "owasp",
        "version": "2021",
        "ids": [
          "A02"
        ]
      }
    ],
    "contacts": {
      "security": {
        "contacts": [
          {
            "email": "dummy@sample.com"
          }
        ]
      },
      "technical": {
        "contacts": [
          {
            "email": "dummy@sample.com"
          }
        ]
      }
    },
    "createTime": "2022-11-24T09:28:52.589Z",
    "database": {},
    "description": "An application appears to be transmitting a password field in clear text. An attacker can eavesdrop network traffic and sniff the password field.",
    "eventTime": "2022-11-24T04:56:26Z",
    "exfiltration": {},
    "externalUri": "https://sample.dummy.com/",
    "findingClass": "VULNERABILITY",
    "findingProviderId": "organizations/ORGANIZATION_ID/firstPartyFindingProviders/css",
    "indicator": {},
    "kernelRootkit": {},
    "kubernetes": {},
    "mitreAttack": {},
    "mute": "UNDEFINED",
    "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
    "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
    "parentDisplayName": "Web Security Scanner",
    "resourceName": "//dummy.sample.com",
    "severity": "MEDIUM",
    "sourceDisplayName": "Web Security Scanner",
    "state": "ACTIVE",
    "vulnerability": {},
    "workflowState": "NEW"
  },
  "resource": {
    "name": "//cloudresourcemanager.googleapis.com",
    "display_name": "dummy_name",
    "project_name": "//cloudresourcemanager.googleapis.com",
    "project_display_name": "dummy_name",
    "parent_name": "//dummy.sample.com",
    "parent_display_name": "Sample-Dev-Project",
    "type": "sample.cloud.dummy.Project",
    "folders": [
      {
        "resourceFolderDisplayName": "Sample-Dev-Project",
        "resourceFolder": "//cloudresourcemanager.googleapis.com/"
      }
    ]
  },
  "sourceProperties": {
    "severity": "MEDIUM",
    "fuzzedUrl": "dummy.domain.com",
    "form": {
      "actionUri": "dummy.domain.com",
      "fields": [
        "os_username",
        "os_password",
        "",
        "os_cookie",
        "os_destination",
        "user_role",
        "atl_token",
        "login"
      ]
    },
    "name": "projects/PROJECT_ID/scanConfigs/SCAN_CONFIG_ID/scanRuns/SCAN_RUN_ID/findings/FINDING_ID",
    "description": "An application appears to be transmitting a password field in clear text. An attacker can eavesdrop network traffic and sniff the password field.",
    "reproductionUrl": "http://198.51.100.1:0000/login.jsp?searchString=",
    "httpMethod": "GET",
    "finalUrl": "http://0.0.0.0:0000/sample.dummy=",
    "ResourcePath": [
      "projects/sample-dummy/",
      "folders/FOLDER_ID/",
      "organizations/ORGANIZATION_ID/"
    ],
    "compliance_standards": {
      "owasp": [
        {
          "version": "2017",
          "ids": [
            "A3"
          ]
        },
        {
          "version": "2021",
          "ids": [
            "A02"
          ]
        }
      ]
    }
  }
}
GCP_SECURITYCENTER_ERROR sample logs
JSON
{
  "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID",
  "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID",
  "resourceName": "//cloudresourcemanager.googleapis.com/projects/742742027423",
  "state": "ACTIVE",
  "category": "KTD_SERVICE_ACCOUNT_MISSING_PERMISSIONS",
  "securityMarks": {
    "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/findings/FINDING_ID/securityMarks"
  },
  "eventTime": "2022-11-23T16:36:03.458107Z",
  "createTime": "2022-11-01T07:36:37.078Z",
  "severity": "CRITICAL",
  "canonicalName": "projects/742742027423/sources/SOURCE_ID/findings/FINDING_ID",
  "mute": "UNDEFINED",
  "findingClass": "SCC_ERROR",
  "access": {
    "callerIpGeo": {}
  },
  "contacts": {
    "security": {
      "contacts": [
        {
          "email": "test.user@domain.com"
        }
      ]
    },
    "technical": {
      "contacts": [
        {
          "email": "test.user@domain.com"
        }
      ]
    }
  },
  "parentDisplayName": "Security Command Center",
  "description": "Either all or some Container Threat Detection findings aren\\u0027t being sent to Security Command Center. A service account is missing permissions required for Container Threat Detection.",
  "iamBindings": [
    {
      "member": "test.user@domain.com"
    }
  ],
  "nextSteps": "Restore the required IAM roles on the Container Threat Detection service account. \\n1. Go to [IAM](/iam-admin/iam) \\n2. Select the service account: \\"test.user@domain.com\\" \\n   - If you don\\u0027t see the service account listed, click  **Add** at the top of the page and enter it as a new principal \\n3. Apply the following role:* \\n    1. Container Threat Detection Service Agent \\n4. Click **Save**. \\n \\n*If you use custom roles, apply these missing permissions: \\n - container.clusterRoleBindings.create,container.clusterRoleBindings.delete,container.clusterRoleBindings.update,container.clusterRoles.create,container.clusterRoles.delete,container.clusterRoles.escalate,container.clusterRoles.update,container.customResourceDefinitions.create,container.customResourceDefinitions.delete,container.customResourceDefinitions.update,container.daemonSets.create,container.daemonSets.delete,container.daemonSets.update,container.daemonSets.updateStatus,container.networkPolicies.update,container.pods.attach,container.pods.create,container.pods.delete,container.pods.exec,container.pods.getLogs,container.pods.portForward,container.pods.update,container.roleBindings.create,container.roleBindings.delete,container.roleBindings.update,container.roles.bind,container.roles.create,container.roles.delete,container.roles.escalate,container.roles.update,container.secrets.create,container.secrets.list,container.secrets.delete,container.secrets.update,container.serviceAccounts.create,container.serviceAccounts.delete,container.serviceAccounts.update"
}
GCP_SECURITYCENTER_UNSPECIFIED sample logs
JSON
{
  "findings": {
    "access": {},
    "canonicalName": "organizations/595779152576/sources/SOURCE_ID/findings/FINDING_ID",
    "category": "OPEN_FIREWALL",
    "compliances": [
      {
        "standard": "pci",
        "ids": [
          "1.2.1"
        ]
      }
    ],
    "contacts": {
      "security": {
        "contacts": [
          {
            "email": "test.user@dummy.xyz"
          }
        ]
      },
      "technical": {
        "contacts": [
          {
            "email": "test.user@dummy.xyz"
          }
        ]
      }
    },
    "createTime": "2021-07-20T08:33:25.343Z",
    "database": {},
    "eventTime": "2022-07-19T07:44:38.374Z",
    "exfiltration": {},
    "externalUri": "dummy.domain.com",
    "indicator": {},
    "kernelRootkit": {},
    "kubernetes": {},
    "mitreAttack": {},
    "mute": "MUTED",
    "muteInitiator": "Muted by test.user@dummy.xyz",
    "muteUpdateTime": "2022-03-08T05:41:06.507Z",
    "name": "organizations/595779152576/sources/SOURCE_ID/findings/FINDING_ID",
    "parent": "organizations/595779152576/sources/SOURCE_ID"
    "parentDisplayName": "Security Health Analytics",
    "resourceName": "//compute.googleapis.com/projects/calcium-vial-280707/global/firewalls/3199326669616479704",
    "severity": "HIGH",
    "sourceDisplayName": "Sanity_grc",
    "state": "ACTIVE",
    "vulnerability": {},
    "workflowState": "NEW"
  },
  "resource": {
    "name": "//compute.googleapis.com/projects/calcium-vial-280707/global/firewalls/3199326669616479704",
    "display_name": "",
    "project_name": "",
    "project_display_name": "",
    "parent_name": "",
    "parent_display_name": "",
    "type": "",
    "folders": []
  },
  "sourceProperties": {
    "ScannerName": "FIREWALL_SCANNER",
    "ResourcePath": [
      "projects/calcium-vial-280707/",
      "organizations/ORGANIZATION_ID/"
    ],
    "ReactivationCount": 0,
    "AllowedIpRange": "All",
    "ExternallyAccessibleProtocolsAndPorts": [
      {
        "IPProtocol": "tcp",
        "ports": [
          "80"
        ]
      }
    ]
  }
}
GCP_SECURITYCENTER_SENSITIVE_DATA_RISK sample logs
JSON
{
  "finding": {
    "name": "organizations/688851828130/sources/10254798010023864080/locations/global/findings/6CSKHYY",
    "parent": "organizations/688851828130/sources/10254798010023864080/locations/global",
    "resourceName": "//storage.googleapis.com/ci-sdw-ext-flx-ab8613-1501_cloudbuild",
    "state": "INACTIVE",
    "category": "SENSITIVE_DATA_BUCKET_CMEK_DISABLED",
    "externalUri": "",
    "sourceProperties": [],
    "securityMarks": {
      "name": "organizations/688851828130/sources/10254798010023864080/locations/global/findings/6CSKHYY/securityMarks",
      "marks": []
    },
    "eventTime": "2025-01-24T05:41:27.746Z",
    "createTime": "2024-12-31T18:31:18.956Z",
    "severity": "CRITICAL",
    "canonicalName": "projects/898485744945/sources/10254798010023864080/locations/global/findings/6CSKHYY",
    "mute": "UNDEFINED",
    "findingClass": "SENSITIVE_DATA_RISK",
    "launchState": "LAUNCH_STATE_GENERAL_AVAILABILITY",
    "indicator": {
      "ipAddresses": [],
      "domains": [],
      "signatures": [],
      "uris": []
    },
    "dataProtectionKeyGovernance": {
      "violations": []
    },
    "vertexAi": {
      "datasets": [],
      "pipelines": []
    },
    "muteUpdateTime": "1970-01-01T00:00:00Z",
    "muteInitiator": "",
    "muteInfo": {
      "staticMute": {
        "state": "UNDEFINED",
        "applyTime": "1970-01-01T00:00:00Z"
      },
      "dynamicMuteRecords": []
    },
    "contacts": [
      {
        "key": "security",
        "value": {
          "contacts": [
            {
              "email": "t1@test.com"
            },
            {
              "email": "t2@test.com"
            },
            {
              "email": "t3@test.com"
            },
            {
              "email": "t4@test.com"
            },
            {
              "email": "t5@gmail.com"
            },
            {
              "email": "t6@test.com"
            },
            {
              "email": "t7@test.com"
            },
            {
              "email": "t8@test.com"
            },
            {
              "email": "t9@test.com"
            }
          ]
        }
      },
      {
        "key": "technical",
        "value": {
          "contacts": [
            {
              "email": "j1@test.com"
            },
            {
              "email": "j2@test.com"
            },
            {
              "email": "j3@test.com"
            },
            {
              "email": "j4@test.com"
            }
          ]
        }
      }
    ],
    "externalSystems": [],
    "access": {
      "principalEmail": "",
      "callerIp": "",
      "callerIpGeo": {
          "regionCode": ""
      },
      "userAgent": "",
      "userAgentFamily": "",
      "serviceName": "",
      "methodName": "",
      "principalSubject": "",
      "serviceAccountKeyName": "",
      "serviceAccountDelegationInfo": [],
      "userName": ""
    },
    "mitreAttack": {
      "primaryTactic": "TACTIC_UNSPECIFIED",
      "primaryTechniques": [],
      "additionalTactics": [],
      "additionalTechniques": [],
      "version": ""
    },
    "description": "Data Security Posture Management (DSPM) system has detected that this resource has highly sensitive data and is not using CMEK for encryption. This poses a data security risk and requires immediate attention.",
    "compliances": [],
    "iamBindings": [],
    "nextSteps": "1. Follow the remediation steps for the related findings - \\n   - Bucket CMEK disabled finding \\n   - High Sensitive Data finding \\n2. Once any of the findings is resolved, this finding will automatically get resolved. \\n \\n For more detailed information, view the user guide.",
    "connections": [],
    "exfiltration": {
      "sources": [],
      "targets": [],
      "totalExfiltratedBytes": "0"
    },
    "processes": [],
    "containers": [],
    "kubernetes": {
      "pods": [],
      "nodes": [],
      "nodePools": [],
      "roles": [],
      "bindings": [],
      "accessReviews": [],
      "objects": []
    },
    "parentDisplayName": "Data Security Posture Management",
    "moduleName": "",
    "vulnerability": {
      "cve": {
          "id": "",
          "references": [],
          "cvssv3": {
              "baseScore": 0,
              "attackVector": "ATTACK_VECTOR_UNSPECIFIED",
              "attackComplexity": "ATTACK_COMPLEXITY_UNSPECIFIED",
              "privilegesRequired": "PRIVILEGES_REQUIRED_UNSPECIFIED",
              "userInteraction": "USER_INTERACTION_UNSPECIFIED",
              "scope": "SCOPE_UNSPECIFIED",
              "confidentialityImpact": "IMPACT_UNSPECIFIED",
              "integrityImpact": "IMPACT_UNSPECIFIED",
              "availabilityImpact": "IMPACT_UNSPECIFIED"
          },
          "upstreamFixAvailable": false,
          "impact": "RISK_RATING_UNSPECIFIED",
          "exploitationActivity": "EXPLOITATION_ACTIVITY_UNSPECIFIED",
          "observedInTheWild": false,
          "zeroDay": false,
          "exploitReleaseDate": "1970-01-01T00:00:00Z",
          "firstExploitationDate": "1970-01-01T00:00:00Z"
      },
      "offendingPackage": {
          "packageName": "",
          "cpeUri": "",
          "packageType": "",
          "packageVersion": ""
      },
      "fixedPackage": {
          "packageName": "",
          "cpeUri": "",
          "packageType": "",
          "packageVersion": ""
      },
      "securityBulletin": {
          "bulletinId": "",
          "submissionTime": "1970-01-01T00:00:00Z",
          "suggestedUpgradeVersion": ""
      }
    },
    "database": {
      "name": "",
      "displayName": "",
      "userName": "",
      "query": "",
      "grantees": [],
      "version": ""
    },
    "dataAccessEvents": [
      {
        "eventId": "da-event-12345abcdef",
        "principalEmail": "user@example.com",
        "operation": "READ",
        "eventTime": "2025-11-12T10:00:00Z"
      }
    ],
    "dataFlowEvents": [
      {
        "eventId": "df-event-67890fedcba",
        "principalEmail": "test@domain.com",
        "operation": "COPY",
        "violatedLocation": "US-EAST-4",
        "eventTime": "2025-11-12T11:30:00Z"
      }
    ],
    "dataRetentionDeletionEvents": [],
    "attackExposure": {
      "score": 0,
      "latestCalculationTime": "1970-01-01T00:00:00Z",
      "attackExposureResult": "",
      "state": "STATE_UNSPECIFIED",
      "exposedHighValueResourcesCount": 0,
      "exposedMediumValueResourcesCount": 0,
      "exposedLowValueResourcesCount": 0
    },
    "files": [],
    "orgPolicies": [],
    "ipRules": {
      "direction": "DIRECTION_UNSPECIFIED",
      "allowed": {
        "ipRules": []
      },
      "denied": {
        "ipRules": []
      },
      "sourceIpRanges": [],
      "destinationIpRanges": [],
      "exposedServices": []
    },
    "kernelRootkit": {
      "name": "",
      "unexpectedCodeModification": false,
      "unexpectedReadOnlyDataModification": false,
      "unexpectedFtraceHandler": false,
      "unexpectedKprobeHandler": false,
      "unexpectedKernelCodePages": false,
      "unexpectedSystemCallHandler": false,
      "unexpectedInterruptHandler": false,
      "unexpectedProcessesInRunqueue": false
    },
    "backupDisasterRecovery": {
      "backupTemplate": "",
      "policies": [],
      "host": "",
      "applications": [],
      "storagePool": "",
      "policyOptions": [],
      "profile": "",
      "appliance": "",
      "backupType": "",
      "backupCreateTime": "1970-01-01T00:00:00Z"
    },
    "apigee": {
      "organization": "",
      "environment": "",
      "securityProfileId": ""
    },
    "disk": {
      "name": ""
    },
    "risks": [],
    "loadBalancers": [],
    "deactivationReason": {
      "reason": "REASON_UNSPECIFIED"
    },
    "domains": [],
    "affectedResources": {
      "count": "0"
    },
    "aiModel": {
      "name": "",
      "domain": "",
      "library": "",
      "location": "",
      "publisher": "",
      "deploymentPlatform": "DEPLOYMENT_PLATFORM_UNSPECIFIED",
      "displayName": ""
    },
    "cloudDlpInspection": {
      "inspectJob": "",
      "infoType": "",
      "infoTypeCount": "0",
      "fullScan": false
    },
    "caiResource": "//storage.googleapis.com/ci-sdw-ext-flx-ab8613-1501_cloudbuild",
    "cloudDlpDataProfile": {
      "dataProfile": ""
    },
    "application": {
      "baseUri": "",
      "fullUri": ""
    },
    "securityPosture": {
      "name": "",
      "revisionId": "",
      "policyDriftDetails": [],
      "policySet": "",
      "postureDeploymentResource": "",
      "postureDeployment": "",
      "changedPolicy": ""
    },
    "logEntries": [],
    "cloudArmor": {
      "securityPolicy": {
        "name": "",
        "type": "",
        "preview": false
      },
      "requests": {
        "ratio": 0,
        "shortTermAllowed": 0,
        "longTermAllowed": 0,
        "longTermDenied": 0
      },
      "adaptiveProtection": {
        "confidence": 0
      },
      "attack": {
        "volumePps": 0,
        "volumeBps": 0,
        "classification": ""
      },
      "threatVector": "",
      "duration": "0s"
    },
    "notebook": {
      "name": "",
      "service": "",
      "lastAuthor": "",
      "notebookUpdateTime": "1970-01-01T00:00:00Z"
    },
    "toxicCombination": {
      "attackExposureScore": 0,
      "relatedFindings": []
    },
    "groupMemberships": [],
    "networks": [],
    "chokepoint": {
      "relatedFindings": []
    },
    "remediationDetails": {
      "remediationIntent": "",
      "repositoryUri": "",
      "pullRequestUri": "",
      "remediationExplanation": "",
      "remediationState": "REMEDIATION_STATE_UNSPECIFIED",
      "remediationError": "",
      "prGenerationTime": "1970-01-01T00:00:00Z",
      "owner": ""
    },
    "complianceDetails": {
      "frameworks": [],
      "cloudControl": {
        "cloudControlName": "",
        "type": "CLOUD_CONTROL_TYPE_UNSPECIFIED",
        "policyType": "",
        "version": 0
      },
      "cloudControlDeploymentNames": []
    }
  },
  "resource": {
    "name": "//storage.googleapis.com/ci-sdw-ext-flx-ab8613-1501_cloudbuild",
    "displayName": "ci-sdw-ext-flx-ab8613-1501_cloudbuild",
    "type": "google.cloud.storage.Bucket",
    "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
    "service": "storage.googleapis.com",
    "location": "us-central1",
    "gcpMetadata": {
      "project": "//cloudresourcemanager.googleapis.com/projects/898485744945",
      "projectDisplayName": "ci-sdw-ext-flx-ab8613-1501",
      "parent": "//cloudresourcemanager.googleapis.com/projects/898485744945",
      "parentDisplayName": "ci-sdw-ext-flx-ab8613-1501",
      "folders": [
        {
          "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/1001425801717",
          "resourceFolderDisplayName": "bug2"
        },
        {
          "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/82835227591",
          "resourceFolderDisplayName": "rohit"
        }
      ],
      "organization": "organizations/688851828130"
    },
    "awsMetadata": {
      "organization": {
        "id": ""
      },
      "organizationalUnits": [],
      "account": {
        "id": "",
        "name": ""
      }
    },
    "azureMetadata": {
      "tenant": {
        "id": "",
        "displayName": ""
      },
      "managementGroups": [],
      "subscription": {
        "id": "",
        "displayName": ""
      },
      "resourceGroup": {
        "name": ""
      }
    },
    "resourcePath": {
      "nodes": [
        {
          "nodeType": "GCP_PROJECT",
          "id": "projects/898485744945",
          "displayName": "ci-sdw-ext-flx-ab8613-1501"
        },
        {
          "nodeType": "GCP_FOLDER",
          "id": "folders/1001425801717",
          "displayName": "bug2"
        },
        {
          "nodeType": "GCP_FOLDER",
          "id": "folders/82835227591",
          "displayName": "rohit"
        },
        {
          "nodeType": "GCP_ORGANIZATION",
          "id": "organizations/688851828130",
          "displayName": ""
        }
      ]
    },
    "resourcePathString": "organizations/688851828130/folders/82835227591/folders/1001425801717/projects/898485744945",
    "application": {
      "name": ""
    }
  }
}
GCP_SECURITYCENTER_POSTURE_VIOLATION sample logs
JSON
{
    "finding": {
        "access": {},
        "application": {},
        "attackExposure": {},
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/locations/global/findings/FINDING_ID",
        "category": "SECURITY_POSTURE_POLICY_DELETE",
        "cloudDlpDataProfile": {},
        "cloudDlpInspection": {},
        "createTime": "2024-03-18T19:21:50.337Z",
        "database": {},
        "eventTime": "2024-03-18T19:21:46.269Z",
        "exfiltration": {},
        "findingClass": "POSTURE_VIOLATION",
        "indicator": {},
        "kernelRootkit": {},
        "kubernetes": {},
        "mitreAttack": {},
        "mute": "UNDEFINED",
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "parentDisplayName": "Security Posture",
        "resourceName": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "risks": [
            {
                "riskCategory": "AI_WORKLOAD_AT_RISK"
            }
        ],
        "securityPosture": {
            "name": "POSTURE_NAME",
            "revisionId": "REVISION_ID",
            "policySet": "POLICY_SET",
            "postureDeploymentResource": "projects/PROJECT_NUMBER",
            "postureDeployment": "POSTURE_DEPLOYMENT_ID",
            "changedPolicy": "//orgpolicy.googleapis.com/projects/PROJECT_NUMBER/policies/ainotebooks.accessMode"
        },
        "severity": "MEDIUM",
        "state": "ACTIVE",
        "vulnerability": {},
        "externalSystems": {}
    },
    "resource": {
        "name": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
        "displayName": "PROJECT_DISPLAY_NAME",
        "type": "google.cloud.resourcemanager.Project",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "cloudresourcemanager.googleapis.com",
        "gcpMetadata": {
            "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "projectDisplayName": "PROJECT_DISPLAY_NAME",
            "parent": "//cloudresourcemanager.googleapis.com/organizations/ORGANIZATION_ID",
            "parentDisplayName": "ORG_DISPLAY_NAME",
            "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
            "nodes": [
                {
                    "nodeType": "GCP_PROJECT",
                    "id": "projects/PROJECT_NUMBER",
                    "displayName": "PROJECT_DISPLAY_NAME"
                },
                {
                    "nodeType": "GCP_ORGANIZATION",
                    "id": "organizations/ORGANIZATION_ID"
                }
            ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_NUMBER"
    },
    "sourceProperties": {
        "posture_deployment_resource": "projects/PROJECT_NUMBER",
        "posture_deployment": "POSTURE_DEPLOYMENT_ID",
        "changed_policy": "//orgpolicy.googleapis.com/projects/PROJECT_NUMBER/policies/ainotebooks.accessMode",
        "categories": [
            "AI"
        ],
        "policy_drift_details": [],
        "name": "POSTURE_NAME",
        "revision_id": "REVISION_ID"
    }
}
GCP_SECURITYCENTER_TOXIC_COMBINATION sample logs
JSON
{
    "finding": {
        "name": "organizations/123456789012/sources/9876543210987654321/findings/abcdef1234567890abcdef1234567890",
        "parent": "organizations/123456789012/sources/9876543210987654321",
        "resourceName": "//cloudresourcemanager.googleapis.com/projects/987654321098",
        "state": "ACTIVE",
        "category": "SECURITY_POSTURE_DRIFT",
        "sourceProperties": {
            "posture_revision_id": "40034217",
            "policy_drift_details": [
                {
                    "drift_details": {
                        "expected_configuration": "[EXTERNAL]",
                        "detected_configuration": "[is:INTERNAL]"
                    },
                    "field_name": "constraint.implementation.policy_rules[0].allowed_values"
                }
            ],
            "changed_policy": "//orgpolicy.googleapis.com/projects/987654321098/policies/compute.restrictProtocolForwardingCreationForTypes",
            "posture_deployment_resource": "organizations/123456789012",
            "posture_name": "Posture-drift",
            "posture_deployment_name": "PD-drift"
        },
        "securityMarks": {
            "name": "organizations/123456789012/sources/9876543210987654321/findings/abcdef1234567890abcdef1234567890/securityMarks"
        },
        "eventTime": "2023-01-03T17:00:00Z",
        "createTime": "2023-10-06T13:41:17.198Z",
        "propertyDataTypes": {
            "policy_drift_details": {
                "listValues": {
                    "propertyDataTypes": [
                        {
                            "structValue": {
                                "fields": {
                                    "drift_details": {
                                        "structValue": {
                                            "fields": {
                                                "expected_configuration": {
                                                    "primitiveDataType": "STRING"
                                                },
                                                "detected_configuration": {
                                                    "primitiveDataType": "STRING"
                                                }
                                            }
                                        }
                                    },
                                    "field_name": {
                                        "primitiveDataType": "STRING"
                                    }
                                }
                            }
                        }
                    ]
                }
            },
            "changed_policy": {
                "primitiveDataType": "STRING"
            },
            "posture_revision_id": {
                "primitiveDataType": "STRING"
            },
            "posture_name": {
                "primitiveDataType": "STRING"
            },
            "posture_deployment_name": {
                "primitiveDataType": "STRING"
            },
            "posture_deployment_resource": {
                "primitiveDataType": "STRING"
            }
        },
        "severity": "MEDIUM",
        "workflowState": "NEW",
        "canonicalName": "projects/987654321098/sources/9876543210987654321/findings/abcdef1234567890abcdef1234567890",
        "mute": "UNDEFINED",
        "findingClass": "POSTURE_VIOLATION",
        "originalProviderId": "SECURITY_POSTURE",
        "parentDisplayName": "Security Posture",
        "securityPosture": {
            "name": "Posture-drift",
            "revisionId": "40034217",
            "postureDeploymentResource": "organizations/123456789012",
            "postureDeployment": "PD-drift",
            "changedPolicy": "//orgpolicy.googleapis.com/projects/987654321098/policies/compute.restrictProtocolForwardingCreationForTypes"
        },
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM"
    },
    "resource": {
        "name": "//cloudresourcemanager.googleapis.com/projects/987654321098",
        "project": "//cloudresourcemanager.googleapis.com/projects/987654321098",
        "projectDisplayName": "my-test-project",
        "parent": "//cloudresourcemanager.googleapis.com/folders/555666777888",
        "parentDisplayName": "DevEnvironment",
        "type": "google.cloud.resourcemanager.Project",
        "folders": [
            {
                "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/555666777888",
                "resourceFolderDisplayName": "DevEnvironment"
            },
            {
                "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/111222333444",
                "resourceFolderDisplayName": "TeamFolders"
            },
            {
                "resourceFolder": "//cloudresourcemanager.googleapis.com/folders/666777888999",
                "resourceFolderDisplayName": "RootFolder"
            }
        ],
        "displayName": "my-test-project",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "organization": "organizations/123456789012",
        "service": "cloudresourcemanager.googleapis.com",
        "resourcePath": {
            "nodes": [
                {
                    "nodeType": "GCP_PROJECT",
                    "id": "projects/987654321098",
                    "displayName": "my-test-project"
                },
                {
                    "nodeType": "GCP_FOLDER",
                    "id": "folders/555666777888",
                    "displayName": "DevEnvironment"
                },
                {
                    "nodeType": "GCP_FOLDER",
                    "id": "folders/111222333444",
                    "displayName": "TeamFolders"
                },
                {
                    "nodeType": "GCP_FOLDER",
                    "id": "folders/666777888999",
                    "displayName": "RootFolder"
                },
                {
                    "nodeType": "GCP_ORGANIZATION",
                    "id": "organizations/123456789012"
                }
            ]
        },
        "resourcePathString": "organizations/123456789012/folders/666777888999/folders/111222333444/folders/555666777888/projects/987654321098"
    }
}
GCP_SECURITYCENTER_CHOKEPOINT sample logs
JSON
{
    "finding": {
        "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global/findings/FINDING_ID",
        "canonicalName": "projects/PROJECT_NUMBER/sources/SOURCE_ID/locations/global/findings/FINDING_ID",
        "parent": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global",
        "resourceName": "//compute.googleapis.com/projects/PROJECT_ID/global/firewalls/FIREWALL_NAME",
        "state": "ACTIVE",
        "category": "Firewall that exposes many valued resources",
        "securityMarks": {
            "name": "organizations/ORGANIZATION_ID/sources/SOURCE_ID/locations/global/findings/FINDING_ID/securityMarks"
        },
        "eventTime": "2025-05-04T22:42:33.175Z",
        "createTime": "2025-03-12T19:48:59.485Z",
        "severity": "CRITICAL",
        "mute": "UNDEFINED",
        "findingClass": "CHOKEPOINT",
        "muteUpdateTime": "1970-01-01T00:00:00Z",
        "originalProviderId": "RISK_ENGINE",
        "parentDisplayName": "Risk Engine",
        "description": "An attacker who succeeds with Use Rule on the asset FIREWALL_NAME would benefit from that when targeting other assets as well. Therefore, mitigations applied to this asset are expected to have positive effects on the security posture of the environment in general as well.",
        "nextSteps": "When dealing with firewall rules that allow external ingress traffic in GCP.",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "muteInfo": {
            "staticMute": {
                "state": "UNDEFINED",
                "applyTime": "1970-01-01T00:00:00Z"
            }
        },
        "groupMemberships": [
            {
                "groupType": "GROUP_TYPE_CHOKEPOINT",
                "groupId": "FINDING_ID"
            }
        ],
        "domains": [
            {
                "category": "DATA"
            },
            {
                "category": "IDENTITY_AND_ACCESS"
            }
        ],
        "chokepoint": {
            "relatedFindings": [
                "organizations/ORGANIZATION_ID/sources/RELATED_SOURCE_ID/locations/global/findings/RELATED_FINDING_ID"
            ]
        }
    },
    "resource": {
        "name": "//compute.googleapis.com/projects/PROJECT_ID/global/firewalls/FIREWALL_NAME",
        "displayName": "FIREWALL_NAME",
        "type": "google.compute.Firewall",
        "cloudProvider": "GOOGLE_CLOUD_PLATFORM",
        "service": "compute.googleapis.com",
        "location": "global",
        "gcpMetadata": {
            "project": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "projectDisplayName": "PROJECT_ID",
            "parent": "//cloudresourcemanager.googleapis.com/projects/PROJECT_NUMBER",
            "parentDisplayName": "PROJECT_ID",
            "organization": "organizations/ORGANIZATION_ID"
        },
        "resourcePath": {
            "nodes": [
                {
                    "nodeType": "GCP_PROJECT",
                    "id": "projects/PROJECT_NUMBER",
                    "displayName": "PROJECT_ID"
                },
                {
                    "nodeType": "GCP_ORGANIZATION",
                    "id": "organizations/ORGANIZATION_ID"
                }
            ]
        },
        "resourcePathString": "organizations/ORGANIZATION_ID/projects/PROJECT_NUMBER"
    }
}
Field mapping reference
This section explains how the Google Security Operations parser maps Security Command Center log fields to Google Security Operations Unified Data Model (UDM) fields for the data sets.
Field mapping reference: raw log fields to UDM fields
The following table lists the log fields and corresponding UDM mappings for the Security Command Center Event Threat Detection findings.
RawLog field
UDM mapping
Logic
compliances.ids
about.labels [compliance_ids]
(deprecated)
compliances.ids
additional.fields [compliance_ids]
compliances.version
about.labels [compliance_version]
(deprecated)
compliances.version
additional.fields [compliance_version]
compliances.standard
about.labels [compliances_standard]
(deprecated)
compliances.standard
additional.fields [compliances_standard]
connections.destinationIp
about.labels [connections_destination_ip]
(deprecated)
If the
connections.destinationIp
log field value is
not
equal to the
sourceProperties.properties.ipConnection.destIp
, then the
connections.destinationIp
log field is mapped to the
about.labels.value
UDM field.
connections.destinationIp
additional.fields [connections_destination_ip]
If the
connections.destinationIp
log field value is
not
equal to the
sourceProperties.properties.ipConnection.destIp
, then the
connections.destinationIp
log field is mapped to the
additional.fields.value.string_value
UDM field.
connections.destinationPort
about.labels [connections_destination_port]
(deprecated)
connections.destinationPort
additional.fields [connections_destination_port]
connections.protocol
about.labels [connections_protocol]
(deprecated)
connections.protocol
additional.fields [connections_protocol]
connections.sourceIp
about.labels [connections_source_ip]
(deprecated)
connections.sourceIp
additional.fields [connections_source_ip]
connections.sourcePort
about.labels [connections_source_port]
(deprecated)
connections.sourcePort
additional.fields [connections_source_port]
kubernetes.pods.ns
target.resource.attribute.labels[kubernetes_pods_ns]
kubernetes.pods.name
target.resource.attribute.labels[kubernetes_pods_name]
kubernetes.nodes.name
target.resource.attribute.labels[kubernetes_nodes_name]
kubernetes.nodePools.name
target.resource.attribute.labels[kubernetes_nodePools_name]
about.resource.attribute.cloud.environment
The
about.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
externalSystems.assignees
additional.fields[externalSystems_assignees]
externalSystems.status
about.resource.attribute.labels.key/value [externalSystems_status]
kubernetes.nodePools.nodes.name
target.resource.attribute.labels.key/value [kubernetes_nodePools_nodes_name]
kubernetes.pods.containers.uri
target.resource.attribute.labels.key/value [kubernetes_pods_containers_uri]
kubernetes.pods.containers.createTime
target.resource.attribute.labels[kubernetes_pods_containers_createTime]
kubernetes.roles.kind
target.resource.attribute.labels.key/value [kubernetes_roles_kind]
kubernetes.roles.name
target.resource.attribute.labels.key/value [kubernetes_roles_name]
kubernetes.roles.ns
target.resource.attribute.labels.key/value [kubernetes_roles_ns]
kubernetes.pods.containers.labels.name/value
target.resource.attribute.labels.key/value [kubernetes.pods.containers.labels.name/value]
kubernetes.pods.labels.name/value
target.resource.attribute.labels.key/value [kubernetes.pods.labels.name/value]
externalSystems.externalSystemUpdateTime
about.resource.attribute.last_update_time
externalSystems.name
about.resource.name
externalSystems.externalUid
about.resource.product_object_id
indicator.uris
security_result.detection_fields[indicator_uri]
extension.auth.type
If the
category
log field value is equal to
Initial Access: Account Disabled Hijacked
or
Initial Access: Disabled Password Leak
or
Initial Access: Government Based Attack
or
Initial Access: Suspicious Login Blocked
or
Impair Defenses: Two Step Verification Disabled
or
Persistence: SSO Enablement Toggle
, then the
extension.auth.type
UDM field is set to
SSO
.
extension.mechanism
If the
category
log field value is equal to
Brute Force: SSH
, then the
extension.mechanism
UDM field is set to
USERNAME_PASSWORD
.
extensions.auth.type
If the
principal.user.user_authentication_status
log field value is equal to
ACTIVE
, then the
extensions.auth.type
UDM field is set to
SSO
.
vulnerability.cve.references.uri
extensions.vulns.vulnerabilities.about.labels [vulnerability.cve.references.uri]
(deprecated)
vulnerability.cve.references.uri
additional.fields [vulnerability.cve.references.uri]
vulnerability.cve.cvssv3.attackComplexity
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_attackComplexity]
(deprecated)
vulnerability.cve.cvssv3.attackComplexity
additional.fields [vulnerability_cve_cvssv3_attackComplexity]
vulnerability.cve.cvssv3.availabilityImpact
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_availabilityImpact]
(deprecated)
vulnerability.cve.cvssv3.availabilityImpact
additional.fields [vulnerability_cve_cvssv3_availabilityImpact]
vulnerability.cve.cvssv3.confidentialityImpact
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_confidentialityImpact]
(deprecated)
vulnerability.cve.cvssv3.confidentialityImpact
additional.fields [vulnerability_cve_cvssv3_confidentialityImpact]
vulnerability.cve.cvssv3.integrityImpact
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_integrityImpact]
(deprecated)
vulnerability.cve.cvssv3.integrityImpact
additional.fields [vulnerability_cve_cvssv3_integrityImpact]
vulnerability.cve.cvssv3.privilegesRequired
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_privilegesRequired]
(deprecated)
vulnerability.cve.cvssv3.privilegesRequired
additional.fields [vulnerability_cve_cvssv3_privilegesRequired]
vulnerability.cve.cvssv3.scope
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_scope]
(deprecated)
vulnerability.cve.cvssv3.scope
additional.fields [vulnerability_cve_cvssv3_scope]
vulnerability.cve.cvssv3.userInteraction
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_userInteraction]
(deprecated)
vulnerability.cve.cvssv3.userInteraction
additional.fields [vulnerability_cve_cvssv3_userInteraction]
vulnerability.cve.references.source
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_references_source]
(deprecated)
vulnerability.cve.references.source
additional.fields [vulnerability_cve_references_source]
vulnerability.cve.upstreamFixAvailable
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_upstreamFixAvailable]
(deprecated)
vulnerability.cve.upstreamFixAvailable
additional.fields [vulnerability_cve_upstreamFixAvailable]
vulnerability.cve.id
extensions.vulns.vulnerabilities.cve_id
vulnerability.cve.cvssv3.baseScore
extensions.vulns.vulnerabilities.cvss_base_score
vulnerability.cve.cvssv3.attackVector
extensions.vulns.vulnerabilities.cvss_vector
sourceProperties.properties.loadBalancerName
intermediary.resource.name
If the
category
log field value is equal to
Initial Access: Log4j Compromise Attempt
, then the
sourceProperties.properties.loadBalancerName
log field is mapped to the
intermediary.resource.name
UDM field.
intermediary.resource.resource_type
If the
category
log field value is equal to
Initial Access: Log4j Compromise Attempt
, then the
intermediary.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
parentDisplayName
metadata.description
eventTime
metadata.event_timestamp
category
metadata.product_event_type
sourceProperties.evidence.sourceLogId.insertId
metadata.product_log_id
If the
canonicalName
log field value is
not
empty, then the
finding_id
is extracted from the
canonicalName
log field using a Grok pattern.
If the
finding_id
log field value is empty, then the
sourceProperties.evidence.sourceLogId.insertId
log field is mapped to the
metadata.product_log_id
UDM field.
If the
canonicalName
log field value is empty, then the
sourceProperties.evidence.sourceLogId.insertId
log field is mapped to the
metadata.product_log_id
UDM field.
metadata.product_name
The
metadata.product_name
UDM field is set to
Security Command Center
.
sourceProperties.contextUris.cloudLoggingQueryUri.url
security_result.detection_fields.key/value[sourceProperties_contextUris_cloudLoggingQueryUri_url]
metadata.vendor_name
The
metadata.vendor_name
UDM field is set to
Google
.
network.application_protocol
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
, then the
network.application_protocol
UDM field is set to
DNS
.
sourceProperties.properties.indicatorContext.asn
network.asn
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
, then the
sourceProperties.properties.indicatorContext.asn
log field is mapped to the
network.asn
UDM field.
sourceProperties.properties.indicatorContext.carrierName
network.carrier_name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
, then the
sourceProperties.properties.indicatorContext.carrierName
log field is mapped to the
network.carrier_name
UDM field.
sourceProperties.properties.indicatorContext.reverseDnsDomain
network.dns_domain
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.indicatorContext.reverseDnsDomain
log field is mapped to the
network.dns_domain
UDM field.
sourceProperties.properties.dnsContexts.responseData.responseClass
network.dns.answers.class
If the
category
log field value is equal to
Malware: Bad Domain
, then the
sourceProperties.properties.dnsContexts.responseData.responseClass
log field is mapped to the
network.dns.answers.class
UDM field.
sourceProperties.properties.dnsContexts.responseData.responseValue
network.dns.answers.data
If the
category
log field value matches the regular expression
Malware: Bad Domain
, then the
sourceProperties.properties.dnsContexts.responseData.responseValue
log field is mapped to the
network.dns.answers.data
UDM field.
sourceProperties.properties.dnsContexts.responseData.domainName
network.dns.answers.name
If the
category
log field value is equal to
Malware: Bad Domain
, then the
sourceProperties.properties.dnsContexts.responseData.domainName
log field is mapped to the
network.dns.answers.name
UDM field.
sourceProperties.properties.dnsContexts.responseData.ttl
network.dns.answers.ttl
If the
category
log field value is equal to
Malware: Bad Domain
, then the
sourceProperties.properties.dnsContexts.responseData.ttl
log field is mapped to the
network.dns.answers.ttl
UDM field.
sourceProperties.properties.dnsContexts.responseData.responseType
network.dns.answers.type
If the
category
log field value is equal to
Malware: Bad Domain
, then the
sourceProperties.properties.dnsContexts.responseData.responseType
log field is mapped to the
network.dns.answers.type
UDM field.
sourceProperties.properties.dnsContexts.authAnswer
network.dns.authoritative
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
, then the
sourceProperties.properties.dnsContexts.authAnswer
log field is mapped to the
network.dns.authoritative
UDM field.
sourceProperties.properties.dnsContexts.queryName
network.dns.questions.name
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
, then the
sourceProperties.properties.dnsContexts.queryName
log field is mapped to the
network.dns.questions.name
UDM field.
sourceProperties.properties.dnsContexts.queryType
network.dns.questions.type
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
, then the
sourceProperties.properties.dnsContexts.queryType
log field is mapped to the
network.dns.questions.type
UDM field.
sourceProperties.properties.dnsContexts.responseCode
network.dns.response_code
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
, then the
sourceProperties.properties.dnsContexts.responseCode
log field is mapped to the
network.dns.response_code
UDM field.
sourceProperties.properties.anomalousSoftware.callerUserAgent
network.http.user_agent
If the
category
log field value is equal to
Persistence: New User Agent
, then the
sourceProperties.properties.anomalousSoftware.callerUserAgent
log field is mapped to the
network.http.user_agent
UDM field.
sourceProperties.properties.callerUserAgent
network.http.user_agent
If the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.callerUserAgent
log field is mapped to the
network.http.user_agent
UDM field.
access.userAgentFamily
network.http.user_agent
finding.access.userAgent
network.http.user_agent
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.rawUserAgent
network.http.user_agent
If the
category
log field value is equal to
Discovery: Service Account Self-Investigation
, then the
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.rawUserAgent
log field is mapped to the
network.http.user_agent
UDM field.
sourceProperties.properties.ipConnection.protocol
network.ip_protocol
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Outgoing DoS
, then the
network.ip_protocol
UDM field is set to one of the following values:
ICMP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
1
or
ICMP
.
IGMP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
2
or
IGMP
.
TCP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
6
or
TCP
.
UDP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
17
or
UDP
.
IP6IN4
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
41
or
IP6IN4
.
GRE
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
47
or
GRE
.
ESP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
50
or
ESP
.
EIGRP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
88
or
EIGRP
.
ETHERIP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
97
or
ETHERIP
.
PIM
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
103
or
PIM
.
VRRP
when the following condition are met:
The
sourceProperties.properties.ipConnection.protocol
log field value is equal to
112
or
VRRP
.
UNKNOWN_IP_PROTOCOL
if the
sourceProperties.properties.ipConnection.protocol
log field value is equal to any other value.
sourceProperties.properties.indicatorContext.organizationName
network.organization_name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.indicatorContext.organizationName
log field is mapped to the
network.organization_name
UDM field.
sourceProperties.properties.anomalousSoftware.behaviorPeriod
network.session_duration
If the
category
log field value is equal to
Persistence: New User Agent
, then the
sourceProperties.properties.anomalousSoftware.behaviorPeriod
log field is mapped to the
network.session_duration
UDM field.
sourceProperties.properties.sourceIp
principal.ip
If the
category
log field value matches the regular expression
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.sourceIp
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.attempts.sourceIp
principal.ip
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.sourceIp
log field is mapped to the
principal.ip
UDM field.
access.callerIp
principal.ip
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
or
access.callerIp
or
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: CloudSQL Restore Backup to External Organization
or
Persistence: New Geography
or
Persistence: IAM Anomalous Grant
, then the
access.callerIp
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.callerIp
principal.ip
If the
category
log field value is equal to
Discovery: Service Account Self-Investigation
, then the
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.callerIp
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.changeFromBadIp.ip
principal.ip
If the
category
log field value is equal to
Evasion: Access from Anonymizing Proxy
, then the
sourceProperties.properties.changeFromBadIp.ip
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.dnsContexts.sourceIp
principal.ip
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
, then the
sourceProperties.properties.dnsContexts.sourceIp
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.ipConnection.srcIp
principal.ip
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Outgoing DoS
, then the
sourceProperties.properties.ipConnection.srcIp
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.callerIp sourceProperties.properties.indicatorContext.ipAddress
principal.ip
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then if the
sourceProperties.properties.ipConnection.srcIp
log field value is
not
equal to the
sourceProperties.properties.indicatorContext.ipAddress
, then the
sourceProperties.properties.indicatorContext.ipAddress
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.anomalousLocation.callerIp
principal.ip
If the
category
log field value is equal to
Persistence: New Geography
, then the
sourceProperties.properties.anomalousLocation.callerIp
log field is mapped to the
principal.ip
UDM field.
sourceProperties.properties.scannerDomain
additional.fields [sourceProperties_properties_scannerDomain]
If the
category
log field value matches the regular expression
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.scannerDomain
log field is mapped to the
additional.fields.value.string_value
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.jobState
principal.labels [sourceProperties.properties.dataExfiltrationAttempt.jobState]
(deprecated)
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.jobState
log field is mapped to the
principal.labels.key/value
and UDM field.
sourceProperties.properties.dataExfiltrationAttempt.jobState
additional.fields [sourceProperties.properties.dataExfiltrationAttempt.jobState]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.jobState
log field is mapped to the
additional.fields.value.string_value
UDM field.
access.callerIpGeo.regionCode
principal.location.country_or_region
sourceProperties.properties.indicatorContext.countryCode
principal.location.country_or_region
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.indicatorContext.countryCode
log field is mapped to the
principal.location.country_or_region
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.job.location
principal.location.country_or_region
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.job.location
log field is mapped to the
principal.location.country_or_region
UDM field.
sourceProperties.properties.extractionAttempt.job.location
principal.location.country_or_region
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.job.location
log field is mapped to the
principal.location.country_or_region
UDM field.
sourceProperties.properties.anomalousLocation.typicalGeolocations.country.identifier
principal.location.country_or_region
If the
category
log field value is equal to
Persistence: New Geography
or
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.anomalousLocation.typicalGeolocations.country.identifier
log field is mapped to the
principal.location.country_or_region
UDM field.
sourceProperties.properties.anomalousLocation.anomalousLocation
principal.location.name
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.anomalousLocation.anomalousLocation
log field is mapped to the
principal.location.name
UDM field.
sourceProperties.properties.ipConnection.srcPort
principal.port
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Outgoing DoS
, then the
sourceProperties.properties.ipConnection.srcPort
log field is mapped to the
principal.port
UDM field.
sourceProperties.properties.extractionAttempt.jobLink
target.url
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.jobLink
log field is mapped to the
target.url
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.jobLink
target.url
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.jobLink
log field is mapped to the
target.url
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.job.jobId
additional.fields[properties_dataExfiltrationAttempt_job_jobId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.job.jobId
log field is mapped to the
additional.fields[properties_dataExfiltrationAttempt_job_jobId]
UDM field.
sourceProperties.properties.extractionAttempt.job.jobId
additional.fields[properties_dataExfiltrationAttempt_job_jobId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.job.jobId
log field is mapped to the
additional.fields[properties_dataExfiltrationAttempt_job_jobId]
UDM field.
sourceProperties.properties.srcVpc.subnetworkName
principal.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_destVpc_subnetworkName]
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.srcVpc.subnetworkName
log field is mapped to the
principal.resource_ancestors.attribute.labels.value
UDM field.
principal.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_srcVpc_projectId]
principal.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_srcVpc_projectId]
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.srcVpc.projectId
log field is mapped to the
principal.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.srcVpc.vpcName
principal.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
principal.resource_ancestors.name
UDM field and the
principal.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
sourceProperties.sourceId.customerOrganizationNumber
principal.resource.attribute.labels.key/value [sourceProperties_sourceId_customerOrganizationNumber]
If the
message
log field value matches the regular expression
sourceProperties.sourceId.*?customerOrganizationNumber
, then the
sourceProperties.sourceId.customerOrganizationNumber
log field is mapped to the
principal.resource.attribute.labels.key/value
UDM field.
resource.projectName
principal.resource.name
sourceProperties.properties.projectId
principal.resource.name
If the
sourceProperties.properties.projectId
log field value is
not
empty, then the
sourceProperties.properties.projectId
log field is mapped to the
principal.resource.name
UDM field.
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.projectId
principal.resource.name
If the
category
log field value is equal to
Discovery: Service Account Self-Investigation
, then the
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.projectId
log field is mapped to the
principal.resource.name
UDM field.
sourceProperties.properties.sourceInstanceDetails
principal.resource.name
If the
category
log field value is equal to
Malware: Outgoing DoS
, then the
sourceProperties.properties.sourceInstanceDetails
log field is mapped to the
principal.resource.name
UDM field.
principal.user.account_type
If the
access.principalSubject
log field value matches the regular expression
serviceAccount
, then the
principal.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
Else if, the
access.principalSubject
log field value matches the regular expression
user
, then the
principal.user.account_type
UDM field is set to
CLOUD_ACCOUNT_TYPE
.
access.principalSubject
principal.user.attribute.labels.key/value [access_principalSubject]
access.serviceAccountDelegationInfo.principalSubject
principal.user.attribute.labels.key/value [access_serviceAccountDelegationInfo_principalSubject]
access.serviceAccountKeyName
principal.user.attribute.labels.key/value [access_serviceAccountKeyName]
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.callerUserAgent
additional.fields[sourceProperties_properties_serviceAccountGetsOwnIamPolicy_callerUserAgent]
If the
category
log field value is equal to
Discovery: Service Account Self-Investigation
, then the
principal.user.attribute.labels.key
UDM field is set to
rawUserAgent
and the
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.callerUserAgent
log field is mapped to the
additional.fields
UDM field.
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Discovery: Service Account Self-Investigation
, then the
sourceProperties.properties.serviceAccountGetsOwnIamPolicy.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.changeFromBadIp.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Evasion: Access from Anonymizing Proxy
, then the
sourceProperties.properties.changeFromBadIp.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.userEmail
principal.user.email_addresses
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.userEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
or
Initial Access: Account Disabled Hijacked
or
Initial Access: Disabled Password Leak
or
Initial Access: Government Based Attack
or
Impair Defenses: Strong Authentication Disabled
or
Impair Defenses: Two Step Verification Disabled
or
Persistence: GCE Admin Added Startup Script
or
Persistence: GCE Admin Added SSH Key
, then the
sourceProperties.properties.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
If the
category
log field value is equal to
Initial Access: Suspicious Login Blocked
, then the
sourceProperties.properties.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
access.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
or
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: CloudSQL Restore Backup to External Organization
or
Persistence: New Geography
, then the
access.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.sensitiveRoleGrant.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.sensitiveRoleGrant.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.anomalousSoftware.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Persistence: New User Agent
, then the
sourceProperties.properties.anomalousSoftware.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.exportToGcs.principalEmail
principal.user.email_addresses
sourceProperties.properties.restoreToExternalInstance.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
access.serviceAccountDelegationInfo.principalEmail
principal.user.email_addresses
sourceProperties.properties.customRoleSensitivePermissions.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.customRoleSensitivePermissions.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.anomalousLocation.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Persistence: New Geography
, then the
sourceProperties.properties.anomalousLocation.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Credential Access: External Member Added To Privileged Group
, then the
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.privilegedGroupOpenedToPublic.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Credential Access: Privileged Group Opened To Public
, then the
sourceProperties.properties.privilegedGroupOpenedToPublic.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.sensitiveRoleToHybridGroup.principalEmail
principal.user.email_addresses
If the
category
log field value is equal to
Credential Access: Sensitive Role Granted To Hybrid Group
, then the
sourceProperties.properties.sensitiveRoleToHybridGroup.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.vpcViolation.userEmail
principal.user.email_addresses
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.vpcViolation.userEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
sourceProperties.properties.ssoState
principal.user.user_authentication_status
If the
category
log field value is equal to
Initial Access: Account Disabled Hijacked
or
Initial Access: Disabled Password Leak
or
Initial Access: Government Based Attack
or
Initial Access: Suspicious Login Blocked
or
Impair Defenses: Two Step Verification Disabled
or
Persistence: SSO Enablement Toggle
, then the
sourceProperties.properties.ssoState
log field is mapped to the
principal.user.user_authentication_status
UDM field.
database.userName
principal.user.userid
If the
category
log field value is equal to
Exfiltration: CloudSQL Over-Privileged Grant
, then the
database.userName
log field is mapped to the
principal.user.userid
UDM field.
sourceProperties.properties.threatIntelligenceSource
security_result.threat_feed_name
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.threatIntelligenceSource
log field is mapped to the
security_result.threat_feed_name
UDM field.
workflowState
security_result.about.investigation.status
sourceProperties.properties.attempts.sourceIp
security_result.about.ip
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.sourceIp
log field is mapped to the
security_result.about.ip
UDM field.
sourceProperties.findingId
metadata.product_log_id
kubernetes.accessReviews.group
target.resource.attribute.labels.key/value [kubernetes_accessReviews_group]
kubernetes.accessReviews.name
target.resource.attribute.labels.key/value [kubernetes_accessReviews_name]
kubernetes.accessReviews.ns
target.resource.attribute.labels.key/value [kubernetes_accessReviews_ns]
kubernetes.accessReviews.resource
target.resource.attribute.labels.key/value [kubernetes_accessReviews_resource]
kubernetes.accessReviews.subresource
target.resource.attribute.labels.key/value [kubernetes_accessReviews_subresource]
kubernetes.accessReviews.verb
target.resource.attribute.labels.key/value [kubernetes_accessReviews_verb]
kubernetes.accessReviews.version
target.resource.attribute.labels.key/value [kubernetes_accessReviews_version]
kubernetes.bindings.name
target.resource.attribute.labels.key/value [kubernetes_bindings_name]
kubernetes.bindings.ns
target.resource.attribute.labels.key/value [kubernetes_bindings_ns]
kubernetes.bindings.role.kind
target.resource.attribute.labels.key/value [kubernetes_bindings_role_kind]
kubernetes.bindings.role.ns
target.resource.attribute.labels.key/value [kubernetes_bindings_role_ns]
kubernetes.bindings.subjects.kind
target.resource.attribute.labels.key/value [kubernetes_bindings_subjects_kind]
kubernetes.bindings.subjects.name
target.resource.attribute.labels.key/value [kubernetes_bindings_subjects_name]
kubernetes.bindings.subjects.ns
target.resource.attribute.labels.key/value [kubernetes_bindings_subjects_ns]
kubernetes.bindings.role.name
target.resource.attribute.roles.name
sourceProperties.properties.delta.restrictedResources.resourceName
security_result.about.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
Restricted Resource: sourceProperties.properties.delta.restrictedResources.resourceName
log field is mapped to the
security_result.about.resource.name
UDM field.
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.delta.restrictedResources.resourceName
log field is mapped to the
security_result.about.resource.name
UDM field and the
security_result.about.resource_type
UDM field is set to
CLOUD_PROJECT
.
sourceProperties.properties.delta.allowedServices.serviceName
security_result.about.resource.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.delta.allowedServices.serviceName
log field is mapped to the
security_result.about.resource.name
UDM field and the
security_result.about.resource_type
UDM field is set to
BACKEND_SERVICE
.
sourceProperties.properties.delta.restrictedServices.serviceName
security_result.about.resource.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.delta.restrictedServices.serviceName
log field is mapped to the
security_result.about.resource.name
UDM field and the
security_result.about.resource_type
UDM field is set to
BACKEND_SERVICE
.
sourceProperties.properties.delta.accessLevels.policyName
security_result.about.resource.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.delta.accessLevels.policyName
log field is mapped to the
security_result.about.resource.name
UDM field and the
security_result.about.resource_type
UDM field is set to
ACCESS_POLICY
.
security_result.about.user.attribute.roles.name
If the
message
log field value matches the regular expression
contacts.?security
, then the
security_result.about.user.attribute.roles.name
UDM field is set to
security
.
If the
message
log field value matches the regular expression
contacts.?technical
, then the
security_result.about.user.attribute.roles.name
UDM field is set to
Technical
.
contacts.security.contacts.email
security_result.about.user.email_addresses
contacts.technical.contacts.email
security_result.about.user.email_addresses
security_result.action
If the
category
log field value is equal to
Initial Access: Suspicious Login Blocked
, then the
security_result.action
UDM field is set to
BLOCK
.
If the
category
log field value is equal to
Brute Force: SSH
, then if the
sourceProperties.properties.attempts.authResult
log field value is equal to
SUCCESS
, then the
security_result.action
UDM field is set to
BLOCK
.
Else, the
security_result.action
UDM field is set to
BLOCK
.
sourceProperties.properties.delta.restrictedResources.action
security_result.action_details
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.delta.restrictedResources.action
log field is mapped to the
security_result.action_details
UDM field.
sourceProperties.properties.delta.restrictedServices.action
security_result.action_details
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.delta.restrictedServices.action
log field is mapped to the
security_result.action_details
UDM field.
sourceProperties.properties.delta.allowedServices.action
security_result.action_details
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.delta.allowedServices.action
log field is mapped to the
security_result.action_details
UDM field.
sourceProperties.properties.delta.accessLevels.action
security_result.action_details
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.delta.accessLevels.action
log field is mapped to the
security_result.action_details
UDM field.
security_result.alert_state
If the
state
log field value is equal to
ACTIVE
, then the
security_result.alert_state
UDM field is set to
ALERTING
.
Else, the
security_result.alert_state
UDM field is set to
NOT_ALERTING
.
findingClass
security_result.catgory_details
The
findingClass - category
log field is mapped to the
security_result.catgory_details
UDM field.
category
security_result.catgory_details
The
findingClass - category
log field is mapped to the
security_result.catgory_details
UDM field.
description
security_result.description
indicator.signatures.memoryHashSignature.binaryFamily
security_result.detection_fields.key/value [indicator_signatures_memoryHashSignature_binaryFamily]
indicator.signatures.memoryHashSignature.detections.binary
security_result.detection_fields.key/value [indicator_signatures_memoryHashSignature_detections_binary]
indicator.signatures.memoryHashSignature.detections.percentPagesMatched
security_result.detection_fields.key/value [indicator_signatures_memoryHashSignature_detections_percentPagesMatched]
indicator.signatures.yaraRuleSignature.yararule
security_result.detection_fields.key/value [indicator_signatures_yaraRuleSignature_yararule]
mitreAttack.additionalTactics
security_result.attack_details.tactics.name
mitreAttack.additionalTechniques
security_result.attack_details.techniques.name
mitreAttack.primaryTactic
security_result.attack_details.tactics.name
mitreAttack.primaryTechniques.0
security_result.attack_details.techniques.name
mitreAttack.version
security_result.attack_details.version
muteInitiator
security_result.detection_fields.key/value [mute_initiator]
If the
mute
log field value is equal to
MUTED
or
UNMUTED
, then the
muteInitiator
log field is mapped to the
security_result.detection_fields.value
UDM field.
muteUpdateTime
security_result.detection_fields.key/value [mute_update_time]
If the
mute
log field value is equal to
MUTED
or
UNMUTED
, then the
muteUpdateTimer
log field is mapped to the
security_result.detection_fields.value
UDM field.
mute
security_result.detection_fields.key/value [mute]
securityMarks.canonicalName
security_result.detection_fields.key/value [securityMarks_cannonicleName]
securityMarks.marks
security_result.detection_fields.key/value [securityMarks_marks]
securityMarks.name
security_result.detection_fields.key/value [securityMarks_name]
sourceProperties.detectionCategory.indicator
security_result.detection_fields.key/value [sourceProperties_detectionCategory_indicator]
sourceProperties.detectionCategory.technique
security_result.detection_fields.key/value [sourceProperties_detectionCategory_technique]
sourceProperties.properties.anomalousSoftware.anomalousSoftwareClassification
security_result.detection_fields.key/value [sourceProperties_properties_anomalousSoftware_anomalousSoftwareClassification]
If the
category
log field value is equal to
Persistence: New User Agent
, then the
sourceProperties.properties.anomalousSoftware.anomalousSoftwareClassification
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.attempts.authResult
security_result.detection_fields.key/value [sourceProperties_properties_attempts_authResult]
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.authResult
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.indicator.indicatorType
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_indicator_indicatorType]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.indicator.indicatorType
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.indicator.lastSeenTsGlobal
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_indicator_lastSeenTsGlobal]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.indicator.lastSeenTsGlobal
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.indicator.summaryGenerationTs
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_indicator_summaryGenerationTs]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.indicator.summaryGenerationTs
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.customer_industry
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_customer_industry]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.customer_industry
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.customer_name
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_customer_name]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.customer_name
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.lasthit
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_lasthit]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.lasthit
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.myVote
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_myVote]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.tag_definition_scope_id
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.source
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_source]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.myVote
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.support_id
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_support_id]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.support_id
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.tag_class_id
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_tag_class_id]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.tag_class_id
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.tag_definition_id
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_tag_definition_id]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.tag_definition_id
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.tag_definition_scope_id
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_tag_definition_scope_id]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.tag_definition_scope_id
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.tag_definition_status_id
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_tag_definition_status_id]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.tag_definition_status_id
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.tag_name
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_tag_name]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.tag_name
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.upVotes
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tags_upVotes]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.upVotes
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.properties.autofocusContextCards.tags.downVotes
security_result.detection_fields.key/value [sourceProperties_properties_autofocusContextCards_tagsdownVotes]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.downVotes
log field is mapped to the
security_result.detection_fields.value
UDM field.
sourceProperties.contextUris.mitreUri.url
security_result.detection_fields[sourceProperties_contextUris_mitreUri_url]
sourceProperties.contextUris.mitreUri.displayName
security_result.detection_fields[sourceProperties_contextUris_mitreUri_displayName]
sourceProperties.contextUris.relatedFindingUri.url
security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_url]
sourceProperties.contextUris.relatedFindingUri.displayName
security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_displayName]
sourceProperties.contextUris.virustotalIndicatorQueryUri.url
security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_url]
sourceProperties.contextUris.virustotalIndicatorQueryUri.displayName
security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_displayName]
sourceProperties.contextUris.workspacesUri.url
security_result.detection_fields[sourceProperties_contextUris_workspacesUri_url]
sourceProperties.contextUris.workspacesUri.displayName
security_result.detection_fields[sourceProperties_contextUris_workspacesUri_displayName]
sourceProperties.properties.autofocusContextCards.tags.public_tag_name
security_result.detection_fields.key/value [sourceProperties.properties.autofocusContextCards.tags.public_tag_name/description]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.public_tag_name
log field is mapped to the
intermediary.labels.key
UDM field.
sourceProperties.properties.autofocusContextCards.tags.description
security_result.detection_fields.key/value [sourceProperties.properties.autofocusContextCards.tags.public_tag_name/description]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.tags.description
log field is mapped to the
intermediary.labels.value
UDM field.
sourceProperties.properties.autofocusContextCards.indicator.firstSeenTsGlobal
security_result.detection_fields.key/value [sourcePropertiesproperties_autofocusContextCards_indicator_firstSeenTsGlobal]
If the
category
log field value is equal to
Malware: Bad IP
, then the
sourceProperties.properties.autofocusContextCards.indicator.firstSeenTsGlobal
log field is mapped to the
security_result.detection_fields.value
UDM field.
createTime
metadata.collected_timestamp
nextSteps
security_result.outcomes.key/value [next_steps]
sourceProperties.detectionPriority
security_result.priority
If the
sourceProperties.detectionPriority
log field value is equal to
HIGH
, then the
security_result.priority
UDM field is set to
HIGH_PRIORITY
.
Else if, the
sourceProperties.detectionPriority
log field value is equal to
MEDIUM
, then the
security_result.priority
UDM field is set to
MEDIUM_PRIORITY
.
Else if, the
sourceProperties.detectionPriority
log field value is equal to
LOW
, then the
security_result.priority
UDM field is set to
LOW_PRIORITY
.
sourceProperties.detectionPriority
security_result.priority_details
sourceProperties.detectionCategory.subRuleName
security_result.rule_labels.key/value [sourceProperties_detectionCategory_subRuleName]
sourceProperties.detectionCategory.ruleName
security_result.rule_name
severity
security_result.severity
sourceProperties.properties.vpcViolation.violationReason
security_result.summary
If the
category
log field value is equal to
Exfiltration: BigQuery Exfiltration
, then the
sourceProperties.properties.vpcViolation.violationReason
log field is mapped to the
security_result.summary
UDM field.
name
security_result.url_back_to_product
database.query
target.process.command_line
If the
category
log field value is equal to
Exfiltration: CloudSQL Over-Privileged Grant
, then the
database.query
log field is mapped to the
target.process.command_line
UDM field.
resource.folders.resourceFolderDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_folders_resourceFolderDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.folders.resourceFolderDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
resource.parentDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_parentDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.parentDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
resource.parentName
src.resource_ancestors.attribute.labels.key/value [resource_parentName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.parentName
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
resource.projectDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_projectDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.projectDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.datasetId
src.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_dataExfiltrationAttempt_sourceTables_datasetId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.datasetId
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.projectId
src.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_dataExfiltrationAttempt_sourceTables_projectId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.projectId
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.resourceUri
src.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_dataExfiltrationAttempt_sourceTables_resourceUri]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.resourceUri
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
parent
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
parent
log field is mapped to the
src.resource_ancestors.name
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.tableId
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.sourceTables.tableId
log field is mapped to the
src.resource_ancestors.name
UDM field and the
src.resource_ancestors.resource_type
UDM field is set to
TABLE
.
resourceName
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
resourceName
log field is mapped to the
src.resource_ancestors.name
UDM field.
resource.folders.resourceFolder
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.folders.resourceFolder
log field is mapped to the
src.resource_ancestors.name
UDM field.
sourceProperties.sourceId.customerOrganizationNumber
src.resource_ancestors.product_object_id
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.sourceId.customerOrganizationNumber
log field is mapped to the
src.resource_ancestors.product_object_id
UDM field.
sourceProperties.sourceId.projectNumber
src.resource_ancestors.product_object_id
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.sourceId.projectNumber
log field is mapped to the
src.resource_ancestors.product_object_id
UDM field.
sourceProperties.sourceId.organizationNumber
src.resource_ancestors.product_object_id
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.sourceId.organizationNumber
log field is mapped to the
src.resource_ancestors.product_object_id
UDM field.
resource.type
src.resource_ancestors.resource_subtype
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.type
log field is mapped to the
src.resource_ancestors.resource_subtype
UDM field.
database.displayName
target.resource.attribute.labels[database_displayName]
If the
category
log field value is equal to
Exfiltration: CloudSQL Over-Privileged Grant
, then the
database.displayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
database.grantees
target.resource.attribute.labels[database_grantees]
If the
category
log field value is equal to
Exfiltration: CloudSQL Over-Privileged Grant
, then the
target.resource.attribute.labels.key
UDM field is set to
database_grantees
and the
database.grantees
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.displayName
src.resource.attribute.labels.key/value [resource_displayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
or
Exfiltration: BigQuery Data to Google Drive
, then the
resource.displayName
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
resource.displayName
principal.hostname
If the
resource.type
log field value matches the regular expression pattern
(?i)google.compute.Instance or google.container.Cluster
, then the
resource.displayName
log field is mapped to the
principal.hostname
UDM field.
resource.display_name
src.resource.attribute.labels.key/value [resource_display_name]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
or
Exfiltration: BigQuery Data to Google Drive
, then the
resource.display_name
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
sourceProperties.properties.extractionAttempt.sourceTable.datasetId
src.resource.attribute.labels.key/value [sourceProperties_properties_extractionAttempt_sourceTable_datasetId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
then the
sourceProperties.properties.extractionAttempt.sourceTable.datasetId
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
Else if the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
then the
sourceProperties.properties.extractionAttempt.sourceTable.datasetId
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
sourceProperties.properties.extractionAttempt.sourceTable.projectId
src.resource.attribute.labels.key/value [sourceProperties_properties_extractionAttempt_sourceTable_projectId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
then the
sourceProperties.properties.extractionAttempt.sourceTable.projectId
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
Else if the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
then the
sourceProperties.properties.extractionAttempt.sourceTable.datasetId
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
sourceProperties.properties.extractionAttempt.sourceTable.resourceUri
src.resource.attribute.labels.key/value [sourceProperties_properties_extractionAttempt_sourceTable_resourceUri]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
then the
sourceProperties.properties.extractionAttempt.sourceTable.resourceUri
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
Else if the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
then the
sourceProperties.properties.extractionAttempt.sourceTable.datasetId
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
sourceProperties.properties.restoreToExternalInstance.backupId
additional.fields[sourceProperties_properties_restoreToExternalInstance_backupId]
If the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.backupId
log field is mapped to the
additional.fields
UDM field.
exfiltration.sources.components
src.resource.attribute.labels.key/value[exfiltration_sources_components]
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: BigQuery Data Extraction
, then the
src.resource.attribute.labels.key/value
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
resourceName
src.resource.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.sources.name
log field is mapped to the
src.resource.name
UDM field and the
resourceName
log field is mapped to the
src.resource_ancestors.name
UDM field.
sourceProperties.properties.restoreToExternalInstance.sourceCloudsqlInstanceResource
src.resource.name
If the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.sourceCloudsqlInstanceResource
log field is mapped to the
src.resource.name
UDM field and the
src.resource.resource_subtype
UDM field is set to
CloudSQL
.
sourceProperties.properties.exportToGcs.cloudsqlInstanceResource
src.resource.name
If the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.sourceCloudsqlInstanceResource
log field is mapped to the
src.resource.name
UDM field and the
src.resource.resource_subtype
UDM field is set to
CloudSQL
.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.cloudsqlInstanceResource
log field is mapped to the
src.resource.name
UDM field and the
src.resource.resource_subtype
UDM field is set to
CloudSQL
.
database.name
src.resource.name
exfiltration.sources.name
src.resource.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.sources.name
log field is mapped to the
src.resource.name
UDM field and the
resourceName
log field is mapped to the
src.resource_ancestors.name
UDM field.
sourceProperties.properties.extractionAttempt.sourceTable.tableId
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
then the
sourceProperties.properties.extractionAttempt.sourceTable.tableId
log field is mapped to the
src.resource_ancestors.name
UDM field.
Else if the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.sourceTable.tableId
log field is mapped to the
src.resource.product_object_id
UDM field.
access.serviceName
target.application
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
or
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: CloudSQL Restore Backup to External Organization
or
Exfiltration: CloudSQL Over-Privileged Grant
or
Persistence: New Geography
or
Persistence: IAM Anomalous Grant
, then the
access.serviceName
log field is mapped to the
target.application
UDM field.
sourceProperties.properties.serviceName
target.application
If the
category
log field value is equal to
Initial Access: Account Disabled Hijacked
or
Initial Access: Disabled Password Leak
or
Initial Access: Government Based Attack
or
Initial Access: Suspicious Login Blocked
or
Impair Defenses: Strong Authentication Disabled
or
Impair Defenses: Two Step Verification Disabled
or
Persistence: SSO Enablement Toggle
or
Persistence: SSO Settings Changed
, then the
sourceProperties.properties.serviceName
log field is mapped to the
target.application
UDM field.
sourceProperties.properties.domainName
target.domain.name
If the
category
log field value is equal to
Persistence: SSO Enablement Toggle
or
Persistence: SSO Settings Changed
, then the
sourceProperties.properties.domainName
log field is mapped to the
target.domain.name
UDM field.
sourceProperties.properties.domains.0
target.domain.name
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.domains.0
log field is mapped to the
target.domain.name
UDM field.
sourceProperties.properties.sensitiveRoleGrant.bindingDeltas.action
target.group.attribute.labels.key/value [sourceProperties_properties_sensitiveRoleGrant_bindingDeltas_action]
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.sensitiveRoleGrant.bindingDeltas.action
log field is mapped to the
target.group.attribute.labels.key/value
UDM field.
sourceProperties.properties.sensitiveRoleToHybridGroup.bindingDeltas.action
target.group.attribute.labels.key/value [sourceProperties_properties_sensitiveRoleToHybridGroup_bindingDeltas_action]
If the
category
log field value is equal to
Credential Access: Sensitive Role Granted To Hybrid Group
, then the
sourceProperties.properties.sensitiveRoleToHybridGroup.bindingDeltas.action
log field is mapped to the
target.group.attribute.labels.key/value
UDM field.
sourceProperties.properties.sensitiveRoleGrant.bindingDeltas.member
target.group.attribute.labels.key/value[sourceProperties_properties_sensitiveRoleGrant_bindingDeltas_member]
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.sensitiveRoleGrant.bindingDeltas.member
log field is mapped to the
target.group.attribute.labels.key/value
UDM field.
sourceProperties.properties.sensitiveRoleToHybridGroup.bindingDeltas.member
target.group.attribute.labels.key/value[sourceProperties_properties_sensitiveRoleToHybridGroup]
If the
category
log field value is equal to
Credential Access: Sensitive Role Granted To Hybrid Group
, then the
sourceProperties.properties.sensitiveRoleToHybridGroup.bindingDeltas.member
log field is mapped to the
target.group.attribute.labels.key/value
UDM field.
sourceProperties.properties.privilegedGroupOpenedToPublic.whoCanJoin
target.group.attribute.permissions.name
If the
category
log field value is equal to
Credential Access: Privileged Group Opened To Public
, then the
sourceProperties.properties.privilegedGroupOpenedToPublic.whoCanJoin
log field is mapped to the
target.group.attribute.permissions.name
UDM field.
sourceProperties.properties.customRoleSensitivePermissions.permissions
target.group.attribute.permissions.name
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.customRoleSensitivePermissions.permissions
log field is mapped to the
target.group.attribute.permissions.name
UDM field.
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.sensitiveRoles.roleName
target.group.attribute.roles.name
If the
category
log field value is equal to
Credential Access: External Member Added To Privileged Group
, then the
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.sensitiveRoles.roleName
log field is mapped to the
target.group.attribute.roles.name
UDM field.
sourceProperties.properties.sensitiveRoleToHybridGroup.bindingDeltas.role
target.group.attribute.roles.name
If the
category
log field value is equal to
Credential Access: Sensitive Role Granted To Hybrid Group
, then the
sourceProperties.properties.sensitiveRoleToHybridGroup.bindingDeltas.role
log field is mapped to the
target.group.attribute.roles.name
UDM field.
sourceProperties.properties.sensitiveRoleGrant.bindingDeltas.role
target.group.attribute.roles.name
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.sensitiveRoleGrant.bindingDeltas.role
log field is mapped to the
target.group.attribute.roles.name
UDM field.
sourceProperties.properties.privilegedGroupOpenedToPublic.sensitiveRoles.roleName
target.group.attribute.roles.name
If the
category
log field value is equal to
Credential Access: Privileged Group Opened To Public
, then the
sourceProperties.properties.privilegedGroupOpenedToPublic.sensitiveRoles.roleName
log field is mapped to the
target.group.attribute.roles.name
UDM field.
sourceProperties.properties.customRoleSensitivePermissions.roleName
target.group.attribute.roles.name
If the
category
log field value is equal to
Persistence: IAM Anomalous Grant
, then the
sourceProperties.properties.customRoleSensitivePermissions.roleName
log field is mapped to the
target.group.attribute.roles.name
UDM field.
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.groupName
target.group.group_display_name
If the
category
log field value is equal to
Credential Access: External Member Added To Privileged Group
, then the
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.groupName
log field is mapped to the
target.group.group_display_name
UDM field.
sourceProperties.properties.privilegedGroupOpenedToPublic.groupName
target.group.group_display_name
If the
category
log field value is equal to
Credential Access: Privileged Group Opened To Public
, then the
sourceProperties.properties.privilegedGroupOpenedToPublic.groupName
log field is mapped to the
target.group.group_display_name
UDM field.
sourceProperties.properties.sensitiveRoleToHybridGroup.groupName
target.group.group_display_name
If the
category
log field value is equal to
Credential Access: Sensitive Role Granted To Hybrid Group
, then the
sourceProperties.properties.sensitiveRoleToHybridGroup.groupName
log field is mapped to the
target.group.group_display_name
UDM field.
sourceProperties.properties.ipConnection.destIp
target.ip
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Outgoing DoS
, then the
sourceProperties.properties.ipConnection.destIp
log field is mapped to the
target.ip
UDM field.
access.methodName
target.labels [access_methodName]
(deprecated)
access.methodName
additional.fields [access_methodName]
processes.argumentsTruncated
target.labels [processes_argumentsTruncated]
(deprecated)
processes.argumentsTruncated
additional.fields [processes_argumentsTruncated]
processes.binary.contents
target.labels [processes_binary_contents]
(deprecated)
processes.binary.contents
additional.fields [processes_binary_contents]
processes.binary.hashedSize
target.labels [processes_binary_hashedSize]
(deprecated)
processes.binary.hashedSize
additional.fields [processes_binary_hashedSize]
processes.binary.partiallyHashed
target.labels [processes_binary_partiallyHashed]
(deprecated)
processes.binary.partiallyHashed
additional.fields [processes_binary_partiallyHashed]
processes.envVariables.name
target.labels [processes_envVariables_name]
(deprecated)
processes.envVariables.name
additional.fields [processes_envVariables_name]
processes.envVariables.val
target.labels [processes_envVariables_val]
(deprecated)
processes.envVariables.val
additional.fields [processes_envVariables_val]
processes.envVariablesTruncated
target.labels [processes_envVariablesTruncated]
(deprecated)
processes.envVariablesTruncated
additional.fields [processes_envVariablesTruncated]
processes.libraries.contents
target.labels [processes_libraries_contents]
(deprecated)
processes.libraries.contents
additional.fields [processes_libraries_contents]
processes.libraries.hashedSize
target.labels [processes_libraries_hashedSize]
(deprecated)
processes.libraries.hashedSize
additional.fields [processes_libraries_hashedSize]
processes.libraries.partiallyHashed
target.labels [processes_libraries_partiallyHashed]
(deprecated)
processes.libraries.partiallyHashed
additional.fields [processes_libraries_partiallyHashed]
processes.script.contents
target.labels [processes_script_contents]
(deprecated)
processes.script.contents
additional.fields [processes_script_contents]
processes.script.hashedSize
target.labels [processes_script_hashedSize]
(deprecated)
processes.script.hashedSize
additional.fields [processes_script_hashedSize]
processes.script.partiallyHashed
target.labels [processes_script_partiallyHashed]
(deprecated)
processes.script.partiallyHashed
additional.fields [processes_script_partiallyHashed]
sourceProperties.properties.methodName
target.labels [sourceProperties_properties_methodName]
(deprecated)
If the
category
log field value is equal to
Impair Defenses: Strong Authentication Disabled
or
Initial Access: Government Based Attack
or
Initial Access: Suspicious Login Blocked
or
Persistence: SSO Enablement Toggle
or
Persistence: SSO Settings Changed
, then the
sourceProperties.properties.methodName
log field is mapped to the
target.labels.value
UDM field.
sourceProperties.properties.methodName
additional.fields [sourceProperties_properties_methodName]
If the
category
log field value is equal to
Impair Defenses: Strong Authentication Disabled
or
Initial Access: Government Based Attack
or
Initial Access: Suspicious Login Blocked
or
Persistence: SSO Enablement Toggle
or
Persistence: SSO Settings Changed
, then the
sourceProperties.properties.methodName
log field is mapped to the
additional.fields.value.string_value
UDM field.
sourceProperties.properties.network.location
target.location.name
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.network.location
log field is mapped to the
target.location.name
UDM field.
processes.parentPid
target.parent_process.pid
sourceProperties.properties.ipConnection.destPort
target.port
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Outgoing DoS
, then the
sourceProperties.properties.ipConnection.destPort
log field is mapped to the
target.port
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.query
target.process.command_line
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.query
log field is mapped to the
target.process.command_line
UDM field.
processes.args
target.process.command_line_history [processes.args]
processes.name
target.process.file.full_path
processes.binary.path
target.process.file.full_path
processes.libraries.path
target.process.file.full_path
processes.script.path
target.process.file.full_path
processes.binary.sha256
target.process.file.sha256
processes.libraries.sha256
target.process.file.sha256
processes.script.sha256
target.process.file.sha256
processes.binary.size
target.process.file.size
processes.libraries.size
target.process.file.size
processes.script.size
target.process.file.size
processes.pid
target.process.pid
containers.uri
target.resource_ancestors.attribute.labels.key/value [containers_uri]
containers.labels.name/value
target.resource_ancestors.attribute.labels.key/value [containers.labels.name/value]
The
containers.labels.name
log field is mapped to the
target.resource_ancestors.attribute.labels.key
UDM field and the
containers.labels.value
log field is mapped to the
target.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.destVpc.projectId
target.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_destVpc_projectId]
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.destVpc.projectId
log field is mapped to the
target.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.destVpc.subnetworkName
target.resource_ancestors.attribute.labels.key/value [sourceProperties_properties_destVpc_subnetworkName]
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
, then the
sourceProperties.properties.destVpc.subnetworkName
log field is mapped to the
target.resource_ancestors.attribute.labels.value
UDM field.
sourceProperties.properties.network.subnetworkName
target.resource_ancestors.key/value [sourceProperties_properties_network_subnetworkName]
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
sourceProperties.properties.network.subnetworkName
log field is mapped to the
target.resource_ancestors.value
UDM field.
sourceProperties.properties.network.subnetworkId
target.resource_ancestors.labels.key/value [sourceProperties_properties_network_subnetworkId]
If the
category
log field value is equal to
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
sourceProperties.properties.network.subnetworkId
log field is mapped to the
target.resource_ancestors.value
UDM field.
sourceProperties.affectedResources.gcpResourceName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.properties.destVpc.vpcName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.properties.vpcName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
resourceName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.properties.projectId
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.properties.vpc.vpcName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
parent
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.affectedResources.gcpResourceName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
containers.name
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Cryptomining Bad IP
or
Malware: Bad IP
or
Malware: Cryptomining Bad Domain
or
Malware: Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.destVpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
sourceProperties.properties.vpc.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VPC_NETWORK
.
Else if, the
category
log field value is equal to
Active Scan: Log4j Vulnerable to RCE
, then the
sourceProperties.properties.vpcName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.sensitiveRoles.resource
target.resource_ancestors.name
If the
category
log field value is equal to
Credential Access: External Member Added To Privileged Group
, then the
sourceProperties.properties.externalMemberAddedToPrivilegedGroup.sensitiveRoles.resource
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.properties.privilegedGroupOpenedToPublic.sensitiveRoles.resource
target.resource_ancestors.name
If the
category
log field value is equal to
Credential Access: Privileged Group Opened To Public
, then the
sourceProperties.properties.privilegedGroupOpenedToPublic.sensitiveRoles.resource
log field is mapped to the
target.resource_ancestors.name
UDM field.
kubernetes.pods.containers.name
target.resource.attribute.labels[kubernetes_pods_containers_name]
sourceProperties.properties.gceInstanceId
target.resource_ancestors.product_object_id
If the
category
log field value is equal to
Persistence: GCE Admin Added Startup Script
or
Persistence: GCE Admin Added SSH Key
, then the
sourceProperties.properties.gceInstanceId
log field is mapped to the
target.resource_ancestors.product_object_id
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
sourceProperties.sourceId.projectNumber
target.resource_ancestors.product_object_id
If the
category
log field value is equal to
Persistence: GCE Admin Added Startup Script
or
Persistence: GCE Admin Added SSH Key
, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
sourceProperties.sourceId.customerOrganizationNumber
target.resource_ancestors.product_object_id
If the
category
log field value is equal to
Persistence: GCE Admin Added Startup Script
or
Persistence: GCE Admin Added SSH Key
, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
sourceProperties.sourceId.organizationNumber
target.resource_ancestors.product_object_id
If the
category
log field value is equal to
Persistence: GCE Admin Added Startup Script
or
Persistence: GCE Admin Added SSH Key
, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
containers.imageId
target.resource_ancestors.product_object_id
If the
category
log field value is equal to
Persistence: GCE Admin Added Startup Script
or
Persistence: GCE Admin Added SSH Key
, then the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
sourceProperties.properties.zone
target.resource.attribute.cloud.availability_zone
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.zone
log field is mapped to the
target.resource.attribute.cloud.availability_zone
UDM field.
canonicalName
metadata.product_log_id
The
finding_id
is extracted from the
canonicalName
log field using a Grok pattern.
If the
finding_id
log field value is
not
empty, then the
finding_id
log field is mapped to the
metadata.product_log_id
UDM field.
canonicalName
src.resource.attribute.labels.key/value [finding_id]
If the
finding_id
log field value is
not
empty, then the
finding_id
log field is mapped to the
src.resource.attribute.labels.key/value [finding_id]
UDM field.
If the
category
log field value is equal to one of the following values, then the
finding_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
src.resource.product_object_id
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
src.resource.product_object_id
UDM field.
If the
category
log field value is equal to one of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
src.resource.attribute.labels.key/value [source_id]
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
src.resource.attribute.labels.key/value [source_id]
UDM field.
If the
category
log field value is equal to one of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
target.resource.attribute.labels.key/value [finding_id]
If the
finding_id
log field value is
not
empty, then the
finding_id
log field is mapped to the
target.resource.attribute.labels.key/value [finding_id]
UDM field.
If the
category
log field value is
not
equal to any of the following values, then the
finding_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
target.resource.product_object_id
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
target.resource.product_object_id
UDM field.
If the
category
log field value is
not
equal to any of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
target.resource.attribute.labels.key/value [source_id]
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
target.resource.attribute.labels.key/value [source_id]
UDM field.
If the
category
log field value is
not
equal to any of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.datasetId
target.resource.attribute.labels.key/value [sourceProperties_properties_dataExfiltrationAttempt_destinationTables_datasetId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.datasetId
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.projectId
target.resource.attribute.labels.key/value [sourceProperties_properties_dataExfiltrationAttempt_destinationTables_projectId]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.projectId
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.resourceUri
target.resource.attribute.labels.key/value [sourceProperties_properties_dataExfiltrationAttempt_destinationTables_resourceUri]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.resourceUri
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
sourceProperties.properties.exportToGcs.exportScope
target.resource.attribute.labels.key/value [sourceProperties_properties_exportToGcs_exportScope]
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
target.resource.attribute.labels.key
UDM field is set to
exportScope
and the
sourceProperties.properties.exportToGcs.exportScope
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
sourceProperties.properties.extractionAttempt.destinations.objectName
target.file.names
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.objectName
log field is mapped to the
target.file.names
UDM field.
sourceProperties.properties.extractionAttempt.destinations.originalUri
target.resource.attribute.labels.key/value [sourceProperties_properties_extractionAttempt_destinations_originalUri]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.originalUri
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
sourceProperties.properties.metadataKeyOperation
target.resource.attribute.labels.key/value [sourceProperties_properties_metadataKeyOperation]
If the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.metadataKeyOperation
log field is mapped to the
target.resource.attribute.labels.key/value
UDM field.
exfiltration.targets.components
target.resource.attribute.labels.key/value[exfiltration_targets_components]
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: BigQuery Data Extraction
, then the
exfiltration.targets.components
log field is mapped to the
target.resource.attribute.labels.key/value
UDM field.
sourceProperties.properties.exportToGcs.bucketAccess
target.resource.attribute.permissions.name
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketAccess
log field is mapped to the
target.resource.attribute.permissions.name
UDM field.
sourceProperties.properties.name
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.exportToGcs.bucketResource
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
resourceName
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.attempts.vmName
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.instanceDetails
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.extractionAttempt.destinations.collectionName
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
exfiltration.targets.name
target.resource.name
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.bucketResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: CloudSQL Restore Backup to External Organization
, then the
sourceProperties.properties.restoreToExternalInstance.targetCloudsqlInstanceResource
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.vmName
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
or
Malware: Cryptomining Bad Domain
or
Configurable Bad Domain
, then the
sourceProperties.properties.instanceDetails
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.attribute.name
UDM field and the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field and the
sourceProperties.properties.dataExfiltrationAttempt.destinationTables.tableId
log field is mapped to the
target.resource.attribute.labels
UDM field and the
target.resource.resource_type
UDM field is set to
TABLE
.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
sourceProperties.properties.instanceId
target.resource.product_object_id
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.instanceId
log field is mapped to the
target.resource.product_object_id
UDM field.
kubernetes.pods.containers.imageId
target.resource.attribute.labels[kubernetes_pods_containers_imageId]
sourceProperties.properties.extractionAttempt.destinations.collectionType
target.resource.resource_subtype
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.destinations.collectionName
log field is mapped to the
target.resource.resource_subtype
UDM field.
Else if, the
category
log field value is equal to
Credential Access: External Member Added To Privileged Group
, then the
target.resource.resource_subtype
UDM field is set to
Privileged Group
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
target.resource.resource_subtype
UDM field is set to
BigQuery
.
target.resource.resource_type
If the
sourceProperties.properties.extractionAttempt.destinations.collectionType
log field value matches the regular expression
BUCKET
, then the
target.resource.resource_type
UDM field is set to
STORAGE_BUCKET
.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
target.resource.resource_type
UDM field is set to
TABLE
.
sourceProperties.properties.extractionAttempt.jobLink
target.url
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
sourceProperties.properties.extractionAttempt.jobLink
log field is mapped to the
target.url
UDM field.
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
, then the
sourceProperties.properties.extractionAttempt.jobLink
log field is mapped to the
target.url
UDM field.
sourceProperties.properties.exportToGcs.gcsUri
target.url
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
, then the
sourceProperties.properties.exportToGcs.gcsUri
log field is mapped to the
target.url
UDM field.
sourceProperties.properties.requestUrl
target.url
If the
category
log field value is equal to
Initial Access: Log4j Compromise Attempt
, then the
sourceProperties.properties.requestUrl
log field is mapped to the
target.url
UDM field.
sourceProperties.properties.policyLink
target.url
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
, then the
sourceProperties.properties.policyLink
log field is mapped to the
target.url
UDM field.
sourceProperties.properties.anomalousLocation.notSeenInLast
principal.user.attribute.labels.key/value [sourceProperties_properties_anomalousLocation_notSeenInLast]
If the
category
log field value is equal to
Persistence: New Geography
, then the
sourceProperties.properties.anomalousLocation.notSeenInLast
log field is mapped to the
principal.user.attribute.labels.value
UDM field.
sourceProperties.properties.attempts.username
target.user.userid
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.attempts.username
log field is mapped to the
target.user.userid
UDM field.
If the
category
log field value is equal to
Initial Access: Suspicious Login Blocked
, then the
userid
log field is mapped to the
target.user.userid
UDM field.
sourceProperties.properties.principalEmail
target.user.userid
If the
category
log field value is equal to
Initial Access: Suspicious Login Blocked
, then the
userid
log field is mapped to the
target.user.userid
UDM field.
sourceProperties.Added_Binary_Kind
target.resource.attribute.labels[sourceProperties_Added_Binary_Kind]
sourceProperties.Container_Creation_Timestamp.nanos
target.resource.attribute.labels[sourceProperties_Container_Creation_Timestamp_nanos]
sourceProperties.Container_Creation_Timestamp.seconds
target.resource.attribute.labels[sourceProperties_Container_Creation_Timestamp_seconds]
sourceProperties.Container_Image_Id
target.resource_ancestors.product_object_id
sourceProperties.Container_Image_Uri
target.resource.attribute.labels[sourceProperties_Container_Image_Uri]
sourceProperties.Container_Name
target.resource_ancestors.name
sourceProperties.Environment_Variables
target.labels [Environment_Variables_name]
(deprecated)
sourceProperties.Environment_Variables
additional.fields [Environment_Variables_name]
target.labels [Environment_Variables_val]
(deprecated)
additional.fields [Environment_Variables_val]
sourceProperties.Kubernetes_Labels
target.resource.attribute.labels.key/value [sourceProperties_Kubernetes_Labels.name/value]
sourceProperties.Parent_Pid
target.process.parent_process.pid
sourceProperties.Pid
target.process.pid
sourceProperties.Pod_Name
target.resource_ancestors.name
sourceProperties.Pod_Namespace
target.resource_ancestors.attribute.labels.key/value [sourceProperties_Pod_Namespace]
sourceProperties.Process_Arguments
target.process.command_line
sourceProperties.Process_Binary_Fullpath
target.process.file.full_path
sourceProperties.Process_Creation_Timestamp.nanos
target.labels [sourceProperties_Process_Creation_Timestamp_nanos]
(deprecated)
sourceProperties.Process_Creation_Timestamp.nanos
additional.fields [sourceProperties_Process_Creation_Timestamp_nanos]
sourceProperties.Process_Creation_Timestamp.seconds
target.labels [sourceProperties_Process_Creation_Timestamp_seconds]
(deprecated)
sourceProperties.Process_Creation_Timestamp.seconds
additional.fields [sourceProperties_Process_Creation_Timestamp_seconds]
sourceProperties.VM_Instance_Name
target.resource_ancestors.name
If the
category
log field value is equal to
Added Binary Executed
or
Added Library Loaded
, then the
sourceProperties.VM_Instance_Name
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource_ancestors.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
target.resource_ancestors.resource_type
resource.parent
target.resource_ancestors.attribute.labels.key/value [resource_project]
resource.project
target.resource_ancestors.attribute.labels.key/value [resource_parent]
sourceProperties.Added_Library_Fullpath
target.process.file.full_path
sourceProperties.Added_Library_Kind
target.resource.attribute.labels[sourceProperties_Added_Library_Kind
sourceProperties.affectedResources.gcpResourceName
target.resource_ancestors.name
sourceProperties.Backend_Service
target.resource.name
If the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
or
Application DDoS Attack Attempt
, then the
sourceProperties.Backend_Service
log field is mapped to the
target.resource.name
UDM field and the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
sourceProperties.Long_Term_Allowed_RPS
target.resource.attribute.labels[sourceProperties_Long_Term_Allowed_RPS]
sourceProperties.Long_Term_Denied_RPS
target.resource.attribute.labels[sourceProperties_Long_Term_Denied_RPS]
sourceProperties.Long_Term_Incoming_RPS
target.resource.attribute.labels[sourceProperties_Long_Term_Incoming_RPS]
sourceProperties.properties.customProperties.domain_category
target.resource.attribute.labels[sourceProperties_properties_customProperties_domain_category]
sourceProperties.Security_Policy
target.resource.attribute.labels[sourceProperties_Security_Policy]
sourceProperties.Short_Term_Allowed_RPS
target.resource.attribute.labels[sourceProperties_Short_Term_Allowed_RPS]
target.resource.resource_type
If the
category
log field value is equal to
Increasing Deny Ratio
or
Allowed Traffic Spike
or
Application DDoS Attack Attempt
, then the
target.resource.resource_type
UDM field is set to
BACKEND_SERVICE
.
If the
category
log field value is equal to
Configurable Bad Domain
, then the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
sourceProperties.properties.sensitiveRoleGrant.principalEmail
principal.user.userid
Grok : Extracted
user_id
from
sourceProperties.properties.sensitiveRoleGrant.principalEmail
log field, then the
user_id
field is mapped to the
principal.user.userid
UDM field.
sourceProperties.properties.customRoleSensitivePermissions.principalEmail
principal.user.userid
Grok : Extracted
user_id
from
sourceProperties.properties.customRoleSensitivePermissions.principalEmail
log field, then the
user_id
field is mapped to the
principal.user.userid
UDM field.
resourceName
principal.asset.location.name
If the
parentDisplayName
log field value is equal to
Virtual Machine Threat Detection
, then Grok : Extracted
project_name
,
region
,
zone_suffix
,
asset_prod_obj_id
from
resourceName
log field, then the
region
log field is mapped to the
principal.asset.location.name
UDM field.
resourceName
principal.asset.product_object_id
If the
parentDisplayName
log field value is equal to
Virtual Machine Threat Detection
, then Grok : Extracted
project_name
,
region
,
zone_suffix
,
asset_prod_obj_id
from
resourceName
log field, then the
asset_prod_obj_id
log field is mapped to the
principal.asset.product_object_id
UDM field.
resourceName
principal.asset.attribute.cloud.availability_zone
If the
parentDisplayName
log field value is equal to
Virtual Machine Threat Detection
, then Grok : Extracted
project_name
,
region
,
zone_suffix
,
asset_prod_obj_id
from
resourceName
log field, then the
zone_suffix
log field is mapped to the
principal.asset.attribute.cloud.availability_zone
UDM field.
resourceName
principal.asset.attribute.labels[project_name]
If the
parentDisplayName
log field value is equal to
Virtual Machine Threat Detection
, then Grok : Extracted
project_name
,
region
,
zone_suffix
,
asset_prod_obj_id
from
resourceName
log field, then the
project_name
log field is mapped to the
principal.asset.attribute.labels.value
UDM field.
sourceProperties.threats.memory_hash_detector.detections.binary_name
security_result.detection_fields[binary_name]
sourceProperties.threats.memory_hash_detector.detections.percent_pages_matched
security_result.detection_fields[percent_pages_matched]
sourceProperties.threats.memory_hash_detector.binary
security_result.detection_fields[memory_hash_detector_binary]
sourceProperties.threats.yara_rule_detector.yara_rule_name
security_result.detection_fields[yara_rule_name]
sourceProperties.Script_SHA256
target.resource.attribute.labels[script_sha256]
sourceProperties.Script_Content
target.resource.attribute.labels[script_content]
state
security_result.detection_fields[state]
assetDisplayName
target.asset.attribute.labels[asset_display_name]
assetId
target.asset.asset_id
findingProviderId
target.resource.attribute.labels[finding_provider_id]
sourceDisplayName
target.resource.attribute.labels[source_display_name]
processes.name
target.process.file.names
target.labels[failedActions_methodName]
sourceProperties.properties.failedActions.methodName
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.methodName
log field is
mapped to the
target.labels
UDM field.
additional.fields[failedActions_methodName]
sourceProperties.properties.failedActions.methodName
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.methodName
log field is
mapped to the
additional.fields
UDM field.
target.labels[failedActions_serviceName]
sourceProperties.properties.failedActions.serviceName
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.serviceName
log field is
mapped to the
target.labels
UDM field.
additional.fields[failedActions_serviceName]
sourceProperties.properties.failedActions.serviceName
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.serviceName
log field is
mapped to the
additional.fields
UDM field.
target.labels[failedActions_attemptTimes]
sourceProperties.properties.failedActions.attemptTimes
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.attemptTimes
log field is
mapped to the
target.labels
UDM field.
additional.fields[failedActions_attemptTimes]
sourceProperties.properties.failedActions.attemptTimes
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.attemptTimes
log field is
mapped to the
additional.fields
UDM field.
target.labels[failedActions_lastOccurredTime]
sourceProperties.properties.failedActions.lastOccurredTime
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.lastOccurredTime
log field
is mapped to the
target.labels
UDM field.
additional.fields[failedActions_lastOccurredTime]
sourceProperties.properties.failedActions.lastOccurredTime
If the
category
log field value is equal to
Initial Access: Excessive Permission Denied Actions
, then the
sourceProperties.properties.failedActions.lastOccurredTime
log field.
is mapped to the
additional.fields
UDM field.
resource.resourcePathString
src.resource.attribute.labels[resource_path_string]
If the
category
log field value contain one of the following values, then the
resource.resourcePathString
log field is mapped to the
src.resource.attribute.labels[resource_path_string]
UDM field.
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
Else, the
resource.resourcePathString
log field is mapped to the
target.resource.attribute.labels[resource_path_string]
UDM field.
Field mapping reference: event identifier to event type
Event Identifier
Event Type
Security Category
Active Scan: Log4j Vulnerable to RCE
SCAN_UNCATEGORIZED
Brute Force: SSH
USER_LOGIN
AUTH_VIOLATION
Credential Access: External Member Added To Privileged Group
GROUP_MODIFICATION
Credential Access: Privileged Group Opened To Public
GROUP_MODIFICATION
Credential Access: Sensitive Role Granted To Hybrid Group
GROUP_MODIFICATION
Defense Evasion: Modify VPC Service Control
SERVICE_MODIFICATION
Discovery: Can get sensitive Kubernetes object checkPreview
SCAN_UNCATEGORIZED
Discovery: Service Account Self-Investigation
SCAN_UNCATEGORIZED
Evasion: Access from Anonymizing Proxy
USER_RESOURCE_ACCESS
Exfiltration: BigQuery Data Exfiltration
USER_RESOURCE_ACCESS
DATA_EXFILTRATION
Exfiltration: BigQuery Data Extraction
USER_RESOURCE_ACCESS
DATA_EXFILTRATION
Exfiltration: BigQuery Data to Google Drive
USER_RESOURCE_ACCESS
DATA_EXFILTRATION
Exfiltration: CloudSQL Data Exfiltration
USER_RESOURCE_ACCESS
DATA_EXFILTRATION
Exfiltration: CloudSQL Over-Privileged Grant
USER_CHANGE_PERMISSIONS
DATA_EXFILTRATION
Exfiltration: CloudSQL Restore Backup to External Organization
USER_RESOURCE_ACCESS
DATA_EXFILTRATION
Impair Defenses: Strong Authentication Disabled
SETTING_MODIFICATION
Impair Defenses: Two Step Verification Disabled
SETTING_MODIFICATION
Initial Access: Account Disabled Hijacked
USER_UNCATEGORIZED
Initial Access: Disabled Password Leak
USER_UNCATEGORIZED
Initial Access: Government Based Attack
USER_UNCATEGORIZED
Initial Access: Log4j Compromise Attempt
SCAN_UNCATEGORIZED
EXPLOIT
Initial Access: Suspicious Login Blocked
USER_LOGIN
ACL_VIOLATION
Initial Access: Dormant Service Account Action
USER_RESOURCE_ACCESS
Initial Access: Database Superuser Writes to User Tables
USER_RESOURCE_UPDATE_CONTENT
Log4j Malware: Bad Domain
NETWORK_CONNECTION
SOFTWARE_MALICIOUS
Log4j Malware: Bad IP
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Malware: Bad Domain
NETWORK_CONNECTION
SOFTWARE_MALICIOUS
Malware: Bad IP
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Malware: Cryptomining Bad Domain
NETWORK_CONNECTION
SOFTWARE_MALICIOUS
Malware: Cryptomining Bad IP
NETWORK_CONNECTION
SOFTWARE_MALICIOUS
Malware: Outgoing DoS
NETWORK_CONNECTION
NETWORK_DENIAL_OF_SERVICE
Persistence: GCE Admin Added SSH Key
SETTING_MODIFICATION
Persistence: GCE Admin Added Startup Script
SETTING_MODIFICATION
Persistence: IAM Anomalous Grant
USER_UNCATEGORIZED
POLICY_VIOLATION
Persistence: New API MethodPreview
USER_RESOURCE_ACCESS
Persistence: New Geography
USER_RESOURCE_ACCESS
NETWORK_SUSPICIOUS
Persistence: New User Agent
USER_RESOURCE_ACCESS
Persistence: SSO Enablement Toggle
SETTING_MODIFICATION
Persistence: SSO Settings Changed
SETTING_MODIFICATION
Privilege Escalation: Changes to sensitive Kubernetes RBAC objectsPreview
RESOURCE_PERMISSIONS_CHANGE
Privilege Escalation: Create Kubernetes CSR for master certPreview
RESOURCE_CREATION
Privilege Escalation: Creation of sensitive Kubernetes bindingsPreview
RESOURCE_CREATION
Privilege Escalation: Get Kubernetes CSR with compromised bootstrap credentialsPreview
USER_RESOURCE_ACCESS
Privilege Escalation: Launch of privileged Kubernetes containerPreview
RESOURCE_CREATION
Added Binary Executed
PROCESS_LAUNCH
Added Library Loaded
USER_RESOURCE_ACCESS
Allowed Traffic Spike
NETWORK_CONNECTION
Increasing Deny Ratio
NETWORK_CONNECTION
Configurable bad domain
NETWORK_CONNECTION
Execution: Cryptocurrency Mining Hash Match
SCAN_UNCATEGORIZED
Execution: Cryptocurrency Mining YARA Rule
SCAN_UNCATEGORIZED
Malicious Script Executed
PROCESS_LAUNCH
SOFTWARE_MALICIOUS
Malicious URL Observed
SCAN_UNCATEGORIZED
NETWORK_MALICIOUS
Execution: Cryptocurrency Mining Combined Detection
SCAN_UNCATEGORIZED
Application DDoS Attack Attempt
SCAN_NETWORK
Defense Evasion: Unexpected ftrace handler
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected interrupt handler
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected kernel code modification
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected kernel modules
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected kernel read-only data modification
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected kprobe handler
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected processes in runqueue
PROCESS_UNCATEGORIZED
SOFTWARE_MALICIOUS
Defense Evasion: Unexpected system call handler
SCAN_UNCATEGORIZED
SOFTWARE_MALICIOUS
Reverse Shell
SCAN_UNCATEGORIZED
EXPLOIT
account_has_leaked_credentials
SCAN_UNCATEGORIZED
DATA_AT_REST
Initial Access: Dormant Service Account Key Created
RESOURCE_CREATION
Process Tree
PROCESS_UNCATEGORIZED
Unexpected Child Shell
PROCESS_UNCATEGORIZED
Execution: Added Malicious Binary Executed
PROCESS_LAUNCH
SOFTWARE_MALICIOUS
Execution: Modified Malicious Binary Executed
PROCESS_LAUNCH
SOFTWARE_MALICIOUS
Privilege Escalation: Anomalous Multistep Service Account Delegation for Admin Activity
USER_RESOURCE_ACCESS
Privilege Escalation: Anomalous Multistep Service Account Delegation for Data Access
USER_RESOURCE_ACCESS
Privilege Escalation: Dormant Service Account Granted Sensitive Role
USER_CHANGE_PERMISSIONS
Breakglass Account Used: break_glass_account
USER_RESOURCE_ACCESS
Configurable Bad Domain: APT29_Domains
NETWORK_CONNECTION
Unexpected Role Grant: Forbidden roles
USER_CHANGE_PERMISSIONS
Configurable Bad IP
NETWORK_CONNECTION
Unexpected Compute Engine instance type
RESOURCE_CREATION
Unexpected Compute Engine source image
RESOURCE_CREATION
Unexpected Compute Engine region
RESOURCE_CREATION
Custom role with prohibited permission
USER_CHANGE_PERMISSIONS
Unexpected Cloud API Call
USER_RESOURCE_ACCESS
The following tables contain UDM event types and UDM fields mapping for Security Command Center -
VULNERABILITY
,
MISCONFIGURATION
,
OBSERVATION
,
ERROR
,
UNSPECIFIED
,
POSTURE_VIOLATION
finding classes.
VULNERABILITY category to UDM event type
The following table lists the VULNERABILITY category and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
DISK_CSEK_DISABLED
SCAN_UNCATEGORIZED
ALPHA_CLUSTER_ENABLED
SCAN_UNCATEGORIZED
AUTO_REPAIR_DISABLED
SCAN_UNCATEGORIZED
AUTO_UPGRADE_DISABLED
SCAN_UNCATEGORIZED
CLUSTER_SHIELDED_NODES_DISABLED
SCAN_UNCATEGORIZED
COS_NOT_USED
SCAN_UNCATEGORIZED
INTEGRITY_MONITORING_DISABLED
SCAN_UNCATEGORIZED
IP_ALIAS_DISABLED
SCAN_UNCATEGORIZED
LEGACY_METADATA_ENABLED
SCAN_UNCATEGORIZED
RELEASE_CHANNEL_DISABLED
SCAN_UNCATEGORIZED
DATAPROC_IMAGE_OUTDATED
SCAN_VULN_NETWORK
PUBLIC_DATASET
SCAN_UNCATEGORIZED
DNSSEC_DISABLED
SCAN_UNCATEGORIZED
RSASHA1_FOR_SIGNING
SCAN_UNCATEGORIZED
REDIS_ROLE_USED_ON_ORG
SCAN_UNCATEGORIZED
KMS_PUBLIC_KEY
SCAN_UNCATEGORIZED
SQL_CONTAINED_DATABASE_AUTHENTICATION
SCAN_UNCATEGORIZED
SQL_CROSS_DB_OWNERSHIP_CHAINING
SCAN_UNCATEGORIZED
SQL_EXTERNAL_SCRIPTS_ENABLED
SCAN_UNCATEGORIZED
SQL_LOCAL_INFILE
SCAN_UNCATEGORIZED
SQL_LOG_ERROR_VERBOSITY
SCAN_UNCATEGORIZED
SQL_LOG_MIN_DURATION_STATEMENT_ENABLED
SCAN_UNCATEGORIZED
SQL_LOG_MIN_ERROR_STATEMENT
SCAN_UNCATEGORIZED
SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY
SCAN_UNCATEGORIZED
SQL_LOG_MIN_MESSAGES
SCAN_UNCATEGORIZED
SQL_LOG_EXECUTOR_STATS_ENABLED
SCAN_UNCATEGORIZED
SQL_LOG_HOSTNAME_ENABLED
SCAN_UNCATEGORIZED
SQL_LOG_PARSER_STATS_ENABLED
SCAN_UNCATEGORIZED
SQL_LOG_PLANNER_STATS_ENABLED
SCAN_UNCATEGORIZED
SQL_LOG_STATEMENT_STATS_ENABLED
SCAN_UNCATEGORIZED
SQL_LOG_TEMP_FILES
SCAN_UNCATEGORIZED
SQL_REMOTE_ACCESS_ENABLED
SCAN_UNCATEGORIZED
SQL_SKIP_SHOW_DATABASE_DISABLED
SCAN_UNCATEGORIZED
SQL_TRACE_FLAG_3625
SCAN_UNCATEGORIZED
SQL_USER_CONNECTIONS_CONFIGURED
SCAN_UNCATEGORIZED
SQL_USER_OPTIONS_CONFIGURED
SCAN_UNCATEGORIZED
SQL_WEAK_ROOT_PASSWORD
SCAN_UNCATEGORIZED
PUBLIC_LOG_BUCKET
SCAN_UNCATEGORIZED
ACCESSIBLE_GIT_REPOSITORY
SCAN_UNCATEGORIZED
DATA_EXFILTRATION
ACCESSIBLE_SVN_REPOSITORY
SCAN_NETWORK
DATA_EXFILTRATION
CACHEABLE_PASSWORD_INPUT
SCAN_NETWORK
NETWORK_SUSPICIOUS
CLEAR_TEXT_PASSWORD
SCAN_NETWORK
NETWORK_MALICIOUS
INSECURE_ALLOW_ORIGIN_ENDS_WITH_VALIDATION
SCAN_UNCATEGORIZED
INSECURE_ALLOW_ORIGIN_STARTS_WITH_VALIDATION
SCAN_UNCATEGORIZED
INVALID_CONTENT_TYPE
SCAN_UNCATEGORIZED
INVALID_HEADER
SCAN_UNCATEGORIZED
MISMATCHING_SECURITY_HEADER_VALUES
SCAN_UNCATEGORIZED
MISSPELLED_SECURITY_HEADER_NAME
SCAN_UNCATEGORIZED
MIXED_CONTENT
SCAN_UNCATEGORIZED
OUTDATED_LIBRARY
SCAN_VULN_HOST
SOFTWARE_SUSPICIOUS
SERVER_SIDE_REQUEST_FORGERY
SCAN_NETWORK
NETWORK_MALICIOUS
SESSION_ID_LEAK
SCAN_NETWORK
DATA_EXFILTRATION
SQL_INJECTION
SCAN_NETWORK
EXPLOIT
SOFTWARE_VULNERABILITY
SCAN_VULN_HOST
STRUTS_INSECURE_DESERIALIZATION
SCAN_VULN_HOST
SOFTWARE_SUSPICIOUS
XSS
SCAN_NETWORK
SOFTWARE_SUSPICIOUS
XSS_ANGULAR_CALLBACK
SCAN_NETWORK
SOFTWARE_SUSPICIOUS
XSS_ERROR
SCAN_HOST
SOFTWARE_SUSPICIOUS
XXE_REFLECTED_FILE_LEAKAGE
SCAN_HOST
SOFTWARE_SUSPICIOUS
BASIC_AUTHENTICATION_ENABLED
SCAN_UNCATEGORIZED
CLIENT_CERT_AUTHENTICATION_DISABLED
SCAN_UNCATEGORIZED
LABELS_NOT_USED
SCAN_UNCATEGORIZED
PUBLIC_STORAGE_OBJECT
SCAN_UNCATEGORIZED
SQL_BROAD_ROOT_LOGIN
SCAN_UNCATEGORIZED
WEAK_CREDENTIALS
SCAN_VULN_NETWORK
NETWORK_MALICIOUS
ELASTICSEARCH_API_EXPOSED
SCAN_VULN_NETWORK
NETWORK_MALICIOUS
EXPOSED_GRAFANA_ENDPOINT
SCAN_VULN_NETWORK
NETWORK_MALICIOUS
EXPOSED_METABASE
SCAN_VULN_NETWORK
NETWORK_MALICIOUS
EXPOSED_SPRING_BOOT_ACTUATOR_ENDPOINT
SCAN_VULN_NETWORK
HADOOP_YARN_UNAUTHENTICATED_RESOURCE_MANAGER_API
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
JAVA_JMX_RMI_EXPOSED
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
JUPYTER_NOTEBOOK_EXPOSED_UI
SCAN_VULN_NETWORK
KUBERNETES_API_EXPOSED
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
UNFINISHED_WORDPRESS_INSTALLATION
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
UNAUTHENTICATED_JENKINS_NEW_ITEM_CONSOLE
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
APACHE_HTTPD_RCE
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
APACHE_HTTPD_SSRF
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
CONSUL_RCE
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
DRUID_RCE
SCAN_VULN_NETWORK
DRUPAL_RCE
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
FLINK_FILE_DISCLOSURE
SCAN_VULN_NETWORK
NETWORK_SUSPICIOUS
GITLAB_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
GoCD_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
JENKINS_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
JOOMLA_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
LOG4J_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
MANTISBT_PRIVILEGE_ESCALATION
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
OGNL_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
OPENAM_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
ORACLE_WEBLOGIC_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
PHPUNIT_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
PHP_CGI_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
PORTAL_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
REDIS_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
SOLR_FILE_EXPOSED
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
SOLR_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
STRUTS_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
TOMCAT_FILE_DISCLOSURE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
VBULLETIN_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
VCENTER_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
WEBLOGIC_RCE
SCAN_VULN_NETWORK
SOFTWARE_SUSPICIOUS
OS_VULNERABILITY
SCAN_VULN_HOST
IAM_ROLE_HAS_EXCESSIVE_PERMISSIONS
SCAN_UNCATEGORIZED
SOFTWARE_SUSPICIOUS
SERVICE_AGENT_GRANTED_BASIC_ROLE
SCAN_UNCATEGORIZED
SOFTWARE_SUSPICIOUS
UNUSED_IAM_ROLE
SCAN_UNCATEGORIZED
SERVICE_AGENT_ROLE_REPLACED_WITH_BASIC_ROLE
SCAN_UNCATEGORIZED
SOFTWARE_SUSPICIOUS
MISCONFIGURATION category to UDM event type
The following table lists the MISCONFIGURATION category and their corresponding UDM event types.
Event Identifier
Event Type
API_KEY_APIS_UNRESTRICTED
SCAN_UNCATEGORIZED
API_KEY_APPS_UNRESTRICTED
SCAN_UNCATEGORIZED
API_KEY_EXISTS
SCAN_UNCATEGORIZED
API_KEY_NOT_ROTATED
SCAN_UNCATEGORIZED
PUBLIC_COMPUTE_IMAGE
SCAN_UNCATEGORIZED
CONFIDENTIAL_COMPUTING_DISABLED
SCAN_HOST
COMPUTE_PROJECT_WIDE_SSH_KEYS_ALLOWED
SCAN_UNCATEGORIZED
COMPUTE_SECURE_BOOT_DISABLED
SCAN_HOST
DEFAULT_SERVICE_ACCOUNT_USED
SCAN_UNCATEGORIZED
FULL_API_ACCESS
SCAN_UNCATEGORIZED
OS_LOGIN_DISABLED
SCAN_UNCATEGORIZED
PUBLIC_IP_ADDRESS
SCAN_HOST
SHIELDED_VM_DISABLED
SCAN_HOST
COMPUTE_SERIAL_PORTS_ENABLED
SCAN_HOST
DISK_CMEK_DISABLED
SCAN_UNCATEGORIZED
HTTP_LOAD_BALANCER
SCAN_NETWORK
IP_FORWARDING_ENABLED
SCAN_HOST
WEAK_SSL_POLICY
SCAN_NETWORK
BINARY_AUTHORIZATION_DISABLED
SCAN_UNCATEGORIZED
CLUSTER_LOGGING_DISABLED
SCAN_UNCATEGORIZED
CLUSTER_MONITORING_DISABLED
SCAN_UNCATEGORIZED
CLUSTER_PRIVATE_GOOGLE_ACCESS_DISABLED
SCAN_UNCATEGORIZED
CLUSTER_SECRETS_ENCRYPTION_DISABLED
SCAN_UNCATEGORIZED
INTRANODE_VISIBILITY_DISABLED
SCAN_UNCATEGORIZED
MASTER_AUTHORIZED_NETWORKS_DISABLED
SCAN_UNCATEGORIZED
NETWORK_POLICY_DISABLED
SCAN_UNCATEGORIZED
NODEPOOL_SECURE_BOOT_DISABLED
SCAN_UNCATEGORIZED
OVER_PRIVILEGED_ACCOUNT
SCAN_UNCATEGORIZED
OVER_PRIVILEGED_SCOPES
SCAN_UNCATEGORIZED
POD_SECURITY_POLICY_DISABLED
SCAN_UNCATEGORIZED
PRIVATE_CLUSTER_DISABLED
SCAN_UNCATEGORIZED
WORKLOAD_IDENTITY_DISABLED
SCAN_UNCATEGORIZED
LEGACY_AUTHORIZATION_ENABLED
SCAN_UNCATEGORIZED
NODEPOOL_BOOT_CMEK_DISABLED
SCAN_UNCATEGORIZED
WEB_UI_ENABLED
SCAN_UNCATEGORIZED
AUTO_REPAIR_DISABLED
SCAN_UNCATEGORIZED
AUTO_UPGRADE_DISABLED
SCAN_UNCATEGORIZED
CLUSTER_SHIELDED_NODES_DISABLED
SCAN_UNCATEGORIZED
RELEASE_CHANNEL_DISABLED
SCAN_UNCATEGORIZED
BIGQUERY_TABLE_CMEK_DISABLED
SCAN_UNCATEGORIZED
DATASET_CMEK_DISABLED
SCAN_UNCATEGORIZED
EGRESS_DENY_RULE_NOT_SET
SCAN_NETWORK
FIREWALL_RULE_LOGGING_DISABLED
SCAN_UNCATEGORIZED
OPEN_CASSANDRA_PORT
SCAN_NETWORK
OPEN_SMTP_PORT
SCAN_NETWORK
OPEN_REDIS_PORT
SCAN_NETWORK
OPEN_POSTGRESQL_PORT
SCAN_NETWORK
OPEN_POP3_PORT
SCAN_NETWORK
OPEN_ORACLEDB_PORT
SCAN_NETWORK
OPEN_NETBIOS_PORT
SCAN_NETWORK
OPEN_MYSQL_PORT
SCAN_NETWORK
OPEN_MONGODB_PORT
SCAN_NETWORK
OPEN_MEMCACHED_PORT
SCAN_NETWORK
OPEN_LDAP_PORT
SCAN_NETWORK
OPEN_FTP_PORT
SCAN_NETWORK
OPEN_ELASTICSEARCH_PORT
SCAN_NETWORK
OPEN_DNS_PORT
SCAN_NETWORK
OPEN_HTTP_PORT
SCAN_NETWORK
OPEN_DIRECTORY_SERVICES_PORT
SCAN_NETWORK
OPEN_CISCOSECURE_WEBSM_PORT
SCAN_NETWORK
OPEN_RDP_PORT
SCAN_NETWORK
OPEN_TELNET_PORT
SCAN_NETWORK
OPEN_FIREWALL
SCAN_NETWORK
OPEN_SSH_PORT
SCAN_NETWORK
SERVICE_ACCOUNT_ROLE_SEPARATION
SCAN_UNCATEGORIZED
NON_ORG_IAM_MEMBER
SCAN_UNCATEGORIZED
OVER_PRIVILEGED_SERVICE_ACCOUNT_USER
SCAN_UNCATEGORIZED
ADMIN_SERVICE_ACCOUNT
SCAN_UNCATEGORIZED
SERVICE_ACCOUNT_KEY_NOT_ROTATED
SCAN_UNCATEGORIZED
USER_MANAGED_SERVICE_ACCOUNT_KEY
SCAN_UNCATEGORIZED
PRIMITIVE_ROLES_USED
SCAN_UNCATEGORIZED
KMS_ROLE_SEPARATION
SCAN_UNCATEGORIZED
OPEN_GROUP_IAM_MEMBER
SCAN_UNCATEGORIZED
KMS_KEY_NOT_ROTATED
SCAN_UNCATEGORIZED
KMS_PROJECT_HAS_OWNER
SCAN_UNCATEGORIZED
TOO_MANY_KMS_USERS
SCAN_UNCATEGORIZED
OBJECT_VERSIONING_DISABLED
SCAN_UNCATEGORIZED
LOCKED_RETENTION_POLICY_NOT_SET
SCAN_UNCATEGORIZED
BUCKET_LOGGING_DISABLED
SCAN_UNCATEGORIZED
LOG_NOT_EXPORTED
SCAN_UNCATEGORIZED
AUDIT_LOGGING_DISABLED
SCAN_UNCATEGORIZED
MFA_NOT_ENFORCED
SCAN_UNCATEGORIZED
ROUTE_NOT_MONITORED
SCAN_NETWORK
OWNER_NOT_MONITORED
SCAN_UNCATEGORIZED
AUDIT_CONFIG_NOT_MONITORED
SCAN_UNCATEGORIZED
BUCKET_IAM_NOT_MONITORED
SCAN_UNCATEGORIZED
CUSTOM_ROLE_NOT_MONITORED
SCAN_UNCATEGORIZED
FIREWALL_NOT_MONITORED
SCAN_NETWORK
NETWORK_NOT_MONITORED
SCAN_NETWORK
SQL_INSTANCE_NOT_MONITORED
SCAN_UNCATEGORIZED
DEFAULT_NETWORK
SCAN_NETWORK
DNS_LOGGING_DISABLED
SCAN_NETWORK
PUBSUB_CMEK_DISABLED
SCAN_UNCATEGORIZED
PUBLIC_SQL_INSTANCE
SCAN_HOST
SSL_NOT_ENFORCED
SCAN_NETWORK
AUTO_BACKUP_DISABLED
SCAN_UNCATEGORIZED
SQL_CMEK_DISABLED
SCAN_UNCATEGORIZED
SQL_LOG_CHECKPOINTS_DISABLED
SCAN_UNCATEGORIZED
SQL_LOG_CONNECTIONS_DISABLED
SCAN_UNCATEGORIZED
SQL_LOG_DISCONNECTIONS_DISABLED
SCAN_UNCATEGORIZED
SQL_LOG_DURATION_DISABLED
SCAN_UNCATEGORIZED
SQL_LOG_LOCK_WAITS_DISABLED
SCAN_UNCATEGORIZED
SQL_LOG_STATEMENT
SCAN_UNCATEGORIZED
SQL_NO_ROOT_PASSWORD
SCAN_UNCATEGORIZED
SQL_PUBLIC_IP
SCAN_HOST
SQL_CONTAINED_DATABASE_AUTHENTICATION
SCAN_UNCATEGORIZED
SQL_CROSS_DB_OWNERSHIP_CHAINING
SCAN_UNCATEGORIZED
SQL_LOCAL_INFILE
SCAN_UNCATEGORIZED
SQL_LOG_MIN_ERROR_STATEMENT
SCAN_UNCATEGORIZED
SQL_LOG_MIN_ERROR_STATEMENT_SEVERITY
SCAN_UNCATEGORIZED
SQL_LOG_TEMP_FILES
SCAN_UNCATEGORIZED
SQL_REMOTE_ACCESS_ENABLED
SCAN_UNCATEGORIZED
SQL_SKIP_SHOW_DATABASE_DISABLED
SCAN_UNCATEGORIZED
SQL_TRACE_FLAG_3625
SCAN_UNCATEGORIZED
SQL_USER_CONNECTIONS_CONFIGURED
SCAN_UNCATEGORIZED
SQL_USER_OPTIONS_CONFIGURED
SCAN_UNCATEGORIZED
PUBLIC_BUCKET_ACL
SCAN_UNCATEGORIZED
BUCKET_POLICY_ONLY_DISABLED
SCAN_UNCATEGORIZED
BUCKET_CMEK_DISABLED
SCAN_UNCATEGORIZED
FLOW_LOGS_DISABLED
SCAN_UNCATEGORIZED
PRIVATE_GOOGLE_ACCESS_DISABLED
SCAN_NETWORK
kms_key_region_europe
SCAN_UNCATEGORIZED
kms_non_euro_region
SCAN_UNCATEGORIZED
LEGACY_NETWORK
SCAN_NETWORK
LOAD_BALANCER_LOGGING_DISABLED
SCAN_NETWORK
INSTANCE_OS_LOGIN_DISABLED
SCAN_UNCATEGORIZED
GKE_PRIVILEGE_ESCALATION
SCAN_UNCATEGORIZED
GKE_RUN_AS_NONROOT
SCAN_UNCATEGORIZED
GKE_HOST_PATH_VOLUMES
SCAN_UNCATEGORIZED
GKE_HOST_NAMESPACES
SCAN_UNCATEGORIZED
GKE_PRIVILEGED_CONTAINERS
SCAN_UNCATEGORIZED
GKE_HOST_PORTS
SCAN_UNCATEGORIZED
GKE_CAPABILITIES
SCAN_UNCATEGORIZED
OBSERVATION category to UDM event type
The following table lists the OBSERVATION category and their corresponding UDM event types.
Event Identifier
Event Type
Persistence: Project SSH Key Added
USER_RESOURCE_CREATION
Persistence: Add Sensitive Role
RESOURCE_PERMISSIONS_CHANGE
Impact: GPU Instance Created
USER_RESOURCE_CREATION
Impact: Many Instances Created
USER_RESOURCE_CREATION
ERROR category to UDM event type
The following table lists the ERROR category and their corresponding UDM event types.
Event Identifier
Event Type
VPC_SC_RESTRICTION
SCAN_UNCATEGORIZED
MISCONFIGURED_CLOUD_LOGGING_EXPORT
SCAN_UNCATEGORIZED
API_DISABLED
SCAN_UNCATEGORIZED
KTD_IMAGE_PULL_FAILURE
SCAN_UNCATEGORIZED
KTD_BLOCKED_BY_ADMISSION_CONTROLLER
SCAN_UNCATEGORIZED
KTD_SERVICE_ACCOUNT_MISSING_PERMISSIONS
SCAN_UNCATEGORIZED
GKE_SERVICE_ACCOUNT_MISSING_PERMISSIONS
SCAN_UNCATEGORIZED
SCC_SERVICE_ACCOUNT_MISSING_PERMISSIONS
SCAN_UNCATEGORIZED
UNSPECIFIED category to UDM event type
The following table lists the UNSPECIFIED category and their corresponding UDM event types.
Event Identifier
Event Type
Security Category
OPEN_FIREWALL
SCAN_VULN_HOST
POLICY_VIOLATION
POSTURE_VIOLATION category to UDM event type
The following table lists the POSTURE_VIOLATION category and their corresponding UDM event types.
Event Identifier
Event Type
SECURITY_POSTURE_DRIFT
SERVICE_MODIFICATION
SECURITY_POSTURE_POLICY_DRIFT
SCAN_UNCATEGORIZED
SECURITY_POSTURE_POLICY_DELETE
SCAN_UNCATEGORIZED
SECURITY_POSTURE_DETECTOR_DRIFT
SCAN_UNCATEGORIZED
SECURITY_POSTURE_DETECTOR_DELETE
SCAN_UNCATEGORIZED
SENSITIVE_DATA_RISK category to UDM event type
The following table lists the SENSITIVE_DATA_RISK category and their corresponding UDM event types.
Event Identifier
Event Type
DATA_SECURITY_POSTURE_ACCESS_VIOLATION
USER_RESOURCE_ACCESS
DATA_SECURITY_POSTURE_FLOW_VIOLATION
SCAN_UNCATEGORIZED
DATA_SECURITY_POSTURE_CMEK_POLICY_MISCONFIGURED
SCAN_UNCATEGORIZED
DATA_SECURITY_POSTURE_CMEK_POLICY_DELETED
SCAN_UNCATEGORIZED
DATA_SECURITY_POSTURE_CMEK_VIOLATION
SCAN_UNCATEGORIZED
SENSITIVE_DATA_PUBLIC_SQL_INSTANCE
SCAN_UNCATEGORIZED
SENSITIVE_DATA_PUBLIC_BUCKET_ACL
SCAN_UNCATEGORIZED
SENSITIVE_DATA_PUBLIC_DATASET
SCAN_UNCATEGORIZED
SENSITIVE_DATA_SQL_PUBLIC_IP
SCAN_UNCATEGORIZED
SENSITIVE_DATA_BIGQUERY_TABLE_CMEK_DISABLED
SCAN_UNCATEGORIZED
SENSITIVE_DATA_BUCKET_CMEK_DISABLED
SCAN_UNCATEGORIZED
SENSITIVE_DATA_DATASET_CMEK_DISABLED
SCAN_UNCATEGORIZED
SENSITIVE_DATA_SQL_CMEK_DISABLED
SCAN_UNCATEGORIZED
Field mapping reference: VULNERABILITY
The following table lists the log fields of the VULNERABILITY category and their corresponding UDM fields.
RawLog field
UDM mapping
Logic
assetDisplayName
target.asset.attribute.labels.key/value [assetDisplayName]
assetId
target.asset.asset_id
findingProviderId
target.resource.attribute.labels.key/value [findings_findingProviderId]
sourceDisplayName
target.resource.attribute.labels.key/value [sourceDisplayName]
sourceProperties.description
extensions.vuln.vulnerabilities.description
sourceProperties.finalUrl
network.http.referral_url
sourceProperties.form.fields
target.resource.attribute.labels.key/value [sourceProperties_form_fields]
sourceProperties.httpMethod
network.http.method
sourceProperties.name
target.resource.attribute.labels.key/value [sourceProperties_name]
sourceProperties.outdatedLibrary.learnMoreUrls
target.resource.attribute.labels.key/value[sourceProperties_outdatedLibrary_learnMoreUrls]
sourceProperties.outdatedLibrary.libraryName
target.resource.attribute.labels.key/value[outdatedLibrary.libraryName]
sourceProperties.outdatedLibrary.version
target.resource.attribute.labels.key/value[sourceProperties_outdatedLibrary_libraryName]
sourceProperties.ResourcePath
target.resource.attribute.labels.key/value[sourceProperties_ResourcePath]
externalUri
about.url
category
extensions.vuln.vulnerabilities.name
resourceName
principal.asset.location.name
Extracted
region
from
resourceName
using a Grok pattern, and mapped to the
principal.asset.location.name
UDM field.
resourceName
principal.asset.product_object_id
Extracted
asset_prod_obj_id
from
resourceName
using a Grok pattern, and mapped to the
principal.asset.product_object_id
UDM field.
resourceName
principal.asset.attribute.cloud.availability_zone
Extracted
zone_suffix
from
resourceName
using a Grok pattern, and mapped to the
principal.asset.attribute.cloud.availability_zone
UDM field.
sourceProperties.RevokedIamPermissionsCount
security_result.detection_fields.key/value[revoked_Iam_permissions_count]
sourceProperties.TotalRecommendationsCount
security_result.detection_fields.key/value[total_recommendations_count]
sourceProperties.DeactivationReason
security_result.detection_fields.key/value[deactivation_reason]
iamBindings.role
about.user.attribute.roles.name
iamBindings.member
about.user.email_addresses
iamBindings.action
about.user.attribute.labels.key/value[action]
Field mapping reference: MISCONFIGURATION
The following table lists the log fields of the MISCONFIGURATION category and their corresponding UDM fields.
RawLog field
UDM mapping
assetDisplayName
target.asset.attribute.labels.key/value [assetDisplayName]
assetId
target.asset.asset_id
externalUri
about.url
findingProviderId
target.resource.attribute.labels[findingProviderId]
sourceDisplayName
target.resource.attribute.labels[sourceDisplayName]
sourceProperties.Recommendation
security_result.outcomes[sourceProperties_Recommendation]
sourceProperties.ExceptionInstructions
security_result.outcomes[sourceProperties_ExceptionInstructions]
sourceProperties.Explanation
security_result.outcomes[sourceProperties_Explanation]
sourceProperties.debug
additional.fields[sourceProperties_debug]
sourceProperties.debug2
additional.fields[sourceProperties_debug2]
sourceProperties.ScannerName
principal.labels.key/value[sourceProperties_ScannerName]
sourceProperties.ResourcePath
target.resource.attribute.labels.key/value[sourceProperties_ResourcePath]
sourceProperties.ReactivationCount
target.resource.attribute.labels.key/value [sourceProperties_ReactivationCount]
sourceProperties.DeactivationReason
target.resource.attribute.labels.key/value [DeactivationReason]
sourceProperties.ActionRequiredOnProject
target.resource.attribute.labels.key/value [sourceProperties_ActionRequiredOnProject]
sourceProperties.VulnerableNetworkInterfaceNames
target.resource.attribute.labels.key/value [sourceProperties_VulnerableNetworkInterfaceNames]
sourceProperties.VulnerableNodePools
target.resource.attribute.labels.key/value [sourceProperties_VulnerableNodePools]
sourceProperties.VulnerableNodePoolsList
target.resource.attribute.labels.key/value [sourceProperties_VulnerableNodePoolsList]
sourceProperties.AllowedOauthScopes
target.resource.attribute.permissions.name
sourceProperties.ExposedService
target.application
sourceProperties.OpenPorts.TCP
target.resource.attribute.labels.key/value[sourceProperties_OpenPorts_TCP]
sourceProperties.OffendingIamRolesList.member
about.user.email_addresses
sourceProperties.OffendingIamRolesList.roles
about.user.attribute.roles.name
sourceProperties.ActivationTrigger
target.resource.attribute.labels.key/value [sourceProperties_ActivationTrigger]
sourceProperties.MfaDetails.users
target.resource.attribute.labels.key/value [sourceProperties_MfaDetails_users]
sourceProperties.MfaDetails.enrolled
target.resource.attribute.labels.key/value [sourceProperties_MfaDetails_enrolled]
sourceProperties.MfaDetails.enforced
target.resource.attribute.labels.key/value [sourceProperties_MfaDetails_enforced]
sourceProperties.MfaDetails.advancedProtection
target.resource.attribute.labels.key/value [sourceProperties_MfaDetails_advancedProtection]
sourceProperties.cli_remediation
target.process.command_line_history
sourceProperties.OpenPorts.UDP
target.resource.attribute.labels.key/value[sourceProperties_OpenPorts_UDP]
sourceProperties.HasAdminRoles
target.resource.attribute.labels.key/value [sourceProperties_HasAdminRoles]
sourceProperties.HasEditRoles
target.resource.attribute.labels.key/value [sourceProperties_HasEditRoles]
sourceProperties.AllowedIpRange
target.resource.attribute.labels.key/value [sourceProperties_AllowedIpRange]
sourceProperties.ExternalSourceRanges
target.resource.attribute.labels.key/value [sourceProperties_ExternalSourceRanges]
sourceProperties.ExternallyAccessibleProtocolsAndPorts.IPProtocol
target.resource.attribute.labels.key/value [sourceProperties_ExternallyAccessibleProtocolsAndPorts_IPProtocol]
sourceProperties.OpenPorts.SCTP
target.resource.attribute.labels.key/value[sourceProperties_OpenPorts_SCTP]
sourceProperties.RecommendedLogFilter
target.resource.attribute.labels.key/value [sourceProperties_RecommendedLogFilter]
sourceProperties.QualifiedLogMetricNames
target.resource.attribute.labels.key/value [sourceProperties_QualifiedLogMetricNames]
sourceProperties.HasDefaultPolicy
target.resource.attribute.labels.key/value [sourceProperties_HasDefaultPolicy]
sourceProperties.CompatibleFeatures
target.resource.attribute.labels.key/value [sourceProperties_CompatibleFeatures]
sourceProperties.TargetProxyUrl
target.url
sourceProperties.OffendingIamRolesList.description
about.user.attribute.roles.description
sourceProperties.DatabaseVersion
target.resource.attribute.label[sourceProperties_DatabaseVersion]
Field mapping reference: OBSERVATION
The following table lists the log fields of the OBSERVATION category and their corresponding UDM fields.
RawLog field
UDM mapping
findingProviderId
target.resource.attribute.labels[findingProviderId]
sourceDisplayName
target.resource.attribute.labels.key/value [sourceDisplayName]
assetDisplayName
target.asset.attribute.labels.key/value [asset_display_name]
assetId
target.asset.asset_id
Field mapping reference: ERROR
The following table lists the log fields of the ERROR category and their corresponding UDM fields.
RawLog field
UDM mapping
externalURI
about.url
sourceProperties.ReactivationCount
target.resource.attribute.labels.key/value [sourceProperties_ReactivationCount]
findingProviderId
target.resource.attribute.labels[findingProviderId]
sourceDisplayName
target.resource.attribute.labels.key/value [sourceDisplayName]
Field mapping reference: UNSPECIFIED
The following table lists the log fields of the UNSPECIFIED category and their corresponding UDM fields.
RawLog field
UDM mapping
sourceProperties.ScannerName
principal.labels.key/value [sourceProperties_ScannerName]
sourceProperties.ResourcePath
src.resource.attribute.labels.key/value [sourceProperties_ResourcePath]
sourceProperties.ReactivationCount
target.resource.attribute.labels.key/value [sourceProperties_ReactivationCount]
sourceProperties.AllowedIpRange
target.resource.attribute.labels.key/value [sourceProperties_AllowedIpRange]
sourceProperties.ExternallyAccessibleProtocolsAndPorts.IPProtocol
target.resource.attribute.labels.key/value [sourceProperties_ExternallyAccessibleProtocolsAndPorts_IPProtocol]
sourceProperties.ExternallyAccessibleProtocolsAndPorts.ports
target.resource.attribute.labels.key/value [sourceProperties_ExternallyAccessibleProtocolsAndPorts_ports
sourceDisplayName
target.resource.attribute.labels.key/value [sourceDisplayName]
Field mapping reference: POSTURE_VIOLATION
The following table lists the log fields of the POSTURE_VIOLATION category and their corresponding UDM fields.
Log field
UDM mapping
Logic
finding.resourceName
target.resource.name
If the
finding.resourceName
log field value is
not
empty, then the
finding.resourceName
log field is mapped to the
target.resource.name
UDM field.
The
project_name
field is extracted from  the
finding.resourceName
log field using the Grok pattern.
If the
project_name
field value is
not
empty, then the
project_name
field is mapped to the
target.resource_ancestors.name
UDM field.
resourceName
target.resource.name
If the
resourceName
log field value is
not
empty, then the
resourceName
log field is mapped to the
target.resource.name
UDM field.
The
project_name
field is extracted from  the
resourceName
log field using the Grok pattern.
If the
project_name
field value is
not
empty, then the
project_name
field is mapped to the
target.resource_ancestors.name
UDM field.
finding.sourceProperties.posture_revision_id
security_result.detection_fields[source_properties_posture_revision_id]
sourceProperties.posture_revision_id
security_result.detection_fields[source_properties_posture_revision_id]
sourceProperties.revision_id
security_result.detection_fields[source_properties_posture_revision_id]
finding.sourceProperties.policy_drift_details.drift_details.expected_configuration
security_result.rule_labels[policy_drift_details_expected_configuration]
sourceProperties.policy_drift_details.drift_details.expected_configuration
security_result.rule_labels[policy_drift_details_expected_configuration]
finding.sourceProperties.policy_drift_details.drift_details.detected_configuration
security_result.rule_labels[policy_drift_details_detected_configuration]
sourceProperties.policy_drift_details.drift_details.detected_configuration
security_result.rule_labels[policy_drift_details_detected_configuration]
finding.sourceProperties.policy_drift_details.field_name
security_result.rule_labels[policy_drift_details_field_name]
sourceProperties.policy_drift_details.field_name
security_result.rule_labels[policy_drift_details_field_name]
finding.sourceProperties.changed_policy
security_result.detection_fields[changed_policy]
sourceProperties.changed_policy
security_result.detection_fields[changed_policy]
finding.sourceProperties.posture_deployment_resource
security_result.detection_fields[source_properties_posture_deployment_resource]
sourceProperties.posture_deployment_resource
security_result.detection_fields[source_properties_posture_deployment_resource]
finding.sourceProperties.posture_name
security_results.rule_name
sourceProperties.posture_name
security_results.rule_name
sourceProperties.name
security_results.rule_name
finding.sourceProperties.posture_deployment_name
security_result.detection_fields[source_properties_posture_deployment_name]
sourceProperties.posture_deployment_name
security_result.detection_fields[source_properties_posture_deployment_name]
sourceProperties.posture_deployment
security_result.detection_fields[source_properties_posture_deployment_name]
finding.propertyDataTypes.policy_drift_details.listValues.propertyDataTypes.structValue.fields.drift_details.structValue.fields.expected_configuration.primitiveDataType
security_result.rule_labels[expected_configuration_primitive_data_type]
propertyDataTypes.policy_drift_details.listValues.propertyDataTypes.structValue.fields.drift_details.structValue.fields.expected_configuration.primitiveDataType
security_result.rule_labels[expected_configuration_primitive_data_type]
finding.propertyDataTypes.policy_drift_details.listValues.propertyDataTypes.structValue.fields.drift_details.structValue.fields.detected_configuration.primitiveDataType
security_result.rule_labels[detected_configuration_primitive_data_type]
propertyDataTypes.policy_drift_details.listValues.propertyDataTypes.structValue.fields.drift_details.structValue.fields.detected_configuration.primitiveDataType
security_result.rule_labels[detected_configuration_primitive_data_type]
finding.propertyDataTypes.policy_drift_details.listValues.propertyDataTypes.structValue.fields.field_name.primitiveDataType
security_result.rule_labels[field_name_primitive_data_type]
propertyDataTypes.policy_drift_details.listValues.propertyDataTypes.structValue.fields.field_name.primitiveDataType
security_result.rule_labels[field_name_primitive_data_type]
finding.propertyDataTypes.changed_policy.primitiveDataType
security_result.rule_labels[changed_policy_primitive_data_type]
propertyDataTypes.changed_policy.primitiveDataType
security_result.rule_labels[changed_policy_primitive_data_type]
finding.propertyDataTypes.posture_revision_id.primitiveDataType
security_result.detection_fields[posture_revision_id_primitiveDataType]
propertyDataTypes.posture_revision_id.primitiveDataType
security_result.detection_fields[posture_revision_id_primitiveDataType]
finding.propertyDataTypes.posture_name.primitiveDataType
security_result.detection_fields[posture_name_primitiveDataType]
propertyDataTypes.posture_name.primitiveDataType
security_result.detection_fields[posture_name_primitiveDataType]
finding.propertyDataTypes.posture_deployment_name.primitiveDataType
security_result.detection_fields[posture_deployment_name_primitiveDataType]
propertyDataTypes.posture_deployment_name.primitiveDataType
security_result.detection_fields[posture_deployment_name_primitiveDataType]
finding.propertyDataTypes.posture_deployment_resource.primitiveDataType
security_result.detection_fields[posture_deployment_resource_primitiveDataType]
propertyDataTypes.posture_deployment_resource.primitiveDataType
security_result.detection_fields[posture_deployment_resource_primitiveDataType]
finding.originalProviderId
target.resource.attribute.labels[original_provider_id]
originalProviderId
target.resource.attribute.labels[original_provider_id]
finding.securityPosture.name
security_result.detection_fields[security_posture_name]
securityPosture.name
security_result.detection_fields[security_posture_name]
finding.securityPosture.revisionId
security_result.detection_fields[security_posture_revision_id]
securityPosture.revisionId
security_result.detection_fields[security_posture_revision_id]
finding.securityPosture.postureDeploymentResource
security_result.detection_fields[posture_deployment_resource]
securityPosture.postureDeploymentResource
security_result.detection_fields[posture_deployment_resource]
finding.securityPosture.postureDeployment
security_result.detection_fields[posture_deployment]
securityPosture.postureDeployment
security_result.detection_fields[posture_deployment]
finding.securityPosture.changedPolicy
security_result.rule_labels[changed_policy]
securityPosture.changedPolicy
security_result.rule_labels[changed_policy]
finding.cloudProvider
about.resource.attribute.cloud.environment
If the
finding.cloudProvider
log field value contains one of the following values, then the
finding.cloudProvider
log field is mapped to the
about.resource.attribute.cloud.environment
UDM field.
MICROSOFT_AZURE
GOOGLE_CLOUD_PLATFORM
AMAZON_WEB_SERVICES
.
finding.files.path
target.file.full_path
Iterate through log field
finding.files
, then
If the
index
value is equal to
0
then,
finding.files.path
log field is mapped to the
target.file.full_path
UDM field.
Else,
finding.files.path
log field is mapped to the
about.file.full_path
UDM field.
files.path
target.file.full_path
Iterate through log field
files
, then
If the
index
value is equal to
0
then,
files.path
log field is mapped to the
target.file.full_path
UDM field.
Else,
files.path
log field is mapped to the
about.file.full_path
UDM field.
finding.files.size
target.file.size
Iterate through log field
finding.files
, then
If the
index
value is equal to
0
then,
finding.files.size
log field is mapped to the
target.file.size
UDM field.
Else,
finding.files.size
log field is mapped to the
about.file.size
UDM field.
files.size
target.file.size
Iterate through log field
files
, then
If the
index
value is equal to
0
then,
files.size
log field is mapped to the
target.file.size
UDM field.
Else,
files.size
log field is mapped to the
about.file.size
UDM field.
finding.files.sha256
target.file.sha256
Iterate through log field
finding.files
, then
If the
index
value is equal to
0
then, If
finding.files.size
value is equal to
finding.files.hashedSize
then
finding.files.sha256
log field is mapped to the
target.file.sha256
UDM field.
Else, If
finding.files.size
value is equal to
finding.files.hashedSize
then
finding.files.sha256
log field is mapped to the
about.file.sha256
UDM field.
files.sha256
target.file.sha256
Iterate through log field
files
, then
If the
index
value is equal to
0
then, If
files.size
value is equal to
files.hashedSize
then
files.sha256
log field is mapped to the
target.file.sha256
UDM field.
Else, If
files.size
value is equal to
files.hashedSize
then
files.sha256
log field is mapped to the
about.file.sha256
UDM field.
finding.files.hashedSize
additional.fields
Iterate through log field
finding.files
, then
the
additional.fields.key
UDM field is set to
file_hashedSize_%{index}
and
finding.files.hashedSize
log field is mapped to the
additional.fields.value.string_value
UDM field.
files.hashedSize
additional.fields
Iterate through log field
files
, then
the
additional.fields.key
UDM field is set to
file_hashedSize_%{index}
and
files.hashedSize
log field is mapped to the
additional.fields.value.string_value
UDM field.
finding.files.partiallyHashed
additional.fields
Iterate through log field
finding.files
, then
the
additional.fields.key
UDM field is set to
file_partiallyHashed_%{index}
and
finding.files.partiallyHashed
log field is mapped to the
additional.fields.value.string_value
UDM field.
files.partiallyHashed
additional.fields
Iterate through log field
files
, then
the
additional.fields.key
UDM field is set to
file_partiallyHashed_%{index}
and
files.partiallyHashed
log field is mapped to the
additional.fields.value.string_value
UDM field.
finding.files.contents
additional.fields
Iterate through log field
finding.files
, then
the
additional.fields.key
UDM field is set to
file_contents_%{index}
and
finding.files.contents
log field is mapped to the
additional.fields.value.string_value
UDM field.
files.contents
additional.fields
Iterate through log field
files
, then
the
additional.fields.key
UDM field is set to
file_contents_%{index}
and
files.contents
log field is mapped to the
additional.fields.value.string_value
UDM field.
finding.files.diskPath.partitionUuid
additional.fields
Iterate through log field
finding.files
, then
the
additional.fields.key
UDM field is set to
file_diskPath_partitionUuid_%{index}
and
finding.files.diskPath.partitionUuid
log field is mapped to the
additional.fields.value.string_value
UDM field.
files.diskPath.partitionUuid
additional.fields
Iterate through log field
files
, then
the
additional.fields.key
UDM field is set to
file_diskPath_partitionUuid_%{index}
and
files.diskPath.partitionUuid
log field is mapped to the
additional.fields.value.string_value
UDM field.
finding.files.diskPath.relativePath
additional.fields
Iterate through log field
finding.files
, then
the
additional.fields.key
UDM field is set to
file_diskPath_relativePath_%{index}
and
finding.files.diskPath.relativePath
log field is mapped to the
additional.fields.value.string_value
UDM field.
files.diskPath.relativePath
additional.fields
Iterate through log field
files
, then
the
additional.fields.key
UDM field is set to
file_diskPath_relativePath_%{index}
and
files.diskPath.relativePath
log field is mapped to the
additional.fields.value.string_value
UDM field.
finding.files.operations.type
additional.fields
Iterate through log field
finding.files
, then
the
additional.fields.key
UDM field is set to
file_operations_type_%{index}
and
finding.files.operations.type
log field is mapped to the
additional.fields.value.string_value
UDM field.
files.operations.type
additional.fields
Iterate through log field
files
, then
the
additional.fields.key
UDM field is set to
file_operations_type_%{index}
and
files.operations.type
log field is mapped to the
additional.fields.value.string_value
UDM field.
cloudProvider
about.resource.attribute.cloud.environment
If the
cloudProvider
log field value contains one of the following values, then the
cloudProvider
log field is mapped to the
about.resource.attribute.cloud.environment
UDM field.
MICROSOFT_AZURE
GOOGLE_CLOUD_PLATFORM
AMAZON_WEB_SERVICES
.
resource.cloudProvider
target.resource.attribute.cloud.environment
If the
resource.cloudProvider
log field value contains one of the following values, then the
resource.cloudProvider
log field is mapped to the
target.resource.attribute.cloud.environment
UDM field.
MICROSOFT_AZURE
GOOGLE_CLOUD_PLATFORM
AMAZON_WEB_SERVICES
.
resource.organization
target.resource.attribute.labels[resource_organization]
resource.gcpMetadata.organization
target.resource.attribute.labels[resource_organization]
resource.service
target.resource_ancestors.name
resource.resourcePath.nodes.nodeType
target.resource_ancestors.resource_subtype
resource.resourcePath.nodes.id
target.resource_ancestors.product_object_id
resource.resourcePath.nodes.displayName
target.resource_ancestors.name
resource.resourcePathString
target.resource.attribute.labels[resource_path_string]
finding.risks.riskCategory
security_result.detection_fields[risk_category]
finding.securityPosture.policyDriftDetails.field
security_result.rule_labels[policy_drift_details_field]
finding.securityPosture.policyDriftDetails.expectedValue
security_result.rule_labels[policy_drift_details_expected_value]
finding.securityPosture.policyDriftDetails.detectedValue
security_result.rule_labels[policy_drift_details_detected_value]
finding.securityPosture.policySet
security_result.rule_set
sourceProperties.categories
security_result.detection_fields[source_properties_categories]
Field mapping reference: CHOKEPOINT
The following table lists the log fields of the CHOKEPOINT category and their corresponding UDM fields.
Log field
UDM mapping
Logic
finding.chokepoint.relatedFindings
about.resource.attribute.labels.key/value [chokepoint_relatedFindings]
Iterate through log field
finding.chokepoint.relatedFindings
, then
the
about.resource.attribute.labels.key
UDM field is set to
chokepoint_relatedFindings_%{index}
and
finding.chokepoint.relatedFindings
log field is mapped to the
about.resource.attribute.labels.value
UDM field.
finding.originalProviderId
target.resource.attribute.labels[original_provider_id]
resource.cloudProvider
target.resource.attribute.cloud.environment
If the
resource.cloudProvider
log field value contains one of the following values, then the
resource.cloudProvider
log field is mapped to the
target.resource.attribute.cloud.environment
UDM field.
MICROSOFT_AZURE
GOOGLE_CLOUD_PLATFORM
AMAZON_WEB_SERVICES
.
resource.resourcePath.nodes.nodeType
target.resource_ancestors.resource_subtype
resource.resourcePath.nodes.id
target.resource_ancestors.product_object_id
resource.resourcePath.nodes.displayName
target.resource_ancestors.name
resource.organization
target.resource.attribute.labels[resource_organization]
Field mapping reference: SENSITIVE_DATA_RISK
The following table lists the log fields for the
SENSITIVE_DATA_RISK
category and their corresponding UDM fields.
Log field
UDM mapping
Logic
finding.dataAccessEvents.eventId
security_result.detection_fields.key/value[dataAccessEvents_%{index}_eventId]
Iterate through log field
finding.dataAccessEvents
, then
if the
finding.dataAccessEvents.eventId
log field value is
not
empty then,
dataAccessEvents_%{index}_eventId
log field is mapped to the
security_result.detection_fields.key
UDM field and
finding.dataAccessEvent.eventId
log field is mapped to the
security_result.detection_fields.value
UDM field.
finding.dataAccessEvents.principalEmail
principal.user.email_addresses
finding.dataAccessEvents.operation
security_result.action_details
Iterate through log field
finding.dataAccessEvents
, then
if the
index
value is equal to
0
and if the
finding.dataAccessEvents.operation
log field value is
not
empty then,
finding.dataAccessEvents.operation
log field is mapped to the
security_result.action_details
UDM field.
Else,
dataAccessEvents_%{index}_operation
log field is mapped to the
security_result.detection_fields.key
UDM field and
Operation: %{finding.dataAccessEvent.operation}
log field is mapped to the
security_result.detection_fields.value
UDM field.
finding.dataAccessEvents.eventTime
additional.fields[dataAccessEvents_%{index}_eventTime]
Iterate through log field
finding.dataAccessEvents
, then
if the
finding.dataAccessEvents.eventTime
log field value is
not
empty then,
dataAccessEvents_%{index}_eventTime
log field is mapped to the
additional.fields.key
UDM field and
finding.dataAccessEvents.eventTime
log field is mapped to the
additional.fields.value
UDM field.
finding.dataFlowEvents.eventId
security_result.detection_fields.key/value[dataFlowEvents_%{index}_eventId]
Iterate through log field
finding.dataFlowEvents
, then
if the
finding.dataFlowEvents.eventId
log field value is
not
empty then,
dataFlowEvents_%{index}_eventId
log field is mapped to the
security_result.detection_fields.key
UDM field and
finding.dataFlowEvents.eventId
log field is mapped to the
security_result.detection_fields.value
UDM field.
finding.dataFlowEvents.principalEmail
principal.user.email_addresses
finding.dataFlowEvents.operation
security_result.detection_fields.key/value[dataFlowEvents_%{index}_operation]
Iterate through log field
finding.dataFlowEvents
, then
if the
finding.dataFlowEvents.operation
log field value is
not
empty then,
dataFlowEvents_%{index}_operation
log field is mapped to the
security_result.detection_fields.key
UDM field and
Operation: %{finding.dataFlowEvents.operation}
log field is mapped to the
security_result.detection_fields.value
UDM field.
finding.dataFlowEvents.violatedLocation
about.location.name
finding.dataFlowEvents.eventTime
additional.fields[dataFlowEvents_%{index}_eventTime]
Iterate through log field
finding.dataFlowEvents
, then
if the
finding.dataFlowEvents.eventTime
log field value is
not
empty then,
dataFlowEvents_%{index}_eventTime
log field is mapped to the
additional.fields.key
UDM field and
finding.dataFlowEvents.eventTime
log field is mapped to the
additional.fields.value
UDM field.
Common Fields: SECURITY COMMAND CENTER - VULNERABILITY, MISCONFIGURATION, OBSERVATION, ERROR, UNSPECIFIED, POSTURE_VIOLATION, TOXIC_COMBINATION CHOKEPOINT, SENSITIVE_DATA_RISK
The following table lists common fields of the SECURITY COMMAND CENTER -
VULNERABILITY
,
MISCONFIGURATION
,
OBSERVATION
,
ERROR
,
UNSPECIFIED
,
POSTURE_VIOLATION
,
TOXIC_COMBINATION
,
CHOKEPOINT
,
SENSITIVE_DATA_RISK
categories and their corresponding UDM fields.
RawLog field
UDM mapping
Logic
compliances.ids
security_result.detection_fields[compliances_id]
compliances.version
security_result.detection_fields[compliances_version]
compliances.standard
security_result.detection_fields[compliances_standard]
connections.destinationIp
about.labels [connections_destination_ip]
(deprecated)
If the
connections.destinationIp
log field value is
not
equal to the
sourceProperties.properties.ipConnection.destIp
, then the
connections.destinationIp
log field is mapped to the
about.labels.value
UDM field.
connections.destinationIp
additional.fields [connections_destination_ip]
If the
connections.destinationIp
log field value is
not
equal to the
sourceProperties.properties.ipConnection.destIp
, then the
connections.destinationIp
log field is mapped to the
additional.fields.value
UDM field.
connections.destinationPort
about.labels [connections_destination_port]
(deprecated)
connections.destinationPort
additional.fields [connections_destination_port]
connections.protocol
about.labels [connections_protocol]
(deprecated)
connections.protocol
additional.fields [connections_protocol]
connections.sourceIp
about.labels [connections_source_ip]
(deprecated)
connections.sourceIp
additional.fields [connections_source_ip]
connections.sourcePort
about.labels [connections_source_port]
(deprecated)
connections.sourcePort
additional.fields [connections_source_port]
kubernetes.pods.ns
target.resource.attribute.labels.key/value [kubernetes_pods_ns]
kubernetes.pods.name
target.resource.attribute.labels[kubernetes_pods_name]
kubernetes.nodes.name
target.resource.attribute.labels[kubernetes_nodes_name]
kubernetes.nodePools.name
target.resource.attribute.labels[kubernetes_nodePools_name]
target.resource_ancestors.resource_type
The
target.resource_ancestors.resource_type
UDM field is set to
CLUSTER
.
about.resource.attribute.cloud.environment
The
about.resource.attribute.cloud.environment
UDM field is set to
GOOGLE_CLOUD_PLATFORM
.
externalSystems.assignees
additional.fields[externalSystems_assignees]
externalSystems.status
about.resource.attribute.labels.key/value [externalSystems_status]
kubernetes.nodePools.nodes.name
target.resource.attribute.labels.key/value [kubernetes_nodePools_nodes_name]
kubernetes.pods.containers.uri
target.resource.attribute.labels.key/value [kubernetes_pods_containers_uri]
kubernetes.roles.kind
target.resource.attribute.labels.key/value [kubernetes_roles_kind]
kubernetes.roles.name
target.resource.attribute.labels.key/value [kubernetes_roles_name]
kubernetes.roles.ns
target.resource.attribute.labels.key/value [kubernetes_roles_ns]
kubernetes.pods.containers.labels.name/value
target.resource.attribute.labels.key/value [kubernetes.pods.containers.labels.name/value]
kubernetes.pods.labels.name/value
target.resource.attribute.labels.key/value [kubernetes.pods.labels.name/value]
externalSystems.externalSystemUpdateTime
about.resource.attribute.last_update_time
externalSystems.name
about.resource.name
externalSystems.externalUid
about.resource.product_object_id
indicator.uris
about.url
vulnerability.cve.references.uri
extensions.vulns.vulnerabilities.about.labels [vulnerability.cve.references.uri]
(deprecated)
vulnerability.cve.references.uri
additional.fields [vulnerability.cve.references.uri]
vulnerability.cve.cvssv3.attackComplexity
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_attackComplexity]
(deprecated)
vulnerability.cve.cvssv3.attackComplexity
additional.fields [vulnerability_cve_cvssv3_attackComplexity]
vulnerability.cve.cvssv3.availabilityImpact
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_availabilityImpact]
(deprecated)
vulnerability.cve.cvssv3.availabilityImpact
additional.fields [vulnerability_cve_cvssv3_availabilityImpact]
vulnerability.cve.cvssv3.confidentialityImpact
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_confidentialityImpact]
(deprecated)
vulnerability.cve.cvssv3.confidentialityImpact
additional.fields [vulnerability_cve_cvssv3_confidentialityImpact]
vulnerability.cve.cvssv3.integrityImpact
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_integrityImpact]
(deprecated)
vulnerability.cve.cvssv3.integrityImpact
additional.fields [vulnerability_cve_cvssv3_integrityImpact]
vulnerability.cve.cvssv3.privilegesRequired
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_privilegesRequired]
(deprecated)
vulnerability.cve.cvssv3.privilegesRequired
additional.fields [vulnerability_cve_cvssv3_privilegesRequired]
vulnerability.cve.cvssv3.scope
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_scope]
(deprecated)
vulnerability.cve.cvssv3.scope
additional.fields [vulnerability_cve_cvssv3_scope]
vulnerability.cve.cvssv3.userInteraction
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_cvssv3_userInteraction]
(deprecated)
vulnerability.cve.cvssv3.userInteraction
additional.fields [vulnerability_cve_cvssv3_userInteraction]
vulnerability.cve.references.source
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_references_source]
(deprecated)
vulnerability.cve.references.source
additional.fields [vulnerability_cve_references_source]
vulnerability.cve.upstreamFixAvailable
extensions.vulns.vulnerabilities.about.labels [vulnerability_cve_upstreamFixAvailable]
(deprecated)
vulnerability.cve.upstreamFixAvailable
additional.fields [vulnerability_cve_upstreamFixAvailable]
vulnerability.cve.id
extensions.vulns.vulnerabilities.cve_id
vulnerability.cve.cvssv3.baseScore
extensions.vulns.vulnerabilities.cvss_base_score
vulnerability.cve.cvssv3.attackVector
extensions.vulns.vulnerabilities.cvss_vector
vulnerability.cve.impact
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_cve_impact]
vulnerability.cve.exploitationActivity
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_cve_exploitation_activity]
vulnerability.cve.exploitReleaseDate
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_cve_exploit_release_date]
vulnerability.cve.firstExploitationDate
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_cve_first_exploitation_date]
parentDisplayName
metadata.description
eventTime
metadata.event_timestamp
category
metadata.product_event_type
sourceProperties.evidence.sourceLogId.insertId
metadata.product_log_id
If the
canonicalName
log field value is
not
empty, then the
finding_id
is extracted from the
canonicalName
log field using a Grok pattern.
If the
finding_id
log field value is empty, then the
sourceProperties.evidence.sourceLogId.insertId
log field is mapped to the
metadata.product_log_id
UDM field.
If the
canonicalName
log field value is empty, then the
sourceProperties.evidence.sourceLogId.insertId
log field is mapped to the
metadata.product_log_id
UDM field.
sourceProperties.contextUris.cloudLoggingQueryUri.url
security_result.detection_fields.key/value[sourceProperties_contextUris_cloudLoggingQueryUri_url]
sourceProperties.sourceId.customerOrganizationNumber
principal.resource.attribute.labels.key/value [sourceProperties_sourceId_customerOrganizationNumber]
If the
message
log field value matches the regular expression
sourceProperties.sourceId.*?customerOrganizationNumber
, then the
sourceProperties.sourceId.customerOrganizationNumber
log field is mapped to the
principal.resource.attribute.labels.value
UDM field.
resource.projectName
target.resource.attribute.labels[resource_projectName]
resource.gcpMetadata.project
target.resource.attribute.labels[resource_gcpMetadata_project]
principal.user.account_type
If the
access.principalSubject
log field value matches the regular expression
serviceAccount
, then the
principal.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
Else if, the
access.principalSubject
log field value matches the regular expression
user
, then the
principal.user.account_type
UDM field is set to
CLOUD_ACCOUNT_TYPE
.
access.principalSubject
principal.user.attribute.labels.key/value [access_principalSubject]
access.serviceAccountDelegationInfo.principalSubject
principal.user.attribute.labels.key/value [access_serviceAccountDelegationInfo_principalSubject]
access.serviceAccountKeyName
principal.user.attribute.labels.key/value [access_serviceAccountKeyName]
access.principalEmail
principal.user.email_addresses
If the
access.principalEmail
log field value is
not
empty and the
access.principalEmail
log field value matches the regular expression
^.+@.+$
, then the
access.principalEmail
log field is mapped to the
principal.user.email_addresses
UDM field.
access.principalEmail
principal.user.userid
If the
access.principalEmail
log field value is
not
empty and the
access.principalEmail
log field value does not match the regular expression
^.+@.+$
, then the
access.principalEmail
log field is mapped to the
principal.user.userid
UDM field.
database.userName
additional.fields[database_userName]
workflowState
security_result.about.investigation.status
sourceProperties.findingId
metadata.product_log_id
kubernetes.accessReviews.group
target.resource.attribute.labels.key/value [kubernetes_accessReviews_group]
kubernetes.accessReviews.name
target.resource.attribute.labels.key/value [kubernetes_accessReviews_name]
kubernetes.accessReviews.ns
target.resource.attribute.labels.key/value [kubernetes_accessReviews_ns]
kubernetes.accessReviews.resource
target.resource.attribute.labels.key/value [kubernetes_accessReviews_resource]
kubernetes.accessReviews.subresource
target.resource.attribute.labels.key/value [kubernetes_accessReviews_subresource]
kubernetes.accessReviews.verb
target.resource.attribute.labels.key/value [kubernetes_accessReviews_verb]
kubernetes.accessReviews.version
target.resource.attribute.labels.key/value [kubernetes_accessReviews_version]
kubernetes.bindings.name
security_result.about.resource.attribute.labels.key/value [kubernetes_bindings_name]
kubernetes.bindings.ns
target.resource.attribute.labels.key/value [kubernetes_bindings_ns]
kubernetes.bindings.role.kind
target.resource.attribute.labels.key/value [kubernetes_bindings_role_kind]
kubernetes.bindings.role.ns
target.resource.attribute.labels.key/value [kubernetes_bindings_role_ns]
kubernetes.bindings.subjects.kind
target.resource.attribute.labels.key/value [kubernetes_bindings_subjects_kind]
kubernetes.bindings.subjects.name
target.resource.attribute.labels.key/value [kubernetes_bindings_subjects_name]
kubernetes.bindings.subjects.ns
target.resource.attribute.labels.key/value [kubernetes_bindings_subjects_ns]
kubernetes.bindings.role.name
target.resource.attribute.roles.name
security_result.about.user.attribute.roles.name
If the
message
log field value matches the regular expression
contacts.?security
, then the
security_result.about.user.attribute.roles.name
UDM field is set to
security
.
If the
message
log field value matches the regular expression
contacts.?technical
, then the
security_result.about.user.attribute.roles.name
UDM field is set to
Technical
.
contacts.security.contacts.email
security_result.about.user.email_addresses
contacts.technical.contacts.email
security_result.about.user.email_addresses
security_result.alert_state
If the
state
log field value is equal to
ACTIVE
, then the
security_result.alert_state
UDM field is set to
ALERTING
.
Else, the
security_result.alert_state
UDM field is set to
NOT_ALERTING
.
findingClass, category
security_result.catgory_details
The
findingClass - category
log field is mapped to the
security_result.catgory_details
UDM field.
description
security_result.description
indicator.signatures.memoryHashSignature.binaryFamily
security_result.detection_fields.key/value [indicator_signatures_memoryHashSignature_binaryFamily]
indicator.signatures.memoryHashSignature.detections.binary
security_result.detection_fields.key/value [indicator_signatures_memoryHashSignature_detections_binary]
indicator.signatures.memoryHashSignature.detections.percentPagesMatched
security_result.detection_fields.key/value [indicator_signatures_memoryHashSignature_detections_percentPagesMatched]
indicator.signatures.yaraRuleSignature.yararule
security_result.detection_fields.key/value [indicator_signatures_yaraRuleSignature_yararule]
mitreAttack.additionalTactics
security_result.attack_details.tactics.name
mitreAttack.additionalTechniques
security_result.attack_details.techniques.name
mitreAttack.primaryTactic
security_result.attack_details.tactics.name
mitreAttack.primaryTechniques.0
security_result.attack_details.techniques.name
mitreAttack.version
security_result.attack_details.version
muteInitiator
security_result.detection_fields.key/value [mute_initiator]
If the
mute
log field value is equal to
MUTED
or
UNMUTED
, then the
muteInitiator
log field is mapped to the
security_result.detection_fields.value
UDM field.
muteUpdateTime
security_result.detection_fields.key/value [mute_update_time]
If the
mute
log field value is equal to
MUTED
or
UNMUTED
, then the
muteUpdateTimer
log field is mapped to the
security_result.detection_fields.value
UDM field.
mute
security_result.detection_fields.key/value [mute]
securityMarks.canonicalName
security_result.detection_fields.key/value [securityMarks_cannonicleName]
securityMarks.marks
security_result.detection_fields.key/value [securityMarks_marks]
securityMarks.name
security_result.detection_fields.key/value [securityMarks_name]
sourceProperties.detectionCategory.indicator
security_result.detection_fields.key/value [sourceProperties_detectionCategory_indicator]
sourceProperties.detectionCategory.technique
security_result.detection_fields.key/value [sourceProperties_detectionCategory_technique]
sourceProperties.contextUris.mitreUri.url
security_result.detection_fields[sourceProperties_contextUris_mitreUri_url]
sourceProperties.contextUris.mitreUri.displayName
security_result.detection_fields[sourceProperties_contextUris_mitreUri_displayName]
sourceProperties.contextUris.relatedFindingUri.url
security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_url]
sourceProperties.contextUris.relatedFindingUri.displayName
security_result.detection_fields[sourceProperties_contextUris_relatedFindingUri_displayName]
sourceProperties.contextUris.virustotalIndicatorQueryUri.url
security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_url]
sourceProperties.contextUris.virustotalIndicatorQueryUri.displayName
security_result.detection_fields[sourceProperties_contextUris_virustotalIndicatorQueryUri_displayName]
sourceProperties.contextUris.workspacesUri.url
security_result.detection_fields[sourceProperties_contextUris_workspacesUri_url]
sourceProperties.contextUris.workspacesUri.displayName
security_result.detection_fields[sourceProperties_contextUris_workspacesUri_displayName]
createTime
metadata.collected_timestamp
nextSteps
security_result.outcomes.key/value [next_steps]
sourceProperties.detectionPriority
security_result.priority
If the
sourceProperties.detectionPriority
log field value is equal to
HIGH
, then the
security_result.priority
UDM field is set to
HIGH_PRIORITY
.
Else if, the
sourceProperties.detectionPriority
log field value is equal to
MEDIUM
, then the
security_result.priority
UDM field is set to
MEDIUM_PRIORITY
.
Else if, the
sourceProperties.detectionPriority
log field value is equal to
LOW
, then the
security_result.priority
UDM field is set to
LOW_PRIORITY
.
sourceProperties.detectionCategory.subRuleName
security_result.rule_labels.key/value [sourceProperties_detectionCategory_subRuleName]
sourceProperties.detectionCategory.ruleName
security_result.rule_name
severity
security_result.severity
name
security_result.url_back_to_product
database.query
target.process.command_line
resource.folders.resourceFolderDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_folders_resourceFolderDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.folders.resourceFolderDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
Else, the
resource.folders.resourceFolderDisplayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.gcpMetadata.folders.resourceFolderDisplay
src.resource_ancestors.attribute.labels.key/value [resource_folders_resourceFolderDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.gcpMetadata.folders.resourceFolderDisplay
log field is mapped to the
src.resource_ancestors.attribute.labels.value
UDM field.
Else, the
resource.gcpMetadata.folders.resourceFolderDisplay
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.gcpMetadata.folders.resourceFolder
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.gcpMetadata.folders.resourceFolder
log field is mapped to the
src.resource_ancestors.name
UDM field.
Else, the
resource.gcpMetadata.folders.resourceFolder
log field is mapped to the
target.resource_ancestors.name
UDM field.
resource.organization
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.organization
log field is mapped to the
src.resource_ancestors.name
UDM field.
Else, the
resource.organization
log field is mapped to the
target.resource_ancestors.name
UDM field.
resource.gcpMetadata.organization
src.resource_ancestors.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.gcpMetadata.organization
log field is mapped to the
src.resource_ancestors.name
UDM field.
Else, the
resource.gcpMetadata.organization
log field is mapped to the
target.resource_ancestors.name
UDM field.
resource.parentDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_parentDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.parentDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.key/value
UDM field.
Else, the
resource.parentDisplayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.gcpMetadata.parentDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_parentDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.gcpMetadata.parentDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.key/value
UDM field.
Else, the
resource.gcpMetadata.parentDisplayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.parentName
src.resource_ancestors.attribute.labels.key/value [resource_parentName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.parentName
log field is mapped to the
src.resource_ancestors.attribute.labels.key/value
UDM field.
Else, the
resource.parentName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.gcpMetadata.parent
src.resource_ancestors.attribute.labels.key/value [resource_parentName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.gcpMetadata.parent
log field is mapped to the
src.resource_ancestors.attribute.labels.key/value
UDM field.
Else, the
resource.gcpMetadata.parent
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.projectDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_projectDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.projectDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.key/value
UDM field.
Else, the
resource.projectDisplayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.gcpMetadata.projectDisplayName
src.resource_ancestors.attribute.labels.key/value [resource_projectDisplayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.gcpMetadata.projectDisplayName
log field is mapped to the
src.resource_ancestors.attribute.labels.key/value
UDM field.
Else, the
resource.gcpMetadata.projectDisplayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.type
src.resource_ancestors.resource_subtype
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.type
log field is mapped to the
src.resource_ancestors.resource_subtype
UDM field.
database.displayName
target.resource.attribute.labels.key/value [database_displayName]
If the
category
log field value is equal to
Exfiltration: CloudSQL Over-Privileged Grant
, then the
database.displayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
database.grantees
target.resource.attribute.labels.key/value [database_grantees]
If the
category
log field value is equal to
Exfiltration: CloudSQL Over-Privileged Grant
, then the
target.resource.attribute.labels.key
UDM field is set to
database_grantees
and the
database.grantees
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.displayName
src.resource.attribute.labels.key/value [resource_displayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
or
Exfiltration: BigQuery Data to Google Drive
, then the
resource.displayName
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
Else, the
resource.displayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.display_name
src.resource.attribute.labels.key/value [resource_display_name]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
or
Exfiltration: BigQuery Data to Google Drive
, then the
resource.display_name
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
Else, the
resource.display_name
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.type
src.resource_ancestors.resource_subtype
If the
category
log field value is equal to
Exfiltration: BigQuery Data to Google Drive
, then the
resource.type
log field is mapped to the
src.resource_ancestors.resource_subtype
UDM field.
database.displayName
target.resource.name
If the
database.name
log field value is empty, then the
database.displayName
log field is mapped to the
target.resource.name
UDM field.
database.grantees
target.resource.attribute.labels.key/value [database_grantees]
resource.displayName
target.resource.attribute.labels.key/value [resource_displayName]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
or
Exfiltration: BigQuery Data to Google Drive
, then the
resource.displayName
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
Else, the
resource.displayName
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
resource.display_name
target.resource.attribute.labels.key/value [resource_display_name]
If the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
or
Exfiltration: BigQuery Data to Google Drive
, then the
resource.display_name
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
Else, the
resource.display_name
log field is mapped to the
target.resource.attribute.labels.value
UDM field.
exfiltration.sources.components
src.resource.attribute.labels.key/value[exfiltration_sources_components]
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: BigQuery Data Extraction
, then the
exfiltration.sources.components
log field is mapped to the
src.resource.attribute.labels.value
UDM field.
resourceName
src.resource.name
If the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: BigQuery Data Exfiltration
, then the
resourceName
log field is mapped to the
src.resource.name
UDM field.
database.name
src.resource.name
exfiltration.sources.name
src.resource.name
access.serviceName
target.application
If the
category
log field value is equal to
Defense Evasion: Modify VPC Service Control
or
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
or
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: CloudSQL Restore Backup to External Organization
or
Exfiltration: CloudSQL Over-Privileged Grant
or
Persistence: New Geography
or
Persistence: IAM Anomalous Grant
, then the
access.serviceName
log field is mapped to the
target.application
UDM field.
access.methodName
target.labels [access_methodName]
(deprecated)
access.methodName
additional.fields [access_methodName]
processes.argumentsTruncated
target.labels [processes_argumentsTruncated]
(deprecated)
processes.argumentsTruncated
additional.fields [processes_argumentsTruncated]
processes.binary.contents
target.labels [processes_binary_contents]
(deprecated)
processes.binary.contents
additional.fields [processes_binary_contents]
processes.binary.hashedSize
target.labels [processes_binary_hashedSize]
(deprecated)
processes.binary.hashedSize
additional.fields [processes_binary_hashedSize]
processes.binary.partiallyHashed
target.labels [processes_binary_partiallyHashed]
(deprecated)
processes.binary.partiallyHashed
additional.fields [processes_binary_partiallyHashed]
processes.envVariables.name
target.labels [processes_envVariables_name]
(deprecated)
processes.envVariables.name
additional.fields [processes_envVariables_name]
processes.envVariables.val
target.labels [processes_envVariables_val]
(deprecated)
processes.envVariables.val
additional.fields [processes_envVariables_val]
processes.envVariablesTruncated
target.labels [processes_envVariablesTruncated]
(deprecated)
processes.envVariablesTruncated
additional.fields [processes_envVariablesTruncated]
processes.libraries.contents
target.labels [processes_libraries_contents]
(deprecated)
processes.libraries.contents
additional.fields [processes_libraries_contents]
processes.libraries.hashedSize
target.labels [processes_libraries_hashedSize]
(deprecated)
processes.libraries.hashedSize
additional.fields [processes_libraries_hashedSize]
processes.libraries.partiallyHashed
target.labels [processes_libraries_partiallyHashed]
(deprecated)
processes.libraries.partiallyHashed
additional.fields [processes_libraries_partiallyHashed]
processes.script.contents
target.labels [processes_script_contents]
(deprecated)
processes.script.contents
additional.fields [processes_script_contents]
processes.script.hashedSize
target.labels [processes_script_hashedSize]
(deprecated)
processes.script.hashedSize
additional.fields [processes_script_hashedSize]
processes.script.partiallyHashed
target.labels [processes_script_partiallyHashed]
(deprecated)
processes.script.partiallyHashed
additional.fields [processes_script_partiallyHashed]
processes.parentPid
target.parent_process.pid
processes.args
target.process.command_line_history [processes.args]
processes.name
target.process.file.full_path
processes.binary.path
target.process.file.full_path
processes.libraries.path
target.process.file.full_path
processes.script.path
target.process.file.full_path
processes.binary.sha256
target.process.file.sha256
processes.libraries.sha256
target.process.file.sha256
processes.script.sha256
target.process.file.sha256
processes.binary.size
target.process.file.size
processes.libraries.size
target.process.file.size
processes.script.size
target.process.file.size
processes.pid
target.process.pid
containers.uri
target.resource_ancestors.attribute.labels.key/value [containers_uri]
containers.labels.name/value
target.resource_ancestors.attribute.labels.key/value [containers.labels.name/value]
resourceName
target.resource_ancestors.name
If the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Persistence: GCE Admin Added SSH Key
or
Persistence: GCE Admin Added Startup Script
, then the
sourceProperties.properties.projectId
log field is mapped to the
target.resource_ancestors.name
UDM field.
parent
security_result.detection_fields[finding_parent]
sourceProperties.affectedResources.gcpResourceName
target.resource_ancestors.name
containers.name
target.resource_ancestors.name
kubernetes.pods.containers.name
target.resource.attribute.labels[kubernetes_pods_containers_name]
sourceProperties.sourceId.projectNumber
target.resource_ancestors.product_object_id
sourceProperties.sourceId.customerOrganizationNumber
target.resource_ancestors.product_object_id
sourceProperties.sourceId.organizationNumber
target.resource_ancestors.product_object_id
containers.imageId
target.resource_ancestors.product_object_id
sourceProperties.properties.zone
target.resource.attribute.cloud.availability_zone
If the
category
log field value is equal to
Brute Force: SSH
, then the
sourceProperties.properties.zone
log field is mapped to the
target.resource.attribute.cloud.availability_zone
UDM field.
canonicalName
metadata.product_log_id
The
finding_id
is extracted from the
canonicalName
log field using a Grok pattern.
If the
finding_id
log field value is
not
empty, then the
finding_id
log field is mapped to the
metadata.product_log_id
UDM field.
canonicalName
src.resource.attribute.labels.key/value [finding_id]
If the
finding_id
log field value is
not
empty, then the
finding_id
log field is mapped to the
src.resource.attribute.labels.key/value [finding_id]
UDM field.
If the
category
log field value is equal to one of the following values, then the
finding_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
src.resource.product_object_id
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
src.resource.product_object_id
UDM field.
If the
category
log field value is equal to one of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
src.resource.attribute.labels.key/value [source_id]
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
src.resource.attribute.labels.key/value [source_id]
UDM field.
If the
category
log field value is equal to one of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
target.resource.attribute.labels.key/value [finding_id]
If the
finding_id
log field value is
not
empty, then the
finding_id
log field is mapped to the
target.resource.attribute.labels.key/value [finding_id]
UDM field.
If the
category
log field value is
not
equal to any of the following values, then the
finding_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
target.resource.product_object_id
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
target.resource.product_object_id
UDM field.
If the
category
log field value is
not
equal to any of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
canonicalName
target.resource.attribute.labels.key/value [source_id]
If the
source_id
log field value is
not
empty, then the
source_id
log field is mapped to the
target.resource.attribute.labels.key/value [source_id]
UDM field.
If the
category
log field value is
not
equal to any of the following values, then the
source_id
is extracted from the
canonicalName
log field using a Grok pattern:
Exfiltration: BigQuery Data Extraction
Exfiltration: BigQuery Data to Google Drive
Exfiltration: BigQuery Data Exfiltration
Exfiltration: CloudSQL Restore Backup to External Organization
exfiltration.targets.components
target.resource.attribute.labels.key/value[exfiltration_targets_components]
If the
category
log field value is equal to
Exfiltration: CloudSQL Data Exfiltration
or
Exfiltration: BigQuery Data Extraction
, then the
exfiltration.targets.components
log field is mapped to the
target.resource.attribute.labels.key/value
UDM field.
resourceName
exfiltration.targets.name
target.resource.name
If the
category
log field value is equal to
Brute Force: SSH
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field.
Else if, the
category
log field value is equal to
Malware: Bad Domain
or
Malware: Bad IP
or
Malware: Cryptomining Bad IP
, then the
resourceName
log field is mapped to the
target.resource_ancestors.name
UDM field and the
target.resource.resource_type
UDM field is set to
VIRTUAL_MACHINE
.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Extraction
or
Exfiltration: BigQuery Data to Google Drive
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else if, the
category
log field value is equal to
Exfiltration: BigQuery Data Exfiltration
, then the
exfiltration.target.name
log field is mapped to the
target.resource.name
UDM field.
Else, the
resourceName
log field is mapped to the
target.resource.name
UDM field.
kubernetes.pods.containers.imageId
target.resource.attribute.labels[kubernetes_pods_containers_imageId]
kubernetes.pods.containers.createTime
target.resource.attribute.labels[kubernetes_pods_containers_createTime]
resource.project
target.resource.attribute.labels.key/value [resource_project]
resource.parent
target.resource_ancestor.name
processes.name
target.process.file.names
sourceProperties.Header_Signature.significantValues.value
principal.location.country_or_region
If the
sourceProperties.Header_Signature.name
log field value is equal to
RegionCode
, then the
sourceProperties.Header_Signature.significantValues.value
log field is mapped to
principal.location.country_or_region
UDM field.
sourceProperties.Header_Signature.significantValues.value
principal.ip
If the
sourceProperties.Header_Signature.name
log field value is equal to
RemoteHost
, then the
sourceProperties.Header_Signature.significantValues.value
log field is mapped to
principal.ip
UDM field.
sourceProperties.Header_Signature.significantValues.value
network.http.user_agent
If the
sourceProperties.Header_Signature.name
log field value is equal to
UserAgent
, then the
sourceProperties.Header_Signature.significantValues.value
log field is mapped to
network.http.user_agent
UDM field.
sourceProperties.Header_Signature.significantValues.value
principal.url
If the
sourceProperties.Header_Signature.name
log field value is equal to
RequestUriPath
, then the
sourceProperties.Header_Signature.significantValues.value
log field is mapped to
principal.url
UDM field.
sourceProperties.Header_Signature.significantValues.proportionInAttack
security_result.detection_fields [proportionInAttack]
sourceProperties.Header_Signature.significantValues.attackLikelihood
security_result.detection_fields [attackLikelihood]
sourceProperties.Header_Signature.significantValues.matchType
security_result.detection_fields [matchType]
sourceProperties.Header_Signature.significantValues.proportionInBaseline
security_result.detection_fields [proportionInBaseline]
sourceProperties.compromised_account
principal.user.userid
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.compromised_account
log field is mapped to
principal.user.userid
UDM field and the
principal.user.account_type
UDM field is set to
SERVICE_ACCOUNT_TYPE
.
sourceProperties.project_identifier
principal.resource.product_object_id
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.project_identifier
log field is mapped to
principal.resource.product_object_id
UDM field.
sourceProperties.private_key_identifier
principal.user.attribute.labels.key/value [private_key_identifier]
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.private_key_identifier
log field is mapped to
principal.user.attribute.labels.value
UDM field.
sourceProperties.action_taken
principal.labels [action_taken]
(deprecated)
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.action_taken
log field is mapped to
principal.labels.value
UDM field.
sourceProperties.action_taken
additional.fields [action_taken]
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.action_taken
log field is mapped to
additional.fields.value
UDM field.
sourceProperties.finding_type
principal.labels [finding_type]
(deprecated)
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.finding_type
log field is mapped to
principal.labels.value
UDM field.
sourceProperties.finding_type
additional.fields [finding_type]
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.finding_type
log field is mapped to
additional.fields.value
UDM field.
sourceProperties.url
principal.user.attribute.labels.key/value [key_file_path]
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.url
log field is mapped to
principal.user.attribute.labels.value
UDM field.
sourceProperties.security_result.summary
security_result.summary
If the
category
log field value is equal to
account_has_leaked_credentials
, then the
sourceProperties.security_result.summary
log field is mapped to
security_result.summary
UDM field.
kubernetes.objects.kind
target.resource.attribute.labels[kubernetes_objects_kind]
kubernetes.objects.ns
target.resource.attribute.labels[kubernetes_objects_ns]
kubernetes.objects.name
target.resource.attribute.labels[kubernetes_objects_name]
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_offendingPackage_packageName]
vulnerability.offendingPackage.packageName
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_offendingPackage_cpeUri]
vulnerability.offendingPackage.cpeUri
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_offendingPackage_packageType]
vulnerability.offendingPackage.packageType
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_offendingPackage_packageVersion]
vulnerability.offendingPackage.packageVersion
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_fixedPackage_packageName]
vulnerability.fixedPackage.packageName
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_fixedPackage_cpeUri]
vulnerability.fixedPackage.cpeUri
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_fixedPackage_packageType]
vulnerability.fixedPackage.packageType
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_fixedPackage_packageVersion]
vulnerability.fixedPackage.packageVersion
extensions.vulns.vulnerabilities.about.security_result.detection_fields[vulnerability_securityBulletin_bulletinId]
vulnerability.securityBulletin.bulletinId
security_result.detection_fields[vulnerability_securityBulletin_submissionTime]
vulnerability.securityBulletin.submissionTime
security_result.detection_fields[vulnerability_securityBulletin_suggestedUpgradeVersion]
vulnerability.securityBulletin.suggestedUpgradeVersion
target.location.name
resource.location
additional.fields[resource_service]
resource.service
target.resource_ancestors.attribute.labels[kubernetes_object_kind]
kubernetes.objects.kind
target.resource_ancestors.name
kubernetes.objects.name
kubernetes_res_ancestor.attribute.labels[kubernetes_objects_ns]
kubernetes.objects.ns
kubernetes_res_ancestor.attribute.labels[kubernetes_objects_group]
kubernetes.objects.group
finding.groupMemberships.groupType
security_result.about.group.attribute.labels.key/value [groupType]
Iterate through log field
finding.groupMemberships.groupType
, then
the
security_result.about.group.attribute.labels.key
UDM field is set to
groupType_%{index}
and
finding.groupMemberships.groupType
log field is mapped to the
security_result.about.group.attribute.labels.value
UDM field.
finding.groupMemberships.groupId
security_result.about.group.attribute.labels.key/value [groupId]
Iterate through log field
finding.groupMemberships.groupId
, then
the
security_result.about.group.attribute.labels.key
UDM field is set to
groupId_%{index}
and
finding.groupMemberships.groupId
log field is mapped to the
security_result.about.group.attribute.labels.value
UDM field.
finding.attackExposure.score
security_result.detection_fields.key/value [var_attackExposure_score]
finding.attackExposure.latestCalculationTime
security_result.detection_fields.key/value [var_attackExposure_latestCalculationTime]
finding.attackExposure.attackExposureResult
security_result.detection_fields.key/value [var_attackExposure_attackExposureResult]
finding.attackExposure.state
security_result.detection_fields.key/value [var_attackExposure_state]
finding.attackExposure.exposedHighValueResourcesCount
security_result.detection_fields.key/value [var_attackExposure_exposedHighValueResourcesCount]
finding.attackExposure.exposedMediumValueResourcesCount
security_result.detection_fields.key/value [var_attackExposure_exposedMediumValueResourcesCount]
finding.attackExposure.exposedLowValueResourcesCount
security_result.detection_fields.key/value [var_attackExposure_exposedLowValueResourcesCount]
finding.muteInfo.staticMute.state
security_result.detection_fields.key/value [var_static_mute_state]
finding.muteInfo.staticMute.applyTime
security_result.detection_fields.key/value [static_mute_apply_time]
finding.muteInfo.staticMute.applyTime
security_result.detection_fields.key/value [static_mute_apply_time]
resource.name
target.resource.attribute.labels[resource_name]
What's next
Data ingestion to Google Security Operations
Need more help?
Get answers from Community members and Google SecOps professionals.
