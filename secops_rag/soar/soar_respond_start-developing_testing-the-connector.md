# Test a connector

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/testing-the-connector/  
**Scraped:** 2026-03-05T10:08:53.586404Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Test a connector
Supported in:
Google secops
SOAR
This document explains how to test a connector by ingesting a sample malicious
  email into the Google Security Operations platform. The test process demonstrates how to:
Ingest a sample malicious email.
Run the connector.
Load the alert into the case queue.
View how alert data is translated.
After completing these steps, you can view the new case, preview
  the email content, and understand how the alert data is translated and
  displayed within the platform before it's mapped and modeled.
Ingest a sample malicious email
To ingest a sample malicious email into the Google SecOps
platform, follow these steps:
Insert a malicious email into the platform.
Copy the following sample email text and send this email from another user:
Subject:
Your new salary notification
Email body:
Hello, You have an important email from the Human Resources Department with regards to your December 2018 Paycheck. This email is enclosed in the Marquette University secure network.
Access the documents here: www.example.com. Ensure your login credentials are correct to avoid cancellations.
Faithfully,
Human Resources
University of California, Berkeley
Run the connector
To run the connector, follow these steps:
Go to
Settings
>
Ingestion
>
Connectors
.
On the
Testing
tab, click
Run connector once
; The results appear in
    the
Output
section and show a new connector instance created in the platform 
    Each time you run this function, it will execute as if it's the first iteration.
    No timestamps are saved and no IDs are stored in the backend.
If your connector runs
    successfully, an alert for a single unread email appears. Make sure your
    mailbox contains at least one unread email for this test.
Optional: Click
Preview
to see a preview of the email.
Load the alert into the case queue
After ingesting a sample alert, ingest the alert into the case queue by following these steps:
Select the alert and click
Load to system
.
In the
Cases
tab, view the ingsted case.
After the connector receives the email by translating the email data to
    Google SecOps data, you can see your alert in the
Cases
tab in
    the case queue.
After the connector translates the email data to Google SecOps format, the alert appears in the case queue. When the case first appears, it is not mapped or modeled. These steps occur next in the workflow.
View how alert data is translated
You can see how each field in the connector code corresponds to the relevant field
  presented in the platform's context details.
To see how the alert data appears in the platform, click the alert to view the
Alert Context details
.
Platform field
Description
Code mapping
Field name/Value
Email subject, for example: "YOUR NEW SALARY NOTIFICATION"
alert_info.name = email_message_data['Subject']
RuleGenerator / Mail
The name of the Google Security Operations SIEM rule which causes the creation of the alert
alert_info.rule_generator = RULE_GENERATOR_EXAMPLE
TicketID
The email message unique ID
alert_info.ticket_id = f"{alert_id}"
AlertID
The email message unique ID
alert_info.display_id = f"{alert_id}"
DeviceProduct / Mail
As we defined in CONSTANTS:
PRODUCT= "Mail"
alert_info.device_product = PRODUCT
DeviceVendor / Mail
As we defined in CONSTANTS:
VENDOR = "Mail"
alert_info.device_vendor = VENDOR
DetectionTime / EndTime / StartTime / EstimatedStartTime
The time the email message was received
alert_info.start_time = datetime_in_unix_time
alert_info.end_time = datetime_in_unix_time
Priority / Informative
As we defined for this alert:
Informative = -1
Low = 40
Medium = 60
High = 80
Critical = 100
alert_info.priority = 60
Need more help?
Get answers from Community members and Google SecOps professionals.
