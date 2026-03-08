# Develop the connector

**Source:** https://docs.cloud.google.com/chronicle/docs/soar/respond/start-developing/developing-the-connector/  
**Scraped:** 2026-03-05T10:08:51.248914Z

---

Home
Documentation
Security
Google Security Operations
Guides
Stay organized with collections
Save and categorize content based on your preferences.
Develop the connector
Supported in:
Google secops
SOAR
This document explains how to build a new connector in the Integrated Development Environment (IDE) by
creating an integration and then linking a connector to it.
Create an email connector integration
To create an email connector integration, follow these steps:
In the
Response
>
IDE
window, click
add
Add
to add a new IDE item.
Select
Integration
and name the integration
Email Connector
.
Click
Create
. The integration appears in the sidebar with a default icon.
Click
more_vert
Configure Custom Integration
and define these settings:
Description
Icon
Python Dependencies
Integration Parameters
Click
Save
.
Create an email connector
To create an email connector, follow these steps:
In the
Response
>
IDE
window, click
add
Add
to add a new IDE item.
Select the
Connector
radio button and name the connector
My Email Connector
.
In the list, select the integration
Email Connector
to associate the connector with the integration.
Click
Create
.
Set the connector parameters
After you create the connector, set the connector parameters:
Set the connector parameters according to the table:
Parameter
Description
Type
Username
Required
. IMAP username. The email address from which the connector pulls the emails into the Google SecOps platform. The default value is
email@gmail.com
.
string
Password
Required
. Internet Message Access Protocol (IMAP) password for the email address the connector uses to pull emails into the Google SecOps platform.
password
IMAP Port
Required
. The specific network port used by the IMAP to access emails from a remote server. For example:
993
(default value).
int
IMAP Server Address
Required
. The incoming mail server for an IMAP account. For example,
imap.gmail.com
(default value).
string
Folder to check for emails
Optional
. Pulls emails only from the specified folder. For example:
Inbox
(default value).
inbox
Enter the following field details:
Product Field Name = device_product
: Determines the raw field value to assign to the alert's product name. Find the related field in the code, which was defined as
Mail
(product).
event["device_product"] = PRODUCT #The PRODUCT constant is `"Mail"
Event Field Name = event_name
: Determines the raw field value to assign to the event type field. Find the related field in the code, defined as
Suspicious email
.
event["event_name"] = Suspicious email
Edit the email connector
To edit the parameters for the email connector, follow these steps:
Copy the following code created for
My Email Connector
, paste it in the IDE, and follow the instructions:
from SiemplifyConnectors import SiemplifyConnectorExecution
from SiemplifyConnectorsDataModel import AlertInfo
from SiemplifyUtils import output_handler, convert_datetime_to_unix_time, convert_string_to_datetime
import email, imaplib, sys, re

# CONSTANTS
CONNECTOR_NAME = "Mail"
VENDOR = "Mail"
PRODUCT = "Mail"
DEFAULT_PRIORITY = 60 # Default is Medium
RULE_GENERATOR_EXAMPLE = "Mail"
DEFAULT_FOLDER_TO_CHECK_INBOX = "inbox"
DEFAULT_MESSAGES_TO_READ_UNSEEN = "UNSEEN"
URLS_REGEX = r"(?i)\b(?:http(?:s)?:\/\/)?(?:www\.)?[a-zA-Z0-9:%_\+~#=][a-zA-Z0-9:%\._\+~#=]{1,255}\.[a-z]{2,6}\b(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)"

def create_alert(siemplify, alert_id, email_message_data, datetime_in_unix_time, created_event):
    """Returns an alert which is one event that contains one unread email message"""
    siemplify.LOGGER.info(f"Started processing Alert {alert_id}")

    create_event = None
    alert_info = AlertInfo()
    # Initializes alert_info
    alert_info.display_id = f"{alert_id}" # Each alert needs to have a unique id, otherwise it won't create a case with the same alert id.
    alert_info.ticket_id = f"{alert_id}" # In default, ticket_id = display_id. However, if for some reason the external alert id is different from the display_id, you can save the original external alert id in the "ticket_id" field. 
    alert_info.name = email_message_data['Subject']
    alert_info.rule_generator = RULE_GENERATOR_EXAMPLE # The name of the siem rule which causes the creation of the alert. 
    alert_info.start_time = datetime_in_unix_time # Time should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime 
    alert_info.end_time = datetime_in_unix_time # Time should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime
    alert_info.priority = 60 # Informative = -1,Low = 40,Medium = 60,High = 80,Critical = 100.
    alert_info.device_vendor = VENDOR # The field will be fetched from the Original Alert. If you build this alert manually, state the source vendor of the data. (ie: Microsoft, Mcafee) 
    alert_info.device_product = PRODUCT # The field will be fetched from the Original Alert. If you build this alert manually, state the source product of the data. (ie: ActiveDirectory, AntiVirus)

    siemplify.LOGGER.info(f"Events creating started for alert {alert_id}")
    try:
        if created_event is not None:
            alert_info.events.append(created_event)
            siemplify.LOGGER.info(f"Added Event {alert_id} to Alert {alert_id}")
    # Raise an exception if failed to process the event
    except Exception as e:
        siemplify.LOGGER.error(f"Failed to process event {alert_id}")
        siemplify.LOGGER.exception(e)
    return alert_info

def create_event(siemplify, alert_id, email_message_data, all_found_url_in_emails_body_list, datetime_in_unix_time):
    """Returns the digested data of a single unread email"""
    siemplify.LOGGER.info(f"--- Started processing Event: alert_id: {alert_id} | event_id: {alert_id}") 
    event = {} 
    event["StartTime"] = datetime_in_unix_time # Time should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime 
    event["EndTime"] = datetime_in_unix_time # Time should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime 
    event["event_name"] = "Suspicious email" 
    event["device_product"] = PRODUCT # ie: "device_product" is the field name that describes the product the event originated from. 
    event["Subject"] = email_message_data["Subject"] 
    event["SourceUserName"] = email_message_data["From"] 
    event["DestinationUserName"] = email_message_data["To"] 
    event["found_url"] = ",".join(all_found_url_in_emails_body_list) 
    siemplify.LOGGER.info(f"---Finished processing Event: alert_id: {alert_id} | event_id: {alert_id}")
    return event

def find_url_in_email_message_body(siemplify, email_messages_data_list):
    """Search for a url in the email body"""
    all_found_url_in_emails_body_list = []
    for message in email_messages_data_list:
        for part in message.walk():
            if part.get_content_maintype() == 'text\plain':
                continue
            email_message_body = part.get_payload()
            all_found_urls = re.findall(URLS_REGEX, str(email_message_body))
            for url in all_found_urls:
                if url not in all_found_url_in_emails_body_list:
                    all_found_url_in_emails_body_list.append(url)

def get_email_messages_data(imap_host, imap_port, username, password, folder_to_check):
    """Returns all unread email messages"""
    email_messages_data_list = []

    # Login to email using 'imap' module
    mail = imaplib.IMAP4_SSL(imap_host, imap_port)
    mail.login(username, password)

    # Determining the default email folder to pull emails from - 'inbox'
    if folder_to_check is None:
        folder_to_check = DEFAULT_FOLDER_TO_CHECK_INBOX

    # Selecting the email folder to pull the data from
    mail.select(folder_to_check)

    # Storing the email message data
    result, data = mail.search(None, DEFAULT_MESSAGES_TO_READ_UNSEEN)

    # If there are several emails collected in the cycle it will split each
    # email message into a separate item in the list chosen_mailbox_items_list
    if len(data) > 0:
        chosen_mailbox_items_list = data[0].split()
        # Iterating each email message and appending to emails_messages_data_list
        for item in chosen_mailbox_items_list:
            typ, email_data = mail.fetch(item, '(RFC 822)')
            # Decoding from binary string to string
            raw_email = email_data[0][1].decode("utf-8")
            # Turning the email data into an email object
            email_message = email.message_from_string(raw_email)
            # Appending the email message data to email_messages_data_list
            email_messages_data_list.append(email_message)
    return email_messages_data_list

@output_handler
def main(is_test_run):
    alerts = [] # The main output of each connector run that contains the alerts data 
    siemplify = SiemplifyConnectorExecution() # Siemplify main SDK wrapper
    siemplify.script_name = CONNECTOR_NAME

    # In case of running a test
    if (is_test_run):
        siemplify.LOGGER.info("This is an \"IDE Play Button\"\\\"Run Connector once\" test run")

    # Extracting the connector's Params
    username = siemplify.extract_connector_param(param_name="Username") 
    password = siemplify.extract_connector_param(param_name="Password") 
    imap_host = siemplify.extract_connector_param(param_name="IMAP Server Address")
    imap_port = siemplify.extract_connector_param(param_name="IMAP Port")
    folder_to_check = siemplify.extract_connector_param(param_name="Folder to check for emails")

    # Getting the digested email message data
    email_messages_data_list = get_email_messages_data(imap_host, imap_port, username, password, folder_to_check)
    # If the email_messages_data_list is not empty
    if len(email_messages_data_list) > 0:
        for message in email_messages_data_list:
            # Converting the email message datetime from string to unix time by SiemplifyUtils functions
            datetime_email_message = message['Date']
            string_to_datetime = convert_string_to_datetime(datetime_email_message)
            datetime_in_unix_time = convert_datetime_to_unix_time(string_to_datetime)
            found_urls_in_email_body = find_url_in_email_message_body(siemplify, email_messages_data_list)
            # Getting the unique id of each email message and removing the suffix '@mail.gmail.com' from the Message-ID, Each alert id can be ingested to the system only once.
            alert_id = message['Message-ID'].replace('@mail.gmail.com','') 
            # Creating the event by calling create_event() function 
            created_event = create_event(siemplify, alert_id, message, found_urls_in_email_body, datetime_in_unix_time) 
            # Creating the alert by calling create_alert() function 
            created_alert = create_alert(siemplify, alert_id, message, datetime_in_unix_time, created_event)
            # Checking that the created_alert is not None 
            if created_alert is not None: 
                alerts.append(created_alert) 
                siemplify.LOGGER.info(f'Added Alert {alert_id} to package results')
    # If the inbox for the user has no unread emails. 
    else: 
        siemplify.LOGGER.info(f'The inbox for user {username} has no unread emails') 
    # Returning all the created alerts to the cases module in Siemplify 
    siemplify.return_package(alerts) 

if __name__ == '__main__':
# Connectors run in iterations. The interval is configurable from the ConnectorsScreen UI. 
    is_test_run = not (len(sys.argv) < 2 or sys.argv[1] == 'True') 
    main(is_test_run)
After copying the connector's code, review the necessary modules to be imported and then proceed to the main function. Each method called from the main function will be discussed later in more detail.
Relevant imports
A Python module has a set of functions, classes, or variables defined and implemented.
To implement all the following functions, import those modules into the script:
from SiemplifyConnectors import SiemplifyConnectorExecution # This module is responsible for executing the connector 
from SiemplifyConnectorsDataModel import AlertInfo # The data model that contains the alert info class
from SiemplifyUtils import output_handler, convert_datetime_to_unix_time, convert_string_to_datetime # The functions that convert time 
import email, imaplib, sys, re
Main function
The
Main
function is the script's entry point. The Python interpreter runs the code sequentially and calls each method defined in the script.
Extract the connector parameters. Use the
siemplify.extract_connector_param
function to extract each configured parameter for the connector (
username
,
password
,
imap_host
,
imap_port
,
folder_to_check
).
# Extracting the connector's Params
    username = siemplify.extract_connector_param(param_name="Username") 
    password = siemplify.extract_connector_param(param_name="Password") 
    imap_host = siemplify.extract_connector_param(param_name="IMAP Server Address") 
    imap_port = siemplify.extract_connector_param(param_name="IMAP Port") 
    folder_to_check = siemplify.extract_connector_param(param_name="Folder to check for emails")
Use the function
get_email_messages_data (`imap_host`, `imap_port`, `username`, `password`, `folder_to_check)
to collect all 
information from the unread emails.
# Getting the digested email message data 
    email_messages_data_list = get_email_messages_data(imap_host, imap_port, username, password, folder_to_check)
After you receive all information from the email, confirm that the information is collected, and then perform these
actions on each email:
# If the email_messages_data_list is not empty 
if len(email_messages_data_list) > 0:
   for message in email_messages_data_list:
       # Converting the email message datetime from string to unix time by SiemplifyUtils functions
This code extracts the message date by
datetime_email_message =
message['Date']
and then converts this date time to Unix epoch time using
Google SecOps functions:
string_to_datetime = convert_string_to_datetime(datetime_email_message) 
datetime_in_unix_time = convert_datetime_to_unix_time(string_to_datetime)
Search for URLs in the email message body using the
find_url_in_email_message_body(siemplify_email_messages_data_list)
function. If a URL is found, use other products in our playbook to check if it is malicious.
found_urls_in_email_body = find_url_in_email_message_body(siemplify, email_messages_data_list)
Extract the unique ID of each email message, and assign it to the
alert_id
variable:
# Getting the unique id of each email message and removing the suffix '@mail.gmail.com' from the Message-ID, Each alert id can be ingested to the system only once. 
alert_id = message['Message-ID'].replace('@mail.gmail.com','')
After you extract all the necessary details to ingest the alert
into the Google SecOps platform, create the alert and the event:
# Creating the event by calling create_event() function 
created_event = create_event(siemplify, alert_id, message, found_urls_in_email_body, datetime_in_unix_time) 
# Creating the alert by calling create_alert() function 
created_alert = create_alert(siemplify, alert_id, message, datetime_in_unix_time, created_event)
Validate the created alert and the created event. After
validating, add the alert to the alert list.
# Checking that the created_alert is not None 
    if created_alert is not None: 
        alerts.append(created_alert)     
        siemplify.LOGGER.info(f"Added Alert {alert_id} to package results")
In a scenario where the inbox for the given user has no unread emails, add the following code:
else:
    siemplify.LOGGER.info(f"The inbox for user {username} has no unread emails")
Return the alerts list to the system and each alert is then presented as a case in the case queue:
# Returning all the created alerts to the cases module in Siemplify 
    siemplify.return_package(alerts)
Run the
Main
function within the times you set in the connector configuration:
if __name__ == "__main__": 
    # Connectors run in iterations. The interval is configurable from the Connectors UI. 
    is_test_run = not (len(sys.argv) < 2 or sys.argv[1] == 'True')
    main(is_test_run)
Get the unread email message
The
Get the unread email message
function connects to the email with
the
Imap
and
Email
modules, and retrieves the email message details. It also returns a list
containing all the information of all the unread email messages.
From the main class, use the function:
get_email_messages_data(imap_host, imap_port, username, password,
folder_to_check)
.
def get_email_messages_data(imap_host, imap_port, username, password, folder_to_check):
    """Returns all unread email messages"""
    email_messages_data_list = []
Connect to the email by using the
imap module
:
# Login to email using 'imap' module
    mail = imaplib.IMAP4_SSL(imap_host, imap_port)
    mail.login(username, password)
Determine the folder in the email to check for unread messages.
In this example, you extract emails from the
Inbox
folder
(DEFAULT_FOLDER_TO_CHECK_INBOX = "inbox")
:
# Determining the default email folder to pull emails from - 'inbox'
if folder_to_check is None:
    folder_to_check = DEFAULT_FOLDER_TO_CHECK_INBOX
# Selecting the email folder to pull the data from mail.select(folder_to_check)
Collect all unread messages
DEFAULT_MESSAGES_TO_READ_UNSEEN = "UNSEEN"
, and then convert this data to a list:
# Storing the email message data
result, data = mail.search(None, DEFAULT_MESSAGES_TO_READ_UNSEEN)
# If there are several emails collected in the cycle it will split each
# email message into a separate item in the list chosen_mailbox_items_list
if len(data) > 0:
    chosen_mailbox_items_list = data[0].split()
    # Iterating each email message and appending to emails_messages_data_list
    for item in chosen_mailbox_items_list:
        typ, email_data = mail.fetch(item, '(RFC 822)')
        # Decoding from binary string to string
        raw_email = email_data[0][1].decode("utf-8")
        # Turning the email data into an email object
        email_message = email.message_from_string(raw_email)
        # Appending the email message data to email_messages_data_list
        email_messages_data_list.append(email_message)
return email_messages_data_list
Create the event
The
Create the event
function creates the event by associating each email message component
to the event fields, respectively.
From the main class create the event by using the
function:
create_event(siemplify, alert_id, email_message_data,
                      all_found_url_in_emails_body_list,
                      datetime_in_unix_time)
def create_event(siemplify, alert_id, email_message_data, all_found_url_in_emails_body_list, datetime_in_unix_time):
    """Returns the digested data of a single unread email"""
    siemplify.LOGGER.info(f"--- Started processing Event: alert_id: {alert_id} | event_id: {alert_id}")
Create a dictionary for the event fields. The mandatory fields are
event["StartTime"], event["EndTime"], event["event_name"] and event["device_product"]
:
event = {} 
event["StartTime"] = datetime_in_unix_time # Time should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime 
event["EndTime"] = datetime_in_unix_time # Time should be saved in UnixTime. You may use SiemplifyUtils.convert_datetime_to_unix_time, or SiemplifyUtils.convert_string_to_datetime 
event["event_name"] = "Suspicious email" 
event["device_product"] = PRODUCT # ie: "device_product" is the field name that describes the product the event originated from. 
event["Subject"] = email_message_data["Subject"] 
event["SourceUserName"] = email_message_data["From"] 
event["DestinationUserName"] = email_message_data["To"] 
event["found_url"] = ",".join(all_found_url_in_emails_body_list) 
siemplify.LOGGER.info(f"---Finished processing Event: alert_id: {alert_id} | event_id: {alert_id}")
return event
Each alert contains one or more
events. In this example, an alert contains a single event: one email message. Therefore, after creating the event,
create the alert that contains all the event information.
Create the alert info and initialize the alert information characteristics
fields
This function creates the alert. Each alert
contains one or more events within it. In this case, each alert contains one event
which is basically one email message.
From the main class, create
the alert:
def create_alert(siemplify, alert_id, email_message_data,datetime_in_unix_time, created_event): 
    """Returns an alert which is one event that contains one unread email message"""
    siemplify.LOGGER.info(f"-------------- Started processing Alert {alert_id}")
    create_event = None
Create the
alert_info
instance and initialize it:
# Initializes the alert_info Characteristics Fields 
alert_info.display_id = f"{alert_id}" 
alert_info.ticket_id = f"{alert_id}" 
alert_info.name = email_message_data['Subject'] 
alert_info.rule_generator = RULE_GENERATOR_EXAMPLE 
alert_info.start_time = datetime_in_unix_time 
alert_info.end_time = datetime_in_unix_time 
alert_info.device_vendor = VENDOR 
alert_info.device_product = PRODUCT
After you create the alert, validate the event and
append it to the
aert_info
characteristics:
siemplify.LOGGER.info(f"Events creating started for alert {alert_id}")
try:
    if created_event is not None:
        alert_info.events.append(created_event)
    siemplify.LOGGER.info(f"Added Event {alert_id} to Alert {alert_id}")
# Raise an exception if failed to process the event
except Exception as e:
    siemplify.LOGGER.error(f"Failed to process event {alert_id}")
    siemplify.LOGGER.exception(e)
return alert_info
Find the URL in the email body function
The
find the URL in the email body
function scans the email body for URLs.
To use this function, follow these steps:
For each email message, locate the part of the message body with plain text content:
def find_url_in_email_message_body(siemplify, email_messages_data_list):
    """
    Search for a url in the email body,
    """
    all_found_url_in_emails_body_list = []
    for message in email_messages_data_list:
        for part in message.walk():
            if part.get_content_maintype() == 'text\plain':
                continue
If the body contains the required content, 
load this information with
email_message_body =
part.get_payload()
, and search for URLs using the regular expression:
URLS_REGEX=r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
This example extracts URLs from the email body:
email_message_body = part.get_payload()
all_found_urls = re.findall(URLS_REGEX, str(email_message_body))
for url in all_found_urls:
    if url not in all_found_url_in_emails_body_list:
        all_found_url_in_emails_body_list.append(url)
siemplify.LOGGER.info(f"The URL found : {all_found_url_in_emails_body_list}") 
return all_found_url_in_emails_body_list
After reviewing
the connector code, you can configure a connector to
ingest cases into the platform from a selected Gmail inbox.
Need more help?
Get answers from Community members and Google SecOps professionals.
