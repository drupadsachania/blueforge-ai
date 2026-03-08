# Set up a webhook

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/ingest/webhooks/setting-up-a-webhook/  
**Scraped:** 2026-03-05T09:31:03.626596Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Set up a webhook
Supported in:
Google secops
SOAR
Webhooks
are a lightweight solution for ingesting alerts from your
organization into the Google Security Operations SOAR platform.
Webhook-ingested alerts appear in the platform with the same information as alerts ingested using connectors.
Google recommends using either a connector or a webhook from the same source, but not both, to avoid creating duplicate cases.
Webhooks are best for scenarios that require basic mapping logic, while connectors are better for advanced and flexible mapping.
Set up a webhook to ingest alerts
The following use case focuses on using CrowdStrike as the platform
through which to ingest alerts.
To set up a webhook to ingest alerts, follow these steps:
Go to
SOAR Settings
>
Ingestion
>
Webhooks
.
Click
add
Add incoming Webhook
.
Enter a name for the new webhook, and choose an environment.
Click
Save
.
This example uses CrowdStrike.
After saving, it appears on the main page.
Copy the webhook URL and note it for later use. You'll need it to enter 
    it in the CrowdStrike platform as the webhook destination.
Map data
In the
Data Mapping
section, click
Upload JSON sample
(use the sample taken from CrowdStrike).
Map the Google Security Operations fields with the
    corresponding fields in the CrowdStrike JSON fields. For example, the mandatory Google SecOps alert
    field
StartTime
, select the CrowdStrike field
Detections.Last.Update
. This
    appears in the Expression Builder. For more information, see
Use the Expression Builder
.
Add a function (on the side) to further refine this field, for example,
Date Format
.
Once the
Detections.Last.Format
appears in the Expression Builder,
    click
Run
to see the results.
The
Start
displays with a green checkmark, indicating that the field is mapped.
After you map all the necessary fields, click
Save
and then
    enable the webhook.
Test the webhook
The
Testing
area lets you test the webhook's
    end-to-end functionality, and provides detailed error descriptions.
In the
Testing
tab, copy 
    the webhook URL.
Upload a JSON file with the relevant data.
Click
Run
. The results display together with the output.
Use case: Configure the CrowdStrike platform
This use case takes you through the steps in
    CrowdStrike for the webhook to start ingesting alerts into the
    Google SecOps platform.
In the CrowdStrike Falcon dashboard, go to the
Falcon store
and install the Webhooks add-on.
Configure the webhook with the name and the webhook URL that you copied
     from the Google SecOps platform and click
Save
.
Go to the
Workflows
section.
Click
Create a Workflow
.
Select a trigger, such as
New detection
, and click
Next
.
Select
Add Action
.
In the
Customize action
section, select
Notifications
from
     the
Action type
menu and select
Call webhook
from the
Action
menu.
Select the name you added in the initial step and all necessary fields, and then click
Finish
.
Need more help?
Get answers from Community members and Google SecOps professionals.
