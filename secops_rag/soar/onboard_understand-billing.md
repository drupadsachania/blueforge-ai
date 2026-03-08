# Understand your Google SecOps billing components

**Source:** https://docs.cloud.google.com/chronicle/docs/onboard/understand-billing/  
**Scraped:** 2026-03-05T09:45:26.547427Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Understand your Google SecOps billing components
Supported in:
Google secops
SIEM
This document explains how you're billed for Google Security Operations usage and
how these charges appear in your Google Cloud billing console.
Google SecOps uses a credit-based model for your core
data ingestion. The packages (Standard, Enterprise, Enterprise Plus)
use a subscription-based billing model that includes a subscription and a
metering component.
For a high level understanding of Google Cloud billing, see
Cloud Billing overview
.
Key considerations
For your subscription credits and usage metering to function correctly, the
following configuration is required:
Confirm that your project and subscription billing accounts match
. The
Google Cloud project that hosts your SecOps instance must link to the
same billing account ID used for your SecOps subscription order.
Important
: If the project and subscription billing accounts don't match, the
system can't apply your subscription credits to your usage. This results in
incorrect charges.
Ensure your contract specifies your intended provisioning region
.
Google SecOps uses region-specific SKUs to comply with data residency
requirements. Pricing may vary between regions due to differences in underlying
operational costs.
Initial setup
After you purchase Google SecOps, your billing account receives a
credit balance equal to the total amount of GB purchased. Your actual data is
metered and draws down this credit balance. This usage appears in your billing
console under the
Bytes of data ingested SKU
.
Monitor costs and usage in Google Cloud
To track and analyze your spending, monitor all consolidated cost and usage data under
Billing
in the Google Cloud console.
Default components
The following two components always appear in your billing summary.
Report header
Description
SecOps (commitment) SKU
Your recurring subscription fees, based on your booked subscription. This subscription type is a fixed amount as per the specified billing frequency in your subscription.
SKU Example
:
Commitment - dollar based v1: Chronicle SecOps US
Usage (data ingestion) SKU
Your actual data ingested, which offsets your SecOps credits.
SKU Example
:
Bytes of data ingested in US for the Enterprise package under subscription
Additional charges
The following charges appear only if you meet specific usage conditions or
purchase additional services.
Report header
Description
Usage overage
If your ingestion exceeds your commitment and no SecOps credits are available, you incur overage charges. The subscription SKU then shows monthly charges for the additional data at your negotiated rate.
SKU Example
:
Bytes of data ingested in the US for the Enterprise package under subscription.
Data retention SKU
If you opt for extended data retention (greater than 12 months), the associated charges are calculated and billed as follows:
Cost basis
: Charges are determined by the total volume of data ingested.
Billing timing
: Charges are always billed in arrears (post-paid). For example, your data usage in January appears as a charge on your February bill.
SKU Example
:
Additional data retention
Assured Workloads SKU
If you select a
Premium control package
, the following billing rules apply:
Charge type
: You'll incur a percentage uplift calculated on the cost of all Google Cloud services running within that folder.
Billing appearance
: These uplift charges appear under the
Assured Workloads SKU
in your billing console.
Pricing reference
: For additional details, visit the
Assured Workloads pricing page
.
SKU Example
:
Google Cloud Assured Workloads PAYG Subscription
Grace period
If your subscription contract expires before a renewal is finalized,
Google SecOps automatically enters a grace period. This ensures
that your security coverage continues without interruption while you finalize
your renewal or offboard from the service.
During the grace period, the following billing conditions apply:
Pricing rate
: All usage (including data ingestion) is billed at the
standard list price on a pay-as-you-go basis.
Discounting
: Negotiated discounts, special rates, or unused credits
from the expired subscription don't apply during the grace period.
Billing cycle
: Charges are billed monthly in arrears.
Renew your subscription
If you renew your subscription during the grace period, your new contract terms
and pricing begin on the day the new contract start date is booked.
To deprovision your Google SecOps instance, follow the steps
in
Self-service deprovisioning for Google SecOps
.
Assured Workloads fees
If your organization requires specific compliance regimes (for example,
FedRAMP High), deploy and use Google SecOps within a configured
Google Cloud Assured Workloads environment.
Assured Workloads environments may incur additional fees, which are
billed separately from your standard Google SecOps subscription.
The cost is a percentage uplift to the charges of all Google Cloud services
running within that Assured Workloads folder. You can find these
charges on your invoice as separate line items.
For specific rate details and applicable percentages, see
Assured Workloads pricing
.
Track and analyze SecOps billing
Google Cloud provides the following tools to help you monitor, report on, and
optimize your Google SecOps spending:
Analyze spending trends
: In the Google Cloud console, use reports
(
Billing
>
Reports
) to view detailed spending trends and
filter usage by SKU. For more information, see
Cloud Billing Reports
.
Set spending thresholds
: Configure email notifications
(
Billing
>
Budgets & alerts
). For more information, see
Create, edit, or delete budgets and budget alerts
.
Apply labels
to your Google SecOps resources. Labels
are essential to categorize and track costs by team, environment,
or cost center. For more information, see
Organize resources using labels
.
Billing for Google SecOps SIEM or SOAR products
This section applies
only
if you purchased Google SecOps SIEM
or Google SecOps SOAR as standalone products, separate from the
unified Google SecOps packages.
These standalone products are billed through a different system, not through
the integrated Google Cloud
Billing
platform.
Invoice:
You'll receive invoices through the email address provided
on your service order form.
Charges:
Detailed charge breakdowns for these standalone products are
not
available in the Google Cloud console.
Invoice access:
You can view and download your invoices from the
Google Payments Center
.
Support:
For billing queries, contact the support contact specified in
your contract or your Google Account team.
Important
: Google Cloud
Billing Support in the Google Cloud console can't assist with these charges.
Get Google Cloud billing support
For questions related to your Google SecOps bill, specific
charges, or invoice generation, contact
Cloud Billing support
.
Need more help?
Get answers from Community members and Google SecOps professionals.
