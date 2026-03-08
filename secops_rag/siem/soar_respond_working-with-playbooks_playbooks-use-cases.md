# Explore basic use cases in playbooks

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbooks-use-cases/  
**Scraped:** 2026-03-05T09:35:20.233938Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Explore basic use cases in playbooks
Supported in:
Google secops
SOAR
This document discusses some basic use cases that you can automate within your playbooks.
Send emails within a playbook
You can incorporate interactive email correspondence into your playbooks. Using the built-in email actions, you can send outbound emails from the Google SecOps platform and automatically track, ingest, and log user responses directly to the case, ensuring that all communication and user input are recorded for further playbook processing.
Before you begin
Before you begin, you'll need to enable email capabilities, which requires you to install one of these integrations:
Microsoft Graph Mail
–Use for Exchange Online.
Gmail
–Use for Gmail accounts.
Send an email
To send an email and log its response in Google SecOps, follow these 
  steps:
Select the
Send Mail
action to send an email.
Add the
Wait For Mail From User
action to periodically 
    query the mailbox for a response. This action identifies the correspondence 
    by using a unique ID.
Once the response is received, it's fetched into the platform.
The response can be seen on the case wall and used as an input for other actions
in the playbook.
Scan multiple URLS in VirusTotal
The
VirusTotal Scan URL
action iterates over the selected scope
  entities, and initiates a request to VirusTotal for each entity of type
  URL. When finished, the action enriches the URL entities with a VirusTotal
  report and also posts the result on the case wall.
  An
is_risky
value is exposed so that you can add further
  conditions to the playbook for high-risk URLs. For details on how to use the
Scan Hash
action to scan file hashes with VirusTotal, mark entities as
  suspicious, and show insights, see the
Scan Hash
action for VirusTotal.
Scan URLs received by email
You can build a security automation workflow that extracts and scans URLs from inbound emails to detect phishing or malicious links. This process ensures that any dangerous links are neutralized before they pose a risk, letting your playbook take immediate action, such as blocking the URL or quarantining the email.
Before you begin
You must have the following integration installed and configured in your environment:
Email integration: Microsoft Graph Mail or Gmail (to read and extract data from the email/alert).
Reputation integration: VirusTotal or a similar URL analysis tool.
To scan URLs received by email, you'll need to configure a connector that monitors an email box (with the
Email
or
Exchange
integrations).
Build the scan logic in your playbook
Use the following steps to build the scanning logic in your playbook:
Use the email integration's action (for example,
Gmail_Enrich Email
) to get the full email body or event data. Use the Expression Builder to parse the email and extract the specific URL(s) you want to scan. For details, see
Use the Expression Builder
.
When emails start coming into Google Security Operations SOAR, their content can be either parsed by the mapping feature or extracted by the
Create Entity
playbook action (if playbooks are attached to the incoming emails).
Add your selected action (for example,
VirusTotal_Scan
URL) and use a placeholder to input the extracted URL from the previous step.
Add a Condition flow immediately after the scan action. For details, see
Use flows in playbooks
.
Configure the branches of the condition to evaluate the JSON Result from the reputation scan:
Branch 1 (Malicious): If
Scan Result
is reported as malicious (for example, score > 5, or specific engine found a threat).
Branch 2 (Clean/Unknown): If
Scan Result
is clean or if the condition fails to find malicious indicators.
Once all URLs are extracted, you can use them in manual actions and in playbooks.
Send messages to a phone number
To send messages to a phone number, you must have the Twilio
  integration installed and an active account with Twilio.
Once configured in the Content Hub, Twilio actions
  will let you send SMS messages and even fork playbooks according to an
  SMS response.
Put elements of the case data into an email
Placeholders are dynamic expressions used in playbook actions to insert
  specific case data, entity attributes, or alert details into text fields
  (like an email message). At runtime, the placeholder is replaced by the actual
  data extracted from the Google Security Operations platform.
Placeholder structure
A placeholder always starts and ends with square brackets [ ], which
  contain the specific data path (for example,
[Alert.Name]
references the alert's name).
The following placeholders won't render for any automatic operation:
General.CurrentUserEmail
General.CurrentUserID
General.CurrentUserFullName
General.CurrentUserRole
Use a placeholder
To use a placeholder, follow these steps:
Click
data_array
Placeholder
next to a text field (for example, the message field in a
Send Email
action).
Select the preferred content path to insert the placeholder (for example,
[Alert.Name]
).
You can combine multiple placeholders with static text to create rich, custom content.
Need more help?
Get answers from Community members and Google SecOps professionals.
