# Self-service deprovisioning for Google SecOps

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/customer-initiated-secops-deprovision/  
**Scraped:** 2026-03-05T09:16:17.822884Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Self-service deprovisioning for Google SecOps
Supported in:
Google secops
SIEM
This document explains how to use the self-service deprovisioning feature in Google Security Operations to delete a Google SecOps tenant and all related data. This feature provides a scalable and compliant process for handling deletion requests efficiently.
With deprovisioning, you can remove user access to Google SecOps and delete the tenant, including all associated data and resources. You manage the deletion process directly without relying on external support.
Required roles to deprovision and restore
To deprovision (or restore) a tenant, the user initiating the action must have the specified role, determined by the way your Google SecOps tenant is deployed:
If your Google SecOps tenant is deployed on a Google Cloud project that you own (BYOP stack)
: The user must have the
Data Governor
role.
If there is no customer-owned Google Cloud project associated with your Google SecOps tenant (legacy stack)
: The user must have access to the
Admin
role in the legacy role-based access control (RBAC) system.
Billing implications of deleting your instance
Before initiating the deprovisioning process, it's important to understand the billing implications, as follows:
Deleting a Google SecOps instance does not cancel your billing.
If you have an active contract, you're still responsible for the full contract value, even after you delete the instance.
Billing continues until the contract term ends, regardless of the tenant's status.
Deprovisioning phases
Self-service deletion occurs in two phases:
Soft delete phase (12-day grace period)
Hard delete phase (permanent deletion)
Soft delete phase
Only the Data Governor or the legacy IAM admin can access the Google SecOps
Profile
page, where they can:
View the remaining days in the soft delete phase.
Click
Restore
to cancel the deletion and restore the tenant.
The Data Governor or the legacy IAM admin initiates a 12-day grace period for soft deletion before data is permanently deleted. During this phase, the following restrictions and actions apply:
The system disables UI and API access and data ingestion is halted; no new data will be ingested into the Google SecOps tenant after the deletion request is initiated.
All roles can access the profile page.
The Data Governor can see the 12-day remaining soft-delete phase and use the
Restore
button, which reverts the soft delete and restores the tenant.
Most product functions are deactivated for all the users.
Hard delete phase
After the 12-day soft delete phase has ended, the data deletion process starts, systematically removing data and resources associated with the Google SecOps tenant. The amount of time that the data deletion process takes depends on various factors, including regional laws and contracts.
Once the process begins, the following irreversible actions occur:
All customer data, including backup snapshots, are permanently deleted.
All UI access is permanently deactivated.
Deprovision a Google SecOps tenant
To deprovision a Google SecOps tenant, do the following:
Go to Google SecOps
Settings
>
Profile
.
Click
Disable & Delete
. A notification window displays several warning messages:
Access to Google SecOps will stop immediately; by proceeding with disabling and deleting this instance, the following occurs:
Only Admin users with the Data Governor role can restore the instance within 12 days. All other users will immediately lose access to Google SecOps and its data.
Data collection will stop within a few hours.
The instance can continue to be charged for a period of time, depending on your billing agreement.
All data, including cases, alerts, detection rules, settings, and logs will be permanently deleted after 12 days and can't be recovered.
Enter
Delete
in the confirmation field.
Click
Disable & Delete
. The message
Google SecOps has been disabled. All data will be deleted starting [date]
appears, where the date is 12 days once you click
Disable & Delete
. The user can't navigate within the platform. A timer displays the start and progress of the 12-day soft delete phase.
Restore a deleted tenant
You can restore your tenant within 12 days after initiating deletion. The system reverts your tenant to its original state with previously existing data. The
Restore
button appears after you click
Disable & Delete
. Click
Restore
to restore the Google SecOps tenant/platform.
Limitations
The deprovision feature only provides self-service capabilities handled by
Customer Support
. It doesn't unify or automate the deprovision process across all Google SecOps systems.
After restoring a tenant, all data feeds remain inactive. You must manually re-activate the data feeds that you need.
The system deprovisions the SIEM and any associated SOAR instances; however, associated VirusTotal and Mandiant instances required manual deprovisioning, tracked by a bug ticket.
Need more help?
Get answers from Community members and Google SecOps professionals.
