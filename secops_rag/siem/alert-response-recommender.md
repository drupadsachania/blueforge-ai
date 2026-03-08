# Use the Alert Response Recommender

**Source:** https://docs.cloud.google.com/chronicle/docs/secops/alert-response-recommender/  
**Scraped:** 2026-03-05T09:14:34.032984Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use the Alert Response Recommender
Supported in:
Google secops
This document explains how to use the
Alert Response Recommender
pilot, an 
experiment in the Google Security Operations Labs. The pilot significantly reduces the time analysts spend on investigations. It analyzes historical data from similar, previously closed alerts with a Large Language Model (LLM). By providing actionable recommendations, the Alert Response Recommender helps streamline the triage process and accelerate case resolution.
For more information about the Google SecOps Labs, see
Use Gemini and Google SecOps experiments
.
Locate the alert ID or ticket ID
Go to the
Cases
page, select the case you want to investigate from the 
queue.
Navigate to the
Case Overview
.
Go to the
Alerts widget
and click
View Details
for the specific alert 
you need.
In the side drawer that appears, go to the
Case
section and copy the
Ticket ID
or
Alert ID
.
Run the experiment
On the Google SecOps page, click
experiment
Labs
.
In the
Alert Response Recommender
card, click
Try
.
In the
Open Alert ID
field, enter the Ticket ID or Alert ID you copied.
Click
Submit
.
Review the output
Once the pilot has analyzed the data, it generates a recommendation based on an 
analysis of similar historical alerts. The output includes these key sections:
Analyst Actions:
Recommended manual steps.
Content Hub Actions:
Suggested actions within the Content 
Hub.
Closure Recommendation:
A suggested reason to close the alert.
The output also includes a detailed breakdown of the analysis, with a list of 
similar historical alerts, their closure reasons, and playbook usage.
Example output:
Recommendations

  Step 1: Recommendation for Analyst Actions

  No specific manual analyst actions are recommended based on the provided data.

  Step 2: Recommendation for Content Hub Actions

  No Content Hub actions are recommended based on the provided data.

  Step 3: Closure Recommendation

  Close the alert as "Maintenance".

  Recommendations Are Based on the Following Similar Historical Closed Alerts

  Step 4: Identify Similar Alerts

  The following characteristics are shared between the current alert and the similar alerts:

  * AlertRuleGenerator: "Data Exfiltration"
  * AlertProduct: "DLP_Product"
  * AlertDisplayName: "DATA EXFILTRATION"
  * AlertVendor: "DLP"
  * AlertSourceSystemName: "Arcsight"
  * AlertIsManual: false
  * AlertOriginalName: "DATA EXFILTRATION"
  * AlertSourceIdentifier: "Simulation"
  * AlertUsefulness: "None"
  * AlertPriority: "High"
  * All EntityIdentifiers are identical.

  The similar alerts are:

  * DATA EXFILTRATION_96C92028-70E5-4947-87DF-CC64133B2583
  * DATA EXFILTRATION_79D74832-4C9D-4315-AD0C-77F640A1766A
  * DATA EXFILTRATION_6C6713D6-8A50-48AB-B168-FE23791EC86C
  * DATA EXFILTRATION_C6493390-3544-46A6-A219-0DDC64FE8547
  * DATA EXFILTRATION_B44A1099-2DBD-4F02-9173-5931C538AE9D

  Step 5: Analyze Playbook Usage in Similar Alerts

  No playbooks were used in the identified similar alerts.

  Step 6: Analyze Case Closure Information

  All similar alerts, except DATA EXFILTRATION_8D4E6467-F503-447A-8B38-BC521296E194, 
  have the closure reason as "Maintenance", with a root cause of "Lab Test". The alert 
  DATA EXFILTRATION_8D4E6467-F503-447A-8B38-BC521296E194 has the closure reason "NotMalicious". 
  Comments in most cases contain the word "test" along with the Case closed by Siemplify API 
  information.
Limitations
To ensure you interpret the recommendations correctly, be aware of the following limitations:
Dependence on historical data: The quality and relevance of the 
recommendations are directly tied to the historical data available. If there 
isn't enough similar data, the advice may be limited or less accurate.
Limited alert types: The recommendations may be less effective for some 
alert types, particularly if they're new or have few precedents.
Minimum alerts required: The Alert Response Recommender must find at 
least one similar historical alert to provide a recommendation. If no similar 
alerts are found, it can't provide a useful analysis. The application will 
notify you of this by showing an empty
Identify Similar Alerts
tab.
Need more help?
Get answers from Community members and Google SecOps professionals.
