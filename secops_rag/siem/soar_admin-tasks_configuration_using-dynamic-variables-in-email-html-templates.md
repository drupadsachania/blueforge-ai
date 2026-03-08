# Use dynamic variables in email HTML templates

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/using-dynamic-variables-in-email-html-templates/  
**Scraped:** 2026-03-05T09:15:54.020666Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Use dynamic variables in email HTML templates
Supported in:
Google secops
SOAR
This document explains how to use dynamic variables in email HTML
  templates to create reusable and customizable email content within Google Security Operations.
Create the email HTML template
You can create the email HTML template with a fixed subject header and title. The
{Text}
placeholder lets playbook builders manually  insert content when they create a new playbook.
To do this, follow these steps:
Go to
Settings
>
Environments
>
Email HTML templates
.
Add a new template and give it a name. For example,
Testing Text Option
.
In the template body, make sure you include the
{Text}
placeholder. This placeholder will be replaced with the custom content provided in the playbook.
Click
Add
.
Add the template to a playbook
In your playbook, drag in a
Send Email
action.
Choose the specific template: click the list and select
Testing Text Option
.
In the
Content
field, enter the body of your email. This content will replace the
{Text}
placeholder when the playbook runs.
Click
Save
.
When an alert is ingested into the Google SecOps platform, the playbook runs and triggers an email. The system renders the email template, inserting the content from the
Content
field into the
{Text}
placeholder before sending the email to the recipient.
Need more help?
Get answers from Community members and Google SecOps professionals.
