# Create and edit a playbook with Gemini

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/create-edit-playbook-with-gemini/  
**Scraped:** 2026-03-05T10:08:01.386967Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Create and edit a playbook with Gemini
Supported in:
Google secops
SOAR
You can use Gemini to streamline your security operations by learning how to create and edit playbooks using basic, natural language prompts.
Create a playbook using prompts
To create a playbook using Gemini prompts, do the following:
Go to
Response
>
Playbooks
.
Click
add
Add
and create a new playbook.
Choose the folder for your playbook and the environment it applies to.
Click
Create
.
In the new playbook pane, select
Create Playbook with Gemini
.
In the prompt pane, enter a comprehensive and well-structured prompt in
English. For more information on how to write a playbook prompt, see
Write prompts for Gemini playbook creation
.
Click
Generate Playbook
. A preview pane with the generated playbook is displayed. Click
edit
Edit
to refine the prompt, if needed.
Click
Create Playbook
.
Edit a playbook using prompts
Select the required playbook and select
Edit Playbook with Gemini
.
Add any changes that are required. A preview pane with the edited playbook shows you the before and after versions.
Click
Back
and refine the prompt, as needed.
When done with the changes, click
Edit Playbook
.
Provide feedback for playbooks created by Gemini
Select one of the options provided and add additional feedback:
If the playbook results are good, click
thumb_up
Thumb up
. You can add more information in the
Additional Feedback
field.
If the playbook results weren't as expected, click
thumb_down
Thumb down
.
Write prompts for Gemini playbook creation
The
Gemini Playbook
feature creates Google SecOps
playbooks (including triggers, actions, blocks, and conditions) based on your
natural language input. To generate an effective playbook, you must enter clear,
specific, and well-structured prompts. The quality of the output is directly
influenced by the quality of the input.
Capabilities of playbook creation with Gemini
You can do the following with the Gemini playbook creation feature:
Create new playbooks with actions, triggers, flows, and blocks.
Use all downloaded commercial and custom integrations.
Put specific actions, blocks and integration names in the prompt as playbook steps.
Understand prompts to describe the flow where specific integrations and names aren't given.
Use condition flows as supported in SOAR response capabilities.
Detect which trigger is necessary for the playbook.
You can't do the following when creating playbooks using prompts:
Create playbook blocks.
Use parallel actions in playbooks.
Use integrations which haven't been downloaded and installed.
Use integration instances.
Capabilities of playbook editing with Gemini
You can do the following with the Gemini playbook editing feature:
Add playbook steps anywhere in the playbook.
Delete any playbook step.
Modify playbook trigger.
Move steps around in the playbook.
Replace actions, blocks, or integrations with their corresponding counterparts.
You can't do the following when editing playbooks using prompts:
Edit conditions.
Construct effective prompts
FTo make sure the Gemini Playbook feature generates the most accurate and
automated workflow possible, we recommend that you follow these best practices
for writing your natural language prompts:
Be specific with integrations
: Use specific integration names (for example, "enrich with VirusTotal") only if the integration is already installed and configured in your environment.
Leverage Gemini specialization
: Gemini is designed to build playbooks that align with incident response, threat detection, and automated security workflows. Tailor your prompts to these security use cases.
Define the logic
: Ensure your prompt clearly details the full logic:
Start with a clear
objective
(for example, managing malware alerts).
Specify the
trigger
that activates the playbook (for example, upon receiving an alert".
Detail the
actions
(for example, enrich data, quarantine files).
Include the
condition
for those actions (for example, based on threat analysis results).
Example prompts for Gemini playbook creation
This section shows practical examples that highlight how clear objectives,
defined triggers, specific actions, and conditional responses work together to
create effective, automated security workflows.
Example: Prompt with integration name
The following example shows a well-structured prompt using an integration name:
Write a playbook for malware alerts. The playbook should take the file hash 
from the alert and enrich it with VirusTotal. If the file hash is malicious, quarantine 
the file.
This prompt contains the four components defined earlier:
Clear objective
: Has a defined goal, handling malware alerts.
Specific trigger
: Activation is based on a specific event, 
receiving a malware alert.
Playbook actions
: Enhances a Google Security Operations SOAR entity with data from a third-party integration (VirusTotal).
Conditional response
: Specifies a condition that is 
based on previous results. For example, if the file hash is found to be malicious, 
the file should be quarantined.
Example: Prompt by action flow
The following example shows a well-structured prompt, but describes the flow 
without mentioning the specific integration name.
Write a playbook for malware alerts. The playbook should take the file hash 
from the alert and enrich it. If the file hash is malicious, quarantine the file.
The Gemini playbook creation feature is capable of taking this
description of an action—enrich a file hash—and looking through the installed
integrations to find the one that best fits this action.
The Gemini playbook creation feature can only choose from integrations 
that are already installed in your environment.
Customized triggers
In addition to using standard triggers, you can customize a trigger in the playbook
prompt. You can specify placeholders for the following objects:
Alert
Event
Entity
Environment
Free text
In the following example, free text is used to create a trigger that's executed 
for all emails from the
suspicious email
folder except for those emails 
that contain the word [TEST] in the email subject line.
Write a phishing playbook that'll be executed for all emails from the 
'suspicious email' folder ([Event.email_folder]) that the subject 
does not contain '[TEST]' ([Event.subject]). The playbook should take the 
file hash and URL from the alert and enrich it with VirusTotal. If the file hash 
is malicious, quarantine the file. If the URL is malicious, block it in the firewall.
Example: Well-structured prompts
Write a playbook for phishing alerts. The playbook enriches usernames, 
 URLs and file hashes from the email and enriches them in available sources. 
 If one of the findings is malicious, block the finding, remove the email 
 from all the users' mailboxes and assign the case to tier 2.
Create a playbook for my Google Cloud Anomalous Access alert. The playbook should 
 enrich user account information with Google Cloud IAM, and then 
 enrich the IP information with VirusTotal. 
 If the user is an admin and the IP is malicious, the user account should be 
 disabled in IAM.
Write a playbook for suspicious login alerts. The playbook should enrich 
 the IP address with VirusTotal and get GeoIP information. If VirusTotal reported 
 more than 5 malicious engines and the IP address is from Iran or China, 
 block the IP address in Checkpoint Firewall and send an email notification to 
 zak@example.com.
Creating playbooks from large free-form prompts
You can also create a playbook from a detailed prompt containing free-form text. 
For example, create a prompt that describes the remediation steps for a specific cyberattack. The more precisely you describe the scenario, 
the greater the accuracy of the generated playbook.
Need more help?
Get answers from Community members and Google SecOps professionals.
