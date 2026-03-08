# Frequently Asked Questions on SOAR migration

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-soar-faq/  
**Scraped:** 2026-03-05T09:47:04.888065Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Frequently Asked Questions on SOAR migration
Supported in:
Google secops
SOAR
Get answers to common questions about the SOAR migration process. Find solutions to frequent issues and best practices for a successful transition.
Migration scope and impact
Q: Why is this migration necessary?
We're modernizing the SOAR infrastructure by migrating to Google Cloud. 
This critical upgrade provides key benefits, including enhanced reliability, 
improved security, greater compliance, and more granular access control. It also gives
access to Agentic AI capabilities through Model Context Protocol (MCP) integration.
The migration provides the following:
Enhances SOAR's reliability and monitoring capabilities 
by utilizing Google's best-in-class API layer. This layer provides a 
leading API solution with advanced features for quota management, auditing, and observability.
Unlocks Role-Based Access Control (RBAC) for features and 
data throughout the entire platform.
Provides higher compliance functionality, 
such as VPC Service Controls, Data Residency, and Customer-Managed Encryption Keys (CMEK).
Q: What's the scope of the migration?
The migration involves the following components:
Migrating SOAR project to a customer owned Google Cloud project.
Migrating SOAR authentication and permissions to Google Cloud IAM.
Migrating SOAR APIs to Chronicle API.
Migrating remote agents.
Migration of SOAR Audit Logs.
Q: What are the immediate changes after the migration?
Immediately following the migration, you'll experience several key changes:
GCP Project Ownership
: Your SOAR project will migrate from Google's ownership 
to your customer-owned Google Cloud project.
Authentication
:
Unified SecOps customers: No change. Authentication will continue to be managed 
by Google Cloud IAM.
SOAR Standalone customers: Authentication will now be managed by Google Cloud 
IAM. For users using SAML, this means adopting Workforce Identity Federation, 
and the SAML configuration will no longer be stored and managed within the 
SOAR system itself, leading to stronger security controls.
RBAC
: User permissions will become more granular 
and managed using IAM. Environments and SOC roles 
will continue to be managed within the SOAR module using Identity Provider (IdP) groups.
Audit Logging
: Audit logs will be more detailed and managed within **Cloud Audit Logs **.
New URL (SOAR only)
: SOAR standalone users will receive a new URL (new domain) for accessing SOAR.
Q: How are customers / partners being notified of this migration?
An in-product pop up is displayed for all customers and partners which includes 
the migration date and a link to a form to fill out. They will be prompted to confirm their migration date and time slot.
Q: Will our infrastructure costs change as a result of SOAR being bound to our Google Cloud project?
No, your costs won't be impacted. You shouldn't experience any change 
on the frontend. No new resources will run in your project, so there are no associated costs.
Q: How do we connect our project to SOAR?
Google will migrate your SOAR project to your Google Cloud project. 
If you are a Unified SecOps customer, we already have your Google Cloud project ID. 
If you are a SOAR standalone customer, you will need to share your Google Cloud project ID with us.
Q: For customers who already have a Google SecOps deployment, should we use the same project ID as SIEM, or do we need a separate project?
For a unified Google SecOps deployment (one SIEM, one SOAR), you 
should use the existing Google Cloud project ID associated with your SIEM. 
This allows for unified management of administrative flows, such as RBAC and logs.
Q: For Google SecOps instances with special considerations such 
as VPC Service Controls (VPC SC), what steps are needed?
To enable the migration, you'll need to define both Ingress and Egress rules within your VPC SC policy. 
 If your Google Cloud Project has VPC SC, contact the Support team for detailed guidance on these specific rules.
Downtime and continuity
Q: Is there any downtime during the migration, and what is its impact?
Yes. The expected downtime is as follows:
Up to 2 hours for SOAR standalone customers.
Up to 1.5 hours for Google SecOps customers.
During this period, you won't be able to sign in to the platform. SOAR services (including ingestion, playbooks, jobs) 
will be paused but SIEM services will continue running in the background.
Q: Will data generated during the downtime be automatically ingested once SOAR services resume?
Yes. Once the system is back online, ingestion and playbooks will resume and
process any alerts that were generated or ingested during the downtime.
Q: What happens to playbooks that are running when downtime begins?
The playbook service will be turned off before the migration begins, some running playbooks 
may fail and will either need to be restarted manually or will resume after the migration is complete.
Q: Is there a rollback or contingency plan if something goes wrong during the migration?
Yes. The migration process keeps your existing SOAR instance fully intact (though turned off). 
If the migration process doesn't complete successfully, we can switch 
back to your existing instance and remove the new one. 
This rollback process takes up to 30 minutes. We'll perform extensive testing and 
close monitoring, with on-call staff on standby to ensure successful migration.
If you experience access issues after migration, you likely have an incorrect authentication setup. You will need to coordinate with your Identity, IDP, or Google Cloud administrator to use the
troubleshooting guide
for identification and resolution. If the problem persists or if it is unrelated to access, open a
Support ticket
to document the concern and monitor its resolution.
Q: When can I migrate to the new SOAR Endpoints v1 in Chronicle API?
You can migrate to the new SOAR endpoints v1 in Chronicle API from mid January, 2026.
The legacy SOAR API and API Keys will be deprecated and no longer function after June 30, 2026. To ensure a smooth transition, follow these two mandatory steps:
You must first complete the migration of SOAR Permission Groups to Cloud IAM.
Update your existing scripts and integrations to replace the legacy SOAR API endpoints with the corresponding Chronicle API endpoints.
Authentication and permissions
Q: How do I migrate my SOAR permission groups and permissions?
You will use a migration script in your Google Cloud console to 
migrate existing permission groups to IAM custom roles. 
The script also assigns custom roles to users (for Cloud Identity customers) 
or to IdP groups (for Workforce Identity Federation customers).
Q: What if I prefer not to migrate custom permission groups and only use predefined roles?
You can opt out of the automated migration and manually map IdP groups to 
Cloud IAM roles instead.
Q: We're a SOAR standalone customer with a custom SAML provider with manual authentication. If we change this to IdP groups for IdP mapping, what's the impact on existing user accounts?
Assuming your existing users match one of the groups and permissions are mapped correctly, 
there shouldn't be any impact on your pre-existing user accounts. 
However, if users aren't mapped to groups, they won't be able to sign in. 
If permissions are mapped differently, users will receive new permissions based on the new mapping.
Q: Are there specific prerequisites for MSSPs using multiple identity providers?
Customers who have configured multiple identity providers on the 
SOAR external authentication page, should define Workforce Identity Federation for 
authentication and create a separate Workforce Pool for each provider. 
Each provider is associated with a different subdomain. For more information, read
MSSP migration guide
.
Q: How do I authenticate to the Chronicle API?
Follow the instructions in
Authenticate to Chronicle API
.
Q: What are the new IPs required to access the new SOAR API?
It's not required to allow list any IP addresses to access Chronicle API. Optionally, you can allow list the range of IP addresses indicated
here
and
here
.
Logging and monitoring
Q: We completed the first stage of migration, but we don't see logs in Cloud Audit Logs Logs.
Logs are stored in the SOAR platform after the completion of the first migration stage. 
Logs become available in your Google Cloud project after the completion of 
the second migration stage.
Q: Will customers sending SOAR data to a Managed BigQuery (BQ) instance still be able to access this BigQuery data after the migration?
Yes. The existing managed BigQuery will continue working.
Logistics and support
Q: Can I choose a different time slot for the migration?
No. Migrating outside of the suggested time slots isn't possible.
Q: Will we receive real-time status updates during the migration?
You'll receive an email notification at both the start and end of the migration process.
Q: Who should we contact if an issue arises post-migration?
If you experience access issues after migration, the authentication setup is likely incorrect.
You will need to coordinate with your Identity, IDP, or Google Cloud administrator to use the
troubleshooting guide
for identification and resolution. If the problem persists or if it is unrelated to access, open a
Support ticket
to document the concern and monitor its resolution.
Need more help?
Get answers from Community members and Google SecOps professionals.
